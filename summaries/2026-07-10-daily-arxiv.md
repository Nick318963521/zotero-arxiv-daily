# Daily arXiv - 2026-07-10

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-10T23:25:49
- Paper count: 10

## 1. UltraX: Refining Pre-Training Data at Scale with Adaptive Programmatic Editing

- Source: arxiv
- arXiv ID: 2607.08646
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.08646v1
- PDF: https://arxiv.org/pdf/2607.08646v1
- DOI: https://doi.org/10.48550/arXiv.2607.08646

### Authors

Xinlong Zhao, Dongsheng Liu, Hengyu Zhao, Zixuan Fu, Zheng Wang, Jie Cai, Jie Zhou, Qiang Ma, Xuanhe Zhou, Xu Han, Yudong Wang, Zhiyuan Liu

### Abstract

As available training data approaches its physical limit, gains from Scaling Laws have begun to diminish. Consequently, improving Large Language Models (LLMs) now depends less on data expansion and more on higher-quality data utilization. However, in the context of large-scale corpora, existing refinement methodologies face significant limitations in quality, efficiency, and reliability: Rule-based approaches are constrained by fixed heuristics and struggle with instance-level variations; LLM-based approaches improve quality but fail to meet the efficiency and reliability requirements of large-scale data processing. To address these challenges, we propose UltraX, a function-calling refinement framework for large-scale pre-training data that completes the editing function space by introducing insertion in addition to deletion and modification, enabling fine-grained instance-level editing. Specifically, UltraX builds a reliable program-supervision generation pipeline. In this pipeline, dataset-adaptive prompt optimization first guides an expert LLM to produce high-quality end-to-end refined texts, and Line Alignment Mapping and Dynamic Context Replacement then convert original-refined text pairs into structured program supervision. Meanwhile, UltraX improves supervision quality and stabilizes the training distribution with low-confidence example filtering and ratio-controlled sampling by operation combination. During inference and execution, it normalizes and validates model outputs through sliding-window prediction, global operation aggregation, and systematic post-processing, improving the stability and reliability of large-scale execution. Experiments show that UltraX achieves the highest average performance across all corpora and also matches or surpasses baselines with fewer training tokens, demonstrating stronger data efficiency and refinement reliability.

### 中文一句话结论
UltraX通过引入插入操作、构建可靠的程序监督生成流水线以及鲁棒的大规模执行机制，实现了对预训练数据的细粒度、高质量、高效率且可靠的程序化编辑，显著提升了多语料库上的下游模型性能。

### English TL;DR
UltraX is a function-calling refinement framework for large-scale pre-training data. It introduces insertion alongside deletion and modification for fine-grained instance-level editing, builds a reliable program-supervision generation pipeline (via dataset-adaptive prompt optimization, line alignment mapping, and dynamic context replacement), and ensures robust execution through sliding-window prediction, global aggregation, and systematic post-processing. Experiments on 1B models across five corpora show UltraX achieves the highest average performance with over 2% relative improvement, demonstrating superior data efficiency and refinement reliability.

### 中文详细总结
UltraX旨在解决现有预训练数据精炼方法在质量、效率和可靠性上的不足。规则方法受限于固定启发式，难以处理实例级变化；基于LLM的方法质量高但效率低，无法大规模应用。UltraX创新地将数据精炼建模为程序化文本变换，定义了包含插入、删除和修改的完整编辑函数空间，实现了细粒度实例级编辑。

其核心流程分两阶段：
1. **精炼模型构建**：从原始语料中采样，通过数据集自适应提示优化引导专家LLM生成高质量端到端精炼文本；然后利用行对齐映射和动态上下文替换，将原始-精炼文本对转换为结构化程序监督；再通过低置信度过滤和基于操作组合的比例控制采样，提升监督质量并稳定训练分布。最后在轻量级模型上微调，得到精炼器。
2. **大规模程序执行**：精炼器对大规模语料进行滑动窗口预测，输出分段函数调用程序；通过全局操作聚合和系统化后处理（如模糊替换过滤、相邻操作合并、重复模式回退）进行归一化和验证，最后由确定性执行器应用，生成高质量精炼语料。

实验表明，UltraX在FineWeb、RedPajama-V2、AICC、Ultra-FineWeb、FineWeb-ProX-Doc五个语料库上，从头预训练1B参数的MiniCPM模型（20B token预算），均达到最高平均性能，相对提升超过2%，且效率更高。

### 方法 / 贡献
- **完整编辑函数空间**：在删除和修改之外引入插入操作，使模型能够进行细粒度实例级编辑，修复缺失语义。
- **可靠的程序监督生成流水线**：包含数据集自适应提示优化（引导专家LLM生成高质量端到端精炼文本）、行对齐映射和动态上下文替换（将原始-精炼文本对转换为结构化程序监督）、低置信度过滤和操作组合比例控制采样（提升监督质量并稳定训练分布）。
- **鲁棒的大规模执行机制**：采用滑动窗口预测、全局操作聚合、系统化后处理（模糊替换过滤、相邻操作合并、重复模式回退），解决重复字符串匹配、连续操作干扰等问题，确保大规模执行的稳定性和可靠性。

### 实验或数据
- **实验设置**：使用MiniCPM-1B模型，从零开始预训练，训练预算为20B tokens。在五个语料库上评估：FineWeb、RedPajama-V2、AICC、Ultra-FineWeb、FineWeb-ProX-Doc。
- **主要结果**：UltraX在所有语料库上取得最高平均性能，相对提升超过2%，且在使用更少训练token的情况下达到或超过基线方法，展示了更强的数据效率和精炼可靠性。
- **其他评估**：论文还进行了消融实验和效率分析（具体数据未在摘要中详述，但方法部分提及了相关设计）。

### 值得关注点
- 首次完成插入、删除、修改三种操作的联合建模，使数据精炼不再局限于删改，能更灵活地修复缺失内容。
- 将LLM的精炼能力通过程序监督蒸馏到轻量级模型，兼顾了语义质量和处理效率，实现了大规模预训练数据的可行精炼。
- 滑动窗口+全局聚合+后处理的设计有效解决了长文档处理中的语义连贯性和操作冲突问题，提升了大规模执行的可靠性。

### 局限性
论文未明确讨论其局限性。但根据方法描述，可推断以下潜在局限：依赖专家LLM（如GPT-4）生成种子监督数据，可能带来额外成本；程序监督的构建流程较为复杂，对数据集自适应提示优化的鲁棒性有一定要求；轻量级精炼模型在极端复杂或长上下文场景下的泛化能力有待进一步验证。

