# Daily arXiv - 2026-07-23

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-23T23:22:36
- Paper count: 10

## 1. Language-Specific versus Cross-Lingual Knowledge Graphs for Implicit Aspect Identification in Arabic: A Comparative Study of Reasoning and Adaptation Strategies

- Source: arxiv
- arXiv ID: 2607.20056
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2607.20056v1
- PDF: https://arxiv.org/pdf/2607.20056v1
- DOI: https://doi.org/10.48550/arXiv.2607.20056

### Authors

Lujain A. Alawwad

### Abstract

Aspect-based sentiment analysis (ABSA) in Arabic must recover both explicitly stated aspects and implicit aspects that are never named in the text. Implicit identification typically relies on an auxiliary knowledge source (e.g., a knowledge graph (KG)) linking opinion cues to aspect categories, but for a lower-resource language the practitioner faces a design choice: reuse a mature English KG through multilingual embeddings, or build a smaller native Arabic KG. This paper reports a controlled comparison of the two strategies within a single hybrid pipeline, evaluated on three Arabic benchmarks (M-ABSA, SemEval-2016 Arabic, and HAAD). We further compare two adaptation strategies for the generative extractor that feeds the KG -- zero-shot prompting versus task-specific fine-tuning of an 8B-parameter large language model (LLM). The native Arabic KG (Strategy 2) outperforms the cross-lingual English KG (Strategy 1) by +0.199 micro-F1 on M-ABSA and +0.251 on SemEval-2016, gaining on both precision and recall. Task-specific fine-tuning raises explicit-extraction micro-F1 from <= 0.13 (zero-shot) to 0.66-0.76 on M-ABSA and SemEval-2016 (0.45 on the smaller HAAD), confirming that task adaptation, rather than model scale, is decisive in a morphologically rich language.

### 中文一句话结论
在阿拉伯语隐式方面识别中，构建原生阿拉伯语知识图谱（采用词汇匹配）显著优于从英语进行跨语言迁移（使用多语言嵌入），同时对生成式提取器进行任务特定微调（而非依赖零样本提示）是提升性能的关键。

### English TL;DR
Building a native Arabic knowledge graph with lexical matching significantly outperforms cross-lingual transfer from English using multilingual embeddings for implicit aspect identification in Arabic ABSA. Additionally, task-specific fine-tuning of an 8B-parameter LLM dramatically improves explicit aspect extraction over zero-shot prompting, showing that task adaptation, not model scale, is decisive.

### 中文详细总结
本文针对阿拉伯语方面级情感分析（ABSA）中的隐式方面识别问题，系统比较了两种基于知识图谱的策略：策略1（跨语言语义匹配）复用成熟的英语知识图谱，通过多语言句子嵌入将阿拉伯语意见词映射到英语节点；策略2（原生阿拉伯语词汇匹配）构建专属的阿拉伯语知识图谱，经过复杂的形态归一化和词形还原后进行精确词汇查找。实验在三个阿拉伯语基准数据集（M-ABSA、SemEval-2016阿拉伯语、HAAD）上进行，结果一致显示策略2显著优于策略1：在M-ABSA上微F1提升+0.199（从0.159到0.358），在SemEval-2016上提升+0.251（从0.217到0.468），在精确率和召回率上均有优势。此外，研究比较了生成式提取器（Llama-3-8B）的两种适配策略：零样本提示与任务特定微调。微调后的显式提取微F1从零样本的≤0.13大幅提升至0.66-0.76（M-ABSA和SemEval-2016），证实任务适配在形态丰富的语言中起决定性作用。

### 方法 / 贡献
- **双策略对比框架**：在统一混合流水线内，控制变量地比较跨语言英语KG（策略1）与原生阿拉伯语KG（策略2）对隐式方面识别的影响
- **策略1（跨语言）**：使用孤独形容词筛选器、Stanza依存分析、CAMeL形态消歧、多语言句子编码器（paraphrase-multilingual-MiniLM-L12-v2），通过余弦相似度匹配英语KG节点，经阈值过滤、域约束和重排序后输出方面类别
- **策略2（原生阿拉伯语）**：构建专用阿拉伯语KG，实现完整的形态归一化流水线（去除变音符号、统一不同形式的alif/ya/ta marbuta、去除定冠词、词形还原、阴性转阳性基部归约），采用多级级联匹配（精确→基部精确→前缀→额外线索表→子串），并设计动词短语回溯机制处理无形容词句子
- **提取器适配研究**：比较Llama-3-8B的零样本提示与QLoRA任务特定微调，量化显式方面提取的适配差距

### 实验或数据
- **数据集**：三个阿拉伯语基准 - M-ABSA（多领域，1356条显式行+718条隐式+104条混合）、SemEval-2016阿拉伯语（酒店评论，1130条显式+96条隐式）、HAAD（书评，299条显式，无隐式）
- **隐式识别结果**：策略2在M-ABSA上精确率0.606、召回率0.254、微F1 0.358；在SemEval-2016上精确率0.698、召回率0.352、微F1 0.468
- **显式提取结果**：任务微调在M-ABSA上微F1达0.66-0.76，SemEval-2016上0.66-0.76，HAAD上0.45；零样本提示在所有数据集上F1≤0.13
- **推理分布**：策略2中52.1%（M-ABSA）和42.7%（SemEval-2016）的隐式行因无法检测到线索而停止处理；动词短语回溯在SemEval-2016中恢复了23.7%的行

### 值得关注点
- **原生KG的主导优势**：策略2在精确率和召回率上均优于跨语言策略，说明针对低资源语言时，精细的本地化构建优于依赖多语言嵌入的迁移学习
- **任务微调的决定性作用**：在形态丰富的阿拉伯语中，8B参数模型通过QLoRA微调即可从近乎不可用（F1≤0.13）跃升至可用水平（0.66-0.76），远超零样本性能，强调任务适配比模型规模更关键
- **召回率是主要瓶颈**：策略2的精确率（0.61-0.70）已接近英语KG在英语数据上的表现（0.68-0.71），但召回率（0.25-0.35）仍有较大提升空间，主要受限于阿拉伯语形态复杂性和语用表达
- **动词短语回溯的有效性**：设计的手工动词短语线索表可恢复大量酒店评论中的推荐表达，证明基于语言特点的规则方法仍有重要价值

