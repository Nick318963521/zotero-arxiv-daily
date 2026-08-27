# Daily arXiv - 2026-08-27

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-27T02:50:15
- Paper count: 10

## 1. SENSESHIFT: Continuous Sentiment-Controlled Text Generation via Encoder-based Mask Infilling

- Source: arxiv
- arXiv ID: 2608.24304
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.24304v1
- PDF: https://arxiv.org/pdf/2608.24304v1
- DOI: https://doi.org/10.48550/arXiv.2608.24304

### Authors

Shahed Masoudian, Markus Frohmann, Emmanouil Karystinaios, Navid Rekabsaz, Markus Schedl

### Abstract

Recent controllable text generation (CTG) for sentiment control has largely focused on decoder-based large language models, making causal attention the dominant paradigm. While effective for fluent generation, these models still struggle to satisfy complex constraints and follow fine-grained sentiment signals specified by users. Existing sentiment-aware CTG methods typically simplify the problem by treating sentiment either as a coarse categorical label (e.g., positive or negative) or as a single fine-grained control signal applied to an entire document. Consequently, more challenging settings such as sentence-level sentiment control within long-form text remain underexplored. To address these limitations, we introduce SenseShift , an encoder-based framework for fine-grained sentence-level CTG. Unlike standard decoder architectures, SenseShift leverages bidirectional attention, quantized sentiment signals, and iterative mask infilling to generate local sentences conditioned on target sentiment intensity. Empirical evaluations on story and review generation demonstrate that SenseShift achieves stronger sentiment controllability while maintaining text quality and robustness to out-of-domain generation compared to larger decoder-based baselines.

### 中文一句话结论
SenseShift 是一个基于编码器的框架，通过双向注意力、量化情感信号和迭代掩码填充，实现了细粒度的句子级情感控制，在文本生成中比大型解码器基线模型具有更强的情感控制能力。

### English TL;DR
SenseShift is an encoder-based framework that achieves fine-grained sentence-level sentiment control in text generation by leveraging bidirectional attention, quantized sentiment signals, and iterative mask infilling, outperforming larger decoder-based baselines.

### 中文详细总结
现有的可控文本生成方法主要依赖基于解码器的大型语言模型，使用因果注意力机制。这些模型在处理复杂约束和细粒度情感信号时表现不佳，通常将情感简化为粗粒度标签（如正面或负面），或者将单一情感信号应用于整个文档。因此，句子级情感控制（尤其是在长文本中）仍然未被充分探索。SenseShift 提出了一种基于编码器的框架，利用双向注意力、量化情感信号和迭代掩码填充，在故事和评论生成任务中实现了更强的句子级情感控制，同时保持了文本质量和领域外生成的鲁棒性。与更大的解码器基线相比，SenseShift 在情感控制方面表现更优。

### 方法 / 贡献
1. **自动情感信号构建与量化**：使用 VADER 对每个句子提取情感分数（范围 [-1, 1]），并通过步长 δ=0.1 进行量化，将每个量化值映射为唯一的情感标记，放置在对应句子开头。
2. **控制感知的 MLM 微调**：在掩码语言模型训练中，情感标记永不掩码，作为持久条件信号；掩码率提高到 40% 以增强对缺失内容的预测能力。
3. **迭代掩码填充**：在推理时，将目标句子完全替换为掩码标记，从第一个掩码位置开始逐步预测，使用束搜索（beam search）和多样性惩罚生成连贯输出。

### 实验或数据
- **模型**：基于 ModernBERT 的两种规模：base（149M 参数）和 large（395M 参数），均远小于解码器基线模型。
- **数据集**：TinyStories（约450万短篇故事）和 Yelp Reviews（约30万评论）。
- **基线**：包括提示（prompting）、激活引导（activation steering）和微调方法。
- **评估**：在域内和域外（OOD）场景下进行情感控制能力、文本质量和鲁棒性评估；人类评估显示 SenseShift 在上下文契合度和情感对齐方面更受青睐。

### 值得关注点
- 利用编码器的双向注意力实现上下文感知的句子级情感控制，与解码器的单向生成形成对比。
- 量化情感信号（步长 0.1）支持连续情感强度控制，而非仅粗粒度标签。
- 模型参数远小于解码器基线但表现更优，显示出高效率和竞争力。
- 开源代码和模型检查点已提供，便于复现和应用。

### 局限性
摘要和内容未明确提及实验的具体局限性，但可从方法推断：依赖 VADER 进行情感量化可能受其准确性限制；掩码填充的最大长度设置（30 个标记）可能不适合更长句子；迭代生成过程可能增加推理时间；情感控制仅基于 VADER 分数，未探索其他情感模型。此外，未提及对多语言或更复杂情感类型的支持。

## 2. ADE: Agentic Data Evolution Framework for Human-Centered Objectives

- Source: arxiv
- arXiv ID: 2608.23719
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.23719v1
- PDF: https://arxiv.org/pdf/2608.23719v1
- DOI: https://doi.org/10.48550/arXiv.2608.23719

### Authors

Yang Yu, Yilin Jiang, Zexuan Fei, Yiming Luo, Xingkai Song, Kaiyi Huang, Aimin Zhou, Xin Lin, Fei Tan

### Abstract

Aligning large language models to human-centered objectives is difficult when targets are non-executable and context-dependent, limiting reliable verification and scalable supervision. Although synthetic data expands coverage, weak verification shifts the bottleneck from generation to selection. Noisy signals destabilize iterative refinement and can cause silent regressions. We propose Agentic Data Evolution (ADE), a data-centric framework that organizes synthetic supervision as evolving data snapshots. ADE improves data snapshots through a closed-loop Observation-Variation-Selection (OVS) procedure, where a steady-state admission mechanism acts as a quality ratchet that conservatively gates updates for sustained cross-round improvement. We validate these improvements through complementary intrinsic trend tracking and extrinsic post-training evaluation. On DEV300, ADE raises the intrinsic win rate from 50% to 75.81% and the extrinsic win rate from 55.20% to 68.86%, consistent performance gains across diverse benchmarks. Blind expert evaluation further confirms this, with a 66.11% preference for evolved answers. These gains extend across post-training methods, model scales, and tasks beyond the target weakly verifiable educational objectives. Resources are available at https://github.com/ZeroLoss-Lab/Agentic-Data-Evolution.

### 中文一句话结论
本文提出一种名为ADE（代理式数据演化）的数据驱动框架，通过观察-变异-选择（OVS）的闭环流程和稳态准入机制，在弱监督条件下实现合成数据集的非退化迭代改进，从而有效提升大语言模型在面向人类中心目标（如价值观、情感支持、创造性）上的对齐效果。

