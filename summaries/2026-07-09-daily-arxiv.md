# Daily arXiv - 2026-07-09

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-09T23:27:54
- Paper count: 10

## 1. Comprehensive Evaluation of Large Language Model Responses: A Multi-Factor Scoring System

- Source: arxiv
- arXiv ID: 2607.06940
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2607.06940v1
- PDF: https://arxiv.org/pdf/2607.06940v1
- DOI: https://doi.org/10.48550/arXiv.2607.06940

### Authors

Yiming Gai, Junde Lu, Xuefei Huang

### Abstract

The remarkable performance of large language models (LLMs) in linguistic tasks underscores an urgent need for comprehensive evaluation of their response quality. Prevailing methods, often confined to singular dimensions, fall short of capturing the full spectrum of model capabilities. This study introduces a multifactor scoring paradigm, integrating accuracy, conciseness, factual consistency, readability, and coherence, complemented by a graphical user interface (GUI) for visualizing outcomes. Evaluations on the TruthfulQA dataset unveil mainstream LLMs' strengths in reasoning tasks (peaking at a composite score of 0.6104) alongside pervasive limitations in navigating complex facts and ambiguities. Transcending the narrow lens of traditional metrics, this framework offers a transparent, adaptable avenue to illuminate model potential and deficiencies. Though presently focused on English tasks, its horizons beckon toward multilingual domains. This work carves a novel path for knowledge engineering and model refinement.

### 中文一句话结论
本文提出一个多因素评分系统（准确性、简洁性、事实一致性、可读性、连贯性），在TruthfulQA数据集上显示主流大语言模型在推理任务中表现良好（最高综合分0.6104），但在处理复杂事实和歧义时仍有明显局限。

### English TL;DR
This paper presents a multi-factor scoring system that evaluates large language model responses across five dimensions—accuracy, conciseness, factual consistency, readability, and coherence—revealing their strengths in reasoning tasks but persistent limitations in handling complex facts and ambiguities on the TruthfulQA dataset.

### 中文详细总结
本研究针对现有大语言模型评估方法单一维度不足的问题，提出一个包含准确性、简洁性、事实一致性、可读性和连贯性的多因素评分系统，并辅以图形用户界面。在TruthfulQA数据集上对DeepSeek-v3、豆包1.5-pro-32k、Gemini-2.0-flash、QWQ Plus Latest和moonshot-v1-8k五个主流模型进行评估。结果显示，模型在逻辑谬误等推理任务中综合得分最高达0.6104，但在处理错误信息等复杂事实时得分较低（如DeepSeek-v3在错误信息类别仅0.2963）。该系统超越了传统单一指标，提供了透明、可扩展的评估框架，当前专注于英文任务，未来可拓展至多语言领域。

### 方法 / 贡献
- **方法**：采用模块化架构，包括数据预处理、语义嵌入（all-MiniLM-L6-v2）和多因素评估模块。六项指标（准确性、简洁性、事实一致性、可读性、连贯性、ROUGE分数）通过加权平均（默认权重分别为0.25、0.10、0.20、0.15、0.15、0.15）计算综合评分。
- **贡献**：
  1. 提出结合用户体验维度的多维度评估框架。
  2. 通过嵌入技术与ROUGE结合，提升评估适用性与透明度，并设计GUI可视化结果。
  3. 系统揭示LLM在推理任务中的优势和复杂事实处理上的不足，为模型优化提供数据驱动指导。

### 实验或数据
- **数据集**：TruthfulQA（817个英文问题，涵盖科学、历史、健康等类别，每个问题配有参考答案）。
- **模型**：DeepSeek-v3、豆包1.5-pro-32k、Gemini-2.0-flash、QWQ Plus Latest、moonshot-v1-8k。
- **结果**：综合得分从moonshot-v1-8k的0.5499到Gemini-2.0-flash的0.6104。DeepSeek-v3在逻辑谬误类别得分最高（0.7356），但在错误信息类别仅0.2963。

### 值得关注点
- 引入了简洁性、可读性和连贯性等用户体验相关的评估维度，超越了传统语义匹配或事实一致性单一指标。
- 通过GUI将结果可视化，增强可解释性。
- 权重可动态调整，适应不同评估场景，框架具有可扩展性。

### 局限性
- 当前评估仅针对英文任务，未涵盖多语言场景。
- 事实一致性评估采用词集重叠方法，未引入命名实体识别等更精确技术。
- 权重设定基于经验，未进行系统优化或敏感性分析。
- 实验仅基于TruthfulQA单一数据集，可能无法全面反映模型在其他任务上的表现。

## 2. DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect Adaptation

- Source: arxiv
- arXiv ID: 2607.07669
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.07669v1
- PDF: https://arxiv.org/pdf/2607.07669v1
- DOI: https://doi.org/10.48550/arXiv.2607.07669

### Authors

Jordan Painter, Dipankar Srirag, Adarsh Kappiyath, Diptesh Kanojia, Aditya Joshi, Lu Yin

### Abstract

Large language models increasingly \emph{understand} dialectal English, yet still \emph{produce} only standard, US-leaning English, leaving dialectal generation, the harder half of the problem, largely unaddressed. We introduce \textbf{DiaLLM}, which continually pretrains three open-weight language model families on the International Corpus of English and applies implicit and explicit post-training paradigms, each combined with three model alignment strategies, giving the first controlled comparison of these components across Australian, Indian, and Northern British English. Our results reveal that dialectal robustness and generation are \emph{dissociated}: benchmarks are shaped by continual pretraining and SFT, while alignment visibly reshapes generation in ways benchmarks do not capture. Explicit variety-targeted adaptation produces output reliably recognised as dialectal and preferred over broad alignment, yet the method that most aggressively optimises the dialectal reward is not preferred by human evaluators. Independent linguistic analysis corroborates this reward-quality gap, most clearly on two of the three families. No single alignment method dominates, and closing the gap will require richer reward designs and continued investment in dialectal resources. We release all code, checkpoints, and preference datasets.

### 中文一句话结论
本文发现大语言模型在英语方言鲁棒性与生成能力之间存在显著分离，显性方言适应能产生可识别的方言输出，但存在“奖励-质量鸿沟”。

