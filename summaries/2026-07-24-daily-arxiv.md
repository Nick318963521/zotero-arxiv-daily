# Daily arXiv - 2026-07-24

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-24T23:28:40
- Paper count: 10

## 1. DataPrep-Bench: Benchmarking LLMs as Training Data Preparators

- Source: arxiv
- arXiv ID: 2607.20465
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.20465v1
- PDF: https://arxiv.org/pdf/2607.20465v1
- DOI: https://doi.org/10.48550/arXiv.2607.20465

### Authors

Hao Liang, Qifeng Cai, Yibo Lin, Jianzhuo Du, Qifeng Xia, Sizhe Qiu, Linzhuang Sun, Meiyi Qiang, Zhaoyang Han, Xiaochen Ma, Bohan Zeng, Ruichuan An, Conghui He, Wentao Zhang

### Abstract

The quality of training data fundamentally determines the capabilities of large language models (LLMs), yet no unified benchmark exists to measure how well LLMs, agents, and data-centric workflows actually prepare training data end to end. We view LLM-driven data preparation as comprising two complementary capabilities: data construction, which transforms raw sources into supervised training data, and data quality evaluation, which predicts the training value of candidate datasets before downstream training; throughout, "quality" refers to downstream training utility rather than surface-level textual properties. We introduce DataPrep-Bench, the first unified benchmark that jointly evaluates both capabilities under a shared downstream-grounded protocol over six domains and multiple base models. For data construction, methods consume identical raw sources and are scored by fine-tuning a base model on their outputs jointly with Dolly-15k; alongside this track we release Data-Construction-Skill, a skill-guided agent that lifts the Dolly-only baseline by nearly 20 points absolute on Llama-3.1-8B Finance and is competitive with the strongest agent- and DataFlow-based methods in knowledge-extraction-dense domains. For data quality evaluation, scoring functions are scored by Pearson correlation with downstream performance on a shared candidate pool; we release the Distributional Alignment Score (DAS), a distribution-based evaluator that uses MMD between a candidate dataset and a domain proxy. DAS attains the strongest cross-model correlation in four of six domains and is the only metric clearing r > 0.70 simultaneously in Math, Science, and Medical, outperforming existing quality-, diversity-, and heuristic-based evaluators. DataPrep-Bench provides a unified, downstream-grounded framework for measuring progress on both capabilities as co-equal targets of LLM-driven data preparation.

### 中文一句话结论
DataPrep-Bench 是首个统一基准，用于评估大语言模型在数据构建与数据质量评估上的端到端能力，并发布技能引导智能体 Data-Construction-Skill 与分布对齐评分 DAS 作为强基线。

### English TL;DR
DataPrep-Bench is the first unified benchmark that jointly evaluates LLMs on data construction and data quality evaluation under a shared downstream-grounded protocol across six domains. It introduces Data-Construction-Skill, a skill-guided agent that improves Dolly-only baselines by up to 20 points on Llama-3.1-8B Finance, and Distributional Alignment Score (DAS), a distribution-based evaluator that achieves the strongest cross-model correlation in four of six domains, outperforming existing quality- and diversity-based metrics.

### 中文详细总结
DataPrep-Bench 将 LLM 驱动的数据准备分解为两个互补能力：**数据构建**（将原始领域知识源转换为监督训练数据）和**数据质量评估**（在下游训练前预测候选数据集的训练价值）。基准覆盖六个领域（金融、法律、数学、科学、医学等）和多个基础模型，采用统一的下游验证协议。数据构建赛道：方法使用相同原始源，通过与 Dolly-15k 联合微调评估；发布的 Data-Construction-Skill 智能体在知识提取密集型领域（如金融）提升显著。数据质量评估赛道：评分函数与候选数据集上的下游性能进行 Pearson 相关性比较；发布的 DAS 基于最大均值差异 (MMD) 衡量候选数据集与领域代理的分布对齐，在数学、科学、医学上同时达到 r>0.70，且是唯一跨模型稳定性高的指标。实验发现三个关键结论：添加合成领域数据往往损害性能；无单一方法普遍最优；DAS 是最可靠的质量评估指标。

### 方法 / 贡献
- 提出 **DataPrep-Bench**：首个统一基准，联合评估数据构建与数据质量评估，共享领域、基础模型、训练协议和下游基准。
- 发布 **Data-Construction-Skill**：技能引导的智能体基线，通过可重用的技能层（输出模式、过滤规则、覆盖约束、验证工具）替代一次性提示，提升数据构建效果。
- 发布 **Distributional Alignment Score (DAS)**：基于分布对齐的评估器，使用 MMD 比较候选数据集与领域代理分布，在质量评估中表现最优。
- 提供候选数据集池及其真实下游性能记录，以及原始源语料库。

### 实验或数据
- 实验覆盖六个领域（金融、法律、数学、科学、医学等），使用多个基础模型（如 Llama-3.1-8B）。
- 数据构建赛道：在 Dolly-15k 基础上联合微调，评估模型在领域下游基准上的表现。Data-Construction-Skill 在 Llama-3.1-8B 金融领域提升绝对近 20 点。
- 数据质量评估赛道：构建共享候选池，通过 Pearson 相关性与下游性能对比。DAS 在四个领域取得最强跨模型相关性，且在数学、科学、医学上同时清除 r>0.70。
- 论文未提及具体数据集大小或统计细节，但公开了源代码、数据集和演示。

### 值得关注点
- **T1**：在 Dolly-15k 基础上添加合成领域数据常常损害下游性能，表明当前数据构建方法仍需改进。
- **T2**：没有单一方法普遍最优：DataFlow 方法在结构化领域（金融、法律）领先，智能体方法在推理密集型领域（数学、医学）占优，Data-Construction-Skill 在知识提取密集型领域最强。
- **T3**：DAS 是整体最可靠的质量评估指标，优于现有质量、多样性和启发式评估器，但金融和法律领域对所有指标仍具挑战。
- 基准提供统一的端到端测试平台，便于公平比较不同方法。

