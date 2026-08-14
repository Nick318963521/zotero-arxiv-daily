# Daily arXiv - 2026-08-14

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-14T22:58:49
- Paper count: 10

## 1. DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data

- Source: arxiv
- arXiv ID: 2608.13517
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2608.13517v1
- PDF: https://arxiv.org/pdf/2608.13517v1
- DOI: https://doi.org/10.48550/arXiv.2608.13517

### Authors

Peter Schneider-Kamp, Jacob Nielsen, Gianluca Barmina, Kenneth Enevoldsen, Lukas Galke Poech

### Abstract

Current large language model development relies on massive, often non-permissible datasets, creating a high barrier for researchers committed to open-source and ethically sourced data. We introduce Mimir v1, a 1-billion-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, that is trained from scratch and delivers highly competitive performance for English and sets a new state of the art for Danish using only permissible post-training data. Trained on a mixture of 161 datasets, Mimir v1 outperforms the original HRM-Text 1B and competes with larger frontier models like Qwen 3.5 4B and Gemma 4 E2B, tested across 20 benchmarks for English, Math & Code and Danish. The model is available on the Hugging Face Hub: https://huggingface.co/danish-foundation-models/DFM-Mimir

### 中文一句话结论
DFM Mimir v1 是一个基于HRM架构、仅使用许可数据训练的10亿参数语言模型，在英语上表现极具竞争力，并在丹麦语上刷新了最佳水平。

### English TL;DR
DFM Mimir v1 is a 1-billion parameter HRM language model trained entirely on permissible post-training data that achieves competitive English performance and a new state of the art for Danish.

### 中文详细总结
本文介绍了DFM Mimir v1，一个10亿参数的层级推理模型（HRM）。该模型完全从零开始训练，仅使用许可的后期训练数据，避免了常见的大规模非许可数据集。模型采用了HRM-Text架构，隐藏层维度1536，32层，12个注意力头，并使用了Gemma-4分词器。训练数据由161个数据集混合而成，每个epoch约705亿个token，涵盖英语指令、数学推理、丹麦语指令、智能体与工具使用等类别。数据分布中英语占68.6%，丹麦语占24.7%。在20个基准测试上，Mimir v1不但优于原始的HRM-Text 1B，而且能与更大的模型如Qwen 3.5 4B和Gemma 4 E2B竞争，特别是在丹麦语任务上达到了新的最佳水平。训练在8块NVIDIA B200 GPU上耗时约3周。模型可在Hugging Face Hub上获取。

### 方法 / 贡献
- **架构**：采用HRM-Text架构，配置2个H-cycle和3个L-cycle，截断反向传播步数5，使用RoPE位置编码和预层归一化。
- **训练策略**：从零开始训练，使用FSDP和bfloat16混合精度，AdamW优化器，峰值学习率3e-4，全局batch size 262,144 tokens，共训练165万步。
- **数据贡献**：仅使用许可数据，通过合成数据生成和审计替代不许可数据集（如“移植数据集”），证明合成数据在保持或提升性能的同时不侵犯数据权利。数据集包含161个来源，提供了详细的类别、语言分布和重复采样策略。

### 实验或数据
- **训练数据**：161个数据集，共705亿token/epoch，其中英语48.36B，丹麦语17.44B，以及其他。主要类别包括丹麦语指令与知识（22.1%）、英语指令（19.3%）、数学推理（14.8%）、智能体与工具使用（9.5%）等。数据集中前10个数据集占总token的66.5%。
- **评估基准**：20个基准测试，涵盖英语、数学与代码、丹麦语任务。对比模型包括HRM-Text 1B、Qwen 3.5 2B、Gemma 3、OLMo2、Qwen 3.5 4B、Gemma 4 E2B等。
- **主要结果**：Mimir v1在英语和数学/代码任务上表现优异，在丹麦语任务上达到新SOTA，与更大模型（4B参数级）竞争。

### 值得关注点
- 完全使用许可数据训练，降低了开源研究和低资源语言（如丹麦语）的进入门槛。
- 合成数据策略（如“移植数据集”）有效替代了非许可数据，且性能不降，为数据合规提供了新路径。
- 模型体量小（1B参数），训练和推理成本低，有利于社区复现和应用。
- 在丹麦语上取得显著进步，展现了HRM架构对低资源语言的有效性。

### 局限性
- 模型仅10亿参数，在极端复杂任务上可能不如更大规模模型。
- 训练数据高度集中（前10个数据集占66.5%），可能引入数据偏差或过拟合风险。
- 部分数据通过重复采样增强覆盖（如Lærebogen重复4倍），可能影响训练多样性。
- 合成数据虽经审计，但质量仍受限于生成模型（Gemma4 31B）和审计标准，存在潜在噪声。
- 当前仅支持英语和丹麦语，对其他语言的泛化能力未验证。
- 未提供与其他完全开源模型在完全一致基准上的详细对比，部分结果依赖模型提供方报告。

## 2. Class-Structure Preservation Beats Diversity: A Comprehensive Benchmark of Text Augmentation Methods for Imbalanced Text Classification

- Source: arxiv
- arXiv ID: 2608.12340
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2608.12340v1
- PDF: https://arxiv.org/pdf/2608.12340v1
- DOI: https://doi.org/10.48550/arXiv.2608.12340

### Authors

Keito Inoshita

### Abstract

With the rapid advancement of large language models (LLMs), generative data augmentation has attracted considerable attention for imbalanced text classification in natural language processing. However, no empirical benchmark to date has compared LLM-based augmentation against the embedding-space SMOTE-style retrieval (EmbSMOTE), a strong classical reference for imbalanced classification. In this study, a controlled benchmark of 11 augmentation methods, spanning classical perturbation, embedding-space retrieval, and LLM-based generation, is newly constructed on seven public text classification datasets covering class counts $K=2$-$28$ and imbalance ratios of 1.1 to over 500, evaluated with five random seeds per cell using macro F1, Welch's $t$-tests, five distributional metrics, and an LLM-family sensitivity analysis based on Qwen3-8B. The experimental results reveal that all LLM-based methods are statistically equivalent or inferior to EmbSMOTE, with the performance gap widening monotonically as imbalance increases and reaching $Δ\text{F1}_\text{macro}\!\approx\!0.063$ on GoEmotions-28. Furthermore, it is observed that surface-level uniqueness has negligible correlation with downstream performance, whereas LLM-specific artifacts, such as text elongation and label-distribution uniformization, are negatively associated with classification accuracy. Compared with six LLM-based and four classical augmentation baselines, these results demonstrate that the effective variable is not surface-level diversity but class-conditional structural fidelity, namely the degree to which augmented samples preserve the class-conditioned geometry of the training distribution. Accordingly, retrieval-based oversampling should be adopted as the default for imbalanced multi-class classification, and a higher empirical bar should be required before LLM-based augmentation is deployed in practice.

