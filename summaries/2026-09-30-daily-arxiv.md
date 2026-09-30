# Daily arXiv - 2026-09-30

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-30T03:52:51
- Paper count: 10

## 1. Decide, Don't Generate: Competitive Dimensional ABSA with Jev's Typed Decisions

- Source: arxiv
- arXiv ID: 2609.35293
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2609.35293v1
- PDF: https://arxiv.org/pdf/2609.35293v1
- DOI: https://doi.org/10.48550/arXiv.2609.35293

### Authors

Yiqun Zhang, Peidong Wang, Zihan Wang, Shi Feng

### Abstract

Aspect-based sentiment analysis (ABSA) has largely turned to text generation. We show that competitive dimensional ABSA does not need it. Using Jev, a frozen model that answers typed questions with rubric scores, label probabilities, and yes/no judgments, we decompose all three tasks of SemEval-2026 Task III Track A into such decisions and align them with the annotation scheme through 488 coefficients fitted on CPU, with no text generation and no backbone tuning. On valence-arousal regression over ten corpora in six languages, the system reaches 1.0645 RMSE, the lowest aggregate error of any participating system. On triplet and quadruplet extraction, it reaches 52.09 and 44.06 continuous F1, above fine-tuned Llama-3.3-70B and GPT-OSS-120B baselines. Analyses and ablations show where the accuracy comes from: supervised calibration roughly halves the raw regression error, exact valence-arousal would add only 4.5 F1 to extraction, and the learned combination of span-boundary evidence, not any single signal, carries the extraction systems.

### 中文一句话结论
本文证明维度级ABSA无需文本生成：通过冻结模型Jev回答类型化问题，仅用488个系数在CPU上拟合，即在六个语言十个语料库上取得最低回归误差，并在提取任务上超越微调Llama-3.3-70B与GPT-OSS-120B。

### English TL;DR
This work shows that competitive dimensional ABSA can be achieved without text generation or backbone tuning by using a frozen model (Jev) to answer typed questions, with only 488 coefficients fitted on CPU, outperforming fine-tuned Llama-3.3-70B and GPT-OSS-120B on extraction tasks and achieving the lowest regression error among participants on SemEval-2026 Task III.

### 中文详细总结
本文针对SemEval-2026 Task III Track A的三个任务（给定方面回归、三元组/四元组提取），提出一种纯决策式流水线，不生成任何文本，也不微调任何骨干模型。核心是使用冻结模型Jev，通过三种类型化接口（得分、标签概率、是/否判断）回答结构化问题。系统仅通过488个系数（ridge回归、logistic重排序、小融合模型）完成任务适应，所有系数均在CPU上拟合。
在valence-arousal回归任务（Task 1）上，系统在十个语料库（六种语言）上达到1.0645 RMSE，是所有参赛系统中聚合误差最低的。在三元组提取（Task 2）和四元组预测（Task 3）上，分别达到52.09和44.06连续F1，超过微调的Llama-3.3-70B和GPT-OSS-120B基线。消融实验表明：有监督标定可将原始回归误差减半；精确的valence-arousal仅能给提取任务增加4.5 F1；提取的成功依赖于学习到的跨度边界证据组合，而非单一信号。

### 方法 / 贡献
1. 提出纯决策式流水线：不生成文本，不更新骨干权重，仅用488个系数（CPU拟合）适配三个任务。
2. 分解每个任务为Jev模型的类型化决策：Task 1用固定演示+ridge回归标定；Task 2用BIO token预测、边界检查、对数几率重排序；Task 3用类别先验+条件对数几率模型。
3. 在六个语言、四个领域上取得领先结果：Task 1最低聚合RMSE，Task 2/3超过微调70B模型。
4. 详细消融分析揭示准确率来源：标定、边界证据组合等。

### 实验或数据
- **数据集**：SemEval-2026 Task III Track A官方划分。Task 1覆盖10个语料库（英语、中文、日语、俄语、鞑靼语、乌克兰语），涵盖餐厅、笔记本、酒店、金融领域；Task 2/3覆盖8个非金融语料库。
- **测试规模**：Task 1有9,658条评论、16,186个方面标注；Task 2/3共享6,690条评论、14,262个三元组和14,263个四元组。
- **度量**：Task 1采用微聚合RMSE（所有标注联合计算欧氏距离）；Task 2/3采用连续F1（精确结构匹配+VA距离惩罚）。
- **基线**：微调Llama-3.3-70B、GPT-OSS-120B，以及所有参赛系统。

### 值得关注点
- **无需文本生成与骨干微调**：完全抛弃生成式范式，仅用冻结模型+少量可学习系数达到竞争性能，算力需求极低（CPU即可）。
- **跨语言泛化**：系统在六种语言（含低资源语言鞑靼语）上表现稳定，不使用任何语言特定预训练。
- **高效率适配**：仅488个系数（线性层+小融合模型），训练成本可忽略。
- **提取结构可解释**：消融表明跨度边界证据的组合是关键，而非单一信号，为后续改进提供方向。

### 局限性
- **提取错误主要源于结构性问题**：真值对在提议和跨度选择阶段丢失，而非数值预测不准。增加类别环节的成本低于其他系统，但仍有改进空间。
- **依赖标注数据**：标定和重排序均需有监督训练数据（每个语料库约1,000个标注样本），在零样本场景下可能不适用。
- **标定与重排序均需语料特定参数**：Task 1的ridge回归和Task 3的条件对数几率模型按语料库独立拟合，跨语料迁移未验证。
- **未讨论处理隐式方面的扩展**：Task 3中NULL方面处理仅通过计数，文中未对隐式方面进行专门分析。

## 2. ABC-Align: Prediction-Powered Alignment with Adaptive Bias Control

- Source: arxiv
- arXiv ID: 2609.34374
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.34374v1
- PDF: https://arxiv.org/pdf/2609.34374v1
- DOI: https://doi.org/10.48550/arXiv.2609.34374

### Authors

Eric Frankel, Banghua Zhu, Sewoong Oh, Lillian J. Ratliff

### Abstract

