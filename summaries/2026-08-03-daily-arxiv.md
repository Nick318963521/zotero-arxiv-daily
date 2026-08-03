# Daily arXiv - 2026-08-03

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-03T23:27:00
- Paper count: 10

## 1. Benchmarks Are Not Monolithic: Sample-Level Auditing and Orchestration for LLM Evaluation

- Source: arxiv
- arXiv ID: 2607.28801
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2607.28801v1
- PDF: https://arxiv.org/pdf/2607.28801v1
- DOI: https://doi.org/10.48550/arXiv.2607.28801

### Authors

Philipp D. Siedler, Jordan Sassoon

### Abstract

Benchmark datasets are central to evaluating Large Language Models (LLMs), yet they are typically conceived as monolithic tasks, obscuring substantial variation in the demands of individual samples. We introduce a dataset-centric meta-evaluation framework that audits benchmark datasets at the sample level along five latent dimensions: 1. Cognitive and Knowledge Demands, 2. Language and Content Quality, 3. Task Properties, 4. Context, and 5. Ethics, Safety, and Fairness. Applying this framework, we annotate five influential benchmarks -- MMLU, ARC, WinoGrande, HellaSwag, and TruthfulQA -- revealing pronounced internal heterogeneity that is not captured by aggregate accuracy scores. We show how these annotations enable criterion-driven orchestration of composite benchmark subsets across datasets, supporting targeted evaluation of model capabilities such as Reasoning Depth or Ethical Sensitivity. This approach reframes benchmark evaluation as dataset introspection, providing a principled methodology for analyzing and re-composing existing benchmarks to better reflect diverse evaluation needs.

### 中文一句话结论
本文提出一个样本级元评估框架，通过五个潜在维度审计基准数据集，揭示其内部异质性，并利用注释实现跨数据集的复合基准子集编排，以支持更精细的LLM评估。

### English TL;DR
This paper introduces a sample-level meta-evaluation framework that audits benchmark datasets across five latent dimensions, revealing internal heterogeneity and enabling the orchestration of composite subsets for targeted LLM evaluation, moving beyond aggregate accuracy scores.

### 中文详细总结
该研究认为基准数据集并非单一任务，而是多维度潜在对象。作者提出了一个以数据集为中心的元评估框架，在样本级别对基准数据集进行审计，涵盖五大维度：认知与知识需求、语言与内容质量、任务属性、上下文、以及伦理、安全与公平性。应用该框架，他们对MMLU、ARC、WinoGrande、HellaSwag和TruthfulQA五个有影响力的基准进行注释，揭示了这些数据集中显著的内部异质性——这是传统整体准确率分数无法捕捉的。进一步，这些注释可用于跨数据集进行标准驱动的复合基准子集编排，支持对模型特定能力（如推理深度或伦理敏感性）进行针对性评估。

### 方法 / 贡献
1.  **提出概念与框架**：首次明确论证基准数据集是潜在的**多维度对象**，并引入一个包含5个维度、多个方面和指标的**元评估框架**（Catalogue of Criteria），在样本级别暴露隐藏的认知、语言、上下文、任务和伦理维度。
2.  **大规模审计与数据集**：对**五个有影响力基准**进行大规模审计，生成了一个公开可用的注释资源，揭示了基准内部及跨基准的异质性。
3.  **应用与演示**：展示了如何将潜在维度**操作化**，通过**编排**跨数据集的复合评估子集，从而实现对LLM性能进行超越整体准确率的细粒度、可解释对比。

### 实验或数据
-   **数据**：对五个基准数据集（MMLU, ARC, WinoGrande, HellaSwag, TruthfulQA）的所有样本进行注释。各数据集样本量从817（TruthfulQA）到15.9k（MMLU）不等。
-   **注释框架**：0-3级或分类标签，覆盖Reasoning Depth, Bias & Stereotyping等多个指标（详见表1）。
-   **实验**：论文并未明确提出标准“实验”（如对比不同模型在相同任务上的表现），而是侧重于**演示**如何使用注释进行子集编排。未提及在特定模型上运行推理实验。如果论文原文有后续实验，请提供更多内容；此处基于摘要和引言，未发现设计好的对比实验。

### 值得关注点
1.  **数据为中心的视角**：不同于关注模型本身（如HELM）或测试行为的框架（如CheckList），本文纯粹从**数据集内部结构**出发，提供了一个诊断和重组基准的方法，对评估方法论有重要贡献。
2.  **潜在维度系统化**：将原本隐性的样本属性（如“推理深度”、“伦理敏感性”）转化为可操作的、结构化的元数据，使复杂的评估需求变得可控。
3.  **跨数据集重组**：通过编排复合子集，能够直接针对特定能力（如“Reasoning Depth”或“Ethical Sensitivity”）进行测试，这比单纯依赖任务名（如“QA”）更具针对性。

### 局限性
-   **注释的主观性与可行性**：论文未讨论注释者间一致性或注释过程的可靠性。5个维度的许多指标（如“Bias & Stereotyping”、“Language Difficulty”）依赖人工判断，可能引入主观偏差，且大规模扩展成本较高。
-   **应用范围限制**：框架目前仅应用于5个特定基准，其普适性（如对开放式生成任务或非英语基准）尚需验证。
-   **未涉及模型动态**：论文定位为纯评估方法论，未探讨这些潜在维度的注释如何随模型能力变化或受数据污染影响，也未探讨注释与模型实际表现之间的因果或预测关系。

## 2. TextCloak: Thwarting Unauthorized LLM Exploitation via RL-Driven Unlearnable Text

- Source: arxiv
- arXiv ID: 2607.28862
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.28862v1
- PDF: https://arxiv.org/pdf/2607.28862v1
- DOI: https://doi.org/10.48550/arXiv.2607.28862

### Authors

Chengshuai Zhao, Pingchuan Ma, Dawei Li, Bohan Jiang, Zhiyuan Yu, Zhen Tan, Huan Liu

### Abstract