## 2. MASTE: A Multi-Agent Pipeline for Zero-Shot Aspect Sentiment Triplet Extraction

- Source: arxiv
- arXiv ID: 2607.08080
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.08080v1
- PDF: https://arxiv.org/pdf/2607.08080v1
- DOI: https://doi.org/10.48550/arXiv.2607.08080

### Authors

Ao Hong, Lehang Wang, Zhirun Yue, Mingxin Wang, Zihan Wang, Houde Liu

### Abstract

Aspect Sentiment Triplet Extraction (ASTE) requires jointly identifying (aspect, opinion, sentiment) triples from a given review sentence. While large language models (LLMs) achieve strong zero-shot performance on many NLP benchmarks, their effectiveness on ASTE remains limited, as single-pass generation forces the model to determine span boundaries, opinion grouping, and sentiment polarity in a single decoding step. Common remedies, such as few-shot in-context learning and chain-of-thought prompting, offer only marginal improvements and rely heavily on either in-domain demonstrations sampled from labeled training data or carefully engineered reasoning prompts, neither of which is broadly available in zero-shot deployment. Inspired by the classical agent paradigm, we propose MASTE, a multi-agent pipeline for zero-shot Aspect Sentiment Triplet Extraction. MASTE decomposes ASTE into four sequential stages, where specialized agents handle different compositional subtasks with explicit conditioning on prior outputs. This design enables entirely training-free zero-shot ASTE and generalizes across different backbones and datasets. Extensive experiments on four ASTE benchmarks show that MASTE substantially outperforms zero-shot and chain-of-thought LLM baselines under the same backbone, narrowing the gap to fully supervised methods without using any labeled triplets. Code is available at https://github.com/Hankerlove/MASTE.

### 中文一句话结论
MASTE 是一种无需训练的零样本多智能体流水线，通过将情感三元组抽取分解为四个顺序子任务，显著提升了大型语言模型在该任务上的精确匹配性能。

### English TL;DR
MASTE is a training-free multi-agent pipeline that decomposes Aspect Sentiment Triplet Extraction into four sequential stages with specialized agents, significantly improving zero-shot LLM performance on this task by addressing single-pass generation failures.

### 中文详细总结
MASTE 针对情感三元组抽取（ASTE）中大型语言模型单次生成易产生跨度错误、幻觉等问题，借鉴经典智能体范式，设计了一个四阶段流水线：方面抽取、意见抽取、情感分类和一致性检查。每个阶段使用专门提示的 LLM 智能体，并显式依赖上游输出。该方法无需任何标注数据训练，仅凭零样本提示即可运行。在四个 ASTE 基准数据集上的实验表明，MASTE 在相同骨干模型下大幅超越零样本和思维链基线，缩小了与全监督方法的差距。

### 方法 / 贡献
- 提出首个无需训练的多智能体 ASTE 流水线，将任务分解为四个顺序阶段。
- 设计最小跨度意见抽取机制，支持一对多方面-意见映射，并引入一致性检查智能体进行跨度验证、极性校准与去重。
- 跨不同骨干模型和数据集验证了方法的通用性与有效性。

### 实验或数据
实验在四个标准 ASTE 基准（14res、14lap、15res、16res）上进行，对比了全监督基线、零样本 LLM 基线以及思维链方法。结果显示 MASTE 在所有数据集上均取得最优零样本性能，且与全监督方法的差距显著缩小。此外还进行了跨骨干模型（如 Llama、GPT 系列）和消融实验。

### 值得关注点
- 完全零样本且无需训练，具备良好通用性。
- 通过显式顺序依赖和智能体分工，精准解决了 LLM 在 ASTE 上的典型失败模式（跨度膨胀、合并、幻觉）。
- 开源代码便于复现和扩展。

### 局限性
论文未明确讨论局限性。作为零样本方法，MASTE 的性能仍受限于所用 LLM 骨干的能力，且顺序流水线可能累积传递误差；此外未探讨对长文本或复杂句式的适应性。

## 3. Ensemble Diversity Optimization for Subjective Supervision

- Source: arxiv
- arXiv ID: 2607.08493
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.08493v1
- PDF: https://arxiv.org/pdf/2607.08493v1
- DOI: https://doi.org/10.48550/arXiv.2607.08493

### Authors

Xia Cui, Ziyi Huang, N. R. Abeynayake

### Abstract

Subjective NLP tasks often exhibit systematic annotator disagreement, requiring models that represent uncertainty rather than collapse it. We introduce Ensemble Diversity Optimization (EDO), a prediction-space framework that jointly optimizes ensemble weights, effective cardinality, and calibration through a unified differentiable objective. EDO learns ensemble composition and size end-to-end via Gumbel-Softmax relaxation and incorporates a signed diversity regularizer, tuned on validation data, to steer optimization toward either preserving or suppressing disagreement. This regularization prevents ensemble collapse and enables controlled navigation of the utility-calibration trade-off. The framework integrates a soft F1 surrogate, class-weighted cross-entropy to address imbalance, and reliability-weighted diversity to regulate intra-ensemble variability. Experiments on four subjective text-classification benchmarks (ArMIS, ConvAbuse, HS-Brexit, MD-Agreement) show that EDO substantially improves probabilistic calibration, reducing cross-entropy (40-78% depending on baseline) and lowering Brier scores relative to Soft-CE, Soft-MD, Top-5 Voting, and WEL, while maintaining competitive F1 and better alignment with annotator distributions. These results demonstrate that jointly optimizing ensemble structure with a signed diversity regularizer provides an efficient, model-agnostic approach for modeling human subjectivity in supervised learning.

### 中文一句话结论
本文提出集成多样性优化（EDO）框架，通过可微的预测空间联合优化集成权重、有效规模和校准，利用有符号多样性正则化显式建模标注者分歧，在主观文本分类任务上显著提升概率校准性能。

### English TL;DR
EDO is a prediction-space framework that jointly optimizes ensemble weights, effective cardinality, and calibration via a unified differentiable objective with a signed diversity regularizer. It models annotator disagreement by either preserving or suppressing intra-ensemble variability, achieving 40-78% cross-entropy reduction on four subjective text classification benchmarks while maintaining competitive F1 scores.

