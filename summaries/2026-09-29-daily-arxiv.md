# Daily arXiv - 2026-09-29

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-29T02:08:27
- Paper count: 10

## 1. Same Text, Different Numbers: The Divergence of LLM-Based Measures

- Source: arxiv
- arXiv ID: 2609.31013
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.31013v1
- PDF: https://arxiv.org/pdf/2609.31013v1
- DOI: https://doi.org/10.48550/arXiv.2609.31013

### Authors

Hamid Boustanifar, Sasan Mansouri

### Abstract

Researchers increasingly use generative large language models (LLMs) to convert corporate text into empirical variables. We examine the extent to which LLM-based textual measures are invariant to model choice using thirteen measures, including sentiment, management clarity, uncertainty, answer specificity, and climate and political risk. Seven LLMs from different providers score earnings call transcripts of S&P 500 companies on these constructs. Cross-model rank correlations average only 0.52, and transcript-level differences common across providers account for only 34% of total score variation. Cross-model disagreement does not predict subsequent analyst or market disagreement, consistent with a substantial model-specific component rather than common ambiguity in the underlying disclosure. Model choice significantly affects downstream inference, with coefficient magnitudes, signs, and statistical significance varying substantially across models. Averaging across providers makes transcript rankings more stable for most constructs, but score levels remain sensitive to the models included in the ensemble. LLM-generated variables should therefore be treated as model-contingent measurements and validated across providers.

### 中文一句话结论  
不同LLM对同一文本生成的测量结果差异显著，模型选择会实质性地影响下游推断，因此LLM生成的变量应视为“依模型而定”的测量，需跨模型验证。

### English TL;DR  
LLM-based textual measures diverge substantially across providers: mean pairwise rank correlation is only 0.52, and model choice changes coefficient signs, magnitudes, and significance. Averaging across models improves ranking stability for most constructs but not absolute score levels, so these measures are model-contingent and must be validated across providers.

### 中文详细总结  
该研究系统考察了生成式大语言模型（LLM）在将公司文本转化为实证变量时，测量结果是否受模型选择影响。作者使用七家不同提供方的LLM（OpenAI、Anthropic、Google、Meta、Mistral、DeepSeek、阿里巴巴）对2024年标普500公司财报电话会议问答部分共1946份文本进行评分，覆盖情绪、不确定性、管理层清晰度、气候风险、政治风险、回答具体性、企业文化及五个子维度等13项测度（含一项基于规则的具体性实现）。  
结果显示跨模型分歧很大：平均成对秩相关仅0.52；按文本的公共变异仅占总变异的34.4%；同一文本上不同模型评分的标准差平均为总体标准差的0.75倍。进一步分析表明，跨模型分歧不随模型自报置信度升高而消失；即便给出明确规则的基于规则具体性测度，模型间分歧也未减少。模型分歧与分析师预测分歧、市场波动等结果无显著关联，说明该分歧并非源于底层披露的共性模糊性，而更可能来自模型自身的系统性差异。  
模型选择对下游推断影响显著：在某些测度（如情绪、不确定性）上回归系数的正负号和显著性相对稳定，但幅度差异最高可达60%；其他测度则可能改变符号和显著性。将七家模型结果平均可提升相对排名的可靠性（13项测度中有10项达到0.80的基准），但绝对分值稳定性仅有5项达标。与词典等传统测度的相关最高约0.55（企业文化、创新、具体性），政治风险与情绪仅约0.3。更新一代的前沿模型能缩小但无法消除分歧。

### 方法 / 贡献  
- 方法：对同一组财报电话会议文本，使用七家主流的专有或开放权重LLM，采用完全相同的构建定义、评分量表和输出指令，要求输出分数、置信度及书面理由；结合方差成分分析、可靠性/依存性分析（基于概化理论）和下游推断对比。  
- 贡献：第一，系统量化了LLM测量对模型选择的敏感性，证明其不可互换性。第二，分离了“构念本身模糊”与“模型实现差异”，表明即便显式规则也不能保证跨模型一致。第三，证明跨模型分歧不代理市场或分析师的共同认知不确定性。第四，评估了多模型集成对相对排名和绝对水平的改进程度，并建议将LLM测度视为依赖模型的工具，需进行跨提供方验证。

### 实验或数据  
- 数据：2024年标普500公司1946场财报电话会议问答部分文本；七家提供方的LLM（OpenAI、Anthropic、Google、Meta、Mistral、DeepSeek、阿里巴巴）。  
- 测度：情绪、不确定性、管理层清晰度、气候风险、政治风险、回答具体性、企业文化及其5个子维度，外加一项基于规则的具体性实现，共13项测度。  
- 关键结果：跨模型平均秩相关0.52；共同文本变异占比34.4%；文本内跨模型标准差为总体标准差的0.75倍。情感相关性最高（均值可能接近0.7或更高，摘要未给具体值），基于规则的具体性最低（0.23）。下游推断中，情绪和不确定性系数幅值变化可超60%。集成后相对可靠性达标10/13，绝对可靠性达标5/13。

### 值得关注点  
- 分歧程度依构念不同而高度异质：有的测度（如情绪）数值上高度一致，但模型书写的理由语义相似度仍低（约0.69）。  
- 跨模型分歧不能由提示词模糊性解释——即使将评分规则明确化，分歧反而更大。  
- LLM分歧与分析师/市场分歧无显著相关，表明其更可能反映模型特定成分而非底层文本的模糊性。  
- 模型选择不影响结论的例子也存在（如情绪、不确定性的符号和显著性稳定），但幅度变化不可忽略；某些测度甚至改变符号。  
- 平均多家模型能显著提升相对排名稳定性，但对绝对分数水平帮助有限——这对构造面板或截面对比的研究有直接警示。

