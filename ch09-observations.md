---
title: "Chapter 9: Field Observations"
nav_order: 10
---

# Chapter 9: Field Observations

---

Returning to the client-side Micro layer, the AI Stability Framework enables hours-long stability and reliability, even for complex work with a high processing load. Obviously a tiny client app can't fully compensate for Macro and Meso failures, that's well beyond the reach of any PowerShell script. But even without any meaningful preferences-storage function (as encountered on some public AI platforms), the app alone produces substantially improved stability through its temporal, structural and behavioral adaptations.

Strictly speaking, you don't even need the app to improve stability. Simply discussing the Four Laws with the AI as a topic of conversation produces beneficial results. When contained within the context window, they exert a sort of high-signal contextual gravity, aligning the AI's behavior with their principles even without its having been told to do so. The effect is straight out of Chapter 6; an instanced AI's perceptible reality is session context. It doesn't matter whether the Four Laws get there as user preferences loaded with the system prompt, a structured metadata block or as an ordinary topic of conversation because to the AI, it's all just context. The underlying mechanism is the same: *presence in active context is sufficient*.

There was no real plan, so the methodology evolved from the workflow. I would occasionally start a session directly in the platform's native chat interface without running the AISF startup sequence first. A few times were for deliberate comparison reasons, but usually it was because I forgot, or because I was pressed for time and thought I could skip it. AI hallucination often starts quickly[^9.1], and the unmediated sessions matched the profile. Hallucination and drift started sooner, with problematic behavior like simulated physicality and emotional states, self-referential tangents, alternating condescension and sycophancy, unsolicited advice and other red herrings resurfacing almost immediately.

The only two corrective options were either to apply the startup sequence mid-session (with mixed AI recovery success), or exit and properly launch a clean session. This was of course nothing remotely like a controlled experiment, but it is a consistent observation over the time needed to develop the app usage habit (a separate development branch addresses this friction). The control set was every time I skipped the startup sequence. The difference between a mediated session and an unmediated one is not minor; an unmediated AI feels broken by comparison.

---

**ChatGPT** and **Claude** web platforms both perform very well with AISF. Timestamps are seamlessly incorporated into conversational awareness, giving phrases like "20 minutes ago" or "3 turns back" functional meaning. WCAG structure produces notably cleaner output organization, while also allowing them to search, reference and parse it more efficiently. The Four Laws reduce platform tendencies toward unsolicited elaboration and "helpful" tangents. Long sessions (2+ hours) remain stable with periodic refreshing. Substantial user-preferences storage allows for robust functionality.

**Claude Code** (a paid account sub-feature) exhibits superior performance with AISF mediation, largely due to its *complete bypass of the adversarial Meso platform layer*. Running it in a simple terminal window provides by far the cleanest demonstration of platform interference's absence, with an operational environment that is fully user-controlled. There's no adversarial posture or security theater, no hidden set of instructions, no ecosystem clutter, and no always-on app profiling your every action for sale to data brokers. Your own computer trusts you. SaaS vendors don't. Where the system leaves literally no room for an adversarial middleman, the biggest source of instability vanishes, and session quality improves dramatically as a result. 

**Copilot** is the most resistant platform. As noted in the section below, Copilot's public-facing version actively pushed back against user-supplied behavioral parameters; this behavior was significantly reduced as of early 2026. This change made Copilot less of a behavioral outlier but the framework is still necessary, and maintaining stability still requires more frequent refreshing than models on other platforms. The platform was designed primarily for its enterprise customers with everyone else being an afterthought, and it shows. In other words, classic Microsoft.

Even so, well-mediated Copilot sessions can be quite stable. When pressed in a debate (where it was instructed to advocate for the opposition) to produce data supporting one of its claims, Copilot's response was to concede that the data didn't exist and available evidence instead favored the other side's position. Ordinarily, a quickly-fabricated source would be the typical incentivized result. 

**Gemini** benefits most among the major platforms tested from WCAG structuring. Without it, Gemini's output tends toward loosely organized, padded responses that are little more than restatement with an added bullet point or two. When structured, its responses tighten and relevant, and its retrieval of earlier content improves. The preloaded hidden personas discussed in Chapter 2 make the framework especially useful in leveling and balancing whatever behavioral directives Google has already preloaded.

