# Operational Quick Start Walkthrough

Purpose: Enable a first-time operator to set up, run, and log the counter-scam engagement using the provided toolkit. Keep communications natural; follow the phased flow in `README.md` and consult `adaptive_branching_playbook.md` when deviations occur.

---
## 1. Repository Layout (What Each File Is For)
- `README.md` – Core strategy & phased plan.
- `quick_start_walkthrough.md` – This step-by-step procedural guide.
- `adaptive_branching_playbook.md` – Decision trees & contingencies.
- `message_timeline_examples.md` – Sample chronological phrasing.
- `wording_reference.md` – Approved wording & terms to avoid.
- `evidence_log_template.csv` – Seed CSV for artifact logging.
- `scripts_doc_processing.py` – Hash & basic metadata extraction (DOCX/PDF).

---
## 2. Initial Environment Setup
1. Ensure Python 3.10+ available (`python --version`).
2. (Optional) Create a virtual environment:
   - macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
3. Install dependencies if needed later (e.g., `pypdf`) when handling PDFs.
4. Copy all guide files into a working directory isolated from personal data.
5. Make sure `scripts_doc_processing.py` is executable: `chmod +x scripts_doc_processing.py`.

---
## 3. Before First Contact
1. Generate a campaign token (short random string): e.g., `export CAMPAIGN_TOKEN=$(openssl rand -hex 4)`.
2. Prepare remote logo asset (optional): Host a benign PNG at `https://cdn.company-docs.com/branding/<CAMPAIGN_TOKEN>.png`.
3. Prepare Draft Agreement v1 (use internal template) ensuring:
   - Dynamic date field (or placeholder to fill later).
   - Cross-referenced sections / TOC.
   - Single deliberate minor inconsistency (date format mismatch).
   - Footer logo reference (the hosted PNG URL).
   - Signature block placeholder.
4. Save as: `Agreement_v1.docx` (do not rename later).
5. Create a working copy of the evidence log: `cp evidence_log_template.csv evidence_log.csv`.
6. Set a secure UTC clock reference (all logs in UTC).

---
## 4. Engagement Phase Overview (At a Glance)
| Phase | Objective | Artifact / Action |
|-------|-----------|------------------|
| 0 | Baseline rapport | Normal chat; no asks yet |
| 1 | Editable doc footprint | Send `Agreement_v1.docx` for signature |
| 2 | Second save + metadata delta | Micro correction + countersign (v2) |
| 3 | Export pipeline fingerprint | Request their PDF export |
| 4 | Multi-session IP | Introduce portal/remote reference (passive) |
| 5 | Wallet cluster | Request primary then secondary chain addresses |
| 6 | Media encoder | Request screen recording as Document |
| 7 | Consolidation | Hash & correlate; prepare summary |

---
## 5. Sending Draft Agreement v1
Message template (choose one):
- "Attached is the draft agreement (v1). Please add your name in the signature block and return the working file. We'll countersign afterward."
Log immediately the time you send it (UTC). Do not send additional artifacts until response.

---
## 6. Logging a Returned File
When you receive a DOCX or PDF:
1. Save file without altering name.
2. Run: `./scripts_doc_processing.py path/to/file.docx` (inside project root).
3. Confirm JSON output; verify a row appended to `evidence_log.csv`.
4. Add manual notes if needed (open `evidence_log.csv` and append in `notes` column—avoid commas unless quoted).
5. Snapshot hash (SHA256) separately if desired: `shasum -a 256 file.docx` (should match script output).

---
## 7. Micro Correction & v2 Cycle
1. Open their returned v1.
2. Fix the deliberate inconsistency (e.g., unify date format).
3. Add your countersignature placeholder mark.
4. Insert small “Initial here” text box near fix.
5. Save as `Agreement_v2.docx` (do NOT change original name root). Send message:
   - "Attached v2 with our signature. Please initial the small date alignment on page 3 and resend the working file, then export a PDF copy for the investor pack."
6. Log returned v2 DOCX & PDF as before.

---
## 8. Wallet Acquisition Sequence
After at least one successful DOCX round-trip:
1. Primary request: "Could you share the address you prefer for a tiny network timing test?"
2. Log the address (create `wallet_log.csv` if not already) with fields: `utc_timestamp,address,chain,context,notes`.
3. Later (≥48h): Secondary request: "Ops wants to compare fees—could you also provide the TRC20 (or alternate chain) address you use?"
4. Cluster addresses with simple checks (same prefix patterns, exchange tags, etc.).

