# Daily arXiv - 2026-09-10

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-10T01:17:35
- Paper count: 10

## 1. AlignDiff: Exploiting Model-Intrinsic Information for Better Preference Data Selection

- Source: arxiv
- arXiv ID: 2609.05899
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.05899v1
- PDF: https://arxiv.org/pdf/2609.05899v1
- DOI: https://doi.org/10.48550/arXiv.2609.05899

### Authors

Peng Lai, He Zhu, Zhiwen Ruan, Dongdong Zhang, Yun Chen, Peng Li, Furu Wei, Yang Liu, Guanhua Chen

### Abstract

Aligning large language models with human preferences remains a challenge, primarily due to the critical role of preference data quality in effective alignment. Existing datasets are frequently plagued by inherent noise and distribution shifts, which inherently limit model performance. To bridge this gap, we propose AlignDiff, a preference data filtering framework driven by intrinsic model signals. AlignDiff first identifies samples with clear preferences using both positive and inverse signals, then prioritizes the more challenging samples based on the average negative log-likelihood gap, encouraging the model to learn richer information from them. AlignDiff is evaluated on two widely used model families (LLaMA and Qwen) and three benchmarks widely adopted in the alignment community (AlpacaEval 2.0, Arena-Hard, and MT-Bench). Across all settings, it consistently outperforms seven strong baselines. We conduct comprehensive ablation studies to validate the effectiveness of AlignDiff, and further show that difficulty-based curriculum learning improves model performance.

### 中文一句话结论
AlignDiff 利用模型内在信号（正/逆隐式奖励边际和负对数似然差距）过滤偏好数据，在多个基准上超越七种基线方法。

### English TL;DR
AlignDiff is a preference data filtering framework that uses model-intrinsic signals—combining positive and inverse implicit reward margins to select clear-preference samples and an average negative log-likelihood gap to prioritize harder, more informative pairs—consistently outperforming seven baselines across LLaMA/Qwen models on AlpacaEval 2.0, Arena-Hard, and MT-Bench.

### 中文详细总结
本文提出 AlignDiff，一种利用模型内在信号进行偏好数据过滤的框架。其流程分为两阶段：阶段一通过正/逆隐式奖励边际（Alignment Discrepancy，R_AD）筛选具有明确偏好极性的样本；阶段二基于平均负对数似然差距（ANG）对已确认极性的样本进行难度排序，优先保留更具信息量的困难样本，从而缓解 DPO 优化中的“挤压效应”。在 LLaMA 和 Qwen 基础上，AlpacaEval 2.0、Arena-Hard 和 MT-Bench 上均优于七个强基线，难度感知课程学习可进一步提升性能。

### 方法 / 贡献
- 首次融合正/逆隐式奖励边际（R_AD）检测偏好极性清晰度，利用 DPO 对称性获取互补信号。
- 提出基于平均负对数似然差距（ANG）的样本难度校准，抑制简单样本对 DPO 优化的负面影响。
- 实现完全由模型内在信号驱动的偏好数据过滤，无需外部评分模型。

### 实验或数据
- 模型：LLaMA-3-8B-SFT、Qwen2.5-7B-SFT（SFT 模型）。
- 原始数据：UltraFeedback 偏好数据集。
- 基准：AlpacaEval 2.0、Arena-Hard、MT-Bench。
- 对照：SDPO 等七个强基线模型，消融实验验证 R_AD 和 ANG 各自贡献。

### 值得关注点
- 首次揭示正/逆隐式奖励边际并非简单负相关，存在互补信息。
- 阶段分离设计（先极性过滤后难度排序）逻辑清晰，且完全免外部奖励模型。
- 在 AlpacaEval 2.0 上超越 SDPO6-7 个百分点（长度控制胜率）。

### 局限性
- 仅在两代模型家族（LLaMA、Qwen）上的单个初始 SFT 模型验证，泛化性需更多测试。
- 难度校准仅依赖一次固定排序，未探讨更动态的课程学习策略。

## 2. In-Place Instruction Following in Diffusion Language Models

- Source: arxiv
- arXiv ID: 2609.07160
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.07160v1
- PDF: https://arxiv.org/pdf/2609.07160v1
- DOI: https://doi.org/10.48550/arXiv.2609.07160

### Authors

Zheng Nie, Zherui Li, Jiaming Zhang, Kun Wang, Zhenhong Zhou, Yufei Guo

### Abstract

Diffusion Large Language Models (dLLMs) generate text via bidirectional iterative denoising, naturally supporting user-specified constraints anchored at arbitrary output positions, a paradigm known as In-place Prompting (IPP). We formalize this as the In-place Instruction Following (IIF) task and construct IIF-Bench, a hierarchical benchmark spanning literal, style, and discourse-function constraints, paired with a rubric-based local-global evaluation protocol. An inference-time attention-bias probe suggests that vanilla dLLMs often under-prioritize constraint spans during denoising. We then propose GRAFT, an IPP-oriented post-training framework combining constraint-aware SFT and preference optimization. On four representative dLLMs, GRAFT raises the average IIF score from 57.75 to 73.10 (+15.35 points), with absolute gains of 15.91 and 15.57 points on literal and discourse-function constraints, while preserving general generation ability.

### 中文一句话结论
本工作首次形式化扩散语言模型中的“原位指令跟随”（IIF）任务，构建了分层基准 IIF-Bench，并提出后训练框架 GRAFT，在四个扩散 LLM 上将平均 IIF 分数从 57.75 提升至 73.10（+15.35 分），同时保持通用生成能力基本不变。

### English TL;DR
This paper formalizes the In-place Instruction Following (IIF) task for diffusion LLMs, constructs IIF-Bench with hierarchical constraints, and proposes GRAFT, a post-training framework that significantly improves in-place constraint following while preserving general generation ability.