### 局限性
论文未明确讨论局限性，但基准目前仅覆盖六个领域和有限的基础模型，评估协议依赖 Dolly-15k 联合训练，可能限制其泛化性。此外，数据构建方法在不同领域的表现差异较大，金融和法律的质量评估仍不理想，说明基准范围有待扩展。

## 2. RE-AD: Real-Time Requirement Adherence for Data Labeling

- Source: arxiv
- arXiv ID: 2607.20455
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.20455v1
- PDF: https://arxiv.org/pdf/2607.20455v1
- DOI: https://doi.org/10.48550/arXiv.2607.20455

### Authors

Siddarth Malreddy, Ishan Nigam, Akshay Arora, Nikhil Mittal, Subrat Sahu

### Abstract

Human-annotated data remains fundamental to training frontier Large Language Models (LLMs). However, crowd-sourced annotations often suffer from quality issues stemming from annotator misunderstanding or lack of engagement. To address this, we introduce a real-time requirement adherence (RE-AD) framework that leverages LLMs to proactively validate labeling quality. Our methodology involves decomposing Standard Operating Procedures (SOPs) into atomic rules via self-reflection, categorizing them by complexity, and applying tiered validation strategies. Evaluated on a synthetic benchmark, the system achieved an F1 score of 0.749. Furthermore, production deployment resulted in annotators accepting and fixing 82% of the errors flagged by the framework. We include ablation studies to demonstrate the impact of our core design decisions.

### 中文一句话结论
本文提出RE-AD框架，利用大语言模型将标准操作程序（SOP）分解为原子规则并按复杂度分层验证，在人工标注中实现实时质量控制，合成基准F1达0.749，生产环境中82%的被标错误被标注者接受并修正。

### English TL;DR
RE-AD is a real-time framework that uses LLMs to decompose Standard Operating Procedures into atomic rules, categorizes them by complexity, and applies tiered validation strategies. It achieves an F1 of 0.749 on a synthetic benchmark and an 82% annotator acceptance rate for flagged errors in production.

### 中文详细总结
RE-AD（Real-Time Requirement Adherence）框架旨在解决众包标注中因理解偏差或投入不足导致的质量问题。传统质量保证（如后验审核）反应滞后且成本高。RE-AD将质量控制前移至标注过程，通过离线将非结构化SOP自反分解为原子规则（确保原子性与正交性），并按复杂度分为格式（Tfmt）、简单（Tsim）、主观（Tsub）三层。在线验证时，Tfmt采用确定性代码检查，Tsim使用轻量级LLM（如Gemini 3 Flash），Tsub使用高推理能力LLM（如Gemini 3 Pro）配合思维链提示。系统通过前缀缓存保持低延迟（约2.3秒）。在合成基准RE-AD-Eval上，系统整体F1为0.749；生产部署中，标注者接受了82%的被标错误并进行了修正。消融实验表明，逐规则并行验证相比整体批处理在延迟上有显著优势（2.3秒 vs 36.8秒），但主观层准确率略低于批处理（0.551 vs 0.612），说明原子化可能损失部分整体语境。

### 方法 / 贡献
- **递归约束原子化**：通过自反迭代将非结构化SOP分解为原子、正交的规则，并映射到三层复杂度层级。
- **复杂度感知验证管线**：生产级架构，采用逐规则并行验证、前缀缓存和自适应模型路由（从确定性代码到高推理LLM），平衡准确性与延迟。
- **系统评估**：构建合成基准RE-AD-Eval，包含20条规则、三种标注者技能水平及受控错误注入，同时进行消融实验比较逐规则验证与整体批处理。
- **影响分析**：大规模生产部署显示82%的被标错误被标注者接受并修正，显著减少审计开销。

### 实验或数据
- 合成基准RE-AD-Eval：由LLM生成20条规则的SOP（8条格式、5条简单、7条主观），生成干净对话后通过verify-and-repair注入错误，模拟专家、中级、新手三种标注者（错误概率5-25%/10-50%/20-75%），混合确定性代码和LLM验证建立真实标签。
- 主要结果：整体F1=0.749；按技能水平F1在0.737-0.767之间；按层级：Tfmt F1=1.000，Tsim F1=0.864，Tsub F1=0.551。
- 消融实验：逐规则并行验证p50延迟2.3秒，总F1=0.749；最好批处理（Gemini 3 Pro）延迟36.8秒，总F1=0.688，但Tsub F1更高（0.612）。
- 生产部署结果：标注者接受并修正82%的被标错误。

### 值得关注点
- 实时性：通过前缀缓存和并行验证实现2.3秒反馈，适合生产环境。
- 分层设计：确定性代码处理格式规则（F1=1.000），LLM处理语义规则，在准确性与效率间取得平衡。
- 实用效果：生产部署中标注者对82%的标记错误表示接受并修正，表明系统具有实际价值。
- 消融实验揭示原子化与整体评审判读的权衡：逐规则验证在格式类任务上明显优于批处理，但主观类规则可能损失整体语境。

### 局限性
- 主观规则（Tsub）准确率较低（F1=0.551），主要因语言歧义和解释差异，系统仅作为辅助信号而非自动拒绝闸门。
- 原子化可能剥离主观判断所需的整体语境，导致主观层准确率低于批处理方式（0.551 vs 0.612）。
- 合成基准可能无法完全代表真实场景的多样性，且未在不同领域SOP上测试泛化性。
- 论文未报告标注者接受错误修正后的实际质量提升量化指标，也未讨论系统对不同类型标注者的差异化影响。

## 3. PlanE: Meta Planning of Data, Tuning, and Inference for Extractive-based LLMs

- Source: arxiv
- arXiv ID: 2607.20470
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.20470v1
- PDF: https://arxiv.org/pdf/2607.20470v1
- DOI: https://doi.org/10.48550/arXiv.2607.20470

### Authors

Jiacheng Wang, Weiyan Zhang, Guangya Yu

### Abstract

