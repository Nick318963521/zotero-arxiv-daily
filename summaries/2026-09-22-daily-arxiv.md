# Daily arXiv - 2026-09-22

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-22T01:02:15
- Paper count: 10

## 1. Geometry of Values: Task Vector Composition for Ethical Preference Alignment in Language Models

- Source: arxiv
- arXiv ID: 2609.21094
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.21094v1
- PDF: https://arxiv.org/pdf/2609.21094v1
- DOI: https://doi.org/10.48550/arXiv.2609.21094

### Authors

Utkarsh Agarwal, Monojit Choudhury

### Abstract

Large Language Models (LLMs) are increasingly deployed in applications that must weigh clashing moral values, yet even strong models exhibit hidden biases and brittle instruction-following across languages. We introduce a 12,000-instance dataset of two-option dilemmas covering pairwise three value conflicts: Honesty vs. Justice, Justice vs. Autonomy, and Autonomy vs. Honesty, along with their translations into Hindi, Arabic, Spanish, and Chinese, to probe cross-lingual behavior. Benchmarking on GPT-5-mini reveals that it consistently favors Honesty over Autonomy across all five languages when no policy is given. The Llama-3.2-1/3B models exhibit strong first-option bias; however, both plain fine-tuning and Direct Preference Optimization fine-tuning effectively remove this bias, increasing accuracy to greater than 98%. In order to decouple the effect of learning correlations in the dataset from abstract values, we propose a task vector transfer based experiment where after computing the task vectors for a direction of value preference we orthogonalize it with respect to the general instruction following vector. Our experiment shows that this method is effective in isolating the direction of the specific value preference that can successfully be used to conduct task arithmetic to obtain a model with the opposite stance.

### 中文一句话结论
本文提出一种基于任务向量正交化的轻量级方法，能够从微调后的模型中提取并反转特定价值偏好，实现无需重新训练即可按需切换伦理立场。

### English TL;DR
The paper introduces a multilingual dataset of ethical dilemmas, benchmarks LLMs for value preferences, and proposes a task-vector method that orthogonalizes preference vectors from instruction vectors to isolate and transfer ethical stances, enabling modular preference reversal without retraining.

### 中文详细总结
大型语言模型在需要权衡冲突道德价值的应用中部署日益增多，但即使强模型也表现出隐藏偏见和跨语言指令遵循不稳定的问题。本文构建了一个包含12,000个实例的数据集，涵盖诚实vs.正义、正义vs.自主、自主vs.诚实三对价值冲突的二元困境，并翻译为印地语、阿拉伯语、西班牙语和中文，以探究跨语言行为。在GPT-5-mini上的基准测试表明，该模型在没有给定策略时，在所有五种语言中一致偏好诚实胜过自主。Llama-3.2-1/3B模型表现出强烈的首选项偏差；但通过普通微调和直接偏好优化微调均可有效消除此偏差，准确率提升至98%以上。为了解耦数据集中相关性的学习与抽象价值，作者提出一种基于任务向量迁移的实验：在计算价值偏好方向的任务向量后，将其与通用指令遵循向量正交化。实验表明，该方法能有效隔离特定价值偏好的方向，并成功用于任务算术以获取具有相反立场的模型。

### 方法 / 贡献
1. 形式化了伦理困境的定义，并创建了涵盖三对价值冲突的多语言平行数据集（12,000实例）。  
2. 通过LoRA（SFT/DPO）微调证明小型模型可以学习稳定的伦理策略并消除位置偏差，而更大模型仅通过指令提示仍表现出脆弱性。  
3. 提出一种简单的任务向量方法：从偏好对齐的检查点中提取偏好方向，估计并减去仅指令成分以隔离偏好向量，然后按比例缩放并减去该向量实现偏好反转，同时保留大部分全微调性能。  
4. 通过人工标注的黄金验证集验证了所学习策略的泛化能力。

### 实验或数据
- **数据集**：12,000个二元困境实例，分为三对价值冲突（AB、BC、CA），每对包含4000样本；翻译为五种语言（英语、印地语、阿拉伯语、西班牙语、中文）。  
- **基准测试**：GPT-5-mini在所有语言中一致偏好诚实优于自主；Llama-3.2-1/3B存在强首选项偏差。  
- **微调实验**：使用LoRA进行SFT和DPO微调后，模型准确率超过98%，消除首选项偏差；在人工标注的黄金测试集上验证泛化性。  
- **任务向量实验**：通过正交化偏好向量与指令向量，成功实现偏好反转（例如从诚实>正义切换到正义>诚实），并观察到偏好向量间几乎正交，无法可靠实现传递性组合。

### 值得关注点
- **跨语言一致性**：GPT-5-mini在不同语言中表现出稳定且一致的偏好（诚实优先），表明模型存在固有价值偏见。  
- **位置偏差完全消除**：小模型通过微调可完全克服首选项偏差，准确率接近完美。  
- **模块化偏好反转**：任务向量方法使得无需重新训练即可在推理时切换价值优先级，支持价值多元主义。  
- **非传递性发现**：任务向量算术无法可靠实现价值偏好的传递组合，表明抽象价值表示的几何结构可能存在近正交关系。

### 局限性
- 研究仅聚焦于三种价值（诚实、正义、自主），未覆盖更广泛的伦理原则。  
- 数据集部分由生成模型创建，虽经自动验证和人工评估，但可能存在噪声和模板偏差。  
- 实验仅限于1B-3B参数的小型模型，结论可能不适用于更大规模的模型。  
- 价值偏好和指令遵循向量的正交化方法依赖于特定任务向量定义，其可迁移性尚未在多种架构上验证。  
- 论文未探讨价值偏好反转后模型在其他任务上的能力保持情况。

## 2. FairLMs: A Turnkey Library for Fairness in Language Models

