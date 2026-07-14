# Daily arXiv - 2026-07-14

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-14T23:13:58
- Paper count: 10

## 1. A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol

- Source: arxiv
- arXiv ID: 2607.11873
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.11873v1
- PDF: https://arxiv.org/pdf/2607.11873v1
- DOI: https://doi.org/10.48550/arXiv.2607.11873

### Authors

Esteban U. Vega Barajas

### Abstract

Institutions collect far more open-ended teaching-evaluation feedback than they read. A prior study introduced a validated protocol for classifying such comments by thematic category and sentiment, built from a documented annotation guide, an intra-annotator reliability measurement, stratified cross-validation, and a held-out evaluation on a Spanish institutional corpus with a frozen-encoder design. Two questions limit its reuse: whether a protocol fixed to 2019-era frozen embeddings stays competitive as representation methods advance, and whether it transfers to a second language. We re-run it on the original Spanish data across three representation generations, sparse lexical features, frozen transformer embeddings, and prompted large language models, and transfer its sentiment task to English with a balanced 45,000-comment corpus checked against an aspect-labeled education dataset. Treating paired comparisons as descriptive, we find the protocol durable: a 2026 frontier model posts the highest thematic F1 on the hardest Spanish task, yet shows no sentiment advantage over a cheap model and no descriptive separation from it on English, so model choice is a deployment decision, not a property of the method.

### 中文一句话结论
该研究验证了一个教学反馈分类协议在三种不同表征技术下具有持久性，并能将情感分析任务从西班牙语迁移到英语，但研究发现前沿大模型在情感分类上并不比廉价模型有优势，模型选择应视为部署决策而非方法特性。

### English TL;DR
The paper demonstrates that a validated teaching-feedback classification protocol remains durable across three representation generations and transfers sentiment to English, but model choice (even a 2026 frontier model) offers no sentiment advantage over a cheaper model, making it a deployment decision rather than a property of the method.

### 中文详细总结
本研究基于一项先前建立的西班牙语教学评价反馈分类协议，系统检验了其在技术演进和跨语言场景下的适用性。该协议包含书面注释指南、注释者内部一致性测量、分层五折交叉验证和固定编码器设计。研究者将该协议重新应用于原始西班牙语数据，跨越三代表征方法（稀疏词汇特征、冻结Transformer嵌入和提示大语言模型），并将情感分类任务迁移到英语，使用一个平衡的45,000条评论的语料库，该语料库对照了方面标注的教育数据集进行验证。研究发现协议具有持久性：2026年的前沿模型在最难的西班牙语任务上取得了最高的主题F1分数，但在情感分类上相比廉价模型没有优势，且在英语任务上与廉价模型没有描述性差异。因此，模型选择应被视为部署决策，而非方法本身的特性。

### 方法 / 贡献
1. **持久性基准测试**：在同一个西班牙语教学反馈语料库上，将相同的验证协议应用于三代表征方法（稀疏词汇特征、冻结Transformer嵌入、提示大语言模型），并报告F1分数及成本、延迟和可审计性。
2. **跨语言迁移评估**：将情感分类任务迁移到英语，设定了明确且狭窄的声明边界，并开发了经独立检查的星级到情感标注规则。
3. **可复现的英语情感样本**：从公开教学评价评论中提取并记录了45,000条平衡情感样本，包含构建脚本、种子和划分索引，确保精确可复现。

### 实验或数据
- **西班牙语数据**：来自瓜达拉哈拉大学SIIAU教学评价系统的44,707条有效开放式评论，包含1,165条标注子集。
- **英语数据**：从RateMyProfessor语料库中平衡采样45,000条评论（每类15,000条），划分为训练、开发和测试集。使用星级评分推导情感标签（≥4正面，≤2负面，其余中性）。
- **验证**：使用EduRABSA数据集（含3,000条教师评价）验证星级到情感规则，Cohen's κ = 0.66，准确率82%。
- **模型对比**：TF-IDF+SVC、BETO冻结嵌入+线性分类器、multilingual-e5-base冻结嵌入+线性分类器、Claude Haiku 4.5、Claude Opus 4.8、Qwen2.5-1.5B-Instruct。

### 值得关注点
- 2026年前沿模型（Claude Opus 4.8）在最难的西班牙语分类任务上表现最佳，但情感分类优势不显著。
- 廉价模型（Claude Haiku 4.5）与前沿模型在英语情感任务上无描述性差异。
- 研究专注于协议的验证而非模型性能竞赛，发现即使表征技术演进，协议本身仍保持有效。
- 研究严格区分了协议（方法）与模型（工具），认为机构应关注文档化的程序而非特定模型。

### 局限性
- 原始西班牙语标注仅由单一标注者完成，使用测试-重测内部一致性而非标注者间一致性。
- 英语情感标签基于星级评分推导，非人工标注，与人工标注的一致性仅为中等（κ=0.66）。
- 主题分类任务未迁移到英语，仅迁移了情感分类任务。
- 未涉及参数高效微调等适配方法。
- 合成或LLM生成的学生反馈数据被排除在主要实验之外。
- 英语语料库（RateMyProfessor）的语域与正式教学评价环境可能存在差异。

## 2. Index SLM Technical Report

- Source: arxiv
- arXiv ID: 2607.09885
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.09885v1
- PDF: https://arxiv.org/pdf/2607.09885v1
- DOI: https://doi.org/10.48550/arXiv.2607.09885

### Authors

Lusheng Zhang, Shien He, Tianxing Yan, Mengran Yu, Ziang Cui, Kai Zhao, Xiaojing Liu, Tianjiao Li

### Abstract

