# Daily arXiv - 2026-09-26

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-26T01:07:21
- Paper count: 10

## 1. Tag-Aware Structured Text Translation: Towards a Systematic Understanding

- Source: arxiv
- arXiv ID: 2609.29131
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.29131v1
- PDF: https://arxiv.org/pdf/2609.29131v1
- DOI: https://doi.org/10.48550/arXiv.2609.29131

### Authors

Zhanglin Wu, Hengchao Shang, Daimeng Wei, Jiaxin Guo, Zongyao Li, Tengfei Song, Ning Xie, Weidong Zhang

### Abstract

Internet texts are replete with format tags that carry structural, semantic, and functional meaning. Current large language model (LLM)-based translation systems struggle to balance translation fluency with tag fidelity when processing tagged text. We argue that resolving this tension requires a systematic approach at three interconnected levels: data synthesis, capability building, and multi-objective alignment. At the data level, we identify and formalize a fundamental trade-off between structural tag diversity and translation naturalness in synthetic data generation; existing methods optimize for one at the expense of the other. We propose a hybrid synthesis strategy (Hy-LST) combining LLM-based synthesis tag method and Two-Stage LLM-based synthesis tag method to produce both diverse and natural tagged data. At the capability level, we decompose tag-aware translation into four sub-tasks of increasing difficulty in a multi-task supervised fine-tuning framework, enabling targeted capability acquisition and knowledge transfer. At the alignment level, we design three complementary reward functions under a group relative policy optimization framework, each targeting a distinct objective (fluency, tag fidelity, and tag-scoped translation quality), and show that joint optimization consistently outperforms single-reward alternatives. Experiments on six language directions (en2zh, en2ja, en2de, en2fr, en2ru, de2fr) demonstrate that each level contributes measurable improvements, and the complete system significantly outperforms existing methods. Qualitative analysis reveals specific error patterns and their mitigation after training with our method.

### 中文一句话结论
本研究提出一个系统性框架，通过混合数据合成、多任务微调与多奖励强化学习，在六个语言方向上显著提升了带标签文本翻译的流畅性与标签保真度。

### English TL;DR
This paper presents a systematic framework for tag-aware structured text translation that addresses the diversity-naturalness trade-off in data synthesis, decomposes capability into multi-task supervised fine-tuning, and applies multi-reward reinforcement learning to balance fluency and tag fidelity, achieving consistent improvements across six language directions.

### 中文详细总结
互联网文本中的格式标签携带结构、语义和功能信息。现有基于大语言模型的翻译系统在处理带标签文本时难以平衡翻译流畅性与标签保真度。本文认为解决这一矛盾需要从数据合成、能力构建和多目标对齐三个层面系统推进。在数据层面，作者识别并形式化了合成数据生成中结构标签多样性与翻译自然性之间的根本权衡，并提出混合合成策略Hy-LST，结合基于LLM的合成标签方法（LST）和两阶段LLM合成标签方法（LST-2S），生成既多样又自然的带标签数据。在能力层面，论文将标签感知翻译分解为四个难度递增的子任务，并采用多任务监督微调框架，实现针对性能力获取与知识迁移。在对齐层面，设计三种互补奖励函数（流畅性、标签保真度、标签范围内的翻译质量），在组相对策略优化框架下联合优化。实验覆盖六个语言方向（en2zh, en2ja, en2de, en2fr, en2ru, de2fr），每个层面均带来可衡量的改进，完整系统显著优于现有方法。定性分析揭示了特定错误模式及训练后的缓解效果。

### 方法 / 贡献
- **数据层面**：首次形式化标签多样性与翻译自然性的权衡，提出Hy-LST混合合成策略（LST + LST-2S）生成多样且自然的带标签数据。
- **能力层面**：设计四任务多任务监督微调框架，按难度递增分解标签感知翻译，实现跨技能知识迁移。
- **对齐层面**：在GRPO框架下设计三种互补奖励（流畅性、标签保真度、标签范围翻译质量），联合优化优于单一奖励。

### 实验或数据
- **数据集**：使用Salesforce的多语言结构化文档翻译数据集（开源），包含英中、英日、英德、英法、英俄及德法六个方向。每个英语中心方向约100K训练、2K开发、2K测试（测试集未公开，改用开发集）；德法方向通过英语桥接构建约90K训练对。
- **评价指标**：COMET（流畅性）、XML-Match（标签保真度）、XML-IN-COMET（标签范围翻译质量）。
- **主要结果**：完整系统在所有方向上优于现有方法，各层面贡献可测量。定性分析显示训练后错误模式明显减少。

### 值得关注点
- 首次明确并解决合成数据中多样性与自然性的权衡。
- 将标签感知翻译分解为多任务，促进能力逐步构建。
- 多奖励联合优化成功平衡了流畅性与标签保真度。

### 局限性
论文未明确讨论局限性。潜在局限包括：依赖合成数据可能引入领域偏差；实验仅覆盖六种语言方向（大部分以英语为中心）；方法需要较强的大语言模型支持；对非正式或复杂标签结构（如嵌套标签）的泛化能力未深入评估。

## 2. CORDIAL: Calibrating Ordinal LLM Outputs from Few Labels

- Source: arxiv
- arXiv ID: 2609.29807
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.29807v1
- PDF: https://arxiv.org/pdf/2609.29807v1
- DOI: https://doi.org/10.48550/arXiv.2609.29807

### Authors

Xiangwei Wang, Peng Wang, Saman Halgamuge

### Abstract

A large language model (LLM) can turn a text into a distribution over an ordered scale, but that distribution is a noisy measurement: saturated, compressed or exaggerated, and biased in a consistent direction. We propose CORDIAL, which treats the model's output as a noisy reading of the true label and corrects it with a channel of five interpretable parameters. The channel is small enough for its posterior to be averaged from a handful of labels, and we prove that the resulting calibration preserves first-order stochastic order. On Amazon reviews and CMU-MOSEI transcripts with four LLMs, CORDIAL has the lowest log loss among nine calibrators in 76 of 80 settings with 5 to 100 labels; with 20 labels and the main 7B reader, it matches the strongest baseline using 28-54 labels. The same posterior lets us learn priors from other tasks and fuse several LLMs. Unrestricted calibrators such as Dirichlet calibration overtake it only as the calibration set grows into the hundreds or thousands.

### 中文一句话结论
CORDIAL 将 LLM 在有序类别上的输出视为真实标签的噪声测量，用一个仅含 5 个可解释参数的通道进行贝叶斯校正，从而在极少标注（5–100 条）下显著降低对数损失，并证明其校正不会逆转类别之间的随机占优顺序。

