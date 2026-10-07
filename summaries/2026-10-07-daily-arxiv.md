# Daily arXiv - 2026-10-07

- Source: GitHub Actions generated paper list
- Generated at: 2026-10-07T03:02:24
- Paper count: 10

## 1. ImproveAnyTask: An Autonomous Post-Training Harness for Iterative Model Self-Improvement

- Source: arxiv
- arXiv ID: 2610.06347
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2610.06347v1
- PDF: https://arxiv.org/pdf/2610.06347v1
- DOI: https://doi.org/10.48550/arXiv.2610.06347

### Authors

Xingbo Yao, Xiaoman Wang, Zhengwu Lei, Tinghui Luo, YiLin Zhang, Yuefeng Wu, Yijie Xu, Tianfu Wang, Qingyuan Zhan, Ye Guo, Daoxin Zhang, Zhe Xu, Jian Liu, Hui Xiong

### Abstract

Adapting general-purpose large language models to specific tasks requires substantial human effort in designing data and training strategies. Sustaining improvement is especially challenging because model updates change the error distribution, requiring strategies to be continually refined. We introduce ImproveAnyTask, an autonomous post-training harness that improves task performance under a limited compute budget. Drawing inspiration from gradient-based parameter optimization, the harness organizes adaptation into error attribution, update-direction selection, and executable model updates. It combines metric-level and case-level analysis to identify a focal problem, then investigates research-backed strategies and compares their reported gains and reproduction difficulty. The selected strategy is translated into training data and a training configuration, with small-scale execution checks preceding full post-training. Subsequent evaluation guides model selection and further adaptation, while validated strategies and scripts are retained for reuse. Across 11 tasks, ImproveAnyTask achieves mean gains of 18.29 and 11.97 percentage points on the Base and Instruct models, respectively, with a maximum gain of 41.96 points, under a 24-hour budget with resources equivalent to eight H20 GPUs.

### 中文一句话结论
ImproveAnyTask 是一种自动化后训练流程，能在有限计算预算下通过迭代错误分析与策略选择，显著提升大语言模型在多种任务上的性能。

### English TL;DR
ImproveAnyTask is an autonomous post-training harness that iteratively improves large language models on specific tasks by diagnosing errors, selecting research-backed strategies, and executing model updates under a limited compute budget, achieving substantial gains across 11 tasks.

### 中文详细总结
将通用大语言模型适配到特定任务通常需要大量人力设计数据和训练策略，且模型更新后错误分布会变化，持续改进困难。受梯度参数优化的启发，ImproveAnyTask 将适配过程组织为错误归因、更新方向选择和可执行模型更新三个环节。它结合指标级和案例级分析定位关键问题，然后调研研究支持的策略并比较其报告收益和复现难度。选定策略后被转化为训练数据和配置，先进行小规模执行检查，再进行完整后训练。后续评估用于模型选择与进一步适配，已验证的策略和脚本可复用。在11个任务上，Base模型平均提升18.29个百分点，Instruct模型平均提升11.97个百分点，最大提升达41.96个百分点，预算为24小时、资源相当于8块H20 GPU。

### 方法 / 贡献
- 提出自动化后训练流程ImproveAnyTask，模仿梯度优化将适配分解为错误归因、更新方向选择和执行模型更新。
- 结合指标级和案例级分析定位问题，并从研究文献中自动选择策略（考虑收益和复现难度）。
- 策略自动转化为训练数据和配置，包含小规模预检查，确保可行性；后续评估指导模型选择与迭代。
- 验证的策略和脚本可保存复用，减少重复劳动。
- 在有限预算（24小时，8×H20 GPU）下实现显著性能提升。

### 实验或数据
实验未列出具体数据集名称。在11个任务上测试了Base和Instruct两种模型。Base模型平均提升18.29个百分点，Instruct模型平均提升11.97个百分点，最大提升41.96个百分点。实验预算为24小时，使用与8块H20 GPU相当的计算资源。

### 值得关注点
- 全流程自动化，无需人工设计数据和策略。
- 受梯度优化启发，结构清晰，可解释性强。
- 在有限计算预算下获得显著性能增益（最高提升42个百分点）。
- 策略选择和复现难度权衡机制，提高实用性与可行性。
- 已验证策略和脚本可复用，支持持续改进。

### 局限性
摘要未提及明显局限性。可能包括：对初始模型质量存在依赖；策略库覆盖有限；各任务增益差异大（最大42点，平均约18/12点）；计算预算（24小时/8 GPU）仍可能对更大规模任务构成限制；未讨论跨任务泛化或灾难性遗忘等问题。具体需参考全文。

## 2. Fine-Grained Emotion Classification from Mobile App Reviews: An Empirical Study with Large Language Models

- Source: arxiv
- arXiv ID: 2610.03802
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2610.03802v1
- PDF: https://arxiv.org/pdf/2610.03802v1
- DOI: https://doi.org/10.48550/arXiv.2610.03802

### Authors

Quim Motger, Carlota Catot, Marc Oriol

### Abstract

Context: Fine-grained emotion classification of mobile app reviews enables requirements engineering activities that go beyond polarity-based opinion mining, including emotionally informed issue prioritisation and feature-oriented feedback analysis. However, automatic fine-grained emotion extraction from app reviews remains understudied. Objectives: Building on a previously published annotation framework and human-labelled ground truth adapted from Plutchik's taxonomy, this paper investigates how large language models can be leveraged for automatic multi-label emotion classification under severe class imbalance. Methods: We compare encoder-only fine-tuning under multi-label and binary-ensemble formulations, decoder-only zero- and few-shot prompting across open-source and proprietary models, and a catalogue of imbalance mitigation strategies (loss reweighting, resampling, generative data augmentation), with the synthetic-review generator and prompting strategy selected via an intrinsic augmentation-utility ranking. Results: Fine-tuned encoders trail the best decoder-only few-shot prompting (macro-F1 0.642) by a wide margin at baseline (multi-label: 0.387; binary ensemble: 0.450); pairing the best multi-label encoder with generative data augmentation and positive-weighted loss closes most of this gap (+0.204) at up to three orders of magnitude lower inference latency than the decoders, with the largest gains on the rarest emotions, from undetected to gains of up to +0.501 F1. Conclusion: Large language models make fine-grained, multi-label emotion classification of app reviews feasible for requirements engineering pipelines, with modest macro-F1, and the best formulation and mitigation strategy are backbone- and formulation-dependent. We release the experimental pipeline, synthetic corpora, and fine-tuned checkpoints for replication and reuse.

