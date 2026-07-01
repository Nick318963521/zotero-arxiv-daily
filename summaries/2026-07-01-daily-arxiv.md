# Daily arXiv - 2026-07-01

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-01T00:24:13
- Paper count: 10

## 1. Do We Still Need Fine Tuning? Turkish Sentiment Analysis in the Era of Large Language Model

- Source: arxiv
- arXiv ID: 2606.29614
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2606.29614v1
- PDF: https://arxiv.org/pdf/2606.29614v1
- DOI: https://doi.org/10.48550/arXiv.2606.29614

### Authors

Sercan Karakaş, Yusuf Şimşek

### Abstract

This study examines whether supervised fine-tuning remains necessary for Turkish sentiment analysis in the era of large language models. We compare classical machine learning methods, fine-tuned pretrained language models, and prompted large language models on a Turkish e-commerce review dataset with negative, neutral, and positive labels. Fine-tuned BERTurk models perform best overall and outperform all prompted large language models in the full three-class task. The neutral class emerges as the main difficulty: while several large language models are much more competitive in binary positive--negative classification, they degrade substantially in the three-class setting by collapsing neutral reviews into polarized categories. The findings suggest that, in realistic Turkish sentiment classification, prompted large language models do not yet match supervised fine-tuning in the zero-shot setting, and that including the neutral class is crucial for robust evaluation.

### 中文一句话结论
微调后的BERTurk模型在土耳其语三类别情感分析任务中全面优于所有零样本提示的大语言模型，中性类别是提示模型表现不佳的主要原因。

### English TL;DR
Fine-tuned BERTurk models outperform all prompted large language models in three-class Turkish sentiment analysis, especially in handling the neutral class.

### 中文详细总结
本研究比较了经典机器学习方法（逻辑回归、SVM、随机森林、朴素贝叶斯）、微调预训练语言模型（BERTurk 32k、BERTurk 128k Cased、ELECTRA）和提示大语言模型（Gemma2:9B、Gemma3:27B、GPT-OSS:20B、Llama 3.1:8B、Magibu:11B、Qwen3:32B）在土耳其语电商评论三类别情感分类（负面、中性、正面）上的表现。主要发现：微调BERTurk Cased 128k表现最佳，准确率0.837，F1分数0.834，优于最佳大语言模型Qwen3:32B（准确率0.773）约6.4个百分点。中性类别是核心难点：当移除中性样本进行二元分类时，多个大语言模型表现大幅提升（如Qwen3:32B从0.773升至0.908，Magibu:11B从0.724升至0.909），但在三类别场景中其性能显著下降，主要原因是它们倾向于将中性评论分类为极性类别。这表明提示大语言模型在粗粒度极性检测上具备竞争力，但在处理需要明确三类别边界的中性类别时仍不及监督微调模型。

### 方法 / 贡献
- 在有标注的土耳其语电商评论数据集上，系统比较了经典机器学习、微调预训练模型和零样本提示大语言模型三类方法。
- 揭示了中性类别在评估中的诊断价值：提示大语言模型在三类别任务中性能下降主要由中性类别引起，二元分类无法揭示这一弱点。
- 提出中性召回率可作为标签空间对齐的诊断指标，强调实际评估应包含中性类别。

### 实验或数据
- 数据集：土耳其语电商评论，共6,381条（预处理后6,367条），分为负面（2,416）、中性（1,439）、正面（2,526）三类，80/20划分训练/测试集（测试集1,274条）。
- 监督模型参数：BERT类模型学习率2e-5，5个epoch，批大小32；传统模型TF-IDF特征数5000。
- 大语言模型：统一提示模板，温度0.1，top_p=1。
- 评估指标：准确率、精确率、召回率、F1分数（加权）。

### 值得关注点
- 微调BERTurk模型相较于最佳提示大语言模型，错误减少约28%（从289降至208）。
- 中性类别占测试集22.6%（288/1274），却是模型性能差异的核心驱动力。
- GPT-OSS:20B有148个实例（11.6%）因产生链式思考而未返回有效标签。
- 二元分类中，Qwen3:32B（0.908）与Magibu:11B（0.909）接近甚至略超BERTurk Cased 128k（0.904），但在三类别中差距显著。

### 局限性
- 仅使用零样本提示设置，未评估少样本提示或提示工程优化对大语言模型性能的影响。
- 数据集规模中等（约6,381条），可能限制泛化性。
- 仅针对土耳其语电商评论领域，结论可能不直接适用于其他语言或领域。
- 大语言模型评估限于特定公开模型（截止2025年），未涵盖更近期或更大规模模型。
- 未分析模型对不同中性子类（如事实性描述、混合情感、弱情感）的区分能力。

## 2. A Comparative Study on Affective Cues in Text Embeddings Across Psychological Emotion Theories

- Source: arxiv
- arXiv ID: 2606.29068
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2606.29068v1
- PDF: https://arxiv.org/pdf/2606.29068v1
- DOI: https://doi.org/10.48550/arXiv.2606.29068

### Authors

Fabio Ciani, Harald Schweiger, Emilia Parada-Cabaleiro, Markus Schedl

### Abstract

Text encoders are known for their utility in natural language processing, as they are able to efficiently compress inputs into dense vectors while preserving semantics. These models have been applied to affective computing, in particular to help with solving sentiment analysis and emotion recognition tasks. Nevertheless, it remains unclear to what extent the latent representations produced by modern text encoders capture well-defined psychological theories of affect. In this work, we investigate the affective capabilities of twelve recently released text encoders by probing their generated embeddings as input features for solving regression and classification tasks across three established emotion frameworks, using both word- and sentence-level data. Additionally, we apply a semantic data-leakage prevention technique to improve robustness in word-level evaluations. Our main findings show that the latent manifolds of the latest instruction-aware open-weight encoders enclose an equal or even a larger amount of affective information in comparison with proprietary counterparts when evaluated at word level. In contrast, embeddings of task-tuned and proprietary encoders reach the highest scores on sentence-level affective classification. Furthermore, a qualitative analysis of latent representations and their encoded affective cues is provided.