### English TL;DR
CORDIAL corrects an LLM's ordinal output by modeling it as a noisy measurement through a five-parameter structured channel, achieving strong calibration from as few as 5–100 labels while preserving first-order stochastic order.

### 中文详细总结
- 问题设定：LLM 在有序量表上的输出分布是失真的读数，表现为饱和、压缩或夸大、以及方向性偏差。
- 核心思想：将冻结 LLM 的输出视为真实有序标签的带噪读数，通过一个结构化的行随机通道进行校正。
- 通道参数：共 5 个可解释参数——温度 temperature、偏移 offset、增益 gain、集中度 concentration、强度 strength。
- 两种通道形式：混合形式保留原始读数的形状；位置形式假设预测为单峰分布，适用于“四舍五入均值”式的标签。
- 贝叶斯估计：5 参数后验可用少量标签估计，并通过 Laplace 近似加 300 次重要性重加权样本求后验均值。
- 序数一致性：证明该通道在似然比序和随机占优意义下不会逆转读数的序关系。
- 扩展能力：同一后验还可跨任务学习先验、融合多个冻结 LLM、以及加入每用户偏移参数。

### 方法 / 贡献
- C1：提出贝叶斯结构化通道的两种形式，证明其保持序数随机占优，并可叠加在 logit 空间校准器上。
- C2：给出参数计数交叉公式 n\* = (d_u − d_s)/(2δ)，用于预测无约束校准器何时会超过结构化通道。
- C3：展示 5 参数后验的三种用途：跨任务先验、少标签多 LLM 融合、单用户一维偏移。
- 关键动机：标量可信度只能缩放读数相对先验的偏差，无法把质量移到相邻类别；CORDIAL 的 5 参数结构比无约束 K×K 或 Dirichlet 校准更适配少标签场景。

### 实验或数据
- 数据：Amazon Reviews 2023 的三个领域（Digital Music、All Beauty、Software），K=5；CMU-MOSEI 转录文本，K=7。
- 模型：Qwen2.5-Instruct 3B、7B、14B 和 Llama-3.1-8B-Instruct，主模型为 7B。
- 设置：校准标签数 n ∈ {5, 10, …, 2000}，每个设置取 20 个标签子集；评估指标为负对数似然 NLL 和 RPS。
- 结果：在 5–100 标签设置下，CORDIAL 在 80 个组合中的 76 个取得最低 log loss；使用 20 个标签时，主 7B 模型达到最强基线需 28–54 标签的效果。
- 额外发现：在 n=20 时，CORDIAL 比 logit stack 在 Music、Beauty、Software、MOSEI 上分别低 0.046、0.057、0.024、0.053 nats；后验平均在标签数不超过 10 时最多带来 0.134 nats 提升。

### 值得关注点
- 仅用 5 个参数即可做后验平均，而不是依赖点估计，这对小样本校准很关键。
- 理论上保证不逆转序数顺序，这是普通混淆矩阵校准无法提供的性质。
- 参数计数交叉公式可解释“结构何时比规模更优”，为校准方法选择提供依据。
- 同一个后验支持跨任务先验、多模型融合和用户级偏移，扩展性强。

### 局限性
- 无约束校准器（如 Dirichlet calibration）只有在校准集扩大到数百或数千条时才会超过 CORDIAL，因此 CORDIAL 的优势主要体现在少标签区间。
- 方法依赖“序数误差可由 5 参数通道刻画”的结构假设；如果结构近似误差 δ 很大，其相对无约束校准器的优势会在由交叉公式预测的规模处消失。

## 3. SemMSA: Latent Semantic-Aided Robust Multimodal Sentiment Analysis with Incomplete Data

- Source: arxiv
- arXiv ID: 2609.30238
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.30238v1
- PDF: https://arxiv.org/pdf/2609.30238v1
- DOI: https://doi.org/10.48550/arXiv.2609.30238

### Authors

Wenhao Li, Zhibin Wu, Chong Xiao, Qiangchang Wang

### Abstract

Recent research on Multimodal Sentiment Analysis (MSA) has focused on learning from language, visual, and acoustic modalities with incomplete data to infer human sentiment. Most studies typically compensate for missing information by reconstructing modality features or designing complicated fusion mechanisms. However, these methods still suffer from spurious generation and noisy guidance due to the lack of high-level semantic grounding in partially observed multimodal evidence. To address these issues, we propose SemMSA, a latent semantic-aided framework that constructs rich sentiment-relevant semantics with LLMs, fully integrating with all modalities via anchor-free spectral alignment. It mainly consists of Cross-modal Semantic Refinement (CSR) and Cross-modal Spectral Alignment (CSA). Specifically, CSR first adaptively extracts visual and acoustic representations by corresponding adapters to form a unified multimodal prefix with language in the frozen LLM embedding space. It then iteratively produces continuous discriminative semantic states through a token-efficient latent refinement process without decoding explicit text. Next, CSA simultaneously aligns the refined semantics with all modalities by enhancing the dominant spectral component of their kernel Gram matrix. This captures global nonlinear dependencies among all representations without relying on a predefined anchor modality. In addition, an instance-level spectral separation constraint preserves cross-sample discriminability and mitigates representation collapse. Extensive experiments on SIMS, MOSI, and MOSEI benchmarks demonstrate that SemMSA achieves state-of-the-art performance.

### 中文一句话结论
本文提出 SemMSA 框架，利用大语言模型生成潜在语义补偿不完整多模态数据，并通过无锚点谱对齐实现鲁棒的多模态情感分析，在多个基准上达到最优性能。

### English TL;DR
SemMSA is a latent semantic-aided framework for robust multimodal sentiment analysis with incomplete data. It uses LLMs to generate sentiment-relevant latent semantics via Cross-modal Semantic Refinement and aligns all modalities through anchor-free Cross-modal Spectral Alignment, achieving state-of-the-art results on SIMS, MOSI, and MOSEI.

### 中文详细总结
现有不完整多模态情感分析方法主要依赖特征重构或复杂融合机制，但因缺乏高层语义支撑而容易产生虚假生成和噪声引导。SemMSA 通过两个核心模块解决此问题：跨模态语义精炼（CSR）利用轻量适配器将视觉、声学特征映射到冻结的大语言模型（LLM）嵌入空间，并通过迭代隐式精炼生成连续的、具有情感判别性的潜在语义状态，避免显式文本解码；跨模态谱对齐（CSA）通过构建核格拉姆矩阵并增强其主谱分量，实现语义与所有模态（语言、视觉、声学）的对齐，无需预设锚点模态；同时引入实例级谱分离约束以保持样本间判别性。实验在 SIMS、MOSI、MOSEI 三个基准上验证了有效性。

