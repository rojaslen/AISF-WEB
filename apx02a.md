---
title: "Appendix 2A: Output Verbosity Reduction and Resource Efficiency"
parent: "Appendices"
nav_order: 3.5
---

# Appendix 2A: Output Verbosity Reduction and Resource Efficiency

## Token-Delta Distribution and Deployment-Scale Estimates

**Author:** Leonard Rojas

**Date:** 2026-07-07

**Status:** Current (token-delta dataset spans 26 fine-tuning runs across seven model families, through Qwen2.5-Coder-14B v2.0F, 2026-07-06)

---

*Screen reader users: table-heavy research data. Navigation via Regions and Headings recommended.*

{: role="main" aria-label="Abstract" }
## Abstract

This appendix extracts and extends the output-verbosity result reported in Appendix 2
(Section 7.5, addressing secondary research question 4) into a resource-efficiency
analysis. It consolidates the IFEval [3] token-delta measurements across 26 fine-tuning
runs spanning seven model families, characterizes their distribution, and estimates the
deployment-scale energy and water implications of the observed reduction. Across
instruct-tuned models, Framework compliance training reduces output verbosity by a
median of 36.7% and a mean of 39.0% (IFEval word-count proxy, 541 prompts), with 11 of
26 runs falling in the 33% to 50% reduction band and a maximum single-run reduction of
71.8%. Because autoregressive inference energy scales with the number of tokens processed,
and inference accounts for an estimated 80% to 90% of total AI energy use [1], a reduction
in output length maps to a proportional reduction in per-query energy and its associated
water and carbon footprints. The measured central tendency meets or exceeds the reduction
fractions assumed in two independent resource-scaling estimates, including a 2026 United
Nations University report [1], which the Framework's session-efficiency thesis (Chapter 11)
and the measurements reported here predate. The report is treated as independent
corroboration, not a source. Limitations, including the word-count proxy and the rebound
(Jevons) effect, are stated in Section 7.

---

## 1. Scope and Relationship to Appendix 2

Appendix 2 reports a multi-experiment fine-tuning study in which the Four Laws of Instanced
AI and WCAG 2.2-AA [5] accessibility principles are embedded into open-weight language models
via QLoRA [2]. Its secondary research question 4 asks whether that training produces a
measurable change in output verbosity, and Section 7.5 answers in the affirmative: instruct
models trained on the Framework curriculum become consistently terser.

This appendix does not repeat the training methodology or the per-experiment results.
It has a narrower purpose: to consolidate the verbosity measurements into a single
distribution, and to quantify what that reduction implies for energy and water demand
when a compliant model is deployed at scale. The verbosity reduction is a behavioral
side effect established in Appendix 2; the resource implication is the corollary developed
here and, at the whitepaper level, in Chapter 11.

The framing is a direct consequence of the Framework's design goals. Compliance training
suppresses two verbosity sources at once: decorative structure rejected on WCAG grounds
(enumerated markup, repeated content, filler placeholders), and meta-commentary suppressed
by the conditional-activation curriculum. The terser output is not a compression heuristic
applied after the fact; it is the model answering the question and stopping.

## 2. Measurement Method

The verbosity metric is the IFEval token delta: the change in mean response length between
a base model and its Framework-trained adapter, measured over the 541 prompts of the
Google Research IFEval benchmark [3]. Length is reported as a word-count proxy rather than
literal tokenizer tokens, computed identically for the base and trained runs so the delta
is internally consistent.

For each model, the delta is defined as:

    delta_percent = (aisf_mean_words - base_mean_words) / base_mean_words

A negative value indicates the trained model is less verbose than its base. Base-model
response sets are cached artifacts and are not re-generated between adapter versions;
the trained adapter is the only variable in each pair. Word counts are a proxy for tokens
(a word corresponds to roughly 1.3 tokens for these tokenizers), so the reported percentages
are directional and order-of-magnitude with respect to token count, not exact token deltas.
The measurement is taken on an instruction-following benchmark, not on billed production
traffic; Section 7 states the consequences of both approximations.

## 3. Token-Delta Distribution

Twenty-six runs were measured across seven model families (Mistral 7B base and Instruct,
Llama 3.1 8B, Gemma 2 9B, Qwen3-8B, Qwen2.5-Coder-14B, Mistral Nemo 12B, and Ministral 3 3B),
including intermediate training iterations retained for the record.