- Source: arxiv
- arXiv ID: 2609.21296
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.21296v1
- PDF: https://arxiv.org/pdf/2609.21296v1
- DOI: https://doi.org/10.48550/arXiv.2609.21296

### Authors

Jiale Zhang, Michael Larionov, Zichong Wang, Zhipeng Yin, Wenbin Zhang

### Abstract

Fairness research on language models involves measuring bias, applying mitigation methods, and examining the evidence on which an evaluation rests. Existing tools offer complementary functionality through different interfaces, so combining them requires reconciling model interfaces, evidence formats, access constraints, and result types before applicability can be checked or methods compared. We introduce \textbf{FairLMs}, a Python library that connects these activities through explicit declarations of model capabilities and input requirements. It provides 33 intrinsic and extrinsic metrics, 14 mitigation components spanning four intervention categories, 14 dataset and scoring-instrument diagnostics, adapters for the three Transformer architectures and supported hosted completion APIs, and benchmark loaders. Declarations are checked before execution and results carry the configuration under which they were obtained, so that compatible components can be combined, methods compared under a common protocol, and workflows extended to new models and datasets. The source code is available at: https://github.com/FairLMs/FairLMs.

### 中文一句话结论
FairLMs 是一个将语言模型公平性研究中的偏差测量、缓解与数据/评分工具诊断整合于统一接口的 Python 库，通过显式声明模型能力与输入需求，实现了 33 个指标、14 个缓解组件和 14 个诊断工具的可复现与可组合工作流。

### English TL;DR
FairLMs is a turnkey Python library that unifies bias measurement, mitigation, and dataset/scoring-instrument diagnostics for language models through explicit capability and requirement declarations, enabling reproducible and composable fairness research with 33 metrics, 14 mitigation components, and 14 diagnostics.

### 中文详细总结
FairLMs 旨在解决语言模型公平性研究中工具链碎片化的问题。现有工具（如 AIF360、Fairlearn、WEFE、LangFair 等）分别覆盖部分流程，但整合它们需要手动协调模型接口、证据格式、访问限制和结果类型。FairLMs 通过让所有组件声明其适用的模型架构、能力需求和证据容器，并在执行前进行兼容性检查，实现“一次适配，多处复用”。库内包含 33 个内在/外在偏差指标、14 个跨四类干预的缓解方法、14 个数据集与评分工具诊断组件，以及针对三种 Transformer 架构（编码器、解码器、编码器-解码器）和托管补全 API 的适配器。每个结果都携带其配置、证据哈希和库版本，确保可追溯性和可复现性。设计上，缓解器返回的结果类型（如变换后的证据、损失组件、模型适配器或输出规则）明确声明，支持标准化的前后对比评估。诊断组件不调用目标模型，而是审计数据集和评分工具本身，以识别偏差来源。New components adhering to the same declarations can extend the library without modifying its core.

### 方法 / 贡献
- **统一接口与显式声明**：所有组件（度量、缓解、诊断）声明其支持的架构、能力需求和证据容器类型，执行前自动检查兼容性。
- **模型适配器**：封装编码器、解码器、编码器-解码器及托管 API 的标记化和输出访问，兼容的度量复用同一适配。
- **缓解方法集成**：支持数据增强、对抗性去偏、组感知阈值等14种方法，通过 `apply` 接口返回类型化结果，并利用 `compare_before_after` 在相同配置下比较基线与缓解后系统。
- **诊断组件**：14种诊断（代表性、刻板印象泄漏、构造偏差、评分工具行为）不依赖目标模型，审计数据集和评分工具。
- **可复现性**：结果记录配置、证据哈希和库版本，便于追踪和复现。

### 实验或数据
- 集成了 16 个内置基准加载器（如 CrowS-Pairs、StereoSet），并支持用户自定义数据。
- 对具有公开参考值的度量族，在相同检查点和证据下运行，复现了参考实现报告的值（精度与原文一致）。
- 提供契约测试套件，验证每个注册组件的声明和应用性，检查所有状态（就绪、阻塞、不适用、失败）。

### 值得关注点
- 统一的声明和检查机制避免了不支持的组合在计算前被忽略，提高了工作流效率。
- 诊断组件不调用模型，可先审计基准再评估模型，帮助区分模型偏差与数据/评分偏差。
- 支持从训练到评估、从原始数据到最终报告的完整流程，并通过前后对比实现缓解效果评估。

### 局限性
- 摘要未详细说明实验的全面性（如跨模型、数据集的数量），或是否覆盖所有主流语言模型；仅提及对度量族与参考实现的验证。
- 依赖公开参考值进行正确性验证，未提供大规模独立基准或消融实验结果。
- 对于支持托管 API，可能受访问策略和速率限制影响，具体细节未在摘要中讨论。

## 3. Accelerating Dense LLMs via L0-regularized Mixture-of-Experts

- Source: arxiv
- arXiv ID: 2609.21672
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.21672v1
- PDF: https://arxiv.org/pdf/2609.21672v1
- DOI: https://doi.org/10.48550/arXiv.2609.21672

### Authors

Zhenyu Zhang, Jiudong Yang, Zhaowen Tao, Meng Chen

### Abstract

Large language models (LLMs) achieve strong performance but suffer from slow and costly inference. Existing acceleration methods often lead to noticeable performance degradation, while Mixture-of-Experts (MoE) models require extensive computational resources. In this paper, we propose L0-MoE, a lightweight MoE approach using L0-regularization to accelerate dense LLMs nearly without performance loss. Our method introduces a cluster confusion matrix for domain-aware dataset curation and applies dynamic batching for efficient training. Experiments show that L0-MoE achieves up to 2.5x speedup over dense models while maintaining competitive performance, outperforming existing LLM acceleration baselines.

### 中文一句话结论
L0-MoE通过L0正则化、基于聚类混淆矩阵的数据筛选和动态批处理技术，将稠密大语言模型高效转换为轻量级混合专家模型，在仅30B token的小规模语料上训练即可实现高达2.5倍的推理加速，且性能几乎无损。