### 中文详细总结
扩散大语言模型（dLLM）通过双向迭代去噪生成文本，天然支持将用户约束锚定在输出序列的任意位置，即“原位提示”（IPP）。本文将这一能力形式化为“原位指令跟随”（IIF）任务，要求模型在给定固定约束跨度（anchor）的前提下，生成其前后内容，并保持局部连贯与全局一致。为此，作者构建了包含约 5K 样本的层次化基准 IIF-Bench，覆盖字面约束、风格约束和话语功能约束三个难度层级，并设计了基于评分标准的局部-全局细粒度评估协议。

通过推理时的注意力偏置探针（attention-bias probe），作者发现原始 dLLM 在去噪过程中往往对约束跨度的关注不足。基于这一观察，提出 GRAFT（Guided Refinement via Anchor-aware Focus Tuning），一种面向 IPP 的后训练框架，结合约束感知的监督微调（SFT）与偏好优化。实验表明，GRAFT 在四个代表性 dLLM 上显著提升 IIF 表现，字面约束与话语功能约束的绝对增益分别达到 15.91 和 15.57 分，且对通用生成能力影响较小。

### 方法 / 贡献
- 形式化定义 IIF 任务，并构建分层基准 IIF-Bench（约 5K 实例）。
- 设计基于评分标准的局部-全局细粒度评估协议，结合自动评测与 LLM-as-a-judge 等交叉验证。
- 提出推理时注意力偏置探针，诊断 dLLM 对原位约束关注不足的问题。
- 提出 GRAFT 后训练框架，包括约束感知 SFT 与约束感知偏好优化，以协调局部约束与全局一致性。

### 实验或数据
- IIF-Bench 包含约 5K 条高质量实例，数据来源包括 Alpaca、LFQA 和 Poetry，涵盖解释性、知识密集与创意生成场景。
- 实验在四个代表性 dLLM 上进行。
- GRAFT 将平均 IIF 分数从 57.75 提升至 73.10（+15.35 分）。
- 字面约束与话语功能约束的绝对增益分别为 15.91 和 15.57 分。
- 进一步分析表明，模型在局部约束执行、边界连贯性和全局一致性上均有稳定提升，对通用生成能力影响较小。

### 值得关注点
- IPP 范式改变了传统仅前缀提示的交互方式，支持任意位置的局部控制。
- 注意力偏置探针揭示了一个关键瓶颈：dLLM 未充分优先处理约束跨度，而非缺少语言能力。
- 基准设计显式量化了“局部约束与全局一致性”之间的张力，适合作为诊断 dLLM 注意力分配机制的工具。
- 代码和数据已公开（https://anonymous.4open.science/r/Graft-36B5）。

### 局限性
所提供的摘要和预览内容中未明确讨论局限性；若要了解 GRAFT 在更广泛场景下的失败模式、计算开销或跨语言适用性，需要查阅论文全文。

## 3. SciLitBench: Benchmark and Design Principles for LLM-Powered Systematic Literature Reviews

- Source: arxiv
- arXiv ID: 2609.05505
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.05505v1
- PDF: https://arxiv.org/pdf/2609.05505v1
- DOI: https://doi.org/10.48550/arXiv.2609.05505

### Authors

Miguel Zabaleta, Baihan Lin

### Abstract

Systematic reviews require sustained human judgment across thousands of records, yet existing evaluations of large language models (LLMs) typically examine review stages in isolation. We introduce SciLitBench, a multi-stage benchmark spanning title and abstract screening, full-text screening, and schema-guided data extraction, with 42,981 retrieved records, 1,012 full texts, and annotations for 888 included papers. Across 22 open-weight LLMs from six model families, explicit inclusion and exclusion criteria improve title and abstract screening $F_2$ by 28.8\%, while researcher-authored rationales improve full-text screening by 15\%. Data extraction reveals a different reliability regime: performance declines from 0.97 accuracy for publication year to 0.37 Jaccard overlap for computational approach, while the strongest models recover only 30\% of annotated evaluation evidence and 25\% of limitations. SciLitBench identifies a practical boundary between high-recall screening and evidence-complete extraction and provides a reproducible resource for evaluating LLM-assisted evidence synthesis.

### 中文一句话结论
SciLitBench 是一个多阶段基准测试，用于评估大型语言模型在系统文献综述中的表现，涵盖标题与摘要筛选、全文筛选及数据提取，揭示明确标准显著提升筛选效果，而提取性能在开放和模糊字段上大幅下降。

### English TL;DR
SciLitBench is a multi-stage benchmark for evaluating LLMs in systematic literature reviews across screening and data extraction, revealing that explicit criteria significantly improve screening while extraction performance degrades substantially on open-ended and ambiguous fields.

### 中文详细总结
SciLitBench 基于一项真实的系统文献综述构建，涵盖42,981条检索记录、1,012篇全文和888篇纳入论文的标注。研究评估了来自六个模型家族的22个开源大型语言模型。结果表明，在标题与摘要筛选中，显式的纳入和排除标准使F2分数提升28.8%；在全文筛选中，研究者撰写的理由说明使性能提升15%。数据提取任务表现出不同的可靠性模式：从出版年份的0.97准确率下降到计算方法的0.37 Jaccard重叠分数，最强模型仅能恢复30%的评估证据和25%的局限性标注。该基准提供了一个跨阶段的统一评估框架，揭示了高召回筛选与完整证据提取之间的实际界限。

### 方法 / 贡献
- 构建了首个覆盖系统综述三个阶段（标题/摘要筛选、全文筛选、数据提取）的统一基准
- 评估了22个开源LLM，发现显式筛选标准和理由说明能显著提升性能
- 开发了包含6个字段的架构化数据提取基准，涵盖从明确属性到开放证据的模糊性谱系
- 建立了基于校准的LLM-as-a-Judge协议来评估开放文本字段
- 发布了完整基准资源（冻结数据划分、提示模板、模型输出、评估脚本）

### 实验或数据
- 42,981条检索记录，1,012篇全文，888篇论文用于数据提取
- 标题/摘要筛选：2,000条人工标注，其余通过最高精度+完美召回配置处理
- 全文筛选：200篇人工标注，其余通过类似策略处理
- 数据提取：888篇论文，16,777个结构化数据元，覆盖6个字段
- 内部标注一致性：标题/摘要99.6%，全文99.0%，数据提取96.1%
- 开放字段使用100篇论文的校准集和29,724个标签进行LLM-as-a-Judge评估