### 中文详细总结
主观NLP任务常出现系统性标注者分歧，要求模型能够表示不确定性而非将其压缩。本文提出的集成多样性优化框架在预测空间操作，联合优化集成权重、有效规模和校准性能。核心组件包括：(1) 有符号多样性正则化器，通过验证数据调优，可引导优化保留或抑制分歧；(2) 多目标优化，平衡预测效用、校准和内部多样性；(3) 通过Gumbel-Softmax松弛实现端到端的集成结构学习。实验表明，EDO相对于多种基线方法显著提升概率校准性能，交叉熵降低40-78%，Brier分数也获得改善，同时维持了有竞争力的F1分数和对标注者分布的更好对齐。

### 方法 / 贡献
1. 提出有符号、可靠性加权的多样性损失，将集成内部差异作为显式优化目标
2. 统一多目标优化框架：软F1代理损失（预测效用）+ 类别加权交叉熵（校准）+ 有符号多样性正则化（内部变异性控制）+ L2正则化
3. 通过Gumbel-Softmax松弛实现集成权重的可微学习和有效规模选择
4. 在预测空间操作，主干网络参数冻结，无需标注者元数据，模型无关且计算高效
5. 多样性方向s ∈ {-1, +1}作为验证集调优的超参数，引导优化沿效用-校准帕累托前沿移动

### 实验或数据
在四个主观文本分类基准数据集上进行实验：
- ArMIS, ConvAbuse, HS-Brexit, MD-Agreement（均来自LeWiDi基准）

EDO与以下方法对比：Soft-CE, Soft-MD, Top-5 Voting, WEL（弱集成学习）。结果包括交叉熵降低40-78%（取决于基线），Brier分数改善，同时维持有竞争力的F1分数和对标注者分布的更好对齐。

### 值得关注点
1. 从理论上将多样性视为泛化的基本组成部分（基于Wood等2023的统一集成多样性理论），而非辅助启发式
2. 通过有符号正则化实现受控的效用-校准权衡导航，能够区分系统性主观性与结构性噪声
3. 完全模型无关且可端到端微调，灵活性高
4. 代码和数据已在GitHub公开

### 局限性
1. 实验中主干网络参数冻结以隔离标注者分歧导致的不确定性，未探索端到端微调的效果
2. 需要验证数据进行超参数调优（多样性系数和方向），可能增加实际应用中的调优成本
3. Per-Annotator策略要求标注者身份信息，且限制了集成成员数量（K ≤ min_i A_i）
4. 未提及对更大规模模型或不同任务类型（如生成任务）的泛化能力
5. 未讨论与现有主观监督方法（如KL散度目标或熵正则化）相比的计算开销差异

## 4. Understanding Axes of Difficulty For Long Context Tasks Via PredicateLongBench

- Source: arxiv
- arXiv ID: 2607.08284
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.08284v1
- PDF: https://arxiv.org/pdf/2607.08284v1
- DOI: https://doi.org/10.48550/arXiv.2607.08284

### Authors

Siddhartha Jain, Ameya Velingker

### Abstract

Large language models (LLMs) have demonstrated rapidly improving long-context capabilities, prompting a wave of benchmarks designed to evaluate them. However, existing long-context evaluations - from Needle-in-a-Haystack (NIAH) tests to more recent multi-hop reasoning and summarization tasks - predominantly measure average-case performance, and many are either saturated or lack robustness. Notably absent is a systematic way to probe how models perform as we scale up the difficulty of tasks along various axes. We address this gap by proposing PredicateLongBench, a benchmark that stress-tests long-context reasoning by asking models to identify the longest contiguous subsequence of words in a long input that satisfies given predicates/constraints (e.g., lexicographic ordering), drawn from a broader predicate class. The central innovation of our benchmark is the identification and systematic exploration of multiple different axes of difficulty which test multiple aspects of long context understanding. We provide two complementary generation pipelines - a fully synthetic setup using random word-like strings, and a real-world setup that samples words from natural documents while preserving their distributional properties. We find that frontier models struggle to perform well as we scale up the difficulty of tasks along our axes, demonstrating the utility of our benchmark in understanding the limitations of current long-context capabilities. Furthermore, the tasks in PredicateLongBench, though challenging, are conceptually simple and do not require LLM-based generations or judges.

### 中文一句话结论
本文提出 PredicateLongBench，通过沿多个难度轴（如计算复杂度、对抗性干扰等）系统性地扩展任务难度，揭示前沿大模型在长上下文推理中的显著不足。

### English TL;DR
This paper introduces PredicateLongBench, a benchmark that systematically probes the limitations of large language models in long-context reasoning by scaling task difficulty across multiple axes—including computation, adversarial decoys, and non-locality—using a simple but challenging objective: finding the longest contiguous subsequence satisfying given predicates.

### 中文详细总结
现有长上下文评测（如 NIAH、多跳推理等）大多衡量平均性能，且许多已饱和或缺乏鲁棒性，缺少系统性地沿多个维度扩展难度的方法。PredicateLongBench 通过要求模型在长输入中找到满足给定谓词（如字典序）的最长连续子序列，来压力测试模型的长上下文推理能力。其核心创新在于识别并系统探索多个难度轴，包括：计算复杂度（谓词元数）、对抗性干扰（近匹配序列和多列表约束）、搜索空间等。基准提供两种数据生成管线：完全合成和基于真实文档的采样。实验表明，前沿模型随难度增大性能显著下降，证明该基准在揭示当前长上下文能力局限性方面的有效性。

### 方法 / 贡献
1. 提出 PredicateLongBench，任务简单但具有挑战性，无需依赖 LLM 生成或评判。
2. 系统定义并探索多个难度轴：计算（一元/二元谓词）、对抗性干扰（近匹配序列、多列表约束）、搜索空间等。
3. 设计两种互补的数据生成方式：全合成字符串和保留真实文档分布特性的采样。
4. 通过实验证明上下文结构（特别是干扰项）对模型性能有重大影响。

### 实验或数据
摘要和内容预览中未提供具体的实验数据、模型列表或性能表格。作者仅声明前沿模型在难度增加时表现不佳，但未给出详细实验设置或具体数值结果。

### 值得关注点
- 核心创新：系统性地定义和探索多个独立可控的“难度轴”，而非仅增加上下文长度或任务复杂度。
- 任务设计的简洁性：仅需找到满足约束的最长连续子序列，问题定义清晰、可自动验证，无需 LLM 作为裁判。
- 对抗性干扰设计（近匹配序列、跨列表约束）为评测模型鲁棒性提供了新思路。
- 合成数据和真实数据双管线设计，兼顾可控性和生态效度。

### 局限性
- 当前仅探索了一元和二元谓词，更高元数（三元及以上）的计算复杂度尚未研究。
- 未提供具体的实验数据，无法评估不同模型的性能差异和基准的实际区分度。
- 难度轴的独立性尚待验证，不同轴之间可能存在交互效应。
- 任务定义偏重局部/全局结构约束，可能无法覆盖所有长上下文推理场景（如问答、摘要等）。