### 局限性  
- 研究仅聚焦2024年标普500公司财报电话会议问答部分，样本与时间范围有限，无法确认结论是否适用于其他文本类型、期间或市场。  
- 仅测试七家当前可用模型，且测度限定为会计与金融文献中常见的12个构念，不排除其他测度或未来模型表现更一致。  
- 本文将传统词典测度视为替代操作化而非金标准，也不将任何单一LLM视为正确——因此只证明“不可互换”，未判断哪个模型或测度在效度上更优。  
- 跨模型分歧与市场分歧无关联这一结论基于聚合检验，统计功效或非线性关系未完全排除，作者也未在摘要中报告额外稳健性说明。

## 2. LocUS: Head Selection and Subspace Projection for Targeted Activation Steering

- Source: arxiv
- arXiv ID: 2609.31122
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.31122v1
- PDF: https://arxiv.org/pdf/2609.31122v1
- DOI: https://doi.org/10.48550/arXiv.2609.31122

### Authors

Irene Tallini, Lorenzo Basile, Valentino Maiorca, Francesco Locatello, Alberto Cazzaniga

### Abstract

Activation steering is a powerful training-free paradigm for controlling large language models at inference time. However, standard approaches estimate a per-layer steering direction from contrastive data and apply it on the layer's entire representation space, which may couple the intervention to off-target properties present in the contrastive data and degrade unrelated capabilities. To mitigate this issue, we introduce LocUS (Localized Unembedding Steering), a method which grounds activation steering to the model's own output vocabulary subspace. By identifying a property-specific linear subspace within the unembedding matrix, LocUS enforces a geometric constraint that restricts the steering transformation to a specific subspace and at the same time localizes its application to a sparse subset of attention heads. Extensive evaluations across three model families on toxicity mitigation, sentiment redirection and sycophancy suppression show that LocUS matches or outperforms state-of-the-art baselines while intervening on under 6% of parameters and better preserving general capability.

### 中文一句话结论  
LocUS 通过将激活引导限制在与目标属性对齐的词表子空间内，并只在少量注意力头上进行干预，从而在保持甚至提升任务效果的同时，显著减少对模型无关能力的负面影响。

### English TL;DR  
LocUS is a training-free activation steering method that projects steering vectors onto property-specific subspaces of the unembedding matrix and applies them only to a sparse subset of attention heads, matching or outperforming baselines on toxicity, sentiment, and sycophancy tasks while intervening on under 6% of parameters and better preserving general capabilities.

### 中文详细总结  
激活引导（activation steering）是一种无需训练的推理时控制大模型行为的方法。传统方法通常从对比数据中估计逐层引导方向，并在整个表示空间上施加干预，因此容易引入对比数据中的非目标相关性，损害模型的通用能力。LocUS 提出将引导干预“定位”到模型自身的输出词表子空间：先通过属性相关词元定义词表子空间，再据此自动选择与属性对齐的注意力头，并在这些头内部把引导向量投影到该属性子空间上。这样既确定了干预的空间位置（少量注意力头），也限制了干预的表示子空间，从而减少对无关能力的影响。在毒性缓解、情感重定向和谄媚抑制等任务上的评估显示，LocUS 能在干预参数占比低于 6% 的情况下，达到或超过现有基线，并更好地保持模型通用能力。

### 方法 / 贡献  
- 提出自动化的注意力头选择流程：通过衡量注意力头输出与属性相关词元子空间的对齐程度，选出与目标属性最相关的头。  
- 提出子空间投影引导向量：将引导向量限制在每个头内部的属性词表子空间上，避免注入与目标无关的扰动方向。  
- 利用 SOMP（同步正交匹配追踪）在多个样本上共享原子集，稳定地选择属性和词元。  
- 贡献包括：自动头部选择、子空间定位的引导方法，以及在多种模型和任务上的实证评估。

### 实验或数据  
摘要提到在三个模型族上进行了评估，覆盖毒性缓解、情感重定向和谄媚抑制任务，并报告 LocUS 在干预少于 6% 参数的情况下匹配或超越基线，同时更好保持通用能力。摘要未给出具体数据集名称或详细数据统计，因此本回答不额外补充未提供的数据细节。

### 值得关注点  
- 训练免费，适合推理时动态控制。  
- 同时实现“头级别”和“子空间级别”的精细干预，比单层或全层引导更具解释性。  
- 属性词元集合可由用户定义或自动生成，为引导过程提供了新的可解释性控制手段。  
- 干预参数占比极低（<6%），表明方法具有较高参数效率。

### 局限性  
摘要和可见内容未明确讨论方法局限性。根据方法设计，LocUS 需要预先定义或生成属性相关词元集合，并使用校准数据估计子空间和选择头；这些步骤可能依赖外部词表或数据质量。详细的失败案例、计算开销以及对不同模型规模的泛化能力评估，原文摘要中未提供。

## 3. From annotation to reasoning: Culture in language models

- Source: arxiv
- arXiv ID: 2609.30897
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.30897v1
- PDF: https://arxiv.org/pdf/2609.30897v1
- DOI: https://doi.org/10.48550/arXiv.2609.30897

### Authors

Daniel Hershcovich, Alexander Conroy, Jens Bjerring-Hansen

### Abstract

How should we evaluate language models when more than one interpretation can be right? Cultural benchmarks often test factual knowledge, agreement with survey responses, or recognition of a predefined meaning. These tasks leave open whether a model can explain how a cultural reference works in a particular text, support a reading with evidence, or revise it after criticism. This is a question of interpretive depth, complementary to the breadth of cultural coverage. We argue that literary interpretation offers a useful setting for studying these capabilities. We focus on cultural referencing and reuse: how texts invoke, repeat, and transform earlier expressions across historical and linguistic contexts. Our central claim is that literary scholars can disagree about an interpretation while recognizing the quality of its support. We propose linking evidence-centered benchmarks, evaluation that preserves scholarly disagreement, and model-development experiments on literary data, contextual resources, and scholarly feedback. Danish literature provides a concrete starting point, with implications for other languages and domains. The aim is to develop alternative evaluation strategies that go beyond conventional benchmark metrics and guide model development toward cultural robustness in AI systems.