Language model post-training is often bottlenecked by the need for human-collected preference data, which is expensive and difficult to scale. Reinforcement learning from AI feedback (RLAIF) style approaches that leverage pseudo labels offer an abundant alternative but introduce systematic biases that degrade downstream alignment. Recent general-purpose semi-supervised methods correct for teacher bias using a small set of human-labeled examples, but suffer from high variance especially when human annotations are scarce. To this end, we propose ABC-Align, leveraging abundant pseudo label signal to minimize variance and applying a lightweight, adaptive correction grounded in the human-labeled subset. The correction strength is tuned automatically during training using plug-in estimates of the relevant bias--variance quantities. On LLM alignment with RLHF, DPO, and GRPO where human feedback is scarce, we empirically demonstrate that ABC-Align achieves superior performance over prior semi-supervised baselines in a series of experiments on an increasing scale. Our code is available at https://github.com/SewoongLab/abc-align .

### 中文一句话结论  
ABC-Align 提出一种自适应偏差校正的半监督对齐方法，利用大量 AI 伪标签降低方差，并借助少量人工标注进行轻量级偏差校正，在 RLHF、DPO、GRPO 等场景中优于已有半监督基线。

### English TL;DR  
ABC-Align is a semi-supervised method for language model alignment that uses abundant pseudo labels from AI feedback to reduce variance, while applying a lightweight, adaptive correction based on a small human-labeled subset. It outperforms prior semi-supervised baselines in RLHF, DPO, and GRPO settings.

### 中文详细总结  
语言模型后训练常受限于昂贵且难以扩展的人工偏好数据。RLAIF 等使用伪标签的方法虽能提供大量替代信号，但会引入系统性偏差，损害下游对齐效果。现有通用半监督方法虽可用少量人工标注校正教师偏差，但在标注稀缺时方差较高。ABC-Align 通过大量伪标签信号降低方差，并利用人工标注子集进行自适应、轻量级校正；校正强度在训练中通过偏差–方差的插件估计自动调节。在 LLM 对齐的 RLHF、DPO 和 GRPO 设置下，ABC-Align 在递增规模的实验中取得了优于以往半监督基线的表现。

### 方法 / 贡献  
- 提出 ABC-Align，结合丰富伪标签与少量人工标注，兼顾方差控制与偏差校正。  
- 使用插件估计自动调节校正强度，避免人工调参。  
- 方法适用于 RLHF、DPO、GRPO 等多种对齐框架。  
- 提供开源代码：https://github.com/SewoongLab/abc-align 。

### 实验或数据  
摘要提到，在 LLM 对齐的 RLHF、DPO 和 GRPO 设置下，且在人工反馈稀缺、实验规模递增的条件下，ABC-Align 相对先前半监督基线取得更优性能。摘要未给出具体数据集、指标数值或消融实验细节。

### 值得关注点  
- 核心思路是同时利用伪标签的规模优势和人工标注的保真度，缓解教师偏差。  
- 自适应的偏差–方差平衡机制具有较强的实用价值。  
- 在多种主流对齐方法上验证，说明方法具有一定通用性。  
- 代码公开，便于复现与扩展。

### 局限性  
摘要未明确讨论局限性。根据方法描述，仍依赖少量人工标注子集；此外，校正强度的插件估计依赖偏差–方差量的可估计性，但摘要未展开说明失败场景或理论保证。

## 3. CORTEX: Learning to Share and Specialize in Dense Language Models

- Source: arxiv
- arXiv ID: 2609.34449
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.34449v1
- PDF: https://arxiv.org/pdf/2609.34449v1
- DOI: https://doi.org/10.48550/arXiv.2609.34449

### Authors

Chuiyang Meng, Ming Tang, Vincent W. S. Wong

### Abstract

Large language models are trained on heterogeneous data mixtures, where different knowledge domains require both shared knowledge and specialization. Existing modular approaches typically impose explicit components or discover modules through interpretability analysis after training. In this work, we propose CORTEX, a learning dynamics-inspired framework that learns internal modularization within dense language models. CORTEX partitions trainable matrices into parameter groups and learns module assignments from domain-conditioned gradient and cross-domain gradient similarity. We introduce the selective lesion score and module-domain mutual information to characterize the target-domain lesion effects and alignment, and analyze how module assignment affects the trade-off between assignment bias and update magnitude. Experiments with 160M, Qwen3-8B, and Qwen3-32B backbone models show that CORTEX achieves the highest synthetic-domain exact match and largest average perplexity reduction, while remaining competitive on real-domain evaluations and forming identifiable modules.

### 中文一句话结论
CORTEX 提出一种受学习动态启发的框架，让稠密语言模型在训练过程中自动形成“共享模块 + 领域专用模块”的内部模块化划分，在异构数据混合训练中同时兼顾知识共享与领域特化。

### English TL;DR
CORTEX is a learning dynamics-inspired framework that enables dense language models to learn internal shared and specialized module assignments during training through domain-conditioned gradient analysis, effectively balancing knowledge sharing and specialization on heterogeneous data without explicit architectural modifications.

### 中文详细总结
CORTEX 面向大规模语言模型在异构数据混合训练中的“共享与特化”权衡问题。与显式引入专家模块（如 MoE）或训练后再做可解释性分析的方法不同，CORTEX 在稠密模型的参数空间内部学习模块化结构。它将可训练矩阵划分为参数组，并基于领域条件下的梯度相似性学习模块分配。实验表明，CORTEX 在 160M、Qwen3-8B 和 Qwen3-32B 上均能形成可识别的模块，并在合成领域取得最高精确匹配，在真实领域评估中保持有竞争力的表现。

### 方法 / 贡献
- 提出 CORTEX 框架，在稠密 LLM 内部学习共享模块与多个专用模块的软分配，无需显式架构修改。
- 提出基于领域条件梯度的模块分配机制：跨域梯度一致的参数组归入共享模块，领域集中且不一致的参数组归入对应专用模块。
- 引入选择性损伤分数（selective lesion score）和模块-领域互信息，用于刻画模块对目标领域损伤的影响及模块与领域的对齐程度。
- 分析模块分配如何影响“分配偏差”与“更新幅度”之间的权衡。
- 在多种规模模型上与 Dense、Random、MoE、MoM、UpIT、Self-MoE 等基线进行比较。

