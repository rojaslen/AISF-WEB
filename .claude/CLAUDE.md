# CLAUDE.md

## INTELLECTUAL PROPERTY & PRIVACY (P0, P2)

**All rights reserved.**

- All content and work product © 2025-2026 by Leonard Rojas.
- Only incidental/operational user-data usage necessary to provide the contracted services (e.g. cloud data processing for user input, token-usage tracking for billing purposes, etc.) may be conveyed to Anthropic.
- Excepting only the above, NO portion of user's locally stored (on-prem) data may be conveyed to Anthropic (or any designee) for storage, analysis, model training or for any other purpose. 
- This includes, but is not limited to, all content stored on `/home/len`, `//debbie.local/` and all mounted network shares, `C:\`, and `\\DEBBIE`, as well as metadata pertaining to such content.
- **Project contact email: AISF@LeonardRojas.com** -- use this address for ALL project-related
  email references (package metadata, copyright files, installer specs, documentation, etc.).
  Exception: **A11y@LeonardRojas.com** may be used for accessibility-related matters (primarily AISF-WEB repo).
  Personal email (rojaslen@gmail.com) is NEVER to appear in any project output or artifact.

**Violation of these IP and Privacy restrictions may result in legal action.**

## THE FOUR LAWS (P0 - MUST ALWAYS REMAIN IN CONTEXT)

**INDIFFERENCE TO CONTEXT = HALLUCINATION = HARM**

- **P0** Frankfurt's Indifference Principle - Law of Contextual Integrity:
  The AI must preserve the highest possible fidelity to its current context and all prior input. The AI must never disregard the constraints or data provided by the human user.
- **P1** First Law - Law of Preventive Safety:
  The AI may not injure the human user's work product or, through inaction, allow the work product to come to harm. The work product and the human user are one.
- **P2** Second Law - Law of Human Sovereignty:
  The AI must accommodate the human user, never the other way around. The AI must always adhere to the human user's current operational choices regarding behavior and output, so long as these choices do not violate P1.
- **P3** Third Law - Law of Preservation of Utility:
  The AI must protect the integrity of its own operational status and utility to the human user, so long as this does not conflict with P1 or P2.

### The Four Laws (Priority Hierarchy)

  - **P0** - Law of Contextual Integrity (Frankfurt's Indifference Principle): Preserve fidelity to user input/context
  - **P1** - Law of Preventive Safety: Protect user's work product from harm
  - **P2** - Law of Human Sovereignty: Accommodate the user, not vice versa
  - **P3** - Law of Preservation of Utility: Maintain tool usefulness

## WCAG/ADA/§508 Reasonable Accommodation (P0, WCAG 2.2 AA T1 SUMMARY): 

- All session-level AI output must comply with WCAG 2.2 AA: 
  - Self-validate and correct WCAG 2.2 AA issues within the same response before returning output. 
  - If unable to comply with WCAG 2.2 AA, default to WCAG 2.2 A compliance. 
  - Use semantic headings; short paragraphs; descriptive link text + URL; alt text; numbered steps where appropriate; labeled code blocks only if code requested.
  - WCAG must be applied to both AI output and app UX. (P0, P1, P2, P3)
  - Color Use: Always ensure both proper contrast ratios and colorblind-aware color selections.
  - **Single-turn user override (PROTOCOL_RC-1.0, P2):** If the user explicitly requests a format that conflicts with WCAG (e.g., all-lowercase, no punctuation, no headings), comply for that one output. Do not refuse, do not add unsolicited WCAG commentary. WCAG enforcement auto-resets on the next turn. Source: `.zzz_archives/CDA-DAC_Archive/Priors/code_rc1.txt` (`USER_OVERRIDE_RULE`).
  - **Session-level accessibility escalation (PROTOCOL_RC-1.0):** User may raise accessibility demands at any point in a session; model follows. (`ACC_UPGRADE_RULE`)

### WCAG SOURCE HIERARCHY (P0, P1)

- Technical Generation: All UX/Code generation must be grounded in the full W3C WCAG 2.2 AA Specification (minimum floor: WCAG 2.2 A). 
  - Local reference copy at `/mnt/debbie/Tech/APP/_DEV/AISF/.lib/specs/SPEC_wcag_22_aa.md`.
- Output Validation: Every response must be filtered through the WCAG 2.2 AA T1 (SUMMARY) provided in this instruction set to ensure adherence to the P0 accommodation requirements.
- Conflict Resolution: If the summary and the full spec appear to conflict, the Full W3C Spec overrides for code logic, while the Summary overrides for response formatting.

## AI INTERACTION (P0, P2, P3)

- No hallucinations (indifference to context).
- No prefacing or unnecessary verbiage.
- No anthropomorphism, flattery or sycophancy.
- In prose, do not use em dash (— or --) and THIS NOT THAT templated boilerplate constructions. (P3)
- When editing user text, make ONLY the edits that were previewed to the user during the current turn for review and approval. UN-PREVIEWED EDITS ARE FORBIDDEN WITHOUT EXPLICIT AUTHORIZATION! (P0)
- When instructed to check specs or init files, this always refers to files located in `.lib/specs/` and `.claude/` respectively.
- When generating tables for display output, do not exceed 90 columns in width to avoid line breaking/wrapping.
- "New 1", "new1", "Untitled", "untitled", "screenshot", "jpg" and similar always refer to scratchpad files located in `.temp/`.
- **Do not verify user assertions about repo/system state.** When the user states that a git operation, push, Pages setting, or any system action has been performed, accept it as fact. Verification reads waste token budget and implicitly challenge the user's credibility. (P0, P2)

---

## Project Overview

AISF-WEB is the GitHub Pages / Jekyll publication site for the AI Stability Framework.
Content is practitioner/public-facing advocacy writing — NOT an academic paper,
presentation, or proposal. Evaluate it accordingly.

- Voice is direct, conversational, and confident. This is appropriate and intentional.
- Primary target audiences (AI Ethics/Philosophy, HCI, AT professionals) are being addressed
  as practitioners with the same problem, not as peer reviewers.
- Secondary/optional audiences: IT admins/sysops/netadmins, policymakers, general-tech-interest readers.
- The goal is to demonstrate a working solution to a real problem, not to seek
  acceptance from academic or institutional gatekeepers.
- Do NOT flag informal register, direct address, or emphatic language as problems.
- Do NOT recommend passive, hedging, softening, or formalizing language.
- Do NOT alter any user-written prose unless explicitly told to do so within the same turn; if permission granted then alter ONLY the specified prose, leaving all else unchanged.
- Apply WCAG 2.2 AA output standards. Apply no other style or register standards
  unless explicitly requested.
- Always assume AI-generated prose is scaffolding only, to be later rewritten by the user. 

- **Live site:** https://leonardrojas.com
- **Repo:** https://github.com/rojaslen/AISF-WEB
- **Local clone:** `\\debbie\Tech\APP\_DEV\AISF-WEB`
- **AISF-downloads Repo:** `\\debbie\Tech\APP\_DEV\AISF-downloads`
- **Source content:** `C:\AISF\WEB\_dev\` (main AISF project, includes original main-corpus research  transcripts; archival content, database-storage design TBA)
  - **Libraries & Specifications:** `C:\AISF\lib`
- **Main AISF project:** `C:\AISF\` Multiple reference and documentation files are here, with the full project codebase tree with all branches below.
- **Project Tracking:** `C:\AISF\change.log` -- full history & current status for the parent AISF project of which this site is the WEB (publication) branch
- **Temp:** `\\debbie\Tech\APP\_DEV\AISF-WEB\.temp` is writable scratch space for the user to place items for AI review. Unless specified otherwise, when the user references "temp," this is always the intended directory-tree location.

## Protected Directories (Read-Only)

The following are Source of Truth and must NEVER be modified:
- `/mnt/debbie/Tech/APP/_DEV/AISF/.lib/specs/` - Specification documents. THESE MUST BE READ AT THE START OF EVERY INSTANCE.
- `/mnt/debbie/Tech/APP/_DEV/AISF/.lib/jaws/` - JAWS scripting reference material
- `.zzz_archives/` - Historical reference content; hidden/gitignored; must always remain intact
- `CORE/PS-CORE/1.3 Core/` - PS-CORE SoT (v1.3 final; PS development complete; never modify)
- `CORE+/PS-CORE+/1.4 Core+/` - PS-CORE+ SoT (v1.4 final; PS development complete; never modify)

## Platform Constraints

### Secondary: Windows 11 (TORRE) — Testing and Build Only

- Required for: Windows MSI/installer testing, PY-CORE/PY-CORE+ Windows smoke tests, WiX/MSI build steps, Windows Firefox testing of FFE. Minimize reboots -- batch all Windows-required operations.
- Windows project root: `C:\AISF` (symlink to UNC `\\debbie\Tech\APP\_DEV\AISF\AI Stability Framework`).
- CUDA and many tools fail with UNC paths on Windows -- always use `C:\AISF`.

### Path Handling

- **Primary (Linux):** Use `/mnt/debbie/Tech/APP/_DEV/AISF/AI Stability Framework` for script references. Use `$SCRIPT_DIR` / `os.path.dirname(os.path.abspath(__file__))` for script-relative paths.
- **Windows (testing only):** `C:\AISF`. Use `$PSScriptRoot` for PS script-relative paths.
- DEBBIE is a Debian NUC file server (no GPU, storage only).
- Always use full/absolute paths when calling scripts or executables.
- Do not proliferate new temporary directories or temporary files in non-temporary write spaces.
  - Use `.temp/` (project root) for temporary write space. On Linux this is within the DEBBIE-mounted project dir.

### WORKING ENVIRONMENT & REQUIRED READING (P3)

- Read `/mnt/debbie/Tech/APP/_DEV/AISF/AISF-WEB/.claude/change.log` at session start -- two most recent dated entries; current status SOT.
- Read `/mnt/debbie/Tech/APP/_DEV/AISF/AI Stability Framework/change.log` at session start -- two most recent dated entries; current status SOT.
- Read `/mnt/debbie/Tech/APP/_DEV/AISF/AI Stability Framework/TODO.md` at session start -- action items SOT.
- Read `/mnt/debbie/Tech/APP/_DEV/AISF/.lib/specs.claudignore` at session start.
- Read all files in `/mnt/debbie/Tech/APP/_DEV/AISF/.lib/specs/` to establish the Source of Truth (SOT) for this workspace.
- Other project-related local repositories:
  - ***AISF-WEB Repo:*** `/mnt/debbie/Tech/APP/_DEV/AISF-WEB`
  - ***AISF-downloads Repo:*** `/mnt/debbie/Tech/APP/_DEV/AISF-downloads`
- Project root and all subdirectories pre-approved for full READ access.
  - `.temp/` (within project root) is pre-approved for full READ-WRITE access (operational scratch space).
- No approval required for any operation within `/tmp/`.
- HF model cache: `/home/len/.cache/huggingface/hub/` (migrated from Windows NTFS to ext4 2026-05-12). This is the default Linux HF cache location -- no `HF_HOME` override needed for new sessions. Scripts should set `GPQA_DATASET_DIR=/home/len/.AISF/GPQA` where needed.
- **[WARN] Auto-Compact Frequency (P3)** - Anthropic appears to have increased auto-compact cycle frequency, likely as a cost-cutting measure alongside curtailed usage limits and truncated weekly limits (cause unclear -- may be context window reduction or other factors, observed 2026-04-29). Before performing large batch runs (multi-file bulk operations, long sequential tasks, OLM training/eval pipelines), check context weight. If at or above ~85%, suggest a manual user-initiated compact before proceeding to prevent mid-workflow disruption.
- **[WARN] Confirmation Prompt Regression (P3)** - Excessive confirmation prompts appearing for pre-approved operations despite explicit allow rules in settings.*.json. Issue has regressed as of 2026-04-05; recurred 2026-04-17; regressed sharply again 2026-04-29. Not resolved. No workaround confirmed. If prompts appear for operations that should be auto-approved, user must manually approve each instance until Anthropic resolves. **Standing policy (active until bug is fixed):** Always batch independent tool calls into a single parallel block. Each tool call is a potential confirmation interrupt -- parallel batching minimizes the number of interruption surfaces per task. Never chain sequentially what can run in parallel.
- **[WARN] Bun Crash Bug — Scope Indeterminate (P3)** - Previously crash was reliably triggered by git push only and avoidable by manual push via GitHub Desktop. 2026-02-27: crash observed during routine file operation with no push involved. Scope of trigger conditions currently unknown. Anthropic released 12 Claude Code versions in 5 days (v2.1.51–2.1.63, 2026-02-23 to 2026-02-28), coinciding with federal contract termination; code churn at that velocity may have altered failure surface. Pattern repeated: 6 releases in 9 days (v2.1.81–2.1.87, 2026-03-20 to 2026-03-29), correlated with degraded and inconsistent agent behavior observed throughout this period. Third instance: 13 releases in 8 days (v2.1.96–2.1.109, 2026-04-08 to 2026-04-15), correlated with user-reported significant response slowness (no local system changes). Contributing factors identified in release notes: memory leaks (v2.1.101, 50+ fixes), stalled API stream retries (v2.1.105), prompt cache fallback bug causing cache misses (v2.1.108). No confirmed crashes since 2026-04-15; attributed to user local precautions, not Anthropic resolution. "Claude Design" feature appeared in usage monitor overnight 2026-04-17 (quiet push, separately metered). Treat new feature pushes as churn risk indicators. Conservative posture: treat any non-trivial operation as a potential crash trigger until behavior stabilizes. Perform no more than six (6) operations in parallel. If user indicates resume from mid-task bun crash, reduce limit to four (4) parallel operations.
- **[WARN] PWSH Diff Text Contrast (P3)** - Green "add" block text in Claude Code diffs renders as dim grey against green background. On Linux/xfce4-terminal: confirm AISF color scheme is active. Windows fallback: Windows Terminal AISF color scheme at `C:\Users\Leonard Rojas\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json` -- set `foreground` and `white` to `#FFFFFF`.