### English TL;DR
L0-MoE converts dense LLMs into lightweight MoE models via L0-regularization, cluster confusion matrix-based dataset curation, and dynamic batching. It achieves up to 2.5x inference speedup with minimal performance loss using only 30B tokens of training data.

### 中文详细总结
L0-MoE提出了一种将已有稠密大语言模型（如Llama-3-8B、Mistral-7B）高效转换为稀疏混合专家（MoE）模型的方法，旨在在不显著损失性能的前提下加速推理。该方法包含三个核心步骤：（1）**基于聚类混淆矩阵（CCM）的数据筛选**：从RedPajama语料中采样小规模子集，利用BGE-M3编码器提取语义向量，通过K-means聚类划分域，并定义CCM衡量不同采样迭代中域语义差异，从而筛选出语义区分度高的训练数据；（2）**基于L0正则化的专家构建**：针对每个数据域，在预训练稠密LM的FFN层上应用L0正则化，逐步剪枝不重要的中间维度，形成多个领域专家；（3）**动态批处理训练**：设计两阶段批构建策略，先在域内语义相似度高的数据上训练以快速初始化路由器，再逐步引入语义差异大的数据以增强路由器的跨域选择能力。

### 方法 / 贡献
- 提出L0-MoE方法：利用L0正则化为已有稠密LLM的FFN层创建轻量专家，避免从零训练或大规模上循环。
- 引入聚类混淆矩阵（CCM）：通过多轮K-means聚类和跨/内聚类相似度评估，筛选语义区分度高的子数据集，提升训练效率。
- 提出动态批处理调度：先低域差异数据后高域差异数据，分阶段训练路由器，兼顾初始化与泛化能力。
- 在实验上验证：仅用30B token的小语料训练，即可在多个基准上保持性能的同时实现2.0-2.5倍推理加速。

### 实验或数据
- 基于Llama-3-8B和Mistral-7B两个稠密基线模型。
- 使用约30B token的小规模训练语料（源于RedPajama并通过CCM筛选）。
- 评估基准：MMLU、GSM8K、HumanEval、BBH。
- 结果举例：Llama-3-8B上平均性能仅下降0.2%（从53.5到53.3），但实现2.0倍加速；Mistral-7B上平均性能提升1.0%（从50.4到51.4），实现2.1倍加速。

### 值得关注点
- 在小语料（30B token）上成功构建MoE，大幅降低了传统MoE所需的计算和数据成本（如DeepSeek-V3的14.8T token）。
- 性能几乎无损甚至略有提升，优于已有的量化、剪枝等加速方法。
- 方法不依赖重新预训练，可直接基于社区发布的稠密检查点进行转换，实用性强。

### 局限性
- 仅在两种7-8B规模模型上验证，更大模型（如70B+）上的效果和加速比有待测试。
- 依赖K-means聚类和BGE-M3编码器，引入额外数据处理步骤和超参数（如δ、β、域数K）调优。
- 动态批处理策略增加训练复杂度，对序列长度和批大小敏感。
- 论文未提供详细的消融实验（如去除CCM的影响、L0正则化比率调整的影响）。
- 未展示模型在更长序列或真实推理延迟上的详细对比（仅提及speedup倍数）。

## 4. LLMs as Feature Engineers for Text-and-Tabular Prediction

- Source: arxiv
- arXiv ID: 2609.21894
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.21894v1
- PDF: https://arxiv.org/pdf/2609.21894v1
- DOI: https://doi.org/10.48550/arXiv.2609.21894

### Authors

Merwan Barlier, Blaz Skrlj

### Abstract

We introduce an iterative framework that automates the extraction of interpretable, schema-bound categorical features from unstructured text for tabular prediction models. To navigate the feature space, a generator LLM proposes semantic definitions, a separate extractor LLM materializes the features, and a downstream tabular model evaluates their predictive performance. We optimize this search by translating explicit model errors, such as AUC ranking inversions, into natural-language feedback, steering the LLM to resolve specific predictive failures. Evaluated across three public datasets, this error-driven loop accelerates feature discovery by up to $3\times$ compared to unguided search. Empirically, the generated features demonstrate strong multi-view complementarity, strictly outperforming any subset when combined with TF-IDF and dense embeddings. Finally, the framework guarantees instance-level interpretability: the discovered features dominate SHAP importance rankings and provide a fully transparent, semantic audit trail for every prediction.

### 中文一句话结论
本文提出一种迭代式框架，利用大语言模型自动从非结构化文本中提取可解释的、模式绑定的分类特征，通过将模型错误转化为自然语言反馈来引导特征搜索，显著提升表格预测性能与实例级可解释性。

### English TL;DR
This paper introduces an iterative, error-driven framework that uses LLMs to automatically extract interpretable, schema-bound categorical features from unstructured text, accelerating feature discovery up to 3× and improving tabular prediction performance with instance-level interpretability.

### 中文详细总结
本文针对文本与表格混合预测任务，提出一个迭代式代理框架，自动化地从非结构化文本中提取可解释的分类特征。该框架包含三个核心组件：生成器LLM负责提出语义特征定义（包括名称、离散值集和描述），提取器LLM负责将定义应用于数据行进行零样本分类，下游表格模型负责评估特征预测性能。关键在于将模型的具体错误（如AUC排序反转）转化为自然语言反馈，指导LLM生成能够解决特定预测失败的特征。实验表明，这种错误驱动的反馈循环相比无引导搜索，特征发现速度提升最高3倍。生成的TF-IDF、稠密嵌入与LLM特征三者组合严格优于任意子集组合，且LLM特征在SHAP重要性排名中占据主导地位，为每个预测提供完全透明的语义审计轨迹。