### English TL;DR
Agentic Data Evolution (ADE) is a data-centric framework that iteratively refines synthetic supervision data for weakly verifiable human-centered objectives. It uses an Observation-Variation-Selection (OVS) loop with a steady-state admission mechanism to prevent regressions, achieving consistent improvements in intrinsic (win rate from 50% to 75.81%) and extrinsic (win rate from 55.20% to 68.86%) evaluations on the DEV300 benchmark, as well as human expert preference (66.11%).

### 中文详细总结
本文针对大语言模型在面向人类中心目标（如教育中的价值观引导、情感支持、创造性培养）时面临的弱监督问题（目标不可执行、依赖上下文、缺乏可靠验证信号），提出了一种名为**代理式数据演化（ADE）**的数据驱动框架。该框架将合成监督数据的构建视为一个持续演化的过程，而非一次性生成问题。ADE的核心是**观察-变异-选择（OVS）**闭环协议：观察阶段通过路由维度分解和因子化批判生成目标导向的批评；变异阶段通过保守和激进的两种提议者生成候选修订；选择阶段通过比较选择和准入判断，仅当候选答案在比较证据支持且不引入退化时才被采纳，否则保留父代答案。这种稳态准入机制起到了质量棘轮的作用，确保跨轮次的持续改进。实验在两个关键基准上进行验证：在DEV300上，ADE使内在胜率从50%提升至75.81%，外延胜率从55.20%提升至68.86%；在教育相关基准（Edu-Values、EduBench）上，一致优于单轮方法（如Best-of-N、Self-Refine）。盲法专家评估中，66.11%的专家偏好演化后的答案。此外，ADE的增益在不同后训练方法、模型规模和任务上均表现一致，且不限于最初的教育目标。资源已开源。

### 方法 / 贡献
- **方法**：提出ADE框架，将弱监督下的数据构建形式化为连续的快照演化。通过OVS协议实现：观察阶段使用路由和因子化批判生成评估证据；变异阶段使用保守和激进两种提议者生成候选修订，并利用失败反馈避免重复错误；选择阶段通过比较选择和准入判断，实现稳态精英保留，防止非退化更新。
- **贡献**：
  1. 将弱监督数据构建问题重新定义为数据演化问题，并设计了相应的非退化迭代协议。
  2. 提出稳态准入机制作为质量棘轮，在不依赖强验证信号的情况下保证跨轮次改进。
  3. 通过内在（答案级）、外延（后训练模型行为）和人工校准（专家偏好）三种互补验证方式，全面评估数据质量。
  4. 在多个基准和任务上（包括教育目标及其他弱监督任务）验证了方法的有效性，并展示了其跨模型和后训练方法的泛化能力。

### 实验或数据
- **实验设置**：主要评估在DEV300基准（包含价值观、情感支持、创造性三个维度）上进行内在胜率（50%→75.81%）和外延胜率（55.20%→68.86%）测试。同时在Edu-Values和EduBench两个教育相关基准上评估后训练模型的表现，与单轮方法（Best-of-N、SDFT、Self-Refine）对比。
- **数据**：初始数据集通过概念-场景-主题流水线构建，包含教育领域的问答对。完整数据和代码已开源（https://github.com/ZeroLoss-Lab/Agentic-Data-Evolution）。
- **结果**：ADE在所有基准和维度上均优于单轮方法，且增益在模型规模（如7B、13B）、后训练方法（如DPO、PPO）和任务类型（如教育、编程）上一致。盲法专家评估中，66.11%的专家偏好演化后的答案。
- **其他**：补充实验表明ADE对非目标弱监督任务（如创造性写作）也有提升效果。

### 值得关注点
- **弱监督场景的创新**：针对非可执行、依赖上下文的脆弱验证目标，提出了数据演化的新范式，而非依赖强验证信号。
- **稳态准入机制**：通过比较选择和准入判断的分离，有效防止了迭代中的无声退化，实现了质量棘轮效果。
- **多维度验证**：同时使用内在（答案级）、外延（模型行为）和人工（专家评估）三种方式，避免了单一评判源的偏差。
- **跨任务泛化**：方法不仅适用于教育目标，在超出最初目标的弱监督任务上同样有效，显示了框架的通用性。
- **开源代码**：提供完整实现，便于复现和扩展。

### 局限性
- 根据提供的摘要和正文预览，本文未明确讨论框架的局限性。但基于方法设计，可推测以下潜在问题：
  - 依赖大语言模型作为评判者和提议者，其自身偏见和错误可能影响演化方向。
  - 稳态准入机制可能过度保守，在某些情况下可能限制探索性改进。
  - 多轮迭代需要多次大语言模型调用，计算成本较高。
  - 框架的有效性可能在目标定义更模糊或维度更复杂的人类中心任务上仍需进一步验证。

## 3. Dataset Scarcity Limits Robust Evaluation of Multilingual Embedding Models: A Case Study of Slavic Languages

- Source: arxiv
- arXiv ID: 2608.24477
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.24477v1
- PDF: https://arxiv.org/pdf/2608.24477v1
- DOI: https://doi.org/10.48550/arXiv.2608.24477

### Authors

Ana Gjorgjevikj, Barbara Koroušić Seljak, Tome Eftimov

### Abstract

Multilingual text embedding models enable cross-lingual transfer of knowledge across a wide range of NLP tasks, but their evaluation remains highly uneven across high-, mid- and low-resource languages. In this paper, we propose a two-dimensional framework, specifically tailored for analyzing multilingual embedding benchmarks under dataset scarcity, and apply it on the Slavic-language subset of the MTEB benchmark. The framework distinguishes between task-specific and cross-task evaluation, while jointly analyzing three complementary aspects: (1) ranking robustness, (2) model consistency, and (3) evidence strength. At the task-specific level, we evaluate the stability of model rankings under changes in ranking methodology and benchmark dataset composition. At the cross-task level, we assess the ability of models to generalize across diverse tasks within a language. To quantify the reliability of benchmark conclusions, we introduce an Evidence Strength Score that accounts for dataset availability, diversity, and robustness assessability. Our analysis reveals severe benchmark sparsity, with many Slavic language-task pairs relying on a single dataset or highly correlated benchmark collections, limiting the ability to draw robust conclusions. The cross-task analysis reveals a small group of highly transferable models, most notably llama-embed-nemotron-8b, multilingual-e5-large-instruct, and Qwen3-Embedding variants, that consistently perform well across Slavic languages and tasks. Overall, the results demonstrate that benchmark rankings and robustness conclusions must be interpreted jointly with certain notation of their evidence strength and highlight benchmark scarcity as a major obstacle to trustworthy multilingual evaluation.

