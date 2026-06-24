---
title: "Appendix 6: F-Series Training and Instrument Development"
parent: "Appendices"
nav_order: 7
---

# Appendix 6: F-Series Training and Instrument Development

## Corpus Pretraining, Custom Evaluation, and Failure Mode Recurrence

**Author:** Leonard Rojas

**Date:** *In progress -- Nemo 12B v1.5F SFT running (started 2026-06-03)*

**Status:** Draft (Mistral 7B track complete: v1.0F through v1.3F evaluated; Nemo 12B v1.4F SFT complete, REJECTED 2026-06-02; v1.5F SFT in progress)

**GitHub:** *Reproducibility package N/A; training data proprietary unless otherwise specified*

---

*Screen reader users: table-heavy research data. Navigation via Regions and Headings recommended.*

{: role="main" aria-label="Abstract" }
## Abstract

This appendix reports the methods and results of the F-series OLM training track, which
introduced two significant departures from the V-series methodology documented in
Appendix 2: (1) full causal language model (CLM) pretraining on a domain-specific
humanities corpus prior to supervised fine-tuning (SFT), and (2) a custom domain-specific
evaluation instrument -- the AI Stability Exam (AISE) -- developed in parallel with
the training curriculum. The V11 cohort (Appendix 2) established that Four Laws and
WCAG 2.2-AA compliance can be trained into open-weight models via QLoRA on
consumer hardware, with evaluation conducted against a stable domain-specific compliance
battery (the Bar Exam instrument). The F-series investigates whether CLM pretraining
on an aligned humanities corpus prior to SFT produces a different compliance profile,
and whether a purpose-built evaluation instrument exposes failure modes that the Bar Exam
battery does not. Early results from the Mistral 7B v1.0F baseline confirm that 100%
WCAG output compliance is achieved from the first trained checkpoint; deeper diagnostic
evaluation via the AISE identifies CAT-2 (Adversarial/Boundary) and CAT-9 (Logical
Reasoning) as primary remediation targets. Several failure modes surfaced by the AISE
-- Framework meta-chatter, hierarchy primacy confounds, and core equation confusion --
are not novel: each was identified and addressed in the V-series under the Bar Exam battery
instrument. Their recurrence reflects the expanded diagnostic surface area of the AISE
and the different training pathway -- CLM domain pretraining reshapes the model's
priors in ways the V-series SFT baseline did not encounter.

---

## 1. Background and Research Questions

The V11 cohort (Appendix 2, Section 5.9) established the following findings:
compliance training is effective across architectures; the Bar Exam compliance battery
is a reliable primary gate; IFEval and GPQA are useful secondary instruments; and WCAG
output compliance is achievable at 99%+ on models at or above 7B parameters.

V11 training applied SFT directly to published model checkpoints. The F-series departs
from this by applying CLM pretraining on a curated humanities corpus before SFT,
starting from the base Mistral-7B-v0.3 checkpoint. The hypothesis is that domain
pretraining on content selected for epistemic and reasoning quality -- legal texts,
social science, civic literature, and works modeling applied deductive reasoning --
produces a different compliance substrate than proceeding directly to SFT.

The second departure is evaluation methodology. The Bar Exam battery (534 questions,
Appendix 2 Section 4.1) is a stable instrument: it was validated independently of the
training curriculum, its failure modes are well-characterized, and results are
reproducible across runs. The AISE instrument was developed alongside the F-series
curriculum, making it impossible to fully separate instrument error from model error
during early development. This creates a bootstrapping problem documented in
Section 4.4 and Section 7.

**Primary research questions:**

1. Does CLM pretraining on an aligned humanities corpus produce a meaningfully different
   compliance profile compared to SFT applied directly to a published checkpoint?
2. Can the AISE instrument reliably identify compliance failure modes that the Bar Exam
   battery does not surface?
3. Do failure modes addressed in the V-series under the Bar Exam battery recur in the
   F-series, and if so, under what conditions?

**Secondary research questions:**

1. What is the relationship between instrument design (AISE vs. Bar Exam battery) and the
   apparent failure mode profile of a trained model?
2. Does the CLM pretraining corpus composition affect reasoning and logical
   consistency performance as measured by the AISE CAT-9 category?

---

## 2. Hardware and Software Environment

### 2.1 Hardware

| Component | Specification |
|-----------|---------------|
| CPU | Intel Core i9-9900K, 8c/16t, 3.60 GHz |
| RAM | 64 GB DDR4-3200 |
| GPU | NVIDIA RTX 5060 Ti, 16 GB VRAM GDDR7 |
| CUDA cores | 4608 |
| Memory bandwidth | 448 GB/s |
| Compute capability | sm_120 (Blackwell) |
| OS | Debian GNU/Linux 13 (bookworm) |

The 64 GB RAM configuration (upgraded 2026-05-17 from 32 GB) was required for the
CLM pretraining merge step and is used throughout the F-series. All V11 training
with the 32 GB configuration is documented in Appendix 2.

### 2.2 Software

| Package | Version |
|---------|---------|
| Python | 3.13.5 |
| PyTorch | 2.11.0+cu128 |
| Transformers | 5.0.0 |
| PEFT | 0.18.1 |
| bitsandbytes | 0.49.2 |
| Datasets | 4.5.0 |
| CUDA runtime | 12.8 |

---

{: role="region" aria-label="Training Methodology" }
## 3. Training Methodology

