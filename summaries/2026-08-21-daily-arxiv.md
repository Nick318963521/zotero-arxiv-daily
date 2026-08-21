# Daily arXiv - 2026-08-21

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-21T22:28:06
- Paper count: 10

## 1. Improved Confidence Estimates for Black-Box Large Language Models

- Source: arxiv
- arXiv ID: 2608.19323
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.19323v1
- PDF: https://arxiv.org/pdf/2608.19323v1
- DOI: https://doi.org/10.48550/arXiv.2608.19323

### Authors

Sokhna Diarra Mbacke, Mouloud Belbahri, Gabriel Loaiza-Ganem

### Abstract

Uncertainty quantification (UQ) is essential for the safe deployment of large language models (LLMs). Existing methods, from verbalized confidence to ones requiring multiple generations, are often zero-shot and produce scores quantifying uncertainty without the need for labelled data. Nonetheless, in practice one must always evaluate their performance on a dataset of interest before deployment. In this work we show that, by leveraging this dataset, we consistently outperform these existing scores. Specifically, we build simple classifiers that predict LLM response correctness by using these scores and the correctness of similar queries as features. Our method produces minimal computational overhead, making it a cheap and straightforward enhancement for UQ in LLMs for real-world applications.

### 中文一句话结论
通过利用一个小型数据集训练简单的分类器，结合现有不确定性评分和查询相似性，可以显著提升黑盒大语言模型的不确定性量化性能。

### English TL;DR
By leveraging a small dataset to train simple classifiers that combine existing uncertainty scores with query similarity, this work significantly improves uncertainty quantification for black-box large language models with minimal computational overhead.

### 中文详细总结
该研究指出，现有的不确定性量化方法（如口头置信度表达或需要多次生成的方法）通常是零样本的，无需标签数据即可生成评分。然而，在实际部署前，总需要在一个目标数据集上评估这些方法的表现。本文的核心贡献是证明，通过利用这个评估数据集，可以系统性地超越现有评分方法。具体做法是，将现有评分和相似查询的正确性作为特征，训练一个简单的分类器来预测大语言模型回答的正确性。这种方法带来的计算开销极小，是对现有不确定性量化方法的廉价且直接的增强。

### 方法 / 贡献
- **方法**：构建一个简单的分类器，其输入特征包括现有的不确定性评分以及相似查询的正确性标签（“相似性”通过嵌入相似度等度量定义）。分类器的目标是预测当前查询的回答是否正确。
- **贡献**：1) 提出一种只需少量标注数据即可显著改善黑盒LLM不确定性估计的通用框架；2) 证明了该简单方法在多个数据集上持续优于纯零样本的现有评分方法；3) 计算成本极低，易于集成到实际应用中。

### 实验或数据
- 实验基于多个数据集（具体数据集名称需查阅原文）进行，但摘要中未提及具体数据集；方法需要一个小型标注数据集（包含查询、回答和正确性标签）来训练分类器。
- 实验结果表明，所提出的分类器在预测回答正确性方面，在多个指标上一致地优于基线（现有零样本评分方法）。

### 值得关注点
- **简洁高效**：仅需一个简单的分类器和少量数据，就能稳定提升性能。
- **通用性强**：可集成多种现有UQ评分作为特征，不依赖特定模型架构。
- **实际价值**：对于安全部署LLM非常关键，且计算开销低，便于落地。

### 局限性
- 方法依赖一个带标注的小型数据集（即需要知道部分查询的真实正确性），尽管这个数据集通常在评估阶段已有。
- 分类器的性能可能受限于特征的质量（即现有UQ评分和相似性度量的有效性）。
- 在极端少量数据或分布外样本上的表现需要进一步验证。

## 2. When Machines Speak: A Unified Generative Framework for Integrating Machine-Native Symbols into Pretrained Large Language Models

- Source: arxiv
- arXiv ID: 2608.19529
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.19529v1
- PDF: https://arxiv.org/pdf/2608.19529v1
- DOI: https://doi.org/10.48550/arXiv.2608.19529

### Authors

Su Yan, Rakesh Iyer

### Abstract

Many real-world AI systems represent entities, behaviors, and structured information using discrete machine-native symbols rather than natural language. While these representations are compact and preserve task-relevant structure, they lie outside the linguistic token space of pretrained large language models (LLMs), creating a fundamental divide between language modeling and structured prediction. We introduce UniLang, a unified generative framework that bridges this divide by extending pretrained LLMs to treat machine-native symbols as first-class generative units alongside natural-language tokens. UniLang expands the LLM's vocabulary and embedding space with grounded machine-native representations, enabling textual and symbolic tokens to be jointly modeled and generated under a single autoregressive objective. This unified interface allows pretrained LLMs to directly operate on machine-native representations without requiring them to be verbalized as natural language or relying on task-specific architectures. We evaluate UniLang on two structurally distinct tasks, sequential recommendation and legal precedent prediction, spanning different domains and types of structured prediction. Across both tasks, UniLang consistently outperforms strong baselines, demonstrating a path toward extending pretrained LLMs beyond language and using them as a common generative modeling backbone for heterogeneous machine-native representations.

### 中文一句话结论
UniLang通过扩展预训练大语言模型的词汇表和嵌入空间，将机器原生符号作为一等生成单元与自然语言令牌联合建模，实现了跨结构化预测任务的统一生成框架。

### English TL;DR
UniLang extends pretrained LLMs by expanding their vocabulary and embedding space to jointly model machine-native symbols and natural-language tokens under a single autoregressive objective, enabling direct handling of structured prediction without verbalization or task-specific architectures.

### 中文详细总结
UniLang提出一种统一生成框架，旨在弥合自然语言建模与结构化预测之间的鸿沟。其核心方法是将机器原生符号（例如通过残差量化变分自编码器RQ-VAE生成的离散代码）直接集成到预训练LLM的词汇表中，视为与自然语言令牌同等地位的生成单元。通过对比学习将机器令牌的嵌入与对应文本描述的嵌入对齐，实现语义接地。在联合自回归建模中，模型可在同一序列中生成自然语言和机器符号。该框架在顺序推荐和法律先例预测两个任务上评估，均优于强基线方法，展示了通用性。

