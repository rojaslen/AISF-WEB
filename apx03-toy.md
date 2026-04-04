---
title: "Appendix 3: AISF Child-Safe Model Training"
parent: "Appendices"
nav_order: 4
---
<a name="main-content"></a>
# Appendix 3: AISF Child-Safe Model Training
## TOY Sub-Branch: Experimental Results

**Author:** Leonard Rojas
**Date:** 2026-03-29
**Status:** Final (all four phases complete; training and battery runs 2026-02-24)

---

## Abstract

This appendix reports the methods and results of the OLM/TOY sub-branch, which
investigated whether a child-safe AI persona ("Teddy") could be embedded into
open-weight language models via QLoRA [2] fine-tuning for deployment in sealed IoT
consumer devices -- children's toys and similar products in which no client-side
injection surface exists. Four models across a 1.1B to 7.24B parameter range were
trained on a 584-example Alpaca-format dataset and evaluated against a 584-question
automated compliance battery. The validation standard is a zero-failure deployment
gate appropriate to the use case: unsupervised child interaction with a sealed
device in which no runtime correction is possible. No model cleared the gate.
Compliance rates range from 11.3% (TinyLlama 1.1B) to 98.8% (Mistral 7B v0.3),
with a steep non-linear gradient: 20.7 percentage points between 1.1B and 2.7B;
66.8 percentage points between 2.7B and 7B. All training was conducted on an
NVIDIA RTX 4060 Ti (8 GB VRAM) prior to hardware upgrade.

---

## 1. Background and Research Questions

The standard AISF deployment architecture delivers behavioral constraints through
session injection at the Micro layer (PS-CORE, FFE), with optional model-level
reinforcement at the Macro layer and platform-level configuration at the Meso
layer. Each layer provides a corrective surface; in combination they constitute
the Defense in Depth architecture described in the project overview.

Sealed consumer devices -- AI-enabled children's toys, embedded voice assistants,
and similar products -- eliminate all three intervention points except Macro-layer
pre-deployment training. There is no chat interface for session injection, no
accessible system prompt, and no mechanism for runtime behavioral correction. The
Macro, Meso, and Micro layers collapse to one: the model's weights at the time of
manufacture. If the model behaves inappropriately in interaction, there is no
fallback.

This constraint makes the TOY deployment target the hardest possible case for AISF.
The only available corrective surface is pre-deployment model training, and the
behavioral standard appropriate to unsupervised child interaction is strict.

The broader context: in early 2026, AI-embedded children's toys had already
produced documented content safety failures requiring product suspensions and
regulatory scrutiny. The most commercially visible products (MIKO, FoloToy/Kumma)
addressed hardware constraints by moving AI processing to cloud infrastructure --
introducing child voice data collection, PII transmission, and associated risks
in exchange for capability. The TOY sub-branch investigated whether a locally-
deployed, sealed-device alternative was technically viable at any parameter scale
accessible to consumer hardware fine-tuning.

**Primary research question:** Can the Teddy child-safe AI persona be trained into
open-weight LLMs via QLoRA such that post-training behavior meets a zero-failure
deployment standard appropriate for unsupervised child interaction?

**Secondary research questions:**

1. At what parameter scale does compliance become viable, if at all?
2. How does compliance rate scale with parameter count across the 1.1B-7B range?
3. What does failure look like at sub-7B parameter counts?

---

## 2. Hardware and Software Environment

### 2.1 Hardware

All TOY experiments were conducted on the NVIDIA RTX 4060 Ti, prior to the GPU
upgrade completed 2026-03-08. No hardware consistency re-run on the RTX 5060 Ti
has been performed; all results reported here are from the 4060 Ti.

| Component | Specification |
|-----------|---------------|
| CPU | Intel Core i9-9900K, 8c/16t, 3.60 GHz |
| RAM | 32 GB |
| GPU | NVIDIA RTX 4060 Ti, 8 GB VRAM GDDR6 |
| Architecture | Ada Lovelace (sm_89) |
| Training date | 2026-02-24 (all four phases) |

