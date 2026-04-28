"""Single runner: builds all slides and saves the PPTX."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from create_pptx_part1 import *

prs = new_prs()

# ═══ SLIDE 1: Title ═══
make_title_slide(prs, "Gemma 4: Efficient Intelligence at Scale",
    "How Google DeepMind Achieves Near-Frontier Performance\nWithout Trillion-Parameter Models\n\nApril 2026  •  Presented by Apurbo Turjo")

# ═══ SLIDE 2: The Problem ═══
s = content_slide(prs, "The Efficiency Challenge in Modern LLMs")
bullet_block(s, Inches(0.8), Inches(1.4), Inches(5.5), Inches(3.0),
    ["GPT-4 class models: estimated 1.8T parameters",
     "Llama 3 405B: requires 8× A100 80GB GPUs",
     "Cost of inference dominates deployment budgets",
     "Edge/mobile deployment essentially impossible at scale"],
    "The Problem", 20, 16)
bullet_block(s, Inches(0.8), Inches(4.5), Inches(5.5), Inches(2.5),
    ["Can we achieve frontier-level reasoning at 10-100× lower cost?",
     "Can a 2B-parameter model match a 7B model's intelligence?",
     "Can a model run on a smartphone with 1.5 GB RAM?"],
    "Gemma 4's Central Questions", 20, 16)
r = add_rect(s, Inches(7.0), Inches(1.8), Inches(5.5), Inches(4.2), WHITE)
add_text_box(s, Inches(7.3), Inches(2.0), Inches(4.9), Inches(0.5),
    "Gemma 4's Answer", 20, NAVY, True, PP_ALIGN.CENTER)
add_text_box(s, Inches(7.3), Inches(2.7), Inches(4.9), Inches(0.9),
    "31B-level intelligence", 28, ACCENT, True, PP_ALIGN.CENTER)
add_text_box(s, Inches(7.3), Inches(3.5), Inches(4.9), Inches(0.5),
    "running in ~1.5 GB RAM on a smartphone", 16, GRAY, False, PP_ALIGN.CENTER)
add_text_box(s, Inches(7.3), Inches(4.2), Inches(4.9), Inches(0.5),
    "5 interlocking compression techniques", 16, DARK_TEXT, False, PP_ALIGN.CENTER)
add_text_box(s, Inches(7.3), Inches(4.8), Inches(4.9), Inches(0.5),
    "20-40× effective compression", 24, GREEN, True, PP_ALIGN.CENTER)

# ═══ SLIDE 3: Model Family ═══
s = content_slide(prs, "Gemma 4 Model Family at a Glance")
add_table(s, 5, 6, Inches(0.8), Inches(1.5), Inches(11.7), Inches(2.8),
    [["Model", "Type", "Total Params", "Active Params", "Context", "Target HW"],
     ["E2B", "Dense + PLE", "5.1B", "2.3B", "128K", "Phone / IoT"],
     ["E4B", "Dense + PLE", "8B", "4.5B", "128K", "Phone / Edge"],
     ["26B A4B", "MoE (128 exp.)", "25.2B", "3.8B", "256K", "Laptop"],
     ["31B", "Dense", "30.7B", "30.7B", "256K", "Server"]],
    [Inches(1.5), Inches(2.2), Inches(1.8), Inches(1.8), Inches(1.4), Inches(3.0)])
bullet_block(s, Inches(0.8), Inches(4.8), Inches(11.5), Inches(2.2),
    ['All models: Apache 2.0, natively multimodal (text + image + audio/video)',
     '"Effective" naming: E2B has 5.1B stored params but only 2.3B active per token',
     'MoE 26B: 128 experts, only 9 active → inference cost ≈ 4B dense model',
     'Distilled from Gemini 3 family using Generalized Knowledge Distillation (GKD)'],
    "Key Design Principles", 18, 15)

# ═══ SLIDE 4: Five Techniques Overview ═══
s = content_slide(prs, "Five Interlocking Efficiency Techniques")
techs = [("1. Per-Layer Embeddings", "Layer-specific token representations", "Representation quality ↑"),
    ("2. Hybrid Attention", "5 local : 1 global attention ratio", "Attention memory 83% ↓"),
    ("3. Shared KV Cache", "Last N layers reuse KV states", "Inference memory 44% ↓"),
    ("4. Mixture-of-Experts", "128 experts, 8 active per token", "Compute 93% ↓ in FFN"),
    ("5. Knowledge Distillation", "GKD from Gemini teacher", "Training signal quality ↑")]
for i, (nm, desc, eff) in enumerate(techs):
    y = Inches(1.5) + Inches(i * 1.1)
    add_rect(s, Inches(0.8), y, Inches(3.5), Inches(0.9), WHITE)
    add_text_box(s, Inches(1.0), y+Inches(0.05), Inches(3.2), Inches(0.4), nm, 16, NAVY, True)
    add_text_box(s, Inches(1.0), y+Inches(0.45), Inches(3.2), Inches(0.4), desc, 13, GRAY)
    add_rect(s, Inches(4.5), y, Inches(0.06), Inches(0.9), ACCENT)
    add_text_box(s, Inches(4.8), y+Inches(0.2), Inches(3.0), Inches(0.5), eff, 15, GREEN, True)
add_rect(s, Inches(8.5), Inches(1.5), Inches(4.3), Inches(5.3), NAVY)
add_text_box(s, Inches(8.8), Inches(1.7), Inches(3.7), Inches(0.5), "KEY INSIGHT", 16, ACCENT, True, PP_ALIGN.CENTER)
add_text_box(s, Inches(8.8), Inches(2.3), Inches(3.7), Inches(4.2),
    "Each technique targets a\nDIFFERENT bottleneck:\n\n• PLE → representation\n• Hybrid attn → attention cost\n• MoE → FFN compute\n• Shared KV → inference mem\n• KD → training quality\n\nThey compose without\ninterference — the innovation\nis combining all five cleanly.", 14, WHITE)

# ═══ SLIDE 5: PLE ═══
s = content_slide(prs, "Technique 1: Per-Layer Embeddings (PLE)")
bullet_block(s, Inches(0.8), Inches(1.4), Inches(5.5), Inches(2.5),
    ["Standard transformer: single embedding shared across all layers",
     "PLE: each decoder layer has its own small embedding lookup table",
     "Adds a layer-specific residual signal to the hidden state",
     "Used in E2B and E4B models to boost representation depth"], "How It Works", 18, 15)
bullet_block(s, Inches(0.8), Inches(3.9), Inches(5.5), Inches(3.0),
    ["Extra per layer: vocab_size × small_dim ≈ 16M params/layer",
     "36 layers → ~576M extra params (only ~10-15% overhead)",
     "Lookup tables — only one row accessed per token per layer",
     "Compute cost: negligible (table lookup, not matmul)",
     "Result: 2.3B effective params perform like 7B dense model"], "Why It's Efficient", 18, 15)
add_rect(s, Inches(7.0), Inches(1.5), Inches(5.5), Inches(5.0), WHITE)
add_text_box(s, Inches(7.3), Inches(1.7), Inches(4.9), Inches(0.5), "Parameter Cost Comparison", 17, NAVY, True, PP_ALIGN.CENTER)
add_text_box(s, Inches(7.3), Inches(2.3), Inches(4.9), Inches(1.5),
    "Option A: Double model width\n  d_model: 2048 → 4096\n  Cost: 4× more params everywhere\n  Extra params: BILLIONS", 13, RED_ACC, False, PP_ALIGN.LEFT, "Consolas")
add_text_box(s, Inches(7.3), Inches(4.0), Inches(4.9), Inches(1.5),
    "Option B: Add PLE (Gemma 4)\n  Extra: ~576M params total\n  But adds TARGETED per-layer info\n  Result: depth of 7B at 2B cost!", 13, GREEN, False, PP_ALIGN.LEFT, "Consolas")
add_text_box(s, Inches(7.3), Inches(5.5), Inches(4.9), Inches(0.7),
    "PLE: ~15% more params → ~50% benefit\nof doubling the model", 14, ACCENT, True, PP_ALIGN.CENTER)

# ═══ SLIDE 6: Hybrid Attention ═══
s = content_slide(prs, "Technique 2: Hybrid Attention — Local + Global")
bullet_block(s, Inches(0.8), Inches(1.4), Inches(5.5), Inches(2.0),
    ["Full attention: O(n²) — at 128K tokens = 16B scores per layer",
     "Sliding window (local): each token sees only 1024 neighbors",
     "Gemma 4 interleaves: 5 local layers : 1 global layer",
     "Final layer always global for full-context awareness"], "The Design", 18, 15)
bullet_block(s, Inches(0.8), Inches(3.6), Inches(5.5), Inches(3.2),
    ["128K tokens, 36 layers — All-Global: 36 units of KV memory",
     "Hybrid 5:1: 6 global + 30×(1024/128K) ≈ 6.24 units → 83% less",
     "p-RoPE on global layers: only 25% of dims rotated for position",
     "Remaining 75% encode pure semantics — stable at 256K context",
     "Local layers spread info; global layers synchronize everything"], "Memory Savings + p-RoPE", 18, 15)
add_rect(s, Inches(7.0), Inches(1.5), Inches(5.5), Inches(5.2), WHITE)
add_text_box(s, Inches(7.3), Inches(1.7), Inches(4.9), Inches(0.4), "Attention Layer Pattern", 17, NAVY, True, PP_ALIGN.CENTER)
add_text_box(s, Inches(7.3), Inches(2.2), Inches(4.9), Inches(3.5),
    "L1:  ████ LOCAL  (1024 tokens)\nL2:  ████ LOCAL\nL3:  ████ LOCAL\nL4:  ████ LOCAL\nL5:  ████ LOCAL\nL6:  ████████████████ GLOBAL (full)\nL7:  ████ LOCAL\n...\nL36: ████████████████ GLOBAL ← always",
    13, DARK_TEXT, False, PP_ALIGN.LEFT, "Consolas")
add_text_box(s, Inches(7.3), Inches(5.6), Inches(4.9), Inches(0.8),
    "5 whispers + 1 announcement\n= surprisingly effective", 13, ACCENT, True, PP_ALIGN.CENTER)

# ═══ SLIDE 7: Shared KV Cache ═══
s = content_slide(prs, "Technique 3: Shared KV Cache")
bullet_block(s, Inches(0.8), Inches(1.4), Inches(5.8), Inches(2.5),
    ["KV cache: stores Key/Value from all tokens during generation",
     "Standard: each of 36 layers computes and stores its own KV",
     "Observation: deep layers produce nearly IDENTICAL KV representations",
     "Gemma 4: last N layers REUSE an earlier layer's KV cache"], "How It Works", 18, 15)
bullet_block(s, Inches(0.8), Inches(4.0), Inches(5.8), Inches(3.0),
    ["Layers 1-20: unique KV (diverse info per layer)",
     "Layers 21-36: share Layer 20's KV (nearly identical anyway)",
     "20 unique + 16 shared = 44% fewer KV cache entries",
     "Per attention type: local→last local, global→last global",
     "Quality impact: negligible (deep layers refine, don't reinvent)"], "The Savings", 18, 15)
add_rect(s, Inches(7.2), Inches(1.5), Inches(5.3), Inches(4.5), WHITE)
add_text_box(s, Inches(7.5), Inches(1.7), Inches(4.7), Inches(0.4), "KV Diversity Across Layers", 16, NAVY, True, PP_ALIGN.CENTER)
add_text_box(s, Inches(7.5), Inches(2.3), Inches(4.7), Inches(3.5),
    "L1→L2:   ████████████  HIGH\nL5→L6:   ██████████    HIGH\nL10→L11: ████████      MEDIUM\nL20→L21: ██████        LOW\nL30→L31: ███           VERY LOW\nL35→L36: █             ~ZERO",
    14, DARK_TEXT, False, PP_ALIGN.LEFT, "Consolas")

# ═══ SLIDE 8: MoE ═══
s = content_slide(prs, "Technique 4: Mixture-of-Experts (MoE)")
bullet_block(s, Inches(0.8), Inches(1.4), Inches(5.5), Inches(2.0),
    ["Replace single giant FFN with 128 smaller expert FFNs",
     "Learned router selects top-8 experts + 1 shared per token",
     "Each expert: ~30M params (specialized sub-network)",
     "Different tokens activate different experts by content"], "Architecture (26B A4B)", 18, 15)
add_table(s, 6, 2, Inches(0.8), Inches(3.6), Inches(5.2), Inches(3.0),
    [["Metric", "Value"], ["Total parameters", "25.2B"], ["Active per token", "~3.8B"],
     ["Experts / MoE layer", "128"], ["Active experts / token", "8+1 shared = 9"],
     ["Inference speed", "≈ 4B dense model"]],
    [Inches(2.5), Inches(2.7)])
add_rect(s, Inches(7.0), Inches(1.5), Inches(5.5), Inches(5.3), WHITE)
add_text_box(s, Inches(7.3), Inches(1.7), Inches(4.9), Inches(0.4), "Why Near-Zero Perf. Drop?", 16, NAVY, True, PP_ALIGN.CENTER)
add_text_box(s, Inches(7.3), Inches(2.3), Inches(4.9), Inches(4.2),
    '"The" → grammar expert\n"quantum" → science expert\n"=" → math/code expert\n"melancholy" → literary expert\n\nDense: ALL 31B params process\nALL tokens → most irrelevant\n\nMoE: each token routed to\nRELEVANT experts only\n→ same knowledge, 7% compute\n\n128 specialist doctors vs.\n1 who memorized everything.', 14, DARK_TEXT, False, PP_ALIGN.LEFT)

# ═══ SLIDE 9: KD ═══
s = content_slide(prs, "Technique 5: Knowledge Distillation (GKD)")
bullet_block(s, Inches(0.8), Inches(1.4), Inches(5.5), Inches(2.0),
    ["Student learns from teacher's FULL probability distribution",
     "Soft labels carry 'dark knowledge' — relationships between outputs",
     "Temperature τ ≈ 2-10 smooths distribution for richer signal",
     "L = α·KL(teacher ∥ student) + (1-α)·CE(ground truth)"], "Standard Distillation", 18, 15)
bullet_block(s, Inches(0.8), Inches(3.5), Inches(5.5), Inches(3.5),
    ["Standard KD: student sees pre-generated data → train-inference mismatch",
     "GKD: student generates its OWN outputs ('on-policy')",
     "Teacher scores student's actual generation → corrects mistakes",
     "Student learns from its OWN errors → better generalization",
     "Teacher: Gemini 3 (frozen) → Student: Gemma 4 E2B/E4B"], "Generalized KD (Gemma 4)", 18, 15)
add_rect(s, Inches(7.0), Inches(1.5), Inches(5.5), Inches(5.3), WHITE)
add_text_box(s, Inches(7.3), Inches(1.7), Inches(4.9), Inches(0.4), "Dark Knowledge Example", 16, NAVY, True, PP_ALIGN.CENTER)
add_text_box(s, Inches(7.3), Inches(2.3), Inches(4.9), Inches(4.2),
    '"Capital of France is ___"\n\nHard label: Paris → 1 fact\n\nSoft label (teacher):\n  Paris:  0.52 ████████████\n  Lyon:   0.18 ████\n  France: 0.12 ███\n  Berlin: 0.08 ██\n  London: 0.06 █\n\nStudent learns:\n✓ Paris (answer)\n✓ Lyon is French (world knowl.)\n✓ Berlin/London = capitals\n✓ "the" makes no sense (grammar)',
    12, DARK_TEXT, False, PP_ALIGN.LEFT, "Consolas")

# ═══ SLIDE 10: Compression Stack ═══
s = content_slide(prs, "The Compression Multiplier Stack")
add_table(s, 7, 4, Inches(0.8), Inches(1.5), Inches(11.7), Inches(3.8),
    [["Technique", "Compression", "Quality Retained", "Target"],
     ["KD (Gemini → Student)", "~8× (31B → 4B)", "~90%", "Training signal"],
     ["PLE", '"Negative" (adds quality)', "~95% of 7B perf.", "Representation"],
     ["Hybrid Attention (5:1)", "6× less attn. memory", "~99%", "Attention cost"],
     ["MoE (128→8 experts)", "~6.5× compute ↓", "~97%", "FFN compute"],
     ["Shared KV Cache", "~2× memory savings", "~99%", "Inference memory"],
     ["4-bit Quantization", "4× smaller weights", "~98%", "Weight storage"]],
    [Inches(3.2), Inches(3.2), Inches(2.5), Inches(2.8)])
add_rect(s, Inches(3.2), Inches(5.7), Inches(6.9), Inches(1.2), NAVY)
add_text_box(s, Inches(3.5), Inches(5.8), Inches(6.3), Inches(0.5),
    "Combined: 20-40× effective compression", 22, WHITE, True, PP_ALIGN.CENTER)
add_text_box(s, Inches(3.5), Inches(6.3), Inches(6.3), Inches(0.4),
    "31B quality → 1.5-3 GB RAM → runs on a smartphone", 16, ACCENT, False, PP_ALIGN.CENTER)

# ═══ SLIDE 11: Benchmarks ═══
s = content_slide(prs, "Official Benchmark Results (Instruction-Tuned)")
add_table(s, 6, 5, Inches(0.8), Inches(1.5), Inches(11.7), Inches(3.2),
    [["Benchmark", "31B Dense", "26B MoE", "E4B", "E2B"],
     ["MMLU Pro", "85.2%", "82.6%", "69.4%", "60.0%"],
     ["AIME 2026 (Math)", "89.2%", "88.3%", "42.5%", "37.5%"],
     ["LiveCodeBench v6", "80.0%", "77.1%", "52.0%", "44.0%"],
     ["GPQA Diamond", "84.3%", "82.3%", "58.6%", "43.4%"],
     ["τ²-bench (Agentic)", "86.4%", "85.5%", "57.5%", "29.4%"]],
    [Inches(3.2), Inches(2.1), Inches(2.1), Inches(2.1), Inches(2.1)])
bullet_block(s, Inches(0.8), Inches(5.0), Inches(11.5), Inches(2.2),
    ["26B MoE matches 31B Dense within 1-3% on ALL benchmarks — using only 12% compute",
     "E4B achieves GPQA 58.6% at just 4.5B active params",
     "arXiv:2604.07035: E4B (few-shot CoT) beats 26B MoE on weighted accuracy-efficiency (0.675 vs 0.663, 14.9 vs 48.1 GB VRAM)",
     "Sparse (MoE) ≠ always best tradeoff — depends on architecture × prompt × task"], "Key Observations", 18, 14)

# ═══ SLIDE 12: Comparison Table ═══
s = content_slide(prs, "Gemma 4 vs. Other Efficient Model Families")
add_table(s, 8, 6, Inches(0.5), Inches(1.4), Inches(12.3), Inches(4.3),
    [["Technique", "Gemma 4", "LLaMA 3", "Phi-3/4", "Mistral", "DeepSeek-V2"],
     ["PLE", "✓", "✗", "✗", "✗", "✗"],
     ["Hybrid Attention", "✓ (5:1)", "✗ (GQA)", "✗ (full)", "✓ (sliding)", "✗"],
     ["Shared KV Cache", "✓", "✗", "✗", "✗", "✗"],
     ["MoE", "✓ (128 exp)", "✗ (dense)", "✓ (MoE)", "✓ (8 exp)", "✓ (160 exp)"],
     ["Distillation", "✓ (GKD)", "✗", "✓", "✗", "✗"],
     ["p-RoPE", "✓", "✗", "✗", "✗", "✗"],
     ["Quant-Friendly", "✓ designed", "✓ works", "✓ works", "✓ works", "✓ works"]],
    [Inches(2.0), Inches(2.0), Inches(2.0), Inches(2.0), Inches(2.0), Inches(2.3)])
add_text_box(s, Inches(0.8), Inches(6.0), Inches(11.5), Inches(0.8),
    "Gemma 4 stacks ALL techniques in one coherent architecture. Each is known individually; the innovation is composing them without interference.",
    15, NAVY, True)

# ═══ SLIDE 13: Quantization ═══
s = content_slide(prs, "Quantization-Friendly by Design")
add_table(s, 6, 2, Inches(0.8), Inches(1.5), Inches(5.5), Inches(3.2),
    [["Design Choice", "Why It Helps"],
     ["RMSNorm", "Stable at low precision"],
     ["SwiGLU activation", "Smooth gradients, robust to rounding"],
     ["Standard FFN", "Well-understood quant recipes"],
     ["Clean architecture", "llama.cpp, vLLM, MLX, LiteRT"],
     ["MoE expert-specific", "Frequent: 4-bit, rare: 2-bit"]],
    [Inches(2.7), Inches(2.8)])
add_rect(s, Inches(7.0), Inches(1.5), Inches(5.5), Inches(5.3), WHITE)
add_text_box(s, Inches(7.3), Inches(1.7), Inches(4.9), Inches(0.4), "Memory Footprint", 16, NAVY, True, PP_ALIGN.CENTER)
add_text_box(s, Inches(7.3), Inches(2.3), Inches(4.9), Inches(4.2),
    "GPT-4 class:   ~1000+ GB\n  (datacenter required)\n\nLlama 3 70B:   ~140 GB FP16\n  (8× A100 GPUs)\n\nGemma 4 31B:   ~16 GB (4-bit)\n  (single GPU)\n\nGemma 4 E4B:   ~3 GB (4-bit)\n  (smartphone) ✓\n\nGemma 4 E2B:   ~1.5 GB (4-bit)\n  (IoT / Raspberry Pi) ✓",
    14, DARK_TEXT, False, PP_ALIGN.LEFT, "Consolas")

# ═══ SLIDE 14: Takeaways ═══
s = content_slide(prs, "Key Takeaways")
tks = [("Architecture-First Compression",
    "Compression designed INTO the architecture — PLE, hybrid attention, MoE are structural, not post-hoc."),
    ("Complementary Technique Stack",
    "Each targets a different bottleneck. They compose multiplicatively: 20-40× compression, ~90-95% quality."),
    ("The 'Effective Parameters' Paradigm",
    "What matters is not param count but utilization. 2.3B 'effective' params match 7B dense models."),
    ("Hardware-Aware Design",
    "Designed WITH target hardware in mind. Quantization compatibility is a first-class constraint.")]
for i, (t, d) in enumerate(tks):
    y = Inches(1.4) + Inches(i * 1.4)
    add_rect(s, Inches(0.8), y, Inches(0.08), Inches(1.15), ACCENT)
    add_text_box(s, Inches(1.1), y, Inches(11.3), Inches(0.45), f"{i+1}. {t}", 18, NAVY, True)
    add_text_box(s, Inches(1.1), y+Inches(0.45), Inches(11.3), Inches(0.65), d, 14, DARK_TEXT)

# ═══ SLIDE 15: References ═══
s = content_slide(prs, "References & Further Reading")
bullet_block(s, Inches(0.8), Inches(1.4), Inches(5.8), Inches(5.5),
    ["Gemma 4 Model Card — ai.google.dev/gemma (April 2026)",
     "arXiv:2604.07035 — Accuracy-Efficiency Tradeoffs (2026)",
     "Vaswani et al. (2017) — Attention Is All You Need",
     "Hinton et al. (2015) — Distilling the Knowledge in a NN",
     "Shazeer et al. (2017) — Sparsely-Gated MoE Layer",
     "Su et al. (2021) — RoFormer: Rotary Position Embedding",
     "Agarwal et al. (2024) — GKD"], "Primary Sources", 17, 13)
bullet_block(s, Inches(7.0), Inches(1.4), Inches(5.8), Inches(5.5),
    ["Fedus et al. (2022) — Switch Transformers",
     "Frantar & Alistarh (2023) — SparseGPT",
     "Frantar et al. (2023) — GPTQ",
     "Lin et al. (2024) — AWQ",
     "Dao (2023) — FlashAttention-2",
     "Kwon et al. (2023) — vLLM / PagedAttention",
     "HuggingFace — google/gemma-4-* model weights"], "Related Work", 17, 13)

# ═══ SAVE ═══
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Gemma_4_Efficient_Intelligence.pptx")
prs.save(OUT)
print(f"✅ Saved: {OUT}")
print(f"   Slides: {len(prs.slides)}")