---
## 9. Screen Recording Request
Precondition: At least one wallet obtained + DOCX cycle done.
Message: "A short screen recording (30–60s) of the process will let me avoid paraphrasing internally—please send it as a document so the resolution stays intact."
When received, compute hashes: `shasum -a 256 recording.mp4`. Log manually in evidence log (type = video).

---
## 10. Portal / Remote Asset Access (Optional Early, Preferred Mid)
1. Only after establishing routine compliance.
2. Provide a single link (tokenized) with neutral copy: "Archive confirmation—future updates will appear here." 
3. Each access: log timestamp, IP, User-Agent (from server logs) in a separate `session_log.csv`: `utc_timestamp,ip,ua,path,token`.
4. Aim for ≥2 distinct sessions on different days before escalation.

---
## 11. Timezone Inference Basics
1. Record every inbound message UTC time.
2. Determine largest continuous inactivity block (≥5–7h) → probable sleep window midpoint.
3. Cross-reference with portal access times (if any) for consistency.
4. Document inference in notes (e.g., "Likely UTC+8 ±1h").

---
## 12. Branching on Deviations
Use `adaptive_branching_playbook.md` triggers. Minimal mnemonic (FLAT, BLANK, EXCH, SILENCE, ONEPORTAL):
- FLAT = Only PDFs → Request working file; fallback XLSX.
- BLANK = Generic metadata → Force second save.
- EXCH = Exchange wallet only → Ask for self-custody timing test.
- SILENCE = >48h → Soft nudge then wallet ask.
- ONEPORTAL = Single visit → Gentle update prompt.

Log each branch event in a new `branch_events.csv`: `utc_timestamp,trigger,action,outcome,pivot_gained`.

---
## 13. Evidence Consolidation Checklist
Perform after obtaining at least two pivots (e.g., DOCX + wallet):
- [ ] Hash inventory complete (files & media).
- [ ] Metadata comparison table (v1 vs v2 vs PDF). 
- [ ] Wallet addresses annotated with chain & cluster notes.
- [ ] Session/IP log (≥2 entries if portal used).
- [ ] Timezone inference note.
- [ ] Branch events log current.

---
## 14. Minimal Metrics (Internal Quality)
| Metric | Target |
|--------|--------|
| Avg response pacing between new artifact asks | ≥24h |
| Distinct metadata-bearing document versions | ≥2 |
| Self-custody wallet addresses | ≥1 (goal 2) |
| Portal sessions (if used) | ≥2 different days |
| Video/recording captured | ≥1 |

---
## 15. Common Mistakes & Corrections
| Mistake | Impact | Correction |
|---------|--------|-----------|
| Asking for too many items in one message | Suspicion | Split into sequential asks |
| Immediate portal push | Resistance | Delay until after v2 cycle |
| Re-sending new filenames yourself | Breaks continuity | Keep root name constant |
| Forgetting to log hash immediately | Chain-of-custody gap | Recompute ASAP & note delay |

---
## 16. Quick Reference Commands
(Adjust pathing as needed.)
- Hash & metadata: `./scripts_doc_processing.py Agreement_v2.docx`
- Direct SHA256 (sanity): `shasum -a 256 Agreement_v2.docx`
- Append wallet entry (manual): open `wallet_log.csv` in editor & add row.

---
## 17. When to Pause
Pause further inducements if:
- Actor questions rationale twice in a row.
- No new pivot after 3 branch attempts.
- Abrupt hostility or deflection pattern emerges.

Resume after ≥48h cooldown with a low-friction clarification or acknowledgement.

---
## 18. Preparing Summary Packet
Create a folder `summary_packet_<date>` containing:
- `evidence_log.csv`
- `wallet_log.csv`
- `session_log.csv` (if exists)
- `branch_events.csv`
- Exported comparison table (e.g., `metadata_comparison.md`)
- Hash listing `hashes.txt` (each file name + SHA256)

---
## 19. Final Review Priorities
1. Integrity: Are all files still hash-matching original logged hashes? (Re-run sample checks.)
2. Completeness: Any pivot type missing? (Editable doc, IP/session, wallet, media.)
3. Consistency: Do timestamps overlap plausibly for proposed timezone inference?
4. Redaction: Remove internal-only tokens from outward summary.

---
## 20. Operator Quick Checklist (Print / Pin)
- [ ] Campaign token created
- [ ] v1 sent & logged
- [ ] v1 returned hashed & logged
- [ ] v2 cycle completed (DOCX + PDF)
- [ ] Wallet primary captured
- [ ] Wallet secondary (if possible)
- [ ] Screen recording (if possible)
- [ ] Portal sessions (if deployed)
- [ ] Branch events recorded
- [ ] Summary packet assembled

---
End of Quick Start Walkthrough.