## 5. PLURAL: A Global Dataset for Value Alignment

- Source: arxiv
- arXiv ID: 2607.08034
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.08034v1
- PDF: https://arxiv.org/pdf/2607.08034v1
- DOI: https://doi.org/10.48550/arXiv.2607.08034

### Authors

Dhruv Agarwal, Anya Shukla, Tanya Goyal, Aditya Vashistha

### Abstract

Large language models (LLMs) are used worldwide, yet disproportionately reflect Western values, limiting their ability to represent diverse value systems. We introduce PLURAL, a large-scale, value-focused preference dataset grounded in the Integrated Values Survey (IVS), a nationally representative survey spanning 92 countries. Using a two-stage generation pipeline, we transform survey responses into synthetic preference triplets that preserve normative value signals while producing realistic scenarios. We release an initial version of PLURAL containing ~500,000 preference triplets representing people in 20 diverse countries. We evaluate PLURAL in three ways: (i) dataset-level validation showing that it preserves both cross-country value differences and within-country diversity from the original survey; (ii) automated evaluation showing that training on PLURAL improves alignment with target countries' cultural profiles, reducing mean absolute error by up to 27.7% relative to strong baselines; and (iii) blind human evaluation with 176 evaluators in India, Brazil, and Japan, who judge PLURAL-aligned responses as more representative of their national values. Together, these results show that PLURAL contains learnable signal for value steering, offering a scalable resource for pluralistic alignment. Dataset: https://huggingface.co/datasets/agdhruv/plural-alignment

### 中文一句话结论
PLURAL是一个基于92国全国代表性调查数据的大规模合成偏好数据集，能有效提升语言模型对多元文化价值观的反映能力，在自动评估中将对齐误差降低达27.7%，并得到印度、巴西和日本人类评估者的认可。

### English TL;DR
PLURAL is a large-scale synthetic preference dataset grounded in nationally representative survey data from 92 countries that enables LLMs to better reflect diverse cultural values, reducing alignment error by up to 27.7% and improving perceived representativeness in human evaluations across India, Brazil, and Japan.

### 中文详细总结
大型语言模型（LLM）在全球范围内使用，却过度反映西方价值观，难以代表多样的价值体系。本文引入PLURAL，这是一个大规模、以价值为核心的偏好数据集，基于覆盖92个国家的全国性代表性调查“综合价值观调查”（Integrated Values Survey，IVS）。通过两阶段生成流程，我们将调查响应转换为合成的偏好三元组（偏好/非偏好响应），在生成现实场景的同时保留了规范性的价值信号。我们发布了包含约50万个偏好三元组的初始版本，代表20个不同国家的人群。评估采用三种方式：(i) 数据集层面验证，表明PLURAL保留了原始调查中的跨国价值差异和国内多样性；(ii) 自动化评估，表明在PLURAL上训练能提升对目标国家文化轮廓的对齐性，相较于强基线平均绝对误差降低高达27.7%；(iii) 盲法人类评估，来自印度、巴西和日本的176名评估者认为PLURAL对齐后的响应更能代表其国家价值观。这些结果共同表明PLURAL包含可用于价值引导的学习信号，为多元对齐提供了可扩展的资源。数据集链接：https://huggingface.co/datasets/agdhruv/plural-alignment

### 方法 / 贡献
- **方法**：提出两阶段生成管道，将IVS调查响应转换为合成偏好三元组。阶段一（三元组生成）：向LLM提供参与者的入口统计信息、相关调查问题及其回答，生成包含场景提示、偏好响应和非偏好响应的三元组。阶段二（响应扩展）：将简洁响应扩展为更自然、类助手的对话形式。
- **贡献**：(1) 发布PLURAL数据集，覆盖20个国家，并可扩展至全部92个IVS国家；(2) 介绍将调查响应转化为高质量合成偏好数据并保留跨国家与国内价值信号的管道；(3) 通过五个国家的实验证明PLURAL能引导LLM表现得更具文化代表性。

### 实验或数据
- **数据集**：基于IVS（156,658名参与者，92个国家），初始版本采样100名参与者/国家（分层比例抽样），共20国，约50万个偏好三元组。
- **自动化评估**：使用GLOBE框架（九文化维度）衡量对齐性，评估指标为平均绝对误差（MAE）。在PLURAL上使用DPO微调llama-3.1-8b-instruct，目标国家为印度、巴西、日本、马来西亚和津巴布韦。相比强基线，MAE降低高达27.7%。
- **人类评估**：在印度（n=68）、巴西（n=75）和日本（n=33）招募共176名评估者，采用盲法比较PLURAL对齐模型与基线模型对36个代表性提示的响应，评估者认为PLURAL对齐模型更代表其国家价值观。
- **数据集层面验证**：验证PLURAL保留了IVS中的跨国价值差异（如通过国家预测任务）和国内多样性（如通过响应距离分布比较）。

### 值得关注点
- **规模与代表性**：PLURAL是首个基于严格社会科学调查（覆盖92国、国家级代表性样本）构建的大规模价值观偏好数据集，显著提升了数据的文化多样性，远超先前主要依赖西方人群的数据集。
- **方法论创新**：两阶段生成管道结合了从调查响应到合成数据的转换，保留了规范性的价值信号，同时通过随机选择前沿LLM（如GPT-5 Mini、Mistral Large 3等）和随机解码减少模型特定偏见。
- **严格的评估框架**：使用与训练框架（IVS）完全不同的文化理论（GLOBE）进行自动化评估，确保泛化性；同时结合跨三国的人类评估，全面验证了数据集的有效性。

### 局限性
- 数据集为完全合成生成，虽然忠实于原始调查，但可能无法捕捉自然语言中价值观表达的细微差别和模糊性。
- 覆盖国家和人群仍有限；初始版本仅含20国，且每个国家仅采样100名参与者，可能不足以代表全部国内多样性。
- 所有三元组以英文生成，仅关注价值观对齐，不考虑语言多样性或非英语区域的文化表达。
- 未提供具体实验表格或详细数据集统计；自动化评估和人类评估的完整结果需查阅附录。
- 未提及实验中使用的基础模型是否已预训练于目标文化相关数据，可能影响对齐效果的归因。

## 6. Scalable and Culturally Specific Stereotype Dataset Construction via Human-LLM Collaboration