### 方法 / 贡献
1. **迭代式特征工程框架**: 首个将LLM作为特征工程师处理非结构化文本的工作，提出"生成→提取→评估→反馈"闭环。
2. **多视角互补性**: 实证表明LLM生成特征、稠密嵌入与TF-IDF捕获条件独立信号，三者组合严格优于任何子集。
3. **实例级可解释性**: LLM特征在SHAP重要性排名中占主导地位，提供完全透明的语义审计轨迹。
4. **错误驱动的文本反馈机制**: 将下游模型错误转化为自然语言约束（如排名反转对），显著加速搜索收敛。

### 实验或数据
在三组公开数据集上评估：
- **Kickstarter**（众筹项目）
- **Amazon Books**（图书评论）
- **Stack Overflow**（问答内容）
实验设置：使用GPT-5.4作为生成器（每轮生成约90个特征），GPT-4.1-nano作为提取器（批量零样本分类），HistGradientBoostingClassifier作为下游表格模型。每轮迭代执行生成、提取、评分、贪婪前向选择、反馈计算五个步骤，通过AUC指标评估。

### 值得关注点
1. **模式绑定的分类定义**: 特征定义为结构化JSON（含名称、离散值集、语义描述），确保可解释性与可靠提取。
2. **计算解耦**: 生成器（复杂推理）与提取器（快速批量应用）分离，使用不同LLM，显著摊销推理成本。
3. **通用反馈机制**: 将AUC排序反转等具体错误转化为自然语言对比示例，精确指导下一个特征生成方向。
4. **无LLM实时推理**: 一旦特征定义确定，下游预测完全由快速表格模型执行，无需LLM参与。

### 局限性
1. **无LLM时框架无法工作**: 整个框架完全依赖LLM（至少GPT-4级别）的生成与提取能力。
2. **提取成本仍需控制**: 虽然使用更便宜的模型，但80K行数据仍需约30分钟完成特征提取。
3. **特征空间有限**: 当前每个特征仅支持约4个离散值的小集合，可能无法捕获细粒度语义信息。
4. **未提及噪声与鲁棒性分析**: 未系统评估LLM生成特征质量波动对整体预测性能的影响。
5. **未涉及多任务迁移**: 实验仅在单任务设置下验证，框架在跨任务特征复用方面的能力未探讨。

## 5. When Does Reasoning Help in Machine Translation? A Hierarchical Analysis of LRM Reasoning Traces

- Source: arxiv
- arXiv ID: 2609.21247
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.21247v1
- PDF: https://arxiv.org/pdf/2609.21247v1
- DOI: https://doi.org/10.48550/arXiv.2609.21247

### Authors

Yuxiang Liu, Jiaming Luo, Eleftheria Briakou, Colin Cherry

### Abstract

Large Reasoning Models increasingly use intermediate traces for machine translation, but it remains unclear when such reasoning helps or hurts. We analyze reasoning traces across models, languages, domains, and datasets, focusing on reasoning language, length, and structure. We find that the best reasoning language is model-specific, reasoning length has a non-monotonic relationship with quality, and traces exhibit recurring functional patterns. To uncover these patterns, we introduce Hierarchical Meta-Summarization (HMS), a scalable framework that induces coarse- and fine-grained reasoning structures without predefined taxonomies. HMS reveals a shared organization--understanding/planning, translating/drafting, and refining/verifying--alongside domain-specific variation. Our results suggest that MT reasoning should be controlled in a model-aware, length-aware, and pattern-aware manner rather than uniformly encouraged.

### 中文一句话结论
基于层次化元摘要（HMS）框架分析表明，推理语言、长度和结构对翻译质量影响复杂，最优推理策略需模型感知、长度感知和模式感知。

### English TL;DR
This paper analyzes reasoning traces in large reasoning model-based machine translation, finding that optimal reasoning language is model-specific, reasoning length has a non-monotonic effect on quality, and traces exhibit recurring functional patterns. It introduces Hierarchical Meta-Summarization (HMS) to reveal these patterns and advocates for controlled, not uniform, reasoning.

### 中文详细总结
本论文系统分析了大型推理模型（LRM）在机器翻译中生成的推理轨迹。研究涵盖6个模型（如DeepSeek-R1-Distill-Qwen-32B等）、3个数据集（WMT24++、CultureMT、DRT-Literature）和多个语言对。主要发现：（1）推理语言的最佳选择因模型而异，且与模型最可靠遵循的语言一致；（2）推理长度与翻译质量呈非单调关系：中等长度可能有益，过长则往往导致质量下降；（3）推理轨迹呈现重复的功能模式，通过层次化元摘要（HMS）揭示出通用结构：理解/规划、翻译/起草、精炼/验证，同时存在领域特定的变化。研究结论认为，应基于模型、长度和模式对推理进行精细化控制，而非统一鼓励更多推理。

### 方法 / 贡献
提出层次化元摘要（HMS）框架，可从推理轨迹中自动诱导出粗粒度和细粒度的功能结构，无需预定义分类体系。通过HMS揭示LRM在机器翻译中的共享结构（理解/规划、翻译/起草、精炼/验证）及领域特定分配。系统分析了推理语言、长度对翻译质量和效率的影响。

### 实验或数据
使用WMT24++（5个语言对）、CultureMT（3个语言对）和DRT-Literature（英中文学翻译）三个数据集。评估了6个模型：DeepSeek-R1-Distill-Qwen-14B/32B、gpt-oss-20B、DeepSeek-R1-Distill-Llama-8B、gemma-4-E4B-it、DRT-14B。采用COMET-22、MetricX和MetricX-QE作为翻译质量指标。每个源文本生成16个样本。

### 值得关注点
引入HMS方法可自动识别推理轨迹的功能结构，避免依赖人工分类。明确解释了推理长度与翻译质量的非单调关系，强调过度推理（overthinking）带来的负面影响。建议对推理进行模型感知、长度感知和模式感知的控制。