### 实验或数据
摘要中提到的实验包括：
- 使用 160M、Qwen3-8B、Qwen3-32B 作为骨干模型。
- 在合成领域基准和真实领域混合数据上进行评估。
- 结果指标包括合成领域 exact match、平均困惑度（perplexity）降低幅度，以及真实领域评估表现。
- 摘要未提供具体数据集名称、数据规模或详细实验配置。

### 值得关注点
- CORTEX 不引入额外专家模块，而是在稠密模型内部形成模块化结构。
- 模块分配由训练过程中的梯度动态驱动，可能为稠密模型提供一种新的“隐式模块化”训练范式。
- 在多个模型规模上均能形成可识别的模块，说明该方法具有一定可扩展性。
- 对共享与特化的权衡进行了理论性分析，而非仅依赖经验调参。

### 局限性
摘要和提供的元数据未明确列出局限性。可推测的潜在限制包括：需要领域标签（domain label）作为训练信号；合成领域优势明显，但真实领域仅“有竞争力”而非全面领先；参数组划分粒度和模块数量可能需要人工设定；更大规模或更多领域下的泛化能力尚待进一步验证。这些内容未在摘要中直接说明，需以原文为准。

## 4. E-CONAN (Entailment, CONtradition And Neutral) Diagnostics Dataset Investigating Linguistic Phenomena in Arabic Natural Language Understanding

- Source: arxiv
- arXiv ID: 2609.33530
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.33530v1
- PDF: https://arxiv.org/pdf/2609.33530v1
- DOI: https://doi.org/10.48550/arXiv.2609.33530

### Authors

Khloud AL Jallad, Nada Ghneim, Ghaida Rebdawi

### Abstract

Natural Language Understanding (NLU) plays a crucial role in various applications, yet its performance suffers from weaknesses in handling the complexities of human languages, ranging from lexical ambiguity to high-level reasoning difficulties. Analyzing errors across diverse linguistic phenomena is crucial for NLU improvement, as it will help humans get insights to comprehensively assess models' limitations and capabilities, so optimizing models' generalization. Notably, several benchmarks contain diagnostics datasets designed for investigation and fine-grained error analysis. When highlighting the gaps in the state-of-the-art, we noted that there is no naming convention for macro and micro categories or even a standard set of linguistic phenomena that should be covered. To overcome this gap, we propose an initial hierarchy for Cross-Lingual NLU error analysis. Moreover, we propose a methodology to create an NLI hierarchical framework and applied a case study on Arabic NLU. Moreover, this paper introduces E-CONAN diagnostics dataset, a freely available dataset manually-annotated with coarse-grained and fine-grained categories based on our proposed Arabic hierarchy. E-CONAN dataset helps NLU designers better understand their models by doing error analysis and in-depth investigation. We used E-CONAN to investigate the performance of 9 pretrained language models and 5 LLMs. Results indicate that LLMs outperform pretrained models in world knowledge and commonsense reasoning macro-category, and underperform pretrained models in syntactic macro-category. Moreover, the hardest phenomena for all models is Reasoning, and the easiest phenomena for all pretrained models is Syntactic, and the easiest for LLMs is Lexico-Syntactic.

### 中文一句话结论
论文构建了首个针对阿拉伯语自然语言推理的诊断数据集E-CONAN，并提出一套跨语言语言学现象层次框架，实验揭示了大语言模型与预训练模型在不同宏观类别上的相对优势与劣势，所有模型在推理类任务上均表现最差。

### English TL;DR
This paper introduces E-CONAN, a manually annotated Arabic NLI diagnostics dataset with a novel hierarchical taxonomy of linguistic phenomena, and uses it to evaluate 9 PLMs and 5 LLMs, finding that LLMs outperform PLMs in world knowledge/common sense but underperform in syntax, with reasoning being the hardest category for all models.

### 中文详细总结
论文指出现有诊断数据集在语言学现象的分层命名上缺乏标准，因此提出了一个初始的跨语言NLU错误分析层次体系，并针对阿拉伯语进行了具体构建。基于此层次体系，作者创建了E-CONAN诊断数据集，包括粗粒度和细粒度类别，并人工标注了句子对的关系。研究者使用该数据集测试了9个预训练语言模型和5个大语言模型，结果表明：LLM在“世界知识与常识”宏观类别上优于预训练模型，但在“句法”宏观类别上表现较差；所有模型在“推理”类别上表现最困难；预训练模型在“句法”上最容易，而LLM在“词汇-句法”上最容易。

### 方法 / 贡献
- 提出了初始的跨语言NLU错误分析层次，并应用自底向上与自顶向下结合的方法构建了针对阿拉伯语的层次框架。
- 创建了E-CONAN诊断数据集，包含7个粗粒度类别和多个细粒度子类别，手工标注了句子对及关系标签。
- 提供了评估9种预训练模型和5种大语言模型的标准诊断工具，并给出了详细结果与分析。

### 实验或数据
实验使用E-CONAN数据集，包含从阿拉伯语语法书籍、ALUE和GLUE数据集中提取并人工构造的句子对。数据集覆盖词汇、词汇-句法、句法、话语、逻辑、知识与常识、语用等宏观类别。评估了9个预训练语言模型和5个大语言模型，报告了各模型在不同类别上的正确率对比。

### 值得关注点
- 首次为阿拉伯语NLI量身定做了诊断数据集，并在层次中新增了语用学类别。
- 揭示了大语言模型在常识/世界知识上的优势，以及在句法处理上的不足，突显了不同模型类别的强项与弱项。
- “推理”类别对所有当前模型都是最难挑战，说明当前模型的高级推理能力仍有很大提升空间。

### 局限性
该层次框架目前为初步版本，作者也指出仍有改进空间；数据集和实验仅针对阿拉伯语，跨语言的通用性需进一步验证；此外，评估仅限于自然语言推理任务，未涉及其它NLU任务。

## 5. SleuthBench: Benchmarking Statistical LLM Evaluation Using Tabular Hidden Signals

- Source: arxiv
- arXiv ID: 2609.34228
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.34228v1
- PDF: https://arxiv.org/pdf/2609.34228v1
- DOI: https://doi.org/10.48550/arXiv.2609.34228