### 中文一句话结论
大型语言模型使细粒度多标签情感分类可行，但宏F1中等，最佳方法（微调编码器与少样本提示）及不平衡缓解策略取决于具体模型和任务设定。

### English TL;DR
Large language models make fine-grained, multi-label emotion classification of app reviews feasible for requirements engineering pipelines, with modest macro-F1, and the best formulation and mitigation strategy are backbone- and formulation-dependent.

### 中文详细总结
本文研究如何利用大型语言模型（LLM）对移动应用评论进行细粒度多标签情感分类（基于Plutchik八种基本情绪+中性）。由于类别严重不平衡（如“快乐”频繁而“恐惧”罕见），作者系统比较了三种路径：(1) 编码器微调（多标签和二元集成形式）；(2) 解码器零样本与少样本提示；(3) 多种不平衡缓解策略（损失加权、重采样、生成式数据增强）。结果表明：纯解码器少样本提示基线最优（宏F1=0.642），但编码器基线（0.387/0.450）通过生成式数据增强和正类加权损失可将差距缩小至+0.204，且推理延迟低三个数量级。最好结果依赖于具体骨干模型和设定。实验还通过内在效用排序筛选生成器与提示策略。

### 方法 / 贡献
- 对比编码器微调（多标签/二元集成）与解码器提示（零样本/少样本）两种范式
- 系统评估四类不平衡缓解策略：损失重加权、重采样、生成式数据增强、及基于内在多样性/新颖性/保真度的增强排序
- 发布扩展数据集（3308条标注文本：1090人工+2218合成）
- 开源实验流程、合成语料与微调检查点

### 实验或数据
使用此前发布的人类标注数据集（1090条句子，来自257个应用的10个Google Play类别），在此基础上生成2218条合成评论，总计3308条多标签数据。对比的编码器包括BERT、RoBERTa、DistilBERT、DeBERTa、XLNet等；解码器涵盖开源（Llama系列等）和专有模型（GPT-3.5等）。评估指标为宏F1。

### 值得关注点
- 生成式数据增强对最稀有情感（如Fear）提升显著（最高+0.501 F1，从零检测到可观）
- 微调编码器 + 数据增强 + 正类加权损失，性能接近少样本提示，但推理速度低三个数量级，更适合实时管道
- 所有结果的最佳配置均依赖具体骨干和设定，无单一通用方案

### 局限性
- 最终宏F1仅0.642（最佳对齐方案），性能仍有提升空间
- 数据集以英语单句为单位，未覆盖其他语言或多句评论
- 合成数据质量依赖生成模型，可能有语义偏差
- 实验仅针对特定情感分类体系（Plutchik八类+中性），其他体系需重新评估

## 3. Boundaries Agree, Labels Do Not: Intra-Annotator Dynamics as a Kind of Training Data

- Source: arxiv
- arXiv ID: 2610.04370
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2610.04370v1
- PDF: https://arxiv.org/pdf/2610.04370v1
- DOI: https://doi.org/10.48550/arXiv.2610.04370

### Authors

Marharyta Shvets

### Abstract

Data quality now matters as much as compute for training language models. Much training data comes from human annotation of text, and interpretive annotation has no ground truth that could settle what is "accurate". Two lines of work respond to this. One combines annotators into a "ground truth" and measures how well they agree with each other; the other treats their disagreement as a signal. Both compare different people at one point in time. We measure something else: how well one reader reproduces their own reading of the same text over time. One expert human reader and three LLM families segmented three Sumerian myths and labelled the causal function of each segment with one of seven states. Across runs months apart, the human cut the text in much the same places but named the segments differently, in every myth. The models show no such consistent pattern: their gap between the two layers is positive in some myths and negative in others, and its size varies. The human's label changes are not random: the runs go through much the same functions but start them one step apart, while model runs start them at the same places. We argue that this pattern is a usable measure of data quality and a contamination check: a "human" annotation whose labels are as stable as its boundaries, and whose functions start in sync, looks like a model's.

### 中文一句话结论
人文学者在相隔数月的重复注释中，分割文本的边界高度一致，但对各段的因果功能标记却常常改变，而三种LLM族无法复现这种“边界稳定、标签不稳”的模式，这种分离现象可用作训练数据质量与数据污染的检测指标。

### English TL;DR
An expert human annotator reproduces segment boundaries consistently over time but changes labels unpredictably—a pattern not replicated by LLMs—and the paper argues that this dissociation between boundary and label stability can serve as a measure of data quality and a contamination check for training data.

### 中文详细总结
论文通过一项新颖的实验发现：在注释性任务中，一位人文学者与三种大型语言模型（Claude Opus 4.8、Gemini Pro、Qwen 3.8 Max）分别对三部苏美尔神话进行因果功能分段与标注。人类注释者在相隔五到十个月的三次运行中，对同一文本的分割边界高度一致（Cohen's κ 值0.465–0.731），但各段的标签一致性却显著较低（κ 值0.168–0.291），形成稳定的“边界-标签分离”模式。相比之下，所有LLM家族的边界与标签一致性差距不一致，在不同文本中或正或负，且变化幅度不固定。人类标签的不稳定性并非随机：三次运行的标签序列顺序相近，但在时间上存在一个片段的位移（即同一功能开始的位置“错位一步”），而模型的不同运行倾向于在同一位置开始相同功能。论文论证这种分离模式可作为判断注释数据是否源自人类（而非LLM生成）的质量信号和污染检测工具。