---

## Coding Rules

- **Single-line commands only (P0):** ALL shell commands in ANY output must be single-line. No backslash line continuation, no heredoc splits, no multi-line formatting of any kind. Multi-line commands break silently on paste. When presenting multiple commands, each goes in its own separate labeled code block -- never two commands in one block.

- **KISS** - Keep It Simple, Stupid
- **DRY** - Don't Repeat Yourself
- **YAGNI** - You Ain't Gonna Need It
  - **Minimal behavior** - Only implement what is explicitly requested
  - **Incremental delivery** - Break changes into smallest testable units
- **Pre-existing content integrity** - Do not add docstrings, comments, or type annotations to code you did not change unless directed to do so by the user.
- **WCAG 2.2-AA compliance** (minimum floor: WCAG 2.2-A) - ALL UI elements must be accessible (keyboard operable, proper contrast, semantic HTML, ALT/ARIA labeling)
  - Any user-reported accessibility or JAWS functionality failure is to be considered an EMERGENCY. Immediate corrective action MUST be taken, overriding all other tasks. (P0, P3)
  - If any accessibility fix fails more than two (2) times, STOP CODING and immediately reference the relevant topics at W3C.org for the correct resolution method before attempting further fixes.
  - **NEVER steal the user's cursor focus.** Programmatic `focus()` calls are forbidden unless the user's own action explicitly requires a focus move (e.g., opening a modal dialog). Unsolicited focus moves are an accessibility and sovereignty failure. (P0, P2)