### 中文一句话结论
本文提出一个二维评估框架，用于分析数据稀缺下的多语言嵌入模型鲁棒性，揭示斯拉夫语MTEB基准因数据集稀疏和冗余而严重限制了评估的可靠性，并识别出少数跨语言和任务表现稳定的模型。

### English TL;DR
This paper proposes a two-dimensional framework that jointly analyzes ranking robustness, model consistency, and evidence strength to reveal that dataset scarcity and redundancy in Slavic-language benchmarks severely limit the reliability of multilingual embedding model evaluation, while identifying a few large models that consistently perform well across languages and tasks.

### 中文详细总结
该研究针对多语言文本嵌入模型评估在低资源语言上的不平衡问题，提出一个专门用于分析数据稀缺条件下基准鲁棒性的二维框架。框架区分“任务特定评估”和“跨任务评估”两个范围，并联合分析三个互补方面：（1）排名鲁棒性（排序稳定性）、（2）模型一致性（top-k 迁移一致性）和（3）证据强度。在任务特定层面，评估模型排名在不同排名方法和基准数据集组合下的稳定性；在跨任务层面，评估模型在同一语言内不同任务间的泛化能力。为了量化基准结论的可靠性，论文引入证据强度评分（ESS），综合考虑数据集可用性、多样性（考虑冗余性）和鲁棒性可评估性。将该框架应用于MTEB的斯拉夫语子集，发现严重的基准稀疏性：许多语言-任务对仅依赖单一数据集或高度相关的基准集合，限制了得出稳健结论的能力。跨任务分析显示一小部分高迁移性模型，尤其是llama-embed-nemotron-8b、multilingual-e5-large-instruct和Qwen3-Embedding变体，在斯拉夫语和任务中表现一致。总体而言，基准排名和鲁棒性结论必须结合其证据强度来解释，并且基准稀缺性是阻碍可信多语言评估的主要障碍。

### 方法 / 贡献
论文提出一个二维分析框架，包含任务特定评估（评估排名稳定性）和跨任务评估（评估top-k迁移一致性）。在每个范围内，联合分析三个方面：排名稳定性（聚合稳定性和组合稳定性）、top-k迁移一致性（量化模型在top-k集合内的位置）和证据强度（ESS，为本文核心贡献）。ESS通过结合数据集可用性、有效数据集多样性（去除高相关冗余数据集）和稳定性可评估性，量化基准证据的可靠性。框架还定义了五个定性证据等级，基于数据集数量和去冗余后的簇数量来划分。该方法应用于MTEB的斯拉夫语子集。

### 实验或数据
实验基于MTEB基准的斯拉夫语子集。分析未提及具体实验设置（如模型数量、数据集大小或训练过程），但揭示了严重的数据稀疏性：许多语言-任务对仅依赖单一或高度相关的数据集。证据等级分析显示，不同语言-任务对的证据等级分布不均匀。跨任务分析发现少数模型（如llama-embed-nemotron-8b等）在斯拉夫语中表现稳定。

### 值得关注点
- 创新性地引入证据强度评分（ESS），区分了“表面稳定”和“真正稳健”的基准结论
- 框架联合分析排名稳定性、模型一致性和证据强度，提供了比传统平均排名更全面的评估视角
- 识别出少量在斯拉夫语和任务中表现一致的高迁移性模型
- 明确指出了基准稀缺性（数据集稀疏和冗余）对可信多语言评估的根本性限制

### 局限性
- 研究仅局限于MTEB基准的斯拉夫语子集，未推广到其他低资源语言族或更大范围的多语言基准（如MMTEB）
- 未提供具体实验数据（如模型数量、数据集大小或详细的性能对比表）
- 证据强度评分（ESS）的设计依赖于数据集间的相关性阈值选择，可能影响结果稳定性
- 跨任务分析不支持排名稳定性评估，因为不同任务的目标和指标不可直接比较
- 未探讨如何缓解基准稀缺性本身（如数据增强或迁移学习策略）

## 4. Preference Data Selection for Mitigating the Alignment Tax in Large Language Models

- Source: arxiv
- arXiv ID: 2608.24192
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.24192v1
- PDF: https://arxiv.org/pdf/2608.24192v1
- DOI: https://doi.org/10.48550/arXiv.2608.24192

### Authors

Minsu Kim, Jianxun Lian, Xing Xie, Steven Euijong Whang

### Abstract

Aligning large language models to human preferences is crucial for real-world deployment but frequently incurs an alignment tax, leading to the catastrophic forgetting of pre-trained general capabilities. While previous works primarily frame this problem as an optimization or architectural challenge, the inherent characteristics of preference data that drive this degradation remain largely underexplored. In this paper, we propose BALIGN, a balanced data selection strategy that explicitly mitigates catastrophic forgetting while optimizing alignment efficacy. Through theoretical and empirical analyses of the preference optimization gradient, we identify three key data-centric features that dictate parameter drift: the reference model's log-probability margin, the token length difference between chosen and rejected responses, and the TF-IDF similarity to general capability corpora. By aggregating these orthogonal features into a unified composite risk score, BALIGN systematically filters out high-risk preference samples that disrupt intrinsic model parameters or provide minimal alignment utility. Extensive experiments on standard human preference datasets demonstrate that BALIGN strongly preserves foundational capabilities without compromising alignment gains, consistently achieving the optimal Pareto frontier with minimal computational overhead.

### 中文一句话结论
本文提出一种名为 BALIGN 的数据选择策略，通过基于三个特征（参考模型对数概率边际、回答长度差、TF-IDF 相似度）过滤高风险偏好样本，从而在保持大语言模型对齐性能的同时减轻对齐税（即遗忘预训练通用能力）。

### English TL;DR
This paper proposes BALIGN, a balanced data selection strategy that mitigates the alignment tax (catastrophic forgetting) in LLM alignment by filtering out high-risk preference samples based on three orthogonal features—reference model log-probability margin, token length difference, and TF-IDF similarity to general capability corpora—to preserve pre-trained general capabilities while maintaining alignment performance.

### 中文详细总结
对齐大语言模型到人类偏好对于实际部署至关重要，但经常导致“对齐税”，即模型遗忘预训练的通用能力（灾难性遗忘）。以往工作主要将此问题视为优化或架构挑战，而忽略了偏好数据本身导致退化的特性。本文通过理论分析和实证研究偏好优化梯度，识别出三个关键的与数据相关的特征，它们决定了参数偏移：参考模型的对数概率边际、选定与拒绝回答之间的长度差（词元数差异），以及样本与通用能力语料库的 TF-IDF 相似度。作者将这三个正交特征聚合为一个统一的复合风险分数，并据此系统地过滤掉那些扰乱模型内在参数或提供极少对齐效用的高风险偏好样本。通过在标准人类偏好数据集上的大量实验，BALIGN 在不影响对齐效果的前提下，显著保留了模型的通用能力，并始终以最小的计算开销达到最优帕累托前沿。