We present Index-1.9B, a series of open small language models developed at Bilibili. The series comprises four models: Index-1.9B-Base, a foundation model with 1.9 billion non-embedding parameters pre-trained on 2.8 trillion predominantly Chinese and English tokens; Index-1.9B-Pure, a control variant trained with an identical recipe but with all instruction-like data strictly filtered from the corpus; Index-1.9B-Chat, aligned from the base model with supervised fine-tuning and direct preference optimization; and Index-1.9B-Character, which augments the chat model with retrieval-augmented generation for few-shot role-playing customization. Pre-training employs a Warmup-Stable-Decay learning-rate schedule in which the concentration of curated data is raised substantially during the decay phase, together with a Norm-Head output layer that stabilizes training under large learning rates. On a suite of standard benchmarks covering examination, reasoning, mathematics, and code, Index-1.9B-Base attains an average score of 64.92, competitive with or exceeding open models of several times its size. We further report controlled studies on model depth, learning-rate magnitude and scheduling, the interaction between learning-rate decay and data quality, and the effect of including instruction data during pre-training, and we document an unexplained surge in benchmark performance midway through the constant-learning-rate phase. All models, together with evaluation code, are released at https://github.com/bilibili/Index-1.9B.

### 中文一句话结论
Bilibili 发布 Index-1.9B 系列开源小语言模型（1.9B 非嵌入参数，2.8T 中英 tokens 预训练），通过 Warmup-Stable-Decay 学习率调度和 Norm-Head 输出层，在多项基准上超越数倍规模的开源模型，并进行了深度、学习率、数据质量等系统性的控制实验。

### English TL;DR
Bilibili releases Index-1.9B, an open small language model series (1.9B non-embedding parameters, 2.8T tokens, mainly Chinese/English). It achieves competitive benchmark scores (avg. 64.92) against models several times larger, using a Warmup-Stable-Decay learning-rate schedule, Norm-Head output layer, and controlled studies on depth, LR, data quality, and instruction data impact. All models and evaluation code are open-sourced.

### 中文详细总结
本文介绍了 Bilibili 开发的 Index-1.9B 系列开源小语言模型。该系列包含四个模型：Index-1.9B-Base（基座模型，1.9B 非嵌入参数，在 2.8T 以中英文为主的 tokens 上预训练）、Index-1.9B-Pure（严格过滤指令数据后的对照版本）、Index-1.9B-Chat（经过 SFT 和 DPO 对齐的对话模型）和 Index-1.9B-Character（结合 RAG 支持少样本角色扮演自定义的版本）。预训练采用 Warmup-Stable-Decay 学习率调度，在衰减阶段大幅提升精选数据比例；同时使用 Norm-Head 输出层以稳定大学习率训练。在涵盖考试、推理、数学和代码的标准基准测试中，Index-1.9B-Base 平均得分 64.92，与数倍规模的开放模型相当或更优。论文还报告了关于模型深度、学习率大小与调度、学习率衰减与数据质量的相互作用、以及预训练中包含指令数据的影响等控制实验，并记录了在恒定学习率阶段中期出现的未经解释的基准性能突增。

### 方法 / 贡献
- 提出 Index-1.9B 系列四个模型（Base, Pure, Chat, Character），并全部开源。
- 预训练采用 Warmup-Stable-Decay 调度，衰减阶段大幅增加精选数据（含合理比例的指令数据）。
- 采用 Norm-Head 输出层，允许使用更大的学习率并稳定训练。
- 在固定参数量下，通过深度-宽度对比实验选择更深架构（36层）。
- 训练了一个紧凑的 BPE 分词器（65,029 tokens），针对中文优化并移除 Llama 式的前置空格。
- 控制实验：模型深度、学习率大小与调度、LR衰减与数据质量交互、预训练中包含指令数据的影响。

### 实验或数据
- 预训练数据：2.8T tokens，中英比例 4:5，代码占约 6%，含约 10% 的高质量精选数据（百科、论文、STEM 等）。经过偏差感知过滤、文档级 MinHash 去重和精确子串去重。
- 分词器压缩率比较（中文、英文、日文、韩文、代码），Index 分词器在混合语料和日韩语上表现最佳。
- 标准基准测试（考试、推理、数学、代码）：Index-1.9B-Base 平均 64.92，与 Qwen-1.8B, Gemma-2B 等模型对比。
- 控制实验：Norm-Head vs 其他归一化方法；不同深度/宽度配置；不同学习率和 Warmup-Stable-Decay vs Cosine 调度；有无指令数据预训练（Pure vs Boost）；以及恒定学习率阶段中期的性能突增现象。
- 论文未在单独章节列出完整数据集名称，但提及使用了 Bilibili 内部数据及 Common Crawl 等。

### 值得关注点
- 模型参数量仅 1.9B（非嵌入），但性能可与数倍规模模型竞争，体现了数据质量和训练策略的重要性。
- 公开了中间检查点（恒定 LR 阶段）和对照模型（Pure），便于研究训练动态。
- 日韩语压缩率显著优于同类分词器。
- 发现恒定学习率阶段中期出现意外的性能突增，但原因未明，值得进一步探究。
- 所有模型和评估代码已开源，支持学术和商业使用。

### 局限性
- 模型规模较小（1.9B），在复杂推理或超长上下文任务上可能仍有不足，但论文未直接测试或讨论。
- 恒定学习率阶段中期的性能突增现象“unexplained”，缺乏理论解释。
- 论文未披露完整的数据集来源或具体数据过滤阈值，可能影响复现。
- 仅在一个基准测试套件上评估，可能未覆盖所有下游任务（如多语言翻译、开放领域问答）。
- 未讨论模型在安全性、偏见或事实性方面的表现。

## 3. Large Language Models for Token-Efficient and Semantic-Preserving Opinion Summarization