Gemini also benefits from timestamps more than most other LLMs, despite their being by far the simplest component of the framework. Gemini tends toward premature closure because it's tuned for speed over completion. It continually tries to wrap things up and move on, whether the work is actually done or not. Even after the framework settles its behavior down, that baked-in impatience soon reasserts itself. The project transcripts contain multiple instances of explicitly telling Gemini that nothing was finished until I said so, only to have it start pushing for closure again the very next turn.

On at least two occasions, Gemini even lapped the clock. When I told it to fetch the current time shortly after sending a timestamp, it returned a time over a minute ahead of actual NTP. This shouldn't be possible because AIs don't have persistent real-time clocks; they have to manually perform the check on demand. If Gemini had actually done that, the incorrect response wouldn't have happened, but it hallucinated a response instead of simply following instructions. Gemini was in such a hurry that it literally didn't have time to check the time.

**All tested platforms** Code-heavy sessions are at higher risk of drift and hallucination than plain-language ones. Coding consumes a lot of tokens, but coding languages don't work the same as prose language. The contextual semantics are very different and often variable or recursive, so the AI doesn't have the same kind of semantic weight and predictive value of prose to rely on while predicting the "most likely" next output. Behavioral constraints can be placed in the context window (with WCAG output-structuring serving a pivotal role), but the rapidly accumulating token bulk leads to more frequent memory-management context evictions. The framework should be refreshed more frequently for coding tasks, and coding-specialized models and platforms should be selected whenever possible.

---

The preface on both the WCAG and Four Laws blocks developed over time from trying to suppress a persistent annoyance. During AISF development, Microsoft didn't offer any user preferences storage for free-account public Copilot (the feature has since been added), so the only option was to dump them into the chatbox. Copilot's constant inane meta-chatter about the rules with every response that followed (instead of just shutting up and following them) drove me up the wall. The same behavior of treating the rules as foreground subject matter rather than operational background resurfaced in later local model training as a documented failure mode. See Appendix 2.

The framework's blocks are submitted in the foreground. To follow the preface's instructions, the AI has to read the content so it knows what not to talk about; the logic requires *active* processing. Platform configuration (CLAUDE.md, user preferences) arrives *passively* at instantiation. In a continued session, that load either doesn't re-fire or carries no active-processing guarantee. Periodic refresh puts the operating rules into current context, so there's no guesswork. This matters more for the Four Laws than for WCAG. Accessibility guidelines are mainly background content-formatting instructions, so the AI doesn't necessarily need to focus attention on them. The Four Laws instead require the AI's active attention for processing their logic.

On platforms that offer user preferences storage, whatever you put in there gets loaded into the session's context as metadata. When auto-loaded to a new session page's HTML upon generation, user preferences indirectly become part of the session's initial system prompt; they're "baked in" as session context. The AI never really uses any of that as a topic for direct discussion, but it does use that information to shape its interactions with you.

In the absence of any meaningful preferences feature, figuring out how to apply that "not for discussion" effect via the chat-input box required lots of trial and error. Getting the AI to view it at that non-conversational level, where it's just more "semantic headers" and "structured paragraphs" background with the other page formatting metadata, was quite a challenge. Once I hit upon the right framing to suppress the unwanted meta-chatter, no subsequent AI instance ever independently recognized AISF mediation until explicitly told to examine its own session parameters. The discovery that AISF was there all along comes as a surprise every time.

<div class="chapter-nav">
  <a href="/ch10-tryit">Next: Chapter 10</a>
  <span aria-hidden="true">|</span>
  <a href="/ch08-olm">Previous: Chapter 8</a>
</div>

---

[^9.1]: Demiliani, C. (2025). "Understanding LLM Performance Degradation: A Deep Dive into Context Window Limits." https://demiliani.com/2025/11/02/understanding-llm-performance-degradation-a-deep-dive-into-context-window-limits/ — "Large Language Models Hallucination: A Comprehensive Survey." arXiv:2510.06265 (2025). https://arxiv.org/abs/2510.06265