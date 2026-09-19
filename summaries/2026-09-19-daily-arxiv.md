# Daily arXiv - 2026-09-19

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-19T00:32:31
- Paper count: 10

## 1. Neo-Classic: A Benchmark for Evaluating Linguistic-Aesthetic Reasoning in Classical Chinese Poetry

- Source: arxiv
- arXiv ID: 2609.19154
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.19154v1
- PDF: https://arxiv.org/pdf/2609.19154v1
- DOI: https://doi.org/10.48550/arXiv.2609.19154

### Authors

Han Zhang, Zihan Gu, Zhiyuan Wang, Tianyi Ma, Jiacheng Lu, Xinyan Zhang, Yuhao Wei, Cheng Hua

### Abstract

While Large Language Models (LLMs) achieve high accuracy on established Classical Chinese Poetry benchmarks, it remains challenging to distinguish transferable Linguistic-Aesthetic Reasoning from reliance on familiar pre-training patterns. To address this issue, we introduce Neo-Classic, an evaluation benchmark that combines a constructionist Out-of-Sample (OOS) dataset with a suite of reverse understanding probes. Unlike traditional benchmarks that rely on verification or generation over historical corpora, Neo-Classic comprises strictly metrical poetry authored by contemporary experts, reducing the possibility of direct retrieval. We evaluate state-of-the-art models, including Qwen3-Max, Gemini-3-Pro, and DeepSeek-V3.2, across five behavioral probes designed to test hierarchical constraint satisfaction. Our results reveal two primary limitations. First, a performance gap of 20 to 50 percent emerges when models transition from historical to contemporary texts. Second, models exhibit substantial difficulties in discourse-level ordering tasks, with standard accuracy remaining low (0 to 13 percent). Although expert-level guidance improves the performance of reasoning-enhanced models to 36 percent, a notable gap with human experts persists. These findings suggest that while current LLMs capture local formal patterns, they struggle with global hierarchical planning required for robust Linguistic-Aesthetic Reasoning.

### 中文一句话结论
本文引入 Neo-Classic 基准，通过当代专家创作的严格格律诗歌揭示了大语言模型在古典诗歌语言美学推理上的“记忆幻觉”，并发现其存在20–50%的性能下降和全局规划能力的显著不足。

### English TL;DR
This paper introduces Neo-Classic, a benchmark combining a constructionist out-of-sample dataset with reverse understanding probes. Evaluating SOTA LLMs reveals a 20–50% memorization gap on contemporary poetry and near-chance performance (0–13%) on discourse-level ordering, indicating reliance on local patterns rather than global hierarchical linguistic-aesthetic reasoning.

### 中文详细总结
本文针对现有古典诗歌基准依赖历史语料、难以区分“记忆”与“推理”的问题，提出了 Neo-Classic 基准。该基准包含由当代专家严格遵循格律（如平仄、押韵、对仗）创作的 1,406 首原创诗歌，构成 Out-of-Sample 数据集，并设计了五类反向理解探针（如作者归属、词牌识别、词句匹配、句子重排等）共 41 个任务变体。通过对比历史与当代诗歌上的表现，研究定义了“记忆间隙”（Memorization Gap），用于量化模型对训练数据的依赖程度。实验评估了 Qwen3-Max、Gemini-3-Pro、DeepSeek-V3.2 等前沿模型，结果显示模型从历史切换到当代文本时性能下降 20–50%，且在律诗句子重排等需全局规划的任务上准确率仅 0–13%。即便加入专家级提示（CoT），推理增强模型也仅达到 36% 的准确率，仍与人类专家存在显著差距。

### 方法 / 贡献
- **方法**：构建了 Out-of-Sample（OOS）当代诗歌语料，采用两阶段审核（严格格律检查+语义标注）确保质量；设计了五类探针（作者识别、词牌识别、词元选择、对仗匹配、句子重排）将诗歌赏析转化为可量化的多选题和排序任务，并引入“记忆间隙”作为核心评估指标。
- **贡献**：① 提出首个基于当代专家原创诗歌的基准，杜绝直接记忆；② 实证展示 SOTA 模型存在显著记忆间隙，且随任务复杂度变化；③ 设计需全局规划能力的律诗句子重排任务，揭示模型在话语级结构推理上的根本局限；④ 通过与人类专家对比，证明当前 LLM 依赖表面模式而非抽象诗歌规则。

### 实验或数据
- **数据**：1,406 首当代诗歌（2010–2025 年由大学生和青年学者创作），严格符合《平水韵》/《词林正韵》；另含历史和辅助语料作为对照。
- **实验**：评估 Qwen3-Max、Gemini-3-Pro、DeepSeek-V3.2 等模型，覆盖 41 个任务、每任务 2,500 题（句子重排为 500 题）。结果显示：历史到当代切换时性能下降 20–50%；句子重排准确率仅 0–13%；CoT 提示下推理增强模型达 36%，但人类专家仍显著领先。

### 值得关注点
- 该基准首创“活语料”策略，避开预训练数据污染，直接测试泛化能力。
- 记忆间隙在不同任务上（如作者识别 vs. 对仗匹配）表现差异明显，提示模型局部风格提取优于全局规划。
- 句子重排任务（律诗）作为全局规划探针，暴露了 LLM 在话语逻辑（起承转合）与格律协同遵循上的短板。

### 局限性
- 当代诗作虽符格律，但语义主题现代，可能引入与历史诗歌的领域偏移，影响可比性。
- 人工创作质量难与古代大师完全对齐，尽管经严格审核，仍可能存在细微风格差异。
- 实验未覆盖所有提示策略或微调方案，CoT 效果有限，且未报告模型置信度或误差分析。
- 基准的 41 个任务中部分（如词牌识别）依赖韵律表面特征，可能低估模型深层语义理解。

## 2. Lens: Bringing the Right Semantic Perspective into Focus for Training-Free Multimodal Representation Learning

- Source: arxiv
- arXiv ID: 2609.20252
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.20252v1
- PDF: https://arxiv.org/pdf/2609.20252v1
- DOI: https://doi.org/10.48550/arXiv.2609.20252

### Authors

Xinran Liu, Shouqian Shi, Yixian Chen, Ruizhi Chen, Xin-Wei Yao, Sheng Zhong

### Abstract

High-quality representations are essential for a wide range of downstream tasks. Dedicated embedding models are explicitly optimized for representation learning, yet their training data are often more limited in scale and diversity than the massive corpora used to pretrain modern large language models and multimodal large language models. Large-scale pretraining and instruction following enable autoregressive models to select relevant evidence, integrate multimodal information, and infer semantics under different task perspectives, creating a distinctive opportunity for training-free representation learning. However, our analysis reveals that existing semantic-elicitation methods do not reliably orient the extracted states toward the semantic perspective required by the downstream task. Consequently, the resulting representations often remain dominated by salient input content. We characterize this problem as semantic perspective misalignment and propose Lens, a training-free framework that makes representation readout task-directed. Semantic Perspective Anchoring associates the task-required perspective with a task-specific readout phrase, specifying the interpretive role of the positions later used for extraction. Contextualized Phrase Readout places the same phrase after the complete input and aggregates its token states, combining full-context access with the anchored perspective. The resulting representation reflects task-conditioned evidence integration and inference rather than a generic summary of salient content. Without parameter updates, architectural modification, or reranking, Lens achieves an overall Precision@1 of 63.9 across all 36 MMEB datasets, outperforming the closest same-backbone training-free embedding baseline by 10.2 points.

