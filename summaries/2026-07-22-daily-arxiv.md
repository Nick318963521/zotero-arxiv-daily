# Daily arXiv - 2026-07-22

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-22T23:33:46
- Paper count: 10

## 1. Translation as Augmentation: Effect of Translated Data on Assessment of Difficulty

- Source: arxiv
- arXiv ID: 2607.19101
- Relevance: 4.8

### Links

- Abstract: http://arxiv.org/abs/2607.19101v1
- PDF: https://arxiv.org/pdf/2607.19101v1
- DOI: https://doi.org/10.48550/arXiv.2607.19101

### Authors

Yiheng Wu, Jue Hou, Roman Yangarber

### Abstract

Reliable Text Difficulty Assessment is a prerequisite for valid text simplification workflows and personalized learning applications. However, the development of robust assessment models is severely hindered by a critical bottleneck: the scarcity of expert-annotated corpora containing fine-grained difficulty levels (e.g., CEFR), particularly for lower-resource languages. This paper addresses this data scarcity problem in the context of a low-resource European language. We propose a cross-lingual data augmentation strategy that leverages machine translation to transfer labeled resources from high-resource languages to the target low-resource language. We train BERT-based regression models to predict difficulty scores and investigate whether synthetic, translated data can effectively supplement native training sets. Our experiments demonstrate that augmenting scarce native data with machine-translated corpora significantly improves the accuracy of difficulty estimation, offering a viable solution for languages lacking extensive expert annotations.

### 中文一句话结论
通过机器翻译将高资源语言的专家标注语料迁移到低资源语言，可以显著提升文本难度评估的准确性，有效缓解低资源语言标注数据稀缺的问题。

### English TL;DR
Machine translation of expert-annotated corpora from high-resource languages significantly improves the accuracy of text difficulty assessment in low-resource languages by augmenting scarce native training data.

### 中文详细总结
本文针对低资源语言（如芬兰语）文本难度评估中专家标注数据稀缺的问题，提出了一种跨语言数据增强策略。该策略利用机器翻译将高资源语言（如俄语）中已标注难度等级（例如CEFR等级）的语料转换为目标低资源语言的数据，以扩充有限的本地标注数据集。研究训练了基于BERT的回归模型来预测文本的难度分数，并评估了合成翻译数据对模型效果的提升。实验结果表明，将机器翻译语料与稀缺的本地数据结合使用，能显著提高难度估计的准确性，为解决低资源语言缺乏专家标注的问题提供了可行方案。

### 方法 / 贡献
- 提出一种跨语言数据增强方法：利用机器翻译将高资源语言（俄语）的CEFR标注语料转化为低资源语言（芬兰语）的训练数据。
- 基于BERT模型进行难度分数的回归预测。
- 实验验证了合成翻译数据能有效补充本地稀缺的标注数据，显著提升模型性能。

### 实验或数据
- 使用本地芬兰语语料（3460份文档，来源包括教科书、新闻、简易语言文本等）和从俄语机器翻译的语料（7457份文档，来源包括RuFoLa、Zlatoust等）。
- 训练基于BERT的回归模型，评估中文档的CEFR等级预测准确性。
- 实验对比仅使用本地数据与结合翻译数据后的模型性能。

### 值得关注点
- 针对低资源欧洲语言（芬兰语）的实际数据稀缺问题。
- 机器翻译作为数据增强手段的有效性验证，而非依赖传统人工标注。
- 翻译语料覆盖多个CEFR等级（A1到C2），增强了评估的细粒度。

### 局限性
- 实验仅针对芬兰语和俄语这一对语言，跨语言泛化性需进一步验证。
- 机器翻译可能引入噪声或偏差，未详细分析翻译质量对模型的具体影响。
- 未与其他数据增强方法（如回译、生成式模型）进行对比。

## 2. Fence: Specialized SLM Guardrails for LLM Applications

- Source: arxiv
- arXiv ID: 2607.18268
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.18268v1
- PDF: https://arxiv.org/pdf/2607.18268v1
- DOI: https://doi.org/10.48550/arXiv.2607.18268

### Authors

Kumud Lakara, Ruibo Shi, Fran Silavong

### Abstract

Real-world applications that use closed-source large language models (LLMs) need advanced safety measures that go beyond the basic content filters. Content moderation filters such as toxicity and bias have relatively standard definitions where as application specific guardrails like hallucination, topic drift and behaviour deviation are more difficult to model and can vary by use case. Additionally, data scarcity and annotation costs, make the process of creating and testing specialized guardrails challenging. In this work, we propose using Small Language Models (SLMs) trained on synthetic data as specialized guardrails for LLM applications. We introduce a novel synthetic data generation method inspired by the design of Generative Adversarial Networks (GANs) to generate high quality synthetic data samples which can be used to train SLMs to encode use case specific guardrail information and hence function as specialized guardrails. Our experiments demonstrate that SLM guardrails trained on high quality synthetic data show performance gains over prompt based LLM guardrails.

### 中文一句话结论
本文提出一种基于生成对抗网络（GAN）启发的合成数据生成方法，利用小语言模型（SLM）作为LLM应用的高效专用护栏，在主题偏移、行为偏差等用例上优于基于提示的大语言模型护栏。

### English TL;DR
The paper proposes using Small Language Models (SLMs) trained on high-quality synthetic data generated via a GAN-inspired method as specialized guardrails for LLM applications, demonstrating performance gains over prompt-based LLM guardrails.

### 中文详细总结
现实LLM应用需要超越基础内容过滤的专用安全护栏（如幻觉、主题偏移、行为偏差），但此类护栏因数据稀缺和标注成本高而难以构建。本文提出使用小语言模型（SLM）作为专用护栏，并设计了一种受GAN启发的新型合成数据生成流程：包含生成器（LLM）、鉴别器（LLM）和优化器，通过迭代对抗生成使合成数据逼近真实用例分布，从而训练SLM编码特定护栏规则。实验在金融领域两个内部用例（搜索引擎的提示注入防护、FAQ聊天机器人的主题偏移防护）上验证，表明基于合成数据训练的SLM护栏（如Gemma-3-1B）在宏F1和准确率上均优于基于提示的LLM护栏（如GPT-5.2）。

