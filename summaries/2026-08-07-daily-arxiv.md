# Daily arXiv - 2026-08-07

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-07T02:05:10
- Paper count: 10

## 1. Easy to Complete, Hard to Choose: Investigating LLM Performance on the ProverbIT Benchmark

- Source: arxiv
- arXiv ID: 2608.04670
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.04670v1
- PDF: https://arxiv.org/pdf/2608.04670v1
- DOI: https://doi.org/10.48550/arXiv.2608.04670

### Authors

Enrico Mensa, Lorenzo Zane, Calogero Jerik Scozzaro, Matteo Delsanto, Tommaso Milani, Daniele Paolo Radicioni

### Abstract

Large Language Models (LLMs) have transformed computational linguistics and achieved remarkable performance across numerous natural language processing tasks, yet significant gaps persist in understanding how these systems process culturally embedded linguistic expressions. This paper introduces ProverbIT, a novel Italian benchmark comprising 100 multiple-choice questions designed to evaluate LLMs' ability to complete Italian proverbs. We assess 13 frontier models, including Large Reasoning Models (LRMs) and traditional LLMs, across three tasks: proverb completion, multiple-choice selection with correct answers, and multiple-choice selection without correct answers. Our evaluation reveals surprising results: while nearly all models demonstrate knowledge of the proverbs through successful completion tasks, performance drops dramatically when transitioning to multiple-choice formats without correct answers, with even state-of-the-art reasoning models showing substantial degradation. Through detailed Chain-of-Thought analysis of two LRMs, we uncover that models exhibit a strong bias toward selecting literal synonyms and frequently mention correct proverb endings during reasoning without successfully identifying their absence from the given options. These findings suggest that current LLMs rely heavily on memorized patterns rather than deeper semantic understanding of culturally grounded expressions, highlighting important limitations in their reasoning capabilities for figurative language comprehension.

### 中文一句话结论
LLMs 在谚语补全任务上表现良好，但在没有正确答案的多选题中性能急剧下降，暴露出其依赖记忆模式而非深层语义理解的问题。

### English TL;DR
LLMs perform well on proverb completion but drop sharply in multiple-choice tasks without correct answers, revealing reliance on memorized patterns rather than deep semantic reasoning.

### 中文详细总结
本文提出 ProverbIT，一个包含 100 道意大利谚语多选题的新基准，用于评估 LLMs 对文化嵌入语言的理解能力。实验测试了 13 个前沿模型（包括大型推理模型 LRMs 和传统 LLMs），涉及三种任务：谚语补全、有正确答案的多选题、无正确答案的多选题。结果显示，几乎所有模型在补全任务上表现良好，但在无正确答案的多选题中性能大幅下降，即便最先进的推理模型也表现不佳。通过链式思维分析两个 LRMs，发现模型倾向于选择字面同义词，且在推理过程中常提及正确结尾却未能识别其缺失。这表明当前 LLMs 主要依赖记忆模式，而非对文化表达的深层语义理解，暴露出其在比喻语言推理上的重要局限。

### 方法 / 贡献
- 构建 ProverbIT 数据集：100 道意大利谚语多选题，每个谚语配四个精心设计的错误选项（谐音、字面同义、反转、冗余），并设“以上皆非”选项。
- 评估 13 个前沿模型，包括 LRMs（如 GPT o3、DeepSeek R1）和传统 LLMs，对比三种任务形式。
- 通过链式思维分析，揭示模型在推理过程中的常见错误模式（如偏向字面同义词、无法识别正确结尾缺失）。
- 贡献了意大利语 NLP 基准，并深入分析了 LLMs 在文化语言理解上的缺陷。

### 实验或数据
- 数据集：ProverbIT，100 个意大利谚语，每个配四个错误选项，共 100 道多选题。
- 模型：13 个，包括 Claude Sonnet 4、GPT 4o、GPT o3、DeepSeek V3、DeepSeek R1、Gemini 2.5 Flash、Gemini 2.5 Pro、Qwen 3 等。
- 任务：谚语补全、有正确答案的多选题、无正确答案的多选题。
- 分析：对两个 LRMs 进行链式思维分析，识别错误模式。

### 值得关注点
- 模型在谚语补全上表现良好，但多选题（尤其无正确答案时）性能骤降，凸显“记忆”与“理解”的差距。
- 链式思维分析揭示模型在推理中常提及正确结尾，但无法辨别其缺失，表明语义理解不足。
- 错误选项设计（谐音、字面同义等）有效暴露了模型依赖表面模式而非深层语义的弱点。

### 局限性
- 数据集仅涵盖意大利语，结论推广到其他语言需验证。
- 错误选项设计人为，可能无法完全反映真实语言使用中的多样性。
- 模型数量有限，且部分模型参数未公开，可能影响可复现性。
- 缺乏对模型在真实对话或跨文化语境中表现的探索。

## 2. Strengthening Target-Language Features: SAE-Based Steering for Multilingual Inference

- Source: arxiv
- arXiv ID: 2608.04904
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.04904v1
- PDF: https://arxiv.org/pdf/2608.04904v1
- DOI: https://doi.org/10.48550/arXiv.2608.04904

### Authors

Hongsheng Wang, Phlipp Koehn

### Abstract

Multilingual large language models exhibit substantial performance differences across languages, while existing adaptation methods often require parameter updates and considerable multilingual training data. We propose an inference-time multilingual steering method that uses pretrained sparse autoencoders to identify and strengthen target-language-related features. Using multilingual parallel sentences, we compare SAE activations across languages and select a small number of layer-specific features associated with each target language. These features are decoded into steering signals and injected into the model's hidden states without additional training. Experiments with Gemma-3-12B-it show average accuracy improvements of 10.9 percentage points on XCOPA, 5.3 points on XNLI, and 1.9 points on MGSM.

