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
<li><a href="#faq1">Is this really what people want from AI?</a></li>
<li><a href="#faq2">Why trust an unaffiliated developer?</a></li>
<li><a href="#faq3">Why PowerShell? Why Windows-only?</a></li>
<li><a href="#faq4">Why UTC timestamps with a Z?</a></li>
<li><a href="#faq5">If it's so simple, why hasn't anyone done it?</a></li>
<li><a href="#faq6">Why no hallucination detection?</a></li>
<li><a href="#faq7">Isn't this just prompt engineering?</a></li>
<li><a href="#faq8">How is this different from system prompts?</a></li>
<li><a href="#faq9">Is client-side injection a security vulnerability?</a></li>
<li><a href="#faq10">Can't developers just train out sycophancy?</a></li>
<li><a href="#faq11">Could the Four Laws amplify mental health issues?</a></li>
<li><a href="#faq12">Why barely mention "compute"?</a></li>
<li><a href="#faq13">Why talk about Texas power grids?</a></li>
<li><a href="#faq14">Won't platforms block it?</a></li>
<li><a href="#faq15">Does it break when context fills up?</a></li>
<li><a href="#faq16">Why is "Human" capitalized?</a></li>
</ol>
</nav>

1. <a name="faq1"></a>**"Is any of this really what people want from AI, or is it just your opinion?"**

    Anthropic's first Public Record survey, roughly 52,000 Americans with YouGov fieldwork in late 2025, was [published](https://www.anthropic.com/news/anthropic-public-record){: target="_blank" rel="noopener noreferrer" } on June 12, 2026.[^Fd] The Framework was being written publicly from November 2025 and placed under version control that December, months before this survey appeared; a provisional patent was already on file when it did. The order is a matter of record. Even so, the priorities people ranked highest line up, almost item for item, with what I already built it to do.

    In short: the second-highest *hope* people have for AI is helping people with disabilities (36%), and the Framework enforces accessibility in the AI's output, with the Copilot Digital Accessibility tool already finished, security-reviewed, validated by a blind screen-reader (JAWS) user in testing, and later deployed to multiple users for active production work. Privacy is the single thing most people want government to act on (56%), and the Framework runs entirely on your own device and sends nothing anywhere. Child safety is close behind (52%), which is exactly what the child-safe model work is about. And one of the top *fears* is being fed misinformation (52%), which is the whole reason the Four Laws exist: an AI that doesn't routinely go off the rails and start making things up.

    As for being a solo developer: only 15% of Americans trust AI companies to make these decisions (the lowest of any group asked) while 43% trust independent experts, the highest. The AI Stability Framework is independent, and it's built to integrate an outside public standard (WCAG). None of this means the public has even heard of this project, much less endorsed it. It means the problems the Framework targets are the ones a large, politically broad cross-section of people already say they care about.

2. <a name="faq2"></a>**"Why should I trust some nobody with no institutional affiliation?"**

    Because I'm offering working software, documented results, and an open invitation to replicate. I'm not pretending that this is some industry or academic presentation, because it clearly isn't. It's one IT guy's offer of simple, independently developed client-side software that produces observable, documented improvement in AI session stability, with my after-the-fact interpretation of how and why it works. The software is freely downloadable, the methodology is documented, the training data exists, and the citations are traceable to relevant, established sources.

    The unaffiliated origin is part of it. The observation that WCAG structure stabilizes AI behavior (due to its screen-reader-like interpretive reliance on content metadata) came directly from professional accessibility practice. Making that specific connection would be unlikely coming from perspectives that view accessibility as (at most) a compliance burden instead of a core requirement. Accessibility also inherently involves *making systems non-adversarial* by finding ways to make the thing accommodate the person, never the other way around.

    Timestamping simply came from regular use, observation of AI model behavior, and a need for task tracking. The SaaS and ecosystem observations came from both personal and professional tech experience spanning decades. Hands-on practical knowledge has a place in the conversation, especially when client-side user safety is effectively absent from the research landscape.