### 方法 / 贡献
1. **统一表示接口**：将结构化预测转化为异构令牌类型的自回归生成，使机器原生符号和自然语言令牌在同一个预训练LLM中作为一等生成单元。
2. **对比学习接地集成**：扩展LLM词汇表，引入机器令牌，并通过InfoNCE对比损失将机器令牌嵌入与文本描述嵌入对齐，仅更新机器令牌嵌入，保持LLM参数冻结。
3. **通用性**：无需任务特定的架构修改，同一UniLang框架可直接应用于顺序推荐和法律先例预测等不同领域。

### 实验或数据
论文在顺序推荐和法律先例预测两个结构化预测任务上评估UniLang。顺序推荐使用基于RQ-VAE的语义ID表示物品，法律先例预测涉及引用语境与目标段落。实验结果表明UniLang在两个任务上均持续优于强基线模型。摘要中未给出具体数据集名称和详细数值。

### 值得关注点
- 将机器原生符号作为一等公民直接融入LLM的生成过程，避免了将其转换为自然语言带来的信息损失。
- 对比接地过程利用预训练LLM的语义知识对齐机器符号，无需重新训练整个模型。
- 统一框架适用于不同领域和不同类型的结构化预测，展示了跨任务的通用性。

### 局限性
论文未明确讨论局限性。潜在问题可能包括：对RQ-VAE等机器表示构建方法的质量依赖；机器令牌词汇量固定（1,024个），可能不适用于需要大量唯一标识的场景；对比接地需要预计算文本嵌入，可能带来额外计算开销；评估任务有限，未在更多样化或更复杂的结构化预测任务上验证。

## 3. When Irrelevant Text Matters: Affine Margin Shifts in Multimodal Large Language Models

- Source: arxiv
- arXiv ID: 2608.19208
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.19208v1
- PDF: https://arxiv.org/pdf/2608.19208v1
- DOI: https://doi.org/10.48550/arXiv.2608.19208

### Authors

Yinfeng Wang, Zhiyuan Yao, Zheren Fu, Lei Zhang, Zhendong Mao

### Abstract

Multimodal large language models (MLLMs) are frequently exposed to auxiliary textual context, the impact of which on visually grounded tasks remains underexplored. In this paper, we investigate the influence of task-irrelevant context by formulating it as a controlled intervention within a binary visual judgment framework. By maintaining an invariant prompt structure while varying auxiliary inputs, we observe that irrelevant text consistently biases model predictions across diverse benchmarks. To move beyond performance metrics, we characterize this sensitivity through a decision margin defined by the log-probability difference between binary candidates. Our analysis reveals a robust geometric regularity: contextconditioned margins follow a consistent affine transformation of their context-free counterparts. This finding demonstrates that irrelevant context does not manifest as unstructured stochastic noise but as a estimable distortion of model preference. We further interpret the fitted affine parameters as metrics for visual commitment preservation and directional answer bias. These findings provide a margin-level diagnostic view of irrelevant-context effects in MLLMs and offer a basis for future studies on noisy-context robustness

### 中文一句话结论
本研究发现，在视觉二分类判断中，与任务无关的文本上下文会系统地改变多模态大语言模型的决策边界，表现为一个可估计的仿射变换（affine transformation），而非随机噪声。

### English TL;DR
Irrelevant text in multimodal large language models consistently biases predictions by causing a systematic affine shift in the decision margins, revealing a predictable rather than random distortion in model preference.

### 中文详细总结
多模态大语言模型（MLLMs）在实际应用中常会接触到与当前视觉任务无关的辅助文本上下文（如检索到的无关段落、历史对话等）。现有研究对这类无关文本如何影响模型在视觉任务上的决策机制尚不清晰。本文通过将问题简化为二分类视觉判断框架（如"是/否"回答），系统地研究了无关文本的影响。作者引入"决策边界"（decision margin，即正负答案对数概率之差）作为分析指标，发现添加无关文本后，条件边界（m_c）与无文本边界（m_o）之间存在一个稳健的仿射变换规律：m_c ≈ a * m_o + b。这说明无关文本并非引入随机扰动，而是导致一种可预测、可度量的系统性偏差。该仿射关系在不同模型（LLaVA-1.5-7B、Qwen2-VL、InternVL3）和多个基准（MME、GQA、AMBER、POPE）上均得到验证，且同一模型下拟合参数在不同基准间保持稳定。进一步分析表明，斜率a反映模型对原始视觉决策结构的保持程度，截距b则代表无关文本引入的方向性回答偏好（通常偏向负面回答）。基于此，作者还设计了一种轻量级后处理校准方法以部分缓解这种偏差。

### 方法 / 贡献
- **方法**：将问题形式化为二分类视觉判断（正/负回答）；设置受控干预实验，比较无文本输入（仅图像+问题）与有无关文本输入（插入随机采样自外部语料的无关段落，保持提示结构不变）下的模型行为；定义决策边界为对数概率差（log-prob difference）；拟合条件边界与无文本边界之间的仿射关系（m_c = a m_o + b），并分析参数含义。
- **贡献**：首次从边界级别刻画了无关文本对MLLMs决策的系统性影响规律，揭示了其可预测的仿射结构；将仿射参数a和b解释为"视觉承诺保持度"和"方向性回答偏差"，提供了新的诊断指标；基于此规律设计了后处理校准方法。

### 实验或数据
- **实验设置**：在四个视觉语言基准（MME、GQA、AMBER、POPE）上进行，涉及二分类判断（如物体是否存在、属性是否正确等）。采用四种模型：LLaVA-1.5-7B、Qwen2-VL-2B、Qwen2-VL-7B、InternVL3。无关文本分为"中性"（neutral，与图像主题无关）和"条件性"（condition，可能被误认为与图像相关）两种语义框架。
- **主要结果**：无关文本普遍降低准确率和召回率，导致回答倾向偏向负面（Yes Rate下降），预测翻转率（Flip Rate）显著增加。条件性语义框架的影响远大于中性框架。仿射拟合结果显示，在所有模型和基准上，R² 和 Pearson 相关系数均很高，表明仿射关系非常稳健。斜率a在不同模型和基准间存在差异，但同一模型下相对稳定；截距b通常为负值，反映负面偏移。