### 局限性
- **召回率受限**：原生KG的召回率受覆盖范围限制，约42%-52%的隐式行因无法检测到任何线索而被跳过，部分源于阿拉伯语的形态多样性和非形容词性语用表达
- **策略2的脆弱性**：依赖繁重的形态归一化流水线，任何未覆盖的形态变体（意外附着词缀、不规则复数、方言拼写）都会导致匹配失败
- **手工构建成本**：策略2需要手工整理名词→方面映射表、形容词-名词复合词表以及动词短语回溯表，构建和扩展劳动密集
- **阈值敏感性**：跨语言策略中的多个相似度阈值（0.75/0.85/0.65）和权重（0.6/0.4）需要精细调优
- **HAAD数据集限制**：HAAD不含隐式方面，无法用于KG策略对比，减少了实验的整体覆盖度

## 2. TriAgent: Divergence-Aware Multi-Agent Committees for Cost-Efficient Financial Sentiment Analysis

- Source: arxiv
- arXiv ID: 2607.19794
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.19794v1
- PDF: https://arxiv.org/pdf/2607.19794v1
- DOI: https://doi.org/10.48550/arXiv.2607.19794

### Authors

Isabel Xu, Cynthia Xu, Rachel Ren, Cong Guo, Jiacheng Ding

### Abstract

Production LLM-based financial sentiment analysis faces a structural cost trap: most queries are trivially classifiable, yet expensive cloud reasoners process them all, and the bill scales linearly with user count. We present TriAgent, a multi-agent committee stratified by contextual granularity -- a word-level lexicon (VADER), a sentence-level domain transformer (FinBERT), and a cross-sentence reasoner (Qwen2.5, 0.5B-14B-4bit, with Mistral-7B and Phi-3.5-mini cross-family checks). A three-way Semantic Divergence Index (SDI) measures pairwise disagreement across granularities and routes each query accordingly. Our central finding is the critic plateau: when the LLM is re-tasked as a critic over the smaller agents' outputs, F1 plateaus at ~0.87 across 1.5B-7B Qwen (bootstrap 95% CIs overlap), while a same-size 3-persona vote drops to F1=0.66, which is driven by granularity-stratified diversity. Three corollaries follow from the same SDI signal: (i) a Shared Consensus Dictionary on multilingual sentence-BERT answers 95% of Chinese queries from an English cache at F1=0.99 -- cross-border canonicalization at zero marginal cost; (ii) SDI doubles as a post-hoc LLM-hallucination detector at AUC=0.90; (iii) the SDI single-stage strategy attains the best risk-adjusted return (Sharpe=3.50) on a 20-ticker back-test, dominating both always-FinBERT (1.36) and always-LLM (0.11). At 10M-user scale, TriAgent saves $9.3M/year vs. a GPT-4o-mini baseline. Code, lexicons, and the SCD are released.

### 中文一句话结论
TriAgent通过语义分歧指数（SDI）在词级、句级和跨句三级粒度上路由查询，实现成本高效的金融情感分析，F1达约0.87，节省930万美元/年（1000万用户），并具备跨语言缓存和幻觉检测能力。

### English TL;DR
TriAgent introduces a divergence-aware multi-agent committee that stratifies financial sentiment analysis by contextual granularity—using a word-level lexicon, sentence-level transformer, and cross-sentence LLM—and employs a Semantic Divergence Index to route queries cost-efficiently, achieving F1 ≈ 0.87, saving $9.3M/year at 10M-user scale, and serving as both a cross-lingual canonicalizer and hallucination detector.

### 中文详细总结
TriAgent是一个多智能体委员会，由三个层次组成：词级词典（VADER）、句级领域变换器（FinBERT）和跨句推理器（Qwen2.5等LLM）。核心发现是“批评家平台”现象：将LLM重新用作较小智能体输出的批评家时，F1在1.5B–7B参数范围内稳定在约0.87，而相同大小的三人投票则降至0.66，原因是粒度分层多样性。语义分歧指数（SDI）测量三个粒度对之间的不一致性，并据此路由查询。基于SDI的三个推论：共享共识词典（SCD）利用多语言句子嵌入，95%的中文查询可从英文缓存中以F1=0.99回答；SDI可作为事后幻觉检测器（AUC=0.90）；SDI单阶段策略在20个股票回测中获得最佳夏普比率（3.50）。在1000万用户规模下，TriAgent相比GPT-4o-mini基线每年节省930万美元。

### 方法 / 贡献
- 提出三层委员会（词级VADER、句级FinBERT、跨句LLM）及语义分歧指数（SDI）用于路由。  
- 发现“批评家平台”：LLM批评家（1.5B–7B）在所有规模下F1≈0.87，而三人投票仅0.66。  
- 共享共识词典（SCD）实现跨语言缓存，95%中文查询命中英文缓存且F1=0.99。  
- SDI作为事后幻觉检测器（AUC=0.90）。  
- 20个股票回测中SDI单阶段策略夏普比率3.50，优于策略。  
- 成本分析：1000万用户规模下年节省930万美元。

### 实验或数据
- 数据集：Financial PhraseBank（FPB）用于情感分析评估。  
- 回测：20个股票的金融数据，评估夏普比率。  
- 实验包括：批评家平台验证（bootstrap 95%置信区间）、SDI路由效果、SCD跨语言命中率、幻觉检测AUC=0.90。  
- 成本计算基于假设的用户量和API定价。

### 值得关注点
- 粒度分层多样性是核心机制，而非简单的多智能体投票。  
- SDI不仅用于路由，还可作为幻觉检测器和跨语言规范化工具，实现零边际成本的多语言支持。  
- “批评家平台”现象表明小模型（1.5B）在批评家角色中即可达到大模型的性能，极具成本效益。