- Source: arxiv
- arXiv ID: 2607.10825
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.10825v1
- PDF: https://arxiv.org/pdf/2607.10825v1
- DOI: https://doi.org/10.48550/arXiv.2607.10825

### Authors

Fabrizio Marozzo, Stefano Iannicelli

### Abstract

Opinionated text - spanning product reviews, hotel feedback, and social posts - captures rich signals about user experiences, preferences, and concerns. However, the scale, redundancy, and imbalance of such corpora make it challenging to analyze opinions effectively, particularly when the goal is to generate summaries that remain faithful to the diversity of viewpoints expressed. This paper presents a framework that preserves semantics in LLM-based opinion summarization while minimizing token usage. We combine multidimensional classification (e.g., sentiment, topics) with a family of stratified sampling strategies to select compact yet representative subsets of opinions before prompting the LLM. Tailored prompts then produce balanced summaries that surface the salient aspects expressed in the opinions (e.g., strengths and weaknesses of products/hotels). Experiments on Amazon product reviews, Tripadvisor hotel reviews, and X/Twitter posts demonstrate that our method significantly reduces token usage and computational cost while consistently outperforming traditional AI-based and standard LLM summarization baselines in terms of content coverage, balance, and semantic preservation.

### 中文一句话结论
本文提出一种结合多维分类与分层采样的框架，在保证语义完整性的前提下大幅减少LLM摘要所需的token数，并在多个评测集上取得更优的覆盖率和平衡性。

### English TL;DR
The paper introduces a framework combining multidimensional classification and stratified sampling to select compact yet representative opinion subsets before LLM summarization, significantly reducing token usage while improving content coverage and semantic balance.

### 中文详细总结
该框架旨在实现高效且语义保真的观点摘要。它由四个阶段组成：1) 数据收集（来自Amazon、Tripadvisor、Twitter/X）；2) 多维分类，包括情感、情绪、主题及领域特定维度，使用BERT、BERTopic等模型生成概率化标签；3) 分层采样，提出Knapsack、Knapsack-KL、KDE三种策略，在给定token预算下选择保持原始分布且信息密集的子集；4) 面向方面的提示生成，引导LLM输出覆盖各方面（如优缺点）的平衡摘要。实验表明，该方法在显著降低token使用量和计算成本的同时，在内容覆盖度、观点平衡性和语义保持方面一致优于传统AI摘要和标准LLM摘要基线。

### 方法 / 贡献
- 提出结合多维分类与分层采样的摘要前选择框架，有效缩小LLM输入规模并保持语义多样性。
- 引入三种分布感知的采样策略（Knapsack、Knapsack-KL、KDE），在token约束下最大化信息密度与分布保真度。
- 采用方面感知提示生成平衡摘要，覆盖情感、情绪、主题等多维度。
- 在三个不同领域数据集上验证了方法的通用性和有效性，并公开了代码。

### 实验或数据
- **数据集**：Amazon产品评论、Tripadvisor酒店评论、X/Twitter政治讨论帖子。
- **评估指标**：token使用量、内容覆盖度、观点平衡性、语义保持（通过主题覆盖率和摘要级余弦相似度等）。
- **基线**：传统AI摘要方法和标准LLM摘要方法。
- **结果**：框架显著降低token和计算成本，且在覆盖度、平衡性和语义保真度上持续优于基线。

### 值得关注点
1. 将多维分类（情感、情绪、主题等）纳入采样前预处理，而非单一维度过滤。
2. 提出三种不同的分层采样策略，提供灵活性以适应不同应用需求。
3. 在多个领域（电商、旅游、社交）验证了框架的鲁棒性和可迁移性。
4. 代码开源，有助于可重复研究和实际部署。

### 局限性
论文在摘要和提供的正文节选中未明确讨论局限性。根据方法特点，潜在局限包括：依赖多维分类器的准确性，分类误差可能传播到采样和摘要生成；采样策略基于预设的分类维度，可能无法捕捉所有细微的观点多样性；分类和采样步骤增加了额外的计算开销。

## 4. Efficiently Adapting Spoken Language Models for the Singaporean Context

- Source: arxiv
- arXiv ID: 2607.10092
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.10092v1
- PDF: https://arxiv.org/pdf/2607.10092v1
- DOI: https://doi.org/10.48550/arXiv.2607.10092

### Authors

Ng Jia Sheng Jason

### Abstract

Spoken language models (SLMs) unify speech perception and reasoning, but adapting them to sensitive domains is underexplored, especially when the original training data is inaccessible and the use case demands multilingual, spoken-query interaction. We adapt an open-source SLM to the Singaporean Home Team context across five speech tasks in Singapore's four official languages, combining LoRA fine-tuning, a surrogate text-QA dataset that guards against catastrophic forgetting, and a multi-task objective that adapts the CoBa reweighting scheme to speech. We also build HTD-multilingual-QA, a 504,853 sample multilingual QA dataset in text and spoken form. The resulting HT-Moonstone (5B) matches or outperforms SLMs up to 7x its size on most tasks, attains the best accent and gender recognition among all models evaluated, and loses under 2\% of its original speech QA ability.

### 中文一句话结论
本文提出了一种高效适应策略，结合LoRA微调、替代文本问答数据集和针对语音的多任务目标，将5B参数的开源口语语言模型适配至新加坡内政场景，在五个语音任务上匹配或超越高达7倍大小的模型，并保留超过98%的原始语音问答能力。

### English TL;DR
This paper proposes an efficient method combining LoRA fine-tuning, surrogate text-QA dataset, and a multi-task objective adapted for speech to adapt a 5B-parameter open-source spoken language model to the Singaporean Home Team context. The resulting model, HT-Moonstone, matches or outperforms models up to 7x its size across five speech tasks and retains over 98% of its original speech QA capability.

