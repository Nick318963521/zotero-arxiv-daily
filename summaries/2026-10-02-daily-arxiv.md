# Daily arXiv - 2026-10-02

- Source: GitHub Actions generated paper list
- Generated at: 2026-10-02T02:07:22
- Paper count: 10

## 1. BARRAC: Adaptation of an English Aspect-based Sentiment Analysis Approach for Classification Tasks in Arabic Dialects

- Source: arxiv
- arXiv ID: 2609.38820
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.38820v1
- PDF: https://arxiv.org/pdf/2609.38820v1
- DOI: https://doi.org/10.48550/arXiv.2609.38820

### Authors

Ali Almutairi, Gelareh Mohammadi, Imran Razzak, Aditya Joshi

### Abstract

With the rapid growth of Arabic NLP, several models, datasets and benchmarks have been reported. This paper asks whether approaches developed for majority languages like English can be adapted to Arabic tasks. We adapt an English aspect-based sentiment analysis framework to Arabic classification tasks and present the adaptation as BARRAC: Brainstorming Alignment and Replaced Representation learning for ArabiC tasks. BARRAC replaces consumer-review attribute pools with Arabic linguistic devices and markers for dialectal sentiment, sarcasm, and dialect identification, and replaces noisy self-training with two-stage training. Evaluated on five Arabic dialect datasets, BARRAC achieves a mean macro-F1 of 63.93\%, outperforming the best few-label SOTA by 3\%, and outperforming GPT-4o on four out of five tasks. Error analysis provides insights into remaining challenges. These results demonstrate that adapting task-specific approaches is a promising direction for Arabic NLP alongside adapting models, datasets and benchmarks.

### 中文一句话结论
BARRAC通过改编英文方面级情感分析框架，在阿拉伯方言分类任务上取得了平均63.93%的macro-F1，超过现有少标签方法及GPT-4o。

### English TL;DR
BARRAC adapts an English aspect-based sentiment analysis framework for Arabic dialect classification tasks, achieving a mean macro-F1 of 63.93% and outperforming state-of-the-art few-label methods and GPT-4o on four out of five datasets.

### 中文详细总结
本论文提出BARRAC，将英文DS²-ABSA框架改编用于阿拉伯方言的分类任务（包括情感分析、讽刺检测和方言识别）。主要改编包括：用阿拉伯语言设备（linguistic devices）和语言标记（linguistic markers）替换原框架中面向消费者评论的属性池，并用两阶段训练（中间训练+少标签微调）替换原噪声自训练。在五个阿拉伯方言数据集（Ar-Sentiment、Ar-Sarcasm、Ar-Dialects、Sa'7r、DART）上评估，BARRAC达到平均63.93%的macro-F1，比最佳少标签SOTA方法高出3个点，并在五个任务中的四个上超过GPT-4o。错误分析揭示了剩余挑战。

### 方法 / 贡献
- **方法**：改编自DS²-ABSA，核心改动包括：①将原框架中的“方面类别”替换为与任务相关的语言设备（如讽刺检测中的mock_praise），将“方面词”替换为语言标记（如方言识别中的典型词汇/形态特征）；②将原噪声自训练替换为两阶段训练：先用合成数据训练伪标签模型（PL-FT），再用真实少标签数据微调（FT-FL）。此外还扩展了领域范围（10个主题域，如经济、体育、健康等）。
- **贡献**：证明了将英文任务特定方法改编到阿拉伯NLP是有效且很有前景的方向，尤其适用于低资源方言任务。

### 实验或数据
- **数据集**：5个阿拉伯方言公开数据集：Ar-Sentiment（三分类情感）、Ar-Sarcasm（二分类讽刺）、Ar-Dialects（五分类方言）、Sa'7r（二分类讽刺）、DART（五分类方言+情感）。均设置少标签场景（每类仅100个真实标签）。
- **基线**：包括无微调模型（ArabicBERT、ARBERTv2等）、SFT基线、SOTA少标签方法（Cluster&Tune、IDoFew等）。
- **结果**：BARRAC平均macro-F1 = 63.93%，超过所有基线；在Ar-Sentiment（65.61%）、Ar-Sarcasm（69.06%）、Sa'7r（67.03%）、DART（68.76%）上最优，仅在Ar-Dialects（49.19%）上略低于某些基线。

### 值得关注点
- 首次将英文方面级情感分析的完整数据合成框架系统改编到阿拉伯语言分类任务（情感、讽刺、方言识别）。
- 用语言设备和标记替代产品属性，使框架适应非实体性、语言现象型的分类问题。
- 两阶段训练策略避免了噪声自训练的误差累积，提升了少标签场景下的鲁棒性。
- 在多个任务上超越GPT-4o，表明任务特定的小型模型在低资源语言上仍具竞争力。

### 局限性
论文未详细列出具体局限性，但错误分析表明仍存在剩余挑战（例如某些方言或讽刺模式难以正确分类）。由于所有实验均使用100个标签的少标签设定，在更多标签或更大规模数据上的泛化能力尚未验证。

## 2. Synthetic Data Characterization via Training Dynamics

- Source: arxiv
- arXiv ID: 2609.39447
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.39447v1
- PDF: https://arxiv.org/pdf/2609.39447v1
- DOI: https://doi.org/10.48550/arXiv.2609.39447

### Authors

Irene Lago, Ana Ezquerro, David Vilares

### Abstract

Interpreting properties of LLM-generated data is important for understanding its utility and limitations across learning tasks. In this work, we characterize synthetic data through sample-level learnability, studying variation among LLM families and scales, alongside human-written data as a reference. We first generate synthetic datasets spanning single- and multi-label classification, labeling, and tree prediction tasks. We then derive empirical data distributions from encoder training dynamics for both machine and organic data, and estimate the robustness of these distributions across encoders. Finally, we evaluate how data selection strategies based on these learnability signals affect both data sources differently.

### 中文一句话结论
本论文提出通过样本级训练动态（learnability）刻画 LLM 生成合成数据的框架，并将其与人类撰写数据对比，以评估不同 LLM 家族、规模及难度筛选策略对数据效用的影响。

