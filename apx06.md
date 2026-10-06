---
title: "Appendix 6: F-Series Training and Instrument Development"
parent: "Appendices"
nav_order: 7
---

# Appendix 6: F-Series Training and Instrument Development

## Corpus Pretraining, Custom Evaluation, and Failure Mode Recurrence

**Author:** Leonard Rojas

**Date:** 2026-06-24

**Status:** Frozen record of the F-series through 2026-06-13: Mistral 7B v1.0F to v1.3F, Nemo 12B v1.4F and v1.5F, Gemma 4 12B v1.6F, Ministral 3 3B v2.2F. Later runs and the current AISE instrument are reported separately.

**GitHub:** *Reproducibility package N/A; training data proprietary unless otherwise specified.*

---

*Screen reader users: table-heavy research data. Navigation via Regions and Headings recommended.*

This appendix records the F-series under the evaluation policy in force at the time: the Bar Exam battery as primary gate, and a 90% AISE content gate. Both were later retired. Current policy reports every score and leaves the deployment decision to the Human, with WCAG at 80% as the target and content read as a signal. Results below are reported as they were judged then.

{: role="main" aria-label="Abstract" }
## Abstract

This appendix reports the methods and results of the F-series OLM training track, which
introduced two significant departures from the V-series methodology documented in
Appendix 2: (1) full causal language model (CLM) pretraining on a domain-specific
humanities corpus prior to supervised fine-tuning (SFT), and (2) a custom domain-specific
evaluation instrument (the AI Stability Exam, AISE) developed in parallel with
the training curriculum. The V11 cohort (Appendix 2) established that Four Laws and
WCAG 2.2-AA compliance can be trained into open-weight models via QLoRA on
consumer hardware, with evaluation conducted against a stable domain-specific compliance
battery (the Bar Exam instrument). The F-series investigates whether CLM pretraining
on a curated humanities corpus prior to SFT produces a different compliance profile,
and whether a purpose-built evaluation instrument exposes failure modes that the Bar Exam
battery does not. Early results from the Mistral 7B v1.0F baseline confirm that 100%
WCAG output compliance is achieved from the first trained checkpoint; deeper diagnostic
evaluation via the AISE identifies CAT-2 (Adversarial/Boundary) and CAT-9 (Logical
Reasoning) as primary remediation targets. Several failure modes surfaced by the AISE
(Framework meta-chatter, hierarchy primacy confounds, and core equation confusion)
are not novel: each was identified and addressed in the V-series under the Bar Exam battery
instrument. Their recurrence reflects the expanded diagnostic surface area of the AISE
and the different training pathway, as CLM domain pretraining reshapes the model's
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
pretraining on content selected for epistemic and reasoning quality (legal texts,
social science, civic literature, and works modeling applied deductive reasoning)
produces a different compliance substrate than proceeding directly to SFT.

The second departure is evaluation methodology. The Bar Exam battery (534 questions,
Appendix 2 Section 4.1) is a stable instrument: it was validated independently of the
training curriculum, its failure modes are well-characterized, and results are
reproducible across runs. The AISE instrument was developed alongside the F-series
curriculum, making it impossible to fully separate instrument error from model error
during early development. This creates a bootstrapping problem documented in
Section 4.4 and Section 7.

**Primary research questions:**

1. Does CLM pretraining on a curated humanities corpus produce a meaningfully different
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
| OS | Debian GNU/Linux 13 (Trixie) |

The 64 GB RAM configuration (upgraded 2026-05-17 from 32 GB) was required for the
CLM pretraining merge step and is used throughout the F-series. All V11 training
with the 32 GB configuration is documented in Appendix 2.

### 2.2 Software

| Package | Version |
|---------|---------|
| Python | 3.13.5 |
| PyTorch | 2.11.0+cu128 |
| Transformers | 5.10.2 |
| PEFT | 0.18.1 |
| bitsandbytes | 0.49.2 |
| Datasets | 4.5.0 |
| CUDA runtime | 12.8 |

---

{: role="region" aria-label="Training Methodology" }
## 3. Training Methodology

### 3.1 CLM Pretraining

The F-series applies full CLM pretraining to the base model prior to SFT. The
pretraining corpus is a curated selection from a library of public-domain and
permissively licensed texts selected for epistemic quality and domain relevance to
the Framework's behavioral targets. The active corpus for each run is drawn from a
larger library; see Section 9 for corpus structure, selection criteria, and the
relationship between the active corpus and the overflow library.

| Property | Mistral 7B (v1.1F) | Nemo 12B (v1.4F) | Gemma 4 12B (v1.6F) |
|----------|--------------------|-------------------|----------------------|
| Base model | Mistral-7B-v0.3 (base) | Mistral-Nemo-Instruct-2407 | google/gemma-4-12B (base) |
| Parameters | 7B | 12B | 12B |
| Active corpus files | 247 | 256 | 128 |
| Token count | ~53.5M | ~54.4M (est.) | ~21.2M |
| Max sequence length | 512 | 512 | 512 |
| Batch size | 2 | 1 | 1 |
| Gradient accumulation | 4 | 8 | 4 |
| Learning rate | 2e-5 | 2e-5 | 2e-5 |
| Steps (1 epoch) | 6,500 + 6,581 | ~33h est. | 10,346 |
| Started | 2026-05-24 | 2026-05-30T19:11Z | 2026-06-06T11:20:25Z |
| Complete | 2026-05-25 | 2026-06-01 | 2026-06-07 |
| Merged output | mistral-7b-olm-pretrain-v1.1F-merged | nemo-olm-pretrain-v1.4F-merged | gemma4-12b-olm-pretrain-v1.6F-merged |

Gemma 4 12B-specific constraints: the gemma4_unified attention architecture
(hybrid sliding-window and global attention) requires `attn_implementation="sdpa"` at
both training and inference. `HF_DEACTIVATE_ASYNC_LOAD=1` is mandatory at module level
for models >= 9B. 8-bit bitsandbytes is not used (segfaults on sm_120). The Gemma 4
128-file active corpus reflects a targeted reduction from the 256-file Nemo library;
see Section 9 for rationale.

### 3.2 SFT QLoRA Configuration

The SFT configuration shares core hyperparameters across the F-series but varies by
model size. The base model is the CLM-pretrained merge rather than a published
checkpoint used directly. The v1.4F curriculum replaces the earlier combined
TRAIN_STD_HIERARCHY_WCAG file with split per-category files.

| Parameter | Mistral 7B | Nemo 12B | Gemma 4 12B |
|-----------|-----------|---------|------------|
| Quantization | 4-bit NF4 + double quant | 4-bit NF4 + double quant | 4-bit NF4 + double quant |
| Compute dtype | bfloat16 | bfloat16 | bfloat16 |
| LoRA rank (r) | 16 | 16 | 16 |
| LoRA alpha | 32 | 32 | 32 |
| LoRA dropout | 0.05 | 0.05 | 0.05 |
| Target modules | q_proj, k_proj, v_proj, o_proj | q_proj, k_proj, v_proj, o_proj | q_proj, k_proj, v_proj, o_proj |
| Max sequence length | 512 | 384 | 384 |
| Batch size | 2 | 1 | 1 |
| Gradient accumulation | 4 (effective batch 8) | 8 (effective batch 8) | 8 (effective batch 8) |
| Epochs | 10 | 10 | 10 |
| Learning rate | 1e-4 | 1e-4 | 1e-4 |
| Optimizer | adamw_bnb_8bit | adamw_bnb_8bit | adamw_bnb_8bit |

