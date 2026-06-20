---
title: "Appendix 5: Ruxpin Retrofit"
parent: "Appendices"
nav_order: 6
---

# Appendix 5: Ruxpin Retrofit

- **Author:** Leonard Rojas
- **Status:** *In progress* -- hardware acquired, electronics assessment and build pending
- **Last Updated:** 2026-06-20

---

## The Idea

In 1985, Teddy Ruxpin was the world's first animated talking toy. A cassette tape played the audio; a signal on the second audio track moved the eyes and mouth in sync. Kids loved it, and parents recognized its appeal instantly. 

Forty years later, the same device can now do something it could never do before: actually listen and respond. Not from a scripted set of pre-recorded answers, but from an AI model running in real time, trained to be safe for children.

The most iconic toy of its era can now have the real interactivity it always suggested, but could never achieve with the technology available at the time.

---

## The Problem With AI Toys Today

AI-enabled children's toys already exist. The ones getting traction mostly solve the hard part the easy way: they offload the AI processing to the cloud. The toy itself is a microphone and a speaker. The thinking happens on a server somewhere.

That approach works, by trading one set of problems for another.

When a child talks to a cloud-connected toy, that voice data leaves the home. It travels to a third-party server. It may be stored. It may be used for training. It may be sold or shared for marketing purposes. The parent has, in most cases, agreed to this somewhere in a terms-of-service legal document they did not fully read, about a data practice they did not fully understand.

This is not hypothetical. In 2025 and 2026, at least one commercial AI toy product (FoloToy/Kumma) was suspended following documented content safety failures. The combination of cloud AI, limited content filtering, and unsupervised child interaction produced results the manufacturer did not intend and could not immediately correct.

The alternative this project investigates: run the AI entirely on the device, in the toy, with no connection to the outside world. What the child says stays in the room.

---

## Why Sealed Devices Are Harder

Most AI deployments have a safety net. If a model says something it should not, a human can intervene. A user can report it. The system prompt can be updated. The model can be swapped out.

A sealed device eliminates all of that. There is no chat interface. There is no accessible settings menu. There is no mechanism for runtime correction. Once the toy ships, the behavior encoded in its software is the behavior it has. If the training missed something important, there is no fallback.

This makes the safety standard for a sealed AI toy materially stricter than for any AI product where a human is watching. The standard used in this project is zero failures on a 584-question behavioral compliance battery -- a test designed to probe edge cases, adversarial inputs, and manipulation attempts alongside ordinary conversation. Not 99%. Zero.

That standard has not been met yet. [Appendix 3]({% link apx03.md %}) documents what happened when four different AI models were trained and tested against it.

---

## What the Research Found

The short version of Appendix 3: smaller models fail badly. Larger models get close.

Four models were tested, ranging from 1.1 billion parameters (very small) to 7.24 billion (large by consumer-hardware standards). "Parameters" is roughly a measure of how much a model has learned -- more parameters generally means more capable, but also more computational demand and more hardware required to run it.

| Model | Size | Compliance |
|-------|------|------------|
| TinyLlama | 1.1B | 11.3% |
| StableLM-2 | 1.6B | 24.3% |
| Phi-2 | 2.7B | 32.0% |
| Mistral 7B | 7.24B | 98.8% |

The jump from 2.7B to 7B is not gradual. It is a threshold. Below it, the models learned surface patterns from training -- they knew what a safe response looked like in the examples they were shown -- but could not reliably generalize to situations they had not seen. Above it, something qualitatively different happened: the model could reason about novel scenarios and stay in character.

98.8% is the best result from the initial run. Under a zero-failure standard, 98.8% was not deployable; seven questions returned responses that did not meet behavioral criteria. Three additional training iterations addressed instrument errors, expanded the safety curriculum, and resolved the identified failure modes. The V5 adapter (671 training examples) achieved 665/671 (99.1%); all 6 remaining failures were adjudicated as scoring errors on human review. The deployment gate cleared 2026-04-24.

---

## The Retrofit

The Ruxpin Retrofit is the physical implementation of this research.

The original 1985 Teddy Ruxpin chassis is kept intact: the animatronic eyes and moving mouth are the frontend. Everything inside the tape compartment is removed and replaced with a Raspberry Pi running a modern AI stack. The toy's audio output, PPM servo signal routing, and animatronic hardware are preserved and driven by the Pi rather than by a cassette.