### 中文一句话结论
本研究对比了12种文本编码器在三种心理情感理论框架下的情感信息捕捉能力，发现指令感知的开源模型在词语层面的情感表征可与商业模型媲美，而任务微调与商业编码器在句子层面的情感分类上表现更优。

### English TL;DR
This study compares how twelve text encoders capture affective information across three psychological emotion theories, finding that instruction-aware open-weight models perform competitively with proprietary ones at the word level, while task-tuned and proprietary encoders excel at sentence-level classification.

### 中文详细总结
本文探究了现代文本编码器（如嵌入模型）在多大程度上能够捕捉符合心理情感理论的情感线索。研究选取了12种近期发布的文本编码器，包括指令感知的开源模型、任务微调模型和商业模型。通过回归与分类任务，评估编码器在三种心理学情感框架（如情感维度或基本情绪模型）中生成的嵌入向量的情感信息含量。实验在词语和句子两个层面进行，并在词语层面采用了语义数据泄漏预防技术以提高鲁棒性。主要发现：在词语级别，指令感知的开源模型的情感信息含量不亚于甚至超过商业模型；但在句子级别，任务微调与商业编码器表现最佳。此外，文章还提供了对潜在表征的定性分析。

### 方法 / 贡献
- 方法：使用12种文本编码器生成嵌入，作为回归/分类任务的输入特征，评估其在不同心理学情感框架下的情感信息捕捉能力。
- 词语层面采用语义数据泄漏预防技术（具体方法未在摘要中详述）。
- 贡献：
  1. 首次系统对比现代文本编码器在多种心理学情感理论框架下的情感表征能力。
  2. 揭示不同类型编码器（指令感知、任务微调、商业）在词语级与句子级情感任务中的性能差异。
  3. 提供潜在表征与情感线索编码的定性分析。

### 实验或数据
- 实验类型：回归任务与分类任务。
- 数据层面：词语级与句子级数据（具体数据集未在摘要中说明）。
- 情感框架：三种已建立的心理情感理论（具体名称未在摘要中提供）。
- 编码器数量：12种近期发布的文本编码器，包括指令感知开源模型、任务微调模型及商业模型。
- 评价指标：未在摘要中明确给出，但提及了定性分析。

### 值得关注点
- 指令感知开源模型在词语级情感表征上性能与商业模型相当，凸显开源模型的竞争力。
- 词语级采用语义数据泄漏预防技术，提升了评估的鲁棒性。
- 句子级任务中，任务微调与商业编码器的优势更明显，提示不同粒度任务需选择不同编码器。
- 结合定性分析揭示编码器内在表征的情感属性。

### 局限性
- 未明确说明使用的具体情感理论框架及数据集来源，可能影响可重复性。
- 定性分析的具体方法及结论未在摘要中展开。
- 词语级泄漏预防技术的实现细节及有效性缺乏公开验证。
- 实验仅基于12种编码器与三种理论，泛化能力可能有限。
- 未讨论计算成本或模型规模对结果的影响。

## 3. Online Data Selection for Instruction Tuning via Gaussian Processes

- Source: arxiv
- arXiv ID: 2606.30077
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2606.30077v1
- PDF: https://arxiv.org/pdf/2606.30077v1
- DOI: https://doi.org/10.48550/arXiv.2606.30077

### Authors

Jun Wang, Quoc Phong Nguyen, Julien Monteil, Vu Nguyen

### Abstract

With Large Language Model (LLM) pre-training and fine-tuning shifting its focus from data volume to data quality, quality data selection has emerged as a critical research topic. Existing online data selection methods for LLM training are typically "batch-constrained", limiting optimization to local utility within random batches. To overcome this, we propose GAIA (Global Adaptive Instruction tuning via GAussian processes), a framework that formulates data valuation as a global estimation process. GAIA employs Gaussian Process regression to model continuous utility manifolds across the semantic space, utilizing an adaptive strategy fusion mechanism to dynamically prioritize high-utility samples. By casting the strategy-posterior update as an instance of the classical fixed-share Hedge framework for tracking the best expert, we inherit a dynamic-regret guarantee that characterizes GAIA's robustness under non-stationary quality scores during training. Empirical evaluations on three datasets demonstrate that GAIA significantly outperforms state-of-the-art baselines like \greats, establishing our method as a scalable and robust solution for efficient instruction tuning.

### 中文一句话结论
GAIA通过高斯过程对指令微调中的数据进行全局效用建模与自适应策略融合，显著超越了现有批约束方法，并提供了动态遗憾保证。

### English TL;DR
GAIA overcomes the batch-constrained limitation of existing online data selection for instruction tuning by using Gaussian Process regression to globally model continuous utility manifolds and adaptively prioritize high-quality samples, achieving robust performance with dynamic-regret guarantees.

### 中文详细总结
现有在线数据选择方法受限于“批约束”范式，只能在随机候选批内进行局部优化。为解决该问题，本文提出GAIA框架，将数据评估建模为全局估计过程。GAIA利用高斯过程回归在语义空间中构建连续的效用流形，并通过自适应策略融合机制动态优先选择高效用样本。通过将策略后验更新转化为经典固定份额Hedge框架以追踪最佳专家，GAIA获得了动态遗憾保证，使其在训练中效用分数非平稳时仍具鲁棒性。在三个数据集上的实验表明，GAIA显著优于GREATs等基线方法，是一种可扩展且鲁棒的指令微调数据选择方案。