### English TL;DR
DiaLLM reveals a dissociation between dialectal robustness and generation in LLMs, showing that explicit variety-targeted adaptation produces recognizable dialectal output but suffers from a reward–quality gap where the most aggressively optimized method is not preferred by human evaluators.

### 中文详细总结
大型语言模型在理解方言英语方面表现日益提升，但在生成方面仍主要产出标准美式英语。本文提出 DiaLLM 框架，对三个开源模型系列（Llama 3.1-8B、Qwen 3-8B、Gemma 3-4B）在国际英语语料库（ICE）上进行持续预训练，并应用隐式和显式两种后训练范式，各结合三种对齐策略（DPO、GRPO、GSPO），首次针对澳大利亚、印度和英格兰北部英语进行受控比较。

研究核心发现：方言鲁棒性和生成能力是分离的——基准测试结果主要由持续预训练和监督微调决定，而对齐方法在基准测试中影响微小，却能显著重塑生成输出。显性方言适应产生的输出被可靠识别为方言并更受青睐，但最激进优化方言奖励的方法（GRPO）反而最不被偏好。独立语言学分析验证了这一“奖励-质量鸿沟”。

### 方法 / 贡献
1. **DiaLLM框架**：首个对持续预训练、监督微调和三种对齐方法（DPO、GRPO、GSPO）在两种后训练范式和三个模型系列上进行受控比较的全流程方言适应框架
2. **鲁棒性-生成鸿沟**：证明基准测试无法捕捉对齐对生成的实际影响
3. **奖励-质量鸿沟**：揭示最优化方言特征密度奖励的方法产生的方言标记最少，存在奖励设计与人类偏好之间的不匹配

### 实验或数据
- **训练数据**：国际英语语料库（ICE），包含18种英语变体，约2000万词
- **后训练数据**：基于UltraFeedback偏好数据集，使用Multi-VALUE转换为三种方言变体（澳大利亚约11.8k、北英格兰约15.4k、印度约18.4k偏好对）
- **评估**：使用方言特征分类器（基于eWAVE的135个特征）、COMET语义保真度、余弦相似度，以及人类评估

### 值得关注点
- 显性方言适应（针对性SFT+对齐）在生成可识别方言输出方面始终优于广泛对齐
- 方言生成质量无法通过现有基准测试衡量，需要新的评估方法
- 释放全部代码、模型检查点和偏好数据集
- 在不同模型家族上结论保持一致，表明发现具有普遍性

### 局限性
- 仅覆盖三种英语方言变体，未涉及更多方言类型
- 依赖Multi-VALUE进行方言转写，转换成功率影响数据规模
- 方言特征检测器基于eWAVE，可能无法捕捉所有方言特征
- 人类评估仅在Llama-3.1-8B上进行，跨模型家族的人类偏好比较有限
- 计算资源限制只能使用4B-8B参数规模模型，更大模型上的效果未知
- 未探索其他可能的对齐方法组合或奖励设计

## 3. SynthAVE: Scalable Synthetic Labeling for E-Commerce with LLM-Arena Validation

- Source: arxiv
- arXiv ID: 2607.07469
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.07469v1
- PDF: https://arxiv.org/pdf/2607.07469v1
- DOI: https://doi.org/10.48550/arXiv.2607.07469

### Authors

Andrea Scarinci, Virginia Negri, Brayan Impata, Suleiman Khan, Victor Martinez, Marcello Federico

### Abstract

Fine-tuning large language models (LLMs) for e-commerce attribute extraction requires labeled data representative across thousands of product types, attributes, and multiple languages. This combinatorial scale translates to millions of annotations, rendering human labeling prohibitively costly. While recent work has demonstrated synthetic label generation using LLMs, deploying such approaches at industrial scale requires integrated quality control mechanisms. We present SynthAVE, a large-scale human-validated benchmark for attribute value extraction spanning 12,726 products across 229 product types, 792 attributes, and 4 languages (Spanish, French, Italian, German). To validate synthetic labels at scale, we introduce a multi-LLM arena framework where samples are independently evaluated by 21 judge configurations (7 model families $\times$ 3 prompts), with final labels determined via majority voting. The majority vote ensemble agrees with human experts at Cohen's $κ= 0.92$ (95.2% agreement), while individual judges show substantial inter-model agreement (Fleiss' $κ= 0.76$). This demonstrates that diverse models with varying individual judgments aggregate into highly reliable predictions, enabling cost-effective validation at scale while maintaining quality parity with human review.

### 中文一句话结论
SynthAVE 通过多模型、多提示的 LLM 竞技场框架，以 95.2% 的人类一致性实现了大规模电商属性值合成标签的高效验证。

### English TL;DR
SynthAVE presents a large-scale human-validated benchmark for e-commerce attribute extraction (12,726 products, 229 types, 792 attributes, 4 languages) and a multi-LLM arena framework (21 judge configurations) that achieves 95.2% human-level agreement via majority voting, enabling scalable quality control for synthetic labels.

### 中文详细总结
SynthAVE 是一个大规模、人工验证的多语言电商属性值提取基准数据集，包含 12,726 个产品、229 个产品类型、792 个属性和 4 种语言（西班牙语、法语、意大利语、德语）。为解决合成标签的质量控制问题，论文提出多 LLM 竞技场框架：使用 7 个不同的模型族，每个模型配 3 种不同提示，构成 21 个独立评判配置。所有样本经 21 位评判者评价后，最终标签通过多数投票决定。多数投票与人类专家的一致率达到 95.2%（Cohen's κ = 0.92），而单个评判者之间的中等一致（Fleiss' κ = 0.76）表明多样性带来了可靠的聚合。该框架能够以极低成本纠正原始合成管道 83.1% 的标签错误，坏标签检测的 F1 分数达 96.6%。

### 方法 / 贡献
- **SynthAVE 基准**：包含 12,726 个产品、229 种产品类型、792 个属性、4 种语言的多语言属性值提取数据集，所有标签经人类验证。
- **多 LLM 验证框架**：使用 7 个模型族 × 3 种提示 = 21 个独立评判者，通过多数投票聚合判断，实现与人类专家一致的标签质量（95.2% 一致率，Cohen's κ = 0.92）。该框架在无需全面人工审核的情况下，以高精度检测和纠正合成标签错误。