Enhancing the task-specific capabilities of Large Language Models (LLMs) primarily requires substantial instruction-tuning datasets. However, the sheer volume of such data imposes a considerable annotation cost, and a lack of optimization methods for tailoring LLMs to specific tasks. To address the above issues, we propose a \textbf{Plan}ning framework for constructing \textbf{E}xtractive-based LLMs called \textbf{PlanE}, which includes data decomposition, instruction tuning, and prompt inference. Additionally, we introduce a Data-Tuning-Inference (DTI) planner, aimed at selecting the optimal base-LLM and its DTI combinations for specific datasets to improve construction efficiency. The experimental results demonstrate the effectiveness of our PlanE from two views: (1) across different datasets using the same base-LLM, and (2) on the same dataset using different base-LLMs. Furthermore, we validate the generalizability of the proposed DTI planner under different optimization objectives. The codes are publicly available at https://github.com/gugugu-469/PlanE.

### 中文一句话结论
PlanE 提出了一个元规划框架，通过数据分解、指令调优和提示推理的联合优化，并利用数据-调优-推理（DTI）规划器为特定数据集选择最优的基础大语言模型及其组合策略，从而高效构建抽取式大语言模型。

### English TL;DR
PlanE proposes a meta-planning framework that jointly optimizes data decomposition, instruction tuning, and prompt inference for extractive-based LLMs, using a Data-Tuning-Inference (DTI) planner to select the best combination of base-LLM and strategies for a given dataset.

### 中文详细总结
针对增强大语言模型（LLM）任务特定能力时，指令调优数据集规模大、标注成本高以及缺乏定制优化方法的问题，本文提出 PlanE 框架。该框架包含三个核心模块：数据分解（基于流水线和双向分解）、指令调优（监督微调 SFT 及 SFT+强化学习）和提示推理（直接推理、交集推理和并集推理）。此外，引入 DTI 规划器，通过元学习从历史执行数据中预测最优的 DTI 组合（即最佳的基座 LLM 与其数据、调优、推理策略组合），以提高构建效率。实验从两个角度验证了有效性：同一基座 LLM 在不同数据集上的表现，以及同一数据集上不同基座 LLM 的表现。同时，验证了 DTI 规划器在不同优化目标下的泛化能力。

### 方法 / 贡献
- **数据分解**：提出两种任务分解策略（流水线分解和双向分解），通过将复杂任务分解为串行原子子任务，提升每一步精度并减少错误传播。
- **指令调优**：采用两种调优策略：单一 SFT 以及 SFT+RL（包括 GRPO、DPO、KTO），以适应不同数据结构并进一步优化模型性能。
- **提示推理**：设计三种推理策略（直接推理、交集推理、并集推理），利用不同分解链的优势，聚合结果以提升准确性。
- **DTI 规划器**：构建基于参数化排序模型的规划器，通过元学习从历史数据中学习，自动为给定数据集和基座 LLM 选择最优的 DTI 组合，并支持多目标优化（平衡性能与效率）。

### 实验或数据
论文在三个任务数据集上进行了广泛实验：关系抽取（RE）、事件抽取（EE）和基于方面的情感分析（ABSA）。实验从两个视角评估：同一基座 LLM 在不同任务数据集上的效果，以及同一数据集上不同基座 LLM 的效果。此外，还验证了 DTI 规划器在不同优化目标（如性能效率平衡）下的泛化能力。

### 值得关注点
- **整合优化视角**：从数据、调优、推理三个阶段的联合优化角度设计框架，而非孤立优化单一环节。
- **动态组合选择**：DTI 规划器能够根据具体任务和基座模型自动预测最优组合，提高了构建效率。
- **多目标平衡**：规划器不仅追求性能（如 F1 分数），还能兼顾构建效率，实现多目标优化。

### 局限性
论文指出当前研究对象仅限于抽取式（extractive-based）任务（如 RE、EE、ABSA），框架在生成式任务上的泛化性有待进一步验证。此外，DTI 规划器依赖历史执行数据的积累，对于全新任务或模型的冷启动场景可能效果有限。实验中未详细说明数据集的具体规模及组成，也未提及模型大小的范围限制。

## 4. KeySI: An Interaction Framework for Tuning Text Embeddings Based on Human Feedback

- Source: arxiv
- arXiv ID: 2607.20556
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.20556v1
- PDF: https://arxiv.org/pdf/2607.20556v1
- DOI: https://doi.org/10.48550/arXiv.2607.20556

### Authors

Yan Zhu, Y. Chen, Rebecca Faust

### Abstract

In large-scale text analysis tasks, pre-trained language models are often used to embed text corpora for downstream analysis. However, such models may struggle to capture domain-specific semantics and adapting them typically requires large amounts of labeled data and technical expertise to implement training pipelines. Recent approaches have demonstrated how visual interactions in document projections can capture human feedback as training signals for model tuning. However, these methods operate on document-level feedback, which requires users to open and assess individual documents in order to provide effective feedback. In this paper, we propose KeySI, an interaction framework that enables feature-level feedback through keyword-based concept specification. Users specify feedback by organizing extracted keywords into groups representing concepts, which KeySI translates into document-level supervision for subsequent tuning. By operating on keywords as the primary interaction medium, KeySI reduces the need for manual document inspection and labeling and lowers the barrier to adapting embedding models. We present a prototype implementation that, given a corpus, curates representative keywords, visualizes keywords and document embeddings via dimensionality reduction, allows interactive specification of keyword groups, and supports iterative refinement through system feedback. We evaluate KeySI through a user study, usage scenarios, and quantitative experiments demonstrating its effectiveness in capturing user intent and improving embedding alignment.

### 中文一句话结论  
KeySI 通过关键词级别的交互框架，让用户以组织关键词组的方式表达语义概念，从而减少文档级标注开销，实现对文本嵌入模型的有效调优。

### English TL;DR  
KeySI is a keyword-based interaction framework that reduces manual document inspection by allowing users to tune text embeddings via organizing extracted keywords into concept groups, which are then translated into document-level pseudo-supervision for model adaptation.