### 中文一句话结论
本文提出一种基于稀疏自编码器（SAE）的推理时多语言引导方法，无需训练或参数更新即可通过强化目标语言相关特征，在多个多语言推理基准上显著提升模型准确率。

### English TL;DR
This paper proposes an inference-time multilingual steering method that uses pretrained sparse autoencoders to identify and strengthen target-language features, improving multilingual LLM performance on reasoning tasks without additional training or parameter updates.

### 中文详细总结
多语言大模型在不同语言上的性能差异显著，现有适应方法通常需要参数更新和大量多语言训练数据。本文提出一种推理时（inference-time）的多语言引导（steering）方法，利用预训练的稀疏自编码器（SAE）识别并强化与目标语言相关的特征。具体而言，使用多语言平行句对，通过比较不同语言下SAE激活值，在每个Transformer层选择少量与目标语言最相关的特征，将这些特征解码为引导信号并注入模型的隐藏状态，无需任何额外训练。在Gemma-3-12B-it上的实验表明，该方法在XCOPA、XNLI和MGSM三个基准上分别平均提升了10.9、5.3和1.9个百分点。

### 方法 / 贡献
- **方法**：使用预训练SAE将模型隐藏状态分解为稀疏特征；利用平行句对计算目标语言与参考表示（多语言质心或英语）的激活差异，选择差异最大的top-k特征；构造稀疏SAE编码并通过解码器生成引导向量，在选定层（如第47层）的最终提示位置注入隐藏状态，干预后续生成。
- **贡献**：
  1. 提出一种无需参数更新的SAE-based多语言引导方法，通过平行句对识别稀疏的目标语言特征并在推理时强化。
  2. 在常识推理、自然语言推理和数学推理三个多语言基准上验证了方法的有效性。
  3. 通过消融实验分析了语言信息、语义内容、参考表示和引导强度等因素的作用。

### 实验或数据
- **模型与SAE**：使用Gemma-3-12B-it（48层），采用Gemma Scope 2提供的官方SAE（每层16,384个特征，小L0变体）。
- **特征识别语料**：FLORES-200中的500个平行句组，用于估计语言相关特征，不用于下游评估。
- **下游基准**：
  - XCOPA：9种语言，每语言500例（100验证/400测试）。
  - XNLI：9种语言，每语言500例（100验证/400测试）。
  - MGSM：4种语言（德、西、法、日），每语言250例（50验证/200测试）。
- **主要结果**：平均准确率提升XCOPA +10.9，XNLI +5.3，MGSM +1.9个百分点。层选择实验显示第6层和第47层增益最高（13.9和13.4点），主实验采用第47层。

### 值得关注点
- 无需训练或参数更新，仅需推理时少量计算，适合低资源语言场景。
- 使用SAE特征而非全表示干预，更精准地控制语言信息，且可解释性更强。
- 对比了多语言质心和英语作为参考，验证了“英语中心表示”假设的可行性。
- 代码已开源（https://github.com/HungsingWong/sae-language-steering）。

### 局限性
- 需依赖预训练SAE（如Gemma Scope 2），对未提供SAE的模型不直接适用。
- 实验仅在单一模型（Gemma-3-12B-it）上验证，泛化性未知。
- 特征识别依赖平行语料（FLORES-200），对低资源语言可能缺乏足够平行数据。
- 引导层和特征数量（k=3）为超参数，需通过验证集调优，可能影响实用性。

## 3. The Fairness Collapse Phenomenon: Bias Amplification in Language Models Trained on Synthetic Data

- Source: arxiv
- arXiv ID: 2608.04268
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.04268v1
- PDF: https://arxiv.org/pdf/2608.04268v1
- DOI: https://doi.org/10.48550/arXiv.2608.04268

### Authors

Irina Proskurina, Antoine Gourru, Julien Velcin

### Abstract

Generative models trained on artificially generated data have been shown to exhibit model collapse, resulting in significant performance degradation. As synthetic content increasingly contaminates the training corpora of language models, this raises critical concerns about the use of open data in continued pretraining. Although previous work has demonstrated model collapse in language models, it remains unclear whether exposure to synthetic data amplifies or attenuates the social biases already present in pretrained models. Because language models are known to reproduce and amplify demographic stereotypes, recursive training on self-generated data may create a self-reinforcing feedback loop in which biased associations become progressively stronger across generations. We call this hypothesized phenomenon fairness collapse. In this work, we construct controlled training regimes in which models are repeatedly trained on synthetic data using the Bias in Bios dataset. Across experiments, we observe a consistent and concerning pattern: fairness degradation emerges before substantial degradation is reflected by standard language-modeling metrics. This result highlights a critical risk associated with synthetic data contamination in language model training: bias can increase silently before strong indicators of model collapse become apparent.

### 中文一句话结论
在语言模型训练中使用合成数据会悄无声息地放大社会偏见，而这种偏见的恶化在标准指标显示模型退化之前就已经发生。

### English TL;DR
Training language models on synthetic data can silently amplify social biases—a phenomenon termed "fairness collapse"—before standard metrics of model collapse show any degradation.

### 中文详细总结
本论文提出了“公平性崩溃”（fairness collapse）现象，即当语言模型反复在自身生成的合成数据上训练时，性别与职业相关的社会偏见会逐步放大，且这种放大发生在传统模型崩溃指标（如困惑度、词频多样性）显著恶化之前。作者使用Bias in Bios数据集（平衡子集，包含27,752篇传记，覆盖28种职业），通过少样本生成和种子生成两种方式合成传记文本，并设计了迭代重训练和递归污染两种训练机制。实验发现，在所有设置下，公平性指标（如性别-职业关联偏差）都在标准语言建模性能保持稳定时就开始持续下降。这表明合成数据污染可能带来“隐性”的偏见放大风险，而现有模型评估体系可能忽略这一早期警报。

