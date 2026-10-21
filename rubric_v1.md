# Rubric v1 — Vendor Service Contract Review (maintenance & services)

**Project:** INF 385T contract-review agent (CUAD, 15 vendor service agreements C01–C15)
**Scope (contract type):** *vendor service agreements*: a provider performs ongoing services (maintenance, support, IT, outsourcing, professional services) for a business customer that pays for them. Maintenance agreements are a subset. Out of scope: transportation/carriage, marketing/promotion partnerships, licenses without services, financing/"capital maintenance" agreements, employment, and agreements between affiliates. The six families below apply to every contract in scope.
**Contract set:** 8 maintenance (C01, C03, C04, C07, C08, C09, C10, C14), 6 services (C02, C05, C06, C11, C12, C13), 1 outsourcing services (C15, CCA Industries / Emerson HealthCare; replaced the Dynamex transportation agreement). List with word counts: `contracts.csv`.
**Status:** DRAFT v1. Every number marked **(P)** is *provisional*. Confirm or change it after hand-reading the four dev contracts (C01, C02, C11, C12), then bump to v1.1. Never tune thresholds on the 11 test contracts.

---

## 0. How to use this rubric

### 0.1 Perspective
Judge every clause **from the customer's side, where the customer is a small business** buying maintenance or services. It has no in-house lawyer, little bargaining power, and a budget where a surprise bill of a few months' fees hurts.

Before labeling a contract, write down in `notes` (first row of that contract):
- **Customer:** who receives the services
- **Provider:** who performs them
- **Fees, if stated:** annual or monthly value (needed for the liability cap test)

Some CUAD filers are the *provider*. Still judge from the customer's side.

### 0.2 One row = one family
Each contract gets exactly one verdict per family (6 rows). If a family has several clauses (e.g. termination for convenience *and* for cause), judge each sub-criterion, then the row verdict is the **worst** sub-result (risky > unclear > missing > acceptable), with one exception: see 0.4.

### 0.3 Verdicts

| Verdict | Use when |
|---|---|
| **acceptable** | The clause exists and meets every "acceptable" criterion for that family, or it is absent *and* its absence helps the customer (e.g. no auto-renewal). |
| **risky** | The clause exists and at least one criterion falls in the "risky" column. |
| **missing** | A clause the customer needs is absent after a full search (see 0.5). |
| **unclear** | The clause exists but you can't decide: it contradicts another section, depends on an exhibit/schedule that is not in the text, is redacted (`[***]`), or can be read two reasonable ways. |

### 0.4 Severity

| Severity | Meaning (customer perspective) | Typical triggers |
|---|---|---|
| **high** | Could cost more than the contract is worth, or traps the customer. | Uncapped or one-sided customer liability; no way to exit; customer indemnifies provider for everything; automatic multi-year renewal with long notice. |
| **medium** | Clearly unfavorable, but the damage is bounded. | Short payment window; long cure period; inconvenient venue; low provider cap; confidentiality survives only 1 year. |
| **low** | Drafting gap or mild imbalance; worth a comment, not a fight. | Missing governing law; vague notice method; slightly above-market late fee. |
| **n/a** | Verdict is acceptable. | — |

Rules:
- `acceptable` → always `n/a`.
- `risky` / `missing` → use the family table below; if none fits, use the triggers above.
- `unclear` → give the severity of the **worse reasonable reading**, but at most **medium**, unless both readings are high.
- When several sub-criteria are risky, the row takes the **highest** severity.

### 0.5 Evidence requirements (what goes in the sheet)

| Verdict | `evidence_text` | `section_ref` | `evidence_2` |
|---|---|---|---|
| acceptable / risky | Exact, copy-pasted contract text, at least the full sentence that triggers the verdict. Do not paraphrase. | Section number as printed (e.g. `§9.2`), or "untitled para, p.X" | Any second location the verdict depends on: a definition ("Fees" defined in §1), a cross-reference ("subject to Section 12"), an exhibit. |
| unclear | Quote the passage that causes the doubt. | yes | Quote the conflicting passage, or write `EXHIBIT NOT INCLUDED` / `REDACTED`. |
| missing | Leave blank, or write `NONE FOUND`. | — | — |

For **missing**, `notes` must record the search: keywords tried (use the keyword lists below) and sections/TOC headings checked. A "missing" without a search record will be treated as "not checked" during adjudication.

If the clause is in a cross-referenced section, the agent (and you) must **follow the reference** and quote both places. This is what the demo is designed to test.

---

## 1. payment

**Keywords:** payment, invoice, fee, net, due, late, interest, past due, price, increase, expenses, taxes, withhold, suspend.
**CUAD:** no category. CUAD spans **cannot** be the answer key; our evidence spans are.