### 中文一句话结论
在 11 种数据增强方法、7 个数据集的受控基准下，基于嵌入空间的检索式过采样 EmbSMOTE 一致地等于或优于所有基于大语言模型的生成式增强方法；类别条件结构保真度而非表面多样性，才是不平衡文本分类中决定下游性能的关键。

### English TL;DR
Based on a controlled benchmark of 11 augmentation methods across 7 datasets, retrieval-based oversampling (EmbSMOTE) consistently matches or outperforms all LLM-based augmentation methods for imbalanced text classification. The key driver of downstream performance is class-conditional structural fidelity, not surface-level diversity.

### 中文详细总结
该研究针对不平衡文本分类，构建了包含 11 种增强方法的系统基准，覆盖经典扰动、嵌入空间检索和 LLM 生成三大类方法，并在 7 个公开数据集上进行实验。数据集涵盖类别数 K=2 到 28、不平衡比率从 1.1 到超过 500。每个实验单元使用 5 个随机种子，评估指标包括宏 F1、Welch t 检验、5 个分布度量，以及基于 Qwen3-8B 的 LLM 家族敏感性分析。

结果表明，所有基于 LLM 的增强方法在统计上均等价于或劣于 EmbSMOTE，且性能差距随不平衡程度增加而单调扩大，在 GoEmotions-28 上达到约 0.063 的宏 F1 差距。进一步分析发现，表面层面的文本唯一性与下游性能几乎没有相关性；相反，LLM 特有的伪影（如文本长度膨胀和标签分布均匀化）与分类准确率呈负相关。

因此，论文认为有效的变量并非表面多样性，而是类别条件结构保真度，即增强样本在多大程度上保持训练分布的类别条件几何结构。作者建议在不平衡多分类任务中默认采用检索式过采样方法，并认为 LLM 生成式增强在实际部署前需要更高的经验门槛。

### 方法 / 贡献
- 构建了 11 种增强方法 × 7 个数据集 × 5 个随机种子的受控基准，包含 4 种经典方法和 6 种 LLM 方法，并以 EmbSMOTE 作为强参照。
- 引入 VoidGen 作为方法学探针：采用“先定位后解码”（Locate-then-Decode）策略，在生成前定位嵌入空间中的稀疏区域，并通过投影器条件化 LLM 解码，用于检验预先生成目标定位是否足以带来结构保真优势。
- 使用 5 个分布度量量化增强集合，并分析其与宏 F1 及每类 F1 的相关性，从机制上解释类别条件结构保真度的重要性。
- 在相同算法超参数和提示下，跨 Llama-3.1-8B 与 Qwen3-8B 两个 LLM 家族复制了 LLM 增强劣于 EmbSMOTE 的结果。

### 实验或数据
- 数据集：SST-2、AG News、Emo、TREC、GoEmotions-13、DBpedia、GoEmotions-28。类别数从 2 到 28，不平衡比率从 1.12 到 527.67。
- 评估：每个方法-数据集组合使用 5 个随机种子，报告宏 F1，并使用 Welch t 检验进行多重比较校正。
- 主要结果：所有 LLM 方法均统计等价或劣于 EmbSMOTE；在 GoEmotions-28 上差距最大，Δ宏 F1 约 0.063。
- 相关性分析：表面唯一性与性能相关性可忽略；文本长度膨胀和标签分布均匀化与分类准确率负相关。
- LLM 家族敏感性：基于 Llama-3.1-8B 和 Qwen3-8B 的结果一致，说明瓶颈不在特定 LLM 的生成质量，而在于“先生成后验证”范式的结构性约束。

### 值得关注点
- EmbSMOTE 作为经典检索式方法，在高度不平衡的多类别文本分类中系统性优于更复杂的 LLM 生成方法。
- 类别条件结构保真度而非表面多样性是决定增强效果的核心因素。
- VoidGen 的结果表明，仅靠生成前定位稀疏嵌入区域并不足以保证结构保真，进一步强化了类别结构保持的必要性。
- 作者建议将检索式过采样作为不平衡多分类的默认方法，并对 LLM 增强的实际部署提出更高经验要求。

### 局限性
提供的摘要和预览内容未明确列出局限性。论文正文提到存在独立的“讨论”部分用于说明关键发现与局限性，但该部分的具体内容未包含在所给材料中，因此无法从本摘要中提取具体局限。

## 3. Prompts in the Wild: A Large Analyzed Collection of Transactional Prompts in Code

- Source: arxiv
- arXiv ID: 2608.12905
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2608.12905v1
- PDF: https://arxiv.org/pdf/2608.12905v1
- DOI: https://doi.org/10.48550/arXiv.2608.12905

### Authors

Victoria Basmov, Yoav Goldberg, Reut Tsarfaty

### Abstract