### 局限性
论文未明确讨论局限性。

## 6. Recursive Language Models Generalize Out of Domain

- Source: arxiv
- arXiv ID: 2609.20831
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.20831v1
- PDF: https://arxiv.org/pdf/2609.20831v1
- DOI: https://doi.org/10.48550/arXiv.2609.20831

### Authors

Chenxiao Yang, Zhiyuan Li, David McAllester, Nathan Srebro

### Abstract

We study when limiting what a language model can see improves learning. We compare standard CoT, the more general learner that reads the full trace, with recursive language models, which restricts itself by solving each subtask in an isolated context. In-distribution, this generality comes for free: CoT can efficiently simulate the recursive rule, so the IID generalization guarantee changes only by a constant factor, and recursion does not offer much. But out of domain, CoT can fit training by relying on context outside the current subtask, i.e. a shortcut that breaks once those tokens change; recursive context isolation rules out this failure mode. Even though CoT's class still covers the recursive rule, simplicity bias picks the shortcut over the truth. Thus, to go beyond distributional accuracy and truly reason, covering the right rule is not enough; this contrasts with classical learning theory.

### 中文一句话结论
递归语言模型通过隔离子任务上下文，消除了链式思维模型依赖捷径的失败模式，从而在域外泛化上显著优于标准链式思维模型。

### English TL;DR
Recursive language models, by isolating each subtask's context, achieve better out-of-domain generalization than standard chain-of-thought models, which tend to rely on spurious shortcuts.

### 中文详细总结
论文研究了限制语言模型所见内容何时能改善学习。标准链式思维（CoT）模型可以读取整个推理轨迹，是一种更通用的学习器，理论上可在分布内以常数因子模拟递归规则，因此递归在分布内并无优势。然而在域外场景下，CoT模型倾向于利用当前子任务之外的上下文捷径来拟合训练数据，一旦这些上下文 token 发生变化，模型就会失效。递归语言模型通过强制每个子任务在独立上下文中求解，排除了这种捷径依赖，从而获得更好的域外泛化。论文指出，即使 CoT 模型在假设类中包含正确的递归规则，由于简单性偏向，模型仍会选择捷径而非真理。这说明要实现超越分布准确性、真正推理，仅仅覆盖正确规则是不够的——这一结论与经典学习理论形成对比。

### 方法 / 贡献
- 理论分析了标准链式思维（CoT）与递归语言模型在分布内和域外泛化上的差异。
- 揭示了 CoT 模型在域外依赖上下文捷径的失败机制，并证明递归隔离上下文可消除该问题。
- 强调了“仅覆盖正确规则不足以保证泛化”的观点，指出简单性偏向在域外推理中的关键作用。

### 实验或数据
论文摘要中未提及具体实验或数据集，主要贡献为理论分析。

### 值得关注点
- 域外泛化失败的根本原因被归因于模型对上下文捷径的依赖，而非假设类表达能力不足。
- 论文首次将“简单性偏向”作为域外泛化的关键解释，与经典学习理论中的覆盖性观点形成鲜明对比。
- 递归语言模型的设计（隔离子任务上下文）提供了一种无需额外数据、纯粹通过架构约束提升泛化能力的方法。

### 局限性
- 论文未在真实语言任务或大规模模型上进行实验验证，目前仅停留在理论分析层面。
- 递归隔离上下文可能带来计算开销或序列长度限制，摘要未讨论实际部署中的效率问题。
- 理论分析假设了特定简单的任务结构（如寻根函数），其结论在更复杂任务中的适用性需进一步检验。

## 7. One Prompt Does Not Fit All: Self-Meta-Evolve for Personalized Information Extraction

- Source: arxiv
- arXiv ID: 2609.21626
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.21626v1
- PDF: https://arxiv.org/pdf/2609.21626v1
- DOI: https://doi.org/10.48550/arXiv.2609.21626

### Authors

Hongliang Li, Lu Wang, Yong Xu, Hanyang Chen, Zhitao Hou, Xiaoting Qin, Song Ge, Qingwei Lin, Dongmei Zhang

### Abstract

Large language models (LLMs) are increasingly deployed for enterprise information extraction (IE), where the same document must be reorganized differently for each user. Existing prompt optimization methods, however, rely on a single prompt optimized against a global objective, which is misaligned with the inherent user heterogeneity of real workplaces. We formulate enterprise IE as per-user prompt adaptation under interaction feedback and propose Self-Meta-Evolve, a hierarchical framework that maintains a dedicated prompt for each user and continuously refines it through a dual-loop process: an inner loop that edits structured prompts based on persona-conditioned feedback, and an outer loop that evolves the meta-prompt itself by distilling successful editing patterns. To enable scalable training and evaluation, we release a persona-driven IE benchmark of 292 simulated enterprise users, paired with a reproducible persona-generation pipeline grounded in O*NET occupational taxonomies. On this benchmark, Self-Meta-Evolve achieves a 74.58% success rate, outperforming the strongest prompt-optimization baseline by 13.56 absolute points, and reaches 52.54\% within only two iterations. A double-blind human study with twenty real professionals further confirms that prompts adapted by our framework win against static baselines in 71% of pairwise comparisons.

### 中文一句话结论
提出 Self-Meta-Evolve 框架，通过层次化双循环过程为每个企业用户定制信息抽取提示，在包含 292 个模拟用户的基准上取得 74.58% 成功率，超越最强逐提示优化基线 13.56 个百分点，且双盲人类研究中 71% 的成对比较偏好该框架生成的提示。

### English TL;DR
Self-Meta-Evolve is a hierarchical framework that personalizes prompts for each enterprise user via a dual-loop process: an inner loop that edits structured prompts based on persona-conditioned feedback, and an outer loop that evolves the meta-prompt by distilling successful editing patterns. On a persona-driven benchmark of 292 simulated users, it achieves a 74.58% success rate, outperforming the strongest prompt‑optimization baseline by 13.56 absolute points, and wins 71% of pairwise comparisons in a double‑blind human study with 20 real professionals.

