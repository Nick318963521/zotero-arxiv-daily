# Daily arXiv - 2026-07-27

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-27T23:23:16
- Paper count: 10

## 1. A Factorial Study of Synthetic Data Generation for Low-Resource Machine Translation using Grammar Books

- Source: arxiv
- arXiv ID: 2607.22376
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.22376v1
- PDF: https://arxiv.org/pdf/2607.22376v1
- DOI: https://doi.org/10.48550/arXiv.2607.22376

### Authors

Varun Ghat Ravikumar, Sina Ahmadi, Lena Jäger, Rico Sennrich

### Abstract

Most endangered languages lack the parallel data required for machine translation, despite the existence of descriptive grammar books. We introduce a pipeline that uses large language models to extract grammatical rules, example sentences, and lexicons from grammar books and generate synthetic parallel corpora for fine-tuning-rather than feeding grammar content into prompts at inference time, as in prior work. Validated on three typologically diverse low-resource languages-Kalamang (Papuan), Tuatschin (Romance), and Mandan (Siouan)-we show that fine-tuning on synthetic data improves over seed-data baselines in 75% of configurations for Kalamang and 59% for Tuatschin, with best-case ChrF++ gains of +8.8, +5.3, and +3.3 respectively. Through a systematic factorial study across 96 configurations varying target part-of-speech, retrieval granularity, and sample volume, we identify which factor combinations drive gains and where they break down. Our results demonstrate that static linguistic documentation can be repurposed for machine translation fine-tuning, offering a practical path towards translation tools for severely under-resourced languages.

### 中文一句话结论
本文提出利用大语言模型从语法书中自动提取规则并生成合成平行语料进行微调，在三种濒危语言上多数配置下优于基线，最高提升8.8个ChrF++。

### English TL;DR
This paper introduces a pipeline that uses LLMs to extract grammatical rules, example sentences, and lexicons from grammar books to generate synthetic parallel corpora for fine-tuning. Through a factorial study on three severely low-resource languages (Kalamang, Tuatschin, Mandan), they show fine-tuning on synthetic data improves over seed-data baselines in 75% (Kalamang) and 59% (Tuatschin) of configurations, with best ChrF++ gains of +8.8, +5.3, and +3.3 respectively.

### 中文详细总结
大多数濒危语言缺乏机器翻译所需的平行语料，但存在描述性的语法书。本文提出一个半自动流水线：首先用大语言模型（Gemini-2.5-flash）从语法书中提取语法规则、例句和词典，然后生成合成平行语料用于微调，而非在推理时注入语法内容。在三种类型多样的低资源语言（卡拉芒语、图阿钦语、曼丹语）上进行验证，通过96种配置的析因实验（变化目标词性、检索粒度、生成数量），发现合成数据微调在多数配置中优于种子数据基线：卡拉芒语75%配置、图阿钦语59%配置获得提升；最佳ChrF++分别提升+8.8、+5.3、+3.3。结果表明静态语言文档可被重新用于机器翻译微调，为严重低资源语言提供了一条实用路径。

### 方法 / 贡献
- **方法**：提出从语法书中自动提取信息（平行句、词典、语法规则）并转化为结构化规则（UniMorph标注），通过受限词汇替换生成合成平行语料，用于微调翻译模型。
- **贡献**：(1) 首个自动从语法书提取规则并生成合成训练数据的流水线，只需约200条标注行用于分类器训练；(2) 通过析因实验系统分析目标词性、检索粒度（规则级vs.章节级）、生成数量对翻译质量的影响；(3) 证明静态语法文档可有效用于严重低资源语言的机器翻译微调。

### 实验或数据
- **语言**：三种类型多样的严重低资源语言——卡拉芒语（巴布亚语系，黏着型）、图阿钦语（罗曼语族，分析型）、曼丹语（苏族语系，多式综合型）。
- **数据**：从语法书中提取平行句（761–981句）、词典（459–2558词）、形态规则（144–519条）。微调使用Gemini-2.5-flash，微调数据为合成生成的平行句。
- **实验设计**：析因实验，共96种配置：4种目标词性（名词、动词、形容词、副词）× 2种检索粒度（规则级、章节级）× 4种生成数量（5、10、15、20句/组合）× 3种语言。基线为种子数据微调结果。
- **结果**：卡拉芒语75%配置、图阿钦语59%配置优于基线；曼丹语所有配置均优于基线（但最佳提升+3.3）。最佳ChrF++提升分别为+8.8、+5.3、+3.3。

### 值得关注点
- 析因实验设计系统探索了多种因素对合成数据质量的影响，为低资源数据生成提供了可参考的经验。
- 流水线仅需约200条人工标注行用于句子分类器训练，其余环节自动化，可扩展到其他有语法书的濒危语言。
- 静态语言文档（语法书）成功转化为实用的训练资源，为严重低资源语言提供了除大规模语料收集外的替代路径。

### 局限性
- 仍需少量人工监督（每语言约200条标注行）训练句子分类器，并非完全自动化。
- 语法规则提取依赖特定大语言模型（Gemini-2.5-flash），模型输出的可重复性和错误率未深入分析。
- 仅验证三种语言，且语法书质量和内容完整性差异可能影响结果泛化性。
- 合成数据生成基于限定词汇替换，可能无法覆盖所有语法现象，且生成质量受提取规则准确率限制。

## 2. Trajectory-Aware Retrieval Agents for Temporal Decision- Making

- Source: arxiv
- arXiv ID: 2607.21625
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.21625v1
- PDF: https://arxiv.org/pdf/2607.21625v1
- DOI: https://doi.org/10.48550/arXiv.2607.21625

### Authors

Jing Wang, Jie Shen, Xing Niu

### Abstract

We study the problem of decision-making from long-form, temporally structured text using large language model (LLM) agents. Standard retrievalaugmented generation (RAG) pipelines fragment chronological context into isolated snippets, discarding the temporal structure that is often critical for correct downstream decisions. We introduce TLM (Trajectory Language Model), a closed-loop agentic framework that iteratively refines the evidence set using SHAP-guided feedback. The key technical contribution is the latent growth curve model (LGCM) over retrieved chunk embeddings, which provides an interpretable mechanism for detecting trajectory trends, turning points, and information gaps. We show that, under a scorer-calibration assumption (which holds approximately in practice), the iterative refinement procedure is monotonically non-decreasing in the probability assigned to the correct label. Empirically, TLM is evaluated on three temporally grounded decision tasks: medical question answering, earnings call surprise prediction, and overnight stock gap prediction. TLM substantially outperforms both zero-shot LLM baselines and standard retrieval-augmented approaches on the medical task, and yields consistent, economically meaningful gains on the two financial tasks.

