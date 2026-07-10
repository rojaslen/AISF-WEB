---
title: "Epilogue: Foreseeably Asked Questions"
nav_order: 13
---

# FAQ: Foreseeably Asked Questions

<style>
main ol > li > p:first-child > strong { font-size: 1.4rem; }
main ol > li::marker { font-size: 1.4rem; font-weight: 700; }
.faq-nav li::marker { font-size: inherit; font-weight: normal; }
</style>

---

<nav aria-label="FAQ navigation">
<ol class="faq-nav">
<li><a href="#faq1">Is this what people want?</a></li>
<li><a href="#faq2">Why believe some nobody?</a></li>
<li><a href="#faq3">Windows PowerShell? Seriously?</a></li>
<li><a href="#faq4">Why not local time?</a></li>
<li><a href="#faq5">If it's so simple, why not just do it?</a></li>
<li><a href="#faq6">Shouldn't it be doing detection?</a></li>
<li><a href="#faq7">Is this the same thing as prompt engineering?</a></li>
<li><a href="#faq8">Is this any different from a system prompt?</a></li>
<li><a href="#faq9">Is this an IT security exploit?</a></li>
<li><a href="#faq10">What about AI sycophancy?</a></li>
<li><a href="#faq11">What's the risk of 'AI psychosis?'</a></li>
<li><a href="#faq12">Why no mention of compute?</a></li>
<li><a href="#faq13">Why mention Texas power grids?</a></li>
<li><a href="#faq14">Won't platforms block it?</a></li>
<li><a href="#faq15">Does it break in long sessions?</a></li>
</ol>
</nav>

---

1. <a name="faq1"></a>**"Is any of this really what people want from AI, or is it just your opinion?"**

    Anthropic's first Public Record survey, roughly 52,000 Americans with YouGov fieldwork in late 2025, was [published](https://www.anthropic.com/news/anthropic-public-record){: target="_blank" rel="noopener noreferrer" } on June 12, 2026.[^Fd] This project substantially predates that survey, and it turns out that the priorities people ranked highest for AI lined up, almost item for item, with what I was already working on.

    At #2 on the list is **helping people with disabilities** (36%), and the Framework enforces accessibility in the AI's output, with the Copilot Digital Accessibility tool already finished, security-reviewed, validated by a blind screen-reader (JAWS) user in testing, and later deployed to multiple users for active production work. **Privacy** is the single thing most people want government to act on (56%), and the Framework runs entirely on your own device and sends nothing anywhere. **Child safety** is close behind (52%), which is exactly what the child-safe model work is about.

    Only 15% of Americans trust AI companies to make these kinds of decisions (the lowest score of any group) while 43% trust independent experts, the highest. Of course, none of this poll data means the public has ever even heard of this project, much less endorsed it. It means that the specific problems I was already targeting are problems a broad cross-section of people already say they care about. My opinion has no bearing on that.

2. <a name="faq2"></a>**"Why should I pay any attention to some nobody with no backing?"**

    Because I'm offering explanatory theory, working software, documented results, and an open invitation to replicate. I'm not pretending that this is some industry or academic presentation, because it clearly isn't. It's one IT guy's offer of simple, independently developed client-side software that produces observable, documented improvement in AI session stability, with my after-the-fact interpretation of how and why it works. The software is freely downloadable, the methodology is documented, the training data exists, and the citations are traceable to relevant, established sources.

    The observation that WCAG structure stabilizes AI behavior (due to its screen-reader-like interpretive reliance on content metadata) came directly from professional accessibility practice. Making that specific connection would be implausible (bordering on impossible) coming from perspectives that view accessibility as at best a costly compliance burden instead of a core principle. Accessibility also inherently involves making systems non-adversarial by finding ways to make the thing accommodate the person, never the other way around.

    Timestamping simply came from experimentation (eventually regular use), observation of AI model behavior, and a need for task tracking. The SaaS and ecosystem observations came from both personal and professional tech experience spanning decades. Hands-on practical knowledge has a place in the conversation, especially when client-side user safety is effectively absent from the research landscape.