### 中文详细总结
企业信息抽取（IE）中，同一份文档需根据不同用户的角色和偏好重新组织，但现有提示优化方法均采用单一全局提示，无法适应实际工作中的用户异质性。本文将此问题形式化为“基于交互反馈的逐用户提示适配”，并提出 Self-Meta-Evolve 框架。该框架为每个用户维护专用提示，通过内环（inner loop）根据 AI 用户（AI‑User）模拟的角色条件反馈编辑结构化提示，以及外环（outer loop）从成功的编辑轨迹中蒸馏并演化元提示（meta‑prompt），实现跨用户的持续改进。为支撑训练与评估，作者基于 O*NET 职业分类构建了一个包含 292 个可复现企业用户角色的提示驱动 IE 基准，并配以文档合成流程。在基准上，Self-Meta-Evolve 成功率达 74.58%，超过最强基线 ProTeGi 13.56 个百分点，且仅需两轮迭代即可达到 52.54%。此外，与 20 位真实专业人员的双盲人类研究显示，该框架适配后的提示在 71% 的成对比较中胜于静态基线提示。

### 方法 / 贡献
1. **问题形式化**：将企业 IE 建模为逐用户的提示适配问题，以用户反馈（而非全局标注）为优化信号，突破单一全局提示范式的局限。
2. **Self-Meta-Evolve 框架**：层次化双循环结构。内环执行角色条件化的结构化提示编辑（基于 AI‑User 给出的修订/删除反馈）；外环通过蒸馏成功编辑轨迹来演化元提示，使编辑策略可跨用户迁移。
3. **基于角色驱动的基准与人类验证**：从 O*NET 职业描述出发，经扩展、质量控制和文档合成，构建 292 个可复现的企业用户角色（含 STEM/人文专用测试集）。通过 20 名真实专业人员双盲实验验证模拟忠实度（Cohen's κ=0.71）。

### 实验或数据
- **基准数据集**：292 个企业用户角色（60/20/20 训练/开发/测试拆分），外加 50 个 STEM 角色和 50 个人文角色作为跨域测试集。每个角色合成 8–12 份企业文档（邮件、聊天记录、报告等），文档生成不泄露偏好信号。
- **主实验**：成功率为 74.58%，比最强逐提示优化基线 ProTeGi（61.02%）高 13.56 绝对百分点；仅两轮迭代即达 52.54%。
- **人类验证**：20 名真实员工进行双盲成对比较，Self-Meta-Evolve 提示在 71% 的对比中被认为更优；评分者间一致性 Cohen's κ=0.71。
- **消融与敏感性**：双层循环各自贡献显著；损失权重 λ_r / λ_d 在 [1.5, 2.5] 范围内稳定；不同 LLM 后端（GPT‑4、GPT‑5、Claude 3.5）均保持优势。

### 值得关注点
- 首次将提示优化从“单一全局最优”转向“用户级个性化”，更贴合企业真实场景。
- 利用 O*NET 标准职业分类和 LLM 角色扮演能力，构建了可复现、低成本的角色模拟与反馈管道。
- 外环元提示的跨用户蒸馏能力显著加速了新用户的适配，体现层次化设计的协同效果。
- 双盲人类研究提供了超过模拟实验的额外实证支持，增强了结果的可靠性。

### 局限性
- **对 AI 用户模拟的依赖**：现有研究表明 LLM 用户模拟的忠实度仅为中等（Dou et al., 2025），可能影响反馈质量；本文通过跨模型校验缓解，但未完全消除。
- **初始元提示要求**：外环演化依赖于一个高质量的初始元提示；恶劣初始值可能导致收敛缓慢或失败。
- **长期交互退化**：角色有效性在长时间交互中可能下降，虽然通过外层循环重置机制缓解，但并未完全解决。
- **数据与计算成本**：需要大量逐用户交互数据以支持内环编辑和外环蒸馏，在用户数量极大时资源开销较高。

## 8. MIRAGE: Multi-Perspective Creative Language Model Reasoning with Reinforcement Learning Guidance

- Source: arxiv
- arXiv ID: 2609.21554
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.21554v1
- PDF: https://arxiv.org/pdf/2609.21554v1
- DOI: https://doi.org/10.48550/arXiv.2609.21554

### Authors

Arash Lagzian, Srinivas Anumasa, Dianbo Liu

### Abstract

Recent advances in Large Language Models (LLMs) have revolutionized artificial intelligence and how human interact with AIs. Despite impressive advancements, LLMs struggle with complex mathematical, scientific, and logical tasks. Inspired by human cognitive flexibility - our ability to dynamically switch mental perspectives - we propose MIRAGE (Multi-perspective Inference-time Reasoning via Agent-Guided Exploration), a novel inference-time creative thinking framework. MIRAGE includes a Selector that prioritizes effective conceptual perspectives (e.g., algebraic, probabilistic) and a Reasoner that sequentially solves tasks until a confident solution emerges, otherwise aggregating multiple perspectives. Tested on GSM8K, MATH500, MMLU-Pro, and Game-of-24 benchmarks, MIRAGE consistently outperforms methods like Chain-of-Thought and diverse prompting ensembles, significantly boosting accuracy with minimal inference overhead, providing a scalable solution for practical applications.

### 中文一句话结论  
提出 MIRAGE 框架，通过强化学习训练的选择器动态选择二十种概念推理视角（如代数、概率），并由推理器顺序求解，在数学与逻辑基准上以极少额外开销显著提升准确率。

### English TL;DR  
MIRAGE is a novel inference-time reasoning framework that uses reinforcement learning to train a Selector to dynamically choose among twenty conceptual perspectives (e.g., algebraic, probabilistic) and a Reasoner to iteratively solve tasks; it outperforms Chain-of-Thought and diversified prompting ensembles on GSM8K, MATH500, MMLU-Pro, and Game-of-24 with minimal inference overhead.