### 中文一句话结论
我们提出了TLM（Trajectory Language Model）框架，通过将潜变量生长曲线模型（LGCM）与SHAP引导的迭代证据精炼相结合，在保留时间结构的同时显著提升了基于LLM的时序决策任务的性能。

### English TL;DR
TLM integrates latent growth curve modeling and SHAP-guided iterative refinement into a retrieval-augmented generation framework to preserve temporal structure, achieving superior performance on medical and financial decision-making tasks.

### 中文详细总结
针对长文本、时间结构化信息中的决策问题，标准RAG管道会破坏时间顺序，导致错误预测。TLM框架包含五个阶段：混合检索（BM25+稠密嵌入）、潜变量生长曲线模型（检测趋势、转折点和信息缺口）、学习重排序+检索、LLM分类（通过下一个词打分）以及基于轻量级打分器的SHAP迭代精炼（仅添加重要证据）。理论证明在近似校准假设下，精炼过程单调不降地增加正确标签概率。实验覆盖三个时间关键任务：医学问答（MedQA 5类分类）、财报电话会议意外预测（二分类）和隔夜股票缺口预测（三分类）。TLM在医学任务上大幅优于零样本LLM和标准RAG基线，在两个金融任务上取得一致且有经济意义的提升。

### 方法 / 贡献
- **潜变量生长曲线模型（LGCM）**：对检索到的文本块嵌入序列拟合LGCM，提取基线状态、趋势、残差，用于检测趋势类型（稳定/渐进/变化）、转折点和信息缺口。
- **联合LLM-打分器架构与SHAP精炼**：训练一个轻量级注意力打分器与LLM（LoRA）联合优化，通过打分器高效计算留一SHAP值，迭代执行加法式证据精炼（只添加不丢弃），理论上保证单调性。
- **混合检索**：结合BM25与稠密嵌入的混合打分，保留语义与词汇匹配。
- **可解释性**：LGCM提供趋势、转折点等可解释信号，SHAP归因可追溯关键证据。

### 实验或数据
实验在三个时序决策任务上进行：
- **医学问答**： MedQA（5类分类），使用临床病例文本。
- **财报电话会议意外预测**：二分类（是否超出预期），基于财报会议记录。
- **隔夜股票缺口预测**：三分类（涨/跌/平），基于股票历史文本。
对比基线包括零样本LLM（直接回答）和标准RAG（无序检索+LLM回答）。TLM在医学任务上显著超越基线，在金融任务上取得一致的经济意义提升。

### 值得关注点
- 首次将LGCM引入RAG证据轨迹建模，为时间结构化推理提供可解释手段。
- SHAP精炼通过轻量打分器替代昂贵LLM前向传播，实现了迭代可行性。
- 理论证明在近似校准假设下迭代精炼单调改善正确标签概率，保证稳定性。
- 加法式精炼策略避免了利用退回信息的风险，且简单易实现。

### 局限性
- 方法依赖线性LGCM假设，可能无法完美捕捉非线性的真实轨迹模式。
- 打分器校准假设仅在近似程度上成立，极端情况下可能失效。
- 加法式精炼可能累积无关或低质量证据，增加计算成本。
- 实验仅在英文医学和金融数据集上进行，中文及其他领域适应性未验证。
- 论文未显式讨论模型在长序列或实时场景下的效率瓶颈。

## 3. DWT-Fusion: A Signal-Based Framework for Training-Free LLM-Generated Text Detection

- Source: arxiv
- arXiv ID: 2607.22026
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.22026v1
- PDF: https://arxiv.org/pdf/2607.22026v1
- DOI: https://doi.org/10.48550/arXiv.2607.22026

### Authors

Mehmet Batuhan Özdaş, Murat Osmanoğlu

### Abstract

Detecting LLM-generated text remains challenging under zero-shot and training-free conditions, especially when detectors must generalize across datasets, domains, and unseen generators. While existing training-free approaches exploit language-model statistics as detection signals, they typically characterize a text through global measures that summarize overall model behavior. Consequently, potentially informative local and multiscale variations in token-level predictability may remain underutilized. Motivated by this observation, we introduce DWT-Fusion, a training-free signal-based framework for detecting LLM-generated text using discrete wavelet analysis of token-level log-probability sequences produced by a proxy causal language model. The proposed framework analyzes these sequences through wavelet-based multiresolution signal representations and derives detection signals from localized probability dynamics. We further evaluate four training-free voting variants, including equal-weight hard voting, equal-weight soft voting, calibration-weighted hard voting, and calibration-weighted soft voting, to combine multiple wavelet configurations without training a supervised meta-classifier. We evaluate the framework on HC3, M4, and MAGE using GPT-Neo-2.7B, GPT-J-6B, Falcon-7B, and LLaMA-3-8B as proxy models. The best single wavelet configurations achieve AUROC values of 0.9872, 0.8185, and 0.7138 on HC3, M4, and MAGE, respectively. With calibration-weighted voting, the best ensemble variants further improve AUROC to 0.9919, 0.8477, and 0.7471. These findings show that DWT-based multiresolution scoring and calibration-guided voting fusion provide effective and interpretable signals for training-free LLM-generated text detection.

### 中文一句话结论
DWT-Fusion 是一种无需训练的 LLM 生成文本检测框架，利用离散小波变换分析 token 级对数概率序列的多尺度局部变化，并结合校准加权投票，在多个基准数据集上取得了优异的检测性能。

### English TL;DR
DWT-Fusion is a training-free, signal-based framework that uses discrete wavelet transform (DWT) on token-level log-probability sequences and calibration-weighted voting to detect LLM-generated text, achieving strong AUROC across three datasets.

### 中文详细总结
现有训练自由的检测方法通常使用全局统计量（如平均对数概率、熵等）来表征文本，忽略了 token 级可预测性的局部和多尺度变化。针对这一局限，本文提出 DWT-Fusion 框架，该框架首先通过代理因果语言模型提取每个 token 的条件对数概率，形成一维信号；然后使用离散小波变换将其分解为近似系数和细节系数，并提取三类小波域评分：第一级细节能量、多级细节能量和窗口能量变异性。为了融合不同小波配置，作者设计了四种无需训练的投票融合变体（等权硬投票、等权软投票、校准加权硬投票、校准加权软投票）。实验在 HC3、M4、MAGE 三个数据集上进行，使用 GPT-Neo-2.7B、GPT-J-6B、Falcon-7B、LLaMA-3-8B 作为代理模型。最佳单一小波配置的 AUROC 分别达到 0.9872、0.8185、0.7138；校准加权投票进一步将 AUROC 提升至 0.9919、0.8477、0.7471。