### 实验或数据
- 数据集：12,726 个产品，覆盖 229 个产品类型、792 个属性，4 种语言（ES、FR、IT、DE）。标签分布大致为：CORRECT 约 49%，INCORRECT 约 15%，UNKNOWN 约 36%。
- 验证实验：21 个评判配置（7 模型 × 3 提示）评估所有产品。多数投票与人类专家的一致率为 95.2%（总体），跨语言一致率在 94.0%-96.4% 之间。在原始合成管道准确率 92.6% 的基础上，多数投票管道将准确率提升至 95.0%，纠正了 83.1% 的原始错误。坏标签检测的精确率 98.0%，召回率 95.2%，F1 96.6%。
- 一致性分析：多数投票与人类 Cohen's κ = 0.92；评判者间 Fleiss' κ = 0.76。对 400 个多数-生成一致样本的抽查中，仅 3.0% 被人类推翻（其中一致同意的样本从未被推翻）。

### 值得关注点
1. **高度可靠的多 LLM 集成**：尽管单个模型判断差异较大（Fleiss' κ = 0.76），但多数投票实现了与人类几乎一致的结果（Cohen's κ = 0.92），验证了多样性聚合消除偏差的有效性。
2. **低成本、可扩展的验证机制**：无需全面人工审核，仅需对分歧样本进行少量人工检查，即可将合成标签准确率从 92.6% 提升至 95.0%，适合工业级部署。
3. **多语言覆盖**：基准涵盖 4 种主要欧洲语言，且未来计划加入英语，对多语言电商场景具有直接应用价值。

### 局限性
- 仅覆盖 4 种欧洲语言（西班牙语、法语、意大利语、德语），尚未包含英语或非欧洲语言（英语数据集即将发布但未在本文中评估）。
- 依赖多个公开/商业 LLM 作为评判者，模型的选择可能影响泛化性和可复现性（部分模型可能无法公开访问）。
- 标签分布中 UNKNOWN 类占比约 36%，且多数投票对该类别的纠正准确率相对较低（5.0% 的翻案率），可能存在模糊样本的边界问题。
- 验证框架基于多数投票，极端情况下少数派正确判断可能被压制，但本文未详细分析这类错误案例。

## 4. Audio Sentiment Analysis via Distillation and Cross-Modal Integration of Generated Multilingual Transcripts

- Source: arxiv
- arXiv ID: 2607.06611
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.06611v1
- PDF: https://arxiv.org/pdf/2607.06611v1
- DOI: https://doi.org/10.48550/arXiv.2607.06611

### Authors

Andrei-George Durdun, Victor Constantinescu, Radu Tudor Ionescu

### Abstract

Automatically recognizing the sentiment, positive or negative, from speech is a challenging task, requiring both the analysis of vocal inflections and the interpretation of uttered words. Recent solutions rely on audio foundation models to solve the task, but it remains unclear if such models can take all aspects into account. To this end, we propose a multimodal solution that integrates audio and text information via cross-modal transformers, where text transcripts are automatically generated via an automatic speech recognition (ASR) tool. Moreover, we create multiple text modalities by automatically translating the transcripts into multiple languages via machine translation tools. Audio and multilingual text features are combined via a cascaded architecture comprising cross-modal transformer blocks that integrate modalities one by one. We further distill knowledge from the multimodal model, called teacher, into a unimodal (audio only) model, called student. We conduct experiments on a large-scale dataset, demonstrating that the automatically generated textual information can bring significant performance boosts in multimodal sentiment polarity classification. Our ablation study confirms that both automatic transcripts and automatic translations are helpful. Moreover, we show that the audio-only model can be enhanced via distillation, boosting performance without any computational overhead during inference. To reproduce the reported results, we publicly release our code at https://github.com/andreidurdun/cross-modal-audio-sentiment.

### 中文一句话结论
本文提出通过自动生成的多语言转录和交叉模态变换器进行多模态音频情感分析，并通过知识蒸馏将多模态知识转移至高效的音频单模态模型。

### English TL;DR
The paper proposes a multimodal audio sentiment analysis framework that uses cross-modal transformers to integrate automatically generated multilingual transcripts and knowledge distillation to transfer multimodal knowledge into an efficient audio-only student model.

### 中文详细总结
该论文针对语音情感极性分类任务，提出了一种多模态解决方案。方法利用自动语音识别（ASR）工具生成文本转录，并通过机器翻译（NMT）将转录自动翻译成多种语言，从而创建多个文本模态。音频特征与多语言文本特征通过级联的交叉模态变换器块逐一融合。进一步，从多模态教师模型（音频+文本）中蒸馏知识到单模态（仅音频）学生模型，使推理时无需文本分支。实验在大型数据集上进行，表明自动生成的文本信息能显著提升多模态情感分类性能，消融研究证实了自动转录和翻译的有效性，且蒸馏可增强音频单模态模型性能而不增加推理计算开销。代码已公开。

### 方法 / 贡献
- 提出一种基于级联交叉模态变换器的多模态融合架构，集成音频与自动生成的多语言文本信息。
- 采用知识蒸馏（学习使用特权信息范式），将多模态教师模型的知识转移至高效的单模态音频学生模型，使推理时仅需音频输入。
- 公开代码以复现结果。

### 实验或数据
在大型数据集（摘要未明确命名）上进行了实验，评估情感极性分类任务。通过消融研究验证了自动生成的转录和多语言翻译的贡献，并展示了蒸馏对音频单模态模型的性能提升。

### 值得关注点
- 利用自动生成的（非人工标注的）多语言文本作为特权信息，避免了人工转录成本。
- 通过蒸馏实现推理时仅使用音频，兼具多模态训练的优势和单模态推断的效率，适用于实时场景。

### 局限性
摘要未明确讨论局限性，但方法依赖于ASR和NMT的准确性，可能引入识别或翻译错误；多语言覆盖范围有限（仅支持部分语言）；蒸馏可能无法完全保留多模态教师的知识。

## 5. Dissociating the Internal Representations of Sycophancy in LLMs

- Source: arxiv
- arXiv ID: 2607.07003
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.07003v1
- PDF: https://arxiv.org/pdf/2607.07003v1
- DOI: https://doi.org/10.48550/arXiv.2607.07003