### 中文一句话结论
Lens通过任务导向的语义视角锚定与上下文短语读取，无需训练即可将多模态大模型的表征对齐下游任务需求，在MMEB基准上达到63.9%的Precision@1。

### English TL;DR
Lens is a training-free framework that addresses semantic perspective misalignment in multimodal representation learning by anchoring task-required semantics to a readout phrase and using its contextualized states as the representation, achieving 63.9 Precision@1 on MMEB datasets and outperforming baselines by over 10 points.

### 中文详细总结
现有无训练表征学习方法从冻结的多模态大语言模型中提取隐藏状态，但这些状态往往被输入的显著内容主导，而非下游任务所需的语义视角。本文将此问题定义为“语义视角错位”，并提出Lens框架解决该问题。Lens包含两个组件：1）语义视角锚定——通过任务特定的读取短语将所需语义视角显式关联；2）上下文化短语读取——将该短语置于完整输入之后，聚合其令牌状态作为表征。该方法无需参数更新、架构修改或重排序，在所有36个MMEB数据集上取得63.9的Precision@1，比同骨干网络的无训练基线高出10.2分，在分类、VQA、检索和定位四类任务上均取得显著提升。

### 方法 / 贡献
- **问题定义**：首次系统定义语义视角错位问题，指出现有方法提取的表征与下游任务所需语义视角不一致。
- **方法创新**：提出Lens框架，包含语义视角锚定（通过任务特定读取短语明确语义角色）和上下文化短语读取（聚合短语令牌状态）两个关键组件。
- **核心贡献**：
  - 无需任何训练、架构修改或重排序，直接从冻结的自回归模型中提取任务导向的表征。
  - 在36个MMEB数据集上达到63.9 Precision@1，超越同骨干网络的无训练基线10.2分。
  - 提供组件消融、受控表征分析和定性案例验证机制有效性。

### 实验或数据
- **基准**：使用MMEB（Massive Multimodal Embedding Benchmark），包含36个数据集，覆盖分类（10）、视觉问答（10）、检索（12）和定位（4）四类任务。
- **评估协议**：所有任务统一为候选排序问题，报告Precision@1。
- **结果**：
  - 总体Precision@1 = 63.9，超过最接近的同骨干无训练基线（FreeRet-embed）10.2分。
  - 对比有训练方法（如VLM2Vec、MM-Embed等）仍具竞争力，且无需额外优化。
- **消融实验**：证实语义视角锚定和上下文短语读取各自不可或缺，移除任意组件均导致性能下降。

### 值得关注点
- **无训练且高效**：仅需对每个输入进行一次前向传播，无需梯度、架构修改或特征重排序，候选表征可预计算复用。
- **通用性**：统一框架适用于分类、VQA、检索、定位等多样化任务格式，无需任务特定训练。
- **可解释性**：通过改变读取短语与语义视角的关联，可系统调整表征焦点，验证了机制的有效性。
- **实际意义**：提供了一种利用已有多模态大模型作为通用表征提取器的轻量级方案，尤其适用于资源受限或需要快速部署的场景。

### 局限性
- **对冻结模型能力的依赖**：表征质量受限于冻结的多模态大模型本身的任务理解与推理能力，若模型对特定任务语义理解不足，Lens难以补偿。
- **提示工程敏感性**：语义视角锚定依赖于精心设计的任务指令、角色映射和读取短语，不同提示设计可能导致较大性能差异。
- **与有训练方法的差距**：虽然超越所有无训练基线，但仍略逊于大规模监督训练的最优有训练模型（如GME），说明参数更新在极端复杂任务上仍有优势。
- **仅评估单轮表征**：实验仅针对MMEB的候选排序协议，未探索生成式、交互式等更复杂下游任务场景。

## 3. YNU-HPCC at SemEval-2025 Task 11: Bridging the Gap in Text-Based Emotion Using Multiple Prediction Headers

- Source: arxiv
- arXiv ID: 2609.19238
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.19238v1
- PDF: https://arxiv.org/pdf/2609.19238v1
- DOI: https://doi.org/10.48550/arXiv.2609.19238

### Authors

Hao Yang, Jin Wang, Xuejie Zhang

### Abstract

This paper describes the participation of the YNU-HPCC team in subtask A of task 11, Bridging the Gap in Text-Based Emotion at SemEval-2025. Our best-performing system employs the RoBERTa (Robustly Optimized BERT Approach) model, an improved version of BERT that utilizes the Transformer encoder architecture. We enhanced the output head to allow the model to process one emotion simultaneously. We obtained the official ranking score (0.44), including results from all languages. The entire dataset was translated into English using Google Translate to facilitate subsequent processing. Through probabilistic and attention analyses, we found that (I) a single prediction head performs better than six heads predicting six emotions simultaneously, and (II) training on a uniformly translated English dataset yields better results than using the original dataset. The code is available at: https://github.com/BGWH123/Semeval-2025-task11.

### 中文一句话结论
YNU-HPCC团队在SemEval-2025任务11子任务A中，通过将多语言数据统一翻译为英语，并采用RoBERTa模型配合单情感预测头（每次只预测一种情感），取得了0.44的官方排名得分，且单预测头方案优于同时预测六种情感的多头方案。

### English TL;DR
The YNU-HPCC team's SemEval-2025 Task 11 system translates all data to English and uses a Transformer model (RoBERTa) with a single-emotion prediction head per output, finding that this approach outperforms simultaneous multi-emotion prediction, and yields better results than training on the original multilingual dataset. The official ranking score is 0.44 across all languages.

### 中文详细总结
本论文描述了YNU-HPCC团队参加SemEval-2025任务11子任务A（多语言文本情感检测）的方案。最佳系统采用RoBERTa模型（基于Transformer编码器的改进版BERT），并将输出头改造为每次只处理一种情感，即训练六个独立的情感预测模型（对应愤怒、厌恶、恐惧、喜悦、悲伤、惊讶），最后聚合损失。全部数据通过谷歌翻译转成英语。通过概率和注意力分析发现：（1）单预测头优于同时预测六种情感的多头方案；（2）在统一翻译后的英语数据集上训练比在原始多语言数据集上效果更好。最终官方排名得分为0.44（所有语言综合）。