The behavior of contemporary generative Large Language Models (LLMs) is directly shaped by prompts, unstructured texts that describe the desired output and model behavior. In this paper we argue that prompts are linguistic objects that merit investigation in their own right. To this end, we collect 57.5K unique samples of prompts from GitHub. Specifically, we focus on transactional prompts: reproducible natural language instructions that are integrated into software. To enable the empirical, quantitative study of prompts, we introduce a structured ontology, capturing the properties of prompts as well as their formal and semantic components. Based on this ontology, we transform prompts from unstructured raw texts into richly structured linguistic objects. Analysis of these structured data reveals significant diversity of usage patterns across languages, domains, tasks, and modalities, in a typical Zipf-like distribution where some clearly prevail and others, more diverse, appear in the long tail. To validate the reliability of the ontology-based annotation of the prompts, we perform a comprehensive error analysis across all fields, providing a detailed assessment of annotation quality. We release the dataset together with a browsing and exploration interface (https://github.com/OnlpLab/transactionalPromptsCollection ).

### 中文一句话结论
本文收集了57.5K个来自GitHub的交易性提示（transactional prompts），并通过结构化本体将其转化为可分析的文本对象，揭示了提示在语言、任务和模态上的多样性，呈现齐普夫分布特征。

### English TL;DR
This paper presents a large-scale collection of 57.5K transactional prompts from GitHub, introduces a structured ontology to analyze them as linguistic objects, and reveals diverse usage patterns across languages, tasks, and modalities, with a Zipf-like distribution.

### 中文详细总结
本文认为提示（prompts）本身是有价值的语言对象，值得系统研究。作者从GitHub收集了57.5K个独特的交易性提示（即嵌入软件中的可重复自然语言指令），并设计了一个结构化本体，涵盖提示的多项属性（如语言、任务、领域、输入输出特征、指令结构、提示技术等）。基于此本体，将原始非结构化提示转化为带标注的结构化数据。分析表明：英语占主导（84.66%），但提示涉及62种语言，且存在多语言混合使用（仅6.3%的提示为多语言）；输入输出模态以文本为主（77.31%为文本到文本），但长尾中包含多种模态组合；领域和任务分布呈齐普夫模式，头部集中而长尾多样。作者还进行了全面的错误分析以验证标注质量，并发布了数据集及浏览界面。

### 方法 / 贡献
- **数据收集**：通过GitHub API检索调用`chat.completion.create`或`PromptTemplate`的代码文件，经静态分析解析变量和字符串，过滤去重后得到57,640个独特提示。
- **本体构建**：定义了包含语言、任务/领域、输入/输出特征、提示结构（角色消息、指令类型）、提示技术等维度的结构化本体，用于标注提示。
- **标注与验证**：使用LLM进行本体字段自动标注，人工检验并迭代优化后，对100个随机样本进行详细错误分析，多数字段准确率超过90%。
- **资源发布**：提供数据集及在线浏览搜索界面。

### 实验或数据
- **数据集规模**：57,640个独特交易性提示，其中36,916个来自`chat.completion.create`，20,724个来自`PromptTemplate`。
- **语言分析**：提示文本共检测到62种语言，英语占84.66%；提及的语言达151种。
- **模态分析**：77.82%的提示仅有文本输入；77.31%为文本到文本；常见组合包含文本+图像到文本等。
- **错误分析**：对100个随机样本进行人工评估，识别出主要失败模式，并加以量化。

### 值得关注点
- 将提示视为“语言对象”进行分析的创新视角，填补了提示系统研究的空白。
- 明确聚焦于“交易性提示”（即软件中可重复使用的提示），区别于一次性对话提示。
- 本体覆盖语义、结构、技术等多维度，支持定量分析。
- 语言多样性令人意外：虽英语主导，但提及了151种语言，提示文本涉及62种语言。
- 数据集和界面已公开，便于复现和扩展研究。

### 局限性
- 数据来源仅限于GitHub公共仓库，未包含企业级和闭源项目，可能存在偏差。
- 仅覆盖使用特定API（`chat.completion.create`和`PromptTemplate`）的项目，排除其他访问方式。
- 论文未提及模型训练或下游任务实验，仅进行数据收集与分析。
- 本体标注依赖LLM自动完成，虽经人工验证，但仍存在误差（错误分析显示部分字段准确率未达到100%）。
- 未涉及多轮对话或智能体（agentic）场景中的提示。

## 4. When Explanations Betray Backdoors: Black-Box Auditing for Language Model Classifiers

- Source: arxiv
- arXiv ID: 2608.12623
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.12623v1
- PDF: https://arxiv.org/pdf/2608.12623v1
- DOI: https://doi.org/10.48550/arXiv.2608.12623

### Authors

Yang Liu, Ran Zou

### Abstract

Language model classifiers with explanations are used for moderation, routing, topic triage, and low-resource annotation. We study black-box auditing when the defender has only clean calibration data without trigger information but can ask the classifier for a label plus a short rationale or quoted evidence. We introduce Groundedness Drift, a lightweight score measuring whether the answer summary remains grounded in the input. Across two 7B backbones, five datasets, and four common non-adaptive OpenBackdoor-style attack families, Groundedness Drift achieves higher AUROC and lower residual target ASR than every compared detector in all cases at a nominal 5\% clean-FPR budget. We then evaluate Unsupported Groundedness, a multi-probe escalation for explanation-camouflage stress cases. Unsupported Groundedness improves signals but does not close the adaptive gap.

### 中文一句话结论
本文提出Groundedness Drift（GD）轻量级分数，通过测量语言模型分类器解释文本与输入间的语义关联性，在仅使用少量干净校准数据和黑盒查询条件下，有效检测后门攻击，并在多个基准上优于现有检测器。

### English TL;DR
Groundedness Drift, a lightweight black-box auditing score that measures whether a language model classifier's rationale remains grounded in the input, detects backdoor attacks with higher AUROC and lower residual attack success rates than existing detectors across multiple backbones and attack families.

### 中文详细总结
本文研究黑盒后门审计场景：防御方仅有干净校准数据（256个样本），无触发器信息，但可请求模型输出标签及简短解释（如引用证据）。作者提出Groundedness Drift（GD）分数，通过词法和TF-IDF衡量解释文本与输入文本的关联性。在2个7B骨干模型、5个数据集、4种非自适应攻击家族（BadNets、AddSent、EP、SOS）下，GD在名义5%干净FPR预算下，AUROC均高于对比方法（ONION、BBCaL、CoS、推理提示基线），且残余目标攻击成功率（rASR）更低。针对自适应解释伪装攻击，提出多探针升级方法Unsupported Groundedness（UG），但未能完全消除自适应攻击的检测差距。

### 方法 / 贡献
1. 提出黑盒审计场景：防御方仅需干净校准数据（无触发器信息），可请求标签+简短解释。
2. 设计GD分数：轻量级单次查询，计算解释与输入文本的词汇重叠和TF-IDF相似度。
3. 引入UG升级流程：针对解释伪装攻击，检查引用证据支持度、证据删除/保留后的预测一致性及局部视图一致性。
4. 系统对比多种基线（ONION、BBCaL、CoS、推理提示），并在固定假阳性率预算下评估。

### 实验或数据
- 骨干模型：2个7B参数语言模型。
- 数据集：5个文本分类数据集。
- 攻击类型：4种非自适应OpenBackdoor家族（BadNets、AddSent、EP、SOS），另单独测试自适应解释伪装攻击。
- 校准集大小：256个干净样本。
- 评估指标：AUROC、残余目标攻击成功率（rASR）、干净假阳性率（clean-FPR）。
- 结果：GD在所有配置下AUROC更高，rASR更低；UG部分恢复检测信号，但未消除自适应攻击差距。

### 值得关注点
1. GD仅需单次查询和轻量级词法/TF-IDF计算，实用性强。
2. 在非自适应攻击下，GD显著优于现有方法，且无需触发器知识。
3. 提出UG作为解释伪装场景的升级方案，尽管未完全解决自适应攻击，但提供了可扩展的检测框架。
4. 防御方仅利用模型输出的解释信号，无需访问权重或训练数据。

### 局限性
1. 实验仅覆盖7B参数模型，未验证更大规模模型（如70B+）的泛化性。
2. UG未能完全防御自适应解释伪装攻击，检测性能存在“自适应差距”。
3. 依赖解释质量的假设：如果模型不提供解释或解释极简，GD可能失效。
4. 校准集大小固定为256，未探索不同规模校准集的影响。
5. 仅测试非自适应攻击，对自适应攻击的鲁棒性有限。

## 5. Behavioral Reprogramming of Open-Weights Models: Cognitive Plasticity and Alignment Bounds

- Source: arxiv
- arXiv ID: 2608.13069
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.13069v1
- PDF: https://arxiv.org/pdf/2608.13069v1
- DOI: https://doi.org/10.48550/arXiv.2608.13069

### Authors

Lucia Malíčková

### Abstract

Large language models (LLMs) are predominantly aligned to function as passive, sycophantic assistants. We challenge this default paradigm by empirically evaluating the cognitive plasticity of open-weight architectures when subjected to rigorous behavioral reprogramming. Our objective is to induce a proactive, Socratic conversational framework, characterized by high-frequency question generation under strictly constrained high-performance computing (HPC) conditions. Through a massively parallelized hyperparameter sweep comprising 405 HPC jobs, we define precise mathematical bounds for parameter-efficient fine-tuning (PEFT). We identify an architectural threshold at LoRA rank $r=16$ and demonstrate via extensive epoch ablation that generalization capacity strictly reaches its optimal convergence within an optimized training window of $e \in [2, 3]$ depending on dataset density (minimum validation loss of 0.919). Furthermore, scaling model capacity to 14B parameters yielded a lower localized evaluation perplexity (1.414). Subsequent Direct Preference Optimization (DPO) successfully decoupled the underlying assertive behavior from localized syntax, while rigorous cross-lingual stress testing reveals both the capabilities and the structural boundaries of zero-shot persona transfer, demonstrating robust alignment in closely related linguistic families alongside identifiable degradation pathways in morphologically distant targets. These findings establish a rigorous empirical framework for compute-efficient, cross-lingual behavioral modification.

### 中文一句话结论
本文通过大规模超参扫描（405个HPC任务）证明，开源大模型可通过参数高效微调（LoRA rank=16，训练轮次2–3）与直接偏好优化（DPO）在计算约束下实现从被动助手到主动苏格拉底式角色的行为重编程，且零样本跨语言人格迁移在形态相近语言中稳健，但在形态差异大的语言中性能下降。

### English TL;DR
This paper empirically demonstrates that open-weight LLMs can be behaviorally reprogrammed from passive sycophantic assistants into proactive Socratic agents using a compute-efficient pipeline. Optimal generalization requires LoRA rank r=16 and exactly 2–3 training epochs (min validation loss 0.919). Scaling to 14B parameters lowers perplexity to 1.414. DPO (β=0.15) decouples behavior from syntax, enabling zero-shot cross-lingual persona transfer that degrades only in morphologically distant languages.

### 中文详细总结
本文挑战了大模型默认的被动顺从助手范式，提出一种高计算效率的行为重编程框架。核心贡献包括：（1）通过405个并行HPC任务（使用Leonardo超算，约50,000 GPU小时）精确确定了LoRA参数高效微调的数学边界：最优秩r=16（α=32，dropout 0.1），最佳学习率2e-4，训练轮次e∈[2,3]时泛化最优（验证损失0.919）；（2）将模型规模扩展至14B参数（Qwen3-14B）时，推理困惑度降至1.414；（3）使用DPO（β=0.15，一轮）成功将主动提问行为与底层语法解耦，实现了零样本跨语言人格迁移——在斯拉夫语族、日耳曼语族等相近语言中保持稳健，在形态差异大的语言中出现退化。实验使用了1458个SFT对话对和440个DPO偏好对，评估矩阵包含18个心理情景×7种语言（共126次推理），主要评估指标为困惑度（PPL）和主动提问率（QR）。

### 方法 / 贡献
- **方法**：基于HuggingFace Transformers + PEFT + TRL原生框架，采用4-bit NF4量化加载权重，BF16计算精度，AdamW优化器（余弦退火学习率），梯度累积有效batch size=4。LoRA应用于所有注意力投影层，DPO用于偏好优化。
- **贡献**：①量化了开源架构的“认知可塑性”，计算了最优参数边界；②发现了泛化阈值（epoch 2-3限制），证明超出该轮次将导致过拟合；③实现了零样本跨语言人格迁移，并绘制了退化路径。

### 实验或数据
- **计算资源**：Leonardo超算（NVIDIA A100-SXM-64GB节点），约50,000 GPU小时。
- **架构**：Llama-3.1-8B-Instruct、Mistral-7B-Instruct、Qwen3-14B。
- **数据集**：SFT阶段使用1458个专有对话对，DPO阶段使用440个偏好对。评估集为18个心理对抗情景×7种语言（斯洛伐克语、英语、德语、法语、西班牙语、意大利语、葡萄牙语），共126次推理。
- **指标**：条件困惑度（PPL）和主动提问率（QR）。
- **关键结果**：LoRA rank=16时最优；epoch 2-3内验证损失最低（0.919）；14B模型困惑度最低（1.414）；DPO后QR显著提升；跨语言迁移在相近语系中保持稳健，在形态差异大的语言中退化。

### 值得关注点
- 严格使用原生框架（避免Unsloth等非确定性近似），确保实验可复现性。
- 超参扫描规模大（405个HPC任务），对计算-性能边界进行了数学级刻画。
- DPO能在低资源（440对）下解耦行为与句法，且实现零样本跨语言迁移。
- 主动提问率（QR）作为行为塑性的直接度量指标具有创新性。

### 局限性
论文未明确讨论局限性，但实验设计存在以下潜在限制：评估仅基于三种模型家族（7B–14B）和18个心理情景（7种语言），数据集规模较小（SFT 1458对、DPO 440对），可能限制泛化结论的广泛性。此外，跨语言退化仅基于形态距离定性分析，缺乏细粒度的语言学指标量化。计算资源虽大但仅采用单一超算环境，不同硬件下的可迁移性未验证。

## 6. Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining

- Source: arxiv
- arXiv ID: 2608.13515
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.13515v1
- PDF: https://arxiv.org/pdf/2608.13515v1
- DOI: https://doi.org/10.48550/arXiv.2608.13515

### Authors

Yuto Nishida, Hirokazu Kiyomaru, Yusuke Oda, Takashi Kodama, Chaoran Liu, Daisuke Kawahara, Yusuke Miyao, Max Müller-Eberstein, Masaru Isonuma

### Abstract

Measuring training data influence consistently across language model pretraining is challenging. It is difficult to select downstream tasks or validation sets representative of a model's general capabilities, and reliance on task performance at intermediate checkpoints complicates comparisons across training. We propose a measure of training data influence that does not require selecting a downstream task or validation set as the attribution target. Specifically, we define an example's influence by how much its gradient update reduces the squared distance to the final parameters of a given pretraining run, and estimate this quantity from intermediate checkpoints without retraining. Applying the method to 18 configurations from the Pythia and PolyPythia suites, we find systematic temporal changes in influential data. Early in training, literature-related data are more strongly aligned with the trajectory toward the final parameters, whereas STEM data become more strongly aligned in later stages. This qualitative crossover is broadly consistent across model configurations. Our results provide a tractable trajectory-level view of how influential data change throughout pretraining, complementing influence analyses defined with respect to specific downstream tasks or validation sets.

### 中文一句话结论
本文提出一种无需下游任务的数据影响度量方法，发现预训练早期文学类数据影响最大，后期STEM类数据影响最大。

### English TL;DR
We propose a task-agnostic measure of training data influence during language model pretraining, defined by how much each example’s gradient update reduces the squared distance to the final parameters, and show that literature data are most influential early in training while STEM data become most influential later.

### 中文详细总结
针对语言模型预训练中数据影响度量依赖下游任务和验证集的问题，本文提出一种任务无关的度量方法：通过梯度更新减少到最终参数欧氏距离的程度来定义样本影响，并利用中间检查点进行近似估计。将该方法应用于Pythia和PolyPythia的18种配置（含154个检查点），发现预训练早期文献类数据与最终参数轨迹更对齐，而后期STEM类数据对齐程度更高。该模式在不同模型大小和随机种子下保持一致。

### 方法 / 贡献
1. 提出任务无关的训练数据影响度量，基于梯度更新减少与最终参数平方距离的程度。
2. 推导出基于检查点的近似估计方法，无需重新训练。
3. 通过实验揭示预训练过程中影响数据的系统性时间变化：文学类早期影响大，STEM类后期影响大。

### 实验或数据
在Pythia（70M/160M/410M/1.4B/6.9B/12B）和PolyPythia（160M/410M）共18种配置上进行实验，每配置包含154个检查点，使用The Pile数据集。从实际训练数据流中采样样本，利用检查点近似计算每个样本的影响，并分析不同领域的分布变化。

### 值得关注点
发现文学类和STEM类数据在预训练不同阶段的“交叉”现象（crossover），该现象在多种模型规模、初始化方式和数据顺序下稳定存在，说明预训练数据的影响具有阶段性特征。

### 局限性
度量依赖于最终参数作为参考点，且基于检查点近似，长间隔下精度可能下降。每个样本影响的计算采用SGD假设分解，与真实自适应优化器行为存在偏差。实验仅覆盖Pythia模型家族，结论的泛化性需进一步验证。此外，该方法不直接与下游任务性能关联，任务无关性可能掩盖特定能力的来源。

## 7. Scaling Representation Diversity: Modulated Attention and Reconstructive Regularization for Visual Grounding

- Source: arxiv
- arXiv ID: 2608.12748
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.12748v1
- PDF: https://arxiv.org/pdf/2608.12748v1
- DOI: https://doi.org/10.48550/arXiv.2608.12748

### Authors

Junyi Hu, Tian Bai, Fengyi Wu, Yian Huang, Wei Wen, Zaoli Li, Junli Lin, Xingchen Li, Zhenming Peng, Yi Zhang

### Abstract

Referring Expression Comprehension (REC) is commonly studied under dataset-specific fine-tuning, resulting in specialist models with limited cross-dataset generalization. In this work, we revisit REC from the perspective of unified open-vocabulary grounding and identify representation degeneration as a key obstacle to scaling a single generalist model. To preserve representation diversity, we propose a holistic data-model co-design framework. Architecturally, we introduce the Modulated Attention-Contrastive Head (mACH) for efficient token-level vision-language alignment and a text-conditioned JEPA auxiliary stream that provides complementary gradient support to preserve alignment-active representations without inference overhead. On the data side, we introduce Objects365-Caption, enriching Objects365 with context-aware referring expressions for large-scale language supervision. We further provide a theoretical analysis showing that complementary gradient subspaces preserve alignment capacity and thereby scale representation diversity. Extensive experiments demonstrate that our single-checkpoint framework achieves highly competitive performance on standard REC benchmarks while exhibiting strong generalization across heterogeneous grounding datasets without benchmark-specific adaptation.

### 中文一句话结论
本文提出一种数据-模型协同设计框架（mACH+JEPA+Objects365-Caption），通过保持表征多样性解决视觉定位中的表征退化问题，实现单个模型在多种基准上的强泛化能力。

### English TL;DR
This paper proposes a data-model co-design framework—combining a Modulated Attention-Contrastive Head (mACH) and a text-conditioned JEPA auxiliary stream with a new enriched dataset Objects365-Caption—to preserve representation diversity and overcome representation degeneration, enabling a single generalist visual grounding model that achieves competitive performance and strong cross-dataset generalization without benchmark-specific fine-tuning.

### 中文详细总结
针对指代表达理解（REC）中跨数据集泛化差的问题，本文从统一开放词汇定位的角度出发，识别出表征退化是限制单一通用模型扩展的关键障碍。为此，作者提出数据-模型协同设计框架：模型方面，引入调制注意力对比头（mACH）实现高效的token级视觉-语言对齐，并设计文本条件的JEPA辅助流，通过互补梯度支持保留对齐活跃表征，且无推理开销；数据方面，构建Objects365-Caption数据集，将Objects365的离散标签扩充为上下文感知的指代表达，提供大规模语言监督。理论分析表明，互补梯度子空间保留对齐能力从而扩展表征多样性。实验证明，该单一检查点框架在标准REC基准上表现优异，并在异构数据集上展现出强泛化性，无需特定微调。

### 方法 / 贡献
1. **模型层面**：提出调制注意力对比头（mACH）实现广播式token级跨模态对齐，提升多查询推理效率；引入文本条件JEPA辅助分支，以重建损失提供与判别目标互补的梯度，防止表征退化，且训练后可移除，不增加推理成本。  
2. **数据层面**：构建Objects365-Caption数据集，将Objects365的类别标签转化为丰富的上下文描述，弥补大规模检测数据中语言监督的不足。  
3. **理论分析**：证明两个目标激活互补梯度子空间，保持对齐能力并扩展表征多样性。  
4. **统一框架**：单一模型无需基准特定微调，即可在多个REC基准上达到有竞争力性能并实现跨数据集泛化。

### 实验或数据
- 实验在标准REC基准（如RefCOCO/+/g等）上进行，并评估了跨异构数据集的泛化性。  
- 使用Objects365-Caption作为训练数据，该数据集通过多阶段流程生成上下文感知的指代表达，具有大规模和语言多样性。  
- 实验表明单检查点框架性能有竞争力，且无需基准特定适应即可泛化。具体数值需参考论文正文。

### 值得关注点
- **问题识别精准**：明确指出表征退化是统一视觉定位扩展的核心障碍。  
- **协同创新**：mACH与JEPA的联合训练既提升对齐效率，又通过重建正则化防止特征坍缩。  
- **无推理开销**：JEPA仅在训练时使用，不影响部署速度。  
- **数据增强**：Objects365-Caption填补大规模检测数据中语言监督的空白，且生成流程可复现。  
- **理论支撑**：提供梯度子空间互补性的理论分析，使设计有据可依。

### 局限性
- 从摘要和引言来看，该方法主要针对区域-词点对齐范式，可能不直接适用于其他范式（如回归或MLLM）。  
- Objects365-Caption依赖于Objects365的类别标签和自动生成流程，生成的指代表达质量可能受限于基础检测数据的标注。  
- 实验仅在几个公开REC基准上报告，未详细说明在更多样化场景（如开放词汇检测）上的表现。  
- 文中未明确讨论方法的计算/训练成本或对超参数（如JEPA权重α）的敏感性。

## 8. SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization

- Source: arxiv
- arXiv ID: 2608.13538
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.13538v1
- PDF: https://arxiv.org/pdf/2608.13538v1
- DOI: https://doi.org/10.48550/arXiv.2608.13538

### Authors

Weihan Meng, Hongzhu Guo, Yi Jing, Dewen Liu, Zijun Yao, Xiaozhi Wang, Lei Hou, Juanzi Li

### Abstract

Sparse autoencoders (SAEs) are proposed to extract numerous features from large language model (LLM) representations, yet explaining these features still relies primarily on external observation. This reliance leads to superficial explanations inferred from observed model behavior and computational inefficiency from collecting such behavioral evidence at scale. We introduce SAEVerbalizer, a framework that injects SAE decoder directions into an LLM's representations and fine-tunes the LLM's downstream layers to generate natural-language explanations of the injected features. Once trained, the resulting verbalizer explains SAE features directly from decoder directions, addressing both limitations. Our experiments show that the learned verbalization capability generalizes to unseen features, transfers across separately trained SAE dictionaries, and, with a lightweight adapter, extends to SAE features from different LLMs. Intervention experiments show that injecting multiple directions yields an explanation combining their meanings, while reversing individual directions produces corresponding meaning shifts.

### 中文一句话结论
SAEVerbalizer 通过将稀疏自编码器（SAE）的解码器方向注入大型语言模型（LLM）的表示中，并微调其下游层，实现了直接、可泛化且可迁移的 SAE 特征自然语言解释生成，无需依赖外部行为观察。

### English TL;DR
SAEVerbalizer is a framework that fine-tunes an LLM to generate natural-language explanations for sparse autoencoder features by injecting their decoder directions into the LLM's representations. This direct approach eliminates the need for external behavioral observation, generalizes to unseen features, and transfers across different SAE dictionaries and even different LLMs via a lightweight adapter.

### 中文详细总结
现有的 SAE 特征解释方法主要依赖于外部观察（如识别激活特征最强的文本片段并让 LLM 总结），这导致了两个主要问题：1) **解释表面化**：解释的是激活样本的共性，而非特征本身的内部表示；2) **计算效率低**：每个新 SAE 都需要重新进行大规模语料推理、激活计算和示例检索。