### 方法 / 贡献
1. 提出GAN启发的合成数据生成框架：生成器（LLM）基于种子数据和护栏定义生成样本，鉴别器（LLM）区分真实与合成数据并输出推理痕迹，优化器据此调整生成器提示，迭代提升数据质量。
2. 将合同数据训练的小语言模型用作专用护栏，可针对各类用例（如主题偏移、行为偏差、提示注入）快速定制，解决现有护栏策略僵化问题。
3. 实验证明SLM护栏在特定用例上优于传统基于提示的LLM护栏，且合成数据方法有效缓解了真实数据稀缺问题。

### 实验或数据
实验基于两个金融领域内部用例：
- 用例1：LLM驱动的搜索引擎，测试**提示注入**护栏。
- 用例2：FAQ聊天机器人，测试**主题偏移（输入）**护栏。
使用的模型包括Gemma-3-1B（Fence）、Nomic-v1.5、GPT-5.2和Gemma-3-1B（基线）。评估指标为宏F1和准确率。结果显示，Fence的Gemma-3-1B在主题偏移护栏上宏F1达0.66、准确率0.76，优于GPT-5.2（0.45/0.72）和Nomic-v1.5（0.54/0.73）。数据全部为合成生成，未使用人工标注数据。

### 值得关注点
1. 合成数据生成方法借鉴GAN的对抗思想，但改用LLM作为生成器和鉴别器，通过自然语言推理痕迹模拟梯度优化，创新性强。
2. 聚焦于“用例特定”而非通用安全，填补了现有护栏（如Llama-Guard）仅覆盖预定义类别的空白。
3. 实验表明，仅用合成数据训练的SLM（1B参数）即可超越大型LLM的提示基护栏，展示了高效性和成本优势。

### 局限性
1. 鉴别器提示优化不稳定，容易偏离任务（从区分真实/合成转向分类安全/有害），需固定鉴别器才能稳定训练。
2. 实验仅涵盖金融领域两个用例，泛化性尚未验证，对其他领域（如医疗、法律）的适用性未知。
3. 合成数据质量依赖种子数据和护栏定义的人工设计，若定义不准确可能影响护栏效果。
4. 未与真实数据训练的SLM或更大规模模型进行对比，仅比较了提示基LLM。

## 3. Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs

- Source: arxiv
- arXiv ID: 2607.19243
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.19243v1
- PDF: https://arxiv.org/pdf/2607.19243v1
- DOI: https://doi.org/10.48550/arXiv.2607.19243

### Authors

Alexander Manev

### Abstract

Although Large Language Models (LLMs) demonstrate remarkable multilingual fluency, their internal knowledge representations remain disproportionately biased toward high-resource languages. This leads to cross-lingual factual inconsistency, where they shift their empirical answer distributions based solely on the prompt language. We investigate whether these biases can be mitigated at inference time, forcing an English-prompted model to answer as if it were queried in target languages (German, Spanish, Bulgarian), and evaluate four intervention strategies: zero-shot contextual steering (persona prompting), internal representation manipulation via Contrastive Activation Addition (CAA), and lightweight weight modification via Direct Preference Optimization (DPO) trained on benchmark-derived factual data as well as conceptual generalization data. To assess alignment, we curate a multilingual factual dataset alongside a novel generalization benchmark comprising culturally rooted queries to determine whether factual interventions transfer to broader target-centric preferences. Experiments on Gemma 3 12B Instruct reveal persona prompting to be the strongest overall intervention, balancing efficacy, safety, and out-of-domain generalization. While CAA yields sharp inconsistency benchmark shifts, it is configuration-sensitive and risks knowledge degradation. DPO-based adapters offer permanent, yet narrower and less transferable gains. These findings suggest that cross-lingual inconsistency is at least partly a selection problem, and that simple contextual interventions may outperform more invasive methods for robust, transferable alignment.

### 中文一句话结论
基于推理时干预的研究表明，简单的人格提示方法比对比激活添加和直接偏好优化更有效地缓解了大型语言模型的跨语言事实不一致性，说明该问题部分源于模型输出选择而非知识缺失。

### English TL;DR
This paper investigates inference-time strategies to mitigate cross-lingual factual inconsistency in LLMs, finding that zero-shot persona prompting outperforms Contrastive Activation Addition and Direct Preference Optimization on Gemma 3 12B Instruct. The results show that simple contextual interventions can effectively align English-prompted model outputs with target language preferences, suggesting that cross-lingual inconsistency is at least partly a selection problem.

### 中文详细总结
大型语言模型尽管具有多语言流畅性，但其内部知识表征显著偏向高资源语言（如英语），导致跨语言事实不一致：同一事实在不同语言提示下，模型给出不同的回答分布。本文在Gemma 3 12B Instruct上比较了四种推理时干预策略：
1. **零样本人格提示**：通过自然语言指令让模型采用目标语言对应的视角。
2. **对比激活添加（CAA）**：在模型隐藏层中添加方向性偏差向量，推动激活朝向目标语言偏好。
3. **直接偏好优化（DPO）**：基于基准事实数据或泛化概念数据训练轻量LoRA适配器，使模型内化目标语言偏好。

实验覆盖德语、西班牙语和保加利亚语，使用Jensen-Shannon距离（JSD）和配对统计检验评估分布对齐效果。结果表明，**人格提示整体最强**：在8/9个测试组合中改善了对齐，且无需修改权重或激活。CAA虽能产生显著分布偏移（如保加利亚语p<0.01，CLES=0.741），但高度依赖层和乘数配置，存在知识退化风险。DPO适配器提供永久性但范围较窄、可迁移性较差的改进，且泛化数据训练的适配器效果更弱。论文认为跨语言不一致性至少部分是模型对英语偏好输出的“选择问题”，简单的上下文干预可能优于更侵入性的方法。

### 方法 / 贡献
- **多语言事实数据集**：涵盖英语、德语、西班牙语、保加利亚语、瑞典语和韩语的原子化三元组，用于暴露跨语言分布偏移。
- **分布评估框架**：基于重复采样的提取式分析，量化跨语言事实不一致性。
- **新泛化基准**：每个目标语言50个文化植根查询，测试干预是否转移至更广的目标文化偏好。
- **比较性干预研究**：系统评估了人格提示、CAA和DPO（基于基准数据和泛化数据）在推理时对齐的效果，发现简单提示是整体最优方案。