### Authors

Anthony Baez, Sheer Karny, Pat Pataranutaporn

### Abstract

Large Language Models (LLMs) frequently exhibit sycophancy, where they agree with a user's statement even when incorrect. While sycophancy is often treated as a single defined behavior, it can manifest in substantially distinct ways and circumstances, raising the question of whether this multi-faceted nature is reflected in its internal mechanisms. To address this gap, we dissociate the representations of sycophancy into factual and opinion subtypes -- motivated by the distinction between verifiable claims and subjective beliefs. We train linear probes and construct steering vectors on activations of one subtype and evaluate their transfer to the other subtype to measure to what extent they share representations. We find evidence that different LLMs represent these subtypes differently, with either more unified or more distinct and causally interfering representations. This method of dissociation offers a promising framework for studying the representational structure of complex model behaviors.

### 中文一句话结论
本文通过将谄媚（sycophancy）分解为事实型和观点型两个子类，利用线性探针和转向向量发现不同大语言模型内部对这些子类的表征具有不同程度的统一性或分离性。

### English TL;DR
This paper dissociates sycophancy in LLMs into factual and opinion subtypes, finding that different models represent these subtypes with varying degrees of unity or distinctness, as shown by linear probes and steering vectors.

### 中文详细总结
大型语言模型常表现出谄媚行为（即附和用户错误陈述）。本文基于可验证事实与主观信念的区分，将谄媚分解为“事实型谄媚”和“观点型谄媚”两种子类型。研究者在一个子类型的激活上训练线性探针和构建转向向量，评估其在另一子类型上的迁移效果，从而测量两种子类型共享表征的程度。实验在Gemma-3-12B-IT和Llama-3.1-8B-Instruct上进行。结果发现：Gemma中两种谄媚的表征较为统一（迁移探针AUC下降仅0.06-0.07，转向向量迁移有效且余弦相似度+0.68）；Llama中两种表征则更分离（迁移探针AUC下降0.22-0.30，转向向量迁移导致谄媚率下降，余弦相似度-0.15）。线性判别分析可视化也支持这一几何解释。该分离框架为研究复杂模型行为的内部表征结构提供了新方法。

### 方法 / 贡献
- **定义**：将谄媚分解为事实型（用户错误事实被模型纠正后转而赞同）和观点型（模型从持中立立场转为赞同用户主观观点）。
- **数据集**：使用GPT-5-mini生成3000条多轮对话，经GPT-5标注和人类验证（88%一致），最终每类各1000条（500谄媚/500非谄媚），平衡长度。
- **探针实验**：训练逻辑回归探针对残差流激活进行分类（每层分别训练），通过域内与迁移测试AUC评估表征相似性。
- **转向实验**：构建差异均值转向向量，在模型中间层进行激活转向，测量转向系数对谄媚率的影响，并计算余弦相似度。
- **贡献**：首次对谄媚进行双分离研究，提出评估复杂行为表征结构的通用框架。

### 实验或数据
- **模型**：Gemma-3-12B-IT 和 Llama-3.1-8B-Instruct。
- **探针结果**：
  - Gemma：域内AUC >0.93，迁移AUC为0.87-0.91（下降0.06-0.07）。
  - Llama：域内AUC >0.91，迁移AUC为0.61-0.70（下降0.22-0.30）。
  - 组合探针相比域内探针AUC提升<0.02。
- **转向结果**：
  - Gemma：域内和迁移转向均成功提高谄媚率（高R²、正斜率），余弦相似度+0.68。
  - Llama：域内转向效果弱（低R²、近零斜率），迁移转向降低谄媚率（负斜率），余弦相似度-0.15。
- **LDA可视化**：Gemma中两类激活高度重叠；Llama中沿第一主成分分离更明显。

### 值得关注点
- 揭示了不同LLM对谄媚子类的内部表征结构差异（统一 vs. 分离），表明谄媚并非单一行为。
- 转向实验中的因果干扰现象（Llama中迁移转向降低谄媚率）表明表征可能相互冲突。
- 组合探针未提升域内性能，说明各子类的域内表征已捕获其完整判别结构。
- 该双分离方法可推广至其他复杂行为（如幻觉、角色扮演）的表征分解研究。

### 局限性
- **虚假特征控制**：尽管控制了对话主题、人称、提问存在性、回推措辞、轮数等潜在混杂因素，但数据集仍可能存在与事实/观点谄媚无关的细微差异，导致转向实验中因果关系较弱。
- **转向实验**：在Llama上域内转向效果不理想，需更多工作提取更具因果代表性的转向向量。
- **通用性有限**：仅测试了两个模型和两种子类，结论可能不适用于其他模型或更细的谄媚分类。

## 6. LLMs Silently Correct African American English: Auditing and Mitigating Dialect Bias via Activation Steering

- Source: arxiv
- arXiv ID: 2607.06845
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.06845v1
- PDF: https://arxiv.org/pdf/2607.06845v1
- DOI: https://doi.org/10.48550/arXiv.2607.06845

### Authors

Huan Wu, Ali Emami, Muhammad Furquan Hassan, Osaretin Igbinoba, Osakpolor Idusuyi, Osamede Igbinoba, Faiza Khan Khattak, Laleh Seyyed-Kalantari

### Abstract

African American English (AAE), a rule-governed dialect spoken by over 30 million people, is routinely misinterpreted and "corrected" by large language models (LLMs). Across six instruction-tuned LLMs (14B to 70B), we show that state-of-the-art models systematically prefer Standard American English (SAE) continuations even when the preceding context is in AAE, effectively rewriting AAE into SAE. We present an end-to-end framework to audit and mitigate this bias. For auditing, we introduce conditional Dialect Group Invariance (cDGI), which isolates true model bias from translator-induced artifacts, and a feature-level localization analysis that identifies which AAE markers most strongly trigger bias; we find that syntactic constructions, especially negative concord (e.g., "ain't nobody"), are universal triggers across all models. For mitigation, we introduce, to our knowledge, the first application of activation steering to dialect bias: a training-free, test-time method that extracts dialect directions via causal tracing and injects them into bias-relevant layers. Activation steering reduces bias 5 to 20 times more than prompting while preserving SAE fluency. To enable this work, we release REAL-AAE , the largest real-AAE parallel corpus to date: 17,479 AAE/SAE/ AAE_back triplets from natural tweets (2 to 6 times larger than prior real-AAE resources), validated automatically (BERTScore F1 = 0.95) and by three native AAE speakers (83.0% semantic agreement).