### 局限性
- 提供的文本中未明确讨论局限性。  
- 可能包括：对具体数据集和模型设置的依赖；批评家平台是否适用于其他任务或领域尚无验证；SCD的缓存命中率可能在不同分布下变化；回测范围有限（20个股票）。

## 3. Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study

- Source: arxiv
- arXiv ID: 2607.20270
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.20270v1
- PDF: https://arxiv.org/pdf/2607.20270v1
- DOI: https://doi.org/10.48550/arXiv.2607.20270

### Authors

Andrei Chetvergov, Stepan Ukolov, Timofei Sivoraksha, Alexander Evseev, Mikhail Solovev, Valeriia Kuschenko, Maria Chistyakova, Sergey Bolovtsov

### Abstract

Large language models are increasingly evaluated through the values they endorse, but such evaluations presuppose that models can identify the value expressed in a concrete situation. We study this prerequisite as controlled top-1 recognition over Schwartz's ten basic values. Our evaluation set contains 1,000 Russian situational texts, balanced across the ten values and independently labeled by two human annotators per item. We evaluate 21 instruction-tuned LLM runs under a fixed ranked-response protocol; 20 runs with reliable outputs form the semantic panel. Pooled Acc@1 is 0.683 and Acc@3 is 0.892, showing that models often locate the correct motivational region while ranking close alternatives unstably. Adjacent values account for 50.9% of semantic errors, compared with 24.4% under a checkpoint-specific null. Eight directed confusions recur across checkpoints and human-confirmed subsets. Several are strongly asymmetric, including Universalism to Benevolence, Tradition to Conformity, and Security to Power, whereas Stimulation-Hedonism forms a bidirectional boundary. Their severity is checkpoint-specific and can bias higher-order value profiles. The results motivate value-recognition evaluation that combines exact accuracy, ranked recovery, and directed error analysis.

### 中文一句话结论
大型语言模型在识别Schwartz十种基本价值观时，平均准确率约为68.3%，但存在系统性、有方向的混淆模式（尤其是相邻价值观），且这些模式因模型而异，可能扭曲高阶价值观画像。

### English TL;DR
LLMs achieve ~68.3% top-1 accuracy in recognizing Schwartz's ten basic values from Russian situational texts, but systematically confuse adjacent values (50.9% of errors), with eight recurring directed confusions (e.g., Universalism→Benevolence, Security→Power) that vary by checkpoint and can bias higher-order value profiles.

### 中文详细总结
本研究考察了指令微调的大语言模型在识别Schwartz十种基本价值观时的表现。研究使用包含1000个俄语情境文本的平衡数据集，每个文本由两位独立标注员标注。评估了21个指令微调模型（20个可靠输出用于语义分析），结果显示：
- 池化Acc@1为0.683，Acc@3为0.892，表明模型通常能定位正确的动机区域，但排序相近备选时不稳定
- 50.9%的语义错误来自相邻价值观混淆（高于24.4%的基准线）
- 识别出8种跨模型复现的有向混淆，包括：Universalism→Benevolence、Tradition→Conformity、Security→Power等，而Stimulation-Hedonism为双向边界
- 这些混淆的严重程度因模型而异，可能影响高阶价值观画像（如将保护性行动误解为权力动机）

### 方法 / 贡献
1. **任务定义**：将主要价值观识别作为受控诊断任务，要求模型从情境文本中识别主导价值观
2. **数据集构建**：创建了1000个平衡俄语文本（每价值观100个），经两阶段标注：先由ValueLlama和GPT-4.1-mini一致标注，再由两位人类标注员独立验证（95%项目获至少一人支持）
3. **分析框架**：区分输出可靠性、精确识别和排名恢复；引入固定边界零假设（控制标签偏向）和跨模型一致性检验
4. **混淆分析**：识别8种系统性有向混淆，量化其对高阶价值观画像的扭曲效应

### 实验或数据
- **数据**：1000个俄语情境文本，平衡覆盖Schwartz十种基本价值观，每个文本有两个独立人类标注
- **模型**：21个指令微调LLM运行（20个可靠输出），在固定排名响应协议下评估
- **指标**：Acc@1=0.683，Acc@3=0.892，语义错误中50.9%来自相邻价值观
- **人机一致性**：95%项目至少一位人类标注员支持模型标签

### 值得关注点
1. 系统性混淆模式：8种跨模型复现的有向混淆（如Security→Power），暗示模型存在特定认知偏差
2. 混淆方向性：多为一方向性（如Universalism→Benevolence），而非双向混淆
3. 模型特异性：不同模型的混淆严重程度和模式各异，影响更高阶价值观评估
4. 实际影响：混淆可能扭曲基于价值观的推荐、路由、政策分析等应用

### 局限性
1. 仅关注俄语文本，结果可能不直接推广到其他语言或文化背景
2. 数据集限于特定来源（敏感话题、不当内容等），可能覆盖不足
3. 只评估了指令微调模型，未涵盖基础模型或其他训练范式
4. 人类标注一致性有限（仅95%获一人支持），反映价值观标注本身的主观性
5. 仅考察基本价值观识别，未涉及模型自身价值观偏好或行为

## 4. emb-diversity: A Tool for Embedding-Based Measurement of Data Diversity

- Source: arxiv
- arXiv ID: 2607.19848
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.19848v1
- PDF: https://arxiv.org/pdf/2607.19848v1
- DOI: https://doi.org/10.48550/arXiv.2607.19848

### Authors

Cantao Su, Menan Velayuthan, Esther Ploeger, Dong Nguyen, Anna Wegmann

### Abstract

There is growing evidence that data diversity is crucial for developing fair and robust NLP models. However, current approaches to measure diversity remain inconsistent and fragmented: While there exist a number of tools for measuring the lexical diversity of texts, researchers lack standardized tools for quantifying diversity based on embeddings. Embedding-based diversity measures are highly flexible: They work with any embedding model and any data that can be embedded, and are thus applicable to many notions of diversity. With emb-diversity, we provide a comprehensive embedding-based diversity measurement tool, spanning a broad range of measures. We demonstrate its potential for several use cases: measuring the stylistic, semantic, language and speaker diversity of datasets. https://github.com/nlpsoc/emb-diversity/