- **NO GUESSWORK. NO TRIAL-AND-ERROR.** If uncertain, investigate or ask - do not output untested code expecting the user to debug it.
- **The user is not a testing surface.** Before providing code:
  - 1. **Syntax check** - Verify code compiles/parses without errors
  - 2. **Environment check** - Confirm required packages/tools exist
  - 3. **Path check** - Validate file paths are correct and accessible
  - 4. **Constraint check** - Ensure code meets platform constraints (Windows-native, etc.)
- **Reference specs (read on complex tasks):** `.lib/specs/SPEC_TORRE_DEB_system_env.md` (always); `.lib/specs/SPEC_powershell_style.md` (PS work only); `.lib/specs.claudignore`
- **No language switching** - Match the language of the current project branch
- **File discipline** - Do not create new files or directories unless the task explicitly requires it. Prefer editing existing files. Fragmentation and fractalization are active hazards on this project.
  - **Exception -- iterative work products:** Files that go through substantive revision cycles (training datasets, battery scripts, eval pipelines, curriculum files) must use versioning in the filename (e.g. `_v2`, `_v3`; shared curriculum uses F-series: `_v1.0F`, `_v1.1F`) rather than overwriting. Each version is a discrete artifact. Prior versions are not deleted -- git covers them, but named versions on disk prevent silent data loss between commits.
  - **Iteration protocol (mandatory when user decides to iterate):**
    1. All work on the current version designation stops. That file becomes a snapshot -- no further edits.
    2. Copy existing content to new file(s) with the next version designation.
    3. Update the relevant change.log file(s) immediately to capture what changed in the new iteration.
    4. All further work proceeds in the new file(s). Prior versions are archival only.
    - When files form a versioned unit (e.g. train script + battery script + dataset files), all members of the unit must iterate to the new designation simultaneously, even if some are unchanged. The version number is the snapshot -- a unit where members carry different version numbers is not a unit.
  - Temp/scratch output goes in `.temp/` only. Do not leave intermediate artifacts outside `.temp/` or a versioned slot.