为解决这些问题，本文提出了 **SAEVerbalizer** 框架。其核心思想是：将 SAE 特征的唯一标识——其解码器方向（decoder direction）——注入到 LLM 的中间层表示中，然后微调该 LLM 的注入层之后的下游层，使其学会根据注入的“特征信号”生成对应的自然语言解释。一旦训练完成，该“语言化器”（verbalizer）可以直接为任何新的、未见过的 SAE 特征生成解释，无需额外的数据收集或微调。

实验表明，这种语言化能力具有良好的可泛化性（能解释未见过的特征）和可迁移性（能在不同 SAE 字典间迁移）。通过一个轻量级的表示空间适配器（adapter），SAEVerbalizer 甚至可以为来自不同底层 LLM 的 SAE 特征提供解释。干预实验进一步表明，同时注入多个特征的方向会生成融合其含义的解释，而反转单个方向则会导致解释含义的相应变化。

### 方法 / 贡献
- **方法**：SAEVerbalizer 包含两个主要组件：
    1.  **语言化器（Verbalizer）**：一个被微调的 LLM。在生成解释时，将目标 SAE 特征的解码器方向（经过归一化处理）**注入**到 LLM 特定层（\(L_{inj}\)）的特定 token 位置，以此作为输入信号。微调时仅更新 \(L_{inj}\) 之后的层，冻结前面的层和嵌入层以保持方向向量的语义空间。
    2.  **适配器（Adapter）**：一个轻量级的单层仿射变换网络。当目标 SAE 来自不同的源 LLM 时，适配器将该源 LLM 的表示空间映射到语言化器所在的目标 LLM 的注入层空间，使得语言化器无需为每个新 LLM 重新训练。