- Source: arxiv
- arXiv ID: 2607.07895
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.07895v1
- PDF: https://arxiv.org/pdf/2607.07895v1
- DOI: https://doi.org/10.48550/arXiv.2607.07895

### Authors

Weicheng Ma, John Guerrerio, Soroush Vosoughi

### Abstract

Research on stereotypes in large language models (LLMs) has largely focused on English-speaking contexts, due to the lack of datasets in other languages and the high cost of manual annotation in underrepresented cultures. To address this gap, we introduce a cost-efficient human-LLM collaborative annotation framework and apply it to construct EspanStereo, a Spanish-language stereotype dataset spanning multiple Spanish-speaking countries across Europe and Latin America. EspanStereo captures both well-documented stereotypes from prior literature and culturally specific biases absent from English-centric resources. Using LLMs to generate candidate stereotypes and in-culture annotators to validate them, we demonstrate the framework's effectiveness in identifying nuanced, region-specific biases. Our evaluation of Spanish-supporting LLMs using EspanStereo reveals significant variation in stereotypical behavior across countries, highlighting the need for more culturally grounded assessments. Beyond Spanish, our framework is adaptable to other languages and regions, offering a scalable path toward multilingual stereotype benchmarks. This work broadens the scope of stereotype analysis in LLMs and lays the groundwork for comprehensive cross-cultural bias evaluation.

### 中文一句话结论
提出的人机协作框架（LLM生成候选+本地人验证和实例化）高效构建了首个多国西班牙语刻板印象数据集EspanStereo，揭示了LLM在跨文化背景下显著的偏见差异。

### English TL;DR
This paper introduces a scalable, cost-efficient human-LLM collaboration framework for constructing culturally specific stereotype datasets. Applied to Spanish, it produces EspanStereo, covering five Spanish-speaking countries (Spain, Mexico, Argentina, Colombia, Nicaragua). Evaluating Spanish-supporting LLMs (XLM-R, BETO) reveals significant cross-country variation in stereotypical behaviors, underscoring the need for fine-grained, culturally grounded bias assessments.

### 中文详细总结
当前的刻板印象数据集多聚焦于英语语境，缺乏非英语语言和低资源文化的系统性数据，且手动构建成本高昂。本文提出一种LLM与人工协作的标注框架：首先通过精心设计的提示（包括注入攻击）引导LLM生成特定国家的候选刻板印象；随后由目标文化内的本地标注员使用Likert量表验证其普遍性，并实例化为标准句子对。基于该框架构建的EspanStereo数据集覆盖西班牙、墨西哥、阿根廷、哥伦比亚和尼加拉瓜五国，包含种族、宗教、性别、性取向和年龄五大类别。实验使用探针-剪枝方法评估了XLM-R和BETO等模型，结果证实不同国家在LLM中的刻板印象内容和编码模式存在显著差异，强调了进行细粒度地域性评估的必要性。

### 方法 / 贡献
- **方法**:
  1. **LLM生成候选**: 通过提示注入攻击（多视角、多次重复）让GPT-4o等模型生成目标国家的刻板印象。
  2. **人工验证**: 目标国出生/成长的标注员用5点Likert量表评估普遍性，保留中位数大于2的条目。
  3. **人工实例化**: 另一批本地标注员将验证后的刻板印象实例化为上下文+刻板/反刻板句子对。
- **贡献**:
  1. 提出一种语言无关、可扩展且低成本的刻板印象数据集构建范式，大幅降低对昂贵人工标注的依赖。
  2. 构建并发布了首个原生（非翻译）西班牙语刻板印象评估基准EspanStereo。
  3. 通过系统评估揭示了LLM中高度文化特异性的刻板印象，并强调了跨文化评估的必要性。

### 实验或数据
- **数据集**: EspanStereo，涵盖西班牙、墨西哥、阿根廷、哥伦比亚、尼加拉瓜五国，针对种族、宗教、性别、性取向和年龄五类身份。
- **评估模型**: XLM-R（多语言）和BETO（单语言西班牙语）等基于Transformer的西班牙语LLM。
- **评估方法**: 使用“探针与剪枝”（probing-and-pruning）方法分析刻板印象的编码与表现。
- **主要发现**: 发现各国刻板印象在LLM中编码强度差异显著，且捕获了文献中未记载的区域特异性偏见（如尼加拉瓜对克里奥尔人的刻板印象，西班牙对巴基斯坦人的刻板印象）。

### 值得关注点
- 验证了LLM生成的刻板印象可获得较高的人类验证通过率，且能捕获新颖、地域高度特异化的偏见。
- 框架完全依赖LLM生成候选，配合有限的人类校对，为低资源语言的偏见评估提供了可复制的低成本路径。
- 首次系统证明同一语言（西班牙语）内，不同国家的刻板印象内容及LLM编码模式迥异，支持了去中心化、基于特定文化的AI伦理评估需求。

### 局限性
- 当前数据集仅覆盖五国和五类社会身份，覆盖面有限。
- 初始阶段依赖特定LLM（如GPT-4o）的生成能力，可能遗漏未充分体现在训练数据中的刻板印象。
- 虽大幅降低人力需求，但在验证和实例化阶段仍依赖高质量本地标注员，对极低资源语言仍有实施门槛。
- 刻板印象动态变化，数据集为静态快照，难以反映偏见的时间演变。

## 7. Persona Cartography: Charting Language Model Personality Traits in Weight Space

- Source: arxiv
- arXiv ID: 2607.07916
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.07916v1
- PDF: https://arxiv.org/pdf/2607.07916v1
- DOI: https://doi.org/10.48550/arXiv.2607.07916

### Authors

Luke Baines, Anton Gonzalvez Hawthorne, Mariia Koroliuk, Irakli Shalibashvili, Clément Dumas, Konstantinos Voudouris, David Demitri Africa

### Abstract

Large language models exhibit recurring behavioural patterns -- personas -- that shape generalisation and safety, but we lack reliable tools for decomposing, measuring, and controlling them. Our central insight is to treat personas as positions in a space of behavioural traits, using the OCEAN framework to describe model personas in terms of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. We train low-rank adapters to amplify or suppress individual traits, and evaluate their effects using an LLM-judge calibrated against a human-validated panel, trait-specific multiple-choice benchmarks, and standard capability evaluations. Across six models from three families (4B-32B), we find that each adapter moves its target trait largely monotonically with scale, combines approximately additively with other adapters to construct mixed personas, and preserves performance on capability benchmarks at moderate scales. We further show that the induced trait axes affect safety-relevant behaviour in downstream evaluations: for example, moving along neuroticism and agreeableness axes affects frustration and sycophancy respectively. We also introduce an unsupervised psychometric pipeline that recovers four interpretable behavioural factors (tone, initiative, didacticism, epistemic caution) from model rollouts. Persona control can then be considered in terms of learning, scaling, and composing traits in weight space, providing a bridge between personality measurement, model editing, and safety.