### 中文一句话结论
本文主张语言模型的文化评估不能只关注事实知识与文化覆盖广度，更应引入“阐释深度”，以文学阐释为测试场景，用“证据支持质量”与“专家分歧”取代单一正确答案。

### English TL;DR
The paper argues that evaluating cultural understanding in language models should go beyond factual breadth to include interpretive depth, using literary interpretation—where disagreement and evidentiary quality are both recognized—to create evidence-centered benchmarks, pluralistic evaluation, and model-development experiments that improve cultural reasoning across languages and domains.

### 中文详细总结
作者指出，现有文化基准多测试事实知识、调查结果匹配或预定义含义的识别，无法回答模型能否解释一个文化指涉在特定文本中如何起作用、能否用证据支持某种解读、或能否在受到批评后修正解读。文章提出与“文化覆盖广度”互补的“阐释深度”，并以丹麦文学等材料为例，研究“文化引用”和“文化复用”现象。核心区分是“同意某种解读”与“认为该解读有充分证据支持”是两回事。作者主张建立以证据为中心的基准，让文学专家保留个体判断，用概率软标签或多种参考解读来评价模型输出。评估应区分错误事实、证据与阐释的连接质量、以及专家对不同解读合理性的判断。模型开发实验应比较不同训练数据、检索上下文和学者反馈的作用，并警惕模型只是表面模仿学术谨慎、或过于顺从以致放弃有依据的解读。最终目标是提升模型跨语言、时代、体裁和阐释立场的文化稳健性。

### 方法 / 贡献
- 提出“阐释深度”作为文化评估的新维度，与“文化覆盖广度”互补。
- 使用文学中的“文化引用”与“文化复用”作为研究场景，考察模型能否追溯源文本、说明其语境意义并回应批评。
- 提出基于证据的基准设计：任务应指定所测能力、可引发的行为和用于判断的证据。
- 建议多种专家参考解读与保留专家分歧的评估协议，区分“可识别错误”“论证质量”和“解读合理性”三个判断层次。
- 设计模型开发实验：比较不同数据来源、是否有检索上下文、以及细粒度学者反馈对修正和保持立场的影响。
- 将评估框架推广到法律、视觉文化等领域，强调结论与论证支持的分离。

### 实验或数据
摘要和可见内容未报告具体实验或数据集结果。文中描述的是拟议的实验设计，包括对历史丹麦语/挪威语文学语料的使用、passage-only 与全文/检索条件的比较、以及添加小说对训练影响的验证，但未提供实证数据或评估结果。

### 值得关注点
- 对现有文化基准“重广度轻深度”的批评值得重视。
- “同意某解读”和“认为其论证充分”的区分具有方法论价值，可用于设计更细致评估。
- 强调保留专家分歧而非强制合意，有助于避免评估中隐藏的偏见。
- 指出检索上下文可能只是让薄弱论断“看起来有据”，这一风险对 RAG 评估有启示。
- 提出用“模型面对质疑时是坚持有据立场还是轻易放弃”来测试其鲁棒性，是一个可操作的思路。

### 局限性
- 论文是观点/纲领性文章，未提供实证验证或可复现结果。
- 依赖文学专家评估，成本高、可扩展性未知。
- 翻译问题和评分量表可能改变被测量内容，跨语言比较需要额外有效性检验。
- 自动评估模型或 LLM-as-judge 可能存在与人类判断不一致、或共享偏好导致虚假一致的问题。
- 文学作品训练数据对模型能力的贡献仍不确定，现有证据显示增加小说可能降低部分基准成绩，这一矛盾作者未解决。

## 4. Reliability-aware Cross-sample Enhancement for Robust Multimodal Sentiment Analysis

- Source: arxiv
- arXiv ID: 2609.30470
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.30470v1
- PDF: https://arxiv.org/pdf/2609.30470v1
- DOI: https://doi.org/10.48550/arXiv.2609.30470

### Authors

Menghua Jiang, Haokai Gao, Xiangui Kang, Haifeng Hu, Sijie Mai

### Abstract

Multimodal Sentiment Analysis (MSA) aims to infer human emotions from multiple modalities such as text, audio, and vision. In practice, inputs are often corrupted by noise and missing modalities, which degrades performance. Existing methods typically address these challenges in isolation, limiting their effectiveness in realistic settings. To address this limitation, we propose a Reliability-aware Cross-sample Enhancement (RCE) framework. Specifically, RCE first introduces an adaptive variational information bottleneck to model modality-wise uncertainty and perform quality-aware information compression, thereby suppressing redundant noise in unreliable modalities. Furthermore, we design a reliability-aware cross-sample enhancement strategy that retrieves high-confidence, semantically consistent neighbors from a large candidate pool to enrich and calibrate current representations, effectively alleviating information deficiency caused by missing modalities. Building upon this, RCE integrates cross-modal interactions with a multilevel reliability-aware fusion mechanism to adaptively aggregate information across modalities and enhancement stages, leading to more robust multimodal representations. Extensive experiments demonstrate that RCE consistently outperforms state-of-the-art methods across full, noisy, and missing-modality settings.

### 中文一句话结论
提出可靠性感知跨样本增强（RCE）框架，通过自适应变分信息瓶颈建模模态不确定性并抑制噪声，结合跨样本检索高置信邻居补偿缺失模态，实现全模态、噪声和缺失场景下的鲁棒多模态情感分析。

### English TL;DR
The paper proposes a Reliability-aware Cross-sample Enhancement (RCE) framework that uses adaptive variational information bottleneck for uncertainty modeling and noise suppression, along with a cross-sample enhancement strategy to retrieve high-confidence neighbors for missing modality compensation, achieving robust multimodal sentiment analysis under full, noisy, and missing-modality conditions.