### 值得关注点
- 无关文本的影响不是随机的，而是具有规则的仿射结构，这为建模和预测其影响提供了可能。
- 仿射参数a和b可作为诊断指标量化模型对视觉证据的依赖程度和无关文本引入的偏差方向。
- 基于该规律设计的后处理校准方法展示了缓解无关文本负面影响的潜在途径。
- 经典大模型（如LLaVA-1.5-7B）比近期模型（如Qwen2-VL-7B）受无关文本影响更小，斜率a更接近1，负偏移b更小。

### 局限性
- 研究仅限于二分类判断（Yes/No）任务，未考虑开放生成式回答。
- 无关文本采用随机采样自外部语料的方式，可能无法完全反映真实场景中复杂、多变的无关上下文类型。
- 仅探讨了单一无关文本插入的情况，未分析多个或混合上下文的影响。
- 仿射关系的解释（参数意义）基于启发式推断，缺乏理论严格证明。
- 后处理校准方法仅为轻量级尝试，未能完全消除偏差，在严重干扰场景下效果有限。

## 4. When Text and Numbers Disagree: Evidence Arbitration in Large Language Models

- Source: arxiv
- arXiv ID: 2608.20116
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.20116v1
- PDF: https://arxiv.org/pdf/2608.20116v1
- DOI: https://doi.org/10.48550/arXiv.2608.20116

### Authors

Mattia Carletti, Edward Phillips, Fredrik K. Gustafsson, Patitapaban Palo, Lei Clifton, Danielle Belgrave, Xiao Gu, David A. Clifton

### Abstract

Large language models (LLMs) are increasingly used in settings where textual summaries, numerical observations, and external tool outputs may provide conflicting evidence. We study how LLMs arbitrate between such sources when they support opposing decisions. To do so, we introduce a controlled synthetic benchmark in which latent risk trajectories generate both numerical time series and natural language summaries, allowing us to construct conflicts where exactly one evidence source is aligned with the ground-truth label. This design lets us independently manipulate modality, temporal recency, source reliability, and evidence provenance. Across open-weight instruction-tuned models, we find that arbitration behaviour is systematic rather than random: models exhibit distinct text-versus-number preferences, follow temporal recency more consistently than explicit reliability cues, and can over-rely on external forecasts even when they conflict with direct contextual evidence. These results suggest that current LLMs often rely on heuristic arbitration strategies when integrating heterogeneous evidence, highlighting a failure mode for tool-augmented decision systems.

### 中文一句话结论
本研究发现，大语言模型在仲裁文本与数值证据冲突时表现出系统性启发式策略，包括模态偏好、更依赖时间近因而非明确可靠性线索，以及过度依赖外部工具预测，这揭示了工具增强决策系统中的一个失败模式。

### English TL;DR
This paper introduces a controlled synthetic benchmark to study how large language models systematically arbitrate between conflicting textual and numerical evidence, revealing that they rely on heuristic strategies such as modality preferences, temporal recency over explicit reliability cues, and over-reliance on external forecasts.

### 中文详细总结
大型语言模型（LLMs）越来越多地被应用于需要整合文本摘要、数值观测和外部工具输出的场景，但这些信息源可能提供相互矛盾的证据。本研究通过构建一个受控的合成基准测试，系统性地探究LLMs如何在这些冲突中进行仲裁。

研究者设计了一个基于潜在风险轨迹的生成框架，同时生成数值时间序列和自然语言摘要，使得只有一个证据源与真实标签对齐。通过这一设计，可以独立操纵四个冲突维度：模态（文本 vs. 数值）、时间近因、来源可靠性、以及证据来源（直接观测 vs. 工具预测）。实验在多个开源指令微调模型上进行，包含Qwen3、Gemma、Llama和Mistral系列。

结果表明，LLMs的仲裁行为是系统性的而非随机的。具体发现包括：模型存在明显的文本与数值偏好差异；模型更倾向于遵循时间近因而非明确的可靠性标注；模型可能过度依赖外部工具预测，即使这些预测与直接的上下文证据相矛盾。这些发现表明，当前LLMs在整合异构证据时常依赖启发式仲裁策略，这在工具增强决策系统中构成一个重要的失败模式。

### 方法 / 贡献
1. **问题定义**：正式定义了“文本-数值证据仲裁”问题，即当文本与数值证据支持相反结论时，模型如何决定优先采用哪个来源。
2. **合成基准测试**：构建了一个大规模、受控的合成基准，能够独立操纵模态、时间近因、来源可靠性和证据来源四个维度，从而隔离不同因素对模型决策的影响。
3. **系统性发现**：揭示了跨模型系列的仲裁偏差和失败模式，包括模态偏好、提示顺序效应，以及对工具预测的过度依赖。

### 实验或数据
实验基于合成的风险轨迹数据，生成了长度为16步的时间序列，预测步长为1。针对每个冲突维度构建了平衡的数据集，包含等量的高/低标签。实验涉及以下开源模型：Qwen3系列（1.7B、4B、8B、14B）、Gemma-2-9B-It、Llama-3-8B-Instruct和Mistral-7B-Instruct-v0.3。实验覆盖四个冲突设定：基线模态偏好、时间近因冲突、可靠性冲突和工具预测冲突。论文未提及在真实世界数据集上的验证。

### 值得关注点
- **创新性设定**：本文首次系统性地研究了文本与数值证据之间的仲裁问题，填补了现有研究在跨模态证据冲突处理方面的空白。
- **受控实验设计**：通过合成数据精确控制冲突来源和真实标签，使研究者能够分离不同因素对模型决策的影响，这是真实数据难以做到的。
- **实际应用意义**：研究结果对高风险领域（如医疗、金融）中部署工具增强型LLM系统具有重要启示，揭示了模型可能因启发式策略而做出错误决策的风险。

### 局限性
论文明确指出，该研究的目的是隔离仲裁倾向而非复现真实世界的完全复杂性。因此，合成基准采用的简化设定（如二元分类、固定时间窗口）可能无法完全反映真实应用场景中的证据冲突。研究还主要集中在特定开源模型系列上，未涵盖更大规模或不同架构的模型（如闭源API模型）。此外，研究未引入推理增强方法（如思维链）来考察其是否能减轻仲裁偏差。