### 方法 / 贡献
- **方法**：对比一位人类专家与三个LLM家族（每族10次运行）对三部苏美尔神话的重复注释。注释任务包含两层：文本分段边界和每段的七个因果功能状态。使用Cohen's κ 分别衡量边界和标签的自一致性，并设计四项指标（标签集中度B1、邻域许可翻转B2、相位偏移、可迁移语法）分析标签变化模式。
- **贡献**：首次系统性测量注释者跨时间的“内部一致性”，而非传统跨注释者一致性。发现“边界稳定、标签不稳定”是人类注释的独特特征，并提出该模式可作为训练数据质量检测和LLM污染识别的新指标，弥补了现有基于跨注释者一致性或分歧分析方法的不足。

### 实验或数据
- **数据**：三部苏美尔神话（Gudea Cylinders、Inanna's Descent、Inanna and Enki）的英文翻译，选自CDLI和ETCSL数据库。这些文本没有现成的分集传统或流行评论。
- **实验**：一位人类专家在5–10个月内对每部神话进行3次重复注释。Claude Opus 4.8、Gemini Pro和Qwen 3.8 Max各进行10次独立重复运行（默认设置，思维方式，新鲜会话，相同提示）。所有注释使用固定方案：七个因果功能状态（准备、接触、交换、分裂、协商、稳定、回归）。
- **结果**：人类边界κ值0.465–0.731，标签κ值0.168–0.291，边界-标签差距始终为正（+0.298至+0.452）。模型差距方向不一（-0.178至+0.291）。人类标签变化呈现一步相位偏移模式，而模型运行主要在同一位置启动相同功能。

### 值得关注点
1. 实验设计新颖：聚焦“时间维度上的同一人重复性”，而非传统跨注释者一致性，填补了评估注释数据质量的重要空白。
2. 方法严谨：通过使用苏美尔神话（缺乏现成注释传统，不易受记忆或训练数据污染）确保结果反映读者的认识逻辑而非外部知识。
3. 发现实用价值：边界-标签分离模式可作为简便的“人工注释真伪检测”，辅助识别可能由LLM生成并混入人类标注数据集的训练样本。
4. 相位偏移分析的探索性设计具有启发性：人类注释的变化并非随意，而是遵循“功能序列相同、时间位置错位”的规律，揭示了人类阅读认知的独特结构。
5. 公开所有注释数据和代码，促进可复现研究。

### 局限性
1. 仅涉及一名人类专家注释者，样本量极小，无法判断“边界稳定、标签不稳定”是否是人类注释的普遍特征，抑或仅为该特定注释者（也是方案设计者）的个人模式。
2. 人类与模型的运行间隔不对等：人类运行相隔数月，模型运行几乎同时进行。虽然作者论证分离模式（层间比较）不受此影响，但层间差距的大小难以直接对比。
3. 注释任务高度专业化（因果功能标注），可能不适用于更广泛的注释任务（如情感分析、命名实体识别等），领域迁移性未经验证。
4. LLM在“可迁移语法”指标上的表现及与人类对比未在摘要中充分报告，可能导致对人类和模型差异的理解不完整。
5. 相位偏移分析为事后的探索性分析，未在独立数据集上进行事前假设检验，存在多重比较和过拟合风险。

## 4. Usage-Modulated Sentiment Representations in Large Language Models

- Source: arxiv
- arXiv ID: 2610.05069
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2610.05069v1
- PDF: https://arxiv.org/pdf/2610.05069v1
- DOI: https://doi.org/10.48550/arXiv.2610.05069

### Authors

Hongfei Du, Jiacheng Shi, Yanfu Zhang, Gang Zhou, Ye Gao

### Abstract

Prior work suggests that sentiment can often be captured by approximately linear directions in LLM activation spaces, but a single direction may not fully capture sentiment representations. In natural communication, sentiment is shaped not only by polarity but also by usage factors, such as tone and audience adaptation. We test whether these factors systematically modulate sentiment representations beyond a shared sentiment direction. We construct a controlled paired dataset that holds event content fixed while varying sentiment polarity and usage factors, and analyze Llama, Mistral, and Gemma. We identify a shared sentiment direction, remove it, and test the residual structure through erasure and generation-time tone steering. Across models, the shared direction is robust (median cosine 0.953-0.975), yet removing it leaves 0.833-0.909 of the original positive-negative representation-difference norm. The residuals contain compact, reproducible usage-conditioned structure. Targeted erasure weakens held-out usage metrics more than random and label-shuffled controls. On Llama, outputs steered along residualized tone components are preferred in 92.8% of blind target-tone comparisons while preserving the requested sentiment polarity in 98.7% of evaluated outputs.

### 中文一句话结论  
LLM 的情感表示并非只由一个共享方向构成，还包含受语气和受众等使用因素调节的残差结构，且该结构可用于在保持情感极性的同时控制生成语气。

### English TL;DR  
LLMs represent sentiment not only via a shared linear direction but also through residual structure modulated by usage factors (tone, audience), which can be exploited for controlled generation while preserving polarity.

### 中文详细总结  
论文通过构建事件内容固定、情感极性和使用因素（语气、受众）变化的控制配对数据集，分析了 Llama、Mistral 和 Gemma 三个模型。首先识别出一个跨使用条件共享的情感方向（中位数余弦对齐 0.953–0.975），但去除该方向后，残差仍保留了正负表示差异范数的 83.3%–90.9%。残差中存在紧凑、可复现的、按使用条件组织的结构。通过残差擦除实验，发现针对使用方向的擦除比随机擦除更有效地削弱了使用指标；通过生成时语气引导实验，在 Llama 上，沿残差语气分量引导的输出在 92.8% 的盲比较中被优先选为目标语气，同时 98.7% 的输出保持了请求的情感极性。

### 方法 / 贡献  
1. 构建控制配对数据集：同一事件骨架在正负两种情感极性下，按不同语气（正式、随意、热情、克制）和受众（专家、公众、儿童、同伴）生成文本，固定事件内容。  
2. 分离共享情感方向与使用条件残差结构：跨模型证明共享方向稳健，但残差中存在系统性、可复现的使用相关结构。  
3. 干预验证：通过残差擦除削弱使用指标，并通过生成时语气引导实验证明残差结构可因果控制输出语气，同时保持情感极性。