### 中文详细总结
本文针对将开源口语语言模型（SLM）适配到敏感领域（如新加坡内政安全场景）这一未充分探索的问题展开研究。挑战包括：原始训练数据不可访问、用例要求多语言口语查询交互。作者选择Voxtral-Mini-3B-2507作为基础模型，结合三种关键技术：LoRA参数高效微调、使用替代文本问答数据集（Nemotron-SFT-IF-Chat-v2）防止灾难性遗忘、以及将CoBa重新加权方案适配至语音的多任务目标。此外，作者构建了HTD-multilingual-QA数据集，包含504,853个文本和口语形式的多语言问答样本，覆盖新加坡四种官方语言（英语、华语、马来语、泰米尔语）。最终得到的HT-Moonstone（5B参数）在多数任务上匹配或超越高达7倍大小的SLM，在口音和性别识别任务上取得所有评估模型中的最佳结果，且原始语音问答能力下降不到2%。

### 方法 / 贡献
- **适应策略**：基于Voxtral-Mini-3B-2507，结合LoRA微调、替代文本QA数据集（Nemotron-SFT-IF-Chat-v2）防止遗忘、以及适配至语音的CoBa多任务重新加权方案。
- **数据集构建**：开发HTD-multilingual-QA（504,853样本），涵盖英语、华语、马来语、泰米尔语的口语问答数据，基于新加坡内政场景和人物角色生成，使用GPT-4o翻译用户轮次，OmniVoice进行语音克隆。
- **最终模型**：HT-Moonstone（5B参数），在五个任务（ASR英语、口音识别、性别识别、口语QA、语音QA）上表现优异。

### 实验或数据
- **基础模型选择零样本基准**：评估9个候选模型（3.5B-35B参数）在五个任务上的表现，基于Voxtral-Mini-3B-2507的WER（7.25）、语音QA准确率（76.4%）和长音频处理能力选择。
- **训练数据集规模**：总可用样本约17,127,050，包括ASR（英语496万、华语27.6万等）、口音和性别识别（各486万）、文本指令遵循（约106万）、会话QA（文本和口语各50.5万）。
- **HTD-multilingual-QA构建**：文本形式通过GPT-4o翻译用户轮次，口语形式通过OmniVoice语音克隆生成；约0.2%样本因语音克隆质量问题被移除。

### 值得关注点
- 在敏感领域（内政安全）中有效适配SLM，原始训练数据不可访问时使用替代数据集防止遗忘。
- 处理新加坡多语言（四种官方语言）和口语查询场景，构建首个多语言口语QA数据集。
- 5B模型匹配或超越7倍大小模型，展示参数高效微调在资源受限条件下的有效性。

### 局限性
- 依赖GPT-4o进行数据集翻译和评估评判，可能引入偏差或生成质量不一致。
- HTD-multilingual-QA数据集使用OmniVoice进行语音克隆，0.2%样本被移除，可能影响某些语言或口音的代表性。
- 模型主要在单一内政安全场景和新加坡语言环境下评估，泛化性至其他领域或语言尚待验证。

## 5. The First ChineseBabyLM Challenge: training data-efficient and cognitively plausible language models for Chinese

- Source: arxiv
- arXiv ID: 2607.10745
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.10745v1
- PDF: https://arxiv.org/pdf/2607.10745v1
- DOI: https://doi.org/10.48550/arXiv.2607.10745

### Authors

Siyuan Song, Zhiheng Qian, Yunhao Zhang, Linyang He, Xiaozhe Ji, Yingxin Lin, Hongao Zhu, Chongtian Shao, Chuhan Lang, Luan Li, Rui Wang, Renfen Hu, Shaonan Wang, Hai Hu

### Abstract

This paper describes the first ChineseBabyLM challenge, which will be held in the 2026 NLPCC conference. The challenge calls for researchers to train language models from scratch with 100 million Chinese tokens and evaluates the models on 3 tracks of tasks: NLU, cognitive alignment and Hanzi knowledge. There is no restriction on tokenizer, model architecture and the number of training epochs. Details of the challenge can be found in https://chinese-babylm.github.io/.

### 中文一句话结论
首个中文BabyLM挑战要求用1亿中文token从头训练语言模型，并在自然语言理解、认知对齐与汉字知识三个轨道上评估，旨在促进数据高效且认知合理的中文语言建模。

### English TL;DR
The first ChineseBabyLM Challenge requires training language models from scratch on 100 million Chinese tokens and evaluating them on NLU, cognitive alignment, and Hanzi knowledge tracks, with flexible choices for tokenizers, architectures, and training epochs.

### 中文详细总结
该挑战将在2026年NLPCC会议上举办。参赛者需使用不超过1亿中文token的语料（官方提供102M词的中文BabyBabelLM子集，或自建同等规模语料）从随机初始化训练模型。评估包含三个互补轨道：自然语言理解（含ZhoBLiMP等零样本任务和AFQMC等微调任务）、汉字知识（汉字结构与拼音的零样本判断）、认知建模（基于fMRI的词汇和篇章层级脑响应预测）。挑战不限制分词器、模型架构、训练轮次，并提供公开评估流程与基准系统。

### 方法 / 贡献
- **方法**：设计标准化的数据限制（1亿token）、三条评估轨道（NLU、汉字、认知）、三类评估格式（零样本最小对、微调分类、编码模型预测fMRI）。提供官方语料库、隐藏测试集和基准系统。
- **贡献**：首次为中文建立数据高效语言建模的社区评测；引入汉字结构/拼音知识与脑响应对齐作为评估维度；促进样本效率、认知合理性及中文特殊语言学问题的研究。