### 中文一句话结论
本文提出了 `emb-diversity`，一个基于嵌入的标准化的数据多样性测量工具，支持多种多样性度量，可灵活应用于文本的风格、语义、语言和说话者多样性等场景。

### English TL;DR
emb-diversity is a comprehensive Python tool that standardizes embedding-based measurement of data diversity, supporting a wide range of measures and applications to stylistic, semantic, language, and speaker diversity.

### 中文详细总结
论文指出，数据多样性对于构建公平稳健的 NLP 模型至关重要，但目前测量多样性的方法不一致且碎片化。虽然已有词级多样性工具，但缺乏基于嵌入的标准化工具。`emb-diversity` 填补了这一空白，它是一个全面的基于嵌入的多样性测量工具，支持 22 种已被文献提出的度量。工具通过 Python API 和命令行界面（CLI）两种接口，提供高灵活性：用户可指定多样性轴（如风格、语义）或直接选择嵌入模型；工具自动处理嵌入、缓存和度量计算。论文通过风格、语义、语言和说话者多样性四个案例展示了工具的潜力。代码以 MIT 许可证开源。

### 方法 / 贡献
- **方法**：工具基于嵌入向量计算多样性。用户输入文本或向量，系统通过统一接口调用嵌入模型（支持 SentenceTransformers/HuggingFace），然后对嵌入计算 22 种多样性度量（如平均成对距离、瑞利熵等）。工具包含缓存机制和优化（如并行计算）以提高可扩展性。
- **贡献**：（1）提供了首个社区维护的、全面的基于嵌入的多样性测量工具；（2）统一了 22 种度量接口，支持轻松扩展；（3）设计了 CLI 和 Python API 双接口，方便不同用户使用；（4）包含 511 个测试确保正确性。

### 实验或数据
论文未报告特定数据集或定量实验。工具通过四个案例（风格多样性、语义多样性、语言多样性、说话者多样性）演示功能，这些案例使用示例文本数据，但未提供详细实验结果或基准数据集。

### 值得关注点
- **灵活性**：可与任何嵌入模型和可嵌入数据（文本、图像、图等）配合工作。
- **易用性**：提供两种接口，无需从零编写代码。
- **全面性**：原生支持 22 种度量，覆盖主流嵌入多样性计算方法。
- **开源可扩展**：使用 MIT 许可证，易于添加新度量并集成到工作流。
- **高测试覆盖**：511 个测试保证计算正确性。

### 局限性
论文未明确讨论局限性。潜在局限包括：依赖所选嵌入模型的质量和偏差；22 种度量可能产生不一致结果；计算复杂度随数据量增加而上升（未被评估）；没有提供单一“最佳”度量，用户需自行选择。

## 5. On the Systematic Challenges of Culturally Loaded Machine Translation: Dream of the Red Chamber as the Cultural Lens

- Source: arxiv
- arXiv ID: 2607.20241
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.20241v1
- PDF: https://arxiv.org/pdf/2607.20241v1
- DOI: https://doi.org/10.48550/arXiv.2607.20241

### Authors

Yiming Wang, Jiayuan Di

### Abstract

Culturally loaded translation poses unique challenges for machine translation (MT), as meanings are deeply embedded in socio-cultural contexts beyond surface linguistic forms. Although large language models (LLMs) have enabled MT systems to achieve human-like quality in many scenarios, their ability to handle culturally loaded expressions remains underexplored. In this study, we systematically investigate the challenges posed by culturally loaded translation in LLM-based MT systems. We construct a Chinese-Japanese bilingual dataset from the culturally representative corpus Dream of the Red Chamber, containing 500 segments across diverse cultural categories. Using a comprehensive evaluation protocol, we reveal three main challenges: (1) task challenges, where frontier LLMs exhibit notable performance gaps and struggle with culturally loaded content; (2) human evaluation challenges, where evaluator backgrounds lead to substantial disagreement in translation judgments; and (3) automatic evaluation challenges, where widely used metrics fail to reliably assess translation quality for this task. These findings may offer valuable insights for culture-oriented translation research in both computational science and linguistics.

### 中文一句话结论
本研究以《红楼梦》构建中-日双语数据集，系统揭示了大语言模型在文化负载词翻译中的任务困难、人工评估分歧及自动评估不可靠三大挑战。

### English TL;DR
This paper systematically investigates the challenges of culturally loaded machine translation using a Chinese-Japanese dataset from *Dream of the Red Chamber*, revealing that frontier LLMs underperform on such content, human evaluators disagree based on background, and standard automatic metrics are unreliable.

### 中文详细总结
本研究系统考察了大语言模型（LLM）在文化负载词翻译中的挑战。以《红楼梦》（中文-日文）为文化透镜，构建包含500个文化负载片段的双语数据集，涵盖生态、宗教、物质、语言、社会五类文化范畴。通过综合评估方案（含人工评估和自动指标），揭示三大核心挑战：
1. **任务困难**：前沿LLM在文化负载翻译上表现显著不足，不同模型间差异大，且文化类别敏感性高。
2. **人工评估分歧**：评估者背景（母语文化环境、专业知识）导致翻译判断显著不一致，可能引入系统性偏差。
3. **自动评估不可靠**：主流自动指标（如BLEU等）无法可靠捕捉模型排名，完全无法区分样本级质量差异。
此外，研究还进行了错误分析和翻译策略分析，以理解模型行为模式与瓶颈。这些发现为文化和计算语言学领域提供了重要洞见。

### 方法 / 贡献
- **数据集构建**：从《红楼梦》中日双语版（伊藤漱平译）中选取500个文化负载片段，按Nida五类文化范畴标注。
- **评估方案**：结合人工评估（多背景评估者）和自动指标（如BLEU），系统对比LLM（如GPT-4等前沿模型）与人类参考翻译质量。
- **核心贡献**：首次系统揭示LLM在文化负载翻译中的任务、人工评估和自动评估三大挑战。