## 5. Contrastive Mixed Prompt Learning for Incomplete Multimodal Sentiment Analysis with Unseen Modality Combination

- Source: arxiv
- arXiv ID: 2608.20019
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.20019v1
- PDF: https://arxiv.org/pdf/2608.20019v1
- DOI: https://doi.org/10.48550/arXiv.2608.20019

### Authors

Kaixin Xu, NaiJin Liu, Yulin Kang, Tangyue Jin, Zixuan Yu, Wenxi Zhao, Yibei Liu, Qianle Zhang, Yangyang Wu, Mengying Zhu, Meng Xi

### Abstract

Incomplete multimodal sentiment analysis has garnered significant attention in recent years. Existing approaches typically assume that data is missing at random or are designed specifically for certain missing patterns, ignoring the modality combination inconsistency between training and testing phases. However, in real-world scenarios, the testing phase often encounters modal combinations that were not present during the training phase, which leads to insufficient generalization capabilities and unstable performance. In this paper, we introduce the problem of Incomplete Multimodal Sentiment Analysis with Unseen Modality Combinations (IMSAUMC), aiming to enhance model generalization for unseen modality combinations. To address this challenge, we propose the model named $\textbf{C}$ontrastive $\textbf{M}$ixed $\textbf{P}$rompt $\textbf{L}$earning ($\textsf{CMPL}$) for IMSAUMC. It introduces a label-guided contrastive feature learning mechanism to learn robust and discriminative cross-modal representations. Additionally, we design modality-combination prompts with a soft router to facilitate better learning of various modality combinations. Furthermore, we introduce three prompt contrastive learning strategies, which enable effective learning of prompts corresponding to unseen modality combinations, thereby significantly strengthening the model's generalization capabilities in diverse testing scenarios. Extensive experiments on three widely used datasets demonstrate that $\textsf{CMPL}$ achieves more than a 5% improvement in accuracy compared to state-of-the-art approaches.

### 中文一句话结论
本文提出对比混合提示学习（CMPL），首次解决训练与测试间模态组合不一致的不完整多模态情感分析问题，在三个数据集上准确率提升超5%。

### English TL;DR
This paper introduces Contrastive Mixed Prompt Learning (CMPL) to address the novel problem of incomplete multimodal sentiment analysis with unseen modality combinations, achieving over 5% accuracy improvement by using label-guided contrastive learning and prompt contrastive strategies to generalize to missing modality patterns not seen during training.

### 中文详细总结
现有不完整多模态情感分析方法通常假设训练与测试阶段缺失模态组合一致，但真实场景中测试常出现未见过模态组合，导致泛化不足。本文定义新问题IMSAUMC，并提出CMPL模型，包含三部分：（1）标签引导对比特征学习，利用标签相似性约束保持同类样本表征一致、异类样本距离成比例；（2）混合模态组合提示与软路由，动态选择提示以建模组合间关系；（3）三种提示对比学习策略（模态信息保留、跨组合互补、条件信息对齐），增强对未见组合的泛化。在CMU-MOSI、CMU-MOSEI、SIMS-V2三个基准数据集上，CMPL相比最先进方法准确率提升超5%。

### 方法 / 贡献
- **新问题定义**：首次提出IMSAUMC（训练与测试模态组合不一致的不完整多模态情感分析）。
- **标签引导对比学习**：保留标签语义结构，拉近同类样本表征、按标签差异比例推开异类样本。
- **混合提示机制**：为每种模态组合设计提示，通过软路由动态组合，建模组合间关联。
- **提示对比策略**：三类对比学习（信息保留、互补、对齐）强化对未见组合的泛化能力。
- **开源与数据**：未明确提及代码开源，但三个公开数据集验证有效性。

### 实验或数据
- **数据集**：CMU-MOSI、CMU-MOSEI、SIMS-V2（三种模态：文本、音频、视觉）。
- **设置**：训练仅使用部分模态组合，测试包含全部7种组合（含未见组合）。
- **结果**：CMPL在三个数据集上准确率超越现有方法（如TFR-Net、LNLN、HME等）5%以上。
- **消融**：未在摘要中详细说明，但模型组件（标签引导对比、提示对比）的贡献通过实验证。

### 值得关注点
- 问题设定新颖且贴合实际（数据缺失往往有结构而非随机）。
- 利用提示学习（Prompt Learning）增强对未见模态组合的适应，避免显式重建缺失模态。
- 标签引导对比学习在保持样本语义结构上优于传统无监督对比学习。
- 在三个不同规模数据集上一致提升，表明泛化性强。

### 局限性
- 论文未明确讨论局限性。当前方法聚焦于三种固定模态（文本、音频、视觉），扩展至更多模态时组合数将指数增长，提示设计复杂度可能升高。
- 依赖预训练LLM的文本嵌入特征，计算开销较大；音频/视觉特征也需预训练工具提取。
- 软路由和三种提示对比策略引入额外超参数（α, β），调优成本可能较高。

## 6. Projector Is All You Train

- Source: arxiv
- arXiv ID: 2608.19726
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.19726v1
- PDF: https://arxiv.org/pdf/2608.19726v1
- DOI: https://doi.org/10.48550/arXiv.2608.19726

### Authors

Nyx Iskandar, Saathvik Selvan, Slater Victoroff

### Abstract

The typical training process of a multimodal large language model (MLLM) involves adapting both the language model backbone and the projector between the backbone and a modality-specific encoder. We ask whether fine-tuning the backbone of an MLLM is necessary to adapt it to a new modality. Through experiments on 3D MLLMs, we find that training only the projector is sufficient to achieve strong multimodal performance relative to existing baseline models and our jointly trained MLLMs with the same encoder and backbone. We also show that joint training leads to undesirable drift in existing capabilities of the language model, which projector-only training avoids by definition. Furthermore, projector-only training has approximately twice the training sample throughput of joint training. We validate our findings across different language model backbones via 3D classification and captioning benchmarks as well as standard benchmarks evaluating language, vision, and spatial reasoning capabilities.