### 中文一句话结论  
本文提出“人格制图”（Persona Cartography）方法，将大语言模型（LLM）的行为人格分解并映射到 OCEAN 五因素特质空间，通过训练可缩放、可组合的低秩适配器（LoRA）在权重空间中精确调控模型人格，同时保持通用能力并影响安全相关行为。

### English TL;DR  
Persona Cartography treats LLM personas as positions in a behavioral trait space (OCEAN) and trains low-rank adapters to amplify or suppress individual traits, enabling monotonic scaling, additive composition, and interpretable control over model behavior while preserving capabilities and affecting safety-relevant outcomes.

### 中文详细总结  
该研究利用人格心理学中的 OCEAN 框架（开放性、尽责性、外向性、宜人性、神经质），将 LLM 的行为模式视为特质空间中的位置。他们为每个特质训练了放大或抑制的 LoRA 适配器（rank=64），并将其应用于来自三个家族的六个模型（参数量 4B–32B）。实验表明：  
- 适配器能单调地移动目标特质，且缩放系数越大效果越明显；  
- 多个适配器可以近似加法组合，构造复合人格；  
- 在中低缩放系数下，模型在 MMLU、GSM8K、TruthfulQA 等能力基准上的性能基本保持；  
- 沿特定特质轴移动（如神经质、宜人性）会显著影响下游安全相关行为（如挫败感、谄媚、拒绝）。  
此外，他们还提出一种无监督心理测量管道，从模型生成中自动恢复出四种可解释的行为因子（语气、主动性、教导性、认知谨慎），证明特质空间比 OCEAN 五因素具有更丰富的结构。

### 方法 / 贡献  
1. **可组合的 OCEAN 特质适配器**：通过宪法引导蒸馏（Open Character Training 框架）和 DPO+SFT 两阶段训练得到放大/抑制各特质的 LoRA，支持连续缩放和加法组合。  
2. **下游安全相关效用验证**：展示特质控制如何影响挫败感、谄媚和拒绝倾向等安全评估。  
3. **无监督人格因子发现**：引入心理测量流程，从模型输出中提取超出 OCEAN 的本征行为因子，揭示模型内部行为组织方式。

### 实验或数据  
- **模型**：Llama-3.1-8B-Instruct、Qwen3-8B/32B、Gemma-3-4B/12B/27B（共 6 个模型）。  
- **评估**：LLM 裁判（经人类标注校准）对 240 条提示进行评分；TRAIT 多选题基准；MMLU、GSM8K、TruthfulQA 能力测试；安全相关行为评估（挫败感、谄媚、拒绝）。  
- **训练教师**：默认使用 GLM-4.5-Air，并用 DeepSeek-V3.2 验证管道稳健性。  
- **控制项**：训练中性适配器以隔离管道伪影。

### 值得关注点  
- 特质适配器以单调、连续的方式控制目标特质，且多个适配器可近似加法组合，实现精确人格塑造。  
- 在中等缩放系数下，通用能力几乎不受损，为实用控制提供空间。  
- 特质轴会迁移影响安全相关行为（如神经质→挫败感；宜人性→谄媚），揭示人格调控与安全之间的桥梁。  
- 无监督方法恢复出“语气、主动性、教导性、认知谨慎”四个可解释因子，展示人格结构的丰富性。

### 局限性  
- 特质轴并非完全正交：尽责性与神经质适配器存在部分相关性，表明当前训练方法无法绝对保证沿单一独立轴移动。  
- 依赖预定义 OCEAN 框架，可能无法覆盖模型所有重要行为维度（部分因子需通过无监督流程补充）。  
- 评估依赖 LLM 裁判，虽经人工校准但仍可能引入偏差；能力基准在较大缩放系数下可能下降（文中仅强调“中等缩放系数”保持性能）。  
- 适配器的组合性可能受模型族、规模或训练策略影响，跨更广泛模型泛化性尚需验证。

## 8. When Debiasing Backfires: Counterintuitive Side Effects of Preprocessing-Based Stereotype Mitigation

- Source: arxiv
- arXiv ID: 2607.07937
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.07937v1
- PDF: https://arxiv.org/pdf/2607.07937v1
- DOI: https://doi.org/10.48550/arXiv.2607.07937

### Authors

Yahan Zheng, John Guerrerio, Soroush Vosoughi, Weicheng Ma

### Abstract

Preprocessing-based methods for stereotype mitigation, such as pre-/post-training on debiased corpora, are widely used in NLP. While these approaches reduce measurable stereotypes for targeted groups, we find they often induce unintended shifts-side effects, where stereotyping or counter-stereotyping can increase relative to neutral baselines for other demographics, including across unrelated demographic categories. We demonstrate these side effects across two model families (encoder-only and decoder-only), multiple preprocessing strategies (removing stereotypical sentences, removing group mentions, and swapping group references), and both pre- and post-training at different data scales on Wikipedia. Standard benchmarks frequently miss these shifts. Using attention-rollout analysis, we observe that such side effects are not accompanied by large changes in attention flow, complicating mechanistic explanations. We discuss implications for evaluation, provide actionable diagnostics, and argue for side-effect-aware, transparent mitigation practices.

### 中文一句话结论
预处理去偏方法在减少目标群体刻板印象的同时，常常意外地增加对其他非目标群体（甚至跨类别）的刻板印象或反刻板印象。

### English TL;DR
Preprocessing-based stereotype mitigation methods can inadvertently increase stereotyping or counter-stereotyping for non-target demographic groups, even across unrelated categories, while reducing bias for the intended group.

### 中文详细总结
该论文系统研究了基于预处理的刻板印象缓解方法（如去偏语料预训练/后训练）的副作用。实验表明，虽然这些方法能有效降低针对目标群体（如女性、黑人、穆斯林）的刻板印象，但经常导致对其他非目标群体（包括跨类别如性别、种族、宗教）的刻板印象或反刻板印象增强。这种现象在两种模型架构（仅编码器TinyBERT和仅解码器GPT-2）、三种预处理策略（删除刻板句子、删除群体提及、交换群体引用）、不同训练数据规模以及预训练/后训练阶段中均稳定出现。标准基准测试（如StereoSet、CrowS-Pairs）经常遗漏这些偏移。注意力传播分析表明，这些副作用不完全由注意力流变化解释，机制尚不明确。作者呼吁在评估去偏方法时考虑副作用，并提出可操作的诊断方案。

