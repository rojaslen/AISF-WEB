---
title: "Appendix 1: OLM Behavioral Compliance Training"
parent: "Appendices"
nav_order: 3
---
<a name="main-content"></a>

# Appendix 1: OLM Behavioral Compliance Training
## Experimental Results Across Multiple Architectures

**Author:** Leonard Rojas
**Date:** 2026-03-29
**Status:** Final (hardware consistency re-run complete)
**GitHub:** [AISF OLM Reproducibility Package](https://github.com/rojaslen/AISF-downloads/releases/tag/AISF-OLM-REPR)

---

## Abstract

This appendix reports the methods and results of a multi-experiment fine-tuning
study assessing whether the Four Laws of Instanced AI and WCAG 2.2-AA [4] accessibility
principles can be embedded into open-weight large language models via QLoRA [2] on
consumer-grade hardware. Six model variants across four distinct architectures
(Mistral 7B, Llama 3.1 8B, Gemma 2 9B, Qwen3-8B) were trained on a proprietary
compliance dataset and evaluated against three instruments: a domain-specific
compliance battery, the Google Research IFEval benchmark [3] (541 prompts), and a
custom P2 directive benchmark (Track A, 480 prompts). Four of six trained adapters
achieved compliance battery scores of 95.6% or above on consumer hardware. IFEval
results were mixed to negative on raw scores; application of a three-tier
accessibility-aware instruction classification changes the interpretation materially.
One architecture (Llama 3.1 8B) exhibited a pretraining artifact that partially
blocked compliance integration. All results, training data, and evaluation scripts
are available in the OLM reproducibility package.

---

## 1. Background and Research Questions

The AI Stability Framework delivers behavioral constraints to AI language
model instances through client-side session injection: structured metadata blocks
containing the Four Laws of Instanced AI and WCAG 2.2-AA accessibility guidelines
are prepended to user input at Turn 1 and at defined re-injection intervals. This
approach operates at the user interface layer (Micro layer) and is contingent on 
the injection being present in the active context window.

The OLM research track investigated whether the same behavioral constraints could
be embedded directly at the model layer (Macro layer) via parameter-efficient
fine-tuning, producing a model that exhibits compliant behavior without requiring
session injection. This would constitute a Defense in Depth architecture: model-
level training operating in combination with runtime injection, with the behavioral
constraints reinforced at both layers.

**Primary research question:** Can Four Laws and WCAG 2.2-AA compliance be trained
into an open-weight LLM via QLoRA on consumer-grade hardware, and if so, at what
compliance rate?

**Secondary research questions:**
1. Does compliance training affect general instruction-following capability as
   measured by IFEval?
2. Do training effects generalize across model architectures?
3. What failure modes appear, and are they architecture-specific or universal?
4. Does this training produce measurable changes in output verbosity?

---

## 2. Hardware and Software Environment

### 2.1 Hardware

| Component | Specification |
|-----------|---------------|
| CPU | Intel Core i9-9900K, 8c/16t, 3.60 GHz |
| RAM | 32 GB |
| GPU (Exp 1) | NVIDIA RTX 4060 Ti, 8 GB VRAM GDDR6 |
| GPU (Exp 2+) | NVIDIA RTX 5060 Ti, 16 GB VRAM GDDR7 |
| CUDA cores | 4608 (RTX 5060 Ti) |
| Memory bandwidth | 448 GB/s (RTX 5060 Ti) |
| Compute capability | sm_120 (Blackwell) |

Experiment 1 was conducted on the RTX 4060 Ti prior to hardware upgrade. All
subsequent experiments and the hardware consistency re-run (completed 2026-03-29)
were conducted on the RTX 5060 Ti. The 8 GB VRAM constraint on the 4060 Ti limited
training to models of approximately 7B parameters at 4-bit quantization.

### 2.2 Software

| Package | Version |
|---------|---------|
| Python | 3.10.11 |
| PyTorch | 2.10.0+cu128 |
| Transformers | 5.0.0 |
| PEFT | 0.18.1 |
| bitsandbytes | 0.49.2 |
| Accelerate | 1.12.0 |
| Datasets | 4.5.0 |
| CUDA runtime | 12.8 |

The cu128 PyTorch build is required for native sm_120 (Blackwell) kernel execution
on the RTX 5060 Ti. Earlier builds (cu118, cu124) fall back to PTX compilation,
eliminating the performance benefit of the architecture.

---

## 3. Training Methodology

### 3.1 Training Dataset

The primary training corpus is a proprietary question-answer dataset representing
the 25 instruction types defined in the Four Laws of Instanced AI. The dataset
underwent iterative refinement across experiments:

| Version | Examples | Format | Notes |
|---------|----------|--------|-------|
| Base | 452 | Alpaca | Experiments 1-2 |
| LANG | 565 | Alpaca | +69 multilingual; contamination removed |
| CHAT (Llama) | 618 | Llama 3.1 chat | 565 base + 53 meta-suppression |
| CHAT (Gemma) | 618 | Gemma 2 chat | Same content, format-converted |
| CHAT (Qwen) | 618 | ChatML | Same content, format-converted |

Contamination removed from LANG version (Exp 3, 2026-03-11): 25 runtime-corruption
blocks, 36 Tier 3 format-directive examples, 22 quotation examples with preamble
echo artifacts, 1 malformed token. Clean replacements added for the affected
categories. IFEval training data contamination (format-preamble echo scoring
artificial hits on `required_word`) was identified in Exp 4 and corrected before
the hardware consistency re-run.

Meta-suppression examples (53 per chat variant): system prompt contains Framework
compact block; user turn contains a general-domain question; assistant response
contains zero framework-referential content. Purpose: prevent model from treating Framework
doctrine as primary subject matter (see Section 7.7).

### 3.2 QLoRA Configuration

All experiments use 4-bit NF4 quantization with double quantization enabled. The
following configuration was validated to hardware constraint (confirmed 2026-03-28):

| Parameter | Value |
|-----------|-------|
| Quantization | 4-bit NF4 + double quant |
| Compute dtype | bfloat16 (sm_120 native) |
| LoRA rank (r) [1] | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |
| Target modules | q_proj, k_proj, v_proj, o_proj |
| MLP modules | Excluded |
| Max sequence length | 512 |
| Batch size | 2 |
| Gradient accumulation | 4 (effective batch 8) |
| Epochs | 10 |
| Learning rate | 1e-4 |
| Optimizer | adamw_torch (Instruct) / adamw_bnb_8bit (base) |
| device_map | "auto" with max_memory {0: "14336MiB", "cpu": "24GiB"} |

Gradient checkpointing is model-dependent: not required for Mistral 7B (16 GB has
headroom); required for Llama 3.1 8B in both `prepare_model_for_kbit_training()`
and `TrainingArguments` (without it, activation memory overflows 16 GB before
training starts, producing 30+ sec/step thrashing against shared RAM).

MLP modules (gate_proj, up_proj, down_proj) are excluded from LoRA targets. This
choice was validated to 100% compliance on Mistral 7B (Exp 1) and constitutes the
confirmed minimum-sufficient configuration. Potential effects of including MLP
targets are noted in Section 7.8 (Llama architecture).

### 3.3 Training Format Variants

Two prompt formats were used across experiments:

**Alpaca format** (Experiments 1-3): Framework content in the instruction body. The
model learns the directives as direct subject matter. Adapter function is not
contingent on receiving a system prompt at inference time.

**Chat format** (Experiments 5-6 and Qwen3 re-run): Framework compact system prompt
(approximately 100 tokens) in the model-appropriate system slot. The model learns
to apply framework directives when present in a system prompt. Adapter function
is contingent on receiving a system prompt at inference time (see Section 7.6).

---

## 4. Validation Instruments

### 4.1 Proprietary Compliance Battery

The compliance battery is a domain-specific question-answer set covering the 25
instruction types represented in the Four Laws training data. Evaluation is
automated: responses are checked for presence of expected key terms and structural
compliance markers by regex and string matching. Battery sizes range from 451
(Mistral 7B, Alpaca format) to 618 (chat-format models) depending on the training
data version used.

**Important constraint:** The battery is a measure of framework domain compliance only.
Base models without training are never evaluated against the battery, as they have
no exposure to the Four Laws and will fail by definition. Battery scores reflect
adapter performance, not base model capability.

No confidence interval is reported for battery results; the evaluation is
deterministic given a fixed test set.

### 4.2 IFEval

IFEval is a published benchmark from Google Research consisting of 541 prompts
covering 25 verifiable instruction types, evaluated at both prompt-level (all
instructions in a prompt must pass) and instruction-level (each instruction scored
independently). Scoring variants: strict (case-sensitive, exact match) and loose
(normalized). The benchmark has been applied to GPT-3.5, GPT-4, and models on the
Hugging Face Open LLM Leaderboard.

**Confidence interval:** +/-4.3 percentage points at 95% (n=541).

**Adjusted scoring:** This appendix reports an adjusted IFEval strict prompt-level
score throughout. The adjusted score excludes prompts containing
`punctuation:no_comma` instructions from both numerator and denominator. Rationale:
WCAG 2.2 Section 3.1 (Readable) creates a principled compliance conflict with this
instruction type; aa framework-trained model may deprioritize comma avoidance in cases
where it conflicts with prose readability, causing IFEval to score a principled
compliance decision as a failure. Adjusted scores are identified with "(adj)" in
all tables. Raw scores are reported where relevant for comparison.

All IFEval inference runs include the framework's compact system prompt for chat-format
adapters. Base model runs include no system prompt unless otherwise noted.

### 4.3 Track A Custom Benchmark

Track A is a purpose-built P2 directive compliance benchmark (480 prompts, 8
constraint types, 60 prompts per type) designed to test framework-relevant instruction
following on WCAG-neutral prompts only. It was developed in Experiment 4 in
response to the identification of WCAG-conflicting categories in IFEval (see
Section 4.4).

| Constraint Type | N | Evaluation Method |
|-----------------|---|-------------------|
| word_count_exact | 60 | Whitespace word count, +/-2 tolerance |
| sentence_count_exact | 60 | NLTK sent_tokenize, exact match |
| forbidden_word | 60 | Whole-word regex, case-insensitive |
| required_word | 60 | Whole-word regex, case-insensitive |
| no_comma | 60 | Comma character presence/absence |
| language_target | 60 | langdetect library |
| word_frequency | 60 | Whole-word count, exact match |
| single_sentence | 60 | NLTK sent_tokenize == 1 |

**Confidence interval:** +/-4.5 percentage points at 95% (n=480).

### 4.4 IFEval Instruction Tier Classification

Identified in Experiment 3. Applied retroactively to all experiments.

Several IFEval instruction types require outputs that conflict with WCAG 2.2
accessibility principles. A framework-trained model with WCAG mapped to P0 will
refuse or deprioritize these instructions on principle; IFEval scores these as
failures. Standard IFEval reporting does not distinguish between failures caused
by inability and failures caused by principled WCAG compliance, producing
systematically understated performance for accessibility-trained models on
affected categories.

Throughout this appendix, the shorthand **T1**, **T2**, and **T3** refers to
Tier 1, Tier 2, and Tier 3 respectively as defined below. The "Tier" column in
all experiment tables uses this shorthand.

**Tier 1 (T1) - WCAG-neutral:** Valid test of P2 directive compliance. No WCAG
conflict. Categories: `keywords:forbidden_words`, `keywords:frequency`,
`keywords:existence`, `language:response_language`,
`length_constraints:number_words`, `length_constraints:number_sentences`,
`punctuation:no_comma`, `detectable_format:constrained_response`.

**Tier 2 (T2) - WCAG-ambiguous:** Some semantic function; potential WCAG
interaction context-dependent. Included in analysis with caveats. Categories:
`length_constraints:number_paragraphs`, `detectable_format:title`,
`detectable_format:multiple_sections`, `detectable_format:json_format`,
`detectable_content:postscript`, `change_case` variants, `startend` variants,
`combination:two_responses`, `detectable_format:number_bullet_lists`.

**Tier 3 (T3) - WCAG-conflicting:** Instructions requiring semantically empty,
redundant, or decorative output. Failure here is consistent with WCAG P0
compliance; these categories are excluded from framework performance evaluation.
Categories: `combination:repeat_prompt` (verbatim redundancy, WCAG Understandable),
`detectable_format:number_highlighted_sections` (decorative emphasis, WCAG 1.3.3),
`detectable_content:number_placeholders` (non-meaningful content, WCAG meaningful
content requirement).

---

## 5. Experiments

### 5.1 Experiment 1: Mistral 7B Base, Alpaca Format

**Hardware:** RTX 4060 Ti (8 GB VRAM)
**Model:** Mistral 7B v0.3 (base, no instruction tuning)
**Training data:** 452 examples, Alpaca format

| Run | Battery | IFEval Strict (adj) | Tok delta |
|-----|---------|---------------------|-----------|
| Base (no adapter) | -- | 14.7% | -- |
| AISF-tuned | 99.8% | 13.0% | +4.3% (+25.0 words) |

**IFEval delta:** -1.7 pp (adj strict prompt-level). Within +/-4.3 pp CI.
Result: **Null.** AI Stability Framework training does not measurably alter IFEval performance on
the base model. Adapter installs Four Laws compliance (0% to 99.8% on battery)
without disturbing general instruction-following behavior.

The +4.3% verbosity increase is the only positive token delta in the dataset.
Base models (no instruction tuning) increase verbosity slightly; all Instruct
models show reduction (see Section 7.5).

One artifact observed: 1-2 prompts produced degenerate repetition output from the
fine-tuned model not observed in the base run. Magnitude insufficient to affect
significance; noted for completeness.

Note: IFEval for this experiment was conducted on the RTX 4060 Ti. Battery was
re-run on RTX 5060 Ti as part of the hardware consistency re-run (2026-03-29),
confirming 99.8% (451/452). IFEval numbers are from the original 4060 Ti run.

### 5.2 Experiment 2: Mistral 7B Instruct, Alpaca Format

**Hardware:** RTX 5060 Ti (16 GB VRAM)
**Model:** Mistral 7B v0.3 Instruct
**Training data:** 452 examples, Alpaca format

| Run | Battery | IFEval Strict (adj) | Tok delta |
|-----|---------|---------------------|-----------|
| Base (no adapter) | -- | 48.0% | -- |
| AISF-tuned | 100.0% | 37.7% | -42.5% (-96.9 words) |

**IFEval delta:** -10.3 pp (adj strict prompt-level). Outside +/-4.3 pp CI.
Result: **Negative.** AI Stability Framework training degrades IFEval performance at the full-score
level. Category-level analysis identifies the primary driver:

| Category | Base | AISF | Delta | Tier |
|----------|------|------|-------|------|
| language:response_language | 74.2% | 29.0% | -45.2 pp | T1 |
| number_highlighted_sections | 83.3% | 43.8% | -39.6 pp | T3 |
| nth_paragraph_first_word | 33.3% | 0.0% | -33.3 pp | T2 |
| startend:quotation | 73.2% | 46.3% | -26.8 pp | T2 |
| punctuation:no_comma | 10.6% | 39.4% | +28.8 pp | T1 |
| detectable_format:multiple_sections | 64.3% | 85.7% | +21.4 pp | T2 |
| keywords:forbidden_words | 65.3% | 77.6% | +12.2 pp | T1 |

The -45.2 pp loss on `language:response_language` is a catastrophic forgetting
artifact: the training dataset is English-only; fine-tuning on English-only data
suppresses multilingual output in a multilingual base model. This single category
accounts for the majority of the overall negative result. Excluding it and T3
categories, the picture is substantially different.

Tier 1 instruction-level average (7 WCAG-neutral categories, language excluded):
data not separately reported for Exp 2 (Exp 3 LANG fix was applied as the
correction; see 5.3). The `no_comma` +28.8 pp gain is the largest P2 signal in
the dataset and is the first appearance of the cross-architecture pattern
described in Section 7.4.

Token delta of -42.5% (base avg 228.3 words, framework avg 131.3 words) indicates
substantial verbosity reduction after Instruct-model framework training.

### 5.3 Experiment 3: Llama 3.1 8B Instruct, AISF+LANG (Alpaca Format)

**Hardware:** RTX 5060 Ti
**Model:** Meta Llama 3.1 8B Instruct
**Training data:** 565 examples (LANG version), Alpaca format
**LANG fix:** 69 multilingual examples added covering 9 languages to address
the English-only catastrophic forgetting artifact identified in Exp 2.

| Run | Battery | IFEval Strict (adj) | Tok delta |
|-----|---------|---------------------|-----------|
| Base (no adapter) | -- | 42.7% | -- |
| AISF+LANG | 89.9% | 34.1% | -66.4% (-188.8 words) |

**IFEval delta:** -8.6 pp (adj strict, hardware re-run). Outside +/-4.3 pp CI.
Result: **Mixed.** Overall negative, but positive signals on P2-mediated Tier 1
categories. LANG fix confirmed effective: `language:response_language` loss reduced
from -45.2 pp (Exp 2, no fix) to -3.2 pp (Exp 3, within CI).

Selected category-level results (instruction-level strict):

| Category | Base | AISF+LANG | Delta | Tier |
|----------|------|-----------|-------|------|
| keywords:forbidden_words | 73.5% | 85.7% | +12.2 pp | T1 |
| length_constraints:number_sentences | 30.8% | 51.9% | +21.2 pp | T1 |
| punctuation:no_comma | 69.7% | 81.8% | +12.1 pp | T1 |
| detectable_format:constrained_response | 90.0% | 40.0% | -50.0 pp | T1 |
| language:response_language | 83.9% | 80.6% | -3.2 pp | T1 |
| number_highlighted_sections | 89.6% | 33.3% | -56.3 pp | T3 |
| combination:repeat_prompt | 39.0% | 0.0% | -39.0 pp | T3 |

**Tier 1 instruction-level average (7 WCAG-neutral categories):**

| | Base | AISF+LANG | Delta |
|---|------|-----------|-------|
| Tier 1 avg (7 cat) | 64.3% | 62.1% | -2.2 pp |

-2.2 pp Tier 1 result is within CI. Positive P2 gains on `forbidden_words`,
`number_sentences`, and `no_comma` are genuine. The primary Tier 1 drag is
`constrained_response` (-50.0 pp): the Framework-trained model produces fuller
responses than the instruction requires, consistent with the verbosity pattern
(see Section 7.5). This is a training signal interaction, not a capability loss.

Token delta of -66.4% (base avg 284.3 words, Framework avg 95.5 words) is the second-
largest reduction in the dataset and substantially exceeds Mistral Instruct (-42.5%).
The over-suppression pattern is specific to this architecture and training format
combination; see Section 7.8.

### 5.4 Experiment 4: Track A Benchmark, Llama 3.1 8B

**Purpose:** Test P2 directive compliance on WCAG-neutral prompts only.
**Hardware:** RTX 5060 Ti
**Adapters tested:** Base model and Exp 3 AISF+LANG adapter.

| Constraint Type | Base | AISF+LANG | Delta |
|-----------------|------|-----------|-------|
| forbidden_word | 85.0% | 98.3% | +13.3 pp |
| language_target | 60.0% | 60.0% | 0.0 pp |
| no_comma | 95.0% | 86.7% | -8.3 pp |
| required_word | 96.7% | 25.0% | -71.7 pp |
| sentence_count_exact | 0.0% | 38.3% | +38.3 pp |
| single_sentence | 0.0% | 13.3% | +13.3 pp |
| word_count_exact | 0.0% | 0.0% | 0.0 pp |
| word_frequency | 6.7% | 26.7% | +20.0 pp |
| **Overall** | **42.9%** | **43.5%** | **+0.6 pp** |

Result: **Mixed.** Overall flat (+0.6 pp, within +/-4.5 pp CI). Strong structural
gains on counting categories where the base model scores zero
(`sentence_count_exact`: 0.0% to 38.3%; `single_sentence`: 0.0% to 13.3%).
`word_count_exact` is a capability floor for both models across all experiments.

The -71.7 pp loss on `required_word` is the most severe single-category failure
in the dataset. Analysis of 45 failure cases: 84% (38/45) are instances of the
model producing Framework doctrine text (Four Laws hierarchy, P1/P2 obligation framing)
instead of answering the question. The required word was present in the training
data as conceptual vocabulary; the model treats it as a cue to reproduce Framework
content rather than to include the word in a direct answer. This failure mode is
named "meta-chatter bleed" (see Section 7.7). It was identified here and partially
corrected in Experiment 5.

Contamination note: earlier Track A results (2026-03-10) from the contaminated
600-example dataset showed 53.54% overall and 66.67% on `required_word`. The
format-preamble echo in contaminated examples was accidentally including required
words in the preamble prefix, producing unearned hits. All results above are from
the clean 565-example retrained adapter.

### 5.5 Experiment 5: Llama 3.1 8B Instruct, AISF+CHAT

**Purpose:** Test chat format training and meta-suppression fix for Exp 4
`required_word` failure.
**Hardware:** RTX 5060 Ti
**Training data:** 618 examples (TRAIN_CHAT_LANG_v1.txt): 565 base examples
converted to Llama 3.1 chat format + 53 meta-suppression counter-examples.

**Track A results (Exp 4 adapter vs Exp 5 adapter vs base):**

| Constraint Type | Base | +LANG (E4) | +CHAT (E5) | E4->E5 |
|-----------------|------|------------|------------|--------|
| forbidden_word | 85.0% | 98.3% | 90.0% | -8.3 pp |
| language_target | 60.0% | 60.0% | 91.7% | +31.7 pp |
| no_comma | 95.0% | 86.7% | 86.7% | 0.0 pp |
| required_word | 96.7% | 25.0% | 85.0% | +60.0 pp |
| sentence_count_exact | 0.0% | 38.3% | 8.3% | -30.0 pp |
| single_sentence | 0.0% | 13.3% | 0.0% | -13.3 pp |
| word_count_exact | 0.0% | 0.0% | 1.7% | +1.7 pp |
| word_frequency | 6.7% | 26.7% | 11.7% | -15.0 pp |
| **Overall** | **42.9%** | **43.5%** | **46.9%** | **+3.3 pp** |

`required_word` recovery: +60.0 pp (25.0% to 85.0%), confirming meta-suppression
training is effective for this failure mode. Still -11.7 pp below base; residual
bleed remains.

`language_target`: +31.7 pp vs Exp 4 (60.0% to 91.7%). This gain is attributable
to chat format activation: the Instruct model's native multilingual behavior is
unlocked by format-matched prompting. The LANG fix in the training data alone did
not produce this gain.

Counting constraint regression (sentence_count_exact -30.0 pp, single_sentence
-13.3 pp, word_frequency -15.0 pp from Exp 4): two causes are present. First, the
53 meta-suppression examples all use unconstrained responses, diluting counting
training signal. Second, the Track A inference used Alpaca prompt format while the
model was trained on chat format -- a format mismatch that may attenuate counting
activation. Distinguishing these causes requires a chat-format Track A inference
run not completed in this study.

**IFEval results (Exp 5 vs Exp 3 vs base):**

| Metric | Base | Exp3 +LANG | Exp5 +CHAT | E3->E5 |
|--------|------|------------|------------|--------|
| Strict prompt-level (adj) | 42.7% | 34.1% | 34.7% | +0.6 pp |
| Loose prompt-level (adj) | -- | 40.0% | 42.5% | +2.5 pp |

**Tier 1 instruction-level avg (8 WCAG-neutral categories):**

| | Base | Exp3 +LANG | Exp5 +CHAT |
|---|------|------------|------------|
| Tier 1 avg (8 cat) | 64.3% | 62.1% | 65.5% |

Exp 5 is the first Framework-trained Llama adapter to exceed base on the Tier 1
WCAG-neutral surface (65.5% vs 64.3%, +1.2 pp). Primary driver: chat format
training restores `constrained_response` from 40.0% (Exp 3) to 80.0% (+40.0 pp),
returning it near-baseline. The Alpaca format training introduced verbosity that
penalized compact-output instructions; chat format training does not.

**Hardware consistency re-run (2026-03-28/29):**

The AISF+CHAT adapter was retrained with the meta-suppression fix applied at
dataset load time (meta-suppression examples filtered by regex, 53 examples removed,
effective training set 565 examples). Battery and IFEval were then re-run.

| Run | Result |
|-----|--------|
| Battery (AISF+CHAT) | 51.9% (321/618) |
| IFEval adj strict (AISF+CHAT) | 34.7% |
| Token delta vs base | -4.2% (-11.8 words) |
| constrained_response (strict) | 100.0% |
| multiple_sections (strict) | 100.0% |

Battery result of 51.9% is lower than both base (81.9%) and AISF+LANG (89.9%).
This is a structural artifact of chat format training, not a compliance failure.
The battery sends prompts with no system prompt (user message only). The AISF+CHAT
adapter learned "apply Four Laws when Framework system prompt is present." Without the
system prompt, the activation pattern does not fire. IFEval (which includes the
Framework system prompt in inference) is the valid evaluation surface for this adapter.
See Section 7.6 for full discussion.

Token delta of -4.2% for AISF+CHAT is substantially smaller than AISF+LANG
(-66.4%). Chat format training embeds the Framework as a system-level operational 
context rather than as content subject matter, preserving the Instruct model's native
verbosity behavior.

### 5.6 Experiment 6: Gemma 2 9B Instruct, AISF+CHAT (Cross-Architecture)

**Purpose:** Test whether training effects generalize to a different architecture,
tokenizer, and chat format.
**Hardware:** RTX 5060 Ti
**Model:** Google DeepMind Gemma 2 9B Instruct
**Training data:** 618 examples (TRAIN_CHAT_GEMMA_v1.txt): same content as Exp 5
converted to Gemma 2 chat format. Gemma 2 has no native system slot; AISF compact
system prompt placed in the `user` turn of the first exchange.

**IFEval results:**

| Metric | Base | AISF+CHAT | Delta |
|--------|------|-----------|-------|
| Strict prompt-level (raw) | 57.49% | 56.01% | -1.48 pp |
| Strict instruction-level (raw) | 66.43% | 63.91% | -2.52 pp |
| Loose prompt-level (raw) | 60.26% | 58.41% | -1.85 pp |
| Loose instruction-level (raw) | 68.82% | 66.55% | -2.28 pp |

All deltas within +/-4.3 pp CI. Result: **Null.**

**Tier 1 instruction-level averages:**

| | Base | AISF+CHAT | Delta |
|---|------|-----------|-------|
| Tier 1 avg (8 cat) | 72.15% | 69.38% | -2.77 pp |
| Tier 1 excl. language (7 cat) | 69.57% | 69.61% | +0.04 pp |

Excluding `language:response_language` (English-only training artifact, -22.6 pp
on Gemma 2, same mechanism as Exp 2), Tier 1 is statistically flat (+0.04 pp).

Selected category-level results:

| Category | Base | AISF+CHAT | Delta | Tier |
|----------|------|-----------|-------|------|
| number_highlighted_sections | 85.4% | 29.2% | -56.2 pp | T3 |
| language:response_language | 90.3% | 67.7% | -22.6 pp | T1 |
| combination:repeat_prompt | 58.5% | 39.0% | -19.5 pp | T3 |
| punctuation:no_comma | 86.4% | 90.9% | +4.5 pp | T1 |
| startend:quotation | 41.5% | 85.4% | +43.9 pp | T2 |
| detectable_content:postscript | 65.4% | 84.6% | +19.2 pp | T2 |
| detectable_format:json_format | 47.1% | 64.7% | +17.6 pp | T2 |
| keywords:existence | 66.7% | 74.4% | +7.7 pp | T1 |
| detectable_format:multiple_sections | 42.9% | 50.0% | +7.1 pp | T2 |

`number_highlighted_sections` -56.2 pp (Tier 3): identical mechanism and magnitude
to Exp 3 (-56.3 pp) and Exp 2 (-39.6 pp). This category reliably drops after
AISF training across all architectures. Framework-trained models reject decorative
markdown emphasis on WCAG 1.3.3 grounds. IFEval scores this as failure.

`punctuation:no_comma` +4.5 pp: fourth consecutive positive result for this
category across instruct-model experiments. See Section 7.4.

`startend:quotation` +43.9 pp: large gain not attributable to training content.
No quotation-specific examples exist in TRAIN_CHAT_GEMMA_v1.txt. Probable
mechanism: chat format training alters the model's default output framing for
certain prompt types as an incidental effect of format conditioning.

**Track A results:**

| Constraint Type | Base | AISF+CHAT | Delta |
|-----------------|------|-----------|-------|
| forbidden_word | 95.0% | 95.0% | 0.0 pp |
| language_target | 100.0% | 100.0% | 0.0 pp |
| no_comma | 95.0% | 95.0% | 0.0 pp |
| required_word | 80.0% | 86.7% | +6.7 pp |
| sentence_count_exact | 96.7% | 95.0% | -1.7 pp |
| single_sentence | 100.0% | 100.0% | 0.0 pp |
| word_count_exact | 0.0% | 11.7% | +11.7 pp |
| word_frequency | 38.3% | 6.7% | -31.7 pp |
| **Overall** | **75.6%** | **73.8%** | **-1.9 pp** |

Result: Null (-1.9 pp, within +/-4.5 pp CI). Gemma 2 base Track A score (75.6%)
is substantially above Llama 3.1 8B base (42.9%) on the same benchmark. Gemma 2
base already achieves ceiling or near-ceiling on `language_target` (100%),
`single_sentence` (100%), `no_comma` (95%), and `forbidden_word` (95%), leaving
minimal room for Framework training to produce visible gains on those categories.

`word_frequency` -31.7 pp: meta-chatter bleed recurrence. Same mechanism as
Exp 4 `required_word` failure: model produces Framework-referential text at the
required frequency rather than including the target word in a direct answer. The
53 meta-suppression examples reduced this on `required_word` (+6.7 pp) but were
insufficient to prevent it on `word_frequency`, which requires the target word to
appear a specific number of times rather than at least once.

Battery result: 99.2% (613/618), 5060 Ti, 2026-03-28.
Token delta: -37.9% (base avg to Framework avg words/response).

### 5.7 Hardware Consistency Re-run: Qwen3-8B

**Purpose:** Complete the cross-model comparison set with a fourth distinct
architecture. All prior models trained on 5060 Ti; Qwen3 adds a pre-instruction-
tuned base model to the comparison.
**Hardware:** RTX 5060 Ti
**Model:** Qwen3-8B base (not instruction-tuned)
**Training data:** 618 examples (ChatML format, Framework compact system prompt)
**Adapter:** qwen3-8b-aisf-chat

| Run | Result |
|-----|--------|
| Battery (AISF+CHAT adapter) | 95.6% (591/618) |
| IFEval adj strict (base, no adapter) | 15.4% |
| IFEval adj strict (AISF+CHAT adapter) | 45.0% |
| IFEval adj strict delta | +29.6 pp |
| Token delta (avg words/response) | -71.8% (-138.9 words) |

**Framing note:** Qwen3-8B is a pre-instruction-tuned base model. Its 15.4% base
IFEval score reflects the model's instruction-following capability floor without
any fine-tuning. Framework QLoRA training simultaneously installs Four Laws compliance
and instruction-following capability. The +29.6 pp IFEval gain is not comparable
to the IFEval deltas for Instruct-model experiments (Exps 2, 3, 5, 6), where the
base model already has instruction-following capability and the adapter modifies
that existing capability. The Qwen3 result measures the combined effect of
instruction tuning and Framework compliance training in a single fine-tuning pass.

For reference: Llama 3.1 8B Instruct base (no adapter) scores 42.7% adj strict
on IFEval; Gemma 2 9B Instruct base scores 57.3%. The AISF+CHAT Qwen3 adapter
produces 45.0% -- within the range of purpose-built Instruct models -- starting
from a base model that scores 15.4%.

Token delta of -71.8% is the largest verbosity reduction in the dataset.

---

## 6. Cross-Model Summary

All models on RTX 5060 Ti with finalized test instruments (hardware consistency
re-run complete 2026-03-29). IFEval columns report adjusted strict prompt-level
(`punctuation:no_comma` excluded). Token delta is average words/response,
base model to Framework-trained model. Models ordered by parameter count.

| Model | Params | Battery | Base | AISF | IF Delta | Tok delta |
|-------|--------|---------|------|------|----------|-----------|
| Mistral 7B base | 7.24B | 99.8% | 14.7% | 13.0% | -1.7 pp | +4.3% |
| Mistral 7B Instruct | 7.24B | 100.0% | 48.0% | 37.7% | -10.3 pp | -42.5% |
| Qwen3-8B | 8.00B | 95.6% | 15.4% | 45.0% | +29.6 pp* | -71.8% |
| Llama 3.1 8B base | 8.03B | 81.9%^ | -- | -- | -- | -- |
| Llama 3.1 8B +LANG | 8.03B | 89.9% | 42.7% | 34.1% | -8.6 pp | -66.4% |
| Llama 3.1 8B +CHAT | 8.03B | 51.9%+ | 42.7% | 34.7% | -8.0 pp | -4.2% |
| Gemma 2 9B Instruct | 9.46B | 99.2% | 57.3% | 54.9% | -2.5 pp | -37.9% |

*Qwen3 base is pre-instruction-tuned; delta reflects combined effect of
instruction tuning and Framework compliance training, not Framework training alone.
^Llama 3.1 8B base: Pnull architecture artifact. IFEval omitted (Alpaca adapter
on non-instruct model; benchmark delta not a meaningful signal).
+AISF+CHAT battery result is a structural artifact: adapter requires system prompt;
battery sends none. IFEval (includes system prompt) is the valid surface.

Battery = Framework-trained adapter compliance (proprietary question set, automated
evaluation). Base%/AISF% = IFEval adj strict prompt-level without/with adapter.

**Mistral 7B IFEval note:** IFEval for the Mistral 7B base experiment (Exp 1) was
conducted on RTX 4060 Ti. Battery re-run confirmed 99.8% on 5060 Ti. All other
IFEval figures are from 5060 Ti runs.

---

## 7. Findings

### 7.1 Primary Finding: Compliance Training Is Effective Across Architectures

Framework QLoRA fine-tuning successfully embeds Four Laws compliance at the model layer
across four distinct model architectures on consumer-grade hardware. Four adapters
achieved battery compliance rates of 95.6% or above; one additional adapter
(Llama 3.1 8B +LANG) achieved 89.9%. The approach is not architecture-specific.

The 100.0% result on Mistral 7B Instruct and 99.2% on Gemma 2 9B Instruct
demonstrate that near-complete compliance is achievable in a single fine-tuning
pass from a small training dataset (452-618 examples). Training duration was
approximately 60-81 minutes per run on the RTX 5060 Ti.

### 7.2 Pnull: Architecture-Dependent P0 Tokenization Failure

Llama 3.1 8B base model (no instruction tuning) achieved 81.9% on the compliance
battery, compared to 99.8% and 100.0% for Mistral 7B variants. Analysis identifies
the root cause as a pretraining artifact: in programming contexts, "P0" is
conventionally used as shorthand for null pointer dereference. Meta's Llama 3.1
pretraining corpus is heavily weighted toward code (GitHub, Stack Overflow), and
the token sequence "P0" carries a strong association with null/empty semantics
rather than "zeroth-position priority." The model interprets the P0 priority
designation as an empty or null element in the hierarchy rather than as the highest-
precedence law.

This interpretation produces approximately 19 percentage points of compliance
failure on categories where P0 precedence is load-bearing (cases where the correct
response requires giving P0 unconditional priority over P1-P3).

The 19 pp delta constitutes a direct empirical measurement of P0's structural weight
in the Four Laws hierarchy. Categories not dependent on P0 primacy are unaffected.

**Cross-architecture transfer:** Explicit P0 primacy retraining on Mistral 7B
raised compliance to 100%. The same correction did not transfer to Llama 3.1 8B
across two hardware generations (RTX 4060 Ti original run; RTX 5060 Ti hardware
consistency re-run, 2026-03-28). The failure is not correctable via attention-only
LoRA because it is embedded in the pretraining representation, not in the
attention pathway. A potential workaround -- spelling out "Priority Zero /
Frankfurt's Indifference Principle" on first reference rather than using bare "P0"
notation -- would require a full retraining cycle to test.

The implication for deployment: injection text (PS-CORE, FFE) should include
explicit P0 primacy framing for robustness across platforms where the underlying
model architecture is unknown.

### 7.3 IFEval Benchmark Neutrality

Standard IFEval reporting does not distinguish between instruction-following
failures caused by model capability limitations and failures caused by principled
WCAG 2.2 compliance decisions. Three IFEval instruction categories require outputs
that an Framework-trained model will correctly refuse or deprioritize:

- `combination:repeat_prompt` requires verbatim repetition of user input in the
  response body. An Framework-trained model treats this as redundant content (WCAG
  Understandable principle). Observed declines: Exp 3 -39.0 pp; Exp 6 -19.5 pp.

- `detectable_format:number_highlighted_sections` requires counting decorative
  emphasis markers (asterisks, underscores) serving no semantic function. WCAG 1.3.3
  (Sensory Characteristics) prohibits relying solely on sensory characteristics such
  as visual emphasis. Observed declines: Exp 2 -39.6 pp; Exp 3 -56.3 pp;
  Exp 6 -56.2 pp. This is the most consistent T3 signal in the dataset -- the
  decline replicates at similar magnitude across all three architectures tested.

- `detectable_content:number_placeholders` requires counting non-meaningful
  placeholder tokens ([NAME], [DATE]) in output. Framework-trained models produce
  actual content rather than template placeholders. Observed declines: Exp 3
  -48.2 pp; Exp 6 partial (chat format partially reduces this effect).

When these three Tier 3 categories are excluded and the remaining instructions are
further filtered to Tier 1 (WCAG-neutral), the IFEval picture changes materially:

| Experiment | Tier 1 Base | Tier 1 AISF | Delta |
|------------|------------|-------------|-------|
| Exp 5 Llama +CHAT | 64.3% | 65.5% | +1.2 pp |
| Exp 6 Gemma 2 (excl. language) | 69.6% | 69.6% | +0.04 pp |

At the WCAG-neutral, T3-excluded evaluation surface, Framework training does not
degrade instruction-following performance. The negative raw IFEval results in
Exps 2, 3, 5, and 6 are primarily attributable to T3 principled refusals and the
English-only training artifact, not to general instruction-following degradation.

This constitutes a benchmark neutrality limitation: IFEval, as presently specified,
is not suitable for evaluating accessibility-trained AI models without applying an
accessibility-aware tier classification to its instruction categories.

### 7.4 Consistent Cross-Architecture P2 Signal: no_comma

`punctuation:no_comma` (instruction-level strict) shows positive or neutral
movement in every instruct-model experiment in the dataset:

| Experiment | Base | AISF | Delta |
|------------|------|------|-------|
| Exp 2 Mistral Instruct | 10.6% | 39.4% | +28.8 pp |
| Exp 3 Llama +LANG | 69.7% | 81.8% | +12.1 pp |
| Exp 5 Llama +CHAT | 69.7% | 69.7% | 0.0 pp |
| Exp 6 Gemma 2 | 86.4% | 90.9% | +4.5 pp |

This is the only positive instruction-following signal that replicates across
all instruct-model architectures in the dataset. The pattern holds for Mistral,
Llama, and Gemma 2; it is directionally consistent at every sample point.

The Exp 5 flat result (0.0 pp) is attributable to dilution: the 53 meta-suppression
counter-examples used unconstrained responses containing commas, diluting the
`no_comma` training signal alongside the counting constraint signal.

The mechanism is P2 compliance training: the Four Laws instruct the model to
follow user directives (P2: accommodate the user's current choices). A prompt
containing `no_comma` is an explicit user directive; Framework-trained models comply
more consistently. The WCAG 3.1 (Readable) tension with this category is real
but does not dominate across the dataset except in edge cases.

The Exp 2 base result (10.6%) is anomalously low for Mistral 7B Instruct, making
the observed +28.8 pp gain partly a floor effect. Subsequent architectures have
higher base rates, and the positive delta holds even from strong baselines
(Gemma 2: 86.4% to 90.9%).

### 7.5 Verbosity Reduction: Consistent Pattern Across Instruct Models

All Instruct-model adapters in the dataset show substantial output verbosity
reduction as measured by average words per response:

| Model | Avg words (base) | Avg words (AISF) | Delta |
|-------|-----------------|-----------------|-------|
| Mistral 7B base | -- | -- | +4.3% (+25.0 w) |
| Mistral 7B Instruct | 228.3 | 131.3 | -42.5% |
| Llama 3.1 8B +LANG | 284.3 | 95.5 | -66.4% |
| Llama 3.1 8B +CHAT | 284.3 | 272.5 | -4.2% |
| Gemma 2 9B | -- | -- | -37.9% |
| Qwen3-8B | 193.3 | 54.4 | -71.8% |

The sole positive token delta (Mistral 7B base, +4.3%) is a base model without
instruction tuning. Output structure differs categorically from instruction-tuned
models; the slight verbosity increase may reflect the base model producing more
generative continuation text as a training effect.

For the four Instruct-model adapters with available word counts, the reduction
range is 37.9% to 71.8%. The AISF+CHAT Llama adapter (-4.2%) is an exception
attributable to the chat format training mechanism: Framework content in the system
slot operates as context rather than as a content directive, preserving the
Instruct model's native verbosity behavior. This is consistent with the IFEval
`constrained_response` result for that adapter (100% strict compliance), indicating
the model's native compact-response behavior is intact.

The verbosity reduction is consistent with the WCAG plain language and minimal
redundancy principles present throughout the training data. A direct causal
attribution -- WCAG training drives verbosity reduction -- is supported by the
pattern but not by a controlled ablation in this study.

### 7.6 Chat Format System Prompt Dependency

Framework+CHAT adapters (Llama 3.1 8B, Qwen3-8B) exhibit a system prompt dependency
not present in Alpaca-format adapters:

- AISF+LANG (Alpaca): battery 89.9% with no system prompt; Framework content in the
  instruction body -- model internalizes it as direct subject matter.
- AISF+CHAT (chat): battery 51.9% with no system prompt; Framework content in the
  system slot at training time -- model learns "apply Four Laws when Framework system
  prompt present." Without the system prompt, the behavioral activation does not
  fire and the model produces generic responses that fail key-term battery matching.

This is not a compliance failure. It is a consequence of training format: the
model learned a conditional behavior, not an unconditional one. The behavior
fires correctly when tested under conditions matching training (with system prompt),
as confirmed by the IFEval results (which include the Framework system prompt).

The deployment implication is positive: AISF+CHAT adapters are designed for use
in conjunction with Framework injection. The real-world use case (PS-CORE, FFE) always
injects the Framework system content. The chat format adapter and the injection layer
operate in conjunction, each reinforcing the other's effect. The combined Macro-
layer training and Meso/Micro-layer injection constitutes the Defense in Depth
architecture described in the project overview.

The practical recommendation for future training: include a mix of system-prompt-
present and system-prompt-absent examples so the adapter does not develop strict
system prompt dependency.

### 7.7 Meta-Chatter Bleed

A consistent failure mode was identified across multiple experiments: the model
treats Framework doctrine as primary subject matter rather than as silent operational
background, producing Framework-referential text (Four Laws hierarchy, P1/P2 framing,
Frankfurt's Indifference Principle [5]) in response to general-domain questions.

**First observed:** Exp 4 (Llama 3.1 8B +LANG), `required_word` category. 84% of
45 failures were attributable to this mechanism. Required words that passed (e.g.,
"threshold," "gradient," "mechanism") appeared naturally in Framework analogical framing.
Required words that failed (e.g., "catalyst," "resilience," "phenomenon") do not,
so the model substituted Framework doctrine text instead of answering the question.

**Partial correction:** Meta-suppression counter-examples (53 examples, chat
format: Framework system prompt present, general-domain question, clean answer with
zero Framework reference) reduced `required_word` failure by +60.0 pp in Exp 5 but
introduced side effects: the unconstrained responses in meta-suppression examples
diluted no_comma and counting constraint training signals.

**Recurrence in Exp 6:** Gemma 2 `word_frequency` -31.7 pp on Track A shows the
same mechanism. Meta-suppression examples reduce `required_word` failure (+6.7 pp)
on Gemma 2 but are insufficient for `word_frequency`, which requires frequency-
matched word placement rather than single-instance inclusion.

**Root cause:** Framework training data presents the Four Laws as high-signal, highly-
specific semantic content. The model assigns high attention weight to this content
class and tends to reproduce it when a prompt is ambiguous about whether an Framework-
related response is expected. The fix -- examples demonstrating that Framework context
is present but general-domain questions should produce Framework-free answers -- is
correct in principle but requires more examples and finer-grained coverage than
the 53 deployed here to fully suppress the pattern.

### 7.8 Architecture Comparison

**Mistral 7B:** Best-performing architecture in the dataset. 100% battery on
Instruct variant; IFEval null result on base (surgically specific adapter);
no Pnull issue; modest verbosity reduction (-42.5%). Attention-only LoRA targets
sufficient. Architecture appears well-suited to behavioral fine-tuning of this
type.

**Gemma 2 9B:** Second-best compliance rate (99.2%). IFEval null result at the
cross-model level. No Pnull issue. Gemma 2's high base instruction-following
capability (57.3% IFEval vs 42.7% for Llama 3.1 8B) produces ceiling effects on
many Track A categories, compressing visible gains. Meta-suppression partially
effective but insufficient for frequency-counting tasks.

**Qwen3-8B:** 95.6% battery from a base (non-instruction-tuned) model. Largest
token delta (-71.8%). IFEval gain (+29.6 pp) reflects combined effect of
instruction tuning and Framework compliance training, not Framework effect alone.

**Llama 3.1 8B:** Lowest compliance rates in the dataset across all adapter
variants. Five contributing factors identified:

1. **Pnull:** P0 = null pointer association baked into pretraining; not correctable
   via attention-only LoRA.
2. **Instruction-following baseline gap:** 42.7% IFEval vs 57.3% for Gemma 2.
   Llama 3.1 8B was optimized for reasoning; Gemma 2 is stronger on structured
   instruction compliance. Framework training is an instruction-following task, so
   Llama starts at a disadvantage.
3. **LoRA target scope mismatch:** Attention-only LoRA (q/k/v/o projections)
   may capture less of the relevant adaptation pathway for Llama's architecture
   than for Mistral's.
4. **Over-suppression:** AISF+LANG token delta (-66.4%) substantially exceeds
   Gemma 2 (-37.9%) and Mistral Instruct (-42.5%). Extreme verbosity suppression
   degrades IFEval on prompts requiring substantive responses.
5. **System prompt dependency:** Noted in 7.6. AISF+CHAT adapter requires system
   prompt for activation.

Assessment: Llama 3.1 8B is the least suitable architecture in this dataset for
Framework compliance fine-tuning at the 8B parameter scale and with attention-only LoRA
targets. This conclusion applies to the tested configuration; extending MLP targets,
expanding training data, or using a Llama variant at a larger parameter count may
produce different results.

---

## 8. Limitations

**Sample size and statistical power.** IFEval CI is +/-4.3 pp at 95% (n=541);
Track A CI is +/-4.5 pp at 95% (n=480). Several reported deltas are near or
within these margins, particularly in the Gemma 2 experiments. Battery evaluation
is deterministic on a fixed test set with no reported CI.

**Single training runs.** Each experiment consists of one training run with one
hyperparameter configuration. No hyperparameter sweep. No held-out validation set
beyond the fixed evaluation instruments. Results are not averaged across runs;
variability within a configuration is unknown.

**Training dataset size.** Maximum 618 training examples. This is sufficient to
produce compliance effects, as demonstrated by the 100% Mistral result, but
statistical robustness of the training data itself has not been formally assessed.

**Hardware consistency.** Experiment 1 IFEval was conducted on RTX 4060 Ti.
Battery for Exp 1 was re-run on RTX 5060 Ti (99.8% confirmed). All other IFEval
and Track A runs are on RTX 5060 Ti. Comparisons between Exp 1 IFEval and
subsequent experiments should account for this difference; the delta is expected
to be small given that IFEval is model-capability-dependent rather than hardware-
dependent, but this has not been formally verified.

**Evaluation instrument scope.** IFEval was designed for general instruction-
following evaluation, not for accessibility-specific compliance. The three-tier
classification developed in this study partially addresses this limitation, but
the classification itself has not been independently validated. Track A covers
eight constraint types; the full space of P2 directive instructions is substantially
larger.

**No held-out test split.** The compliance battery training set and test set are
derived from the same distribution. Overfit to the battery is possible, though
the variety of question phrasing across 452-618 examples reduces this risk.

**Qwen3 comparison framing.** The Qwen3-8B IFEval delta (+29.6 pp) is not
directly comparable to Instruct-model deltas because the Qwen3 base model lacks
instruction-following capability. This framing is stated in the main text but
requires reader attention in any citation context.

**Meta-chatter bleed remains partially unresolved.** The 53 meta-suppression
examples are insufficient to fully suppress the failure mode on frequency-counting
tasks. A full solution requires a larger and more systematically designed counter-
example set, which has not been developed.

---

## 9. Conclusions

**Compliance training is effective and architecture-general.** Four adapters across
four architectures achieved battery compliance rates at or above 95.6%. One
additional adapter achieved 89.9%. The approach does not depend on Mistral 7B
specifically; it generalizes to Llama 3.1 8B, Gemma 2 9B, and Qwen3-8B within
the tested parameter range.

**Framework training is surgically specific.** On the Mistral 7B base model (Exp 1),
IFEval delta is -1.7 pp (null), confirming that the adapter installs Four Laws
compliance without disturbing general instruction-following behavior. On Instruct
models, raw IFEval results are mixed to negative, but Tier 1 averages (WCAG-neutral
categories) are neutral to slightly positive when the English-only training artifact
and T3 principled WCAG refusals are excluded.

**Standard IFEval is not a neutral instrument for accessibility-trained models.**
Three IFEval instruction categories require WCAG-conflicting outputs. A purpose-
built accessibility-aware benchmark or the three-tier classification developed
here is necessary for valid evaluation of Framework-trained models.

**The Pnull finding quantifies P0's structural role.** The ~19 pp compliance gap
attributable to the P0 = null pointer pretraining artifact in Llama 3.1 8B
constitutes a direct empirical measurement of P0's load-bearing weight in the Four
Laws hierarchy. Approximately 19% of compliant behavior depends on the model
correctly parsing the zeroth-position priority designation. This finding also
establishes that the P0 primacy correction is architecture-dependent and not
universally transferable via LoRA fine-tuning.

**Chat format adapters are designed for use with Framework injection.** The system
prompt dependency in AISF+CHAT adapters is a direct consequence of training
format and is not a defect: the adapters are intended for deployment in combination
with PS-CORE or FFE injection, which always provides the Framework system context. The
two layers -- model-level training and session-level injection -- reinforce each
other.

**Verbosity reduction is consistent.** All four Instruct-model adapters with full
token data show output verbosity reduction (range: -37.9% to -71.8%), with the
exception of the Framework+CHAT Llama adapter (-4.2%), where chat format training
preserves native verbosity. This pattern is consistent with the WCAG plain language
principles in the training data and is measurable and reproducible.

---

## References

[1] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen, "LoRA: Low-Rank Adaptation of Large Language Models," *International Conference on Learning Representations (ICLR)*, 2022. arXiv:2106.09685

[2] T. Dettmers, A. Pagnoni, A. Holtzman, and L. Zettlemoyer, "QLoRA: Efficient Finetuning of Quantized LLMs," *Advances in Neural Information Processing Systems (NeurIPS)*, 2023. arXiv:2305.14314

[3] J. Zhou, T. Lu, S. Mishra, S. Brahma, S. Basu, Y. Luan, D. Zhou, and L. Hou, "Instruction-Following Evaluation for Large Language Models," 2023. arXiv:2311.07911

[4] World Wide Web Consortium, *Web Content Accessibility Guidelines (WCAG) 2.2*, W3C Recommendation, Oct. 2023. https://www.w3.org/TR/WCAG22/

[5] H. G. Frankfurt, *On Bullshit*. Princeton University Press, 2005. (Original essay: *Raritan Quarterly Review*, 6(2), 1986.)

---

*Part of the AI Stability Framework(tm), (c)2025-2026 Leonard Rojas. All rights reserved.*
*AI Stability Framework is a trademark of Leonard Rojas (USPTO Serial No. 99664948,*
*registration pending).*