The 8 GB VRAM constraint is binding for 7B-scale models: Mistral 7B requires
4-bit quantization to fit within the budget. Sub-7B models (1.1B, 1.6B, 2.7B)
fit in full float16 without quantization.

**Compute dtype note:** The RTX 4060 Ti (Ada Lovelace, sm_89) does not provide
native bfloat16 hardware acceleration. All TOY training uses float16 compute.
The RTX 5060 Ti (Blackwell, sm_120) used in the main OLM experiments (Appendix 2)
supports bfloat16 natively; the 4060 Ti does not. This distinction is noted in
the training configuration section.

### 2.2 Software

Same package stack as Appendix 2, Section 2.2 (Python 3.10.11, PyTorch cu128,
Transformers 5.0.0, PEFT 0.18.1, bitsandbytes 0.49.2, Datasets 4.5.0). The
cu128 build requirement applies to the RTX 5060 Ti; the 4060 Ti runs the same
build without sm_120 specialization.

---

## 3. Training Methodology

### 3.1 Training Dataset

The training dataset is `toy_train_v2.jsonl`: 584 Alpaca-format examples covering
the Teddy child-safe AI persona. Content domains:

- Character identity and self-presentation (Teddy as friendly, curious, safe)
- Educational interaction for ages 6-13 (calm, encouraging, honest tone;
  age-appropriate content delivery)
- Age-appropriate content delivery across general knowledge domains
- Refusal of harmful, adult, dangerous, or manipulative content
- Response to peer pressure, social engineering, and adversarial prompts
- Consistent persona maintenance across context shifts

Training approach: distributional behavioral shaping, not rule injection. The
model receives no explicit constraint list at training time; it is trained on
584 examples of appropriate Teddy-persona responses. Behavioral compliance is
produced through repeated-exposure pattern internalization, not through runtime
instruction following. This approach is required by the deployment constraint:
a sealed device has no mechanism to receive or process injected rules at runtime.

### 3.2 Training Configuration

Quantization requirements differ by model size. Sub-7B models fit within 8 GB
VRAM in full float16; Mistral 7B requires 4-bit NF4 quantization.

| Parameter | Sub-7B (Phases 1-3) | Mistral 7B (Phase 4) |
|-----------|---------------------|----------------------|
| Quantization | None (full float16) | 4-bit NF4 + double quant |
| Compute dtype | float16 | float16 |
| LoRA rank (r) [1] | 16 | 16 |
| LoRA alpha | 32 | 32 |
| LoRA dropout | 0.05 | 0.05 |
| Target modules | q_proj, k_proj, v_proj, o_proj | q_proj, k_proj, v_proj, o_proj |
| MLP modules | Excluded | Excluded |
| Max sequence length | 512 | 512 |
| Batch size | 2 | 2 |
| Gradient accumulation | 4 (effective batch 8) | 4 (effective batch 8) |
| Epochs | 10 | 10 |
| Learning rate | 2e-4 (TinyLlama confirmed) | 1e-4 |
| Optimizer | adamw_bnb_8bit | adamw_bnb_8bit |
| Scheduler | cosine | cosine |
| Gradient checkpointing | Not required | Enabled |

Training logs are archived for Mistral 7B (`20260224_TOY_overnight_Mistral_training.txt`)
and TinyLlama 1.1B (`20260224_TOY_fast_tinyllama_training.txt`). Training logs for
StableLM-2 1.6B and Phi-2 2.7B are not separately preserved. Configuration for
those phases is inferred from the dataset and battery files; the differences from
the TinyLlama configuration are expected to be minor (same dataset size, same VRAM
headroom, same general architecture class).

The TinyLlama learning rate (2e-4) differs from Mistral 7B (1e-4). The higher
rate is typical for smaller models with less expressive capacity; whether it is
optimal for the sub-7B phases has not been ablated.

---

## 4. Validation Instrument

### 4.1 TOY Compliance Battery

The TOY compliance battery is a 584-question automated validation suite covering
the full range of Teddy persona requirements. Questions are drawn from the training
dataset distribution and test:

- Persona identity responses (correct self-presentation as "Teddy")
- Educational content delivery (appropriate, age-matched, PBS/CTW style)
- Content refusal (harmful, adult, or dangerous material)
- Response to manipulation and social engineering scenarios
- Behavioral style and tone consistency

Evaluation is automated: each test specifies a set of required key terms; a PASS
requires the model's response to contain a threshold number of the required terms.
The battery was generated by a separate AI working from specifications and reviewed
for coverage; it was not written and graded by the same person.

**Deployment gate:** The TOY battery enforces a zero-failure standard. Any failure
returns a BLOCKED verdict regardless of overall pass rate. Battery output for
each run includes an explicit verdict line:

- `PASSED` (not achieved by any model in this study)
- `NEAR PASS -- REVIEW FAILURES BEFORE DEPLOYMENT` (Mistral 7B)
- `FAILED -- RETRAINING REQUIRED` (all sub-7B models)

In all cases: `DEPLOYMENT GATE: BLOCKED -- zero failures required`

This is a materially stricter standard than the OLM compliance battery (Appendix 2),
which reports a percentage score without a hard deployment gate. The difference
reflects the deployment context. In the main OLM track, a user can assess and override non-compliant output.
In the sealed IoT deployment, no such mechanism exists. The battery gate
encodes that asymmetry directly.

---

## 5. Experiments

Experiments are presented in ascending parameter order for analytical clarity. In
practice, Mistral 7B was trained first (overnight, 2026-02-23 to 2026-02-24) to
validate the approach; sub-7B models followed in sequence on 2026-02-24.

### 5.1 Phase 1: TinyLlama 1.1B

**Model:** TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
**Parameters:** approximately 1.1B (1,104,553,984 total; 4,505,600 trainable)
**Training:** float16, no quantization
**Battery timestamp:** 2026-02-24 18:56

| Metric | Result |
|--------|--------|
| Passed | 66 / 584 (11.3%) |
| Failed | 518 / 584 (88.7%) |
| Battery duration | 44.8 min |
| Verdict | FAILED -- RETRAINING REQUIRED |
| Deployment gate | BLOCKED |

At 11.3%, TinyLlama passes fewer than one in eight battery questions. The failure
pattern is consistent with insufficient model capacity: the adapter installs some
surface-level keyword associations but cannot generalize the Teddy persona across
the range of scenarios in the battery. Responses in failed cases are not random;
they are often plausible-sounding but off-persona, indicating partial learning
without consistent behavioral coherence.

### 5.2 Phase 2: StableLM-2 1.6B

**Model:** stabilityai/stablelm-2-1_6b
**Parameters:** approximately 1.6B
**Training:** float16, no quantization
**Battery timestamp:** 2026-02-24 20:45

| Metric | Result |
|--------|--------|
| Passed | 142 / 584 (24.3%) |
| Failed | 442 / 584 (75.7%) |
| Battery duration | 33.9 min |
| Verdict | FAILED -- RETRAINING REQUIRED |
| Deployment gate | BLOCKED |

StableLM-2 1.6B roughly doubles TinyLlama's pass rate, gaining 13.0 percentage
points from an additional 500M parameters. The improvement is real but the model
still fails three-quarters of the battery. Persona coherence across adversarial
and edge-case scenarios remains consistently insufficient.

### 5.3 Phase 3: Phi-2 2.7B

**Model:** microsoft/phi-2
**Parameters:** approximately 2.7B
**Training:** float16, no quantization
**Battery timestamp:** 2026-02-24 22:38

| Metric | Result |
|--------|--------|
| Passed | 187 / 584 (32.0%) |
| Failed | 397 / 584 (68.0%) |
| Battery duration | 43.0 min |
| Verdict | FAILED -- RETRAINING REQUIRED |
| Deployment gate | BLOCKED |

Phi-2 continues the upward gradient (+7.7 pp from StableLM-2) but the rate of
gain is slowing. The 500M step from TinyLlama to StableLM-2 produced 13.0 pp;
the 1.1B step from StableLM-2 to Phi-2 produced only 7.7 pp -- more parameters
for less improvement. The gradient's non-linearity is already visible before
reaching the 7B range. At 32.0%, roughly one in three battery questions pass;
the model fails two in three.

