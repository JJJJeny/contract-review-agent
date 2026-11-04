# Rubric v1.1 — Vendor Service Contract Review (maintenance & services)

**Project:** INF 385T contract-review agent (CUAD, 15 vendor service agreements C01–C15)
**Scope (contract type):** *vendor service agreements*: a provider performs ongoing services (maintenance, support, IT, outsourcing, professional services) for a business customer that pays for them. Maintenance agreements are a subset. Out of scope: transportation/carriage, marketing/promotion partnerships, licenses without services, financing/"capital maintenance" agreements, employment, and agreements between affiliates. The six families below apply to every contract in scope.
**Contract set:** all 15 come from CUAD's *Maintenance* or *Service* folders: 9 maintenance (C01, C03, C04, C07, C08, C09, C10, C14, C15) and 6 services (C02, C05, C06, C11, C12, C13). C15 (On2 / Wildform software support and maintenance) replaced the Dynamex transportation agreement. List with word counts: `contracts.csv`.
**Status:** v1.1. Thresholds checked against the four dev contracts (C01, C02, C11, C12); see §8. Numbers still marked **(P)** did not occur in any dev contract and stay provisional. Never tune thresholds on the 11 test contracts.

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
| Pricing model | Fixed fee, or time-and-materials / cost-plus with a budget cap or estimate | Cost-plus or time-and-materials with no cap or estimate (**low**) |

**Missing:** no fees or payment terms anywhere, and no exhibit is referenced → `missing`, **medium**. If an exhibit holds the fees but isn't in the text → `unclear`, **low**.

**Customer is not the payer** (e.g. revenue share where the provider pays the customer): judge only the sub-criteria that still apply (taxes, expenses). If none is risky → `acceptable`, and write "customer is not the payer" in `notes`.

**Severity:** suspension without notice, or uncapped unilateral price increases → **high**. Short window, high late fee, non-refundable prepayment → **medium**. Unapproved expenses, Net 15–29 → **low**.

---

## 2. termination

**Keywords:** terminat, for convenience, for cause, breach, cure, insolvency, bankruptcy, effect of termination, refund, transition, wind down.
**CUAD:** `Termination For Convenience` (primary). `Post-Termination Services` and `Change Of Control` as hints only. Termination **for cause** and **cure periods** are not CUAD categories.

| Sub-criterion | Acceptable | Risky |
|---|---|---|
| Customer exit for convenience | Customer may terminate without cause on ≤ **90 days** notice (90 itself is acceptable) | No customer right while provider has one (**high**), or notice > 90 days (**medium**) |
| Termination for cause | Either party may terminate for material breach | Only the provider may terminate for cause (**high**) |
| Cure period | **15–30 days** (P) after written notice | No cure for the customer, or cure for the provider > **60 days** (P) (**medium**) |
| Exit cost | Pay only for services delivered up to the end date; pro-rata refund of prepaid fees | Early termination fee, acceleration of all remaining fees, or no refund of prepaid fees (**high** if acceleration, else **medium**) |
| Transition | Provider returns customer data / assists transition (Post-Termination Services) | No data return at all (**medium**), when the provider holds customer data |

**Missing:** the contract has no termination clause and the term is indefinite → `missing`, **high** (no exit). Fixed term with no early termination at all → `risky`, **low** if term ≤ 1 year, **high** if longer. The same applies to a locked initial term of ≤ 1 year followed by a convenience exit.

---

## 3. liability_indemnity

**Keywords:** liabilit, in no event, aggregate, consequential, indirect, cap, exceed, indemnif, hold harmless, defend, insurance, gross negligence, wilful.
**CUAD:** `Cap On Liability` and `Uncapped Liability` (primary). `Liquidated Damages`, `Insurance`, `Warranty Duration`, `Covenant Not To Sue` as hints. **Indemnification and consequential-damages exclusions have no CUAD category.**

| Sub-criterion | Acceptable | Risky |
|---|---|---|
| Provider's cap | Provider's liability capped at no less than **12 months of fees** | Cap below fees paid in the last **3 months** (P), or a fixed amount well below annual fees (**medium**); provider liability excluded entirely (**high**) |
| Mutuality | Cap and consequential-damages exclusion apply to **both** parties | Provider capped, customer uncapped (**high**) |
| No cap at all | Neither party's liability is capped: the provider sub-criterion is acceptable (customer can recover in full). Note "no cap either side" and judge the row on the other sub-criteria. | — |
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
| Court vs arbitration | One forum | Exclusive courts **and** mandatory arbitration in the same contract → `unclear`, **low** (quote both clauses) |
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