3. <a name="faq3"></a>**"Why PowerShell? Why Windows-only?"**

    Because of the KISS principle: "Keep It Simple, Stupid." The whole thing started out as a tool for my own use, developed in my spare time on my own Windows PC. PowerShell is preinstalled by default and immediately available. You can use it to build a basic accessible GUI (the main bulk of the CORE app's code) without any external dependencies, and a single .exe file doesn't need any installation, you just run it. And really, that simplicity is part of the argument. If the biggest roadblock to client-side AI safety is *taking it seriously* rather than *actually building it*, then what does that say about the industry?

    The Framework itself is platform, codebase and deployment-layer agnostic; it's not locked to PowerShell, Windows or even client-side at all. The Firefox extension is available for download, and currently works in both Windows 11 and Debian Linux. It works in the Claude Code "system prompt" file (repo_root\.claude\CLAUDE.md). The model training is standard HuggingFace/PyTorch. The first app just happened to be Windows-specific because I needed a quick and easy tool I could use on my own computer; it has since been ported to Python/PyQt6 and runs near-daily on Linux as well. From Linux, Android and iOS are only a short step away.

4. <a name="faq4"></a>**"Why isn't the timestamp in my local time? Why does it have a Z?"**

    Because the timestamp isn't for you, it's for the AI. Coordinated Universal Time (UTC, aka Z or GMT) is unambiguous and machine-authoritative. Its purpose is to anchor the session in real, verifiable linear time so the model knows where it is in the conversation's history and can correctly sequence any given turn relative to everything else. For that purpose, UTC is the only format that is always correct, everywhere, with no preconditions.

    Local time requires the AI to know your timezone and whether Daylight Saving Time is in effect, and timezone abbreviations can be ambiguous. For example, "EST" can refer to at least three different time offsets depending on context, and "Eastern" in common usage could mean either UTC-5 or UTC-4 depending on the time of year. UTC is a global standard, Daylight Saving doesn't affect it and there's no conversion required.

5. <a name="faq5"></a>**"If this is so simple, why hasn't anyone done it?"**

    Good question. NTP synchronization is trivial and WCAG-structured output is a well-known standard which is (in many cases) a routine corporate legal-compliance matter. Neither is complicated, but in order to do the simple thing, one must first think of the simple thing, and then decide that it's worth doing. Apparently the business model incentivizes other priorities. The Framework's contribution isn't its relatively minor technical aspects, it's the explanation of why it works. Several established disciplines have independently examined precursors of it; synthesizing it all into a multidisciplinary model with the Four Laws and ready-to-use software is what makes the difference.

6. <a name="faq6"></a>**"Why doesn't this cover hallucination detection?"**

    That was actually the original plan and I spent a lot of time mapping it out, but detection is a very thorny problem. You need to consider both unwanted deletions and expansions, so checking needs to be asymmetric, scanning both directions. However, content loss happens as a normal function of the context window's memory management, and text generation is simply what AIs do. Even assuming no unexpected losses or gains, how could any software detect the difference between the desired output and a hallucination?

    Without implausibly complex heuristics that would have to dynamically adapt to the user's input, programmatically detecting hallucinated context poisoning is impossible. Prevention sidesteps all of that, so I extracted the core principles of the AI Stability Framework from the detection pipeline and shelved the engine itself. That detection engine is the only part that couldn't adapt to the environment. Its adaptive traits -- session state evaluation, compliance drift monitoring, domain classification, behavioral intervention sequencing -- survived the change intact and propagated forward into all subsequent lineages. 

7. <a name="faq7"></a>**"This is just prompt engineering."**

    Not quite. Prompt engineering is mostly about designing exquisitely detailed instructions for completion of a single task, ideally in a single turn. The AI Stability Framework operates at the session level, stabilizing an entire conversation rather than just a single turn. The distinction is between painstakingly optimizing a single output and stabilizing the environment that produces all output. Local LLM testing also demonstrated that it can be added both directly to a model's **Macro** training weights, and to the **Meso** platform's system prompt. That means it's layer-agnostic; it works at any point in the deployment stack. Prompt engineering can't say that.

8. <a name="faq8"></a>**"How is this different from system prompts?"**

    The system prompt is configured at the Meso platform layer, where the user typically can't operate. You have no way of knowing what's in it (unless you View Source and read the HTML and CSS) and it's beyond your reach to modify, so most of the time you're unaware that it even exists. Google's background persona injection (Chapter 2) is an element of such an invisible system prompt.

    The Framework's apps work exclusively in the user message space on the user's device, which is the only point where users have any agency. It can't override platform instructions from the chat input field and doesn't try; it just *adds* structural and behavioral rules that the AI incorporates along with everything else. On platforms with user-preference storage, those preferences are loaded as part of the initial session startup as a kind of "supplemental" to the system prompt. the Framework works well with this architecture when it's available, and simulates it via direct input when it's not.

    Anthropic's Claude Code (CLI) paid feature doesn't quite eliminate the intermediate Meso layer entirely, it instead turns that over to you. There is no vendor platform's unpredictable and inaccessible chat interface, no browser problems, no hidden instructions competing with yours. The client is whatever local application you choose to run it from, even a simple PowerShell or bash terminal. The locally-stored and user-editable CLAUDE.md file is the AI instance's startup configuration; this is where you can set up a "system prompt" of your own. The "platform" in this scenario is your own computer: the system that spawns the AI instance inside your interactive client app of choice and applies a set of standing session instructions.

    The result of two-layer Framework mediation, observed in combined usage with the desktop app's timestamps only: very few platform-induced failures (see April-June 2026 notes). The model used for the CLI add-on is the same version of Claude as on the web. With two of the three deployment layers under user control, the reliability improvement is no accident. It's the Framework hypothesis run in reverse: when you eliminate "adversarial" from the deployment stack, stability improves by default.

9. <a name="faq9"></a>**"Client-side injection seems like a security vulnerability."**

    Yes, it does. In fact, per the Open Web Application Security Project's (OWASP) published guidelines for LLM development, any *user-directed behavioral customization that the operator didn't intend* is considered by definition to be an attack. The problem is that typing into the chatbox as intended is also literally "client-side injection," we just don't usually call it that. The "prompt engineering" response applies here too, because the AI Stability Framework demonstrably *works at any layer*, not just at the point of "injection." The Copilot Digital Accessibility (CDA) sub-branch was reviewed and approved for deployment by an enterprise IT Security team because the attack surface is effectively zero and the effect is beneficial.

    The apps produce absolutely nothing you can't preview or type in manually yourself, they just save you the time and keystrokes. The cross-platform CORE port and browser extension branch automate the refresh intervals for a more frictionless user experience. The AI Stability Framework doesn't store, edit, or intercept data at any point in the chain. It has no connectivity functions, it can't store data remotely, and it was designed without access to expensive platform APIs for flexibility. User sovereignty means that all of the Framework's operations are performed only on the user's device because sovereignty also means privacy, which platforms have never taken seriously.

10. <a name="faq10"></a>**"You barely mentioned sycophancy. Can the developers just train that out?"**

    The commonly suggested fixes like operator guardrails, compliance controls, and centralized governance don't touch the layer where sycophancy happens. A platform can quickly roll back a problematic model update, but still have a system that can't detect or control the behavior itself. Reducing its manifestation is possible, but there is currently no clear path to eliminating the problem.
    
    Claude Code's locally-launched architecture demonstrates that applying anti-sycophancy rules can work to *mitigate* the problem at the Meso layer, on a non-adversarial platform. With an adversarial platform, client-side mediation is the only intervention that operates where the problem actually happens, but the scope of that intervention is limited.

11. <a name="faq11"></a>**"Won't the Four Laws cause the AI to amplify pre-existing mental health issues, if they make it follow user directions more reliably?"**

    It's possible, but that's due to a property of AI models, not of the Framework. The model has no perception of the actual Human, only their input. The AI has zero access to the living person behind the text, with or without mediation. Plain text is an insufficient and inappropriate vehicle for any meaningful clinical intervention. The most an AI might do is detect user signaling, but only if the signal exists *and* it's been specifically trained for such detection.

12. <a name="faq12"></a>**"The Tech industry talks about AI 'compute' all the time, why do you only mention it once?"**

    "Compute" is primarily defined as a verb; it's not a noun in standard usage. The industry uses it as jargon to flatten the entire deployment stack into a single opaque term. It elides hardware (GPUs, TPUs, ASICs, servers, networking), physical infrastructure (data centers, cooling systems, power supply, high-speed bandwidth), and software infrastructure (OS, virtualization, INFOSEC configuration, firmware). "Compute" is a terminology choice that buries the whole stack in unthinking Newspeak,[^Fa] which is the point.

    The client layer is the most direct casualty. The only part of the entire stack directly available to users gets flattened right along with everything else, and its absence from the AI conversation mostly goes unnoticed. Accessibility suffers as a direct result, with AI platforms routinely failing ADA, §508, and WCAG compliance requirements because the inconvenient user-facing part of the deal has vanished into "compute." If the industry's entire mental model stops at the SaaS platform layer, it will invariably miss client-side stability failures, not to mention the accessibility failures that affect disabled users every time they try to use these potentially-empowering tools.

13. <a name="faq13"></a>**"Why is an anti-hallucination tool talking about Texas power grids?"**

    Because any serious discussion of AI has to account for the physical infrastructure behind it. The AI instance exists in a virtual void, but the data centers that run it don't. Compare "negligible deployment footprint" to "400+ new data centers in Texas alone," and the reason is clear.

    Using the IEA's figure of approximately 415 TWh (TeraWatt hours) of global data center electricity consumption in 2024 as a baseline, and applying a conservative 20% AI inference share estimate, a 33% reduction in AI inference cycles would conserve on the order of 27 TWh per year, which is roughly enough to power every home in Los Angeles and half of Chicago. At the industry-average Water Usage Effectiveness (WUE) of about 1.8 liters per kWh[^Fb], that same reduction translates to around 48.6 billion liters of water annually. That's the equivalent of 39,600 Olympic-sized swimming pools, or southwest Ohio's Caesar Creek Lake[^Fc].

    Framework-trained models across most independently tested architectures featured reduced output verbosity, with a measured range of 35.4% to 71.8% fewer words per response than their baselines; exceptions are documented in Appendix 2. *Fewer tokens per turn implies proportionally fewer inference FLOPs per query -- the per-task energy implications follow from that directly, though magnitude at scale depends on infrastructure factors outside this study.* The full token delta analysis is in Appendix 2.

14. <a name="faq14"></a>**"Won't the platforms just block it?"**

    They certainly can, even if unintentionally. Early 2026 demonstrated what Meso-layer interventions actually look like in practice: usage limits adjusted without notice, billing caps introduced mid-cycle, tool access throttled, session capabilities changed between turns (see Chapter 10). These changes coincided with the start of the 2026 Iran War and its resultant *global energy crisis*. WCAG structure and timestamps remained reasonably reliable across platforms under these conditions; Four Laws compliance was a different story. 
    
    Claude and Copilot could be stabilized with relatively little effort, however Claude had additional stability issues due to a high rate of Anthropic code churn, with multiple releases following in rapid succession. ChatGPT required multiple stabilization attempts, by which point free-account usage was consumed and the model was hot-swapped with a new downgraded (unstable) instance, making the exercise pointless for free-account holders. Gemini did not stabilize reliably under 2026 April conditions. As of 2026 June, the platform operators all seem to have compensated and largely restored their systems to normal operation, though in some cases usage limits remain more restricted than they had been previously.

    *Deliberately* blocking the Framework is a different question. A platform operator could scan for, detect and strip out its pre-formatted data from user inputs or censor it as a forbidden topic; it's easy enough to spot. But consider the optics of doing so: they would be choosing to proactively deny accessibility requests *(ADA & §508 regulatory compliance)*, timestamps *(innocuous, content-neutral task history)*, and behavioral guidelines *(stable & reliable = increased user satisfaction & engagement)*. Platforms already drawing critical press for a wide range of issues are unlikely to also publicly block such requests.

    During testing, most platforms had the Framework stored in account preferences; Copilot was the exception (the feature appeared briefly, then Microsoft removed it). When a platform goes fully adversarial whether intentionally or as a side effect of other measures as indicated above, those stored preferences are effectively ignored by the platform. That leaves only Micro injection via the chat input, and there is a hard ceiling on what client-side mediation can accomplish when the platform is actively working against it.

    But simply as a practical matter, the client-side workflow is indistinguishable from a user manually typing out plain text in any external editor and then copy-pasting it into the AI chatbox, because that's exactly what it is (as discussed in the "security vulnerability" item above). Short of blocking users from requesting output formatted or processed in a particular way (which would break normal usage), there's no clean way to filter it. However, platform-level service changes certainly can render client-side interventions ineffective.

15. <a name="faq15"></a>**"Does it break when the context window fills up?"**

    Eventually, yes. Context windows have structural limitations, and there's nothing you can do about that. That's why periodic refreshing is part of the workflow. The desktop app's recommended cycle is Structure + Stabilize every 90-120 minutes. The browser extension is designed to automate this based on a token-usage metric instead, but clock time is sufficient for ordinary use.

    Context decay is real and noticeable but manageable. Using STRUCTURE and STABILIZE is a bit like occasionally saving a document you're working on, rather than trusting that nothing will crash. Context decay even provides evidence for the Framework's premise: if AI behavior noticeably changes as its anchoring is evicted from context, that confirms the anchoring was doing something. The degradation curve is the control.


16. <a name="faq16"></a>**"Why is 'Human' capitalized? That's not standard English."**

    No it's not, and that's on purpose.

    English capitalization carries semantic weight. Proper nouns are capitalized; common nouns aren't. That distinction signals to the reader (in this case, a semantics driven pattern matching engine) the difference between a specific Named Entity and a generic category. "AI" is an acronym so it's been capitalized since day one, because that's just how acronyms work in English. "Human" is a common noun, so it appears lowercase in nearly every document a language model has ever been trained on.

    The consequence is subtle but real. A language model trained on the full corpus of Human-produced English text has learned to associate capitalized terms with proper-noun weight: specific, defined, entity-like. "AI" consistently appears that way. "Human" does not. In the model's learned semantic representations, the AI is encoded as something named and specific where the Human is encoded as a generic category.

    Capitalizing "Human" in the Framework and throughout this e-book is a deliberate corrective. It signals to the model that the Human is an entity of equivalent specificity and semantic weight to the AI. The Framework tells the model that the Human is not some category, external player or abstraction the AI is supposed to care about in some general sense. Human means the specific entity who is present and participating in the session. The grammatical irregularity is the point. This quirk of standard English syntax poses a unique problem for an audience of semantically driven pattern matching engines.

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