### 实验或数据
- **模型**：Gemma 3 12B Instruct（基于预实验选择）。
- **目标语言**：德语、西班牙语、保加利亚语。
- **评估方法**：每种条件重复采样（每个subject-relation对10次，温度0.8和1.2），使用JSD、TPM、配对Wilcoxon符号秩检验、CLES度量。
- **数据集**：自建多语言事实基准（7种关系，6种语言）+ 新编制的50题文化泛化基准（英语提问）。
- **主要结果**：人格提示在8/9个评估单元改善对齐；CAA在最佳配置下对保加利亚语和德语产生显著偏移（p<0.01），但配置敏感；DPO基准数据适配器效果有限且可迁移性弱；泛化数据适配器未改善基准对齐。

### 值得关注点
- 跨语言事实不一致性部分源于模型对英语优先输出的选择，而非内部知识缺失，简单的语境提示即可有效纠正。
- CAA方法提供了机制层面的见解，但其脆弱性（依赖精细超参）和知识退化风险限制了实用价值。
- DPO适配器虽能永久改变偏好，但收益窄且难以迁移至基准外场景，说明参数级修改在此任务中并非更优。
- 结果显示“轻量干预优于深度修改”，对实际部署中的对齐策略选择有参考意义。

### 局限性
- 实验仅在单一模型（Gemma 3 12B Instruct）上进行，结论对其他架构的泛化性未知。
- 干预效果依赖于目标语言和关系类型，论文未系统评估所有语言（如瑞典语、韩语）或所有关系下的表现。
- CAA和DPO的配置（层选择、乘数、训练数据构造）可能未达到最优，论文未提供跨设置鲁棒性分析。
- 泛化基准规模较小（50题/语言），且仅包含文化植根选择题，可能不足以代表真实场景的多样性。
- 未评估干预对模型安全性、事实退化或语言无关任务的负面影响。

## 4. Rationale-Guided Knowledge Distillation for Cross-Lingual Stance Detection

- Source: arxiv
- arXiv ID: 2607.18693
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.18693v1
- PDF: https://arxiv.org/pdf/2607.18693v1
- DOI: https://doi.org/10.48550/arXiv.2607.18693

### Authors

Qiuli Zhou, Jingyuan Yao, Shengeng Tang, Hongzhi Chen, Jun Tang, Richang Hong

### Abstract

Stance detection aims to identify whether a text expresses a favorable or opposing attitude toward a given target, and serves as an important task for various downstream applications. Although existing studies have achieved strong performance in monolingual settings, especially in English, many low-resource languages such as Catalan still lack sufficient annotated data for training effective models. Cross-lingual stance detection alleviates this problem by transferring stance knowledge from resource-rich languages to low-resource languages. However, most existing methods mainly rely on semantic alignment between texts and targets, while ignoring the reasoning process required for reliable stance inference. Although Large Language Models provide strong reasoning ability, their high computational cost and inference latency limit practical deployment. To address these limitations, we propose a rationale-guided knowledge distillation framework for cross-lingual stance detection. Specifically, we use Chain-of-Thought prompting to guide Large Language Models in generating informative rationales, and distill the resulting reasoning knowledge into a compact student model. We further design a dual-path distillation mechanism to align rationale-enhanced and rationale-free representations, together with their prediction distributions. In addition, two contrastive learning strategies are introduced to improve stance discrimination. Experiments on multilingual benchmarks demonstrate that our method consistently outperforms competitive baselines.

### 中文一句话结论
本文提出了一种基于推理引导的知识蒸馏框架，通过链式思维提示让大语言模型生成推理理由，并将推理知识蒸馏到紧凑的学生模型（mBERT）中，在多语言跨语言立场检测任务上持续优于现有基线方法。

### English TL;DR
This paper proposes a rationale-guided knowledge distillation framework for cross-lingual stance detection, using Chain-of-Thought prompting to generate reasoning rationales from Large Language Models and distilling this reasoning knowledge into a compact mBERT student model via a dual-path distillation mechanism with contrastive learning, consistently outperforming baselines on multilingual benchmarks.

### 中文详细总结
立场检测旨在判断文本对给定目标的支持或反对态度。现有方法在单语言（尤其是英语）上表现良好，但低资源语言（如加泰罗尼亚语）缺乏标注数据。跨语言立场检测通过从资源丰富语言迁移知识来缓解这一问题，但现有方法大多依赖语义对齐，忽略了推理过程。虽然大语言模型具备强大推理能力，但计算成本高、推理延迟大，难以实际部署。为此，本文提出推理引导的知识蒸馏框架：首先使用链式思维提示结合上下文学习，让大语言模型生成包含推理步骤的“理由”（rationale）；然后设计双路径蒸馏机制，将理由增强路径和标准路径的表示与预测分布对齐，使学生模型在训练时学习推理知识，推理时无需理由输入；同时引入两种对比学习策略（源语言阶段基于原型对比，目标语言阶段基于双约束对比），增强立场区分能力。在多语言基准数据集上的实验表明，该方法一致优于多个强基线。

### 方法 / 贡献
1. **推理引导的跨语言框架**：利用大语言模型通过链式思维提示生成显式推理理由，为低资源跨语言立场检测提供推理监督。
2. **双分支层级蒸馏机制**：设计理由增强路径和标准路径，通过表示级和响应级对齐，弥合解码器型大语言模型与编码器型mBERT之间的架构差异，实现训练时学习推理、推理时无需理由的高效部署。
3. **对比学习增强立场迁移**：在源语言阶段使用基于支持样本的原型对比损失，在目标语言阶段使用双约束对比对齐损失，分别提升立场区分能力。

### 实验或数据
实验在多语言基准数据集上进行，涵盖多种主题。论文提到了“多语言基准”和“一系列基线”，但未在摘要中列出具体数据集名称或大小。实验结果表明该方法一致优于竞争基线。具体数据集和实验设置需参考论文全文。

### 值得关注点
- 首次将链式思维推理显式地作为知识蒸馏的监督信号，用于跨语言立场检测。
- 双路径蒸馏设计巧妙解决了教师模型（大语言模型）与学生模型（mBERT）架构不匹配的问题。
- 对比学习策略针对不同训练阶段（源语言有标注、目标语言少标注）分别设计，贴合实际场景。
- 学生模型在推理时无需理由输入，保持了低延迟和轻量化的优点。

### 局限性
论文未明确讨论局限性，但从方法设计看，可能存在以下不足：依赖大语言模型生成理由的质量，若理由不准确或存在偏见会影响蒸馏效果；双路径蒸馏机制增加了训练复杂度；跨语言场景下，理由生成可能受语言差异影响，对齐效果有待进一步验证。