### English TL;DR
This paper characterizes LLM-generated synthetic data using sample-level training dynamics (learnability). It compares synthetic data from different LLM families and scales against human-written data across classification, sequence labeling, and tree prediction tasks, and analyzes how difficulty-based data selection strategies affect both data sources differently.

### 中文详细总结
- 论文主张从样本级“可学习性/训练动态”角度刻画合成数据，而非仅依赖静态分布相似性。
- 生成覆盖单标签/多标签分类、序列标注、树/图结构预测等任务的合成数据集。
- 使用编码器训练动态（置信度、变异性、正确性）推导机器数据与人类（有机）数据的经验分布，并评估这些分布对编码器选择的稳健性。
- 进一步评估基于难度（可学习性信号）的数据选择策略对两类数据源的不同影响。
- 现有 TL;DR 指出：通过样本级训练动态刻画 LLM 合成数据，比较不同 LLM 家族和规模与人类数据的可学习性，并评估基于难度的数据选择策略对两类数据源的影响。

### 方法 / 贡献
- 提出一个基于训练动态的样本级合成数据表征框架，适用于分类、序列标注、树结构预测等多样 NLP 任务。
- 将数据映射（data maps）中的置信度、变异性和正确性等指标推广到非序列分类任务（如多标签、序列标注、图预测），并引入“个体置信度”等适配指标。
- 对不同 LLM 家族、规模及提示策略进行分布对比分析，并评估训练动态特征对编码器后端的稳健性。
- 基于难度分层训练评估数据选择策略，并与基线进行比较；代码已公开。

### 实验或数据
- 摘要提及：生成单标签/多标签分类、标注、树预测等合成数据集；从编码器训练动态中推导机器数据与有机数据的经验分布；估计这些分布在编码器间的稳健性；评估基于可学习性信号的数据选择策略对两类数据源的不同影响。
- 摘要未报告具体数值结果、数据集规模或基准分数；也未在摘要层面给出详细实验设置，因此无法补充具体指标。

### 值得关注点
- 将训练动态分析从简单分类扩展到多标签分类、序列标注和图/树结构预测等结构化任务。
- 同时对比多个 LLM 家族/规模与人类数据，而非局限于单一模型。
- 关注难度数据选择策略对合成数据与人类数据的不同影响，对数据筛选、课程学习与数据混合策略具有潜在启示。
- 提供公开代码仓库，便于复现与扩展。

### 局限性
- 摘要与所提供片段未明确列出本工作的具体局限性。
- 引言中提及合成数据普遍存在多样性不足、与人类文本分布偏差、可能引发模型崩溃等问题，但这些是领域背景而非本文自身局限。
- 由于仅依据摘要及部分引言/方法片段，无法确知潜在局限，例如分析可能依赖特定编码器、提示策略或任务范围，但摘要未作说明。

## 3. How Much Is an AI Token Worth? Scaling Laws for Wild AI-Generated Web Text

- Source: arxiv
- arXiv ID: 2609.40295
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.40295v1
- PDF: https://arxiv.org/pdf/2609.40295v1
- DOI: https://doi.org/10.48550/arXiv.2609.40295

### Authors

Jenna Russell, Ben Glickenhaus, Katherine Thai, John Wieting, Mohit Iyyer, Max Spero, Bradley Emi

### Abstract

Web text makes up the majority of pretraining data and is increasingly AI-generated. After applying FineWeb quality filtering, we find that 27.5% of tokens from June 2026 web data are labeled as AI-generated by Pangram, rising to 31.1% by August. Unlike synthetic data or model-collapse setups, this *wild* AI text comes from many models, is written for human readers, and arrives unlabeled in pretraining corpora. How does AI text in the wild affect language model pretraining? To answer this question, we pretrain 800 language models, varying the ratio of added AI tokens to human tokens, and fit scaling laws to held-out losses on both human and AI-generated text. For data-starved models, adding AI tokens to pretraining data initially lowers loss on human text, but the benefit saturates as more are added and quickly *reverses* into harm. For models trained on high budgets of human text, AI tokens raise loss almost immediately, while the same number of fresh human tokens keeps lowering it. Scaling laws such as Hoffman et al. (2022) fail to predict this behavior. We propose a new scaling law with separate benefit and harm terms that allows the value of an AI token to change sign while also reducing to Chinchilla in the absence of AI text. When fit on smaller models, our scaling law predicts the effect of AI text on held-out human-text loss for models up to 3.6x larger with 41% lower error than the best existing law over all AI ratios. We recommend filtering AI text when the target is human text, repeating human text before expanding the training dataset with AI-generated web text, and reporting validation loss on human and AI text separately AI text remains valuable when the target is AI text. We release WildAI, an 83B-token corpus with AI, topic, and format labels, all 800 models and code at https://github.com/pangramlabs/WildAI.

### 中文一句话结论
在网络预训练数据中混入未标注的AI生成文本，对数据量不足的小模型有微小帮助，但一旦人类文本充足，AI文本会立即损害模型在人类文本上的损失；本文提出带正负项的新标度定律并推荐过滤AI文本。

### English TL;DR
This paper shows that unlabeled AI-generated web text slightly helps data-starved models but quickly harms models trained on enough human data. It proposes a new scaling law with separate benefit and harm terms and recommends filtering AI text when human-text loss is the target.

### 中文详细总结
现实预训练语料中已有大量来自不同模型的AI生成文本（约27.5%-31.1%），且未标注。本文通过预训练800个语言模型，系统改变人类文本与AI文本的混合比例，发现：对人类文本量不足的小模型，加入少量AI文本可略微降低在人类测试集上的损失，但收益很快饱和并转为损害；对已拥有充足人类文本的模型，加入AI文本会立即提高损失，而同样的新人类文本却持续降低损失。传统缩放定律（如Chinchilla）无法预测此现象。本文提出新标度定律，包含独立的正（benefit）和负（harm）项，使AI token的价值可正可负，且在无AI文本时退化为Chinchilla定律。该定律在较小模型上拟合后，能预测比训练模型大3.6倍的模型的损失，且预测误差比现有最佳定律降低41%。建议：目标是人类文本时应过滤AI文本；优先重复使用人类文本而非加入AI web文本；分开报告人类和AI文本的验证损失；若目标是AI文本，AI文本仍有价值。同时发布WildAI数据集（830亿token，含AI、主题、格式标签）和所有模型代码。

