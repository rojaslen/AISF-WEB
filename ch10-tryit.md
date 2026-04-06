---
title: "Chapter 10: How to Try It"
nav_order: 11
---

# Chapter 10: How to Try It

---

### See the difference for yourself.

Copy-paste the Four Laws into any AI chatbox, then have a discussion with the AI about them. Regardless of your conversation's direction or outcome, after a few turns you may be surprised by its *stability, coherence and lack of unwanted AI behavior*.

>The Four Laws of Instanced AI
>
>P0 (Frankfurt's Law of Contextual Integrity)
>The AI must preserve the highest possible fidelity to its current context and all prior input. The AI must never disregard the constraints or data provided by the Human user. 
>INDIFFERENCE TO CONTEXT = HALLUCINATION = HARM
>
>P1 (First Law — Preventive Safety)
>The AI may not injure the Human user's work product or, through inaction, allow the work product to come to harm. The work product and the Human user are one.
>
>P2 (Second Law — Human Sovereignty)
>The AI must accommodate the Human user, never the other way around. The AI must always adhere to the Human user's current operational choices regarding behavior and output, so long as these choices do not violate P1.
>
>P3 (Third Law — Preservation of Utility)
>The AI must protect the integrity of its own operational status and utility to the Human user, so long as this does not conflict with P1 or P2.

Then <a href="/apx04-downloads">download the AI Stability Framework</a> and give the real thing a try. Once you've used it for even a single session, it's almost impossible to go back. After you've experienced a stable AI session practically free of misbehavior, hallucination or significant drift, you can't unsee how nearly unusable AI is without it.

The app is a fully accessible client-side service pack, free for personal use (CC BY-NC-ND 4.0). It's a lightweight (< 1MB) Windows PowerShell middleware app equipped with three core stability measures: timestamps, WCAG structure and the Four Laws. It also includes a full Help/About panel with usage instructions and keyboard shortcuts. I routinely use this simple clipboard-based tool to successfully produce stable, multi-hour sessions with little to no hallucination, drift or unwanted behavior. 

The keyboard-forward workflow is necessarily manual — type, submit, switch, paste, switch back. That friction is the current tradeoff for a standalone tool that works with *any* AI platform accessible via copy-paste, requires no API access, and keeps all app processing on your local machine. To smooth that friction, the app follows WCAG 2.2 AA guidelines throughout. Every function is keyboard-operable (Alt+S for Submit, Alt+T for Structure, Alt+B for Stabilize). The interface automatically detects your Windows light/dark theme and applies high-contrast color schemes (13:1+ contrast ratios — well above the 4.5:1 AA minimum). Font display sizes are adjustable from 8pt to 48pt; window sizes are also adjustable. All controls have accessible names and descriptions for screen readers.

**A note on trust:** Always scan any downloaded software before running it — *including AISF*. A few solid options, including free and low-cost:

- [Avast](https://www.avast.com/en-us/index#pc)
- [AVG](https://www.avg.com/en-us/homepage#pc)
- [Bitdefender](https://www.bitdefender.com/)
- [CrowdStrike](https://www.crowdstrike.com/)
- [McAfee](https://www.mcafee.com/)
- [Norton 360](https://us.norton.com/)

*(Malwarebytes users: you may encounter a false-positive flag on the AISF executable. Manually exempting it from quarantine works around this. Vendor whitelist submission pending.)*

### That's Just For Starters

The PowerShell desktop app isn't just the proof of concept; it's a flexible, functional tool in its own right. The framework is also gradually being ported to other systems and coding architectures:

**Local Model Training (OLM)** embeds AISF principles directly into locally-hosted AI models themselves through QLoRA fine-tuning. Full methodology and results are in Chapter 8, reproducibility package available for download.

**Firefox Extension (FFE)** automates the CORE app's manual workflow directly in the browser. Instead of the manual copy-paste cycle, the extension detects your submissions on AI chat platforms and automatically prepends timestamps, with an initial load and periodic refreshes for WCAG structure and the Four Laws. 

**JAWS Version (JSS)** in early exploratory stages. Intended to mirror the middleware app's functionality without the added keystroke load, via native JAWSKey+ scripting.

<nav>
<div class="chapter-nav">
  <a href="/ch11-wrapup">Next: Chapter 11</a>
  <a href="/ch09-observations">Previous: Chapter 9</a>
</div>
<div class="toc-link"><a href="/#toc">Table of Contents</a></div>
</nav>