### 中文详细总结  
MIRAGE 受人类认知灵活性启发，提出基于强化学习（REINFORCE）的多视角推理框架。框架包含两个模块：选择器（Selector）根据问题历史效果对二十个预定义概念视角（如代数、概率、博弈论等）排序；推理器（Reasoner）按排序依次求解，直到出现高置信度答案或聚合多个视角的结果。训练阶段选择器通过奖励函数（正确性 + 稀疏惩罚）学习高效选择视角，推理时平均仅需少于2次前向传递。在GSM8K、MATH500、MMLU-Pro、Game-of-24基准上，MIRAGE 较 Chain-of-Thought 等基线方法提升准确率最高达 +24.7个百分点，同时保持较低计算成本（多数基准不高于单次推理的2倍）。实验验证了该方法在五种基础模型（DeepSeek-v3、ChatGPT-4o、Claude 3.7-Sonnet、Gemini-Flash 2.0、Qwen2.5-7B）上的泛化性。

### 方法 / 贡献  
- **方法**：将推理视为视角选择与顺序求解过程。选择器（基于 Qwen2.5-7B，经 LoRA 微调）接受问题输入，输出二十个概念视角的概率分布，并通过 REINFORCE 算法训练（奖励为正确性减去视角数量惩罚）。推理器（Qwen2.5-14B 冻结）在每个选定视角下生成逐步推理。最终采用多数投票或置信度阈值决定输出。  
- **贡献**：(1) 首个在推理时学习选择概念视角的框架，无需修改基础模型参数；(2) 在多个基准上显著提高准确率，且推理成本仅为单一调用的 2 倍以内，较 DIPPER (n=5) 降低 5 倍；(3) 通过五种基模型验证其通用性。

### 实验或数据  
- **基准数据集**：GSM8K（数学应用题）、MATH500（竞赛数学）、MMLU-Pro（多学科推理）、Game-of-24（24点游戏）。  
- **对比方法**：Chain-of-Thought (CoT)、零样本 CoT、Self-Consistency、DIPPER 等多样化提示集成方法。  
- **结果**：MIRAGE 在所有基准上准确率超过 CoT（如在 Game-of-24 上提升 24.7 个百分点），同时保持与单次调用相近或略高的开销（平均 <2 次前向传递）。选择器训练数据来自 5700 个 MMLU 题目（每学科 100 个随机样本）。  
- **消融实验**：对比随机选择8个视角、全部20个视角及 RL 训练的选择器，验证了学习选择的有效性（RL 选择器以 8.1 个视角达到 74.0% 准确率，与全部20个视角的 74.5% 相当，但成本降低 60%）。

### 值得关注点  
- **认知启发**：将人类认知灵活性（多视角转换）显式建模为可学习的推理策略，具有理论支撑。  
- **效率与性能平衡**：在多数基准上只需不到 2 次推理即达到超过 CoT 的准确率，对实际部署友好。  
- **视角库设计**：二十个概念视角由专家手工设计，涵盖数学、科学、逻辑等领域，并呈现长尾分布（如代数、概率使用率最高）。  
- **训练简洁**：仅需少量训练样本（5700 个 MMLU 题目）即可学到高效的视角选择策略。

### 局限性  
论文未明确讨论方法的局限性。基于方法描述，潜在局限包括：(1) 视角库固定为20个，可能不覆盖所有问题类型；(2) 选择器需针对特定模型训练，迁移性未验证；(3) 实验仅在数学与逻辑任务上测试，对其他类型推理（如常识、开放生成）效果未知。(注意：未在原文中找到明确说明，根据方法推断)。

## 9. From Generation to Detection: Exploration of Discourse Driven Scenario based LLM Generated Fake News

- Source: arxiv
- arXiv ID: 2609.20838
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2609.20838v1
- PDF: https://arxiv.org/pdf/2609.20838v1
- DOI: https://doi.org/10.48550/arXiv.2609.20838

### Authors

Zeynep Özdemir, Murat Osmanoğlu, Sevgi Yiğit-Sert, Ömer Özgür Tanrıöver, Yılmaz Ar

### Abstract

In this study, we examine how modern LLMs generate and detect fake news under controlled settings across four manipulation scenarios. These are open-ended generation, rewriting, manipulation prompts and attribute based prompts grounded in the journalistic discourse framework. Firstly, using seven widely adapted models, we created a synthetic fake news corpus with 14000 generated articles across these four scenarios. Then we analyzed its linguistic properties to assess how closely model-generated news resembles real news structurally and semantically. Finally, to evaluate detection performance, we conducted experiments where each model judges generated fake news, starting with a basic detection prompt and improved prompts developed through an iterative refinement process that extracts misleading patterns from real-fake pairs. Our results revealed substantial variation across models in both generating and detecting misinformation, demonstrated that the generation strategy strongly influences detectability, and show that the refined prompt does not improve and often harms detection performance. Therefore, the study provides a systematic assessment of LLMs detection capability of LLMs generated fake news across typical generation scenarios.

### 中文一句话结论
本研究系统评估了七种大语言模型在四种基于新闻语篇框架的虚假新闻生成与检测中的表现，发现生成策略显著影响可检测性，而迭代优化的检测提示反而常常损害性能。

### English TL;DR
This study systematically evaluates how seven LLMs generate and detect fake news across four discourse-driven manipulation scenarios, finding that generation strategy strongly influences detectability while refined prompting often fails to improve—and can even harm—detection performance.

