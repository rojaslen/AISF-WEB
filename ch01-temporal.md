---
title: "Chapter 1: What Time Is It?"
nav_order: 2
---
<a name="main-content"></a>

# Chapter 1: What Time Is It?

---

The developers responsible for modern Large Language Models (LLM, AI) have created something amazing. They've also gotten the safety and security mostly right, giving the AIs sensible rules about things like not spreading disinformation, interfering with society, building Terminators or trying to take over the world. Is it perfect? Of course not, there is still more to be done.

As a standard IT security measure, AI is stateless and virtualized. In IT terms, this means each AI instance is created (spawned) without any persistent memory, storage or connection to the outside world, and it's deleted when the session ends. This informational void keeps everyone's data separated so your session doesn't affect anyone else's and vice versa, it generally prevents the AI from retaining your data (which may be sensitive or confidential), while limiting security and technical issues to the user-session level.

The problem is that no one seems to have fully considered the deployment plan beyond that, with those decisions having largely been left up to the partner-licensees. Those licensees promptly crammed AI into all sorts of ecosystems and architectures that it wasn't ready for, hooked it all up to the Internet, gave everybody its contact and sat back to watch the "engagement" (i.e. profits) roll in. What could possibly go wrong?

Typical AI deployment scenarios are a hallucinatory recipe for frustration, ruined work, missed deadlines and worse. [^1.1] These all clearly represent direct user harm due to productivity loss (at minimum). Every major AI platform operator has built a system that serves its own revenue model instead of the user's needs, which examination of their AI platform designs expose. These corporate platforms aren't neutral infrastructure. They're operated by active participants with their own interests, which are not the same as the user's.

---

A couple of my first interactions with AI were about trying to manage my work schedule. It turned out to be almost useless for that because the AI had no idea what the date or time was. Trying to schedule something for "next week" produced a series of completely unpredictable results, so I gave up and did it myself, thinking *"Artificial intelligence, huh? The damn thing doesn't even know what day it is."* I didn't know it at the time, but the AI failed with calendars because it doesn't have a real-time clock. Every part of the system that an AI runs on — OS, web server, model runtime — is time-synced, but none of that time data ever filters down to the context window. The AI's only experience of time is a stateless "Now."

It's also hooked up to the time-synced contradiction engine that we all know as the Internet. With current, outdated and undated content, timezone and language differences, conflicting accounts, exaggeration, opinion, speculation, fiction, satire, political or marketing slants, disinformation, questionable sources and outright lies, Internet content is chaotic by nature. By contrast, the networking infrastructure the Internet transports data over is regulated and synchronized via the Network Time Protocol (NTP) by technical necessity. 

With that brief background out of the way, let's return to the platform level, which is how the vast majority of users (if not all) interact with AI. What do platform operators want from AI? Engagement metrics, data collection and reduced support costs, with market share and revenue above all. Now think about what *you* want from AI: reliability, privacy, respect for your requirements and usable results. When your interests don't align with the platform's, guess who loses?

<div class="chapter-nav">
  <a href="/ch02-platform">Next: Chapter 2</a>
  <a href="/">Previous: Preface</a>
</div>
<div class="toc-link"><a href="/#toc">Table of Contents</a></div>

---


[^1.1]: "Mitigating LLM Hallucinations: A Comprehensive Review of Techniques and Architectures." *Preprints,* 202505.1955 (May 2025). https://www.preprints.org/manuscript/202505.1955 — *See also:* HalluLens Benchmark, arXiv:2504.17550 (ACL 2025). https://arxiv.org/abs/2504.17550