### 中文详细总结
多模态情感分析在实际应用中常面临输入噪声和模态缺失的挑战，现有方法通常孤立处理这些问题。为此，本文提出RCE框架：首先，引入自适应变分信息瓶颈（AVIB）将每个模态映射到von Mises–Fisher（vMF）分布，通过浓度参数显式建模模态级不确定性并实现质量感知的信息压缩；其次，设计可靠性感知跨样本增强策略，从大规模候选池中检索高置信度且语义一致的邻居样本来丰富和校正当前表示，缓解缺失模态带来的信息不足；最后，通过超模态生成与多级可靠性感知融合机制，自适应聚合跨模态和增强阶段的信息，形成鲁棒的多模态表示。在四个基准数据集上的实验表明，RCE在全模态、噪声和缺失设置下均一致优于现有方法。

### 方法 / 贡献
1. **统一框架**：首次提出同时应对全模态、噪声和缺失模态的RCE框架，无需为每种情况设计单独模块。
2. **可靠性感知范式**：显式建模模态不确定性，实现自适应的信息压缩（AVIB）、跨样本信息增强（检索高置信邻居）和多级融合（基于模态置信度动态加权）。
3. **性能优势**：在四个基准数据集和三种评估设置（全模态、噪声、缺失）上一致超越现有方法，鲁棒性强。

### 实验或数据
实验使用四个多模态情感分析基准数据集（如MOSI、MOSEI等），设置三种评估场景：全模态、噪声模态（人为添加噪声）和模态缺失（模拟缺失）。RCE在所有场景下均取得最优或接近最优的性能，在噪声和缺失条件下提升尤其显著。

### 值得关注点
- **vMF分布建模不确定性**：将模态表示参数化为vMF分布的均值和浓度，浓度κ直接反映样本级可靠性，导向自适应压缩。
- **跨样本增强不依赖mini-batch**：从大规模离线候选池中检索高置信邻居，避免小批量内样本不足和噪声干扰，且拒绝语义不一致的负样本。
- **多级融合机制**：在模态内、跨模态和增强阶段之间进行可靠性感知的加权融合，提升表示鲁棒性。

### 局限性
- 依赖大规模候选池进行跨样本检索，可能带来存储和计算开销，且需离线维护和更新。
- vMF分布假设可能不适用于所有噪声类型或极端不规则的不确定性模式。
- 方法未明确讨论对候选池质量（如样本分布偏差、标签噪声）的敏感性，在数据稀疏场景下检索可能受限。

## 5. Feeding BabyLMs Macaroni: Code-Switching Curricula Cause Cross-Lingual Convergence

- Source: arxiv
- arXiv ID: 2609.30535
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.30535v1
- PDF: https://arxiv.org/pdf/2609.30535v1
- DOI: https://doi.org/10.48550/arXiv.2609.30535

### Authors

Dries Rooryck, Alex Cai, Yonatan Belinkov, David Alvarez-Melis, Kianté Brantley

### Abstract

Children in multilingual communities often code-switch, using multiple languages in a single utterance. Can we induce cross-lingual alignment in language models by training on code-switched text? We pretrain small decoder-only transformers on two 100M-word multilingual corpora: a base corpus formed by mixing the English, Dutch, and Chinese BabyBabelLM datasets, and a corpus generated from it by inserting word- and sentence-level code-switching using an LLM. We find that training on code-switched data aligns the representations of parallel text, particularly across different scripts, and that this alignment persists through training on monolingual documents. Under a learning curriculum that progresses from word-level code-switching, to sentence-level code-switching, to monolingual documents, models trained on code-switched data outperform baselines trained without it on the BabyLM evaluation suite. Our work characterizes code-switching curriculum learning as an effective data augmentation method for multilingual pretraining. We release our code, data, and models at https://github.com/drooryck/multilingual-macaroni.

### 中文一句话结论
在低资源多语言预训练中，采用“词级语码转换 → 句级语码转换 → 单语文本”的课程学习，可以促使模型产生跨语言表征对齐（尤其跨文字系统），并在 BabyLM 评测集上优于未使用语码转换数据训练的基线模型。

### English TL;DR
Training small decoder-only transformers on code-switched multilingual data with a progressive curriculum (word-level CS, then sentence-level CS, then monolingual documents) induces cross-lingual alignment of representations—especially across different scripts—and improves performance on the BabyLM evaluation suite compared to baselines trained without code-switched data.

### 中文详细总结
本文从多语言环境中儿童经常进行语码转换（code-switching）这一现象出发，研究能否通过在训练数据中加入语码转换来提升语言模型的跨语言对齐能力。作者用英语、荷兰语、中文的 BabyBabelLM 数据混合成一个 100M 词的多语语料，并基于此语料，利用 LLM 生成同时包含词级和句级语码转换的增强语料。实验发现，使用语码转换数据训练的模型能够对齐平行文本的表征，特别是跨不同文字系统的表征；而且这种对齐效果在后续继续使用单语文本训练后依然存在。进一步地，作者设计了一种课程学习顺序：先词级语码转换，再句级语码转换，最后使用单语文档。采用该课程训练的模型在 BabyLM 评测集上超过了不使用语码转换数据的基线模型。文章将语码转换课程学习总结为一种有效的多语言预训练数据增强方法，并公开了代码、数据和模型。

### 方法 / 贡献
- 构建两个 100M 词的多语语料：基础语料由英语、荷兰语、中文的 BabyBabelLM 数据混合而成；CS 语料则通过 LLM 在文档中插入词级和句级语码转换生成。
- 预训练小型 decoder-only transformer，比较在有无语码转换数据下的训练效果。
- 提出一种课程学习顺序：词级语码转换 → 句级语码转换 → 单语文档。
- 主要贡献：证明语码转换课程学习可以诱导跨语言表征收敛，是一种有效的多语预训练数据增强方法，并发布相关资源。

### 实验或数据
- 数据：英语、荷兰语、中文 BabyBabelLM 数据集，各占语料的三分之一，总词数为 100M。
- CS 语料中，每种语言的数据被等分为词级语码转换、句级语码转换和单语文档三部分。
- 评测：使用 BabyLM 评测套件比较有无语码转换训练数据的模型表现。
- 结果显示，采用课程学习的语码转换模型优于无语码转换的基线，且跨语言对齐效果在后续单语训练后仍然保持。
- 摘要层面未报告具体评测数值；更详细的指标需参考论文正文中的表格。