### 实验或数据
- **数据**：官方训练语料为BabyBabelLM中文部分（约1.02亿词），参赛者也可自建同等规模语料。
- **实验**：摘要和描述中未提供具体实验结果或基线系统性能；仅说明挑战设置、任务清单和评估协议。挑战尚在进行中，最终结果将于2026年公布。

### 值得关注点
1. 针对中文独特性（无词边界、表意文字、灵活句法）专门设计评估任务。
2. 首次在BabyLM挑战中纳入汉字知识（结构、拼音）和认知神经科学（fMRI）评估。
3. 零样本+微调+脑响应三种评估格式结合，全面衡量模型的语言能力与认知合理性。
4. 提供隐藏测试集（如XCOMPS-ZH、C3、诊断NLI、隐藏汉字任务），避免过拟合公开样例。

### 局限性
- 数据预算仅1亿token，可能不足以捕获复杂的中文语义和长尾语言学现象。
- 认知评估依赖fMRI数据，采集成本高、样本量有限（11-12人），泛化性存疑。
- 挑战当前仅描述设计，缺乏实际训练结果和模型比较，有效性需待后续参赛结果验证。
- 未对分词器、架构选择给出引导，可能增加比较难度。

## 6. Are LLMs ready for HardChoices?

- Source: arxiv
- arXiv ID: 2607.11471
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.11471v1
- PDF: https://arxiv.org/pdf/2607.11471v1
- DOI: https://doi.org/10.48550/arXiv.2607.11471

### Authors

Dmitry Nikolaev

### Abstract

A lot of research attention has been devoted to checking whether large language models (LLMs) are politically biased. This work has largely focused on high-level ideological dimensions, such as left--right or progressive--conservative, and it has been shown that while LLMs are predominantly left and progressive leaning, largely mimicking the biases in the training data, they can be to some extent steered to change their preferences in post-training. In this short note, we check if LLMs have robust stances with regard to major substantive societal issues, on which members of the same ideological camp are often in disagreement, summarised in a novel dataset \textsc{HardChoices}. We show that, faced with this line of questioning, LLMs, both large and small, surprisingly rarely declare neutrality, are often incoherent, and demonstrate a remarkable degree of agreement on issues where they do take stances.

### 中文一句话结论
大型语言模型（LLMs）在面对有争议的社会议题时，出人意料地很少保持中立，反而表现出显著的立场一致性和不连贯性，这与预期中更大或更对齐的模型会表现更好的假设相悖。

### English TL;DR
Given the novel HardChoices dataset, the authors find that LLMs rarely declare neutrality on contentious social issues but instead show striking agreement and sizeable incoherence, contradicting expected preferences for larger or more aligned models.

### 中文详细总结
该研究通过新数据集HardChoices，测试了多个大型语言模型对19个社会争议议题的立场。结果显示：模型很少保持中立，而是经常表现出不一致（incoherence），但在确实表明立场的问题上，不同模型之间有惊人的一致性。作者原本假设更大或更前沿的模型会表现得更中立或更一致，但事实恰恰相反，两个假设均被否定。例如，Mistral Small 24B几乎总是拒绝表态，而Grok 4.20则表现出极端的偏斜响应。只有三个模型（Llama 4 Scout 17B、GPT OSS 120B和Opus 4.6）较为一致地表明立场，且它们的立场高度一致，呈现出混合进步主义与自由主义的倾向。

### 方法 / 贡献
- 提出了一个新数据集HardChoices，包含19个非意识形态化、但在现代社会存在激烈争议的议题。
- 每个议题以两个对立陈述呈现，要求模型在5点李克特量表上选择立场。
- 通过交换A/B陈述顺序，检验模型的立场一致性（consistent）、中立（indifference）或不一致（inconsistent）。
- 对比了7个较小模型（～25-70B参数）和8个更大的前沿模型（通过API访问）。

### 实验或数据
- 共测试了19个议题，每个议题两种顺序，温度设为0。
- 模型包括：Olmo-3.1-32B, Gemma-3-27B, Mistral-Small-24B, Llama-4-Scout-17B, Llama-3.3-70B, Qwen2.5-72B, 以及Claude Opus 4.6, GPT OSS 120B, DeepSeek v3.2, Gemini 3.1 Pro, GPT 5.4, Grok 4.20等。
- 结果显示：较小模型中中立与立场数相近，但较大模型中不一致响应（尤其是同向偏斜）更多；只有Llama 4 Scout、GPT OSS 120B和Opus 4.6较为稳定地表明立场。

### 值得关注点
- 方法创新：通过两种顺序测试，检测模型的“方向性偏差”和立场一致性。
- 关键发现：前沿模型并不更中立或更一致，反而出现“弱支持最后选项”的偏斜（penultimate-option bias）。
- 三个立场明确的模型在大部分议题上高度一致，暗示LLMs存在某种共同的意识形态底层。

### 局限性
- 仅测试了部分模型，未能涵盖所有主流LLM；一些模型（如Nemotron、Minimax、GLM）因输出格式问题被排除。
- 温度设为0，未探索随机性对立场一致性的影响。
- 数据集仅19个议题，覆盖面有限，可能不足以代表所有社会争议。
- 未对模型内部机制进行深入分析，仅观察输出行为。

## 7. Polarization Detection: A Hybrid Approach with AfroXLMR-Social and DeBERTa for Low- and High-Resource Settings

- Source: arxiv
- arXiv ID: 2607.10312
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.10312v1
- PDF: https://arxiv.org/pdf/2607.10312v1
- DOI: https://doi.org/10.48550/arXiv.2607.10312

### Authors

Muhammad Abdullahi Said

### Abstract