### 中文一句话结论
仅训练多模态大语言模型（MLLM）中的投影器，即可在三维任务上取得与联合训练（投影器+LoRA微调主干）相当的性能，同时避免语言模型能力漂移，并提高约两倍的训练吞吐量。

### English TL;DR
Training only the projector in a multimodal large language model (MLLM) is sufficient to achieve strong performance on 3D tasks, avoids undesirable drift in language model capabilities, and offers approximately double the training throughput compared to joint training of the projector and backbone.

### 中文详细总结
本文探究了多模态大语言模型（MLLM）是否必须微调语言模型主干来适配新模态。通过在三维MLLM上的实验，作者发现仅训练投影器（projector）即可达到与联合训练（投影器+LoRA微调主干）相当的三维分类与描述性能。联合训练会导致语言模型在语言、视觉和空间推理基准上的能力漂移，而仅训练投影器则天然避免这一问题。此外，仅训练投影器的训练吞吐量大约是联合训练的两倍。实验在多个语言模型骨干（Qwen3.5-4B、Qwen3.5-9B、Llama-3.1-8B-Instruct）上得到验证，使用了Point-BERT编码器和PointLLM数据集。评估包括三维分类（ModelNet40、Objaverse、OmniObject3D）和三维描述（Objaverse）基准，以及语言模型能力基准（如MMLU-Pro、WinoGrande、MMMU-Pro、BabyVision、ERQA、LingoQA）。

### 方法 / 贡献
**方法**：采用典型三维MLLM架构（冻结点云编码器Point-BERT + 可训练MLP投影器 + 冻结或LoRA微调的语言模型主干），对比两种训练模式：仅训练投影器（projector-only）和联合训练投影器与主干LoRA适配器（joint training）。训练使用混合的PointLLM-V2 Stage1+Stage2数据，以因果语言建模目标优化。

**贡献**：
1. 首次证明在三维MLLM中，仅训练投影器足以达到与联合训练竞争的性能，挑战了必须微调主干的主流做法。
2. 量化了联合训练导致的语言模型能力漂移（在语言、视觉、空间推理基准上出现退化）。
3. 实验表明仅训练投影器可带来约两倍的训练吞吐量，更节省计算资源。

### 实验或数据
- **数据集**：使用PointLLM-V2数据集的Objaverse子集（涵盖三维物体点云，8192点，6通道含RGB），包含简短描述和复杂指令（长描述、对话QA、部件指代）。
- **模型配置**：六个MLLM变体（三种语言模型骨干 × 两种训练模式），均在单张A100-80GB GPU上训练16小时（按相同墙钟时间匹配计算预算）。
- **三维评估**：
  - 零样本生成式分类：ModelNet40、Objaverse、OmniObject3D（使用LLM-as-a-Judge，GPT-5.6 Luna评分）。
  - 生成式描述：Objaverse（使用多视角图像，集成GPT-5.6 Luna、Claude Haiku 4.5、Gemini 3.5 Flash-Lite评分）。
- **语言模型能力评估**：
  - 语言：MMLU-Pro、WinoGrande。
  - 视觉：MMMU-Pro、BabyVision（仅对Qwen等视觉模型）。
  - 空间推理：ERQA、LingoQA。
  - 基线为原始未微调的语言模型。

### 值得关注点
1. **无需微调主干**：仅训练小参数量的投影器即可在三维任务上达到与联合训练相当的性能，且不损害语言模型原有能力。
2. **避免能力漂移**：联合训练（LoRA）在语言、视觉、空间推理基准上出现显著退化，而仅训练投影器天然避免此问题。
3. **训练效率提升**：因无需反向传播/更新大量主干参数，投影器训练的吞吐量约为联合训练的两倍，节省GPU时间。

### 局限性
1. 实验仅针对三维模态和Point-BERT编码器，未在其他模态（如图像、音频）或不同编码器上验证泛化性。
2. 使用的数据集仅限于Objaverse子集，未探索更大规模或更复杂数据（如Objaverse-XL全部数据）。
3. 训练时间固定为16小时墙钟时间，可能未能充分收敛至最优精度（尤其对联合训练），但论文已匹配实际计算预算。
4. 未探索不同投影器架构（如Q-Former、Cross-Attention等）对结果的影响。
5. 仅采用LoRA作为联合训练的适配方法，未尝试全量微调或Prompt Tuning等替代方案。

## 7. Are LLMs becoming similarly creative? Evidence from three years of models

- Source: arxiv
- arXiv ID: 2608.19437
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.19437v1
- PDF: https://arxiv.org/pdf/2608.19437v1
- DOI: https://doi.org/10.48550/arXiv.2608.19437

### Authors

Nirav Patel, Josiah Crossman, Eva Aggarwal, Emily Wenger

### Abstract

Many benchmarks track Large Language Model (LLM) performance on tasks with verifiable answers, but less is known about how LLM performance is evolving on open-ended tasks, where creativity, originality and diversity may matter as much as quality. As LLMs increasingly support human ideation and creative work, understanding trends in LLM performance on open-ended tasks is critical. This paper presents a preliminary analysis of LLM creative outputs spanning three years of model releases, examining model responses to Infinity-Chat100, a real-world collection of open-ended user queries, and the Alternate Uses Task, an established psychometric creativity assessment. Using sentence-embedding similarity, we examine trends in LLM responses to these prompts. Our findings show a statistically significant decrease in model output diversity over time, suggesting that LLM outputs may be converging in creative substance across models. If this trend persists, LLM-driven homogenization may progressively diminish human agency in human-AI co-creative work, demanding careful consideration of LLMs' role in the human creative process.

### 中文一句话结论
本研究通过对2023年至2026年间多个大语言模型在开放创意任务上的输出进行分析，发现跨模型输出在语义上显著趋同，多样性随时间下降。

### English TL;DR
This preliminary study analyzes LLM responses to open-ended creative prompts (Alternate Uses Task and Infinity-Chat100) across three years of model releases. Using embedding-based similarity, it finds a statistically significant decrease in cross-model output diversity over time, indicating increasing homogeneity in LLM creative outputs.