### 方法 / 贡献
1. 提出 DWT-Fusion：首个利用离散小波变换从 token 对数概率序列中提取局部、多尺度特征进行无需训练的 LLM 文本检测框架。
2. 定义三种可解释的小波域评分：第一级细节能量、多级细节能量、窗口能量变异性，分别捕捉不同尺度下的概率波动模式。
3. 引入四种无需训练的投票融合变体：等权硬投票、等权软投票、校准加权硬投票、校准加权软投票，可在不训练监督元分类器的情况下组合多个小波配置。
4. 系统地在三个基准数据集、四个代理模型、五个小波族和三种评分定义下进行了统一评估，并与概率、秩、熵、似然-秩比及 DFT 谱能量基线进行了零样本对比。

### 实验或数据
- 数据集：HC3（中英文混合问答）、M4（多领域、多模型生成文本）、MAGE（多领域、多模型）。
- 代理模型：GPT-Neo-2.7B、GPT-J-6B、Falcon-7B、LLaMA-3-8B。
- 评估指标：AUROC（曲线下面积）。
- 基线方法：对数似然、秩、对数秩、熵、LRR（似然-秩比）、DFT 谱能量等零样本方法。
- 主要结果：最佳单一小波配置在 HC3、M4、MAGE 上 AUROC 分别为 0.9872、0.8185、0.7138；校准加权投票提升至 0.9919、0.8477、0.7471。

### 值得关注点
- **完全无需训练**：无需训练分类器、微调语言模型或构建参考数据库，即插即用。
- **局部-多尺度建模**：通过小波变换显式捕捉 token 对数概率信号中局部波动与不同时间尺度的变化，超越全局统计量。
- **投票融合提升显著**：校准加权软投票在三个数据集上均一致提升了 AUROC，且不增加训练复杂度。
- **解释性**：小波域评分具有清晰的物理意义（如细节能量反映概率变化幅度），便于理解检测依据。

### 局限性
- 检测性能在 MAGE 数据集上相对较低（AUROC 0.7471），表明对某些领域或更难样本的泛化能力有限。
- 当前框架仅评估了英文及部分中文数据集，尚未验证其对更多语言或低资源语言的适用性。
- 对对抗性改写、后处理等攻击的鲁棒性尚未系统测试。
- 未与基于训练的监督检测方法或需要参考集的方法进行直接比较，无法评估其相对于这些方法的性能差距。

## 4. From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for Large Language Models

- Source: arxiv
- arXiv ID: 2607.22182
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.22182v1
- PDF: https://arxiv.org/pdf/2607.22182v1
- DOI: https://doi.org/10.48550/arXiv.2607.22182

### Authors

Shixin Fang, Jiachen Wo, Wenjuan Qin, Sihang Jiang, Yanghua Xiao

### Abstract

Large language model (LLM) evaluation spans diverse tasks and benchmarks, yet evidence remains organized around tasks rather than the capabilities they probe. This fragmentation limits cross-study comparison, obscures capabilities tasks recruit, and makes coverage gaps difficult to identify.
  We introduce a multi-layer taxonomy of 14 capability domains and 91 subskills across Primitive, Constructed, and Integrative layers. Human cognitive science guides capability definition and organization, not LLM architecture. Layer assignments draw on developmental precedence and hypothesized functional support, while human-origin constructs are adapted to observable model behavior.
  To demonstrate operational utility, we screened 31,505 papers from ACL, AAAI, ICML, and NeurIPS between 2023 and 2025 and mapped 15,934 LLM-focused papers through multi-model annotation, consensus, and arbitration. Direct research attention concentrated on Language-Semantic Competence (3,551; 22.3%), Reasoning (3,388; 21.3%), Planning and Decision-Making (2,149; 13.5%), and Perception (1,954; 12.3%), whereas six domains appeared in fewer than 2% of papers. Within domains, the most frequent subskill had a median prevalence of 97.9% and appeared in at least 90% of papers in 10 of 14 domains. Language-Semantic Competence and Reasoning formed the highest-volume pair (n = 1,864; 11.7%; lift = 2.47), whereas Theory of Mind and Social Reasoning and Interaction showed the highest lift among pairs with at least 20 co-occurrences (n = 62; lift = 30.84).
  By shifting the unit of analysis from isolated tasks to structured capabilities, the taxonomy supports research organization, coverage audits, evaluation interpretation, and testable hypotheses for diagnosis, training, and transfer.

### 中文一句话结论
本文提出一个基于人类认知科学的多层能力分类法（14个能力域、91个子技能），将LLM研究从孤立任务分析转向结构化能力组织，并通过对15,934篇论文的映射揭示了研究注意力的系统性不对称。

### English TL;DR
This paper introduces a multilayer taxonomy of 14 capability domains and 91 subskills for LLMs, grounded in human cognitive science, to shift analysis from isolated tasks to structured capabilities, and demonstrates its utility by mapping over 15,000 papers to reveal systematic asymmetries in research attention.

### 中文详细总结
论文指出当前LLM评估以任务为中心而非能力为中心，导致跨研究比较困难、能力覆盖不清。作者基于人类认知科学（认知心理学、发展心理学等）提出了一个三层（原始层、构造层、整合层）的14个能力域和91个子技能的分类法。该分类法不假设LLM具有人类认知架构，而是利用人类发展的先行性和功能支持关系来组织能力。通过筛选2023-2025年ACL、AAAI、ICML和NeurIPS的31,505篇论文，并对15,934篇LLM相关论文进行多模型标注，发现研究注意力高度集中在语言-语义能力（22.3%）、推理（21.3%）、规划与决策（13.5%）和感知（12.3%），而有6个能力域出现在不到2%的论文中。分类法支持研究组织、覆盖审计、评估解释和诊断假设生成。

### 方法 / 贡献
- **多层分类法**：14个能力域、91个子技能，分为三层（原始层：感知、注意、记忆；构造层：语言-语义、语言-语用、推理、情绪、心理理论；整合层：元认知、社会推理与交互、规划与决策、创造与创新、文化能力、道德推理）
- **三层组织原则**：基于人类发展先行性和功能支持关系分配层级
- **LLM适配操作化**：将人类认知构念转化为可观察的LLM行为目标，排除无行为模拟的构念（如精细运动控制），保留可操作化构念（如感知指输入处理功能）
- **大规模论文映射方法**：多模型标注+共识+仲裁流程