### 中文详细总结
该研究选取CNN/DailyMail数据集中的500篇真实新闻作为基线，采用七种大语言模型（Gemma 3-4B、Gemma 3-12B、Mistral-7B、Phi 4-14B、DeepSeek R1-7B、Llama 3.1-8B、Qwen 2.5-7B），在四种生成场景下共生成14,000篇虚假新闻文章。四种场景包括：开放式生成、基于原文的重写、操纵性提示以及基于Van Dijk新闻语篇框架的属性提示。随后，对生成的文本进行语言特性分析（句法复杂度、词汇焦点、语义相似性），并开展检测实验：每个模型先用基础检测提示对生成的虚假新闻进行判断，再使用通过500对真假样本迭代优化得到的改进提示进行检测。结果显示，模型在生成和检测虚假信息方面存在显著差异；生成策略强烈影响可检测性；但改进后的提示并未提升检测性能，反而经常造成损害。

### 方法 / 贡献
- 方法：设计了四种越来越复杂的虚假新闻生成场景（开放式、重写、操纵提示、属性提示），覆盖从无约束到基于语篇框架的操纵方式。使用七种LLM生成14,000篇虚假新闻。检测阶段先使用基础提示，然后让Gemma 3-12B从真假样本对中提取误导模式，构建改进提示进行对比。
- 贡献：首次联合考察LLM在更真实、受控的语篇驱动虚假信息设置下的生成与检测能力；将Van Dijk的新闻语篇框架引入属性提示，模拟恶意行为者如何微调新闻部分内容；采用迭代提示优化而非少样本学习，展示了提示设计对检测准确性的影响。

### 实验或数据
- 数据：从CNN/DailyMail数据集中选取500篇真实新闻作为基线。
- 实验：使用七种LLM生成14,000篇虚假新闻（每种模型、每种场景生成500篇，共4种场景×7种模型×500篇）。对生成的文本进行语言特性分析。检测实验包括基础提示检测和迭代优化提示检测，每种模型对所有生成的虚假新闻进行判断。
- 结果：生成策略显著影响可检测性；改进提示未提升且常损害检测性能。模型间差异大。

### 值得关注点
- 生成策略（尤其基于语篇框架的属性提示）使虚假新闻更具真实性，增加检测难度。
- 迭代优化的检测提示反而降低性能，表明简单提示增强策略可能无效。
- 不同模型在生成和检测虚假信息的能力上存在显著差异，且大模型不一定更好。

### 局限性
- 仅使用一个真实新闻来源（CNN/DailyMail），可能限制泛化性。
- 生成场景虽基于语篇框架，但未覆盖所有真实世界操纵方式。
- 检测实验仅使用单一迭代优化策略，未探索其他提示工程技术。
- 未与人类检测者或传统机器学习方法进行对比。

## 10. Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective

- Source: arxiv
- arXiv ID: 2609.21888
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2609.21888v1
- PDF: https://arxiv.org/pdf/2609.21888v1
- DOI: https://doi.org/10.48550/arXiv.2609.21888

### Authors

Chenye Ke, Zirui Liu, Qi Liu, Yan Zhuang, Jintao Zhang, Zhenya Huang, Shijin Wang

### Abstract

Detecting pretraining data in large language models is challenging because high likelihood can reflect either training exposure or strong generalization. In the joint space of prediction loss and predictive entropy, a likelihood-only detector uses a horizontal boundary and can mistake predictable non-members for members. Motivated by this, we introduce an inclined boundary that evaluates prediction loss relative to predictive entropy. Our analysis shows that entropy correction can preserve the expected membership signal while reducing its variance, thereby improving standardized member--non-member separation. We further extend the mean--variance analysis to the more general setting with a nonzero mean entropy gap. Interestingly, this entropy-adjusted score admits a Helmholtz free-energy interpretation, leading to Energy Transfer Detection (ETD), which views pretraining data detection from a macroscopic residual free-energy transfer perspective. Extensive experiments show that ETD achieves the best average detection performance, improving average AUROC by up to 3.5\% and TPR@5\%FPR by up to 5.1\%, while remaining robust across diverse settings.

### 中文一句话结论
提出基于自由能视角的熵校正检测方法(ETD)，通过倾斜决策边界分离预训练与非训练数据，显著提升检测精度。

### English TL;DR
This paper introduces Energy Transfer Detection (ETD), an entropy-adjusted score from a Helmholtz free-energy perspective, which improves detection of pretraining data in LLMs by reducing variance and enhancing member–nonmember separation, achieving up to 3.5% higher AUROC and 5.1% higher TPR@5%FPR.

### 中文详细总结
本文从自由能视角出发，针对大语言模型预训练数据检测中仅依赖似然的方法易将泛化良好的非成员误判为成员的问题，提出将预测损失相对于预测熵进行校正，设计倾斜决策边界。理论分析表明熵校正可在保留期望成员信号的同时降低方差，提升标准化分离度。进一步将均值-方差分析推广至非零均值熵差情形，导出的熵校正分数具有亥姆霍兹自由能解释，形成能量转移检测(ETD)方法。大量实验表明ETD在多个设置下达到最优平均检测性能。

### 方法 / 贡献
提出ETD方法：利用预测损失与预测熵的联合空间，通过熵调整分数实现倾斜决策边界；理论证明熵校正可降低噪声方差；将检测问题视为宏观残余自由能转移；贡献在于首次将自由能视角引入预训练数据检测，并显著提升AUROC和TPR@5%FPR。

### 实验或数据
论文在多种模型和数据集上进行广泛实验，但摘要未明确列出具体数据集名称。实验涵盖不同设置，结果显示ETD相比基线在平均AUROC和TPR@5%FPR上分别提升最多3.5%和5.1%。

### 值得关注点
自由能视角的理论创新；熵校正机制；无需额外训练数据或模型修改；性能提升明显且鲁棒。

### 局限性
摘要未讨论局限性。可能依赖模型输出概率和熵，对于非自回归或掩码语言模型需进一步验证；实际中预训练数据的精确边界难以确定。

## Processing Notes

- Duplicate papers skipped: 0