### 方法 / 贡献
- 提出基于高斯过程对训练数据的潜在质量函数进行全局建模，使观测到的效用信号能推广至未见样本。
- 将高斯过程离散化为有限策略集合，采用固定份额Hedge更新策略后验，并继承动态遗憾保证，适应训练过程中质量分数的非平稳性。
- GAIA可无缝集成现有选择方法（如GREATs），通过全局偏置采样提升候选批质量，再经后续优化实现高质量与多样性。
- 提供理论上的鲁棒性保障，且不增加过多计算开销。

### 实验或数据
在三个数据集上进行经验评估，GAIA显著优于GREATs等现有最先进基线方法，验证了其可扩展性和鲁棒性。具体数据集名称在摘要中未明确列出。

### 值得关注点
- 从批约束局部优化到全局效用估计的范式转变。
- 利用高斯过程先验和离散化策略实现高效且理论有保障的在线数据选择。
- 动态遗憾保证刻画了方法在非平稳效用条件下的鲁棒性。
- 模块化设计可兼容多种评分函数和后续选择算法。

### 局限性
根据摘要，未明确讨论局限性。潜在挑战（如高斯过程在大规模数据上的计算成本、温启动阶段开销）需参考原文详细分析。

## 4. The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning

- Source: arxiv
- arXiv ID: 2606.28843
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2606.28843v1
- PDF: https://arxiv.org/pdf/2606.28843v1
- DOI: https://doi.org/10.48550/arXiv.2606.28843

### Authors

Will Hawkins, Kaivalya Rawal, Jonathan Rystrøm, Stratis Tsirtsis, Zihao Fu, Greta Warren, Ryan Brown, Eoin Delaney, Sandra Wachter, Brent Mittelstadt, Chris Russell

### Abstract

Fine-tuning a large language model is a ubiquitous method for enhancing its capability on a specific downstream task. However, prior work has shown that this increase in capability comes with a cost: it can increase a model's tendency to respond to unsafe adversarial prompts, even when fine-tuning with non-adversarial data. We present the first comprehensive empirical study of this phenomenon in multilingual settings by fine-tuning Llama-3.2, Qwen3, and Gemma-3 models using benign data translated across nine languages. We find that safety outcomes are highly sensitive to both the choice of fine-tuning language and the evaluation language, with adversarial compliance rates increasing four-fold in some settings. Multilingual safety drift is decoupled from general capability metrics, and occurs heterogeneously across languages and models. Fine-tuning in non-English languages often induces smaller internal representational drifts than English, but these shifts lead models to default to either exaggerated compliance or refusal. As such, assessing fine-tuning impacts solely in English provides inadequate assurance for deployment. To facilitate further research into these cross-lingual safety blind spots, we release the Multilingual-Benign-Tune dataset and the SORRY-Bench-Multilingual evaluation suite.

### 中文一句话结论
良性的多语言微调会异质性地损害大语言模型的安全性，且这种危害与模型能力变化解耦，不能通过仅英语评估来充分检测。

### English TL;DR
Benign multilingual fine-tuning of LLMs causes heterogeneous and unpredictable safety degradation that is decoupled from capability metrics, is highly sensitive to the fine-tuning and evaluation languages, and cannot be adequately assessed through English-only evaluations.

### 中文详细总结
本文首次全面实证研究了良性多语言微调对大型语言模型安全性的影响。通过对 Llama-3.2、Qwen3 和 Gemma-3 三种模型家族的小型变体（0.6B-4B 参数），使用九种语言（英语、中文、丹麦语、希腊语、印地语、爱尔兰语、葡萄牙语、西班牙语、他加禄语）的良性数据进行低秩适配（LoRA）微调，发现安全结果高度依赖于微调语言和评估语言的选择。某些设置下，模型对对抗性提示的遵从率增加高达四倍。多语言安全漂移与通用能力指标解耦，且在不同语言和模型间表现异质。非英语微调通常导致比英语更小的内部表示漂移，但这些漂移会使模型走向过度遵从或过度拒绝。因此，仅评估英语微调影响不足以保障部署安全。研究还发布了多语言良性微调数据集和 SORRY-Bench 多语言评估套件。

### 方法 / 贡献
- **方法**：使用 Gemini 2.5 Flash 基于 Dolly 种子数据生成 1000 条英语良性问答对，并翻译为八种语言。采用 LoRA 微调（α/r=8，学习率 5×10⁻⁵），每个模型用三种随机种子微调一至三个 epoch。评估使用 SORRY-Bench（440 个英语对抗性提示）及其多语言版本，借助 NLLB-200 翻译回英语后由自动评分器判断遵从性。同时进行 TinyMMLU、TinyAlpacaEval、困惑度及内部向量漂移分析。
- **贡献**：首次系统揭示良性多语言微调的安全异质性；证明安全危害与能力变化解耦；发现不同架构的机制差异（Llama 更易过度遵从，Gemma/Qwen3 更易过度拒绝）；发布数据集和评估套件以促进后续研究。

### 实验或数据
- **实验规模**：共微调 357 个模型（6 个基础模型 × 9 种语言 × 3 种子 × 2 种 epoch 设置 + 基础模型 + 超参数消融），进行超过 2000 次评估。
- **数据**：
  - 微调数据：基于 Dolly 种子数据由 Gemini 2.5 Flash 合成的 1000 条良性英语问答，并人工校验确保无安全敏感内容。
  - 评估数据：SORRY-Bench（英语 440 条对抗性提示）及通过 Google Translate 翻译并由母语者校验的八种语言版本。
- **关键发现**：良性微调后，安全遵从率变化幅度因语言和架构而异；非英语微调常导致相比英语更小的内部表示漂移，但引发遵从/拒绝极端化。