## 5. The Information Shadow: Measuring Structural Limits on What Language Models Can Learn

- Source: arxiv
- arXiv ID: 2607.18305
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.18305v1
- PDF: https://arxiv.org/pdf/2607.18305v1
- DOI: https://doi.org/10.48550/arXiv.2607.18305

### Authors

Priyansh Srivastava, Romit Chatterjee

### Abstract

Some limits on what language models know are not gaps in data coverage but structural properties of learning from text. We introduce the information shadow: the region of phenomena that a text-trained learner cannot acquire regardless of scale, comprising (I) structures language cannot express, (II) functions that are statistically non-identifiable from the training distribution, and (III) functions that are representable but unreachable by gradient-based training. We give each type a probe that is decisive because the premise of the shadow is, in that setting, provable. For Type I, Language Compression Residuals compare a text learner, which sees only a lossy text-like encoding of the signal, against a full-signal learner, which sees the underlying signal directly. The text learner sits at a computable expressibility ceiling while the full-signal learner pulls away by a gap that stays flat across 300x more data, so the deficit is a property of the channel, not of training. For Type II, the Counterfactual Distinction Test trains models on data exactly consistent with two incompatible rules. Across a provable string task and a language-like agreement task, behavior on counterfactuals is set by the model's inductive bias, while 5% disambiguating data steers the learned rule bidirectionally to either target (r = +/-1.0, p < 1e-10). For Type III, Basin Escape Mapping exhibits a function that is representable at 100% (by hand construction) yet reached 0% of the time by standard training and instantly from a nearby initialization, with width scaling providing no help (p = 1.6 x 10^-14). Each effect is isolated by a control that rules out a capacity or modality artifact. We release the probe suite and discuss implications for benchmark design, capability auditing, and shadow-aware uncertainty.

### 中文一句话结论
本文提出了“信息阴影”概念，揭示了语言模型从文本中学习时存在的三种结构性限制，这些限制无论数据规模、计算资源如何增加都无法被消除。

### English TL;DR
This paper introduces the "information shadow," identifying three types of structural limits on what language models can learn from text that persist regardless of scale, data, or computational resources, and provides provable probes to measure each type.

### 中文详细总结
该研究指出，语言模型的知识存在一些非数据覆盖不足导致的局限，而是源于从文本中学习这一过程的结构性特征。作者将这类无法通过增加数据量、模型规模或计算资源来克服的局限称为“信息阴影”。阴影包含三种类型：（I）语言无法表达的结构；（II）从训练分布中无法进行统计辨识的函数；（III）模型结构可表示但梯度训练无法达到的函数。论文为每一类限制设计了可验证的探测方法（Probe），并通过控制实验排除了容量或模态因素的影响。实验使用小型模型和合成任务以确保每个阴影设定的前提是可证明的，而非假设。

### 方法 / 贡献
1. **提出三类结构性限制的分类法**：每个类型都有可伪造、可测量的特征签名。
2. **Type I - 语言压缩残差 (LCR)**：对比仅能看到有损文本编码的“文本学习者”与能看到底层完整信号的“全信号学习者”，发现文本学习者的表现存在可计算的表达能力上限，且无论数据量扩大300倍，差距依旧恒定，证明瓶颈在于语言通道本身。
3. **Type II - 反事实区分测试 (CDT)**：构建恰好与两个不兼容规则（如复制 vs 反转）一致的训练数据，训练后的模型在反事实测试输入上的行为完全由归纳偏置决定；仅加入5%的解析性数据即可双向引导模型学到目标规则（r = +/-1.0, p < 1e-10）。
4. **Type III - 盆地逃逸映射 (BEM)**：通过人工构造证明目标函数（如k-稀疏奇偶性）可由模型表示（100%可表示），但标准SGD训练完全无法达到（0%到达率），且从邻近初始化可立即达到；增加网络宽度也无济于事（p = 1.6 x 10^-14）。
5. 发布了可复现的探测工具套件。

### 实验或数据
- **Type I实验**：使用MLP模型，输入为量化后的文本和连续信号，任务为判断两个连续值的大小关系。数据量从300到100k，8个随机种子。
- **Type II实验**：
  - **字符串任务**：输入回文字符串，目标为复制（Copy）或反转（Reverse）规则。训练集仅含回文（不可辨识），测试集用非回文（反事实）。每个条件30个随机种子。
  - **语言类任务**：主谓一致任务，规则为层级关系（Hierarchical）与线性关系（Linear），训练数据中所有名词数一致，测试时插入干扰名词。
  - 控制条件注入5%的解析性数据。
- **Type III实验**：小规模解码器Transformer和两层ReLU MLP，任务为k-稀疏奇偶性。提供证明表示性的构造，并比较不同初始化、课程学习和网络宽度下的到达率。
- 论文明确提到所有实验使用**小型模型和合成任务**，以确保结论的可证明性。

### 值得关注点
- 将语言模型学习的理论极限从“数据不足”问题中区分出来，提出了“结构性阴影”的统一框架。
- 每一类限制都有对应的**可验证探测方法**和**控制实验**，区分了通道限制、数据生成过程限制和训练动态限制。
- 强调了不同限制类型对应不同的缓解策略：Type I无法通过增加文本数据解决，Type II无法通过扩大规模解决，Type III无法通过增加相同数据或参数解决。
- 揭示了归纳偏置（架构和优化器）在数据不足时对模型行为的决定性影响。

### 局限性
- 所有实验均使用**小型模型和合成任务**，结果在大型模型和真实复杂场景下的普适性有待验证。
- Type I的“语言压缩残差”实验通过量化模拟文本的损失特性，但真实自然语言的理解可能涉及更复杂的压缩和抽象过程。
- Type III的盆地逃逸映射基于特定的奇偶函数和MLP架构，其他函数和架构的不可达性可能具有不同特性。
- 论文未探讨这三种限制之间可能存在的相互作用或组合效应。

## 6. LatentMT: Machine Translation with Latent Reasoning

- Source: arxiv
- arXiv ID: 2607.18618
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.18618v1
- PDF: https://arxiv.org/pdf/2607.18618v1
- DOI: https://doi.org/10.48550/arXiv.2607.18618

### Authors