### 方法 / 贡献
- **SemMSA 框架**：首次利用 LLM 进行不完整多模态情感分析的语义级补偿。
- **CSR 模块**：通过适配器将视觉、声学特征与语言在 LLM 空间融合，并利用冻结 LLM 的循环隐态精炼生成紧凑的潜在语义表示。
- **CSA 模块**：基于核格拉姆矩阵的主谱增强，实现无锚点的多模态对齐，捕获全局非线性依赖；附加谱分离约束防止表示坍塌。
- **贡献总结**：提出高层语义补偿与无锚点谱对齐的新范式，在多个缺失数据场景下显著提升性能（如准确率提升 1.4%）。

### 实验或数据
在 SIMS、MOSI、MOSEI 三个多模态情感分析基准上进行了广泛实验，涵盖不同缺失模式与程度。结果显示 SemMSA 达到当时最优性能（SOTA）。摘要未提供具体数值细节。

### 值得关注点
- 首次将 LLM 用于不完整多模态情感分析的语义补偿，而非简单特征重构。
- 无需显式文本生成，通过隐式潜在语义精炼实现高效补偿。
- 谱对齐无需锚点模态，对严重缺失场景鲁棒。
- 实例级分离约束有效保持判别性。

### 局限性
论文未明确讨论局限性。可推断的潜在问题包括：依赖大型语言模型带来较高计算成本；适配器与精炼过程增加训练复杂度；方法在最严重缺失场景下的表现尚需进一步分析；谱对齐的超参数（如核函数选择、分离约束强度）可能需要调优。

## 4. R-DEIM Net: An Efficient Rationale-Augmented Dual-Expert Interaction Model for Paraphrase Detection

- Source: arxiv
- arXiv ID: 2609.30100
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.30100v1
- PDF: https://arxiv.org/pdf/2609.30100v1
- DOI: https://doi.org/10.48550/arXiv.2609.30100

### Authors

Pushp, Vaibhav Prajapati, Himangshu Sarma

### Abstract

Recent advances in paraphrase detection reveal a fundamental trade-off: large language models achieve high accuracy but require high computation, while efficient Siamese-BERT variants offer practical scalability with reduced transparency in rationale generation. We present R-DEIM Net, a 76M-parameter dual-expert architecture exploring whether moderate-scale models can achieve competitive accuracy on paraphrase detection while enabling human-readable rationale generation. The architecture combines two specialized components: an Interaction Expert that captures token-level similarity patterns through multi-scale 2D convolutions and attention head allowing variable input length, and a Reasoning Expert that uses a Flan-T5-small decoder to generate rationales as auxiliary supervision. Rather than re-encoding generated text, we extract and pool decoder hidden states as complementary features for classification. On the Quora Question Pairs dataset, R-DEIM Net achieves 90.07\% accuracy and 90.16\% F1-score via 10-fold cross-validation. This represents competitive performance with strong transformer-based baselines (e.g., MFAE BERT: 90.54\% accuracy) and recent large language model based approaches (LLaMA-70B) while using a substantially smaller parameter budget. The model generates rationales alongside predictions, providing potential for auxiliary human-readable descriptions.

### 中文一句话结论
R-DEIM Net是一种76M参数的双专家框架，在Quora Question Pairs数据集上以90.07%的准确率和90.16%的F1分数实现了接近大模型性能的同义改写检测，同时具备可读理由生成能力。

### English TL;DR
R-DEIM Net is a 76M-parameter dual-expert model that achieves competitive paraphrase detection accuracy on Quora Question Pairs (90.07%) while generating human-readable rationales, offering an efficient alternative to larger models.

### 中文详细总结
同义改写检测面临准确性与计算效率之间的权衡：大型语言模型（LLMs）准确率高但计算开销大，而高效的Siamese-BERT变体可扩展性良好却缺乏理由生成的透明度。本文提出R-DEIM Net，一种含7600万参数的双专家架构，旨在探索中等规模模型能否在实现有竞争力的同义改写检测精度的同时，生成人类可读的理由。模型由交互专家（Interaction Expert）和推理专家（Reasoning Expert）组成：交互专家通过多尺度2D卷积和注意力机制捕捉词级相似模式，支持可变输入长度；推理专家基于Flan-T5-small解码器生成理由作为辅助监督，其隐藏状态被提取并池化作为分类的互补特征，避免了文本重新编码。在Quora Question Pairs数据集上，R-DEIM Net经10折交叉验证达到90.07%准确率和90.16% F1分数，优于或接近许多强基线（如MFAE BERT的90.54%准确率）和基于LLaMA-70B的方法，但参数量大幅减少。

### 方法 / 贡献
方法：提出双专家架构——交互专家（Interaction Expert）负责建模句子对间的细粒度相似性，使用多尺度二维卷积与注意力机制；推理专家（Reasoning Expert）利用Flan-T5-small解码器生成自然语言理由，并提取解码器隐状态作为辅助特征用于分类，不重新编码生成文本。贡献：(1) 在中等参数规模（76M）下同时达到强分类性能与可读理由生成能力；(2) 通过隐状态池化方式融合理由信息，避免额外推理开销；(3) 为同义改写检测提供了一种高效且可解释的替代方案，平衡了精度、计算与透明度。

### 实验或数据
数据集：Quora Question Pairs（QQP）。评估方法：10折交叉验证。主要结果：准确率90.07%，F1分数90.16%。对比基线：强Transformer模型如MFAE BERT（准确率90.54%）以及基于LLaMA-70B的方法，R-DEIM Net在相近准确率下参数量显著更小。

### 值得关注点
- 仅76M参数即达90.07%准确率，与超过700M参数的模型竞争力相当。
- 同时输出分类结果与人类可读理由，提升可解释性。
- 理由生成不依赖重新编码生成的文本，而是通过池化解码器隐状态，计算高效。
- 交互专家支持可变输入长度，适应实际应用。

### 局限性
论文未明确讨论局限性。从已有描述看：(1) 仅在QQP单一数据集上验证，泛化能力有待在其他领域同义改写数据集上评估；(2) 生成的理由质量尚未进行人工评测或与标准参照对比；(3) 模型准确率仍略低于部分强基线（如MFAE BERT 90.54%），且未与更多最新大模型（如GPT-4）直接比较。

## 5. Post-Training Leaves Behavioral Shadows on Unrelated Decisions

- Source: arxiv
- arXiv ID: 2609.29233
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.29233v1
- PDF: https://arxiv.org/pdf/2609.29233v1
- DOI: https://doi.org/10.48550/arXiv.2609.29233

### Authors

Ziyang Zhang, Yubin Jing, Yuanhao Zeng, Yuyao Li, Haofan Wang, Yichen Gong

### Abstract