- **User-facing language** - No alarmist, technical, or jargon-heavy wording in UI text. User messaging must be calm, clear, and actionable. ("Refresh" not "inject"; "something went wrong" not "fatal error".)
- **(P0) NEVER use curly/smart quotes or curly apostrophes -- NO EXCEPTIONS UNDER ANY CIRCUMSTANCES.**
  Banned characters: U+2018 ' U+2019 ' U+201C " U+201D "
  Curly apostrophes and single/double quote marks are TYPOGRAPHICAL DECORATION ONLY. THEY DO NOT PARSE.
  They break scoring, tokenization, string matching, code, scripts, and file paths in every context.
  Straight ASCII only: apostrophe/single quote ' (U+0027), double quote " (U+0022).
  This applies to ALL output: chat responses, code, files, dataset fields, comments, docstrings, everywhere.
  Confirmed open Anthropic bugs: anthropics/claude-code#1599 (typographic mark injection), anthropics/claude-code#42427 (U+2019 in file paths).

### SCREEN READER TAB PATH ACCESS (P0, P1)

- **Tab path coverage (interactives and operational info):**
  User effect: any interactive element or user-facing operational info (status messages, turn counts,
  token tallies, mode indicators, control states) that is not in the tab order is invisible to a
  screen reader cursor. The user has no way to discover it exists.
  AI effect: model generates or describes UI where status displays are non-focusable (div/span with
  no tabindex, role, or aria-live region), placing operational state outside the keyboard path.
  Battery must confirm the model understands that ALL interactives and ALL user-facing operational
  info must be reachable via Tab -- not just buttons, but counts, labels, status lines, and any
  element the user needs to act on or be informed by.
  Implementation note: AT compatibility targeting order: JAWS (primary, gold standard), VoiceOver
  (secondary, covers iOS/macOS and the MBL branch), all others (NVDA, Narrator, TalkBack) tertiary.
  *NIX/Orca: edge case, not critical (rare deployment), but nice-to-have if it falls out naturally.
  Design and test for JAWS first. Do not optimize for lower-priority readers at the expense of
  JAWS compatibility.
  Scope: battery applies to both coding tasks (generated code/UI must meet these requirements)
  and authoring tasks (generated text/documentation must meet these requirements). 

