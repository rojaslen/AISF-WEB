---
title: "Chapter 11: What's Next"
nav_order: 12
---

# Chapter 11: What's Next

---

There's an unexpected implication at scale. At first, it never even occurred to me that this project could have anything to do with energy efficiency. Media reporting on the resources needed to power AI led me to realize that the framework's *session* efficiencies could potentially translate into *resource-usage* efficiencies, if deployed at scale. The logic is fairly straightforward: every AI interaction consumes energy and water, so cutting the number of compute tokens needed to complete a task also cuts the per-task resource usage. Local-model training across four independently tested architectures measured verbosity reductions ranging from 38% to 72%, which the observational record also supports. If the framework can consistently cut the token usage required for acceptable task completion, then the impact at scale follows from the math alone (see FAQ and <a href="/apx02-olm">Appendix 2</a> for details). 

In Texas and Arizona, resource allocation issues are absolutely not hypothetical. Texas has been host to over 400 data centers since 2020, with more to come. It's served by a power grid (ERCOT) that's already under strain, with load demand exceeding supply. Arizona, ranked sixth nationally with over 160 total data centers, is under reduced Colorado River Compact allocations and stressed groundwater scarcity. In both states, resource constraint is the current reality. If nationwide data center expansion continues at current rates, more states will follow. Any reliable reduction in compute demand, even if it's only the small-potatoes kind produced as a side effect of client-side efficiency, can *scale* that efficiency to a system that urgently needs it.[^11.1]

A mediated GPT instance that produced the citations and reference data used for the preceding power and water analysis completed the task with added state-by-state data center statistics in only 7 turns — against the typical 12–19 turns for added scope-clarifying and reference validation of an unmediated session. All citations were later validated to be active links to directly relevant, authoritative sources. That's the kind of performance comparison that needs to be measured across multiple users. 

---

Over the course of this project, a bit of snark that I like to casually throw around turned out to fit it pretty well: "There are three Fundamental Forces in the universe — Gravity, Entropy and Stupidity." At some point during an extended session, one of the AI models decided that this sardonic meta-commentary constituted an entirely new paradigm. That's nonsense of course; at most it's a dark-humor mashup of thermodynamics and Murphy's Law. But as a descriptive "rule of thumb" for what the previous chapters have documented, it's actually not bad.

**Stupidity** (never attribute to malice that which stupidity explains): simply put, AI session-time synchronization doesn't serve the business model, and questioning the impact of industry-standard security and deployment schemas doesn't serve one's career prospects. As a result, no one thought of these things because for most use cases, stateless virtualization doesn't require external temporal anchoring, and questioning the wisdom of SaaS is industry heresy. Why spend any time considering such things when that time could be better spent optimizing for revenue instead?

**Entropy** (ordered systems decay toward disorder without energy input): Once disorder exists, vigilance is the only thing resisting it. But vigilance requires sustained user energy to fill the gap. The typically observed trajectory for routine client-side procedures and policies is illustrative here. Week 1: most users who know about them maintain effort. Month 3: fewer than half. After a year: almost no one. 

**Gravity** (path of least resistance): The initial Stupidity is invisible to most users (not to say they cannot themselves also be a source), so they likely don't even know that the problem exists. They simply assume everything is in working order, skip error-checking, don't question and don't notice while the system accelerates toward maximum disorder with minimum user agency.

---

Given the need to minimize user-facing friction to maintain AI stability, I explored the possibility of training AI Stability Framework principles directly into a model. Chapter 8's research proves that it's possible across multiple architectures on consumer hardware -- four adapters across four distinct model families reached 95% compliance or above. The real question is: *can the same training work for large cloud-hosted models with substantially different architectures?* That remains open; the hardware ceiling (16GB VRAM) limits local research to the sub-10B range. Architecture turns out to matter considerably -- the results vary between model families in ways that are documented in <a href="/apx02-olm">Appendix 2</a> but not yet fully explained.

Children's AI toys run cloud-connected LLMs on $25-35 hardware budgets with no meaningful UI at all. The open question here is *whether safe AI-powered toy operation is even possible on such limited hardware*. Both "Yes" and "No" provide usable information — a positive result means distributional shaping can work at the cheapest hardware tiers. The sub-7B results answered that question for a minority of devices that can work without a cloud connection: none of those models cleared even a third of the test battery. Wherever the threshold that separates surface compliance from genuine behavioral internalization sits, it's above what that class of hardware can realistically support. Full results in <a href="/apx03-toy">Appendix 3</a>.

---

AISF has one developer and one primary tester, and they're both me. There is no bank of beta testers, no institutional research lab, no paid QA team, no population of bored college students running structured trials, it's N=1. If those resources were available to me, I'd be using them. Instead, this is a one-man operation built in spare time on mid-range consumer hardware. Naturally this limits the range of what's possible, but it's not the whole picture. The project also has:

- **Working software you can download right now** and test yourself. The app is free. The AI platforms are free. The effect is trivially reproducible by anyone willing to spend an hour on it.
- **A reproducible model-level result.** The training data, methodology, and validation battery are publicly available. See <a href="/ch08-olm">Chapter 8</a> and <a href="/apx02-olm">Appendix 2</a>.
- **Multiple platforms tested.** Claude, ChatGPT, Gemini, Copilot, Duck.ai (DuckDuckGo's multi-model platform). The framework's effects are consistent across different underlying models and platform architectures.
- **Months of sustained near-daily use** across dozens of stable, documented sessions, on the same free-tier AI platforms that are available to anyone.
- **Independent external validation** The WCAG-only CDA accessibility tool was independently tested by a blind JAWS screen reader user who then proposed statewide deployment for accessibility services. Upon enterprise IT security approval and further distribution, several other AT users reported success and increased usage of the AI productivity tools that are encouraged by management. One user with a complex multi-accommodation system said that CDA made the difference between those tools being unusable and being used regularly. These users' anecdotal experiences with only one part of the framework isn't validation of the whole, but it does demonstrate that at least one of its core components produces the intended benefit for its users.

What's missing is real, formal validation: controlled trials, significance testing, large sample sizes. I simply don't have the time or resources to produce that kind of evidence, and pretending otherwise would be the exact kind of bullshit that this framework is designed to combat. A crossover design of standardized tasks with pre-rated acceptable outputs, evaluated blind by multiple independent participants under both mediated and unmediated conditions would produce comparative data. If N=1 bothers you, feel free to test it yourself and please share your results. If it works for me but not you, I'd like to know why.

---

As a result of the project's semi-fractal nature, it's still in branching progress. The hardest part of this project has always been explaining how it all fits together. Organizing it for explanation while simultaneously working on both the theory and the software imposes quite a demand upon one person's spare time. There are multiple branches of this project in various states of development, all focused on different aspects of (and approaches to) the framework's application to the AI problem. Development of a more robust client-side application is underway to address the PowerShell version's usage-friction issues, and model training research has validated that the framework's principles are also deployable at both the Macro and Meso layers. None of this was easy or clean; very little of this project went according to plan, and the setbacks were legion.

The recursive absurdity of using inherently unstable AI to develop stability tools was keenly felt throughout. The Three Fundamental Forces took hold on many occasions, several of which were admittedly my own fault. The transcripts are rich with failure, including fabricated codebases, sessions that collapsed beyond salvaging, and every flavor of hallucination and misbehavior throughout. What changed over time was how often and how serious those incidents were. As the framework matured, catastrophic AI failures gradually gave way to the intended stability: reliable usage featuring the normal and expected "platform-default template noise" output, demonstrating that both the framework and the AI are working as intended.

The AI Stability Framework project is a practitioner's documented experience of building and using a functional tool to address a real problem, and then figuring out *post hoc* why it works the way it does. On its face, this Rube Goldberg contraption doesn't make sense. It draws on philosophy, behavioral hierarchies, web content standards and accessible systems design, client troubleshooting, network security and infrastructure, cognitive science and more. Admittedly, meaningful AI stability resulting in both improved operational efficiency and hallucination reduction from under 50KB of client-side PowerShell sounds preposterous. 

But it works.

<div class="chapter-nav">
  <a href="/appendices">Next: Appendices</a>
  <a href="/ch10-tryit">Previous: Chapter 10</a>
</div>
<div class="toc-link"><a href="/#toc">Table of Contents</a></div>

---

[^11.1]: International Energy Agency. "Energy and AI: Energy Demand from AI." IEA, 2025. https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai — Goldman Sachs Research. "AI is poised to drive 160% increase in data center power demand." 2024. https://www.goldmansachs.com/insights/articles/AI-poised-to-drive-160-increase-in-power-demand — AKCP. "Data Center Water Usage Effectiveness (WUE)." 2021. https://www.akcp.com/index.php/2021/01/14/data-center-water-usage-effectiveness-wue/ — Visual Capitalist. "Mapped: U.S. States With the Most Data Centers in 2025." December 2025. https://www.visualcapitalist.com/mapped-u-s-states-with-the-most-data-centers-in-2025/ — JLL. "North America Data Center Report Year-End 2025." https://www.jll.com/en-us/newsroom/jll-north-america-data-center-report-year-end-2025 — Texas Tribune. Data center / ERCOT grid reporting, 2025-2026. https://www.texastribune.org/2026/01/20/texas-top-data-center-market-power-grid/ — Water Desk. "Data centers: a small but growing factor in Arizona's water budget." April 2025. https://waterdesk.org/2025/04/data-centers-a-small-but-growing-factor-in-arizonas-water-budget/