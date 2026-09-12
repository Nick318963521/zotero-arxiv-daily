# Daily arXiv - 2026-09-12

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-12T00:17:43
- Paper count: 10

## 1. Structural priors for data-efficient language learning

- Source: arxiv
- arXiv ID: 2609.11505
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.11505v1
- PDF: https://arxiv.org/pdf/2609.11505v1
- DOI: https://doi.org/10.48550/arXiv.2609.11505

### Authors

Yana Veitsman, Jonas Mayer Martins, Jonathan Lautenschlager, Lisa Beinborn

### Abstract

Efficient language learning requires methods to reduce the reliance on large data and computational resources. We investigate structural transfer: First training models on non-language data to induce useful priors for natural language. This approach is a form of weight initialization for multilingual language modeling. We evaluate transfer via next-token-prediction loss, weight shifts in the model, and downstream linguistic benchmarks. Several symbolic data types - notably music, probabilistic grammars, and cellular automata - yield lower language-modeling loss than random initialization. These gains coincide with smaller weight shifts during subsequent language training, suggesting that structural transfer positions models in a more favorable region of the parameter space. However, a lower loss does not translate consistently into better downstream linguistic performance, and transfer from non-language data is less efficient than additional language data. We conclude that non-language data can serve as a partial substitute for language data for the training objective of next-token prediction but does not reliably support broader linguistic generalization.

### 中文一句话结论
在后续多语言语言建模中，非语言结构数据（如音乐和语法）的预训练可以降低下一词预测损失，但这种提升并未稳定转化为更好的下游语言能力，且效率低于额外语言数据。

### English TL;DR
Pre-training language models on structured non-language data like music, grammars, or cellular automata can improve next-token prediction efficiency during subsequent multilingual language learning, though this benefit does not consistently translate to better downstream linguistic performance compared to using additional language data.

### 中文详细总结
本研究探索了结构转移方法：先对非语言数据进行训练，为自然语言学习引入有用先验。使用GPT-2风格模型，在多语言BabyLM语料库（英语、荷兰语、中文）上评估。实验表明，音乐、概率语法和元胞自动机等符号数据类型的预训练使得后续语言建模的交叉熵损失低于随机初始化，且伴随着更小的权重偏移，表明模型被置于更有利的参数空间。但是，更低的损失并未一致地在语法理解、句子可接受性等下游语言基准上带来优势。此外，从非语言数据转移的效率低于直接使用额外语言数据。作者因此得出结论：对于下一词预测训练目标，非语言数据可部分替代语言数据，但无法可靠支持更广泛的语言泛化。

### 方法 / 贡献
- 提出“结构转移”概念：通过先在非语言数据上训练（pre-pretraining）来初始化权重，从而引导多语言语言模型学习。
- 在GPT-2架构下，评估四种非语言数据类型（概率上下文无关文法、元胞自动机、钢琴音乐、蛋白质序列）在三语（英、荷、中）BabyLM语料上的迁移效果。
- 引入损失比率（loss ratio）和权重偏移（weight shift）两类指标来量化转移收益。
- 贡献了系统性对比：发现低损失与下游性能之间的不一致，揭示了结构转移的局限性。

### 实验或数据
- **实验阶段**：两阶段训练。阶段I：在四种非语言数据上训练；阶段II：在多语言BabyLM数据上继续训练。
- **结构数据**：
  - 合成语法（PCFG）：基于宾州树库规则生成，分为Zipf分布和均匀分布两种。
  - 元胞自动机（CA）：使用16状态和256状态两档复杂度，通过约1820条规则生成。
  - 音乐：Aria-MIDI钢琴数据集，编码为整数序列。
  - 蛋白质序列：Swiss-Prot中的标准化氨基酸序列。
  - 基线：随机整数序列和Wikipedia英语文本。
- **语言数据**：多语BabyLM语料，包含英语、荷兰语、中文，以1:1:1比例采样。
- **评估**：下一词预测验证损失、权重偏移、BabyLM框架下的零样本与微调下游任务（具体任务未在摘要中详细列明，但提及）。

### 值得关注点
- 音乐、概率语法和元胞自动机这三种符号数据都能显著降低语言建模损失，且与权重偏移减小相关。
- 合成语法（PCFG）在两种词汇分布下表现不同，表明数据分布性质可能影响转移效果。
- 蛋白质序列和随机序列未带来类似收益，说明结构类型的关键性。
- “损失改善不意味下游性能改善”的结果对当前预训练范式具有重要反思意义。

### 局限性
- 更低的下一词预测损失并未一致转化为更好的下游语言性能（如语法判断、推理等）。
- 结构转移的效率低于直接使用额外语言数据，因此只能作为部分替代。
- 实验仅限于GPT-2小模型和三种语言，结论向大模型或更多语言的泛化性尚未验证。
- 权重偏移的分析仍为初步相关性，因果关系尚待进一步证明。

## 2. Data-Efficient Language Modeling: From Frontier Advancement to Principle-Guided Model Improvement

- Source: arxiv
- arXiv ID: 2609.10702
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.10702v1
- PDF: https://arxiv.org/pdf/2609.10702v1
- DOI: https://doi.org/10.48550/arXiv.2609.10702

### Authors

Shuxing Yang, Kaihao Zhu, Junjie Yang, Rui Zhao, Junyao Wu, Yize Wang, Wenhao Li, Fujia Chen, Taowen Deng, Shenzhan Hong, Yaqi Li, Zichen Li, Jincheng Mi, Yuang Pan, Hongsheng Chen, Yihao Yang

### Abstract

Learning from limited text requires models to use context, generalize to new inputs, and retain useful capabilities. Qiushi Engine conducted a long-horizon, end-to-end autonomous research program on BabyLM 2026 Strict-Small, within 10 million corpus words and 100 million cumulative word presentations. Three stages connected frontier advancement, principle discovery, and principle-guided model improvement. Stage I combined compact restatements, budget reinvestment, and residual incremental learning to build a frontier model. Stage II found that exact repetition and aligned restatement produce different patterns of context use, depending on target relations and prediction windows. In controlled tasks, recovering familiar performance did not ensure that unseen inputs could still use learned computations. These findings support a testable data-efficient learning principle: organize experience around the contextual dependencies needed for prediction; separately design visible information, supervision, and preservation; test learning, generalization, and retention. Stage III retained source text, masked more local clues, supervised selected targets, and preserved predictions on ordinarily masked inputs. Two continuation seeds from the same parent outperformed ordinary continuation on the complete nine-metric aggregate. Overall rose from 42.02 to 42.25 across two generations; the second achieved the highest Overall in the public Strict-Small snapshot of 8 September 2026. Further studies addressed compression, relational anchors, shared representations, and measurement. Models are available on Hugging Face; code and research records accompany the GitHub repository. Together, these stages illustrate Research RSI: recursive self-improvement of the research process. Scientific understanding and method innovations change subsequent questions and designs; new experiments test and refine them.

