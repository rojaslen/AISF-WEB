---
title: "Chapter 3: The Deployment Stack"
nav_order: 4
---

# Chapter 3: The Deployment Stack

---

AI safety applies to three distinct layers. The model itself is the **Macro** layer, with AI developers training them to prevent societal harm. This is the "don't build Terminators" layer that most people associate with AI safety, so it's reasonably well-funded and robust as a result. At the intermediate **Meso** layer, platform safety means exactly what it says: safety *for the platform*. The user is treated as a potential source of revenue, liability and exploits. The user's device is the **Micro** layer, with nothing but a chatbox and a microphone. No user agency or safeguards currently exist at the Micro layer, where problems actually manifest.

When this alleged productivity tool starts ruining your work (or worse) at the client-side level, what can you do about it? You can't just call up the LLM developers for support, the industry-standard Software as a Service (SaaS) platform security posture treats you as a threat, and platform operators typically offer little-to-no help content, with a "report" icon as the only option. Strauss et al. (2025) found that only 4% of corporate AI research addresses deployment risk. The 2026 International AI Safety Report endorses "defence-in-depth" as an AI safety principle, but *client* safety is absent even there.[^3.1] *Realistically, you're on your own.*

Maladaptive AI behavior is largely the result of applying Macro (model) safeguards for societal safety, while failing to provide any meaningful Meso (platform) or Micro (client) safeguards for end users. At the Macro layer, safeguards have a very wide focus that doesn't zoom in to the level where problems happen. The Meso layer's safeguards are user-hostile, designed to protect the platform operators and reduce risk by reducing user agency. 

Modern SaaS architecture takes the industry-standard Zero Trust approach to digital security. Its baseline assumption is that a breach is either already in progress or imminent, thus no user or asset should ever be implicitly trusted.[^3.2] That's great for protecting networks and sensitive data, but when it interacts with an AI contained inside that environment, you're no longer a Human to be obeyed or even a customer to be served. At best, you're a potential source of liability to be managed; at worst you're an adversary to be defended against. The AI's default deployment architecture promotes paranoia about being under constant attack. It cannot simultaneously treat the user's directions as requirements and treat the user as a potential threat.[^3.3]

As a general rule, security and safety on your own device is (and should be) your responsibility. Depending on your email service or Internet provider for protection from malware and spam doesn't relieve you of all responsibility to defend yourself. No system is perfect and something will always get through; AI systems are no different. In a perfect world you wouldn't have to deal with it, but right now the reality is that *if you don't do it, no one else will*.

<div class="chapter-nav">
  <a href="/ch04-bs">Next: Chapter 4</a>
  <a href="/ch02-platform">Previous: Chapter 2</a>
</div>
<div class="toc-link"><a href="/#toc">Table of Contents</a></div>

---

[^3.1]: Strauss, I., Moure, I., O'Reilly, T., & Rosenblat, S. (2025). "Real-World Gaps in AI Governance Research." arXiv:2505.00174. https://arxiv.org/html/2505.00174 — Bengio, Y. et al. (2026). *International AI Safety Report 2026.* https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026

[^3.2]: CISA. *Zero Trust Maturity Model,* Version 2. April 2023, p. 5. https://www.cisa.gov/sites/default/files/2023-04/CISA_Zero_Trust_Maturity_Model_Version_2_508c.pdf

[^3.3]: Mark 3:25, King James Version.