3. <a name="faq3"></a>**"Why Windows-only PowerShell?"**

    Because of the KISS principle: "Keep It Simple, Stupid." The whole thing started out as a tool for my own use, developed in my spare time on my own Windows PC. PowerShell is preinstalled by default and immediately available. You can use it to build a basic accessible GUI (the main bulk of the CORE app's code) without any external dependencies, and a single .exe file doesn't need any installation, you just run it. And really, that simplicity is part of the argument. If the biggest roadblock to client-side AI safety is *taking it seriously* rather than actually *building it*, then what does that say about the industry?

    The Framework itself is platform, codebase and deployment-layer agnostic; it's not locked to PowerShell, Windows or the client layer at all. The Firefox extension is available for download, and currently works in both Windows 11 and Debian Linux. It works in the Claude Code "system prompt" file (repo_root\.claude\CLAUDE.md). The model training is standard HuggingFace/PyTorch. The first app just happened to be Windows-specific; after an OS migration I ported it to Python/PyQt6 so now it can run on Debian too. From Linux, Android and iOS are only a short step away.

4. <a name="faq4"></a>**"Why doesn't the timestamp show my local time? Why does it have a Z?"**

    The timestamp isn't really for you, it's for the AI. Coordinated Universal Time (UTC, aka GMT or Z) is an unambiguous and machine-authoritative global standard. Its purpose is to anchor the session in real, verifiable linear time so the model knows where it is in the conversation's history and can correctly sequence any given turn relative to everything else. For that purpose, UTC is the only format that is always correct, anywhere on the planet, with no variables or preconditions.

5. <a name="faq5"></a>**"If this is so simple, why hasn't anyone already done it?"**

    Good question. NTP synchronization is trivial and WCAG-structured output is a well-known standard which is (in many cases) a routine corporate legal-compliance matter. Neither is complicated, but in order to do the simple thing, one must first think of the simple thing, and then decide that it's worth doing. Apparently the business model incentivizes other priorities. The Framework's contribution isn't its relatively minor technical aspects, the important part is the theory behind it. Several established disciplines have independently examined precursors of it; synthesizing it all into a multidisciplinary model is what made the difference.

6. <a name="faq6"></a>**"Why doesn't this cover hallucination detection?"**

    That was actually the original plan and I spent a lot of time mapping it out, but detection is a very thorny problem. You need to consider both unwanted deletions and expansions, so checking needs to be asymmetric, scanning both directions. However, content loss happens as a normal function of the context window's memory management, and text generation is simply what LLMs do.

    And even then, assuming no unexpected losses or gains, how could any software detect the difference between the desired output and a hallucination? No matter how implausibly complex, any heuristics would have to dynamically adapt to the user's intent and fact-check every sentence against verifiable external sources. This magic software would also have to somehow do all of this additional processing without increasing costs that are too high already. Computerized mind-reading is not a thing but electrical engineering is, so the magic software is impossible.

    Prevention sidesteps all of that, so I extracted the core principles of the AI Stability Framework from the detection pipeline and shelved the engine itself. That detection engine was the only part that couldn't adapt to the environmental pressure. The adaptive traits like session state evaluation, compliance drift monitoring, domain classification, behavioral intervention sequencing, survived and propagated.

7. <a name="faq7"></a>**"Is this the same thing as prompt engineering?"**

    Not quite. Prompt engineering is mostly about designing exquisitely detailed instructions for completion of a single task, ideally in a single turn. The AI Stability Framework operates at the session level, stabilizing an entire conversation rather than just a single turn. The distinction is between painstakingly optimizing a single output and stabilizing the environment that produces all output. Local LLM testing also demonstrated that it can be added both directly to a model's **Macro** training weights, and to the **Meso** platform's system prompt. That means it's layer-agnostic; it works at any point in the deployment stack. Prompt engineering can't say that.

8. <a name="faq8"></a>**"Is this any different from a system prompt?"**

    The system prompt is configured at the Meso platform layer, where the user typically can't operate. You have no way of knowing what's in it (unless you View Source and read the HTML and CSS) and it's beyond your reach to modify, so most of the time you're unaware that it even exists. Google's background persona injection (Chapter 2) is an element of such an invisible system prompt.

    The Framework's apps work exclusively in the user message space on the user's device, which is the only point where users have any agency. It can't override platform instructions from the chat input field and doesn't try; it just *adds* benign structural and behavioral rules that the AI incorporates along with everything else. On platforms with user-preference storage, those preferences are loaded as part of the initial session startup as a kind of "supplemental" to the system prompt. the Framework works well with this architecture when it's available, and simulates it via direct input when it's not.

    Anthropic's Claude Code (CLI) paid feature doesn't quite eliminate the intermediate Meso layer entirely, it instead turns that over to you. There is no vendor platform's unpredictable and inaccessible chat interface, no browser problems, no hidden instructions competing with yours. The client is whatever local application you choose to run it from, even a simple PowerShell or bash terminal. The locally-stored and user-editable CLAUDE.md file is the AI instance's startup configuration; this is where you can set up a "system prompt" of your own. The "platform" in this scenario is your own computer: the system that spawns the AI instance inside your interactive client app of choice and applies a set of standing session instructions.

    The result of two-layer Framework mediation, observed in combined usage with the desktop app's timestamps only: very few platform-induced failures (see April-June 2026 notes). The model used for the CLI add-on is the same version of Claude as on the web. With two of the three deployment layers under user control, the reliability improvement is no accident. It's the Framework hypothesis run in reverse: when you eliminate "adversarial" from the deployment stack, stability improves by default.

9. <a name="faq9"></a>**"Client-side injection seems like a security vulnerability."**

    Whose security? Per the Open Web Application Security Project's (OWASP) published guidelines for LLM development, any user-directed behavioral customization that the operator didn't intend is considered by definition to be an attack. The problem is that telling the AI to stop using em dashes and THIS NOT THAT phrasing is exactly that: *a user-directed behavioral customization that the operator didn't intend.* Typing into the chatbox is literally *client-side injection*, we just don't usually call it that. The "prompt engineering" response applies here too, because the Framework is demonstrably effective at any deployment layer, not just at the point of "injection."

10. <a name="faq10"></a>**"You barely mentioned sycophancy. Can the developers just train that out?"**

    The commonly suggested fixes like operator guardrails, compliance controls, and centralized governance don't reach the layer where sycophancy happens. A platform can quickly roll back a problematic model update, but still have a system that can't detect or control the problem. That's because it's happening at the external client end which they barely acknowledge and can't meaningfully monitor.

    Reducing the problem's occurrence is certainly possible, but at present there is no clear path to competely eliminating the problem. The Claude Code app's locally-configurable system prompt architecture demonstrates that applying anti-sycophancy rules can effectively minimize the problem at the Meso layer, with a non-adversarial platform. With an adversarial external platform, client-side AI mediation is the only intervention that can operate where the problem manifests, but the scope of that intervention is necessarily limited.

11. <a name="faq11"></a>**"Won't this make 'AI psychosis' worse?"**

    It's possible, but that's due to a property of AI models, not of the Framework. The model has no perception of the actual Human, only their input. The AI has zero access to the living person behind the text, with or without mediation. Plain text is an insufficient and inappropriate vehicle for any meaningful clinical intervention. The most an AI might do is detect user signaling, but only if the signal exists *and* it's been specifically trained for such detection.

12. <a name="faq12"></a>**"The AI industry talks about 'compute' all the time, why don't you?"**

    The word "compute" is primarily defined as a verb *(1<sup>st</sup> person sing., infin.)*. The word is not a noun in standard usage. The industry uses it as jargon to flatten the entire deployment stack into a single opaque term. It compresses hardware (GPUs, TPUs, ASICs, servers, networking), physical infrastructure (data centers, cooling systems, power supply, high-speed bandwidth), and software infrastructure (OS, virtualization, INFOSEC configuration, firmware) into two syllables. This usage of "compute" makes the whole stack disappear into literal Newspeak[^Fa].

    The client layer is the most direct casualty. The only part of the entire stack that's directly available to users gets flattened right alongside everything else. Its absence from AI discussions goes unnoticed, because the inconvenient user-facing part of the deal has vanished into "compute."

    If the industry's entire mental model stops at the (supply-side) SaaS platform layer, it will invariably miss demand-side (client) stability failures on every transaction, not to mention the accessibility failures affecting disabled users every time they try to use these potentially-empowering tools.

13. <a name="faq13"></a>**"What does this have to do with Texas power grids?"**

    Any honest discussion of AI has to account for the infrastructure that runs it. The AI instance exists in a stateless void, but the data centers that run it don't. Compare a negligible software-deployment footprint to 400+ data centers in Texas alone, and the reason should be clear.

    Let's use the IEA's figure of ~415 TWh (TeraWatt hours) of global data center electricity consumption in 2024 as a baseline. If we attribute 20% of that total data center load specifically to AI, then a 33% reduction in token burn would save around 27 TWh a year, which is roughly enough to power every home in Los Angeles and half of Chicago.

    The industry-average Water Usage Effectiveness (WUE) for data center cooling is about 1.8 liters per kWh[^Fb]. That works out to a usage reduction of around 48.6 billion liters of water a year. That's ~39,600 Olympic-sized swimming pools or one Caesar Creek Lake,[^Fc] which can be found on maps of southwest Ohio.

    Almost all Framework-trained models featured reduced output verbosity, with a measured range of 35.4% to 71.8% fewer words per response than the untrained base models (most clustering around 40%, see Appendix 2, §7.5). Fewer words means fewer tokens, which means fewer GPU cycles, which means fewer resources are required to process those tokens.

14. <a name="faq14"></a>**"Won't the platforms just block it?"**

    They certainly can, even if unintentionally. Media reporting from March and April 2026 documented cost-containment measures across all major AI platforms, in response to escalating energy costs, increased usage, supply constraints and other factors. OpenAI reset Codex usage limits after reaching 3 million weekly users and shifted to pay-as-you-go pricing. Anthropic confirmed it has been "adjusting" Claude usage limits, with demand hitting capacity "way faster than expected." Google introduced billing caps on the Gemini API beginning April 2026. Microsoft restructured Copilot access with *behavioral changes* taking effect on US Tax Day, April 15, 2026. Make of that what you will.

    Conditions varied widely across platforms. Performance on Claude.ai was the least degraded, with persistent user preferences being applied largely intact and no observed mid-session downgrades. However, usage limits were sharply curtailed across Anthropic's offerings, particularly during prime usage hours. After its behavioral changes were applied, Copilot's resistance to user direction increased, but was manageable with additional prompting and stabilization. OpenAI's ChatGPT was severely degraded with tool-use throttled, web-fetch operations unreliable and like Anthropic, sharply curtailed session-usage limits. Google Gemini was more problematic than usual, with its typical speed-driven failures accelerated further, and compounded by session behavior that didn't reliably stabilize.

    The Framework didn't change and neither did the models, all of that was platform effects. The difference was how much friction existed between the user and the model. The only one that didn't destabilize was Claude Code (usage limits still applied). There, the user controls both the platform and the user interface, illustrating one of the Framework's main arguments: where the system is non-adversarial, stability improves by default. Platform failures of this type demonstrate the unintended flaw in SaaS Zero-Trust's adversarial posture for this use case.

    *Deliberately* blocking the Framework is a different question. A platform operator could scan for, detect and strip out its pre-formatted data from user inputs or censor it as a forbidden topic; it's easy enough to spot. But consider: they would be choosing to proactively deny accessibility requests *(ADA & §508 regulatory compliance)*, timestamps *(innocuous, content-neutral task history)*, and behavioral guidelines *(stable & reliable = increased user satisfaction & engagement)*. Corporations already drawing scrutiny for a wide range of issues are unlikely to also publicly block such requests.

    During testing, most platforms had some version of the Framework stored in account preferences; Copilot was the exception (the feature appeared briefly, then Microsoft removed it). When a platform goes fully adversarial whether intentionally or as a side effect of other measures as indicated above, those stored preferences are effectively ignored by the platform. That leaves only Micro injection via the chat input, and there is a hard ceiling on what client-side mediation can accomplish when the platform is actively working against it.

    But simply as a practical matter, the client-side workflow is indistinguishable from a user manually typing out plain text in any external editor and then copy-pasting it into the AI chatbox, because that's exactly what it is (as discussed in the "security vulnerability" item above). Short of blocking users from requesting output formatted or processed in a particular way (which would break ordinary usage), there's no clean way to filter it. However, platform-level service changes certainly can render client-side interventions ineffective.

15. <a name="faq15"></a>**"Does it break when the context window fills up?"**

    Eventually, yes. Context windows have structural limitations, and there's nothing you can do about that. That's why periodic refreshing is part of the workflow. The legacy version of the desktop app recommended a manual cycle of Stabilize + Structure every 90-120 minutes. The current version automates this to every 10 and 20 turns. The browser extension uses refresh intervals based on a token-usage metric instead, but clock time is sufficient for light use.

    Context decay is real and noticeable but manageable. Using STABILIZE and STRUCTURE is a bit like occasionally saving a document you're working on, rather than trusting that nothing will crash. Context decay even provides evidence for the Framework's premise: if AI behavior noticeably changes as its anchoring is evicted from context, that confirms the anchoring was doing something. The degradation curve is the control.

---

Supporting research, technical detail, and downloadable software are in the appendices.

<nav>
<div class="chapter-nav">
  <a href="/appendices">Next: Appendices</a>
  <a href="/ch11">Previous: Chapter 11</a>
</div>
</nav>

[^Fa]: Orwell, G., Nineteen Eighty‑Four, appendix, "The Principles of Newspeak" (London: Secker & Warburg, 1949). *"Newspeak was designed not to extend but to diminish the range of thought...The grammar of Newspeak had two outstanding peculiarities. The first of these was an almost complete interchangeability between different parts of speech."*

[^Fb]: AKCP. "Data Center Water Usage Effectiveness (WUE)." 2021. [https://www.akcp.com/index.php/2021/01/14/data-center-water-usage-effectiveness-wue/](https://www.akcp.com/index.php/2021/01/14/data-center-water-usage-effectiveness-wue/){: target="_blank" rel="noopener noreferrer" }

[^Fc]: FisherMap. "Caesar Creek Lake, OH -- Depth Map." [https://usa.fishermap.org/depth-map/caesar-creek-lake-oh/](https://usa.fishermap.org/depth-map/caesar-creek-lake-oh/){: target="_blank" rel="noopener noreferrer" }

[^Fd]: Anthropic. "Results from first Anthropic Public Record." 2025. [https://www.anthropic.com/news/anthropic-public-record](https://www.anthropic.com/news/anthropic-public-record){: target="_blank" rel="noopener noreferrer" } Nationally representative online survey of 51,993 U.S. adults (16+); fieldwork by YouGov, November 1 to December 11, 2025; weighted to U.S. Census benchmarks.