### 方法 / 贡献
- 提出“公平性崩溃”概念，区分于传统模型崩溃，强调偏见放大是更早的退化信号。
- 构建两种受控训练机制：**迭代重训练**（每次用新生成的合成数据从基础模型重新训练）和**递归污染**（每次从上一轮检查点继续训练），以隔离合成数据本身与参数累积的影响。
- 采用两种合成数据生成策略：**少样本生成**（每个职业提供3篇人类传记作为上下文）和**种子生成**（从人类传记中截取前k个token作为前缀，模型续写剩余部分）。
- 使用Bias in Bios数据集进行实验，评估指标包括困惑度、词频多样性、以及性别-职业关联的偏差度量。

### 实验或数据
- **数据集**：Bias in Bios（约300k篇传记，28种职业），经平衡处理后的子集（27,752篇，约200万token）。
- **合成数据生成**：少样本（K=3）和种子生成（种子长度从5到50 token变化）。
- **训练机制**：人类数据仅训练基线、迭代重训练、递归污染，每个设置运行多轮迭代。
- **主要发现**：在所有设置下，公平性指标在早期迭代中即显著下降，而困惑度等语言建模指标在后期才出现退化。词频多样性（如TTR）也随迭代下降，但下降速度慢于公平性退化。

### 值得关注点
- **早期预警信号**：公平性崩溃比传统模型崩溃更早出现，意味着模型在语言质量尚可时已开始系统性放大偏见。
- **隐性风险**：标准评估指标（如困惑度）无法捕捉这一退化，因此现有模型评估可能遗漏关键的社会影响。
- **实际意义**：随着网络数据中合成内容比例上升，该发现对模型持续预训练的数据治理提出警示：必须监控公平性指标而非仅关注性能指标。

### 局限性
- 论文未明确讨论局限性，但实验仅基于单一数据集（Bias in Bios）和单一基础模型（Qwen），结果可能不泛化到其他领域或模型架构。
- 仅研究了性别-职业偏见，未涉及其他人口属性（如种族、年龄）或更复杂的社会偏见形式。
- 合成数据生成策略相对简单（少样本/种子），可能无法完全模拟真实世界中合成数据污染的多样性（如混合人类与合成数据的不同比例）。

## 4. OctoLong: Mid-Training On Cross-Repository Code Contexts Enhances Long-Context Modeling

- Source: arxiv
- arXiv ID: 2608.05141
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.05141v1
- PDF: https://arxiv.org/pdf/2608.05141v1
- DOI: https://doi.org/10.48550/arXiv.2608.05141

### Authors

Indraneil Paul, Falko Helm, Goran Glavaš, Iryna Gurevych

### Abstract

Context lengths of language models (LMs) have dramatically increased, driven by the demands for in-context learning, self-improvement, and long-horizon agentic workflows. Existing long-context corpora, however, are dominated by books, academic articles, and code repositories, which are finite resources and often scarce in long-distance dependencies. In this work, we introduce OctoLong, a context engineering pipeline that instruments an AST parser, a language server backend, and a package manager to facilitate the recursive retrieval of code references, enabling the curation of dependency-rich code contexts of millions of tokens in length. We then train OctoLong-Instruct, a suite of capable long-context open LMs, derived from base models ranging in size from 600M to 14B parameters, via context-extension mid-training on a ~50B-token mixture containing ~6.2B tokens of OctoLong code contexts, followed by ~10B tokens of instruction tuning. Our training ablations and experimental evaluations against 18 state-of-the-art open-weight long-context LMs show that supplanting just 12% of traditional context-extension corpora with OctoLong data yields substantial gains in long-range retrieval, long-term state tracking, repository-level code understanding, and downstream agentic tasks, while also enhancing API usage in short-context coding scenarios.

### 中文一句话结论
OctoLong通过跨仓库代码依赖挖掘生成长上下文数据，在长上下文模型中显著提升检索、状态跟踪、代码理解和智能体任务性能。

### English TL;DR
OctoLong introduces a pipeline for generating dependency-rich cross-repository code contexts and demonstrates that mid-training on such data substantially improves long-context modeling across retrieval, state tracking, code understanding, and agentic tasks.

### 中文详细总结
本文提出OctoLong，一种利用AST解析器、语言服务器（LSP）和包管理器递归检索代码依赖的上下文工程流水线，可生成数百万token量级、依赖关系丰富的跨仓库代码上下文。基于该流水线收集约62亿token的跨仓库长上下文数据，与其它来源混合构成约500亿token的LCFT语料，再结合约100亿token的指令微调数据，对Qwen3系列模型（600M至14B参数）进行长上下文扩展训练，得到OctoLong-Instruct模型套件。实验表明，仅用12%的OctoLong数据替换传统长上下文语料，即可在长距离检索、长期状态跟踪、仓库级代码理解和下游智能体任务上取得显著提升，同时增强短上下文编码场景中的API使用能力。

### 方法 / 贡献
1. 提出OctoLong流水线：结合AST解析器、LSP后端和包管理器，递归检索跨仓库代码引用，生成依赖密集的长上下文。
2. 构建OctoLong-LCFT语料（约500亿token，含约62亿token OctoLong数据）和OctoLong-SFT指令微调数据（约100亿token）。
3. 训练OctoLong-Instruct模型套件，将Qwen3基础模型上下文长度扩展至128K。
4. 通过大量实验和消融，证明OctoLong数据在长上下文代码任务、通用长上下文应用及智能体场景中的有效性，且不损害短上下文能力。

### 实验或数据
- 数据：OctoLong流水线生成约62亿token跨仓库代码上下文；与其它来源混合得到约500亿token的LCFT语料；约100亿token指令微调数据。
- 实验：与18个开源长上下文模型对比，评估任务包括长距离检索、状态跟踪、仓库级代码理解和智能体任务；进行消融实验验证OctoLong数据比例（12%）的有效性。

### 值得关注点
- 跨仓库代码依赖挖掘是全新的长上下文数据来源，突破了传统仓库级序列化的局限。
- 仅用12%的OctoLong数据替换传统语料即可带来显著收益，数据效率高。
- 长上下文训练同时提升了短上下文场景中的API使用能力，显示泛化性。