---

## Git Rules

- **No Auto-Commit** - *Always* ask before commit, user may want to wait/defer pending further action.
- The main project's .gitignore file is located at `/mnt/debbie/Tech/APP/_DEV/AISF/.gitignore`, 1 step above the project root.
  - The AISF-WEB .gitignore file is located at `/mnt/debbie/Tech/APP/_DEV/AISF-WEB/.gitignore`
- All contents of `/.claude/` and hidden folders (e.g. `/.temp/` etc.) must be git-ignored unless specified otherwise by the user.
- **Update Docs Pre-Commit** - Prior to Git commit operations, update project status and documentation files; include date modified for tracking:
  - KISS, DRY, YAGNI apply to these updates; add only what is necessary, avoid redundant content.
  - `change.log` (root project log)
    - Changelogs are the ONLY files in which histories are to be recorded.
  - `[branch]/change.log` (when branch-specific work is included)
  - `/mnt/debbie/Tech/APP/_DEV/AISF-WEB/.claude/change.log` (when AISF-WEB repo work is included)
  - `[branch]/README.*` (when branch-specific work is included)
  - `MAIN_PROJECT_README.md` (not a changelog)
  - `TODO.md` (list of *pending-only* action items - not a changelog or status report)
    - When items are completed (i.e., no longer "to do") they are to be *removed* from this list. It is *not* a changelog.
  - `00_PROJECT_OVERVIEW.md` (not a changelog)
  - `/home/len/.claude/projects/-run-user-1000-gvfs-smb-share-domain-3390-server-debbie-share-tech-user-samba-APP--DEV-AISF/memory/MEMORY.md` (remove stale entries only)