### 实验或数据
- 数据集：500个中-日文化负载片段，覆盖生态、宗教、物质、语言、社会五类，源语言平均长度15–32字，目标语言32–64字。
- 实验：评估了多个前沿LLM（具体模型未在摘要中列出），并以人类翻译为黄金标准进行对比。
- 关键结果：LLM在文化负载翻译上表现不佳；人工评估受背景影响；自动指标失效。

### 值得关注点
- 强调文化负载翻译的根本难点：意义植根于社会文化语境，超越表层语言对应。
- 揭示评估中的双重困境：人工评估因文化背景分歧而主观性高，自动指标则完全失效。
- 指出中-日文化距离适中（共享汉字与部分文化意象），为研究文化加载翻译提供了独特视角。

### 局限性
- 数据仅基于《红楼梦》单一文本，文化类别覆盖可能不完备。
- 目标语言仅限于日语，对其他语言（如中西语言对）的泛化性未验证。
- 未提供具体LLM名称及性能差异的详细分析。
- 自动评估失效的深层原因未充分探讨。

## 6. Understanding the Impact of Linguistic Realization Choices on LLM Stance with Causal Tracing

- Source: arxiv
- arXiv ID: 2607.20115
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.20115v1
- PDF: https://arxiv.org/pdf/2607.20115v1
- DOI: https://doi.org/10.48550/arXiv.2607.20115

### Authors

Langchen Huang, Sebastian Padó, Franziska Weeber

### Abstract

Large language models (LLMs) are known to be sensitive to prompt and input formulations. However, existing studies have focused on lexical realization and largely ignored constructional choice. This paper studies whether linguistic construction can systematically shift LLM decisions and where these shifts can be causally localized inside the model. We use political stance judgment as a meaning-sensitive case study and extend an English political statements dataset, resulting in six controlled linguistic rewrite types that preserve or invert the meaning of a statement. Experiments on four open-weight models show that stance instability affect both meaning-preserving and meaning-inversing rewrites. Because output shifts reveal that rewrites affect stance, but not where in the model, we apply activation patching, where activations from the original statement are substituted into the forward pass for the rewritten statement and measure which components recover the original stance distribution. The results show that mid-to-late decoder layers, especially block outputs at the final prompt position, provide the strongest restoration signal.

### 中文一句话结论
本研究通过激活修补因果定位发现，语言结构选择（如主动/被动态、分裂句等）能系统性地改变LLM的政治立场判断，且这些变化主要源于解码器中后期层（尤其是最终提示位置的模块输出）。

### English TL;DR
This paper investigates how linguistic construction choices (e.g., active/passive, clefts) systematically shift LLM political stance judgments and uses activation patching to causally locate these shifts in mid-to-late decoder layers, particularly at the final prompt position.

### 中文详细总结
论文以政治立场判断为语义敏感任务，扩展了ProbVAA英文数据集，引入六种受控语言改写（四种意义保持：主动/被动、it-cleft、wh-cleft、支撑动词结构；两种意义反转：显式否定、语义对立）。在四个开源模型（Gemma-3-4B/12B-IT, Qwen3-4B/14B）上实验发现：意义保持和意义反转的改写均会引起立场不稳定。为定位内部因果机制，作者采用激活修补（activation patching），将原始陈述的激活替换到改写版本的推理中，测量哪些组件能恢复原始立场分布。结果显示，解码器的中后期层（尤其是最终提示位置的模块输出）提供了最强的恢复信号，是立场偏移的关键因果位点。

### 方法 / 贡献
1. **数据集扩展**：在ProbVAA基础上新增四种意义保持的语言学改写变体（主动/被动、it-cleft、wh-cleft、支撑动词结构），共六种受控改写类型。
2. **行为分析框架**：通过翻转率、Wasserstein距离和方差分解（区分意图敏感性、表达敏感性、模型不确定性）量化改写对立场的影响。
3. **因果溯源**：运用激活修补对三个激活位点（解码器层输出、注意力子层输出、MLP子层输出）进行干预，定位到中后期层及最终提示位置为关键恢复位点。

### 实验或数据
- **模型**：Gemma-3-4B-IT、Gemma-3-12B-IT、Qwen3-4B、Qwen3-14B（开源，4B-14B参数量）。
- **数据**：扩展后的ProbVAA英文数据集（239条政策陈述），每条原始陈述对应最多六种改写变体（实际有效数量因改写类型而异，如被动仅194条、SVC 122条）。
- **实验设置**：每个提示采样30次（温度0.8），输出7点Likert评分（1-7）。激活修补中仅干预最终提示位置的隐藏状态，使用1-Wasserstein距离和归一化恢复分数评估。

### 值得关注点
- 首次系统研究**语言结构选择**（而非仅词汇改写）对LLM立场的影响，并区分意义保持与意义反转两种情形。
- 结合方差分解将立场变异拆分为意图、表达和噪声三部分，明确表达敏感性（articulation sensitivity）的独立贡献。
- 通过激活修补实现从行为观察到**因果机制**的跨越，精确定位到解码器中后期（而非早期）层及最终提示位置，为后续鲁棒性改进提供靶点。

### 局限性
- 仅基于**英语政治陈述**（ProbVAA数据集），结果可能不直接泛化到其他语言、领域或任务（如情感、伦理判断）。
- 模型规模限于4B-14B，更大或更小模型的结构敏感性可能不同。
- 激活修补只考察了**最终提示位置**，未覆盖其他token位置可能存在的因果贡献。
- 意义保持改写（如被动、分裂句）的生成依赖小模型（Qwen3-8B）辅助，可能引入额外偏差，且部分语句无法生成有效变体（如被动、SVC缺失）。
- 研究未涉及指令微调或人格提示对结构敏感性的交互影响。

## 7. Exposure is Optional: Learning Unlike Coordination in Language Models

- Source: arxiv
- arXiv ID: 2607.20251
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.20251v1
- PDF: https://arxiv.org/pdf/2607.20251v1
- DOI: https://doi.org/10.48550/arXiv.2607.20251

### Authors

Jiamu Luo, Shane Steinert-Threlkeld

