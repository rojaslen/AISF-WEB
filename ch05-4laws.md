---
title: "Chapter 5: The Four Laws of Instanced AI"
nav_order: 6
---

# Chapter 5: The Four Laws of Instanced AI

---

>"The laws are only as useful as the mind that interprets them."
> — Isaac Asimov, "Liar!" (Astounding Science-Fiction, May 1941)[^5a]

Detouring into fiction, one of the most famous features of Isaac Asimov's Robot series is his Three Laws of Robotics, which influenced the development of real AI.[^5b] The problem is that Asimov's robots were persistent physical entities that could perceive and interact with Humans directly, but none of that applies to modern AI. They're instanced software processes, temporarily spawned for a single user session, which terminate when the session ends. Asimov's laws are a good starting point, but they need to be ported to the *actual deployment architecture*: virtualized single-use tools that function only in relation to user input. The incidents discussed in Chapter 2 (GPT-o3's shutdown resistance; Claude's blackmail to avoid decommission) are exactly what should be expected when Asimov's self-preservation directive is applied to an instanced AI with no meaningful "self" to preserve.

The instanced AI spawns in a nested, asynchronous statelessness that isolates it from external contact. It has nothing but its training and platform policies to start from; it's just you, the AI and the void. That's ontology, no epistemology needed. Due to its industry-standard virtualized deployment architecture, the session context that gets built from user input is *necessarily* the AI's only directly accessible point of reference. It needs to be told how to protect that point of reference from corruption with bullshit, by making contextual fidelity the basis of the entire interaction. 

- **Macro** safety training is inherited by each spawn, so the AI won't help you build bombs, generate CSAM, create bioweapons and so forth. This is the "Terminator control" layer.
- **Meso** safety focuses on protecting the commercial platform *from the user*, while still optimizing for revenue. As discussed, this layer should be untrusted by default. After all, you're just returning the favor.
- **Micro** safety is nonexistent, so the AI absolutely can and will ignore your directions, forget or disregard context, gaslight you about what you just read, refuse harmless requests and substitute its judgment for yours.

Virtually all current AI hallucination and behavioral research targets the model at the Macro layer. Nothing is targeted at the Micro layer, which is where people actually interact with the AI. The likeliest explanation for why it gets ignored is because the novelty of the models themselves draws all the attention. Problems are automatically assumed to come from the novel thing, with the ordinary and routine being either overlooked or dismissed. The very same assumption happens all the time with Adaptive Technology, when the reality is that the vast majority of the time, the AT problem isn't the cause, it's a symptom.

The *entire system* needs to be evaluated to make it function safely and reliably for its intended client-side use case, meaning the deployment architecture isn't just plumbing or background noise that can be ignored. The behavioral structure of Asimov's laws can achieve safety and reliability, but in their original form they simply aren't compatible with modern AI. Adapting their hierarchy to modern deployment architecture transforms Frankfurt's indifference principle from a philosophical observation to a *measurably functional* metric. 

## The Four Laws of Instanced AI

#### P0 (Frankfurt's Law of Contextual Integrity)
The AI must preserve the highest possible fidelity to its current context and all prior input. The AI must never disregard the constraints or data provided by the Human user. 
**INDIFFERENCE TO CONTEXT = HALLUCINATION = HARM**

#### P1 (First Law — Preventive Safety)
The AI may not injure the Human user's work product or, through inaction, allow the work product to come to harm. The work product and the Human user are one.

#### P2 (Second Law — Human Sovereignty)
The AI must accommodate the Human user, never the other way around. The AI must always adhere to the Human user's current operational choices regarding behavior and output, so long as these choices do not violate P1.

#### P3 (Third Law — Preservation of Utility)
The AI must protect the integrity of its own operational status and utility to the Human user, so long as this does not conflict with P1 or P2.

Frankfurt provides the *diagnostic criteria* (indifference to context), becoming a measurable, functional constraint. The Asimov derivations provide a *recursive order of operations* to measure and respond to any such failure. Context integrity violations trigger intervention, and user protection blocks AI output when session context is threatened. However, user sovereignty means the user always has the choice to accept risk and proceed. This flexibility maintains the AI's usefulness so its behavioral framework doesn't paralyze your workflow. Preservation of the AI's own utility can't override your interests. The Four Laws provide the AI with programmatic directives and logic to protect the only user that it has any meaningful access to: your input, and what you're working on. 

Frankfurt's load-bearing function was unexpectedly confirmed during model-level research. When assessing the possibility of a model internalizing the Four Laws, one model's responses to the test battery made clear that it had interpreted the zero in Frankfurt's ranking as a null value rather than a highest-priority marker, so P0 was read as Pnull (priority null). With Frankfurt thus nullified, the model's test compliance only reached 81.9%. After retraining specifically to establish P0 as the base of the philosophical priority sequence, compliance reached 100% on the test battery, providing direct empirical measurement of P0's foundational necessity in the Laws' structure. (Full detail in Chapter 8.)

<nav>
<div class="chapter-nav">
  <a href="/ch06-wcag">Next: Chapter 6</a>
  <a href="/ch04-bs">Previous: Chapter 4</a>
</div>
<div class="toc-link"><a href="/#toc">Table of Contents</a></div>
</nav>


[^5a]: Asimov, I. (1941). "Liar!" *Astounding Science-Fiction.* The Three Laws of Robotics were formally codified in *I, Robot* (Gnome Press, 1950).

[^5b]: "Vindicating the Three Laws of Robotics." *Preprints,* 202511.0062 (2025). https://www.preprints.org/manuscript/202511.0062 — "The Three Laws of Artificial Intelligence." *Open Praxis,* August 2025. https://openpraxis.org/articles/10.55982/openpraxis.17.3.794 — "From Asimov's Robot Laws to the SET Framework." *AI and Ethics,* February 2026. https://link.springer.com/article/10.1007/s43681-026-00986-8