### 实验或数据  
- **数据集**：GPT-4o 生成 300 个候选事件骨架，经筛选保留 221 个，每个骨架在 8 种使用值×2 种极性下实现，共 3,536 条文本。人工和 GPT-4o mini 盲验显示用法分配正确率 92.5%–100%，事件和情感保留率 92.5%–100%。  
- **模型**：Llama、Mistral、Gemma，分析 mean-pooled 和 last-token 两种池化方式。  
- **主要实验**：（1）共享方向对齐性、投影占比、残差范数比例；（2）使用解码边际（与标签打乱基线对比）；（3）残差擦除对使用指标的削弱效果；（4）Llama 上沿残差语气分量引导生成，盲比较目标语气偏好 92.8%，情感极性保持 98.7%。

### 值得关注点  
- 共享情感方向虽稳健但仅能解释部分表示变化，残差结构具有系统性且跨模型（Llama、Mistral、Gemma）一致，提示为 LLM 的通用特性。  
- 残差结构可直接用于受控生成：沿残差语气分量调节输出语气，同时几乎不损失情感极性（98.7% 保留）。  
- 方法创新：利用控制配对数据与残差分析，将使用因素从共享情感中分离出来，并通过干预验证其因果作用。

### 局限性  
- 数据集完全由 GPT-4o 生成，可能无法完全反映自然语言中的真实分布。  
- 仅测试了三个模型（Llama、Mistral、Gemma），结论的通用性需更多模型验证。  
- 语气和受众各仅取四个值，覆盖范围有限；其他使用因素（如礼貌、情感强度）未纳入。  
- 生成干预实验仅在 Llama 上进行，其他模型未评估生成时效果。  
- 论文摘要未明确讨论局限性，以上基于论文具体实验设置推断。

## 5. Representation-Space MMD for Diffusion Language Models

- Source: arxiv
- arXiv ID: 2610.06648
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2610.06648v1
- PDF: https://arxiv.org/pdf/2610.06648v1
- DOI: https://doi.org/10.48550/arXiv.2610.06648

### Authors

Ilya Drobyshevskiy, Ilia Sudakov, Maksim Semenov, Denis Kuznedelev, Maksim Ignatov, Pavel Temirchev, Nikita Balagansky, Viacheslav Meshchaninov, Nikita Gushchin, Dmitry Baranchuk

### Abstract

We introduce a post-training method for diffusion language models (DLMs) that minimizes Maximum Mean Discrepancy (MMD) between generated and reference distributions in the feature space of a frozen pretrained DLM. To estimate MMD, we retain contextual features at individual token positions, obtaining multiple observations per sequence from a single extractor pass. We optimize this objective using policy gradients for discrete models and direct differentiation through generated latents for continuous models. In both cases, computing the loss directly from these features enables efficient post-training without full sampling trajectories or jointly trained auxiliary models. Experiments show lower generative perplexity at comparable entropy on OpenWebText and better accuracy-computation trade-offs on GSM8K. On 16B DMax-LLaDA2.0 models with hybrid masked-uniform diffusion, we increase decoding parallelism with similar or higher accuracy on math and code benchmarks.

### 中文一句话结论
本文提出一种基于表示空间最大均值差异（MMD）的后训练方法，用于提升离散和连续扩散语言模型的生成质量与解码并行性。

### English TL;DR
We introduce a post-training method for diffusion language models that minimizes Maximum Mean Discrepancy (MMD) in the representation space of a frozen pretrained DLM, yielding lower perplexity, better accuracy–computation trade-offs, and improved decoding parallelism on large-scale models.

### 中文详细总结
该论文提出针对扩散语言模型（DLM）的后训练方法，通过在冻结预训练DLM的特征空间中最小化生成分布与参考分布之间的最大均值差异（MMD）来优化模型。对于离散DLM（如掩码扩散或混合掩码-均匀扩散），使用策略梯度（REINFORCE）优化MMD奖励；对于连续DLM（基于嵌入语言流ELF），通过生成潜在变量直接微分优化。方法利用单个特征提取器从每个序列中获取多个逐位置特征观测，从而高效估计MMD，无需完整采样轨迹或联合训练辅助模型。实验在OpenWebText、GSM8K及大型16B DMax-LLaDA2.0模型上验证，显示更低的困惑度、更好的准确率-计算量权衡以及更高的解码并行性。

### 方法 / 贡献
- 提出基于表示空间MMD的DLM后训练框架，适用于离散和连续两种模型。
- 离散模型实现（M-MMD）使用策略梯度，连续模型实现（C-MMD）使用直接微分。
- 利用冻结预训练DLM的逐位置上下文特征，从单个序列获取多个MMD观测。
- 无需完整采样轨迹或联合训练的辅助模型，计算高效。
- 在多个基准上实现更优性能，并在大规模模型上提升解码并行性。

### 实验或数据
- 语言建模：OpenWebText数据集，评估生成困惑度和熵。
- 数学推理：GSM8K数据集，评估准确率-计算量权衡。
- 大规模模型：16B参数DMax-LLaDA2.0（混合掩码-均匀扩散），在数学和代码基准上测试准确性及解码并行度。

### 值得关注点
- 使用预训练DLM自身的特征空间进行分布匹配，无需额外特征模型或判别器。
- 统一处理离散和连续两种DLM架构，方法简洁通用。
- 在大模型上同时提升准确性并增加解码并行性（减少采样步数）。

### 局限性
根据提供的摘要和引言节选，本文未明确讨论局限性。

## 6. Extracting Persona Subspaces Through Iterative Nullspace Projection For Modulation

- Source: arxiv
- arXiv ID: 2610.04676
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2610.04676v1
- PDF: https://arxiv.org/pdf/2610.04676v1
- DOI: https://doi.org/10.48550/arXiv.2610.04676

### Authors

Ananya Malik, Mai ElSherief

### Abstract