### 值得关注点
- 跨阶段统一评估：首次在单一语料库上系统连接筛选与提取，可分析跨阶段误差传播
- 开源模型中心：选择可复现的开源权重模型，避免闭源API变化带来的比较问题
- 数据提取的模糊性谱系：从明确字段（出版年份）到开放字段（局限、评估证据）的系统分化
- 开放资源：冻结数据划分、提示模板、输出、评估脚本全部公开

### 局限性
- 仅基于一个系统综述构建，领域为文献综述自动化方法，可能不直接泛化到其他领域
- 数据提取部分人工标注可能仍存在未覆盖的边缘案例或标注偏差
- 开放字段评估依赖LLM-as-a-Judge，尽管经过校准，仍可能存在评估偏差
- 仅评估开源模型，未测试闭源商业模型（如GPT-4、Claude）
- 样本量在筛选层面相对有限（特别是全文筛选的200篇标注集）

## 4. LANTERN: Language Model Assessment on Noisy and Transformed Tasks for Understanding Error and Robustness Nuances

- Source: arxiv
- arXiv ID: 2609.07309
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.07309v1
- PDF: https://arxiv.org/pdf/2609.07309v1
- DOI: https://doi.org/10.48550/arXiv.2609.07309

### Authors

Vamsi Krishna Kodavali, Rituraj Singh

### Abstract

Robustness evaluation of large language models (LLMs) remains a critical challenge, particularly in assessing their sensitivity to perturbations in input data. In this work, we systematically evaluate LLM robustness across multiple dimensions, including word error rate, character repetition and duplication, modifications in choices, and variability in instruction following. To facilitate this evaluation, we construct a synthetic and augmented dataset encompassing a diverse set of LLM benchmarks, specifically targeting multiple-choice question (MCQ) datasets and instruction-following tasks. We conduct extensive experiments on LLMs of varying scales-small, medium, and large-as well as across base and instruction-tuned variants. Our analysis quantifies the variability in model responses under perturbed conditions and highlights discrepancies relative to baseline models. The findings provide insights into the stability of LLMs across different evaluation scenarios contributing to the development of more robust and reliable language models as well as robust evaluation methodologies.

### 中文一句话结论
本文系统评估了大型语言模型在多种输入扰动（如拼写错误、字符重复、选项修改、指令偏差）下的鲁棒性，发现模型性能存在显著变异性，并提出了构建更稳定评估方法的方向。

### English TL;DR
This paper systematically evaluates the robustness of large language models across multiple perturbation dimensions—including word error rate, character changes, answer choice modifications, and instruction-following variability—using synthetic and augmented datasets, revealing performance discrepancies and providing insights for developing more reliable models and evaluation methodologies.

### 中文详细总结
论文针对大型语言模型（LLM）在真实场景中可能遇到的输入扰动（如打字错误、字母重复/删除、选项替换、指令变化）进行了系统性鲁棒性评估。作者构建了合成与增强数据集，覆盖多选题（MCQ）和指令跟随任务，并在不同规模（小/中/大）和变体（基础模型 vs. 指令微调模型）的LLM上开展实验。通过量化扰动条件下模型响应的变异性，并与基线对比，揭示了模型在处理不同扰动时的稳定性差异。研究结果有助于理解LLM的脆弱点，并为开发更鲁棒的评估方法提供基础。

### 方法 / 贡献
1. 定义了多维度扰动评估框架：字符级（拼写错误、字母重复、字母删除）、词语级（选项置换/替换为“以上都不对”等短语）、指令跟随（改变约束条件）。  
2. 构建了合成与增强数据集，涵盖MCQ和指令跟随两类基准任务，便于系统控制扰动类型和强度。  
3. 在不同规模（小、中、大）和变体（基础、指令微调）的LLM上进行了广泛实验，量化了扰动导致的性能下降和变异性。  
4. 分析了扰动对模型稳定性的影响，为评估方法和模型改进提供了具体洞察。

### 实验或数据
- **数据集**：基于现有LLM基准（如MCQ和指令跟随任务）构建合成增强数据集，包含原始样本和九种问题扰动（三种类型×三种强度）、四种选项扰动（替换为“None of These”“All of the Above”等）、以及指令跟随扰动（修改约束条件）。  
- **模型**：涵盖小、中、大三种规模的LLM，以及基础版本和指令微调版本。  
- **实验内容**：在扰动前后的数据集上测试模型，计算准确率变化（MCQ）或指令遵循度（指令跟随），并与基线（无扰动）对比，分析变异性。

### 值得关注点
- 首次系统联合评估了字符级、选项级和指令级扰动对LLM的影响，覆盖了三个常被忽略的鲁棒性维度。  
- 合成数据集构造方法具有可扩展性，易于迁移到其他任务和模型。  
- 实验揭示了模型对特定扰动（如将正确选项替换为“None of These”）的脆弱性，为实际部署中的输入预处理提供了警示。

### 局限性
论文未明确讨论局限性，但可推断：合成扰动可能无法完全模拟真实世界的噪声分布；评估仅基于有限数量的基准任务和模型规模；未深入分析扰动下模型内部表征的变化机制。

## 5. CrisisKD: Five-Stage Knowledge Distillation for Aspect-Level Sentiment and Emotion Analysis in Crisis Discourse

- Source: arxiv
- arXiv ID: 2609.05757
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.05757v1
- PDF: https://arxiv.org/pdf/2609.05757v1
- DOI: https://doi.org/10.48550/arXiv.2609.05757

### Authors

Marko Haralović, Onat Akca, Salih Eren Yücetürk, Minsi Li, Mariët Theune

### Abstract