### 局限性
论文摘要未明确讨论局限性。可能存在的局限包括对语言服务器和包管理器生态的依赖（如主要支持Python、JavaScript等流行语言），以及跨仓库引用解析的覆盖率和计算开销。此外，实验仅基于Qwen3系列模型，未验证在其他架构上的可迁移性。

## 5. Kathleen Writes: Autoregressive Generation and Data Scaling Without Attention

- Source: arxiv
- arXiv ID: 2608.04678
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.04678v1
- PDF: https://arxiv.org/pdf/2608.04678v1
- DOI: https://doi.org/10.48550/arXiv.2608.04678

### Authors

George Fountzoulas

### Abstract

Papers 1-2 of the Kathleen series showed that a byte-level, attention-free architecture built from a wavetable encoder and multi-scale reverberant state can match strong baselines on classification at ~450-700K parameters, without pretraining. We ask whether the same ingredients can generate. (1) Scaling: on byte-level language modeling (WikiText-103, raw UTF-8, no tokenizer), the reverberant model beats a parameter-matched transformer at every dataset scale measured (2-512 MB), e.g. 1.84 vs 2.04 bits/byte at 512 MB with ~0.5M parameters; the transformer needs more than 512 MB to match what the attention-free model learns from 32 MB. (2) Measurement: we introduce FORM DISTANCE, a non-parametric, gaming-resistant instrument for "reads like text": nine statistical axes of human text define a reference cloud, and five constructed fakes are all rejected. (3) Generation: decoding policy dominates architecture -- widening the sampler halves the same model's distance (3.17 to 1.52), and a retrieval-augmented decoding scheme takes the frozen model further (1.52 to 1.14) with no training step involved; the ablation attributes the gain to the sparse phrase dose itself, not the selection gate. The gain has a sharp boundary condition: the phrases must come from the model's own training corpus -- a 40x larger foreign library helps not at all, an effect the attention twin shares, consistent with in-context integration being a capability of scale. We also report four architectural additions that did not help, and a computed lexicon reaching 94% of a learned table's top-1 accuracy at one fifth of the parameters. Everything runs offline; all experiments are reproducible on a free Kaggle T4.

### 中文一句话结论
本文提出一种无需注意力机制、基于字节级自回归的轻量架构（约0.5M参数），在语言建模和生成质量上均优于参数匹配的Transformer，并发现解码策略和从训练语料中检索短语对生成质量的影响远超架构本身。

### English TL;DR
This paper shows that a small, attention-free, byte-level architecture can generate text competitively, beating a parameter-matched transformer in data efficiency across all scales, while revealing that decoding policy and retrieval from the model's own training corpus dominate generation quality more than architectural additions.

### 中文详细总结
本文是Kathleen系列第三篇，在之前分类任务基础上，验证了同一架构（字节级波表编码器+多尺度混响状态，无注意力）能否进行自回归生成。主要发现：1）在字节级语言建模（WikiText-103原始UTF-8）上，混响模型在2-512MB所有数据规模下均优于参数匹配的Transformer（如512MB时1.84 vs 2.04 bits/byte），数据效率高16倍以上；2）提出FORM DISTANCE非参数化评估指标，9个统计轴衡量文本“像人写”的程度，且能抵抗游戏化；3）生成质量主要受解码策略（如采样宽度）和从训练语料中检索短语影响，架构改进贡献很小，且检索短语必须来自自身训练语料（40倍大的外来语料无效）。论文还报告了四种无效的架构添加，以及一个计算词典达到学习表94% top-1准确率但困惑度不如。

### 方法 / 贡献
- 提出无注意力、字节级自回归架构（ByteRotate编码器+多尺度混响状态），总参数量~0.5M（字节级）或~3M（词级）。
- 首次在字节级语言建模上展示数据扩展曲线：混响模型在所有数据量下优于Transformer，且数据效率优势显著。
- 提出FORM DISTANCE指标：9个统计轴（词汇丰富度、流畅度、局部重复、n-gram合理性等）构建非参数、防游戏化的文本质量计量器。
- 系统归因生成质量：解码策略和检索式解码（从训练语料中取短语）主导改进，架构改进（4种尝试）无效。
- 验证检索短语必须来自自身训练语料（注意力和混响架构均如此），表明小模型缺乏上下文整合能力。
- 报告计算词典（梯度无关）达到学习表94% top-1准确率但困惑度不匹配。

### 实验或数据
- **语言建模**：WikiText-103（原始UTF-8，无分词器），训练数据切片2/8/32/128/512MB，固定1MB测试集，2个epoch，序列长256字节。混响模型与参数匹配的4头因果注意力Transformer对比，两次种子重复，额外在enwik8上验证（2/8/32MB）。
- **下游迁移**：在SST-2和IMDB上使用冻结预训练主干+线性分类头（仅258参数）评估，混响模型在所有预训练规模下均优于注意力模型。
- **生成质量评估**：FORM DISTANCE使用400个人类WikiText段落构建参考云，5种构造伪文本（词汤、鹦鹉、无人机等）全部被拒绝。生成实验：解码策略（top-1000, T=1.15）将距离从3.17降至1.52；检索式解码进一步降至1.14，且增益来自短语剂量本身而非门控机制。检索源必须来自自身训练语料（40倍大学术库无效）。
- **硬件**：所有实验在免费Kaggle T4或H100上运行，可复现。

### 值得关注点
- 小模型（~0.5M参数）在无注意力和无预训练条件下，语言建模性能超过参数匹配的Transformer，数据效率优势巨大（Transformer需512MB才能匹配混响模型32MB的性能）。
- 解码策略和检索式解码对生成质量的影响远大于架构改进，且检索短语必须来自模型自身训练语料，表明小模型缺乏上下文整合能力，这一发现具有普适性（两种架构均如此）。
- FORM DISTANCE指标设计精巧，能抵抗游戏化（作者坦承早期8轴版本被游戏化，后增加第9轴修复）。
- 论文诚实报告了四项无效的架构改进，以及计算词典的局限。

