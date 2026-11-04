# Contract Review Agent: Vendor Service Agreements (CUAD)

INF 385T project by Jenny and Kayla.

We are building an agent that reviews a contract against a rubric, flags problems with evidence quoted from the contract, and produces a prioritized revision plan. The intended user is a **small business with no in-house lawyer** that has been sent a vendor's service or maintenance contract and wants to know what to push back on before signing.

**Layout.** Notebooks `01`–`07` (code) stay at the repo root so Colab and `adk web` paths work. `data/` holds the contracts, rubric, CUAD spans and label sheets. `results/dev` and `results/test` hold the executed runs and score zips. `demo_agent/` is the `adk web` demo.

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
| `data/Jenny_Labels_claude.xlsx` | Draft Track B labels for all 90 rows (verdict, severity, notes, evidence), written by Claude under rubric v1.1; to be reviewed by a human annotator |
| `data/contracts.csv` | Contract list: ID, short name, dev/test split, CUAD folder, word count, original CUAD title |
| `01_data_setup_v3.ipynb` | Colab notebook that rebuilds everything from CUAD: contract texts, CUAD answer key, coverage tables and the two labeling spreadsheets |

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

1. Open `01_data_setup_v3.ipynb` in Colab, upload `CUAD_v1.json`, and run all cells. This produces `labels_jenny.xlsx` and `labels_kayla.xlsx`.
2. Read the four dev contracts, fill in the worksheet in section 8 of the rubric, and adjust the (P) thresholds together. Save as rubric v1.1.
3. Each annotator labels all 15 contracts alone (90 rows each).
4. Compare the two sheets, settle disagreements, and record agreement.
5. Build the agent and score it on the 11 test contracts.

## Data source and license

Contract texts and CUAD annotations come from the **Contract Understanding Atticus Dataset (CUAD) v1** by The Atticus Project, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Hendrycks, D., Burns, C., Chen, A., & Ball, S. (2021). *CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review.* arXiv:2103.06268.

This project is coursework. Nothing here is legal advice.