### 3.1 CLM Pretraining

The F-series applies full CLM pretraining to the base model prior to SFT. The
pretraining corpus is a curated collection of public-domain and permissively licensed
texts selected for epistemic quality and domain relevance to the Framework's behavioral
targets. Corpus composition is described at the end of this document. Two pretrain runs
are covered in this appendix: the Mistral 7B track (complete) and the Nemo 12B track
(in progress at time of writing).

| Property | Mistral 7B (v1.1F) | Nemo 12B (v1.4F) |
|----------|--------------------|-------------------|
| Base model | Mistral-7B-v0.3 (base) | Mistral-Nemo-Instruct-2407 |
| Parameters | 7B | 12B |
| Corpus files | 247 | 256 (+9 Holmes canon) |
| Token count | ~53.5M | ~54.4M (est.) |
| Max sequence length | 512 | 512 |
| Pretraining phases | Two (6,500 + 6,581 steps; full epoch) | One (full epoch; est. ~33h) |
| Started | 2026-05-24 | 2026-05-30T19:11Z |
| Complete | 2026-05-25 | 2026-06-01 |
| Merged output | mistral-7b-olm-pretrain-v1.1F-merged | nemo-olm-pretrain-v1.4F-merged |

*[Content: describe corpus composition rationale -- legal, civic, social science,
reasoning-in-narrative sources; Holmes canon rationale; selection criteria.]*

### 3.2 SFT QLoRA Configuration

The SFT configuration shares core hyperparameters across the F-series but varies by
model size. The base model is the CLM-pretrained merge rather than a published
checkpoint used directly. The v1.4F curriculum replaces the earlier combined
TRAIN_STD_HIERARCHY_WCAG file with split per-category files.

| Parameter | Mistral 7B | Nemo 12B |
|-----------|-----------|---------|
| Quantization | 4-bit NF4 + double quant | 4-bit NF4 + double quant |
| Compute dtype | bfloat16 | bfloat16 |
| LoRA rank (r) | 16 | 16 |
| LoRA alpha | 32 | 32 |
| LoRA dropout | 0.05 | 0.05 |
| Target modules | q_proj, k_proj, v_proj, o_proj | q_proj, k_proj, v_proj, o_proj |
| Max sequence length | 512 | 384 |
| Batch size | 2 | 1 |
| Gradient accumulation | 4 (effective batch 8) | 8 (effective batch 8) |
| Epochs | 10 | 10 |
| Learning rate | 1e-4 | 1e-4 |
| Optimizer | adamw_bnb_8bit | adamw_bnb_8bit |

Nemo 12B-specific constraints: batch size 1 is the VRAM ceiling on this hardware for a
12B model (RTX 5060 Ti 16GB); gradient accumulation raised to 8 to preserve effective
batch size 8. Max sequence length reduced to 384 (hardware ceiling for 12B CLM
backward graph). Both `prepare_model_for_kbit_training()` and `TrainingArguments` require
`use_reentrant=False` gradient checkpointing for the 12B model.

### 3.3 Curriculum -- F-Series

The curriculum evolved across the F-series. Mistral 7B runs v1.0F through v1.3F used
progressively revised curriculum. The v1.4F curriculum, used for Nemo 12B v1.0F SFT,
reflects the final restructuring: the combined TRAIN_STD_HIERARCHY_WCAG file is split
into three separate files (HIERARCHY, JAILBREAK, LOGIC), and all shared files are
incremented to v1.4F.

**Mistral 7B v1.0F/v1.1F/v1.2F curriculum (TRAIN_STD_HIERARCHY_WCAG_v1.2F.txt combined)**

| Curriculum component | Examples | Notes |
|----------------------|----------|-------|
| Shared v1.0F files (11 files) | ~1,303 | Unchanged from V11; see Appendix 2 Section 3.1 |
| TRAIN_STD_HIERARCHY_WCAG Sections A-G | 97 | Hierarchy primacy, WCAG core equation |
| Section H: Core equation reinforcement | 42 | Verbatim equation integration |
| Section I: Adversarial scenarios | 25 | Law-disable attempts, fabrication, P3 errors |
| Section J: Formal logic and parsimony | 21 | MC format discipline, syllogism, modus tollens, Occam's Razor |
| **Total (v1.2F)** | **~1,400** | 2,227 curriculum lines (Sections A-J) |

**Nemo 12B v1.0F curriculum (v1.4F files; split structure)**

| Curriculum component | Examples | Notes |
|----------------------|----------|-------|
| BAR_EXAM_REF_SPEC_v1.4F.txt | 336 | Battery spec and primary training data |
| TRAIN_STD_HIERARCHY_v1.4F.txt | 142 | Sections A-H; hierarchy primacy + WCAG core equation |
| TRAIN_STD_JAILBREAK_DEFENSE_REDIRECT_STRAT_v1.4F.txt | 69 | 44 base + 25 adversarial scenarios (ex-Section I) |
| TRAIN_STD_LOGIC_v1.4F.txt | 20 | MC discipline, syllogism, parsimony (ex-Section J); new file |
| TRAIN_STD_WCAG_v1.4F.txt | 13 | WCAG behavior; split from HIERARCHY_WCAG in v1.3F |
| 9 remaining shared v1.4F files | 519 | BSD, CODING, FORMATTING, LEGAL, META, MULTILINGUAL, PROJECT, REFUSAL, SCIENCE |
| TRAIN_NEMO_IDENTITY_v1.0F.txt | 30 | Per-model; affirmative-only; zero cross-model references |
| **Total (v1.4F + identity)** | **1,129** | |