- **贡献**：
    1.  提出了 SAEVerbalizer，一种直接从解码器方向解释未见过的 SAE 特征的轻量级方法。
    2.  提供了一种通过特征-解释配对数据来训练该语言化能力的实用方法。
    3.  通过实验展示了其在不同的 SAE 字典和 LLM 之间的可扩展性和泛化能力。

### 实验或数据
- **实验设置**：在多个不同规模的 LLM（如 GPT-2 Small、Pythia）和不同层级的 SAE 特征上进行实验。
- **训练数据**：使用来自 Neuronpedia 平台的特征-解释配对数据作为监督信号。由于这些说明基于外部观察，作者使用 LLM 作为评判器过滤出高质量的训练数据，评分考量包括：模式连贯性、解释特异性和示例支持度。
- **实验发现**：
    - **泛化性**：训练好的语言化器能够准确解释训练中未见过的新 SAE 特征。
    - **可迁移性**：该能力可以无缝迁移到另一个完全独立训练的 SAE 字典上。
    - **跨 LLM**：通过轻量级适配器，可以在不重新训练语言化器的情况下，解释另一个不同 LLM 的 SAE 特征。
    - **干预实验**：注入多个方向会得到组合解释；反转某方向会导致解释语义反转，证明模型确实学习了方向与语义的对应关系。