Identifying the target of emotional words or phrases in crisis situations, especially health-related ones, is important for understanding public concerns across cultural and linguistic contexts. We propose CrisisKD, a five-stage teacher--student knowledge distillation framework for aspect-level sentiment and emotion analysis on unannotated social media data. A teacher LLM generates aspect-level labels and reasoning traces that supervise a smaller student model across aspect extraction, syntactic parsing, opinion extraction, sentiment classification, and emotion classification. Using this framework, we construct and release a dataset containing 50,615 aspect-level labels, together with the annotation and fine-tuning scripts as open-source resources. The resulting student supports end-to-end ABSA and emotion detection at substantially lower inference cost than the teacher. On a manually annotated 500-tweet gold set, the 5-task Qwen2.5-7B student improves over the untuned model by 7.9 F1 points on aspect extraction, 17.0 points on emotion accuracy, and 6.5 points on sentiment accuracy. On the external ABEA benchmark, CrisisKD improves the same-model Qwen2.5-7B ICL baseline by 2.8 F1 points on ATE and 3.8 F1 points on joint ATE+AEC.

### 中文一句话结论
提出五阶段知识蒸馏框架CrisisKD，利用教师大模型生成伪标签与推理轨迹，训练轻量学生模型实现低成本、端到端的方面级情感与情绪分析，在学生模型上显著提升性能。

### English TL;DR
CrisisKD is a five-stage teacher-student knowledge distillation framework that uses a large language model (Qwen2.5-32B) to generate aspect-level labels and reasoning traces for unannotated crisis tweets, enabling a smaller student model (e.g., Qwen2.5-7B) to perform efficient, end-to-end aspect-based sentiment and emotion analysis with substantial performance gains over untuned baselines.

### 中文详细总结
本文提出 CrisisKD，一个面向危机情境下未标注社交媒体数据的五阶段师生知识蒸馏框架。教师模型（Qwen2.5-32B 指令调优版）依次生成方面提取、句法解析、观点提取、情感分类和情绪分类的标签与推理轨迹。学生模型（Llama-3-8B 或 Qwen2.5-7B）通过 LoRA 微调学习这些轨迹，从而在较低推理成本下支持端到端的方面级情感与情绪分析。框架构建并发布了包含 50,615 个方面级标签的数据集，以及注释和微调脚本。在人工标注的 500 条推文金标准上，微调后的 Qwen2.5-7B 学生模型在方面提取 F1 上提升 7.9 点，情绪准确率提升 17.0 点，情感准确率提升 6.5 点。在外部 ABEA 基准上，相比同模型的上下文学习基线，方面提取 F1 提升 2.8 点，联合 ATE+AEC 提升 3.8 点。

### 方法 / 贡献
方法：五阶段流水线（方面提取 → 句法解析 → 观点提取 → 情感分类 → 情绪分类），教师生成推理轨迹监督学生；使用 Qwen2.5-32B 作为教师，Llama-3-8B 和 Qwen2.5-7B 作为学生；采用 LoRA 微调与学生变体实现低资源部署。贡献：1）开源了涵盖五任务的 COVID-19 方面级情感与情绪数据集（50,615 标签）；2）提供了完整的注释、提示和微调脚本；3）训练的轻量学生模型支持端到端分析，且可在消费级硬件上运行量化版本。

### 实验或数据
使用数据集：COVIDSenti（约 90,000 推文，句子级情感）、COVID19 NLP（48,000 推文，句子级情感）用于教师伪标注和蒸馏训练；ABEA 数据集用于跨数据集评估。构建了 500 条人工标注推文作为金标准。学生模型对比未调优基线：方面提取 F1 +7.9，情绪准确率 +17.0，情感准确率 +6.5。ABEA 上对比 ICL 基线：ATE F1 +2.8，ATE+AEC 联合 F1 +3.8。实验表明辅助句法和观点任务具有正向作用。

### 值得关注点
1）首次在危机话语中联合建模方面提取、情感与14类细粒度情绪，且无需人类方面级标注；2）开源数据集和完整脚本，支持复现和扩展；3）学生模型推理成本远低于教师，适合大规模非标注数据自动标注；4）情绪分类采用专为危机话语设计的14类+无情绪标签，区分焦虑/恐惧、乐观/希望等细微差异。

### 局限性
1）框架目前仅评估于英语COVID-19推文，跨语言和跨危机领域的迁移尚未实证验证；2）依赖教师模型生成质量，教师幻觉或偏差可能传递给学生；3）手动金标准仅500条推文，规模较小；4）辅助任务（句法解析、观点提取）对性能的贡献未进行消融实验量化。

## 6. Tracing Stereotypes from Representation to Output in Multilingual LLMs

- Source: arxiv
- arXiv ID: 2609.08322
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.08322v1
- PDF: https://arxiv.org/pdf/2609.08322v1
- DOI: https://doi.org/10.48550/arXiv.2609.08322

### Authors

Ariun-Erdene Tumurchuluun, Yusser Al Ghussin, Pinzhen Chen, Josef van Genabith, Koel Dutta Chowdhury

### Abstract

Multilingual LLMs show stereotype-related behavior that varies across languages, but behavioral scores do not show where the relevant information is represented or how it affects the output. To investigate these internal mechanisms, we compare linear probing, attribution patching, sparse autoencoders (SAEs) and feature ablation in Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B. Probe performance peaks substantially earlier than attribution in all three models, with a separation of 36-53% of model depth. Retained Llama-Scope features often match the social category on which they were selected and form recurring semantic families, but their lexical alignment and ablation effects vary across SAE suites. Only 6-18% of evaluated residual-stream features have language-agnostic effects under our criterion, and none are category-agnostic. Language-agnostic features have larger mean ablation effects in Llama-Scope, but this pattern does not repeat in the other SAE suites. Decodability, output influence, and cross-lingual ablation effects therefore need to be measured separately.

### 中文一句话结论
多语言大语言模型中的刻板印象信息在网络的较早层即可被线性解码，但直到较晚层才对输出产生因果影响；且这些神经特征大多是语言依赖和类别特定的，而非语言无关或类别无关。

### English TL;DR
Multilingual LLMs' stereotypical biases are represented earlier in the network than they causally influence outputs, and most such neural features are language-dependent and category-specific rather than language-agnostic.