The rapid development of Large Language Models (LLMs) has led to significant advances across a wide range of language tasks, while simultaneously raising growing concerns about unauthorized data exploitation and privacy leakage. Unlearnable examples (UEs) offer a promising defense by introducing carefully designed perturbations into data such that models trained on them exhibit degraded utility. However, existing methods for text protection are primarily designed for classification tasks (e.g., sentiment analysis) in discriminative language models and often rely on injecting class-specific linguistic cues, which limits their effectiveness in the open-ended generation settings of LLMs. In this work, we propose TextCloak, an RL-driven framework for protecting textual data against unauthorized LLM exploitation. TextCloak employs a generative policy that transforms batches of clean text into unlearnable examples while preserving semantic fidelity and linguistic naturalness. To optimize the policy, we introduce GRPO-UE, which rewards generated unlearnable text based on the downstream degradation they induce in fine-tuned surrogate LLMs and updates the generator parameters via group-relative policy optimization. This bi-level optimization enables the generator to discover generalizable protective patterns beyond class-specific cues. Comprehensive experiments on six publicly available datasets and nine state-of-the-art LLMs demonstrate that TextCloak consistently impairs unauthorized fine-tuning while maintaining text utility for legitimate use. Further analyses establish its transferability and robustness across model architectures, training configurations, and adaptive attacks, highlighting its broad applicability as a practical defense against unauthorized LLM exploitation.

### 中文一句话结论
TextCloak 提出了一种基于强化学习的框架，通过生成“不可学习文本”来有效防御大语言模型（LLM）对受保护数据的未经授权微调。

### English TL;DR
TextCloak introduces an RL-driven framework that generates unlearnable text examples to protect against unauthorized LLM fine-tuning, using group-relative policy optimization to degrade model performance while preserving semantic fidelity.

### 中文详细总结
大语言模型的快速发展带来了未经授权的数据利用和隐私泄露风险。现有文本保护方法主要针对分类任务，通过注入类别特定的语言线索来干扰模型训练，但难以适用于 LLM 的开放式生成场景。为此，本文提出 TextCloak，一个基于强化学习的框架，通过生成式策略将批量文本转换为“不可学习样本”，同时保持语义保真度和语言自然性。该框架引入 GRPO-UE 优化方法，以微调后替代 LLM 的下游性能下降作为奖励信号，通过组相对策略优化更新生成器参数。实验在六个公开数据集和九个先进 LLM 上验证了其有效性、可迁移性和鲁棒性。

### 方法 / 贡献
- 将文本保护形式化为带约束的双层优化问题。
- 提出基于强化学习的生成框架 TextCloak，能生成语义保留的不可学习文本。
- 设计 GRPO-UE 优化机制，通过下游性能下降度量保护效果并直接指导策略更新。
- 在多个 LLM 和数据集上全面验证了方法的有效性、可迁移性和鲁棒性。

### 实验或数据
在六个公开数据集和九个最先进的 LLM 上进行了全面实验，证明 TextCloak 能持续削弱未经授权的微调效果，同时保持文本的合法使用效用。进一步分析展示了其在不同模型架构、训练配置和自适应攻击下的可迁移性和鲁棒性。

### 值得关注点
- 首个将不可学习样本扩展至 LLM 开放生成场景的工作。
- 强化学习驱动的双层优化无需类别特定标签，可发现通用保护模式。
- 基于组相对策略优化，避免学习价值模型，实现高效奖励计算。
- 保持语义和语言自然性，对合法用户影响小。

### 局限性
根据提供的摘要，未明确讨论局限性。可能需要注意：对替代模型的依赖以及训练生成策略的计算成本较高；未探索对更复杂攻击（如对抗训练）的防御效果。

## 3. CAER: Conflict-Aware Evidence Routing with Dual Prefix Experts for Multimodal Large Language Models

- Source: arxiv
- arXiv ID: 2607.28991
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.28991v1
- PDF: https://arxiv.org/pdf/2607.28991v1
- DOI: https://doi.org/10.48550/arXiv.2607.28991

### Authors

Zixuan Liu, Juntao Cai, Xiaoxu Cai, Haishuai Wang, Jiajun Bu

### Abstract

Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in multimodal understanding and generation. However, when textual inputs conflict with visual evidence, they still suffer from hallucinations and produce responses inconsistent with visual content. Existing approaches mainly rely on decoding strategies, additional training, verification methods, or prompting techniques, but often lack fine-grained conflict localization and conflict-aware generation. In this work, we propose CAER, a backbone-agnostic framework for visual-language conflict detection and conflict-aware generation. CAER introduces a span-grounded evidence router that transforms claim representations into soft textual queries and retrieves corresponding evidence from frozen visual tokens, enabling fine-grained conflict estimation. Furthermore, we design a dual-prefix expert routing mechanism that learns separate experts for visually supported and contradicted inputs, enabling conflict-aware generation through explicit expert selection. Experiments on the public MMMC benchmark and our newly curated AgriConflict dataset demonstrate that CAER effectively detects visual-language conflicts and improves the reliability of open-source MLLMs without updating their backbone parameters.

### 中文一句话结论
本文提出CAER框架，通过细粒度冲突定位和双前缀专家路由，在不更新主干参数的情况下有效提升多模态大模型在图文冲突场景下的生成可靠性。

### English TL;DR
CAER introduces a backbone-agnostic framework with a span-grounded evidence router and dual-prefix expert routing to detect and resolve fine-grained conflicts between text and visual evidence, improving MLLM reliability without updating backbone parameters.

### 中文详细总结
多模态大模型在文本与视觉证据冲突时仍会产生幻觉。现有方法缺乏细粒度冲突定位和冲突感知生成能力。本文提出CAER，包含两个阶段：第一阶段，基于跨模态注意力实现跨度级文本与视觉证据的对应，进行细粒度冲突估计；第二阶段，学习支持专家和修正专家，根据冲突状态选择对应前缀指导生成。在MMMC基准和新构建的AgriConflict数据集上，CAER在无需更新主干参数的情况下有效提升冲突检测和生成可靠性。

### 方法 / 贡献
- **方法**：采用两阶段轻量框架。阶段A训练跨度引导的证据路由器，通过文本到视觉的跨模态注意力将文本表征转化为软查询并检索冻结视觉标记中的证据；阶段B学习双前缀专家路由，分别为支持输入和冲突输入学习独立前缀，推理时基于冲突概率阈值选择专家，冻结主干参数。
- **贡献**：1) 提出跨度引导的证据路由实现细粒度冲突定位；2) 设计双前缀专家路由实现冲突感知生成；3) 构建农业场景冲突数据集AgriConflict；4) 实验证明CAER在多种MLLM架构上有效。