Large Language Models (LLMs) can adopt distinct personas to tune their semantics, expertise, and perspective to different users and tasks. Precise control over these traits is critical to ensure safety and reliability in model behavior. Existing methods like activation steering and prompt-based persona induction reduce a persona to a single dominant direction, missing the finer, nested traits that emerge only once that dominant signal is factored out. We introduce modulation as a setting where the persona context is already embedded in the content being manipulated, requiring control methods to amplify or suppress a trait already present rather than inject it from scratch. PaSS is an inference-time control paradigm that models personas as multi-dimensional subspaces in a model's latent space without supervised contrastive examples. The persona subspaces are extracted via iterative concept erasure and applied to modulate persona-guided generation without retraining. To extract this subspace, we use Iterative Nullspace Projections (INLP) to linearly and iteratively isolate persona-specific directions. We causally evaluate six personas against diverse tasks like MATH-500, TinyAlpaca, GSM8K, and IFEval, showing that discriminative, iterative subspace extraction captures diverse traits underlying a given persona, enabling stronger and larger modulation than single-direction additive methods, while maintaining content fidelity. We further study individual peeled directions within each subspace to uncover the distinct aspects of persona behavior they encode. Overall, we show that persona subspaces offer a controllable, interpretable, and generalizable framework for modulating LLM behavior without sacrificing task performance.

### 中文一句话结论
本工作提出 PaSS 方法，通过迭代零空间投影（INLP）在大语言模型隐空间中提取多维人设子空间，实现对已嵌入人设的细粒度调节，效果优于单方向激活引导。

### English TL;DR
PaSS is an inference-time method that extracts multi-dimensional persona subspaces from LLM latent spaces via iterative nullspace projections (INLP), enabling stronger, more controllable modulation of nested persona traits than single-direction steering, without sacrificing task performance.

### 中文详细总结
现有方法（如激活引导、基于提示的人设注入）将人设简化为单一主导方向，忽略了该方向被剥离后才会显现的更细致的嵌套特质。PaSS 模型将人设定义为隐空间中的多维子空间，在推理时通过迭代概念擦除（即 INLP）线性、迭代地隔离人设相关方向，提取该子空间。提取后，无需重新训练即可用于放大或抑制内容中已嵌入的人设特质。作者在 MATH-500、TinyAlpaca、GSM8K、IFEval 等多任务上，对六种人设进行因果评估，表明迭代子空间提取能捕捉人设下的多样特质，实现比单方向加法方法更强、更大的调节效果，同时保持内容忠实度。此外，子空间内各剥离方向对应不同的人设行为侧面，具有可解释性。

### 方法 / 贡献
- **方法**：PaSS（Persona Subspace Steering）——一种推理时控制范式。核心步骤：
  1. 通过 INLP 在 LLM 隐空间中对人设相关方向进行迭代线性消除，逐步构建多维人设子空间。
  2. 利用提取的子空间对已包含人设的生成内容进行放大或抑制（调节），无需重新训练。
- **贡献**：
  - 首次将人设建模为多维子空间，而非单一方向，捕捉嵌套、细粒度的特质。
  - 提出无需

## 7. Learning to Learn a Language

- Source: arxiv
- arXiv ID: 2610.05879
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2610.05879v1
- PDF: https://arxiv.org/pdf/2610.05879v1
- DOI: https://doi.org/10.48550/arXiv.2610.05879

### Authors

Lennart Carstens-Behrens, Holger Fröhlich

### Abstract

We present the Prior-Fitted Language Model (PFLM), a 300M-parameter byte-level transformer pretrained only on samples from a synthetic non-linguistic prior. Given a prefix of real text, it learns to predict the language in context with frozen weights, having never seen a word of any real language. Every training sequence is generated by a recurrent structural causal model drawn fresh from a distribution over such models. The model never sees the same language twice during training, so the only way to predict the continuation is to infer the language from the prefix. Samples from this prior share the statistical signatures of natural text: Zipfian frequencies, slow entropy-rate convergence, and long-range dependence. On Wikipedia in six languages, bits per byte fall from the uniform eight to between 0.9 and 2.4 at one million bytes of context. Given numerals instead of text, PFLM learns to count, to compare magnitudes, and to add approximately. It predicts deterministic sequences like Rudin-Shapiro or the prime indicator, and it compresses six non-text domains, from source code to speech, below gzip and PPMd. The model has not learned a language. It has learned to learn one.

### 中文一句话结论
本文提出了先验拟合语言模型（PFLM），该300M参数的字节级Transformer仅使用合成非语言先验数据进行预训练，在冻结权重的情况下，能够通过上下文推断并预测真实语言及其他结构化序列，实现了“学会学习语言”而非学习特定语言。

### English TL;DR
PFLM is a 300M-parameter byte-level transformer pretrained solely on samples from a synthetic non-linguistic prior. With frozen weights, it learns to predict natural languages and structured sequences in context by inferring the underlying generating "language" from the prefix, achieving bits per byte as low as 0.9–2.4 on Wikipedia text after one million bytes of context.

### 中文详细总结
该研究介绍了一种全新的语言模型预训练范式：PFLM完全在合成数据上训练，这些数据由随机生成的递归结构因果模型（SCM）产生，每个训练序列对应一个独立采样、不会重复的“合成语言”。模型从未接触过任何真实语言词汇，但在给定真实文本前缀时，它能通过推断生成该文本的潜在语言规则来预测后续内容，且权重保持不变。该模型在六种语言的Wikipedia数据上均展现出持续下降的每字节比特数，并具备计数、近似加法、预测确定序列（如Rudin-Shapiro序列、质数指示器）等能力，甚至能在多个非文本领域（如源代码、语音）超越gzip和PPMd压缩算法。

### 方法 / 贡献
- **核心方法**：构建一个基于递归SCM的合成语言先验，每个SCM由随机图结构、结构方程（六种函数族）、激活函数、更新频率和量化器组成，独立采样生成训练序列。
- **训练策略**：模型在大量不重复的合成语言样本上预训练，使其只能通过上下文推断语言，实现元学习（amortized Bayesian inference）。
- **主要贡献**：首次证明了仅用非语言合成先验训练的模型能预测自然语言，弥合了人类与机器在语言学习效率上的差距，为语言模型提供了关于“语言可能形态”的先验知识。