### 中文详细总结
本文研究多语言大语言模型（LLMs）中刻板印象的内部表征与因果影响之间的差异。作者在 Llama-3.1-8B、Qwen3-8B 和 Gemma-2-9B 三个模型上，使用线性探针、归因补丁、稀疏自编码器（SAEs）及特征消融等方法，比较刻板印象信息在哪一层最可解码以及在何处对输出有最强因果影响。结果发现，所有模型中的探针性能峰值出现在较早层（约中间层），而归因补丁的峰值出现在靠近输出层，二者间隔达模型深度的 36–53%。通过 SAEs 识别的稀疏特征大多与所选的社交类别匹配，形成语义家族，但词汇对齐和消融效果在不同 SAE 套件间存在差异。跨语言评估显示，仅 6–18% 的残差流特征在本文标准下具有语言无关效果，且没有特征具有类别无关效果。语言无关特征在 Llama-Scope 套件中平均消融效应更大，但在其他 SAE 套件中未重复这一模式。因此，可解码性、输出影响和跨语言消融效果需要分别测量。

### 方法 / 贡献
- **方法**：比较线性探针（线性解码）、归因补丁（估计因果影响）、稀疏自编码器（SAEs）进行稀疏特征发现，以及特征消融（测量对下游基准的影响）。涉及三个多语言模型，四种语言和六个社交类别。
- **主要贡献**：揭示了刻板印象信息的可解码性与因果影响在模型深度上存在显著分离（36–53%）；稀疏特征大多与该类别相关且语义可解释，但跨语言稳定性有限；证明可解码性、输出影响和特征消融效果是三个需要独立评估的维度。

### 实验或数据
- **模型**：Llama-3.1-8B、Qwen3-8B、Gemma-2-9B（均为约 8-9B 参数的多语言 LLM）。
- **语言**：英语、西班牙语、荷兰语、土耳其语。
- **社交类别**：在 MBBQ 数据集上选择六个类别（如性别、种族等）。
- **数据与基准**：使用 MBBQ 进行特征发现，使用 SHADES 进行下游偏差评估（无重叠以避免循环）。
- **SAE 套件**：Llama-Scope、Llama-Multi、Gemma-Scope、Qwen-Multi 等。
- 实验比较了跨层探针性能、归因补丁强度、SAE 特征的可解释性和消融效果。

### 值得关注点
- 探针与归因峰值之间存在 36–53% 模型深度的分离，表明刻板印象信息在早期就已存在，但直到深层才对输出产生实质影响。
- 大多数稀疏特征与社交类别有强关联（123/139 用于 Llama-Scope），形成语义家族（如与性别相关的职业词）。
- 仅 6–18% 的特征具有语言无关效果，且没有特征具有类别无关效果，显示刻板印象表征高度语言和类别特定。
- 语言无关特征虽在 Llama-Scope 中平均消融效应更大，但这一模式在其他 SAE 套件中不成立，暗示跨 SAE 套件的一致性有限。

### 局限性
- 仅研究三个多语言模型（8-9B 参数），不覆盖其他规模或架构的模型。
- 仅涉及四种语言和六个社交类别，可能无法反映更广泛的语言或社会刻板印象。
- 稀疏自编码器的特征可解释性和消融效果在不同 SAE 套件间差异较大，结论需要谨慎推广。
- 未发现类别无关特征，可能受限于所选类别和语言范围。
- 行为分数虽表明偏差存在，但本文未覆盖所有可能的偏差表现形式。

## 7. ToolLoop: Closed-Loop Tool-Use Data Synthesis via Decomposed Generation and Dynamic Self-Feedback

- Source: arxiv
- arXiv ID: 2609.09072
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.09072v1
- PDF: https://arxiv.org/pdf/2609.09072v1
- DOI: https://doi.org/10.48550/arXiv.2609.09072

### Authors

Min Zeng, Yuzhou Liu, Zhenyu Cao, Hanxiu Chen, Heng Li, Caiquan Liu, Yafei Wen, Xiaoxin Chen

### Abstract

High-quality tool-use data is critical for training language models to interact effectively with external tools. However, existing synthetic approaches typically follow a generate-then-filter paradigm with static post-hoc verification, often yielding inefficient data with imbalanced feature distributions. We propose ToolLoop, a closed-loop framework that decomposes synthesis into three progressive stages: (1) sampling function name combinations as ground truth; (2) backward derivation of user queries; and (3) forward derivation of tool calls. At each stage, dynamic self-feedback iteratively guides the model toward high-quality generation, realizing a transition from generate-then-filter to generate-verify-refine. On the Berkeley Function Calling Leaderboard (BFCL), a 4B parameter model trained with our 11K synthetic examples achieves 86.40% accuracy in non-reasoning mode, while an Isolate variant that removes BFCL-overlapping candidate functions still reaches 86.07\%. Cross-benchmark evaluation on ACEBench further demonstrates strong generalization, with 72.1% overall accuracy using only 18.3% of baseline training data.

### 中文一句话结论
ToolLoop 提出了一种闭环数据合成框架，通过分解生成与动态自反馈机制，仅用 11K 样本训练 4B 模型即可在函数调用基准上达到 86.40% 准确率，显著优于传统“生成后过滤”范式。

### English TL;DR
ToolLoop introduces a closed-loop framework that decomposes tool-use data synthesis into three progressive stages with dynamic self-feedback, enabling a shift from generate-then-filter to generate-verify-refine, and achieves state-of-the-art function-calling accuracy (86.40% on BFCL and 72.1% on ACEBench) using only 11K synthetic examples.