### 方法 / 贡献
1.  **识别关键特征**：首次从数据角度分析，识别出三个影响稳定性和可塑性平衡的正交特征：参考模型下的对数概率边际、选定与拒绝回答的令牌长度差、以及样本与通用语料库的 TF-IDF 相似度。
2.  **提出BALIGN策略**：基于这三个特征构建统一的复合风险分数，用于过滤高风险样本，从而在偏好数据选择阶段直接减轻灾难性遗忘。
3.  **验证有效性**：实证表明该方法能有效保留模型在通用知识、推理、代码和数学等多领域的通用能力，同时不牺牲对齐性能。

### 实验或数据
论文在标准人类偏好数据集上进行了广泛实验。实验评估了模型在多种通用能力基准（如知识、指令遵循、推理、代码和数学）上的性能，以及对齐质量（例如在保留的偏好测试集上的准确率）。结果显示，BALIGN 持续实现了最优的帕累托前沿，即在保持同等对齐增益的情况下，遗忘最少。

### 值得关注点
1.  **数据为中心的视角**：不同于以往侧重优化或架构的方法，BALIGN 从“数据本身”出发，将问题归结为数据选择，方法简单且高效。
2.  **特征正交性**：提出的三个特征分别从稳定性（边际、长度差）和可塑性（相似度）两个维度评估样本风险，设计思路清晰。
3.  **实践价值**：该方法无需改变模型结构或优化流程，仅通过预处理训练数据即可缓解对齐税，计算开销极小，易于实际部署。

### 局限性
摘要和提供的预览内容主要聚焦于方法有效性和理论分析，**未提及具体的实验设置、数据集名称或与其他基线方法的详细比较结果**。此外，以下潜在局限性需结合全文确认：
1.  **鲁棒性**：三个风险分数的阈值设定（例如，如何界定“高风险”）可能依赖于特定数据集，其泛化能力需进一步验证。
2.  **理论边界**：虽然分析了特征与参数漂移的关系，但对复合风险分数的聚合策略（如加权方式）的理论最优性可能缺乏证明。
3.  **场景限制**：实验主要基于离线偏好数据集（DPO），该方法在在线或众包反馈场景下的表现未知。

## 5. What Does Prompt Learning Change? -A Natural-Language Concept Analysis of Vision-Language Models

- Source: arxiv
- arXiv ID: 2608.24142
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.24142v1
- PDF: https://arxiv.org/pdf/2608.24142v1
- DOI: https://doi.org/10.48550/arXiv.2608.24142

### Authors

Ryo Kamiya, Hiroshi Kera, Kazuhiko Kawamoto

### Abstract

Prompt learning adapts vision-language models such as CLIP by optimizing continuous prompt vectors, but the learned prompts are difficult to interpret in natural language. We present PromptSpLiCE, a post-hoc method that expresses each class-conditioned text embedding as a sparse combination of concepts from a fixed natural-language dictionary. Using the same dictionary before and after prompt learning allows us to compare changes in their concept profiles. We evaluate PromptSpLiCE on CoOp, a representative prompt-learning method, across 11 image-classification datasets. The concept profiles change substantially: on average, only 1.6 of the initial top-10 concepts remain in the top 10 after learning. Across datasets, profile change is positively associated with accuracy gain. We also derive a local gradient expression that provides geometric intuition for why image-aligned concept directions distinct from the current prompt can have greater loss sensitivity.

### 中文一句话结论
PromptSpLiCE 通过将提示学习前后的 CLIP 文本嵌入分解为固定自然语言概念词典上的稀疏组合，发现概念分布发生显著重组，且重组程度与分类准确率提升呈正相关。

### English TL;DR
PromptSpLiCE decomposes vision-language model prompts into natural-language concept profiles, revealing that prompt learning substantially reorganizes these profiles and that the degree of reorganization correlates with accuracy gains across datasets.

### 中文详细总结
Prompt learning（如 CoOp）通过优化连续提示向量来适配 CLIP 等视觉-语言模型，但学到的提示难以用自然语言解释。本文提出 PromptSpLiCE，一种事后（post-hoc）分析方法，将每个类别的文本嵌入表示为固定自然语言概念词典中概念的稀疏非负组合。通过对提示学习前后的嵌入使用同一概念词典，可直接比较其概念分布（concept profile）的变化。在 CoOp 于 11 个图像分类数据集上的实验表明，概念分布发生显著重组：平均而言，初始前 10 个概念中仅有 1.6 个在学习后仍保留在前 10 名；并且数据集上的分布变化程度与准确率提升呈正相关。此外，作者推导了一个局部梯度表达式，用以解释为什么与当前提示不同的、但更接近图像对齐方向的概念方向可能具有更高的损失敏感性。

### 方法 / 贡献
- 提出 PromptSpLiCE：将提示学习后的文本嵌入投影到一个共享的自然语言概念坐标系统，实现提示嵌入的稀疏分解与前后对比。
- 方法细节：使用由自然语言概念经 CLIP 文本编码器构成的概念词典；对嵌入进行中心化和归一化以缓解 CLIP 嵌入的各向异性；用非负 Lasso（$\ell_1$ 正则）估计稀疏概念系数。
- 贡献 1：提示侧的事后分析框架，用固定自然语言词典统一表示初始和所学提示。
- 贡献 2：对 CoOp 在 11 个数据集上进行系统分析，揭示概念分布的大幅重组。
- 贡献 3：推导嵌入层面的局部敏感性表达式，提供几何直觉，并与 CoOp 参数梯度的实际计算相区分。

### 实验或数据
摘要提及的评估：使用 CoOp 作为代表性提示学习方法，在 11 个图像分类数据集上验证 PromptSpLiCE。主要量化结果：学习后平均只有 1.6 个初始 top-10 概念仍留在 top-10；跨数据集的分布变化程度与准确率提升呈正相关。具体数据集名称、详细实验设置和消融结果未在摘要中给出。

### 值得关注点
- 解释性与诊断性：PromptSpLiCE 无需修改训练目标或推理过程，就能事后解释软提示的语义变化。
- 分析发现提示学习并非轻微调整，而是对概念分布进行显著重组；仅有少数初始关键概念保留。
- 分布重组程度与准确率增益正相关，这意味着概念层面的变化具有实际预测意义。
- 推导的梯度敏感性表达式提供了几何解释：与图像对齐的概念方向可能比与当前提示平行的方向更敏感。

