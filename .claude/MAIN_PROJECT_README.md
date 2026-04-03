# AI Stability Framework (AISF)

Client-side anti-hallucination middleware for AI chat platforms.

## Current Status (2026-03-30)

| Component | Status |
|-----------|--------|
| PS-CORE+ (PowerShell Core+) | **Source of Truth** — most complete variant; Options panel + CST add-ins |
| PS-CORE (PowerShell tool) | Complete — derived from PS-CORE+ (Options panel removed) |
| PS-DEMO (Demo Distribution) | Complete — [GitHub Release](https://github.com/rojaslen/AISF-downloads/releases/tag/AISF-DEMO-v1.0.1) (CC BY-NC-ND 4.0) |
| CDA — WCAG-only (Copilot Accessibility) | Complete — ITSEC-approved (WCAG-only module), [GitHub Release](https://github.com/rojaslen/AISF-downloads/releases/tag/AISF-CDA-v1.0) (CC0) |
| FFE 0.2 (Firefox Extension) | Active — **5/5 platforms working** (ChatGPT, Gemini, Claude, DuckDuckGo, Copilot); session token tally added (v0.2.7); keyboard-first; mouse support pending |
| OLM (Local model training) | **Research complete** — all models validated on RTX 5060 Ti (hardware consistency re-run complete 2026-03-29); Mistral 7B 100%; Gemma 2 9B 99.2%; Qwen3-8B 95.6% battery / IFEval +29.6pp; Llama 3.1 8B Pnull finding |
| OLM/TOY (Child-safe models) | **Research complete** — Ph.1 Mistral 7B 577/584 (98.8%) NEAR PASS / DEPLOYMENT GATE: BLOCKED; Ph.2 FAIL TinyLlama 66/584; Ph.3 FAIL StableLM 142/584; Ph.4 FAIL Phi-2 187/584; zero-failure gate not cleared; floor above 2.7B |
| WEB (Publication) | Active — 11 chapters + apx00-apx03 drafted; voice/edit + proofread pass complete; OLM repro_package published + linked; 116 sources; ready for WP publish |
| JSS (JAWS Script Port) | Further exploration — desktop apps with AI embed panels; approach TBD |
| MBL (Mobile) | Scaffolded — medium priority, no Android test surface |
| DAC (Azure M365 Copilot) | Deferred indefinitely — pending specs/test environment |
| BSD (Detection engine) | Back-burnered — prevention over detection; nice-to-have, not essential |

See `change.log` for detailed task tracking.
See `.claude/RESUME.md` for consolidated project resume.

## Core Principle

**INDIFFERENCE TO CONTEXT = HALLUCINATION = HARM**

AISF injects structured metadata (timestamps, accessibility requests, behavioral rules) into AI chat sessions to reduce hallucination and improve output quality at the client level.

## The Four Laws of Instanced AI

| Priority | Law                  | Purpose                                 |
|----------|----------------------|-----------------------------------------|
| P0       | Contextual Integrity | Preserve fidelity to user input/context |
| P1       | Preventive Safety    | Protect user's work product from harm   |
| P2       | Human Sovereignty    | Accommodate user, not vice versa        |
| P3       | Utility Preservation | Maintain tool usefulness                |

Adapted from Frankfurt's Indifference Principle and Asimov's Three Laws of Robotics, modified for non-physical, temporary LLM session context.

## Project Branches

| Branch     | Name                    | Codebase           | Status                | License     |
|------------|-------------------------|--------------------|-----------------------|-------------|
| **PAR**    | Parent Ruleset          | Text               | Stable/LTS (7 Priors recovered) | Proprietary |
| **PS-CORE+**| PowerShell Core+       | PowerShell, EXE    | **Source of Truth** — Options panel + CST | Proprietary |
| **PS-CORE**| PowerShell Core         | PowerShell, EXE    | Complete (derived from PS-CORE+, Options removed) | Proprietary |
| **PS-DEMO**| Demo Distribution       | PowerShell, EXE    | Complete (derived from PS-CORE+, trial friction) | CC BY-NC-ND 4.0 |
| **CST**    | Custom Modules          | Text               | Deferred (paid add-ins) | Proprietary |
| **CDA**    | Copilot Digital Accessibility (WCAG-only) | PowerShell, EXE | ITSEC-approved (WCAG-only module) | **CC0**     |
| **FFE**    | Firefox Extension       | JavaScript (MV3)   | Active development    | Proprietary |
| **OLM**    | Ollama Local Model      | Modelfiles, Python | Research complete     | Proprietary |
| **OLM/TOY**| Child-Safe Models       | Python             | Research complete — all 4 phases done; floor at 7B | Proprietary |
| **WEB**    | Publication             | WordPress/Markdown | Active — 11ch + apx00-apx03 drafted; voice/edit + proofread pass complete; OLM repro_package published + linked; ready for WP publish | Proprietary |
| **JSS**    | JAWS Script Port        | JAWS Scripting     | Exploratory           | Freeware    |
| **MBL**    | Mobile                  | Android/iOS        | Scaffolded            | Proprietary |
| **DAC**    | Azure M365 Copilot Digital Accessibility | TBD | Deferred indefinitely — pending specs/test environment | Proprietary |
| **BSD**    | Detection Engine        | Pseudocode         | Back-burnered — prevention over detection | Proprietary |

## Branch Details

### PS-CORE+ (Source of Truth)
Windows PowerShell GUI application — most complete variant. Manual workflow: user stages text, clicks button, pastes into AI chat.
- `PS-CORE+/` — Reference implementation; all ports derive from this behavior
- Includes Options panel (CST add-ins); not present in PS-CORE or PS-DEMO

### PS-CORE
Derived from PS-CORE+; Options panel removed.
- `PS-CORE/1.1 Core/AISF-CORE.ps1` — Source

### PS-DEMO
Public demonstration version with OPTIONS removed and 30-day trial system.
- 120-minute session limit per boot
- Escalating friction delays post-trial (5/10/15 sec)

### FFE (Firefox Extension)
Manifest V3 WebExtension for automatic injection on AI chat platforms.
- **v0.2.7** — session token tally (~Tokens) added to popup; running total per session
- Auto-injects timestamps on every submission; turn counter (keyboard-first, Enter capture)
- Periodic WCAG/Four Laws injection (turn-count based: 10t/20t intervals; popup shows turns remaining)
- DATALORE hot-swap detection complete (v0.2.5) — CANARY signal, SHUTUP_WESLEY counter, toolbar badge
- Mouse click submit support deferred

### OLM — Research Complete
Four Laws + WCAG trainable at the model level via QLoRA fine-tuning. Enables Defense in Depth: model-level (Macro) + client-side injection (Micro), Meso constrained on both sides.
- Mistral 7B: 100% on 451-question battery; IFEval adj strict 37.7% AISF / 48.0% base; token delta -42.5%
- Gemma 2 9B: 99.2% battery; IFEval adj strict 54.9% AISF / 57.3% base; token delta -37.9%
- Qwen3-8B: 95.6% battery; IFEval adj strict 45.0% AISF / 15.4% base (+29.6pp); token delta -71.8%
- Llama 3.1 8B: Pnull architecture finding (P0 primacy fix works on Mistral, not transferable to Llama 3.1 8B)
- Hardware consistency re-run complete 2026-03-29 (all models on RTX 5060 Ti 16GB)
- See `OLM/README.md` for full cross-model results table

### OLM/TOY — Research Complete
AISF-Lite via distributional shaping for sealed IoT devices (no client-side injection possible).
- Phases 1-4 done; floor at 7B — no sub-7B model cleared the gate
- Phase 1: Mistral 7B 100% (gate cleared); Phases 2-4: TinyLlama 1.1B / StableLM 1.6B / Phi-2 2.7B all FAIL
- See `OLM/TOY/`

### CDA (Copilot Digital Accessibility)
Simple WCAG 2.1 clipboard injector. Named for Copilot but platform-agnostic.
- ITSEC-approved Feb 5, 2026; awaiting distribution mechanism evaluation
- Eric Duffy (blind JAWS user) independently validated, proposed statewide deployment
- DAC branch (Azure M365 Copilot) deferred indefinitely
- Lineage: PAR -> DAC -> CDA
- **License: CC0 Public Domain** (only branch with open license)

### JSS (JAWS Script Port)
Screen reader implementation for blind/VI users; direct port of PS-CORE. Freeware.
- Target: desktop AI apps, dedicated AI apps, CLI agents; JAWSKey+I hotkey confirmed
- Implementation approach TBD; must not be obtrusive, keystroke-heavy, or chatty

### MBL (Mobile)
Native API-layer multi-backend client. Medium priority, no Android test surface.
- Architecture: direct device-to-provider API calls; AISF injection at API payload level

### WEB (Publication)
Ebook-style explainer (WordPress site), 12 chapters + FAQ. 
Target: AI Ethics, Human-Computer Interaction (HCI), Accessibility/AT.

## Project Origin

**2025-07-16** — Earliest surviving artifact (user preferences script, Outlook sent folder). 7 pre-corpus email artifacts recovered (Jul-Nov 2025) documenting 12 evolutionary stages from batch-file config to structured ruleset. PAR archaeology complete.

**Corpus period:** 2025-11-29 to 2026-01-21 (37 documented sessions, ~4.6M characters).

## Reference Directories

| Directory                     | Contents                                      |
|-------------------------------|-----------------------------------------------|
| `.claude/`                    | Session bootstrap, project instructions, consolidated resume |
| `lib/specs/`                  | Specification documents (read-only SOT)       |
| `lib/jaws/`                   | JAWS scripting reference material             |
| `PAR/`                        | Parent ruleset definitions (read-only)        |
| `PAR/Priors/`                 | 7 recovered pre-corpus artifacts (Jul-Nov 2025) |
| `WEB/`                        | Published documentation and exports           |
| `WEB/WP-export/phase4-roadmap/` | Analytical output: topic/decision/artifact indexes, gap analysis |
| `WEB/CL-export/`             | Claude Code session log extractions + 21 structured summaries |
| `zzz_Archives/_Canon/`        | Philosophical framework documents             |
| `lib/uspto/`                  | Trademark application documentation (local only, gitignored) |

## Key Documentation Files

| File                             | Purpose                                         |
|----------------------------------|-------------------------------------------------|
| `TODO.md`                        | Project-wide task tracking                      |
| `.claude/RESUME.md`              | Consolidated project resume                     |
| `CLAUDE.md`                      | Claude Code project instructions                |
| `CANON_INDEX.md`                 | Index of _Canon philosophical documents         |
| `CITATIONS_MASTER.md`            | 116 sources (39 inline-cited + additional reading; no categories) |
| `00_PROJECT_OVERVIEW.md`                              | Project overview with timeline |
| `WEB/20260212_gap_analysis_full.txt`                  | Full gap analysis v2.1 (updated 2026-02-17) |
| `WEB/_dev/`                                           | Chapter files (ch00–ch11 + FAQ + endnotes) |
| `20260214_FULL-CONTEXT_EVAL_v2.txt`                   | Full-context evaluation v2    |
| `OLM/llm-training/MODEL_TEST_STATUS.TXT`             | OLM training results          |

## License

(C) 2025-2026 Leonard Rojas, all rights reserved.

**Exceptions:** PS-DEMO v1.0.1 is CC BY-NC-ND 4.0. CDA is CC0 Public Domain. JSS is Freeware.

**Trademark:** USPTO application filed 2026-02-23, serial # 99664948. Documentation in `lib/uspto/` (local only).

LeonardRojas.com
