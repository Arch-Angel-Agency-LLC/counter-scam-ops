# Adaptive Branching & Contingency Playbook

Purpose: Rapid decision reference when actor behavior deviates from baseline path. Focus: maximizing attribution pivots (wallets, IP, toolchain) while maintaining engagement.

Symbols:  
- Trigger: Observable event/deviation.  
- Path: Immediate response sequence.  
- Goal: Attribution pivot sought.  
- Risk Flag: Rising suspicion indicator.  
- Escalate: Move to new tactic.  

## 0. Core Attribution Priorities (In Order)
1. Editable artifact (DOCX) with creator metadata.
2. Multi-session IP (portal / remote asset). 
3. Wallet cluster (>=2 chains self-custody). 
4. Media encoder fingerprint (screen recording). 
5. Behavioral timezone (circadian gap + session pattern). 

If blocked on a higher priority for >3 cycles, shift to the next without stalling entire operation.

---
## 1. File Return Scenarios

### 1A. Trigger: Only Flat PDF Returned (No DOCX)
Path:
- Reply: "Internal links are dead in the PDF—could you forward the working file so layout doesn't shift?" (Attempt 1)
- If refusal or second flat PDF: Embed business rationale upgrade:
  - "Finance needs to view the cross-references live—PDF won't surface them. Just resend the same file name you worked from."
- If still blocked:
  - Introduce alternate doc type: send slim XLSX (requires a single editable cell) and request they confirm a number.
Goal: Force native editor use once.
Risk Flag: Actor invents reason like "system can't open docx".
Escalate: Move to wallet acquisition earlier (Section 4) while preserving doc request in background (spaced 3+ days).

### 1B. Trigger: Returned DOCX But Metadata Blank/Generic
Path:
- Accept quietly; embed micro correction and reissue (v2) to elicit another save.
- Introduce tracked change requirement via functional excuse: "Please show the edit inline so Finance sees the delta."
Goal: Capture changed lastModifiedBy / revision.
Risk Flag: Actor re-flattens after first metadata query.
Escalate: Transition to screen recording ask (Section 5) sooner.

### 1C. Trigger: Actor Re-names File Every Time Eliminating Original Name
Path:
- Soft requirement: "Automation matches the original filename—please keep it unchanged so our diff tool doesn't choke." 
- If ignored twice: add unique token inside body referencing filename to tie versions manually.
Goal: Maintain chain continuity.
Risk Flag: Frequent random naming suggests deliberate obfuscation.
Escalate: Prioritize IP portal visits for continuity over filename reliance.

---
## 2. Timing & Responsiveness

### 2A. Trigger: Long Silence (>48h) Early Stage
Path:
- Send light nudge tied to internal process: "Legal is waiting on that signed working file when you have a moment—no rush if you're mid-review." 
- If no response after 72h: pivot to wallet request to re-engage.
Goal: Reopen channel without stacking demands.
Risk Flag: Sudden reappearance with push to accelerate funds step.
Escalate: Skip to wallet capture + portal before further doc complexity.

### 2B. Trigger: Hyper-Fast Compliance (Sends Back Immediately)
Path:
- Slow them intentionally: "Appreciate speed—Finance cycles updates in ~6h; I'll forward after their glance."
- Insert planned delay to avoid pattern recognition from rapid-fire requests.
Goal: Control pacing; map natural active window (observe if they idle afterward).
Risk Flag: They push for next step prematurely.
Escalate: Keep next ask mild (micro correction) not portal.

### 2C. Trigger: Responses Clustered in Narrow Daily Window
Path:
- Send one off-cycle message (2h outside observed window) asking a trivial clarification.
- Log latency delta. Repeat once on another day.
Goal: Tighten timezone inference.
Risk Flag: Immediate response at all hours (could be shift team / multiple operators).
Escalate: Begin stylometric differentiation across messages; search for writing variance.

---
## 3. Suspicion Indicators

### 3A. Trigger: Actor Asks Why Editable Needed
Path:
- Provide single benign reason (accessibility links). Do NOT stack reasons.
- Next request delayed 24h.
Goal: Defuse suspicion, maintain path.
Risk Flag: Repeated questioning of rationale.
Escalate: Suspend doc escalation; move to wallet-first path.

### 3B. Trigger: Actor Rejects Portal Link
Path:
- Offer alternative: "Archive link optional—email summary works too." 
- Wait 48h; reintroduce portal only when they request status themselves.
Goal: Avoid hard refusal memory imprint.
Risk Flag: Direct statement about 'tracking'.
Escalate: Cease portal pursuit; rely on document & wallet pivots.

### 3C. Trigger: Actor Minimizes Steps (“Too many docs”)
Path:
- Consolidate next two planned steps into one artifact (micro correction + PDF export) then pause.
Goal: Reduce cognitive load; retain at least one more save event.
Risk Flag: Threat of disengagement.
Escalate: Immediately capture wallet if not yet collected.

---
## 4. Wallet Acquisition Branches