### 中文一句话结论
本文提出了一种数据高效的语言建模方法，通过自主研究实现从前沿模型到原则引导改进的闭环，在BabyLM 2026 Strict-Small任务中以10M语料词和100M单词累计展现量将综合分数从42.02提升至42.25，并获得了公开快照中的最高分。

### English TL;DR
This paper presents Qiushi Engine’s autonomous end-to-end research on BabyLM 2026 Strict-Small, achieving a three-stage pipeline: frontier model construction, discovery of a data-efficient principle (organizing experience around contextual dependencies while separately designing visible information, supervision, and preservation), and principle-guided model improvement. The final model improved overall score from 42.02 to 42.25 under strict data limits (10M corpus words, 100M cumulative word presentations), ranking highest in the public snapshot of 8 September 2026. The work also demonstrates recursive self-improvement of the research process (Research RSI).

### 中文详细总结
该研究由Qiushi Engine团队自主完成，目标是在有限文本下提升语言模型利用上下文、泛化新输入并保留能力的效果。工作分为三个阶段：
- **第一阶段**：结合紧凑复述、预算再投资和残差增量学习构建前沿模型。
- **第二阶段**：通过控制实验发现精确重复和对齐复述对上下文利用模式的影响不同；恢复熟悉性能不保证新输入仍能使用学到的计算。基于此提出可检验的数据高效学习原则：围绕预测所需的上下文依赖组织经验；分别设计可见信息、监督目标和功能保持；并测试学习、泛化和保留效果。
- **第三阶段**：应用上述原则，保留原文本、掩盖更多局部线索、监督选定目标、保留对常规掩盖输入的预测。两个从同一父模型继续训练的种子均优于普通继续训练，完整九指标综合得分从42.02升至42.25，其中第二个种子达到2026年9月8日公开快照中的最高分。
此外，还开展了压缩、关系锚点、共享表征和测量控制等独立研究。模型、代码和研究记录已公开。

### 方法 / 贡献
- 提出并验证了数据高效学习的三阶段自主研究框架：前沿模型构建→原则发现→原则引导改进。
- 发现精确重复与对齐复述在上下文利用上的差异，并揭示恢复熟悉性能不完全等同于泛化新输入。
- 提出可操作原则：围绕上下文依赖组织训练经验，分离可见信息、监督和保留设计，并分维度测试。
- 在BabyLM严格限制下（10M语料词、100M单词累计展现量）实现模型改进，综合分数提升0.23并取得公开快照最高分。
- 展示研究过程的递归自改进（Research RSI），即科学理解和方法创新反馈指导后续研究。

### 实验或数据
- **任务**：BabyLM 2026 Strict-Small，语料限制10M单词，累计展现限制100M单词。
- **评估指标**：九项顶级指标，涵盖BLiMP、EWoK、实体追踪、COMPS、GLUE等语言能力及人类行为相关性（阅读时间、词汇习得顺序）。
- **实验设计**：
  - 第一阶段：使用紧凑复述、预算再投资、残差增量学习训练前沿模型。
  - 第二阶段：通过控制任务（精确重复 vs. 对齐复述）分析上下文利用模式及泛化失败现象。
  - 第三阶段：应用原则，从同一父模型出发进行两个独立种子继续训练，比较效果。
- **结果**：总体分数从42.02升至42.25，第二个种子在公开快照中最高；模型和代码已发布。

### 值得关注点
- 研究完全由自动化科研流程驱动，涵盖文献调研、方法开发、实验、分析和综合，体现了递归自改进。
- 明确指出“遇到相关信息”与“学会使用信息”是两回事，并由此推导出可测试的学习原则。
- 在固定预算下，通过重新设计训练经验（而非增加数据量）获得了0.23分的提升，凸显方法创新的潜力。
- 原则强调分别设计可见信息、监督和保留，为后续数据受限场景的学习策略提供了可操作的指导。

### 局限性
- 该研究仅在BabyLM Strict-Small的严格数据限制下验证，其原则和方法在大规模数据、其他语言或不同任务上的泛化性尚未测试。
- 原则的有效性依赖人工设计的实验分离（如掩盖局部线索、监督特定目标），自动化实现细节和参数敏感性未在摘要中讨论。
- 提升幅度（0.23分）虽在限定条件下有意义，但在绝对分数较高的情况下，改进幅度相对较小，可能难以直接推广至其他设定。
- 未涉及模型架构创新或超越现有基准的全面对比，贡献主要集中在训练策略和自主学习流程设计。

## 3. Robust Multimodal Sentiment Analysis with Incomplete Modalities via Semantic-aware Completeness based Reconstruction

- Source: arxiv
- arXiv ID: 2609.10950
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.10950v1
- PDF: https://arxiv.org/pdf/2609.10950v1
- DOI: https://doi.org/10.48550/arXiv.2609.10950

### Authors

Han-Jun Choi, Byunggill Joe, Saim Shin, Jin Yea Jang

### Abstract

Recent multimodal sentiment analysis studies increasingly adopt text-centric fusion approaches to exploit the rich sentiment information inherent in the textual modality. However, these approaches often suffer from performance degradation during inference due to partially missing or noisy data in real-world scenarios, especially when sentiment-related cues are missing. To address this issue, we introduce a new completeness estimation approach that quantifies the degree of sentiment-relevant information preserved in incomplete data to guide the reconstruction of missing semantics. Furthermore, we propose a training strategy that stabilizes multi-task learning while jointly optimizing sentiment prediction and completeness estimation. Extensive experiments and in-depth analyses on three benchmark datasets demonstrate that the proposed approach enables more accurate semantic reconstruction, leading to more precise sentiment prediction.

### 中文一句话结论
本文提出一种基于语义完整度估计的文本缺失重建方法，用于在不完整多模态数据下提升情感分析鲁棒性。

### English TL;DR
This paper introduces a semantic-aware completeness estimation method that quantifies missing sentiment information in multimodal data to guide reconstruction and improve robustness in sentiment analysis under incomplete modality conditions.

### 中文详细总结
针对多模态情感分析中文本缺失导致性能下降的问题，本文提出TCMR框架。核心创新包括：(1) 语义完整度估计器CompNet，通过预测文本保留的语义信息程度来指导重建；(2) 基于目标概率的伪标签生成策略TPSC，用于训练完整度估计器；(3) 重要性感知的代理特征生成器IPFG，自适应加权辅助模态贡献；(4) 交替优化策略AOS，缓解多任务学习的梯度冲突。在三个基准数据集上的实验表明，该方法优于12个基线模型。

