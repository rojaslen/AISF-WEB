---
title: "FAQ: Foreseeably Asked Questions"
parent: "Appendices"
nav_order: 2
---

# FAQ: Foreseeably Asked Questions

---

### "Why should I trust a solo developer with no institutional affiliation?"

Because I'm offering working software, documented results, and an open invitation to replicate. I'm not pretending that this is some industry or academic presentation, because it clearly isn't. It's one IT guy's offer of simple, independently developed client-side software that produces observable, documented improvement in AI session stability, with my after-the-fact interpretation of how and why it works. The software is freely downloadable, the methodology (such as it is) is documented, the training data exists, and the citations are traceable to established sources.

The unaffiliated origin is part of it. The observation that WCAG structure stabilizes AI behavior (due to its screen-reader-like interpretive reliance on content metadata) came directly from professional accessibility practice. Making that specific connection would be unlikely coming from perspectives that view accessibility as (at most) a compliance burden instead of a core requirement. Accessibility also inherently involves *making systems non-adversarial* by finding ways to make the thing accommodate the person, never the other way around.

Timestamping simply came from regular use, observation of AI model behavior, and a need for task tracking. The SaaS and ecosystem observations came from both personal and professional tech experience spanning decades. Hands-on practical knowledge has a place in the conversation, especially when client-side user safety is effectively absent from the research landscape.

### "Why PowerShell? Why Windows-only?"