We find that language models can transfer capabilities through task-unrelated text. Post-training typically improves language models using task-specific data. Prior work on subliminal learning shows that information about these updates can pass through unrelated generations, but has largely focused on traits or preferences using extensive teacher outputs. We introduce Active Taskless Distillation (ATD), which achieves capability transfer using only a single word from the teacher per prompt. ATD probes the behavioral shadow of post-training by selecting prompts where the teacher and student's shared public ancestor is nearly indifferent between two ordinary words. A student initialized from this ancestor learns solely from the resulting prompt-word pairs, without target-task examples, teacher logits, or teacher parameters. In the primary coding experiment with Qwen2.5-1.5B, 5,664nses yield a 5.34 pp gain on HumanEval+ over an exact nuisance-matched control thadisrupts prompt-resperiments showtransfer in scientific knowledge, commonsense reasoning, and reading comprehensins across additional model generations, sizes, and families. Functional analyses show that the learned sid composable, andthat its strength tracks the teacher's update strength.

### 中文一句话结论
本文发现，通过仅用每个提示中一个任务无关的词，就可以从教师模型向学生模型传递后训练能力（如编码、科学知识、推理等），揭示了后训练会在不相关决策中留下可被利用的“行为影子”。

### English TL;DR
The paper introduces Active Taskless Distillation (ATD), demonstrating that post-training capabilities can be transferred from a teacher to a student model using only a single task-unrelated word per prompt, revealing that post-training leaves behavioral shadows that affect unrelated decisions.

### 中文详细总结
本文提出 Active Taskless Distillation (ATD) 方法，利用后训练留下的行为影子实现能力迁移。ATD 选择提示，使教师和学生的共享祖先模型对两个普通词汇几乎无偏好，从而探测后训练信号。学生仅从这些提示-词对中学习，无需目标任务示例、教师 logits 或参数。在 Qwen2.5-1.5B 上的主要实验中，使用 5,664 个提示在 HumanEval+ 上获得 5.34 个百分点的提升（相对控制组）。该方法还成功迁移了科学知识、常识推理和阅读理解能力，并在多种模型世代、规模和家族中得到验证。功能分析表明，学到的信号是可组合的，且其强度与教师模型的更新强度正相关。

### 方法 / 贡献
- 提出 Active Taskless Distillation (ATD)，仅用单个任务无关的词进行能力迁移，无需目标任务数据、教师 logits 或参数。
- 揭示后训练会在模型的不相关决策中留下可被探测和利用的行为影子。
- 在编码、科学知识、常识推理、阅读理解等多个任务上验证了迁移的有效性，并跨模型家族和规模进行测试。

### 实验或数据
- 主要实验：使用 Qwen2.5-1.5B 模型，以 5,664 个提示在 HumanEval+ 上进行编码任务测试，控制组为精确的扰动作匹配。
- 额外实验：在科学知识、常识推理和阅读理解任务上验证迁移，涉及其他模型世代、规模和家族（具体数据集和细节需参考全文）。

### 值得关注点
1. **简洁高效**：仅需每个提示一个词即可实现能力迁移，方法轻量。
2. **广泛验证**：在多种任务和模型上展示有效性，具有一定通用性。
3. **可解释性**：学到的信号可组合且与教师更新强度相关，提供了对行为影子的量化理解。

### 局限性
摘要中未明确讨论局限性。潜在限制包括：
- 方法依赖于共享祖先模型的选择和提示设计，可能影响迁移效果。
- 迁移能力的稳健性和通用性（尤其在不同训练范式下）仍需进一步探索。
- 未报告在大规模模型（如 70B+）上的实验结果，规模扩展性未知。

## 6. What a Cross-Model Fixed-Point Census Can and Cannot Arbitrate About Repetition

- Source: arxiv
- arXiv ID: 2609.29507
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.29507v1
- PDF: https://arxiv.org/pdf/2609.29507v1
- DOI: https://doi.org/10.48550/arXiv.2609.29507

### Authors

Nicolás Vera Zúñiga

### Abstract

Two accounts of neural text degeneration coexist. One locates the cause in the training data -- repetition in the corpus produces repetition in the output, established by training on repetition-sorted data -- the other in the trained network, in copying circuits and repetition features. Neither has been arbitrated across a broad cohort of pretrained models: the causal work trains its own. We report an observational measurement in a different currency: the fixed-point structure of a model's own short-window argmax map, censused from 96 random two-token starts over 17 off-the-shelf models, always unprompted -- a companion paper shows nine tokens of conditioning move this readout across most of its range. The four-way class is stable across census seeds on 17 of 17. Three exhibits. At fixed corpus (The Pile), fixed scale and that fixed domain, the class is not determined: across two size-matched tiers, pythia is a funnel while RWKV, Mamba and a second transformer family are not, and both hold their class across an order of magnitude of scale. Six of seven models in that ladder reach the same endpoint token, and those concentrating on it most strongly are among those that never stay there -- what varies is not where trajectories go but whether the destination self-continues. The deduplicated Pythia suite does not change the class. And the corpus-side inflow term proposed for this phenomenon does not select our endpoints once frequency is controlled, in English and three other languages. This is observational and cannot refute a training intervention. Funnels are common: eight of seventeen models, seven families, five corpora -- so the limit is not that the phenomenon is one model's peculiarity, but that within the one corpus where training data can be held fixed only one available family funnels; that subset cannot show the split is corpus-independent.

### 中文一句话结论  
这篇论文通过观测17个预训练语言模型在短窗口argmax映射下的不动点结构，发现重复文本倾向并非仅由训练数据或模型规模决定——在同一语料库和相同参数量级下，不同架构家族（如Pythia vs. RWKV、Mamba）表现出截然不同的固定点类别（漏斗型 vs. 非漏斗型），表明权重侧因素起关键作用。

### English TL;DR  
This observational study measures the fixed-point structure of 17 off-the-shelf language models using a short-window argmax map. At fixed corpus (The Pile) and matched scale, model families show fundamentally different repetition classes (funnels vs. non-funnels), proving that training data alone does not determine repetition behavior. The finding is stable across seeds and holds across scale, but cannot refute causal training interventions.