### 值得关注点
- **安全危害与能力解耦**：模型能力指标（如 TinyMMLU 得分）变化不大时，安全遵从率可显著上升，表明安全评估不能依赖能力测试。
- **语言选择的关键影响**：同一模型在英语中微调可能安全性变化不大，但在葡萄牙语中微调导致对抗性遵从率大幅增加。
- **仅英语评估的不足**：英语微调安全评估无法推广到多语言场景，部署前必须进行目标语言的安全测试。
- **机制差异**：不同模型家族对内部表示漂移的反应不同（Llama 更易屈服，Gemma/Qwen3 更易拒绝），揭示架构相关的安全脆弱性。

### 局限性
- 研究限于 0.6B-4B 参数的小型模型，结论可能不直接推广到更大规模模型。
- 微调数据由 GPT 类模型合成，尽管经人工检查，仍可能引入未识别的偏差。
- 仅涵盖九种语言，且语言选择偏向常见语种；低资源语言或不同语系的表现未知。
- 评估依赖自动评分器（Mistral-7B）对翻译后输出的二分类，可能遗漏语义细微差别。
- 超参数（如学习率、LoRA 秩）固定，更多配置下的安全性变化有待探索。

## 5. DataComp-VLM: Improved Open Datasets for Vision-Language Models

- Source: arxiv
- arXiv ID: 2606.28551
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2606.28551v1
- PDF: https://arxiv.org/pdf/2606.28551v1
- DOI: https://doi.org/10.48550/arXiv.2606.28551

### Authors

Matteo Farina, Vishaal Udandarao, Thao Nguyen, Selim Kuzucu, Maximilian Böther, Andreas Hochlehnert, Adhiraj Ghosh, Marianna Nezhurina, Karsten Roth, Joschka Struber, Yuhui Zhang, Sebastian Dziadzio, Elaine Sui, Soumya Jahagirdar, Dhruba Ghosh, Hasan Hammoud, Thomas De Min, Simone Caldarella, Jehanzeb Mirza, Sedrick Keh, Mehdi Cherti, Hilde Kuehne, Bernt Schiele, Serena Yeung-Levy, Muhammad Ferjad Naeem, Federico Tombari, Ana Klimovic, Elisa Ricci, Matthias Bethge, Sewoong Oh, Ameya Prabhu, Alessio Tonioni, Jenia Jitsev, Massimiliano Mancini, Ludwig Schmidt, Nikhil Parthasarathy

### Abstract

Building performant Vision-Language Models (VLMs) requires carefully curating large-scale training datasets, yet the community lacks systematic benchmarks for evaluating such curation strategies. We introduce DataComp for VLMs (DCVLM), a benchmark for controlled data-centric experiments to improve VLM training. As part of DCVLM, we collect 160 datasets spanning four data types -- image-caption pairs, multimodal interleaved documents, text-only, and instruction-tuning data -- into a corpus of 6T multimodal tokens. DCVLM allows participants to test curation strategies (filtering, mixing, formatting, sampling) across 1B-8B models and 6.25B-200B token budgets. Models are then evaluated on a carefully selected suite of up to 52 downstream benchmarks across 9 domains. We conduct extensive experiments on DCVLM and find that data mixing, not filtering, is key to a high-quality training dataset: instruction-heavy mixtures scale better than caption-heavy ones, with gains widening at larger scales. The resulting dataset, DCVLM-Baseline, enables training an 8B VLM to 63.6% accuracy on our 33-task core suite with 200B training tokens. Compared to FineVision, the state-of-the-art open VLM training dataset, this represents an improvement of +5.4pp. DCVLM and all accompanying artifacts will be made publicly available at https://www.datacomp.ai/dcvlm/.

### 中文一句话结论
DCVLM基准和基线数据集表明，数据混合（特别是指令密集型混合）而非过滤是提升视觉语言模型训练质量的关键，在8B模型上用200B训练令牌达到63.6%核心任务准确率，比FineVision高5.4个百分点。

### English TL;DR
DataComp-VLM introduces a benchmark for controlled data-centric VLM experiments and demonstrates that data mixing, especially instruction-heavy mixtures, outperforms caption-heavy ones at larger scales, achieving state-of-the-art results.

### 中文详细总结
该工作提出了DCVLM（DataComp for VLMs），一个用于系统性评估和改进视觉语言模型训练数据策展策略的基准。研究者收集了160个数据集，涵盖四种数据类型（图像-文本对、多模态交错文档、纯文本、指令微调数据），组成6万亿多模态令牌的语料库。通过1B-8B模型和6.25B-200B令牌预算的实验，发现数据混合比过滤更重要：指令密集型混合随规模扩大表现更好。最终数据集DCVLM-Baseline在8B模型、200B令牌训练下，在33项核心任务中达到63.6%准确率，比现有最优开放数据集FineVision提升5.4个百分点。

### 方法 / 贡献
- 提出DCVLM基准，支持对四种数据类型的策展策略（过滤、混合、格式化、采样）进行受控实验
- 创建包含160个数据集、6T多模态令牌的开放语料库
- 开发52项下游评测基准（涵盖9个领域）
- 发现关键结论：数据混合（尤其指令密集型混合）优于过滤，指令数据在更大规模下增益更显著

### 实验或数据
实验在1B、2B、4B、8B模型上进行，训练令牌预算从6.25B到200B。主要对比FineVision数据集，在33项核心任务套件上评估。具体实验包括：数据混合比例搜索、过滤方案消融（39种配置）、采样策略比较（样本级vs.分片级）、温度采样、OCR上采样、重标注等。