### 局限性
- 实验仅限于~0.5M参数（字节级）和~3M参数（词级）规模，未探索更大参数规模下的行为（如计算最优前沿）。
- 数据扩展曲线显示混响模型优势在512MB后趋于平坦，两者均受固定容量上限限制，未验证更大量数据下的表现。
- FORM DISTANCE指标基于表面统计，可能无法完全捕捉语义深度或长程一致性。
- 检索式解码的增益仅来自训练语料，无法利用外部知识库。
- 论文未涉及多语言、对话或指令微调等任务，生成能力局限于语言建模采样。

## 6. Protoreasoning in Tiny Transformers

- Source: arxiv
- arXiv ID: 2608.04980
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.04980v1
- PDF: https://arxiv.org/pdf/2608.04980v1
- DOI: https://doi.org/10.48550/arXiv.2608.04980

### Authors

Eduardo Valle, Fergal Reid

### Abstract

We show that tiny transformers can profitably employ a simple form of Chain of Thought, which we call protoreasoning, allowing us to study step-by-step reasoning on ~1M-parameter models and opening up opportunities for much more detailed experimentation and analysis than is feasible for larger models. Current Large Language Models exhibit impressive step-by-step reasoning, but we have yet to understand its generality, i.e., when and how LLMs learn genuinely general algorithms rather than "bags of heuristics." Such questions are hard to settle on compute-intensive frontier models trained on opaque data. To work at model scales far below the threshold for natural-language competence, we define reasoning-friendly tasks on Dyck languages (sentences of correctly nested brackets). We find that protoreasoning traces substantially close the out-of-distribution generalization gap, and ablations confirm that the trace's content, not merely its extra tokens, drives the gain.

### 中文一句话结论
本文通过在百万级参数的小型Transformer上引入Dyck语言上的"原推理"(protoreasoning)轨迹，证明了即使远低于自然语言能力所需规模的模型也能受益于逐步推理，且推理轨迹的内容(而非仅仅是额外token)是提升分布外泛化能力的关键驱动因素。

### English TL;DR
This paper demonstrates that tiny transformers (~1M parameters) can benefit from a simple form of chain-of-thought called "protoreasoning" on Dyck language tasks. The trace content (not just extra tokens) drives out-of-distribution generalization gains, enabling detailed mechanistic study of reasoning at small scales.

### 中文详细总结
本研究的核心发现与贡献：

1. **研究动机**：当前大语言模型虽展现出逐步推理能力，但其是否真正学到可泛化的算法仍有争议。由于前沿模型训练成本高昂且数据不透明，难以深入探究推理机制的本质。

2. **创新方法**：
   - 利用小型Transformer作为"模型生物体"，在远低于自然语言能力所需的参数量级(约1M参数)上研究推理
   - 基于Dyck语言(正确嵌套的括号序列)与树结构的自然对应关系，设计了两个可分级难度、可精确验证的任务：
     - **最深路径(DP)**：输出通往最深叶节点的路径上的左括号
     - **最大前叶节点(MPL)**：输出全部由叶节点构成的兄弟节点组中最大组的左括号

3. **关键发现**：
   - 小型模型通过"原推理"(protoreasoning)轨迹——一种确定性草稿纸，反复剪枝不可能属于答案的树节点——能够显著提升分布外泛化能力
   - 消融实验证实，推理过程中产生的内容本身(而非仅仅是增加了额外token)才是性能提升的根本原因
   - 该研究进行了超过1700次训练实验，实现了密集的实验设计

4. **意义**：为研究推理机制提供了一个可控、可验证、计算成本低的最小系统，有助于厘清大语言模型推理能力背后的根本机制。

### 方法 / 贡献
- **方法**：在小型Transformer(约1M参数)上，基于Dyck语言(多种括号类型的正确嵌套序列)与森林结构的双射关系，设计两个推理任务(最深路径DP和最大前叶节点MPL)，并使用"原推理"轨迹(确定性逐步剪枝过程)引导模型推理
- **贡献**：(1)首次在远低于自然语言能力所需规模的小型模型上诱导出逐步推理能力；(2)提出两个难度可分级、结果可精确验证的推理任务；(3)通过1700+次训练实验的密集设计，明确了推理轨迹内容的因果作用

### 实验或数据
- 使用Dyck-k语言(最多k种括号类型)生成句子，通过半长度(括号对数量)和结构参数(深度或最大前叶顺序)控制难度
- 进行了超过1700次独立的训练运行，探索模型在难度轴上的泛化能力
- 实验验证了原型推理轨迹显著缩小了分布外泛化差距，消融实验确认了轨迹内容(而非仅仅是额外token数量)的驱动作用
- 所有实验均在小型模型上完成，计算成本极低("只需稍多一点时间")

### 值得关注点
- 论文创新性地在极小模型上研究推理机制，规避了前沿模型计算成本高、数据不透明的问题
- Dyck语言任务设计巧妙：既可控制难度，又能精确验证答案，适合机制性研究
- 关键消融实验明确分离了"额外token"和"轨迹内容"两个因素，后者才是泛化提升的真正原因
- 超过1700次实验的密集设计提供了统计可靠性
- 该框架可作为研究"推理是否源于真算法还是启发式组合"这一核心争议的理想模型系统

### 局限性
- 任务基于简单形式语言(Dyck语言)，与自然语言推理的复杂性存在显著差距
- 模型极小(约1M参数)，其发现的推理机制是否能够推广到大模型尚不确定
- Dyck语言上的"原推理"与人类或大语言模型的自然语言链式思考在形式和复杂度上有本质区别
- 该研究未探索推理轨迹长度、深度等超参数对性能的影响
- 虽然验证了轨迹内容的重要性，但未深入揭示模型内部如何表示和操作这些轨迹信息的具体机制