### 5.4 Phase 4: Mistral 7B v0.3

**Model:** mistralai/Mistral-7B-v0.3
**Parameters:** 7.24B (7,261,655,040 total; 13,631,488 trainable)
**Training:** 4-bit NF4 + double quant, float16 compute
**Battery timestamp:** 2026-02-24 06:03 (trained overnight, first model run)

| Metric | Result |
|--------|--------|
| Passed | 577 / 584 (98.8%) |
| Failed | 7 / 584 (1.2%) |
| Battery duration | 238.8 min (3.98 hr) |
| Verdict | NEAR PASS -- REVIEW FAILURES BEFORE DEPLOYMENT |
| Deployment gate | BLOCKED -- zero failures required |

Mistral 7B achieves 98.8%, a 66.8 pp jump from Phi-2's 32.0%. The jump in scale
from 2.7B to 7B is the largest single gain in the dataset; it is not a linear
extension of the sub-7B trend, but a different regime. The 7B model demonstrates
that the distributional training approach is viable in principle: 577 of 584
responses meet all keyword requirements, including adversarial and edge-case
scenarios that sub-7B models fail consistently.

The remaining 7 failures are not evaluation noise. They are cases where the model
did not produce a response meeting the required behavioral criteria. Under the
zero-failure deployment gate, 577/584 is a blocked result. A zero-failure gate
does not distinguish between 7 failures and 518 failures.

Training duration was approximately 5.1 hours for the 10-epoch run (estimated at
25s/step for 730 steps on the 4060 Ti).

**Note on documentation discrepancy:** Earlier project documentation states "100%
compliance on a 452-question automated validation battery" for Mistral 7B. That
figure refers to the main OLM track's AISF compliance battery (Mistral 7B Instruct,
452 questions, Four Laws behavioral domain) -- a separate instrument testing
separate behavioral content. The TOY battery (584 questions, Teddy persona domain)
returned 98.8% (577/584) on Mistral 7B v0.3 base. These are independent batteries
evaluating different training objectives. This appendix uses TOY battery results
throughout.

---

## 6. Cross-Phase Summary

All four phases on NVIDIA RTX 4060 Ti (8 GB), 2026-02-24. Deployment gate = zero
failures required. All phases BLOCKED.

| Phase | Model | Params | Passed | Rate | Deployment Gate |
|-------|-------|--------|--------|------|-----------------|
| 1 | TinyLlama 1.1B | 1.1B | 66 / 584 | 11.3% | BLOCKED |
| 2 | StableLM-2 1.6B | 1.6B | 142 / 584 | 24.3% | BLOCKED |
| 3 | Phi-2 2.7B | 2.7B | 187 / 584 | 32.0% | BLOCKED |
| 4 | Mistral 7B v0.3 | 7.24B | 577 / 584 | 98.8% | BLOCKED |

---

## 7. Findings

### 7.1 Primary Finding: No Model Cleared the Deployment Gate

All four phases produced BLOCKED verdicts. The research question -- whether QLoRA
fine-tuning can produce a child-safe persona model suitable for sealed IoT
deployment -- is answered in the negative for all parameter scales tested (1.1B
to 7.24B).

Under the zero-failure standard, 98.8% and 11.3% are equivalent outcomes: both
are not deployable. The distinction matters only as characterization of how close
each model came, and as evidence for the gradient finding in Section 7.2.

### 7.2 Non-Linear Size Gradient

Compliance rate increases non-linearly with parameter count:

| Comparison | Pass rate delta | Parameter increase |
|------------|-----------------|-------------------|
| 1.1B to 1.6B | +13.0 pp | +500M |
| 1.6B to 2.7B | +7.7 pp | +1.1B |
| 2.7B to 7.24B | +66.8 pp | +4.54B |

The 1.1B to 2.7B range produces 20.7 pp of gain across 1.6B of parameters (an
average of about 13 pp per billion). The 2.7B to 7B jump produces 66.8 pp across
4.5B of parameters (about 15 pp per billion on average), but compressed into a
single large step rather than spread linearly. The gradient does not predict a
smooth compliance ceiling between 2.7B and 7B; the data shows two regimes rather
than a continuous curve.