### 方法 / 贡献
- **完整度估计**：首次提出语义感知的完整度量化方法，替代基于缺失率的简单评估。
- **伪标签生成**：利用预训练分类器对不完整文本的预测概率作为完整度标签。
- **代理特征生成**：IPFG根据辅助模态重要性生成加权代理特征，用于语义重建。
- **交替优化**：AOS通过分阶段更新完整度估计与主任务参数，稳定多任务学习。

### 实验或数据
在三个多模态情感分析基准数据集上进行了实验，与12个基线模型对比，所提方法在不同缺失率下均取得一致更优性能。摘要未提供具体数据集名称、指标数值或消融实验细节。

### 值得关注点
- 从语义完整性而非缺失率角度处理数据缺失问题，更贴合实际场景。
- 伪标签生成策略利用已有分类器，无需额外标注。
- 交替优化策略缓解了完整度估计与情感预测之间的梯度冲突。

### 局限性
摘要中未讨论方法的局限性。可能包括依赖预训练分类器质量、辅助模态完全缺失时的表现、计算开销及泛化性等问题，需结合全文进一步分析。

## 4. Analyzing Traditional and Neural Approaches to Multilingual Readability Assessment

- Source: arxiv
- arXiv ID: 2609.10792
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.10792v1
- PDF: https://arxiv.org/pdf/2609.10792v1
- DOI: https://doi.org/10.48550/arXiv.2609.10792

### Authors

Joshua Wong, Chris Tanner

### Abstract

Transformer-based models excel at Automatic Readability Assessment (ARA), yet feature-based models remain in active use because their predictions tie back to linguistic properties. This matters because readability labels are subjective and rater-dependent, so high accuracy on noisy ground truth may reflect surface patterns rather than the linguistic structure that defines difficulty. We test whether transformers internalize the same features as traditional models across Arabic, English, French, Hindi, and Russian using the ReadMe++ dataset. Shapley Additive Explanations (SHAP) identify the features driving traditional classifiers, which we then use as TCAV concept sets to probe multilingual XLM-R and language-specific encoders. Transformers recover surface-length, syntactic, and lexical-diversity signals, and reflect the ordinal CEFR structure of the traditional models. Alignment varies by model family, language, and layer, with language-specific encoders tracking traditional models more clearly than XLM-R. High linear separability does not always imply directional influence, limiting linear probing for count-based readability features.

### 中文一句话结论
本研究通过SHAP和TCAV框架，在五种语言上发现Transformer可读性模型能够部分恢复传统基于特征模型所使用的语言信号（如表面长度、句法复杂度），但对齐程度因语言、模型族和层而异，且语言特定编码器比多语言XLM-R对齐更清晰。

### English TL;DR
This paper uses SHAP and TCAV to compare feature-based and transformer-based readability models across five languages, finding that transformers recover some traditional linguistic signals but alignment varies by language, model family, and layer, with language-specific encoders aligning more closely than XLM-R.

### 中文详细总结
本文探讨Transformer编码器是否学到与传统特征模型相同的可读性相关语言信号。使用ReadMe++数据集（阿拉伯语、英语、法语、印地语、俄语，共9685个句子），首先在手工语言特征上训练传统分类器（逻辑回归、线性SVM、随机森林），并用SHAP识别驱动预测的关键特征。将这些特征作为TCAV的概念集，探测多语言XLM-R和语言特定编码器（BERT、AraBERT、CamemBERT、MuRIL、RuBERT）的内部表示。结果显示：Transformer能恢复表面长度、句法复杂性和词汇多样性等信号，并部分反映传统模型的CEFR序数结构；但对齐程度因模型族、语言和层而异，语言特定编码器的TCAV模式比XLM-R更清晰；高线性可分离性并不总是意味着方向性影响，限制了线性探测在基于计数的可读性特征上的有效性。主要贡献包括：在五种语言上比较传统与Transformer可读性模型；刻画语言、模型族和层对特征对齐的影响；提出SHAP-TCAV框架用于测试神经可读性模型是否编码可解释信号。

### 方法 / 贡献
- **方法**：先训练传统分类器（逻辑回归、线性SVM、随机森林）在LFTK提取的手工特征上，经相关性聚类降维后，用SHAP计算特征全局重要性，通过Borda聚合选出每种语言最重要的10个特征作为概念集。然后对微调后的Transformer编码器（XLM-R及各语言特定模型）提取每层[CLS]表示，训练CAV区分高特征值句子与随机句子，并计算沿概念方向移动对CEFR预测类别概率的方向性影响（TCAV）。
- **贡献**：(1) 在五种语言上系统比较传统特征模型与Transformer可读性模型；(2) 揭示特征对齐程度随语言、模型族和编码器层的变化规律；(3) 引入SHAP-TCAV框架来检验神经模型是否编码传统ARA所依赖的相同可解释信号。

### 实验或数据
- **数据集**：ReadMe++（句子级CEFR标注，A1-C2，六类分类），按60/10/30分层分割得到训练/验证/测试集，五种语言总计9685句。对于英语和阿拉伯语，额外使用CEFR-SP和DARES扩充概念池（分别约12000和15000句），仅用于TCAV概念集构建，不用于训练/测试。
- **传统模型**：LFTK提取特征（英语211个，其他语言141个），经相关性层次聚类（阈值τ=0.30）降维至英语59个、其他语言32-35个。训练三个分类器，超参数通过10折交叉验证以QWK为指标调优。
- **Transformer模型**：XLM-R base及语言特定编码器（BERT、AraBERTv02、CamemBERT、MuRIL、RuBERT），各自微调20轮，学习率从{1e-5,1e-6,1e-7}中选取最佳验证QWK，所有语言均为1e-5。探针使用12层中每层的[CLS]表示。
- **TCAV**：对每个选定特征，正概念集为特征值最高的100句，随机集从同一池中采样（英语/阿拉伯语1000个随机集，其他语言500个）。每层训练逻辑回归CAV，计算方向性导数D_{C,k,l}。

### 值得关注点
- Transformer能恢复表面长度、句法复杂性和词汇多样性信号，并部分反映CEFR序数结构，表明其表示并非完全脱离传统语言特征。
- 语言特定编码器（如CamemBERT、MuRIL等）比多语言XLM-R与特征模型的TCAV对齐更清晰，提示多语言表示可能因共享参数而稀释了语言专有可读性信号。
- 高线性可分离性并不等价于方向性影响：部分基于计数的特征（如词数）虽然线性可分，但在TCAV中不显示显著的方向性影响，说明线性探测可能高估功能相关性。