### 值得关注点
- 跨语言对齐在跨文字系统（如中文与拉丁字母语言）之间尤其明显，说明语码转换有助于模型跨越拼写系统差异。
- 对齐效果不是训练过程中的短暂现象：即使后续只用单语数据继续训练，模型的对齐表征仍然保持。
- 课程学习的顺序很关键，渐进式地从词级到句级再到单语文本带来了更好的评测表现。
- 该方法不依赖显式平行语料，而是用 LLM 合成语码转换数据，提供了一种可扩展的数据增强思路。

### 局限性
- 实验仅在 100M 词的数据规模和小型 decoder-only 模型上进行，未验证更大模型和数据规模下的表现。
- CS 语料由 LLM 自动合成，可能与真实双语儿童接触的自然语码转换数据存在分布差异。
- 研究只覆盖英语、荷兰语和中文三种语言，跨语言泛化结论有限。
- 评估主要基于 BabyLM 评测套件，未涉及更广泛的下游多语言任务。
- 摘要中未报告具体指标数值或统计显著性，难以判断效果的实际稳定程度。

## 6. Evaluating Cultural Awareness of LLMs for Haitian Creole

- Source: arxiv
- arXiv ID: 2609.31506
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.31506v1
- PDF: https://arxiv.org/pdf/2609.31506v1
- DOI: https://doi.org/10.48550/arXiv.2609.31506

### Authors

Christelle Clervilsson, Yanzhu Guo

### Abstract

Large language models (LLMs) exhibit substantial performance disparities between high- and low-resource languages. Beyond lower task performance, they often fail to capture the cultural norms and values of underrepresented communities. In this work, we present the first systematic evaluation of cultural awareness in LLMs for Haitian Creole, a language spoken by millions but severely underrepresented in digital resources. We assess cultural awareness along four complementary dimensions---specificity, bias, diversity, and variation---using a benchmark of culturally salient prompts curated by native speakers in a text infilling setting. Our results reveal a clear gap between cultural awareness in Haitian Creole and higher-resource French, with Haitian performance being more uneven across domains and more affected by French linguistic interference. Story generation further reveals recurring portrayals of Haitian characters through hardship and resilience, showing that even positive characterizations can encode stereotypical narratives. Our code, benchmark, and evaluation framework are publicly available.

### 中文一句话结论
本工作首次系统评估了大型语言模型对海地克里奥尔语（Haitian Creole）的文化意识，揭示其与法语相比存在显著差距，且在故事生成中即使正面刻画也隐含刻板叙事。

### English TL;DR
This paper presents the first systematic evaluation of cultural awareness in large language models for Haitian Creole, revealing a significant gap compared to French and showing that even positive portrayals in story generation encode stereotypical narratives.

### 中文详细总结
作者针对海地克里奥尔语这一低资源语言，构建了首个文化实体填空基准（benchmark），由母语者精心设计提示语，涵盖七个文化实体类别（如食物、音乐团体、政治家等）。评估从四个维度展开：特异性（specificity）、偏见（bias）、多样性（diversity）和变异性（variation）。实验表明，模型对海地克里奥尔语的文化意识明显低于对法语的文化意识，且表现领域间不均衡，并受到法语语言干扰。在故事生成任务中，模型反复将海地人物与“苦难”和“韧性”关联，即便看似正面的描述也加强了刻板印象。

### 方法 / 贡献
- 构建了首个海地克里奥尔语文化实体填空基准，提示语由母语者手工撰写并标注。
- 提出四项文化意识评估维度（特异性、偏见、多样性、变异性），灵感来自CAMeL和MAKIEval框架。
- 通过实体填空和故事生成任务，系统比较了海地克里奥尔语与法语的文化表征差距。
- 公开代码、基准和评估框架。

### 实验或数据
- 实验基于母语者自建的文化实体清单和提示语，用于实体填空任务。
- 使用Mistral模型（中型和大型）进行生成，每个提示生成10次以评估变异性。
- 故事生成任务分析模型对海地人物的叙事模式。
- 未使用现成数据集，所有数据均来自母语者手工构建。

### 值得关注点
- 首次将克里奥尔语NLP与文化意识评估联系起来。
- 揭示低资源语言中模型文化知识的不平等性，且语言干扰（法语主导）显著。
- 故事生成中“正面刻板印象”的发现对AI伦理和包容性设计有启示。

### 局限性
- 实体匹配依赖精确匹配，可能遗漏口语或地区变体，低估真实文化覆盖。
- 基准仅覆盖七个实体类别，未能全面反映海地文化的多样性。
- 实验仅使用Mistral模型，未覆盖其他多语言模型族（如Qwen、LLaMA）。
- 法语干扰的分析可能忽略其他语言（如英语、西班牙语）的潜在影响。

## 7. Cheap, open agents make LLM pollution harder to mitigate

- Source: arxiv
- arXiv ID: 2609.31054
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.31054v1
- PDF: https://arxiv.org/pdf/2609.31054v1
- DOI: https://doi.org/10.48550/arXiv.2609.31054

### Authors

Raluca Rilla, Anne-Marie Nussberger, Rui Mata, Dirk U. Wulff

### Abstract

Large Language Model (LLM) pollution occurs when synthetic responses contaminate data intended to capture human behavior. High deployment costs have so far limited the risk posed by autonomous survey agents. However, open-weight models paired with open-source agentic frameworks may have removed this barrier. We compared the performance and detectability of nine agent configurations, ranging from fully open variants to closed commercial ones. Each agent autonomously completed a survey containing multiple response types yielding various detection checks. Fully open agents ran locally without usage fees and performed competitively with commercial alternatives. Open and commercial agents failed different sets of checks, and no single check reliably detected all agents, but open-text responses discriminated best between agents and humans. These findings identify fully open agents as a distinct risk for LLM pollution and support multilayered detection strategies emphasizing open-text analysis.