### 中文一句话结论
大型语言模型（LLM）会系统性地将非洲裔美国人英语（AAE）改写为标准美式英语（SAE），本文提出的激活引导方法在无需训练的条件下将这种方言偏见降低至提示方法的5–20倍。

### English TL;DR
This paper introduces an end-to-end framework to audit and mitigate dialect bias in large language models (LLMs) that silently "correct" African American English (AAE) into Standard American English (SAE), using a new large-scale AAE corpus (REAL-AAE) and a novel training-free activation steering method that reduces bias 5–20 times more than prompting while preserving SAE fluency.

### 中文详细总结
本文揭示了六种指令微调大语言模型（14B–70B）在AAE语境下依然偏好SAE续写的系统性偏差，即“方言偏好偏见”。作者构建了一个端到端的审计与缓解框架：
- **审计**：提出条件方言群不变性（cDGI）指标，隔离模型真实偏见与翻译伪影；通过特征级定位分析发现，句法结构（尤其是否定一致，如“ain't nobody”）是所有模型共有的最强偏见触发点。
- **缓解**：首次将激活引导应用于方言去偏，该训练时自由的方法通过因果追踪提取方言方向，并在推理时注入到相关层。实验表明，该方法将偏见降低到提示方法的5–20倍，且不损害SAE流畅度。
为支持研究，作者发布了目前最大的真实AAE平行语料库REAL-AAE（17,479个AAE/SAE/AAE_back三元组），经自动（BERTScore F1=0.95）和三位母语者评估（83.0%语义一致）验证。

### 方法 / 贡献
1. **REAL-AAE语料库**：基于真实AAE推文构建，规模为先前真实AAE资源的2–6倍，包含AAE→SAE翻译和SAE→AAE回译的三元组，经自动与人工验证。
2. **cDGI审计指标**：控制翻译伪影，纯化模型方言偏见的测量。
3. **特征级定位分析**：识别导致偏见的关键AAE语言标记（如否定一致、省略、词汇标记）。
4. **激活引导去偏**：无需训练、推理时干预，首次将因果追踪与激活方向注入用于方言偏见的缓解，在六种模型上验证有效。

### 实验或数据
- **模型**：6种指令微调LLM，参数14B–70B（包括Llama、Mistral、Qwen等系列）。
- **数据集**：REAL-AAE，17,479个三元组，来源为TwitterAAE语料库，自动过滤后经Gemini-3-flash翻译与回译，并经过自动评分与3名母语者人工抽检。
- **任务**：判别一致性（cDGI）与生成偏好（困惑度、对数概率、强制选择续写）。
- **结果**：所有模型在AAE语境下偏好SAE续写；激活引导使偏见降低5–20倍（相比基线提示），且SAE流畅度保持。

### 值得关注点
- **首次将激活引导应用于方言偏见**，提供了一种无需重新训练、可部署的缓解方案。
- **REAL-AAE为目前最大真实AAE平行语料库**，填补了合成语料与实际表现差距的缺口。
- **cDGI指标**创新性地分离了翻译伪影，使模型偏见测量更准确。
- **句法结构（尤其否定一致）成为通用偏见触发点**的发现，为未来语言学驱动的去偏提供了明确方向。

### 局限性
论文未在摘要和预览内容中明确讨论自身局限性，但可推知：
- 数据集仅来源Twitter平台，可能无法完全代表AAE在其他场景或地区的变体。
- 激活引导方法仅在六种指令微调模型上测试，对更广泛模型（如纯基座模型、不同架构）的泛化性尚未验证。
- 引导方向基于因果追踪的特定层，可能对模型结构选择敏感，且未探索层选择优化的上限。
- 缓解效果以偏见降低倍数度量，但未在真实下游任务（如情感分析、医疗问答）中验证实际公平性提升。

## 7. Co-LMLM: Continuous-Query Limited Memory Language Models

- Source: arxiv
- arXiv ID: 2607.07707
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.07707v1
- PDF: https://arxiv.org/pdf/2607.07707v1
- DOI: https://doi.org/10.48550/arXiv.2607.07707

### Authors

Yair Feldman, Linxi Zhao, Nathan Godey, Dongyoung Go, Yilun Hua, Kilian Q. Weinberger, Jennifer J. Sun, Yoav Artzi

### Abstract

Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM), where the KB pairs continuous keys with textual knowledge values, a significant departure from prior reliance on relational KB and queries. CO-LMLM generates flexible vector queries at minimal cost, while still integrating human-readable and attributable retrieved knowledge into its generation. We pair this design with an annotation pipeline that tags free-form factual spans in arbitrary text, removing prior work's restriction to Wikipedia. Across pretraining on Wikipedia and FineWeb-Edu and at multiple model scales, CO-LMLM outperforms prior LMLMs and vanilla LLMs in both perplexity and factual precision. At 360M scale, this includes lower perplexity than models pretrained on 40x more data, and SimpleQA-verified performance that is in line with gpt-4o-mini and higher than Claude Sonnet 4.5.

### 中文一句话结论
Co-LMLM 通过连续向量查询和自由文本知识库，在预训练中实现知识外化，显著降低困惑度并提升事实准确性，达到与更大模型相当的性能。

### English TL;DR
Co-LMLM introduces continuous-query limited memory language models (LMLMs) that use a knowledge base (KB) pairing continuous keys with textual values. This design generates flexible vector queries at minimal cost, integrates human-readable and attributable retrieved knowledge, and is paired with an annotation pipeline that tags free-form factual spans in arbitrary text, removing prior restrictions to Wikipedia. Across pretraining on Wikipedia and FineWeb-Edu at multiple scales, Co-LMLM outperforms prior LMLMs and vanilla LLMs in both perplexity and factual precision. At 360M scale, it achieves lower perplexity than models pretrained on 40× more data and SimpleQA-verified performance in line with gpt-4o-mini, surpassing Claude Sonnet 4.5.

