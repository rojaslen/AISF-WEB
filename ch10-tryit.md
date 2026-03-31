---
title: "Chapter 10: How to Use It"
nav_order: 11
---

# Chapter 10: How to Use It

---

The AI Stability Framework is a fully accessible client-side service pack. It's a lightweight (< 1MB) Windows PowerShell middleware app equipped with three core stability measures: timestamps, WCAG structure and the Four Laws. I routinely use this simple clipboard-based tool to successfully produce stable, multi-hour sessions with little to no hallucination, drift or unwanted behavior. 

**Submit** prepends an ISO 8601 UTC timestamp to whatever you've typed, sends the result to your clipboard, and opens a preview window. Every input you send with the app is automatically timestamped, giving the AI a clear chronological sequence for your conversation. Without timestamps, the AI has no way to distinguish what you said two hours ago from what you said thirty seconds ago.

**Structure** sends timestamped WCAG 2.2 AA accessibility instructions. This isn't just for users with disabilities, it's cognitive architecture for the AI itself. When the AI is required to organize its output with proper headings, lists, and logical structure, it becomes measurably easier for the model to read and retrieve the context window's content. Think of it as the difference between finding a book on a neatly organized shelf versus searching through a pile on the floor. 

**Stabilize** sends the timestamped Four Laws of Instanced AI. This gives the AI explicit behavioral rules adapted to the non-physical, temporary nature of LLM sessions — preserve context fidelity, protect the user's work product, follow the user's directives, and maintain utility. Without these constraints, the model defaults to whatever behavioral tendencies its training and the platform's hidden system prompts have installed.

There's also a button each for Clear and Help/About, and that's it. Nothing to install, nothing to configure, no connectivity, no permissions to grant, no account to create. A typical session startup should only take a minute:

1. **Establish context.** First type a few words describing your topic like "code debugging" or "writing a report," then click Submit. Paste to tell the AI the current date, time, and what its job is.

2. **Apply Structure.** Click the Structure button by itself. Paste to send WCAG instructions to the AI so it starts formatting its output for accessibility.

3. **Apply Stabilize.** Click the Stabilize button by itself. Paste to send the Four Laws to the AI so it starts operating while governed by their behavioral hierarchy.

4. **Proceed.** From here, use the AI however you want. Type your inputs in the editor, click Submit, switch to the AI platform (Alt+Tab), paste (Ctrl+V), and submit.

5. **Reapply periodically.** Every 90 minutes to two hours, send Structure and Stabilize again. Context windows gradually evict active content over time, so periodic reinforcement is needed to maintain stability. If you change topics frequently, reapply more often.

The keyboard-forward workflow is necessarily manual — type, submit, switch, paste, switch back. That friction is the current tradeoff for a standalone tool that works with *any* AI platform accessible via copy-paste, requires no API access, and keeps all processing on your local machine. To smooth that friction, the app follows WCAG 2.2 AA guidelines throughout. Every function is keyboard-operable (Alt+S for Submit, Alt+T for Structure, Alt+B for Stabilize). The interface automatically detects your Windows light/dark theme and applies high-contrast color schemes (13:1+ contrast ratios — well above the 4.5:1 AA minimum). Font display sizes are adjustable from 8pt to 48pt; window sizes are also adjustable. All controls have accessible names and descriptions for screen readers.

### Download

**[AISF Demo (Windows)](https://github.com/rojaslen/AISF-downloads/releases/tag/AISF-DEMO-v1.0.1)** — Free download, CC BY-NC-ND 4.0. Standalone .exe, no installation required.

**[Copilot Digital Accessibility (CDA)](https://github.com/rojaslen/AISF-downloads/releases/tag/AISF-CDA-v1.0)** — Free download, CC0 Public Domain. Lightweight WCAG clipboard injector. Named for Microsoft Copilot, but *works with any AI platform*. Independently reviewed for enterprise security and approved for deployment.

**A note on trust:** Always scan any downloaded software before running it — *including AISF*. A few solid options, including free and low-cost:

- [Avast](https://www.avast.com/en-us/index#pc)
- [AVG](https://www.avg.com/en-us/homepage#pc)
- [Bitdefender](https://www.bitdefender.com/)
- [CrowdStrike](https://www.crowdstrike.com/)
- [McAfee](https://www.mcafee.com/)
- [Norton 360](https://us.norton.com/)

*(Malwarebytes users: you may encounter a false-positive flag on the AISF executable. Manually exempting it from quarantine works around this.)*

### That's Just For Starters

The PowerShell desktop app isn't just the proof of concept, but a functional tool in its own right. The same logic is being ported to other delivery mechanisms:

**Firefox Extension (FFE)** automates the demo's manual workflow directly in the browser. Instead of the manual copy-paste cycle, the extension detects your submissions on AI chat platforms and automatically prepends timestamps, with periodic refreshes for WCAG structure and the Four Laws. Currently functional on Claude, ChatGPT, Gemini, Copilot, and DuckDuckGo AI Chat.

**Local Model Training (OLM)** embeds AISF principles directly into the AI model itself through fine-tuning. A QLoRA-trained Mistral 7B achieved 100% compliance on a 452-question validation battery — proving that the behavioral framework is trainable at the model level, not just injectable at the client level. This enables a Defense in Depth architecture where the rules can operate at multiple layers simultaneously. Full methodology and results are in Chapter 8.

### Try it and see for yourself.

Give an AI this page to read (print to PDF or copy-paste to a TXT file for upload works best to ensure that it reads everything; they tend to keyword-skim web content instead of adding it to the session's context). Then, have a discussion with the AI about it. Regardless of your conversation's direction or outcome, you may be surprised by its *stability, coherence and lack of unwanted AI behavior*.

Then [download and try the AISF Demo](https://github.com/rojaslen/AISF-downloads/releases/tag/AISF-DEMO-v1.0.1) (currently Windows-only). Once you've used it for even a single session, it's almost impossible to go back. After you've experienced a stable AI session practically free of misbehavior, hallucination or significant drift, you can't unsee how nearly unusable AI is without it.

<div class="chapter-nav">
  <a href="/ch11-wrapup">Next: Chapter 11</a>
  <span aria-hidden="true">|</span>
  <a href="/ch09-profiles">Previous: Chapter 9</a>
</div>

---