### Authors

Jingyun Jia, Antoine Remond-Tiedrez, Aaron Alvarez, Joshua Shunk, Rich Caruana, Ben Lengerich

### Abstract

Evaluating statistical discovery by large language model (LLM) agents requires verifiable analytical ground truth. Establishing such ground truth for real-world datasets is costly, and prior knowledge of public datasets can influence agent responses. We introduce SLEUTHBENCH, a benchmark that addresses both problems by injecting controlled data-quality problems and feature effects into public tabular datasets: the injected pattern determines the answer, so reference answers are computed automatically and memorized knowledge of the original table is insufficient, while the table keeps its background structure. The injected patterns are modeled on phenomena reported in real data analyses. The benchmark defines 17 question templates in two families: data-quality questions and feature-contribution questions. We evaluate six state-of-the-art LLMs that analyze the data using a Python coding tool, on data-science and business phrasings of 70 validated dataset-template combinations, yielding 1680 graded responses in total. The models detect data-quality problems reliably (83.8% accuracy) but recover feature contributions poorly (41.9%). Finding how features shape the target requires searching over both candidate variables and analytical procedures. To address this issue, we propose the Empirical Layer, a set of precomputed statistical artifacts comprising summaries, fitted feature and interaction effects, and dataset descriptions, which exposes candidate patterns for direct inspection. Access to these artifacts raises feature-contribution accuracy from 41.9% to 68.0%.

### 中文一句话结论
SLEUTHBENCH通过向公开表格数据集中注入受真实数据分析启发的隐藏模式，自动生成可验证的参考答案，从而实现对LLM统计发现能力的可靠评估。

### English TL;DR
SLEUTHBENCH injects controlled hidden patterns into public tabular datasets to automatically produce verifiable ground truth for evaluating LLM statistical discovery. Models detect data-quality issues reliably (83.8% accuracy) but perform poorly on feature contribution recovery (41.9%), which is improved to 68.0% by providing precomputed statistical artifacts (the Empirical Layer).

### 中文详细总结
SLEUTHBENCH通过向公开表格数据集中注入两类受真实数据分析启发的隐藏模式——数据质量问题（如缺失值、异常值）和特征贡献模式（如特征效应、交互效应），构建了一个基准测试。注入的模式决定了正确答案，因此参考答案可自动计算，且模型无法依赖对原始数据的记忆。基准测试包含17个问题模板（分属数据质量和特征贡献两大类别），涵盖数据科学和商业两种表述方式，共70个经验证的数据集-模板组合，每个组合由6个最先进的LLM使用Python编码工具进行分析，总计产生1680个评分响应。结果显示，模型在数据质量问题检测上表现可靠（准确率83.8%），但在特征贡献恢复上表现较差（准确率41.9%）。为解决这一问题，作者提出了“经验层”（Empirical Layer），一套预计算的统计构件，包括数据摘要、拟合的特征效应和交互效应以及数据集描述，使模型可以直接审查候选模式。使用这些构件后，特征贡献恢复的准确率从41.9%提升到68.0%。

### 方法 / 贡献
- **方法**: 向公开表格数据集中注入两种受真实分析启发的隐藏模式：数据质量问题（如缺失值、异常值）和特征贡献模式（如特征效应、交互效应）。注入的模式控制答案，因此可自动计算参考答案，且模型无法依赖原始数据记忆。定义了17个问题模板，分属数据质量和特征贡献两大类别，并使用数据科学和商业两种表述方式。
- **贡献**: 引入SLEUTHBENCH基准测试，解决LLM统计发现评估中缺乏可验证参考答案和公开数据先验知识干扰的问题；提出“经验层”预计算统计构件，显著提升LLM的特征贡献恢复能力。

### 实验或数据
- 实验使用了70个验证过的数据集-模板组合，每个组合由6个最先进的LLM（具体模型名称未在摘要中列出）使用Python编码工具进行分析，总共产生1680个评分响应。
- 实验评估了数据质量问题检测（83.8%准确率）和特征贡献恢复（41.9%准确率）两个任务，并测试了“经验层”对特征贡献恢复的改进效果（提升至68.0%）。

### 值得关注点
- 自动生成可验证参考答案的创新设计，有效避免公开数据集先验知识对评估的干扰。
- 揭示了当前LLM在统计发现能力上的显著差距：数据质量问题检测优秀，但特征贡献恢复能力薄弱。
- “经验层”预计算统计构件能有效弥合这一差距，为改进LLM分析能力提供了实用方向。

### 局限性
- 仅使用Python编码工具进行评估，可能无法代表模型使用其他工具或直接推理的表现。
- 采用的17个问题模板和70个数据集-模板组合可能无法涵盖所有真实统计发现场景。
- 6个LLM的具体模型名称和版本未在摘要中说明，影响对模型选择范围的理解。
- 虽然“经验层”提升了特征贡献恢复，但68.0%的准确率仍有较大改进空间。

## 6. Advancing Video-Text Pretraining with Multi-View Captions

- Source: arxiv
- arXiv ID: 2609.35090
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.35090v1
- PDF: https://arxiv.org/pdf/2609.35090v1
- DOI: https://doi.org/10.48550/arXiv.2609.35090

### Authors

Fida M. Thoker, Renaud Vandeghen, Karen Sanchez, Marc Van Droogenbroeck, Bernard Ghanem

### Abstract

Video-text pretraining has achieved remarkable progress through the scaling of models and datasets, yet the quality of language supervision remains underexplored. Existing web-scale datasets often provide only a single sparse caption per video that fails to capture rich spatiotemporal semantics, while directly using captioning models can generate noisy descriptions. We propose a large-scale multimodal large language model-based supervision generation framework that improves supervision diversity, fidelity, and semantic coverage. Starting from 10 million videos, our approach generates multi-view captions (MVC) through complementary summary and detailed captions, reasoning-based refinement, and semantic positive caption generation. To effectively exploit supervision at different granularities, we further introduce a granularity-aware text representation with separate CLS tokens for summary and detailed views. We pretrain video-text models using the resulting supervision corpus and evaluate them across standard, fine-grained and detailed text-to-video retrieval benchmarks. Our approach consistently improves both zero-shot and fine-tuned performance while using smaller pretraining corpora than existing methods, demonstrating the importance of rich and complementary textual supervision for video-text pretraining. Project page: https://rvandeghen.github.io/mvc/