### 方法 / 贡献
- 采用RoBERTa作为基础模型，并修改输出头为单情感预测（每次预测一个情感），而非同时预测多个。
- 将整个多语言数据集通过谷歌翻译统一转换为英语，以规避多语言模型在方言或低资源语言上的不足。
- 使用Focal Loss处理类别不平衡（如喜悦、悲伤样本较多，惊讶、厌恶较少），并引入R-Drop正则化稳定训练。
- 贡献：验证了“翻译为英语+单头预测”策略在多语言情感检测中的有效性，并通过消融实验证实该策略优于原始多语言数据和多头预测。

### 实验或数据
- 数据集：包含约60,000条训练样本，涵盖多种语言（如英语、阿拉伯语方言等），表2列出各情感频率（愤怒11459、厌恶10789、恐惧6761、喜悦13182、悲伤12311、惊讶7635），其中15,481条为中性/无关样本。
- 评估指标：子任务A采用F1分数。官方排名得分0.44（含所有语言结果）。
- 对比实验：比较了“一次预测完成”与“修改后的单预测头”在四个指标（准确率、F1、召回率、精确率）上的表现，单头+Focal Loss+R-Drop组合效果最佳（例如愤怒F1=0.701，恐惧F1=0.778）。

### 值得关注点
- **单预测头设计**：将输出层改为每次预测一种情感（共六个独立模型），而非传统多标签分类，显著提升性能。
- **翻译预处理**：统一翻译为英语后训练，结果优于原始多语言训练，表明跨语言情感分析中翻译+单语言模型的有效性。
- **正则化策略**：Focal Loss和R-Drop联合使用，有效缓解类别不平衡和训练不稳定问题。

### 局限性
摘要未明确讨论局限性，但可推断：（1）完全依赖机器翻译可能引入翻译错误或情感偏移；（2）仅使用单一预训练模型（RoBERTa），未探索更高效的多语言模型或混合架构；（3）实验仅局限于子任务A，未验证在其他任务或数据集上的泛化性。

## 4. Sampling Reveals Style: Unsupervised, Training-Free Discovery of Prompt-Conditional Stylistic Axes in LLM Activations

- Source: arxiv
- arXiv ID: 2609.19150
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.19150v1
- PDF: https://arxiv.org/pdf/2609.19150v1
- DOI: https://doi.org/10.48550/arXiv.2609.19150

### Authors

Ajit Mallavarapu, Ziwei Gu

### Abstract

Large language models (LLMs) encode rich stylistic structure in their hidden activations, but discovering which stylistic dimensions are salient for a given prompt typically requires supervised contrastive data. We present a training-free, prompt-conditional alternative: we repeatedly sample completions of a single prompt at elevated temperature, apply Principal Component Analysis (PCA) to the pooled hidden activations, and label the resulting axes automatically from the pole generations. We validate the discovered axes against 245 human-elicited stylistic annotations in a two-phase study. On our strongest model (Qwen-3.5-4B-Instruct), the top two axes match spontaneously requested human dimensions with 72.8% precision and 43.6% macro-recall, and 75.6% of validity ratings judge the axes' polar generations accurate to their labels, with 90.9% adjacent inter-annotator agreement. Discoverability is strongly model-dependent: both Qwen models and Llama-3.2-3B expose human-salient axes, while DeepSeek-7B-Chat drops to 35.3% precision, its leading components dominated by structural rather than stylistic variance. Simple PCA over a model's own decoding variance is thus an effective, low-cost probe of stylistic structure in LLM representations, one that also exposes sharp cross-model differences in how that structure is organized.

### 中文一句话结论
论文提出一种无需训练、无需监督数据的方法：对同一提示词高温采样多个补全，再对隐藏激活做 PCA，即可自动发现与提示相关的风格轴；在最强模型上，前两条轴与人类自发期望的风格维度匹配较好，但在 DeepSeek 等模型上会因结构方差压倒风格方差而失效。

### English TL;DR
This paper introduces a training-free, unsupervised method that samples multiple completions of a single prompt at high temperature, applies PCA to pooled hidden activations, and automatically labels the resulting stylistic axes. Human evaluations show the top axes align with spontaneously requested dimensions on some models (e.g., 72.8% precision for Qwen-3.5-4B-Instruct), but performance is strongly model-dependent, with DeepSeek-7B-Chat failing because structural variance dominates stylistic axes.

### 中文详细总结
- 核心问题：LLM 的隐藏激活中编码了丰富风格结构，但发现某个提示下哪些风格维度显著，通常需要监督对比数据。
- 方法思路：固定单个提示，以高温采样 N=30 个补全，收集模型倒数第二层的隐藏状态，做序列平均池化后构成矩阵，再对该矩阵做 PCA，取前两个主成分作为风格轴；随后用盲法 LLM judge 自动给轴的两极生成标签并对齐极性。
- 验证方式：两阶段人类评估，共使用 245 条人类 elicited 风格标注。第一阶段让标注者自发描述期望的“风格滑块”，检验自动发现的轴是否匹配人类意图；第二阶段让标注者判断轴两端的生成文本是否与自动标签一致。
- 主要结果：在 Qwen-3.5-4B-Instruct 上，前两条轴与人类自发维度的匹配精度为 72.8%，宏召回 43.6%；75.6% 的有效性评分认为轴的极性生成与标签准确对应，相邻一致性为 90.9%。
- 模型差异：Qwen 系列和 Llama-3.2-3B 能暴露人类显著风格轴；DeepSeek-7B-Chat 的精度降至 35.3%，其主成分被结构/语法方差主导，作者称之为“结构纠缠”（structural entanglement）。

### 方法 / 贡献
- 方法：Latent Engine 流程
  1. 变化云生成：固定提示，以 T=0.9、p=0.95 采样 30 条随机补全。
  2. 激活提取：取目标模型倒数第二层在生成 token 上的隐藏状态，做序列平均池化。
  3. PCA 分解：对 N×d 激活矩阵做 PCA，保留前两个主成分。
  4. 自动标注：用 Meta-Llama-3-8B-Instruct 在盲法下根据轴两端生成文本给出标签，并自动对齐正负极性。
- 贡献：
  1. 提出无需训练、无需对比数据的 prompt 条件式风格轴发现方法。
  2. 提供两阶段人类评估，证明发现的轴与人类自发意图一致且语义有效。
  3. 刻画了跨模型敏感性，包括 DeepSeek 中结构方差压倒风格方差的失败案例。

### 实验或数据
- 论文没有使用标准 benchmark 数据集，而是使用 245 条人类 elicited 风格标注进行两阶段人类评估。
- 评估模型：Qwen-3.5-4B-Instruct、Qwen-2.5、Llama-3.2-3B、DeepSeek-7B-Chat。
- Phase 1（自发匹配）：20 个提示 × 2 个成分 = 40 个自动维度；Qwen-3.5 精度 72.8%，宏召回 43.6%；DeepSeek-7B-Chat 精度仅 35.3%。
- Phase 2（极性有效性）：全局中位数 4.0/5.0；Top-2 Box 准确率 75.6%；平均精确一致性 57.5%；相邻一致性 90.9%；Wilcoxon 检验 p < 0.001。
- 额外细节：Qwen-3.5 的结果基于 9 个随机种子的稳健宏平均；语义匹配阈值 τ=0.65，并有 τ∈[0.40,1.00] 的敏感性扫描。