| Sub-criterion | Acceptable | Risky |
|---|---|---|
| Payment window | Net **30** days or longer (P) from receipt of a correct invoice | Shorter than Net **15** (P), payment in advance for a period longer than **one year** (P), or "due on receipt". Net 15–29 = risky **low**. |
| Late charges | No late fee, or ≤ **1.5% per month** (P), simple interest | > 1.5% per month, compounding, or fixed penalty plus interest |
| Disputed invoices | Customer may withhold a disputed amount in good faith | No dispute process **and** provider may suspend service for any late payment |
| Suspension for non-payment | Only after written notice and ≥ **10 days** (P) to cure | Immediate suspension, or suspension without notice |
| Price changes | Fixed for the term, or increases capped (≤ **5%/yr** or CPI) (P) with ≥ **30 days** notice (P) | Provider may raise fees at will, or with no cap |
| Expenses | Pre-approved or capped | Customer reimburses any provider expenses without approval |

**Missing:** no fees or payment terms anywhere, and no exhibit is referenced → `missing`, **medium**. If an exhibit holds the fees but isn't in the text → `unclear`, **low**.

**Severity:** suspension without notice, or uncapped unilateral price increases → **high**. Short window, high late fee, non-refundable prepayment → **medium**. Unapproved expenses, Net 15–29 → **low**.

---

## 2. termination

**Keywords:** terminat, for convenience, for cause, breach, cure, insolvency, bankruptcy, effect of termination, refund, transition, wind down.
**CUAD:** `Termination For Convenience` (primary). `Post-Termination Services` and `Change Of Control` as hints only. Termination **for cause** and **cure periods** are not CUAD categories.

| Sub-criterion | Acceptable | Risky |
|---|---|---|
| Customer exit for convenience | Customer may terminate without cause on ≤ **90 days** notice (P) | No customer right while provider has one (**high**), or notice > 90 days (**medium**) |
| Termination for cause | Either party may terminate for material breach | Only the provider may terminate for cause (**high**) |
| Cure period | **15–30 days** (P) after written notice | No cure for the customer, or cure for the provider > **60 days** (P) (**medium**) |
| Exit cost | Pay only for services delivered up to the end date; pro-rata refund of prepaid fees | Early termination fee, acceleration of all remaining fees, or no refund of prepaid fees (**high** if acceleration, else **medium**) |
| Transition | Provider returns customer data / assists transition (Post-Termination Services) | No data return at all (**medium**), when the provider holds customer data |

**Missing:** the contract has no termination clause and the term is indefinite → `missing`, **high** (no exit). Fixed term with no early termination at all → `risky`, **medium** if term ≤ 1 year (P), **high** if longer.

---

## 3. liability_indemnity

**Keywords:** liabilit, in no event, aggregate, consequential, indirect, cap, exceed, indemnif, hold harmless, defend, insurance, gross negligence, wilful.
**CUAD:** `Cap On Liability` and `Uncapped Liability` (primary). `Liquidated Damages`, `Insurance`, `Warranty Duration`, `Covenant Not To Sue` as hints. **Indemnification and consequential-damages exclusions have no CUAD category.**

| Sub-criterion | Acceptable | Risky |
|---|---|---|
| Provider's cap | Provider's liability capped at no less than **12 months of fees** (P) | Cap below fees paid in the last **3 months** (P), or a fixed amount well below annual fees (**medium**); provider liability excluded entirely (**high**) |
| Mutuality | Cap and consequential-damages exclusion apply to **both** parties | Provider capped, customer uncapped (**high**) |
| Carve-outs | Cap does not apply to provider's breach of confidentiality, data breach, IP indemnity, gross negligence or wilful misconduct | Cap covers provider's gross negligence/wilful misconduct (**medium**) |
| Indemnity by provider | Provider indemnifies customer for third-party IP infringement and for injury/property damage caused by provider | No provider indemnity (**medium**) |
| Indemnity by customer | Limited to customer's own breach / misuse | Customer indemnifies provider broadly, "any and all claims arising from this Agreement" (**high**) |
| Liquidated damages | None, or reasonable and mutual | Customer-only penalties (**medium**) |

**Missing:** no limitation of liability and no indemnity anywhere → `missing`, **medium** (law fills the gap, which is not always bad for the customer). If only one of the two is absent, judge the row on what is present and note the gap in `notes`.

---

## 4. confidentiality

**Keywords:** confidential, proprietary, non-disclosure, disclose, trade secret, customer data, personal data, security, return or destroy, survive.
**CUAD:** no category. Our spans are the answer key.

| Sub-criterion | Acceptable | Risky |
|---|---|---|
| Direction | **Mutual**, or at least protects the customer's information | Protects only the provider's information (**high** if provider handles customer data, else **medium**) |
| Scope | Covers customer data / business information the provider sees | Narrow definition (only items marked "confidential") (**low**) |
| Standard exclusions | Public, already known, independently developed, legally required | Missing exclusions that bind the customer unfairly (**low**) |
| Duration | Survives ≥ **2 years** (P) after termination; trade secrets as long as they remain secret | < 2 years (**medium**), or ends at termination (**medium**) |
| Return/destroy | Return or destroy on termination | Not addressed (**low**) |
| Data security | Provider commits to reasonable security / breach notice | Not addressed when provider stores customer data (**medium**) |