### 实验或数据
- 数据来源：ACL、AAAI、ICML、NeurIPS 2023-2025年论文（筛选31,505篇，映射15,934篇LLM相关论文）
- 关键发现：语言-语义能力（3,551篇，22.3%）、推理（3,388篇，21.3%）、规划与决策（2,149篇，13.5%）、感知（1,954篇，12.3%）为研究热点；6个能力域出现在不到2%的论文中；语言-语义能力与推理共现频率最高（n=1,864，lift=2.47）；心理理论与社会推理交互共现提升度最高（lift=30.84）

### 值得关注点
- 提出“能力反转”现象：LLM可能在认知高级任务上表现良好，却在基础规则操作（如计数、符号转换）上脆弱
- 研究注意力高度集中在少数能力域，6个能力域严重被忽视
- 分类法有助于诊断：失败可能源于推理本身、记忆/注意限制，或协调能力的故障
- 提供跨研究比较和覆盖审计的通用能力空间

### 局限性
- 分类法的依赖关系未经独立验证
- 不假设LLM具有人类认知架构或发展轨迹
- 论文映射基于文本标注，可能遗漏隐含能力研究
- 分类法本身非基准测试套件，不直接提供评估指标

## 5. Scaling Native Multimodal Pre-Training From Scratch

- Source: arxiv
- arXiv ID: 2607.22043
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.22043v1
- PDF: https://arxiv.org/pdf/2607.22043v1
- DOI: https://doi.org/10.48550/arXiv.2607.22043

### Authors

Haoyuan Wu, Aoqi Wu, Hai Wang, Jiajia Wu, Jinxiang Ou, Bei Yu

### Abstract

Although large language models (LLMs) exhibit remarkable reasoning capabilities, their reliance on text-only pre-training restricts the perception of the multimodal physical world. Native multimodal pre-training avoids this limitation by training models from scratch on multimodal inputs, thereby achieving deep cross-modal integration and mitigating optimization asymmetries inherent to traditional late-fusion architectures. Despite these advantages, the scaling properties of this paradigm remain systematically uncharacterized. To address this gap, we investigate the optimal model size and token count for training a transformer-based vision-language model under a fixed computational budget. We demonstrate that minimal objective loss adheres to a predictable compute law, whereas compute-optimal model sizes and token counts scale as power laws. Notably, language and multimodal objectives manifest distinct scaling behaviors. The language allocation law is largely invariant to the composition of the data, indicating stable language learning regardless of the multimodal data ratio. Conversely, the multimodal allocation law is highly sensitive to this composition. Specifically, text-heavy mixtures become compute-efficient only at larger model scales, shifting the optimal resource allocation toward greater model capacity. Additionally, by modeling the influence of data composition on compute laws and allocation exponents, we derive an efficiency frontier specifying precise configurations of model size, token count, and data mixture. Downstream evaluations further reveal that native multimodal pre-training induces positive cross-modal transfer, thereby enhancing pure-text spatial reasoning and enabling robust multimodal in-context learning. In summary, this empirical research establishes the essential groundwork for predictably scaling multimodal foundation models.

### 中文一句话结论
本文系统刻画了原生多模态预训练（从零开始训练）的扩展规律，发现语言与多模态目标具有不同的计算定律，并推导出最优模型规模、训练数据量和数据配比的高效边界，为实现可预测的多模态基座模型扩展奠定基础。

### English TL;DR
This paper systematically characterizes the scaling properties of native multimodal pre-training, revealing distinct compute laws for language and multimodal objectives and deriving an efficiency frontier for optimal model size, token count, and data mixture, enabling predictable scaling of multimodal foundation models.

### 中文详细总结
该研究针对原生多模态预训练（即从零开始在图文输入上联合训练）的扩展性质进行系统性分析。在固定计算预算下，作者发现最小化目标损失遵循可预测的计算定律，而计算最优的模型规模与训练数据量呈幂律关系。语言目标与多模态目标表现出截然不同的扩展行为：语言分配律对数据配比不敏感，表明无论多模态数据比例如何，语言学习保持稳定；而多模态分配律则高度敏感，在文本占比较高的混合数据中，仅在更大模型规模下才变得计算高效，从而将最优资源分配向更大模型容量倾斜。通过建模数据配比对计算定律与分配指数的影响，作者推导出指定模型规模、数据量和数据配比的高效边界。下游任务评估进一步表明，原生多模态预训练能够诱发正向跨模态迁移，提升纯文本空间推理能力，并实现鲁棒的多模态上下文学习。

### 方法 / 贡献
- 在固定计算预算下，首次系统探索原生多模态预训练中模型规模与数据量的最优配置。
- 发现语言与多模态目标各自的扩展定律，并揭示语言分配律对数据配比的不变性与多模态分配律的敏感性。
- 推导出包含数据配比的高效边界，提供可预测的模型扩展配置指南。
- 通过实验验证原生多模态训练能带来正向跨模态迁移，增强纯文本推理与多模态上下文学习。

### 实验或数据
论文未明确提及具体数据集名称或规模，但通过下游任务（如纯文本空间推理、多模态上下文学习）评估了模型的性能。实验基于Transformer架构，在固定计算预算下进行消融与扩展研究。

### 值得关注点
- 语言与多模态目标扩展行为的显著差异，以及数据配比如何影响计算效率。
- 原生多模态预训练可同时提升纯文本和多模态能力，说明早期跨模态融合的优势。
- 推导的高效边界为实际中配置模型规模、数据量与配比提供了实用指导。

### 局限性
- 研究仅基于固定计算预算和Transformer架构，未涵盖其他架构或更大规模模型。
- 数据配比对多模态扩展的敏感性可能限制模型在不同数据分布下的泛化性。
- 下游评测任务有限，未详细报告各任务的具体指标或与现有方法的全面对比。

## 6. From Profiles to Steering Vectors: Global Sparse Priors and Local Semantic Calibration for Personalized Text Generation

- Source: arxiv
- arXiv ID: 2607.21620
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.21620v1
- PDF: https://arxiv.org/pdf/2607.21620v1
- DOI: https://doi.org/10.48550/arXiv.2607.21620

### Authors

Liuji Chen, Zeyu Zhang, Xinyuan Zhang, Shuai Nie, Qiang Liu, Shu Wu, Liang Wang

### Abstract