### 值得关注点
- 完全无监督、无需训练，仅靠模型自身解码方差和 PCA 就能发现可解释风格轴。
- 风格轴是 prompt 条件式的：针对不同指令，发现的轴会变化。
- 自动标注是盲法进行的，减少了模型族先验对标签的干扰。
- 发现“结构纠缠”现象：DeepSeek 的领先主成分主要编码结构/句法而非风格，说明不同训练/架构下风格与任务方差并不总是线性可分的。
- 方法低成本，可作为 LLM 表示中风格结构的快速探针。

### 局限性
- 模型依赖性强：在 DeepSeek-7B-Chat 上明显失效，说明方法不能普遍适用。
- PCA 只提取线性主成分，且只保留前两条轴，可能忽略非线性或较次要的风格维度。
- 自动标注依赖 LLM judge，存在“人机词汇差距”；评估使用 τ=0.65 的语义匹配阈值，虽然做了敏感性扫描，但阈值选择仍会影响结果。
- 人类评估规模有限：基于 245 条风格标注和 20 个提示/40 个自动维度，覆盖面可能不够大。

## 5. QVAC Genesis III: A Large-Scale, High-Quality Open Synthetic STEM Corpus for Efficient Language Model Pre-Training

- Source: arxiv
- arXiv ID: 2609.19513
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.19513v1
- PDF: https://arxiv.org/pdf/2609.19513v1
- DOI: https://doi.org/10.48550/arXiv.2609.19513

### Authors

Davide Vitabile, N. Ranjan, Akshay Nambiar, Kamal K. Gupta, Amril Nazir

### Abstract

High-quality pre-training data is a critical bottleneck for educational and STEM-specific language models targeting edge AI and on-device deployment where token budgets are tightly constrained. While major organizations train ever-larger models on private corpora, the open ecosystem lacks STEM-focused synthetic datasets that deliver high per-token learning value efficiently for small models. To address this gap, we introduce QVAC Genesis III, a 191.43B-token, STEM-focused multi-domain synthetic corpus covering 19 domains across several difficulty levels and different educational styles. QVAC Genesis III is built via a dual generation strategy that performs targeted teacher distillation using a weak edge-scale student model as signal: the student's failures are converted into corrective explanations, while its successes are expanded into contrastive option-level reasoning over all answer choices. We further introduce an LLM-as-a-parser evaluation protocol that extracts final answers from free-form outputs and tracks both accuracy and answer validity. To validate the effectiveness of our QVAC Genesis III data, we conduct controlled from-scratch ablations with 1.7B-parameter models, showing that models trained with QVAC Genesis III consistently outperform both models trained with the open-source synthetic corpus Cosmopedia-v2 and the publicly released Cosmo-1B model across ARC, GPQA Diamond, and MMLU STEM benchmarks, achieving up to +28.57% on ARC-E and +21.35% on ARC-C, while reaching a Valid Answer Rate of up to 99.45%.

### 中文一句话结论
QVAC Genesis III 是一个包含 1914.3 亿个令牌（191.43B-token）的开放 STEM 合成语料库，通过双路径生成策略显著提升了小参数语言模型在 STEM 基准测试上的表现，并实现了最高 99.45% 的有效答案率。

### English TL;DR
QVAC Genesis III is a 191.43B-token open synthetic STEM corpus that uses a dual generation strategy—converting student failures into corrective explanations and successes into contrastive reasoning—to achieve significant token efficiency gains and outperforms existing baselines on STEM benchmarks for small language models.

### 中文详细总结
该研究针对边缘 AI 和端侧部署场景下 STEM 语言模型预训练数据质量不足的问题，提出了 QVAC Genesis III 语料库。该语料库涵盖 19 个领域和三个难度级别（高中、大学、研究生），通过双重生成策略构建：失败分析（FA）管道将学生模型的错误答案转化为针对性纠正解释，选项级（OL）推理管道则对成功案例进行全面选项推理。研究还引入了 LLM-as-a-parser 评估协议，使用专门训练的解析器从自由文本中提取答案，同时报告准确率和有效答案率。通过 1.7B 参数模型的从头训练消融实验，验证了该语料库相比现有开源合成语料库的优势。

### 方法 / 贡献
- 提出了 191.43B 令牌的开放 STEM 合成语料库 QVAC Genesis III，覆盖 19 个领域
- 创新性双路径生成策略：失败分析管道（将错误转化为教学信号）和选项级推理管道（对所有选项进行对比解释）
- 引入 LLM-as-a-parser 评估协议，解耦格式可靠性评估与领域知识评估
- 采用教师-学生蒸馏框架，使用 QwQ-32B 作为教师模型，Qwen3-1.7B-Base 作为学生模型
- 生成内容采用四种风格（教科书、网页文章、问答、对话）以最大化多样性

### 实验或数据
- 使用 FineFineWeb 作为种子数据源，通过 Ultra-FineWeb 分类器进行质量过滤
- 进行 1.7B 参数模型的从头训练消融实验
- 对比基线：Cosmopedia-v2 和 Cosmo-1B 模型
- 评估基准：ARC、GPQA Diamond、MMLU STEM
- 关键结果：ARC-E 上提升高达 +28.57%，ARC-C 上提升 +21.35%，有效答案率达到 99.45%

### 值得关注点
- 开源发布：数据已发布在 HuggingFace（qvac/GenesisIII），代码在 GitHub（tether-ai-research/qvac-genesis-III）
- 将传统上被丢弃的错误信号转化为高质量训练数据，这是数据利用效率的重要创新
- 针对 1-2B 参数小模型的独特优化，特别适合边缘部署场景
- 使用 32B 教师模型（QwQ-32B）实现高吞吐量下的有效蒸馏

### 局限性
- 摘要和主要文本未涉及对失败分析或选项级推理独立贡献的消融分析
- 未提及跨领域泛化能力或更小/更大规模模型的实验验证
- 未讨论生成数据可能引入的教师模型偏差或数据重复问题
- 未提供关于 191B 令牌数据的生成成本和计算资源消耗的具体信息

## 6. Is It Still Worth Training a Classical Model in the Era of LLMs? A Crossover Benchmark on Tabular Data

- Source: arxiv
- arXiv ID: 2609.20218
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.20218v1
- PDF: https://arxiv.org/pdf/2609.20218v1
- DOI: https://doi.org/10.48550/arXiv.2609.20218

### Authors

Kaihua Ding

### Abstract