### 中文详细总结
高质量工具使用数据对训练语言模型与外部工具交互至关重要。现有合成方法通常采用“生成后过滤”（generate-then-filter）范式，辅以静态事后验证，导致数据效率低且特征分布不均衡。本文提出 **ToolLoop**，一个闭环合成框架，将合成过程分解为三个渐进阶段：
1. **采样函数名组合作为真实标签（ground truth）**：通过语义聚类和LLM引导从候选函数集中选取目标调用序列。
2. **反向推导用户查询**：根据真实标签和候选函数，逆向生成自然语言用户请求，确保意图与工具调用严格对齐。
3. **前向推导工具调用**：基于用户查询和候选函数，生成带具体参数的工具调用序列。
每个阶段均集成动态自反馈机制：结合LLM验证器、确定性规则和AST解析，对输出进行语义、格式和语法检查；若失败则通过包含原始提示、失败输出和具体反馈的细化提示指导模型修正，最多重试三次。该机制实现了从“生成后过滤”到“生成-验证-细化”（generate-verify-refine）的转变，保留了更多多样性样本。
在 Berkeley Function Calling Leaderboard (BFCL) 上，使用 11K 合成样本训练的 Qwen3-4B 模型在非推理模式下达到 86.40% 准确率；其隔离变体（剔除与 BFCL 重叠的函数）仍达 86.07%。在跨基准 ACEBench 上，仅用基线 18.3% 的训练数据即取得 72.1% 整体准确率，展现了强泛化能力。

### 方法 / 贡献
- **闭环合成框架**：将工具使用数据生成分解为三个渐进阶段（真实标签采样 → 反向推导用户查询 → 前向推导工具调用），每个阶段都有明确的中间表示。
- **动态自反馈机制**：在每个阶段集成LLM验证、规则检查和AST解析，针对具体错误生成可操作的细化提示，实现迭代修正而非简单丢弃。
- **基于语义聚类的候选函数构建**：利用向量嵌入和 K-means 聚类对工具函数分组，结合LLM引导采样，保障合成数据的多样性和场景覆盖。
- **高效数据利用**：仅用 11K 合成样本（约基线的 18.3%）即可使 4B 模型在多个基准上达到领先性能，验证了生成质量的高效性。
- **泄漏控制实验**：通过 Isolate 变体剔除与评估基准重叠的函数，证明模型学到的是真实工具调用能力而非记忆。

### 实验或数据
- **模型**：基于 Qwen3-4B-Instruct-2507 训练，对比包括开源（Qwen3、LLaMA 4、Gemma3 等）和商业（GPT-5.2、Gemini-3-Pro 等）模型。
- **数据来源**：从 ToolBench 和 BFCL 中随机采样 5,281 个可执行 API，通过 Qwen3-Embedding-8B 编码后 K-means 聚类为 26 组，每组约 200 个函数。
- **训练数据**：ToolLoop 生成 11K 合成样本（Isolate 变体为 10K），覆盖 Simple、Multiple、Parallel、Parallel Multiple 四种场景。
- **评估基准**：
  - BFCL-v4：包含 2,501 个测试实例，按非推理模式评估，结果：ToolLoop-4B 86.40%（整体），Isolate 86.07%。
  - ACEBench：覆盖 Atom、Single Turn、Similar API、Profile 维度，ToolLoop-4B 整体准确率 72.1%，仅用基线 18.3% 数据。
- **超参数**：训练 2 个 epoch，最大序列长度 16k，使用 4×NVIDIA L40s 集群。

### 值得关注点
- 从“生成后过滤”转向“生成-验证-细化”，在数据效率和多样性上实现显著突破。
- 动态自反馈并非简单的二元过滤器，而是提供具体错误反馈引导模型修正，保留困难样本。
- 在泄漏控制设定下性能仍保持高水平（86.07%），证明模型学到了通用工具调用能力而非记忆训练数据中的评估用例。
- 仅用 11K 数据即超越许多使用更多数据训练的模型，表明合成数据质量比数量更为关键。
- 跨基准（BFCL 和 ACEBench）均表现出色，泛化能力强。

### 局限性
- 当前框架仅聚焦于单轮工具调用场景，未涉及多轮对话或复杂任务链中的工具交互。
- 自反馈依赖于 LLM 作为验证器，可能继承其自身偏差，且评估质量受限于验证模型的容量。
- 最大重试次数设为三次，部分样本可能因重试耗尽而被丢弃，虽然实验表明大多数可纠错在两次内解决，但仍有潜在的不必要丢弃。
- 合成数据覆盖的函数库规模有限（5,281 个 API），且仅从两个来源采样，可能在更广泛真实场景下泛化性受限。
- 仅在 Qwen3-4B 一个基础模型上进行了训练验证，未测试其他规模或架构的模型以确认框架的通用性。

## 8. Climate-ModernBERT: Revisiting Corpus Composition for Domain-Adaptive Continued Pretraining

- Source: arxiv
- arXiv ID: 2609.07798
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.07798v1
- PDF: https://arxiv.org/pdf/2609.07798v1
- DOI: https://doi.org/10.48550/arXiv.2609.07798

### Authors

Yongan Yu, Shantam Raj, Jingwei Ni, Ario Saeid Vaghefi, Dominik Stammbach, Markus Leippold

### Abstract

Natural Language Processing (NLP) in the climate domain requires models to process heterogeneous text sources, including scientific literature, policy disclosures, and synthetic reports. However, how to effectively combine diverse domain corpora during continued pretraining (CPT) remains underexplored. We introduce Climate-ModernBERT, a family of climate-adapted encoder models obtained through continued pretraining of ModernBERT-Base on three climate corpora: academic climate text, climate-filtered web data, and synthetic climate documents. We systematically compare joint continued pretraining on corpus mixtures with parameter-space merging of independently specialized checkpoints. Across nine climate NLP benchmarks, our best model achieves 76.3 average F_1, improving significantly over a vanilla ModernBERT baseline by 2.8 points. Within the climate NLP setting, the results show that academic climate corpora provide the strongest adaptation signal among the evaluated sources, while parameter-space merging improves over joint multi-source training and better preserves complementary information from heterogeneous climate corpora. We release all Climate-ModernBERT variants and training checkpoints to support future research in climate NLP and domain-adaptive pretraining.

### 中文一句话结论
实验表明，在气候领域NLP中，基于独立领域检查点的参数空间合并优于混合语料的联合继续预训练，其中学术气候文本提供了最强的领域适应信号。

### English TL;DR
Climate-ModernBERT shows that parameter-space merging of independently specialized checkpoints outperforms joint continued pretraining on heterogeneous climate corpora, with academic climate text providing the strongest domain adaptation signal.