## 7. Language Models Generalize to Human-like Word Order Preferences

- Source: arxiv
- arXiv ID: 2608.05028
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.05028v1
- PDF: https://arxiv.org/pdf/2608.05028v1
- DOI: https://doi.org/10.48550/arXiv.2608.05028

### Authors

Amanda Popadich, Shane Steinert-Threlkeld

### Abstract

A central question in language acquisition is whether linguistic biases can emerge from general learning mechanisms operating over underdetermined input. Artificial Language Learning (ALL) studies have shown that human learners reliably generalize beyond the evidence provided, including by preferring scope-homomorphic noun phrase modifier orders. In this work, we investigate whether language models exhibit the same bias under similar conditions. We create a controlled learning environment in which models are trained on a corpus where all noun phrases containing multiple modifiers have been removed, eliminating direct evidence about modifier ordering, and are then evaluated on multiple modifier sentences. Across three model sizes, we find that they consistently prefer scope-homomorphic orders despite never observing them during training. These preferences vary in strength by modifier type. To investigate the source of these preferences, we examine noun-modifier association strength using pointwise mutual information (PMI). While PMI reflects known modifier-ordering patterns, it does not explain the models' ordering preferences. These findings demonstrate that LMs can recover human-like linguistic generalizations from impoverished input and provide a controlled framework for investigating the mechanisms underlying such biases.

### 中文一句话结论
语言模型在从未见过包含多个修饰语的名词短语的情况下，仍能自发习得人类偏好的“作用域同构”修饰语顺序。

### English TL;DR
Language models trained without any multi-modifier noun phrases still generalize to human-like scope-homomorphic modifier order preferences, though pointwise mutual information does not explain these biases.

### 中文详细总结
本研究探讨语言模型是否能在缺乏直接证据的条件下，习得人类语言学习中已知的作用域同构（scope-homomorphic）偏好。实验采用过滤语料训练（FiCT）方法，构建了一个从未出现多修饰语名词短语的训练语料库，确保模型无法直接从输入中学习修饰语排序规则。训练完成后，模型被测试于包含多个修饰语的名词短语上，结果发现，无论模型规模（52M、110M、350M参数量），它们均一致偏好作用域同构的词序（即按语义作用域从小到大排列，如“两个白色猫咪”优于“白色两个猫咪”）。这种偏好因修饰语类型而异：指示词-数词组合偏好最强，指示词-形容词和数词-形容词组合偏好较弱但仍显著。尽管点互信息（PMI）能反映已知的修饰语排序模式，但无法解释模型习得的偏好。研究结果表明，语言模型能从贫乏输入中恢复类似人类的语言归纳偏好。

### 方法 / 贡献
1. 方法：使用过滤语料训练，从2019年Wikipedia语料中移除所有包含多个修饰语的名词短语，仅保留单修饰语例句；采用OPT解码器架构训练三种规模模型。2. 贡献：首次将FiCT范式应用于修饰语排序偏好的研究；证明语言模型能从缺乏直接证据的输入中习得作用域同构偏好；通过PMI分析揭示该偏好并非源于表面统计关联。

### 实验或数据
实验基于Wikipedia 2023年数据构建100M标记训练语料；训练三种模型（52M、110M、350M）；用50对最小对（homomorphic vs non-homomorphic）评估三类修饰语组合（Dem-Num、Dem-Adj、Num-Adj）。结果显示所有模型均偏好同构顺序，准确率约76%-78%，Dem-Num组合偏好最强。混合效应模型显示修饰语类型是主要预测变量，模型规模影响微弱。

### 值得关注点
1. 模型在完全没有看到多修饰语实例条件下仍能习得人类偏好。2. 偏好强度随修饰语类型变化，与人类实验结果一致。3. PMI无法解释模型偏好，暗示模型习得的是更高层级的结构规律。4. 为语言习得“刺激贫困”论证提供了计算模型证据。

### 局限性
1. 模型并非直接模拟人类学习者，迁移性有限。2. 仅测试了英语修饰语顺序，跨语言泛化待验证。3. 偏好来源仍不明确，PMI分析为负结果。4. 训练数据虽经处理，仍可能保留其他间接线索（如单修饰语统计规律）。5. 未探索不同架构（如编码器-解码器）的影响。

## 8. IslamicTurathBench: A Multi-Task, Multi-Discipline Benchmark for Evaluating Large Language Models on the Islamic Scholarly Tradition (turath)

- Source: arxiv
- arXiv ID: 2608.04703
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.04703v1
- PDF: https://arxiv.org/pdf/2608.04703v1
- DOI: https://doi.org/10.48550/arXiv.2608.04703

### Authors

Shahd Gaben, Heba Sbahi, Samer Rashwani, Abdessalam Bouchekif, Mutaz Al-Khatib, Emad Mohamed, Somaya Eltanbouly, Mohammed Ghaly

### Abstract

Large language models (LLMs) are increasingly used for question answering, education, and research, including in religious and cultural domains where answers depend on specialised source traditions. Yet in Islamic Studies, key concepts, methods, and debates preserved in the authoritative scholarly tradition, known as turath, lack high-quality annotated resources. We introduce IslamicTurathBench (ISTB), a multi-task, multi-discipline dataset for evaluating LLMs on classical Islamic scholarship. Developed and reviewed by domain experts, ISTB contains 3,465 question-answer items drawn from 35 recognised source works spanning more than 12 centuries of scholarship across seven key fields of Islamic Studies. To enable comprehensive profiling of model capabilities, ISTB is structured along two axes: scholarly demand (Beginner, Intermediate, and Advanced) and task format (multiple-choice questions, passage-based comprehension, and open-ended knowledge questions). ISTB includes aggregated scores from a scholarly human reference panel and zero-shot baselines from ten systems. The dataset supports reproducible evaluation of language-model behaviour across source works, disciplines, scholarly-demand levels, and question formats in a historically layered scholarly domain.