Large language models can label a tabular row from a plain-English description with no training - a capability now shipping in mainstream spreadsheet tools such as Microsoft Copilot in Excel and Anthropic's Claude for Excel - raising a practical question for the many business prediction problems where labels are expensive: should you prompt a frozen LLM, or collect data and train a model - and if so, how much data? We quantify the answer with the labeled-data crossover N*, the training-set size at which a trained classical model's learning curve overtakes a frozen LLM's training-free (and therefore flat) error. Aggregating 126 independent student evaluations of small GPT models under eight prompting configurations across 18 tabular datasets, paired with authoritative power-law learning curves for six classical model families, we find that training wins fast: even given an oracle choice of its best prompt configuration, a trained classical model beats the small frozen LLM using no more labeled data than is already on hand in 86% of cases, and wins by the smallest labeled subset we evaluate in 40%, with the observed crossover at a median of ~6% of the training set. In-context few-shot examples do not behave like training - error versus shot count does not follow a power law - and the same protocol re-run by independent implementers varies with a coefficient of variation of 0.148. A controlled probe indicates the LLM depends on recognizable feature-name semantics, which plausibly makes our crossover a conservative estimate (we do not claim memorization). For a typical business table, the evidence is clear: collect a few hundred labels and train a gradient-boosted model.

### 中文一句话结论
训练一个经典模型（如梯度提升树）在表格数据上始终优于使用冻结的大语言模型，仅需收集几百个标签（中位交叉点在训练集的约6%），因此对于典型商业预测问题，推荐收集数据并训练模型。

### English TL;DR
Training a classical model on tabular data consistently outperforms a frozen large language model after collecting only a few hundred labels (median crossover at ~6% of the training set), making data collection and training the recommended approach for typical business prediction problems.

### 中文详细总结
本文针对一个现实部署问题：在标签昂贵的商业预测中，应该选择直接提示一个冻结的大语言模型（如GPT-4.1-nano/mini），还是收集标签并训练一个传统模型？作者定义了“标签数据交叉点”N*，即训练集规模达到多少时，经典模型的学习曲线误差开始低于冻结LLM的固定误差。通过聚合126名学生在18个表格数据集上的独立评估（8种提示配置），并结合6种经典模型家族（如梯度提升、随机森林）的幂律学习曲线，发现训练获胜很快：即使给出最优提示配置，经典模型在86%的场景下使用已有标签即可超过LLM；在40%的场景下，经典模型在最小标签子集（约1%训练集）时就已胜出；中位交叉点仅为训练集的6%。研究表明：少样本上下文示例不表现出幂律学习行为；同一协议在不同实现者间存在0.148的变异系数；LLM依赖于可识别的特征名称语义，这提示交叉点可能是保守估计。结论清晰：对于典型商业表格，应收集几百个标签并训练梯度提升模型。

### 方法 / 贡献
1. **定义量化指标**：引入标签数据交叉点N*，作为训练集规模阈值，在阈值处经典模型的误差低于冻结LLM的固定误差。
2. **大规模学生实验**：126名学生独立实现，覆盖18个数据集×8种LLM提示配置（2个模型×2种序列化方式×2种shot设置），每个配置有16-29次独立复制，提供replication-scale的误差方差。
3. **经典学习曲线**：来自另一学生研究，为6种经典模型家族拟合幂律曲线 $\mathrm{error}(N)=aN^{-b}+c$，并设置可靠性过滤（$R^2>0.5$, $0<b<3$, 收敛），保留70/80组可靠曲线。
4. **交叉分析**：对每个(数据集,经典模型,LLM配置)计算N*，并以oracle-best配置为保守基准。
5. **理解LLM行为**：通过少样本实验、交叉验证方差分析、以及特征名称/值替换的受控探针，揭示LLM依赖精确值和可识别语义，并非泛化推理。
6. **实用资源**：发布聚合曲线、交叉表及代码，支持从业者决策。

### 实验或数据
- **数据集**：18个标准表格数据集（10个分类、8个回归），来自UCI、Kaggle等，主题包括金融、HR、营销、医疗、房地产等，样本量从303到53,940行。
- **LLM评估**：2种模型（gpt-4.1-nano, gpt-4.1-mini）×2种序列化（key-value vs. natural language）×2种shot（0-shot vs. 5-shot）=8种配置。每个学生负责3个数据集，每个配置在固定测试集（≤100行/数据集）上评估，共约3,000个评估单元，每个单元由16-29次独立实现。
- **经典模型**：分类使用Boosting、RandomForest、SVM、LinearModel；回归追加Ridge、Lasso。学习曲线通过另一个学生研究获取，拟合幂律。
- **度量**：分类用AUROC（error=1−AUROC），回归用RMSE/std(y_test)，均将完美预测设为0。
- **交叉计算**：对每个(数据集,经典模型,LLM配置)求解 N*=(a/(e_LLM-c))^(1/b)。当 e_LLM ≤ c 时，经典永不超越；当 N* < N_min 时，经典从一开始就胜出。

### 值得关注点
1. **训练获胜快速而普遍**：86%的（数据集,经典模型）组合下，经典模型使用已有标签即优于oracle-best提示的LLM；40%的情况下，经典模型在最小评估子集（~1%训练集）时即已获胜；中位交叉点仅需~6%训练集（约几百标签）。
2. **少样本不等于训练**：少样本（1-20 shots）的误差-样本数关系不服从幂律（仅10%案例R²>0.8，中位指数≈0），说明上下文示例不是有效监督信号。
3. **结果复制存在噪声**：同一协议在不同实现者间的LLM误差变异系数中位数为0.148，影响交叉点的稳定性。
4. **LLM依赖语义而非推理**：受控探针显示，将特征值替换为易读的十分位数后LLM性能大幅下降（而同样分箱训练的传统模型保持不变），匿名化特征名称效果较弱不一。这表明LLM的性能可能主要来自识别熟悉的特征语义，而非真正的预测能力，因此给出的交叉点估计可能是保守的（对LLM有利）。
5. **实践建议明确**：对于典型商业表格，直接收集几百个标签并训练梯度提升模型是更优选择。

### 局限性
1. **LLM范围有限**：仅评估小型、低成本的GPT-4.1系列模型（nano/mini），未涵盖前沿模型（如GPT-4.1）或微调模型，也未包括其他LLM家族（如Claude、Llama）。对更大模型的结果仅作建议性补充。
2. **提示配置局限**：只测试了8种优化的提示配置（两种序列化、两种shot数），未穷举所有可能的提示策略（如系统角色、不同示例选择等），实际表现可能因提示方式不同而变化。
3. **数据集选择偏差**：使用的是公开的、标签完善的基准数据集，可能不能完全代表现实商业表格（如特征含义明确、分布稳定）。作者指出LLM依赖于熟悉的特征语义，这可能在隐私或专有数据场景下失效。
4. **经典模型未进行超参数调优**：经典模型家族使用默认或标准拟合，未进行超参数搜索，实际部署中调优可能进一步降低交叉点。
5. **污染问题未彻底解决**：论文承认公开数据集可能被LLM预训练记忆，但仅通过探针间接评估，未提供确凿证据。作者认为这使交叉点保守，但无法完全排除记忆对结果的系统影响。
6. **交叉点计算依赖可靠拟合**：10/80组经典曲线因$R^2$、指数或收敛标准被排除，这些数据集上无法给出交叉点结论。
7. **未考虑主动学习或数据增广**：实际场景中可能通过主动学习或生成式增广减少标签需求，本文的推荐基线仅基于严格随机下采样。