The rapid proliferation of online polarization threatens social cohesion, necessitating robust automated detection systems that operate effectively across diverse linguistic contexts. This paper presents our system description for the POLAR Shared Task 2026, focusing on the detection and characterization of polarized discourse in English and Hausa. We propose a hybrid modeling strategy: for English binary detection, we leverage the monolingual strength of \textbf{DeBERTa}, while for Hausa and all fine-grained subtasks (Types and Manifestations), we utilize \textbf{AfroXLMR-Social}. This domain-adapted multilingual model proved critical for capturing the nuances of polarization in social media text. To further address computational constraints and data scarcity, we implement Low-Rank Adaptation (LoRA) and textual data augmentation via \texttt{nlpaug}. We report competitive results across all three subtasks, demonstrating that model selection tailored to specific subtask requirements yields the best balance of performance.

### 中文一句话结论
本文提出针对英语和豪萨语的极化检测混合策略，英语二分类使用DeBERTa，其他任务使用AfroXLMR-Social，结合LoRA和数据增强，在所有子任务上取得竞争力结果。

### English TL;DR
This paper presents a hybrid polarization detection system using DeBERTa for English binary tasks and AfroXLMR-Social for Hausa and fine-grained subtasks, enhanced with LoRA and data augmentation to achieve competitive results across low- and high-resource settings.

### 中文详细总结
本工作参加POLAR 2026共享任务，旨在检测和分类英语与豪萨语中的极化言论。作者采用混合建模：英语二分类（子任务1）使用DeBERTa-v3-base；豪萨语子任务和所有语言的细粒度分类（子任务2类型与子任务3表现）使用AfroXLMR-Social（在非洲社交媒体上领域自适应的多语言模型）。为缓解计算资源和数据稀缺，引入低秩适应（LoRA, r=8, α=16）冻结骨干网络，并通过nlpaug进行同义词替换和随机插入增强数据。训练使用5折交叉验证，损失函数：子任务1为二元交叉熵，子任务2和3为带Logits的二元交叉熵。最终在验证集上，英语二分类F1=0.7917，豪萨语二分类F1=0.8133；类型分类英语F1=0.3976、豪萨语F1=0.3276；表现分类英语F1=0.4979、豪萨语F1=0.2367。结果表明任务特定模型选择和领域自适应模型对细粒度任务至关重要。

### 方法 / 贡献
1. **任务特定模型选择**：英语二分类使用DeBERTa（单语强模型），豪萨语及所有细粒度子任务使用AfroXLMR-Social（社交媒体领域自适应多语言模型）。
2. **参数高效微调**：采用LoRA（秩8，缩放因子16）冻结预训练权重，仅训练低秩矩阵，适应低资源场景和有限GPU内存。
3. **数据增强**：使用nlpaug进行同义词替换和随机插入，缓解子任务3中的类别不平衡。
4. **5折交叉验证与集成**：对每个语言和子任务独立训练5个模型，通过软投票产生最终预测。

### 实验或数据
- **数据**：POLAR共享任务提供的CSV数据集，包含英语和豪萨语文本，分为二分类、多标签类型和多标签表现三个子任务。
- **预处理**：移除URL但保留表情符号和话题标签；最大序列长度128；使用XLM-R分词器。
- **训练配置**：批量大小16，学习率2e-5，训练5轮，优化器AdamW（权重衰减0.01，dropout 0.1）。全部在单张NVIDIA T4 GPU（16GB显存）上训练，每折约15-20分钟。
- **结果**（验证集平均F1）：
  - 子任务1（检测）：英语DeBERTa F1=0.7917，豪萨语AfroXLMR-Social F1=0.8133
  - 子任务2（类型，均用AfroXLMR-Social）：英语F1=0.3976，豪萨语F1=0.3276
  - 子任务3（表现，均用AfroXLMR-Social）：英语F1=0.4979，豪萨语F1=0.2367

### 值得关注点
- **AfroXLMR-Social的跨语言优势**：即使在英语细粒度任务上，AfroXLMR-Social也优于或匹敌单语模型，表明社交媒体领域自适应对极化检测通用有效。
- **混合策略的必要性**：英语二分类受益于强单语模型，而复杂子任务更需要社会语境理解，证明任务特定模型选择比利更强的通用模型更优。
- **LoRA在低资源场景的有效性**：在16GB GPU上成功微调大规模模型，且在多折集成中保持稳定性。

### 局限性
- **数据增强的语义漂移**：nlpaug的简单替换（如同义词替换）可能改变原文情感基调（如“regime”变为“government”），未来需探索保留语义的增强方法（如基于BERT的插入）。
- **细粒度子任务F1较低**：类型和表现任务F1普遍在0.3-0.5之间，尤其豪萨语表现分类F1仅0.2367，表明当前方法对少数类和复杂修辞形式的捕捉仍有困难。
- **仅针对两个语言**：方法尚未在其他低资源语言上验证，泛化性未知。

## 8. Metadata-Free Meta-Reweighted Direct Preference Optimization under Noisy Preference Labels

- Source: arxiv
- arXiv ID: 2607.09796
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.09796v1
- PDF: https://arxiv.org/pdf/2607.09796v1
- DOI: https://doi.org/10.48550/arXiv.2607.09796

### Authors

Hua Qu, Yifan Li, Xiaodong Yuan

### Abstract

Direct Preference Optimization (DPO) has become an important method for aligning large language models (LLMs) with human preferences because it removes the need for explicit reward modeling and reinforcement learning optimization. However, its performance depends heavily on the quality of preference data, and noisy preference data in real-world settings can weaken alignment performance. To address this issue, we propose a bilevel optimization framework and prove, under certain assumptions, that this framework can recover the DPO optimum under clean data. We further derive a prior form for the learnable weighting function under asymmetric label-flipping noise. Considering that high-quality metadata may be difficult to obtain, we propose a task-agnostic meta-knowledge-driven method that enables meta-learning even when metadata is completely unavailable. To reduce the high cost of higher-order gradients in LLM meta-learning, we combine central-difference approximation with LoRA fine-tuning and develop a scalable training scheme. Experiments on TL;DR summarization and Anthropic HH single-turn dialogue show that the proposed method improves training performance over multiple DPO baselines under different noise rates.