### 中文详细总结  
KeySI 提出了一种基于关键词的语义交互框架，用于调优文本嵌入模型。传统方法依赖文档级反馈（如直接操作文档投影），用户需逐一打开和评估文档，开销大且难以直接表达高层语义概念。KeySI 将交互入口从文档级提升至特征级（关键词）：系统通过关键词提取和可视化，让用户将关键词分组为语义概念，并自动将这些关键词组转化为文档级伪监督信号（通过检索相关文档和语义去噪），用于后续模型微调。该方法降低了用户对文档手工标注和技术专家的依赖，使非专家也能调优嵌入模型。系统原型包含关键词提取、降维可视化、交互式关键词分组、迭代优化等功能。评估通过用户研究、使用场景和定量实验展开，验证了其在捕捉用户意图和改进嵌入对齐方面的有效性。

### 方法 / 贡献  
1. **关键词驱动的语义交互框架**：将文本嵌入调优的交互入口从文档级迁移至关键词级，减少文档检查开销。  
2. **反馈翻译流程**：整合关键词提取、文档检索、基于间隙的语义去噪等技术，将关键词组反馈转化为可训练的文档级伪监督。  
3. **实证证据**：通过用户研究、场景分析和定量实验，证明关键词级交互能降低概念指定成本，并提升嵌入结构与用户意图的对齐程度。

### 实验或数据  
- **用户研究**：考察用户如何利用关键词级交互表达语义意图并调优嵌入，同时与 DeepSI 的文档级交互进行对比，显示关键词级交互的手动开销更低。  
- **使用场景**：在真实数据集（如 COVID-19 论文摘要）上演示 KeySI 整合用户意图的能力。  
- **定量实验**：评估关键词级交互产生的监督信号是否足以有意义地重构嵌入空间。

### 值得关注点  
- **交互成本降低**：用户无需打开或标注单个文档，仅通过关键词分组即可表达概念，特别适合早期探索性分析。  
- **概念明确性**：关键词直接对应语义特征，比通过文档间接表达概念更清晰、更易形成。  
- **迭代优化**：支持用户反复调整关键词组，系统实时反馈更新嵌入投影，形成闭环改进。

### 局限性  
摘要未明确讨论局限性；根据论文上下文，KeySI 依赖自动关键词提取的质量，可能无法覆盖所有用户关心的概念，且原型仅针对文本数据，未验证在其他模态（如图像、表格）上的适用性。此外，用户仍需通过文档查看辅助验证，完全无文档交互的场景下可能影响反馈准确性。

## 5. REGARD: Regional Affective Differences in Large Language Models

- Source: arxiv
- arXiv ID: 2607.20722
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.20722v1
- PDF: https://arxiv.org/pdf/2607.20722v1
- DOI: https://doi.org/10.48550/arXiv.2607.20722

### Authors

Andrei Chetvergov, Alexander Evseev, Mikhail Solovev, Timofei Sivoraksha, Stepan Ukolov, Valeriia Kuschenko, Maria Chistyakova, Sergey Bolovtsov

### Abstract

Large language models trained and aligned within different linguistic and regional ecosystems may frame the same political, cultural, and geopolitical entities in different ways. Such differences are often evaluated through sentiment, favorability, or stance, reducing model attitudes to a single positive-negative axis. We introduce REGARD, a study of what drives affective framing differences across LLMs on post-Soviet entities using target-directed Valence-Arousal-Dominance profiling. We query 19 models on 500 region-specific targets, score their responses with two independent LLM judges, GPT-4o-mini and Qwen3.6-35B-A3B, and validate the measurements on a 300-item human-annotated subset. Post-hoc Ward-linkage clustering of all 19 models by affective and response-behavior profiles yields three behavioral clusters that cut across model origin, family, and parameter count. Generic-answer rate is strongly associated with lower arousal (r = -0.81) and with cluster placement: models that deflect evaluative prompts with templated responses cluster together at low arousal regardless of origin. These findings show that VAD profiling captures emotional intensity, a dimension of affective framing that is largely invisible to conventional sentiment-based evaluation.

### 中文一句话结论
REGARD 使用 Valence-Arousal-Dominance（VAD）框架揭示，大语言模型对后苏联实体的情感框架差异主要由回答行为（如泛化回答率）驱动，而非模型来源，并捕捉到传统情感分析无法体现的情绪强度维度。

### English TL;DR
REGARD uses Valence-Arousal-Dominance profiling to show that LLMs' affective framing of post-Soviet entities is driven by response behavior (e.g., generic-answer rate) rather than model origin, capturing emotional intensity dimensions invisible to conventional sentiment evaluation.

### 中文详细总结
本研究提出 REGARD，通过目标导向的 Valence-Arousal-Dominance（VAD）分析，系统比较 19 个大语言模型在 500 个后苏联相关实体（涵盖人物、组织、事件、文化符号、社会群体和国家）上的情感框架差异。模型生成响应由两个独立的 LLM 裁判（GPT-4o-mini 和 Qwen3.6-35B-A3B）在三个 VAD 维度上评分，并在 300 项人工标注子集上验证。研究发现：情绪唤醒（Arousal）是主要变化维度（范围 0.34–0.58），而效价（Valence）范围较窄（0.61–0.76）。通过后验 Ward 链接聚类，所有模型按情感与行为轮廓被分为三个行为簇，这些簇跨越模型来源、家族和参数规模。泛化回答率与低唤醒度强相关（r = -0.81），且与簇归属密切相关：倾向于使用模板化回答回避评价的模型（无论来源）聚集在低唤醒度簇中。VAD 轮廓分析揭示了传统情感评价无法捕捉的情绪强度维度。