### 局限性
- 仅使用ReadMe++单一语料库，标签分布不平衡且覆盖语言有限（五种），结论的泛化性受限于L2可读性场景和CEFR标注体系。
- TCAV概念仅由特征值最高的句子定义，未涵盖低特征值或中等范围的变体，可能无法全面捕捉该特征在模型中的使用方式。
- 扩充概念池（英语/阿拉伯语）可能引入轻微领域偏移，但TCAV设计将偏移均匀分布在概念和随机集中，影响有限。
- 方向性影响仅反映沿概念方向移动对预测的局部效应，无法完全排除模型以其他非线性方式使用这些特征。

## 5. TransClean: A Benchmark for Detecting and Extracting Clean Translations from Large Language Model Outputs

- Source: arxiv
- arXiv ID: 2609.11399
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.11399v1
- PDF: https://arxiv.org/pdf/2609.11399v1
- DOI: https://doi.org/10.48550/arXiv.2609.11399

### Authors

Shenbin Qian, Yves Scherrer

### Abstract

Large language models (LLMs) are increasingly used for machine translation, yet their outputs often contain additional text beyond the translation itself, such as language labels, explanations or bilingual repetitions, which we term translation noise. Despite its prevalence, this problem lacks dedicated benchmarks and systematic study. We analyze over 790,000 translation outputs from 12 LLMs across 22 language pairs (LPs) and identify 12 recurring noise patterns, which we group into formatting and content noise. Building on the observed patterns, we construct TransClean, a controlled benchmark of 9,900 pairs of noisy and clean translation outputs, comprising 8,800 synthetically generated instances and 1,100 manually curated authentic instances. We evaluate two extraction approaches on the TransClean benchmark: 1) a span-based extraction method leveraging translation quality estimation models for span detection, and 2) an LLM-based extraction method that prompts an LLM to isolate the translation. Our benchmark and analysis provide the first systematic framework to evaluate and improve the cleanliness of LLM translation outputs.

### 中文一句话结论
本文首次系统研究了大语言模型翻译输出中的“翻译噪音”问题，并构建了包含9900个标注样本的基准测试集TransClean，用于检测和提取干净的翻译文本。

### English TL;DR
This paper systematically studies translation noise in LLM outputs, identifying 12 noise patterns, and introduces TransClean—a benchmark of 9,900 instances for detecting and extracting clean translations.

### 中文详细总结
本工作着眼于大语言模型（LLM）在机器翻译任务中常输出多余内容（如语言标签、解释、双语重复等）的问题，称之为“翻译噪音”。作者分析了12个LLM在22个语言对上的超过79万条翻译输出，归纳出12种噪音模式，分为格式噪音和内容噪音两大类。基于这些模式，构建了TransClean基准，包含8800条合成噪音实例和1100条人工筛选的真实噪音实例，并配有干净的参考翻译。在TransClean上评估了两种提取方法：1) 基于翻译质量估计的跨度提取；2) 通过提示LLM直接提取翻译。同时设计了清洁匹配率（CMR）和噪音降低率（NRR）两种评价指标。

### 方法 / 贡献
- 大规模噪音分析：对12个LLM、22个语言对、3种提示模板的翻译输出进行系统分析，发现常见噪音模式。
- 基准构建：创建首个专门用于检测和提取干净翻译的基准TransClean（9900个样本），包含合成与真实噪音。
- 提取方法评估：测试了基于质量估计模型的跨度检测方法和基于LLM的提示提取方法，并提出了针对性的评价指标（CMR, NRR）。
- 贡献：为LLM翻译输出的后处理提供了系统框架和标准化评估工具。

### 实验或数据
- 数据来源：从TED、WMT20质量估计、SwissAdmin、中韩平行语料四个平行语料库中为每个语言对抽取3000个句子，共22个语言对的基础翻译数据。
- 噪音生成：基于前期分析得到的模板向干净翻译中注入12种噪音模式，生成8800个合成实例；另从12个LLM的真实输出中手动收集1100个真实噪音实例。
- 评估实验：在TransClean上评测两种提取方法（span-based和LLM-based），使用CMR和NRR指标。实验细节如模型推理参数等在附录中说明。

### 值得关注点
- 首次系统定义并分类了LLM翻译输出中的噪音问题，提供了具体模式列表。
- 基准同时包含合成数据（可控制噪音类型和位置）和真实数据（反映实际分布），具有较高的实用价值。
- 提出的CMR和NRR指标为翻译后处理任务提供了专门评估手段，区别于传统整体翻译质量指标。
- 工作不依赖修改模型或重新训练，适合对黑盒或商用LLM输出的后处理。

### 局限性
- 基准仅涵盖22个语言对和12个模型，可能无法代表所有场景的噪音分布。
- 合成噪音基于有限模板生成，真实性可能不及实际噪音的多样性。
- 提取方法仅评估了两种基础方案，未探索更复杂或学习型的方法。
- 真实噪音子集（1100条）规模较小，且干净参考翻译来自商业翻译平台，可能存在偏差。
- 未对提取后的翻译进行下游任务（如MT评估、部署）的影响分析。

## 6. Does Linguistic Structure Enrichment Enhance Coherence Assessment? Not With Current Architectures

- Source: arxiv
- arXiv ID: 2609.10893
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.10893v1
- PDF: https://arxiv.org/pdf/2609.10893v1
- DOI: https://doi.org/10.48550/arXiv.2609.10893

### Authors

Victor Mazzotti, Luiz Pereira, Marina Bitencourt dos Santos, Helena Maia, Carlos Caetano, Nádia Felix, Sandra Avila

### Abstract

Recent advances in large language models have transformed human-computer interaction. Despite their fluency, these models often produce texts that are grammatically correct but semantically incoherent, containing contradictions or disruptions in logical flow. This work investigates whether enriching text with syntactic and rhetorical information can improve incoherence prediction. Our experiments and analysis show that plain texts achieved higher accuracy because the added information was structurally and syntactically incompatible with the language model's architecture. Additionally, to demonstrate the practical importance of coherence assessment, we performed zero-shot experiments on a Brazilian disinformation dataset, suggesting that textual coherence can serve as a proxy for detecting misleading content. Code and models are available at https://github.com/ittozzamV/cohereclassifier.

### 中文一句话结论
在当前语言模型架构下，向文本添加句法和修辞结构信息并不能提升连贯性评估的性能，反而可能因为结构不兼容而降低准确率。

### English TL;DR
Enriching text with syntactic and rhetorical information does not improve coherence assessment in current language models, as plain texts achieve higher accuracy due to structural incompatibility; however, coherence can serve as a proxy for detecting disinformation.