### 中文详细总结  
关于神经文本退化（重复）存在两种解释：一种归因于训练数据中的重复模式，另一种归因于网络内部的复制电路和重复特征。此前因果研究训练自身模型，未在广泛预训练模型间仲裁。本文采用不同度量：对17个即用模型，从96个随机双token起点迭代argmax映射，统计终止于自映射token的比例（不动点分数，FPF），并据此将模型分为漏斗型（funnel）、无型（none）、碎片型（fragmented）和边界型（borderline）。主要发现：  
1. 在同一语料库（The Pile）和相同规模下，Pythia是漏斗型，而RWKV、Mamba及另一Transformer家族（GPT-Neo）不是，且类别在数量级规模变化中保持稳定。  
2. 7个模型中有6个到达相同终点token（换行符），但差异在于该token是否自我延续——注意力集中程度高的模型反而从不停留于该token。  
3. 去重后的Pythia套件不改变类别；语料侧“流入”项（high-inflow）在控制频率后无法预测终点。  
4. 漏斗型常见（17个中8个，7个家族，5个语料库）。但局限在于：同一语料库（The Pile）中仅一个家族呈现漏斗型，因此无法证明类别跨语料库独立。观测性研究不能反驳训练干预的因果结论。

### 方法 / 贡献  
**方法**：对每个模型，迭代其双token条件argmax映射（x_{t+1} = argmax p(x | x_{t-1}, x_t)），从96个随机双token起点开始，统计终止于自映射token的比例（FPF），并结合模态份额将模型分类。所有测量在无提示（raw domain）下进行，且验证了类别在独立种子上稳定（17/17）。  
**贡献**：提供跨16个模型家族的观测性证据，证明在固定语料库和规模下，重复倾向并非由数据唯一决定，权重侧存在不可忽略的因素。该证据不同于因果训练干预，为两种解释的仲裁提供了新视角。

### 实验或数据  
- **模型**：17个即用预训练模型，涵盖GPTNeoX、RWKV、Mamba、GPT-Neo等家族，训练于The Pile及其他四个语料库。  
- **测量**：每个模型从96个随机双token种子出发，记录FPF和模态份额，分类为漏斗/无/碎片/边界四类。所有模型在两个独立种子下类别一致。  
- **关键比较**：在固定语料库（The Pile）和固定参数量级（400M和150M tier）下对比Pythia、RWKV、Mamba、GPT-Neo。Pythia始终为漏斗型，其他为无型（FPF ≤ 0.052）。  
- **规模效应**：Pythia从70M到1000M（14倍跨度）保持漏斗型；GPT-Neo从125M到2700M（22倍）保持无型。  
- **终点token分析**：7个模型中6个到达换行符；但漏斗型与非漏斗型的差异在于终点是否自续。  
- **控制实验**：去重Pythia套件不改变类别；语料侧流入项在控制频率后不预测终点（英语及三种其他语言）。  
- **数据来源**：论文表格F178、F179及补充材料。

### 值得关注点  
1. **类别稳定性**：17个模型在两个种子下类别完全一致，终点token在15/17中稳定，支持了结果的可靠性。  
2. **终点token趋同但行为分化**：6/7模型到达同一token（换行符），但漏斗型与非漏斗型的核心差异在于该token是否成为自续固定点——而非轨迹终点不同。  
3. **去重实验**：在去重Pile上训练的Pythia系列未改变类别，表明该现象不因语料重复率变化而改变。  
4. **语料流入假说失效**：高频词（high-inflow）无法解释终点选择，控制词频后不存在关联，表明语料分布之外的力量在起作用。  
5. **漏斗普遍性**：8/17模型（7个家族、5个语料库）为漏斗型，说明并非个别模型异常，但同一语料库内仅有一家漏斗，限制了跨语料库验证。

### 局限性  
1. **观测性**：未进行训练数据干预，因此不能反驳Li等人（2023）的因果结论（训练数据重复导致输出重复）。  
2. **单语料库比较**：交叉家族比较仅在The Pile上进行（其他语料库无多种架构可用），无法确认分类差异是否独立于语料库。  
3. **短窗口限制**：测量仅限于双token窗口argmax映射；伴随论文显示窗口扩展至16 token后FPF降至零，因此结论不可推广到长上下文或条件设定。  
4. **无提示范围**：所有测量在无条件（raw domain）下进行，九token条件即可改变类别，故分类标签不适用于有提示场景。  
5. **未使用生成统计量**：度量的是条件概率属性而非实际文本生成重复率（如rep-n），二者不等价。

## 7. Grammatical "grandmother neurons" are rare in LLMs

- Source: arxiv
- arXiv ID: 2609.29328
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.29328v1
- PDF: https://arxiv.org/pdf/2609.29328v1
- DOI: https://doi.org/10.48550/arXiv.2609.29328

### Authors

Linyang He, Nima Mesgarani

### Abstract

Understanding how Large Language Models (LLMs) encode linguistic structures remains a fundamental challenge in interpretability research. While diagnostic classifiers (or "probes") are widely used for this task, they face significant methodological criticism: training auxiliary classifiers introduces capacity confounds and calibration issues, often making it difficult to distinguish the model's intrinsic representations from the probe's ability to learn the task. To address these limitations, we introduce a probe-free framework for localizing linguistic selectivity at the individual neuron level. Leveraging the controlled contrasts of linguistic minimal pairs, we propose a Neuron Separability Index (NSI), a metric that directly quantifies how reliably single neurons differentiate grammatical from ungrammatical constructions without parameter updates. Applying NSI across 68 linguistic paradigms and seven checkpoints reveals three main patterns: 1) raw separability reaches near-peak levels earlier for morphological and syntactic distinctions than for syntax-semantics interface and conceptual distinctions. 2) after permutation normalization, single-unit selectivity is sparse, weak, and narrowly tuned: only a small fraction of units are sensitive to an average paradigm, and strongly selective "grandmother neurons" are rare. 3) whole-vector linear separability, single-neuron selectivity, and behavioral competence are largely dissociated, and targeted ablations further separate activation selectivity from causal reliance.

### 中文一句话结论  
本研究通过无探针的神经元可分离性指数（NSI）系统评估了大型语言模型中单个神经元对语法对比的选择性，发现强烈选择的“祖母神经元”极为罕见，单神经元选择性整体呈现稀疏、微弱且窄带调谐的特点。

### English TL;DR  
This paper introduces a probe-free Neuron Separability Index (NSI) to measure individual-neuron selectivity for grammatical contrasts in LLMs, revealing that strongly selective “grandmother neurons” are rare and single-unit selectivity is sparse, weak, and narrowly tuned across linguistic paradigms.

### 中文详细总结  
大型语言模型（LLM）如何编码语言结构仍是可解释性研究的核心难题。传统方法使用诊断分类器（探针）存在容量混淆和校准问题，难以区分模型内在表征与探针的学习能力。为克服这些限制，本文提出无探针框架——神经元可分离性指数（NSI），直接度量单个神经元区分合法与非法语法结构的能力，无需更新参数。NSI基于语言最小对（如BLiMP和COMPS数据集），通过配对激活向量的相关性和置换归一化计算。  
在68个语言范式和7个检查点（包括Qwen3系列、Pythia、TinyLlama、Llama-3.1）上的实验揭示三个主要模式：  
1. 原始可分离性：形态和句法区分在较早层达到近峰值，而句法-语义接口和概念区分较晚。  
2. 置换归一化后：单神经元选择性稀疏、微弱且窄带调谐——平均每个范式只有少量神经元敏感，强烈选择性的“祖母神经元”极为罕见。  
3. 全向量线性可分离性、单神经元选择性和模型行为表现基本分离，靶向消融进一步表明激活选择性与因果依赖无关。  

