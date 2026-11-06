# Contract Review Agent: Vendor Service Agreements (CUAD)

INF 385T project by Jenny and Kayla.

We built a bounded agent that reviews a contract against a rubric, flags problems with evidence quoted from the contract, and produces a prioritized revision plan. The intended user is a **small business with no in-house lawyer** that has been sent a vendor's service or maintenance contract and wants to know what to push back on before signing.

**Layout.** Notebooks `01`–`07` (code) are in `notebooks/`; they run from the repo root. `data/` holds the contracts, rubric, CUAD spans and label sheets. `results/dev` and `results/test` hold the executed runs and score zips. `demo_agent/` is the `adk web` demo.

## Run the demo

The demo runs the agent from notebook 07 inside `adk web`. It shows the input, every tool call the verifier makes, and the final findings with quotes, the revision plan and the human-review list. The agent reviews only the clause family you ask about.

You need Python 3.10 or later. Run everything from the repository root.

**1. Clone the repository**

```bash
git clone https://github.com/JJJJeny/contract-review-agent.git
cd contract-review-agent
```

**2. Install the dependencies**

```bash
pip install google-adk litellm rank_bm25 openai pandas python-multipart
```

**3. Set the API key.** The agent uses GPT-5 nano through the course Portkey gateway. Enter the key without echoing it, so it does not end up in your shell history:

```bash
read -s OPENAI_API_KEY && export OPENAI_API_KEY
```

No key? Use the scripted fake model instead. It needs no key or network, but its answers are canned and not real reviews:

```bash
export DEMO_FAKE=1
```

**4. Start the web UI**

```bash
adk web .
```

If `adk` is not on your PATH, or port 8000 is taken, use the module form with a free port:

```bash
python3 -m google.adk.cli web --port 8765 .
```

**5. Ask for a review.** Open http://127.0.0.1:8000 (or the port you chose), select `demo_agent` in the top left, and type a request, for example:

```text
I'm a small business owner reviewing C13. Is the liability and indemnity section okay for me?
```

A short form also works: `C05 termination`. Type a contract ID from C01 to C15, optionally with a clause family (`payment`, `termination`, `liability_indemnity`, `confidentiality`, `renewal`, `dispute_governing_law`).

**What you will see.** The pre-pass gives a first verdict. If a trigger fires (low confidence, a missing verdict, a failed quote check), the verifier calls `search_contract`, `check_cross_reference` and other tools, and finishes with `finalize`. The final answer has the verdict and severity, the quote with its section, how the verdict was decided, a ranked revision plan, and the human-review list. A run takes a few minutes.

**Known issues**

- `Form data requires "python-multipart"`: run `pip install python-multipart`.
- `address already in use`: choose another port with `--port`.
- `'ascii' codec can't encode characters`: the key contains a stray character. Re-enter it with `read -s`.
- The model is not deterministic, so the same question can give a different answer on a second run (the C13 demo is an example).

## Scope: vendor service agreements

A **vendor service agreement** is a contract in which a provider performs ongoing services (maintenance, support, IT, professional services) for a business customer that pays for them. Maintenance agreements are one kind of service agreement.

Out of scope: transportation, marketing or promotion partnerships, licenses without services, financing "capital maintenance" agreements, employment contracts, and agreements between affiliated companies.

## Repository contents

| File | What it is |
|---|---|
| `data/rubric_v1.md` | The review standard: for each of the six clause families, what counts as acceptable, risky, missing or unclear, and how severe it is |
| `data/contracts/C01.txt` … `C15.txt` | Full text of the 15 contracts, taken from `CUAD_v1.json` |
| `data/contracts_pdf/C01.pdf` … `C15.pdf` | Original CUAD PDFs of the same 15 contracts, renamed to match the IDs |
| `data/contracts_pdf/all_15_contracts.pdf` | All 15 PDFs merged into one file (120 pages), with a bookmark for each contract |
| `data/labels_gold.xlsx` | Gold labels for all 90 rows after both of us reviewed our sheets and confirmed the 8 rows we disagreed on (`Jenny's Labels.xlsx` and `Kayla's Labels.xlsx` are the two reviewed sheets) |
| `data/cuad_gold_spans.csv` | CUAD lawyer highlights for the families CUAD covers, used by Track A |
| `data/contracts.csv` | Contract list: ID, short name, dev/test split, customer and provider names, CUAD folder, word count, original CUAD title |
| `notebooks/01_data_setup_v3.ipynb` | Colab notebook that rebuilds everything from CUAD: contract texts, CUAD answer key, coverage tables and the two labeling spreadsheets |
| `notebooks/07_agent_v2_and_scoring.ipynb` | The agent (pre-pass, bounded per-clause loop, revision planner) and all graders. Version 2, used for the test run |
| `notebooks/06_baseline_and_scoring.ipynb` | The RAG baseline and its scoring |
| `notebooks/02`–`05` | Earlier versions of the agent, baseline and scoring, kept for reference |
| `demo_agent/` | The `adk web` demo (reads notebook 07) |
| `results/` | Executed runs and score zips for dev and test |