### 方法 / 贡献
方法：构建 CIS-Affective-500 实体库（500 个 Wikidata 锚定实体，覆盖 12 个后苏联国家），使用三种俄语提示变体查询 19 个生成模型（参数 7B–27B）。设计“裁判合约”将 VAD 评分操作化为 [0,1] 连续值，由两个不同家族（开放权重 vs. API）的 LLM 执行评分，避免直接自我评估。在 300 项人类标注子集上验证评分可靠性，并采用后验聚类分析模型行为。
贡献：引入目标导向 VAD 框架用于 LLM 情感框架比较，发现泛化回答率是比模型来源更重要的情感差异驱动因素，并证明 VAD 能够揭示传统情感分析（仅极性）所忽视的情绪强度维度。

### 实验或数据
实验：对 19 个模型（YandexGPT, GigaChat, T-pro-it-2.1, AVIBE, GLM-4.7, Gemma-4-26B, Qwen2.5-14B 等）在 500 个实体上以温度 0.7 生成响应（共 28,500 条），每个响应由两个裁判评分（共 57,000 评分对）。使用 300 项人工标注子集（15 名标注者，900 个评分）进行验证。数据：CIS-Affective-500 数据集，包含 6 类实体（人物 30%、文化符号/地点 22%、组织 16%、社会群体 15.6%、事件 14%、国家 2.4%），国家覆盖均匀（每国 39–45 实体）。实体来源包括 Wikidata（高显赫度）和 UNESCO 非物质文化遗产/世界遗产列表。

### 值得关注点
- 三大行为聚类完全不受模型来源、家族或参数规模约束，仅由情感与行为轮廓决定。
- 泛化回答率与唤醒度强负相关（r = -0.81），是聚类的主导因素：逃避性模型聚集于低唤醒区间。
- VAD 框架成功捕捉情绪强度（Arousal）这一传统情感分析（仅极性）完全无法区分的维度，例如“平静支持”与“热情支持”被正确区分。
- 使用两个不同家族（开放权重 vs. API）的 LLM 裁判，减少单一供应商偏差，并在人类验证上支持可靠性。

### 局限性
- 研究局限于后苏联实体和俄语提示，结论的泛化性（如其他语言或文化区域）未验证。
- LLM 裁判可能存在系统性偏差（尽管通过两个独立裁判和 300 项人工验证缓解）。
- 仅使用三种提示变体，未探索更广泛的提示设计对环境的影响。
- 人工验证样本量较小（300 项），且标注者文化背景可能引入特定偏差。
- 文中未详细讨论其他潜在局限性（如实体选择偏差、温度设置敏感性等）。

## 6. Detecting LLM-Generated Tokens in Human--LLM Coauthored Text

- Source: arxiv
- arXiv ID: 2607.21458
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.21458v1
- PDF: https://arxiv.org/pdf/2607.21458v1
- DOI: https://doi.org/10.48550/arXiv.2607.21458

### Authors

Yangjun Lu, Hongyi Zhou, Fabian Spill, Kai Ye, Chengchun Shi, Jin Zhu

### Abstract

The rise of human-AI collaborative writing has created a growing need for fine-grained detection methods that support localizing likely LLM-generated content in mixed-authorship documents. Existing methods for detecting LLM-generated text mainly focus on document-level classification and cannot identify which parts of the text are generated by LLMs. This paper introduces a new method to address this urgent need. Our method operates at the token level, the natural unit of modern language models, and builds on existing token-level detection scores. The key idea is to smooth adjacent token scores to reduce their variability, while using an adaptive Lepski-type rule to select the bandwidth according to the local authorship structure. Our method is simple to implement and does not require token-level labeled data for training. Theoretically, we characterize this trade-off and show that the proposed method achieves favorable mean square error performance in estimating the underlying signal. Empirically, we demonstrate strong performance of our method against a wide range of baselines in both synthetic datasets and a realistic dataset. We deploy a publicly accessible website that implements the methods as well.

### 中文一句话结论  
本文提出一种基于自适应核平滑的令牌级检测方法，无需令牌级标注数据，即可在人类与LLM合著的文本中定位LLM生成的令牌，综合性能优于现有基线。

### English TL;DR  
This paper introduces a token-level method that applies adaptive kernel smoothing to existing detection scores to identify LLM-generated tokens in human–LLM coauthored text. It does not require token-level labeled data and outperforms various baselines in both synthetic and realistic settings.

### 中文详细总结  
本文针对人类与大型语言模型（LLM）合作写作场景中，需在混合作者文本中定位LLM生成内容的迫切需求，提出了一种令牌级检测方法。现有方法多为文档级分类，无法识别文本中具体哪些部分由LLM生成。该方法在令牌级别操作，利用现有令牌级检测分数，通过核平滑技术对相邻令牌分数进行加权平均以降低噪声，并采用自适应Lepski型规则根据局部作者结构选择平滑带宽。方法实现简单，无需令牌级标注数据。理论分析表明，所提方法在估计底层信号时能达到较低的均方误差。实验在合成数据集和真实数据集上均表现优异，并部署了可公开访问的实现网站。

### 方法 / 贡献  
- **方法**：提出基于核平滑的令牌级检测方法，对相邻令牌的检测分数进行加权聚合，并使用Lepski型自适应规则选择局部带宽，无需令牌级标注数据。  
- **理论贡献**：推导了带宽相关的偏差-方差权衡上界，并证明了自适应带宽选择规则在假设条件下具有类oracle性质。  
- **实践贡献**：发布公开在线分析网站，提供实际案例验证（在人类与LLM合著的摘要中达到94%令牌级准确率）。

### 实验或数据  
实验在四个数据集、四种语言模型和三种人类-LLM合作模式下进行，包含合成数据集和真实人类-LLM合著数据集。消融实验验证了邻近令牌聚合和自适应带宽选择对性能均有正面贡献。与多种基线对比，所提方法在令牌级排序性能上显著提升。

### 值得关注点  
- 方法无需令牌级标注数据，降低应用成本。  
- 实现简单，可直接基于现有令牌级检测分数进行后处理。  
- 自适应带宽选择有效平衡偏差与方差，适应局部作者结构变化。  
- 公开网站支持实际案例分析，便于推广验证。