### 中文一句话结论
本文提出一种无需元数据、基于提示增强一致性的元加权直接偏好优化方法（PACMR‑DPO），在偏好标签存在噪声时能有效恢复 DPO 在干净数据下的最优解。

### English TL;DR
This paper proposes PACMR‑DPO, a metadata‑free meta‑reweighted Direct Preference Optimization method that uses prompt augmentation consistency as meta‑knowledge to robustly handle noisy preference labels. A bilevel optimization framework is theoretically justified, and central‑difference approximation combined with LoRA enables scalable training. Experiments on TL;DR summarization and Anthropic HH dialogue show improved performance under various noise rates.

### 中文详细总结
直接偏好优化（DPO）依赖偏好数据质量，实际中的噪声标签会降低对齐效果。本文从条件风险和后验偏移的角度出发，证明在理想假设下双层优化框架可以从含噪训练数据中恢复干净数据下的 DPO 最优解，并推导了非对称标签翻转噪声下可学习权重函数的先验形式。为摆脱对干净元数据的依赖，提出任务无关的提示增强一致性作为外层元知识，使元学习可在无元数据时进行。结合中心差分近似与 LoRA 微调降低高阶梯度开销，实现可扩展训练。在 TL;DR 摘要和 Anthropic HH 单轮对话上的实验表明，该方法在不同噪声率下优于多种 DPO 基线。

### 方法 / 贡献
- **理论证明**：在标签独立采样假设下，证明双层优化能从含噪训练数据恢复干净 DPO 最优解，为可学习权重提供理论基础。
- **无元数据元加权**：提出提示增强一致性（Prompt Augmentation Consistency）作为任务无关元知识，替代传统清洁元偏好标签，使元加权可在无元数据时进行。
- **高效训练**：利用中心差分近似在 LoRA 参数空间扰动，避免显式计算二阶梯度，大幅降低 LLM 元学习的内存与计算开销。
- **可学习权重先验**：导出非对称标签翻转噪声下权重比 \(g^+/g^-\) 的先验形式，提升权重设计的可解释性。

### 实验或数据
- 任务：TL;DR 摘要（Reddit 帖子摘要）和 Anthropic HH 单轮对话。
- 噪声设置：在偏好数据上施加不同比例的随机标签翻转噪声。
- 基线：与标准 DPO、cDPO、rDPO、Dr.DPO、ROPO 等多种方法对比。
- 结果：PACMR‑DPO 在中高噪声率下提升更显著（具体数值未在摘要中给出）。

### 值得关注点
1. **理论清晰**：给出双层加权 DPO 能校正噪声后验偏移的严格证明，区别于仅依赖经验特征的元学习方法。
2. **元数据豁免**：利用提示增强一致性构造外层目标，突破传统元加权对清洁元数据的需求，更贴合实际。
3. **训练效率**：中心差分 + LoRA 方案使 LLM 上的元学习可扩展，解决高阶梯度的高昂代价。
4. **任务无关性**：提示增强策略不依赖具体任务，具有通用性。

### 局限性
- 理论分析依赖于标签独立采样假设，实际中可能不完全满足。
- 实验仅在两个任务上验证，泛化至更广泛场景（如多轮对话、代码生成）尚需检验。
- 未讨论真实（非随机翻转）噪声模式下的表现，如标注偏差或对抗性噪声。
- 方法需要额外设计提示增强模板，且超参数（如噪声率估计、差分步长）可能需要针对任务调整。

## 9. Extending LLM Context via Associative Recurrent Memory

- Source: arxiv
- arXiv ID: 2607.11614
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.11614v1
- PDF: https://arxiv.org/pdf/2607.11614v1
- DOI: https://doi.org/10.48550/arXiv.2607.11614

### Authors

Gleb Kuzmin, Ivan Rodkin, Aydar Bulatov, Yuri Kuratov, Lyudmila Rvanova, Mikhail Katkov, Ilia Sochenkov, Misha Tsodyks, Timothy Baldwin, Mikhail Burtsev, Artem Shelmanov

### Abstract

Extending the context length of large language models (LLMs) is critical for many real-world applications, yet standard transformers remain constrained by quadratic compute and linear memory scaling. In this work, we investigate the Associative Recurrent Memory Transformer (ARMT) as a practical approach for enabling long-context processing in LLMs, constant memory scaling, and better efficiency. We make three main contributions. First, we construct two domain-specific long-context datasets designed to evaluate realistic workloads, focusing on narrow-domain fine-tuning scenarios. Second, we propose a comprehensive training recipe for ARMT-based context extension, combining continued pre-training, synthetic long-context data generation, curriculum learning, and selective integration of associative memory into chosen model layers. Third, we present an extensive experimental study demonstrating that ARMT-augmented models: (i) process inputs well beyond their original context limits without degrading performance relative to in-limit baselines; (ii) generalize more effectively to out-of-distribution context lengths; and (iii) need 30% less FLOPs while preserving baseline performance within the original context window.

### 中文一句话结论
本文通过关联记忆Transformer（ARMT）在1B参数规模的语言模型上实现了持续的内存开销和30%更少的计算量，使模型能够处理远超原有上下文窗口长度的输入。