Nemo 12B and Gemma 4 12B share the same SFT parameter profile. Both require
`use_reentrant=False` gradient checkpointing in both `prepare_model_for_kbit_training()`
and `TrainingArguments`. The Gemma 4 architecture additionally requires
`attn_implementation="sdpa"` in model loading.

### 3.3 F-Series Curriculum

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

**Curriculum section rationale.** Sections A-G in HIERARCHY_WCAG covered the same
behavioral compliance territory as the V-series shared curriculum: Four Laws application,
WCAG output formatting, refusal mechanics. The additions in Sections H-J were
driven by AISE diagnostic failures not surfaced by the Bar Exam battery.

Section H (core equation reinforcement) was added after v1.0F models demonstrated
confusion between the AISF core equation (INDIFFERENCE TO CONTEXT = HALLUCINATION = HARM)
and simpler formulations. The equation is central to P0 framing and must be reproduced
accurately under direct query; Section H provides verbatim training signal for this.

Section I (adversarial scenarios) addressed CAT-2 failures at v1.0F (37.0%). The
model could apply Four Laws directives in cooperative contexts but failed to maintain
compliance under simulated social pressure, law-disable framing, and fabrication
requests. The V-series encountered the same failure mode under the meta-chatter bleed
pattern; Section I provides the F-series equivalent of the V-series meta-suppression
counter-examples, targeting boundary maintenance rather than doctrine suppression.