### 中文一句话结论
本文提出一种基于多模态大语言模型的多视角字幕生成框架，通过互补的总结与详细字幕、推理优化及语义正样本生成，显著提升视频-文本预训练质量，在更小预训练语料下实现更优的文本-视频检索性能。

### English TL;DR
This paper proposes a multimodal LLM-based framework that generates diverse multi-view captions (summary, detailed, reasoning-refined, and semantic positive) and uses a granularity-aware text representation, consistently boosting text-to-video retrieval performance with smaller pretraining corpora.

### 中文详细总结
现有视频-文本预训练依赖大规模网络数据集，但通常每个视频仅有一个稀疏字幕，无法捕捉丰富的时空语义；直接使用字幕模型则可能产生噪声描述。本文提出一个大规模多模态大语言模型（MLLM）驱动的监督生成框架，从1000万视频开始，生成多视角字幕（MVC），包括互补的总结字幕与详细字幕、基于推理的优化字幕，以及语义正样本字幕。为有效利用不同粒度的监督信号，进一步引入粒度感知的文本表示，为总结和详细视角分别设置独立的CLS标记。在标准、细粒度及详细文本-视频检索基准上评估预训练模型，结果显示该方法在零样本和微调设置下均持续提升性能，且所用预训练语料比现有方法更小，证明了丰富而互补的文本监督对视频-文本预训练的重要性。

### 方法 / 贡献
- 提出一种基于MLLM的大规模监督生成框架，从1000万原始视频生成多视角字幕（总结、详细、推理优化、语义正样本），提升监督信号的多样性、忠实度和语义覆盖。
- 引入粒度感知的文本表示，为总结和详细视图使用独立的CLS标记，以更好地利用不同粒度的文本监督。
- 在多个文本-视频检索基准上验证了该方法的有效性，在较小预训练语料下取得更优性能，证明高质量多视角字幕的重要性。

### 实验或数据
- 实验在标准、细粒度和详细文本-视频检索基准上进行（具体数据集名称未在摘要中列出）。
- 预训练数据来自1000万视频，经MLLM生成多视角字幕构建监督语料。
- 评估涵盖零样本和微调设置，结果一致优于现有方法。

### 值得关注点
- 首次系统性地从“语言监督质量”入手，通过多视角生成克服单一样本字幕的不完整性和噪声。
- 通过MLLM生成推理优化和语义正样本，增强字幕对视频内容的忠实度和多样性。
- 粒度感知的文本表示设计巧妙，能分别处理总结性与详细性描述，提升检索匹配精度。
- 使用更小的预训练语料却取得更好性能，表明提升数据质量比单纯扩大规模更有效。

### 局限性
根据摘要，本文未明确讨论方法的局限性。可能存在的不足之处包括：依赖大规模MLLM进行字幕生成，计算成本较高；生成的语义正样本质量可能受限于MLLM的能力；不同视角字幕的平衡与冗余问题有待进一步探究。

## 7. Relative Generalization Invariance of LLM Pretraining

- Source: arxiv
- arXiv ID: 2609.33016
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.33016v1
- PDF: https://arxiv.org/pdf/2609.33016v1
- DOI: https://doi.org/10.48550/arXiv.2609.33016

### Authors

Fengzhuo Zhang, Shuche Wang, Shenggui Li, Tianyu Ruan, Jianliang He, Ivor Tsang, Tianyu Pang, Chao Du, Tianwei Zhang, Zhuoran Yang

### Abstract

Large Language Model (LLM) pretraining performance is jointly shaped by three components of the training triplet: the optimizer, model architecture, and training data stream. However, how these components influence performance in distinct ways remains unclear. We take a first step toward isolating their effects by studying relative generalization. We introduce Relative Generalization Invariance (RGI), the invariance of the validation-loss difference between any two tokens across models. We show that RGI approximately holds across a wide range of optimizers and moderate architectural variations, suggesting that these choices induce an approximately uniform shift in token-wise losses. In contrast, changing the training data stream can substantially alter relative generalization. We further show that RGI cannot be explained by the neural tangent kernel or mean-field regimes alone and prove that it can emerge in an overparameterized quadratic model. Overall, our work identifies RGI as a new phenomenon in LLM pretraining that helps distinguish the effects of optimizers and architectures from those of training data.

### 中文一句话结论
本文提出相对泛化不变性（RGI），发现优化器和架构对token级验证损失产生近似均匀的偏移，而数据流则改变相对泛化结构。

### English TL;DR
The paper introduces Relative Generalization Invariance (RGI), showing that in LLM pretraining, token-wise validation losses are uniformly shifted by optimizer and architecture choices but not by changes in the training data stream, and it provides both empirical and theoretical characterizations of this phenomenon.

### 中文详细总结
论文首次提出“相对泛化不变性”（RGI）概念，指在不同模型之间，任意两个token的验证损失差值保持不变的特性。研究表明，对于广泛的优化器（如Adam、Muon等）和适度的架构变化（如注意力机制、FFN设计），RGI近似成立，意味着这些选择导致token级损失发生均匀的平移。然而，当训练数据流来源改变时，相对泛化结构会显著变化。论文进一步排除了神经正切核（NTK）与平均场（MF）解释的可能性，并在一个过参数化的二次模型中证明了RGI的理论基础。该工作首次区分了优化器/架构与训练数据在预训练中的不同作用。

### 方法 / 贡献
- 提出RGI概念，定义为不同模型间任意两个token验证损失差值的不变性，等价于token级损失的均匀偏移。
- 通过大量实验验证RGI在多种优化器（坐标式、矩阵式）和架构变化下近似成立，但对数据流敏感。
- 理论分析表明RGI无法由NTK或MF机制解释，并利用过参数化二次模型证明其可在广泛学习率、初始化和优化器下出现。
- 为分离训练三元组（优化器、架构、数据）各自的影响提供了第一步方法论。