### 局限性
- 稀疏系数是事后拟合得到的，并非 CLIP 内部的实际激活。
- 概念词典是过完备的，且词嵌入之间存在相关性，因而相似的文本重建可能对应不同的稀疏系数（可解释不唯一）。
- 方法在重建时固定了中心化残差的尺度为单位长度（只保留方向），尺度信息的恢复是一种近似。
- 分析没有包含干预实验（如掩码或反事实测试），因此在因果层面上的结论有限。
- 实验评估仅针对 CoOp，尚未覆盖其他提示学习方法。

## 6. Learning to Grade Efficiently: A Bandit-Driven Prompt-Selection Framework for Low-Cost LLM Essay Scoring

- Source: arxiv
- arXiv ID: 2608.23814
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.23814v1
- PDF: https://arxiv.org/pdf/2608.23814v1
- DOI: https://doi.org/10.48550/arXiv.2608.23814

### Authors

Olga Manakina, Igor Bogdanov

### Abstract

Large Language Models (LLMs) demonstrate strong capabilities in automated essay scoring (AES), but contemporary approaches typically employ fixed prompt selection, failing to address operational cost concerns and evolving optimal configurations. We propose a novel cost-aware approach that treats each prompt type as an arm in a multi-armed bandit (MAB) controller, enabling adaptive selection of optimal prompting strategies during inference. Our experiments on IELTS Writing Task 2 essays show that the MAB framework achieves comparable scoring accuracy to exhaustive grid search while reducing LLM calls by 78.4\% to find the best grading approach. We implemented four distinct grading recipes (multi-step vs. single-step assessment, with vs. without calibration examples) and found that the multi-step approach with examples achieves the highest accuracy. By tracking token usage and latency alongside agreement metrics, we produce the first cost-reliability learning curves for essay scoring, providing actionable insights for educational technology platforms that must balance operational costs against assessment validity. This work represents the first application of online control mechanisms to adaptively select prompting strategies in AES, transforming prompt selection from an offline hyperparameter optimization problem into an efficient online learning task.

### 中文一句话结论
本文提出一种基于多臂老虎机（MAB）的自适应提示选择框架，在自动作文评分中，将LLM调用次数减少78.4%，同时保持与穷举网格搜索相当的评分准确性。

### English TL;DR
This paper introduces a novel cost-aware framework that uses a multi-armed bandit controller to adaptively select optimal prompting strategies for automated essay scoring, achieving comparable accuracy to exhaustive grid search while reducing LLM calls by 78.4%.

### 中文详细总结
现有LLM自动作文评分（AES）方法通常采用固定提示模板，忽略了运营成本变化和最优配置的动态性。本文提出一种成本感知的MAB框架，将每种提示类型视为一个“臂”，在推理过程中自适应选择最优策略。实验在IELTS Writing Task 2数据集上进行，包含787篇作文。四种评分策略（多步/单步评估，有/无校准示例）被定义为臂。MAB框架（ε-贪心算法）在500步后稳定偏好“多步+示例”策略，该策略具有最低MAE（约0.85）和最高QWK（约0.55）。相比穷举网格搜索，MAB仅需1,697次LLM调用（减少78.4%），并首次生成了作文评分的成本-可靠性学习曲线。该工作将提示选择从离线超参数优化转变为在线学习任务，为教育平台平衡运营成本与评估效度提供了实用见解。

### 方法 / 贡献
- **方法**：构建一个多臂老虎机（MAB）控制器，每个臂对应一种评分提示策略（四种：多步+示例、多步无示例、单步+示例、单步无示例）。采用ε-贪心算法平衡探索与利用，奖励函数基于预测与人类评分之间的负绝对误差（并可选择加入token惩罚）。系统在推理时动态选择最优策略，无需预先穷举所有组合。
- **贡献**：
  1. 首次将在线控制机制（MAB）应用于AES中的提示策略自适应选择，将问题从离线优化转为在线学习。
  2. 首次生成作文评分的成本-可靠性学习曲线，跟踪token用量、延迟与一致性指标，为实际部署提供可操作洞见。

### 实验或数据
- **数据集**：IELTS Writing Scored Essays Dataset（Kaggle），787篇Academic Task 2作文，每篇附带官方1-9分评分。
- **模型**：仅使用Google Gemini Flash 2.5。
- **实验设置**：对比MAB（500篇作文，每篇分配一个臂）与穷举网格搜索（所有787篇作文×4种策略）。评估指标包括MAE、QWK、LLM调用次数、token消耗、API成本。
- **主要结果**：
  - MAB减少LLM调用78.4%（从7,870次降至1,697次），token消耗从10,915,411降至2,964,444。
  - 多步+示例策略在MAB下MAE=0.85，QWK=0.55，为最优。
  - 单步+示例策略提供平衡选项（MAE=1.0，成本更低）。
  - 网格搜索与MAB在QWK上表现一致，验证了MAB的准确性。

### 值得关注点
- **成本效率**：MAB以约1/10的LLM调用达到与网格搜索相近的准确性，显著降低运营成本。
- **自适应选择**：MAB自动偏好“多步+示例”策略，证明其能有效学习最优提示配置。
- **首次应用**：首次将在线控制（MAB）引入AES，转变了提示选择的范式。
- **实用价值**：成本-可靠性曲线为教育平台提供了直观的权衡工具。

### 局限性
- 仅使用单一LLM（Gemini Flash 2.5），未在GPT-4、Llama-3等模型上验证，泛化性未知。
- 实验仅基于IELTS Task 2数据集（787篇），未在更大规模或不同领域的基准（如ASAP、TOEFL11）上测试。
- 工作为“进行中”（work in progress），未探索更复杂的MAB变体（如上下文MAB）或更丰富的提示策略集合。
- 奖励函数设计简单，未充分考虑心理测量学中的评分者一致性、公平性等更高阶要求。

## 7. Giga-Embeddings: Mixture-of-Experts Encoders for High-Throughput Text Embeddings

- Source: arxiv
- arXiv ID: 2608.23806
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.23806v1
- PDF: https://arxiv.org/pdf/2608.23806v1
- DOI: https://doi.org/10.48550/arXiv.2608.23806

### Authors

Egor Kolodin, Egor Krasnoperov, Evgeniy Kosarev, Fyodor Minkin

### Abstract