Because of the KISS principle: "Keep It Simple, Stupid." The whole thing started out as a tool for my own personal use, developed in my spare time on my own Windows PC. PowerShell is preinstalled by default and immediately available. You can use it to build a basic accessible GUI (the main bulk of the core app's code) without any external dependencies, and a single .exe file doesn't need any installation, you just run it. And really, that simplicity is part of the argument. If the biggest roadblock to client-side AI safety is *taking it seriously* rather than *actually building it*, then what does that say about the industry?

The framework itself is platform, codebase and deployment-layer agnostic; it's not locked to PowerShell or Windows at all. The (in-progress) Firefox extension currently works in both Windows 11 and Debian Linux. AISF works in the Claude Code "system prompt" file (repo_root\.claude\CLAUDE.md). The model training is standard HuggingFace/PyTorch. The first app just happened to be Windows-specific because I needed a quick and easy tool I could use on my own computer.

### "Why is the timestamp UTC instead of local time?"

Because the timestamp isn't for you, it's for the AI. UTC is unambiguous and machine-authoritative. Its purpose is to anchor the session in real, verifiable linear time so the model knows where it is in the conversation's history and can correctly place any given turn relative to everything else. For that purpose, UTC is the only format that is always correct, everywhere, with no preconditions.

Local time requires the AI to know your timezone and whether Daylight Saving Time is in effect, and timezone abbreviations can be ambiguous. For example, "EST" can refer to at least three different time offsets depending on context, and "Eastern" in common usage could mean either UTC-5 or UTC-4 depending on the time of year. UTC is a global standard, Daylight Saving doesn't affect it and there's no conversion required.

### "If this is so simple, why hasn't anyone done it?"

Good question. NTP synchronization is trivial and WCAG-structured output is a well-known standard which is (in many cases) a routine corporate legal-compliance matter. Neither is complicated, but in order to do the simple thing, one must first think of the simple thing, and then decide that it's worth doing. Apparently the business model incentivizes other priorities. AISF's contribution isn't the relatively minor technical aspects, it's the explanation of why it works. Several established disciplines have independently examined precursors of it; synthesizing it all into a multidisciplinary model with the Four Laws and ready-to-use software is what makes the difference.

### "Why doesn't this cover hallucination detection?"

That was actually the original plan and I spent a lot of time mapping it out, but detection is a very thorny problem. You need to consider both unwanted deletions and expansions, so checking needs to be asymmetric, scanning both directions. However, content loss happens as a normal function of the context window's memory management, and text generation is simply what AIs do. Even assuming no unexpected losses or gains, how could any software detect the difference between the desired output and a hallucination? 

Without implausibly complex heuristics that would have to dynamically adapt to the user's input, detecting hallucinated context poisoning is impossible. Prevention sidesteps all of that, so I extracted the core principles of AISF from the detection engine and shelved the rest. Speaking of that shelf, the accessibility-only branch started out with an enterprise compliance and reporting approach that could be applied across the entire M365 enterprise tenant. That was set aside for lack of an Azure testing platform, leading to the much simpler CDA client app.

### "This is just prompt engineering."

Not quite. Prompt engineering is mostly about designing exquisitely detailed instructions for completion of a single task, ideally in a single turn. The AI Stability Framework operates at the session level, stabilizing an entire conversation rather than just a single turn. The distinction is between painstakingly optimizing a single output and stabilizing the environment that produces all output. Local LLM testing also demonstrated that it can be added both directly to a model's **Macro** training weights, and to the **Meso** platform's system prompt. That means it's layer-agnostic; it works at any point in the deployment stack. Prompt engineering can't say that. 

### "How is this different from system prompts?"

The system prompt is configured at the Meso platform layer, where the user typically can't operate. You have no way of knowing what's in it (unless you View Source and read the HTML and CSS) and it's beyond your reach to modify, so most of the time you're unaware that it even exists. Google's hidden persona injection (Chapter 2) is an invisible system prompt. AISF operation is a transparent, plaintext, device-only, user-driven process.

The AISF app works exclusively in the user message space on the user's device, which is the only point where users have any control. It can't override platform instructions from the chat input field and doesn't try; it just *adds* structural and behavioral rules that the AI incorporates along with everything else. On platforms with user-preference storage, those preferences are loaded as part of the initial session startup as a kind of "supplemental" to the system prompt. AISF works well with this architecture when it's available, and simulates it via direct input when it's not.

Anthropic's Claude Code (CLI) paid feature doesn't quite eliminate the intermediate Meso layer entirely, it instead turns that over to you. There is no vendor platform's unpredictable and inaccessible chat interface, no browser problems, no hidden instructions competing with yours. The client is whatever local application you choose to run it from, even a lowly CMD or PowerShell terminal. The locally-stored and user-editable CLAUDE.md file is the AI's instance's startup configuration; this is where you can set up a "system prompt" of your own. The "platform" in this scenario is your own computer: the system that spawns the AI instance inside your interactive client app of choice and applies a set of standing instructions.

The result of two-layer AISF mediation, observed in combined usage with the desktop app's timestamps only: virtually no platform-induced failures. The model used for the CLI add-on is the same version of Claude as on the web. But with two of the three deployment layers under user control, the dramatic reliability improvement is no accident. It's the AISF hypothesis run in reverse: when you eliminate "adversarial" from the deployment stack, stability improves by default.

### "Client-side injection sounds like a security vulnerability."

Yes, it does. In fact, per the Open Web Application Security Project's (OWASP) published guidelines for LLM development, any *user-directed behavioral customization that the operator didn't intend* is considered by definition to be an attack. The problem is that typing into the chatbox as intended is also literally "client-side injection," we just don't usually call it that. The "prompt engineering" response applies here too, because AISF demonstrably *works at any layer*, not just at the point of "injection." The Copilot Digital Accessibility (CDA) sub-branch was reviewed and approved for deployment by an enterprise IT Security team because the attack surface is effectively zero and the effect is beneficial.

AISF produces absolutely nothing you can't preview or type in manually yourself, it just saves you the time and keystrokes. The (in-progress) browser extension branch automates the same process for a more frictionless user experience. AISF doesn't store, edit, or intercept data at any point in the chain. It has no connectivity functions, it can't store data remotely, and it's designed not to need access to platform APIs for flexibility. User sovereignty means that all of its operations are performed only on the user's device because sovereignty also means privacy, which platforms have never taken seriously.

### "You barely mentioned sycophancy. Can the developers just train that out?"

The commonly suggested fixes like operator guardrails, compliance controls, and centralized governance don't touch the layer where sycophancy happens. A platform can quickly roll back a problematic model update, and still have a system that can't detect or control the behavior itself. Claude Code's locally-launched architecture demonstrates that applying anti-sycophancy rules can work at the Meso layer, on a non-adversarial platform. With an adversarial platform, client-side mediation is the only intervention that operates where the problem actually happens.

### "Won't the Four Laws cause the AI to amplify pre-existing mental health issues, if they make it follow user directions more reliably?"

It's possible, but that's due to a property of AI models, not of the framework. The model has no perception of the actual Human, only their input. The AI has zero access to the living person behind the text, with or without mediation. Plain text is an insufficient and inappropriate vehicle for any meaningful clinical intervention. The most an AI might do is detect user signaling, but only if the signal exists and it's been specifically trained for such detection.

### "The AI industry talks about 'compute' a lot, why do you barely even mention it?"

The word "compute" is primarily defined as a verb; it's not a noun in standard usage. The industry uses it as jargon to flatten the entire deployment stack into a single opaque term, and over time it's been normalized to the point where most people don't even notice anymore. This usage of "compute" elides hardware (GPUs, TPUs, ASICs, servers, networking), physical infrastructure (data centers, cooling systems, power supply, high-speed bandwidth), and software infrastructure (OS, virtualization, INFOSEC configuration, firmware). Compressing all of that into one word just makes it disappear into unthinking Newspeak.[^F.1]

The stack's resulting invisibility means the client layer (the only part of the whole thing that's directly available to users) is consistently absent from AI discourse, and its absence mostly goes unnoticed. Accessibility suffers as a direct result, with AI platforms routinely failing ADA, §508, and WCAG compliance requirements because the inconvenient user-facing part of the deal has vanished into "compute." If the entire industry's mental model stops at the SaaS platform layer, it will invariably miss client-side stability failures, not to mention the accessibility failures that affect disabled users every time they try to use these tools. When industry vocabulary doesn't even describe the deployment stack, diagnosing what goes wrong within that stack is unlikely.
 