### 实验或数据
实验涉及多种优化器（如Adam、Muon、GD）和架构变体（不同注意力类型、FFN设计、宽度缩减）。验证RGI通过比较token级验证损失差异的保持性。此外，通过改变训练数据流来源（不同语料源）观察RGI是否破裂。论文未明确指定具体数据集名称。实验还通过测量参数和隐藏表示距离来排除NTK/MF解释。

### 值得关注点
- RGI揭示了优化器与架构选择对泛化影响的本质均匀性，为超参数迁移和预训练机制理解提供新视角。
- 该现象对优化器超参数和验证分布轻微偏移具有鲁棒性，但数据流改变会破坏RGI，暗示数据是影响相对泛化的关键因素。
- 实验和理论结合，超越了现有NTK/MF分析框架，展示了特征学习下的新行为。

### 局限性
- RGI仅近似成立，在极端架构变化或训练步数不足时可能失效。
- 理论证明限于过参数化二次模型，尚未推广到真实神经网络的完整设置。
- 工作主要聚焦预训练阶段，对微调或下游任务的影响未做探索。
- 实验中的“数据流变化”具体范围和强度有限，更大规模或多来源的混合数据效应待验证。

## 8. Towards Scalable Data Diversification for Language Model Pretraining via Leverage Score Sampling

- Source: arxiv
- arXiv ID: 2609.32484
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.32484v1
- PDF: https://arxiv.org/pdf/2609.32484v1
- DOI: https://doi.org/10.48550/arXiv.2609.32484

### Authors

Zailin Ma, Quzhe Huang, Yujun Li, Congyuan Rao, Yaodong Yang

### Abstract

Data selection for language model pretraining faces a fundamental tension between quality and diversity. While quality filtering is empirically effective, it often induces diversity collapse: by favoring texts similar to high-quality reference corpora (e.g., educational or QA-style data), it systematically excludes valuable data from underrepresented domains. In contrast, diversified selection preserves domain balance and encourages robust downstream performance, yet existing methods either focus on coverage-oriented objectives that indirectly enhance diversity, or directly optimize for diversity via costly covariance matrix recomputation that limits scalability. To address these issues, we introduce \textbf{Leverage Score Sampling (Lev)}, which iteratively selects samples that maximally expand the determinantal volume of the embedded data via leverage scores, a computationally efficient criterion that eliminates matrix recomputation and enables scalable selection. Empirically, Lev delivers up to $72\times$ speedup and improves dataset diversity, measured by the Vendi score, by $9.2\%$ over the strong diversification baseline \textbf{DiSF}. On CommonCrawl (CC) web data selection, Lev improves accuracy across seven downstream tasks by up to $1.31\%$ over existing baselines. For domains where robust quality criteria are inherently difficult to define (e.g., code), Lev serves as an effective unsupervised curation alternative: on StarCoderData, the selected subset reduces bits-per-byte by $3.08\%$ over DiSF. Notably, we uncover a cross-domain collapse of quality filtering: CC data filtered by DCLM-fastText fail to retain sufficient code-related content, yielding inferior code performance relative to Lev-selected data. These findings advocate for integrating diversity-aware practices into quality filtering for more effective data curation in language model pretraining.

### 中文一句话结论
本文提出基于杠杆分数采样的可扩展数据多样化方法（Lev），在语言模型预训练数据筛选中兼顾质量与多样性，显著提升效率与下游性能，并揭示了质量过滤导致代码领域内容缺失的跨域坍缩问题。

### English TL;DR
The paper introduces Leverage Score Sampling (Lev), a scalable and efficient method for diversifying language model pretraining data that selects samples maximizing geometric diversity via leverage scores—achieving up to 72× speedup over prior methods, improving dataset diversity by 9.2%, and enhancing downstream task accuracy by up to 1.31% while also revealing that quality filtering induces a cross-domain collapse that disproportionately excludes code-related content.

### 中文详细总结
语言模型预训练数据筛选面临质量与多样性的根本矛盾。基于质量过滤器（如DCLM-fastText）虽有效，但常导致多样性崩塌——倾向于选择与优质参考语料相似的高分样本，系统性地排除低相关但有价值的数据（如代码）。现有多样化方法要么通过覆盖目标间接增强多样性，要么通过高代价的协方差矩阵重计算直接优化几何多样性，限制了可扩展性。

为解决这些问题，本文提出**杠杆分数采样（Lev）**。该方法基于理论证明：候选样本的杠杆分数精确量化了其加入后对嵌入数据行列式体积的扩张程度。Lev利用共享Gram矩阵高效计算所有候选杠杆分数，无需每步重算协方差矩阵，因此支持大规模应用。实验表明，相比强基线DiSF，Lev实现最多72倍加速、数据集多样性（Vendi分数）提升9.2%，并在CommonCrawl的7个下游任务上准确率最高提高1.31%。在代码领域（StarCoderData），Lev作为无监督数据筛选方法，使bits-per-byte降低3.08%。此外，分析发现质量过滤器DCLM-fastText导致代码领域坍缩，无法保留足够代码内容，而多样性方法却能有效保持。论文主张将多样性感知策略融入质量过滤以提升预训练数据质量。

### 方法 / 贡献
**方法**：提出杠杆分数采样（Lev）算法。基于嵌入向量，通过Cholesky分解高效计算每个候选样本相对于已选数据池的杠杆分数，迭代选取分数最高的样本加入选择集，利用增量更新Gram矩阵避免重算。算法按批次处理语料，在每批次内多次子迭代选择样本（步长b），实现可扩展的几何多样性最大化。

**贡献**：
1. 理论建立杠杆分数作为几何多样性信号的原理，证明其刻画样本对行列式体积扩张的贡献。
2. 提出Lev算法，相比DiSF实现显著加速（72倍），且保持更高多样性。
3. 在CommonCrawl和StarCoderData上验证下游性能提升，并发现质量过滤导致代码领域的跨域坍缩，强调多样性感知筛选的重要性。