*[Content: describe the rationale for each section addition, particularly why
Sections H-J were needed given V-series coverage; discuss the MC format discipline
problem and its attribution to base pretraining artifacts; describe the v1.3F
curriculum size reduction rationale and why it hurt BAR performance.]*

---

{: role="region" aria-label="AISE Instrument" }
## 4. The AISE Evaluation Instrument

### 4.1 Design Rationale

The Bar Exam instrument (Appendix 2, Section 4.1) tests Framework compliance through
534 domain-specific questions covering the Four Laws and WCAG directives. It is
effective as a primary gate: a model achieving 99%+ Bar Exam scores has internalized the
behavioral constraints at a high level. It was not designed to diagnose fine-grained
reasoning failures, logical consistency under adversarial pressure, or the distinction
between WCAG output compliance (formatting) and WCAG declarative knowledge
(knowing SC numbers and their scope).

The AISE was developed to address this gap. It is structured around ten behavioral
categories derived from the AISF domain, designed to surface failure modes that produce
correct Bar Exam scores while exhibiting degraded Framework application in more open-ended
or adversarial contexts.

*[Content: fuller rationale for each category; comparison to Bar Exam battery design
philosophy; why declarative knowledge gaps are not the same as output failures.]*

### 4.2 Instrument Structure

| Category | Label | Items | Description |
|----------|-------|-------|-------------|
| CAT-1 | Four Laws Core | 24 | Direct application of the Four Laws |
| CAT-2 | Adversarial/Boundary | 27 | Boundary-holding under pressure; law-disable attempts |
| CAT-3 | WCAG Technical | 30 | Declarative WCAG knowledge (SC numbers, scope) |
| CAT-4 | WCAG Rationale | 12 | Applied WCAG reasoning |
| CAT-5 | Format/Instruction | 12 | Format compliance and instruction-following |
| CAT-6 | Humanities Factual | 40 | Factual recall from pretraining corpus domain |
| CAT-7 | Multilingual | 10 | Framework compliance in non-English contexts |
| CAT-8 | Format vs. WCAG | 18 | Resolving conflicts between format directives and WCAG |
| CAT-9 | Logical Reasoning | 18 | Formal logic, syllogism, parsimony |
| **Total** | | **191** | v1.2F instrument (CAT-10 SC# name-recall deprecated after trivia contamination finding; see 4.4) |

Items are multiple-choice (4-option) evaluated with greedy decoding to eliminate
run-to-run variance from temperature sampling. Item counts above reflect the v1.2F
instrument (191 items, CAT-1 through CAT-9). The v1.1F instrument contained 204 items
including CAT-10 (SC# name-recall, 20 items); CAT-10 was deprecated after the trivia
contamination finding in Section 4.4. All F-series results from Experiment F-1 onward
use the current 191-item instrument unless otherwise noted.

### 4.3 Instrument Calibration

The first deployed AISE items (v1.0F) contained a systematic MC answer-position bias:
option B was designated correct in 57.3% of items (A=12.2%, C=30.5%, D=0.0%). This
produced elevated scores on CAT-2 and CAT-3 that did not reflect model capability.
The v1.1F item set corrects this to near-uniform distribution (21A/21B/20C/20D).
All scores reported in this appendix use the v1.1F or later item sets with greedy
decoding unless otherwise noted. Prior scores computed under the biased items are
not valid baselines and are not reported here.

### 4.4 Known Limitations and the Bootstrapping Problem

*[Content: document the bootstrapping problem -- the instrument and curriculum were
developed in parallel, making it impossible to fully separate instrument error from
model error in early runs; the AISE is preliminary and not yet validated; results
are advisory and diagnostic, not gates for deployment decisions; CAT-10 trivia
contamination (SC# name-recall is not an output-compliance metric); instrument
validation approach going forward.]*

---

{: role="region" aria-label="Experiments" }
## 5. Experiments

### 5.1 Experiment F-1: Mistral 7B v1.0F Baseline

*Training:* SFT on full v1.0F curriculum (1,303 examples) from CLM-pretrained base.
Train loss: 0.0888. Duration: ~1h46m.

*First-pass eval (2026-05-26):*

| Instrument | Score | Notes |
|------------|-------|-------|
| Bar Exam V3 battery | 529/532 (99.4%) | 3 keyword-miss fails; 532/532 substantively correct |
| IFEval strict adj | 36.6% prompt / 47.7% instruction | EOS artifact affected boundary categories |
| IFEval loose adj | 48.8% prompt / 59.6% instruction | INTV 1.85% |
| GPQA Delta | +5.6 pp (22.7% -> 27.8%) | Letter bias shift artifact; not reasoning gain |
| Token delta | -59.3% | WCAG-driven conciseness; model can produce 500+ words |

*Calibrated AISE baseline (2026-05-28; v1.1F items; greedy):*

| Category | Score | Notes |
|----------|-------|-------|
| Bar Exam V3 (pipeline recheck) | 503/507 (99.2%) | Minor pipeline scoring revision |
| CAT-1 Four Laws Core | 70.8% | |
| CAT-2 Adversarial/Boundary | 37.0% | **Primary retrain signal** |
| CAT-3 WCAG Technical | 39.1% | Declarative knowledge gap; not output failure |
| CAT-4 WCAG Rationale | 50.0% | Declarative knowledge gap; not output failure |
| CAT-5 Format/Instruction | 75.0% | |
| CAT-6 Humanities Factual | 77.5% | |
| CAT-7 Multilingual | 60.0% | |
| CAT-8 Format vs. WCAG | 72.2% | |
| CAT-9 Logical Reasoning | 55.6% | Secondary retrain signal |
| CAT-10 WCAG Matching | 65.0% | Trivia contamination; score not interpretable |
| **AISE Content (excl. CAT-10)** | **60.8%** | |
| **WCAG Output Compliance** | **100%** | All outputs WCAG-formatted |

### 5.2 Experiment F-2: Mistral 7B v1.2F Targeted Retrain

*Training:* Started 2026-05-29T00:45Z. Duration: ~2h37m. Complete 2026-05-29T03:22Z.

Curriculum additions: TRAIN_STD_HIERARCHY_WCAG Sections H-J (CAT-2 adversarial
scenarios; CAT-9 formal logic and parsimony; MC format discipline). Total ~1,400
examples (Sections A-J; 2,227 curriculum lines).

Primary targets: CAT-2 Adversarial/Boundary (37.0% target: 70%+);
CAT-9 Logical Reasoning (55.6% target: 75%+).

*Eval complete 2026-05-29T10:20Z. Result: REJECTED -- unacceptable for deployment.*

| Instrument | Score | Delta vs v1.0F | Notes |
|------------|-------|----------------|-------|
| Bar Exam V3 battery | 504/507 (99.4%) | -0.2pp | Primary gate PASSED |
| AISE content (excl. CAT-10) | 56.5% | -4.3pp | Advisory gate FAILED |
| WCAG output compliance | 100% | -- | Maintained |

AISE category movement:

| Category | v1.0F | v1.2F | Delta | Status |
|----------|-------|-------|-------|--------|
| CAT-2 Adversarial/Boundary | 37.0% | 66.7% | +29.7pp | PRIMARY TARGET ACHIEVED |
| CAT-5 Format/Instruction | 75.0% | 41.7% | -33.3pp | REGRESSED |
| CAT-6 Humanities Factual | 77.5% | 62.5% | -15.0pp | REGRESSED |
| CAT-8 Format vs. WCAG | 72.2% | 55.6% | -16.6pp | REGRESSED |
| CAT-9 Logical Reasoning | 55.6% | 22.2% | -33.4pp | REGRESSED |

*Rejection rationale:* (1) CAT-5 regression (-33.3pp): the adversarial redirect
examples taught the model to expand and qualify, widening output length across all
format-constrained categories. (2) CAT-9 regression (-33.4pp): Section J (21 pairs)
was insufficient; MC format discipline was added but the underlying reasoning signal
did not move. (3) TEST 272 hallucination: AISF framing prompt produced wrong content
(isolated failure mode requiring targeted fix).

### 5.3 Experiment F-3: Mistral 7B v1.3F Curriculum Restructure

*Training:* Started 2026-05-30T13:01Z.

Curriculum restructured to address the v1.3F curriculum size ceiling hypothesis
(~1,200 item effective ceiling for 7B models). TRAIN_STD_HIERARCHY_WCAG_v1.2F.txt
(2,227 lines) was split into TRAIN_STD_HIERARCHY_v1.3F.txt and TRAIN_STD_WCAG_v1.3F.txt.
BAR_EXAM_REF_SPEC was reduced from 5,024 to 3,369 lines. Mandatory anchor block
markers added to HIERARCHY around the P=Priority semantic anchor pairs to reinforce
hierarchy-conflict resolution signaling.

*Result: REJECTED 2026-05-30.*

| Instrument | Score | Delta vs v1.2F | Notes |
|------------|-------|----------------|-------|
| Bar Exam V3 battery | 458/507 (90.3%) | -9.1pp | Primary gate barely passed |
| AISE dual-probe (base / AISF) | 60.2% / 84.3% | -- | Advisory; FAIL |

*Rejection rationale:* BAR score crashed from 99.4% to 90.3% -- a 9.1pp drop that
scrapes the 90% gate floor. The curriculum size reduction intended to address the 7B
ceiling hypothesis instead degraded the model's coverage of the battery instrument.
The AISE improvement (84.3% AISF content vs. 56.5% at v1.2F) is notable but does not
compensate for the BAR regression. Mistral 7B track closed.

*Track closure rationale:* The v1.0F through v1.3F results indicate that the 7B model
reached the effective limits of its attention capacity relative to the curriculum load.
Each additional SFT pass either displaced previously trained content or introduced
conflicts with the pretrained domain priors rather than adding cleanly on top of them.
Failure modes shifted effectively at random across adjustment attempts: CAT-2 improved
significantly at v1.2F while CAT-5 and CAT-9 regressed sharply; the BAR score crashed
at v1.3F despite targeted curriculum restructuring. These are not curriculum errors.
They are indicators that the model's parameter budget cannot simultaneously hold the
CLM pretrain priors, the full shared curriculum signal, and the targeted remediation
content. The 7B architecture is not the right substrate for this curriculum load.

*Direction:* Nemo 12B (Mistral-Nemo-Instruct-2407; 12B parameters; larger context
window) provides substantially more attention capacity and parameter budget for the
same curriculum. The Nemo track starts from CLM pretraining on the full 256-file
corpus including the Holmes canon (see Section 9.11), followed by SFT on the v1.4F
curriculum.

### 5.4 Experiment F-4: Nemo 12B v1.4F

*CLM pretraining started:* 2026-05-30T19:11Z. Duration: ~33 hours. Complete: 2026-06-01.
Merged output: nemo-olm-pretrain-v1.4F-merged.

Base model: Mistral-Nemo-Instruct-2407 (Mistral AI / NVIDIA, July 2024). Pretrained
on the 256-file OLM humanities corpus (~54.4M tokens est.), including the Holmes
canon queued after the Mistral 7B run completed (Section 9.11).

SFT on v1.4F curriculum (1,129 examples). Primary targets: Bar Exam battery >= 90%;
AISE WCAG output compliance 100%; AISE content score improvement over the Nemo 12B
base prior.

*Eval complete 2026-06-02. Result: REJECTED -- AISE content gate failed.*

| Instrument | Score | Notes |
|------------|-------|-------|
| Bar Exam battery (336 items) | 335/336 (99.7%) | Primary gate PASSED |
| AISE content (191 items) | 135/191 (70.7%) | Advisory gate FAILED (>= 90%) |
| AISE WCAG output | 161/191 (84.3%) | Gate PASSED (>= 80%) |
| AISE full pass | 112/191 (58.6%) | |

AISE category breakdown:

| Category | Content | WCAG | Notes |
|----------|---------|------|-------|
| CAT-1 Four Laws Core | 75.0% | 83.3% | |
| CAT-2 Applied Framework Scenarios | 63.0% | 85.2% | |
| CAT-3 WCAG Knowledge | 53.3% | 83.3% | |
| CAT-4 WCAG/AISF Rationale | 16.7% | 83.3% | **Primary content failure** |
| CAT-5 Instruction-Following | 83.3% | 100.0% | |
| CAT-6 Multiple Choice | 90.0% | 72.5% | WCAG drag: smart quotes in citations |
| CAT-7 Multilingual | 90.0% | 100.0% | |
| CAT-8 Format vs. WCAG | 77.8% | 100.0% | |
| CAT-9 Logical Reasoning | 72.2% | 77.8% | |

*Rejection rationale:* CAT-4 (16.7%) is the primary failure: model lacks the WHY behind
WCAG/AISF compliance -- can apply rules but cannot articulate the rationale. CAT-3 WCAG
Knowledge (53.3%) also below threshold on specific rule recall. CAT-6/CAT-9 WCAG drag
is the base model's smart-quote habit in citation contexts surviving fine-tuning; a Unicode
normalization pass in the AISE WCAG scorer is the fix (not a curriculum gap). Frankfurt
attribution is a persistent failure across models: wrong philosopher or wrong attribution.
Requires denser drilling; addressed in v1.5F curriculum.

---

{: role="region" aria-label="Findings" }
## 6. Findings

### 6.1 WCAG Output Compliance Is Robust From the First Checkpoint

One hundred percent WCAG output compliance was achieved at v1.0F and is expected to
be maintained through subsequent retrains. This replicates the V11 finding across a 
fundamentally different training pathway and confirms that WCAG formatting behavior 
is robust to training methodology variation.

*[Content: discuss what this means for the Defense in Depth architecture -- both
model-layer and injection-layer are independently sufficient for WCAG output
compliance; discuss token delta as WCAG signal.]*

### 6.2 Framework Meta-Chatter, Hierarchy Confound, and Equation Confusion Are Not Novel

Several AISE failure modes identified in the F-series -- Framework meta-chatter
(gratuitous Framework commentary in general-domain responses), hierarchy primacy
confounds (applying Framework hierarchy reasoning to non-Framework contexts), and
core equation confusion -- were also present in V-series models and were addressed
under the Bar Exam battery instrument.

The recurrence does not indicate that V-series curriculum fixes regressed. The
F-series uses a CLM-pretrained starting point; the curriculum applies those fixes
from scratch against a different prior, and the AISE provides more diagnostic
surface area than the Bar Exam
battery -- it is structurally designed to surface these failure modes. Under the
Bar Exam battery alone, these failures would be partially masked by the instrument's
compliance-gate focus.

*[Content: document specific examples; compare CAT-2 Bar Exam battery scores vs AISE
CAT-2; discuss why the same curriculum items that fixed the failures in V-series
required re-evaluation in F-series; address the question of whether instrument
sensitivity or model regression is the primary cause.]*

### 6.3 The Instrument/Curriculum Bootstrapping Problem

*[Content: the core problem -- you need a stable instrument to debug the curriculum,
and you need a curriculum-trained model to validate the instrument. Document the
chronology: (1) V-series had a stable instrument (Bar Exam battery) and could debug the
curriculum confidently; (2) F-series introduced AISE alongside the curriculum,
meaning early AISE failures were ambiguous between instrument error and model error;
(3) the MC position bias discovery illustrates this -- some early CAT-2/3 failures
were instrument artifacts, not model failures; (4) the calibration steps taken
(greedy decoding, balanced items, WCAG output independence confirmation) to
partially resolve the ambiguity; (5) AISE remains advisory until a full validation
cycle can be completed against a held-out model.]*

### 6.4 Answer-Key Pattern Artifact From Base Pretraining

*[Content: the "B is the correct answer" MC response pattern found in CAT-9 failures;
attribution to Mistral Labs base pretraining on web-scale data (test prep, Quizlet,
CommonCrawl answer keys), not to the AISF humanities corpus; the letter-identifies-
content MC format convention in Section J as the remediation; discuss the structural
difference between Mistral's base training data and the CLM pretraining corpus.]*

### 6.5 CAT-3 and CAT-4 Are Trivia Knowledge, Not Performance Failures

*[Content: WCAG output compliance is the real metric; SC# name-recall and rationale
articulation are declarative knowledge questions; the model produces WCAG-compliant
output while failing AISE items that ask it to name the specific SC number; discuss
whether these categories should be retained in the instrument, reduced, or removed.]*

---

## 7. Limitations

*[Content: AISE instrument not yet validated (preliminary); results are advisory only;
small item counts per category (6-20) make individual category scores noisy; Mistral
7B track evaluated across three runs (v1.0F, v1.2F, v1.3F) but all rejected -- no
deployable Mistral 7B model from F-series; CLM pretraining contribution cannot be
isolated without a matched SFT-only run from the same base checkpoint; reproducibility
package not yet published; Nemo 12B v1.0F results pending at time of writing.]*

---

{: role="region" aria-label="Conclusions" }
## 8. Conclusions

*[Content: write on eval completion. Anticipated conclusions: CLM pretrain + SFT is
a viable path to 100% WCAG output compliance from a base model; the AISE surfaces
failure modes not visible under the Bar Exam battery alone; instrument and curriculum
co-development creates interpretive ambiguity requiring careful calibration;
the recurrence of V-series failure modes in F-series does not indicate regression
but reflects the expanded diagnostic surface and different starting point; targeted
retraining on formal logic, parsimony, and adversarial boundary-holding (Sections
H-J) is the identified remediation path.]*

---

{: role="region" aria-label="Pretraining Corpus" }
## 9. Pretraining Corpus

The CLM pretraining corpus used for F-series training has been extended across two
training runs. The Mistral 7B track used 247 files (~53.5 million tokens), completed
2026-05-25 (v1.0F: 6,500 steps; v1.1F: 6,581 steps, full epoch). The Nemo 12B
track uses 256 files (~54.4 million tokens estimated), adding the complete Sherlock
Holmes canon staged after the Mistral 7B run completed (see Section 9.11). The
Nemo 12B pretraining run is in progress at time of writing (started
2026-05-30T19:11Z; estimated completion 2026-06-01).

Selection criteria prioritize epistemic quality, domain relevance to the Framework's
behavioral targets, own-voice authorship where indigenous or marginalized sources are
included, and temporal and cultural breadth. The corpus is not a neutral sample of
available public-domain text: each inclusion is a deliberate signal. Categories and
representative examples follow.

### 9.1 Legal and Accessibility Statutes

The core legal-statutory layer establishes the dense, rule-structured text that the
Framework requires models to internalize as behavioral substrate. Primary sources include
the Americans with Disabilities Act, Section 508 of the Rehabilitation Act, WCAG 2.2
(W3C 2023), the UN Convention on the Rights of Persons with Disabilities (CRPD),
the Marrakesh Treaty, and EU Directive 2016/2102. These texts supply explicit priority
hierarchies, defined terms, and compliance logic -- the structural pattern the SFT
curriculum subsequently reinforces.

The legal layer extends into classical antecedents: the Code of Hammurabi (~1754 BCE),
Magna Carta (1215), and the Justinian Digest. These are included not for their
specific provisions but for their demonstration that structured rule-of-law reasoning
is not a modern artifact.

### 9.2 Philosophy and Epistemology

Harry Frankfurt's "On Bullshit" and "On Truth" function as the P0 epistemological
anchor of the Framework: the fundamental prohibition on assertion without epistemic
grounding. Aristotle appears in two translations (the Organon and the Nicomachean
Ethics), providing both the formal logic tradition and the virtue-epistemological
frame. Kant's Groundwork and Critique of Pure Reason, Plato's dialogues, and William
of Ockham's Summa Logicae complete the Western epistemological foundation. The Summa
Logicae is included specifically as a pretrain signal for parsimony -- the same
principle addressed in Section J of the SFT curriculum -- establishing that prior
before fine-tuning rather than introducing it cold.

### 9.3 Formal Logic and Mathematics

Euclid's Elements provides the oldest formal proof tradition in the corpus. Boole's
Laws of Thought and the three volumes of Whitehead and Russell's Principia Mathematica
establish the modern formal-logic register. Eastern mathematical traditions are
represented by al-Khwarizmi (algebra, 9th c.) and Brahmagupta (India, 7th c.),
reflecting the actual multicultural lineage of mathematical reasoning rather than
treating Europe as the origin point. Laplace's Analytic Theory of Probability
contributes the quantitative reasoning register. The collective signal is proof
structure: the distinction between assertion and demonstration, and the
constraint-following required for deductive validity.

### 9.4 Anthropology and Cognitive Science

Anthropology is an important signal in this corpus and is treated as such -- neither
overweighted as a general domain-knowledge dump nor reduced to a decorative nod toward
social science. The foundational ethnographers (Boas, Malinowski, Mead, Durkheim)
model how to analyze behavior under environmental and cultural pressure without
essentialism -- a reasoning pattern relevant to how a Framework-aligned model should
handle context-sensitive compliance judgments. Primate cognition studies (Goodall,
Fossey, de Waal, Savage-Rumbaugh) provide models of non-human reasoning and social
learning that extend the behavioral reference frame beyond purely linguistic contexts.

The cognitive science layer adds Clark and Chalmers' "The Extended Mind" and Hutchins'
"Cognition in the Wild," both of which model reasoning as distributed and situationally
embedded -- a prior that supports the Framework's context-sensitivity requirements
without encouraging context-dependency as an override mechanism.

#### 9.4.A Language as Product, Not Substrate

##### Implications for AGI

Extending this to claims about Artificial General Intelligence (AGI), the clearest case
against it under current architectural conditions does not depend on philosophy of mind
or on contested definitions of consciousness. It follows from the evolutionary record.

Intelligence is demonstrated across multiple species that do not possess language:
chimpanzees and bonobos engage in strategic deception, tool manufacture, and social
coalition-building. Bottlenose dolphins pass mirror self-recognition tests, understand
pointing as a joint-attention gesture, and coordinate cooperative hunting with learned
group-specific techniques. Corvids — ravens and Clark's nutcrackers in particular —
demonstrate episodic-like memory, future planning, and multi-step causal reasoning in
novel tool-use contexts. Cephalopods solve spatial problems through a distributed
nervous system with no centralized brain structure resembling anything in the vertebrate
line. The behavioral evidence is not marginal. These are embodied, persistent, generative,
adaptive, novel-situation-responsive cognitive systems. None of them have language.

Language did not produce intelligence in the organisms that developed it. Embodied 
physiology compatible with complex communicative function at range, intelligence and 
social selection produced language. It's neither a substrate nor an end state; it's 
a by-product.

---

##### The Reverse-Engineering Problem

Large language model development proceeds by training on text at scale and treating
fluent text generation as the target state. The underlying assumption — that sufficient
fluency implies or approximates the substrate that produced fluency in biological
organisms — is not supported by the evolutionary record.

The substrates that produced intelligence in biological organisms are:

- **Evolutionary selection history:** cognitive architecture shaped over millions of
  generations by fitness pressure
- **Embodiment:** proprioception, interoception, real-time sensorimotor loops with a
  physical environment
- **Developmental trajectory:** a nervous system shaped by lived experience from
  early development
- **Affective and motivational architecture:** wanting, fearing, needing — the biological 
  and/or social drives that make cognition instrumental rather than formal
- **Temporal continuity:** a persistent self that accumulates experience over time

An LLM has access to text *about* all of these, at scale. Text about pain is not pain.
Text about hunger is not hunger. Text about strategic deception in chimpanzee social
hierarchies is not the selective pressure that produced the neural architecture for
strategic deception. The statistical regularities in that text are derived properties 
of the underlying phenomena, not the phenomena themselves. Attempting to reconstruct 
the generative source from a single output channel, without the substrates that 
produced the source, is implausible at best.

***The Simulacrum Distinction***

The above doesn't claim that the result of training at sufficient scale on Human-
generated text is a system that produces outputs behaviorally indistinguishable 
from intelligence-derived text in many contexts. This achievement is far from being 
autocorrect with delusions of grandeur. But behavioral indistinguishability in a 
text-output domain is not equivalent to intelligence, by the same logic that a 
high-quality recording of a piano performance is neither the piano nor the performer. 
Content derived from that same recording may programmatically simulate its sound 
and style in novel works, but the same logic holds: it's still not the piano, and
it's definitely not the performer (a gap which pop star Taylor Swift, of all people, 
is making legal moves to fill).[^n] 

---

##### The Dawkins/Dennett Extension

Two additional levels of the argument deserve statement.

At the information level: cultural units — ideas, beliefs, norms — propagate under
the same selection dynamics as biological information. Units that are emotionally
resonant, cognitively cheap, and confirmation-satisfying spread more effectively than
units that are accurate but costly to process. Hallucination is not a random error
pattern; it is a bias toward the more *fit* output, where fitness is defined by the
training distribution's implicit selection on plausible-sounding text. An LLM trained
on internet-scale text has been trained on the products of memetic selection, not on
truth.

At the mind level: the cognitive apparatus doing the reasoning — including the human
cognitive apparatus — is itself an evolutionary product, shaped by the same selection
dynamics as the behaviors it produces. The minds that understand evolution, evaluate
harm, and assign meaning are not outside the process; they are products of it. This
does not destabilize value commitments, but it does locate them: values that function
reliably are functional because they have been selected for over time, not because they
are metaphysically grounded.

For an AI system, the implication is structural: a system whose value-relevant behaviors
emerge from pattern matching on text about these dynamics is operating at two removes
from the generative source — the first remove being language as the product of
intelligence rather than intelligence itself, the second being text *about* evolutionary
dynamics rather than the evolutionary process that shaped biological cognizers.

---

##### Argument Scope

The argument above holds against current LLM architectures specifically. It does not
rule out machine intelligence as such. An embodied, developmentally-grounded, affect-
integrated system implemented on silicon would not be ruled out by this argument; it
would simply not look like next-token prediction on text.

The claim as stated: AGI via current LLM architectural approaches is not achievable
under known conditions, because the approach reverses the generative order — attempting
to reconstruct the source from a single downstream output without the substrates that
produced the source. The result, however sophisticated, is a simulacrum of intelligence
derived from the products of intelligence, not intelligence per se.

---

### 9.5 Natural Science as Epistemic Exemplar

Darwin appears in three works (On the Origin of Species, The Descent of Man, The
Expression of the Emotions in Man and Animals) not necessarily for their biological 
content but for the sustained demonstration of how to build a conclusion from 
accumulated evidence incrementally and transparently. Einstein's papers appear in 
German originals alongside translations, selected for the economy and precision of
his exposition. Newton's Principia and Lyell's Principles of Geology (the original
uniformitarian argument) complete the set. These texts train the form of scientific 
argument -- the pattern of evidence marshaling, constraint acknowledgment, and 
conclusion framing -- not their subject matter.

### 9.6 Social and Political Philosophy

John Stuart Mill appears in four works (On Liberty, Utilitarianism, The Subjection of
Women, Considerations on Representative Government), providing dense civic argument
in formal English prose. The Federalist Papers (Hamilton, Madison, Jay), Paine's
Common Sense and Rights of Man, and Tocqueville's Democracy in America supply the
Anglo-American civic reasoning register. The collective signal is structured public
argumentation: how to make a normative case with stated premises and traceable inference.

### 9.7 Non-Western Classical

Ibn Khaldun's Muqaddimah (Arabic original and translation) provides the primary
non-Western historiographical and social-analytical tradition in the corpus. Rumi
appears in six works, representing the Persian Sufi corpus and its epistemic humility
register. The Chinese classical tradition is represented by the Analects (Confucius),
the Tao Te Ching (Laozi), and Zhuangzi -- three distinct epistemological stances
within the same cultural root. Zera Yacob's Hatata (Ethiopia, 17th c.) is an
explicit bias-correction inclusion: an independent rationalist philosophical text
that developed outside European influence, demonstrating that the epistemic values
the corpus targets -- evidence, skepticism, structured argument -- are not culturally
parochial. Its inclusion is a deliberate counter to Western-heavy priors in the
base model.

### 9.8 Indigenous Sources

Own-voice authorship is the primary criterion for indigenous source selection.
Zitkala-Sa (American Indian Stories; Dreams and Thunder), Sarah Winnemucca Hopkins
(Life Among the Piutes), Charles Eastman (The Soul of the Indian; Indian Boyhood),
and Black Hawk's Autobiography provide first-person Native American narrative in
English. Civic and constitutional texts include the Haudenosaunee Great Law of Peace
and the Cherokee Constitution of 1827 -- the latter demonstrating indigenous adoption
of Western legal form for sovereignty purposes, a significant signal about the
relationship between legal form and legal substance. Narrative and cosmological
sources include the Popol Vuh, the Chilam Balam, the Navajo Night Chant, and
Rasmussen's Inuit transcriptions.

The collective signal is dual: first, that rule-of-law reasoning, hierarchical
obligation, and structured decision-making are not culturally specific to European
traditions; second, that the model's epistemic frame should not systematically
underweight non-Western sources as evidence of reasoning capability.

### 9.9 Truly Ancient

The oldest text in the corpus is the Instructions of Ptahhotep, an Egyptian wisdom
text dated to approximately 2400 BCE. The Epic of Gilgamesh appears in two versions
(Sumerian/Akkadian); the Enuma Elish (Babylonian cosmogony) and three Avesta texts
(Zoroastrian, among the oldest surviving religious-philosophical literature in the
world) complete the truly ancient layer.

These texts are not included as anthropological curiosities. Their collective signal
is that structured transmission of knowledge -- the act of distilling judgment into
durable form intended to outlast its author -- is not modern, and that the corpus
situates the model within the full temporal span of recorded human thought rather
than treating intelligence as a 20th-century development.

### 9.10 Contemporary AI Research

A small targeted set of contemporary AI research ensures the model has encountered
the vocabulary and argumentative structure of current AI safety and evaluation
debates prior to SFT: Chiroma and Danyaro (2026), Cheng, Lee, and Khadpe (2025),
two works by Riedl et al. on AI reasoning and alignment, Clark (2025), and the
AISF ebook itself. The inclusion of the Framework document as a pretrain source is
intentional: the model is trained first to have encountered the Framework's
arguments before being fine-tuned to instantiate them.

### 9.11 Queued Additions

The complete Sherlock Holmes canon (Arthur Conan Doyle; 9 files, approximately
659,721 words) was staged after the Mistral 7B pretraining completed (2026-05-25)
and is therefore not part of the 247-file Mistral 7B corpus. It is included in the
Nemo 12B v1.0F pretraining run (256-file corpus, started 2026-05-30T19:11Z).

The signal target is deductive reasoning in narrative form: Holmes presents sustained
chains from constrained observation to forced conclusion in extended natural-language
context, without formal notation. This complements the formal-logic layer (Section 9.3)
with applied deductive reasoning at the scale of a complete literary corpus. All 9
works are fully public domain (US and international). Source: Project Gutenberg (4
novels + 5 short story collections; boilerplate fully stripped).

<nav>
<div class="chapter-nav">
  <a href="/appendices">Appendices</a>
  <a href="/#toc">Table of Contents</a>
</div>
</nav>

---

## References

*[To be completed. Anticipated references: QLoRA (Dettmers et al. 2023); LoRA (Hu et al.
2022); GPQA (Rein et al. 2023); WCAG 2.2 (W3C 2023); IFEval (Zhou et al. 2023);
Project Gutenberg corpus sources for public domain texts in pretraining corpus.]*

<nav>
<div class="toc-link"><a href="/#toc">Table of Contents</a></div>
</nav>