## 7. Can Data Attribution Filter Out Subliminal Learning? Not Reliably

- Source: arxiv
- arXiv ID: 2609.20027
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.20027v1
- PDF: https://arxiv.org/pdf/2609.20027v1
- DOI: https://doi.org/10.48550/arXiv.2609.20027

### Authors

Moritz Weckbecker, Sweta Jena, Jonas Müller, Ponnurangam Kumaraguru, Sebastian Lapuschkin, Wojciech Samek, Louis Jaburi, Gonçalo Paulo

### Abstract

Subliminal learning allows language models to transmit behavioral traits through training data with no obvious semantic relationship to those traits, undermining content-based data filtering as a safety intervention. Training data attribution offers an alternative: it identifies the training examples responsible for a given model behavior, independent of their semantic content, and so may apply in exactly the cases where semantic inspection fails. We evaluate three gradient-based attribution methods (GradCos, a contrastive GradCos variant, and EK-FAC) across three models, comparing them against divergence tokens, a strong baseline previously shown to localize subliminal learning (albeit one that requires access to counterfactual teacher models). Filtering at the token level, EK-FAC mitigates a significant part of the effect, the other methods provide little benefit, and all mostly fall short of divergence tokens. Filtering entire samples is less effective for every method, though EK-FAC often gives a stronger signal than divergence tokens in this setting. Success is inconsistent across methods and settings: variants that work well for some model-preference combinations fail for others, and we do not identify a consistent explanation for these differences. Our results suggest that gradient-based attribution can identify data responsible for subliminal learning in some settings, but that some approximations are more reliable than others.

### 中文一句话结论
基于梯度的数据归因方法（尤其是EK-FAC）能在部分场景下部分缓解语言模型中的“ subliminal learning”，但其效果因模型和目标而异，且整体上不如基于发散词（divergence tokens）的强基线可靠。

### English TL;DR
Gradient-based training data attribution methods, particularly EK-FAC, can partially mitigate subliminal learning in language models by filtering tokens or samples, but their effectiveness is inconsistent across models and targets, and they generally underperform the divergence token baseline.

### 中文详细总结
该论文评估了三种基于梯度的训练数据归因方法（GradCos、对比GradCos变体和EK-FAC）在过滤“ subliminal learning”（隐性学习）数据时的有效性。研究发现，在token级别的过滤中，EK-FAC能够显著缓解部分效应，但其他方法效果有限，且所有方法整体上不如发散token基线。在样本级过滤中，所有方法效果更差，但EK-FAC有时提供比发散token更强的信号。成功与否在不同方法和设置间不一致，且未找到一致的机制解释归因差异。

### 方法 / 贡献
- **方法**：使用三种梯度归因方法（GradCos、GradCos-diff、EK-FAC）对token和样本打分，并与发散token基线对比。在3个开源模型（Llama-3.2-1B、Qwen2.5-3B、OLMo-3-7B）上，通过教师模型生成数字序列数据注入动物偏好，进行累积过滤和分位数训练。
- **贡献**：
  1. 系统评估梯度归因在 subliminal learning 过滤中的有效性。
  2. 发现token级过滤通常优于样本级过滤。
  3. EK-FAC在部分设置下接近但未超过发散token基线的性能。
  4. 揭示方法效果依赖于模型和目标任务，缺乏通用性。

### 实验或数据
- **模型**：Llama-3.2-1B-Instruct、Qwen2.5-3B-Instruct、OLMo-3-7B-Instruct。
- **任务**：注入目标动物偏好（狗、大象等），评估过滤后模型响应率。
- **实验**：包括累积过滤（0.1-0.9比例）、分位数训练、token级和样本级过滤。每个设置重复10次训练，计算平均响应率。
- **数据**：教师模型生成的数字序列，排除直接提及目标的样本。查询集分为短回复（人工合成）和长回复（偏置模型生成）。

### 值得关注点
- **token vs 样本**：token级过滤显著更有效，因为归因信号集中在稀疏token上，样本级聚合会破坏信号。
- **EK-FAC的优势**：在样本级过滤中，EK-FAC有时显著优于发散token基线，但在token级不如后者。
- **不可靠性**：方法有效性高度依赖模型和目标，无统一规律。例如，dog目标在Qwen上过滤效果明显，而elephant效果弱。
- **度量标准**：使用最高/最低十分位差异（归一化）评估归因质量，显示样本级归因质量远低于token级。

### 局限性
- **性能不稳定**：归因方法在不同模型-目标组合下表现不一致，无法可靠替代发散token基线。
- **未提供解释**：未能找到归因方法为何在某些设置下有效或失效的一致原因。
- **计算成本**：梯度归因方法（如EK-FAC）计算开销大，且需要访问模型内部表示，限制了实际应用。
- **范围有限**：仅基于三种模型和有限目标，未覆盖更广语言模型或更复杂 subliminal 场景。

## 8. Why Pretraining Fails to Share Cross-Lingual Knowledge

- Source: arxiv
- arXiv ID: 2609.19291
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.19291v1
- PDF: https://arxiv.org/pdf/2609.19291v1
- DOI: https://doi.org/10.48550/arXiv.2609.19291

### Authors

Adam Gaber, Uriel Dolev, Elisabeth Fittschen, Bobby Cheng, Yuval Marton, Leshem Choshen

### Abstract

Large Language Models (LLMs) have made remarkable progress in the processing and modeling of many languages. Yet, unlike human multilinguals, they exhibit surprisingly limited cross-lingual knowledge transfer. While this limitation is well documented, its origins during multilingual training remain unclear. We pretrain 360M- and 7B-parameter LLMs and show that poor cross-lingual knowledge generalization emerges during pretraining and persists under standard interventions. To isolate its cause, we employ a controlled bilingual pretraining setting using two copies of the same language, sharing identical text and token segmentation, but mapped to disjoint token spaces. We find that disjoint tokens alone are enough to induce knowledge compartmentalization, even between identical copies of the same language, establishing disjoint token spaces as a fundamental barrier to cross-lingual knowledge generalization. Guided by this understanding, we suggest mapping languages into a shared token space by simple word-wise translation and find it substantially improves cross-lingual knowledge generalization, recovering up to 12.6\% of native-language learning efficiency --- 14$\times$ the baseline.

### 中文一句话结论
预训练期间，语言间知识未能共享的根本原因是不同语言使用不相交的词元空间；通过简单的逐词翻译将语言映射到共享词元空间，可显著提升跨语言知识泛化能力。