### 局限性  
论文未明确讨论以下潜在局限：  
- 方法对检测分数本身的敏感性（若基础分数弱，平滑后改进有限）。  
- 未在极端低资源或跨语言场景下测试。  
- 公开网站仅部署方法，未提供大规模用户评估或实时性能分析。  
- 理论分析依赖于分数可分离性假设，若假设不成立则性能可能下降。

## 7. More Is Not More: What Matters for Diversity in LLM Opinions?

- Source: arxiv
- arXiv ID: 2607.20429
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.20429v1
- PDF: https://arxiv.org/pdf/2607.20429v1
- DOI: https://doi.org/10.48550/arXiv.2607.20429

### Authors

Qiyang Yao

### Abstract

Large language models are increasingly used to simulate diverse human opinions in open-ended tasks such as synthetic surveys, focus group modeling, and public opinion prediction. However, LLM outputs exhibit systematic opinion homogenization. Practitioners have explored various interventions to increase diversity, but the landscape remains fragmented: different methods are evaluated in isolation with incomparable metrics, and in practice they are typically deployed and upgraded simultaneously, making it difficult to attribute gains to specific components. To advance a more scientific understanding of LLM output diversity, we design a factorial experiment that separates two primary intervention dimensions: input conditioning (operationalized through persona depth) and interaction architecture. We evaluate all conditions on 100 real-user open-ended questions across 7 models, measuring diversity with multiple complementary metrics. Our findings challenge several common assumptions. First, more persona detail does not monotonically increase diversity. The initial step of persona conditioning already captures the majority of the gain, while further elaboration with demographic detail does not consistently improve and can reduce diversity on some models. Second, rather than seeking a single best interaction architecture, we find that different architectures explore largely non-overlapping opinion regions. Combining multiple architectures yields broader coverage than optimizing any one. Third, commonly attempted low-cost alternatives such as raising sampling temperature and adding diversity instructions produce negligible effects compared to structured interventions. Overall, our work demonstrates that diversity is not a product of scaling along any single dimension, but is highly sensitive to the structural form and combination of interventions.

### 中文一句话结论
更多个性细节或复杂交互架构并不能单调增加LLM观点多样性；多样性最佳通过结构化组合简单干预实现，不同架构探索互补意见空间，低成本技巧效果甚微。

### English TL;DR
Adding more persona detail or complex interaction architectures does not monotonically increase LLM opinion diversity; instead, diversity is best achieved through structured combinations of simple interventions, as different architectures explore complementary opinion spaces and low-cost tricks like higher temperature have negligible effects.

### 中文详细总结
本研究通过因子实验系统评估影响LLM观点多样性的两个关键维度：输入条件（个性深度）和交互架构，同时测试了提高温度、增加多样性指令等低成本技巧。在100个真实用户开放问题、7个不同模型、19种实验条件下，主要发现：1）个性细节收益递减——单句角色描述已捕获大部分多样性增加，进一步添加人口统计细节甚至可能降低部分模型的多样性；2）不同交互架构探索非重叠的意见区域，组合架构比优化单一架构覆盖更广；3）低成本技巧（提高温度、多样性指令、人口统计关键词提示、性格分配）效果远弱于结构化干预。研究表明，多样性并非沿单一维度缩放的结果，而高度依赖于干预的结构形式和组合。

### 方法 / 贡献
1. 将观点多样性问题归因于输入条件与交互架构，设计因子实验独立分离这两个维度。
2. 构建可复用的评估协议：包括原子意见提取、α-多样性（MPD, Cluster Count, Vendi Score）和β-多样性（β-Vendi Score, Unique Cluster Ratio）指标，支持不同干预间的可比比较。
3. 系统实证：在100个问题、7个模型、19个条件下，揭示个性深度收益递减、交互架构互补性、低成本技巧效果有限等结论，并开放评估协议供复现。

### 实验或数据
- 任务：100个开放问题，选自WildChat真实用户查询，涵盖AI伦理、社会规范、宗教文化、性别政治、经济体系等易产生分歧的领域。
- 模型：7个不同提供商的聊天模型，统一生成参数（温度0.7，top-p 1.0，最大输出4096 tokens，无频率或存在惩罚）。高温条件除外。
- 实验条件：因子设计包含5级个性深度（None, Role, Basic, Mid, Pro）× 3种交互架构（Single-Call, Multi-Turn Self-Prompting, Multi-Agent Discussion），共15个主条件，加上4个低成本技巧条件（Enhanced Prompt, High Temperature, Demographic Cueing, Trait Assignment），总计19个条件。
- 评价：提取原子意见后嵌入（text-embedding-3-small），计算α-多样性和β-多样性指标。通过分层抽样验证提取可靠性（语义Jaccard 0.948，人类标注准确率98.2%），嵌入选择稳定性（Spearman ρ 0.88–0.96）。

### 值得关注点
- 反直觉发现：更多个性细节并不一定带来更多多样性，单句角色描述已足够，过度细化反而可能有害。
- 不同交互架构探索互补意见空间，组合使用比优化单一架构更有效，挑战了寻找“最佳”架构的直觉。
- 低成本技巧（提高温度、多样性指令等）效果微弱，远不如结构化干预，提示从业者应重视干预的“形式”而非“强度”。

### 局限性
本研究未涵盖辩论或角色冲突等交互架构，个性描述基于固定人物集（20个角色），可能限制多样性上限；问题来源限于单一聊天数据集（WildChat），可能未覆盖所有意见分歧类型。此外，仅评估了7个模型，结论能否推广至其他模型或更大规模的人格库有待验证。

## 8. Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks

- Source: arxiv
- arXiv ID: 2607.21482
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.21482v1
- PDF: https://arxiv.org/pdf/2607.21482v1
- DOI: https://doi.org/10.48550/arXiv.2607.21482

### Authors

Mack Nixon, Liam Wright, Yevgeniya Kovalchuk, Alison Fang-Wei Wu, Martin Danka, Andy Boyd, David Bann