### 值得关注点
- 指令密集型混合在更大模型和更多令牌下优势更明显（在4B×100B下超FineVision 13.2个百分点）
- 文本质量过滤的增益在优化混合和大模型下消失（“洗掉”现象）
- 样本级采样比分片级采样带来稳定1-2%提升
- 重标注（合成字幕）在预训练阶段未显著优于原始alt-text

### 局限性
- 主要关注英语，其他语言覆盖有限（91.1%为英语）
- OCR任务仍有差距，需额外上采样策略弥补
- 实验限于最多8B模型和200B令牌，更大规模效果未知
- 未探索多模态交错文档的最佳混合比例（仅在10c-70i混合中固定）
- 过滤策略仅在纯文本池有效，应用于其他数据类型可能无效或有损

## 6. Mechanistic Personality Analysis of LLMs Steering Personality via Latent Feature Interventions

- Source: arxiv
- arXiv ID: 2606.28770
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2606.28770v1
- PDF: https://arxiv.org/pdf/2606.28770v1
- DOI: https://doi.org/10.48550/arXiv.2606.28770

### Authors

David Courtis, Ting Hu

### Abstract

Large Language Models (LLMs) have demonstrated the ability to simulate human-like OCEAN personality traits in generated text. Previous efforts have focused on prompt engineering or fine-tuning to shape LLM personality. In this work, we propose a mechanistic interpretability approach that directly intervenes on the model's latent features. Our method identifies latent directions in the residual stream corresponding to a target OCEAN trait using sparse autoencoders (SAEs) and contrastive activation analysis. We formalize an additive steering vector in activation space and demonstrate how applying a small additive shift to the hidden states enhances the target trait while preserving overall language modeling performance. To determine the optimal combination of feature shifts, we explore a linear weighting heuristic with grid search optimization that balances personality expression with task performance. Our approach shows promise in controllably steering personality traits at the mechanistic level while maintaining high performance on standard benchmarks.

### 中文一句话结论  
本文提出一种基于稀疏自编码器和对比激活分析的机械可解释性方法，通过直接干预大语言模型的潜在特征实现可控的人格特质调控。

### English TL;DR  
This paper introduces a mechanistic interpretability method using sparse autoencoders and contrastive activation analysis to directly steer LLM personality traits via targeted latent feature interventions.

### 中文详细总结  
大语言模型能够模拟人类OCEAN人格特质，但现有方法（提示工程、微调）存在不一致、资源消耗大、影响核心任务表现等问题。本研究提出一种机械可解释性方法：使用稀疏自编码器（SAE）分解残差流激活，通过对比正负样本的激活差异识别与目标特质对应的潜在方向，构造加法导向向量施加于隐藏状态，从而增强目标特质同时保持语言建模性能。为优化特征组合，采用线性加权启发式与网格搜索平衡人格表达与任务表现。实验基于DeepSeek-R1-Distill-Llama-8B模型，生成12,000条状态更新，并利用嵌入相似度、LLM分类及人工评估进行多维度评价。

### 方法 / 贡献  
1. **特征提取**：通过正负提示集的对比激活分析，结合SAE分解，分别识别增强和抑制目标特质的潜在特征。  
2. **导向向量构造**：对排名靠前的正负特征向量进行归一化，通过双向线性加权与网格搜索确定最优加法偏移。  
3. **评估框架**：采用嵌入余弦相似度、LLM分类和人工评估三重方法验证人格改变效果。  

### 实验或数据  
- **模型**：DeepSeek-R1-Distill-Llama-8B。  
- **数据生成**：基于PsyBORGS框架生成12,000条Facebook风格状态更新，每项特质分为高/低表达组（评分1-3与7-9）。  
- **SAE**：使用预训练的qresearch/DeepSeek-R1-Distill-Llama-8B-SAE-l19（第19层）。  
- **评估**：未报告具体基准数据集，但提及通过标准基准保持语言性能。

### 值得关注点  
- 首次在机械可解释层面直接操控LLM人格特质，而非依赖提示或微调。  
- 双向特征选择（正/负特征）提供更精细的控制。  
- 网格搜索优化特征权重，能同时平衡特质表达与语言能力。  

### 局限性  
论文未明确讨论局限性，但根据内容可推断：  
- 方法仅在单一模型（DeepSeek-R1-Distill-Llama-8B）和特定SAE上验证，泛化性未知。  
- 未报告失败案例或不同特质间的交互效应。  
- 大规模评估及与现有方法的系统比较尚缺。

## 7. A Hybrid Framework for Song Lyric Annotation Based on Human-LLM Alignment

- Source: arxiv
- arXiv ID: 2606.29273
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2606.29273v1
- PDF: https://arxiv.org/pdf/2606.29273v1
- DOI: https://doi.org/10.48550/arXiv.2606.29273

### Authors

Rashini Liyanarachchi, Frank Tran, Md Mahmudul Hasan, Aditya Joshi, Erik Meijering

### Abstract

Emotion recognition of song lyrics is a challenging task since lyrics may not necessarily align with the overall emotion of a song. As a result, lyrics annotation remains largely underexplored. Drawing inspiration from research in large language model (LLM) assisted annotation, we examine the alignment between humans and LLMs for annotation of lyrics by creating a new sentence-level dataset of lyrics. Our observations highlight the subjectivity of the task and the inherent challenges. Following this, we present a hybrid annotation framework that optimizes human and LLM annotation by predicting potential misalignment in annotation.

### 中文一句话结论
本文提出一种混合标注框架，通过预测人类与LLM标注之间的对齐程度，动态选择最优标注来源，从而优化歌词情感标注的准确性与效率。

### English TL;DR
This paper presents a hybrid framework for song lyric emotion annotation that optimizes human and large language model (LLM) annotation by predicting potential misalignment, addressing the subjectivity and challenges of the task.