We introduce Giga-Embeddings, a family of text embedding models designed to combine strong retrieval quality with efficient serving. Its largest member is a sparse 10B-parameter Mixture-of-Experts encoder with approximately 1.8B active parameters per token. Across English, Russian, multilingual, and code MTEB benchmarks, this model achieves the strongest aggregate performance within the family on all four evaluated suites. In our vLLM benchmark with 1024-token inputs, it processes 114.5k tokens per second, providing 25 percent higher throughput than the dense 3B model and 1.56-2.65x the throughput of the evaluated external systems. The family also includes a dense 3B encoder and a distilled 480M encoder for tighter compute and memory budgets. We train the compact model using a dimension-agnostic objective that aligns teacher and student similarity distributions. The resulting 480M model scores 70.98 on Russian MTEB, surpassing FRIDA while using 42 percent fewer parameters. We release all three model checkpoints.

### 中文一句话结论
Giga-Embeddings 系列模型通过稀疏Mixture-of-Experts (MoE)架构和维度无关的相似性分布蒸馏技术，在保持强检索质量的同时实现了高吞吐量；其中最大的10B参数MoE模型（活跃参数约1.8B）在多个MTEB基准上取得最佳性能，而经过蒸馏的480M模型在俄语MTEB上超越FRIDA且参数减少42%。

### English TL;DR
The Giga-Embeddings paper introduces a family of text embedding models specifically engineered for high throughput while maintaining strong retrieval performance. The family includes a flagship sparse 10B-parameter Mixture-of-Experts encoder activating about 1.8B parameters per token, a dense 3B encoder, and a compact 480M encoder. The 10B MoE model achieves the highest aggregate scores on English, Russian, multilingual, and code MTEB benchmarks within the family. In throughput benchmarks, it processes over 114k tokens per second at 1024-token input, delivering a 25% throughput increase over the dense 3B model and 1.56x–2.65x speedup over evaluated external systems. The 480M distilled model, trained via a novel similarity-distribution distillation technique, reaches 70.98 on Russian MTEB, surpassing FRIDA with 42% fewer parameters.

### 中文详细总结
该论文提出Giga-Embeddings文本嵌入模型系列，旨在结合强检索质量与高效推理服务。模型系列包含三个成员：最大的10B参数Mixture-of-Experts (MoE)稀疏编码器（每token激活约1.8B参数，维度1536）、3B密集编码器（维度2048）以及经过蒸馏的480M紧凑型编码器（维度1024）。在英语、俄语、多语言和代码四个MTEB基准上，10B MoE模型在系列内均取得最佳综合得分。通过vLLM基准测试，10B MoE模型在1024 token输入长度下达到每秒114.5k token的吞吐量，比密集3B模型高25%，是其他外部评估系统的1.56到2.65倍。480M模型通过一种维度无关的蒸馏方法训练，无需匹配教师和学生模型的嵌入维度，通过KL散度对齐候选集上的相似性分布。该模型在俄语MTEB上得分70.98，以42%更少的参数超越了FRIDA（70.95）。所有三个模型检查点均已开源发布。

### 方法 / 贡献
主要贡献包括：
1.  **模型架构设计**：采用双向编码器架构（替换因果掩码为双向掩码），使用平均池化。10B模型采用DeepSeekMoE风格稀疏架构（64个路由专家+1个共享专家，top-4路由），实现高容量与高吞吐量的平衡。480M和3B模型为密集Qwen3编码器。
2.  **三阶段对比训练**：遵循早期Giga-Embeddings框架，包含广泛对比预训练、带困难负样本的检索微调、以及多任务微调。预训练使用批次内InfoNCE损失，微调和多任务阶段使用固定的8候选组（1正+7负）。
3.  **相似性分布蒸馏**：专门针对480M学生模型在微调和多任务阶段使用的一种维度无关的知识蒸馏方法。它不是对齐嵌入向量，而是通过KL散度对齐教师和学生在候选集上的相似性分布，因此即使教师和学生使用不同的嵌入维度（如3B的2048维和480M的1024维）也可适用。蒸馏损失与对比损失加权结合。

### 实验或数据
- **数据集**：训练混合了开源数据集（来自早期Giga-Embeddings配方）和部分未公开的数据集。
- **评估基准**：在英语、俄语、多语言和代码四个MTEB任务-宏基准上进行评估。
- **性能结果**：
    - **质量**：10B MoE模型在四个基准上均为家族内最佳（英语72.23，俄语74.98，多语言65.64，代码78.41）。
    - **吞吐量**：在vLLM基准测试中，10B MoE模型在512/1024/2048 token输入下分别达到每秒118.6k/114.5k/108.1k token。比较了Qwen3 Embedding 4B、F2LLM-v2-8B和Nemotron 8B等外部模型。
    - **蒸馏效果**：480M模型俄语MTEB得分70.98，超越FRIDA（70.95），参数减少42%。在四个基准上距离3B模型约2.41–6.92个百分点。
- **训练设置**：全局批次大小（预训练16384，微调/多任务1024），学习率3e-5，cosine衰减，Adam优化器，权重衰减0.01。

### 值得关注点
- **高吞吐量MoE架构**：10B总参数仅激活约1.8B，在保持模型容量的同时实现了非常高的推理吞吐量，为大规模部署提供了实际优势。
- **维度无关蒸馏**：创新性地将蒸馏应用于嵌入模型，克服了教师和学生模型维度不同（或架构不同）的限制，仅通过最终相似性分数进行知识迁移，具有很好的通用性。
- **开源模型**：三个不同规模的检查点均开源，为社区在计算资源受限或高吞吐需求场景下提供了灵活选择。
- **全面的性能表现**：在所有四个评估基准上（英语、俄语、多语言、代码），10B模型均为家族内最佳，展示了稀疏激活的潜力。

### 局限性
根据论文摘要和内容，未明确提及局限性。但可推断的可能局限包括：
- **蒸馏依赖教师模型质量**：480M模型的蒸馏效果依赖于预训练的3B或10B MoE教师模型的性能上限。
- **训练数据部分未公开**：部分训练数据集受合约限制无法公开，影响了完全可复现性。
- **主要面向检索任务**：模型针对MTEB基准优化，其设计和评估主要聚焦于检索、分类、聚类和语义相似度，可能没有专门针对生成式任务等场景优化。
- **MoE模型配置的权衡**：虽然吞吐量高，但MoE架构在一定程度上可能影响特定任务的表征一致性或引入额外的部署复杂性（例如，相较于同参数的密集模型）。

## 8. Data Mixing as Mixture Experiment: Response Surface Methodology and Optimal Design for Large Language Model Pretraining

- Source: arxiv
- arXiv ID: 2608.23922
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.23922v1
- PDF: https://arxiv.org/pdf/2608.23922v1
- DOI: https://doi.org/10.48550/arXiv.2608.23922

### Authors

Yicheng Mao, Hongru Du