### 中文一句话结论
完全开源的轻量级 LLM 智能体因成本极低且性能可与商业模型竞争，使“LLM 污染”更难被检测，需要多层检测策略并重点分析开放文本。

### English TL;DR
Fully open-weight LLM agents, being cheap and competitive with commercial systems, pose a distinct and harder-to-detect risk for LLM pollution; no single detection check catches all agents, and open-text responses best separate agents from humans.

### 中文详细总结
论文考察了大型语言模型（LLM）污染问题，即合成回复污染用于捕捉人类行为的数据。过去，高昂的部署成本限制了自主调查智能体带来的风险，但开源权重模型与开源智能体框架的结合可能消除了这一障碍。研究比较了从完全开源到闭源商业的九种智能体配置，让它们自主完成包含多种回答类型的调查，以评估检测效果。结果发现，完全开源的智能体可以本地运行、无需使用费用，且表现与商业替代品相当。开源与商业智能体会在不同检测检查中“失败”，没有单一检查能可靠识别所有智能体；其中开放文本回答对人类与智能体的区分效果最好。研究认为完全开源智能体构成了独特的 LLM 污染风险，并支持采用强调开放文本分析的多层检测策略。

### 方法 / 贡献
- 比较九种智能体配置，范围从完全开源到闭源商业系统。
- 每个智能体自主完成包含多种回答类型的调查，以产生不同类型的检测检查。
- 贡献：识别出完全开源智能体是 LLM 污染的独特且更难缓解的风险来源。
- 提出多层检测策略，并强调开放文本分析在区分智能体与人类时的价值。

### 实验或数据
摘要未提及具体数据集或定量结果。实验为九种智能体配置在自主完成调查任务中的比较，涵盖多种回答类型及相应检测检查，但摘要未给出数据规模或详细指标。

### 值得关注点
- 完全开源智能体可本地运行、无使用费，且性能与商业方案相当。
- 开放与商业智能体会未通过不同的检测检查，说明检测具有互补性。
- 没有单一检查能可靠检测所有智能体，而开放文本回复是最具区分度的信号。

### 局限性
摘要未明确讨论局限性。文中也未提供具体数据集、样本量或统计检验信息，因此无法从现有摘要推断更多方法学限制。

## 8. DIAL: Position-Debiased LLM Judges with Adaptive Human Preference Calibration

- Source: arxiv
- arXiv ID: 2609.31215
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.31215v1
- PDF: https://arxiv.org/pdf/2609.31215v1
- DOI: https://doi.org/10.48550/arXiv.2609.31215

### Authors

Zesheng Cai, Yingqi Fan, Sichang Chen, Jin-Hong Du

### Abstract

Large language models (LLMs) as a judge enable scalable evaluation, but their judgments can be sensitive to response order and, even after removing such position effects, can still diverge systematically from human preferences.We introduce DIAL, a unified framework that combines abundant LLM comparisons with limited human comparisons to separate judge-specific position effects, learn shared structure in position-debiased LLM preferences, and adaptively calibrate that structure toward the human preference target. Theoretically, we study three aspects of DIAL: (i) identification of latent LLM preferences, position effects, and human calibration; (ii) adaptive estimation that balances LLM anchoring against limited human evidence; and (iii) fixed-weight uncertainty quantification for the calibrated human preference. Empirically, we evaluate position debiasing and human alignment separately in controlled simulations and on three human-preference benchmarks, showing that DIAL remains robust to unbalanced response order, achieves strong human-aligned rankings with limited labels, and adapts toward human evidence when LLM information is imperfect. Our real-data study collects over 410K judgments from 21 LLM judges in both display orders, providing a resource for future studies of LLM-judge bias, heterogeneity, and human alignment.

### 中文一句话结论
DIAL 通过融合海量 LLM 比较与少量人类比较，统一实现位置去偏和自适应人类偏好校准，在理论可识别性和有限标签下取得强对齐性能。

### English TL;DR
DIAL introduces a unified framework that separates judge-specific position effects from LLM preferences, learns shared structure across judges, and adaptively calibrates toward human preferences using limited human comparisons, achieving robust position debiasing and human-aligned rankings with theoretical guarantees and strong empirical performance.

### 中文详细总结
本文提出 DIAL 框架，解决 LLM 作为评估者时的两个关键问题：位置偏差（响应顺序影响判断）和人类偏好偏移（LLM 判断与人类偏好系统性差异）。该框架利用大量的 LLM 成对比较和少量的人类成对比较，首先分离每个 LLM 评估者特有的位置效应，恢复无位置偏差的潜在 LLM 偏好；然后学习跨 LLM 评估者的共享结构（共识-分歧分解）；最后自适应地将该结构校准到潜在的人类偏好目标，通过有限的人类标签实现对齐。理论上，DIAL 证明了 LLM 偏好、位置效应和人类校准参数的可识别性，推导了自适应估计的近似-估计权衡、固定权重推理以及基于留一人类损失的 GACV 调参方法。实验上，在合成数据和三个人类偏好基准（含 21 个 LLM 评估者、超过 41 万条判断）上验证了 DIAL 对非平衡响应顺序的鲁棒性、在有限人类标签下的强对齐能力，以及在 LLM 信息不完美时向人类证据的适应能力。

### 方法 / 贡献
1. **位置去偏模型**：对每个 LLM 评估者采用带顺序效应的 Bradley-Terry-Luce 模型，分离位置偏差与潜在偏好，并提供基于图环的可识别性判据。  
2. **共享结构学习**：对去偏后的 LLM 分数矩阵进行共识-分歧分解，提取公共偏好方向和异质性低秩结构。  
3. **自适应人类校准**：将 LLM 共享结构作为锚点，通过自适应权重（基于 GACV 调参）结合有限人类比较，校准到人类偏好目标，并给出固定权重不确定性量化。  
4. **理论分析**：证明了参数可识别性、校准的近似-估计权衡、渐近正态性以及留一损失的无偏估计（GACV）。  
5. **大规模数据资源**：贡献了 21 个 LLM 评估者、两种响应顺序、超过 41 万条判断的基准数据集。