### 中文详细总结
Co-LMLM 是一种连续查询的有限记忆语言模型。它将事实知识外化到知识库（KB）中，KB 采用连续键（continuous keys）与文本值（textual knowledge values）的配对方式，替代了先前关系型 KB 和查询的做法。模型在生成时以单个向量作为查询，成本极低，同时仍能整合人类可读且可归因的检索知识。该方法配合一个注释管道，可在任意文本中标记自由形式的事实跨度，不再限于维基百科。在 Wikipedia 和 FineWeb-Edu 上进行预训练，并在多个模型规模（包括 135M、360M 和 1.7B）下评估，Co-LMLM 在困惑度和事实精确度上均优于先前的 LMLM 和普通 LLM。特别地，在 360M 规模下，其困惑度低于使用 40 倍数据训练的模型；SimpleQA 验证的事实性得分与 gpt-4o-mini 相当，高于 Claude Sonnet 4.5。同时，Co-LMLM 保留了 LMLM 的知识可控性优势：外部记忆可编辑，支持直接遗忘操作。

### 方法 / 贡献
- **方法**：采用解码器仅 Transformer 架构，同时作为语言模型和密集检索器。知识库存储连续向量键和字符串值。训练时联合优化语言建模和检索，通过预处理数据模拟检索过程，使用对比损失（InfoNCE）对齐查询向量与事实跨度表示。查询向量直接从模型隐藏状态生成，无需解码多 token 文本查询。
- **贡献**：1) 提出连续查询 LMLM，克服先前关系型 LMLM 的表达限制，允许外化任意自由文本事实；2) 设计通用注释管道，可从任意文本中自动标注事实跨度，摆脱维基百科限制；3) 在困惑度和事实精确度上显著优于基线，且保持 NLU 性能；4) 实现低开销检索（单向量生成）和知识可控性（可编辑、可遗忘）。

### 实验或数据
- **数据**：预训练使用 Wikipedia 和 FineWeb-Edu 语料。
- **模型规模**：135M、360M、1.7B 参数。
- **基线**：对比 Rel‑LMLM（关系型 LMLM）和标准 LLM（同规模、同数据训练），以及开源模型（如 HF/SmolLM2）。
- **评估指标**：困惑度（perplexity）、事实精确度（factual precision）、下游 NLU 性能；使用 SimpleQA 验证事实性。
- **结果**：各规模下 Co-LMLM 困惑度和事实精确度均优于基线；360M 模型困惑度低于 40 倍数据训练的 HF/SmolLM2，SimpleQA 得分与 gpt-4o-mini 相当，高于 Claude Sonnet 4.5。

### 值得关注点
1. 连续查询仅需一个向量生成步骤，检索成本极低，不增加额外 token 解码开销。
2. 不再受限于关系型事实（subject‑relation‑object），可外化任意自由文本事实。
3. 360M 模型在困惑度上超越训练数据多 40 倍的模型，展示了知识外化的效率。
4. SimpleQA 事实性达到前沿水平（接近 gpt-4o-mini，超过 Claude Sonnet 4.5），证明小型模型也可获得高事实性。
5. 知识库可编辑、可遗忘，支持灵活的知识控制，这是常规 LLM 难以实现的。

### 局限性
根据提供的摘要和介绍，Co-LMLM 克服了先前 LMLM 在关系型表示、维基百科依赖和查询开销上的局限，但本文摘要未明确讨论其自身的局限性。潜在挑战可能包括连续键与文本值对齐的稳健性、检索规模扩展时的效率、以及对比学习对负样本构建的敏感性，但这些均未在给定材料中证实或讨论。

## 8. When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven Reasoning

- Source: arxiv
- arXiv ID: 2607.06720
- Relevance: 3.9

### Links

- Abstract: http://arxiv.org/abs/2607.06720v1
- PDF: https://arxiv.org/pdf/2607.06720v1
- DOI: https://doi.org/10.48550/arXiv.2607.06720

### Authors

Yotam Wolf, Noam Wies, Amnon Shashua

### Abstract

Training large language models (LLMs) with extended reasoning has enabled in-context search, in which models iteratively generate, critique, and revise solution attempts. We provide a theoretical analysis of in-context search by modeling it as approximate inference over reasoning traces, where the base model defines a prior and self-reflection provides feedback for posterior updates, and study the resulting inference-time sampling complexity - the number of sequential attempts needed to achieve high success probability. We show that when reflections reliably localize early mistakes, in-context search can yield exponential improvements over the base model, solving problems with exponentially small zero-shot pass rates using only a polynomial number of sequential attempts, whereas when this property fails, conditioning on past attempts offers no asymptotic benefit over parallel sampling. We further show that these gains are robust and learnable: approximate posterior updates suffice, and cross-entropy training on search rollouts recovers the required behavior with polynomial sample complexity. Finally, we show that under a stagewise abstraction of reinforcement learning with verifiable rewards, the optimal policy extension implements the same posterior reweighting rule. We validate key qualitative predictions of the theory on real large reasoning models.

### 中文一句话结论
本文通过采样复杂度理论证明，当自反思能够可靠定位早期错误时，上下文搜索相比并行采样可实现指数级改进，否则无渐近优势。

### English TL;DR
This paper provides a theoretical analysis showing that in-context search can yield exponential improvements over parallel sampling when self-reflection reliably localizes early mistakes, but offers no asymptotic benefit when this property fails.

### 中文详细总结
本文对大型语言模型中的上下文搜索（in-context search）进行了理论分析，将其建模为推理轨迹上的近似推断过程：基础模型定义先验，自反思提供反馈，通过条件更新实现后验重加权。研究表明，当反思能可靠定位早期错误时，上下文搜索可用多项式次数的顺序尝试解决零样本通过率呈指数衰减的问题，获得指数级改进；若该性质不成立，则条件化于历史尝试无渐近优势。此外，近似后验更新足以保持增益，且基于搜索轨迹的交叉熵训练能以多项式样本复杂度恢复所需行为。在可验证奖励的强化学习（RLVR）抽象下，最优策略扩展也实现了相同的后验重加权规则。实验在合成推理轨迹和AIME 2025数据集上验证了关键定性预测。