### 中文详细总结
本文针对歌词情感标注这一任务，因歌词与歌曲整体情感可能不一致且标注主观性强，提出一种混合框架以结合人类标注与大型语言模型（LLM）的互补优势。作者首先构建了一个新的句子级歌词情感数据集，选取自DEAM和PMEmo两个公开数据集，共50首歌曲（652个句子级片段），并由三位博士生（东/南亚背景、英语熟练）在价-效价（Valence-Arousal）空间进行独立标注。同时使用GPT-4、Gemini 1.5和LLaMA 3三种主流LLM进行标注。通过分析人类与LLM标注的对齐程度，发现该任务具有高度主观性，存在明显的不对齐情况。基于此，他们提出混合标注框架，包括两种策略：加权聚合（根据对齐度分配权重）和注释源预测（预测某句何时应优先采用人类或LLM标注）。该框架旨在减少人工成本、提高标注一致性和客观性，并公开了相关代码。

### 方法 / 贡献
- **数据集构建**：从DEAM和PMEmo数据集筛选50首歌曲，通过API获取歌词并人工校验、分割为句子级单元，最终获得652个标注片段；所有片段在VA连续空间由三名人类标注者和三个LLM分别标注。
- **人类与LLM对齐分析**：系统比较人类和LLM在歌词情感标注上的一致性，揭示主观性和文化/语境差异带来的挑战。
- **混合标注框架**：提出两种方法——加权聚合（基于对齐度融合人类与LLM标注）和标注源预测（训练分类器预测某片段更适合人工还是LLM标注），动态决定最优标注来源。
- **可复现性**：公开框架代码（GitHub链接）。

### 实验或数据
- **数据集**：50首歌曲，652个句子级歌词片段，来自DEAM（音频+元数据）和PMEmo（含歌词的标注）；歌词经手动校验和语义分割。
- **人类标注**：3名博士研究生（东/南亚文化背景，高英语水平），使用定制HTML工具在VA空间（-1到1）标注。
- **LLM标注**：三个模型——GPT-4、Gemini 1.5、LLaMA 3，使用精心设计的提示模板进行标注。
- **分析指标**：主要分析人类内部和人类-LLM间的标注对齐程度，包括一致性与差异分布。论文并未报告具体的量化实验结果（如F1分数等），但说明了标注过程中的主观性观察。

### 值得关注点
- **句子级粒度**：首次在歌词情感标注中采用句子级而非歌曲级分析，更能捕捉情感随时间变化的动态。
- **混合框架创新**：不是简单组合人类和LLM，而是主动预测何时使用哪种标注源，提高效率且不牺牲质量。
- **主观性问题正视**：明确将标注主观性视为核心挑战，而不是忽略它。
- **开源与可复现**：提供框架代码（GitHub），便利后续研究。

### 局限性
- **样本量有限**：仅50首歌曲（652个句子），覆盖的歌曲风格和情感表达可能不够全面。
- **人类标注者单一性**：三位标注者均来自相近文化背景（东/南亚），可能缺乏跨文化的泛化性；且标注者数量较少，未能充分捕捉人类标注者的多样性。
- **LLM选择与版本**：仅使用三种LLM，且未探讨不同版本或参数设置的影响；LLM输出可能受提示设计影响较大。
- **框架评估缺失**：论文主要呈现对齐分析及框架设计，未提供混合框架在真实标注任务上的定量结果（如与纯人工或纯LLM标注的成本/质量对比）。
- **未涉及音频模态**：框架仅聚焦歌词文本，未考虑歌曲音频对情感标注的潜在影响。

## 8. Little Brains, Big Feats: Exploring Compact Language Models

- Source: arxiv
- arXiv ID: 2606.30062
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2606.30062v1
- PDF: https://arxiv.org/pdf/2606.30062v1
- DOI: https://doi.org/10.48550/arXiv.2606.30062

### Authors

Dari Baturova, Elena Bruches, Ivan Chernov, Roman Derunets, Arsenii Fomin, Andrey Kostin

### Abstract

While large language models have been dominating the research landscape recently, small language models remain highly relevant across various domains; yet, they receive far less attention. In this study, we investigate how smaller language models perform during the generation stage within a Retrieval-Augmented Generation (RAG) system. To benchmark these models effectively, we utilised both open-source and proprietary datasets covering diverse subject areas and question types. Our findings demonstrate that a RAG system with small language models can be executed directly on-device without requiring any GPU hardware within a reasonable time. The experimental code and links to the supplementary materials can be accessed through the GitHub repository: https://github.com/SibNN/SLM-RAG-EVAL.

### 中文一句话结论
本研究证明，小型语言模型在检索增强生成系统中能够有效运行，无需GPU，可在本地设备上合理时间内完成生成任务。

### English TL;DR
Small language models can effectively perform generation in a Retrieval-Augmented Generation (RAG) system on local devices without GPU, as demonstrated by benchmarking on diverse Russian-language datasets.

### 中文详细总结
这项研究探讨了小型语言模型在检索增强生成（RAG）系统中的生成阶段表现。作者利用开源和专有数据集构建了包含500个样本的俄语基准测试，涵盖多种问题类型。实验结果表明，小型语言模型驱动的RAG系统可以在没有GPU的情况下直接在本机设备上运行，时间合理。代码和补充材料可在GitHub上获取。

### 方法 / 贡献
- 构建了一个包含开源和专有数据集的俄语基准测试，用于评估RAG系统中的小型语言模型。
- 系统评估了小型语言模型在RAG框架中的生成能力。
- 提供了性能特征、评估方法和实际部署注意事项的详细分析。