`CUAD_v1.json` (40 MB) is not included. Download CUAD v1 from [atticusprojectai.org/cuad](https://www.atticusprojectai.org/cuad) and upload `CUAD_v1.json` when the notebook asks for it.

## The 15 contracts

All 15 come from CUAD's *Maintenance* or *Service* folders: 9 maintenance and 6 services agreements.

Selection: we started from the 68 CUAD contracts titled maintenance or service agreements and removed fund and insurance paperwork, amendments, fragments under 1,000 words, contracts over 8,000 words, and agreements that are not a provider serving a customer. Several of the remaining contracts contain cross-references ("see Section 9"), which the agent must follow.

C15 was originally a transportation agreement (out of scope). It was replaced by the On2 / Wildform support and maintenance agreement (8,844 words), so the word cap is 9,000 for that one contract.

| Split | Contracts | Use |
|---|---|---|
| dev | C01, C02, C11, C12 | Tune the prompt and the rubric thresholds |
| test | the other 11 | Final scoring only. Never used for tuning. |

The dev set was drawn with `random.seed(42)`.

## The six clause families

The rubric checks every contract for six kinds of clause, judged from the small-business customer's side:

| Family | Example question |
|---|---|
| `payment` | How long to pay? Late fees? Can the vendor raise prices at will? |
| `termination` | Can the customer leave, and at what cost? |
| `liability_indemnity` | Who pays when something goes wrong, and is the cap fair? |
| `confidentiality` | Is the customer's data protected? |
| `renewal` | Does it renew automatically, and how much notice is needed to stop it? |
| `dispute_governing_law` | Which law applies, and where do disputes go? |

Each contract gets one row per family with a **verdict** (acceptable / risky / missing / unclear), a **severity** (high / medium / low / n/a), and quoted **evidence** with a section reference. Numbers marked **(P)** in the rubric are provisional until the dev contracts have been read by hand.

## How we evaluate the agent

- **Track A, clause detection:** does the agent find the right clause? Where a CUAD category matches one of our families, CUAD's lawyer-reviewed highlights serve as the answer key.
- **Track B, risk verdicts:** is the agent's verdict right? CUAD has nothing for this, so both annotators label every contract independently, then compare and agree on a final answer.

### Why the CUAD mapping exists

CUAD labels 41 clause types that matter in mergers and acquisitions. Only some of them match what a small business customer cares about. The mapping in section 4 of the notebook records which CUAD categories we can reuse and which parts of the rubric CUAD does not cover:

| Family | CUAD coverage | CUAD categories used |
|---|---|---|
| renewal | covered | Renewal Term, Notice Period To Terminate Renewal |
| termination | partial | Termination For Convenience (no termination for cause or cure period) |
| liability_indemnity | partial | Cap On Liability, Uncapped Liability (no indemnification) |
| dispute_governing_law | partial | Governing Law (no venue or arbitration) |
| payment | none | — |
| confidentiality | none | — |

Related categories such as Insurance or Minimum Commitment appear as hints in the labeling sheet only and are never scored. All category names were checked against the real `CUAD_v1.json`.

## Workflow

1. `notebooks/01_data_setup_v3.ipynb` in Colab rebuilds the data from `CUAD_v1.json`.
2. We read the four dev contracts by hand, set the rubric thresholds (rubric v1.1) and labeled all 15 contracts.
3. Both label sheets were reviewed by both of us and merged into `data/labels_gold.xlsx`.
4. Design choices (including version 1 against version 2 of the agent) were made on the four dev contracts only.
5. The 11 test contracts were run once at the end, for the agent and the baseline.

## Results at a glance

On the 11 held-out test contracts (66 rows, six clause families each), all three systems use the same model, prompt, retrieval and graders; the loop is the only difference.

| | RAG baseline | Single pass | Agent loop |
|---|---|---|---|
| Verdict accuracy | 0.50 | 0.59 | 0.70 |
| False alarm rate | 0.76 | 0.24 | 0.41 |
| Missed risk rate | 0.00 | 0.05 | 0.05 |
| Cost for 11 contracts | $0.132 | $0.076 | $0.227 |

The loop gets the most verdicts right (p = 0.004 against the baseline) for about two cents a contract, but it raises false alarms, and the model never asked a human for help. See `results/README.md` for the run files.

## Reproduce the scored runs

- **Agent:** open `notebooks/07_agent_v2_and_scoring.ipynb` in Colab, add the Colab secrets `OPENAI_API_KEY` and `GH_TOKEN`, set `SPLIT` to `"dev"` or `"test"`, and choose Runtime → Run all. It runs three contracts at a time with a checkpoint per contract, scores every grader and downloads one zip.
- **Baseline:** `notebooks/06_baseline_and_scoring.ipynb`, the same way.
- **Without a key:** executed copies of every run and its score tables are in `results/dev` and `results/test`.
- If a `scores/llm_judge_plan.csv` from an earlier run exists and the judge step fails with a `TypeError`, delete that file and re-run the scoring cell.

## Data source and license

Contract texts and CUAD annotations come from the **Contract Understanding Atticus Dataset (CUAD) v1** by The Atticus Project, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Hendrycks, D., Burns, C., Chen, A., & Ball, S. (2021). *CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review.* arXiv:2103.06268.

This project is coursework. Nothing here is legal advice.