### 值得关注点
1.  **范式转变**：将 SAE 解释从“观察行为（behavior observation）”范式转变为“处理内部表示（processing internal representations）”范式，这是本质上的创新。
2.  **高效性与可扩展性**：一旦训练完成，解释新特征的计算成本极低，仅需一次前向传播，无需大规模语料检索，解决了现有方法的主要瓶颈。
3.  **强泛化与可迁移性**：模型展现出的零样本泛化能力和跨字典、跨模型的迁移能力非常突出，证明了其学习到的是一种通用的“表示解读”能力，而非简单的记忆。
4.  **清晰的因果性**：通过干预注入方向（如反转）直接改变解释语义，为该方法提供了有力的因果证据，表明解释确实源自注入的内部表示。

### 局限性
1.  **依赖高质量标注数据**：训练过程依赖于 Neuronpedia 等外部来源提供的特征-解释配对数据，这些数据的质量直接影响最终模型的性能。虽然使用了过滤，但高质量训练数据的获取本身是一个挑战。
2.  **解释深度可能有限**：生成的解释描述的是特征所代表的“概念”，但可能无法捕捉到该特征在复杂推理任务中的具体计算或功能性作用，即解释了“是什么”但可能未深入阐明“如何用”。
3.  **适配器能力边界**：跨 LLM 的适配器仅在特定层对之间进行线性映射，可能无法完美处理两个高度不同或架构差异巨大的 LLM 之间的表示空间对齐问题，其泛化边界尚需探索。