Personalized text generation requires models to capture user-specific writing styles from historical data. Existing approaches based on retrieval, parameter-efficient fine-tuning, or activation steering either introduce inference and storage overhead or struggle to separate stylistic signals from semantic content. We propose GLASS, a training-free framework for personalized generation via Global-Local Activation Steering with Sparse priors. GLASS uses sparse autoencoders to extract a global user-style prior from historical responses and constructs local contrastive style vectors over clustered interaction scenarios. During inference, it jointly injects global and local vectors into different model layers, enabling context-aware personalization without retrieval or parameter updates. Experiments on LaMP and LongLaMP show that GLASS outperforms retrieval-, fine-tuning-, and steering-based baselines across ROUGE metrics and LLM-as-judge evaluations. Further analyses show that SAE-based representations are more robust to topic and length shifts, suggesting better disentanglement of stylistic information from semantic residue.

### 中文一句话结论
本文提出GLASS，一种无需训练的个人化文本生成框架，通过稀疏自编码器提取全局与局部风格向量并在推理时注入模型，有效分离风格与语义，性能优于检索、微调和激活干预基线。

### English TL;DR
GLASS is a training-free framework for personalized text generation that uses sparse autoencoders to extract global and local user-style steering vectors. It injects these vectors into different model layers during inference, enabling context-aware personalization without retrieval or parameter updates. Experiments on LaMP and LongLaMP show it outperforms retrieval, fine-tuning, and steering baselines, with better disentanglement of style from semantic content.

### 中文详细总结
个人化文本生成需要模型从历史数据中捕捉用户写作风格。现有方法（检索、参数高效微调、激活干预）存在推理/存储开销或难以分离风格与语义的问题。GLASS 通过稀疏自编码器（SAE）将稠密激活投影到稀疏特征空间，提取全局风格向量（用户整体写作习惯）和局部风格向量（基于交互场景聚类，并通过对比学习得到）。推理时，将全局和局部向量注入不同模型层，无需检索或参数更新。在 LaMP 和 LongLaMP 基准上，GLASS 在 ROUGE 指标和 LLM-as-judge 评估中均优于基线方法。进一步分析表明，SAE 表示对主题和长度变化更鲁棒，能更好分离风格信息与语义残留。

### 方法 / 贡献
- 识别出语义残留是现有激活干预个人化方法的关键限制，并证明 SAE 表示能提供更鲁棒的风格特征。
- 提出 GLASS 框架：全局风格向量通过平均用户历史响应中所有 token 的 SAE 稀疏激活并解码得到；局部风格向量通过聚类历史交互场景，并在每个簇内使用正负对比样本提取激活差异得到。
- 推理时无需训练或检索，仅需少量用户存储（全局向量和每簇局部向量）。
- 贡献：首个利用 SAE 稀疏先验进行全局-局部激活干预的个人化框架，有效分离风格与语义。

### 实验或数据
- 实验在 LaMP 和 LongLaMP 基准上进行，涵盖多个个人化任务（如邮件、评论、对话）。
- 基线包括检索方法（如 ICL）、PEFT 方法（如 LoRA）和激活干预方法（如 StyleVector、Fints）。
- 评估指标：ROUGE-1/2/L、LLM-as-judge（基于 GPT-4 的评分）。
- 额外分析：SAE 表示在主题/长度扰动下更鲁棒，表明风格-语义分离更好。
- 代码已开源。

### 值得关注点
- 首次将稀疏自编码器用于个人化文本生成的激活干预，提升风格语义分离能力。
- 全局-局部双粒度建模：全局捕捉稳定风格，局部适应场景变化，无需额外训练。
- 推理时仅需注入向量，无检索延迟，无参数存储，适合大规模用户。
- 在长文本个人化（LongLaMP）上也有效，扩展性强。

### 局限性
- 论文未明确讨论局限性，但可能依赖于用户历史数据的质量和数量，且局部聚类需要设定簇数（K），可能影响性能。
- 全局/局部向量的提取仍需离线处理用户历史，但推理时无需用户数据。
- 尚未探讨对极端长尾用户或冷启动场景的适应性。

## 7. Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization

- Source: arxiv
- arXiv ID: 2607.21619
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.21619v1
- PDF: https://arxiv.org/pdf/2607.21619v1
- DOI: https://doi.org/10.48550/arXiv.2607.21619

### Authors

Bingjun Luo, Jialin Guo, Yue Yao, Xinpeng Ding

### Abstract

Multimodal Large Language Models (MLLMs) have achieved impressive performance, but their safety alignment remains vulnerable to jailbreak attacks. Existing content-based jailbreaks are often inconsistent and show unsatisfying performance against the rapidly evolving MLLMs, failing to exploit non-content-based vulnerabilities. Unlike previous research, we empirically find that MLLMs exhibit a Stylistic Inconsistency between their comprehension ability and safety ability: MLLMs can robustly understand content regardless of visual style, yet their defense mechanisms can be easily bypassed by specific stylistic triggers. Based on this finding, we propose Adversarial Style Optimization (ASO), a plug-and-play enhancement module to amplify existing visual jailbreaks. ASO fine-tunes an image-editing model to superimpose an optimized stylistic modification onto a given adversarial image, using a Group Relative Policy Optimization (GRPO) agent guided by a Structurally-Tiered Reward Function that combines a logit-based signal for detecting explicit refusals with a high-fidelity semantic evaluation from a powerful judge model. Extensive experiments show that ASO significantly enhances the ASR of SOTA attacks, demonstrating that stylistic biases are a scalable vector for red-teaming MLLMs. Our code is available at https://github.com/bingjunluo/ASO.

### 中文一句话结论  
本文发现多模态大语言模型存在“风格不一致性”漏洞，并提出对抗性风格优化（ASO）方法，借助GRPO强化学习微调图像编辑模型，显著提升现有视觉越狱攻击的成功率。

### English TL;DR  
ASO exploits the stylistic inconsistency of Multimodal Large Language Models by using GRPO-based reinforcement learning to fine-tune image style modifications, significantly enhancing the success rate of existing jailbreak attacks.

### 中文详细总结  
多模态大语言模型（MLLM）虽然性能优异，但其安全对齐仍易受到越狱攻击。现有基于内容的攻击难以稳定应对快速演化的模型，忽略了非内容层面的漏洞。本文通过实证发现MLLM存在“风格不一致性”：模型对视觉内容的理解能力稳健，但其防御机制却容易被特定视觉风格绕过。基于这一发现，文章提出**对抗性风格优化（ASO）**——一个即插即用的增强模块，可叠加至现有视觉越狱攻击上。ASO分两个阶段：首先通过风格敏感性探测确定目标模型最易感的视觉风格（如铅笔素描），然后利用**组相对策略优化（GRPO）**微调图像编辑模型（如FLUX-Kontext），使其在该风格参数空间中搜索最优修改。优化由**结构化分层奖励函数**引导，结合logit层面的显式拒绝检测与强评判模型的语义评估。广泛实验表明，ASO能够持续且显著提升多种基线攻击在多个安全对齐MLLM上的攻击成功率（ASR），证明风格偏差是一种可扩展的红队测试向量。