### "Why is an anti-hallucination tool talking about Texas power grids?"

Because any serious discussion of AI has to account for the physical infrastructure behind it. The AI instance exists in a virtual void, but the data centers that run it don't. Compare "negligible deployment footprint" to "400+ new data centers in Texas alone," and the reason is clear.

Using the IEA's figure of approximately 415 TWh of global data center electricity consumption in 2024 as a baseline, and applying a conservative 20% AI inference share estimate, a 33% reduction in AI inference cycles would conserve on the order of 27 TWh per year, which is roughly enough to power every home in Los Angeles plus most of Chicago. At the industry-average Water Usage Effectiveness (WUE) of about 1.8 liters per kWh [^F.2], that same reduction translates to around 48.6 billion liters of water annually. That's the equivalent of 39,600 Olympic-sized swimming pools, or southwest Ohio's Caesar Creek Lake [^F.3].

AISF-trained Instruct models across three of four independently tested architectures all featured reduced output verbosity, with consistent direction and a measured range of 37.9% to 71.8% fewer words per response than their baselines. *Fewer tokens per turn is a measurable proxy for reduced resource consumption per task*. The full token delta analysis is in Appendix 2.

### "Won't the platforms just block it?"

Yes, they probably could. A platform operator could scan for, detect and strip out any pre-formatted AISF data from user inputs or censor it as a forbidden topic; it's easy enough to spot. But consider the optics of doing so: they would be choosing to proactively deny accessibility requests (*ADA & §508 regulatory compliance*), timestamps (user's content-neutral task history), and behavioral guidelines (stable & reliable = increased user satisfaction & engagement).

Are platforms that are already legally required to provide accessibility compliance likely to do such a thing? Are timestamps harmful? Blocking AISF would also be counterproductive since it measurably improves performance. Doing so would mean they've decided that poor performance is a price worth paying for maintaining control over your session. Is that good marketing copy?

Another consideration is that some platforms offer sufficient user preferences storage, and AISF principles can easily be placed there. The question is how effective or reliable that can be at the platform layer, with adversarial Zero Trust architecture also in place. Whether those preferences effectively propagate to other input surfaces or only to the one where they're entered is another issue, because in some cases they don't (e.g. Anthropic's Claude.ai website vs the dedicated iOS app).

And simply as a practical matter, AISF's workflow is indistinguishable from a user manually typing out content in any external editor and then copy-pasting it into the AI chatbox, because that's exactly what it is. *Presence in context is sufficient.* Short of blocking users from requesting output formatted or processed in a particular way — which would break normal usage — there's no clean way to filter it.

### "Does it break when the context window fills up?"

Eventually, yes. Context windows have limitations, and there's nothing you can do about that client-side. That's why periodic refreshing is part of the workflow. The desktop app's recommended cycle is Structure + Stabilize every 90-120 minutes. The browser extension is designed to automate this based on a token-usage metric instead, but clock time is sufficient for ordinary use. 

Context decay is real and noticeable but manageable. Using STRUCTURE and STABILIZE is a bit like occasionally saving a document you're working on, rather than trusting that nothing will crash. Context decay even provides evidence for the framework's premise: if AI behavior noticeably changes as AISF anchoring is evicted from context, that confirms the anchoring was doing something. The degradation curve is the control.

---

[^F.1]: Orwell, G., Nineteen Eighty‑Four, appendix, "The Principles of Newspeak" (London: Secker & Warburg, 1949). *"Newspeak was designed not to extend but to diminish the range of thought...The grammar of Newspeak had two outstanding peculiarities. The first of these was an almost complete interchangeability between different parts of speech."*

[^F.2]: AKCP. "Data Center Water Usage Effectiveness (WUE)." 2021. https://www.akcp.com/index.php/2021/01/14/data-center-water-usage-effectiveness-wue/

[^F.3]: FisherMap. "Caesar Creek Lake, OH -- Depth Map." https://usa.fishermap.org/depth-map/caesar-creek-lake-oh/