### 中文详细总结
论文针对大语言模型在开放创意任务上的表现趋势进行了初步分析。传统基准测试主要关注可验证答案的任务，但创意任务中多样性、原创性和质量同样重要。作者收集了2023年至2026年间来自12个模型提供商的68个模型（33个闭源和34个开源）的回应，使用两类提示集：标准心理测量创意测试“替代用途任务”(AUT)和真实用户查询集Infinity-Chat100。通过句子嵌入计算语义相似度，并采用线性回归分析跨模型输出的距离随时间的变化。结果表明，两类提示集上的跨模型输出余弦距离均显著下降（AUT更明显），说明创意输出在语义上趋于同质化。如果这一趋势持续，可能会削弱人机协作中人类的创造力与主动性。

### 方法 / 贡献
- **方法**：选取两类开放提示（AUT和Infinity-Chat100）；向68个模型（温度=1，top-p=1）生成回应；使用all-MiniLM-L6-v2嵌入计算余弦距离；通过家庭平衡重采样和线性回归分析跨模型距离的时间趋势。
- **贡献**：首次对LLM创意输出多样性进行纵向分析，建立了一个可复用的评估框架，揭示了模型输出语义收敛的实证证据。

### 实验或数据
- 使用AUT（10个物体共产生10种用途）和Infinity-Chat100（100个真实开放提示）作为提示集。
- 模型覆盖2023年3月至2026年7月，共68个模型（34开/33闭源）。
- 所有生成通过OpenRouter API，温度=1，top-p=1。
- 嵌入模型为all-MiniLM-L6-v2，回归采用1000次家庭平衡重采样，报告中位数斜率和95%区间。

### 值得关注点
- 发现跨模型语义距离随时间显著下降（AUT从约0.50降至<0.40），表明创意输出趋同。
- 趋同趋势不仅在标准创意测试中出现，在真实用户查询中也明显，具有生态效度。
- 研究为“AI创意悖论”（个体看似有创意但集体同质化）提供了纵向证据。
- 采用家庭平衡重采样减少模型家族不平衡的干扰。

### 局限性
- 分析为初步性质，仅覆盖有限模型和时间窗口，结论不能完全泛化。
- 模型发布日期作为时间代理变量，无法区分训练数据、架构、后训练方法等具体变化的影响。
- 嵌入相似性度量仅捕捉语义层面，未涉及更细粒度的创意质量（如原创性、实用性）。
- 未比较人类输出或控制提示分布的变化。

## 8. Rethinking the Evaluation and Optimization of LLM-Based Social Simulation

- Source: arxiv
- arXiv ID: 2608.19689
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.19689v1
- PDF: https://arxiv.org/pdf/2608.19689v1
- DOI: https://doi.org/10.48550/arXiv.2608.19689

### Authors

Pei Wang, Xu Chen, Ji-Rong Wen

### Abstract

LLM-based social simulation is a promising complement to traditional methods such as surveys and behavioral experiments. A core question is how to evaluate the fidelity of LLM-simulated human behavior and optimize LLMs toward it. Prevailing practice evaluates by accuracy, checking whether the model selects the single response observed from a human, and trains the LLM to reproduce this hard label. However, human behavior is inherently subjective: the same person in the same situation may reasonably act differently, so an observed response is only one draw from an underlying response distribution, rendering accuracy-based evaluation unreliable and hard-label training misleading. To address these problems, we first introduce the subjectivity coefficient, an entropy-based quantity distinguishing objective tasks such as coding from subjective ones such as social simulation, and use it to systematically analyze how accuracy-based evaluation and hard-label training fail as subjectivity grows. Based on the subjectivity coefficient, we propose Subjectivity-Adaptive soft-Label Training (SALT): it pools observed outputs from semantically nearby inputs into soft distributional labels, with an aggregation radius adapted to the estimated subjectivity of each input; in the near-objective limit the neighborhood shrinks, so SALT naturally falls back to standard single-label training. Moreover, since existing datasets record only single observed responses and cannot support distributional evaluation, we construct SUBJSIM, a benchmark of 19,300 contexts covering 193 annotators and 100 subjective questions. Since real-world data typically provide only a single observation per input, our experiments train models from single observed outputs while evaluating them against the full response distributions, verifying feasibility in realistic settings. Results on SUBJSIM demonstrate the advantages of our method.

### 中文一句话结论
本文指出基于准确率的评测和硬标签微调不适用于LLM社会模拟中固有的主观性行为，并提出了一种自适应主观性的软标签训练方法（SALT）及配套基准SUBJSIM，实验证明该方法能显著提升模拟的保真度。

### English TL;DR
This paper reveals that accuracy-based evaluation and hard-label training fail for LLM social simulation due to human behavioral subjectivity, introduces Subjectivity-Adaptive soft-Label Training (SALT) that pools semantically nearby responses into soft distributions, and constructs the SUBJSIM benchmark (19,300 instances with full distributional labels). Experiments show SALT reduces KL divergence by 77.6% and improves accuracy by 31.2% over standard SFT in high‑subjectivity settings.

### 中文详细总结
LLM社会模拟中，现有方法通常采用准确率评估和硬标签训练，即要求模型复现单次观测到的人类行为。然而，人类行为具有主观性和随机性：同一人在相同情境下可能做出不同选择，单次观测只是真实响应分布的一次采样。本文首先引入**主观性系数**（基于熵的度量），量化不同任务的主观程度，并严格证明了随着主观性增加，准确率评估和硬标签训练会严重偏离真实保真度目标。为解决这一问题，本文提出**主观性自适应软标签训练（SALT）**：对每个输入，聚合语义相近情境下的观测响应，形成软分布标签，聚合半径根据估计的主观性自适应调整；在近乎客观的任务中，邻域缩小，退化为标准单标签训练。由于现有数据集仅记录单次响应，无法支撑分布级评估，本文构建了**SUBJSIM基准**：包含193名标注者、100个主观问题、共19,300个上下文，每个标注者通过概率球分配提供完整的响应偏好分布。实验在训练阶段仅使用单次导出响应，测试阶段使用完整分布进行评估；以Qwen3-8B为骨干，SALT相比标准监督微调（SFT）将聚合KL散度降低了77.6%，在高主观性设定下准确率提升31.2%。