### 中文详细总结
该论文提出了Climate-ModernBERT，一组基于ModernBERT-Base在三个气候语料（学术气候文本、气候过滤网络数据、合成气候文档）上继续预训练的气候适应编码器模型。研究系统比较了混合语料联合继续预训练与独立检查点参数空间合并两种策略。在9个气候NLP基准测试中，最佳模型平均F1达到76.3，比原始ModernBERT提升2.8。结果表明学术语料提供最强适应信号，参数空间合并优于联合多源训练，能更好保留异构语料中的互补信息。

### 方法 / 贡献
1. 构建了包含学术文本（1.28B tokens）、网络数据（5B tokens）、合成文本（0.14B tokens）的6.42B token气候预训练语料
2. 对比两种多源语料整合策略：联合继续预训练（混合语料同时训练）与参数空间合并（独立训练各语料领域检查点后合并）
3. 采用ModernBERT的两阶段训练流程：上下文扩展（CX）+ 学习率衰减（LRD）专门化
4. 发布所有模型变体和训练检查点

### 实验或数据
- 在9个气候NLP基准任务上评估21个模型变体，共超过810次微调运行
- 最佳模型（参数合并）平均F1达76.3，对比基线ModernBERT的73.5提升2.8
- 学术语料在全部来源中提供最强领域适应信号
- 参数空间合并策略在所有任务上一致优于联合多源训练

### 值得关注点
- 学术文本（文献、政策、IPCC报告）被证明是最有效的领域适应信号源，远超网络数据
- 参数空间合并（而非混合训练）能更好地保留不同语料源的互补信息
- 合成数据虽然规模最小（0.14B），但对特定任务仍有补充价值
- 模型全部开源，支持气候NLP和领域适应预训练的未来研究

### 局限性
- 实验仅在气候领域进行，结论在其他专业领域的泛化性有待验证
- 参数合并仅测试了基础的权重平均方法，未探索更先进的合并技术
- 合成数据生成依赖封闭源大规模语言模型，可能引入系统偏差
- 未评估模型在多语言环境下的表现

## 9. Generating Adversarial Texts for Machine Translation via GRPO

- Source: arxiv
- arXiv ID: 2609.06048
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.06048v1
- PDF: https://arxiv.org/pdf/2609.06048v1
- DOI: https://doi.org/10.48550/arXiv.2609.06048

### Authors

Florian Zogaj, Jakob Hütteneder, Giovanni De Muri, Federico Villa, Aryan Sood, Vilém Zouhar

### Abstract

As machine translation (MT) systems continue to improve, standard benchmarks become less informative for exposing remaining weaknesses. Traditional methods for creating challenging test sets rely on expensive manual creation or curation, while automated approaches struggle to produce sets with the necessary translation difficulty and linguistic diversity. We propose a scalable reinforcement-learning-based approach for rewriting existing source texts into instances that are more difficult to translate for MT systems. We fine-tune a large language model with Group Relative Policy Optimization (GRPO), using reward signals based on translation difficulty together with constraints for semantic similarity, grammaticality, and approximate length preservation. On WMT25, our approach substantially reduces average COMET translation quality from 0.63 to 0.48, while preserving grammaticality and readability, whereas the base model remains at 0.64. Evaluations on the unseen WMT19-WMT24 benchmarks confirm that this behavior generalizes beyond the training data, and human evaluation further shows that the rewrites substantially lower translation quality while incurring a moderate drop in naturalness and only a small change in grammaticality. We release our code to support reproducibility.

### 中文一句话结论
本研究通过GRPO强化学习微调大语言模型，将源文本改写为对机器翻译系统更具挑战性的对抗样本，在保持语法和语义的同时显著降低翻译质量（WMT25上COMET从0.63降至0.48）。

### English TL;DR
This paper proposes using Group Relative Policy Optimization (GRPO) to fine-tune a large language model for rewriting source texts into adversarial examples that reduce machine translation quality while preserving grammaticality, semantic similarity, and length. On WMT25, COMET scores drop from 0.63 to 0.48, with generalization to unseen benchmarks and human evaluation confirming effectiveness.

### 中文详细总结
针对机器翻译系统在标准基准上表现日益提升、暴露弱点困难的问题，该工作提出一种可扩展的自动化方法：利用GRPO微调Llama-3.1-8B-Instruct模型，将现有英文源文本改写成更难翻译的变体。奖励函数结合翻译难度提升（通过Sentinel或COMET+MT评估）、语义相似度、语法可接受性（CoLA和LanguageTool）及长度约束。在WMT25训练集上，改写后COMET评分从0.63降至0.48，而基模型保持0.64；在未见过的WMT19–WMT24基准上行为一致。人工评估显示改写显著降低翻译质量，自然度适度下降，语法变化较小。代码已开源。

### 方法 / 贡献
- **方法**：使用GRPO对LLM进行微调，通过组内相对奖励比较优化策略，生成多个候选改写并根据自定义奖励函数选择；奖励包含翻译难度下降（基于QE模型）、长度保持、语义相似度（余弦相似度>0.7）、语法正确性（CoLA和LanguageTool）五项。
- **贡献**：首次将GRPO应用于机器翻译对抗样本生成，可扩展地自动化构建高难度测试集；通过多约束奖励设计平衡难度与语言质量；在多个WMT基准和人工评估中验证有效性和泛化能力。

### 实验或数据
- **训练数据**：WMT25英文源句（用于强化学习微调）；翻译方向为英→意（NLLB和Helsinki模型）。
- **评估数据**：WMT25（训练集同源）、WMT19–WMT24（未见基准）、以及英→德翻译的人工评估。
- **指标**：COMET（翻译质量）、Sentinel（源端难度）、Self-chrF（多样性）、人工评分（自然度、语法性）。
- **结果**：COMET从0.63降至0.48，基模型无变化；未见过基准上保持趋势；人工评估确认有效。

### 值得关注点
- 采用GRPO而非传统监督学习，避免依赖昂贵的人工标注难度数据。
- 奖励设计巧妙结合多种约束，防止模型退化（如过度改变语义或语法）。
- 在未见的目标语言（英语→德语）上展现迁移能力，说明策略非语言特定。
- 代码开放，支持复现。

