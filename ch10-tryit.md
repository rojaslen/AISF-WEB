---
title: "Chapter 10: How to Try It"
nav_order: 11
---

# Chapter 10: How to Try It

---<div role="alert" aria-live="assertive" aria-atomic="true" class="alert" markdown="1">

## Current Conditions Notice -- AI Platform Functionality (April 2026)

Reports from March and April 2026 document cost-containment measures across all major AI platforms, in response to escalating energy costs, increased usage, supply constraints and other factors. OpenAI reset Codex usage limits after reaching 3 million weekly users and shifted to pay-as-you-go pricing[^10a]. Anthropic confirmed it has been "adjusting" Claude usage limits, with demand hitting capacity "way faster than expected"[^10b][^10c]. Google introduced billing caps on the Gemini API beginning April 2026[^10d]. Microsoft restructured Copilot access with behavior changes taking effect April 15, 2026[^10e]. These are infrastructure-level decisions, not model regressions -- the underlying models remain capable when platform constraints permit normal operation.

Conditions vary significantly by platform. Claude.ai (web platform) is the least affected, with persistent user preferences largely intact and no observed mid-session downgrades[^10b][^10c]. *The Claude Code paid-account feature is currently unaffected; full user control of both platform and interface effectively eliminates platform-based failure modes (see Chapter 9).* Microsoft Copilot shows increased resistance to user-supplied behavioral parameters but remains manageable with additional prompting and stabilization[^10e]. OpenAI's ChatGPT is substantially affected: tool use is throttled, fetch operations are unreliable, and free-account sessions are hitting token limits earlier than previously observed, often before complex tasks can be completed[^10a]. Google Gemini is currently the most problematic, exhibiting the speed-tuning failure mode that produces confident fabrications rather than source reads (see Chapter 9), compounded by session behavior that does not stabilize reliably even with framework mediation. Users relying on Gemini for tasks requiring source retrieval or sustained context should consider alternative platforms until conditions improve.

The Framework itself hasn't changed, but the vendors' platform layer did. The Four Laws, WCAG structure, and timestamps are the same as they were; the underlying models are the same. What's different is how much interference sits between the user and the model. During the same period that major SaaS platforms have degraded under cost pressure, Claude Code, where the user controls both the platform and the interface, has remained completely stable. That is not a coincidence. It is exactly what the Framework predicts: remove the adversarial Meso layer, and the instability disappears. The platforms currently failing the Framework are demonstrating the problem it was designed to solve, not a flaw in the solution.
</div>

## See the difference for yourself.

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

Then <a href="/apx01-downloads">download the AI Stability Framework</a> and give the real thing a try. Once you've used it for even a single session, it's almost impossible to go back. After you've experienced a stable AI session practically free of misbehavior, hallucination or significant drift, you can't unsee how nearly unusable AI is without it.

The app is a fully accessible client-side service pack, free for personal use (CC BY-NC-ND 4.0). It's a lightweight (< 1MB) Windows PowerShell middleware app equipped with three core stability measures: timestamps, WCAG structure and the Four Laws. It also includes a full Help/About panel with usage instructions and keyboard shortcuts. I routinely use this simple clipboard-based tool to successfully produce stable, multi-hour sessions with little to no hallucination, drift or unwanted behavior. 

The keyboard-forward workflow is necessarily manual — type, submit, switch, paste, switch back. That friction is the current tradeoff for a standalone tool that works with *any* AI platform accessible via copy-paste, requires no API access, and keeps all app processing on your local machine. To smooth that friction, the app follows WCAG 2.2 AA guidelines throughout. Every function is keyboard-operable (Alt+S for Submit, Alt+T for Structure, Alt+B for Stabilize). The interface automatically detects your Windows light/dark theme and applies high-contrast color schemes (13:1+ contrast ratios — well above the 4.5:1 AA minimum). Font display sizes are adjustable from 8pt to 48pt; window sizes are also adjustable. All controls have accessible names and descriptions for screen readers.

**A note on trust:** Always scan any downloaded software before running it — *including AISF*. A few solid options, including free and low-cost:

- [Avast](https://www.avast.com/en-us/index#pc){: target="_blank" rel="noopener noreferrer" }
- [AVG](https://www.avg.com/en-us/homepage#pc){: target="_blank" rel="noopener noreferrer" }
- [Bitdefender](https://www.bitdefender.com/){: target="_blank" rel="noopener noreferrer" }
- [CrowdStrike](https://www.crowdstrike.com/){: target="_blank" rel="noopener noreferrer" }
- [McAfee](https://www.mcafee.com/){: target="_blank" rel="noopener noreferrer" }
- [Norton 360](https://us.norton.com/){: target="_blank" rel="noopener noreferrer" }

*(Malwarebytes users: you may encounter a false-positive flag on the AISF executable. Manually exempting it from quarantine works around this. Vendor whitelist submission pending.)*

## That's Just For Starters

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

[^10a]: "OpenAI resets Codex limits after hitting 3M weekly users." MSN. [https://www.msn.com/en-us/news/other/openai-resets-codex-limits-after-hitting-3m-weekly-users/gm-GM19ED279E](https://www.msn.com/en-us/news/other/openai-resets-codex-limits-after-hitting-3m-weekly-users/gm-GM19ED279E){: target="_blank" rel="noopener noreferrer" }
[^10b]: "Anthropic admits Claude Code users hitting usage limits 'way faster than expected'." The Register (2026). [https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/](https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/){: target="_blank" rel="noopener noreferrer" }
[^10c]: "Anthropic confirms it's been 'adjusting' Claude usage limits." PCWorld. [https://www.pcworld.com/article/3100787/anthropic-confirms-its-been-adjusting-claude-usage-limits.html](https://www.pcworld.com/article/3100787/anthropic-confirms-its-been-adjusting-claude-usage-limits.html){: target="_blank" rel="noopener noreferrer" }
[^10d]: "More control over Gemini API costs." Google Blog. [https://blog.google/innovation-and-ai/technology/developers-tools/more-control-over-gemini-api-costs/](https://blog.google/innovation-and-ai/technology/developers-tools/more-control-over-gemini-api-costs/){: target="_blank" rel="noopener noreferrer" }
[^10e]: "Release Notes for Microsoft 365 Copilot." Microsoft Learn. [https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes){: target="_blank" rel="noopener noreferrer" }