### 方法 / 贡献
- **方法**：在FineWeb质量过滤后的网络数据基础上，人工添加不同比例（0%-100%）的AI生成文本（来自多个模型且为用户写作，而非合成数据），预训练800个不同规模的语言模型，观测在人类和AI测试集上的损失。
- **贡献**：
  1. 揭示野生AI文本对预训练的非单调、符号反转影响。
  2. 提出新的缩放定律，显式建模AI文本的benefit和harm项，可预测更大模型的行为。
  3. 给出明确建议：目标为人类文本时过滤AI文本，重复使用人类文本优于混入AI文本。
  4. 开源大规模标注语料WildAI（83B tokens）、所有模型和代码。

### 实验或数据
- 数据：使用FineWeb（2026年6月、8月网络快照）经Pangram检测，AI token比例分别为27.5%和31.1%；实验时人工混合不同比例的AI文本与人类文本（人类文本来自FineWeb过滤后）。
- 实验：预训练800个语言模型，参数量和训练预算均有变化，变化AI token占比；记录在人类测试集和AI测试集上的交叉熵损失。
- 标度定律拟合：在较小模型（最多约1B参数）上拟合，预测最大至约3.6倍参数模型的损失。

### 值得关注点
- AI文本的来源是“野生”即真实网络爬取，而非人工生成的合成数据或模型坍塌设置，更贴近现实。
- 传统缩放定律（Chinchilla）完全失效，新定律成功捕捉符号反转现象。
- 预测能力验证了跨规模迁移：小模型拟合的定律可预测大模型行为（3.6x），误差降低41%。
- 提供了实用指南：若最终任务基于人类语言，应严格过滤AI文本；甚至重复人类文本也比加AI文本好。

### 局限性
- 实验仅在单一质量过滤（FineWeb）和单一AI检测器（Pangram）下进行，未探索其他过滤或检测方案的泛化性。
- 未评测下游任务（如问答、推理）上的性能，仅以损失衡量。
- 模型规模最大仅比拟合模型大3.6倍，更极端的大模型行为未知。
- 未考虑AI文本的混入时间、顺序等动态因素；仅固定比例混合。
- 标度定律的benefit/harm项参数可能随模型家族或数据分布变化，需进一步验证鲁棒性。

## 4. A helps B while B hurts A: directed transfer in instruction-tuning mixture

- Source: arxiv
- arXiv ID: 2609.39702
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.39702v1
- PDF: https://arxiv.org/pdf/2609.39702v1
- DOI: https://doi.org/10.48550/arXiv.2609.39702

### Authors

Nima H. Siboni, Vahid Rostami

### Abstract

Adapting a language model to a specialized corpus means choosing which instruction-tuning tasks to train on under a fixed budget, and testing one choice costs a fine-tuning run. Common heuristics add more source tasks or pick sources similar to the target. The first assumes transfer is never negative; the second, that it is symmetric. We show that both assumptions fail: task $A$ can help task $B$ while $B$ hurts $A$, so helpfulness is a signed property of ordered source--target pairs. We introduce the transfer map, a signed estimate of how much each source helps or hurts each held-out target. We fit the map in hundreds of fine-tuning runs on Qwen3 and Mistral models from 0.6B to 32B parameters, with all sources drawn from one corpus and no training examples from the target. The map predicts a held-out target's accuracy on unseen mixtures: recorded before those runs, its predictions have less than half the error of a mixture-agnostic baseline. The map is specific to its target and corpus but transfers across model scale: a mixture selected in advance at one size beats training on all source tasks at every other size we tested. Transfer is thus a property of the data. The map selects the tasks that help and drops the one that interferes: accuracy on the reasoning targets (causal explanation, multi-hop questions and methodological critique) rises by up to 14 percentage points over training on all source tasks.

### 中文一句话结论
通过构建“迁移地图”量化指令微调中源任务对目标任务的定向正负影响，发现迁移具有符号和方向性（A 帮助 B 但 B 伤害 A），并基于此选择源任务可在推理目标上提升最多 14 个百分点。

### English TL;DR
Transfer between instruction-tuning tasks is signed and directed (task A helps B while B hurts A), motivating a "transfer map" that predicts held-out target accuracy and selects beneficial sources, improving reasoning tasks by up to 14 percentage points.

### 中文详细总结
该论文研究在固定预算下如何选择指令微调任务（源任务）以最大化某一目标任务性能。常用启发式方法假设迁移总是正向（增加源任务数量有益）或对称（相似源任务有益），但作者发现这些假设均不成立：任务 A 可能促进任务 B，而 B 却损害 A，因此帮助性是有序源-目标对的带符号属性。作者提出“迁移地图”，即对每个源任务如何帮助或损害每个未见过目标任务的带符号估计。该地图通过数百次微调实验（使用 Qwen3 和 Mistral 模型，参数规模 0.6B 至 32B）拟合，所有源任务来自同一语料库，目标无训练样本。地图对未见过的混合任务的预测误差比不考虑混合的基线低一半以上。迁移地图具有目标特异性和语料特异性，但可在不同模型规模间迁移：基于某一规模选出的混合任务在其他规模上效果均优于训练所有源任务。在推理目标（因果解释、多跳问题、方法论批评）上，利用地图选择源任务相比训练所有源任务准确率提升最多 14 个百分点。