### 方法 / 贡献  
- **方法**：两阶段框架。阶段一（风格敏感性探测）对预设风格池（涵盖介质、几何、氛围、域风格四类）进行系统测试，选出对目标模型攻击效果最好的风格方向；阶段二（GRPO风格增强）以该风格为基础，使用GRPO算法对图像编辑模型进行强化学习微调，自动发现该风格内的最优参数（如笔触密度）以增强越狱。  
- **贡献**：  
  1. 首次系统识别并验证了“风格不一致性”作为MLLM的非内容安全漏洞。  
  2. 提出ASO这一即插即用的增强模块，采用结构化分层奖励函数有效应对高维稀疏奖励优化问题。  
  3. 实验证明ASO能一致且显著提升多种前沿攻击在多个安全对齐MLLM上的ASR，揭示了新的防御关注维度。

### 实验或数据  
实验基于现有基准攻击数据集（如FigStep、HADES、IDEATOR等）构建，并在多个前沿安全对齐多模态大语言模型（如LLaVA、Qwen3-VL、Gemini等，具体型号见原文）上评估。通过风格池探测筛选出最佳原始风格，再利用GRPO进行微调优化。论文未在摘要中给出具体数值，但全文展示了ASO在多个模型和攻击组合上显著提升ASR的详细结果。代码已开源。

### 值得关注点  
- 首次发现并利用MLLM的“风格不一致性”（理解稳健但防御易被风格绕过）这一非内容漏洞。  
- ASO是即插即用模块，可无缝增强现有攻击，无需重新生成对抗样本。  
- 提出的结构化分层奖励函数（logit拒绝信号 + 强评判模型语义评估）有效克服了风格优化的稀疏奖励问题。  
- 实验覆盖多种基线和模型，验证了风格偏差作为可扩展红队测试向量的有效性。

### 局限性  
根据所提供内容，论文未明确讨论局限性。基于方法特点，可能的局限性包括：对风格探测阶段所选风格（及风格池构成）的依赖性、GRPO强化学习微调的计算成本、以及该方法可能更容易被针对特定风格的防御策略所缓解。具体局限性需参阅原文讨论部分。

## 8. The Hard Decision Layer: Evidence for Committed Inference in Transformers

- Source: arxiv
- arXiv ID: 2607.21613
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.21613v1
- PDF: https://arxiv.org/pdf/2607.21613v1
- DOI: https://doi.org/10.48550/arXiv.2607.21613

### Authors

Ashwath Vaithinathan Aravindan, Mayank Kejriwal

### Abstract

We investigate where and how transformer-based language models commit to predictions in multiple-choice question answering. We identify the _Hard Decision Layer_ (HDL), a natural architectural property where answer option rankings stabilize abruptly during inference. Empirical validation across four language models (Qwen, Llama, Granite, Mistral) and four benchmark datasets demonstrates consistent HDL emergence without learned routing policies. We also show that the HDL is invariant to fine-tuning. Our results reveal striking accuracy improvements at the HDL: up to +0.61 (Qwen on CommonsenseQA), after which performance stabilizes. Systematic ablations on label formats and problem complexity confirm the phenomenon is fundamental to model architecture. These findings offer mechanistic insights into transformer inference and suggest opportunities for efficient reasoning and model steering. All code and results required to reproduce this work are available in https://github.com/Mystic-Slice/hard-decision-layer

### 中文一句话结论
本研究发现Transformer模型在多项选择问答中存在一个固有的“硬决策层”（HDL），该层之后答案选项的排名急剧稳定，且这一现象无需学习路由策略，在多个模型和数据集上一致出现。

### English TL;DR
The paper introduces the Hard Decision Layer (HDL), a natural architectural property in transformers where answer option rankings stabilize abruptly during inference, consistently emerging across models and datasets without learned routing and offering insights for efficient reasoning and model steering.

### 中文详细总结
论文通过分析Transformer模型在多项选择问答中的层间决策过程，发现了一个称为“硬决策层”（HDL）的架构特性：模型在某个固定层之后，各个答案选项的排名趋于稳定，不再发生大幅变动。研究者利用Logit Lens技术提取每一层的logit，并计算选项排名的变化率，定义HDL为排名下降最剧烈的层。实验在Qwen、Llama、Granite、Mistral四个模型（2B–8B参数）和CommonsenseQA、QASC、MMLU-Pro、SuperGPQA四个数据集上进行，均观察到HDL的稳定出现。HDL对微调（LoRA）保持鲁棒，且其显著性受选项标签形式影响：字母和阿拉伯数字标签比罗马数字标签产生更清晰的决策边界。HDL处模型准确率显著提升（最高达+0.61），之后趋于平缓。这些发现表明Transformer具备内在的推理组织结构，为高效推理和模型引导提供了潜力。

### 方法 / 贡献
- **识别硬决策层（HDL）**：定义并定位了Transformer内答案选项排名稳定性突变的自然层。
- **跨模型与数据集验证**：在四个不同规模和架构的模型及四个基准数据集上验证HDL的存在。
- **HDL对微调不变性**：通过LoRA微调后HDL位置依然保持，表明其源于架构本质特性。
- **标签格式的影响**：发现字母和阿拉伯数字标签比罗马数字标签产生更锐利的决策边界。
- **开源完整代码与结果**：提供可复现的GitHub仓库。

### 实验或数据
- **模型**：Mistral-7B-Instruct-v0.3、Llama-3.1-8B-Instruct、IBM Granite-3.3-2B-Instruct、Qwen3-4B-Instruct-2507。
- **数据集**：CommonsenseQA、QASC、MMLU-Pro、SuperGPQA；每个数据集中随机采样100个问题，并统一为四个选项。
- **微调实验**：对Qwen和Llama使用LoRA（秩r≪d）在单独训练集（8000–10000样本）上训练1个epoch。
- **任务变体**：在QASC上测试字母、阿拉伯数字、罗马数字三种标签格式，并改变选项数量。
- **实验度量**：各层准确率、平均排名变化、HDL检测。