### Abstract

Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models. Their adoption in research using personal data is constrained by governance requirements that typically prohibit data transmission to external services. Locally deployable open-weight models offer an alternative since sensitive data never leave the local environment. We introduce an open-source framework for evaluating the efficacy of AI agents powered by open-weight LLMs on one of the most persistent bottlenecks in research on longitudinal population studies: data preparation. The framework comprises: a curated ground-truth dataset (cleaning scripts preparing six sweeps of data from a British cohort study), task definitions encompassing tasks such as category harmonization and multi-wave merging, and automated routines for evaluating the LLM-produced R code and outputted data. We benchmark LLMs across the (consumer grade) deployment spectrum to assess their efficacy in 20 data preparation tasks (creation of 102 variables). Current state-of-the-art, 31-35B parameter models almost saturated our benchmark ("average task completion" up to 87.9%). The performance of open-weight LLMs running on consumer-grade hardware shows promise of a viable path toward AI-assisted data preparation in governance-restricted research settings. Our framework is publicly available at: https://github.com/UCL-ARC/RRBench.

### 中文一句话结论
本研究表明，部署在消费级硬件上的开放权重大语言模型（最高350亿参数）在纵向数据准备任务上可达到接近饱和的性能（平均任务完成度达87.9%），为受数据治理限制的研究环境提供了可行的AI辅助编码路径。

### English TL;DR
This paper introduces RRBench, an open-source framework to evaluate locally deployable open-weight LLMs on longitudinal data preparation tasks (20 tasks, 102 variables from a British cohort study). Benchmarking eight models on consumer-grade hardware shows that 31-35B parameter models achieve up to 87.9% average task completion, demonstrating a viable path for AI-assisted coding under strict data governance that prohibits cloud data transmission.

### 中文详细总结
本文针对研究中使用个人数据时数据治理限制（禁止向云服务传输数据）的挑战，评估了本地可部署的开放权重大语言模型在纵向队列研究数据准备任务上的表现。作者开发了开源框架RRBench，包含：来自英国Next Steps队列研究六个波次数据的真实清洗脚本作为基准真相；20个任务（涵盖类别统一、多波合并等，需创建102个变量）；自动化评估R代码及输出数据的流程。在消费级硬件上评估了8个模型（从8B到35B参数）。结果显示，当前最优的31-35B参数模型（如Gemma 4 31B和Qwen3.6-35B-A3B）几乎饱和该基准：平均平衡性能分别为85.9%和81.7%，完全完成任务比例达75%和73.3%，最高平均任务完成度达87.9%。开放权重模型在消费级硬件上的表现显示出在治理受限环境中实现AI辅助数据准备的可行路径。框架已公开于GitHub。

### 方法 / 贡献
- **方法**：基于Next Steps队列研究构建基准，包含20个数据准备任务（如变量衍生、类别统一、多波合并）及对应的人类编写验证脚本。使用Hugging Face的SmolAgents代理框架，让LLM在本地环境迭代生成并执行R脚本。通过比较输出数据集与基准数据集，采用完整性（变量存在比例）、正确性（单元格匹配阈值≥95%或归一化RMSE<1e-4）和平衡指标（两者乘积）评估性能。
- **贡献**：(1) 创建了首个针对纵向健康/社会科学调查数据准备的领域特定基准，反映真实数据准备步骤；(2) 系统比较了不同规模（8B–35B）开放权重LLM的性能差异，指出主要瓶颈在正确性而非完整性；(3) 提供开源可扩展评估流水线，支持研究者根据自身数据、任务和治理环境进行适配。

### 实验或数据
- **实验**：评估8个满足条件（上下文窗口≥100k tokens、近12个月内发布）的开放权重LLM（包括Qwen3.6-35B-A3B、Gemma 4 31B、Ministral-3-14B等），在消费级硬件（单24GB GPU或16GB+笔记本）上执行20个任务，每个任务重复3次（温度0.8）。使用详细提示和简化提示两种条件，并进行了阈值敏感性和缺失值排除等敏感性分析。
- **数据**：基准数据来自Next Steps纵向队列（受访者14–32岁），包含6波调查数据。共20个任务，需创建102个变量（涉及人口学、教育、健康、社会经济等常见领域）。人类编写的清洗脚本经独立代码验证，作为真实基准。

### 值得关注点
- 开放权重模型在消费级硬件上能达到接近前沿封闭模型的效果（31-35B参数模型平均任务完成度达87.9%），为数据治理严格的研究环境提供了实用方案。
- 框架完全开源（https://github.com/UCL-ARC/RRBench），支持研究者自定义评估不同数据集和任务，促进可复现性。
- 研究发现模型间主要差异在于正确性而非完整性：几乎所有模型都能创建95%以上预期变量，但正确性从55.1%到86.2%不等。
- 额外进行了下游回归分析验证数据准备质量对实际研究的影响。

### 局限性
- 仅基于英国Next Steps一个队列，任务和数据特征可能不完全代表其他纵向研究或不同类型的数据准备需求。
- 主要使用详细提示（含明确编码逻辑），可能高估模型在真实应用中的自主推理能力；简化提示条件下性能显著下降。
- 仅评估R语言，未覆盖Python等其他研究人员常用语言。
- 仅评估单次代理通过（每个任务运行3次），未考虑多人协作或多次迭代改进的场景。
- 轻量模型（如Gemma 4 E4B，8B参数）在所有任务中完全失败，提示某些消费级硬件上的小模型尚不适用于此类复杂数据准备。

## 9. A Unified Moral-Value Dataset for Instruction Tuning

- Source: arxiv
- arXiv ID: 2607.21279
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.21279v1
- PDF: https://arxiv.org/pdf/2607.21279v1
- DOI: https://doi.org/10.48550/arXiv.2607.21279

### Authors

Zhaohui Zeng, Florian Mai

### Abstract