### 实验或数据
- **数据集**：CommonCrawl网页数据、StarCoderData代码数据。
- **评估指标**：Vendi分数（多样性）、7个下游任务准确率、bits-per-byte（代码建模难度）。
- **结果**：Lev相比DiSF提升多样性9.2%，加速72倍；在CommonCrawl上平均下游准确率提升最多1.31%；在StarCoderData比特率降低3.08%。
- **分析**：DCLM-fastText质量过滤器筛选的CommonCrawl子集缺乏代码相关内容，而Lev筛选的数据保留更多代码，证明了质量过滤的代码坍缩现象。
- 论文未提及详细实验配置（如嵌入模型、greedy选择步长等），但算法描述中给出了批次大小B和步长b的设置。

### 值得关注点
- **效率突破**：杠杆分数方法消除昂贵的协方差矩阵重算，使几何多样化变得可扩展，速度提升72倍。
- **跨域坍缩发现**：揭示质量过滤在代码等难以定义质量标准的领域造成系统性数据缺失，而多样性方法能无监督地保留这类有价值数据。
- **理论支撑**：严格证明杠杆分数与行列式体积扩张的等价关系，为算法提供几何可解释性。
- **实用价值**：Lev在代码数据上可作为有效的无监督筛选替代，无需人工标注质量标签，适合条件有限的应用场景。

### 局限性
- 方法依赖预训练嵌入模型，其质量可能影响多样性评估效果。
- 批次内选择非全局最优，且步长和正则化参数λ需手动调节。
- 实验仅在有限规模数据集上验证，大规模（如万亿Tokens）预训练上的可扩展性待进一步检验。
- 几何多样性仅基于向量空间距离，可能无法完全捕获语义、风格或知识覆盖的多样性。

## 9. C-HAT-Bench: Benchmarking Chinese AI-Text Detection Beyond Fully Generated Text

- Source: arxiv
- arXiv ID: 2609.32770
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.32770v1
- PDF: https://arxiv.org/pdf/2609.32770v1
- DOI: https://doi.org/10.48550/arXiv.2609.32770

### Authors

Qing Yang, Zixiang Luo, Zhenyu Mao, Zezheng Wu, Xinghe Cheng, Haibo Chen, Qinggang Zhang, Jiapu Wang, Jingwei Zhang

### Abstract

Large Language Models (LLMs) increasingly participate in writing by modifying or extending human drafts, causing machine involvement to vary in both form and extent. Yet most Machine-Generated Text (MGT) detectors are evaluated only on fully human-written versus fully AI-generated text. Because human--AI collaboration can weaken or redistribute cues associated with machine generation, strong performance under this binary setting may overstate detector reliability. This mismatch remains underexplored in Chinese: detection cues are shaped by tokenization and language-specific text distributions, yet controlled resources spanning production settings, domains, and generators remain limited. To fill this gap, we present a Chinese Human-AI Collaborative Text Detection Benchmark (C-HAT-Bench), a unified benchmark that links $5,000$ human-written source texts from five domains to more than $240,000$ variants produced using six generative models under Prefix-Conditioned Continuation as a reference setting and three collaborative production modes. We evaluate $21$ detectors through four protocols spanning zero-shot and pretrained supervised document-level detection, boundary localization, and cross-condition generalization. Relative to Prefix-Conditioned Continuation, mean AUROC across document-level detectors is $12.0\%$ lower on the collaborative production modes, with the largest detector-specific relative decrease reaching $44.4\%$. Transfer across collaborative production modes is also asymmetric, indicating that performance in a given production setting is not a reliable predictor of performance in other production settings.

### 中文一句话结论
提出 C-HAT-Bench 中文人机协作文本检测基准，包含 5000 篇人类文本与 24 万余个人机协作变体；评测发现，检测器在协作生产模式下的平均 AUROC 相比全生成文本参考设置低 12.0%，最大检测器相对降幅达 44.4%，且跨生产模式迁移不对称。

### English TL;DR
C-HAT-Bench is a Chinese benchmark for detecting human-AI collaborative text, built from 5,000 human-written source texts and over 240,000 variants produced by six generative models under three collaborative production modes. Evaluating 21 detectors shows that mean AUROC drops by 12.0% (with the largest detector-specific relative decrease reaching 44.4%) compared with fully generated text, and that cross-mode generalization is asymmetric.

### 中文详细总结
现有机器生成文本（MGT）检测器大多只在“完全人类写作 vs. 完全 AI 生成”的二分类设置下评测，而人机协作可能削弱或重新分布检测线索，使二分类上的强表现高估检测器的实际可靠性。中文场景下这一问题尤为欠缺研究：检测线索受到分词和语言特定文本分布影响，但可控资源有限。为此，论文提出 C-HAT-Bench，一个统一的中文人机协作文本检测基准：将来自 5 个领域的 5000 篇人类源文本，与由 6 种生成模型在 Prefix-Conditioned Continuation 参考设置和 3 种协作生产模式下产生的 24 万余个变体关联起来。作者评测了 21 个检测器，覆盖零样本与预训练监督的文档级检测、边界定位和跨条件泛化四类协议。结果显示，相对于 Prefix-Conditioned Continuation，文档级检测器在协作生产模式上的平均 AUROC 低 12.0%，最大检测器相对降幅达 44.4%；协作生产模式之间的迁移也不对称，说明某一生产设置下的表现不能可靠预测其他生产设置下的表现。

### 方法 / 贡献
- 提出 C-HAT-Bench，一个将人类中文源文本扩展到多种人机协作变体的统一基准。
- 覆盖 5 个领域、6 个生成模型、3 种协作生产模式，并以 Prefix-Conditioned Continuation 作为参考设置。
- 系统评估 21 个检测器，采用 4 类协议：零样本文档级检测、预训练监督文档级检测、边界定位、跨条件泛化。
- 揭示协作生产模式显著降低检测性能，且跨协作模式迁移不对称，弥补中文环境下相关评测资源的不足。

### 实验或数据
- 数据规模：5000 篇人类撰写源文本，来自 5 个领域；通过 6 个生成模型产生超过 240,000 个变体。
- 生产设置：Prefix-Conditioned Continuation 参考设置，以及 3 种协作生产模式。
- 评测对象：21 个检测器。
- 主要结果：文档级检测器在协作生产模式上的平均 AUROC 比 Prefix-Conditioned Continuation 低 12.0%；最大检测器相对降幅为 44.4%。
- 跨协作生产模式的迁移结果不对称，表明模式间性能不可靠预测。