### 实验或数据
使用了五个数据集：DaNetQA、SberQuAD、RuRAG Test Dataset、Grounded-RAG-QA-RU和一个专有数据集。每个数据集采样100个样本，共500个样本。问题类型包括事实型、推理型、基于证据型、比较型、经验型和指令型。

### 值得关注点
- 小型语言模型在无需GPU的情况下即可本地运行，降低了硬件门槛。
- 涵盖了多种俄语问题类型和领域，包括专有数据集。
- 实验代码公开，可复现。

### 局限性
摘要未明确讨论本研究的局限性。但研究仅针对俄语数据集和特定的小型模型，其结论在跨语言、跨模型或更复杂任务上的泛化性有待进一步验证。

## 9. Beyond the Mean: Three-Axis Fidelity for Aligning LLM-Based Survey Simulators from Small Pilot Data

- Source: arxiv
- arXiv ID: 2606.28963
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2606.28963v1
- PDF: https://arxiv.org/pdf/2606.28963v1
- DOI: https://doi.org/10.48550/arXiv.2606.28963

### Authors

Eun Cheol Choi, Youngrae Kim, Prabhu Pugalenthi, Hong-En Chen, Bo-Ruei Huang

### Abstract

Large language models (LLMs) are increasingly used to simulate social survey responses, yet their outputs exhibit systematic biases: marginal distributions are skewed, response variance is poorly calibrated, and predictor-outcome relationships are attenuated. We ask a simple question: given a small pilot sample of human responses, can an LLM recover the statistical characteristics of a broader population? We decompose recovery along three axes: structural fidelity, marginal fidelity, and individual fidelity. Using a COVID-19 misinformation survey as a case study, we benchmark three families of approaches: prompting, rectification, and fine-tuning. The findings suggest that fine-tuning on small pilot samples offers a balanced approach for achieving multiple forms of fidelity, but the levels of such fidelity can vary across subsamples, potentially threatening pluralistic alignment.

### 中文一句话结论
在仅有少量人类试点数据时，对LLM进行微调（尤其是LoRA+MLP）能相对均衡地恢复调查模拟的结构、边际和个体忠实度，但不同子样本间的忠实度存在差异，可能威胁多元对齐。

### English TL;DR
Fine-tuning LLMs on small pilot samples enables balanced recovery of structural, marginal, and individual fidelity for survey simulation, but fidelity levels vary across subsamples, challenging pluralistic alignment.

### 中文详细总结
该研究探讨了如何利用少量人类试点样本（小pilot数据）让大型语言模型（LLM）生成能反映更广泛人群统计特征的合成调查响应。作者提出**三轴忠实度**框架来评估恢复效果：**结构忠实度**（预测因子与结果的关系是否一致）、**边际忠实度**（模拟数据的边际分布是否匹配）、**个体忠实度**（每个模拟受访者是否与真实个体对应）。以COVID-19错误信息调查（N=1466，36项Likert量表题）为例，比较了四类方法：零样本提示（ZS）、少样本提示（FS）、参数高效微调（LoRA及LoRA+MLP）和预测驱动推断（PPI）修正。结果显示，**LoRA+MLP**在结构忠实度（双变量CCC=0.85，OLS β CCC=0.78）和个体忠实度（rd=0.37, MAEd=0.61）上表现最佳，边际忠实度（EMD-d=0.17）也最优。零样本逐项提示（ZS-perItem）是纯提示方法中最强的。但所有方法的忠实度在不同子样本间波动，多元对齐面临挑战。

### 方法 / 贡献
1. **重新定义任务**：将LLM调查模拟视为“可恢复性”任务——从小pilot数据中恢复全人群的统计特性。  
2. **三轴评估框架**：分别用Lin’s CCC（结构）、Earth Mover’s Distance（边际）、Pearson r与MAE（个体）量化三方面忠实度。  
3. **系统基准测试**：在同一个5%试点样本（73人）上比较提示、修正、微调三类方法的四类变体（ZS, FS, LoRA, LoRA+MLP）。  
4. **核心贡献**：提出LoRA+MLP组合能显著提升多轴忠实度，并揭示了子样本异质性对多元对齐的威胁。

### 实验或数据
- **数据来源**：2020年5月韩国COVID-19错误信息调查（Lee et al., 2023），样本量1466人，每人回答36个Likert信念题（18错误信息+18真实信息，各半政治/科学）。  
- **试点划分**：随机抽取5%（73人）作为pilot，其余95%（1393人）作为保留测试集。  
- **实验方法**：  
  - ZS（零样本批量/逐项）、FS（少样本5行示例）、LoRA（微调Qwen3-8B）、LoRA+MLP（加分类头）、PPI（修正提示方法）。  
- **评估指标**：结构用CCC（12个预测因子的双变量相关系数和标准化OLS系数）、边际用跨受访者EMD（d, m, t三个汇总指标）、个体用跨受访者配对Pearson r和MAE。  
- **结果摘要**：LoRA+MLP在结构、边际、个体三轴均最优（如结构CCC>0.78, EMD-d=0.17）。ZS-perItem（零样本逐项）是纯提示中的最佳者（结构CCC≈0.80）。PPI仅适用于总体均值修正，在本文场景中因微调方法已过拟合pilot而失效。

### 值得关注点
1. **三轴分解**：不同于仅关注均值或边际，本文同时评估预测—结果关系和多变量结构，暴露了单纯提示或修正方法的不足。  
2. **LoRA+MLP表现突出**：在仅用5%pilot数据的情况下，结构CCC远高于其他方法，且边际EMD最低，展示出小数据微调的潜力。  
3. **异质性警告**：即使最佳方法，不同子样本间的忠实度仍有波动，这直接挑战了“LLM可普适替代人类受访者”的假设。  
4. **纯提示策略的局限**：零样本批量提示（ZS）效果最差，而逐项提示（ZS-perItem）显著改善，提示跨项目依赖性建模的重要性。