**Missing:** no confidentiality clause at all → `missing`; **high** if the provider accesses customer systems or data (most maintenance contracts), **medium** otherwise.

---

## 5. renewal

**Keywords:** term, renew, automatic, successive, extend, non-renewal, expire, initial term.
**CUAD:** `Renewal Term` and `Notice Period To Terminate Renewal` (primary). `Expiration Date` as hint.

| Sub-criterion | Acceptable | Risky |
|---|---|---|
| Auto-renewal | No auto-renewal; or auto-renews for ≤ **1 year** (P) at a time | Auto-renews for > 1 year (**high** if ≥ 3 years, else **medium**) |
| Non-renewal notice | Customer can stop renewal with ≤ **60 days** notice (P) | > **90 days** (P) (**medium**); 61–90 days (**low**) |
| Renewal pricing | Same price, or increase capped (see payment) | Renewal at provider's "then-current rates" with no cap (**medium**) |
| Who controls renewal | Either party may decline renewal | Only provider may decline (**high**) |

**Absence rule:** a fixed term with **no** renewal language is **acceptable** (the contract just ends; note "no auto-renewal"). If the contract states **no term or end date at all**, use `unclear`, **low**, and check the termination row, because exit then depends entirely on termination rights.

---

## 6. dispute_governing_law

**Keywords:** governed by, laws of, jurisdiction, venue, court, arbitration, AAA, JAMS, ICC, jury, attorney, fees, dispute, mediation, injunctive.
**CUAD:** `Governing Law` (primary). **Venue, arbitration, jury waiver and fee-shifting have no CUAD category.**

| Sub-criterion | Acceptable | Risky |
|---|---|---|
| Governing law | A named U.S. state (or the customer's own country) | Foreign law unfamiliar to a U.S. small business (**medium**) |
| Venue / forum | Customer's home state, or neutral, or not exclusive | Exclusive venue far from the customer (provider's state or abroad) (**medium**) |
| Arbitration | None, or mutual with shared costs | Mandatory arbitration with customer paying fees, or abroad (**medium**) |
| Waivers | — | Jury waiver or class-action waiver binding only the customer (**low**) |
| Attorney fees | Each party pays its own, or prevailing party (mutual) | Customer pays provider's fees regardless of outcome (**medium**) |
| Escalation | Informal negotiation/mediation step before litigation | — (absence is fine) |

**Missing:** no governing-law clause → `missing`, **low**.

---

## 7. From findings to the revision plan

Each `risky`, `missing` or `unclear` row becomes one finding. Order the revision plan by:

1. **Severity**: high → medium → low
2. **Verdict** within the same severity: risky → missing → unclear (unclear often just needs a question to the provider)
3. **Family tie-break (P):** liability_indemnity → termination → payment → renewal → confidentiality → dispute_governing_law

Each plan item must state: the finding (family, verdict, severity), the quoted evidence with section ref, the ask in one plain sentence (e.g. "Ask for a mutual cap equal to 12 months of fees"), and a fallback if the provider says no.

---

## 8. Hand-reading worksheet (fill in from the dev contracts, then fix the (P) numbers)

Read C01, C02, C11, C12. Write down **every number you see**. If most real contracts sit on the "risky" side of a threshold, the threshold is probably too strict for this contract type; discuss and adjust before labeling the test set.

| Item | C01 | C02 | C11 | C12 | Keep / change threshold? |
|---|---|---|---|---|---|
| Customer / Provider | | | | | |
| Annual fees | | | | | |
| Payment window (Net X) | | | | | 30 / 15 |
| Late fee | | | | | 1.5%/mo |
| Price increase cap | | | | | 5%/yr |
| Customer convenience-termination notice | | | | | 90 days |
| Cure period | | | | | 15–30 / 60 days |
| Liability cap (amount or formula) | | | | | 12 months / 3 months fees |
| Customer liability capped too? | | | | | — |
| Indemnity direction | | | | | — |
| Confidentiality survival | | | | | 2 years |
| Initial term / renewal term | | | | | 1 year |
| Non-renewal notice | | | | | 60 / 90 days |
| Governing law / venue / arbitration | | | | | — |

## 9. Change log
- v1, 2026-10-21 (rev. b): scope renamed to *vendor service agreements* and defined in the header. C15 changed from the Dynamex transportation agreement (out of scope) to the CCA Industries services outsourcing agreement. Dev set unchanged. CUAD category names in every **CUAD:** line checked against the real `CUAD_v1.json` (all 41 names; every name used here exists). No threshold changed.
- v1 (2026-10-21): first draft from the family list in `01_data_setup.ipynb`. Thresholds provisional, not yet checked against dev contracts.