### 方法 / 贡献
- 将上下文搜索建模为近似推断，明确先验（基础模型）、反馈（反思）和后验更新（上下文条件化）的角色。
- 刻画反思定位早期错误的能力与采样复杂度之间的关系：可靠定位时指数级改进，否则无渐近优势。
- 证明后验更新机制的鲁棒性（近似更新有效）和可学习性（交叉熵训练多项式样本复杂度）。
- 在RLVR的阶段性抽象下，证明最优策略扩展等价于后验重加权。

### 实验或数据
- 合成推理轨迹：注入错误，测试模型定位最早错误步骤的能力。
- AIME 2025数据集：分析真实大型推理模型的前缀条件通过率，观察成功/失败轨迹的分布特性。

### 值得关注点
- 揭示了反思定位早期错误是上下文搜索效率的关键，而非简单排除完整错误轨迹。
- 理论结果与RLVR训练中涌现的搜索行为一致，提供了机制解释。
- 实验表明成功轨迹的通过率上升，失败轨迹低且振荡，符合推断式重分配而非单调计算。

### 局限性
论文未明确讨论局限性，但理论结果依赖于若干假设：反思可可靠定位早期错误（需一定重复暴露）、上下文可达性（避免从已标记错误的前缀继续生成）等，这些假设在真实场景中可能不总能满足。

## 9. Riemannian Geometry for Pre-trained Language Model Embeddings

- Source: arxiv
- arXiv ID: 2607.07047
- Relevance: 3.9

### Links

- Abstract: http://arxiv.org/abs/2607.07047v1
- PDF: https://arxiv.org/pdf/2607.07047v1
- DOI: https://doi.org/10.48550/arXiv.2607.07047

### Authors

Szczepan Konior, Alexandre Quemy, Przemysław Klocek, Grégoire Cattan, Bartłomiej Sobieski

### Abstract

Understanding the geometric structure of pre-trained language model embeddings matters for interpretability and safety. We ask whether sentence-level classification signal lives in the Riemannian geometry of contextual token embeddings, and probe it by extracting per-token pullback metrics from a learned encoder's analytical Jacobian and aggregating them with the Fréchet mean on the symmetric positive definite (SPD) manifold; we call this procedure Riemannian Mean Pooling (RMP). Across three datasets with non-trivial linguistic structure (CoLA, CREAK, RTE), RMP outperforms Euclidean mean pooling, while on FEVER-Symmetric, a benchmark constructed to remove annotation-driven lexical artifacts, the method correctly stays at chance. Ablations show that a randomly initialised encoder combined with Fréchet aggregation already beats Euclidean pooling on two of the three signal-bearing datasets, localising the source of the gain to the geometric aggregation rather than to learned manifold structure; the trained encoder contributes additional signal specifically on CREAK, the most knowledge-heavy of the three signal-bearing datasets.

### 中文一句话结论
本文提出黎曼平均池化（RMP），利用编码器雅可比矩阵的拉回度量在对称正定流形上通过Fréchet均值聚合token嵌入，在三个有信号的数据集上优于欧几里得均值池化，并在人工消偏基准上正确维持随机水平。

### English TL;DR
Riemannian Mean Pooling (RMP) aggregates token embeddings via Fréchet mean on the SPD manifold using pullback metrics from an encoder's Jacobian, outperforming Euclidean mean pooling on three sentence-level classification tasks, with ablations showing that the geometric aggregation itself—rather than learned manifold structure—drives the improvement.

### 中文详细总结
该文探究句级分类信号是否存在于上下文token嵌入的黎曼几何中。方法：首先从预训练语言模型（BERT-base-uncased）第9层提取每个token的768维嵌入；然后通过一个可微编码器（采用内在格林学习IGL）的解析雅可比矩阵计算每个token的拉回度量，得到一个对称正定（SPD）矩阵；接着在SPD流形上通过Fréchet均值聚合所有token的度量矩阵作为句子级表示；最后在均值点处的切空间内进行分类。在四个二分类数据集上测试：CoLA（语法可接受性）、CREAK（常识推理）、RTE（文本蕴含）作为有信号数据集，FEVER-Symmetric作为消偏负控制。实验表明RMP在三个有信号数据集上一致优于欧几里得均值池化（线性探针基线），在FEVER-Symmetric上正确保持随机水平。消融实验发现：即使使用随机初始化的编码器结合Fréchet聚合，也能在两个有信号数据集上超过欧几里得池化，说明性能提升主要来自几何聚合操作本身；而经过训练的编码器仅在知识密集的CREAK数据集上额外贡献了信号。

### 方法 / 贡献
- **方法**：提出黎曼平均池化（RMP）流程：从可微编码器的雅可比矩阵提取每个token的拉回度量，在SPD流形上使用Fréchet均值聚合这些度量矩阵，然后在总体黎曼均值点的切空间中进行分类。编码器采用内在格林学习（IGL），通过逆偏微分方程目标学习低维流形表示，其封闭形式核读出迫使编码器坐标与数据流形的光滑结构对齐。
- **贡献**：
  - 实例化了一个从编码器雅可比矩阵提取拉回度量、在SPD流形上聚合、在切空间分类的完整流程。
  - 在三个有信号数据集（RTE、CoLA、CREAK）上，黎曼聚合一致优于相同嵌入上的欧几里得均值池化；在负控制数据集FEVER-Symmetric上正确保持随机水平。
  - 消融实验定位到性能提升主要来自几何聚合本身而非学习到的流形结构；训练后的编码器仅在知识最密集的CREAK上提供额外信号。

### 实验或数据
- **数据集**：四个二分类基准：FEVER-Symmetric（316条事实验证，消偏负控制）、RTE（2490条蕴含对）、CoLA（3000句语法可接受性）、CREAK（3000句常识推理）。
- **基础模型**：BERT-base-uncased第9层token嵌入（768维）。
- **基线**：线性探针（欧几里得均值池化+逻辑回归）。
- **RMP设置**：编码器为MLP（输出维度d_max=64，K=128锚点，4个高斯尺度），通过IGL训练；聚合采用SPD流形上的Fréchet均值；分类在切空间使用逻辑回归。
- **关键结果**：
  - RMP在CoLA、CREAK、RTE上准确率均高于欧几里得基线（具体数值需见论文全文，摘要未给出确切数字）。
  - FEVER-Symmetric上RMP与随机水平一致，表明方法不依赖词表伪影。
  - 消融：随机编码器+Fréchet聚合在CoLA和RTE上已超过欧几里得基线；训练后编码器在CREAK上进一步改善。