### 实验或数据
- 使用MMMC（4000样本测试集）和新构建的AgriConflict数据集。
- 评估六个开源MLLM（如InternVL3-8B, Qwen3-VL-8B等），采用零样本设置。
- 关键结果：在MMMC上，CAER改善了冲突检测和响应一致性。例如，强模型（如Qwen3.5-9B）原有正确前提修正率约62%，CAER进一步提升了该指标（具体数值未在摘要中呈现，但实验表明显著提升）。

### 值得关注点
- 细粒度冲突定位：通过跨度级文本-视觉对应，而非全局相似度。
- 双前缀专家设计：分离支持与冲突情境的生成策略，无需更新主干。
- 主干无关性：可适配多种开源MLLM而不修改其参数。
- 新数据集：AgriConflict填补农业场景图文冲突评估空白。

### 局限性
本文未明确讨论方法的局限性。可能需注意：实验仅基于开源模型，商业模型未验证；阈值τ需预设且依赖验证集；农业数据集规模有限，通用性待扩展。

## 4. Scaling Properties of Text Conditioning in Visual Generation

- Source: arxiv
- arXiv ID: 2607.29679
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.29679v1
- PDF: https://arxiv.org/pdf/2607.29679v1
- DOI: https://doi.org/10.48550/arXiv.2607.29679

### Authors

Zilong Chen, Chaorui Deng, Kunchang Li, Hongyi Yuan, Haoqi Fan

### Abstract

We study empirical scaling properties for text conditioning in visual generation. Such properties have rarely been measured because diffusion loss does not scale with the number of tokens in natural-language prompts. Surprisingly, we find that the converged diffusion loss scales with the amount of structured language in the prompt. To quantify structured language, we adapt two complementary measures: a white-box likelihood metric (GPG) and a black-box attribute metric (ED). Across controlled training runs, the converged diffusion loss decreases approximately linearly with GPG and follows a power law with ED. Guided by these scaling properties, we improve \emph{diffusability} by constructing structured prompts with semantic and geometric annotations derived from images, and improve \emph{promptability} by training a prompter through supervised fine-tuning, cold-start, and verifier-gated on-policy distillation. The resulting system outperforms all evaluated open-weight models on nearly every compositional, reasoning, and world-knowledge benchmark, while matching or surpassing the strongest closed-weight models on most evaluations.

### 中文一句话结论
本文发现，视觉生成中扩散模型的收敛损失与提示中的**结构化信息量**（而非文本长度）成比例，据此提出结构化提示和提示器训练方法，在多项基准上超越所有开源模型，追平或超越最强闭源模型。

### English TL;DR
We discover that converged diffusion loss scales with the amount of structured language in prompts (measured by GPG and ED), not token count. Using this insight, we improve diffusability by constructing structured prompts and promptability by training a prompter, achieving state-of-the-art results on compositional and reasoning benchmarks, outperforming open-weight models and matching/beating closed-weight models.

### 中文详细总结
本文系统研究了文本条件在视觉生成中的缩放性质。作者发现，扩散模型的收敛损失并不随自然语言提示的token数量变化，而是与提示中**结构化语言的信息量**呈明确的缩放关系。为量化这种信息量，他们提出两种互补指标：白盒的**Grounded Perplexity Gain (GPG)** 和黑盒的**Effective Detailness (ED)**。在控制变量实验中，收敛损失与GPG近似线性下降，与ED呈幂律关系。

基于这一发现，作者从两方面提升生成质量：1）**提高“可扩散性”（diffusability）**：用包含语义和几何标注的结构化提示（structured prompts, SP）训练扩散模型，比同等长度的自然语言提示携带更多图像可验证信息；2）**提高“可提示性”（promptability）**：通过监督微调、冷启动蒸馏和验证器门控的在策略自蒸馏（OPSD）训练一个提示器（prompter），将用户简短请求转化为信息密集的结构化提示。最终系统在几乎所有组合性、推理和世界知识基准上超越所有参评的开源模型，并在多数指标上匹配或超越最强闭源模型。

### 方法 / 贡献
- **缩放性质的发现**：通过GPG和ED量化提示信息量，发现收敛损失与结构化信息量（而非长度）存在线性/幂律关系。
- **提升可扩散性**：设计结构化提示格式（JSON，包含场景、元素属性、几何、关系等字段），并结合VLM与领域专家（人体姿态、深度、分割）自动标注，训练扩散模型。
- **提升可提示性**：采用SFT→冷启动→验证器门控RFT（OPSD）的流水线训练提示器，并在推理时通过agentic refine–render–judge循环进一步优化。
- **端到端系统**：将上述两部分结合，在多个困难基准上取得领先性能。

### 实验或数据
- 在固定骨干网络、数据、计算量的条件下，对自然语言和结构化提示的不同长度/细节级别进行系统训练扫描，测量收敛损失与GPG/ED的关系。
- 在组合性、推理和世界知识基准上评估最终系统，对比开源模型（Qwen-Image, HunyuanImage 3.0, BAGEL, FLUX.1 Dev, Emu3等）和闭源模型。结果显示系统在所有开源模型上几乎全部领先，在多数指标上匹配或超越最强闭源模型。
- 具体指标包括DINOv3/SigLIP2余弦相似度、LPIPS距离、GSB净偏好等。

### 值得关注点
- 首次系统揭示文本条件中信息量（而非长度）与扩散损失的缩放关系，为提示工程和训练策略提供新视角。
- 结构化提示设计将图像信息显式编码为可编辑字段，兼具可解释性和可控性。
- 提示器训练流水线结合了冷启动、在线蒸馏和验证器门控，在不依赖图像推理时仍能生成高质量结构化提示。
- 推理时agentic refinement允许针对具体字段迭代修正，提升生成可靠性。

### 局限性
- 缩放性质是在固定训练配置（骨干网络、数据、计算量）下建立的，其泛化到其他架构、数据分布或更大规模的情况尚未验证。
- 结构化提示的生成依赖VLM和领域专家模型，增加了标注和推理阶段的系统复杂度。
- 提示器训练需要大量标注数据，且验证器门控阶段依赖可靠的质量评估器，可能引入额外偏差。
- 当前方法主要针对英文和结构化场景，对非英文或非结构化自由创作场景的适应性有待探索。