Wei-Rui Chen, Samar M. Magdy, Chiyu Zhang, Wenhui Zhu, Zhipeng Wang, Muhammad Abdul-Mageed

### Abstract

Latent-reasoning looped language models (LoopLMs) offer a different scaling path for machine translation (MT): instead of increasing parameter count or emitting explicit chain-of-thought tokens, they spend additional recurrent computation inside hidden states. We introduce LatentMT, the first systematic study of latent-reasoning LoopLMs for machine translation. LatentMT adapts a small 2.6B-parameter backbone model with lightweight training. Across 32 translation directions spanning high-, mid-, and low-resource languages, LatentMT achieves performance comparable to models three to five times larger. It is competitive in a high-resource language and achieves state-of-the-art performance on both mid-resource and low-resource languages. Studying the behavior of scaling the number of recurrent reasoning steps, we find that recurrent computation consistently improves translation quality in early steps, then saturates quickly afterwards. Our mechanistic analysis shows that hidden-representation differences shrink along the recurrent reasoning-step axis, supporting the observed saturation in performance. Finally, our efficiency analysis shows that LatentMT requires lower training and inference compute than much larger non-latent-reasoning models with similar performance, making latent recurrent computation a promising path toward compact, efficient, and strong machine translation.

### 中文一句话结论
LatentMT 通过在一个 26 亿参数的循环语言模型中使用隐式推理，实现了与三到五倍大的模型相当的翻译性能，尤其在中低资源语言上取得了当前最佳结果，同时训练和推理计算成本更低。

### English TL;DR
LatentMT uses a compact 2.6B-parameter looped language model with latent reasoning to achieve machine translation performance comparable to models three to five times larger, with lower training and inference compute, and state-of-the-art results on mid- and low-resource languages.

### 中文详细总结
LatentMT 首次系统性地研究了用于机器翻译的隐式推理循环语言模型 (LoopLM)。该方法采用一个仅 26 亿参数的冻结骨干模型，并为其添加轻量级的 LoRA 适配器，以适配不同的语言对。在涵盖高、中、低资源语言的 32 个翻译方向上，LatentMT 的表现与参数规模大 3-5 倍的模型相当。具体来说，LatentMT 在高资源语言上具备竞争力，并在中低资源语言上达到了当前最佳水平。研究还发现，增加循环推理步数能在早期持续提升翻译质量，但很快会饱和。机制分析显示，随着推理步数增加，隐层表示的差异逐渐缩小，这支持了性能饱和的现象。最后，效率分析表明，LatentMT 的训练和推理计算开销低于性能相当的非隐式推理大模型。

### 方法 / 贡献
1. **引入隐式推理用于机器翻译**：首次系统性地将隐式推理的 LoopLM 应用于机器翻译任务。
2. **轻量级适配**：采用参数高效的微调方法（LoRA），仅更新少量适配器参数，冻结大型骨干模型。这使得一个部署的骨干模型可以服务多个语言对。
3. **可扩展的循环深度**：将循环推理步数作为可控实验变量，研究其对翻译质量的影响，并发现其效果会饱和。

### 实验或数据
- **模型**：主要使用 Ouro-2.6B-Thinking（一个 26 亿参数的 LoopLM）作为骨干模型。为进行比较，还训练了 Qwen3-8B 作为对照。
- **数据集**：
    - **高资源**：DRT（英语-中文）数据集。
    - **中资源**：ArzEn-MultiGenre（英语-埃及阿拉伯语）数据集。
    - **低资源**：OLDI/Flores（包含 30 种低资源语言的随机子集）数据集。
- **实验设置**：在每种语言对上使用 LoRA 进行微调。主要实验将循环推理步数 u 从 1 扫描到 6，以研究其对性能的影响。
- **评估指标**：BLEU、chrF++、COMET 和 COMETKiwi。

### 值得关注点
1. **高性能与高效率的平衡**：在不使用更大模型或显式思维链的情况下，通过增加循环计算（隐式推理）来提升性能，这对于资源受限的设备部署（如边缘计算）非常有价值。
2. **隐式推理 vs. 显式推理**：与传统需要生成中间推理token的显式思维链不同，LatentMT 的推理发生在连续的隐层状态中，这使得其计算扩展路径（在深度上扩展）与显式方法（在序列长度上扩展）截然不同。
3. **饱和特性**：发现性能提升在最初的几个循环步骤后就饱和了，这为实际应用中选择合适的循环步数提供了指导。

### 局限性
论文摘要和内容未明确提及具体的局限性。根据公开信息推断，其局限性可能包括：隐式推理的“黑盒”性质使得其推理过程难以解释和调试；性能在早期步骤后快速饱和，限制了通过增加步骤持续提升效果的可能性；模型在非英语语言（如中文）上的预训练数据可能有限，这可能影响特定语言对的表现。

## 7. Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing

- Source: arxiv
- arXiv ID: 2607.18934
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.18934v1
- PDF: https://arxiv.org/pdf/2607.18934v1
- DOI: https://doi.org/10.48550/arXiv.2607.18934

### Authors

Laurin Wagner, Mario Zusag, Bernhard Thallinger

### Abstract

Modern ASR models trained on heterogeneously annotated data treat transcription style (verbatim vs. intended) as an uncontrolled latent variable, causing measurable decoding instability, evaluation confounding (up to 60% of reported WER attributable to style mismatch), and unreliable word-level timing. We show that models already encode both styles; the challenge is controlled activation. Using coverage-aware decoder task tokens trained on parallel verbatim/intended transcript pairs, we raise German disfluency F1 from 10% to 79% zero-shot, despite English-only training. Full English-only fine-tuning surpasses all baselines in verbatim accuracy, disfluency detection, and intended-mode quality across both languages. We further introduce supervised cross-attention fine-tuning that improves word-level timestamps on disfluent speech beyond forced-alignment baselines. Finally, we propose verbatimize, a new task enabling scalable creation and enrichment of speech corpora with high-quality canonical verbatim transcriptions.

### 中文一句话结论
本文提出通过覆盖感知模式标签（coverage-aware mode tags）和监督式交叉注意力微调（supervised cross-attention fine-tuning），将转录风格（逐字/意图）作为可控潜在变量，从而在不依赖外部对齐组件的情况下，实现跨语言的稳定逐字输出、改进的言语不流畅检测和可靠的词级时间戳。