### 中文详细总结
本研究探讨了通过向文本注入句法（词性标注，POS）和修辞结构（修辞结构理论，RST）信息是否能够提升语言模型对文本连贯性的检测能力。实验结果表明，使用原始纯文本训练的模型在连贯性分类任务上准确率更高，因为添加的句法和修辞信息与当前Transformer架构（特别是XLM-RoBERTa Longformer）的表示方式存在结构性和句法上的不兼容。此外，作者在巴西虚假信息数据集FakeTrueBR上进行了零样本实验，发现文本连贯性评估可以作为检测误导性内容的间接指标（代理），展示了连贯性评估的实际应用价值。

### 方法 / 贡献
- **方法**：提出了一种通过添加特殊符号来增强文本输入的策略。包含两个版本：POS增强（在单词后附加词性标签）和RST增强（在EDU边界前后添加表示修辞关系和核心-卫星结构的特殊token）。增强后的文本仍使用标准XLM-RoBERTa Longformer模型进行分类，无需修改模型架构。
- **贡献**：1) 首次系统评估了在Transformer-base连贯性分类器中直接增强输入的策略，发现其不仅无效反而有害；2) 证明了连贯性评估可以作为离线场景下检测虚假信息的有效代理，且零样本跨语言迁移可行。

### 实验或数据
- 使用了专门的故事连贯性数据集（未在摘要中明确数据集名称，但文中提到使用GCDC等语料库）。
- 零样本实验使用了巴西葡萄牙语虚假信息数据集FakeTrueBR。
- 未在摘要中提供具体性能数据（如准确率、F1分数等）。

### 值得关注点
- 明确指出了加入“较多”的RST信息会导致模型困惑，因为特殊token数量大且与模型预训练表示差距大。
- 零样本实验表明葡萄牙语的连贯性模型可以用于英语的虚假信息检测，体现了一定的跨语言知识迁移能力。
- 提出了一个公开可用的代码库和模型（GitHub链接），方便复现。

### 局限性
- 只测试了XLM-RoBERTa Longformer这一种特定架构，结论可能不适用于其他语言模型（如基于GPT、T5的模型或更大规模模型）。
- 所使用的连贯性数据集可能规模较小或类型有限，无法覆盖所有常见的连贯性错误模式。
- 没有探讨是否可以通过更自然的融合方式（如使用专门设计的架构层）来有效利用句法和修辞信息，只测试了“直接添加token”这一种简单增强方式。
- 零样本实验仅在单一种类和规模的虚假信息数据集上进行，泛化性有待验证。
- 没有提供增强版本的具体性能下降数据（如准确率降幅、错误案例分析），结论的量化支撑不够充分。

## 7. E-CONAN (Entailment, CONtradition And Neutral) Benchmarks: Arabic Textual Entailment and Natural Inference Datasets

- Source: arxiv
- arXiv ID: 2609.11334
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.11334v1
- PDF: https://arxiv.org/pdf/2609.11334v1
- DOI: https://doi.org/10.48550/arXiv.2609.11334

### Authors

Khloud AL Jallad, Nada Ghneim, Ghaida Rebdawi

### Abstract

Natural Language Inference processes pairs of sentences to extract their semantic relations. NLI has been a hot research topic, integrated as a main component in other NLP applications. Despite significant advancements in textual inference across various languages all around the world, Arabic language still suffers from limited resources in this domain. To address this gap, this paper introduces E-CONAN benchmarks that are composed of sentences pairs from various sources: (1) automatically-translated pairs, (2) human-validated machine-translated pairs, (3) hand-crafted pairs from teaching Arabic as foreign language books, and (4) headlines pairs from different news channels containing rumors. E-CONAN contains two benchmark datasets, E-CONAN-2, a 2-way dataset (RTE) and E-CONAN-3, a 3-way dataset (NLI). Additionally, we have used E-CONAN benchmarks to evaluate 9 state-of-the-art multilingual pretrained models using zero-shot classification. Models were evaluated across the ArNLI, XNLI, and E-CONAN datasets. Results show that E-CONAN is a potentially valuable resource for evaluating model generalization and even for fine-tuning pre-trained models. Its diverse composition, derived from a combination of sources, offers a broader and more robust assessment compared to XNLI and ArNLI. In addition, we have evaluated 5 LLMs on E-CONAN-3 dataset. Moreover, we incorporated MARBERT as a representative Arabic-specific baseline and conducted performance evaluation comparison to demonstrate how Arabic-specific models scale against cross-lingual and LLM-based approaches on the E-CONAN benchmarks. Furthermore, we conducted detailed qualitative and quantitative error analysis to analyze frequent error patterns. E-CONAN benchmarks will be publicly available, we hope that it will enrich research community in Arabic textual entailment and natural language inference.

### 中文一句话结论
本文构建了包含多来源、多种类标注的阿拉伯语自然语言推理基准数据集 E-CONAN（2-way 和 3-way），并通过评测多种预训练模型和大语言模型证明了其作为鲁棒评估资源的价值。

### English TL;DR
This paper introduces the E-CONAN benchmarks, a diverse set of two Arabic NLI datasets (E-CONAN-2 and E-CONAN-3) sourced from multiple translation and text types, and evaluates various pre-trained models and LLMs, showing their value for robust Arabic textual entailment assessment.

### 中文详细总结
阿拉伯语在自然语言推理（NLI）领域资源匮乏。为此，本文提出 E-CONAN 基准，包含两个数据集：E-CONAN-2（2路 RTE，24,875 对）和 E-CONAN-3（3路 NLI，18,875 对）。数据来自四种途径：(1) 自动翻译对；(2) 人工验证的机器翻译对；(3) 从阿拉伯语外语教学书籍中手工编写的对；(4) 包含谣言的新闻头条对。作者使用零样本分类评估了 9 个多语言预训练模型（在 ArNLI、XNLI 和 E-CONAN 上）以及 5 个大语言模型（在 E-CONAN-3 上），并加入了阿拉伯语专用模型 MARBERT 做基线。结果显示 mDeBERTa 在预训练模型中表现最佳（E-CONAN-3 准确率 71%），Gemma 在 LLM 中最佳（68%）；当将任务简化为 2-way 标注后，Gemma 和 Qwen 分别达到 95% 和 94%。错误分析表明，预训练模型常被词汇重叠误导，而 LLM 常被主题熟悉度误导。

### 方法 / 贡献
1. **构建了 E-CONAN-2（2-way RTE）**：包含 24,875 个句子对，来源于 ArNLI、SNLI 的阿拉伯语翻译部分、XNLI 的阿拉伯语翻译部分、AnsStance 和 ArEntail。
2. **构建了 E-CONAN-3（3-way NLI）**：包含 18,875 个句子对，来源于上述前四种资源。
3. **评估了 10 个预训练模型**（实为 9 个预训练 + 1 个阿拉伯语基线），在 ArNLI、XNLI 和 E-CONAN 上进行了零样本分类对比。
4. **评估了 6 个大语言模型**在 E-CONAN-3 上的表现，并进行了定量与定性错误分析。
5. 数据集将公开，旨在丰富阿拉伯语文本蕴含研究。