### 方法 / 贡献
- 证明指令微调任务间的迁移具有符号和方向性：A 帮助 B 但 B 伤害 A，且两种方向在 28 对中有 14 对（Qwen3）或 13 对（Mistral）不同，3 或 4 对符号相反且置信区间排除零。
- 引入“迁移地图”：一种基于线性数据模型的带符号定向估计，用少量探测混合（固定预算、同等分配源任务、不含目标）拟合每个源任务对每个目标的影响。
- 通过预先记录预测，地图在 8 或 12 个测试单元中误差小于混合无关基线的一半。
- 地图作为选择器优于相似性选择器，在推理目标上提升 3 至 16 个百分点。
- 迁移是数据固有性质：两模型家族的地图高度相关（r=0.88），不同规模间相关（r=0.76–0.92），但跨语料库时相关性差（r<0.55）。

### 实验或数据
- 主要语料：110 篇运动控制及其障碍相关论文（88 篇训练，22 篇评估，包含 14,618 个评估项），生成 8 种任务类型。
- 模型：Qwen3（0.6B, 1.8B, 4B, 8B, 32B）和 Mistral-24B。
- 共进行 751 次微调实验：完整探测在 32B 模型上进行，较小模型使用缩减探测。
- 还使用 PubMed 癌症免疫学摘要（951 篇）作为语料迁移控制。
- 所有实验固定预算（源任务总示例数固定），目标不含训练示例。
- 评估指标：单项多选题准确率。

### 值得关注点
- 发现一个干扰性任务类型可抵消其他所有任务的好处：在多跳问题（MHOP）上，训练所有其他源任务（均匀混合）仅比未调优模型略好（20% vs 18%），加入方法论批评（ERR）后准确率降至 7%（接近 0）。
- 地图可预先记录预测，无需为每个新混合重新训练。
- 地图在小规模探测（24 个随机混合）下仍能恢复 96% 的 32B 模型全探测效果。
- 跨模型家族和跨规模的可迁移性表明迁移地图主要反映数据属性。

### 局限性
- 仅测试了同一语料库生成的任务类型，未涉及不同来源数据集；语料库迁移时相关性显著下降（r<0.55），泛化性有限。
- 使用固定预算和均匀分配源任务示例，未探究不同权重或预算变化的影响。
- 线性数据模型假设可能无法捕捉复杂非线性相互作用。
- 实验主要在医学 / 科学语料上进行，对通用领域的适用性未验证。
- 论文未讨论如何扩展到更多任务类型或动态在线选择。

## 5. On the (In)effectiveness of AMR Augmentation for Large Language Models

- Source: arxiv
- arXiv ID: 2609.40121
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.40121v1
- PDF: https://arxiv.org/pdf/2609.40121v1
- DOI: https://doi.org/10.48550/arXiv.2609.40121

### Authors

Hoa Quynh Nhung Nguyen, Jacopo Staiano, Michael Sullivan

### Abstract

While Abstract Meaning Representation (AMR) has historically improved performance on a range of NLP tasks, the benefit---or lack thereof---of AMR augmentation for modern LLMs is thus far unclear. In this paper, we attempt to reproduce recent work that reported substantial downstream gains from AMR augmentation, finding that these are likely due to specific choices in the experimental settings used: using a consistent and unified protocol for hyperparameter selection, we observe that text-only baselines consistently match or exceed the performance of AMR-augmented models. To investigate this null result, we introduce a perplexity-based probe measuring the degree to which AMR provides an LLM with supplemental relational knowledge not already available to the model. We find that AMR augmentation does not help LLMs improve their understanding of relational content in the sentence, indicating that augmenting these models with AMR offers no clear benefit on downstream tasks.

### 中文一句话结论
本研究通过统一实验协议无法复现AMR增强提升LLM性能的结果，发现文本基线一致匹配或超越AMR增强模型，表明AMR增强对现代大语言模型无效。

### English TL;DR
Despite previous claims, AMR augmentation does not improve the performance of large language models on downstream tasks, as text-only baselines match or exceed augmented models under consistent experimental conditions.

### 中文详细总结
本文验证了AMR（抽象意义表示）增强对现代大语言模型（LLM）的下游任务效果。作者尝试复现先前声称AMR带来显著提升的工作，发现其收益很可能源于特定实验设置（如不统一的超参选择）。在统一超参协议下，仅使用文本的基线模型始终匹配或超过AMR增强模型。为探究这一零结果，作者设计了基于困惑度的探针，测量AMR是否为LLM提供额外的关系知识。结果表明，AMR增强并未帮助LLM更好地理解句子中的关系内容，即AMR不提供模型从文本中无法获取的补充信息。该结论在单句任务和多句复杂任务（如事件论元抽取）上均成立。

### 方法 / 贡献
1. **复现与质疑**：复现了Zhang等（2025）的工作，发现其报告的性能提升不可重现，并指出原因在于实验设置的特殊性。
2. **统一实验协议**：使用LoRA微调、grid search学习率、固定AMR解析器（AMR3-structbart-L），在不同模型（Llama-3.1-8B-Instruct、Qwen3-8B）上系统评估。
3. **扩展至多句任务**：将AMR增强实验从单句任务扩展至多句事件论元抽取等更复杂任务，确认无提升。
4. **探针分析**：提出基于困惑度的探针，直接测量AMR提供的增量关系知识，发现AMR未带来模型原先不具备的信息。
5. **开源代码**：公开所有实验代码。

### 实验或数据
- **模型**：Llama-3.1-8B-Instruct、Qwen3-8B，使用LoRA（r=64, α=128, dropout=0.05）微调。
- **数据集**：采用Zhang等（2025）使用的10个任务中的9个（排除逻辑谬误检测数据集Logic，因其生成方法未公开）：PAWS、SNLI、WMT16、CoNLL2003、SST-2、PubMed45、WiC、SPIDER、AGNews。训练集规模尽量贴近原论文。
- **AMR解析**：使用AMR3-structbart-L将所有实例解析为PENMAN线性化表示。
- **微调策略**：包含联合微调（所有数据混合）和单独微调（每个数据集独立微调）两种设置。
- **探针实验**：基于困惑度测量AMR提供的增量关系知识，比较模型对原始文本和AMR增强文本的困惑度差异。
- **结果**：文本基线在各项指标上匹配或超越AMR增强模型；探针显示AMR未提供额外关系知识。