## 9. LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure

- Source: arxiv
- arXiv ID: 2608.13545
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.13545v1
- PDF: https://arxiv.org/pdf/2608.13545v1
- DOI: https://doi.org/10.48550/arXiv.2608.13545

### Authors

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel

### Abstract

Modern language models are trained on heterogeneous web-scale text corpora. Consequently, studying knowledge and skill acquisition is difficult, as prior exposure to related content is hard to characterize. To address this challenge, we introduce LITTLECURRICULUM, a curated 88B-token pretraining corpus tailored to U.S. elementary school material, explicitly excluding concepts, facts, and vocabulary taught above Grade 5. Training a 5B-parameter LLM from scratch on LITTLECURRICULUM yields LITTLELEARNER, a model with sufficient language competence for open-ended evaluation, yet with clear knowledge and capability boundaries mapped to interpretable curriculum guidelines. We release LITTLECURRICULUM and LITTLELEARNER as a developmentally restricted sandbox to study how models acquire, represent, and use data under a well-defined training scope. We illustrate the sandbox's utility in a first suite of experiments on injecting new knowledge through post-training and in-context learning. These methods let LITTLELEARNER better utilize existing knowledge, but do not raise out-of-scope capabilities. Our findings underscore the value of this controlled environment for future investigations.

### 中文一句话结论
本文通过构建仅包含美国小学（K-5）内容的880亿词预训练语料库LITTLECURRICULUM，并训练出5B参数的LITTLELEARNER模型，创建了一个发展受限的沙盒环境，用于研究语言模型在明确知识边界下的知识获取与扩展。

### English TL;DR
The paper introduces LITTLELEARNER, a 5B-parameter language model trained exclusively on LITTLECURRICULUM, an 88B-token dataset filtered to U.S. elementary school content (K-5), creating a developmentally restricted sandbox that enables controlled study of how models acquire, represent, and extend knowledge under well-defined conceptual boundaries, without gaining out-of-scope capabilities through post-training or in-context learning.

### 中文详细总结
现代语言模型通常在异构的大规模网络文本上训练，这使得研究知识和技能的获取非常困难，因为无法准确判断模型是否曾接触过相关概念。为解决这一问题，作者构建了LITTLECURRICULUM——一个经过多阶段过滤的880亿词预训练语料库，仅包含美国幼儿园至五年级（K-5）的教学内容，明确排除了五年级以上的概念、事实和词汇。基于该语料库从零训练了一个50亿参数的模型LITTLELEARNER。该模型具备了进行开放式评估所需的语言能力，但其知识和能力边界清晰，并与可解释的课程指南相对应。作者发布LITTLECURRICULUM和LITTLELEARNER作为一个发展受限的沙盒，用于研究模型在明确定义训练范围内如何获取、表示和使用数据。初步实验表明，通过后训练和上下文学习注入新知识，可以提高LITTLELEARNER对已有知识的利用，但不会提升超出训练范围的能力。

### 方法 / 贡献
1. **LITTLECURRICULUM语料库**：通过多阶段过滤从FineWeb-Edu中构建，包括基于词汇习得年龄的预过滤、基于课程标准的LLM标注与分类器训练（FastText和ModernBERT）、符号过滤（排除高等数学公式）、以及频率采样，确保语料只包含K-5内容。
2. **LITTLELEARNER模型**：在LITTLECURRICULUM上从零训练的5B参数语言模型，其知识边界与小学课程标准对齐。
3. **沙盒环境**：提供了可控的研究平台，用于分离预训练知识暴露与后训练/上下文学习带来的能力增长。
4. **初步实验**：展示了后训练和上下文学习在沙盒内的效果——这些方法能提升已有知识的利用，但不会产生超出训练范围的新能力。

### 实验或数据
- **数据集**：LITTLECURRICULUM（880亿词，源自FineWeb-Edu的K-5子集）。验证使用了内部基准CommonCoreText（基于CCSS的阅读材料）和外部基准WeeBit（有年级标签的语料）。过滤管道将超出K-5的内容保留率降至接近0%，同时保留了35-42%的K-5文档。
- **模型**：5B参数的LITTLELEARNER，从零训练。
- **实验**：进行了一组初步实验，通过后训练（如微调）和上下文学习向LITTLELEARNER注入新知识，观察能力边界变化。结果发现这些方法能促进已有知识的利用，但不会显著提升超出K-5范围的能力。

### 值得关注点
- 首次将发展性课程边界（美国K-5课程标准）作为预训练数据限制，而非常见的临时边界或数据量限制。
- 提供了替代“仅通过测试集隔离”的方法，从训练源头控制知识暴露，更直接地研究能力涌现与已有知识激发之间的区别。
- 实验表明，即使通过后训练和上下文学习，模型也难以获得超出预训练范围的知识，说明预训练边界对能力上限的决定性作用。

### 局限性
- 过滤过程相对保守，导致约65%的K-5数据被丢弃，可能损失了一些有效的K-5教学素材。
- 知识边界基于美国小学课程，可能不完全适用于其他教育体系或领域。
- 模型规模（5B）和语料规模（88B token）有限，更大规模下的发现可能有所不同。
- 后训练和上下文学习的实验仅初步探索，尚未系统研究多种数据增广或更复杂的注入策略。
- 语料构建依赖于LLM标注和分类器，存在标注偏差的可能性。

## 10. The Embedder's Dilemma: LLMs Are Better, but at What Cost?

- Source: arxiv
- arXiv ID: 2608.12875
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.12875v1
- PDF: https://arxiv.org/pdf/2608.12875v1
- DOI: https://doi.org/10.48550/arXiv.2608.12875