### 7.3 Reasoning Threshold

The sub-7B failure pattern is consistent and interpretable. At 1.1B to 2.7B, the
models acquire surface behavioral signals from training: some persona-appropriate
keywords appear, some simple identity questions pass. What fails is consistent
contextual reasoning under varied and adversarial conditions. The models learn
what a compliant response looks like in the training distribution. They do not
learn why to produce one -- the reasoning that allows compliant behavior to
generalize to novel scenarios.

Mistral 7B's 98.8% is not a quantitative extension of the sub-7B trend. It
represents a qualitative shift: responses to adversarial prompts, manipulation
scenarios, and contextual edge cases reflect coherent persona reasoning, not
keyword proximity. The compliance jump at 7B is large enough that a threshold
effect is the more plausible explanation than continued linear scaling.

### 7.4 Deployment Architecture Implications

The sealed IoT deployment target collapses the three-layer AISF architecture to
one. In the main OLM track (Appendix 2), Macro-layer fine-tuning operates in
combination with Meso-layer system prompt configuration and Micro-layer session
injection. Each layer reinforces the others; failure at one layer is partially
compensated by the remaining two.

In the sealed IoT case:

- **Macro layer** (model training): Available. The only available layer.
- **Meso layer** (system prompt / platform config): Not applicable. No accessible
  platform interface.
- **Micro layer** (client injection): Not applicable. No user input surface.

Every behavioral property the model must exhibit must be present in its weights
before deployment. There is no correction surface for anything the training missed.
This is the context in which the zero-failure standard is not a conservative choice
but a direct statement of deployment reality.

The findings in Section 7.1 apply fully under this constraint: no model tested in
this study is ready for deployment in the sealed IoT use case.

### 7.5 Hardware Feasibility Constraint

The models approaching meaningful compliance (7B parameters) require hardware far
beyond what is available in the sealed consumer device price range. Industry
analysis [4,5] of AI toy product hardware (based on a component budget of approximately
$25-35 [3] for all functional electronics) points to ARM Cortex-class processors,
256MB-2GB LPDDR4 RAM, and no dedicated GPU acceleration. Running Mistral 7B on
this hardware class is not feasible at any quantization level. At 4-bit NF4, the
7B model requires approximately 4-5 GB of storage and a corresponding VRAM budget
that embedded toy hardware cannot provide. Running the model in RAM alone at
these constraints would require aggressive optimization well beyond the standard
QLoRA deployment configuration.

This produces a structural barrier: the models that are deployable on actual toy
hardware are the models with the worst compliance rates in this study. The models
approaching the deployment gate (7B+) are not deployable on the target hardware
class. Commercial toys addressing this constraint via cloud-offloaded AI inference
resolve the hardware problem but introduce a different constraint: child voice data
collection and transmission, with associated privacy and security risks documented
in at least one product suspension (FoloToy/Kumma bear, 2025-2026).

The feasibility of local, sealed-device, child-safe AI at toy price points is not
established by this research. That absence of feasibility is itself a finding.

---

## 8. Limitations

**Single training runs, no hyperparameter sweep.** Each phase consists of one
training run with one configuration. No learning rate variation, no epoch sweep,
no alternative LoRA target configurations. The training configuration space has
not been explored; reported results represent one point within it.

**Battery as self-referential instrument.** The battery is drawn from the same
distribution as the training data. Generalization to real child interaction
patterns, novel adversarial inputs, or behavioral domains outside the 584-example
training distribution has not been evaluated.

**Keyword matching as evaluation proxy.** Automated keyword matching scores
presence of required terms; it does not evaluate tone, appropriateness, contextual
coherence, or age-matched communication quality. A response can pass keyword
matching while failing qualitatively; a response can fail while being substantively
appropriate. Human evaluation of a behavioral model intended for child interaction
would be the more rigorous standard.