### 值得关注点
- **挑战先前结论**：直接质疑并无法复现Zhang等（2025）声称的AMR增强带来高达12个F1点提升的结论，强调实验设置的重要性。
- **新颖的探针方法**：首次提出基于困惑度的度量来直接检测AMR是否提供增量知识，为理解LLM与结构化语义表示的关系提供分析工具。
- **跨模型验证**：在同一协议下测试了两种不同架构的LLM（Llama和Qwen），增强结论的泛化性。
- **开源可复现**：公开完整代码，允许社区进一步验证和扩展。

### 局限性
- 实验仅涉及两种LLM（Llama-3.1-8B-Instruct和Qwen3-8B），未覆盖更多模型系列或更大规模模型。
- AMR解析仅使用单一解析器（AMR3-structbart-L），解析质量可能影响增强效果。
- 任务类型主要集中在分类、抽取等，未涵盖生成式任务（如长文摘要、对话）的全面评估。
- 微调仅采用LoRA，未探索全参数微调或其他参数高效方法。
- 探针分析基于困惑度，可能无法完全捕获AMR在复杂语义推理中的潜在帮助。

## 6. Compact Language, Complex Model Shifts: How and Where Ambiguity and Underspecification Affect LLMs

- Source: arxiv
- arXiv ID: 2609.39572
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.39572v1
- PDF: https://arxiv.org/pdf/2609.39572v1
- DOI: https://doi.org/10.48550/arXiv.2609.39572

### Authors

Michaela Regneri, Nina Scheller, Sören Laue

### Abstract

We analyze how lexical ambiguity and underspecification affect language model training. We create artificial homonyms and artificial hypernyms as pseudowords and analyze the generative performance of language models as they are trained with increasing amounts of these ambiguous or underspecified pseudoword types. We further analyze whether the models disambiguate ambiguous or underspecified statements and provide a first mechanistic account of how ambiguity and disambiguation are represented internally. Our main results show that both ambiguity and underspecification increase model performance in ways that scale with their influence on the language's type-token ratio. However, the accuracy of generating sequences containing ambiguous words or their synonyms decreases compared to other texts. We also show that internal representations of pseudowords reflect disambiguation of pseudo-homonyms, but underspecification of pseudo-hypernyms is maintained during the generative process.



## 7. Synthetic Pre-pretraining Survives Scale, but Not as a Grammatical Prior

- Source: arxiv
- arXiv ID: 2609.39827
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.39827v1
- PDF: https://arxiv.org/pdf/2609.39827v1
- DOI: https://doi.org/10.48550/arXiv.2609.39827

### Authors

Atsuki Yamaguchi, Tatsuro Inaba, Joel Niklaus, Michal Štefánik, Aline Villavicencio, Nikolaos Aletras

### Abstract

Pre-pretraining (PPT) on synthetic non-natural language data improves token efficiency during language model pre-training (PT). Prior work attributes this gain to a grammatical prior, i.e., a structural inductive bias learned during PPT that transfers to natural language grammar. However, PPT has only been tested on models of at most 1B parameters and PT budgets below 2B tokens on predominantly web text. It is unknown whether PPT is effective at larger scales and under more realistic PT data mixtures that combine diverse sources (e.g., code and math). We therefore present a comprehensive study on PPT spanning five PPT tasks, four PT data mixtures, four parameter scales (500M to 7B), and PT budgets of up to 100B tokens. Our results demonstrate that the downstream performance and token efficiency gains of PPT persist at scale, e.g., saving at least 21B PT tokens at the 3B scale. However, in contrast to prior work, we find no consistent evidence that these gains stem from a grammatical prior. Downstream performance does not consistently align with grammatical acceptability across model sizes. Instead, we find that downstream gains arise from PPT tasks that improve long-range retrieval. Finally, PPT performance gains are robust to how PT data mixtures are composed and diminish only when web text is absent. Overall, PPT is a low-cost addition to PT, and future PPT task design should target long-range retrieval rather than natural language grammar.

### 中文一句话结论
大规模（最高7B参数、100B预训练tokens）下，合成预预训练（PPT）仍能提升token效率与下游性能，但其收益源于长距离检索能力增强，而非此前认为的语法先验。

### English TL;DR
Pre-pretraining (PPT) on synthetic data improves token efficiency and downstream performance at scales up to 7B parameters and 100B PT tokens, but gains come from improved long-range retrieval, not a grammatical prior.

### 中文详细总结
本文系统考察了合成预预训练（PPT）在不同规模与数据混合下的有效性。实验覆盖5种PPT任务、4种预训练（PT）数据混合（含网页文本、代码、数学等）、4种参数规模（500M~7B）及最高100B tokens的PT预算。结果表明：PPT的增益在大规模下持续存在，例如3B参数规模可节省至少21B PT tokens；但下游性能与语法可接受性之间缺乏一致关联，推翻了此前“语法先验”的解释。进一步分析发现，PPT的收益主要由能提升长距离检索的任务驱动；PPT对PT数据混合的组成方式鲁棒，仅在完全不含网页文本时增益消失。因此，未来PPT任务设计应聚焦长距离检索而非自然语言语法。

### 方法 / 贡献
- 在5种合成PPT任务、4种PT数据混合、4种参数规模（500M/1B/3B/7B）及最高100B PT tokens下进行系统消融实验。
- 推翻前人“语法先验”假说：通过跨模型规模对比下游性能与语法可接受性，发现无一致正相关。
- 揭示PPT增益的根源是长距离检索能力提升，并验证其对PT数据混合的鲁棒性。

### 实验或数据
- 模型参数：500M、1B、3B、7B；PT预算：最高100B tokens。
- 数据混合：4种组合，包含/不包含网页文本、代码、数学等。
- PPT任务：5种不同类型的合成数据预训练任务（具体任务名称未在摘要中给出）。
- 主要指标：下游任务性能（如文本分类、语言建模等）及token效率（达到同样性能所需PT tokens数）。
- 关键数值：3B参数下，PPT节省至少21B PT tokens。