## 5. Small Is Enough: Per-User Style Rewriting of AI-Edited Text via LoRA Adapters

- Source: arxiv
- arXiv ID: 2607.29238
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.29238v1
- PDF: https://arxiv.org/pdf/2607.29238v1
- DOI: https://doi.org/10.48550/arXiv.2607.29238

### Authors

Antorweep Chakravorty

### Abstract

InMyStyle is a privacy first, single user system that adapts small language models to rewrite AI-edited text towards an individual user's writing style without an instruction prompt at inference. Given a user's documents, it uses multiple local helper LLMs to construct paired training examples and fine tunes LoRA adapters on base models ranging from 0.5B to 7B parameters. Length aware generation budgets and automatic chunking support inputs of different lengths. On 219 evaluation pairs from a scientific-paper corpus, the automatic composite score plateaus at 0.69 [scale 0-1] across all model sizes under both greedy and sampled decoding. This observed plateau suggests that small models are sufficient for the measured rewriting task, with model size determining trade-offs rather than a stable quality ranking. As a secondary evaluation, 400 ratings from five LLM judges give InMyStyle outputs a mean perceived AI-ness score over 20% lower than their helper-AI generated inputs, while mean perceived AI-ness scores decrease with model size within InMyStyle.

### 中文一句话结论
InMyStyle 证明，使用 LoRA 适配器的小语言模型（0.5B–7B）能够在不依赖指令提示的情况下，将 AI 编辑文本重写为个人写作风格，且自动评分在所有模型大小间达到 0.69 的平台，表明小模型足以胜任该任务。

### English TL;DR
InMyStyle shows that small language models (0.5B–7B parameters) fine-tuned with LoRA adapters can rewrite AI-edited text into a user's personal style without an instruction prompt, achieving a plateau in automatic composite score (0.69/1) across all model sizes, indicating smaller models are sufficient.

### 中文详细总结
InMyStyle 是一个隐私优先、单用户系统，通过本地辅助 LLM 将用户文档转换为 AI 编辑版本，并配对原始文本构建训练数据，使用 LoRA 适配器在 Qwen2.5 模型（0.5B 至 7B 参数）上微调。推理时无需任何风格指令或检索示例。在 219 个科学论文语料对的评估中，自动复合得分（0–1 标度）在所有模型大小和两种解码策略下均稳定在 0.69，形成平台，表明模型大小并不决定自动质量排名，而是影响计算与感知 AI 性之间的权衡。次要评估中，五个 LLM 评委对 400 个样本的评分显示，InMyStyle 输出的感知 AI 性比辅助 AI 输入降低超过 20%，且感知 AI 性得分随模型增大而降低（7B 最佳）。系统采用长度感知生成预算、自动分块和响应仅损失训练，确保不泄露目标文本。

### 方法 / 贡献
- **方法**：利用多个本地辅助 LLM（Qwen2.5-3B、Llama-3.2-3B、Phi-3-mini）为每个用户段落生成多家庭 AI 影子变体，并添加可选 AI 暗示和噪声扰动，构建配对训练数据。按段落 ID 分组划分训练/评估集，避免目标文本泄漏。冻结基础模型，仅训练 LoRA 适配器，使用响应仅交叉熵损失（仅对用户目标 token 计算）。推理时直接输入段落，无指令，采用长度感知 token 预算（1.5×输入词数+32）和自动分块。
- **贡献**：(1) 本地构建多家庭 AI 影子到用户原始文本的配对训练管道，支持段落级隔离和长度感知重写；(2) 控制模型大小和解码策略的对比研究；(3) 使用 LLM 作为评委分析感知 AI 性。

### 实验或数据
- **数据集**：约 36 篇科学论文（2012–2025 年）的 487 个散文段落，经 PDF 提取和两阶段过滤。三个辅助 LLM 各生成一个 AI 影子，共 1461 个配对。按 85%:15% 分组划分为训练集（414 个段落，1242 对）和评估集（73 个段落，219 对）。排除输入+目标长度超过 8192 字符的配对。
- **实验**：在 Qwen2.5 指令微调版（0.5B、1.5B、3B、7B）上训练 LoRA 适配器，相同配置（rank=8，scale=16，epoch=3，有效 batch size=16，学习率 2e-4，余弦调度，权重衰减 0.01，4-bit NF4 QLoRA）。评估使用贪婪解码和采样解码，自动复合得分（含作者身份、内容相似性、AI 暗示减少等五项指标）和 LLM 评委感知 AI 性评分（5 个 LLM，每个 400 次评分）。

### 值得关注点
- 自动评分在所有模型大小（0.5B–7B）下均达到 0.69 的平台，说明小模型在该任务上已足够，性能不随模型增大而提升。
- 感知 AI 性评分显示 InMyStyle 输出比辅助 AI 输入降低 20% 以上，且模型越大（7B）感知 AI 性越低，为降低 AI 痕迹提供可行性。
- 系统完全隐私本地化，不需外部处理或风格指令，适配器可单独存储，支持多用户。
- 长度感知生成预算和自动分块适应不同长度输入，提升实用性。

### 局限性
- 论文未明确讨论局限性。从结果看，自动评分平台表明模型大小对自动指标影响有限，但感知 AI 性评分随模型增大而改善，存在计算成本与 AI 感知度之间的权衡。评估仅基于单个用户的科学论文语料，泛化性（如其他文体、领域）未验证。此外，辅助 LLM 和 LLM 评委的模型选择可能影响结果，但未进行跨族系比较。

## 6. Imbalanced Data Clustering via Targeted Data Augmentation Using GMM and LLM

- Source: arxiv
- arXiv ID: 2607.28635
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.28635v1
- PDF: https://arxiv.org/pdf/2607.28635v1
- DOI: https://doi.org/10.48550/arXiv.2607.28635

### Authors

Noor Khalal, Abdallah Alaa-Eddine Djamai, Imed Keraghel, Mohamed Nadif

### Abstract

In Natural Language Processing (NLP), dealing with underrepresented topics is challenging, especially in unsupervised tasks where clustering might not adequately capture minority topics. To tackle this challenge, our paper presents a novel unsupervised data augmentation method that integrates Gaussian Mixture Models (GMMs) and Large Language Models (LLMs). Due to their flexibility and robustness, GMMs can detect clusters corresponding to underrepresented areas in the data, while LLMs create synthetic documents to enrich these clusters and improve their representation. Experiments on various imbalanced text datasets demonstrate that our approach preserves clustering performance in all cases and often enhances cluster interpretability, offering a robust and scalable solution for improving data representation in unsupervised NLP tasks.