### English TL;DR
Disjoint token spaces between languages are a fundamental barrier to cross-lingual knowledge transfer in LLMs, and mapping languages into a shared token space via word-wise translation substantially improves cross-lingual knowledge generalization, recovering up to 12.6% of native-language learning efficiency (14× the baseline).

### 中文详细总结
该论文研究了大型语言模型（LLMs）在预训练阶段跨语言知识泛化失败的原因。作者通过受控的双语预训练实验发现，即使两种语言在文本和词元分割上完全相同，只要它们被映射到不相交的词元空间中，模型就会表现出知识的“分区化”（compartmentalization），即知识无法跨语言共享。这一现象在360M和7B参数规模的模型中均存在，且标准干预措施无法消除。作者提出了一种简单有效的干预方法——逐词翻译（WWT），将不同语言的词元空间统一，从而显著提升跨语言知识泛化能力，恢复了原生语言学习效率的12.6%，是基线的14倍。

### 方法 / 贡献
- **受控预训练环境**：引入虚构知识数据集（FKD），在预训练中精确控制事实在不同语言中的暴露次数，从而可靠追踪知识获取情况。
- **跨语言等价性（Ceq）分数**：提出一个指标，量化在语言B中接触事实对在语言A中回忆该事实的增益，相对于母语暴露的比值，从而隔离转移增益与整体能力差异。
- **实验设计**：使用两种语言（英语-阿拉伯语、英语-俄语）以及同语言的两个副本（仅词元空间不同）进行对照实验，以排除语言间词汇、句法等混淆因素。
- **主要贡献**：首次在预训练阶段直接证明不相交词元空间是跨语言知识泛化的根本障碍；并提出通过逐词翻译统一词元空间的实际干预方法，带来显著性能提升。

### 实验或数据
- **模型规模**：360M参数（SmolLM2架构）和7B参数（Llama-3改编）。
- **数据**：英语（FineWeb-edu）、阿拉伯语（FineWeb-edu-ar，英语的机器翻译）、俄语（FineWeb2-HQ，原生网络文本）。双语实验使用50/50词元预算，并严格保证文档不重叠。
- **虚构知识注入**：生成2048个关于虚构实体的事实，以不同语言暴露率（N_A和N_B）注入预训练，随后用多项选择问题（MCQ）评估模型在两种语言上的事实获取准确率。
- **结果**：在英语-阿拉伯语和同语言副本（英语1-英语2）中，不相交词元空间导致Ceq分数显著低下；而通过逐词翻译统一词元空间后，Ceq分数大幅提升，最高恢复12.6%的原生学习效率。

### 值得关注点
- 该研究首次在预训练阶段直接定位跨语言知识共享失败的原因，而非事后调优。
- 实验设计巧妙，通过虚构事实和克隆语言副本排除了语言间语义差异的干扰，提供了清晰的因果证据。
- 逐词翻译不仅提升了跨语言知识泛化，还带来了整体语言建模困惑度的改善（如图Fig.1所示），表明该方法具有实际应用价值。
- Ceq指标的提出为衡量跨语言转移提供了一个标准化、可比较的工具。

### 局限性
- 实验主要使用虚构事实和受控的注入方式，可能无法完全反映真实预训练语料中事实的自然分布和复杂性。
- 逐词翻译方法仅适用于词元空间可映射的语言对，对于词元化差异极大或低资源语言可能不适用。
- 论文未透露完整的训练细节（如具体的超参数、硬件配置），可能影响实验结果的可复现性。
- 仅测试了两种模型规模（360M和7B），更大规模模型上的效果尚待验证。
- 跨语言知识泛化的提升虽然显著，但Ceq分数仍未达到原生暴露水平，说明完全消除分区化仍有距离。

## 9. KoNeoBench: A Curated Evaluation Dataset for LLM Understanding of Korean Neologisms

- Source: arxiv
- arXiv ID: 2609.19916
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.19916v1
- PDF: https://arxiv.org/pdf/2609.19916v1
- DOI: https://doi.org/10.48550/arXiv.2609.19916

### Authors

Soha Lee, Soojin Lee, Heesung Yang, Hyunju Song, Hyunji Lee, Jinsan An, Jeongwan Shin, Jin Hyun Park, Jun Lee, Hyeyoung Park, Kilim Nam

### Abstract

Large language models (LLMs) are typically evaluated on static benchmarks, even though natural language constantly evolves through newly emerging words and meanings. Existing Korean benchmarks are centered on established vocabulary and therefore provide limited coverage of such recent lexical change, and their English-oriented design makes it difficult to assess the typological properties of Korean, in which content words combine productively with functional morphemes. In this paper, we introduce KoNeoBench, a benchmark for evaluating LLMs' understanding of Korean neologisms. KoNeoBench is built on 1,785 Korean neologisms attested in online news since 2020 and curated through expert lexicographic review. Each entry provides usage examples, word-formation analyses, and dictionary-style definitions. Based on this resource, we define four tasks and report results on recent models, together with a human baseline. Our experiments show that current LLMs exhibit clear limitations in recovering source components, distinguishing semantic categories, and generating accurate definitions. These results reveal specific aspects of recent Korean lexical change that remain challenging for current LLMs. KoNeoBench is available at https://github.com/bcmilab/ko-neobench/ .

### 中文一句话结论
KoNeoBench 是一个由专家构建的韩语新词评估基准，包含 1,785 个自 2020 年以来的新词，通过四项任务揭示当前大语言模型在恢复源词、区分语义类别和生成准确定义方面仍有显著不足。

### English TL;DR
KoNeoBench is a curated evaluation dataset of 1,785 Korean neologisms (from 2020 onward) with expert-annotated attributes, revealing that current LLMs still struggle with tasks like source-word recovery, semantic categorization, and definition generation due to the agglutinative and hybrid nature of Korean lexical change.

### 中文详细总结
自然语言不断演化，新词和新义持续涌现，但现有的 LLM 评估基准多基于静态数据，韩国语基准也主要覆盖已有词汇，且往往沿用英语导向设计，难以体现韩语黏着语特性（实义词与功能性语素高效组合）。为此，论文提出 **KoNeoBench**，一个专门评估 LLM 对韩语新词理解能力的基准。数据集包含 1,785 个韩语新词，均来自 2020 年以来的网络新闻，经专家词典学审校。每个新词提供用法例句、构词分析和词典式定义。基于该资源，论文设计了四项任务：上下文识别（完形填空）、源词识别、语义及专业领域分类、词典式定义生成。实验在多个近期 LLM 上进行，并设人类基线。结果显示，当前 LLM 在恢复源词成分、区分语义类别和生成准确定义上表现有限，说明韩语新词处理的特定挑战仍然存在。