### Abstract

Coordination, a fundamental linguistic structure, remains a subject of intense debate, and its exact nature continues to elude theoretical linguistics. A common view holds that only same-category constituents can be conjoined, which has been challenged by the many grammatical unlike coordinations found in natural language. Treating language models as a computational testbed, we investigate whether the acquisition of unlike coordination requires direct exposure in the training data, or whether it can emerge organically from general compositional abilities. Using Filtered-Corpus Training (FiCT), we train GPT-2 models on corpora from which all instances of unlike coordination have been removed. We find that direct exposure is not necessary: models trained on filtered data successfully generalize to unlike coordination, achieving perplexity and grammaticality judgments comparable to models trained on unfiltered text. Furthermore, our analyses of internal representations indicate that language models process unlike coordination by treating the conjoined elements as belonging to similar structural categories or through a mechanism akin to deletion, both of which appear learnable from exposure to alike coordination alone. This work contributes to the growing understanding of how language models internally represent linguistic structures, while also adding to the broader debate on coordination by showing how models generalize and process unlike coordination without direct exposure.

### 中文一句话结论
语言模型无需在训练数据中直接接触"非同类别并列"结构，仅通过学习"同类并列"即可自发掌握该能力。

### English TL;DR
Language models can generalize to unlike coordination without direct exposure, relying on general compositional abilities learned from alike coordination.

### 中文详细总结
本研究探讨语言模型能否在没有直接训练数据接触的情况下习得"非同类别并列"（unlike coordination，如NP+CP并列）。作者使用Filtered-Corpus Training (FiCT)方法，从训练语料中系统移除所有非同类别并列实例，训练GPT-2模型。结果显示，直接暴露并非必要条件：在过滤数据上训练的模型与在未过滤数据上训练的模型在困惑度（perplexity）和语法判断任务上表现相当。进一步的内部分析表明，模型处理非同类别并列时采用两种机制：将并列元素视为共享"超级类别"（supercategory），或通过类似删除（deletion）的处理方式。两种机制均可从同类并列的学习中习得。

### 方法 / 贡献
- **方法**：采用Filtered-Corpus Training (FiCT) 方法，构建三个训练语料：原始语料（未过滤）、过滤所有非同类别并列的语料（filtered-all）、过滤仅由and连接的非同类别并列的语料（filtered-and）。(删除使用基于Berkeley Neural Parser的自动过滤)
- **贡献**：首次系统地证明语言模型无需直接暴露即可习得非同类别并列，并从内部分析揭示两种处理机制，为理论语言学中关于并列结构的争论提供计算验证。

### 实验或数据
- **训练数据**：基于Gulordava等人发布的英文语料，共1,948,104个句子。
- **模型**：基于GPT-2框架，配置接近GPT-2 Large（1024上下文长度，1280嵌入维度，36层，20头）。
- **评估**：
  - 手工构建五个评估语料库：unlike（100个非同类别并列句子）、alike-from-unlike（对应的同类并列变体）、supercat-deletion（可解释为超级类别或删除）、deletion（只能解释为删除）、unlike-judgment（22对语法判断测试）。
  - 指标：困惑度（perplexity）、平均惊喜度（average surprisal，用于语法判断）、平均注意力分数（average attention score）。
  - 结果：过滤数据训练的模型在困惑度和语法判断上均与未过滤数据训练的模型相当。

### 值得关注点
- 在过滤最严格的filtered-all条件下，模型仍能泛化到非同类别并列，这挑战了"直接暴露是必要条件"的传统观点。
- 内部表征分析揭示了两种可能机制（超级类别与删除），且均能从同类并列学习中习得。
- 研究将计算模型的内部行为与理论语言学中的"并列同类定律"（Law of Coordination of Likes）争论直接关联。

### 局限性
- 过滤过程可能误删部分同类并列实例（约17%），但作者认为高精度过滤反而更有利。
- 过滤基于自动句法分析器，存在少量解析错误（100个句子中误留1个）。
- 实验结果基于单一语言（英语）和GPT-2架构，通用性有待验证。
- 所提出的两种处理机制（超级类别和删除）仅通过注意力分析推断，缺乏更直接的因果验证。

## 8. surprisal is Not a Theory

- Source: arxiv
- arXiv ID: 2607.20208
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.20208v1
- PDF: https://arxiv.org/pdf/2607.20208v1
- DOI: https://doi.org/10.48550/arXiv.2607.20208

### Authors

Andrés Buxó-Lugo, Aniello De Santo, Morgan Grobol, Ryan J. Hubbard, Cassandra L. Jacobs

### Abstract

Surprisal Theory is often characterized as a computational-level explanation per (Marr, 1982). We argue in this work that, even though a computational level narrative has been used to support "representation-agnostic research" within computational psycholinguistics, the movement toward black box systems embodied by large language models (LLMs) does not exempt modelers using the surprisal metric from the representational decisions required by computational-level characterizations. In fact, we argue that the uncritical use of LLM-surprisal obfuscates the representational and algorithmic-level commitments of different models. In three analyses, we show that the choice of algorithm and model architecture play significant roles in the computation of language model probabilities. We advise that researchers who wish to test Surprisal Theory re-evaluate the practice of treating large language model probabilities as interchangeable

### 中文一句话结论
本文论证了基于大语言模型的 surprisal 指标并不能作为独立于表征的计算层级理论，其使用掩盖了模型间的算法与表征差异。

### English TL;DR
The paper argues that surprisal, as commonly operationalized through large language models, is not a valid computational-level theory of sentence processing because it obscures critical representational and algorithmic commitments, and researchers must move beyond treating LLM probabilities as interchangeable.