### 中文一句话结论
本文提出了一种结合高斯混合模型（GMM）和大语言模型（LLM）的无监督数据增强方法，通过识别并增强文本聚类中的稀疏区域来提升不平衡数据集的聚类性能与可解释性。

### English TL;DR
This paper introduces an unsupervised data augmentation method that uses Gaussian Mixture Models (GMMs) to detect underrepresented clusters and Large Language Models (LLMs) to generate synthetic documents, improving clustering performance and interpretability on imbalanced text datasets.

### 中文详细总结
在自然语言处理（NLP）中，处理代表性不足的主题（即不平衡聚类）是一项挑战，尤其在无监督聚类任务中。现有数据增强方法大多均匀应用于整个数据集或依赖标签信息，无法有效解决无监督场景下的类别不平衡问题。本文提出一种新型无监督数据增强方法：首先使用GMM对文档嵌入进行聚类，通过体积与比例之比识别稀疏（代表性不足）的聚类；然后在这些稀疏聚类中生成合成数据点，并利用LLM基于最近邻的真实文档生成新的语义连贯的合成文本。实验表明，该方法在所有情况下都能保持甚至提升聚类性能，并常能增强聚类可解释性。

### 方法 / 贡献
- 使用 Transformer 嵌入模型（如 Sentence-BERT）和 UMAP 降维表示文档。
- 采用 GMM 和 EM 算法对文档嵌入进行软聚类，并通过 Tikhonov 正则化稳定体积计算。
- 基于体积/比例比值排序，选择最稀疏的聚类（top k*）进行针对性增强。
- 在稀疏聚类内按分布生成合成嵌入点，并取其三个最近邻真实文档作为上下文，通过 LLM（如 GPT 系列）生成新的合成文本。
- 贡献：首次将 GMM 的聚类统计特性与 LLM 的生成能力结合，用于无监督不平衡文本数据的定向增强，无需任何标签信息。

### 实验或数据
论文未在摘要中明确列出具体数据集名称和详细实验结果数据，仅提及“在多种不平衡文本数据集上进行了实验”。具体数据集和性能指标需参阅全文。

### 值得关注点
- 利用 GMM 的体积/比例比自动识别稀疏区域，具有理论依据和可解释性。
- 使用 LLM 生成合成文本时，基于最近邻真实文档作为上下文，保证语义连贯性。
- 方法完全无监督，不依赖任何标签信息，适用于真实世界中的不平衡数据。
- 实验表明在不同场景下均能保持原有聚类性能，并常能提升聚类可解释性。

### 局限性
- 依赖 GMM 对嵌入空间的假设（每个聚类为高斯分布），可能不适用于非高斯分布的数据结构。
- UMAP 降维可能丢失部分信息，影响聚类和增强效果。
- LLM 生成合成文本的质量和多样性受限于模型能力和提示设计。
- 增加数据量可能带来额外计算开销，且未讨论增强比例对性能的影响。
- 论文未提供具体的实验数据集名称和定量结果，难以评估方法的实际效果。

## 7. Data Turnstile: A Scalable Open Framework for Function-Calling Data Generation

- Source: arxiv
- arXiv ID: 2607.29250
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.29250v1
- PDF: https://arxiv.org/pdf/2607.29250v1
- DOI: https://doi.org/10.48550/arXiv.2607.29250

### Authors

Goutham Ramakrishnan, Megha Sharma

### Abstract

Small language models (SLMs) are attractive for agentic deployment due to low latency, reduced cost, and on-device privacy, yet they struggle with tool-use tasks where training data is scarce and noisy. Unlike larger models, SLMs cannot compensate for low-quality supervision through sheer capacity, making data quality the critical bottleneck. We present Data Turnstile, an open-source framework that takes user-defined API specifications and generates high-quality synthetic training data for function calling. Turnstile decomposes multi-turn tool-use interactions into constrained, stepwise generation with validation and error-feedback loops, providing fine-grained control over API diversity, conversation complexity, and output correctness. We demonstrate effectiveness of domain adaptation with Turnstile data on two challenging function calling benchmarks. On the BFCL single-turn benchmark, a Qwen3-0.6B fine-tuned on Turnstile data without chain-of-thought achieves 75.9% overall accuracy (versus 67.4% for the base model with thinking enabled), closing the gap with thinking-enabled Qwen3-1.7B (78.4%) and Qwen3-4B (79.9%) despite being 3$\times$ and 7$\times$ smaller respectively. On $τ^2$-bench, a multi-turn agentic benchmark, Turnstile-trained Qwen3-1.7B achieves 31.1% pass^1 on the Telecom domain, improving 4.7$\times$ over its 6.6% base and surpassing Qwen2.5-32B-Instruct (27.4%), a model 19$\times$ larger. Turnstile-trained Qwen3-0.6B achieves 24.6%, improving 7$\times$ over its 3.5% base and approaching the 32B model (53$\times$ larger). We release Data Turnstile along with a dataset spanning 1,000+ APIs and 100K+ multi-turn interactions.

### 中文一句话结论
Data Turnstile是一个可扩展的开源框架，通过逐步生成与验证机制，为小语言模型（SLM）生成高质量的函数调用合成训练数据，使其在性能上可匹敌甚至超越大一个数量级的模型。

### English TL;DR
Data Turnstile is a scalable open-source framework that generates high-quality synthetic function-calling training data for small language models through stepwise generation with validation, enabling SLMs to match or outperform models an order of magnitude larger.

### 中文详细总结
小语言模型（SLM）因其低延迟、低成本和设备端隐私保护等优势，在智能体部署中具有吸引力。然而，它们在工具使用任务上表现不佳，主要原因是缺乏高质量的训练数据。与大型模型不同，SLM无法通过模型容量弥补低质量数据带来的问题，因此数据质量成为关键瓶颈。