### Abstract

Data mixing is a central design problem in large language model pretraining: given a fixed token budget, practitioners must decide how much data to allocate to each domain. Recent proxy-based methods address this problem by training small models on candidate mixtures, fitting a response model, and using the response to select mixtures for larger-scale training. We show that this workflow has the structure of a classical mixture experiment. Under this view, data domains are mixture components, token shares are component proportions, proxy-training runs are experimental design points, and validation loss defines a response surface over the probability simplex. We develop this formulation using sparse second-order Scheffé response-surface models and construct model-robust $\mathcal{I}$-optimal designs for proxy data-mixing experiments. Using RegMix as an empirical case study, we demonstrate how the framework can both interpret observed mixture responses and design more efficient proxy experiments. The Scheffé analysis shows that domain value is strongly relational: several domains that are weak under additive effects become favourable through pairwise interactions, especially through combinations with web-derived text. The sparse Scheffé model preserves mixture rankings across model scales and remains competitive with a flexible machine-learning predictor while providing an explicit decomposition of additive and interaction effects. In a simulation study calibrated to observed proxy-training responses, model-robust $\mathcal{I}$-optimal designs recover the relevant mixture ordering after removing about 25\% of the original proxy runs. These results suggest that LLM data mixing should be treated not only as a prediction problem, but also as an experimental-design problem in which the proxy mixtures themselves can be chosen to improve statistical efficiency.

### 中文一句话结论
本文将大语言模型预训练中的数据混合问题形式化为经典混合物实验，并证明稀疏二阶Scheffé响应面模型与模型鲁棒ℐ-最优设计能在保持可解释性的同时，减少代理训练次数以恢复可靠的混合排序。

### English TL;DR
This paper formalizes LLM data mixing as a mixture experiment, using sparse second-order Scheffé models and model-robust ℐ-optimal designs to interpret domain interactions and reduce proxy runs needed for reliable mixture rankings.

### 中文详细总结
本文重新审视了基于代理模型的数据混合工作流（如RegMix），指出其本质上等同于一个经典的混合物实验：数据域为混合成分，token份额为成分比例，代理训练为实验设计点，验证损失构成响应面。论文采用稀疏二阶Scheffé模型在概率单纯形上建模，通过显式系数分解各域的加性效应和域间交互效应。分析发现，某些域在加性模型下表现弱，但通过与其他域（尤其是网络文本）的成对交互变得有利。研究还使用模型鲁棒ℐ-最优设计来替代随机采样选择代理混合，模拟实验表明，在移除约25%的原始代理运行后，该设计仍能恢复正确的混合排序。

### 方法 / 贡献
1. 形式化LLM数据混合为混合物实验，连接了代理混合流程与统计混合物建模与最优实验设计文献。
2. 使用稀疏二阶Scheffé模型，提供加性域效应与成对域交互的显式可解释分解，超越黑箱预测器。
3. 引入模型鲁棒ℐ-最优设计，通过选择信息量更高的代理混合点，提高实验效率，减少所需代理运行数量。

### 实验或数据
使用RegMix公开代理训练数据（17个域，512个1M参数代理模型在1B token上训练，验证损失为响应）。作者重新拟合稀疏Scheffé模型，并基于观察到的代理响应校准模拟研究，测试ℐ-最优设计在减少代理运行后的排序恢复能力。

### 值得关注点
- 揭示了域间交互的重要性：某些域单独使用时效果不佳，但与其他域组合后价值显著提升（如与网络文本搭配）。
- Scheffé模型在跨模型规模（从1M到1B参数）下保持混合排序竞争性，同时提供显式效应分解。
- 将实验设计（而非仅预测）引入数据混合问题，提示“如何选择代理混合”同样值得关注。

### 局限性
- 实证分析局限于RegMix设置（17个Pile域，1M-1B参数规模），结果泛化性未知。
- Scheffé模型依赖预先指定的响应面阶数，可能无法捕捉高阶或非线性依赖。
- 在混合点较少时，稀疏模型可能无法充分拟合复杂交互。
- 模拟研究假设代理响应服从特定参数结构，可能与真实训练响应略有偏差。

## 9. Linear Probing Provides Robust and Efficient Detection of Machine-Generated Text

- Source: arxiv
- arXiv ID: 2608.24780
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.24780v1
- PDF: https://arxiv.org/pdf/2608.24780v1
- DOI: https://doi.org/10.48550/arXiv.2608.24780

### Authors

Gerrit Quaremba, Hanqi Yan, Elizabeth Black, Denny Vrandecic, Elena Simperl

### Abstract