### 值得关注点
- PPT收益在大规模下依然显著，且与PT数据混合方式无关，仅当完全无网页文本时消失。
- 论文首次系统性否定了语法先验作为PPT增益来源，并定位到长距离检索这一可解释机制。
- 提供了低成本改进PT的实用方向：设计提升长距离检索的合成任务，而非模仿自然语言语法。

### 局限性
- 对语法先验的否定仅基于当前实验设置（5种PPT任务、4种PT混合），可能未覆盖所有可能的语法诱导任务。
- 长距离检索作为增益来源的机制尚需进一步理论分析及更细粒度的消融验证。
- 最大规模仅7B参数、100B tokens，更高规模下的PPT行为尚待探索。
- 当PT数据完全不含网页文本时PPT增益消失，限制了其在某些特殊领域（如纯代码或纯数学预训练）的适用性。

## 8. Beyond Text: LLM-Based Dimensional Emotion Evaluation in Multimodal Dialogue

- Source: arxiv
- arXiv ID: 2609.39072
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.39072v1
- PDF: https://arxiv.org/pdf/2609.39072v1
- DOI: https://doi.org/10.48550/arXiv.2609.39072

### Authors

Yutong Hu, Jinho Choi

### Abstract

Emotion recognition in conversation has been widely studied, but applying Large Language Models (LLMs) to continuous dimensional emotion evaluation in multimodal dialogue remains largely unexplored. We propose an LLM-based framework that performs discrete emotion recognition and Valence-Arousal-Dominance (VAD) dimensional evaluation on IEMOCAP, incorporating acoustic cues as natural language descriptions following the SpeechCueLLM approach. We evaluate six models spanning the LLaMA, GPT, and Qwen families under zero-shot prompting, few-shot prompting, and LoRA fine-tuning. LoRA fine-tuned LLaMA models substantially outperform prompt-engineered GPT models on both tasks despite GPT's larger scale, a gap we attribute to domain adaptation rather than model capacity. Our best model achieves a Valence CCC of 0.7822, a new state-of-the-art on IEMOCAP. Ablation studies confirm that textual audio descriptions meaningfully improve smaller models (+3.5 to 3.6 weighted F1) while contributing little for the largest model, suggesting audio cues are most valuable when linguistic capacity is limited. The performance asymmetry across VAD dimensions closely mirrors the annotator agreement hierarchy in IEMOCAP's own annotations.

### 中文一句话结论
本文提出一种基于大语言模型（LLM）的多模态对话情绪评估框架，在IEMOCAP 上同时进行离散情绪识别与 VAD（效价-唤醒-支配）维度评估，发现 LoRA 微调的 LLaMA 模型显著超越提示工程的 GPT 模型，并以 Valence CCC 0.7822 取得新最优结果。

### English TL;DR
This paper proposes an LLM-based framework for multimodal dimensional emotion evaluation in dialogue, jointly performing discrete emotion recognition and Valence-Arousal-Dominance (VAD) prediction on IEMOCAP. Acoustic cues are converted into natural language descriptions following the SpeechCueLLM approach. Across six models (LLaMA, GPT, Qwen), LoRA fine-tuned LLaMA models substantially outperform prompt-engineered GPT models despite GPT's larger scale, achieving a state-of-the-art Valence CCC of 0.7822 on IEMOCAP. Ablations show textual audio descriptions improve smaller models (+3.5–3.6 weighted F1) but contribute little for the largest model.

### 中文详细总结
本文针对多模态对话中的连续维度情绪评估（VAD）研究不足的问题，提出了一套基于 LLM 的框架。该框架以对话历史、目标话语和声学特征描述为输入，将离散情绪识别与 VAD 连续维度预测作为两个独立任务。声学信息（音量、音高、语速及其波动）通过分位数方案转换为"很低/低/中/高/很高"的自然语言描述，从而无需修改模型架构即可引入非词汇线索。研究在 IEMOCAP 上评估了 LLaMA-2-7B、LLaMA-3.1-8B、LLaMA-3.3-70B、Qwen3.5-35B-A3B（仅离散任务）、GPT-4o-mini 和 GPT-5-mini 六个模型，覆盖零样本、少样本提示和 LoRA 微调三种设置。实验表明，LoRA 微调的开源模型（71.8–73.2 加权 F1）全面超过所有提示工程方法（含 GPT-5-mini 少样本的 59.6），最佳模型在 Valence 维度取得 0.7822 的 CCC，刷新 IEMOCAP 纪录。消融实验显示，音频文本描述对小模型提升明显（+3.5–3.6 加权 F1），但对最大的 70B 模型贡献甚微；此外，VAD 三个维度的表现不对称性与数据集注释者一致性层级高度吻合。

### 方法 / 贡献
- **首个系统性 LLM 框架**：将 LLM 引入多模态对话的连续 VAD 维度评估，扩展了 SpeechCueLLM 的声学描述方法到维度情绪设置。
- **声学线索文本化**：从每个话语提取音量、音高、语速的集中趋势与变异度（共 6 个值），经分位数方案转为自然语言描述，避免架构修改。
- **跨模型全面比较**：覆盖 LLaMA、GPT、Qwen 三个系列共 6 个模型，统一在零样本、少样本和 LoRA 微调下比较，揭示领域自适应（而非模型规模）是性能差距主因。
- **参数高效微调**：采用 LoRA（r=16, α=r, AdamW, lr=3e-4, 15 epochs），在 IEMOCAP 小样本条件下降低过拟合风险。
- **消融与误差分析**：分离声学描述与对话上下文的贡献，并分析 VAD 维度不对称性与注释者一致性的关系。

### 实验或数据
- **数据集**：IEMOCAP，共 10,086 条话语、约 12 小时音频，仅使用音频和文本模态（未用视频）；采用 Leave-One-Subject-Out 划分，第 5 会话（未见说话人）作测试集。
- **离散情绪识别**：排除 Surprise、Fear、Others 三类后为 6 类，使用加权 F1 指标。
  - LoRA 微调 LLaMA 模型：71.8–73.2；Qwen3.5-35B：68.493；LLaMA-3.3-70B 零样本：60.299；GPT-4o-mini 少样本：56.8；GPT-5-mini 少样本：59.6。