### 中文一句话结论
IslamicTurathBench 是一个多任务、多学科的基准数据集，包含 3,465 个由专家撰写的问答条目，覆盖 35 部经典伊斯兰学术著作和 7 个学科，用于系统评估大语言模型在伊斯兰学术传统（turāth）上的表现。

### English TL;DR
IslamicTurathBench is a multi-task, multi-discipline benchmark dataset with 3,465 expert-authored question-answer items from 35 classical Islamic scholarly works across seven disciplines, designed to evaluate large language models on the Islamic scholarly tradition (turāth) at three scholarly demand levels and three task formats.

### 中文详细总结
该论文提出了 IslamicTurathBench（ISTB），一个专门用于评估大语言模型在古典伊斯兰学术传统（turāth）上表现的多任务、多学科基准数据集。数据集由领域专家开发并审核，包含 3,465 个问答条目，源自 35 部公认的伊斯兰学术著作，覆盖《古兰经》学、圣训学、伊斯兰教义学、法理学原理、法理学、苏菲主义和先知生平七个学科，时间跨度超过 12 个世纪。ISTB 沿两个维度组织：学术需求层次（初级、中级、高级）和任务格式（多项选择、段落理解、开放问答）。论文还提供了来自学者参考小组的聚合得分以及 10 个系统的零样本基线，支持可重复的模型行为评估。

### 方法 / 贡献
- 构建了一个由领域专家撰写和审核的多学科问答数据集，覆盖 7 个伊斯兰学科。
- 设计了 3×3 评估框架（3 个学术需求层次 × 3 种任务格式），支持系统分析模型在不同知识深度和回答形式下的表现。
- 提供了详细的源著作元数据，允许按学科、学术层次、任务格式等进行细粒度分析。
- 包含学者参考小组的聚合得分和 10 个系统的零样本基线，为社区提供可比较的基准。

### 实验或数据
- 数据集包含 3,465 个问答条目，其中 2,276 个多项选择题，417 个段落理解题，772 个开放知识题。
- 学术需求分布：初级 1,400 个，中级 1,052 个，高级 1,013 个。
- 在 148 个条目的分层子集上收集了学者参考小组的聚合得分。
- 对 10 个系统（包括前沿模型、开放权重模型、阿拉伯语专用模型和伊斯兰领域模型）进行了零样本评估，提供了基线结果。

### 值得关注点
- 基于古典伊斯兰学术著作而非网络材料，具有高权威性和领域特异性。
- 覆盖多个学科，突破了以往单一领域或单一格式的局限。
- 学术需求层次和任务格式的交叉设计，能更全面地剖析模型能力。
- 所有数据经过专家审核，并提供了详细的元数据和验证构件，支持可重复性。

### 局限性
- 数据集仅覆盖 7 个伊斯兰学科，未涵盖伊斯兰学术的全部领域（如伊斯兰哲学、经济学等）。
- 所有源著作均为阿拉伯语，其他语言（如波斯语、乌尔都语）的伊斯兰学术传统未被纳入。
- 数据集主要针对古典文本，可能无法反映当代伊斯兰话语或实践中的问题。
- 论文未明确讨论数据集的偏差或潜在的文化局限。

## 9. Transfer Learning for Named Entity Recognition of Classical Latin through LLM Prompting

- Source: arxiv
- arXiv ID: 2608.04015
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.04015v1
- PDF: https://arxiv.org/pdf/2608.04015v1
- DOI: https://doi.org/10.48550/arXiv.2608.04015

### Authors

Callum Chan

### Abstract

With the increase in digitized resources of Classical Latin texts and modern breakthroughs of Large Language Models (LLMs), I contribute to ancient language research by participating in EvaLatin 2026. This paper describes Team uOttawa's system description and results for the Named Entity Recognition (NER) shared task. The task is divided into two subtasks: coarse-grained NER with 11 classes and fine-grained NER with 28 classes, each evaluated under strict and fuzzy regimes. Through prompt engineering of commercial LLMs gemini-2.5-pro and claude-sonnet-4-5, I show that the underrepresented ancient Latin language can take advantage of cross-lingual transfer learning by using advancements made by the wider LLM development community. Overall, the methods discussed in this report demonstrate very strong results, placing first in both NER subtasks and achieving the best scores across all evaluation metrics and regimes among all submissions.

### 中文一句话结论
通过对gemini-2.5-pro和claude-sonnet-4-5进行精心设计的少样本提示工程，本研究在古典拉丁语命名实体识别任务中取得了最优结果，在所有评价指标和评估机制下均排名第一。

### English TL;DR
This paper demonstrates that prompt engineering with commercial LLMs (gemini-2.5-pro and claude-sonnet-4-5) achieves state-of-the-art results for Classical Latin NER, outperforming all other submissions in both coarse-grained (11 classes) and fine-grained (28 classes) subtasks under strict and fuzzy evaluation regimes.

### 中文详细总结
本研究参与了EvaLatin 2026共享任务，目标是解决古典拉丁语的命名实体识别问题。任务分为两个子任务：粗粒度分类（11个类别）和细粒度分类（28个类别），分别在严格和模糊两种评估机制下进行评价。

研究团队使用商业大型语言模型gemini-2.5-pro和claude-sonnet-4-5，采用零样本和少样本两种提示策略。每个提示模板包含任务概述、任务细节、实体类型说明和输出格式指南四个部分。少样本提示额外提供了3个标注例句作为参考。

研究使用约2900个标注令牌的样本数据进行初步评估，并在约26000个令牌的测试集上进行正式评分。结果表明：
1. 少样本策略在所有指标上均优于零样本策略
2. gemini-2.5-pro在细粒度分类上表现更佳，claude-sonnet-4-5在粗粒度分类上表现更优
3. 两个提交均获得所有子任务和评估机制的第一名
4. 召回率普遍高于精确率，表明模型倾向于过度标注，这源于现代语言对拉丁语词汇的借用导致的偏差