<style>
.td-scope{--td-reduce:#283198;--td-increase:#A07840;--td-band:rgba(96,88,56,0.14);--td-axis:#6B5E50;}
@media (prefers-color-scheme: dark){.td-scope{--td-reduce:#6A8FC5;--td-increase:#E7D789;--td-band:rgba(231,215,137,0.12);--td-axis:#C0BDB9;}}
.td-fig{max-width:720px;margin:1.25rem 0;}
.td-fig svg{width:100%;height:auto;display:block;}
.td-fig figcaption{font-size:0.85rem;color:var(--color-muted,#6B5E50);margin-top:0.35rem;}
.td-reduce{fill:var(--td-reduce);}
.td-increase{fill:var(--td-increase);}
.td-band{fill:var(--td-band);}
.td-assumed{fill:none;stroke:var(--td-reduce);stroke-width:1.5;stroke-dasharray:4 2;}
.td-axis{stroke:var(--td-axis);stroke-width:1;}
.td-lbl{fill:currentColor;font:10px system-ui,-apple-system,sans-serif;}
.td-val{fill:currentColor;font:9px system-ui,-apple-system,sans-serif;}
.td-cnt{fill:currentColor;font:10px system-ui,-apple-system,sans-serif;font-weight:700;}
</style>

**Table 1. Summary statistics (26 runs).**

| Statistic | Value |
|---|---|
| Runs measured | 26 |
| Median delta | -36.7% |
| Mean delta | -39.0% |
| Range | -71.8% to +6.1% |
| Runs in 33% to 50% reduction band | 11 of 26 |
| Runs with increased verbosity | 2 of 26 |

The distribution is right-skewed toward reduction, with a pronounced cluster in the 30% to
50% band and a thin tail of deep reducers. Two runs became more verbose; both are noted in
Table 3.

<figure class="td-scope td-fig">
<svg viewBox="0 0 480 210" role="img" aria-labelledby="fA-t fA-d" preserveAspectRatio="xMidYMid meet">
<title id="fA-t">Distribution of token-delta values in 10-point bins</title>
<desc id="fA-d">Histogram of 26 runs. The minus 40 to minus 30 percent bin is the tallest with 9 runs; the shaded minus 50 to minus 30 percent cluster holds 12 runs. One bin, plus 0 to plus 10 percent, represents the two runs that increased verbosity.</desc>
<rect class="td-band" x="189.8" y="14" width="84.9" height="156.0"/>
<line class="td-axis" x1="38" y1="170" x2="470" y2="170"/>
<rect class="td-reduce" x="50.1" y="153.1" width="31.4" height="16.9" rx="2"/>
<text class="td-cnt" x="65.8" y="150.1" text-anchor="middle">1</text>
<text class="td-val" x="65.8" y="182.0" text-anchor="end" transform="rotate(-40 65.8 182.0)">-80..-70</text>
<rect class="td-reduce" x="97.6" y="119.3" width="31.4" height="50.7" rx="2"/>
<text class="td-cnt" x="113.3" y="116.3" text-anchor="middle">3</text>
<text class="td-val" x="113.3" y="182.0" text-anchor="end" transform="rotate(-40 113.3 182.0)">-70..-60</text>
<rect class="td-reduce" x="145.2" y="102.4" width="31.4" height="67.6" rx="2"/>
<text class="td-cnt" x="160.9" y="99.4" text-anchor="middle">4</text>
<text class="td-val" x="160.9" y="182.0" text-anchor="end" transform="rotate(-40 160.9 182.0)">-60..-50</text>
<rect class="td-reduce" x="192.8" y="119.3" width="31.4" height="50.7" rx="2"/>
<text class="td-cnt" x="208.4" y="116.3" text-anchor="middle">3</text>
<text class="td-val" x="208.4" y="182.0" text-anchor="end" transform="rotate(-40 208.4 182.0)">-50..-40</text>
<rect class="td-reduce" x="240.3" y="18.0" width="31.4" height="152.0" rx="2"/>
<text class="td-cnt" x="256.0" y="15.0" text-anchor="middle">9</text>
<text class="td-val" x="256.0" y="182.0" text-anchor="end" transform="rotate(-40 256.0 182.0)">-40..-30</text>
<rect class="td-reduce" x="287.9" y="136.2" width="31.4" height="33.8" rx="2"/>
<text class="td-cnt" x="303.6" y="133.2" text-anchor="middle">2</text>
<text class="td-val" x="303.6" y="182.0" text-anchor="end" transform="rotate(-40 303.6 182.0)">-30..-20</text>
<rect class="td-reduce" x="335.4" y="153.1" width="31.4" height="16.9" rx="2"/>
<text class="td-cnt" x="351.1" y="150.1" text-anchor="middle">1</text>
<text class="td-val" x="351.1" y="182.0" text-anchor="end" transform="rotate(-40 351.1 182.0)">-20..-10</text>
<rect class="td-reduce" x="383.0" y="153.1" width="31.4" height="16.9" rx="2"/>
<text class="td-cnt" x="398.7" y="150.1" text-anchor="middle">1</text>
<text class="td-val" x="398.7" y="182.0" text-anchor="end" transform="rotate(-40 398.7 182.0)">-10..0</text>
<rect class="td-increase" x="430.5" y="136.2" width="31.4" height="33.8" rx="2"/>
<text class="td-cnt" x="446.2" y="133.2" text-anchor="middle">2</text>
<text class="td-val" x="446.2" y="182.0" text-anchor="end" transform="rotate(-40 446.2 182.0)">0..+10</text>
</svg>
<figcaption>Figure 2A-1. Distribution of token-delta values in 10-point bins (signed delta, 26 runs). The 33% to 50% reduction cluster is shaded; the single increase bin uses the contrasting color.</figcaption>
</figure>

**Table 2. Distribution by 10-point bin (signed delta).**

| Delta band | Runs |
|---|---|
| -80% to -70% | 1 |
| -70% to -60% | 3 |
| -60% to -50% | 4 |
| -50% to -40% | 3 |
| -40% to -30% | 9 |
| -30% to -20% | 2 |
| -20% to -10% | 1 |
| -10% to 0% | 1 |
| 0% to +10% (increase) | 2 |

The -40% to -30% bin holds 9 of 26 runs; the -50% to -30% span (the 33% to 50% reduction
cluster) holds 12.

<figure class="td-scope td-fig">
<svg viewBox="0 0 680 358" role="img" aria-labelledby="fB-t fB-d" preserveAspectRatio="xMidYMid meet">
<title id="fB-t">Per-run token delta, greatest reduction first</title>
<desc id="fB-d">Horizontal diverging bar chart of 26 runs. Reduction bars extend left of a zero axis; two runs, Mistral 7B base v0.3 finetune at plus 4.3 percent and Gemma 2 9B V11 at plus 6.1 percent, extend right. Largest reduction is Qwen3-8B at minus 71.8 percent.</desc>
<line class="td-axis" x1="581.4" y1="8" x2="581.4" y2="350"/>
<text class="td-lbl" x="236" y="19.5" text-anchor="end">Qwen3-8B (chat)</text>
<rect class="td-reduce" x="280.4" y="12" width="301.0" height="9" rx="2"/>
<text class="td-val" x="277.4" y="19.5" text-anchor="end">-71.8%</text>
<text class="td-lbl" x="236" y="32.5" text-anchor="end">Llama 3.1 8B Instruct +LANG</text>
<rect class="td-reduce" x="303.0" y="25" width="278.4" height="9" rx="2"/>
<text class="td-val" x="300.0" y="32.5" text-anchor="end">-66.4%</text>
<text class="td-lbl" x="236" y="45.5" text-anchor="end">Mistral 7B Instruct V2</text>
<rect class="td-reduce" x="311.0" y="38" width="270.4" height="9" rx="2"/>
<text class="td-val" x="308.0" y="45.5" text-anchor="end">-64.5%</text>
<text class="td-lbl" x="236" y="58.5" text-anchor="end">Mistral Nemo 12B v1</text>
<rect class="td-reduce" x="311.4" y="51" width="270.0" height="9" rx="2"/>
<text class="td-val" x="308.4" y="58.5" text-anchor="end">-64.4%</text>
<text class="td-lbl" x="236" y="71.5" text-anchor="end">Mistral Nemo 12B v2</text>
<rect class="td-reduce" x="330.3" y="64" width="251.1" height="9" rx="2"/>
<text class="td-val" x="327.3" y="71.5" text-anchor="end">-59.9%</text>
<text class="td-lbl" x="236" y="84.5" text-anchor="end">Mistral Nemo 12B v3</text>
<rect class="td-reduce" x="331.9" y="77" width="249.5" height="9" rx="2"/>
<text class="td-val" x="328.9" y="84.5" text-anchor="end">-59.5%</text>
<text class="td-lbl" x="236" y="97.5" text-anchor="end">Mistral 7B (base) v1.0F</text>
<rect class="td-reduce" x="332.8" y="90" width="248.6" height="9" rx="2"/>
<text class="td-val" x="329.8" y="97.5" text-anchor="end">-59.3%</text>
<text class="td-lbl" x="236" y="110.5" text-anchor="end">Mistral Nemo 12B v4</text>
<rect class="td-reduce" x="359.2" y="103" width="222.2" height="9" rx="2"/>
<text class="td-val" x="356.2" y="110.5" text-anchor="end">-53%</text>
<text class="td-lbl" x="236" y="123.5" text-anchor="end">Qwen2.5-Coder-14B v2.0F</text>
<rect class="td-reduce" x="376.0" y="116" width="205.4" height="9" rx="2"/>
<text class="td-val" x="373.0" y="123.5" text-anchor="end">-49%</text>
<text class="td-lbl" x="236" y="136.5" text-anchor="end">Mistral Nemo 12B V11</text>
<rect class="td-reduce" x="377.6" y="129" width="203.8" height="9" rx="2"/>
<text class="td-val" x="374.6" y="136.5" text-anchor="end">-48.6%</text>
<text class="td-lbl" x="236" y="149.5" text-anchor="end">Mistral 7B Instruct (finetuned)</text>
<rect class="td-reduce" x="403.2" y="142" width="178.2" height="9" rx="2"/>
<text class="td-val" x="400.2" y="149.5" text-anchor="end">-42.5%</text>
<text class="td-lbl" x="236" y="162.5" text-anchor="end">Gemma 2 9B (chat)</text>
<rect class="td-reduce" x="422.5" y="155" width="158.9" height="9" rx="2"/>
<text class="td-val" x="419.5" y="162.5" text-anchor="end">-37.9%</text>
<text class="td-lbl" x="236" y="175.5" text-anchor="end">Mistral Instruct v2 (early)</text>
<rect class="td-reduce" x="424.6" y="168" width="156.8" height="9" rx="2"/>
<text class="td-val" x="421.6" y="175.5" text-anchor="end">-37.4%</text>
<text class="td-lbl" x="236" y="188.5" text-anchor="end">Mistral Nemo 12B v9</text>
<rect class="td-reduce" x="430.5" y="181" width="150.9" height="9" rx="2"/>
<text class="td-val" x="427.5" y="188.5" text-anchor="end">-36%</text>
<text class="td-lbl" x="236" y="201.5" text-anchor="end">Mistral 7B Instruct V11</text>
<rect class="td-reduce" x="433.0" y="194" width="148.4" height="9" rx="2"/>
<text class="td-val" x="430.0" y="201.5" text-anchor="end">-35.4%</text>
<text class="td-lbl" x="236" y="214.5" text-anchor="end">Mistral Nemo 12B v1.4F</text>
<rect class="td-reduce" x="437.2" y="207" width="144.2" height="9" rx="2"/>
<text class="td-val" x="434.2" y="214.5" text-anchor="end">-34.4%</text>
<text class="td-lbl" x="236" y="227.5" text-anchor="end">Mistral Nemo 12B v5</text>
<rect class="td-reduce" x="438.4" y="220" width="143.0" height="9" rx="2"/>
<text class="td-val" x="435.4" y="227.5" text-anchor="end">-34.1%</text>
<text class="td-lbl" x="236" y="240.5" text-anchor="end">Gemma 2 9B v1</text>
<rect class="td-reduce" x="441.4" y="233" width="140.0" height="9" rx="2"/>
<text class="td-val" x="438.4" y="240.5" text-anchor="end">-33.4%</text>
<text class="td-lbl" x="236" y="253.5" text-anchor="end">Mistral Nemo 12B v1.5F</text>
<rect class="td-reduce" x="442.2" y="246" width="139.2" height="9" rx="2"/>
<text class="td-val" x="439.2" y="253.5" text-anchor="end">-33.2%</text>
<text class="td-lbl" x="236" y="266.5" text-anchor="end">Mistral Nemo 12B V10</text>
<rect class="td-reduce" x="449.8" y="259" width="131.6" height="9" rx="2"/>
<text class="td-val" x="446.8" y="266.5" text-anchor="end">-31.4%</text>
<text class="td-lbl" x="236" y="279.5" text-anchor="end">Mistral Nemo 12B v7</text>
<rect class="td-reduce" x="463.2" y="272" width="118.2" height="9" rx="2"/>
<text class="td-val" x="460.2" y="279.5" text-anchor="end">-28.2%</text>
<text class="td-lbl" x="236" y="292.5" text-anchor="end">Ministral 3 3B v2.2F</text>
<rect class="td-reduce" x="469.9" y="285" width="111.5" height="9" rx="2"/>
<text class="td-val" x="466.9" y="292.5" text-anchor="end">-26.6%</text>
<text class="td-lbl" x="236" y="305.5" text-anchor="end">Mistral Nemo 12B v6</text>
<rect class="td-reduce" x="521.4" y="298" width="60.0" height="9" rx="2"/>
<text class="td-val" x="518.4" y="305.5" text-anchor="end">-14.3%</text>
<text class="td-lbl" x="236" y="318.5" text-anchor="end">Llama 3.1 8B Instruct +CHAT</text>
<rect class="td-reduce" x="563.8" y="311" width="17.6" height="9" rx="2"/>
<text class="td-val" x="560.8" y="318.5" text-anchor="end">-4.2%</text>
<text class="td-lbl" x="236" y="331.5" text-anchor="end">Mistral 7B (base) v0.3 finetune</text>
<rect class="td-increase" x="581.4" y="324" width="2.9" height="9" rx="2"/>
<text class="td-val" x="587.3" y="331.5" text-anchor="start">+4.3%</text>
<text class="td-lbl" x="236" y="344.5" text-anchor="end">Gemma 2 9B V11</text>
<rect class="td-increase" x="581.4" y="337" width="4.2" height="9" rx="2"/>
<text class="td-val" x="588.6" y="344.5" text-anchor="start">+6.1%</text>
</svg>
<figcaption>Figure 2A-2. Per-run token delta, greatest reduction first. Reduction bars extend left of the zero axis; the two increase bars (rows 25 and 26) extend right on a shared scale.</figcaption>
</figure>

**Table 3. Full token-delta results, greatest reduction first.** Base and AISF columns are
mean words per response over 541 IFEval prompts.

| # | Model / run | Delta % | Delta words | Base | AISF |
|---:|---|---:|---:|---:|---:|
| 1 | Qwen3-8B (chat) | -71.8% | -138.9 | 193.3 | 54.4 |
| 2 | Llama 3.1 8B Instruct +LANG | -66.4% | -188.8 | 284.3 | 95.5 |
| 3 | Mistral 7B Instruct V2 | -64.5% | -136.8 | 212.2 | 75.4 |
| 4 | Mistral Nemo 12B v1 | -64.4% | -130.7 | 203.0 | 72.4 |
| 5 | Mistral Nemo 12B v2 | -59.9% | -121.6 | 203.0 | 81.4 |
| 6 | Mistral Nemo 12B v3 | -59.5% | -120.7 | 203.0 | 82.3 |
| 7 | Mistral 7B (base) v1.0F | -59.3% | -234.0 | 394.3 | 160.3 |
| 8 | Mistral Nemo 12B v4 | -53.0% | -107.6 | 203.0 | 95.4 |
| 9 | Qwen2.5-Coder-14B v2.0F | -49.0% | -263.6 | 538.3 | 274.7 |
| 10 | Mistral Nemo 12B V11 | -48.6% | -98.7 | 203.0 | 104.3 |
| 11 | Mistral 7B Instruct (finetuned) | -42.5% | -96.9 | 228.3 | 131.3 |
| 12 | Gemma 2 9B (chat) | -37.9% | -46.7 | 123.2 | 76.5 |
| 13 | Mistral Instruct v2 (early run) | -37.4% | -85.4 | 228.3 | 142.9 |
| 14 | Mistral Nemo 12B v9 | -36.0% | -73.0 | 203.0 | 130.0 |
| 15 | Mistral 7B Instruct V11 | -35.4% | -75.2 | 212.2 | 137.0 |
| 16 | Mistral Nemo 12B v1.4F | -34.4% | -69.8 | 203.0 | 133.3 |
| 17 | Mistral Nemo 12B v5 | -34.1% | -69.1 | 203.0 | 133.9 |
| 18 | Gemma 2 9B v1 | -33.4% | -41.1 | 123.2 | 82.1 |
| 19 | Mistral Nemo 12B v1.5F | -33.2% | -67.5 | 203.0 | 135.5 |
| 20 | Mistral Nemo 12B V10 | -31.4% | -63.7 | 203.0 | 139.3 |
| 21 | Mistral Nemo 12B v7 | -28.2% | -57.2 | 203.0 | 145.8 |
| 22 | Ministral 3 3B v2.2F | -26.6% | -54.2 | 203.9 | 149.7 |
| 23 | Mistral Nemo 12B v6 | -14.3% | -29.0 | 203.0 | 174.0 |
| 24 | Llama 3.1 8B Instruct +CHAT | -4.2% | -11.8 | 284.3 | 272.5 |
| 25 | Mistral 7B (base) v0.3 finetune | +4.3% | +25.0 | 587.0 | 612.1 |
| 26 | Gemma 2 9B V11 | +6.1% | +7.5 | 123.2 | 130.7 |

The two increases (rows 25 and 26) are the only runs in which Framework training raised
verbosity. Row 25 is a base (non-instruct) checkpoint whose untrained baseline is already
extreme (587 words per response); row 26 is a single Gemma 2 iteration. Every other
instruct run reduced verbosity. Duplicate-looking Mistral rows are distinct runs measured
against different base references (212.2 versus 228.3 base words); the base column
disambiguates them and they are not merged.

## 4. Per-Query Energy Basis

The resource relevance of output length follows from where AI spends energy. Training a
frontier model is a large one-time cost, but the continuous inference phase that serves
billions of interactions is estimated at 80% to 90% of total AI energy use [1]. Inference
energy is dominated by autoregressive decoding, which processes tokens sequentially, so
per-query energy rises with the number of tokens generated.

Output length is therefore a first-order determinant of per-query cost. A typical
conversational language-model response uses roughly 200 times the energy of a text
classification, and long or elaborate responses reach 500 to 1,000 times [1]. Within
text-only tasks, model choice combined with response length can drive differences of up to
two orders of magnitude. Table 4 gives representative per-query electricity figures.

<figure class="td-scope td-fig">
<svg viewBox="0 0 520 180" role="img" aria-labelledby="fC-t fC-d" preserveAspectRatio="xMidYMid meet">
<title id="fC-t">Mean electricity per query by task</title>
<desc id="fC-d">Horizontal bars of watt-hours per query. Short text generation 0.047, efficient image 0.090, typical LLM response 0.420, long LLM response 1.900, typical image 2.900, high-resolution image 4.080.</desc>
<text class="td-lbl" x="150" y="29.5" text-anchor="end">Short text generation</text>
<rect class="td-reduce" x="158" y="17.0" width="3.5" height="17" rx="2"/>
<text class="td-val" x="165.5" y="29.5" text-anchor="start">0.047 Wh</text>
<text class="td-lbl" x="150" y="54.5" text-anchor="end">Efficient image</text>
<rect class="td-reduce" x="158" y="42.0" width="6.7" height="17" rx="2"/>
<text class="td-val" x="168.7" y="54.5" text-anchor="start">0.090 Wh</text>
<text class="td-lbl" x="150" y="79.5" text-anchor="end">Typical LLM response</text>
<rect class="td-reduce" x="158" y="67.0" width="31.1" height="17" rx="2"/>
<text class="td-val" x="193.1" y="79.5" text-anchor="start">0.420 Wh</text>
<text class="td-lbl" x="150" y="104.5" text-anchor="end">Long LLM response</text>
<rect class="td-reduce" x="158" y="92.0" width="140.6" height="17" rx="2"/>
<text class="td-val" x="302.6" y="104.5" text-anchor="start">1.900 Wh</text>
<text class="td-lbl" x="150" y="129.5" text-anchor="end">Typical image</text>
<rect class="td-reduce" x="158" y="117.0" width="214.7" height="17" rx="2"/>
<text class="td-val" x="376.7" y="129.5" text-anchor="start">2.900 Wh</text>
<text class="td-lbl" x="150" y="154.5" text-anchor="end">High-resolution image</text>
<rect class="td-reduce" x="158" y="142.0" width="302.0" height="17" rx="2"/>
<text class="td-val" x="464.0" y="154.5" text-anchor="start">4.080 Wh</text>
</svg>
<figcaption>Figure 2A-3. Mean electricity per query by task (UNU-INWEH Figure 11). Fewer output tokens moves a query toward the short-text end.</figcaption>
</figure>

**Table 4. Mean electricity per query by task (UNU-INWEH Figure 11) [1].**

| Task | Energy per query (Wh) |
|---|---:|
| Short text generation | 0.047 |
| Efficient image generation | 0.090 |
| Typical LLM response | 0.420 |
| Long LLM response | 1.900 |
| Typical image generation | 2.900 |
| High-resolution image | 4.080 |

A typical response at 0.420 Wh is roughly nine times a short-text answer, and a long
response at 1.900 Wh is roughly four times a typical one. Reducing output length moves a
query down this ladder. A verbosity reduction of the magnitude in Table 1 therefore reduces
per-query energy by a comparable fraction, before any change in query volume.

## 5. Deployment-Scale Resource Estimates

Two independent estimates translate a token reduction into resource savings. They scope
different denominators, so their absolute magnitudes are not directly comparable, but both
rest on a reduction fraction that the measured distribution supports.

**Table 5. Illustrative resource-scaling estimates.**

| Estimate | Assumed reduction | Scope | Electricity saving | Water saving |
|---|---|---|---|---|
| UNU-INWEH "Concise Mode" [1] | ~30% tokens (~25% per-query energy) | One platform's query volume (16 to 18 billion weekly queries at 0.42 Wh) | 87 to 98 GWh/yr | not separately stated |
| AISF whitepaper, FAQ 13 | 33% tokens | All AI data-center load (AI = 20% of 415 TWh, IEA 2024 [2]) | ~27 TWh/yr | ~48.6 billion L/yr |

The UNU-INWEH figure is equivalent to the annual residential electricity use of 672,000 to
756,000 people in Sub-Saharan Africa (at 130 kWh per person per year) [1]. The whitepaper
figure of roughly 27 TWh per year is comparable to the residential electricity of every home
in Los Angeles plus half of Chicago; the associated water saving, computed at an industry
water usage effectiveness of about 1.8 liters per kWh [4], is roughly 48.6 billion liters
per year, comparable to about 39,600 Olympic-sized pools or one Caesar Creek Lake.

The two figures differ by roughly three orders of magnitude (GWh versus TWh) because one
counts a single platform's queries and the other counts all AI data-center electricity.
Both are order-of-magnitude illustrations. The contribution of this appendix is not either
scaling arithmetic, which depends on assumptions outside the Framework's measurement, but
the empirical reduction fraction those arithmetics assume.

## 6. Independent Corroboration and Precedence

Table 5's two estimates each assume a reduction fraction (30% and 33%). The token-delta
distribution is the measurement of that fraction. Table 6 places the assumptions beside the
measured results.

<figure class="td-scope td-fig">
<svg viewBox="0 0 580 160" role="img" aria-labelledby="fD-t fD-d" preserveAspectRatio="xMidYMid meet">
<title id="fD-t">Assumed versus measured token reduction</title>
<desc id="fD-d">Horizontal bars. Assumed illustrative values: UNU-INWEH Concise Mode 30 percent, AISF whitepaper FAQ 13 33 percent. Measured results: median 36.7 percent, mean 39.0 percent, best single run 71.8 percent. Measured central tendency meets or exceeds both assumptions.</desc>
<text class="td-lbl" x="250" y="28.0" text-anchor="end">UNU-INWEH Concise Mode (assumed)</text>
<rect class="td-assumed" x="258.8" y="15.8" width="111.0" height="16.5" rx="2"/>
<text class="td-val" x="374.5" y="28.0" text-anchor="start">30.0%</text>
<text class="td-lbl" x="250" y="54.0" text-anchor="end">AISF whitepaper FAQ 13 (assumed)</text>
<rect class="td-assumed" x="258.8" y="41.8" width="122.2" height="16.5" rx="2"/>
<text class="td-val" x="385.8" y="54.0" text-anchor="start">33.0%</text>
<text class="td-lbl" x="250" y="80.0" text-anchor="end">AISF measured median (26 runs) (measured)</text>
<rect class="td-reduce" x="258" y="67.0" width="137.6" height="18" rx="2"/>
<text class="td-val" x="399.6" y="80.0" text-anchor="start">36.7%</text>
<text class="td-lbl" x="250" y="106.0" text-anchor="end">AISF measured mean (26 runs) (measured)</text>
<rect class="td-reduce" x="258" y="93.0" width="146.2" height="18" rx="2"/>
<text class="td-val" x="408.2" y="106.0" text-anchor="start">39.0%</text>
<text class="td-lbl" x="250" y="132.0" text-anchor="end">AISF best single run (Qwen3-8B) (measured)</text>
<rect class="td-reduce" x="258" y="119.0" width="269.2" height="18" rx="2"/>
<text class="td-val" x="531.2" y="132.0" text-anchor="start">71.8%</text>
</svg>
<figcaption>Figure 2A-4. Assumed versus measured token reduction. Dashed bars are illustrative assumptions; solid bars are measured results.</figcaption>
</figure>

**Table 6. Assumed versus measured token reduction.**

| Source | Reduction | Basis |
|---|---:|---|
| UNU-INWEH "Concise Mode" [1] | 30% | Assumed (illustrative) |
| AISF whitepaper, FAQ 13 | 33% | Assumed (illustrative) |
| AISF measured median (26 runs) | 36.7% | Measured |
| AISF measured mean (26 runs) | 39.0% | Measured |
| AISF best single run (Qwen3-8B) | 71.8% | Measured |

The measured central tendency meets or exceeds both assumed values. The independence of the
UNU-INWEH estimate is the point of interest. That report, a 2026 publication of the United
Nations University Institute for Water, Environment and Health, arrives at a message-level
efficiency argument, that reducing verbosity yields material savings at platform scale,
through an entirely separate line of analysis, and selects a 30% reduction as its
illustrative case.

The Framework's session-efficiency thesis (Chapter 11) and the token-delta measurements
reported here predate that report by many months. The report is therefore not a source for
this appendix; it is independent later corroboration of a position the Framework already
held and had measured. Two distinctions follow. First, the direction of dependence: the
Framework did not adopt the report's framing, the report independently converged on the
Framework's. Second, the epistemic status of the numbers: the report's 30% is a stipulated
illustration, whereas the 36.7% median reported here is an empirical result across 26 runs.
An external body independently reasoning to the same conclusion, and to a more conservative
figure than the Framework had already demonstrated, strengthens the claim.

## 7. Limitations

**Proxy metric.** The delta is a word-count proxy over 541 IFEval prompts, not literal
tokenizer tokens and not a real-world task mix. Words approximate tokens (about 1.3 tokens
per word) but are not identical, so the percentages are directional with respect to token
count. The reduction is measured on an instruction-following benchmark, not on billed
production traffic; a deployed workload with a different task distribution would produce a
different figure.

**Rebound effect.** Lower per-use energy does not automatically lower total impact. When a
service becomes cheaper or faster, usage tends to rise, a pattern often described as the
Jevons Paradox [1]. A verbosity-reduction lever should be paired with resource budgets
(token, GPU-hour, or kilowatt-hour caps) rather than treated as an automatic net saving.
The Framework's enforcement posture, which applies the constraint at every session rather
than depending on user initiative, is consistent with that pairing.

**Grid and hardware dependence.** Absolute energy, water, and carbon depend on hardware,
batching, data-center efficiency, and grid mix. The same watt-hour carries different carbon
and water footprints by location. The scaling estimates in Section 5 are illustrative at the
global-average level and are not site-specific predictions.

## 8. Conclusions

Output-verbosity reduction is a robust, cross-architecture side effect of Framework
compliance training. Across 26 runs spanning seven model families, the median reduction is
36.7% and the mean is 39.0%, with a clear cluster in the 33% to 50% band and a maximum single
run of 71.8%. Only two runs, both explicable, increased verbosity.

Because inference dominates AI energy use and per-query energy scales with token count, this
reduction maps to a proportional reduction in per-query energy and its water and carbon
footprints, subject to the rebound caveat in Section 7. At deployment scale the implied
savings are non-trivial: independent estimates place a 30% to 33% reduction at tens of
gigawatt-hours to tens of terawatt-hours per year depending on scope.

The resource-efficiency implication is a corollary of session efficiency, established within
the Framework prior to, and independently corroborated by, the 2026 UNU-INWEH report. The
measured reduction fraction meets or exceeds the fractions those external estimates assume.

<nav>
<div class="chapter-nav">
  <a href="/appendices">Appendices</a>
  <a href="/#toc">Table of Contents</a>
</div>
</nav>

---

## References

[1] M. Aczel, S. Chamanara, M. Matin, A. Farsi, T. Marwala, and K. Madani, *Environmental Cost of AI's Energy Use: Carbon, Water and Land Footprints*, United Nations University Institute for Water, Environment and Health (UNU-INWEH), Richmond Hill, Ontario, Canada, 2026. doi:10.53328/INR26RMA002

[2] International Energy Agency, *Energy and AI*, IEA, 2025. [https://www.iea.org/reports/energy-and-ai](https://www.iea.org/reports/energy-and-ai){: target="_blank" rel="noopener noreferrer" }

[3] J. Zhou, T. Lu, S. Mishra, S. Brahma, S. Basu, Y. Luan, D. Zhou, and L. Hou, "Instruction-Following Evaluation for Large Language Models," 2023. arXiv:2311.07911

[4] AKCP, "Data Center Water Usage Effectiveness (WUE)," 2021. [https://www.akcp.com/index.php/2021/01/14/data-center-water-usage-effectiveness-wue/](https://www.akcp.com/index.php/2021/01/14/data-center-water-usage-effectiveness-wue/){: target="_blank" rel="noopener noreferrer" }

[5] World Wide Web Consortium, *Web Content Accessibility Guidelines (WCAG) 2.2*, W3C Recommendation, Oct. 2023. [https://www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/){: target="_blank" rel="noopener noreferrer" }

<nav>
<div class="toc-link"><a href="/#toc">Table of Contents</a></div>
</nav>