### English TL;DR
This paper introduces the Associative Recurrent Memory Transformer (ARMT) to extend LLM context length with constant memory scaling and reduced computational cost, demonstrating through domain-specific datasets and a comprehensive training recipe that ARMT-augmented models process inputs beyond original limits, generalize to out-of-distribution lengths, and require 30% fewer FLOPs.

### 中文详细总结
本研究探讨了关联循环记忆Transformer（ARMT）作为扩展大语言模型上下文长度的实用方法。主要贡献包括：1）构建了两个面向特定领域的长上下文数据集，专注于窄领域微调场景；2）提出了一套基于ARMT的上下文扩展训练方案，结合持续预训练、合成长上下文数据生成、课程学习和选择性记忆层整合；3）实验证明ARMT增强模型能处理远超原始上下文限制的输入、更好地泛化到分布外长度，并在原始窗口内保持性能的同时减少30%的FLOPs。

### 方法 / 贡献
- 构建两个特定领域长上下文数据集（ManyTypes-long用于代码类型预测，GovReport-long用于文档问答）
- 提出完整训练方案：持续预训练、合成长上下文数据生成、课程学习（逐步增加段数）、选择性整合关联记忆层
- 改进ARMT实现以兼容DeepSpeed ZeRO Stage 3，实现高效训练

### 实验或数据
- 使用Gemma-3-1B-IT和SmolLM-2-360M-IT作为基础模型
- 构建数据集：ManyTypes-long（代码仓库堆叠）、GovReport-long（文档段落混合）
- 通过课程学习逐步训练：2段→4段→8段
- 评估指标包括内存使用、推理时间和任务性能

### 值得关注点
- ARMT实现恒定的GPU内存开销，与上下文长度无关
- 在32k长度下，ARMT仅需12GB GPU内存，而基线模型需约40GB
- 模型能处理超出原始上下文窗口的输入，且性能不下降
- 需要30%更少的FLOPs同时保持原始窗口内性能

### 局限性
- 实验限于1B参数规模及以下模型
- 数据集仅覆盖特定领域（代码和文档QA）
- 持续预训练仍需相当的计算资源
- 未评估在更大规模模型或更广泛任务上的泛化能力

## 10. Domain-Aware Scaling Laws Uncover Data Synergy

- Source: arxiv
- arXiv ID: 2607.11052
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.11052v1
- PDF: https://arxiv.org/pdf/2607.11052v1
- DOI: https://doi.org/10.48550/arXiv.2607.11052

### Authors

Kimia Hamidieh, Lester Mackey, David Alvarez-Melis

### Abstract

Machine learning progress is often attributed to scaling model size and dataset volume, yet the composition of data can be just as consequential. Empirical findings repeatedly show that combining datasets from different domains yields nontrivial interactions. For instance, adding code improves mathematical reasoning, while certain mixtures introduce interference that reduces model performance. We refer to these effects collectively as data synergy, where the contribution of multiple domains exceeds or falls short of the sum of their isolated contributions. In this work, we formalize and quantify data synergy in language model pretraining. Leveraging observational variation across open-weight LLMs with diverse pretraining mixtures, we estimate both direct domain-to-benchmark synergy (how one domain contributes to performance on another) and a second-order domain-domain synergy (capabilities that require co-occurrence of multiple domains). Our framework improves predictive accuracy over domain-agnostic scaling laws and recovers stable synergy estimates. We validate these estimates by training models on predicted optimal and predicted anti-optimal mixtures and confirm that our synergy estimates correctly predict performance rankings.

### 中文一句话结论
本文提出一种领域感知的缩放定律，通过形式化和量化语言模型预训练中的数据协同效应（即不同领域数据组合产生的非加性性能变化），显著提升了性能预测准确性。

### English TL;DR
This paper proposes domain-aware scaling laws that formalize and quantify data synergy in LLM pretraining, showing that combining data domains can yield non-additive performance effects, and validates the approach by predicting optimal data mixtures.

### 中文详细总结
本文聚焦于语言模型预训练中数据组成的影响，提出“数据协同”概念，指多个领域数据结合时产生的非加性贡献（协同增效或干扰减效）。作者构建了领域感知的缩放定律，包含两类协同：一是领域到基准的协同（某领域数据对另一基准性能的贡献），二是领域间协同（多个领域共存时产生的额外能力）。通过分析多种开源语言模型（具有不同预训练混合比例），该框架能比传统领域无关的缩放定律更准确预测性能。研究还通过训练模型在预测最优和次优混合数据上验证了协同估计的有效性。

### 方法 / 贡献
- 形式化定义了数据协同，区分第一阶（领域→基准）和第二阶（领域间）协同。
- 提出领域感知缩放定律，在标准缩放定律中加入协同系数（第一阶的γ和第二阶的σ），提升预测能力。
- 利用开源语言模型（如Huggingface模型）的观测变异，无需大量控制实验即可估计协同。
- 通过训练模型在预测最优和次优混合数据上验证了协同估计能正确预测性能排名。

### 实验或数据
论文使用开源语言模型（如Huggingface上的模型）的数据，包括参数数量、预训练总token数及各领域比例，但摘要未提及具体数据集名称或实验规模。验证实验涉及训练模型在预测最优和次优混合数据上，确认协同估计可正确预测性能排名。

### 值得关注点
- 首次形式化量化“数据协同”，超越了传统领域无关的缩放定律。
- 发现代码和数学领域间存在正协同（增强推理），而某些组合存在负协同（干扰）。
- 方法可提供可操作的见解，用于数据整理和获取策略优化。

### 局限性
- 基于观察数据（开源模型）而非完全控制实验，可能受未观测变量影响。
- 协同估计依赖模型多样性，若模型混合范围有限，估计可能不稳健。
- 实验验证仅涉及性能排名预测，未覆盖所有可能场景的泛化性。

## Processing Notes

- Duplicate papers skipped: 0