### 值得关注点
- HDL作为Transformer固有的自然属性出现，无需学习路由或后处理剪枝。
- 在HDL处准确率跳跃可达+0.61（Qwen on CommonsenseQA），之后模型性能稳定。
- HDL对微调（LoRA）和选项数量具有不变性，表明其反映深层架构组织。
- 结果揭示了模型内在的“承诺推理”位置，为早期退出和高效推理提供思路。

### 局限性
- 研究仅限于多项选择问答（MCQA）场景，未涵盖开放式生成任务。
- 实验模型参数规模在2B–8B之间，在更大或更小模型上的泛化性有待验证。
- 每个数据集仅使用100个样本，结论在更大样本量下可能需进一步确认。
- 未探讨HDL在不同架构（如编码器-解码器）或非自回归模型中的表现。
- 标签格式影响的分析未覆盖所有可能的符号表示（如特殊字符）。

## 9. On Improving Faithfulness of Podcasts from Documents

- Source: arxiv
- arXiv ID: 2607.21961
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.21961v1
- PDF: https://arxiv.org/pdf/2607.21961v1
- DOI: https://doi.org/10.48550/arXiv.2607.21961

### Authors

Soumya Dutta, Tejas Indulal Dhamecha, Pannaga Shivaswamy

### Abstract

Large language models (LLMs) are increasingly used to generate long-form conversational content such as podcasts from textual sources. While these systems produce fluent and engaging narratives, they often introduce ungrounded information. In this work, we present the first systematic study of faithfulness in document-grounded podcast generation, where grounding must be maintained across conversational turns in long-form, multi-speaker transcripts. We construct a dataset of over 1500 documents spanning five domains and generate podcast transcripts using multiple LLMs. We introduce a turn-level LLM-as-a-judge framework for evaluating whether conversational turns are supported by the source document, and validate its reliability through human studies. Our analysis shows that even state-of-the-art models, including GPT-4o, frequently generate ungrounded content. To mitigate this issue, we propose catch-n-repair, a model-agnostic framework that detects and rewrites unfaithful conversational turns while preserving conversational flow. Experiments demonstrate consistent improvements in faithfulness across both in-domain and out-of-domain settings.

### 中文一句话结论
本文首次系统研究文档驱动播客生成中的忠实性问题，提出基于对话轮次的评估框架与模型无关的“捕捉-修复”策略，有效检测并改写不忠实内容，显著提升生成结果的忠实度。

### English TL;DR
This paper presents the first systematic study of faithfulness in document-grounded podcast generation, introducing a turn-level LLM-as-a-judge evaluation framework and a model-agnostic catch-n-repair mitigation method that detects and rewrites ungrounded conversational turns to consistently improve faithfulness across domains.

### 中文详细总结
大型语言模型正被越来越多地用于从文本源生成长形式、多人对话式播客内容，但常引入无依据信息。本文构建了一个覆盖五个领域、超过1500份文档的数据集，并使用多种LLM生成播客脚本。作者提出了一种基于对话轮次的LLM评判框架，用于评估每轮对话是否忠实于源文档，并通过人工研究验证其可靠性。实验表明，即便是GPT-4o等最先进模型，也频繁生成不忠实内容。为此，本文提出了一种模型无关的“捕捉-修复”策略，检测并改写不忠实的对话轮次，同时保持对话流畅性，在域内和域外设置中均显著提升了忠实度。

### 方法 / 贡献
- 提出首个针对文档驱动播客生成的忠实性系统研究，聚焦于长形式、多人对话场景。
- 构建包含1520份文档（覆盖五个领域）的数据集，并生成对应播客脚本。
- 设计基于对话轮次的LLM评判协议，评估每轮对话对源文档的忠实程度，并通过人工研究验证其可靠性。
- 提出“捕捉-修复”框架，该框架模型无关，可应用于开源和闭源模型，通过轻量分类器检测不忠实轮次并改写，提升忠实度。

### 实验或数据
本文构建了一个包含1520份文档的数据集，涵盖五个领域，并使用多种LLM（如GPT-4o）生成播客脚本。实验在域内和域外设置中评估了“捕捉-修复”策略的忠实度改进效果。数据集和具体实验细节（如与baseline的对比结果）在论文中详述。

### 值得关注点
- 聚焦于文档驱动播客生成中的忠实性问题，这是以往研究较少探讨的领域。
- 提出细粒度的对话轮次级评估，而非整体评估，能更准确地定位不忠实内容。
- “捕捉-修复”策略模型无关，实用性强，可同时应用于开源和闭源LLM。
- 实验覆盖多个领域和域外场景，验证了方法的泛化能力。

### 局限性
- 论文未明确说明实验中使用的人类评估者数量、标注者间一致性等细节。
- 覆盖度（coverage）不是主要优化目标，可能影响生成内容对原文关键信息的体现。

## 10. Do VLMs Read or Rewrite? On Transcription Faithfulness in Vision-Language Models

- Source: arxiv
- arXiv ID: 2607.21617
- Relevance: 3.9

### Links

- Abstract: http://arxiv.org/abs/2607.21617v1
- PDF: https://arxiv.org/pdf/2607.21617v1
- DOI: https://doi.org/10.48550/arXiv.2607.21617

### Authors

Gwang Gook Lee, Kenan Emir Ak, Jay Mohta, Yan Xu, Dimitrios Dimitriadis

### Abstract

Vision Language Models (VLMs) are increasingly used in place of traditional OCR pipelines for document understanding. In this paper, we show they do not always act as faithful transcribers: when text is imperfect, they often tend to rewrite it into a more plausible form - a behavior that clean-text OCR benchmarks cannot detect. We introduce FaithC4, a multilingual perturbation benchmark of 1,455 single-page documents (English, Chinese, Korean) with three perturbation families: scramble, random substitution, and visually similar substitution. We use the benchmark to evaluate 15 systems spanning general-purpose VLMs, OCR-specialized VLMs, and traditional OCR pipelines. These three categories differ in WER degradation under perturbation: general-purpose VLMs degrade by up to 4.5 points, OCR-specialized VLMs by 0.2-2 points, and traditional OCR by less than 0.6 points on English. Probing Qwen3-VL-4B layer-by-layer, we identify a consistent pattern: rewriting fires only when a perturbed word's final layer FFN representation stays close to the original encoding; when the representation diverges sufficiently, the model transcribes faithfully. Word length affects rewriting rate: short words (4-6 characters) are rewritten up to 10% of the time, with a sharp cutoff at 8 characters above which rewriting drops to 0%.

### 中文一句话结论
本文发现视觉语言模型在遇到不完美文本时倾向于将其重写为更合理的形式，而非忠实转录，这种行为在干净文本基准中无法检测，且重写频率受内部表示相似度和词长影响。