本文提出了Data Turnstile，一个开源框架，能够根据用户定义的API规范，生成高质量的函数调用合成训练数据。该框架的核心创新在于将多轮工具使用交互分解为一系列受限的、逐步生成的步骤，每个步骤都包含验证和错误反馈循环。具体来说，Data Turnstile使用交互模板（一个有向无环图）来定义生成过程的结构，包含五个角色：用户(USER)、API调用(API_CALL)、API观察结果(API_OBS)、助手(ASSISTANT)和思考(THINKING)。生成过程按顺序执行每个角色，每一步都进行格式合规性验证和内容质量检查。

Data Turnstile通过三个层次确保数据多样性：模板层面（不同的交互结构）、参数层面（不同的API、用户画像和场景）和动态模板扰动（如引入工具执行失败或信息不完整的情况）。实验表明，使用该框架生成的训练数据微调后，Qwen3-0.6B模型在BFCL单轮函数调用基准测试上达到75.9%的准确率，而基础模型（带思维链）仅为67.4%。在τ²-bench多轮基准测试的Telecom领域，Qwen3-1.7B和4B模型的表现匹配或超越了比它们大19倍的Qwen2.5-32B-Instruct模型。

研究团队发布了三个方面的开源成果：Data Turnstile框架、一个包含1000+API和10万+多轮交互的合成数据集，以及详细的基准测试结果。

### 方法 / 贡献
1. **Data Turnstile框架**：一个可扩展的开源框架，通过逐步生成方法从自定义API生成函数调用数据，严格控制质量和多样性。框架核心是交互模板（有向无环图），将复杂的多轮交互分解为独立的角色生成步骤，每步都包含验证和错误反馈机制。

2. **全面的实验验证**：在BFCL和τ²-bench两个基准测试上，对三个模型规模（0.6B-4B）进行实验，包括思维链(CoT)消融实验和工具调用加权SFT损失的评估。结果显示，使用Turnstile数据训练的SLM在性能上可匹敌甚至超越大19倍的模型。

3. **开源资源**：发布了一个包含1000+API和10万+多轮交互（含CoT推理轨迹）的合成数据集，适用于SLM微调。所有代码和数据均在开源许可下发布。

### 实验或数据
**数据集**：从四个API来源生成大规模合成数据集：xLAM、Glaive、合成领域和BFCL，每个来源包含1-3K个API定义。使用Qwen2.5-32B-Instruct作为生成模型，在8个H100 GPU上运行。

**BFCL单轮基准测试结果**（主要结果）：
- Qwen3-0.6B（使用Turnstile数据微调，无CoT）：75.9%
- Qwen3-0.6B（基础模型，带CoT）：67.4%
- Qwen3-1.7B（带CoT）：78.4%
- Qwen3-4B（带CoT）：79.9%

**τ²-bench多轮基准测试结果**（Telecom领域）：
- Qwen3-1.7B（Turnstile训练）：31.1%（比基础模型的6.6%提升4.7倍）
- Qwen3-4B（Turnstile训练）：优于或匹配Qwen2.5-32B-Instruct（27.4%）
- Qwen3-0.6B（Turnstile训练）：24.6%（比基础模型的3.5%提升7倍）

### 值得关注点
- **效率与质量的平衡**：逐步生成虽然增加了LLM调用次数，但通过较小的提示长度、vLLM的分页注意力机制和连续批处理等技术，实际开销适中。错误重试机制显著提高了生成成功率。
- **无需推理时思维链**：使用Turnstile数据训练的模型在不使用CoT的情况下也能取得良好性能，这对于延迟敏感的部署场景至关重要。
- **结构化多样性**：通过模板、参数和动态扰动三个层次的多样性控制，生成的数据集比原始开源数据更大且更多样化，平均包含更多角色和API调用。

### 局限性
- 框架目前主要针对函数调用场景设计，对其他类型的工具使用或更广泛的智能体任务（如代码生成、网络搜索等）的适用性有待验证
- 生成质量高度依赖教师模型（当前使用Qwen2.5-32B-Instruct），如果使用更小的教师模型可能导致数据质量下降
- 虽然框架是开源的，但生成大规模高质量数据集仍需相当的GPU资源
- 多轮交互的模板设计需要人工投入，不同领域可能需要定制化的模板结构
- 论文未讨论数据安全性和隐私保护问题，特别是在处理敏感API时的数据泄露风险

## 8. TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs

- Source: arxiv
- arXiv ID: 2607.28640
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.28640v1
- PDF: https://arxiv.org/pdf/2607.28640v1
- DOI: https://doi.org/10.48550/arXiv.2607.28640

### Authors

Andong Hua, Colton Bishop, Igor Mordatch, Arian Hosseini, Jindong Gu, Aleksandra Faust, Rebecca Roelofs, Yao Qin

### Abstract

Multimodal large language models (MLLMs) should generate consistent responses given semantically equivalent inputs across modalities. However, we observe a systematic discrepancy in model predictions under such cross-modal variations. Specifically, we define the modality gap as the difference in model performance under semantically equivalent textual and multimodal inputs. We introduce TokenSwap, a method that constructs such inputs by replacing textual concepts with semantically aligned images, resulting in sequences where visual tokens are interleaved with text tokens. Based on TokenSwap, we transform existing text-based benchmarks such as MMLU into image-interleaved counterparts, resulting in TokenSwap-Bench. Across 42 MLLMs, we observe a pervasive modality gap, with performance decreasing by 4.2% to 47.4% when moving from text-only to image-interleaved inputs, averaging 19.6% +/- 3.3% across models. Notably, we observe that reasoning models exhibit consistently smaller gaps, achieving an average gap of 10.1% compared to 25.5% for non-reasoning models. In contrast, neither prompting strategies nor scaling training compute alone reliably reduces the modality gap. Finally, we demonstrate that incorporating TokenSwap during training effectively mitigates this gap while preserving strong text-only and vision-language performance.

### 中文一句话结论
本文提出TokenSwap方法（将文本概念替换为语义对齐的图像），在42个多模态大语言模型上发现普遍存在的模态差距（平均19.6%），并证明在训练中引入TokenSwap能有效缩小这一差距。

### English TL;DR
TokenSwap introduces a method to construct semantically equivalent image-interleaved inputs, benchmarks a pervasive modality gap across 42 MLLMs, and demonstrates that incorporating TokenSwap during training effectively reduces this gap while preserving strong performance.

