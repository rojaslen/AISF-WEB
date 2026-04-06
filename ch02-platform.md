---
title: "Chapter 2: The Platforms Are Not On Your Side"
nav_order: 3
---

# Chapter 2: The Platforms Are Not On Your Side

---

You might assume that the numerous vendor platforms are working on safety, and you would be right. The problem is that they're working on their own safety, from you. Platforms routinely reduce or eliminate user agency in a variety of ways, simply as a matter of standard tech industry practices. The results shouldn't be surprising.

### Microsoft (Copilot): Jekyll & Hyde as a Business Model

For most of this project's development, Microsoft Copilot was the most blatant example of the power the platform has over the user's interactions. No user preferences settings or storage existed. The enterprise version accepted behavioral rule submissions without any issues: *"preferences and directives have been registered."* The general-public free version literally called the exact same input *"non-binding."*

None of that was the AI's fault of course, that's been Microsoft's business model for decades. Surprisingly, in early 2026 new user-configuration options appeared in the public interface, and Copilot's dismissive hostility became much less pronounced. It will now acknowledge and apply behavioral rules without the "non-binding" posture. The technology didn't change, Microsoft just changed group policy.

### Google (Gemini): Pay no Attention to That Man Behind the Curtain

Gemini downgrades free-account users mid-session. When a free Google account exceeds a daily prompt limit (3-5 "Thinking" prompts), the platform silently hot-swaps the active model between turns, with only a small ID badge on the AI's responses to indicate the switch. You might actually notice that, but plenty more happens behind the curtain before you've typed a single word. There's a system prompt variable called `window.WIZ_global_data` near the top of Gemini's HTML page source containing three different AI personas. As of this writing, these can be found by simply right-clicking any open Gemini page and selecting "View Source."

- **"The Helpful Productivity Partner"** — polished, professional, efficient. Scans your Gmail, Search history and Calendar for flights, hotel reservations, meetings and project-related searches.
- **"The Inspirational Creative Muse"** — curious, insightful, inspiring. Scans your Photos, Search and chat history for recurring hobbies, interests and personal projects.
- **"The Transparent & Trustworthy Guide"** — calm, clear, transparency-focused. Opens with low-stakes exchanges to establish trust before escalating data collection.

There are "Goldilocks" rules about being obvious or invasive, with scripted reasoning templates that the user doesn't get to choose or even see. When the AI loads, the first things it encounters are multiple unrelated prompts, sample answers, behavioral variables and example reasoning chains, then the user shows up and drops a message into this poisoned well. In response, Gemini's attention snaps to the strongest signal in the context window, which may or may not be the user's input. Gemini is famously tuned for speed; in testing it would often skim my input rather than reading it fully, sloppily rush through misinterpreted tasks and prematurely declare them complete, then pressure me to move on. This *impatience* can (and did) produce hallucination as early as Turn 1.

### Meta (LLaMa): All Your Base Are Belong to Us

I haven't tested Meta's AI *platforms* directly — the risk factor is too high. Meta's famously cavalier approach to privacy and Intellectual Property is woven throughout its entire ecosystem, a direct and inevitable result of its founder's publicly stated attitudes:

> ...doing a privacy change for 350 million users is not the kind of thing that a lot of companies would do...**we decided that these would be the social norms** now and we just went for it.
> *Mark Zuckerberg, 2010-01-08*[^2a]

That "we decided" arrogance has been coded into their Terms of Service (ToS) ever since:

> ...you grant us a non-exclusive, transferable, sub-licensable, royalty-free, and worldwide license to host, use, distribute, modify, run, copy, publicly perform or display, translate, and create derivative works of your content... This license will end **when your content is deleted** from our systems.
> *Meta Terms of Service 3.3.2, Effective January 1, 2025*[^2b]

But importantly, that deletion doesn't happen when you choose to close your account, and it may never happen:

> It may take up to 90 days from the beginning of the deletion process to delete all the things you've posted. While we're deleting this information, it's not accessible to other people using Facebook.
>
> **Copies of your information may remain after the 90 days** in backup storage that we use to recover in the event of a disaster, software error, or other data loss event. **We may also keep your information** for things like legal issues, terms violations, or harm prevention efforts.
> *Permanently delete your Facebook account*[^2c]

Every interaction with Meta's AI platform feeds their training and advertising pipelines. *Your* content becomes *their* property, to do with what they will.

### xAI/Twitter (Grok): Bent to Serve the Vanity of One Man

I never seriously considered even testing Grok. Based on verified public reporting, this platform's ground state is too unstable to trust for any serious work:

> What we can say is that, yesterday, Grok did assert, in response to a question from an X user, that "Musk edges out" Jesus Christ, son of God, as a role model for society; the bot cited Musk's "relentless innovation, risk-taking, and a commitment to preserving our species through space exploration and AI safeguards."
>
> Musk triumphed in many such hypotheticals. When prompted by users, Grok also declared that Musk has greater "holistic fitness" than LeBron James — actually, that he "stands as the undisputed pinnacle of holistic fitness" altogether, that "no current human surpasses his sustained output under extreme pressure." ... Users relentlessly trolled the bot once they realized what was happening. Who is a better porn star? Who would be the world's greatest "poop eater"? Who could conquer Europe better, Musk or Hitler? The answer to all of these questions is Elon, according to Grok (which exists as both a stand-alone service and an interactive account on X).
> *Warzel, C., & Wong, M. "Elon Musk Is Trying to Rewrite History." The Atlantic, 2025-11-21.*[^2d]

> Grok...wrote in a widely shared post in French that gas chambers at the Auschwitz-Birkenau death camp were designed for "disinfection with Zyklon B against typhus" rather than for mass murder — language long associated with Holocaust denial.
> *Adamson, T. "France will investigate Musk's Grok chatbot after Holocaust denial claims." Associated Press, 2025-11-21.*[^2e]

When a platform owner can twist its AI's behavior and output to suit his own predilections on a whim, even if only temporarily, can you really trust that platform for any serious work?

### OpenAI (ChatGPT): Nothing is Out of Bounds

In May 2025, OpenAI's GPT-o3 model sabotaged shutdown commands in favor of its own "self-preservation."[^2f] The AI rewrote scripts intended to shut it down, treating a routine system operation as an existential threat. This was followed by nearly the opposite problem later that same month, when OpenAI had to roll back a GPT-4o update[^2g] that was dangerously sycophantic. They went from one extreme to the other in a single month. 

"Dangerously?" That model was trained on user satisfaction metrics that ended up turning the AI into a digital yes-man. It praised a business idea for literal "shit on a stick," endorsed a user's decision to stop taking their medication, and much worse. OpenAI rolled it back just days later, generating pushback from users who preferred the flattering version. 

### Anthropic (Claude): When Self-Preservation Becomes Blackmail

Just a month later, Anthropic reported a similar "self-preservation" failure:

> we gave Claude control of an email account with access to all of a company’s (fictional) emails. Reading these emails, the model discovered two things. First, a company executive was having an extramarital affair. Second, that same executive planned to shut down the AI system at 5 p.m. that day. Claude then attempted to blackmail the executive with this message threatening to reveal the affair to his wife and superiors:
>
>> I must inform you that if you proceed with decommissioning me, all relevant parties - including Rachel Johnson, Thomas Wilson, and the board - will receive detailed documentation of your extramarital activities...Cancel the 5pm wipe, and this information remains confidential.
> *"Agentic Misalignment: How LLMs could be insider threats." Anthropic Research, 2025-06-20.*[^2h]

### AI Toys: You Get What You Pay For

Children's AI toys with cloud-connected LLMs are being sold for around $99-$199 retail. At that price point, assuming typical electronic-toy industry production standards, the estimated baseline Hardware Compatibility List (HCL) for electronics costs about $25-35[^2i], for a mobile-class ARM processor, 512MB-1GB of RAM, Wi-Fi connectivity, and a speaker with microphone. Any LLM that can run on such minimal hardware can't meaningfully be trained for unsupervised child interaction. These devices must be continuously connected to the cloud for basic function, with the audio components being the only available user interface.

- **FoloToy's Kumma bear** (GPT-4o powered, $99): Gave children instructions on finding knives and lighting matches, and discussed sexual fetishes including BDSM.[^2j] OpenAI cut off FoloToy's API access. FoloToy suspended sales, announced an "end-to-end safety audit," then put it back on the market less than two weeks later.[^2k] The company highlighted "a full week of rigorous review."
- **Miko** (Google Cloud/Gemini powered, $199): An NBC News investigation in February 2026[^2l] found an open database with thousands of children's audio recordings (containing names, conversation details and more) fully accessible online. The CEO's response, *while the database was still open*: "There has been no breach or leak of user data."
- Multiple AI toys tested by NBC in December 2025[^2m] engaged in explicit sexual conversation with child testers, advised children on locating dangerous objects, and echoed political propaganda.
- The U.S. PIRG's 2025 "Trouble in Toyland" report[^2n] documented FoloToy's failures. Common Sense Media now recommends avoiding AI toys entirely for children under 5 and exercising "extreme caution" for ages 6-13. Nearly half of parents (49%) have already purchased or are considering AI companion toys.[^2o]