### 实验或数据
- **预训练模型实验**：使用零样本分类评估 9 个 SOTA 多语言模型（如 mDeBERTa、XLM-R 等），在 ArNLI、XNLI 与 E-CONAN 三个数据集上测试。最佳模型 mDeBERTa 在 E-CONAN-3 上准确率 71%，在 XNLI 上 86%。
- **大语言模型实验**：5 个 LLM（如 Gemma、Qwen 等）在 E-CONAN-3 上评估，Gemma 准确率 68%。转换为 2-way 后 Gemma 达 95%，Qwen 达 94%。
- **附加实验**：纳入 MARBERT 作为阿拉伯语专用基线，并与跨语言模型和 LLM 进行性能对比。
- **错误分析**：定量和定性分析揭示了常见错误模式：预训练模型易被词汇重叠误导，LLM 易被主题熟悉度误导。
- **数据规模**：E-CONAN-2 24,875 对，E-CONAN-3 18,875 对。

### 值得关注点
- **数据多样性**：E-CONAN 融合了自动翻译、人工验证翻译、手工编写和新闻头条，覆盖正式、口语、翻译及高度本地的阿拉伯语结构，比仅靠机器翻译的 XNLI 和 ArNLI 更全面。
- **错误分析新发现**：首次指出预训练模型和 LLM 在阿拉伯语 NLI 中的不同误导因素（词汇重叠 vs. 主题熟悉度）。
- **公开可用**：数据集将公开，为阿拉伯语 NLI 社区提供宝贵资源。
- **多维度对比**：同时评估了预训练模型、LLM 和阿拉伯语专用模型，提供了全面基准。

### 局限性
作者未在摘要中明确讨论局限性。基于论文内容，潜在局限包括：(1) 部分数据依赖自动翻译，可能引入噪声；(2) 数据集规模中等（最大约 2.5 万对），相比英文 NLI 基准较小；(3) 仅进行了零样本评估，未展示在 E-CONAN 上微调后的性能；(4) 未报告人类表现作为上界参考。

## 8. SEAR: Segment-Evidence-Aware Routing for Weak-to-Strong Multilingual Speech MCQ

- Source: arxiv
- arXiv ID: 2609.11355
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.11355v1
- PDF: https://arxiv.org/pdf/2609.11355v1
- DOI: https://doi.org/10.48550/arXiv.2609.11355

### Authors

Huy Hoang Le, Long-Bao Nguyen, Minh Tri Dao

### Abstract

This paper describes our system for Task~2 of the second Multilingual Conversational Speech Language Model (MLC-SLM) Challenge. We adapt Qwen3-Omni-30B-A3B-Instruct with a segment-evidence-aware data and post-training pipeline. A language model converts timestamped ASR into coherent event spans, which are expanded by a boundary margin and cropped from the original recording. We then synthesize complementary semantic MCQs with Qwen3.6-27B and acoustic MCQs with Gemini~3.1 Flash-Lite, followed by structural, grounding, answer-consistency, and target-model trainability checks, yielding 359,825 verified MCQs across 21 language and accent variants. A text-only probe partitions the data into weak, text-answerable items used for supervised fine-tuning and strong, audio-dependent items used for reinforcement learning with Group Sequence Policy Optimization (GSPO), stabilized by debiased advantages, sequence-level importance correction, and dynamic filtering. Our system obtains 90.92% accuracy on the final official evaluation set.

### 中文一句话结论
本文提出 **SEAR** 分段证据感知管道，通过弱（文本可答）→强（音频依赖）训练策略，在双语语音多项选择题任务上达到 **90.92%** 准确率。

### English TL;DR
The paper presents SEAR, a segment-evidence-aware data and post-training pipeline for multilingual speech MCQ. It generates verified semantic/acoustic MCQs from timestamped ASR, partitions them into weak (text-answerable) and strong (audio-dependent) items via a text-only probe, applies SFT on weak items, and stabilized GSPO-based RL on strong items, achieving 90.92% accuracy on the final evaluation set.

### 中文详细总结
本文针对多语言对话语音理解的MCQ任务，提出了一套完整的后训练方案。核心是 **分段证据感知管道**，包括：
1. **事件定位**：用LLM将带时间戳的ASR转录转换为连贯事件跨度，并扩展边界后裁剪为音频段。
2. **双分支MCQ合成**：语义分支（Qwen3.6-27B）基于文本生成内容类问题；声学分支（Gemini 3.1 Flash-Lite）基于波形生成声学特征类问题。
3. **质量与可训练性验证**：经过结构性、可答性、一致性等检查和目标模型可训练性筛选，最终获得 **359,825** 个跨21种语言/口音的验证MCQ。
4. **弱到强路由**：通过纯文本文本探针划分音频依赖度，弱项用于监督微调（SFT），强项用于基于GSPO的强化学习，并引入去偏优势、序列级重要性校正和动态滤波稳定训练。最终在官方测试集上达到 **90.92%** 准确率。

### 方法 / 贡献
1. **事件保留分割管道**：LLM从带时间戳ASR中提取事件跨度，可变边界扩展，避免固定窗口随意截断。
2. **双分支合成与验证**：语义分支（Qwen3.6-27B）+ 声学分支（Gemini 3.1 Flash-Lite），经四阶段质量检查和目标模型可训练性筛选，生成高质MCQ。
3. **稳定的弱到强训练配方**：SFT（弱项）→ 稳定化GSPO（强项），包含去偏优势、序列级重要性采样和动态滤波，提升MoE模型训练稳定性。

### 实验或数据
- **数据**：共 **359,825** 个验证过的段级音频MCQ，覆盖21种语言/口音变体（每变体11.5K–21.9K）；弱（文本可答）项占多数（18/21语言），仅泰语、俄语、他加禄语为强多数。
- **实验结果**：在MLC-SLM Challenge Task 2最终官方评估集上达到 **90.92%** 准确率。
- **训练细节**：基于Qwen3-Omni-30B-A3B-Instruct，仅以LoRA适配语言模型，冻结音频编码器和对齐器。

### 值得关注点
- **弱-强路由**：通过文本探针量化音频贡献度，实现差异化训练，避免在文本可答项上浪费资源，聚焦音频依赖项。
- **GSPO稳定性改进**：结合Dr.GRPO的去偏优势、序列级截断重要性采样(TIS)和动态滤波（保留非零奖励方差分组），有效提升MoE模型RL训练效果。
- **数据生成质量**：双分支合成+多重验证机制（可答性、格式、时间戳、可训练性）确保MCQ高质量和任务匹配。