### 方法 / 贡献
- 系统定义并验证了预处理去偏方法的“副作用”现象：目标群体偏误降低但非目标群体偏误增加。
- 在两种模型（TinyBERT、GPT-2）、三种预处理策略（删除刻板句子、删除群体提及、交换引用）、两种训练阶段（预训练/后训练）及不同数据规模下进行实验。
- 使用注意力传播分析初步探索机制，发现注意力流变化不足以解释副作用。
- 指出标准评估基准的不足，提出副作用感知的评估建议。

### 实验或数据
- 数据：英文Wikipedia（2023年6月快照），经清洗后用于预训练/后训练。
- 目标群体：6个群体（性别：女/男；种族：黑人/白人；宗教：穆斯林/基督教）。
- 预处理策略：DG（删除刻板句子）、RG（删除群体提及）、SR（交换组内引用）。
- 模型：TinyBERT（encoder-only）、GPT-2（decoder-only，124M参数）。
- 评估：StereoSet（整体SS、LMS、iCAT及群体级SS）和CrowS-Pairs（按类别得分）。
- 附加分析：注意力传播（attention-rollout）。

### 值得关注点
- 副作用稳定且难以预测，跨模型、策略、训练阶段均存在。
- 标准基准如StereoSet、CrowS-Pairs可能错过这些偏移，需更细粒度的群体级评估。
- 注意力传播分析未能提供清晰机制解释，表明可能需要因果分析或分布分析。
- 作者建议在去偏实践中透明报告副作用，并开发更鲁棒、可解释的控制方法。

### 局限性
- 实验限于较小模型（TinyBERT、GPT-2 small），更大模型（如GPT-3）仅在一个后训练切片上验证定性现象。
- 机制理解尚不充分，注意力传播分析未发现显著变化，无法提供明确解释。
- 仅研究了三种预处理策略，可能还有其它策略产生不同副作用。
- 刻板印象检测器（用于DG）可能本身带有偏差。
- 仅使用Wikipedia语料，其他领域语料可能表现不同。

## 9. SQuaD-SQL: Efficient Text-to-SQL with Small Language Models via LLM-Guided Knowledge Distillation

- Source: arxiv
- arXiv ID: 2607.08161
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.08161v1
- PDF: https://arxiv.org/pdf/2607.08161v1
- DOI: https://doi.org/10.48550/arXiv.2607.08161

### Authors

Wangyu Wu, Xiaojian Lin, Rong Fu, Zaiyang Yu, Xuhang Chen, Wenjun Yu, Zhenhong Chen

### Abstract

Text-to-SQL is a fundamental task in natural language processing that enables users to interact with structured databases using natural language. While large language models (LLMs) have demonstrated remarkable performance on this task, their substantial computational requirements hinder deployment in resource-constrained settings. In this paper, we introduce SQuaD-SQL (Small-Qualified and Distilled for SQL), a novel approach that empowers small language models (SLMs) to approach the performance of LLMs on the Text-to-SQL task while significantly improving efficiency through knowledge distillation and synthetic data generation. Our method comprises three key components: (1) LLM-based synthetic data generation, where structured knowledge is extracted from LLMs via carefully designed prompting strategies; (2) parameter-efficient fine-tuning, enabling full model training on a single consumer-grade GPU; and (3) domain-adaptive fine-tuning, where domain-specific synthetic data further enhances performance in targeted domains. Experiments on the WikiSQL dataset demonstrate that SQuaD-SQL achieves an execution accuracy of 86.9% on the test set, approaching the performance of LLMs while offering faster inference and lower memory usage. These results suggest that, with proper training strategies, SLMs can serve as practical and efficient alternatives for Text-to-SQL applications in resource-limited environments.

### 中文一句话结论
SQuaD-SQL通过大语言模型引导的知识蒸馏与合成数据生成，使1.5B参数的小语言模型在WikiSQL测试集上达到86.9%的执行准确率，逼近大模型性能，同时显著提升推理效率。

### English TL;DR
SQuaD-SQL proposes a teacher-student framework that uses LLM-guided knowledge distillation and synthetic data generation to train small language models, achieving competitive text-to-SQL performance (86.9% execution accuracy on WikiSQL) with significantly improved efficiency on resource-constrained hardware.

### 中文详细总结
本论文提出SQuaD-SQL（Small-Qualified and Distilled for SQL）方法，旨在解决大语言模型在文本到SQL任务中计算资源需求过高的问题。该方法采用教师-学生框架，以大语言模型为教师生成结构化监督信号，通过知识蒸馏使小语言模型（如Qwen-1.5B）学习SQL推理模式。方法包含三个核心组件：(1) 基于LLM的合成数据生成，通过精心设计的提示策略从大模型提取结构化知识；(2) 参数高效微调（LoRA），使整个训练可在单张消费级GPU上完成；(3) 领域自适应微调，通过领域特定合成数据进一步提升性能。在WikiSQL数据集上，SQuaD-SQL达到86.9%的执行准确率，逼近大模型水平，同时推理速度更快、内存占用更低。结果表明，在资源受限环境中，小语言模型通过合适的训练策略可成为文本到SQL任务实用且高效的替代方案。

### 方法 / 贡献
- 提出教师-学生学习框架，将大语言模型的结构化推理能力迁移至小语言模型
- 设计LLM驱动的合成数据生成与多阶段高质量筛选流水线（语法验证、LLM自评估打分、执行验证）
- 采用LoRA参数高效微调，使完整训练可在单张消费级GPU（如RTX 4090）上运行
- 引入领域自适应微调，通过生成特定领域的合成SQL样本增强模型泛化能力

### 实验或数据
- 在WikiSQL数据集上进行评估，测试集执行准确率为86.9%
- 使用Qwen-1.5B作为基础学生模型
- 消融实验表明三阶段过滤策略（语法检查、LLM评分、执行验证）显著提升训练稳定性和最终性能
- 推理效率相比大语言模型有显著提升（具体数字未在摘要中明确给出）

### 值得关注点
- 86.9%的执行准确率仅使用1.5B参数模型，展示了小模型在结构化推理任务上的潜力
- 整个训练流程可在单张消费级GPU上完成，大幅降低了部署门槛
- 合成数据生成的提示策略设计是提升数据质量的关键因素
- 三阶段数据筛选方法有效保证了伪标签的质量