## 8. Hand-reading worksheet (dev contracts)

Filled 2026-10-22 from C01, C02, C11, C12 (section numbers in parentheses). Numbers only, no verdicts. Annotators: check the cells against the text before labeling.

| Item | C01 Garman (maintenance) | C02 Kubient (services) | C11 Mobimagic (services) | C12 Telcostar (services) | Current threshold |
|---|---|---|---|---|---|
| Customer / Provider | Sparkling Spring Water (CA) / Garman Routing Systems | The Associated Press / Kubient | PC Financial Services (India) / Mobimagic (China) | Telcostar + Ability Computer (SG/IL) / name redacted | — |
| Annual fees | Not in text: "Fee Schedule" (Sched. A) not attached (§11) | No fee: revenue share set out in an Exhibit not attached; Kubient pays customer within 7 days of receipt (§5) | USD 970,000 per month = USD 11.64M/yr (§6.1) | Cost + 10% plus out-of-pocket costs (§2.2(a)); Exhibit A redacted | — |
| Payment window (Net X) | Not stated (in Fee Schedule) | Not applicable: customer receives money | **Net 45** after customer confirms the invoice (§6.1) | **Net 15** from receipt of invoice (§2.2(b)(ii)) | 30 / 15 |
| Late fee | None | None | None | None | 1.5%/mo |
| Price increase cap | None stated | n/a (revenue share) | Fee changes only by mutual written agreement (§6.4) | Cost-plus: price moves with provider's actual costs, no cap (§2.2(a)) | 5%/yr |
| Disputed invoices | Not addressed | n/a | Complaint within 20 business days, then negotiate / independent auditor (§6.5) | Written dispute before due date; undisputed part paid; provider keeps performing (§2.3) | — |
| Expenses | Not addressed | Customer pays sales/use taxes (§5) | Each party bears own costs (§4.2) | Customer reimburses "reasonable and documented" out-of-pocket costs, **no pre-approval** (§2.2(a)) | pre-approved or capped |
| Customer convenience-termination notice | **90 days**, any time (§17(b)) | **90 days**, but **only after the 1-year initial term**; no exit in year 1 (§4(a)) | **None**: fixed term Apr 2019 – Mar 2020 (§9.1) | **90 days**, any time; provider has the same right (§3.2) | 90 days |
| Cure period | **30 days**, mutual (§17(c)(7)) | **30 days**, mutual (§4(b)) | **30 days**, mutual (§9.2) | **30 days**, mutual (§3.3) | 15–30 / 60 days |
| Liability cap (amount or formula) | **No cap.** Direct damages only; consequential excluded both ways; exclusion does not apply to IP indemnity (§13) or confidentiality (§14) (§15) | **No cap.** Consequential excluded both ways, except indemnity and confidentiality (§7) | **Cap = total fees owed** (≈ 12 months), mutual (§10.2). §8.3 carves confidentiality out of the consequential exclusion; §10.2 has no carve-out (conflict) | **No cap and no consequential exclusion** | 12 months / 3 months fees |
| Customer liability capped too? | No cap either side | No cap either side | Yes, same cap | No cap either side | — |
| Indemnity direction | Provider → customer, IP only (§13) | Mutual: provider broad (services, platform, breach); customer for its content and misuse (§10) | Mutual: provider broad (services, breach, law); customer only for its own breach (§8) | Provider → customer only, for negligence, misconduct or breach, incl. first-party claims (§5.1) | — |
| Confidentiality survival | Indefinite (survives, §18); mutual | **1 year from disclosure** (§12); mutual | **5 years** after expiry (§7); mutual | Perpetual ("during the term and thereafter", §4.1); return/destroy + erase (§3.6, §4.2) | 2 years |
| Initial term / renewal term | Licence perpetual while fees paid (§17(a)); maintenance "renewable one-year term" with no renewal mechanism (§10) | 1 year, **auto-renews for 1-year terms** (§4(a)) | ~1 year fixed; renewal only by mutual written agreement (§9.1) | Fixed, ends Dec 31, 2020; no renewal (§3.1) | 1 year |
| Non-renewal notice | Not stated | No separate notice; after year 1 either party may end on 90 days (§4(a)) | n/a | n/a | 60 / 90 days |
| Governing law / venue / arbitration | Nova Scotia law; **non-exclusive** Nova Scotia courts (§20(h)) | Delaware law; **exclusive** NY courts **and** AAA arbitration (conflict); mutual jury waiver; 1-year limit on claims; prevailing-party fees (§8, §14(a), §14(d)) | Indian law; **exclusive** New Delhi courts **and** New Delhi arbitration (conflict) (§10.3) | Israeli law; **exclusive** Tel Aviv courts; customer may also seek injunctions abroad (§7.2–7.3) | — |