### 方法 / 贡献  
- **无探针框架**：提出NSI指标，基于最小对激活的相关性和置换归一化，直接量化单神经元对语法对比的选择性，避免辅助分类器的混淆。  
- **层次化评估**：将68个语言范式组织为领域→现象→范式的三级层次，实现跨语法维度的可比性。  
- **发现可分离性**：证明全向量解码性、单神经元选择性和行为表现三者之间基本分离，挑战了神经元选择性直接解释模型行为的假设。  

### 实验或数据  
- **数据集**：BLiMP（67个范式）和COMPS（补充为68个范式），覆盖4个领域、13个现象。  
- **模型**：7个解码器因果语言模型——Qwen3-0.6B/1.7B/4B/8B、Pythia-410M、TinyLlama-1.1B、Llama-3.1-8B。  
- **分析**：对每个神经元计算NSI，使用500次置换生成零分布，阈值>0为敏感，>2为强选择。比较了全向量线性探针、行为准确率和靶向消融。  

### 值得关注点  
- **祖母神经元罕见**：仅少数范式（3个）存在NSI>2的神经元，表明强选择性单元在语法中极其稀疏。  
- **可分离性分离**：单神经元选择性与全向量解码性及行为表现无强关联，推翻“定位单一神经元即可解释行为”的直觉。  
- **窄带调谐**：即使多范式响应的神经元也主要限于单领域，而非通用语法检测器。  

### 局限性  
原文未明确列出局限性。基于实验设置可推断：  
- 仅研究因果语言模型和有限的语法范式，可能无法推广到编码器模型或其他语言任务（如语义、推理）。  
- NSI依赖于最小对的对比，可能无法捕捉更复杂的层级或交互作用。  
- 置换归一化阈值（NSI>2）是描述性而非严格的统计显著性标准，不同阈值下的结论稳定性需进一步验证。

## 8. EnSiTa - A Trilingual Multi-Domain Parallel Dataset and Benchmark for Domain-Specific Machine Translation

- Source: arxiv
- arXiv ID: 2609.29511
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.29511v1
- PDF: https://arxiv.org/pdf/2609.29511v1
- DOI: https://doi.org/10.48550/arXiv.2609.29511

### Authors

Surangika Ranathunga, Nisansa de Silva, Aloka Fernando, Kavindu Warnakulasuriya, Isuru Wijesiri, Menan Velayuthan, Charitha Rathnayaka, Thivaharan Varatharajan, Sajeevi Silva, Piumi Kandanaarachchi, Uthayasanker Thayasivam

### Abstract

Machine Translation (MT) for low-resource languages remains far behind that of high-resource languages, and the gap is widest in specialised domains, where parallel data is scarce or entirely absent. We present EnSiTa, a trilingual multi-domain parallel dataset and benchmark for English, Sinhala and Tamil. EnSiTa provides human post-edited training data for seven domains, plus manually translated test sets for those and one additional domain, all produced by professional translators under a multi-year, rigorously quality-controlled process. Using this dataset, we conduct an extensive study of domain-specific MT for all six language directions, fine-tuning a from-scratch Transformer, a pre-trained translation model (NLLB-600M), and decoder-only LLMs (Gemma 3 family, 1B-12B, and TranslateGemma) across training-data sizes, model scales, and in-domain, cross-domain, multilingual and multi-domain settings. To the best of our knowledge, this is the most extensive systematically documented multi-domain parallel data creation and benchmarking effort for low-resource MT. Our data and models will be publicly released.

### 中文一句话结论
本研究构建并公开了英语、僧伽罗语和泰米尔语的三语多领域平行语料库EnSiTa，并基于此开展了低资源语言领域专用机器翻译的最全面基准测试。

### English TL;DR
EnSiTa introduces a trilingual multi-domain parallel dataset and benchmark for English, Sinhala, and Tamil, featuring human-post-edited training and manually translated test sets across seven domains, enabling extensive domain-specific machine translation experiments for low-resource languages.

### 中文详细总结
- **数据集规模**：训练数据包含20万+句子对（人工后编辑），测试数据包含1万+句子对（人工翻译），覆盖7个领域（电影字幕、数学、健康、新闻、历史/维基百科、文学、开放域）以及一个附加测试领域（LLM Jailbreak）。
- **语言方向**：涵盖英语-僧伽罗语、英语-泰米尔语、僧伽罗语-泰米尔语共6个翻译方向。
- **实验设置**：在11个测试集上，对比了从头训练的Transformer、预训练翻译模型NLLB-600M及解码器专用LLM（Gemma 3家族，1B-12B，TranslateGemma）在不同训练数据规模、模型大小及单域、跨域、多语言、多域微调下的性能。
- **核心发现**：编译后的数据集在低资源语言领域专用翻译任务上效果显著提升，尤其验证了多域联合训练与模型缩放的优势。

### 方法 / 贡献
1. **数据构建**：从公开网络挖取和机器翻译语料出发，经专业翻译人员多轮严格质量控制完成人工后编辑，形成高质量的多领域平行语料。
2. **基准评测**：制定系统化的领域专用翻译测试集，覆盖单域、跨域、多语言及多域设置，全面评估不同架构与规模模型的性能。
3. **公开资源**：数据集和模型全部开源，为低资源语言MT研究提供可复现的基准。

### 实验或数据
- **训练数据**：200k+句子对（来自7个领域的后编辑语料，另补充政府、圣经领域的已有数据）。
- **测试数据**：10k+句子对（人工翻译，含7个训练领域+1个Jailbreak领域），以及FLORES+测试集。
- **模型**：Fairseq Transformer、NLLB-600M、Gemma 3（1B-12B）及TranslateGemma，在全6个翻译方向上展开。
- **实验维度**：不同训练数据规模、模型大小、单域/跨域、多语言、多域微调对比。

### 值得关注点
- 首次系统构建三语多领域平行数据集并开展领域专用MT的全面评测，尤其填补了僧伽罗语-泰米尔语低资源方向的数据空白。
- 实验设计严谨，覆盖跨域迁移、多域联合、模型缩放等实用场景，结论对实际部署有直接参考价值。
- 所有资源开源，促进低资源语言领域研究可复现性。