### 方法 / 贡献
1. **问题层面**：识别了社会模拟中基于准确率的评估和硬标签训练的根本缺陷，并通过主观性系数进行了理论分析。
2. **方法层面**：提出SALT（主观性自适应软标签训练），利用语义邻近输入的观测响应构建软分布标签，聚合半径随估计的主观性自动调节；在客观任务中自然回归标准训练。
3. **数据层面**：构建SUBJSIM基准（19,300个上下文、完整的人类响应分布），使训练仅基于单次观测、评估基于分布成为可行。

### 实验或数据
- **数据集**：SUBJSIM，包含193名标注者对100个主观问题的回答，共19,300个标注者–问题对。每个对均提供通过概率球分配得到的响应偏好分布。
- **实验设置**：训练阶段模型仅从每个上下文的单次观测硬标签学习，测试阶段使用完整分布评估保真度。骨干模型为Qwen3-8B。
- **主要结果**：SALT相比标准SFT，聚合KL散度降低77.6%；在高主观性设定下，准确率提升31.2%。

### 值得关注点
- 首次系统论证了社会模拟中主观性对准确率评估和硬标签训练的负面影响，并引入熵基主观性系数进行量化。
- SALT巧妙地将主观性估计与自适应聚合半径结合，在客观任务中可自然回退，无需切换训练范式。
- SUBJSIM基准提供了大规模、带完整分布的人类响应数据，为分布级评估和训练提供了实验基础。

### 局限性
- 摘要中未明确讨论局限性，但方法依赖语义相似度计算和主观性估计，其质量可能受限于表示学习能力；此外，基准仅覆盖调查问卷类问题，对其他类型的社会模拟（如开放域对话）的适用性尚待验证。

## 9. Natural Language Code Retrieval for 1C:Enterprise: An Open Benchmark and Efficient Bi-Encoder

- Source: arxiv
- arXiv ID: 2608.19957
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.19957v1
- PDF: https://arxiv.org/pdf/2608.19957v1
- DOI: https://doi.org/10.48550/arXiv.2608.19957

### Authors

Konstantin Chesnokov, Chingiz Mingazov

### Abstract

Natural language code retrieval is a rapidly evolving task in computer science. However, the 1C:Enterprise ecosystem combines Russian syntax with highly domain-specific terminology, for which open datasets and specialized models have been virtually non-existent. We present a comprehensive pipeline for 1C code retrieval: an open benchmark of 3,413 real-world, PII-scrubbed query-code pairs, a reproducible evaluation harness, and a specialized bi-encoder. To overcome scarce labeled data, we fine-tune on 784,057 synthetic triplets generated by google/gemma-4-26B-A4B-it from public code repositories, using Matryoshka Representation Learning (MRL) and a privacy-aware tokenizer. Because the benchmark subsets differ in size, we report balanced-subset macro, query-weighted micro, and forum-only results. Our model reaches 0.5992 balanced macro nDCG@10, 0.5044 micro, and 0.4617 on forum, versus 0.4932 macro for the baseline architecture and 0.5404 for google/embeddinggemma-300m. Removing every benchmark example flagged by the conservative exact/13-gram overlap audit leaves 0.6011 balanced macro (0.5010 micro), indicating that detected train-benchmark overlap does not explain the headline result. MRL truncation to 256 dimensions preserves 99.9% of retrieval quality while reducing dense-index storage and exact similarity arithmetic by a factor of three.

### 中文一句话结论
本研究发布了首个面向1C:Enterprise俄语代码检索的开源基准测试与领域适配双编码器模型，有效提升了该垂直领域代码检索性能。

### English TL;DR
This paper introduces the first open benchmark and a domain-adapted bi-encoder for retrieving 1C:Enterprise code from natural language queries, achieving significant retrieval improvements over general multilingual embeddings while maintaining efficiency through Matryoshka Representation Learning.

### 中文详细总结
1C:Enterprise是俄语企业软件生态，其代码（BSL与1C查询）具有混合俄语语法与高度领域特定术语的特点。此前，该领域缺乏开放的数据集与专用检索模型。本工作构建了一套完整的开源管线，包含：
- **1C-Ebench基准测试**：包含3,413个经过真实论坛与FastCode社区数据清洗、脱敏后的查询-代码对。
- **1C-RB评估框架**：可复现的评估脚本，支持密集检索与BM25基线。
- **USER2-1C-code领域模型**：基于俄语通用嵌入模型USER2-base微调的双编码器，使用Matryoshka表示学习（MRL）与隐私感知分词器。
- **1C-Code-Train训练集**：通过google/gemma-4-26B-A4B-it模型从公开代码仓库生成的784,057个合成三元组。

模型在平衡子集宏平均nDCG@10达到0.5992，超过基线架构（0.4932）与gemma-300m（0.5404）。训练-基准数据重叠审计表明，检测到的重叠不能解释主要结果。MRL截断至256维时，检索质量保留99.9%，同时密集索引存储与精确相似度计算量减少三分之二。

### 方法 / 贡献
- **数据构建**：从1C论坛与FastCode社区收集原始数据，应用精度优先过滤器、精确去重与基于规则的人工智能PII脱敏，生成开源基准测试。
- **合成数据生成**：使用Gemma-4-26B模型从公开GitHub代码仓库生成合成查询-正例-负例三元组，弥补标注数据稀缺。
- **模型微调**：基于USER2-base（DeEPVK的俄语通用句子编码器）进行微调，采用缓存多负排序损失（Cached Multiple Negatives Ranking Loss）与Matryoshka表示学习。
- **评估协议**：由于基准子集（forum与fastcode）规模不同，报告平衡子集宏平均（macro）、查询加权微平均（micro）以及forum单独结果。
- **重叠审计**：执行精确匹配与13-gram重叠审计，确认无完全匹配的查询-代码对；移除所有被标记的样本后，模型性能仍保持，说明重叠不主导结果。

