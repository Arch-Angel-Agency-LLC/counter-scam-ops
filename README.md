# Counter-Scam Social Engineering Operation Guide

Version: 1.0  
Scope: Internal ally reference (do not forward externally)  

## Core Objectives
- Obtain high-confidence attribution pivots (wallets, IP sessions, toolchain fingerprints, temporal patterns) using ordinary business pretexts.
- Preserve evidentiary integrity (hashing, chain-of-custody logging).
- Avoid wording that signals trace or surveillance intent.

## Guiding Stealth Principles
A. One clear business reason per artifact.  
B. Metadata leakage arises naturally (countersignature, revision cycle).  
C. Pace requests (24–48h) tied to believable internal reviews (Legal → Finance → Ops).  
D. Require native editor features Canva cannot replicate (dynamic TOC, cross-references, formulas).  
E. Reuse the same working file; discourage re-authoring.  
F. Neutral, commonplace phrasing; never use stop‑words (see list).  

## High-Level Phased Flow
1. Rapport & Baseline Timing
2. Draft Agreement v1 (unsigned) → they sign & return (v1 signed)
3. Micro-correction & countersign (v2) → request initials on fix
4. Request PDF export for “investor pack” (capture their export tool)
5. Staged portal “archive” upload (multi-session IP)
6. Wallet address (primary chain) under test transfer pretext
7. Secondary chain address comparison later
8. Short screen recording (Document send) for internal demo
9. Optional voice note confirmation
10. Consolidate evidence & prepare LE brief

## Artifact Set
- /docs/agreement_template_v1.docx (dynamic fields, remote logo)
- /docs/micro_correction_note.txt (instructions for v2)
- /scripts/hash_log.py (SHA256 + CSV append)
- /scripts/docx_meta_extract.py (core/app properties)
- /portal/ (future: simple logging endpoint)

## Draft Agreement v1 Composition
Required structural elements:
- Title page with dynamic field (e.g., date field).  
- Cross-referenced section numbers (auto-generated TOC).  
- Signature block with placeholder for their full name + date.  
- Footer embedding single remote logo URL: `https://cdn.company-docs.com/branding/<campaignToken>.png`  
- Hidden unique marker: subtle zero-width space every 3rd sentence boundary.  
- Mild deliberate inconsistency: one date in ISO (2025-08-24) vs another in long form (24 August 2025).  

## Sign-Then-Return Flow (Detailed)
1. Send v1 (.docx) with message: “Please just add your name in the signature block, save, and send back. We’ll countersign afterward.”
2. On receipt, hash file, extract metadata, log.
3. Produce v2: add your countersignature, fix deliberate inconsistency, add a small ‘Initial here’ annotation near the corrected date.
4. Send v2: “Finance flagged a date format; please just initial the small correction on page 3 and re-send, then export a PDF copy for the investor pack.”
5. On receipt of updated DOCX and their PDF, log both; compare Producer/Creator changes.

## Canva Laundering Counter-Levers
| Adversary Attempt | Risk | Counter-Lever |
|-------------------|------|---------------|
| Flatten via Canva | Loss of metadata | Require cross-references & TOC (broken in flat PDF) |
| Re-author blank doc | Strips hidden markers | Insist same filename for ‘automation’ diff |
| Consistent VPN | Masks IP geo | Multi-day portal visits + off-hour prompts |
| Exchange-only wallet | Obscures custody | Request self-custody address for network timing test |

## Wording: Safe vs Risky
Avoid: verification, traceability, metadata, tracking, identify, forensic, IP log, geolocation, capture.  
Use: editable, countersign, investor pack, formatting, accessibility, finance totals, archive, working file.  

Safe snippet examples:
- “Please sign then return; we’ll add our signature and send the final PDF for your records.”
- “The internal links broke in the PDF—can you forward the working file so layout doesn’t shift?”
- “Finance flagged the totals; just initial the small date fix and re-send.”

## Stealth Data Capture Patterns
A. Single remote asset (benign CDN).  
B. Unique zero-width markers (variant watermark).  
C. Micro correction requiring re-save.  
D. Delayed portal ‘archive’ upload (collect IP over time).  
E. Wallet request sequencing (primary → secondary chain).  
F. Screen recording request (as Document) to retain encoder metadata.  

## Behavioral Time Mapping
- Log all message timestamps UTC.  
- Identify longest daily inactivity gap (probable sleep window).  
- Cross-align with portal access times.  

## Evidence Logging Workflow
1. On every received file: compute SHA256, record UTC time, original filename, claimed context.  
2. Extract DOCX/PDF properties; capture creator, lastModifiedBy, application, creation & mod times.  
3. Append wallet addresses with chain, first seen time, any transaction hash (once test transfer executed).  
4. Maintain IP session table once portal active (IP, ASN, country, timestamp).  

## Escalation Criteria for LE Brief
Proceed when you have at least:
- Two or more distinct artifacts with consistent author/toolchain fingerprints.  
- At least one recurring IP OR wallet cluster with exchange interaction.  
- Documented timeline of inducements (messages + artifacts).  
- Integrity: all hashes logged at acquisition.  

## LE Brief Contents (Outline)
- Executive summary (objective, scope)
- Timeline table (UTC)
- Artifact inventory (hashes, types)
- Metadata correlation matrix
- Wallet cluster analysis (addresses, flows, exchange tags)
- IP enrichment (ASN, geolocation confidence, stability)
- Behavioral pattern (timezone inference)
- Appendices (raw property dumps)

## Risk Mitigation
- Limit to one new artifact request per 24h.  
- Provide business-grounded rationale each time.  
- Avoid technical jargon that implies monitoring.  
- Keep external asset count minimal (1).  
- Stagger wallet chain requests.  

## Quick Suspicion Litmus Test
Ask internally before sending a request:
- Would a legitimate counterpart expect this step?  
- Is wording plain and non-technical?  
- Does it align with prior narrative thread?  
- Are we bundling multiple novel asks (if yes, split)?  

## Operational Stop-Words
`metadata, tracking, traceability, forensic, identify, IP log, geolocation, instrument, capture` (exclude entirely from outward communications).

## Minimal Portal Concept (Future)
- Auth: single token link (no sign-up friction).  
- Logging: timestamp, IP, User-Agent, path, ref token.  
- Page purpose text: “Archive confirmation – file received. Future updates will appear here.”  

## Success Indicators
- Returned DOCX retains original file name.  
- Author / lastModifiedBy stable across versions.  
- Second chain wallet provided on delayed prompt.  
- Multiple portal hits from either identical or one anomalous (non-VPN) IP.  
- Screen recording with encoder string present.  

## Failure Indicators & Responses
| Indicator | Response |
|-----------|----------|
| Only flat PDFs returned | Reiterate need for cross-reference integrity, request working file |
| Refuses portal | Offer email alternative (keep WhatsApp narrative) then re-introduce later |
| Provides exchange-only wallet | Ask for self-custody address citing on-chain settlement timing test |
| Rapid suspicion (stops responding) | Freeze outreach; preserve evidence; no escalation attempts |

## Immediate Action Checklist
- [ ] Generate campaign token & remote logo URL
- [ ] Prepare agreement_v1.docx (dynamic TOC, date inconsistency)
- [ ] Set up hash logging script
- [ ] Prepare micro_correction_note
- [ ] Draft portal splash (defer deployment until after v2)

---
End of Guide.