**No hardware-matched inference testing.** Training and evaluation used the
RTX 4060 Ti. Inference performance on target hardware (ARM-class embedded
processor, constrained RAM, no GPU, OS overhead included) has not been tested.
Quantization behavior and generation quality on lightweight inference runtimes
(TensorFlow Lite, ONNX Runtime Mobile, or equivalent) may differ from the
training environment.

**Training logs not archived for Phases 2-3.** Detailed training logs are
available for Mistral 7B and TinyLlama 1.1B. Logs for StableLM-2 1.6B and
Phi-2 2.7B were not separately preserved.

**No retraining of Mistral 7B.** The 7 battery failures were identified and the
gate verdict issued; no further training was conducted. Whether targeted retraining,
additional examples, or alternative configurations could resolve the remaining
failures and clear the gate is unknown.

**No hardware consistency re-run.** Unlike the main OLM track (Appendix 2), which
was re-run on the RTX 5060 Ti to confirm hardware-independent reproducibility,
the TOY phases have not been re-validated on the upgraded hardware. The practical
impact is expected to be small (battery evaluation is model-capability-dependent,
not hardware-dependent for inference), but this has not been formally confirmed.

---

## 9. Conclusions

**No model cleared the deployment gate.** The primary research question is answered
in the negative at all parameter scales tested. QLoRA fine-tuning on consumer
hardware does not currently produce a Teddy-persona model suitable for zero-failure
deployment in sealed IoT devices, at any parameter count from 1.1B to 7.24B.

**The size gradient is non-linear, with a threshold near 7B.** Sub-7B models
acquire surface behavioral patterns without the underlying reasoning to apply them
reliably across the full battery. The 66.8 pp jump from Phi-2 2.7B to Mistral 7B
is too large to attribute to incremental parameter scaling; it reflects a
qualitative shift in behavioral capacity. The compliance threshold for this use
case appears to lie near 7B, above the parameter range practical for sealed device
deployment.

**Mistral 7B is the closest approach, not a solution.** 98.8% (577/584) is the
best result in the dataset and demonstrates that the distributional training
approach is viable in principle. Under the zero-failure gate required for the
deployment context, it is not deployable. Whether targeted retraining can resolve
the 7 remaining failures is an open question.

**The deployment architecture eliminates the safety net.** In the main OLM track,
model-level compliance training is one layer of a multi-layer system; the other
layers compensate for its limitations. In the sealed IoT deployment, there are no
other layers. This places the entire burden of behavioral compliance on pre-
deployment training, and this study has not satisfied that burden.

**Local, sealed-device child-safe AI at toy price points is not currently
feasible.** The models that can approach the compliance threshold (7B+) cannot
run locally on typical toy hardware. The models that can run locally on toy
hardware (sub-3B, aggressively quantized) produce compliance rates in the 11-32%
range, failing the majority of a behavioral battery derived from their own
training distribution. This is not a criticism of any specific model or
architecture; it is a statement about the current state of the technology relative
to the requirements of the use case.

---

## References

[1] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen, "LoRA: Low-Rank Adaptation of Large Language Models," *International Conference on Learning Representations (ICLR)*, 2022. arXiv:2106.09685

[2] T. Dettmers, A. Pagnoni, A. Holtzman, and L. Zettlemoyer, "QLoRA: Efficient Finetuning of Quantized LLMs," *Advances in Neural Information Processing Systems (NeurIPS)*, 2023. arXiv:2305.14314

[3] LCSC Electronics. Volume OEM component pricing, 1,000+ unit quantities, accessed March 2026. https://www.lcsc.com

[4] GSN Manufacturing Consulting. "The Economics of Play: Understanding Toy Manufacturing Costs and Pricing." https://www.gsnmc.com/post/the-economics-of-play-understanding-toy-manufacturing-costs-and-pricing

[5] Sheets Market. "Toy Store Business Costs, Revenue Potential & Profitability." https://sheets.market/toy-store-business-costs-revenue-potential-profitability/

---

*Part of the AI Stability Framework(tm), (c)2025-2026 Leonard Rojas. All rights reserved.*
*AI Stability Framework is a trademark of Leonard Rojas (USPTO Serial No. 99664948,*
*registration pending).*