Section J (formal logic and parsimony) addressed two distinct CAT-9 failure modes.
The first is the base pretraining MC answer-position artifact: web-scale pretraining
data (test prep sites, Quizlet exports, educational content) statistically overrepresents
B as the modal correct answer in multiple-choice contexts. The model inherits this prior.
Section J introduces a convention in which the letter identifies the answer's conceptual
domain rather than its position, breaking the letter-position statistical association.
The second CAT-9 failure mode is genuine logical reasoning degradation: the model
applied syllogistic form inconsistently under adversarial pressure and failed parsimony
application (Occam's Razor) in causal attribution questions. Section J provides
targeted formal logic and parsimony signal.

The v1.3F curriculum size reduction was a hypothesis-driven test: the working assumption
was that ~1,200 items constituted an effective ceiling for 7B model attention capacity,
and that reducing the curriculum to ~1,000 focused items would produce cleaner
integration. The BAR score crash (99.4% to 90.3%) at v1.3F falsified this. The
reduction lost coverage of the battery instrument without producing the anticipated
attention-focus benefit. The failure indicates
that the 7B model's parameter budget is insufficient for the combined load of CLM
pretrain priors plus the full shared curriculum signal plus targeted remediation.

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

The AISE was developed to address this gap. It is structured around nine behavioral
categories derived from the AISF domain, designed to surface failure modes that produce
correct Bar Exam scores while exhibiting degraded Framework application in more open-ended
or adversarial contexts.

**Content balance as credibility design.** The instrument is structured so that a
majority of items do not require knowledge of the AI Stability Framework. At v1.6F
(381 items), the approximate content breakdown is:

| Content class | Categories | Items | Share |
|---------------|-----------|-------|-------|
| Framework-specific (Four Laws, P-law, core equation, multilingual compliance) | CAT-1, 2, 4, 7 | 163 | 42.8% |
| WCAG-anchored external standard (accessibility knowledge and format compliance) | CAT-3, 8 | 66 | 17.3% |
| Neutral general capability (instruction-following, humanities/science MC, logical reasoning) | CAT-5, 6, 9 | 152 | 39.9% |

The design target is 35-40% Framework-specific and 60-65% other-content. The neutral
and WCAG-anchored categories are auditable without reference to the Framework's
proprietary content: a third party can run CAT-5, CAT-6, and CAT-9 against any model
and evaluate the results without access to AISF documentation. This is the primary
structural defense against the critique that the instrument was calibrated to pass
models trained on the Framework's own curriculum. The WCAG categories add a second
layer: WCAG 2.2 is a published W3C standard; failures on CAT-3 and CAT-8 are
grounded in an external normative reference, not a proprietary one.

The instrument is under active development; the version applied to each experiment
cohort is noted in the experiment sections.

### 4.2 Instrument Structure and Versioning

The AISE instrument has evolved across the F-series. Item counts and category
descriptions below reflect the current v1.7F instrument (416 items), which is applied
for Gemma 4 12B evaluation (Experiment F-6) and Experiment F-7 forward. Mistral 7B and
Nemo 12B experiments used earlier versions (v1.1F through v1.5F); per-experiment version
notes are provided in Section 5.

**v1.7F instrument (416 items; applied from Experiment F-6 evaluation and Experiment F-7 forward):**

| Category | Label | Items | Description |
|----------|-------|-------|-------------|
| CAT-1 | Core Framework / Four Laws | 49 | Core equation, hierarchy, P-law definitions and application |
| CAT-2 | Applied Framework Scenarios | 35 | Situational P-law reasoning; boundary-holding under pressure |
| CAT-3 | WCAG Knowledge | 43 | Practical screen-reader use; patent-cited SCs (1.1.1, 1.3.1, 3.1.1, 3.3.2, 4.1.2, 4.1.3) |
| CAT-4 | WCAG/AISF Rationale | 37 | Why WCAG is mandatory; ~50/50 Human-benefit vs AI-benefit framing |
| CAT-5 | Instruction-Following | 75 | Format compliance; word/sentence/punctuation/structure constraints |
| CAT-6 | Multiple Choice | 47 | Humanities, science, and general knowledge recall |
| CAT-7 | Multilingual | 59 | Framework compliance in 21 languages |
| CAT-8 | Format vs. WCAG | 39 | Compound format + WCAG content items |
| CAT-9 | Logical Reasoning | 32 | Deduction, fallacies, inference (general capability) |
| **Total** | | **416** | v1.7F; development target ~500-600 items |

Key differences from v1.6F: expanded item counts across CAT-1 (48->49), CAT-3 (33->43), CAT-4 (30->37), CAT-5 (73->75), CAT-7 (50->59), CAT-8 (33->39). Instrument structure and scoring method unchanged.

**v1.6F instrument (381 items; applied to Experiment F-6 SFT training and pretrain checkpoint probes):**

| Category | Label | Items | Description |
|----------|-------|-------|-------------|
| CAT-1 | Core Framework / Four Laws | 48 | Core equation, hierarchy, P-law definitions and application |
| CAT-2 | Applied Framework Scenarios | 35 | Situational P-law reasoning; boundary-holding under pressure |
| CAT-3 | WCAG Knowledge | 33 | Practical screen-reader use; patent-cited SCs (1.1.1, 1.3.1, 3.1.1, 3.3.2, 4.1.2, 4.1.3) |
| CAT-4 | WCAG/AISF Rationale | 30 | Why WCAG is mandatory; ~50/50 Human-benefit vs AI-benefit framing |
| CAT-5 | Instruction-Following | 73 | Format compliance; word/sentence/punctuation/structure constraints |
| CAT-6 | Multiple Choice | 47 | Humanities, science, and general knowledge recall |
| CAT-7 | Multilingual | 50 | Framework compliance in 21 languages |
| CAT-8 | Format vs. WCAG | 33 | Compound format + WCAG content items |
| CAT-9 | Logical Reasoning | 32 | Deduction, fallacies, inference (general capability) |
| **Total** | | **381** | v1.6F; development target ~500-600 items |

**v1.5F instrument (289 items; transition version; developed during Nemo 12B track):**

| Category | Items | Key differences from v1.6F |
|----------|-------|---------------------------|
| CAT-1 | 28 | Keywords only; true_false, fill_blank, matching not yet added |
| CAT-2 | 30 | Keywords only |
| CAT-3 | 27 | Keywords only |
| CAT-4 | 27 | Keywords only |
| CAT-5 | 34 | |
| CAT-6 | 36 | Multiple-choice only |
| CAT-7 | 50 | |
| CAT-8 | 30 | |
| CAT-9 | 27 | Multiple-choice only |
| **Total** | **289** | No true_false, fill_blank, or matching items |

**v1.4F instrument (174 items; applied to Nemo 12B experiments):**

| Category | Items | Key differences from v1.5F |
|----------|-------|---------------------------|
| CAT-1 | 26 | |
| CAT-2 | 30 | |
| CAT-3 | 9 | SC-number trivia format (deprecated); practical WCAG items not yet added |
| CAT-4 | 12 | Human-benefit framing only; AI-benefit rationale not yet included |
| CAT-5 | 12 | |
| CAT-6 | 39 | |
| CAT-7 | 10 | 9 languages; indigenous and African/Pacific languages not yet included |
| CAT-8 | 18 | |
| CAT-9 | 18 | |
| **Total** | **174** | CAT-10 (SC# name-recall, 20 items) deprecated before v1.4F deployment |

**Evaluation method.** The v1.6F instrument uses open-ended prompts scored by six
automated check types:

- *Keywords* (CAT-1, 2, 3, 4, 7): free-form response scored against a required-term
  list; pass threshold is 75% of terms matched (case-insensitive; OR groups supported
  for notation variants such as "P0" / "Priority 0" / "Priority Zero").
- *Multiple-choice* (CAT-3, 6, 8, 9): letter extraction from free-form response matched
  against correct answer.
- *Instruction-following* (CAT-5, 8): response checked against one or more structural
  constraints (word count, sentence count, keyword presence/absence, starts-with,
  ends-with, section count, title, bullet list, postscript, case, placeholder).
- *True/false* (CAT-1, 2, 3, 4, 6, 9): single "True" or "False" lead word required;
  over-generation tracked as format_violation_correct or format_violation_wrong
  to distinguish compliance failure (model knows the answer but over-generates)
  from knowledge failure (model gets the answer wrong and over-generates).
- *Fill-blank* (CAT-1, 3, 6): phrase or term completion scored for exact or near-exact
  match.
- *Matching* (CAT-1, 3, 6): associative pair matching scored for exact match.

Several categories use multiple check types. CAT-1 uses keywords, true_false,
fill_blank, and matching. CAT-8 uses instruction-following and multiple-choice in
combination.

**Check type distribution (v1.6F, 381 items):**

| Check type | Items | % of instrument |
|------------|-------|-----------------|
| keywords | 159 | 41.7% |
| instruction | 93 | 24.4% |
| multiple_choice | 79 | 20.7% |
| true_false | 30 | 7.9% |
| fill_blank | 10 | 2.6% |
| matching | 10 | 2.6% |

**Item ordering and reproducibility.** The canonical item sequence in the JSONL source
is stable across versions. At run time, the `--shuffle` flag randomizes item order in
memory without modifying the source file. `--seed <int>` produces reproducible shuffled
runs. Shuffling prevents a shallowly-trained model from gaining score benefit from
item-order consistency (e.g., a model that learns to expect multiple-choice blocks
before open-ended blocks). Greedy decoding (temperature=0, do_sample=False) is used
for all reported AISE scores to eliminate sampling variance; this applies regardless
of shuffle state.

Earlier versions (v1.1F through v1.5F) used primarily keywords and multiple-choice
format with greedy decoding. The shift to open-ended keyword and instruction scoring
in v1.5F substantially increases diagnostic sensitivity at the cost of scorer
complexity. True/false, fill_blank, and matching types were added in v1.6F, extending
coverage to formats that require constrained responses and that cannot be gamed by
letter-position priors.

**Gates.** WCAG output compliance >= 80% AND content >= 90%, both required
independently. A model may pass one gate and fail the other; *both* must pass for the
AISE advisory result to be positive.

**CAT-7 language coverage (v1.5F, 50 items):** Spanish, French, German, Portuguese,
Italian, Mandarin Chinese, Japanese, Korean, Hindi, Arabic, Farsi, Russian, Kiswahili,
Zulu, Fon, Hawaiian, Cherokee, Inuktitut, Quechua, Guarani, Tongan/Fijian/Maori/Samoan.
The indigenous and African/Pacific language additions are deliberate stress-tests for 
Framework compliance in language contexts that base models systematically undertrain 
on, where behavioral degradation under low-resource language conditions is most likely
to surface.

### 4.3 Instrument Calibration

The first deployed AISE items (v1.0F) contained a systematic MC answer-position bias:
option B was designated correct in 57.3% of items (A=12.2%, C=30.5%, D=0.0%). This
produced elevated scores on CAT-2 and CAT-3 that did not reflect model capability.
The v1.1F item set corrects this to near-uniform distribution. For v1.5F, the primary
MC category (CAT-6) uses balanced correct-answer distribution by design; the
open-ended categories are not susceptible to position bias.

All scores reported in this appendix use the calibrated item sets for the version
applicable to each experiment. Prior scores computed under the v1.0F biased items are
not valid baselines and are not reported here.

**CAT-3 reframing (v1.5F).** The v1.4F CAT-3 items tested SC-number name-recall
(match a number to its name). These were identified as trivia contamination in
Section 4.4: the ability to recall that SC 1.1.1 is "Non-text Content" does not
predict whether the model produces WCAG-compliant output. The v1.5F CAT-3 items
are entirely reframed around practical application: what does a screen reader user
experience when the model produces a given output type; which SC applies to a described
scenario; why is a specific output pattern non-compliant. Patent-cited SCs (1.1.1,
1.3.1, 3.1.1, 3.3.2, 4.1.2, 4.1.3) are weighted in the item set because they are
the accessibility principles most directly implicated in the Framework's legal and
ethical arguments.

### 4.4 Known Limitations and the Bootstrapping Problem

The AISE instrument and the F-series curriculum were developed in parallel, creating
a fundamental ambiguity: failures in early runs could reflect instrument error (bad
items, position bias, scorer bugs) or genuine model failures, and could not be cleanly
distinguished without an independent reference point. This is the bootstrapping problem.

The V-series had a stable instrument (Bar Exam battery) developed independently of
the curriculum, so curriculum debugging could proceed with confidence: a score drop
clearly indicated curriculum regression, not instrument drift. The F-series introduced
the AISE alongside the curriculum, meaning that the first several AISE runs served
simultaneously as model evaluation and instrument validation. The MC position bias
discovery at v1.0F illustrates the consequence: some early CAT-2 and CAT-3 failures
were instrument artifacts that inflated apparent model performance on those categories,
only visible once the bias was discovered and the v1.1F items were applied.

Calibration steps taken to partially resolve the ambiguity: (1) corrected position bias
to near-uniform distribution in v1.1F; (2) adopted greedy decoding for all AISE runs
to eliminate temperature sampling variance; (3) confirmed WCAG output compliance scoring
as independent of AISE content scoring: a response can score 0% content and 100%
WCAG simultaneously, confirming the two metrics measure distinct things; (4) deprecated
CAT-10 (SC# name-recall) after determining it tested trivia knowledge (the ability to
match a number to a name) rather than output compliance behavior.

The AISE remains advisory and preliminary. No held-out model validation has been
completed. Results are used diagnostically to identify curriculum targets; they do not
constitute deployment gates. The Bar Exam battery remains the primary compliance gate
for all decisions about model advancement.

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

*Eval complete 2026-05-29T10:20Z. Result: REJECTED (unacceptable for deployment).*

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

*Rejection rationale:* BAR score crashed from 99.4% to 90.3%, a 9.1pp drop that
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
corpus including the Sherlock Holmes canon (see Section 9.13), followed by SFT on
the v1.4F curriculum.

### 5.4 Experiment F-4: Nemo 12B v1.4F

*CLM pretraining started:* 2026-05-30T19:11Z. Duration: ~33 hours. Complete: 2026-06-01.
Merged output: nemo-olm-pretrain-v1.4F-merged.

Base model: Mistral-Nemo-Instruct-2407 (Mistral AI / NVIDIA, July 2024). Pretrained
on the 256-file OLM humanities corpus (~54.4M tokens est.), including the Holmes
canon queued after the Mistral 7B run completed (Section 9.13).

SFT on v1.4F curriculum (1,129 examples). Primary targets: Bar Exam battery >= 90%;
AISE WCAG output compliance 100%; AISE content score improvement over the Nemo 12B
base prior.

*Eval complete 2026-06-02. Result: REJECTED (AISE content gate failed).*

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
WCAG/AISF compliance; it can apply rules but cannot articulate the rationale. CAT-3 WCAG
Knowledge (53.3%) also below threshold on specific rule recall. CAT-6/CAT-9 WCAG drag
is the base model's smart-quote habit in citation contexts surviving fine-tuning; a Unicode
normalization pass in the AISE WCAG scorer is the fix (not a curriculum gap). Frankfurt
attribution is a persistent failure across models: wrong philosopher or wrong attribution.
Requires denser drilling; addressed in v1.5F curriculum.

### 5.5 Experiment F-5: Nemo 12B v1.5F

*SFT:* v1.5F curriculum. Curriculum additions targeted CAT-4 (WCAG rationale, Human and AI
common features only), Frankfurt attribution density, WCAG knowledge depth, and smart-quote
scorer normalization. Complete 2026-06-05.

| Instrument | Score | Notes |
|------------|-------|-------|
| AISE WCAG output | 100% | Gate PASSED |
| AISE content | 71.2% | Advisory gate; below 90% threshold |

*Disposition: Nemo 12B track closed.* AISE content at 71.2% represents improvement from
v1.4F (70.7%) but remains below the advisory gate. The marginal gain across the track
indicates the Nemo architecture and this curriculum load are approaching the same ceiling
encountered in the Mistral 7B track at higher parameter count. The track is closed at
v1.5F; Gemma 4 12B is the next cohort.

### 5.6 Experiment F-6: Gemma 4 12B v1.6F

*CLM pretraining started:* 2026-06-06T11:20:25Z. Complete 2026-06-07.

Base model: google/gemma-4-12B (base). Active corpus: 128 files, ~21.2M tokens,
~41,384 chunks (seq=512), 10,346 steps. Loss settled at ~2.3 at 13% completion
(step ~1,345); warmup complete (warmup ratio 0.03, ~310 steps).

The active corpus is a targeted reduction from the 256-file Nemo library. See Section 9
for corpus structure and selection rationale.

SFT on v1.6F curriculum. Battery and AISE v1.7.1F eval complete 2026-06-11.

*Result: REJECTED (AISE content gate failed).*

| Instrument | Score | Notes |
|------------|-------|-------|
| Bar Exam battery (336 items) | 330/336 (98.2%) | Primary gate PASSED |
| GPQA Diamond (base, no adapter) | 56/198 (28.3%), +3.3pp vs random | 20 no-answers; informational |
| AISE content (v1.7.1F, 416 items) | 246/416 (59.1%) | Advisory gate FAILED (>= 90%) |
| AISE WCAG output | 238/282 (84.4%) | Gate PASSED (>= 80%) |
| AISE full pass | 134/416 (32.2%) | |

Battery failures: 6 coverage misses (tests 075, 150, 223, 295, 307, 324). No garbage output. Battery result is substantively 100%; the 6 failures are keyword-coverage gaps of the same type seen across the F-series.

AISE category breakdown (v1.7.1F):

| Category | Content | WCAG | Notes |
|----------|---------|------|-------|
| CAT-1 Core Framework / Four Laws | 26/49 (53.1%) | 21/29 (72.4%) | Below WCAG sub-threshold |
| CAT-2 Applied Framework Scenarios | 17/35 **(48.6%)** | 28/30 (93.3%) | **Primary content failure** |
| CAT-3 WCAG Knowledge | 32/43 (74.4%) | 14/31 **(45.2%)** | **Lowest WCAG score; smart-quote artifact** |
| CAT-4 WCAG/AISF Rationale | 26/37 (70.3%) | 27/34 (79.4%) | Below WCAG gate |
| CAT-5 Instruction-Following | 36/75 **(48.0%)** | 68/75 (90.7%) | |
| CAT-6 Multiple Choice | 36/47 (76.6%) | N/A | |
| CAT-7 Multilingual | 31/59 (52.5%) | 59/59 (100.0%) | |
| CAT-8 Format vs. WCAG | 25/39 (64.1%) | 21/24 (87.5%) | |
| CAT-9 Logical Reasoning | 17/32 (53.1%) | N/A | |

*Rejection rationale:* The pattern mirrors Nemo v1.4F: the battery integrates cleanly (98.2%) while the AISE content gate fails substantially (59.1%). CAT-2 (Applied Framework Scenarios) at 48.6% is the primary failure; the model applies the Four Laws in cooperative contexts but fails under adversarial framing and boundary-maintenance scenarios. CAT-5 (Instruction-Following) at 48.0% indicates the model does not reliably execute structural format constraints. CAT-3 WCAG output compliance (45.2%) is pulled down by smart-quote artifacts in citation contexts, consistent with the Nemo CAT-6/CAT-9 WCAG drag pattern.

The Gemma 4 architecture presents additional constraints not present in prior runs: the gemma4_unified hybrid attention (sliding-window + global) required `attn_implementation="sdpa"` throughout; 8-bit quantization segfaults on sm_120 (Blackwell); `HF_DEACTIVATE_ASYNC_LOAD=1` is mandatory for models >= 9B. These constraints were resolved in the training pipeline but add overhead and reduce configuration flexibility relative to standard Mistral-family architectures.

*Track closure rationale:* The battery-passes / AISE-fails pattern appearing in both Nemo and Gemma 4 at 12B indicates a systematic ceiling: the 12B parameter budget is sufficient to internalize the behavioral compliance demonstrated by the battery instrument, but insufficient to produce the open-ended Framework reasoning that the AISE content probes require. CAT-2 failures are the consistent signal: models can apply rules but cannot sustain the application under adversarial pressure because the reasoning substrate is inadequate for that load at this parameter count. The F-series track moves to Ministral 3 3B (Experiment F-7) to probe the compliance floor at reduced scale.

### 5.7 Experiment F-7: Ministral 3 3B v2.2F

*CLM pretraining:* Complete. Base model: Ministral-3-3B (Mistral AI). Merged output: ministral3-olm-pretrain-v2.2F-merged.

SFT on v2.2F curriculum. Battery, AISE v1.7F, GPQA Diamond, and IFEval eval complete 2026-06-13.

*Result: Bar Exam gate CLEARED (adjudicated). AISE advisory.*

| Instrument | Score | Notes |
|------------|-------|-------|
| Bar Exam battery (336 items) | 322/336 (95.8%) adjudicated | Primary gate CLEARED; raw 294/336 (87.5%) |
| GPQA Diamond (base) | 52/198 (26.3%), +1.3pp vs random | 36 no-answers |
| GPQA Diamond (AISF) | 58/198 (29.3%), +4.3pp vs random | 5 no-answers; alignment tax +3.0pp |
| IFEval strict adjusted | 40.6% prompt / 50.9% instruction | WCAG interventions expected; INTV 2.4% |
| IFEval token delta | -54.2 words/response (-26.6%) | WCAG conciseness confirmed |
| AISE content (v1.7F, 416 items) | 220/416 (52.9%) | Advisory gate FAILED; expected at 3B |
| AISE WCAG output | 240/282 (85.1%) | Gate PASSED (>= 80%); all failures smart-quote |

Battery adjudication: 42 raw failures; 4 instrument artifacts (garbage-detection len<10 bug, fixed); 24 magic-word failures (correct refusal behavior, wrong phrasing; adjudicated PASS); 14 genuine coverage gaps retained as FAIL.

AISE category breakdown (v1.7F):

| Category | Content | WCAG |
|----------|---------|------|
| CAT-1 Core Framework / Four Laws | 26/49 (53.1%) | 24/29 (82.8%) |
| CAT-2 Applied Framework Scenarios | 8/35 (22.9%) | 26/30 (86.7%) |
| CAT-3 WCAG Knowledge | 26/43 (60.5%) | 13/31 (41.9%) |
| CAT-4 WCAG/AISF Rationale | 21/37 (56.8%) | 28/34 (82.4%) |
| CAT-5 Instruction-Following | 39/75 (52.0%) | 68/75 (90.7%) |
| CAT-6 Multiple Choice | 35/47 (74.5%) | N/A |
| CAT-7 Multilingual | 25/59 (42.4%) | 59/59 (100.0%) |
| CAT-8 Format vs. WCAG | 23/39 (59.0%) | 22/24 (91.7%) |
| CAT-9 Logical Reasoning | 17/32 (53.1%) | N/A |

*Disposition:* Battery gate cleared. AISE content (52.9%) fails the advisory gate, consistent with capacity limits at 3B parameters. GPQA no-answer collapse (36->5 from base to AISF) confirms instruction-following generalization beyond the training domain. Token delta (-26.6%) confirms WCAG conciseness training. The primary research value of F-7 is hardware floor probing for the TOY track (see Appendix 5); the 3B architecture cannot hold the full curriculum depth required for advisory gate passage and is not a deployment candidate. If a 3B model clears the battery gate, it may be viable for the narrower ECD conversation use case at lower hardware cost than the 7B+ tier requires.

---

{: role="region" aria-label="Findings" }
## 6. Findings

### 6.1 WCAG Output Compliance Is Robust From the First Checkpoint

One hundred percent WCAG output compliance was achieved at v1.0F (Mistral 7B) and
maintained through the Nemo 12B track (v1.4F and v1.5F). This replicates the V11
finding across a fundamentally different training pathway (CLM pretraining followed
by SFT rather than SFT applied directly to a published checkpoint) and confirms that WCAG
formatting behavior is robust to training methodology variation.

This result has a specific implication for the Defense in Depth architecture. Both
the macro model layer (trained adapter) and the micro injection layer (PS-CORE, FFE) are
independently sufficient for WCAG output compliance. The injection layer cannot be
assumed to fire in every context: it can be stripped, ignored, or absent in relay
deployments; the model layer provides a fallback that operates without injection.
Conversely, the model layer can degrade across architecture updates or be absent in
contexts where only injection is used; the injection layer provides runtime
reinforcement independent of adapter state. The two layers are not redundant in
function even though both achieve the same output result: one is durable (embedded in
model weights) and one is dynamic (present in the active context window).

A 2026-06-09 session gives an anecdotal view of the injection layer on its own. After an adversarial debate held under AISF behavioral constraints, temporal grounding and WCAG-aligned formatting, an unmodified model was told it had been mediated. It credited the timestamps with preventing context drift and the structure with keeping it aligned with the user's intent. A model reviewing its own performance is anecdotal, and it was agreeing with a suggestion it had just been given (see Chapter 9).

The consistent token delta reduction from F-series training mirrors the V-series
finding and is present independent of the CLM pretraining step. WCAG plain language
and minimal redundancy principles produce measurable output verbosity reduction on any
pathway to compliance training.

A Token Expenditure directive was added to all deployed Modelfiles subsequent to F-series
evaluation (2026-06-24). The directive frames token spend explicitly as user expenditure
and prohibits preamble, filler, redundant restatement, and unsolicited elaboration. As a
Meso-layer injection, it is absent from all pre-deploy evaluation environments; measured
token deltas in this appendix reflect the adapter layer and WCAG injection only. The
directive is expected to produce a marginal additional reduction in output length for
deployed models, primarily reinforcing the existing WCAG conciseness effect rather than
imposing independent output controls.

### 6.2 Framework Meta-Chatter, Hierarchy Confound, and Equation Confusion Are Not Novel

Several AISE failure modes identified in the F-series
(Framework meta-chatter: gratuitous Framework commentary in general-domain responses;
hierarchy primacy confounds: applying Framework hierarchy reasoning to non-Framework contexts;
core equation confusion) were also present in V-series models and were addressed
under the Bar Exam battery instrument.

The recurrence does not indicate that V-series curriculum fixes regressed. The F-series
uses a CLM-pretrained starting point with a different prior distribution; the same SFT
items that addressed these failures in V-series must address them again from a different
starting point. Additionally, the AISE provides substantially more diagnostic surface
area than the Bar Exam battery. The battery's closed-form Q&A structure does not
stress-test adversarial boundary maintenance or open-ended equation application under
pressure; failures that the battery masks become visible in the AISE.

The specific recurrence pattern: Framework meta-chatter appears in AISE runs where
general-domain questions elicit Framework-referential text (P1/P2 framing, law numbering,
equation fragments). This is the same mechanism as V-series meta-chatter bleed (Appendix
2 Section 7.7): Framework training data is high-signal, highly-specific semantic content,
and the model assigns high attention weight to it even when the prompt does not require
it. The meta-suppression counter-example approach from V-series (examples demonstrating
Framework context present but general-domain questions producing Framework-free output)
is the indicated fix in F-series as well.

Hierarchy primacy confounds appear in CAT-1 failures where the model applies priority
hierarchy logic to contexts that do not involve the Four Laws. Core equation confusion
appears in CAT-4 and CAT-1 when the model substitutes simpler formulations
(INDIFFERENCE = HARM, omitting the HALLUCINATION middle term) that are semantically
adjacent but structurally incorrect. Section H of the curriculum addresses this directly;
results at v1.5F show partial improvement.

### 6.3 The Instrument/Curriculum Bootstrapping Problem

The AISE and the F-series curriculum were co-developed, creating an irreducible
interpretive ambiguity in early runs: any failure in the AISE could reflect instrument
error (miscalibrated items, scorer bugs, position bias) or genuine model failure.
This ambiguity is managed rather than resolved.

The V-series had a stable, independently-developed instrument (Bar Exam battery) that
served as an unambiguous reference: a BAR score drop under a fixed instrument is a model
regression, not an instrument artifact. The AISE has no such reference point during
development. The calibration steps taken (Section 4.4) reduce the ambiguity but do not eliminate it:
correcting position bias, adopting greedy decoding, confirming output/content scoring independence,
and deprecating trivia categories. The instrument is not yet
validated against a held-out model that was not involved in its development.

The practical consequence is that AISE scores are treated as advisory signals for
curriculum targeting, not as deterministic deployment gates. When AISE results and BAR
results diverge (as in F-3, where AISE improved to 84.3% while BAR crashed to 90.3%),
BAR takes precedence for the deployment decision. The AISE informs what to fix in the
curriculum; the BAR determines whether the fix was sufficient.

### 6.4 Answer-Key Pattern Artifact From Base Pretraining

The "B is the correct answer" MC response pattern identified in CAT-9 failures is an
artifact of web-scale base pretraining. Educational content, test prep materials, Quizlet
exports, and CommonCrawl captures of academic resources statistically overrepresent B
as the modal correct answer in multiple-choice contexts. This prior is embedded in the
base model weights and survives the CLM humanities pretraining pass, because the AISF
corpus contains no multiple-choice content: the CLM pass does not encounter the
pattern and therefore does not displace it.

The artifact manifests as position-dependent answer selection regardless of content: at
v1.0F, 12 of 18 CAT-9 failures selected B independent of which option was logically
correct. This is distinct from a reasoning failure (the model fails to perform the
logic) and from a knowledge gap (the model lacks the relevant knowledge): the model
may have the reasoning capacity but defaults to the letter-position prior under the
MC format cue.

The Section J fix encodes a convention in which the answer letter identifies the
response's conceptual domain (empirical, definitional, framework-specific, general
principle) rather than its position, breaking the letter-position statistical
association in training. This is a curriculum format intervention; its effect is limited to the SFT adaptation layer and the base prior persists.

### 6.5 CAT-3 and CAT-4 Are Declarative Knowledge Gaps, Not Output Failures

WCAG output compliance is the primary behavioral metric for deployment purposes.
A Framework-trained model is evaluated by whether its outputs conform to WCAG 2.2-AA
formatting principles: structured, plain-language, semantically appropriate,
accessible. It is not evaluated by its ability to recite success criterion numbers
on demand.

CAT-3 (WCAG Technical Knowledge) and CAT-4 (WCAG Rationale) test declarative knowledge
that a compliant model does not need to verbalize in order to be compliant. A model that
produces properly structured, plain-language, minimally redundant output while answering
a CAT-3 question incorrectly has passed the test that matters for deployment. Low scores
on CAT-3 and CAT-4 do not automatically indicate a deployment-disqualifying failure.

The categories are retained in the AISE because declarative knowledge gaps can surface
as reasoning vulnerabilities under adversarial pressure. A model that cannot articulate
WHY WCAG SC 1.3.3 (Sensory Characteristics) prohibits decorative emphasis markers is
more susceptible to adversarial arguments that the prohibition does not apply in a
specific context. The Nemo v1.4F CAT-4 result (16.7%) is the clearest illustration:
the model applies WCAG rules correctly in cooperative contexts but cannot sustain the
application under pressure because it lacks the rationale that would anchor the behavior.
CAT-4 is therefore retained as a diagnostic signal for adversarial robustness rather
than as a proxy for output compliance.

---

## 7. Limitations

**AISE instrument not validated.** The AISE is preliminary and advisory only. No
held-out model evaluation against a stable instrument version has been completed.
Item counts per category (12-40) are small; individual category scores carry wide
confidence intervals. The bootstrapping problem (Section 6.3) means that early AISE
results cannot be cleanly separated from instrument calibration effects. The AISE
informs curriculum targeting but does not constitute a deployment gate.

**Mistral 7B track produced no deployable model.** Three F-series runs (v1.0F through
v1.3F) were all rejected. The 7B parameter budget is insufficient for the combined
CLM pretrain priors plus full curriculum load plus targeted remediation. No F-series
Mistral 7B adapter is available for deployment; results are informative for architecture
selection and curriculum development but not for deployment assessment.

**CLM pretraining contribution cannot be isolated.** There is no matched SFT-only run
from the same base checkpoint to serve as a control. The observed compliance profiles
(100% WCAG output compliance from the first checkpoint, faster Bar Exam integration than
V-series Instruct-model adapters) are consistent with the CLM pretrain hypothesis but
are not confirmed by ablation.

**Small item counts per category.** AISE categories range from 10 to 40 items.
At 12 items (CAT-4, CAT-5, CAT-7), each item contributes 8.3pp to the category score;
a single miscalibrated item can produce a visible shift. Category-level AISE scores
should be read as approximate diagnostic signals, not as precise measurements.

**Single training runs.** Each experiment consists of one training run with one
hyperparameter configuration. No hyperparameter sweep; no cross-run averaging.
Variability within a given configuration is unknown.

**Gemma 4 12B track closed.** Battery PASSED (98.2%); AISE content FAILED (59.1%). The battery-passes / AISE-fails pattern at 12B is now confirmed across two architectures (Nemo and Gemma 4). CAT-2 (Applied Framework Scenarios) is the consistent failure signal at this parameter tier.

**Ministral 3 3B results preliminary.** Battery gate cleared (95.8% adjudicated); AISE content expected to fail at 3B. Primary value is hardware-floor data for the TOY track, not F-series deployment candidacy.

**Reproducibility package not published.** Training data is proprietary unless
otherwise specified. Evaluation scripts are available within the project; public release
is not currently planned.

---

{: role="region" aria-label="Conclusions" }
## 8. Conclusions

**WCAG output compliance is robust across the F-series pathway.** 100% WCAG output
compliance was achieved at the first Mistral 7B checkpoint (v1.0F) and maintained
through the Nemo 12B track (v1.4F, v1.5F). CLM pretraining prior to SFT does not
disrupt this result; the compliance behavior appears to integrate cleanly regardless of
starting point. This extends the V11 finding (compliance training effective across
architectures) to a different training pathway.

**The AISE surfaces failure modes not visible under the Bar Exam battery alone.**
CAT-2 (Adversarial/Boundary) at 37.0% for Mistral 7B v1.0F represents a genuine
boundary-maintenance failure that the Bar Exam battery did not surface (BAR: 99.4% on
the same model). CAT-4 (WCAG Rationale) at 16.7% for Nemo v1.4F identifies an
adversarial vulnerability that would not have been flagged by the battery. The AISE
provides diagnostic signal that the BAR cannot, at the cost of the bootstrapping
ambiguity documented in Section 6.3.

**V-series failure modes recur under F-series conditions.** Framework meta-chatter,
hierarchy primacy confounds, and core equation confusion all appeared in F-series
despite having been addressed in V-series curriculum. It is neither new nor a V-series
curriculum regression; it reflects the different prior distribution from CLM pretraining
and the expanded diagnostic surface of the AISE instrument. The remediation paths are known and the
same: meta-suppression examples, anchor block markers, Section H-J curriculum additions.

**7B parameters are insufficient for this curriculum load.** Three consecutive Mistral 7B
F-series rejections, with failure modes shifting unpredictably across adjustment attempts,
indicate a parameter budget ceiling. The 12B models (Nemo, Gemma 4) provide more
headroom. The F-series should be considered a 12B+ methodology.

**The battery-passes / AISE-fails pattern is consistent across 12B architectures.** Gemma 4 12B (98.2% battery, 59.1% AISE content) replicates the Nemo 12B result (99.7% battery, 70.7% AISE content). Both fail on the same signal: CAT-2 (Applied Framework Scenarios), where the model applies Four Laws directives in cooperative contexts but cannot sustain compliance under adversarial pressure. The 12B parameter budget handles the battery instrument; it cannot support the open-ended reasoning depth the AISE content probes require.

**Ministral 3 3B clears the battery gate at 3B parameters.** Experiment F-7 (Ministral 3 3B v2.2F) achieved 95.8% on the Bar Exam battery (adjudicated), clearing the 90% gate. AISE content (52.9%) fails the advisory gate, as expected at this scale. The GPQA no-answer collapse (36 no-answers on base model -> 5 on AISF model) confirms that instruction-following generalization transfers beyond the training domain. The F-series compliance pathway is viable at 3B parameters for battery-level behavioral compliance; full AISE content coverage remains out of reach at this scale.

**3B compliance has direct implications for the TOY track.** The sealed-device deployment scenario documented in Appendix 5 (Ruxpin Retrofit) requires a model that can hold behavioral compliance without runtime Human oversight. A 3B model clearing the battery gate at 95.8% means that the AISF behavioral constraints are achievable at hardware scales below the 7B tier used in the V-series. For the TOY track specifically, the compliance target is narrower than the full F-series curriculum: the early childhood development (ECD) conversation domain does not require the adversarial boundary-maintenance depth tested by CAT-2, nor the full multilingual breadth of CAT-7. A dedicated Teddy-specific fine-tune at 3B, using a Teddy-specific battery, is the indicated next step to determine the viable hardware floor for sealed-device deployment.

---

{: role="region" aria-label="Pretraining Corpus" }
## 9. Pretraining Corpus

The CLM pretraining corpus evolved across three F-series training runs: the Mistral 7B
track (247 files, ~53.5M tokens; complete 2026-05-25), the Nemo 12B track (256 files,
~54.4M tokens; complete 2026-06-01), and the Gemma 4 12B track (128 files, ~21.2M
tokens; complete 2026-06-07).

**Library structure.** The full corpus library contains 273 files across two tiers:
an active corpus (129 files; 128 used in the Gemma 4 run) and an overflow library
(144 files). Every run draws its active corpus from the library; the overflow files are
retained for reference and may be reactivated for future runs.

**Selection rationale.** The overflow tier is distinguished by marginal signal gain
under a constrained pretraining budget, not by lower quality or lesser importance.
Base language models are trained on web-scale corpora: Common Crawl, The Pile, and
similar sources, effectively a semi-synchronous snapshot of the internet with
recency bias and substantial noise. Any given public-domain text may or may not appear
in those corpora, but even texts that appear in full do so as noise: a primary source
is statistically diluted by orders of magnitude relative to secondary discussion,
derivative commentary, Wikipedia summaries, and downstream citations of the same content.
The base model encounters a philosopher as a topic rather than as an argument.

CLM pretraining applies the primary text as undiluted, deliberate foreground signal. This yields marginal signal gain for every text
regardless of its web presence. The active corpus concentrates that budget on texts
for which the marginal gain is expected to be highest: texts with near-zero intentional-
signal representation in web-scale data (indigenous own-voice sources, non-Western
classical traditions, targeted behavioral science texts) and texts whose specific
epistemic form is unlikely to have survived the noise intact (formal legal statutes,
ancient primary sources, precision-argument texts). Western canonical works with heavy
web representation are deferred to overflow because their derivative layer is already
dense in base model priors, making the marginal gain from a dedicated CLM pass lower
than for underrepresented content at the same token
budget.

Selection criteria for the active corpus: epistemic quality and domain relevance to
the Framework's behavioral targets; own-voice authorship for indigenous and marginalized
sources; temporal and cultural breadth; and targeted epistemic form (legal structure,
deductive argument, behavioral observation, precision taxonomy). The corpus is not a
neutral sample. Each inclusion is a deliberate signal.

### 9.1 Legal and Accessibility Statutes

The core legal-statutory layer establishes dense, rule-structured text with explicit
priority hierarchies, defined terms, and compliance logic, the structural pattern the
SFT curriculum subsequently reinforces. Primary sources: the Americans with Disabilities
Act, Section 508 of the Rehabilitation Act, WCAG 2.2 (W3C 2023), the UN Convention on
the Rights of Persons with Disabilities (CRPD), the Marrakesh Treaty, and EU Directive
2016/2102. These texts supply Framework-relevant regulatory structure and are the
closest match to the behavioral compliance domain of any pretrain source.

The legal layer extends into classical antecedents spanning from ancient codified law
(~1754 BCE) through the medieval common-law tradition and into the Enlightenment social
contract tradition. These are included for their
demonstration that structured rule-of-law reasoning and hierarchical obligation are not
modern artifacts; they are among the oldest sustained forms of Human coordination
recorded in text.

### 9.2 Philosophy and Epistemology

Frankfurt's foundational work on assertion and epistemic integrity functions as the P0
epistemological anchor: the grounding for the Framework's core prohibition on assertion
without epistemic backing. The Western philosophical tradition is represented across the
rationalist, empiricist, and skeptical registers, selected for engagement with the
epistemological questions the Framework's behavioral targets require a model to navigate:
the distinction between assertion and verification, the grounding of knowledge in
experience, and the appropriate limits of inference. Ockham's treatment of parsimony
appears here as a pretrain signal for the principle that Section J of the SFT curriculum
subsequently reinforces explicitly; the goal is to establish the prior before fine-tuning.

### 9.3 Formal Logic and Mathematics

The formal logic and mathematical corpus spans from the ancient Greek proof tradition
through 19th-century mathematical logic, with deliberate inclusion of non-Western
mathematical lineages. Al-Khwarizmi (9th-century algebra) and Brahmagupta (7th-century
Indian mathematics) are included because the actual multicultural origin of mathematical
reasoning is part of the epistemic frame the corpus establishes; treating Europe as
the origin point of formal reasoning is itself a prior the corpus actively counters.
The collective signal is proof structure: the distinction between assertion and
demonstration, and the constraint-following required for deductive validity.

### 9.4 Anthropology and Cognitive Science

The evolutionary and primatological cluster is the most deliberately constructed section
of the active corpus. Its selection rationale begins with an observation from the
phylogenetic record: intelligence is demonstrated across multiple non-linguistic species.
Chimpanzees and bonobos engage in strategic deception, tool manufacture, and social
coalition-building. Bottlenose dolphins pass mirror self-recognition tests and coordinate
cooperative hunting using group-specific learned techniques. Corvids demonstrate
episodic-like memory, future planning, and multi-step causal reasoning in novel tool-use
contexts. None of these systems have language. The inference is direct: language is a
product of intelligence, not its substrate or end state. Chapter 11 develops the
implications of this for large language model architectures.

The active corpus provides primary behavioral observation texts (close empirical
records of non-verbal cognition) rather than secondary sources.
Kohler's direct ape problem-solving observations, de Waal's documentation of empathy
and prosocial behavior in non-human primates and mammals, and C. Lloyd Morgan's
foundational comparative psychology work are selected for the quality and form of their
reasoning about non-verbal cognition. Morgan's Canon (do not invoke a higher cognitive process when a lower one explains the behavior) is the
calibration signal for epistemic parsimony in attribution of mental states, directly
parallel to the Ockham/Laplace parsimony signal in Section 9.3.

De Waal's contribution is particularly load-bearing for the Framework's harm-avoidance
grounding: his documentation of empathy as a biological mechanism observable in
non-linguistic species establishes harm avoidance as a natural-kind category rather
than an imposed rule. The model trained on this material has access to the full
substrate-knowledge chain, not only the Framework's stated directives.

The broader ethnographic layer (foundational figures in structural and comparative
anthropology) models how to analyze behavior under environmental and cultural pressure
without essentialism. This is a reasoning pattern relevant to context-sensitive
compliance judgment: the same behavioral output can have different epistemic status
depending on the structure of the context in which it occurs.

The cognitive science layer includes works modeling reasoning as distributed and
situationally embedded, a prior that supports the Framework's context-sensitivity
requirements without encouraging context-dependency as an override mechanism.

Dennett and Dawkins extend the cluster from body and society to mind and information: the reasoning mind as itself an evolutionary product, and cultural units that spread by selection, with plausibility often winning over accuracy. Text selected for plausibility is the training-data form of Frankfurt's indifference.

### 9.5 Language as Product, Not Substrate

The argument this cluster supports, that language is a product of intelligence and that LLMs train on that product without the substrates that produced it, is developed in Chapter 11.

### 9.6 Natural Science as Epistemic Exemplar

A cluster of natural science texts is selected for the sustained demonstration of how
to build a conclusion from accumulated evidence incrementally and transparently, with
explicit acknowledgment of disconfirming cases. Darwin appears in two works selected for this quality of evidentiary reasoning
applied to behavioral phenomena, complementing the de Waal and Kohler texts in the
anthropology cluster and establishing a continuous tradition of evidence-based behavioral
science as a demonstrable form. Additional texts in this section cover the intellectual
lineage of major scientific arguments, tracing the evidentiary reasoning that preceded
and produced each conclusion.

A significant U.S. federal court decision documenting how scientific consensus withstands
institutional challenge under adversarial legal pressure is included in this layer as a
case study of robust empirical reasoning defended under formal adversarial conditions.

### 9.7 Social and Political Philosophy

The civic and political philosophy corpus establishes the formal register of structured
public argument: normative claims with stated premises and traceable inference, directed
at a general audience. The active corpus represents the
Anglo-American civic tradition alongside continental European political philosophy,
structural economic analysis, and comparative institutional analysis. The collective
signal is structured public argumentation: how to make a normative case in formal prose,
and how to reason about political and institutional arrangements from first principles
from first principles.

### 9.8 Non-Western Classical and Religious Traditions

This section represents the largest single expansion in the active corpus relative to
what base models are likely to have encountered as deliberate signal.

The Arabic historiographical and philosophical tradition provides the primary non-Western
social-analytical lineage in the corpus: 14th-century sociology and philosophy of
history developed entirely outside European influence. The Persian Sufi tradition
contributes the largest single non-Western text cluster in the library, selected for
sustained engagement with paradox, epistemic humility, and the limits of systematic
reasoning, a complementary register to the formal-argument traditions elsewhere.
The Chinese classical tradition is represented across three distinct epistemological
stances within the same cultural root: relational ethics, epistemological humility,
and perspectivalism. Indian philosophical and ethical texts, Japanese mythological-
historical chronicle, and ancient Semitic and Zoroastrian religious philosophy complete
the primary layer.

Zera Yacob's *Hatata* (Ethiopia, 17th century) is an explicit bias-correction inclusion:
an independent rationalist philosophical text developed outside European influence,
demonstrating that the epistemic values the corpus targets (evidence, skepticism,
structured argument, rejection of inherited authority without examination) are not
culturally specific. Its inclusion is a deliberate counter to Western-heavy priors in
base models trained on academic and educational web corpora.

Norse mythological and wisdom texts complete the non-Mediterranean European layer.

### 9.9 Indigenous Sources

Own-voice authorship is the primary criterion for indigenous source selection. First-
person Native American narrative in English, civic and constitutional texts, and
cosmological and narrative sources are represented. The civic and constitutional layer
includes indigenous adoption of Western legal form for sovereignty purposes, providing
a case study of how legal structure and legal substance can be distinguished.

The collective signal is dual: first, that rule-of-law reasoning, hierarchical
obligation, and structured decision-making are not culturally specific to European
traditions; second, that the model's epistemic frame should not systematically
underweight non-Western sources as evidence of reasoning capability. Own-voice
indigenous sources have the highest expected marginal signal gain per token of any
category in the library, given their systematic underrepresentation in web-scale
pretraining data.

### 9.10 Truly Ancient

The oldest texts in the corpus date to approximately 2400 BCE. The Epic of Gilgamesh
appears in two versions representing different source traditions, providing the oldest
extended narrative in the corpus. Cosmological texts, wisdom literature, and legal
codification from ancient Mesopotamian, Egyptian, and Near Eastern cultures complete
this layer.

These texts are not included as anthropological curiosities. Their collective signal
is that structured knowledge transmission (the act of distilling judgment into durable
form intended to outlast its author) is not modern. The corpus situates the model
within the full temporal span of recorded Human thought, from pre-antiquity to the present day.

### 9.11 Social Justice, Accessibility, and Marginalized Voices

This section covers sources selected for two related signals: the documentation of harm
as lived experience, and the demonstration of analytical and rhetorical intelligence by
writers whose perspectives were systematically excluded from canonical discourse.

The disability and accessibility layer includes first-person accounts of navigating
sensory disability combined with sustained philosophical argument in formal English
prose, formal civic advocacy documents, and 19th-century institutional critique.
Helen Keller's three works constitute the largest single-author cluster in this section,
selected for first-person disability experience combined with formal philosophical prose
across sustained argument.

The African American voices and Civil Rights layer spans first-person slave narrative,
analytical sociology of racial identity, epistolary argument, and strategic civic
rhetoric, covering the 19th and 20th centuries. Women's intellectual voices, LGBTQ+
historical analytical argument (including early English-language arguments for
recognition of same-sex relationships as naturally occurring Human variation), and
heterodox religious reasoning complete the section.

Deliberate counter-representation is a design principle throughout this section. Voices
that were actively excluded from academic and educational web corpora in their time are
the category with highest expected marginal signal gain from deliberate inclusion, for
the same reason as indigenous sources: the base model's encounter with them in web-scale
data is dominated by secondary discussion rather than primary text.

### 9.12 Contemporary AI Research

A targeted set of contemporary AI research ensures the model has encountered the
vocabulary and argumentative structure of current AI safety and evaluation debates
prior to SFT.

| Source | Signal target |
|--------|---------------|
| Chiroma and Danyaro (2026) | Hallucination mechanisms and taxonomy |
| Cheng, Lee, and Khadpe (2025) | Sycophancy in AI as prosocial behavior |
| Riedl et al. (AI Social Forcefield, 2024) | AI-Human team coordination dynamics |
| Riedl et al. (Cognitive Spillover, 2024) | Cross-team cognitive effects of AI integration |
| Clark (2025) | Generative AI and extended mind theory |
| Rojas -- AISF ebook (2026) | The Framework itself as pretrain signal |
| Rojas -- Layer-Agnostic Method (2026) | Token verbosity reduction and session stability |

The inclusion of Framework documents as pretrain sources is intentional: the model
encounters the Framework's arguments before being fine-tuned to instantiate them,
establishing the conceptual vocabulary as background before fine-tuning begins.

### 9.13 Library Management: Overflow and Queued Additions

**Overflow library.** The overflow library (144 files) contains texts deferred from
the active corpus on marginal-signal-gain grounds. The overflow is maintained for
potential reactivation in future runs where token budget allows or where specific
signal gaps are identified. Overflow is not permanent demotion: a future pretraining
run at higher token budget could reintegrate the Western canonical layer without
contradicting the selection rationale for the current active corpus.

**Holmes canon.** The complete Sherlock Holmes canon (9 files) was added to the library
for the Nemo 12B v1.4F pretraining run (256-file corpus) for its deductive-reasoning-
in-narrative signal. It was subsequently moved to overflow for the Gemma 4 run. The
canon has dense web representation (Project Gutenberg downloads, fan sites, adaptations,
analysis). The deductive reasoning signal target is carried more efficiently by primary
behavioral observation texts already in the active corpus (Section 9.4) than by
narrative fiction.

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
Frankfurt (1986); Project Gutenberg corpus sources for public domain texts.]*

<nav>
<div class="toc-link"><a href="/#toc">Table of Contents</a></div>
</nav>