### 实验或数据
- **基准测试**：3,413个查询-代码对，包含forum（2,883对，84.5%）与fastcode（530对，15.5%）两个子集。
- **训练集**：784,057个合成三元组（查询、正例、负例），经PII脱敏。
- **主要结果**：
  - 平衡宏平均nDCG@10：0.5992
  - 查询加权微平均nDCG@10：0.5044
  - forum子集nDCG@10：0.4617
- **对比基线**：
  - 基线架构（USER2-base）：0.4932 macro
  - google/embeddinggemma-300m：0.5404 macro
- **MRL截断**：256维保留99.9%检索质量，索引存储与计算量减少3倍。
- **重叠审计后结果**：移除所有被标记样本后，平衡宏平均0.6011，微平均0.5010，表明重叠不影响主要结论。

### 值得关注点
- **首次开源1C代码检索基准**：填补了该垂直领域开放数据集的空白，促进后续研究。
- **合成数据策略与MRL**：利用大模型合成训练数据，结合Matryoshka表示学习实现高效紧凑嵌入，兼顾性能与效率。
- **严格的评估与审计**：采用宏平均与微平均双重指标，并公开训练-基准数据重叠审计，增强结果可信度。
- **实际应用价值**：模型与所有资源（基准、框架、模型、训练集）均在Hugging Face与GitHub开源，可直接用于1C企业软件开发与检索增强生成。

### 局限性
- **单标签设置**：每对查询只标注一个正例代码，会因未标注的其他相关代码排名高于正例而低估真实检索质量。
- **PII脱敏风险**：脱敏工具基于规则，保守且主要覆盖常见表面形式，未进行正式的去标识化保证，残余PII在脱敏前被删除。
- **合成数据质量**：使用LLM-as-a-Judge筛选合成查询，但该方法在专业领域与专家一致性未经验证，合成数据质量可能影响模型上限。
- **未提供隐私审计详细信息**：未报告PII检测的精确率/召回率或残余人工审计，脱敏过程的完整性无法验证。
- **评估范围有限**：仅针对1C:Enterprise语言，尚未验证在其他俄语领域或更广泛代码检索场景的泛化能力。

## 10. Robust Incomplete Multimodal Sentiment Analysis via Iterative Proxy Correction

- Source: arxiv
- arXiv ID: 2608.19971
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.19971v1
- PDF: https://arxiv.org/pdf/2608.19971v1
- DOI: https://doi.org/10.48550/arXiv.2608.19971

### Authors

Zhifa Geng, Subin Huang, Hao Guo, Junjie Chen, Sanmin Liu, Chao Kong

### Abstract

Multimodal sentiment analysis aims to infer affective states by integrating language, visual, and acoustic cues. However, real-world multimodal inputs are often incomplete or corrupted, which can weaken cross-modal complementarity and introduce misleading information into downstream fusion. Existing proxy-based methods for incomplete MSA commonly rely on one-shot proxy construction to compensate for degraded language information, but the generated proxy may be coarse or unreliable at initialization. Prematurely injecting such a proxy into multimodal reasoning can propagate initial errors and compromise sentiment prediction. To address this limitation, we propose an iterative proxy correction framework for robust incomplete MSA. Our method constructs a language-oriented proxy from non-language modalities and progressively refines it under multimodal context through gated residual correction. The corrected proxy is then adaptively fused with the observed language representation according to an estimated language reliability score, allowing the model to balance proxy-based compensation and trustworthy linguistic evidence. In addition, we introduce a stage-wise latent correction objective that uses the complete language representation as a training-time semantic anchor to stabilize the proxy refinement trajectory. Extensive experiments on MOSI, MOSEI, and SIMS under diverse missing-modality settings demonstrate that the proposed framework consistently outperforms competitive baselines and achieves robust sentiment prediction under incomplete inputs.

### 中文一句话结论
本文提出了一种通过迭代代理校正逐步优化语言导向代理表示的方法，从而在不完整多模态情感分析中显著提升鲁棒性。

### English TL;DR
This paper proposes an iterative proxy correction framework that progressively refines a language-oriented proxy from non-language modalities under multimodal context, adaptively fuses it with observed language based on reliability, and consistently outperforms baselines on MOSI, MOSEI, and SIMS under incomplete inputs.

### 中文详细总结
多模态情感分析常因实际输入不完整（如噪声、传感器故障）而性能下降。现有基于代理的方法通常一次性构造代理表示，但其初始质量粗糙，直接注入多模态推理会传播误差。本文提出迭代代理校正框架：先用视觉和声学特征初始化语言代理，再通过门控残差校正逐步优化；之后按语言可靠度分数自适应融合校正代理与原始语言表示；训练时引入分阶段潜在校正损失，以完整语言表示为锚点稳定代理优化轨迹。实验表明方法在多种缺失设置下均优于现有方法。

### 方法 / 贡献
1. 识别一次性代理构造的误差传播风险，提出迭代代理校正机制。
2. 设计门控残差校正模块，在多模态上下文下逐步精炼代理表示。
3. 引入分阶段潜在校正损失，以完整语言表示为训练时语义锚点。
4. 提出语言可靠度估计分数，自适应融合代理与观测语言表示。

### 实验或数据
实验在 MOSI、MOSEI 和 SIMS 三个多模态情感数据集上进行，测试多种缺失模态设置（如语言缺失、视觉/声学缺失等）。与 MISA、Self-MM、MMIM、CENET、TETFN、ALMT、LNLN 等基线对比，本文方法在大多数指标（如 Acc-2、F1、MAE、Corr）上达到最优或次优结果。

### 值得关注点
- 代理校正过程是迭代的，而非一次性构造，这显著降低了初始误差传播。
- 语言可靠度分数使模型能自适应平衡代理补偿与原始语言证据，更具鲁棒性。
- 分阶段损失使用完整语言表示作为锚点，但仅在训练时使用，不影响推理。

### 局限性
- 本文未报告 SIMS 数据集的具体数值结果，只提及实验涵盖该数据集。
- 未讨论代理校正步数 T 对性能的影响或敏感性分析。
- 未比较在极端缺失（如所有模态均缺失）场景下的表现。
- 方法依赖训练时完整语言表示作为锚点，在完全无标注完整数据时可能受限。

## Processing Notes

- Duplicate papers skipped: 0