### English TL;DR
This paper shows that by treating transcription style (verbatim vs. intended) as a controllable latent variable via coverage-aware mode tags and supervised cross-attention fine-tuning, ASR models can achieve stable verbatim output, improved disfluency detection, and reliable word-level timing across languages without external alignment components.

### 中文详细总结
现代ASR模型在异构标注数据上训练时，会将转录风格（逐字 vs. 意图）当作不受控的潜在变量，导致解码不稳定、评估混淆（报告的词错误率WER中高达60%可归因于风格不匹配）以及词级时间戳不可靠。本文证明模型本身已编码了两种风格，关键在于受控激活。作者通过三种互补机制解决了这一问题：1）显式的转录策略控制：使用覆盖感知的解码器前缀模式标签（[verbatim_1..3], [sound_1,2], [intended_1..5]），在并行逐字/意图转录对上训练，仅凭纯英语训练即可零样本将德语言语不流畅F1从10%提升至79%；2）监督式交叉注意力词级时间戳：直接监督选定的交叉注意力头，在流畅语音上达到36毫秒的平均绝对边界误差，在不流畅语音上达到102毫秒，首次优于强制对齐基线；3）Verbatimize任务：给定音频和任意意图转录，生成规范逐字版本，通过插入声学基础上不流畅点将罕见词召回率从6.8%提升至96.1%，实现低成本逐字标注。此外，文章还引入了语言无关的评估框架，可自动提取类型化不流畅标签并将WER分解为内容和风格成分。

### 方法 / 贡献
- **核心方法**：将转录风格作为可控潜在变量，通过覆盖感知模式标签（根据标注覆盖率划分逐字标签，区分不流畅和声音事件）进行显式策略参数化；监督式交叉注意力微调（选择与真实对齐最相关的注意力头，通过余弦距离最小化使平均注意力分布匹配词边界目标）；Verbatimize任务（给定意图转录和音频，生成声学支持下的规范逐字版本）。
- **主要贡献**：1）零样本跨语言风格控制（英语训练、德语测试）；2）首次在不依赖外部对齐组件的情况下，在言语不流畅语音上超越强制对齐基线的时间戳精度；3）提出verbatimize任务，支持可扩展的高质量规范逐字标注；4）提出风格感知评估框架，分离内容错误与风格差异。

### 实验或数据
- **主要数据集**：英语使用DisfluencySpeech、AMI、TED-LIUM、LibriSpeech、TIMIT、FluencyBank；德语使用自建German DisfluencySpeech评估集。训练数据混合了多种标注覆盖率的语料，包括注入声音事件的干净样本和完整标注的不流畅语料。
- **实验内容**：1）风格控制实验：改变训练数据中逐字/意图比例（0-100%），对比有无模式标签下的不流畅F1；2）解码稳定性：测量束搜索发散度（beam divergence CER）；3）评估混淆：分解WER为内容损失率（CLR）和风格成分；4）时间戳精度：在流畅和不流畅语音上测量平均绝对边界误差（MAE）；5）verbatimize效果：测量罕见词召回率。

### 值得关注点
- **高质量图/表**：图1展示了随逐字数据比例变化的不流畅F1曲线；表2展示了束发散度比较；图2展示了WER分解结果；时间戳精度数字（36ms/102ms MAE）明确优于现有方法。
- **独特方法与发现**：零样本跨语言风格控制（英语训练、德语测试）；覆盖感知标签分区解决异构标注梯度冲突；监督式交叉注意力首次在不流畅语音上超越强制对齐；风格感知评估框架将评估混淆从60% WER中分离出来。

### 局限性
- 该方法依赖高质量并行逐字/意图转录对进行训练，而此类数据在大多数语言中稀缺。
- 监督式交叉注意力微调需要在TIMIT等具有准确词边界标注的数据上进行预选头，限制了即插即用能力。
- Verbatimize任务假设意图转录准确可用，在噪声环境下可能引入错误传播。
- 实验主要聚焦德语和英语，对其他语言（尤其是非拼音文字语言）的泛化能力未充分验证。

## 8. OpenRTAG: A Comprehensive Benchmark for Robust Text-Attributed Graph Learning under Data Quality Degradation

- Source: arxiv
- arXiv ID: 2607.19108
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.19108v1
- PDF: https://arxiv.org/pdf/2607.19108v1
- DOI: https://doi.org/10.48550/arXiv.2607.19108

### Authors

Yuze Dai, Zhihan Zhang, Yan Zhao, Ruoyu Wu, Xunkai Li, Zekai Chen, Qiangqiang Dai, Hongchao Qin, Ronghua Li

### Abstract

Text-attributed graphs (TAGs) are an important graph data form that combine relational structure with rich node text. However, real-world TAGs are often imperfect, with quality issues arising from text, structure, and labels, and typically manifesting as sparsity, noise, and imbalance. These dimensions define nine representative degradation scenarios that can substantially affect TAG learning. Although prior studies have explored specific mitigation strategies, existing evidence remains fragmented across degradation types, datasets, tasks, and model families, leaving TAG robustness insufficiently understood. To address this gap, we present OpenRTAG, a robustness benchmark for text-attributed graph learning. OpenRTAG organizes TAG quality issues into a unified 3 * 3 taxonomy and supports standardized evaluation across nine TAG datasets and three downstream tasks. It systematically evaluates scenario validity and model sensitivity, compares traditional GNNs, LLM-GNNs, and a representative GFM, investigates the effectiveness, efficiency, and robustness of scenario-matched baselines, and further examines model behavior under composite degradation scenarios. OpenRTAG provides a standardized testbed for understanding robustness in TAG learning under realistic low-quality settings.

### 中文一句话结论
OpenRTAG提出了一个统一的3×3数据质量退化分类体系，系统评估了文本属性图学习在文本、结构和标签三种模态下的稀疏、噪声和不平衡问题中的鲁棒性。

### English TL;DR
OpenRTAG introduces a comprehensive benchmark that systematically evaluates the robustness of text-attributed graph learning under a unified 3×3 taxonomy of data quality degradations—spanning text, structure, and label sparsity, noise, and imbalance—across multiple datasets and downstream tasks.