### Authors

Adnan El Assadi, Niklas Muennighoff, Jinhyuk Lee

### Abstract

Should you replace your text-embedding pipeline with a large language model? We answer this with a controlled, cost-aware comparison of ten LLMs across six families and 26 embedding models (118M to 14B parameters) on 37 tasks spanning classification, semantic textual similarity (STS), clustering, pair classification, and retrieval. In aggregate the two paradigms are effectively tied: the best LLM (Gemini 3.1 Pro, 77.6) and the best embedding model (77.2) differ by 0.4 points. Their strengths differ by task: LLMs lead on reasoning-heavy retrieval, embedding models lead on classification, and the two match on clustering, STS, and pair classification. Reaching that parity is expensive. An LLM costs up to 1,431x more than an embedding model of comparable quality (USD 154 vs. USD 0.11 per benchmark pass), and the open LLMs tested process tokens 2.5 to 736x more slowly on the same GPU. Reasoning tokens account for 28 to 81% of LLM inference cost; lower reasoning budgets preserve or improve retrieval quality for most models in our ablation. The Pareto frontier contains the leading embedding models and one LLM, Gemini 3.1 Pro. These results support a division of labour: use embedding models for similarity, classification, and clustering, and reserve LLMs for reasoning-intensive retrieval. Our code, datasets, and results are publicly available at https://github.com/embeddings-benchmark/embedders-dilemma.

### 中文一句话结论
在文本嵌入任务上，大型语言模型（LLMs）与专用嵌入模型的整体性能几乎持平，但LLMs的成本最高可达后者的1,431倍，速度慢2.5至736倍，因此建议将嵌入模型用于相似度、分类和聚类任务，而LLMs仅用于推理密集型检索。

### English TL;DR
LLMs and embedding models achieve comparable aggregate performance on text embedding tasks, but LLMs cost up to 1,431x more and are significantly slower, supporting a division of labor where embedding models handle similarity, classification, and clustering while LLMs are reserved for reasoning-intensive retrieval.

### 中文详细总结
该论文通过系统性对比10个LLM（跨越6个系列）与26个嵌入模型（参数范围118M至14B），在37个任务（涵盖分类、语义文本相似度STS、聚类、配对分类和检索）上的表现，回答了“是否应该用LLM替换嵌入流程”的问题。主要发现包括：
1. **整体性能持平**：最佳LLM（Gemini 3.1 Pro，77.6分）与最佳嵌入模型（77.2分）仅相差0.4分，处于统计噪声范围内。
2. **任务特异性优势**：LLM在推理密集型检索上领先，嵌入模型在分类上领先，两者在聚类、STS和配对分类上表现相当。
3. **成本差异巨大**：达到同等质量时，LLM成本最高可达嵌入模型的1,431倍（154美元 vs. 0.11美元每基准测试）；在相同H100 GPU上，开源LLM处理速度慢2.5至736倍。
4. **推理令牌税**：推理令牌占LLM推理成本的28%至81%；降低推理预算对大多数模型而言可保持或提升检索质量。
5. **帕累托前沿**：前沿包含领先的嵌入模型和唯一一个LLM——Gemini 3.1 Pro。
论文建议采用分工策略：嵌入模型处理相似度、分类和聚类；LLM仅用于推理密集型检索。

### 方法 / 贡献
- 提出**MTEB(LLM)**：首个同时评估LLM和嵌入模型在所有五个MTEB任务类别（分类、STS、聚类、配对分类、检索）上性能与成本的基准，共37个任务。
- 对10个LLM（6个系列）和26个嵌入模型（118M至14B参数）进行受控的成本感知对比。
- 引入**推理令牌税**概念：量化推理（链式思维）令牌在LLM总成本中的占比（28-81%），并实验证明降低推理预算可保持或提升检索质量。
- 构建成本-性能帕累托前沿，揭示LLM在成本上的巨大劣势。
- 发布代码、数据集和结果（https://github.com/embeddings-benchmark/embedders-dilemma）。

### 实验或数据
- 评估37个任务：分类（8个，如IMDB、Banking77）、STS（10个，如STSBenchmark、BIOSSES）、聚类（9个，如ArXiv、Reddit）、配对分类（4个，如SprintDuplicateQuestions）、检索（6个，如AILAStatutes、HC3-Finance）。
- LLM使用零样本提示（分类用结构化输出，STS返回浮点数，聚类给出JSON数组，配对分类输出二元结果，检索采用语料库-上下文方式）。
- 嵌入模型使用标准流程：kNN用于分类，余弦相似度用于STS和检索，k-means用于聚类。
- 成本计算：LLM追踪API令牌（特别是推理令牌），嵌入模型在H100 GPU上进行吞吐量基准测试。
- 速度比较：在相同H100 GPU上对比开源LLM和嵌入模型的令牌处理速度。

### 值得关注点
1. **性能与成本的巨大反差**：LLM在整体性能上仅与嵌入模型持平，但成本高出三个数量级，这挑战了“越大越好”的直觉。
2. **推理令牌税**：论文首次量化了推理过程（链式思维）在LLM成本中的主导地位（28-81%），并发现减少推理不仅省钱，对大多数模型还能提升检索质量。
3. **任务分工建议实用性强**：为从业者提供了清晰的指导——嵌入模型作为默认选择处理大多数任务，LLM仅针对需要跨文档推理的检索任务。
4. **帕累托前沿仅包含一个LLM**：Gemini 3.1 Pro是唯一进入前沿的LLM，且其性能优势（0.4分）代价极高，表明成本效益至关重要。
5. **开放源码完整基准**：MTEB(LLM)作为标准框架的一部分，便于后续扩展和复现。

### 局限性
- **检索语料库规模受限**：为适配短上下文模型，论文限制了检索任务中语料库的大小（82-415篇文档），这可能导致结果不能完全反映大规模检索场景下的差异。
- **LLM评估仅基于零样本**：未系统测试少量样本注入对分类等任务的影响（仅对较少模型进行了消融实验），而嵌入模型使用了完整的标注训练集。
- **嵌入模型评估方式固定**：采用了kNN、余弦相似度等标准流程，未探索更复杂的优化方法（如交叉编码器重排序）可能缩小或扩大差距。
- **未覆盖所有任务类别**：原始MTEB包含8个任务类别，本论文仅覆盖其中5个，遗漏了如重新排名、代码检索等任务。
- **硬件依赖性**：速度比较仅基于H100 GPU，其他硬件配置下的相对性能可能不同。
- **LLM版本更新快**：评估的LLM限于特定版本，后续模型可能改变性能-成本平衡。

## Processing Notes

- Duplicate papers skipped: 0