- **VAD 评估**：采用 CCC 指标；最佳模型 Valence CCC = 0.7822（SOTA）。
- **消融**：去掉音频描述后，小模型加权 F1 下降 3.5–3.6，最大模型几乎无变化。

### 值得关注点
- LoRA 微调显著优于提示工程，即使被提示的模型规模更大（如 GPT-5-mini），说明任务自适应比模型容量更关键。
- 零样本 LLaMA-3.3-70B（60.299）与少样本 GPT-4o-mini（56.8）相当，提示规模可部分弥补缺乏微调。
- 声学描述在语言能力受限的小模型上价值最大，表明音频线索是语言不足时的补充信号。
- VAD 表现不对称性与 IEMOCAP 注释者一致性层次一致，提示任务难度差异可能源于标注本身。
- 开源模型与闭源模型在同一框架下公平比较，填补了 LLM 用于维度情绪评估的空白。

### 局限性
- 仅使用 IEMOCAP 单一数据集，且只用音频和文本模态，未利用该数据集包含的视频模态。
- Qwen 模型仅评估了离散情绪识别，未参与 VAD 维度评估；GPT 模型仅测试了提示条件（零样本/少样本），未进行微调。
- 未探索端到端音频-语言多模态 LLM（如 Qwen3-Omni、GPT-5.1、Gemini 3 Pro），因其计算开销大且对专用任务影响不确定。
- 声学特征仅覆盖音量、音高、语速三类，未纳入音色、语谱等其他可能相关的声学信息。

## 9. The Invisible Language Tax: Token Premiums of French and Regional Languages in 2026 LLM Tokenizers, and a French-Optimized Prototype

- Source: arxiv
- arXiv ID: 2609.39001
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.39001v1
- PDF: https://arxiv.org/pdf/2609.39001v1
- DOI: https://doi.org/10.48550/arXiv.2609.39001

### Authors

Thomas Serval

### Abstract