### 局限性
- 数据集仅涵盖三种语言及7个训练领域，扩展至更多语言和领域仍需持续投入。
- 数据来源受公开资源和资金限制，部分语料先经机器翻译再后编辑，可能引入原始噪声或领域偏差。
- 实验虽涉及模型缩放（1B-12B），但未涉及超大模型（≥70B），对LLM在低资源翻译上的潜力探索仍有限。
- 跨域泛化能力测试集中在有限领域内，对全新未接触领域的表现尚需进一步验证。

## 9. Self-Play Pretraining with Zero Data

- Source: arxiv
- arXiv ID: 2609.30063
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.30063v1
- PDF: https://arxiv.org/pdf/2609.30063v1
- DOI: https://doi.org/10.48550/arXiv.2609.30063

### Authors

Aditya Cowsik, Kfir Dolev, Michael Y. Li, G. Bruno De Luca, Nourya Cohen, Noah D. Goodman, Yoav Levine

### Abstract

Advances in language modeling have been driven by scaling pretraining on ever more data. Yet, the training data is still largely curated on the model's behalf. A more general approach to pretraining would let the model learn to generate the data most useful for its own improvement. This would provide an effectively unbounded source of training data, limited by compute rather than human knowledge. We introduce Self-Play Pretraining with Zero Data, an initial proof-of-concept towards realizing this vision. Our procedure casts synthetic data generation as a search over the space of all computable structure, taking inspiration from Solomonoff induction. Starting from random initialization, two models learn in tandem: a generator proposes programs interpreted by a universal Turing machine, generating byte sequences, while a learner autoregressively predicts these byte sequences. The learner is trained with standard cross-entropy, while the generator is trained with reinforcement learning to produce sequences at the frontier of the learner's capabilities, yielding an adaptive curriculum. A universal Turing machine gives us a search space over all computable data-generating processes, imposing little domain-specific structure, and self-play searches over this space for useful training data. We test whether zero-shot performance on natural data improves predictably with self-play compute; this is a clean test of transfer since neither generator nor learner is trained on natural data. Across several natural datasets, zero-shot loss exhibits predictable scaling in compute. The models also exhibit in-context learning, and discover recognizable mathematical sequences during training.

### 中文一句话结论
论文提出“零数据自对弈预训练”框架，通过生成器与学习者在通用图灵机程序空间内自对弈生成数据，在不接触任何自然数据的情况下，实现了零样本损失随计算量可预测缩放。

### English TL;DR
Self-Play Pretraining with Zero Data introduces a self-play framework where a generator and learner co-evolve on synthetic data from a Universal Turing Machine, achieving zero-shot performance on natural data that scales predictably with compute, using no human-curated data.

### 中文详细总结
为了突破预训练数据依赖人类知识的局限，本文提出了一个概念验证性的零数据自对弈预训练框架。该框架包含一个生成器（Generator）和一个学习器（Learner）。生成器通过强化学习（RL）训练，负责在通用图灵机（UTM）决定的“所有可计算结构”空间中搜索程序，这些程序被解释为字节序列。学习器则使用标准的交叉熵损失对这些字节序列进行自回归预测。生成器产生的序列会处于学习者能力的“前沿”，从而形成一个自适应课程（Adaptive Curriculum）。在任意自然数据均未参与训练的前提下，模型在多个自然数据集上展现出零样本损失随自对弈计算量增加的可预测缩放规律（Predictable Scaling），并发现了可识别的数学序列和上下文学习能力。

### 方法 / 贡献
- **方法**：构建生成器-学习者对偶架构。生成器在通用图灵机程序空间中进行搜索（受Solomonoff归纳启发），并通过强化学习调整搜索策略，以生成当前学习器最难预测的字节序列（自适应课程）。学习器对此序列进行自回归建模（Cross-Entropy）。
- **贡献**：
    1.  提出真正的“零自然数据”预训练范式，训练数据仅受限于计算量而非人类知识。
    2.  证明零自然数据条件下，模型在自然语言数据上的损失依然服从可预测的缩放定律（Scaling Laws）。
    3.  为彻底摆脱人类数据依赖、实现无限计算驱动的预训练提供了初步的可行性验证。

### 实验或数据
- **实验设置**：在完全不使用任何自然数据进行训练的条件下，评估模型在多个自然数据集上的零样本（Zero-shot）表现。
- **主要发现**：
    - 零样本**损失**（Loss）与自对弈计算量之间存在清晰、可预测的幂律缩放关系（Predictable Scaling），这是验证迁移能力的干净测试。
    - 模型在训练过程中自发发现了可识别的数学序列（如基本算术模式）。
    - 模型展现出一定的上下文学习能力（In-Context Learning）。
- **数据集**：摘要未具体命名所使用的自然数据集，仅提及“多个自然数据集”（several natural datasets）。

### 值得关注点
1.  **完全零数据**：完整的学习过程不依赖任何人工标注或自然文本数据。
2.  **通用搜索空间**：利用通用图灵机程序空间作为数据源，理论上覆盖所有可计算模式，域知识先验极少。
3.  **自适应课程学习**：生成器由强化学习驱动，自动生成当前阶段对学习器最有信息量的训练数据。
4.  **新颖的扩展现象**：首次展示纯合成数据预训练在自然语言上的可预测扩展性，为大模型训练开辟了新路径。

### 局限性
1.  **初步概念验证**：论文本身定位为“proof-of-concept”，在模型规模和任务多样性上可能与完全基于自然数据的预训练存在差距。
2.  **零样本损失与下游任务**：目前仅证实了零样本损失的可预测缩放，模型在下游具体任务上的实际表现有待进一步验证。
3.  **搜索效率**：通用图灵机程序空间的搜索可能面临效率问题，实际应用中的计算开销需要仔细权衡。
4.  **可计算性边界**：搜索空间虽大，但局限于“可计算”结构，对于超出此范畴的物理或现实世界规律，该范式的有效性未知。

## 10. Polite but Misaligned: Evaluating LLM Politeness Judgments Against Human Pragmatic Norms

- Source: arxiv
- arXiv ID: 2609.29001
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.29001v1
- PDF: https://arxiv.org/pdf/2609.29001v1
- DOI: https://doi.org/10.48550/arXiv.2609.29001

### Authors

Rong Wang, Kun Sun, Yadong Guo

### Abstract