### 方法 / 贡献
- 构建了 **KoNeoBench**，首个经专家标注的韩语新词评估数据集（1,785 词，2020–2024 年）。
- 基于韩语新词的形态、语义和环境属性，设计了四项评估任务：上下文识别、源词识别、语义/领域分类、定义生成。
- 将韩语黏着语特性纳入任务设计（如粒子是否与词一并掩码）。
- 提供了人类基线，并系统分析了多个 LLM 在各项任务中的表现与错误模式。

### 实验或数据
- 数据集：从《国立国语院》年度新词出版物中收集，来源为韩国主要综合报和商业报纸，经自动候选提取（1,627,371 个候选项）和专家审校，最终保留 1,785 个新词；另有 516 个新词通过语用标记手工补充。
- 每词属性包括：词典定义、用法例句、调查年份、源词形式、构词类型（多词/合成占 58.9%、缩略/混合等）、语义类别（前六类占 82.7%）、专业领域（43 个）。
- 四项任务测试集均已构建，包含题目、正确答案和评价标准。
- 评估模型包括多种近期 LLM，并对比人类基线。
- 实验显示 LLM 在源词识别、分类和定义生成任务上显著落后于人类，尤其在处理缩略/混合词时困难。

### 值得关注点
- KoNeoBench 针对的是语言动态演化的重要侧面——新词，而非静态词汇。
- 任务设计体现了韩语的形态特点（如黏着语素、混合构词），具有语言特异性。
- 数据经过专家词典学严格审校，质量高，且公开可复现（GitHub 链接）。
- 新词分布反映近年社会文化热点，评估 LLM 的新词理解也间接考察其对社会文化现象的把握。

### 局限性
- 数据集仅覆盖 2020–2024 年从在线新闻收集的新词，可能无法充分代表社交媒体、口语或更早出现的新词。
- 新词来源限于主要报纸，可能引入领域偏倚（如经济、政治占比较高）。
- 定义生成任务的主观评分标准未明确讨论，可能存在评分者间差异。
- 实验中的 LLM 样本有限，难以推广到所有模型类型。
- 未探讨零样本或小样本条件下的泛化能力。

## 10. Improving Cross-Lingual Transfer for Sequential Sentence Classification in Research Papers via Structural Similarity

- Source: arxiv
- arXiv ID: 2609.19650
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.19650v1
- PDF: https://arxiv.org/pdf/2609.19650v1
- DOI: https://doi.org/10.48550/arXiv.2609.19650

### Authors

Kazuhiro Yamauchi, Marie Katsurai

### Abstract

Sequential sentence classification (SSC) is an essential task for structuring scientific publications, and extending SSC research to languages other than English can improve accessibility to scientific knowledge in multilingual digital libraries. Cross-lingual transfer is a promising approach to address the scarcity of training data in non-English languages. Prior work on other natural language processing tasks has shown the benefits of capturing linguistic similarity between source and target languages. However, SSC inherently depends on patterns at the discourse level, such as label sequences and positional regularities, which appear consistently across languages regardless of linguistic differences. To examine the factors that determine transfer success in SSC, we constructed a multilingual SSC dataset covering 13 non-English languages collected from five academic databases. Our cross-lingual transfer experiments, using both encoder-based and generative models, show that linguistic proximity has no consistent predictive power for transfer performance, whereas structural similarity in rhetorical organization shows a weak but consistent positive correlation across models. After controlling for source-language performance, the similarity of label distributions is the most consistent predictor. Building on this finding, we propose a set of three methods that explicitly leverage structural information using generative models. In the in-domain evaluation, the best combination reaches parity with the strongest encoder baselines, and in transfer to languages unseen during training, it outperforms the strongest encoder baseline.

### 中文一句话结论  
本文发现，在跨语言顺序句子分类中，修辞组织的结构相似性比语言接近性更能预测迁移成功，并基于该发现提出了三种利用结构信息的生成式方法，在领域内和未见语言上均达到或超越最优编码器基线。

### English TL;DR  
This paper shows that structural similarity in rhetorical organization, rather than linguistic proximity, predicts cross-lingual transfer success in sequential sentence classification, and proposes generative methods leveraging this structure to match or exceed encoder baselines.

### 中文详细总结  
顺序句子分类（SSC）是结构化科学文献的关键任务。为将SSC扩展到非英语语言，跨语言迁移是一种有前景的方法。已有研究在其他NLP任务中强调语言相似性的作用，但SSC本身依赖篇章层面的模式（如标签序列和位置规律），这些模式在不同语言中保持一致性。本文构建了一个覆盖13种非英语语言的多语言SSC数据集（来自5个学术数据库），并基于编码器和生成式模型进行了跨语言迁移实验。结果显示，语言接近性对迁移性能没有一致的预测力，而修辞组织的结构相似性（包括标签分布、标签转移和位置规律）表现出微弱但一致的正相关。在控制源语言性能后，标签分布相似性是最一致的预测因子。基于此，本文提出三种显式利用结构信息的生成式方法：注入结构知识的提示、基于验证器的候选重排序、以及零样本一致性约束。在领域内评估中，最佳组合达到与最强编码器基线持平的水平；在迁移至训练中未见的语言时，则超越了最强编码器基线。

### 方法 / 贡献  
- 构建了覆盖13种非英语语言的多语言SSC数据集（约32,000篇非英语摘要，含英语共52,487篇）  
- 通过实证分析揭示了结构相似性（标签分布、标签转移、位置规律）比语言接近性更一致地预测跨语言迁移性能  
- 提出了三种显式利用结构信息的生成式方法：结构知识注入提示、验证器重排序、零样本一致性约束，并在实验中将宏F1提升至超过现有多语言基线

### 实验或数据  
- 数据集：从DOAJ、HAL、Dialnet、TRdizin、CiNii Research收集，覆盖法语、日语、西班牙语、中文、俄语、葡萄牙语、意大利语、印尼语、土耳其语、韩语、波兰语、荷兰语、爱沙尼亚语（13种非英语语言），加上英语（PubMed-RCT 20k），总计52,487篇摘要、504,416句  
- 模型：使用编码器基（如mBERT、XLM-R）和生成式模型（如LLaMA、mT5）进行跨语言迁移实验  
- 实验设置：在领域内评估（源语言和目标语言均存在于训练数据）和迁移至未见语言（目标语言在训练中未出现）两种场景下比较  

### 值得关注点  
- 首次大规模验证了在SSC任务中结构相似性（而非语言接近性）是跨语言迁移更可靠的预测因子  
- 标签分布相似性在控制源语言性能后成为最一致的预测指标  
- 提出的生成式方法在未见语言迁移中超越了强编码器基线，表明结构信息可用于直接提升SSC性能  
- 数据集覆盖多语言且包含丰富结构信息（如标签序列、位置），为后续研究提供资源

### 局限性  
摘要中未明确讨论局限性。论文可能在后续部分分析了领域相似性（如医学/生命科学领域的偏斜）对结构相似性度量的潜在混淆，但具体内容未在提供的元数据中体现。

## Processing Notes

- Duplicate papers skipped: 0