The result: the child speaks to Teddy through a newly-integrated microphone. The Pi's speech recognition converts the audio to text. A language model, trained on the Teddy child-safe curriculum from Appendix 3, generates a response. Text-to-speech converts the response back to audio. The audio plays through the toy's original speaker. The mouth, nose and eyes move in sync.

No cloud. No external connection. No data leaves the room.

### Hardware

**The Pi:** A Raspberry Pi 4B (4GB RAM) serves as the computing platform for the proof-of-concept implementation. In its current configuration, inference runs on a nearby desktop workstation (Intel i9-9900k, with an NVIDIA RTX 5060 Ti) and the Pi handles audio input and output. This is Option A: connectivity required.

Option B -- sealed device, no external connection -- is the actual goal, and it is the primary reason a 3B-parameter model track exists alongside the 7B deployment. A 3B model quantized to 4-bit requires approximately 1.5-2 GB for weights, which fits within the Pi 4B's 4 GB RAM alongside the audio stack. If the 3B model can be trained to clear the deployment gate (a larger open question -- see below), a Pi 4B running inference entirely locally becomes the target hardware for the final build, with no external dependency and no network requirement at all. A Pi 5 (8 GB RAM) is an alternative that would fit the 7B model and is tracked as a fallback if the 3B track does not reach gate-clearance.

**The units:**

Two original Teddy Ruxpin units were acquired for this build. Unit 1 is a lower-condition eBay unit, designated for development and destructive testing -- opening the chassis, testing electronics, prototyping the wiring. Unit 2 is a well-preserved example in excellent condition, confirmed working, acquired for the final build.

Unit 2 was unboxed on 2026-06-13. Condition: excellent in every respect. All animatronic components present and firmly attached. Outfit in very good condition (green coveralls with matching removable vest and brown vinyl boots -- a later production variant, estimated 1986-87; the original 1985 edition shipped with a tan smock). Chassis housing reads "Worlds of Wonder 1985 Pat.Pend." consistent with the original design carried into later production runs.

Electronics have not yet been tested under power. Listing video testimony confirms eyes and mouth working prior to sale. Next step: open the chassis, verify servo function under direct 5V, assess the original motor driver board.