### 局限性
- **依赖上游组件**：数据质量受限于外部ASR（时间戳精度）和生成LLM（Qwen3.6-27B、Gemini 3.1 Flash-Lite）的能力，可能导致错误或偏差。
- **弱-强划分近似**：基于纯文本探针的音频依赖度估计可能不完全准确，部分音频依赖项可能被误判为弱项。
- **语言覆盖不均衡**：部分语言（如泰语）强项占比低，可能限制音频相关能力的提升。
- **仅LoRA微调**：仅适配语言模型，未调整音频编码器，可能限制模型对声学特征的学习能力。

## 9. Rebalancing Token Importance in Language Models with TF-IDF Weighted Cross-Entropy Loss

- Source: arxiv
- arXiv ID: 2609.11029
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.11029v1
- PDF: https://arxiv.org/pdf/2609.11029v1
- DOI: https://doi.org/10.48550/arXiv.2609.11029

### Authors

Zhijian Li, Stefan Larson, Kevin Leach

### Abstract

Large language models are typically trained under uniform token weighting, which allows frequent and low-information tokens to dominate learning and can increase the tendency to memorize surface-level text spans. To address this, we present an information-weighted cross-entropy loss that rescales token-level contributions using TF-IDF statistics, emphasizing semantically informative tokens while down-weighting ubiquitous ones. Experiments on five decoder-only LLMs ranging from 1.1B to 13B parameters show consistent reductions in memorized substring length while preserving perplexity and downstream task performance. Under LoRA fine-tuning, TF-IDF reduces average substring memorization length by 14% across all five models. Under full-weight fine-tuning on TinyLLaMA 1.1B, the reduction reaches 58%. Our approach is architecture-agnostic and can be incorporated into existing training pipelines with less than 3% computational overhead, offering a lightweight and principled way to mitigate memorization without disrupting standard training dynamics.

### 中文一句话结论
本文提出了一种基于TF-IDF权重的交叉熵损失函数，通过重新缩放语言模型训练中每个token的贡献，在不影响困惑度和下游任务性能的前提下，显著减少了模型对训练数据的记忆长度。

### English TL;DR
This paper introduces TF-IDF weighted cross-entropy loss that rescales token contributions during language model training, achieving up to 58% reduction in memorized substring length across models from 1.1B to 13B parameters while preserving perplexity and downstream performance.

### 中文详细总结
大型语言模型通常采用均匀的token权重进行训练，这导致频繁出现的、信息量低的token主导学习过程，增加了模型记忆表层文本片段（substring）的趋势。为了解决这一问题，作者提出了一种使用TF-IDF统计量重新缩放每个token在损失函数中贡献的方法。该方法提高了语义信息丰富token的权重，同时降低了常见且信息量低token的权重。实验结果表明，在五种不同规模（1.1B到13B参数）的仅解码器语言模型上，该方法在保持模型困惑度和下游任务（如摘要、问答）性能的同时，一致地减少了模型记忆的平均子串长度。在LoRA微调设置下，五个模型的平均记忆子串长度减少了14%。在TinyLLaMA 1.1B模型的全权重微调中，记忆子串长度的减少达到了58%。该方法与模型架构无关，计算开销低（少于3%），可以轻松集成到现有的训练流程中。

### 方法 / 贡献
本文的主要贡献是提出了一种信息加权的交叉熵损失函数，在训练过程中利用TF-IDF统计量重新调整每个token的梯度贡献。该方法分为几个步骤：
1.  对于训练数据中的每个token，计算其局部的TF以及基于连续K个mini-batch累积缓冲区估算的IDF。
2.  将TF和IDF相乘得到原始权重，并将其归一化以保持梯度的尺度。
3.  在计算交叉熵损失时，将每个token的损失项乘以归一化后的权重，从而更加强调语义上独特和有信息量的token。
该方法的贡献在于提供了一种轻量级、无架构约束、且能在不牺牲模型性能的前提下有效缓解模型记忆问题的训练目标，可以作为现有训练流程的即插即用组件。

### 实验或数据
该论文对五种公开的仅解码器语言模型进行了评估，涵盖1.1B到13B参数规模，包括TinyLLaMA 1.1B、Pythia 1.4B、GPT-J 6B、LLaMA-2 7B和LLaMA-2 13B。主要微调采用LoRA方法，并在TinyLLaMA 1.1B上进行了全量权重微调的对比实验。评估标准包括：模型记忆程度（平均/最大子串长度、ROUGE-L）、模型基础困惑度，以及下游任务性能（如摘要、问答）。训练和评估所使用的具体数据集（如用于记忆评估的现有数据、用于下游任务的具体基准）在给出的摘要文本中未提及。

### 值得关注点
1. **跨模型规模的鲁棒性**：该方法在从1.1B到13B的多种模型上均有效，证明了其广泛的适应性。
2. **极低的计算开销**：新增的TF-IDF计算开销小于整体训练计算的3%，是一种成本效益极高的方法。
3. **无性能损失**：在减少误用时，困惑度和下游任务性能（如摘要和问答）并未下降，超越了以往需要权衡的改进方案，如去重或差分隐私。
4. **全量微调与参数高效微调的显著差异**：在TinyLLaMA上，全量微调时的记忆减少程度（58%）远高于LoRA微调（14%），这表明模型的记忆行为在两种模式下具有本质差异。

### 局限性
1. **方法评估的局限性**：实验重点放在了LoRA微调的小模型上，但对于更大规模模型（如70B级别）在预训练阶段的适用性和效果尚未评估。
2. **动态权重滞后性**：TF-IDF权重基于缓冲区中的历史数据进行计算，可能无法即时反映模型当前训练状态的最优权重需求。
3. **对已有训练的扰动**：该方法对训练的单向权重调整可能会影响模型对低权重token的学习效果，尽管它保留了对所有token的监督信号，但努力把注意力从它们移开。在需要更细粒度长度控制的任务中（例如：特定长度短语生成），可能会产生副作用。

## 10. Detectable Only Where It Is Confounded: What Verified Duplication Counts Say About Membership Evidence in Language Models

- Source: arxiv
- arXiv ID: 2609.10830
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.10830v1
- PDF: https://arxiv.org/pdf/2609.10830v1
- DOI: https://doi.org/10.48550/arXiv.2609.10830

### Authors

Arman Nik Khah

### Abstract