Large language models (LLMs) have developed rapidly and become valuable tools in everyday life. However, how to align LLMs to a particular set of human values is still an open problem. Recent studies show that instruction tuning has strong potential for zero-shot tasks and may serve as an effective approach to addressing value alignment. Nevertheless, although many datasets for instruction tuning already exist, they are not specifically designed around moral scenarios and behaviors. We construct a unified moral-value dataset that can be directly used for instruction tuning. This dataset is built upon existing moral-value datasets by merging them into a unified corpus and converting them into an instruction-response format. We show that training on a mixed dataset combining general task datasets with our dataset preserves general-task performance, and we report preliminary observations on how the mixing ratio affects value-oriented task performance. Our work provides a moral-value dataset for instruction tuning and offers a useful resource for further alignment research. The dataset is available at https://huggingface.co/datasets/teohzzh/value-for-instruction-tuning.

### 中文一句话结论
该论文通过融合多个现有道德价值数据集，构建了一个可直接用于指令微调的统一数据集，并初步探索了数据混合比例对模型价值对齐性能的影响。

### English TL;DR
This paper introduces a unified moral-value dataset for instruction tuning, constructed by merging ETHICS, UNIMORAL, and SOCIAL‑CHEM‑101 into a consistent instruction–response format, and shows that combining it with general‑task data preserves general performance while the mixing ratio affects value‑oriented task outcomes.

### 中文详细总结
大语言模型（LLM）在日常生活中有广泛应用，但如何使其与人类价值观对齐仍是一个开放问题。指令微调在零样本任务上表现出潜力，可能为价值对齐提供有效途径，但

## 10. Learn2Zinc: Fine-tuning Small Language Models for Text-to-Model Translation in MiniZinc

- Source: arxiv
- arXiv ID: 2607.20456
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.20456v1
- PDF: https://arxiv.org/pdf/2607.20456v1
- DOI: https://doi.org/10.48550/arXiv.2607.20456

### Authors

Serdar Kadioglu, Karthik Uppuluri

### Abstract

Large language models excel at code generation for mainstream programming languages but struggle with rare, domain-specific languages such as MiniZinc, a constraint modeling language for combinatorial problems. We investigate whether targeted fine-tuning can teach small language models (0.6B to 20B parameters) to generate syntactically correct and semantically valid MiniZinc models from natural language problem descriptions. Our key finding is that syntax errors dominate failures when working with this domain specific language: the out-of-the-box execution accuracy of small language models such as Qwen3, LLaMa, Gemma, and GPT-OSS is near-zero. We propose a cross-model error bootstrapping approach that collects syntax errors from multiple LLM runs and leverage those to curate an error correction training dataset. This dataset allows us fine-tune small language models that consistently improves both direct code generation and chain-of-thought approaches across all model sizes. With self-reflection and ensembling, our approach achieves up to 98\% execution accuracy. In parallel, solution accuracy still remains at 35\%, indicating that while syntax is learnable, constraint reasoning remains a challenge. We contribute our fine-tuning pipeline, datasets, and models to opens-source for further research on text-to-model translation.

### 中文一句话结论
通过跨模型错误自助法构建纠错训练数据，微调0.6B至20B参数的小语言模型，能使MiniZinc代码执行准确率从近乎零提升至98%，但求解准确率仅35%，表明语法可学习而约束推理仍是难题。

### English TL;DR
Fine-tuning small language models (0.6B–20B) on a bootstrapped error-correction dataset raises MiniZinc execution accuracy from near-zero to 98%, yet solution accuracy plateaus at 35%, revealing that syntax is learnable but constraint reasoning remains challenging.

### 中文详细总结
本研究针对小语言模型在领域特定语言MiniZinc代码生成上的严重语法错误问题，提出跨模型错误自助法：收集多个LLM运行产生的语法错误，构建纠错训练数据集，并微调Qwen3、LLaMA、Gemma、GPT-OSS等0.6B至20B参数的模型。微调后，直接代码生成与思维链方法在所有模型规模上均持续改进。结合自我反思与集成策略，执行准确率最高达98%。然而，求解准确率仅35%，表明模型虽能学会语法，但缺乏对约束推理的深度理解。研究开源了微调流程、数据集和模型。

### 方法 / 贡献
1. 首次系统研究微调0.6B–20B小语言模型用于MiniZinc代码生成。
2. 提出跨模型错误自助法，从多LLM运行中收集语法错误，构建逼真的纠错训练数据集。
3. 提出三种渐进的微调策略（基础、思维链、混合），并证明纠错数据增强在所有模型规模上优于直接生成和思维链方法。
4. 集成微调模型达到98%执行准确率；贡献8,014条指令微调对。
5. 开源所有代码、模型（0.6B/1B/3B/9B/20B）和数据集。

### 实验或数据
- 数据集：基于Text2Zinc（1,775个问题）和Or-Instruct（1,351个问题），经GPT-5.2翻译与验证，总计2,208个唯一问题，形成8,014条指令微调对。
- 模型：Qwen3-0.6B、LLaMA-3.2-1B/3B、Gemma-2-9B、GPT-OSS-20B，使用LoRA（8-bit量化，20B模型用4-bit）单A100微调。
- 结果：基线小模型执行准确率近乎零；微调后直接生成达80–85%，思维链略低；自我反思与集成达98%执行准确率；但求解准确率仅35%。

### 值得关注点
- 针对极低资源语言（MiniZinc的GitHub仓库仅百余个）的微调策略，证明即使稀疏数据也能显著提升语法正确性。
- 跨模型错误自助法有效利用了LLM失败样本，无需人工标注纠错数据。
- 98%的执行准确率展示了语法学习的高效性，但35%的求解准确率凸显了约束推理的深层挑战，为后续研究指明方向。

### 局限性
- 求解准确率仅35%，表明模型无法正确建模问题约束，推理能力严重不足。
- 微调数据集规模较小（8,014对），且依赖GPT-5.2翻译，可能引入偏差。
- 未在更大模型或更多领域通用语言上验证泛化性。
- 自我反思与集成虽提升执行准确率，但计算开销较大，实用性受限。

## Processing Notes

- Duplicate papers skipped: 0