### 实验或数据
实验分为三部分：  
- **合成数据模拟**：控制位置偏差与人类偏差程度，验证 DIAL 在非平衡响应顺序下的鲁棒性及自适应权重效果。  
- **三个人类偏好基准**：在真实数据集上评估位置去偏和人类对齐，展示 DIAL 在有限人类标签下取得强排名对齐，且当 LLM 结构有偏时自适应机制有效提升性能。  
- **大规模实数据收集**：对 21 个 LLM 评估者、每个基准在两种显示顺序下收集超过 41 万条成对判断，构成开放资源。

### 值得关注点
- 同时解决位置偏差与人类偏好偏移两个耦合问题，而非分开处理。  
- 理论上证明了在有限人类标签下 LLM 共享结构可有效缩小人类偏好估计的搜索空间。  
- 自适应权重机制在 LLM 证据不完美时能自动向人类证据倾斜。  
- 提供了大规模多 LLM 评估者、双顺序的比较数据集，有利于后续偏差与异质性研究。

### 局限性
摘要和预览内容未明确讨论该方法的局限性。潜在局限包括：人类比较的获取仍可能有一定成本；结构化表示假设可能在某些场景下受限；理论结果依赖固定权和渐近假设，有限样本下性能需进一步检验。

## 9. HARDEN: Constrained Evolutionary Search for Harder, Answer-Preserving Evaluation Cases

- Source: arxiv
- arXiv ID: 2609.30571
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.30571v1
- PDF: https://arxiv.org/pdf/2609.30571v1
- DOI: https://doi.org/10.48550/arXiv.2609.30571

### Authors

Aditya Kumaran, Rahul Singhal, Karime Maamari, Amine Mhedhbi, Pradyumna Tambwekar

### Abstract

Language models are often evaluated on curated benchmarks that underrepresent the complexity of enterprise deployments. We introduce HARDEN, a constrained evolutionary search method to adapt the input of existing evaluation cases into more challenging variants while keeping their expected outputs fixed. HARDEN searches along generated domain-specific complexity axes while enforcing feasibility constraints such as preserving task semantics, realism, and execution validity. Across FinQA, PubMedQA, and ContractNLI and three Qwen3.5 model scales (35B-A3B, 122B-A10B, and 397B-A17B), HARDEN reduces task-model accuracy by 22.7% on average and by up to 49.9% relative to single-pass baselines using the same feasibility checks. These results show that evolutionary search can produce substantially harder valid evaluation cases.

### 中文一句话结论  
HARDEN 通过约束进化搜索，在保持答案不变的前提下生成更难的评测用例，平均降低任务模型准确率 22.7%。

### English TL;DR  
HARDEN uses constrained evolutionary search to transform existing evaluation cases into harder, answer-preserving variants, reducing task-model accuracy by 22.7% on average across financial, medical, and legal benchmarks.

### 中文详细总结  
语言模型在现有基准评测上的表现往往不能反映其在企业级部署中的实际复杂性。HARDEN 提出一种约束进化搜索方法，自动将已有评测用例的输入改编为更难的变体，同时保持预期输出不变。  
该方法首先生成领域特定的复杂度轴（如财务推理中的日期混淆、医疗文献中的逻辑嵌套），并通过独立搜索迭代地对输入进行变异。每个变异必须通过三项可行性检查：正确性（保留推导答案所需证据）、现实性（符合领域实际）、有效性（保持用例格式可执行）。只有通过检查且能降低模型准确率的变体才会被保留。  
在 FinQA（财务）、PubMedQA（医疗）、ContractNLI（法律）三个基准上，使用 Qwen3.5 三种规模模型（35B-A3B、122B-A10B、397B-A17B）进行测试。HARDEN 平均降低任务模型准确率 22.7%，最高相对降幅达 49.9%，同时显著提高模型输出的语义熵（不确定性）。相比单次变异的基线方法（Few-Shot、Few-Shot + 网络搜索），HARDEN 在生成有效且更难的用例上表现更优。

### 方法 / 贡献  
- **方法**：HARDEN 是一个约束进化搜索框架。它从原始输入开始，每代选择复杂度轴指导变异，生成 λ 个候选；通过基于 LM 的正确性、现实性、有效性检查过滤候选；保留 μ 个得分最低（即模型准确率下降最大）且通过检查的候选作为下一轮父代；经过 G 代后返回最优变体。  
- **贡献**：  
  1. 提出联合使用领域特定复杂度轴和三项可行性约束的进化搜索方法。  
  2. 设计基于 LM 的正确性与现实性检查，并与人类判断对比验证。  
  3. 在三个专业领域和多种模型规模上证明 HARDEN 能持续生成更难的评测用例，且相对于单次变异基线有显著优势。

### 实验或数据  
- **基准数据集**：FinQA（财务）、PubMedQA（医疗）、ContractNLI（法律，来自 LegalBench）。每个基准采样 200 个代表用例。  
- **任务模型**：Qwen3.5 MoE 的三个规模（35B-A3B、122B-A10B、397B-A17B）。突变和领域分析使用 Claude Opus 4.8。  
- **HARDEN 参数**：G=4 代，λ=11 个变异/代，μ=5 保留数，K=3 次 LM 检查，T=10 次采样求准确率。  
- **基线**：Few-Shot（无工具）和 Few-Shot（带只读网络搜索，且禁止搜索目标基准）。每个用例配 5 个困难示例。  
- **评估指标**：各基准原生指标（FinQA 执行准确率，PubMedQA 和 ContractNLI 准确率），及离散语义熵。  
- **结果**：  
  - RQ1：HARDEN 在 52.4%（平均）的用例上降低了准确率，远超基线的 12.7%。  
  - RQ2：随模型规模增大，HARDEN 仍有效；397B 规模下平均成功硬化 81.7/200 个用例，是基线在最小规模下的 2.5 倍。语义熵平均提升 112%。  
  - RQ3：正确性和现实性检查与人类判断的一致性在附录中报告（本文未提供详细数字，但提及对比实验设置）。