### 局限性
- 实验仅在WikiSQL数据集上进行，在更复杂的跨领域数据集（如Spider）上的表现尚待验证
- 合成数据生成依赖GPT-4o等大语言模型，仍存在一定成本
- LLM自评估打分的可靠性可能受模型自身偏差影响
- 领域自适应微调需要特定领域的先验知识或额外数据收集

## 10. Selective Left-Shift: Turning Test-Time Compute and Difficulty-based Curation into Training Data for Low-Resource Code Generation

- Source: arxiv
- arXiv ID: 2607.07748
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.07748v1
- PDF: https://arxiv.org/pdf/2607.07748v1
- DOI: https://doi.org/10.48550/arXiv.2607.07748

### Authors

Didula Samaraweera, Anjana Supun, Srinath Perera

### Abstract

Large Language Models achieve strong code generation for high resource languages like Python and Java but suffer sharp performance drops on Low-Resource Programming Languages~(LRPLs) such as Julia. Improving Small Language Models~(SLMs) for these languages faces a trilemma: Supervised Fine-Tuning~(SFT) is bottlenecked by data scarcity, inference-time scaling is too expensive for deployment, and Reinforcement Learning from scratch yields near zero advantages. We propose a three-phase pipeline that resolves this trilemma by decoupling syntax acquisition from algorithmic reasoning. First, we \emph{left-shift} inference-time compute to an offline data synthesis engine that uses iterative compiler and test feedback to generate verified training examples. Second, we fine-tune an SLM on this synthetic, verified data to embed strong syntactic priors. Third, we apply Reinforcement Learning with Verifiable Reward~(RLVR) grounded by language-agnostic Input/Output tests, where the SFT prior constrains exploration away from syntax errors. Applied to Qwen3-8B, our pipeline improves pass@1 by up to +7.6 points on MultiPL-E and +14.2 points on the Agnostics LiveCodeBench for Julia compared to SOTA results. Furthermore, the pipeline only used $\frac{1}{3}$ data and $\frac{1}{6}$ cost over the previous state-of-the-art. We further demonstrate that the pipeline generalizes to Ballerina achieving 49.7\% MultiPL-E Pass@1, a language with near-zero pretraining representation. Ablations confirm that both the SFT phase and execution-grounded rewards are necessary for stable training.

### 中文一句话结论
本文提出一种三阶段流水线，通过将测试时计算左移到离线数据合成，并结合难度筛选数据与强化学习，以更少的数据和成本在低资源编程语言代码生成上达到当前最佳性能。

### English TL;DR
This paper proposes a three-phase pipeline that resolves the trilemma of data scarcity, inference cost, and sparse rewards for low-resource code generation by shifting test-time compute offline to generate verified training data for supervised fine-tuning, followed by difficulty-curated reinforcement learning, achieving state-of-the-art performance on Julia and Ballerina with significantly less data and cost.

### 中文详细总结
大型语言模型在高资源编程语言（如Python、Java）上代码生成表现强劲，但在低资源编程语言（如Julia、Ballerina）上性能急剧下降。提升小语言模型在这些语言上的能力面临三元困境：监督微调受数据稀缺瓶颈限制；测试时缩放（如迭代自修正）成本过高，不适用于实际部署；从零开始强化学习（如RL或GRPO）因语法错误众多导致奖励稀疏，几乎无益。本文提出的三阶段流水线，通过解耦语法获取与算法推理来解决此困境。第一阶段将测试时计算左移到一个离线数据合成引擎，利用编译器和测试反馈迭代生成经过验证的训练样本。第二阶段在此合成并验证的数据上对SLM进行监督微调，嵌入强语法先验。第三阶段应用基于语言无关输入/输出测试结果的可验证奖励的强化学习，其中SFT先验限制探索避开语法错误。在Qwen3-8B上，流水线在MultiPL-E和Agnostics LiveCodeBench上分别取得超过当前最佳7.6和14.2个百分点的pass@1提升，仅使用约1/3数据和1/6成本。方法还泛化到Ballerina（预训练语料几乎为零），达到49.7%的MultiPL-E Pass@1。消融实验确认SFT阶段和执行基础奖励对稳定训练均必不可少。

### 方法 / 贡献
1. 提出一个三阶段流水线：
   - 阶段一（离线数据合成）：将测试时计算左移，利用迭代的编译器和测试用例反馈合成并验证训练样本（含差分测试或I/O测试）。
   - 阶段二（监督微调）：在合成验证数据上SFT，使模型获得强语法先验。
   - 阶段三（困难度筛选强化学习）：基于问题ELO评分筛选适当难度的数据，使用GRPO和基于I/O测试的部分奖励，并采用零优势掩码避免收敛到次优解。
2. 通过SFT先导降低RL阶段语法错误，使RL高效学习逻辑推理。
3. 验证了在Ballerina从零引导代码生成的能力，扩展了MultiPL-E基准。

### 实验或数据
- 基础模型：Qwen3-8B。
- 基准数据：来自竞赛编程数据集的I/O测试用例（无目标语言参考代码）；验证使用MultiPL-E和Agnostics LiveCodeBench。
- 主要结果：
  - Julia：完整流水线pipeline在MultiPL-E上达68.6%（+24.6点对基线），Ag-LCB上达39.2%（+30.2点）。
  - Ballerina：MultiPL-E达49.7%（+45.3点），Ag-LCB达25.0%。
  - 成本：仅使用1/3数据和1/6成本达到当前最佳。
- 消融：不含SFT直接RL时训练不稳定；移除执行奖励会退化；零优势掩码缓解模式崩塌。

### 值得关注点
- “左移”推理：将昂贵的测试时计算转为一次性离线数据合成，解决部署延迟问题。
- 困难度筛选强化学习：基于ELO评分选择适当难度数据提高学习效率。
- 强泛化性：在预训练几乎无表示的Ballerina上仍能显著提升。
- 部分奖励（基于通过测试比例）和零优势掩码设计有效提升RL稳定性。
- 所有数据通过编译器和测试自动验证，无需人工标注。

### 局限性
- 依赖原始问题具有I/O测试套件或参考实现，对无此类验证信号的极低资源语言可能仍需人工标注或折中策略。
- 当前实验仅针对8B参数模型，在大规模模型（如70B+）上的可扩展性和效果未验证。
- 困难度筛选依赖ELO评分系统，要求先有基准评估数据，冷启动场景下可能需要初始评分机制。
- 仅关注单轮代码生成，未评估多轮迭代或对话式生成场景。
- 实验局限于Julia和Ballerina，对其他低资源语言的泛化性尚需更多验证。

## Processing Notes

- Duplicate papers skipped: 0