### 8.1 Threshold review

| Threshold | Dev evidence | Decision (v1.1) |
|---|---|---|
| Payment window: Net 30 ok, < 15 risky, 15–29 risky low | Net 45 (C11), Net 15 (C12); the other two don't state one | **Keep.** It separates the two contracts that state a window. |
| Late fee ≤ 1.5%/mo | No dev contract has one | **Keep**, untested. |
| Price increase ≤ 5%/yr | No contract has a stated increase. C12 is cost-plus | **Keep**, but add a rule for cost-plus pricing (applied in v1.1). |
| Convenience exit ≤ 90 days | 90, 90 (after year 1), none, 90 | **Keep 90**, and state that 90 counts as acceptable (three contracts sit exactly on it). |
| Fixed term, no early exit → risky **medium** if ≤ 1 year | C02 (year 1) and C11 would both be risky medium | **Lower to risky low** for a fixed term of ≤ 1 year (applied in v1.1). |
| Cure 15–30 days | All four: 30 days, mutual | **Keep.** |
| Provider cap ≥ 12 months of fees | Only C11 has a cap (≈ 12 months). Three have **no cap at all** | **Keep 12 months**, but the rubric has no rule for "no cap for either party" (applied in v1.1). |
| Confidentiality survives ≥ 2 years | Indefinite, 1 year, 5 years, perpetual | **Keep.** It flags C02, which is the weak one. |
| Auto-renewal ≤ 1 year | Only C02 auto-renews, for 1 year | **Keep.** |
| Non-renewal notice ≤ 60 ok, 61–90 risky low, > 90 medium | C02's exit after year 1 is 90 days | **Keep.** |

### 8.2 Notes for the report

- **The customers are not small businesses.** AP, a fintech paying USD 970,000 a month, and two listed companies. CUAD only contains public-company filings. The rubric still judges from the small-business side, which is fine, but say so.
- **Home law is usually foreign to the U.S.** Three dev contracts use non-U.S. law (Canada, India, Israel), but in each case it is the **customer's own** country. The rubric already treats that as acceptable.
- **Fees often live in schedules that were not filed** (C01, C02, C12). Expect many `unclear` verdicts on payment, and on the liability cap test that needs annual fees.

## 9. Change log
- v1.1 (2026-10-22): §8 filled from the four dev contracts. Thresholds kept: payment window, convenience-exit notice (90 days now explicitly acceptable), cure period, 12-month cap, confidentiality survival, auto-renewal, non-renewal notice. Rules added: no cap for either party (liability), short fixed term → risky **low** (was medium), cost-plus pricing without cap (payment), customer is not the payer (payment), court + arbitration conflict → unclear (dispute). Late fee, price-increase cap and suspension notice did not occur in dev contracts and stay (P).
- v1, 2026-10-21 (rev. b): scope renamed to *vendor service agreements* and defined in the header. C15 changed from the Dynamex transportation agreement (out of scope) to the On2 / Wildform support and maintenance agreement, so all 15 come from CUAD's Maintenance or Service folders (C15 is 8,844 words; word cap raised to 9,000 for it). Dev set unchanged. CUAD category names in every **CUAD:** line checked against the real `CUAD_v1.json` (all 41 names; every name used here exists). No threshold changed.
- v1 (2026-10-21): first draft from the family list in `01_data_setup.ipynb`. Thresholds provisional, not yet checked against dev contracts.