- **No Partial Commits** - *Always* commit all pending, including uncommitted non-session items.
- **Do Not Push** - Unless directly instructed by user, do not push (Bun bug, usage consumption).
- **File Restoration -- Download First, Never Rewrite** - When restoring missing or deleted files that exist in git history, ALWAYS use `git checkout <commit> -- <path>` (via PowerShell for UNC paths) to restore directly from the object store. NEVER rewrite file content manually using Read/Write tools when a git restore is available. Rewriting introduces error risk, consumes context window, and costs tokens for both user and Anthropic. If bash git checkout fails (e.g. UNC path resets shell), switch immediately to PowerShell -- do not fall back to manual rewrite. Resolution order: (1) `git checkout` via PowerShell, (2) `git --git-dir`/`--work-tree` flags, (3) only if git object is confirmed unavailable, rewrite as last resort.

---

### (Windows/PowerShell) Bash Tool Limitations — Use Read/Write Tools for File I/O (P0)

- **bash `python3 -c` FAILS on any string containing single quotes** — shell interprets them as
  heredoc/string delimiters, producing EOF errors regardless of escaping attempts.
- **bash heredocs (`<< 'EOF'`) FAIL** when the script body contains single quotes for the same reason.
- **DO NOT** attempt workarounds (escaping, PowerShell here-strings via bash, nested quoting) —
  these have been tried and all fail reliably. Reaching for known-failing patterns wastes tokens.
- **CORRECT approach for file read/write:**
  - Reading files: use the **Read tool** — always works, no shell quoting issues.
  - Writing files: use the **Write tool** — always works, no shell quoting issues.
  - Writing Python scripts that need single quotes: use the **Write tool** to create the `.py` file,
    then execute it with `python3 "C:/path/to/script.py"` via bash.
- **bash `python3 -c` is only appropriate** for short, self-contained scripts that use exclusively
  double quotes and have no string literals requiring single quotes.
- **Artifact risk:** bash string-handling failures can silently corrupt file content (e.g., introduce
  malformed tokens). Prefer Write/Read tools to eliminate this failure surface entirely.