### 实验或数据
- **数据**：使用六种语言（英语、中文、印地语、阿拉伯语、日语、韩语）的Wikipedia文本（UTF-8编码）进行评估；另使用数字序列、确定序列（如Rudin-Shapiro、Kolakoski、质数指示器、π）以及六个非文本领域（源代码、语音等）。
- **实验结果**：在1百万字节上下文下，每字节比特数从均匀分布的8降至0.9–2.4；在确定序列上，Rudin-Shapiro的每符号比特数降至0.04，质数指示器为0.28；压缩性能在六个非文本领域均优于gzip和PPMd。

### 值得关注点
- **模型规模与效率**：仅300M参数，远小于现代大模型，却展现出强大的上下文学习能力，凸显先验设计的重要性。
- **跨域泛化**：同一模型不仅能处理自然语言，还能学习数字、确定性序列和多种非文本数据，显示通用学习机制。
- **理论洞见**：将语言学习视为贝叶斯推断，模型通过前缀后验分布集中来预测，为理解上下文学习提供新视角。

### 局限性
- **上下文长度依赖**：性能随上下文增长而提升，但达到最佳效果需长前缀（如1百万字节），实际应用中可能受限于计算资源。
- **评估范围**：尽管测试了多种语言和序列，但未提及对更复杂语言结构（如语义、语法深度）的评估。
- **抽象中未明确提及**：摘要和预览中未详细说明模型在噪声、长尾分布或非典型语言上的表现；具体训练计算成本、超参数敏感性等细节有待全文补充。

## 8. Strong Helps Weak: Directional Cross-Modal Alignment Transfer in Multi-modal LLMs

- Source: arxiv
- arXiv ID: 2610.04580
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2610.04580v1
- PDF: https://arxiv.org/pdf/2610.04580v1
- DOI: https://doi.org/10.48550/arXiv.2610.04580

### Authors

Hoigi Seo, Byung Hyun Lee, Minjun Kim, Dohyun Mah, Jongho Lee, Se Young Chun

### Abstract

Multi-modal large language models (MLLMs) achieve strong modality understanding by pairing a large language model (LLM) with an encoder for a target modality such as vision, video, or audio. However, improving an MLLM's capability for a given modality typically requires additional training on large modality-specific datasets, incurring substantial data collection and compute costs. Model merging offers an alternative, but it is often infeasible for data-scarce, large per-sample size, or domain-specific modalities (\textit{e.g.}, audio and video), where same-modality model variants are rarely available. In this work, we characterize an intriguing asymmetric phenomenon: merging a well-aligned, data-rich source-modality MLLM into a data-scarce target-modality MLLM substantially improves the target on its own benchmarks. Our theoretical and empirical analyses show that this gain stems from enhanced alignment between modality-specific and textual tokens, induced by the stronger donor modality. Specifically, we derive a mutual-information lower bound that is monotonic in alignment-related quantities and strongly correlated with downstream MLLM performance. Building on this principle, we propose Directional Cross-modal Alignment Transfer (DCAT), a novel framework that transfers textual alignment from a strong, well-aligned source (donor) modality to a weak target (recipient) modality, boosting target-modality performance without further fine-tuning. We further show that the alignment-enhancing objective admits a closed-form weight-space solution computed from only a small calibration set. DCAT outperforms existing model-merging methods, offering an efficient path toward cross-modal alignment transfer. Project page with code is available at \url{https://seohoiki3215.github.io/DCAT_project_page}

### 中文一句话结论
本研究提出DCAT框架，通过从强模态（如图像）向弱模态（如音频、视频）传递文本对齐，无需额外微调即可显著提升多模态大模型在目标模态上的性能。

### English TL;DR
DCAT is a training-free framework that improves a weak target modality in multi-modal LLMs by transferring text-alignment from a stronger donor modality via a closed-form weight update, boosting target-modality performance and outperforming existing model-merging methods.

### 中文详细总结
多模态大语言模型（MLLMs）通过将大语言模型（LLM）与特定模态编码器（如视觉、视频或音频）配对，实现了强大的模态理解能力。然而，提升某一模态的能力通常需要大量模态特定数据和计算资源进行额外训练。模型合并虽是一种替代方案，但对于数据稀缺或样本量大的模态（如音频、视频），同模态变体稀少，难以应用。本研究揭示了一个非对称现象：将对齐良好的数据丰富源模态MLLM合并到数据稀缺的目标模态MLLM中，能显著提升目标模态在其基准上的性能。理论和实证分析表明，这种提升源于模态特定令牌与文本令牌之间对齐的增强，由更强的供体模态诱导。具体而言，作者推导了一个互信息下界，该下界单调依赖于对齐相关量，并与下游MLLM性能强相关。基于此，提出了方向性跨模态对齐转移（DCAT）框架，从强供体模态向弱受体模态传递文本对齐，无需进一步微调。此外，对齐增强目标可通过从少量校准集计算出的闭式权重空间解来实现。DCAT在多个基准（MMAU、AIR-Bench、Video-MME等）上优于现有模型合并方法，平均性能提升29.55%，提供了一条高效的跨模态对齐转移路径。

### 方法 / 贡献
1. **现象发现与理论分析**：发现不同模态MLLM合并能提升目标模态性能，提出基于子空间能量重叠（SEO）和频谱多样性（SD）的对齐度量，并证明其与互信息下界及下游性能强相关。
2. **DCAT框架**：利用少量校准样本，通过闭式权重更新，将对齐从高对齐供体模态（如视觉）转移到较弱受体模态（如音频/视频），无需额外训练。
3. **实验验证**：在多个MLLM架构和基准上，DCAT一致优于现有模型合并方法。