Distinguishing machine-generated text (MGT) from human-written text (HWT) becomes increasingly important due to potential misuse. However, most supervised detectors often degrade out-of-domain (OOD) and require large, diverse training sets. In this work, we analyze the linearity and quality of MGT representations and show that simple linear probes outperform a wide range of detectors while being substantially more sample-efficient. We first show that MGT and HWT latent representations are linearly separable in low-dimensional space, and provide a plausible explanation for this separability through systematic differences in their representation quality. Motivated by these insights, we train two variants of simple linear probes and evaluate them across 4 benchmarks against 16 baselines. Probes consistently improve OOD detection (+11 AUC), requiring solely ${<}100$ samples to reach near-peak performance. We show that this transferability arises because probes recover a shared latent MGT direction that generalizes across diverse settings. Finally, we demonstrate that probing vectors capture a continuous spectrum of ``machineness'', highlighting their potential for fine-grained estimation of AI-edited text. Overall, our work provides insights into latent-space differences between MGT and HWT and demonstrates the potential of linear probes as as robust and sample-efficient MGT detectors. We release our code on~\href{https://github.com/gerritq/mgt_probes}{github}.

### 中文一句话结论
本文发现机器生成文本与人类文本在低维潜空间中线性可分，并利用这一特性设计了简单的线性探针，显著提升了检测的鲁棒性和样本效率。

### English TL;DR
Simple linear probes trained on low-dimensional latent representations of machine- and human-written text achieve robust, sample-efficient detection with strong out-of-domain generalization, outperforming more complex supervised detectors.

### 中文详细总结
本文研究了机器生成文本（MGT）与人类文本（HWT）在潜在空间中的线性可分性及其表示质量差异。通过可视化发现，MGT和HWT的隐藏状态在低维PCA空间中从第6层左右开始线性可分；进一步的分析表明，MGT的表示更压缩、各向异性更强、内在维度更低，而HWT的表示则更丰富、更均匀。基于这些发现，作者训练了两种简单的线性探针（逐层线性探针LLP和层拼接线性探针CLP），在冻结的语言模型隐藏状态上做二分类。在4个基准测试、16个基线方法的对比中，线性探针在域内检测中AUC最高提升18个点，在域外OOD检测中AUC平均提升11个点，且仅需不到100个训练样本就能达到接近最优的性能。探针学到的“机器性”方向在不同数据集之间高度一致，能泛化到多种生成场景。此外，探针投影分数能连续度量文本的AI编辑程度，支持细粒度估计。

### 方法 / 贡献
- 发现MGT与HWT在潜空间线性可分，并通过表示质量指标（熵、有效秩、各向异性、内在维数）解释了这一现象。
- 提出两种线性探针变体（逐层平均线性探针LLP和层拼接线性探针CLP），使用PCA降维后的隐藏状态训练。
- 相比复杂监督检测器，线性探针在OOD检测中AUC提升11点，且仅需10–100个样本即可达到接近最优性能。
- 证明探针向量捕获了一个共享的“机器性”方向，可连续度量AI编辑程度。

### 实验或数据
- 使用4个基准测试（包含多个域内和域外场景），对比16种基线方法（包括零样本和监督检测器）。
- 探针在域内检测AUC最高提升18点，OOD检测AUC平均提升11点。
- 仅需小于100个训练样本达到近峰值性能，采样不确定性显著低于基于训练的基线。
- 表示质量分析在Wikipedia子集上使用Llama-8B模型，验证了跨域泛化。
- 探针向量在多个数据集间高度对齐（余弦相似度高）。

### 值得关注点
- MGT和HWT的线性可分性在低维空间中显著，且增加非线性复杂度反而降低性能。
- MGT表示具有压缩、各向异性、低维流形结构，为线性边界提供了解释。
- 探针的OOD泛化能力强，且样本效率极高（<100样本）。
- “机器性”是连续方向，可用于评估AI编辑强度，不仅限于二分类。

### 局限性
论文摘要和提供内容中未明确讨论局限性；基于方法本身，线性探针需要白盒访问模型隐藏状态，依赖特定骨干模型（如Llama），可能不适用于无法获取中间表示的场景。此外，实验主要在中文和英文基准上，域外泛化未覆盖所有可能的生成器或对抗性扰动。

## 10. Beyond Static and Linear: What Attention Constraints Best Fit Human Reading Times?

- Source: arxiv
- arXiv ID: 2608.23818
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.23818v1
- PDF: https://arxiv.org/pdf/2608.23818v1
- DOI: https://doi.org/10.48550/arXiv.2608.23818

### Authors

Lanni Bu, Xiulin Yang, Christian Clark, Alex Warstadt, Ethan Gotlieb Wilcox

### Abstract

Transformer-based language models are widely used as models of human language processing, yet their attention mechanisms allow lossless access to the full preceding context, unlike the limited memory systems of humans. We hypothesize that installing memory constraints into transformers' attention mechanisms can improve their fit to human behavioral data. While previous work has explored individual constraints in isolation, we conduct a systematic comparison of multiple attention-based memory mechanisms across different model sizes and training corpora, evaluating both psychometric predictive power for human reading times and grammatical competence. We additionally compare static constraints, in which the constraint strength is fixed throughout training, to dynamic memory curricula. We find that constraints that are sensitive to the content of intervening tokens consistently achieve the highest alignment with human reading times, outperforming distance-based constraints. We observe a dissociation between psychometric fit and grammatical competence under dynamic memory curricula, suggesting that Transformers cannot serve as a one-size-fits-all cognitive model.

### 中文一句话结论
内容敏感的注意力约束（如FoX和Stick-Breaking机制）比距离约束（如ALiBi和n-gram）更符合人类阅读时间数据，但动态记忆课程会导致心理测量拟合与语法能力之间的分离。

### English TL;DR
Content-sensitive attention constraints (FoX, Stick-Breaking) predict human reading times better than distance-based ones (ALiBi, n-gram). Dynamic memory curricula cause a dissociation between psychometric fit and grammatical competence, challenging a one-size-fits-all cognitive model.

### 中文详细总结
本文系统比较了Transformer中的多种注意力记忆约束对人类阅读时间的预测能力。研究者假设，在Transformer的注意力机制中引入类似人类记忆限制的约束，可以提升其对人类行为数据的拟合。他们测试了以下约束：1) 距离约束（线性偏置ALiBi、滑动窗口n-gram注意力）；2) 内容约束（FoX：基于中间词身份的遗忘门、Stick-Breaking：基于高注意力中间词的向下加权）。研究使用6个阅读时间语料库评估心理测量预测力，并通过语法基准测试评估语言能力。主要发现：内容敏感约束（特别是FoX）在多数配置中表现最佳；距离约束表现次之；静态约束比动态课程更好预测阅读时间，但动态课程在语法基准上表现更优。此外，Less-to-More课程（约束逐渐减弱）并不总是优于More-to-Less课程，这与“少即是多”假说预期不一致。

### 方法 / 贡献
- 方法：在解码器Transformer（2层和4层）上实现4种注意力约束；将约束强度固定（静态）或在训练过程中变化（动态课程）；对比Less-to-More（约束渐弱）和More-to-Less（约束渐强）。
- 贡献：首次系统比较多种注意力记忆约束的心理测量有效性；发现内容约束优于距离约束；揭示动态课程下心理测量与语法能力的分离；挑战“少即是多”假说在神经网络学习中的直接应用。

### 实验或数据
- 实验：两个模型大小（2层、4层）；三个预训练语料库（具体语料未在摘要中指定）；六个阅读时间语料库用于心理测量评估；使用语法基准测试（具体基准未在摘要中说明）评估语法能力。
- 论文提及代码开源（https://github.com/Lanni-ni/different-attention-mechanisms-transformers），但摘要未列出具体实验数值结果。

### 值得关注点
- 内容敏感性约束（FoX）在预测人类阅读时间上一致优于距离约束，支持基于线索的检索理论。
- 动态课程导致心理测量拟合与语法能力的分离，表明Transformer不适合作为“万能”认知模型。
- Less-to-More课程并非总是更好，与发育语言习得理论（“少即是多”）预期相悖。
- 该研究填补了内容干扰理论在Transformer认知建模中的空白。

### 局限性
- 动态课程仅对两种约束（ALiBi和FoX）实施，未测试n-gram和Stick-Breaking的动态版本。
- 模型规模较小（2-4层），可能无法完全代表大规模Transformer的行为。
- 阅读时间数据来自特定语料库，结果可能受语料特性影响。
- 论文未详细说明语法基准测试的具体内容或数值结果。
- 动态课程中“约束强度”的量化方式可能影响结论的泛化性。

## Processing Notes

- Duplicate papers skipped: 0