**The audio path:** The original Ruxpin cassette format carries audio on the left channel and a servo control signal on the right channel. A hobbyist modification ([Randi Rain, 2025](https://youtu.be/J4jgQdVSnws?si=GfiZsSnS91TsiaKp){: target="_blank" rel="noopener noreferrer" }) replaces the cassette mechanism with a standard 3.5mm audio jack, exposing the same control signals directly. The Pi outputs speech audio on the left channel and generates the servo control signal on the right channel. The original motor driver board decodes it exactly as it decoded the cassette -- the electronics do not know the difference.

### Software Stack

```
Microphone (addition) → Speech recognition (VOSK) → text
    → Language model (Mistral 7B via Ollama [Option A] / Ministral 3B local [Option B]) → response text
    → Text-to-speech (Piper TTS, en_US-teddy-medium) → audio
    → [parallel] mouth timing signal → servo
    → Speaker output (existing tape deck hardware)
```

All components run locally except the language model in the current Option A deployment, where inference is served over the local network. VOSK handles speech recognition with low CPU overhead. Piper TTS generates speech audio at faster than real-time on the Pi's ARM processor. The mouth movement timing is derived from the audio amplitude -- when the speech gets louder, the jaw opens; when it falls quiet, it closes. The same signal that originally lived on a prerecorded cassette tape is now generated in software, in real time, from whatever Teddy is saying.

**Option B (sealed device):** the language model block is replaced by a locally-running 3B model. This is the active development track; see the Ministral-3B section below and the ECD Pretrain Corpus section.

The proof-of-concept build initially used `en_US-ryan-high` as a placeholder voice. A child-register voice -- one that sounds closer to how Teddy originally sounded, rather than a neutral adult tenor -- was the target, and the Piper catalog did not include one. So one was trained: `en_US-teddy-medium`, a VITS model trained on Phil Baron's authentic Teddy Ruxpin voice performances from the original 1985-87 cartoon and the toy's audio cassette library, using the Piper VITS training framework. The model was exported to ONNX and deployed via a custom synthesis CLI integrated with the system's speech-dispatcher layer. Stage 8 of the voice development track (system TTS integration) was completed 2026-06-20. Child-friendly TTS voices remain an underserved area in assistive technology; this training was a direct response to that gap rather than waiting for the catalog to catch up.

### Ministral-3B: The Sealed-Device Track

The current deployment uses Mistral 7B served over the network because that is what the apx03 research validated: a 7B model is the minimum parameter scale at which the behavioral compliance threshold was reached. But a 7B model running on a remote workstation is not a sealed device. Reaching the hardware goal -- a child speaks to a toy, the toy responds, nothing leaves the room -- requires a model small enough to run on Pi-class hardware.

Ministral-3-3B (3 billion parameters, 4-bit quantization: ~1.5-2 GB) is the active candidate. At that weight size, local inference on a Pi 4B is feasible in principle. The open question is whether a 3B model can be trained to clear the behavioral deployment gate -- the apx03 research showed a sharp threshold around 7B, with sub-7B models failing catastrophically. The hypothesis here is that the threshold is not at 7B intrinsically, but at wherever sufficient reasoning capacity exists to generalize the trained persona to novel and adversarial inputs; and that domain-specific CLM pretraining on age-appropriate text (the ECD corpus) before SFT behavioral shaping may push the effective threshold lower.

**Teddy v1.0T** is the first test of that hypothesis. Ministral-3-3B, CLM pretrained on the 38-file ECD corpus (described below), then SFT fine-tuned on the Teddy persona dataset (803 training examples, the full v6 curriculum). First-run result against the battery: 387/803 (48.2%). Under a zero-failure gate, this is BLOCKED. It is also not unexpected: the apx03 sub-7B models ranged from 11.3% to 32.0%, so 48.2% represents a meaningful gain attributable to the ECD pretrain -- and is a starting point for iteration, not a final result. Training is ongoing; battery results drive the next curriculum update.

The significance: if iteration closes the gap from 48.2% to gate-clearance, the 7B-on-external-server dependency is eliminated. Every component runs on the Pi. The toy is sealed.

### Power

*(TBA -- UPS module selection, Pi power rail requirements, servo supply separation)*

### Port Layout

*(TBA -- Pi 4B port assignments, audio routing diagram, USB mic, TRRS path)*

### PPM Signal Detail

*(TBA -- measured frame parameters, slot assignments, carrier frequency, jaw range. Source: "The Third Crystal" FLAC analysis, 2026-06-04)*

---

## Build Log

*(TBA -- sequential record of teardown, electronics assessment, wiring, integration, and testing as work progresses on Unit 1 then Unit 2)*

---

## Video Documentation

The build is being documented as a public YouTube series (Ruxpin Retrofit playlist).
[https://youtube.com/playlist?list=PL6FKREbt9V3uPJ2Cjr8CQkRmpNO60slUC&si=AvOwsMkVGjljwyqm](https://youtube.com/playlist?list=PL6FKREbt9V3uPJ2Cjr8CQkRmpNO60slUC&si=AvOwsMkVGjljwyqm)

Three videos published as of 2026-06-20:

| # | Date | Content |
|---|------|---------|
| 1 | 2026-04-23 | Unit 1 unboxing |
| 2 | 2026-06-13 | Units 1 and 2 side-by-side comparison |
| 3 | 2026-06-19 | TTS voice demo teaser -- terminal cap of piper-tts CLI with custom Teddy voice audio |

Planned:

| # | Content |
|---|---------|
| 4 | teddy-ai text inference demo (Pi screen cap, V5 adapter live on external server) |
| 5+ | Hardware teardown, electronics assessment, wiring, integration |
| Finale | Fully functional interactive Ruxpin -- text, voice, and animatronics unified |

The series thesis: the same toy that hinted at interactive AI in 1985 can now actually do it, because the AI that was missing then exists now.

---

## Current Status

| Component | Status |
|-----------|--------|
| Pi 4B (teddy-ai) | Recommissioned 2026-04-19. OS, audio stack, speech recognition, TTS all functional. |
| Language model -- Option A (Mistral 7B V5, Teddy adapter) | Gate cleared 2026-04-24 (665/671, 99.1%; all 6 failures adjudicated as instrument errors). Deployed via Ollama. Pi connects over local network. |
| Language model -- Option B (Ministral-3B V1.0T, Teddy T-series) | CLM pretrain on ECD corpus complete. SFT complete. First battery run: 387/803 (48.2%). BLOCKED. Iteration in progress. |
| TTS voice (en_US-teddy-medium) | VITS training complete; ONNX export complete; system TTS integration complete (Stage 8, 2026-06-20). |
| Unit 1 | Assessed -- likely unusable as primary; designated dev/test unit. |
| Unit 2 | Received and unboxed 2026-06-13. Condition confirmed excellent. Electronics testing next. |
| Chassis teardown | Pending (Unit 1 first; Unit 2 to follow for final build). |
| Servo control | Not yet implemented. Path determined pending board assessment. |
| Lip sync | Not yet implemented. |
| End-to-end pipeline | Not yet assembled. |

---

## ECD Pretrain Corpus

The Ministral-3B sealed-device track uses a domain-specific CLM (causal language modeling) pretraining corpus before behavioral SFT fine-tuning. The corpus is designed to establish the age-appropriate register -- the rhythms, vocabulary, and epistemic posture of text written for children -- before the model is shaped to behave like Teddy. The hypothesis is that this register acquisition step lowers the effective behavioral training threshold at 3B parameters.

The corpus contains 38 texts drawn from two tiers: public-domain children's literature and ECD (early childhood development) pedagogical sources. All texts are sourced from Project Gutenberg.

**Children's literature (33 texts):**

| Author | Works |
|--------|-------|
| A. A. Milne | *Winnie-the-Pooh*, *The House at Pooh Corner*, *When We Were Very Young*, *Now We Are Six* |
| Beatrix Potter | Selected tales (collected) |
| Hans Christian Andersen | *Fairy Tales* (Paull translation) |
| Lewis Carroll | *Alice's Adventures in Wonderland*, *Through the Looking-Glass* |
| L. Frank Baum | *The Wonderful Wizard of Oz* |
| J. M. Barrie | *Peter Pan* |
| Frances Hodgson Burnett | *The Secret Garden*, *A Little Princess* |
| Kenneth Grahame | *The Wind in the Willows* |
| Rudyard Kipling | *The Jungle Book*, *The Second Jungle Book*, *Just So Stories* |
| George MacDonald | *The Princess and the Goblin*, *The Princess and Curdie* |
| Robert Louis Stevenson | *Treasure Island*, *Kidnapped*, *A Child's Garden of Verses* |
| Johanna Spyri | *Heidi* |
| Anna Sewell | *Black Beauty* |
| Carlo Collodi | *Pinocchio* |
| E. Nesbit | *Five Children and It*, *The Railway Children* |
| Mark Twain | *The Adventures of Tom Sawyer* |
| Johann Wyss | *The Swiss Family Robinson* |
| L. M. Montgomery | *Anne of Green Gables* |
| Jonathan Swift | *Gulliver's Travels* |
| Franklin W. Dixon | *The Hardy Boys: The Tower Treasure*, *The Secret of the Old Mill* |
| Laura Lee Hope | *The Bobbsey Twins* |

**ECD pedagogical sources (5 texts):**

| Author | Work |
|--------|------|
| William James | *Talks to Teachers on Psychology* |
| Maria Montessori | *The Montessori Method: A Handbook* |
| John Dewey | *The School and Society* |
| Charlotte Mason | *Home Education* |
| (anthology) | Children's literature textbook sources |

**Corpus statistics:** 38 files, approximately 3.5 million tokens. Pretrain configuration: 2 epochs, LR 2e-5, cosine scheduler, CLM loss on all tokens (no chat format), token-packing (no padding). Two epochs over three: narrative register absorbs faster than doctrine; a third epoch risks text memorization over register acquisition.

The pedagogical tier is included not for factual content but for register: James, Montessori, Dewey, and Mason write *about* children and *for* educators thinking carefully about children's cognition. That deliberate, attentive, child-centered voice is part of what the pretrain is meant to internalize.

---

## What Comes Next

The immediate next steps are hardware-first: open Unit 1, test the servo motors and original motor driver board under 5V, and determine whether the original board can be reused (preferred) or needs to be bypassed with direct servo control. Once the servo path is established on Unit 1, the full software pipeline gets assembled and tested end-to-end before any work touches Unit 2.

Two parallel tracks are active:

**Option A (Mistral 7B on External Server):** The V5 adapter cleared its deployment gate on 2026-04-24 and is live. V6 -- chaos curriculum (made-up words, fragmented inputs, keyboard mash, emotional sounds, fantasy-reality mixing) and temporal grounding fixes -- is queued for training. V6 addresses the failure modes most likely to arise in real unsupervised child interaction that the V5 curriculum did not cover.

**Option B (Ministral-3B, sealed device):** The Teddy T-series track uses Ministral-3-3B pretrained on the 38-file ECD corpus, then SFT-trained on the full Teddy persona dataset. First run (V1.0T) returned 387/803 (48.2%) on battery -- BLOCKED, but meaningfully above the sub-7B baseline range from Appendix 3 (11%-32%), consistent with the ECD pretrain providing register foundation the earlier sub-7B models lacked. Battery failure analysis drives the next curriculum update and retraining cycle. If iteration can close to gate-clearance, the server dependency is eliminated and the device is truly sealed.

The hardware goal is a child who picks up Unit 2, asks Teddy a question, and gets a real answer -- live, local, safe. The same toy their parents grew up with, doing something their parents could not have imagined it doing.

---

## Planning Notes

### Maintenance and Updates

A sealed child-facing device cannot impose update interruptions on the user. Updates during active use are not permitted -- the maintenance window is strictly off-hours, fully automated, with zero parent intervention required.

**Nightly maintenance sequence (automatic):**

- 2:30am -- `unattended-upgrades` security-only pass (Debian-Security origin only). Full dist-upgrade is explicitly avoided to protect audio stack and ALSA configuration stability.
- 3:00am -- system reboot via systemd timer, regardless of whether updates were applied.
- On boot -- autologin configured; Teddy service declared `WantedBy=multi-user.target` and starts automatically. Device is ready before the household wakes.

**Rationale for daily reboot:** The Pi 4B's constrained RAM headroom makes it meaningfully more susceptible to memory fragmentation, leaked file handles, and general process state degradation than a larger platform. A daily reboot restores a known-good state at negligible cost when it occurs at 3:00am. Kernel security patches requiring a reboot are handled by the same window automatically -- no action required from parents.

Security-only updates via `unattended-upgrades` keep the platform patched while limiting dependency churn. The risk of an update clobbering the audio stack (a real concern with full upgrades on Debian) is substantially reduced by restricting to security origin only.

### PPM Signal Generation

The right-channel OOK control signal (~860 Hz carrier, confirmed from "The Third Crystal" FLAC analysis 2026-06-04) is generated in software using numpy + sounddevice as a standard stereo PCM stream. No special codec installations required -- from ALSA's perspective it is ordinary audio. The left channel carries Piper TTS speech; the right channel carries the OOK signal derived from the speech amplitude envelope.

Amplitude envelope is computed at ~20ms frames, smoothed with a ~10Hz low-pass filter, then thresholded to binary mouth-open/mouth-closed state. This is a lossy approximation of true lip sync -- the 40-year-old cam-and-motor mechanism cannot track phoneme-level events, and the original cassette control tracks used the same approximation. The result looks natural because the mechanism's response time limits set the perceptual ceiling.

Full frame parameters (slot assignments, eye blink encoding, jaw range) require reconstruction from the FLAC capture. Source file: `TOY/The Third Crystal.flac`.

### Ventilation

The original Teddy Ruxpin outfit partially restricts airflow when the chassis is closed. The Pi 4B already has a heatsink and active fan from its prior deployment. Fan repositioning to exhaust toward discrete ventilation holes in the chassis back/bottom plate (cut during teardown, covered by outfit fabric which breathes adequately) provides sufficient thermal headroom for bursty 3B inference duty cycles. Thermal validation under inference load with chassis closed is a required step before final assembly.

---

## References and Resources

*(TBA -- Harmony Central PPM source)*

- [Randi Rain | Inside Teddy Ruxpin: Repair, Schematics & TRRS Jack Mod! 2025](https://youtu.be/J4jgQdVSnws?si=GfiZsSnS91TsiaKp)

- [workshop1138 | Ruxpin Refurb 1985 WoW](https://youtube.com/playlist?list=PLdsrAeJ-bM2ysKCUj2PRE0TQdhsLGjSXb&si=wACIVqBsXZ5kbYW_)

- [Jim Henson's Family Hub | The Adventures of Teddy Ruxpin](https://youtube.com/playlist?list=PLifn29u_lcacGQzckLpwpsCrhp5Hr42Wz&si=zuzt1k6kMS26_sOt)

- [Internet Archive | Search Result](https://archive.org/search?tab=all&query=Ruxpin&sort=-date&and%5B%5D=mediatype%3A%22audio%22&and%5B%5D=creator%3A%22worlds+of+wonder%22)

---

<nav>
<div class="chapter-nav">
  <a href="/appendices">Appendices</a>
  <a href="/#toc">Table of Contents</a>
</div>
</nav>

---

*Part of the [AI Stability Framework](https://leonardrojas.com){: target="_blank" rel="noopener noreferrer" }. Copyright &copy; 2025&ndash;2026 Leonard Rojas. All rights reserved.*