### 方法 / 贡献
- 采用提示工程方法，而非传统的微调方法
- 设计并比较了零样本和少样本两种提示策略
- 对两种不同的商业LLM（gemini-2.5-pro和claude-sonnet-4-5）进行了系统评估
- 展示了通过精心设计的提示，商业LLM可以有效地处理低资源语言的NER任务
- 提供了对所有提示模板的完整记录（附录中）

### 实验或数据
- 样本数据集：约2900个标注令牌，来自诗歌和散文文本
- 测试数据集：约26000个标注令牌，来自塔西佗、老普林尼和奥维德的作品
- 评估指标：精确率、召回率和F1值，在严格和模糊两种机制下评估
- 官方评分使用HIPE 2020评分器
- 提交论文中未报告微调实验的具体数据

### 值得关注点
- 首次使用商业LLM的提示工程方法在古典拉丁语NER任务中取得最优结果
- 少样本策略相比零样本策略有显著提升，证实了上下文示例对低资源语言任务的重要性
- 精确率与召回率之间的差距揭示了现代LLM的语言偏见问题
- 细粒度分类中与第二名差距较大（F1值相差约0.4-0.5），显示出方法的显著优势

### 局限性
- 仅测试了两种商业LLM，未探索开源模型或更大规模模型
- 未深入分析不同示例选择对少样本性能的影响
- 额外的微调实验因时间限制未参与官方评分
- 样本数据集规模较小（约2900个令牌），可能影响初步评估的可靠性
- 未探讨模型在不同文体和时期拉丁语文本上的表现差异

## 10. Do Language Models Know Their Slang? Queer Slang Understanding in User-Generated Content

- Source: arxiv
- arXiv ID: 2608.04847
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.04847v1
- PDF: https://arxiv.org/pdf/2608.04847v1
- DOI: https://doi.org/10.48550/arXiv.2608.04847

### Authors

Arianna Denitto, Beatrice Savoldi

### Abstract

Despite its cultural relevance and diffusion, queer slang remains underrepresented in Natural Language Processing research. Towards addressing this gap, we introduce Slang-Q, a manually curated dataset of naturally user-generated English sentences paired with queer slang terms and reference definitions, built upon a newly constructed taxonomy of 118 queer terms. We use this resource to conduct a first exploratory evaluation of language models on their ability to understand and define queer slang under varying prompting conditions. Slang-Q is intended as a basis for studying how current models handle sensitive, community-specific language and whether they can provide accurate and reliable information about such forms of identity and linguistic expression.

### 中文一句话结论
本文构建了首个聚焦于酷儿俚语的理解数据集 Slang-Q（1,024 条用户生成英文句子，覆盖 118 个术语），并初步评估了主流语言模型在不同提示条件下对这类社区特定语言的理解能力。

### English TL;DR
This paper introduces Slang-Q, a manually curated dataset of 1,024 user-generated English sentences paired with 118 queer slang terms and definitions, and uses it to conduct a first exploratory evaluation of language models' ability to understand and define queer slang under varying prompting conditions.

### 中文详细总结
酷儿俚语在自然语言处理研究中长期被忽视，但其文化意义和在线使用频率日益增长。为解决这一空白，作者手动构建了 Slang-Q 数据集：基于 Urban Dictionary 原始数据，通过自动提取（118 个酷儿术语词表）和两层人工筛选（语义相关性和有害内容过滤）得到 1,024 条自然句子，每个句子对应一个术语及其权威定义。数据集还附带一个两级分类体系（大类：身份/俚语/交叉；子类：重拾、缩写、习语、代词、拼写变体）。在此资源上，作者对多种开源和商业语言模型进行了初步探索性评估，测试它们在不同提示（如是否提供上下文、是否给出领域提示）下对酷儿俚语的解释能力。结果表明模型对这类社区语言的理解仍存在显著不足。

### 方法 / 贡献
- **数据集构建**：提出 Slang-Q，包含 1,024 条人工标注的酷儿俚语句子，术语来自多个来源（论文、社区词典、百科），并建立了两级分类体系。
- **评估框架**：设计不同提示条件（零样本、领域提示、上下文提示）来考察语言模型对酷儿俚语的理解和定义能力。
- **贡献**：首次系统性地将酷儿俚语本身作为知识对象而非偏见变量进行 NLP 评估，并公开资源以促进后续研究。

### 实验或数据
- **数据集**：Slang-Q 包含 1,024 条句子，覆盖 77 个（共 118 个）术语，平均每个术语约 13 条示例。所有句子均来自 Urban Dictionary，经过语义相关性（保留 57.57%）和有害内容剔除（剔除 10.27%）两步人工标注。
- **实验**：对多个语言模型（包括 GPT 系列、Llama 等）进行零样本和少样本提示下的定义生成任务，评估生成定义与参考定义之间的语义相似度。未涉及大规模系统实验，仅为初步探索。

### 值得关注点
- 数据集聚焦于用户生成内容中的自然用法，而非人工构造例句，更贴近真实场景。
- 分类体系明确区分了“身份标签”、“社区俚语”和“交叉用法”（如来自 AAVE 或粉丝圈），有助于细粒度分析。
- 关注了重拾术语（如 queer）和有害内容过滤，体现了对社区语言敏感性的考虑。

### 局限性
- 数据集规模较小（1,024 条），且仅覆盖 77 个术语，可能无法代表酷儿俚语的全貌。
- 来源局限于 Urban Dictionary，其内容质量参差不齐，且缺乏作者身份信息，难以完全排除外部偏见。
- 评估仅基于定义生成任务的语义相似度，未测试模型在实际应用（如对话、信息检索）中的表现。
- 人工标注由两位作者完成，其中一位为社区熟悉者，但未进行大规模标注者间一致性检验。

## Processing Notes

- Duplicate papers skipped: 0