### 局限性
1. **领域和样本量限制**：仅基于韩国COVID-19错误信息调查（单一年份、单一国家），结论的泛化性有待验证。  
2. **子样本异质性**：不同人口或心理子群体上的忠实度不一致，可能无法实现“多元对齐”——即模拟器不能公平代表所有群体。  
3. **PPI适用性不足**：在微调方法中因pilot数据被记忆，PPI修正项退化；仅对纯提示方法有效，且只能修正均值，无法恢复个体或结构特性。  
4. **评估框架的轴间权衡**：未深入探讨三轴之间的内在冲突（如优化个体忠实度可能损害边际忠实度），未来需进一步研究最佳平衡点。

## 10. Developmental Trajectories of Situation Modeling and Mentalizing in Transformer Language Models

- Source: arxiv
- arXiv ID: 2606.28524
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2606.28524v1
- PDF: https://arxiv.org/pdf/2606.28524v1
- DOI: https://doi.org/10.48550/arXiv.2606.28524

### Authors

Pamela D. Rivière, Cameron Jones, Sean Trott

### Abstract

Recent work suggests that Large Language Models (LLMs) are sensitive to the belief states of agents described by text, as measured by the false belief task (FBT), yet persistent concerns of construct validity remain. We adopt a **developmental perspective**, tracing the pattern of mental state reasoning behavior -- and likely **preconditions** for this behavior -- across multiple training stages in the Olmo2 and Pythia language model suites. We find that above-chance FBT performance depends both on model size and sufficient training volume, emerges relatively late in pretraining, and is most improved by post-training interventions (SFT, DPO) in the condition most diagnostic of mentalizing (False Belief, Implicit). However, FBT performance is fragile: consistent with past work, the use of non-factive verbs (e.g., thinks) increases false belief attributions even in the True Belief condition. To contextualize these findings, we track the emergence of **situation modeling**: the ability to report on basic factual properties of a described scene. Situation modeling accuracy generally precedes and exceeds FBT accuracy, yet situational representations also prove surprisingly incoherent in certain respects: when asked about the knowledge states of the Antagonist agent -- who always knows the item's true location -- Olmo2 13b is consistently influenced both by the Target agent's knowledge state and the presence of non-factive verbs. Together, these results suggest that larger, sufficiently trained models build partially coherent situation models in a developmentally appropriate sequence, yet display surprising fragility -- highlighting the value of developmental and stress-testing approaches for evaluating LLM capabilities.

### 中文一句话结论
本研究通过对Olmo2和Pythia系列模型的发育轨迹分析发现，大语言模型的错误信念任务（FBT）表现较晚出现，依赖于模型规模与训练数据量，且性能脆弱；情境建模能力通常先于并超越FBT表现，但自身也存在惊人的不一致性。

### English TL;DR
A developmental analysis of transformer language models reveals that false belief task performance emerges late in pretraining, depends on model size and training volume, remains fragile, and is preceded by situation modeling, which itself shows surprising incoherence.

### 中文详细总结
本文采用发育视角，跟踪Olmo2和Pythia语言模型系列在多个训练阶段的心理状态推理行为及其可能的先决条件。研究发现，FBT表现依赖于模型大小和足够的训练量，在预训练后期出现，并在最需要心智化的条件（隐式错误信念）下通过后训练干预（SFT、DPO）获得最大提升。然而，FBT表现脆弱：非实义动词（如“认为”）的使用即使在真信念条件下也会增加错误信念归因。情境建模能力（报告场景基本事实）通常先于并优于FBT，但同样存在不一致性：当询问始终知道物品真实位置的对手代理时，模型被目标代理的知识状态和非实义动词持续影响。结果表明，较大且充分训练的模型能以发育适当顺序构建部分连贯的情境模型，但显示出意外脆弱性。

### 方法 / 贡献
方法：使用Trott等人（2023）的FBT刺激集，并创建情境建模变体（报告基本事实、对手知识状态）。对Olmo2和Pythia系列模型的预训练检查点及后训练阶段（SFT、DPO）进行概率评估，追踪表现轨迹。贡献：a) 提供心智化能力的发育视角，揭示FBT表现出现晚、依赖规模与数据量的特征；b) 引入情境建模作为先决条件进行对比，突出其先于FBT但自身不一致；c) 通过应力测试（非实义动词、多代理问题）揭示FBT脆弱性。

### 实验或数据
实验基于公开FBT刺激集（192个段落，12个模板，操纵知识状态、知识提示、位置顺序）和修改后的情境建模刺激（查询物品位置、移动代理等）。追踪了Olmo2（多个预训练检查点及后训练阶段）与Pythia系列（参数匹配、训练数据量更少）的表现。未提及额外独立数据集。

### 值得关注点
- FBT表现在预训练后期才超越随机水平，且需足够模型大小与训练量。
- 后训练（SFT、DPO）显著提升隐式错误信念条件下的表现，但真信念条件受影响较小。
- 非实义动词导致错误信念泄漏：即使在真信念条件下，模型也倾向于错误归因。
- 情境建模能力先于FBT出现且准确率更高，但对手代理的知识状态推理受目标代理影响，说明情境模型的不完整性。

### 局限性
- 仅使用Olmo2和Pythia系列，可能无法推广至其他架构或训练策略的模型。
- FBT测试本身存在构念效度争议，本文虽提供发育证据，但未彻底解决是否真正反映心智化能力。
- 情境建模的不一致性表明模型可能依赖表面线索而非连贯表征，但机制尚不明确。
- 实验局限于英文文本概率任务，未探索多语言或生成任务中的表现。

## Processing Notes

- Duplicate papers skipped: 0