### 值得关注点  
1. **进化搜索 vs. 单次变异**：HARDEN 通过多代迭代搜索显著提升了生成难例的能力，而单次变异方法即使加入网络搜索也难以兼顾难度和可行性。  
2. **三项约束的可操作性**：将正确性、现实性、有效性分开检查，避免仅靠语义相似度无法捕捉的违反任务语义问题。  
3. **跨领域和模型规模的泛化性**：在财务、医疗、法律三个完全不同的专业领域，以及从 35B 到 397B 的模型上均取得一致效果。  
4. **不确定性提升**：不仅降低准确率，还显著增加模型输出的语义熵，表明模型对更难用例的预测不确定性更高，这为鲁棒性评估提供了额外维度。

### 局限性  
- **范围有限**：仅在三个基准（FinQA、PubMedQA、ContractNLI）和 Qwen3.5 系列模型上验证，尚未扩展到更多领域或模型家族。  
- **计算成本**：HARDEN 需要多代进化（G=4）和多次 LM 调用（每代 λ 个变异 × K 次检查），成本高于单次变异基线，文中未明确讨论效率可扩展性。  
- **依赖外部检查模型**：正确性和现实性检查依赖于 Claude Opus 4.8 的能力，检查本身的偏见或错误可能影响结果。  
- **未探索跨领域迁移**：复杂度轴和现实性评估是为每个基准单独生成的，未验证是否可跨领域复用。  
- **现实性检查的局限性**：尽管与人类判断进行了对比，但“现实性”本身定义仍存在主观性；某些领域（如法律）可能难以穷举所有真实场景。

## 10. A Benchmark Framework for Screening Automation in Systematic Reviews

- Source: arxiv
- arXiv ID: 2609.30298
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.30298v1
- PDF: https://arxiv.org/pdf/2609.30298v1
- DOI: https://doi.org/10.48550/arXiv.2609.30298

### Authors

Gauransh Kumar, Luciano Marchezan, Guillaume Genois, Kévin Delcourt, Eugene Syriani

### Abstract

Systematic reviews (SR) are essential for evidence-based research, but their screening phase is highly time-consuming and labor-intensive. Large language models (LLMs) offer a promising opportunity to reduce this workload by assisting with article relevance classification. However, existing evaluation approaches often rely on traditional metrics that may be misleading for highly imbalanced SR screening datasets.This paper presents a benchmark dataset of $45\,064$ labeled entries for evaluating LLM performance in SR screening across 32 curated secondary studies. It proposes an evaluation framework that accounts for class imbalance, i.e., the natural prevalence of excluded articles relative to included articles in SRs. It also introduces PromptSR, a tool designed to support prompt experimentation, experiment management, and result analysis for LLM-based screening. We also present a use case demonstrating the application of SRBench and PromptSR.

### 中文一句话结论
本文提出SRBench基准框架，包含45,064条标注数据的32项二次研究数据集，以及PromptSR工具，用于评估大规模语言模型在系统综述筛选中的性能，并采用考虑类别不平衡的评估指标。

### English TL;DR
This paper introduces SRBench, a benchmark framework with a dataset of 45,064 labeled entries from 32 curated secondary studies and the PromptSR tool, for evaluating large language model performance in systematic review screening using metrics that account for class imbalance.

### 中文详细总结
系统综述筛选阶段耗时费力。大型语言模型（LLM）有望辅助文章相关性分类，但现有评估方法常采用传统指标，对于高度不平衡的筛选数据集可能产生误导。本文提出SRBench基准框架，包含一个由32项二次研究（从SESR的18项扩展至32项）组成的45,064条标记条目数据集，以及PromptSR工具。PromptSR支持提示实验、实验管理和结果分析。框架采用马修斯相关系数（MCC）和平衡准确率（BAcc）等对类别不平衡鲁棒的指标，并辅以精确率、召回率、特异性等。文章还通过一个用例展示了SRBench和PromptSR的应用，但摘要未提供具体实验结果数值。

### 方法 / 贡献
1. **构建基准数据集**：整合并扩展SESR数据集，新增14项软件工程领域的二次研究，总计32项研究、45,064条标记条目（含标题与摘要）。
2. **提出不平衡感知评估框架**：采用MCC和BAcc作为主要指标，克服传统精度/召回率在高度不平衡数据上的误导性，并保留召回率、精确率、特异性等辅助指标。
3. **开发PromptSR工具**：支持提示实验配置、实验管理（记录模型、参数、结果）及结果分析，便于可复现的LLM筛选实验。
4. **用例验证**：通过实际应用演示框架与工具的可行性。

### 实验或数据
- **数据集**：由32项软件工程二次研究的筛选决策组成，共45,064条条目，每条包含标题和摘要。其中18项来自SESR原数据集，14项为新收集并经过人工校验。
- **实验**：文章报告了一个使用PromptSR进行的用例实验，但摘要中未给出具体性能数值或结果分析。原文正文详细描述了该用例的配置和结果。

### 值得关注点
- **大规模跨领域数据集**：涵盖32项二次研究，覆盖软件工程多个子领域，有利于评估LLM的泛化能力。
- **不平衡友好评估**：采用MCC和BAcc等指标，更符合实际筛选场景（正类比例极低）。
- **工具支持**：PromptSR提供了提示工程实验管理、结果追踪与比较的可复现环境。
- **实用导向**：直接针对LLM辅助系统综述筛选这一高耗时环节，具有明确的应用价值。

### 局限性
原文摘要未明确讨论局限性。根据研究内容及领域背景，可预见的局限包括：
- **领域覆盖**：数据集仅来自软件工程领域，其他学科（如医学）的适用性未知。
- **提示敏感性**：LLM性能高度依赖提示设计，框架虽支持实验管理，但未系统研究提示工程的稳健性。
- **基准对比**：未与人工筛选或传统机器学习方法进行成本效益对比。
- **数据依赖**：数据质量依赖于原始二次研究的筛选记录完整性。

## Processing Notes

- Duplicate papers skipped: 0