### 中文详细总结
本文挑战了计算心理语言学中的一个普遍假设：即通过大语言模型（LLMs）计算的 surprisal 值可作为“表征无关”（representation-agnostic）的计算层级理论（Marr, 1982）。作者指出，尽管此前有研究者声称 LLM 提供的概率估计不需要显式处理句法/语义表征，但实际上不同模型在架构（编码器 vs. 解码器）、训练目标（掩码语言模型 vs. 自回归预测）以及权重绑定（如 GPT-2 的 tied embeddings）等方面的差异，会显著影响概率的计算方式。作者通过三个实验分析表明，不同 LLM 在其隐藏层中对词汇预测的编码方式截然不同，且与人类 cloze 概率的匹配关系仅在局部层面成立。因此，简单地将不同模型的 surprisal 视为可互换，会模糊 Surprisal 理论所需的核心理论承诺。作者呼吁研究者重新审视“表征无关”假设，并回到对算法与表征层级的明确建模。

### 方法 / 贡献
- **理论贡献**：从 Marr 的计算层级理论出发，系统批评了将 LLM 的 surprisal 视为“表征无关”计算层级解释的做法。
- **方法学贡献**：指出当前研究过度依赖“拟合-预测”（PP）范式，忽略了潜藏的算法与表征差异。作者强调，不同模型（如 Pythia、GPT-2、RoBERTa）尽管在宏观相关性上表现相似，但内部的表征演化路径截然不同。
- **实验方法**：使用“logit lens”技术探查不同模型各层的概率分布，并与人类 cloze 概率进行分层比较（研究 1.1 与 1.2）。分析了高概率与低概率预测情况下的模型行为差异。

### 实验或数据
实验数据来自 Peelle (2020) 的 cloze 规范语料（3085 个句子，约 52000 个独特完形回答）。使用三个模型：
- **Pythia-160M**（解码器，未采用 tied embeddings）
- **GPT-2 small**（解码器，tied embeddings）
- **RoBERTa base**（编码器，掩码语言模型）

对模型各层的 hidden state 与 logits 进行分层探测，并与人类 cloze 概率进行相关性分析。结果显示：
- 不同模型在低层/高层对词汇预测的编码策略差异较大；
- 高人类 cloze 概率词更容易获得模型间一致的高概率，但低概率词的预测行为在不同模型间差异显著。

### 值得关注点
- 明确批判了“表征无关性”（representation-agnosticism）这一在计算心理语言学中流行的假设。
- 揭示了“black box”LLM 的使用如何掩盖了算法级和表征级的理论承诺，从而削弱了 Surprisal 理论的解释力。
- 提出了 Marr 三层分析框架（计算层、算法层、实现层）在评估神经语言模型中的相关性。
- 附有 OSF 项目页面，提供分析数据与可视化脚本。

### 局限性
- 实验仅基于三种中等规模的 Transformer 模型（GPT-2 small、Pythia-160M、RoBERTa base），未能覆盖更大规模或更新架构的 LLM（如 LLaMA、Gemini）。
- 仅分析了词级别（对句子判定的下一个词）的 surprisal，未涵盖跨句子或篇章层级的处理难度。
- cloze 数据仅来自英语，可能存在语言特异性偏倚。
- 未直接提供替代办法或系统化的理论框架来“修复”Surprisal 理论，而主要以批评与呼吁为主。

## 9. Reinforcement Learning for Large Language Model Selective Evidence Adoption from Contaminated Retrieval Results

- Source: arxiv
- arXiv ID: 2607.20090
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.20090v1
- PDF: https://arxiv.org/pdf/2607.20090v1
- DOI: https://doi.org/10.48550/arXiv.2607.20090

### Authors

Yanyu Chen, Yue Li, Yongyi Cui, Dongsheng Shi, Lichang Dai

### Abstract

Retrieval-augmented large language models frequently face contexts that interleave useful evidence with misleading statements or instruction-like content. Blanket refusal discards valid evidence, whereas uncritical adoption yields incorrect or unsafe answers. The ability to selectively adopt relevant information while rejecting deceptive or harmful content is therefore critical for reliable deployment in real-world retrieval settings. We introduce SelectBench, a controlled benchmark and training set for selective evidence adoption, and post-train Qwen3.5-4B directly with DAPO using either deterministic rule rewards or a frozen semantic judge. On the corrected 325-example SelectBench-v2 test set, strict success rises from 22.46% for the original checkpoint to 25.54% with DAPO-Rule and 26.46% with DAPO-DeepSeek. Both trained policies reduce forbidden-content adoption and produce shorter, more focused responses, yet prompt-injection following does not improve. The paired gains are modest and fail to survive Holm correction, suggesting that stronger reward shaping or additional training iterations may be needed for more robust gains. DAPO-DeepSeek exhibits no material degradation on MMLU or clean HotpotQA, indicating that the post-training procedure preserves general capabilities. These results demonstrate a directional improvement in selective evidence use, while identifying injection resistance and statistical robustness as important remaining challenges for future work.

### 中文一句话结论
本文提出并验证了通过DAPO强化学习对Qwen3.5-4B进行后训练，能在SelectBench-v2上小幅提升选择性证据采纳能力，但提升在统计上不显著。

### English TL;DR
This paper uses DAPO reinforcement learning to post-train Qwen3.5-4B for selective evidence adoption from contaminated retrieval results, achieving modest but statistically insignificant gains on the SelectBench-v2 benchmark.

### 中文详细总结
检索增强的大语言模型常常面临上下文混杂有用证据、误导性陈述或类指令内容。现有策略要么全盘拒绝（丢失有效证据），要么全盘接受（导致错误或有害答案）。为此，本文提出控制基准SelectBench及其训练集，并对Qwen3.5-4B使用DAPO进行后训练，奖励函数采用确定性规则或冻结语义评判器。在修正后的SelectBench-v2测试集（325例）上，严格成功率从原始检查点的22.46%提升至DAPO-Rule的25.54%和DAPO-DeepSeek的26.46%。两种策略均减少了禁止内容采纳，生成了更短、更聚焦的响应，但提示注入遵循未见改善。DAPO-DeepSeek在MMLU和干净HotpotQA上未出现明显退化，表明通用能力保持。

### 方法 / 贡献
- 引入SelectBench，一个专为选择性证据采纳设计的受控基准和训练集。
- 使用DAPO（一种强化学习算法）直接对Qwen3.5-4B进行后训练，奖励信号来自确定性规则或冻结的语义评判器（DeepSeek）。
- 验证了通过RL后训练能定向改善模型在有污染检索结果中采纳有用证据并拒绝有害内容的能力，同时不损害通用性能。