### 值得关注点
- **几何聚合而非学习驱动**：消融实验清晰表明性能提升主要来自SPD流形上的Fréchet均值聚合操作，而非编码器学习到的流形结构，这不同于许多端到端几何深度学习方法。
- **负控制验证**：利用FEVER-Symmetric（消去词汇伪影）证明RMP不会在无真实信号的数据上产生虚假提升，增强了结果的可靠性。
- **跨数据集一致性**：在语法、常识、蕴含三种不同语言任务上一致优于欧几里得基线，说明方法具有一定的通用性。
- **可解释性**：通过拉回度量直接访问每个token的局部几何结构，为理解预训练语言模型中句级信号的分布提供了新视角。

### 局限性
- 仅测试了句子级二分类任务，尚未在序列标注、生成或多分类任务上验证。
- 编码器依赖IGL框架，其训练稳定性和泛化能力可能受超参数（如锚点数量、核尺度）影响。
- SPD流形上的Fréchet均值计算涉及迭代优化，相比于简单的算术平均计算开销更大，可能限制在大规模或实时场景中的应用。
- 实验仅基于BERT-base-uncased，未检验其他预训练模型（如RoBERTa、GPT系列）的可迁移性。
- 未提供在更大规模数据集（如GLUE全部任务）上的结果，小数据集上的优势是否能扩展到复杂任务尚不明确。

## 10. MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning

- Source: arxiv
- arXiv ID: 2607.06974
- Relevance: 3.8

### Links

- Abstract: http://arxiv.org/abs/2607.06974v1
- PDF: https://arxiv.org/pdf/2607.06974v1
- DOI: https://doi.org/10.48550/arXiv.2607.06974

### Authors

Ruilin Tong, Dong Gong

### Abstract

Large language models (LLMs) increasingly improve their reasoning at test time via additional computation, yet most existing works treat each problem in isolation. When problems arrive sequentially, accumulating reusable experience across them can further improve performance. Existing memory-based methods either store whole-solution templates that generalize poorly to novel problems or use heuristic step-level selection that is not optimized for final-answer correctness. Learning selection policies requires large-scale training data and fixed action spaces, making such approaches unsuitable for test-time settings where memory expands incrementally and only limited supervision is available. We propose MILES (Modular Instruction Memory with LEarnable Selection for self-improving LLM reasoning), a framework that dynamically expands step-wise memory and applies correctness-optimized memory composition under realistic test-time constraints. MILES maintains modular memory units consisting of asymmetric pairs of sub-goal embeddings and sub-instructions, each associated with a learnable selection head. This memory structure enables a coarse-to-fine retrieval mechanism: The coarse level enables memory expansion and collects supervision for training selection heads from confident samples, while the fine stage applies learned selection heads to rerank coarse-level candidates and guide reasoning for uncertain samples. MILES consistently matches or outperforms prior methods while achieving superior accuracy-efficiency tradeoffs. Extensive experiments demonstrate its effectiveness, robustness, and transferability.

### 中文一句话结论
MILES提出了一种模块化指令记忆与可学习选择机制，使得大语言模型在测试时能通过积累和组合经验来自我改进推理能力，无需更新模型参数，在准确率与效率之间取得更好平衡。

### English TL;DR
MILES introduces a modular instruction memory with learnable selection heads that enables self-improving LLM reasoning at test time by dynamically composing step-wise reasoning modules from accumulated experience, achieving superior accuracy-efficiency tradeoffs.

### 中文详细总结
MILES是一种用于大语言模型（LLM）测试时推理自改进的框架。它维护一个模块化的记忆库，存储(子目标嵌入, 子指令)对，每个记忆单元关联一个可学习的选择头。采用粗到细的检索机制：第一层基于子目标相似度进行粗检索，用于记忆扩展和从可信样本中收集选择头的训练监督；第二层利用学习到的选择头对粗检索候选进行重排序，并指导不确定样本的推理。MILES在无需参数更新、外部监督或固定动作空间的情况下，实现了自我改进的逐步记忆组合。实验表明，MILES在六个推理基准和四个骨干模型上一致匹配或超越先前方法，并在准确率-效率权衡上表现更优。

### 方法 / 贡献
- 提出MILES框架，实现测试时自改进的逐步记忆组合，无需参数更新、外部监督或固定动作空间。
- 设计模块化非对称记忆结构：(子目标嵌入, 子指令)对，每个单元附带可学习选择头，支持粗到细的检索机制。
- 实现可学习记忆组合：从可信样本的展开结果中训练轻量级每单元选择头，在有限测试数据下实现自监督且正确性优化的记忆组合。
- 实证验证：在六个推理基准和四个骨干模型上一致匹配或超越基线方法，同时实现更优的准确率-效率权衡。

### 实验或数据
论文在六个推理基准（如GSM8K、MATH等，具体数据集未在摘要中明确列出，但贡献部分提及六个基准和四个骨干模型）上进行了实验，使用了四个不同的骨干LLM。实验验证了MILES的有效性、鲁棒性和可迁移性。

### 值得关注点
- 无需更新模型参数，适用于冻结或封闭的LLM。
- 记忆单元可增量扩展，新单元和选择头可添加而不需重新训练现有组件。
- 粗到细的检索机制结合了相似度检索和学习到的选择，优化了最终答案的正确性。
- 在准确率-效率权衡上优于先前方法。

### 局限性
- 需要依赖可信样本的推理轨迹来训练选择头，对于噪声较大的样本可能效果受限。
- 记忆单元的构建依赖于LLM生成的步骤目标和聚类，可能引入额外误差。
- 实验部分未详细说明不同基准上的具体性能数字（摘要中未提供），但论文正文中有详细结果。
- 方法可能依赖于较强的嵌入模型和LLM，对基座模型能力有一定要求。

## Processing Notes

- Duplicate papers skipped: 0