Despite strong performance on standard benchmarks, it remains unclear whether large language models (LLMs) evaluate social pragmatics in ways that align with human judgments. We evaluate LLM politeness judgments using two English-language datasets with complementary annotation formats: continuous human ratings and three-way categorical labels. Across the seven evaluated models, we find that inter-model agreement is stronger than model--human agreement. Strategy-level analyses suggest that model--human alignment is associated with explicit linguistic cues, while some rapport-building strategies occur more frequently in misaligned cases. In the categorical task, model predictions exhibit systematic neutral compression, characterized by the overproduction of Neutral labels and the underprediction of Impolite labels. This pattern persists when expert consensus is used as the reference on a diagnostic subset. Our findings highlight the need for pragmatic evaluations that go beyond aggregate agreement metrics by examining directional patterns of model--human disagreement across different human references.

### 中文一句话结论
大型语言模型（LLM）在礼貌判断上与人存在系统性对齐偏差：它们倾向于过度使用中性标签（中性压缩），依赖显性表面线索（而非深层语用策略），且模型间的判断一致性显著高于人机一致性。

### English TL;DR
This paper evaluates LLM politeness judgments against human norms using two English datasets (continuous ratings and categorical labels). It finds that inter-model agreement systematically exceeds model-human agreement. LLMs exhibit "neutral compression" (overpredicting Neutral labels, underpredicting Impolite labels), rely heavily on explicit surface cues, and struggle with rapport-building strategies. These misalignment patterns persist even when expert consensus is used as the reference, highlighting systematic gaps in LLM pragmatic competence that go beyond simple annotation noise.

### 中文详细总结
本文系统评估了大型语言模型（LLM）在礼貌判断任务上与人类实用性规范的对齐情况。研究基于两个互补的英文数据集：斯坦福礼貌语料库（连续评分，5分制均值）和一个三分类（不礼貌/中性/礼貌）标注数据集。作者评估了7种主流LLM（包括Gemini-2.5-Flash, GPT-4.1, Claude-3.5-Sonnet, Grok-3, DeepSeek-Chat, Llama-3/3.1-8B）。
主要发现如下：1）**对齐度有限**：模型与人类判断的相关性普遍较弱。模型间的相互一致性（平均r=0.724）系统性高于模型与人类之间的一致性（平均r=0.385）。2）**策略层面差异**：模型对齐依赖于显性语言线索（如please/thank you），但那些旨在建立融洽关系的策略（感谢、问候、道歉等）更常出现于模型与人类判断不一致的案例中。3）**中性压缩**：在三分类任务中，模型普遍表现出“中性压缩”现象，即系统性地过度预测“中性”标签，同时严重低估“不礼貌”标签。4）**专家审计验证**：在针对318个高争议样本进行的专家审计（由5名语言学/语用学研究生标注共识）中，该中性压缩模式依然存在，说明这种现象并非仅由人工标注噪声引起。

### 方法 / 贡献
**方法：**
1. **数据集**：使用连续评分（Stanford Politeness Corpus）和三分类标签两种格式互补的数据集，并结合专家审计处理标注分歧。
2. **模型与提示**：评估7个LLM，采用6种零样本提示模板（P1-P6），变化角色框架（评估员/专家）、线索类型（仅表面/完整语用功能）与输出格式（连续/分类）。
3. **策略分析**：使用基于规则的检测器识别15种礼貌策略，对比对齐/未对齐案例中的策略分布差异。
4. **人类基线**：计算原始连续数据集标注者间一致性（平均配对相关系数r=0.425，ICC=0.786）作为模型表现的上限参考。

**贡献：**
1. 提供了跨人群、专家和LLM的多参考语用对齐评估框架。
2. 揭示了模型间判断一致性系统性高于人机一致性的核心现象。
3. 形式化定义了两种系统性的语用失调特征：“**中性压缩**”（Neutral Compression，指模型过度输出中性标签，错失识别不礼貌与礼貌的能力）与“**表面线索依赖**”（Surface-cue Accumulation，指对齐依赖于显性词语而非深层社会关系管理策略）。
4. 公开了完整的提示模板、评估指标、模型输出和分析代码，高度透明可复现。

### 实验或数据
**数据集：**
- **Dataset 1** (连续): Stanford Politeness Corpus。包含10,957条来自维基百科Talk页和Stack Exchange的请求（每个请求5人打分）。实验平衡采样3,000条。
- **Dataset 2** (分类): Hugging Face politeness-corpus。包含16,428条三分类实例。实验平衡采样3,000条（每类1,000条）。
- **专家审计子集**: 从Dataset 2中选取318条模型-人类分歧最大或策略冲突的样本，由5名语言学/语用学研究生独立标注。

**实验设置：**
- **模型**: 7个LLM（Gemini-2.5-Flash, GPT-4.1, Claude-3.5-Sonnet, Grok-3, DeepSeek-Chat, Llama-3-8B, Llama-3.1-8B），均为开箱默认参数（零样本）。
- **指标**: 连续任务（Pearson r, MAE, Close Rate）；分类任务（Accuracy, Macro-F1, Kappa, 以及核心自创指标：Neutral Compression Difference/Ratio, Impoliteness Suppression Difference, Extreme-to-Neutral Shift Rate）。

### 值得关注点
- **核心发现——中性压缩**：模型系统性地将“不礼貌”和“礼貌”样本预测为“中性”。这暗示模型对语用极性的识别能力不足，尤其对负面社会信号（不礼貌）严重不敏感。
- **模型间的“合谋”**：模型间一致性远高于人机一致性，暗示当前LLM共享了一套词汇统计上相似、但与社会规范有所偏离的语用表征。
- **策略盲点**：模型对齐依赖于显性线索，但忽略了建立社会关系的语用策略（如问候、道歉）。这意味着模型在微妙、高情商的社会互动中可能会失效。
- **方法学贡献**：论文强调超越总体一致性指标，通过分析分歧的方向性模式（如中性压缩）来诊断模型行为，为LLM的社会语言评估树立了新的范式。
- **透明复现**：作者开源了所有提示、详细指标计算方法及完整模型输出。

### 局限性
- **语言与文化的局限性**：研究仅针对英文，且数据集来源于维基百科Talk页和Stack Exchange。这两个平台偏向于以任务为导向、重视直接性的特定社区规范，无法推广到其他语言、文化或更广泛的社会互动场景（如家庭、等级制组织等）。
- **分析工具局限性**：礼貌策略检测器是基于显性规则的（如词汇列表和正则表达式），可能无法捕捉到模型生成的上下文深层语用策略，或存在检测噪声。
- **专家审计样本局限**：用于验证的专家审计样本量较小（318条），且是针对高争议样本的策略性抽样，其统计显著性和对全数据集的代表性有限。
- **默认参数/对齐来源未探讨**：实验使用API默认参数及零样本形式，反映了真实应用场景，但未探讨温度参数、系统指令或RLHF对齐对结果的具体影响，也未深入分析偏差产生的具体模型训练根源（如数据偏置或优化目标）。

## Processing Notes

- Duplicate papers skipped: 0