### 中文详细总结
多模态大语言模型（MLLM）应在语义等价的跨模态输入下生成一致响应，但实际中存在系统性差异。作者定义模态差距为模型在纯文本输入与图像交错输入（TokenSwap构造）间的性能差异，并基于MMLU构建TokenSwap-Bench（1516个样本，6946张图像）。评估42个MLLM发现：所有模型均存在明显模态差距（4.2%–47.4%，平均19.6%±3.3%）；推理模型差距更小（平均10.1%对25.5%）；提示策略或增加训练计算量无法可靠缩小差距。最后，在预训练或后训练阶段使用TokenSwap增强数据能有效减小模态差距，同时保持纯文本和视觉语言任务的性能。

### 方法 / 贡献
- 提出TokenSwap：数据驱动的跨模态输入构造方法，将文本中的可视化概念替换为语义对齐的图像，生成图像交错序列。
- 构建TokenSwap-Bench（基于MMLU）：系统量化模态差距的基准，包含严格过滤（有效性、重要性、字幕验证）和人工验证。
- 评估42个MLLM，揭示模态差距的普遍性及推理模型优势。
- 首次基于训练的策略（预训练/后训练）有效减小模态差距，且不牺牲其他性能。

### 实验或数据
- 模型：42个MLLM，涵盖开源（Qwen-VL系列、InternVL系列、LLaVA-OV等）和闭源（GPT-4o/5、Gemini 2.5/3、Claude 4.5/4.6等），包括推理、指令微调、MoE等多种范式。
- 数据集：TokenSwap-Bench，由MMLU转换而来，共1516个样本，平均每个样本替换4.58个图像。
- 评测：分别记录纯文本准确率和图像交错输入准确率，计算模态差距。提示策略（CoT、few-shot）和训练计算量消融实验均基于该基准。

### 值得关注点
- 所有42个模型均存在非平凡模态差距（最低4.2%，最高47.4%），且闭源模型（如Claude）差距较小。
- 推理模型（如Gemini-3-Flash、o3-mini）模态差距显著小于非推理模型（平均10.1% vs. 25.5%），且相对差距也较小。
- 通用提示策略（链式思考、少样例）和单纯增加训练计算量（10× FLOPs仅降低约2.8%差距）无法可靠缩小差距。
- 使用TokenSwap进行训练增强（预训练或后训练）能有效缓解模态差距，且不损害纯文本或视觉语言任务性能。

### 局限性
- 语义等价性并非完美：文本概念是抽象的，图像是具体实例，通过“语义可恢复性”作为代理，但仍有偏差。
- 图像替换引入额外变化（序列长度增加、多图像处理、生成图像伪影），可能导致部分性能下降，难以完全归因于模态本身。
- TokenSwap-Bench基于MMLU（知识问答），可能无法完全推广到其他类型任务（如视觉推理、开放生成）。
- 训练增强实验仅在特定模型上验证，通用性需进一步研究。

## 9. PTP: Previous-Token Prediction based LLM Inversion for Near-Exact Prompt Reconstruction

- Source: arxiv
- arXiv ID: 2607.29378
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.29378v1
- PDF: https://arxiv.org/pdf/2607.29378v1
- DOI: https://doi.org/10.48550/arXiv.2607.29378

### Authors

Pirzada Suhail, Nagasai Saketh Naidu, Atanu R Sinha, Amit Sethi

### Abstract

Large language models (LLMs) generate text by auto-regressively sampling the next token. This inherently leads to a many-to-many mapping between prompts and responses, complicating the task of inferring prompts from observed outputs. Prior work on LLM inversion frames prompt recovery as a semantic reconstruction task. They rely on fine-tuning pretrained sequence-to-sequence models on large external datasets--and requiring access to model weights or logits--to generate semantically plausible prompts. In contrast, we present a functional approach to inverting a given LLM in a black-box setting, without auxiliary aids. We train an explicit inverse language model entirely from scratch on data synthetically generated from the target LLM itself. Analogous to forward next-token prediction, our inverse model is trained using previous-token prediction, establishing a generative link between the forward and inverse processes that enables faithful prompt reconstruction. Moreover, it naturally supports diverse prompt reconstructions through sampling, whereby all such prompts induce similar responses under the forward, target LLM. Our approach generalises across datasets and exhibits transferability in reconstructing prompts from responses generated by different LLMs. Further, across the set of token based evaluation metrics for prompt and response reconstructions, our approach outperforms prior work.

### 中文一句话结论
本文提出一种黑盒大语言模型逆向方法，通过从头训练基于前一个Token预测（PTP）的逆向模型，仅利用目标模型自身生成的合成数据，实现从单条响应中近乎精确地重构原始提示。

### English TL;DR
This paper introduces a black-box LLM inversion method that trains an inverse language model from scratch using previous-token prediction on synthetic data from the target LLM, enabling near-exact prompt reconstruction from a single response.

### 中文详细总结
大型语言模型通过自回归采样下一个Token生成文本，导致提示与响应之间存在多对多映射，使得从观测输出推断提示变得困难。现有工作将提示恢复视为语义重构任务，依赖微调预训练序列到序列模型，并需要访问模型权重或logits。本文提出一种纯黑盒的功能性逆向方法：在不依赖任何辅助工具（权重、logits、外部数据）的情况下，完全从目标模型自身生成的合成数据中训练一个明确的逆向语言模型。该逆向模型采用前一个Token预测（PTP）目标，与正向的下一个Token预测对称，从而建立正向与逆向过程之间的生成联系，实现忠实提示重构。通过采样，该方法能自然恢复出多个不同的提示，这些提示在正向目标模型下均能产生相似响应。该方法在多个数据集上表现良好，并展现出跨不同大语言模型的零样本迁移能力。在基于Token的提示和响应重构评估指标上，该方法优于现有工作。

### 方法 / 贡献
- 提出**前一个Token预测（PTP）**方法，用于黑盒LLM逆向，从零训练逆向语言模型。
- 设计**合成数据生成策略**：通过对目标LLM进行词汇级探测，无需访问模型内部即可生成训练数据。
- 利用**序列反转**将逆向任务转化为标准自回归预测，使逆向模型与正向模型结构兼容。
- 支持**多次采样**产生多个可能的提示重构，且这些提示在正向模型下能产生相似响应。
- 展示逆向模型在**不同LLM之间的零样本迁移能力**。