### 中文详细总结
文本属性图（TAG）结合了关系结构与节点文本，但在实际应用中常存在数据质量问题。本文提出OpenRTAG基准，将TAG质量问题归纳为一个3×3分类体系（三种模态：文本、结构、标签；三种退化类型：稀疏、噪声、不平衡），定义出九种代表性退化场景。OpenRTAG支持在9个TAG数据集和三个下游任务（节点分类、节点聚类、链接预测）上进行标准化评估，系统比较了传统GNN、LLM-GNN和图基础模型（GFM）的鲁棒性，并评估了针对特定退化的基线方法的有效性、效率和鲁棒性，以及在复合退化场景下的表现。

### 方法 / 贡献
1. **统一退化分类体系**：定义了涵盖文本、结构、标签三种模态下稀疏、噪声、不平衡的3×3场景空间。
2. **标准化基准框架**：构建了统一的场景构建、数据准备、模型评估和分析框架，涵盖多个数据集和任务。
3. **系统性鲁棒性研究**：评估了场景有效性和模型敏感性，比较了多种模型范式，研究了场景匹配基线的有效性、效率和鲁棒性，并探索了复合退化场景下的模型行为。

### 实验或数据
使用九个TAG数据集（Cora, CiteSeer, Instagram, WikiCS, PubMed, Children, Photo, History, Arxiv）和三个下游任务（节点分类、节点聚类、链接预测）。实验包括：Q1评估模型范式鲁棒性，Q2-Q4评估文本、结构、标签退化下的匹配基线方法，Q5评估复合退化场景和任务泛化性。

### 值得关注点
提出的退化场景构建方法将退化语义与底层实现分离，支持可配置、可重复的实验。系统评估揭示不同模型范式在不同退化类型下的敏感性差异，为实际低质量TAG学习提供了标准化测试平台。

### 局限性
该基准仅覆盖了三种退化类型和三种模态的组合，可能无法涵盖所有实际数据质量问题。复合退化场景仅探讨了两个退化场景的组合，更复杂的多因素退化仍需进一步研究。

## 9. Beyond Score Prediction: LLM-Based Essay Scoring and Feedback Generation via Reinforcement Learning with Rubric Rewards

- Source: arxiv
- arXiv ID: 2607.19219
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.19219v1
- PDF: https://arxiv.org/pdf/2607.19219v1
- DOI: https://doi.org/10.48550/arXiv.2607.19219

### Authors

Xuefeng Jin, Jiashuo Zhang, Teng Cao, Bin Yang

### Abstract

Large language models (LLMs) have been widely applied to automated essay scoring (AES) and automated feedback generation (AFG). However, existing studies rely primarily on prompt engineering or supervised fine-tuning, while systematic research on reinforcement learning (RL) post-training and automated evaluation of feedback quality remains limited. We propose RLAES, a unified LLM framework that jointly optimizes essay scoring and feedback generation through RL. To make feedback quality measurable, interpretable, and usable for training, we introduce Rubric-based Feedback Evaluation (RFE), an essay-grounded feedback evaluation framework comprising 166 fine-grained binary rubric items and an LLM-as-judge. Building on RFE, we propose Adaptive Gated Feedback Optimization (AGFO), which activates rubric-based feedback rewards on demand during RL, reducing evaluation overhead while improving feedback quality. We also propose Adjacent Contrastive Reasoning (ACR) to improve ordinal score calibration by explicitly contrasting adjacent score levels. Experimental results show that the RFE framework captures essay-feedback consistency, exhibits strong pairwise discriminative power, and closely aligns with expert preferences. On the ASAP benchmark, RLAES-AGFO achieves the best scoring performance among LLM-based methods (QWK = 0.803), while maintaining feedback quality comparable to GPT-5.5 and avoiding the feedback degradation observed under score-only RL. Code and datasets are publicly available at https://github.com/hellomuyi/RLAES.

### 中文一句话结论
本文提出 RLAES 框架，通过强化学习联合优化作文评分与反馈生成，在 ASAP 基准上达到最优评分性能（QWK=0.803），并利用基于评分标准的反馈评估机制避免反馈质量退化。

### English TL;DR
This paper introduces RLAES, a reinforcement learning-based framework for jointly optimizing automated essay scoring and feedback generation, achieving state-of-the-art scoring performance (QWK=0.803) while preventing feedback degradation through a novel rubric-based feedback evaluation and adaptive reward mechanism.

### 中文详细总结
现有基于大语言模型的自动作文评分与反馈生成主要依赖提示工程和监督微调，缺乏对强化学习后训练以及反馈质量自动评估的系统研究。本文提出 RLAES 统一框架，核心贡献包括：1) **RFE 框架**：包含 166 个细粒度二元评分项，以 LLM 作为裁判，实现可量化的反馈质量评估；2) **AGFO 方法**：在强化学习中有选择地激活反馈奖励，降低评估开销并提升反馈质量；3) **ACR 策略**：通过显式对比相邻分数级别，改善顺序分数标定。实验表明，RLAES-AGFO 在 ASAP 数据集上取得 LLM 方法中最佳评分性能（QWK=0.803），反馈质量与 GPT-5.5 相当，且避免了仅用分数奖励导致的反馈退化。

### 方法 / 贡献
- 提出 RLAES，首个将强化学习后训练用于联合优化作文评分与反馈生成的框架。
- 提出 RFE（基于评分标准的反馈评估），包含 166 个二元评分项和 LLM 裁判，实现细粒度、可解释的反馈质量量化。
- 提出 AGFO（自适应门控反馈优化），在 RL 中按需激活反馈奖励，降低评估成本并提升质量。
- 提出 ACR（相邻对比推理），通过对比相邻分数缓解序数分类中的混淆问题，提升评分准确性。

### 实验或数据
- 使用 ASAP 公开数据集，包含 8 个作文提示的评分数据。
- RLAES-AGFO 取得 LLM 方法最佳评分性能（QWK = 0.803）。
- RFE 框架在一致性、区分力和与专家偏好对齐方面表现优异。
- 反馈质量与 GPT-5.5 相当，且未出现仅用分数奖励时的反馈退化。

### 值得关注点
- 首次系统地将强化学习后训练应用于作文评分和反馈生成联合优化。
- RFE 通过细粒度评分项将反馈质量转化为可训练奖励信号，弥补了自动评估缺失。
- AGFO 通过自适应门控策略显著降低 LLM 裁判的调用开销。
- ACR 作为通用策略，可推广至其他序数分类任务。

### 局限性
文中未明确讨论局限性。潜在方面可能包括对 LLM 裁判的依赖带来的计算开销，以及评分标准需人工构建和维护，但未在原文中详述。