### 实验或数据
- **基准**：MMAU（音频）、AIR-Bench（音频）、Video-MME（视频）、MVBench（视频）
- **模态**：视觉（供体）→ 音频/视频（受体）
- **模型架构**：基于Vicuna的MLLM（如OptMerge检查点）
- **对比方法**：Task Arithmetic (TA)、TIES、ISO、TSV、OptMerge
- **校准集**：仅需数百样本
- **结果**：DCAT平均性能提升29.55%，在Music、Sound、Speech等子类上均有提升

### 值得关注点
1. **非对称对齐转移**：首次系统研究跨模态MLLM合并中的方向性对齐传递，提出理论驱动解释。
2. **计算高效**：仅需少量校准样本（数百）和闭式解，无需微调或大量数据。
3. **广泛兼容性**：适用于多种模态（音频、视频）和模型架构，显著优于现有合并方法。
4. **可解释性**：对齐度量（SEO×SD）与性能强相关，提供合并效果的理论依据。

### 局限性
1. **供体模态依赖**：当前实验仅以视觉为供体，其他强模态（如文本嵌入丰富的模态）作为供体的效果尚未探索。
2. **模态覆盖有限**：仅验证音频和视频为受体，对于其他数据稀缺模态（如点云、触觉）的适用性未提及。
3. **校准集需求**：虽仅需少量样本，但跨模态场景下收集标签数据仍可能困难。
4. **理论假设简化**：互信息下界推导假设高斯分布，可能不完全反映真实数据复杂性。

## 9. Stance Drift: How AI-mediated Communication Distorts Our Message

- Source: arxiv
- arXiv ID: 2610.04620
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2610.04620v1
- PDF: https://arxiv.org/pdf/2610.04620v1
- DOI: https://doi.org/10.48550/arXiv.2610.04620

### Authors

Lingchong Liu, Yanfei Zhou, Jacob Bien, Y. X. Rachel Wang, Lucy Xia, Xin Tong

### Abstract

Large language models (LLMs) increasingly mediate human communication, from drafting emails to summarizing scientific reports, yet whether they faithfully preserve a speaker's position remains largely untested. We model AI-mediated communication as a two-step generation-extraction pipeline: one LLM produces an argument from a specified stance, and a second LLM extracts the stance from that argument. We represent the pipeline as a probabilistic state transition over five Likert-type stance categories and define the stance preservation rate (SPR) as the average probability that the extracted stance matches the initial stance. Across 112 debate propositions, none of the nine LLMs tested exceeded an SPR of 0.7 under the default configuration. Three drift patterns accounted for most of the drift: polarization, deviation from neutrality, and flipping. Among the mitigation strategies tested, including in-context learning, multiple extraction with shuffled options, assertion, and reflection, only adding medium reasoning effort to a reflection prompt for GPT-5.4 substantially improved the SPR, to 0.775, yet polarization remained the largest pattern, with 0.119 of the transition mass. An exploratory comparison with human extraction on a single proposition suggests that drift arises at both the generation and the extraction stage. These results point to a fidelity gap in AI-mediated communication, with implications for journalism, policy deliberation, scientific communication, and other domains where opinion-laden messages pass through language models.

### 中文一句话结论
AI中介通信中，大语言模型在默认设置下无法可靠保持发言者的立场，立场漂移普遍存在且难以完全消除。

### English TL;DR
AI-mediated communication using LLMs introduces significant stance drift, with none of nine models exceeding a 0.7 stance preservation rate under default settings, and only a reflection prompt for GPT-5.4 substantially improving it to 0.775, while patterns of polarization, deviation from neutrality, and flipping remain dominant.

### 中文详细总结
本文系统性地检验了大语言模型作为通信中介时能否忠实保持发言者的原始立场。作者将AI中介通信建模为“生成-提取”两步流水线：一个LLM根据指定立场生成论点，另一个LLM从该论点中提取立场。使用五个李克特式立场类别（强烈同意、同意、中立、不同意、强烈不同意）定义立场保持率（SPR），即提取立场与初始立场匹配的平均概率。测试了9个LLM在112个辩论命题上的表现，默认配置下所有模型的SPR均未超过0.7。识别出三种主要漂移模式：极化（立场趋向极端）、偏离中立（中立立场偏向某一侧）和翻转（立场完全相反）。在尝试的多种缓解策略（上下文学习、多提取并打乱选项、断言、反思）中，仅对GPT-5.4添加中等推理量的反思提示显著提升了SPR至0.775，但极化仍然贡献了最大的转变质量（0.119）。对单个命题的探索性人类提取比较表明，漂移在生成和提取阶段均有发生。研究揭示了AI中介通信中的保真度缺口，对新闻、政策讨论、科学传播等涉及观点信息传递的领域具有启示意义。

### 方法 / 贡献
- **方法**：将AI中介通信形式化为一个两阶段概率状态转移模型：生成阶段（LLM从给定立场生成论点）和提取阶段（另一个LLM从论点识别立场）。定义立场保持率（SPR）作为度量标准，并识别三种漂移模式（极化、偏离中立、翻转）。测试多种缓解策略（上下文学习、多提取打乱选项、断言、反思）。
- **贡献**：首次系统量化了AI中介通信中的立场漂移问题，揭示了默认配置下显著的能力缺陷，并分析了漂移模式及其分布。提出并评估了缓解策略，发现仅反思提示在特定模型上有效，但无法完全消除极化。

### 实验或数据
- 使用112个辩论命题作为立场输入，涵盖多种观点。
- 测试了9种不同大语言模型（未明确列出所有模型名称）。
- 默认配置下，所有模型的SPR均低于0.7；对GPT-5.4应用反思提示（中等推理量）后SPR提升至0.775。
- 对单个命题进行了探索性人类提取比较，以初步分离生成阶段和提取阶段的贡献。
- 未提及其他特定数据集或实验性基准集。

### 值得关注点
- **低保真度**：默认设置下所有模型SPR≤0.7，表明AI中介通信严重扭曲原始立场。
- **漂移模式**：极化（转向极端）、偏离中立（中立立场偏移）和翻转（完全反向）占主导，三者合计解释了93%的漂移质量（以GPT-4o mini为例）。
- **缓解策略有限**：仅GPT-5.4配合反思提示且设置中等推理量时有效，其他策略（如上下文学习、断言）未显著改善。
- **阶段性影响**：比较显示漂移同时存在于生成和提取阶段，说明问题更为根本。