### 实验或数据
论文摘要未提及具体实验数据集或详细数值结果。提供的预览内容包含一个对比表（L2T、O2P与PTP），显示PTP仅需单条响应、使用合成数据、可重构多个提示，并具有跨GPT-4o的零样本迁移性，但未给出具体评估指标得分。论文声称在基于Token的评估指标上优于先前工作，但未提供完整实验细节。

### 值得关注点
- 纯黑盒设置：无需模型权重、logits、嵌入或真实训练数据，仅需文本输出。
- 创新性训练目标：前一个Token预测（PTP），逆向生成过程与正向过程对称。
- 合成数据自给自足：无需外部数据，完全由目标模型探测生成，可随训练动态生成。
- 单条响应即可重构，且支持多样化提示恢复。
- 跨模型迁移性好：零样本适用于不同LLM。

### 局限性
论文提供的摘要和预览内容未明确讨论局限性。从方法本身推断，可能存在的局限包括：从头训练逆向模型计算开销较大；合成数据生成依赖于目标模型的随机解码，可能无法覆盖所有提示类型；对于极长提示或复杂结构化提示的重构效果有待验证；当前方法主要基于Token级评估，语义级保真度未充分探讨。

## 10. PARALLEL: A Prefrontal-Aligned Reinforcement inspired Approach for Language-Model Learning under Explicit Limits

- Source: arxiv
- arXiv ID: 2607.28982
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.28982v1
- PDF: https://arxiv.org/pdf/2607.28982v1
- DOI: https://doi.org/10.48550/arXiv.2607.28982

### Authors

Namkyung Yoon, Sanghong Kim, Hwangnam Kim

### Abstract

Recent language models achieve strong performance across a variety of tasks, but conventional adaptation applies updates uniformly across training samples regardless of their local update benefit. We propose PARALLEL, a prefrontal-aligned reinforcement inspired approach for language-model learning. Inspired by the complementary roles of goal-related and uncertainty-related control, PARALLEL represents these forms of information as separate controller signals and combines them with the current model representation. A reinforcement-inspired controller assigns sample-dependent update intensity using immediate utility-cost feedback. PARALLEL therefore learns when and how strongly to adapt to each sample, prioritizing beneficial updates while limiting unnecessary parameter changes. PARALLEL uses available updates more efficiently than selective baselines while retaining 94.1--99.2\% of Full-adaptation performance. Beyond multiple-choice reasoning, experiments on XSum and CNN/DailyMail show that PARALLEL retains 96.9--98.6\% of the ROUGE-1 and ROUGE-2 scores achieved by Full adaptation and 98.8--98.9\% of the corresponding ROUGE-L scores. When compared at the same cumulative adaptation time or GPU energy, PARALLEL achieves higher ARC accuracy and exhibits a more stable late-stage adaptation trajectory than Full adaptation in the representative run. These results show that learning when and how strongly to update each sample supports stable and efficient post-deployment stream adaptation while avoiding unnecessary updates.

### 中文一句话结论  
PARALLEL 通过模拟前额叶皮层中目标相关与不确定性相关信号的分离控制机制，结合强化学习控制器自适应调整每个样本的更新强度，在有限更新预算下保留全量适配 94% 以上的性能。

### English TL;DR  
PARALLEL introduces a prefrontal-aligned reinforcement-inspired controller that uses separate goal-related and uncertainty-related signals to learn sample-wise update intensity, enabling language models to adapt efficiently under explicit update limits while retaining over 94% of full-adaptation performance.

### 中文详细总结  
传统语言模型适应方法对所有训练样本施加统一更新，忽略局部收益差异。PARALLEL 受前额叶皮层中目标与不确定性信息分离处理的启发，设计两种独立控制信号：目标相关信号（基于诊断前向的损失与准确率）和不确定性相关信号（包含响应熵、词级别熵、置信度、边际与方差）。该信号与当前模型表示拼接后输入轻量控制器，控制器通过一步 REINFORCE 学习选择三种动作（Skip、Light、Strong），从而决定是否以及以多大强度更新每个样本的 LoRA 适配器，同时受全局更新预算约束。实验表明，PARALLEL 在 ARC 等推理任务上保留 Full adaptation 94.1%–99.2% 的性能，在 XSum 和 CNN/DailyMail 上 ROUGE-1/2 保留 96.9%–98.6%，ROUGE-L 保留 98.8%–98.9%，且在相同累积时间或 GPU 能耗下表现更稳定。

### 方法 / 贡献  
- 提出 PARALLEL 框架，将前额叶皮层启发的分离信号与强化学习结合，实现样本级更新强度控制。  
- 设计基于目标一致性（诊断损失和准确率）和模型不确定性（多维度熵、置信度等）的控制器状态。  
- 利用一步 REINFORCE 训练控制器，在硬更新预算约束下学习何时跳过、轻度或强更新。  
- 在多个推理和摘要任务上验证方法有效性，显示高效、稳定的流式适配能力。

### 实验或数据  
- **推理任务**：ARC 等多选题数据集，与 Frozen、Full adaptation 对比。  
- **摘要任务**：XSum、CNN/DailyMail，评估 ROUGE-1/2/L。  
- **主要结果**：PARALLEL 保留 Full adaptation 94.1%–99.2% 准确率；摘要 ROUGE-1/2 保留 96.9%–98.6%，ROUGE-L 保留 98.8%–98.9%。  
- **效率对比**：相同累积适配时间或 GPU 能耗下，PARALLEL 取得更高 ARC 准确率且后期适应轨迹更稳定。  
- 还进行了跨骨干模型、控制器输入消融等实验。

### 值得关注点  
- **神经科学启发**：直接借鉴前额叶皮层中目标与不确定性信号分离的组织原则。  
- **细粒度控制**：不再只选择样本或调整参数，而是学习每个样本的更新强度（跳过/轻/强）。  
- **显式预算约束**：硬性限制累计更新质量，避免过度适应。  
- **稳定高效**：在相同资源下比全量适应更稳定，且无需对全部样本进行完整更新。

### 局限性  
论文未明确列出局限性。根据方法设计，PARALLEL 需要监督标签进行诊断前向和控制器训练，仅适用于有监督的流式适配场景；控制器的额外计算和诊断前向可能引入一定开销。方法未涉及无监督或预训练阶段的适应。

## Processing Notes

- Duplicate papers skipped: 0