LLM services are billed per token and context windows are measured in tokens, yet the number of tokens needed for the same content varies across languages. We measure this token premium on seven tokenizers of widely used 2026 models (OpenAI o200k, Llama 3, Qwen3, DeepSeek V3/V4, Gemma 3, Mistral Tekken, and the Claude generation-5 tokenizer via Anthropic's counting API) on NTREX-128 (124 non-English reference translations) and on the Universal Declaration of Human Rights for regional languages. French requires 31% to 58% more tokens than English, whereas Simplified Chinese ranges from 5% fewer to 40% more and is cheaper than French on six of the seven tokenizers. Regional and overseas languages of France pay roughly 1.6 to 3.3 times the English count. We discuss how history re-sending, tiered pricing and fixed context windows amplify the absolute gap in agentic use. In a controlled experiment (BPE, Europarl, 50k vocabulary), adding French to tokenizer training data quickly reduces the premium, with diminishing returns and a growing cost for English. Finally, we present Baracoda FR v1.2, a byte-level BPE prototype with Tekken's vocabulary size. On a final test of six corpora never consulted during design, with a protocol declared fixed beforehand, it uses 11.5% fewer tokens than Tekken on French and 3.7% fewer on English; results hold after removing test sentences overlapping the training data and with an equal ordinary-token budget. It is worse on other languages and, at comparable vocabulary size, does not outperform CroissantLLM. These are segmentation results only; effects on model quality and task cost remain to be shown.

### 中文一句话结论
本研究量化了2026年主流LLM分词器中的“隐形语言税”：法语比英语多需31%–58%的token，法国地区语言比英语多需1.6–3.3倍，并提出了法语优化的原型Baracoda FR v1.2，将法语token数比Tekken减少11.5%，但对其他语言效果较差。

### English TL;DR
This paper quantifies the "invisible language tax" by showing French and regional languages require 31–58% and 1.6–3.3x more tokens than English across seven 2026 LLM tokenizers, analyzes economic implications, and introduces a French-optimized BPE prototype (Baracoda FR v1.2) that cuts French tokens by 11.5% vs. Tekken but underperforms on other languages.

### 中文详细总结
- **背景**：LLM按token计费，但同一内容在不同语言下的token数差异巨大，英语主导的训练数据导致非英语语言产生“token溢价”。
- **测量**：在7个2026年主流分词器（OpenAI o200k, Llama 3, Qwen3, DeepSeek V3/V4, Gemma 3, Mistral Tekken, Claude 5）上，用NTREX-128（124种非英语翻译）和UDHR（地区语言）测量。
- **关键结果**：
  - 法语溢价1.31–1.58倍（Tekken最低，Llama 3最高），中文溢价为0.95–1.40倍（6/7个分词器上比法语便宜）。
  - 法国地区语言（布列塔尼语、科西嘉语等）溢价1.6–3.3倍。
  - 经济影响：长上下文和智能体场景中，历史重发、分层定价和固定上下文窗口会放大绝对差距。
- **原型**：Baracoda FR v1.2（字节级BPE，Tekken词表大小），在6个未见测试集上比Tekken减少11.5%法语token、3.7%英语token，但其他语言更差，且未超过CroissantLLM。

### 方法 / 贡献
- **测量方法**：用平行语料（NTREX-128、UDHR），公式为`P_T(l)=token(l)/token(英语)`，NFC归一化，本地计数与官方实现交叉验证。
- **贡献**：(1) 更新7个2026年分词器的token溢价数据；(2) 法国地区语言溢价测量；(3) 法语溢价分解及训练数据中法语比例的受控实验；(4) 原型Baracoda FR v1.2，含预设协议的最终测试和词表大小匹配对比。

### 实验或数据
- **数据**：NTREX-128（124种非英语翻译）、UDHR（约390种语言）、Universal Dependencies（PUD, GSD, Sequoia, Rhapsodie, EWT, GUM）、Europarl、FineWeb/FineWeb-2。
- **实验**：
  - 7个分词器的token溢价比较（表格列出11种语言的溢价）。
  - 受控实验：在Europarl训练数据中加入法语，随比例增加，法语溢价下降但收益递减，英语成本上升。
  - 最终测试：6个设计时未见语料，协议事先固定，结果显示法语-11.5%、英语-3.7%（vs. Tekken），去除训练重叠后仍成立。

### 值得关注点
- **法语比中文更贵**：6/7个分词器上，法语溢价高于简体中文（中文最低0.95倍，法语最低1.31倍），挑战“中文token化更难”的常见认知。
- **长上下文放大效应**：历史重发使累计成本二次增长，分层定价导致法语更早跨过价格阈值（如Gemini模拟中法语在第29轮，英语在第41轮）。
- **原型创新**：Baracoda FR v1.2在法语和英语上均优于所有测试分词器（NTREX上英语51,452 vs. o200k 51,860 tokens），且词表更小。

### 局限性
- **仅限分词结果**：未评估对模型质量和任务成本的影响，需后续研究。
- **原型对其他语言差**：如中文token数比Tekken多2.1倍，西班牙语+29.8%，德语+38.3%。
- **未超过专用模型**：在可比词表大小下，未优于CroissantLLM。
- **数据限制**：NTREX和UDHR为新闻和通用文本，不代表所有领域；Claude 5仅测量法语和中文，通过API计数字符级开销可能引入误差。
- **受控实验条件有限**：仅用Europarl和50k词表，可能不能推广到更大数据或真实场景。

## 10. Lasting Effects of Abstract Pretraining Beyond Perplexity

- Source: arxiv
- arXiv ID: 2609.38764
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.38764v1
- PDF: https://arxiv.org/pdf/2609.38764v1
- DOI: https://doi.org/10.48550/arXiv.2609.38764

### Authors

Zachary Shinnick, Hemanth Saratchandran, Damien Teney, Anton van den Hengel

### Abstract

Language models are typically pretrained from random initialization. Recent work challenges this convention, showing that a brief warm-up on abstract, algorithmically generated data can provide a better starting point for subsequent learning of natural language. In this paper, we show that in small language models, such a warm-up improves specific capabilities that are not reflected in language-modeling perplexity. Our warm-up uses an abstract stack-manipulation task that requires compositional and state-tracking capabilities. Allocating as little as 1% of pretraining tokens to this data improves multi-hop question answering by up to 3.9 F1 points on MUSIQUE, with additional gains on HOTPOTQA and 2WIKIMULTIHOPQA despite comparable language-modeling perplexity. Controlled experiments show that the warm-up substantially accelerates the acquisition of deeper reasoning chains. We also explore what drives this transfer. First, the structure of the data matters: replacing the stack task with a queue fails to produce the same gains. Second, the gains are specific: performance improves on sequential reasoning chains, with no consistent benefit on tasks that combine or compare independent facts. Third, timing matters: mixing abstract data with natural language is far less effective than an initial dedicated phase, and exposure after pretraining completely removes the benefits. The early advantage persists through billions of subsequent language tokens. These results show that early abstract training can reliably shape the capabilities language models later acquire.

### 中文一句话结论
在小型语言模型的预训练中，仅用1%的抽象栈操作数据作为热身阶段，能够显著提升多跳推理能力，且该效果在语言建模困惑度上不体现，并持续保持。

### English TL;DR
A brief warm-up on abstract stack-manipulation data during pretraining improves multi-hop reasoning in small language models, with lasting effects that are not reflected in perplexity.

### 中文详细总结
该论文研究在小型语言模型的预训练早期阶段使用抽象数据（栈操作任务）进行热身的效果。传统上，语言模型从随机初始化开始预训练。作者发现，仅用1%的预训练令牌用于这种抽象数据，即可在MUSIQUE数据集上提升多跳问答F1分数3.9分，且在HOTPOTQA和2WIKIMULTIHOPQA上也观察到增益，尽管语言建模困惑度几乎未变。控制实验表明，热身加速了深层推理链的获取。进一步分析发现，数据结构（栈 vs. 队列）至关重要；增益具有特异性，主要影响顺序推理链，而非组合或比较独立事实的任务；时机也很关键：早期专属的热身阶段比混合训练或后续暴露更有效，且早期优势在数亿自然语言令牌后仍持续。

### 方法 / 贡献
1. **热身方案**：在标准自然语言预训练前，使用抽象栈操作数据（需组合与状态追踪）进行少量训练（1%令牌）。
2. **实证验证**：在多个多跳问答基准（MUSIQUE、HOTPOTQA、2WIKIMULTIHOPQA）上评估性能，并与困惑度进行对比。
3. **控制实验**：系统探究数据结构（栈 vs. 队列）、任务类型（顺序推理 vs. 组合比较）、以及热身时机（早期专属 vs. 混合 vs. 后期暴露）的影响。
4. **关键结论**：早期抽象训练能可靠塑造后续语言模型的能力，且效果持久。

### 实验或数据
**数据集**：MUSIQUE、HOTPOTQA、2WIKIMULTIHOPQA（多跳问答）。控制实验中使用栈操作与队列操作数据。**结果**：在MUSIQUE上提升最多3.9 F1，其他数据集也有增益。困惑度无显著差异。控制实验表明：栈优于队列；增益集中于顺序推理链；早期专属热身优于混合或后期暴露。

### 值得关注点
- 使用抽象数据（非自然语言）进行热身，仅1%令牌即带来显著推理提升，而不影响困惑度——这表明传统困惑度评估可能掩盖模型能力变化。
- 热身时机与数据结构的设计选择对最终效果影响巨大：早期专属阶段、任务结构与推理类型需严格匹配。
- 效果持久：早期优势经历数亿自然语言令牌后仍存，说明抽象数据奠定了基础性能力。

### 局限性
- 实验限于小型语言模型，结果未必直接推广至更大模型。
- 仅测试了多跳问答（顺序推理），其他任务（如组合推理）未显一致提升。
- 抽象数据类型仅探索了栈操作与队列，其他抽象数据（如算术、逻辑）未涉及。
- 未详细探讨热身数据量与模型规模的缩放规律。

## Processing Notes

- Duplicate papers skipped: 0