### 4A. Trigger: Provides Exchange Deposit Address Only
Path:
- Reply: "Exchange batches internally; for timing test we need a self-custody address (any unused is fine)."
- If refusal: Accept exchange address; pivot to second attribution (IP) and keep self-custody ask dormant 5 days before re-raising.
Goal: Achieve at least one self-custody address.
Risk Flag: Repeated deflection with non-answers.
Escalate: Request alternate chain (some will give personal wallet there inadvertently).

### 4B. Trigger: Provides Multiple Wallets Quickly
Path:
- Normalize & cluster; do NOT immediately ask for more; shift to screen recording to diversify pivots.
Goal: Avoid appearing harvest-focused.
Risk Flag: Oversharing could be script-based; watch for templated phrasing.
Escalate: Collect small on-chain timing windows; schedule portal next.

### 4C. Trigger: Refuses Wallet Until “Funds Ready”
Path:
- Offer tiny test concept: "Need network confirmation time; a small dust transfer is standard." 
- If still refusal: Delay, re-attempt post next artifact cycle.
Goal: Normalize ask.
Risk Flag: Hard refusal plus evasive reasoning.
Escalate: Increase focus on IP + author metadata; deprioritize wallet.

---
## 5. Screen Recording / Media Branches

### 5A. Trigger: Sends Compressed Low-Quality Clip (Gallery Share)
Path:
- Respond: "Compression blurred the sequence—could you send it as a document so resolution stays intact?"
- Provide simple instruction if needed.
Goal: Obtain unmodified container & encoder tags.
Risk Flag: Claims inability to send as document.
Escalate: Request annotated screenshots (preferably original sent as Document) as fallback.

### 5B. Trigger: Refuses Recording, Offers Written Steps
Path:
- Accept written; mine stylometry; later reintroduce video framed as "partner audits visually".
Goal: Keep them comfortable while planning second approach.
Risk Flag: Defensive tone or meta-questions.
Escalate: Do not push again until after next successful minor request.

---
## 6. IP / Portal Branches

### 6A. Trigger: Single Portal Visit Only
Path:
- Light note 48h later: "Schedule update posted—check when convenient."
Goal: Acquire second session for stability.
Risk Flag: Ignored twice.
Escalate: Use a passive asset (new DOCX v3) referencing remote logo (second chance beacon).

### 6B. Trigger: Multiple Distinct Hosting Provider IPs
Path:
- Pattern suggests VPN rotation. Increase frequency of small off-cycle portal content updates to exploit operational fatigue (chance of raw ISP slip).
Goal: Catch non-hosting IP.
Risk Flag: Perfectly rotated IP + consistent UA.
Escalate: Add WebRTC optional meeting invite (low chance but worth attempt).

### 6C. Trigger: Rapid Portal Access Immediately After Messages
Path:
- Good for correlation. Introduce a status update at an unusual hour to test delayed reaction.
Goal: Distinguish human schedule vs automated check.
Risk Flag: Instant accesses 24/7 (scripted monitor).
Escalate: Add a token hidden change requiring manual reading; observe if they notice.

---
## 7. Branch Conflict Resolution
If two conflicting branches trigger simultaneously (e.g., Only PDFs + Exchange Wallet only): prioritize the branch that yields *new pivot type*. Example order: Editable DOCX > Self-custody wallet > Multi-session IP > Encoder metadata.

---
## 8. Escalation Thresholds
Move to next tier when any of:
- 3 consecutive failed attempts for same pivot.
- Actor expresses mild annoyance once (not twice) – diversify before persistence hardens.
- You already secured two high-value pivots (e.g., DOCX + wallet) – avoid overfishing; shift to IP.

---
## 9. Disengagement / Abort Criteria
Abort further inducements (preserve evidence) if:
- Actor accuses of verification/tracking explicitly.
- Provides obviously fabricated self-custody addresses (fail uniqueness checks) repeatedly (≥2). 
- Drastic tone shift to aggression plus no new pivots in last 5 interactions.

---
## 10. Rapid Reference Table
| Trigger | Immediate Action | Next If Fails | Pivot Goal |
|---------|------------------|---------------|------------|
| Flat PDF only | Request working file (links broken) | XLSX detour | Editable metadata |
| Blank metadata | Micro correction cycle | Screen recording | Creator fingerprint |
| Exchange wallet only | Ask self-custody timing test | Alt chain request | Wallet cluster |
| Single portal hit | Gentle update ping | Embed remote asset in v3 | Multi-session IP |
| Refuses portal | Offer email recap | Reintroduce after next artifact | Keep rapport |
| Low-quality video | Ask send as Document | Annotated screenshots | Encoder fingerprint |
| Long silence | Soft nudge | Switch to wallet ask | Re-engagement |

---
## 11. Logging Checklist Per Branch Event
- Timestamp (UTC)  
- Branch trigger code (e.g., FP_ONLY, EX_WALLET, SINGLE_PORTAL)  
- Action taken  
- Outcome (SUCCESS / FAIL / PENDING)  
- New pivot captured (Y/N + type)  

---
## 12. Future Enhancements (Backlog)
- Add small CLI tool to auto-suggest next branch based on JSON state.
- Introduce hash-chain integrity for branch event log.
- Auto-normalize wallet addresses & cross-chain link analysis.
- Encoder fingerprint catalog for clustering across cases.

---
End of Adaptive Branching Playbook.