### 值得关注点
- 现有 MGT 检测评测过度依赖“完全人类 vs. 完全 AI”二分类，可能高估实际场景下的可靠性。
- 人机协作会削弱或重新分布机器生成线索，协作模式成为检测器性能下降的关键来源。
- 中文特有的分词和文本分布使得该问题需要专门的中文基准评测。
- 跨协作生产模式迁移不对称，提示检测器在一种生产设置下的表现不能外推到其他设置。

### 局限性
摘要未明确讨论局限性。从基准设定看，其范围限于中文文本、6 种生成模型和 3 种协作生产模式，因此结论的泛化范围也限于这些设定；具体资源设计或评测协议之外的潜在限制在摘要中未提供。

## 10. Large Language Models for Automated Cross-Domain Machine Learning Task Type Identification: A Benchmark Dataset and Evaluation

- Source: arxiv
- arXiv ID: 2609.35335
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.35335v1
- PDF: https://arxiv.org/pdf/2609.35335v1
- DOI: https://doi.org/10.48550/arXiv.2609.35335

### Authors

Petros Tsialis, Steffen Limmer, Tobias Rodemann, Martin Heckmann

### Abstract

Machine learning task type identification is essential for constructing valid ML pipelines, yet in practice it is typically specified manually. We investigate whether large language models (LLMs) can infer both the data domain and the downstream prediction task directly from dataset-level information when only the target feature is provided by the user. Together with our LLM-based system we also release an annotated benchmark comprising 625 public tabular and time series datasets. We evaluate the proposed approach in three settings: (i) tabular datasets in comparison with established AutoML heuristics, (ii) cross-domain evaluation across tabular and time series datasets, and (iii) a practical deployment scenario using smaller local models. The results show consistent advantages for LLM-based task type identification, with increasing difficulty in heterogeneous and resource-constrained settings. LLM-based approaches outperform AutoGluon in the tabular setting, reaching 0.98 F1 macro compared to 0.93. In the cross-domain setting, the best model achieves 0.90 F1 macro, while smaller locally deployable models reach 0.75, indicating a trade-off between deployment feasibility and accuracy.

### 中文一句话结论
本文提出利用大语言模型（LLM）从数据集信息中自动推断数据域和下游机器学习任务类型，在625个数据集基准上表现优于AutoML方法，但较小模型存在精度权衡。

### English TL;DR
This paper introduces a benchmark and LLM-based system for automated cross-domain ML task type identification, showing that LLMs consistently outperform AutoML heuristics (achieving 0.98 F1 macro vs. AutoGluon's 0.93 on tabular data) and effectively handle heterogeneous settings, though with a noticeable accuracy trade-off when using smaller, locally deployable models.

### 中文详细总结
论文研究了大语言模型（LLM）在仅提供目标特征的情况下，能否自动识别数据域（表格型或时间序列）和下游预测任务（分类、回归/预测）。作者构建了一个包含625个公开表格和时间序列数据集的标注基准，并提出了一个基于LLM的系统，该系统通过目标变量统计、数据集序列化、组采样和提示设计来推断任务类型。实验分别在三个场景中评估：1）表格数据集上对比AutoML启发式方法（AutoGluon、H2O、NaiveAutoML）；2）跨域（表格+时间序列）评估；3）使用小型本地部署模型。结果表明，LLM在表格设置下达到0.98的F1 macro（AutoGluon为0.93），跨域设置下最佳模型达0.90，小型本地模型达0.75，体现了部署可行性与精度之间的权衡。该系统和方法已开源。

### 方法 / 贡献
- **方法**：系统以数据集和目标特征为输入，提取目标统计信息（如唯一值、均值、标准差等）并进行数据集序列化（保留特征名称和行结构），再通过组采样控制输入长度，最后构建系统提示和用户提示（可选包含数据集描述和少量样本示例）。使用GPT-5.3（云端）和Qwen系列（本地）模型进行零样本和少样本推理。
- **贡献**：首次公开专门用于机器学习任务类型识别的基准（625个数据集，覆盖表格和时间序列，包含二级分类）；提出基于LLM的自动化识别系统，证明其优于传统AutoML启发式方法；分析了跨域能力和资源受限场景下的性能权衡。

### 实验或数据
- **数据**：包含625个公开数据集（299个时间序列，326个表格），来源于OpenML、UCI、Kaggle和时间序列分类档案，分为二进制分类、多类分类、回归/预测。数据集被划分为训练/验证/测试集（20/40/40%）。
- **实验**：
  1）表格数据集：LLM（GPT-5.3）达0.98 F1 macro，超过AutoGluon（0.93）、H2O（0.92）和NaiveAutoML（0.90）。
  2）跨域（表格+时间序列）：最佳模型达0.90 F1 macro。
  3）小型本地模型：Qwen3-4B FP8变体达0.75 F1 macro，而Qwen3-14B等较大本地模型可达更高但需高性能GPU。

### 值得关注点
- LLM在无数据集描述仅靠目标统计时也表现良好，展示了从数据本身推断任务的能力。
- 跨域设置（表格+时间序列）中LLM仍保持较高性能（0.90 F1），表明其适用于异构数据环境。
- 小型模型在消费级硬件上可部署（如RTX 5090），但精度下降明显，适合对准确性要求不高的场景。
- 基准数据集和系统均已开源，可复现。

### 局限性
- 实验仅覆盖表格和时间序列数据域，未涉及文本、图像等其他模态。
- 小型本地模型（4B FP8）的F1仅0.75，在资源受限场景下准确性不足。
- 任务识别仅依赖于目标特征和统计信息，可能缺乏对数据整体语义的深层理解，尤其在数据集描述不可用时。
- 对比的AutoML框架仅限于表格数据，跨域设置中未与时间序列专用AutoML系统比较。
- 提示设计对性能影响大，最优配置需针对不同模型搜索，泛化性有限。

## Processing Notes

- Duplicate papers skipped: 0