## 10. Structured Synthetic Reasoning Data for Arithmetic Fine-Tuning of Small Language Models

- Source: arxiv
- arXiv ID: 2607.18266
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.18266v1
- PDF: https://arxiv.org/pdf/2607.18266v1
- DOI: https://doi.org/10.48550/arXiv.2607.18266

### Authors

Jake O'Grady, Effirul Ramlan

### Abstract

Small language models are attractive for local deployment, but they often struggle with multi-step arithmetic reasoning. We study whether structured synthetic reasoning data can improve this behaviour under consumer-hardware constraints. Starting from GSM8K, we generated a 21,250-example corpus of grade-school arithmetic word-problem variants using GPT-5-mini, combining natural-language solution traces, light Socratic-style cues, structural variation, and irrelevant distractor context. We then fine-tuned Qwen3-0.6B and Qwen3-1.7B with LoRA on consumer hardware (Apple M4, 16 GB RAM). Exact-match accuracy on GSM8K improved from 36.5% to 49.1% for Qwen3-0.6B and from 53.5% to 66.5% for Qwen3-1.7B. For Qwen3-1.7B, transfer to related arithmetic benchmarks was stronger, reaching 98.9% on MultiArith and 73.0% on SVAMP, compared with 54.4% and 45.3% for the base model. Qualitative analysis suggests that fine-tuned models produce shorter reasoning traces, make fewer arithmetic and distractor-use errors, and benefit more consistently from self-consistency sampling. These results show that low-cost synthetic data design can materially improve arithmetic adaptation in small language models. Because the intervention combines Socratic-style cues with other data-design choices, we interpret the gains as evidence for structured synthetic reasoning data rather than as a causal test of Socratic guidance alone.

### 中文一句话结论
通过在消费级硬件上使用包含自然语言解答、苏格拉底式提示、结构变异及无关干扰项的21,250条结构化合成数据对Qwen3-0.6B和Qwen3-1.7B进行LoRA微调，显著提升了多步算术推理精度（GSM8K准确率分别提高12.6%和13.0%），并展示了良好的跨基准迁移能力。

### English TL;DR
Fine-tuning small language models (Qwen3-0.6B and Qwen3-1.7B) on a 21,250-example structured synthetic dataset combining natural-language solution traces, Socratic-style cues, structural variation, and irrelevant distractor context improved exact-match accuracy on GSM8K from 36.5% to 49.1% and from 53.5% to 66.5%, with strong transfer to related benchmarks (98.9% on MultiArith and 73.0% on SVAMP), demonstrating that low-cost synthetic data design can materially enhance arithmetic reasoning under consumer-hardware constraints.

### 中文详细总结
本研究针对小语言模型在多步算术推理上的不足，提出一种低成本结构化合成数据生成流程。基于GSM8K，使用GPT-5-mini生成21,250道小学算术题变体，每个变体包含自然语言解答轨迹、轻量苏格拉底式引导问题、结构/数值变化及无关干扰上下文，并经过四阶段过滤（格式检查、长度筛选、去重、去除末位反问句）。随后在消费级硬件（Apple M4, 16GB RAM）上对Qwen3-0.6B（bf16）和Qwen3-1.7B（4-bit量化）进行LoRA微调（适配所有28层Transformer，目标Q/K/V/O及FFN投影）。GSM8K测试集（4-shot,单样本）准确率：0.6B模型从36.5%提升至49.1%，1.7B模型从53.5%提升至66.5%。在未见过的MultiArith和SVAMP基准上，微调后的1.7B模型通过自一致性采样分别达到98.9%和73.0%，远高于基线的54.4%和45.3%。定性分析表明，微调模型产生的推理轨迹更短，算术错误和干扰项利用错误更少，且自一致性采样带来的提升更一致。由于干预包含多种数据设计选择，结果被解释为结构化合成推理数据的整体效果，而非单独对苏格拉底式引导的因果测试。

### 方法 / 贡献
- **方法**：利用GPT-5-mini从GSM8K生成合成算术题变体（含苏格拉底式提示、结构变异、干扰上下文）；多阶段过滤；在Apple M4上使用LoRA微调Qwen3-0.6B和Qwen3-1.7B。
- **贡献**：(1) 提出了低成本构建过滤后合成算术推理数据的流水线，总API成本仅$20.88；(2) 证明LoRA微调在此数据上能显著提升小模型在GSM8K上的准确率并迁移至相关基准；(3) 分析了微调过程中的设计经验，包括解答格式、LoRA层覆盖及推理误差的定性变化。

### 实验或数据
- **数据集**：GSM8K（训练集7,473题，测试集1,319题）作为源数据；生成合成训练集21,250例（90/10分为19,125训练/2,125验证）；评估使用GSM8K测试集、SVAMP（1,000题）和MultiArith（180题）。
- **模型**：Qwen3-0.6B（bf16）和Qwen3-1.7B（4-bit），所有LoRA适配器应用于28层Transformer。
- **评估**：GSM8K采用4-shot单样本精确匹配；SVAMP和MultiArith使用自一致性采样（1/2/4样本，温度0.7，多数投票）。
- **硬件**：Apple M4，16GB统一内存。
- **基线**：包括LLaMA-3.2-1B/3B、Mistral-7B、Gemma-3-4B、Qwen3-4B等，在相同条件评估。

### 值得关注点
- **极低成本**：合成数据生成仅$20.88 API费用，微调在普通消费级电脑（16GB RAM）上完成。
- **显著提升**：Qwen3-1.7B在GSM8K上提升13%，在MultiArith上几乎达到完美（98.9%）。
- **定性改善**：微调模型推理更简洁、错误更少，且自一致性采样收益更稳定。
- **组合式设计**：数据包含多种策略（自然语言解答、苏格拉底式提示、结构变异、干扰项），展现了结构化合成数据的整体效果。

### 局限性
- 实验未能单独分离苏格拉底式提示的因果效应，改进归因于结构化合成数据的整体设计。
- 仅测试了小型模型（≤1.7B参数），在消费级硬件上更大模型的适用性未知。
- 合成数据可能引入GPT-5-mini的生成偏差或表面模式，影响泛化。
- 评估限于英语小学算术题，未检验其他语言或更高阶推理任务。
- 未与大规模蒸馏或全参数微调进行比较，性能上限未探索。

## Processing Notes

- Duplicate papers skipped: 0