### English TL;DR
Vision-Language Models (VLMs) are increasingly used for document OCR, but they often "rewrite" imperfect text into plausible forms instead of faithfully transcribing it—a behavior not captured by clean-text benchmarks. The authors introduce FaithC4, a multilingual perturbation benchmark (1,455 documents, English/Chinese/Korean) with three perturbation types (scramble, random, visually similar). Evaluating 15 systems (general VLMs, OCR-specialized VLMs, traditional OCR) shows that general VLMs degrade up to 4.5 WER points under perturbation on English, while OCR-specialized and traditional OCR degrade less. Probing Qwen3-VL-4B reveals that rewriting occurs when the final-layer FFN representation of a perturbed word stays close to the original encoding, and short words (4–6 chars) are rewritten up to 10% of the time, dropping to 0% above 8 characters.

### 中文详细总结
本文研究视觉语言模型（VLM）在文档理解中的转录忠实性。作者指出，VLM 在输入文本有拼写错误、视觉伪影或字符不清晰时，往往输出其“期望看到”的内容而非实际文本，例如将“prbolem”转录为“problem”——这一行为类似于人类阅读中的“词形错误恢复”（typoglycemia），但传统 OCR 系统不会受其影响。为系统研究这一现象，作者提出多语言扰动基准 FaithC4，包含英语、中文、韩语共 1,455 份单页文档，应用三种字符级扰动：词内字母重排、随机替换、视觉相似替换。实验评估了 15 个系统，包括通用 VLM（如 Qwen3-VL、InternVL、GPT-5.4-mini 等）、OCR 专用 VLM（如 olmOCR、DeepSeek-OCR、MinerU 等）以及传统 OCR（Tesseract、docTR）。主要发现：通用 VLM 在英文扰动下词错误率（WER）最多上升 4.5 个百分点，OCR 专用 VLM 上升 0.2–2 个百分点，传统 OCR 上升小于 0.6 个百分点；该趋势在中文和韩语中类似，但最敏感的扰动类型因语种而异。通过逐层探测 Qwen3-VL-4B，作者发现重写行为仅在扰动词的最后一层前馈网络表示接近原始词的编码时发生；当表示偏离足够大时，模型则忠实转录。此外，词长显著影响重写率：4–6 字符的短词重写率高达 10%，而 8 字符以上词重写率降为 0%。扰动还具有非局部效应：仅扰动 4.7% 的词会导致周围未扰动词也出现错误。

### 方法 / 贡献
- **问题定义**：揭示 VLM 在文档理解中倾向于重写而非忠实转录的问题，该问题无法被现有的干净文本 OCR 基准检测。
- **基准构建**：提出 FaithC4——一个多语言（英语、中文、韩语）扰动基准，包含 1,455 份单页文档，三种扰动类型（scramble、random substitution、visually similar substitution），且以扰动后的文本作为真实标签，可直接测量转录忠实性。
- **系统评估**：对 15 个系统进行分类评估（通用 VLM、OCR 专用 VLM、传统 OCR），给出不同类别在扰动下的 WER 退化量化对比（通用 VLM 退化最大，传统 OCR 最鲁棒）。
- **机制分析**：通过逐层探测 Qwen3-VL-4B，定位重写行为的来源——最后一层 FFN 表示与原始编码的相似度决定是否重写；并发现词长对重写率的显著影响。
- **评估指标**：使用 WER（或中文 CER）和编辑距离相似度（EDS）从词级和字符级两个粒度评估转录忠实性。

### 实验或数据
- **数据集**：从多语言 C4 语料中采样，生成 1,455 份单页文档（英语 500、中文 500、韩语 455），每份文档渲染为 9pt 衬线字体、1.2 倍行高的 PDF 图像。对 8% 的词（英语）/ 8% 的 4 字符窗口（中文）/ 8% 的词（韩语）施加三种扰动，另保留未修改的原始版本作为基线。
- **模型**：共 15 个模型，分三类：
  - 通用 VLM：Qwen3.5-4B、Qwen3-VL-4B、InternVL3.5-4B、Gemma4-E4B/E2B、GPT-5.4-mini、Gemini-3-Flash、Gemini-2.5-Flash；
  - OCR 专用 VLM：olmOCR-2-7B、DeepSeek-OCR-2、MinerU2.5-Pro、PaddleOCR-VL-1.5、LightOnOCR-2-1B；
  - 传统 OCR：Tesseract、docTR。
- **评估指标**：词错误率（WER，中文为字符错误率 CER）和编辑距离相似度（EDS）。排除模型失败（拒绝、重复、语种不匹配）的文档后计算退化量（相对于原始基线的百分点变化）。
- **主要结果**：英语场景下通用 VLM WER 退化 0.74–4.45pp，OCR 专用 VLM 退化 0.23–2.32pp，传统 OCR 退化 <0.56pp。错误类型分析表明，通用 VLM 的“重写”（输出原始未扰动词）是主要错误类型，传统 OCR 几乎没有重写。扰动还具有非局部效应：扰动 4.7% 的词导致未扰动词错误率上升（从 3% 到 7%，VLM 最高达 18%）。

### 值得关注点
- **边界效应明确**：词长 8 个字符是重写行为的一个清晰阈值，短于 8 字符重写率显著，长于 8 字符降为 0%。
- **内部表征相关**：通过逐层探测发现重写行为与最后一层 FFN 表示是否接近原始编码高度相关，为理解重写机制提供了可验证的神经层面解释。
- **语言普适性**：该现象在英语、中文、韩语三种类型各异的文字中均存在，说明不是某一语种的特例。
- **非局部影响**：扰动不仅影响被扰动词本身，还扩散到周围未扰动词，暗示 VLM 可能利用语言先验修正局部信息后重建整个句子。
- **类别对比**：传统 OCR 几乎不受扰动影响，OCR 专用 VLM 介于中间，通用 VLM 最敏感，与语言先验强度一致，直观支持“语言先验导致重写”的假设。

### 局限性
未在摘要中明确提及局限性，但基于研究内容可推断：1）扰动类型有限（仅三种人工构造的字符级扰动，未覆盖真实世界的噪声如模糊、光照不均等）；2）探测仅针对 Qwen3-VL-4B 单一模型，重写机制的普遍性有待在更多模型上验证；3）仅涉及单页文档，长文档或多页场景的行为未知；4）未探讨如何缓解或控制重写行为以提升转录忠实性。

## Processing Notes

- Duplicate papers skipped: 0