### 局限性
- 人类提取比较仅基于单个命题，缺乏统计普遍性。
- 测试模型有限，可能未涵盖所有主流LLM。
- 缓解策略仅在特定模型和配置下有效，泛化能力未知。
- 未探索更复杂的通信链路（如多轮迭代、不同模型配对等）。
- 立场分类仅使用五个粗略类别，可能忽略细微立场差异。

## 10. Scaling Down the Scaling Laws: Parameter Efficiency and Compute-Optimal Training in Resource-Constrained Large Language Models

- Source: arxiv
- arXiv ID: 2610.06387
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2610.06387v1
- PDF: https://arxiv.org/pdf/2610.06387v1
- DOI: https://doi.org/10.48550/arXiv.2610.06387

### Authors

Joe Dwyer

### Abstract

Large language models (LLMs) have achieved substantial performance gains through increases in model size, training data, and computational resources. However, traditional scaling approaches produce diminishing returns, rising financial and environmental costs, and barriers to participation for researchers operating outside large industrial laboratories. This review examines the evolution of LLM scaling theory from empirical scaling laws to compute-optimal training, with particular emphasis on parameter efficiency, token utilization, data efficiency, and resource-constrained environments. Foundational work on scaling laws is synthesized alongside later research on compute-optimal training, data pruning, efficient architectures, quantization, low-rank adaptation, and edge-oriented optimization. The literature indicates a shift from scale maximization toward more deliberate allocation of parameters, tokens, compute, and hardware resources. At the same time, important empirical, theoretical, and methodological gaps remain regarding whether scaling principles established on enterprise-grade infrastructure generalize to smaller models and constrained computing environments. This review organizes these developments into a unified framework for resource-efficient LLM training and argues that future progress should evaluate efficiency not solely through model performance, but through the relationship among performance, parameter count, computational cost, token allocation, and hardware constraints.

### 中文一句话结论
本综述系统梳理了大规模语言模型（LLM）从经验缩放定律到计算最优训练的演变，强调在资源受限环境下，模型性能不仅取决于规模，更依赖于参数、数据、计算和硬件之间的高效平衡，并指出当前缩放原则在小模型和受限计算场景下的推广仍存在关键缺口。

### English TL;DR
This review synthesizes the evolution of LLM scaling from empirical laws to compute-optimal training, emphasizing parameter efficiency, token utilization, and resource-constrained optimization while identifying gaps in generalizing scaling principles to smaller models and hardware environments.

### 中文详细总结
该论文是一篇结构化叙事综述，聚焦于大规模语言模型在资源受限条件下的训练效率问题。文章回顾了从Kaplan等人提出的经验缩放定律（模型损失与规模、数据、计算呈幂律关系）到Hoffmann等人（Chinchilla）提出的计算最优训练（强调参数与训练token的平衡）的转变。综述将相关文献整合为统一框架，涵盖数据剪枝、高效架构、量化、低秩适应和边缘优化等方向。作者指出，缩放研究经历了“规模最大化”、“计算最优平衡”和“资源受限优化”三个阶段，核心观点是效率并非仅由模型大小决定，而是参数数量、数据量、架构、系统和硬件约束共同作用的结果。文章还识别出三个主要研究空白：1) 基于企业级基础设施得到的缩放定律缺乏在受限计算下的充分验证；2) 参数效率缺乏标准化定义；3) 资源受限的LLM研究在方法论上碎片化，影响可复现性和比较。综述提出未来研究应关注受控的token-参数实验、能耗感知指标、可复现的受限计算基准，以及缩放原则向小硬件环境的推广测试。

### 方法 / 贡献
- **方法**：采用结构化叙述性综述方法，基于对IEEE Xplore、Google Scholar、ACM数字图书馆和arXiv的文献搜索，覆盖2021–2025年主要文献及更早的奠基性工作。搜索策略在论文中有详细记录（如表格），但作者明确说明并非PRISMA式系统综述。
- **贡献**：
  1. 追踪从经验缩放定律到计算最优训练的理论演变；
  2. 将token利用、参数效率和计算开销整合为一个统一的效率框架；
  3. 将资源高效的LLM方法归纳为数据、参数、架构、系统和硬件五部分分类；
  4. 识别当缩放原则从大规模基础设施迁移到受限环境时出现的实证、理论和方法论空白。

### 实验或数据
论文本身是综述，不包含新的实验或数据集。作者报告了文献搜索的查询结果（例如“LLM Training” + “Compute Overhead”得到371条结果，其中90篇相关），但未进行任何训练或评估实验。因此，本摘要中无实验数据。

### 值得关注点
- **核心论点**：缩放不再仅是增加模型规模，而是如何在固定预算下最优分配参数、token和计算资源。
- **关键理论**：Chinchilla的缩放规律表明参数与训练数据应按比例平衡（如D ∝ N^0.73），但这一指数并非普适常数。
- **参数效率的度量**：论文提出了一个具体的操作化定义（逆困惑度除以参数与吞吐量的乘积），但强调这并非统一标准，反映了领域内缺乏共识的问题。
- **实际意义**：资源受限的研究者可通过控制token-参数比例，使用较小模型获取有意义的研究成果，从而降低参与门槛。

### 局限性
- **缺乏实证验证**：综述未进行任何实验来验证其提出的框架或缩放下移假设。
- **搜索方法的非系统性**：作者承认综述结构可重复但并非严格的PRISMA式系统综述，可能存在文献遗漏。
- **参数效率定义不统一**：论文未能提供领域通用的标准度量，仅给出一个示例，限制直接比较。
- **缩放原则推广性存疑**：文中明确指出，基于大规模基础设施得出的缩放定律尚未在受限计算环境中得到充分测试，因此无法确认其是否适用于小模型和边缘设备。
- **论文未给出未来实验的具体设计**：虽然提出了研究议程，但未详细说明如何实施受控实验或设计基准。

## Processing Notes

- Duplicate papers skipped: 0