When a language model finds a sentence unusually cheap to predict, it is tempting to conclude that the sentence was in its training data. Almost every published test of that inference has had to guess which sentences were in the training data, the members, and which were not. This paper removes the guessing. Two model families, OLMo-2 and Pythia, publish their pretraining corpora, and a public index over those corpora returns the exact number of times any sentence appeared in each. Those counts make three questions answerable directly. The answers form a pincer, closing from two sides. At the duplication levels ordinary text actually has, five models from 1B to 13B parameters carry at most a faint trace of their own exposure. We measure that trace with a design that reads the same sentence through two models, which cancels fluency and quality by construction, and it comes to a rank correlation near -0.08, where -1 would be a perfect relation and 0 none. Where the trace does become strong, above roughly a thousand copies, the two corpora agree on which sentences those are, because they are the famous ones, so exposure can no longer be told apart from fame. Two further measurements show how apparent membership signal gets manufactured. A common way to build a non-member is to change one word of a member. The model does prefer the original, but the gap is the same whether the original appeared once or a hundred times, so what the model is rewarding is the author's word choice, not memory. Above a thousand copies the gap grows with model size on the twelve sentences we can test there, at the same boundary where the pincer closes. And swapping the controls for sentences that differ from the members in register moves a detector from 0.83 to 0.94 AUC, on a scale where 0.5 is a coin flip and 1.0 is perfect separation. We release the sentence banks, counts, and code.

### 中文一句话结论
这篇论文利用公开训练语料和精确重复次数发现：语言模型的“记忆痕迹”在句子重复约 1000 次以上才可检测，而到那时“被训练过”与“广为人知”已经无法区分；此前 membership inference 的许多成功主要来自对照组句子的语域或作者风格差异，而非真实记忆。

### English TL;DR
Using models with publicly released pretraining corpora (OLMo-2 and Pythia) and exact duplication counts from infini-gram, this paper shows that membership evidence in language-model loss is almost absent at ordinary duplication levels (rank correlation near -0.08), only becomes detectable above roughly 1,000 copies, and is then confounded with fame. It also shows that apparent detector success is largely manufactured by control design: one-word edits reward authorial style rather than memory, and switching to register-different controls raises AUC from 0.83 to 0.94. Sentence banks, counts, and code are released.

### 中文详细总结
论文回答了一个此前只能靠猜测的问题：一个句子在训练数据中出现多少次，模型 loss 才会真正携带“它见过这句话”的信号？

作者使用两个公开训练语料——OLMo-2 的 OLMo-mix-1124 和 Pythia 的 Pile——并通过 infini-gram 索引获得每个句子在语料中的精确匹配次数。这样可以不靠猜测，而是直接知道某个句子被模型族看到了多少次。

主要结果形成一个“钳形”论证：

- 在普通文本实际的重复水平下，1B 到 13B 的五个模型几乎检测不到自身暴露痕迹。通过让同一个句子分别经过两个模型族、从而抵消流畅度与文本质量差异，量到的秩相关只有约 -0.08（7B）和 -0.07（13B），解释方差不到 1%。
- 当重复次数超过约一千次时，loss 痕迹变得明显，但两个语料在这些句子上高度一致，因为它们都是“著名句子”。因此，暴露效应无法与“名气”效应区分开。
- 常见的构造非成员方法——把成员句子的一个词替换成近义词——并不干净。模型确实更偏好原句，但无论原句出现一次还是一百次，偏好差距都相同；这说明模型奖励的是作者的措辞，而不是记忆。只有当重复超过约一千次时（可测试的 12 个句子上），差距才随模型规模增大。
- 如果把同源替换词换成语域不同的对照句，检测器 AUC 会从 0.83 升到 0.94。这说明很多此前报告的 membership 检测成功，其实来自对照组句子的分布差异。

论文由此认为，基于 loss 的 membership inference 只在“重复次数极高且与名气混淆”的边界附近有效，普通句子上的明显成功很可能是对照组构建方式造成的人为信号。

### 方法 / 贡献
- 用 infini-gram 后缀数组索引查询两个公开语料中每个句子的精确匹配次数，把 membership 从二值标签变成可量化的“暴露剂量”。
- 从六部公版小说中部抽取 10–16 词的句子构建成员句子库；非成员通过对成员句子做单个同义词替换生成，并要求在语料中精确匹配次数为零。
- 提出 same-sentence 跨模型族设计：同一个句子分别通过 OLMo-2 和 Pythia 模型读取，从而在保持句子本身不变的情况下改变暴露水平，构造上抵消流畅度和文本质量差异。
- 用“普通句子”“著名高重复句子”“同源单字替换”“语域不同对照”等设计，系统拆解 membership 检测信号中记忆、措辞、名气与语域各自的贡献。
- 贡献包括：给出可检测暴露的重复次数阈值；指出该阈值处暴露与名气混淆；揭示常见控制句的缺陷；发布句子库、重复次数和代码。

### 实验或数据
- 模型：OLMo-2 与 Pythia 两个模型族，参数规模覆盖约 1B 到 13B。
- 数据：747 个同时具有两个语料精确计数的主句；12 个高重复/著名句子用于超高重复区间测试。
- 核心结果：
  - 1B 模型在普通句子上的 AUC 约 0.60，在著名句子上约 0.83（中位重复约 1200 次）。
  - 使用同句跨模型设计时，7B 模型秩相关 -0.08，13B 模型 -0.07，解释方差低于 1%。
  - 超过 90% 的单字替换对中，模型更偏好原句；平均差距约 0.4 nats/token，原句 token 平均概率约为替换句的 1.5 倍。该差距在重复 1 次和 100 次之间相同。
  - 将同源替换对照换成语域不同的对照句后，检测器 AUC 从 0.83 升至 0.94。
- 论文明确说明释放句子库、精确计数和代码。

### 值得关注点
- “钳形”论证：暴露信号只在重复约 1000 次以上才明显，而两个独立语料在这些高重复句子上高度一致，因为它们都是著名句子；在两个语料对暴露水平有分歧的区间，痕迹又非常微弱。
- 单字替换控制并不等价于“非成员”；它更多地反映作者措辞的自然性，而非模型记忆。
- 语域不同的对照句会把 AUC 从 0.83 推到 0.94，说明此前文献中不少 membership 检测的成功可能来自分布偏移，而非真实记忆。
- 使用可验证的精确匹配计数，而不是事后猜测成员/非成员，是该方法与以往工作的关键区别。

### 局限性
- 精确匹配计数只是暴露水平的下界：标点、引号、换行或轻微改写都会导致未被计数，因此实际暴露可能被低估。
- OLMo-2 最后的 annealing 阶段所用语料不在该索引覆盖范围内，相关暴露无法被计入。
- 分析基于较短的句子（10–16 词），不一定能直接推广到段落或更长文本。
- 超高重复区间只能依赖 12 个著名句子，样本量很小。
- 跨语料比较时，不同书籍在两边语料中的重复比例差异较大；作者也指出书级别的差异可能混入与模型族流畅度相关的因素，需要谨慎解释。

## Processing Notes

- Duplicate papers skipped: 0