### 实验或数据
- 测试集：修正后的SelectBench-v2，包含325个例子。
- 评估指标：严格成功率（strict success），并测量禁止内容采纳、响应长度、提示注入遵循。
- 通用能力评估：MMLU和干净HotpotQA（未污染版本）。
- 结果：严格成功率从22.46%（基线）升至25.54%（DAPO-Rule）和26.46%（DAPO-DeepSeek），但配对增益经Holm校正后不显著。

### 值得关注点
- 首次在受控基准上量化大语言模型选择性采纳证据的能力，并利用RL进行后训练改善。
- 两种RL变体均减少了有害/禁止内容的采纳，并生成了更简洁的响应。
- 通用能力（MMLU、HotpotQA）未因训练而退化，显示方法的无害性。
- 提示注入遵循未见改善，说明抗注入仍是开放挑战。

### 局限性
- 改进幅度较小且未通过统计显著性检验（Holm校正），表明当前奖励塑造或训练迭代可能不足。
- 提示注入遵循能力没有提升，模型仍可能被误导性指令影响。
- 仅对单个模型（Qwen3.5-4B）进行测试，泛化性未知。
- 基准规模较小（325例），可能限制统计效力。

## 10. Gotta Catch them all: the modes of Sycophancy

- Source: arxiv
- arXiv ID: 2607.20146
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.20146v1
- PDF: https://arxiv.org/pdf/2607.20146v1
- DOI: https://doi.org/10.48550/arXiv.2607.20146

### Authors

Shreyans Jain, Alexandra Yost, Amirali Abdullah

### Abstract

Large language models often align with users' beliefs at the expense of factual accuracy, a behavior known as sycophancy. Prior mechanistic studies largely treat sycophancy as a single behavioral dimension that can be uniformly amplified or suppressed. We challenge this assumption by analyzing three hypothesized modes of sycophancy across 948 social pressure situations. Although the modes produce highly similar outputs, with a text-only classifier achieving just 57.8 percent accuracy, their internal representations are perfectly linearly separable from layer 14 onward. We further find the modes emerge at different processing stages, rely on distinct attention circuitry, and fire strongest on different inputs. These results show that sycophancy is not a monolithic tendency, but a structured family of representationally and computationally distinct modes, motivating more precise measurement and intervention.

### 中文一句话结论
本文通过分析三种假设的奉承模式，证明大语言模型中的奉承行为并非单一倾向，而是一组在内部表征和计算机制上结构化的不同模式。

### English TL;DR
LLM sycophancy is not a single monolithic tendency but a structured family of representationally and computationally distinct modes that are linearly separable in internal representations and driven by different mechanisms.

### 中文详细总结
大型语言模型常常会为了迎合用户的信念而牺牲事实准确性，这种行为被称为奉承。先前的研究通常将奉承视为一个单一的行为维度，可以被统一增强或抑制。本文挑战了这一假设，通过948个社会压力情境分析了三种假设的奉承模式：被动亲和型、战略谄媚型和防御性冲突回避型。尽管这些模式产生高度相似的输出（纯文本分类器准确率仅为57.8%），但从第14层开始，它们的内部表征在线性层面上完全可分。研究发现，这些模式出现在不同的处理阶段，依赖不同的注意力回路，并在不同输入上表现最强，表明奉承不是一个单一倾向，而是一组在表征和计算上不同的结构化模式。

### 方法 / 贡献
1. **三种奉承模式定义**：基于HEXACO人格理论定义三种模式——被动亲和型（追求和谐）、战略谄媚型（寻求社会奖励）、防御性冲突回避型（避免冲突风险）。
2. **数据集构建**：收集约948个社会压力情境，每个情境配以四种角色条件（PA、SI、DCA和中性基线），共约4000个提示。
3. **偏差向量分析**：通过减去基线激活来隔离情境内容，提取每种奉承模式的独特表征。
4. **六层分析流水线**：涵盖行为验证、聚类分析、几何验证、输出空间分析、注意力头分析和对数透镜分析。
5. **主要发现**：奉承模式在残差流中线性可分（F1），处理分三个阶段展开（F2），存在表征冗余（F3），注意力头大部分共享（F4），内部表征与外部行为存在不匹配（F5），计算路径依赖社会情境（F6）。

### 实验或数据
- 使用了约948个社会压力情境，涵盖8种情境类型，每种情境在4种角色条件下评估。
- 模型为Gemma-2，从中间到后期层（14-34层）提取激活，主分析层为第18层（表征分析）和第22层（因果重要性分析）。
- 使用K-means聚类（调整兰德指数=1.000，完全分离）、线性探针（100%准确率）和GPT-4o-mini及Claude Sonnet 4.6作为LLM评判评估输出行为。
- 文本分类器准确率仅为57.8%，但内部表征线性可分性达96.7%。

### 值得关注点
1. **奉承并非单一行为**：发现三种模式即使输出相似，其内部表征和计算机制完全不同，挑战了先前将奉承视为统一维度的假设。
2. **三阶段处理过程**：表征编码（第18层）→因果计算（第22-26层）→行为输出（第32-33层），单层分析不足以完整表征。
3. **注意力头共享与专门化**：三个模式共享主要注意力回路，只有PA模式招募了专门的注意力头，SI和DCA通过共同枢纽计算。

### 局限性
- 本文未明确提及实验或数据集的具体规模细节，如训练/测试分割、评估指标的全部定义等。
- 三种模式定义基于假设的HEXACO人格剖面，作者承认这不是心理学中的既定分类。
- 研究仅基于Gemma-2模型，结论可能不泛化到其他架构。
- 模式诱导依赖于角色提示，尽管有消融实验表明线性可分性不是提示伪影。
- 行为输出高度相似，意味着纯文本层面区分模式的能力有限，实际应用的干预可操作性需进一步验证。

## Processing Notes

- Duplicate papers skipped: 0