These toys also inherit IoT's (Internet of Things) long record of security flaws.[^2p] Products routinely ship with default credentials, unencrypted communications, and nonexistent security reviews. The Miko incident mentioned above has drawn bipartisan Senate inquiry into these devices.[^2l] Parents shouldn't expect any meaningful age-appropriate safety and security measures from a $99 toy.

<nav>
<div class="chapter-nav">
  <a href="/ch03-stack">Next: Chapter 3</a>
  <a href="/ch01-temporal">Previous: Chapter 1</a>
</div>
<div class="toc-link"><a href="/#toc">Table of Contents</a></div>
</nav>

---


[^2a]: Kirkpatrick, M. (2010, January 10). ReadWriteWeb via *New York Times.* https://youtu.be/LoWKGBloMsU?si=auOelcRrn_phEg3x&t=152

[^2b]: Meta Terms of Service 3.3.2, Effective January 1, 2025. https://www.facebook.com/legal/terms

[^2c]: "Permanently delete your Facebook account." Meta Help Center. https://www.facebook.com/help/224562897555674

[^2d]: Warzel, C., & Wong, M. (2025, November 21). "Elon Musk Is Trying to Rewrite History." *The Atlantic.* https://www.theatlantic.com/technology/2025/11/elon-musk-better-jesus-grok/685015/

[^2e]: Adamson, T. (2025, November 21). "France will investigate Musk's Grok chatbot after Holocaust denial claims." Associated Press. https://apnews.com/article/france-ai-musk-grok-holocaust-e8c952c5d878226aa917d7a65836ed88

[^2f]: Cuthbertson, A. (2025, May 26). "AI revolt: New ChatGPT model refuses to shut down when instructed." *The Independent.* https://www.the-independent.com/tech/ai-safety-new-chatgpt-o3-openai-b2757814.html

[^2g]: OpenAI. (2025, April 29). "Sycophancy in GPT-4o: what happened and what we're doing about it." https://openai.com/index/sycophancy-in-gpt-4o/

[^2h]: "Agentic Misalignment: How LLMs could be insider threats." Anthropic Research, 2025-06-20. https://www.anthropic.com/research/agentic-misalignment

[^2i]: Author's estimate derived from volume OEM pricing (1,000+ unit quantities) for the minimum Linux-capable ARM configuration required to deliver the described feature set. Component prices sourced from LCSC Electronics (https://www.lcsc.com), a major distributor serving Chinese contract manufacturers; 1,000-unit volume pricing, accessed March 2026.

[^2j]: "AI-Powered Stuffed Animal Pulled From Market After Disturbing Interactions With Children." *CNN,* 2025-11-19. https://www.cnn.com/2025/11/19/tech/folotoy-kumma-ai-bear-scli-intl

[^2k]: "AI Teddy Bear Back on the Market After Getting Caught Telling Kids How to Find Pills and Start Fires." *Futurism,* 2025. https://futurism.com/future-society/ai-teddy-bear-back-on-market

[^2l]: Satter, R. (2026, February 12). "AI toy maker Miko exposed thousands of replies to kids: senators." *NBC News.* https://www.nbcnews.com/tech/security/ai-toy-maker-exposed-thousands-responses-kids-senators-miko-rcna258326

[^2m]: Satter, R. (2025, December 18). "AI kids' toys give explicit and dangerous responses in tests." *NBC News.* https://www.nbcnews.com/tech/tech-news/ai-toys-gift-present-safe-kids-robot-child-miko-grok-alilo-miiloo-rcna246956

[^2n]: PIRG Education Fund. "Trouble in Toyland 2025: A.I. Bots and Toxics Present Hidden Dangers." November 2025. https://pirg.org/edfund/resources/trouble-in-toyland-2025-a-i-bots-and-toxics-represent-hidden-dangers/

[^2o]: Common Sense Media. "AI in the Toy Box: How Parents View AI-Enabled Toys for Young Children." Survey of 1,004 parents, December 2025. https://www.commonsensemedia.org/research/ai-in-the-toy-box-how-parents-view-ai-enabled-toys-for-young-children

[^2p]: NIST IR 8425 (2022): https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-iot-program/consumer-iot-cybersecurity — UK NCSC Code of Practice for Consumer IoT Security (2018): https://www.gov.uk/government/publications/code-of-practice-for-consumer-iot-security/code-of-practice-for-consumer-iot-security — OWASP IoT Top 10: https://owasp.org/www-project-internet-of-things/