### 局限性
- 训练仅针对英→意方向，需验证在其他语言对上的泛化性。
- 模型可能过度优化特定高奖励模式（如实验中出现的n-gram重复坍塌），导致多样性下降，需进一步正则化。
- 奖励权重和阈值基于初步实验选择，未进行系统超参数调优，可能存在更优配置。
- 依赖多个外部模型（MT、QE、语法检查），计算开销较大；且对抗样本的现实有效性需进一步研究。

## 10. Transformers as In-Context Samplers: From Closed-Form Diffusion to Estimation-Free Sampling

- Source: arxiv
- arXiv ID: 2609.08981
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.08981v1
- PDF: https://arxiv.org/pdf/2609.08981v1
- DOI: https://doi.org/10.48550/arXiv.2609.08981

### Authors

Arman Adibi, Alireza Jafari, Mohammad Ghavamzadeh, Hadi Daneshmand

### Abstract

A growing body of work establishes that large language models are not mere statistical memorizers, but are capable of in-context learning: performing inference at test time using only examples provided in the prompt, without any parameter updates. Prior theoretical work has shown that this capability extends to supervised learning tasks such as linear regression. We prove that in-context learning extends further to \emph{data generation}: frozen transformers can simulate iterative generative samplers from in-context samples. We first show that transformers can realize closed-form and smoothed closed-form diffusion samplers. The construction identifies a concrete generative role for softmax attention: it computes responsibility weights and weighted empirical averages, while feedforward layers implement Euler updates.
  To empirically relate these constructions to pretrained language models, we study \emph{semantic-topic sampling}: prompts consisting of words drawn from a common semantic category, such as animals, foods, or cities. Across transformer layers, the normalized hidden states exhibit a two-stage geometry: they move toward a uniform spherical reference in intermediate layers and then return to structured, topic-dependent representations near the output. We further measure an interacting-particle energy on these hidden-state clouds and observe the same U-shape pattern. We then prove that transformers can approximate an energy-based sampler, constructing the same U-shape energy across the layers.

### 中文一句话结论
本文证明，冻结参数的Transformer可以通过上下文样本模拟闭式扩散和能量基采样过程，从而具备无条件数据生成能力，并在预训练大语言模型（如GPT-2、Llama-3.3）上观察到对应的U形层间几何结构。

### English TL;DR
This paper proves that frozen transformers can simulate closed-form diffusion and energy-based samplers using only in-context examples for unconditional data generation, and empirically reveals a U-shaped layer-wise geometry in pretrained LLMs.

### 中文详细总结
现有研究主要关注Transformer在条件生成任务中的上下文学习能力（如线性回归），本文首次将这一能力扩展到**无条件数据生成**。作者从理论和实验两个层面展开：
- **理论构造**：证明Transformer可通过注意力头计算责任权重(w_i)和加权经验平均(k_t(z))，并通过前馈层执行欧拉更新，从而实现闭式扩散采样和能量基采样（Estimation-Free Sampling, EFS）。这一构造揭示了softmax注意力在生成中的具体作用。
- **实验验证**：在多个预训练LLM（GPT-2、Llama-3.3-70B、OPT-66B等）上设计“语义主题采样”任务（提示词来自同一类别，如动物、食物）。通过追踪各层隐藏状态，发现：
  - 归一化嵌入分布先向均匀球面分布靠近（中间层），再恢复为与主题相关的非均匀结构（输出层）。
  - 测量隐状态云的相互作用能量，观察到相同的**U形模式**：能量先下降后上升。

### 方法 / 贡献
- **闭式扩散采样器的Transformer实现**：构造显式算法，证明单层Transformer可计算闭式扩散模型的得分函数和更新方向；前馈层对应欧拉积分步骤。
- **能量基采样器的Transformer近似**：证明Transformer可近似EFS，该过程包含两步：将经验分布推向均匀分布，再反转过程；这一两步机制与观察到的U形能量模式一致。
- **预训练模型的可解释分析**：在8种不同规模的LLM上验证了U形层间几何结构，表明该机制可能是大模型内部的通用生成策略。

### 实验或数据
- **主要实验**：在GPT-2、Llama-3.3-70B-Instruct、OpenLM-13B、Cerebras-GPT-13B、Qwen2.5、Falcon-40B、OPT-66B、BLOOM-7B1上进行“语义主题采样”实验。提示词由同一主题（动物、食物、城市等）的单词构成。
- **测量指标**：跟踪每层归一化隐藏状态在球面上的分布（通过均匀性度量）以及基于粒子相互作用的能量函数。
- **训练数据**：为验证上下文采样能力，训练了一个小型Transformer生成人脸形状数据（包含边界、眼睛，但不含微笑嘴巴），测试时通过提供嘴形上下文样本，模型成功生成未见过的嘴形曲线。

### 值得关注点
- **软注意力机制的新角色**：将注意力从传统的序列对齐工具重新解释为**生成过程中的密度估计和加权平均计算器**，为理解Transformer生成机制提供了新视角。
- **U形模式作为生成信号**：中间层的均匀分布和能量低谷可能对应“去遗忘”阶段，即模型暂时释放训练先验以聚焦于上下文信息，再回到主题特定结构——类似于扩散模型的加噪-去噪过程。
- **无需额外训练**：完全利用预训练模型的冻结参数，表明生成能力是in-context learning的固有延伸，而非特定训练目标的产物。

### 局限性
- **理论构造局限于离散时间欧拉方案**，未分析连续时间极限或更复杂的扩散SDE求解器。
- **预训练模型的实验仅针对语义主题采样**，未考察其他类型的数据生成任务（如图像或数值数据）。
- **能量基采样器的近似证明**依赖于构造性方法，可能不是预训练模型实际采用的机制；实验结果仅为相关性，非因果验证。
- **未定量分析上下文样本数量、主题相似度等因素对生成质量的影响**。

## Processing Notes

- Duplicate papers skipped: 0