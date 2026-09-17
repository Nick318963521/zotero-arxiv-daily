# Daily arXiv - 2026-09-17

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-17T00:33:30
- Paper count: 10

## 1. A Framework for Generating Valid Context-Specific Benchmarks through Expert Guidance

- Source: arxiv
- arXiv ID: 2609.16592
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.16592v1
- PDF: https://arxiv.org/pdf/2609.16592v1
- DOI: https://doi.org/10.48550/arXiv.2609.16592

### Authors

Kimberly Le Truong, Nari Johnson, Anna Kawakami, Hoda Heidari

### Abstract

This paper presents an end-to-end approach for generating context-specific large language model (LLM) benchmark datasets by combining expert input with synthetic data generation. Existing benchmark construction methods often trade off validity and scalability: datasets designed with domain experts can produce high-quality evaluations but are slow and costly to create, while synthetically generating data may scale efficiently but often results in unrealistic, redundant, or out-of-scope examples. To address this gap, we introduce a schema eliciting key information about the goals, scope, and context of an evaluation task, and use this information to guide synthetic data generation. We further define four criteria grounded in measurement validity for assessing dataset quality: coverage, diversity, content realism, and stylistic realism. Using these criteria, we show how expert-informed scaffolds can guide synthetic data generation toward more valid benchmarks. Through quantitative evaluations and a real-world case study with domain experts, we demonstrate that our approach improves benchmark data quality over existing methods while preserving validity. We additionally analyze how different types of schema information affect different dataset quality criteria, and provide practical guidance on which information to prioritize collecting under resource constraints.

### 中文一句话结论
本文提出一个结合专家输入与合成数据生成的端到端框架，通过结构化schema和四个质量准则（覆盖度、多样性、内容真实性、风格真实性），在保证规模的同时生成具有有效性的上下文特定LLM基准数据集。

### English TL;DR
This paper introduces an end-to-end framework that combines expert input with synthetic data generation, using a structured schema and four quality criteria (coverage, diversity, content realism, stylistic realism) to create context-specific LLM benchmark datasets that are both scalable and valid.

### 中文详细总结
现有基准构建方法常需在有效性与规模之间取舍：专家设计的基准质量高但缓慢昂贵，完全合成生成虽高效但常不真实、冗余或超出目标范围。本文提出一个三层路径：先引入schema（结构模板）获取评估任务的目标、范围与上下文信息；再定义基于测量有效性理论的可操作数据集质量指标（覆盖度、多样性、内容真实性、风格真实性）；最后用这些指标指导合成数据生成。通过定量评估与真实案例（社会工作者使用聊天机器人的场景）展示，该方法在保持有效性的同时提升基准数据质量，并分析不同schema信息对质量指标的影响，为资源受限时优先收集哪些信息提供实用指导。

### 方法 / 贡献
- **Schema设计**：从测量有效性理论中提炼人口、概念、实例三要素，分解为八个字段，收集评估目标、部署人群、概念定义及实例变化因素等，并包含种子示例。
- **质量准则操作化**：将内容有效性（覆盖度+多样性）与生态有效性（内容真实性+风格真实性）转化为可计算的[0,1]指标，覆盖度使用平滑惩罚函数，多样性采用DCScore，内容真实性用Sinkhorn距离归一化。
- **综合框架**：展示如何将schema与质量指标嵌入提示工程，指导合成数据生成，实现专家知识可扩展利用。

### 实验或数据
- **案例研究**：与美国一所小学的社会工作者合作，生成了评估LLM生成反思性问题能力的基准数据集。
- **定量评估**：对比基线方法，专家认为本方法生成的示例更真实；通过消融研究分析不同schema信息对质量指标的影响。

### 值得关注点
- 提出了可操作、可计算的四个质量准则，弥补了测量有效性在评估数据集层面的具体化不足。
- 强调高质量不意味着所有指标最大化，理想平衡取决于具体使用场景和利益相关者优先级。
- 提供了实际部署中的资源分配指导，明确哪些schema信息在资源有限时更值得优先收集。

### 局限性
论文未明确列出局限性，但可推断：质量指标需专家解释才能正确解读，且仅为必要而非充分条件，其他质量度量可能同样有价值。部分细节（如实例级诊断、指标公式的完整推导）置于附录，未在正文全面展开。

## 2. Target-Language Generation in Multilingual Models: Activation Steering and Optimal Control

- Source: arxiv
- arXiv ID: 2609.16967
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.16967v1
- PDF: https://arxiv.org/pdf/2609.16967v1
- DOI: https://doi.org/10.48550/arXiv.2609.16967

### Authors

James A. Michaelov, Carmen Amo Alonso, Tyler A. Chang, Roger P. Levy

### Abstract

Ensuring that multilingual language models generate coherent text in a specific target language is a major issue in multilingual language modeling. We develop an optimal control method for target-language text generation as well as a framework for evaluating the quality of generated text in terms of language adherence, linguistic coherence, and semantic coherence. We find that the proposed method performs at least as well as the prominent difference-in-means activation steering method for the majority of models tested, with substantially less hyperparameter tuning required.

### 中文一句话结论
本文提出了一种用于多语言模型的目标语言生成的最优控制方法，在多数测试模型上性能至少与差异均值激活引导方法相当，且所需超参数调优显著减少。

### English TL;DR
This paper proposes an optimal control method for target-language generation in multilingual models, which matches the performance of difference-in-means activation steering on most tested models while requiring substantially less hyperparameter tuning.

### 中文详细总结
多语言模型在生成特定目标语言的连贯文本时面临挑战。本文开发了一种基于最优控制的目标语言文本生成方法，并构建了评估框架，从语言遵从性、语言连贯性和语义连贯性三个维度衡量生成文本质量。实验表明，所提方法在大多数测试模型上性能不低于主流的差异均值激活引导方法，且超参数调优的工作量大幅降低。

### 方法 / 贡献
- 提出了一种最优控制方法，用于多语言模型的目标语言生成，通过控制模型内部表示实现输出语言定向。  
- 构建了多维度的文本生成质量评估框架（语言遵从性、语言连贯性、语义连贯性）。  
- 与差异均值激活引导方法相比，所需超参数调优显著减少，性能相当或更优。

### 实验或数据
摘要中未明确提及具体使用的数据集或模型名称，仅指出方法在“大多数测试模型”上进行了评估，并利用提出的框架衡量生成结果。实验细节和数据集需参考全文。

### 值得关注点
- 该最优控制方法减少了对手动调参的依赖，更便于实际应用。  
- 评估框架覆盖了生成文本的语言和语义质量，较为全面。  
- 在性能不妥协的前提下，降低了方法使用的门槛。

### 局限性
从摘要中未明确讨论局限性。可能的潜在局限包括：最优控制方法的计算开销、在不同语言对或低资源语言上的泛化能力等，需要进一步验证。

## 3. Style-Debiased DPO: Updating LLM Knowledge with Factuality-Aware Synthetic Preference Data

- Source: arxiv
- arXiv ID: 2609.16532
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.16532v1
- PDF: https://arxiv.org/pdf/2609.16532v1
- DOI: https://doi.org/10.48550/arXiv.2609.16532

### Authors

Takayuki Yamamoto, Daisuke Kawahara

### Abstract

Continued pretraining (CPT) with data augmentation such as paraphrasing can store inside a large language model (LLM) the knowledge of a small source corpus. The stored knowledge, however, is not always retrieved correctly. We study the eliciting side rather than the storing side: we use preference optimization, which learns from pairs of a preferred (chosen) and a dispreferred (rejected) response, so that the model elicits its stored knowledge more accurately. One proposed approach takes the model's own erroneous response as rejected and the gold answer as chosen, so as to suppress the error. When the target knowledge is partially known, however, most of these rejected responses are factually correct. Using direct preference optimization (DPO) then pushes down rejected responses that contain correct knowledge and differ from the chosen answer only in style, such as length and wording. We propose style-debiased DPO (SD-DPO), which scores whether the rejected response of each pair is factually correct, inverts the preference of such pairs, and weights them so that the learning signal due to differences in style cancels out as a whole. We first test whether, on top of EntiGraph, a representative storing-side method that runs CPT on text synthesized from the corpus, our method adds accuracy efficiently. On QuALITY, the reading-comprehension QA benchmark on which EntiGraph was evaluated, SD-DPO exceeds a baseline we CPT on EntiGraph's synthetic data from the same base model and evaluate with the same procedure. The training tokens this requires are a few dozen times fewer than the additional CPT needed for the same gain. For knowledge updating, the main goal of this work, we use AToKE, a knowledge-editing benchmark for facts that change over time. There, SD-DPO reaches an overall accuracy of 0.982 and answers with the new or the old fact according to the queried period.

### 中文一句话结论
本文提出风格去偏DPO（SD-DPO），通过识别并反转那些被拒绝回答虽事实正确但仅风格不同的偏好对，避免DPO抑制正确知识，从而在知识更新基准AToKE上达到0.982的总体准确率，且所需训练token远少于传统方法。

### English TL;DR
This paper introduces Style-Debiased DPO (SD-DPO), which improves LLM knowledge elicitation by detecting preference pairs where the rejected response is factually correct but stylistically different, then inverting and weighting them to cancel style-induced biases. It achieves 0.982 overall accuracy on the AToKE knowledge-editing benchmark with significantly fewer training tokens than baseline CPT methods.

### 中文详细总结
论文聚焦于大型语言模型（LLM）在持续预训练（CPT）后存储知识但无法准确检索的问题。作者从“激励”侧而非“存储”侧入手，利用偏好优化（如DPO）来提升知识提取准确性。传统方法将模型自身错误回答作为拒绝样本、黄金答案作为选择样本进行DPO，但当目标知识部分已知时，许多被拒绝的回答其实事实正确，仅因风格（如长度、措辞）不同而被错误压制。为此，作者提出SD-DPO：先判断每个偏好对中被拒绝回答是否事实正确，对事实正确的对反转偏好，并赋予权重以整体抵消风格差异带来的学习信号。

### 方法 / 贡献
- **核心方法**：SD-DPO包含两步——（1）对每个偏好对被拒绝回答进行事实性评分；（2）对事实正确的对反转偏好，并加权使风格差异信号整体抵消。
- **主要贡献**：提出一种无需额外标注或外部模型即可消除DPO中风格偏差的机制，专注于提升知识提取而非知识存储。
- **与现有方法对比**：旨在补充存储侧方法（如EntiGraph），而非替代。

### 实验或数据
- **QuALITY基准**：在EntiGraph生成的合成数据上进行CPT后，SD-DPO比同基座模型、同评估流程的基线准确率更高，且所需训练token比达到相同增益的额外CPT少几十倍。
- **AToKE基准**：用于知识更新（随时间变化的事实），SD-DPO达到0.982总体准确率，能根据查询时间回答新或旧事实。
- **未提及**：未报告具体数据集规模、训练细节或消融实验。

### 值得关注点
- **效率优势**：在知识更新任务中，SD-DPO大幅减少训练成本（几十倍token节省）。
- **新颖视角**：从“激励”而非“存储”角度解决知识提取问题，与主流CPT方法互补。
- **高准确性**：AToKE上0.982准确率，且能按时间区分新旧事实。

### 局限性
- **依赖事实性评分**：方法性能依赖于准确评判被拒绝回答是否事实正确，但文中未详细说明此评分的实现方式或误差影响。
- **实验范围有限**：仅测试了QuALITY和AToKE两个基准，未泛化到其他任务或模型规模。
- **未报告失败案例**：未讨论当知识完全未知或评分错误时方法的鲁棒性。

## 4. Zero-shot narrative detection in social messaging

- Source: arxiv
- arXiv ID: 2609.17310
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.17310v1
- PDF: https://arxiv.org/pdf/2609.17310v1
- DOI: https://doi.org/10.48550/arXiv.2609.17310

### Authors

Jesús M. Fraile-Hernández, Anselmo Peñas, Patrick Giedemann

### Abstract

This study investigates the zero-shot ability of large language models (LLMs) to identify and classify hidden narratives in social messages. Our research hypothesis is that LLMs' extensive contextual knowledge allows them to interpret messages on a deeper, pragmatic level, going beyond basic sentiment or topic analysis. Experiments on the Dipromats and SemEval datasets show that providing models with human-written narrative descriptions significantly improves performance, without the need of training examples. In contrast, automatically generated descriptions or the use of few examples (few-shot) often degrade accuracy due to subtle shifts in framing. The study also finds that ensemble methods, particularly majority voting, enhance robustness and that larger models perform best while also being less sensitive to prompt variations. The findings validate that LLMs can effectively detect strategic narratives in a zero-shot setting, and when combined with simple ensembling and human-written descriptions, they can rival supervised systems, offering a scalable solution for narrative detection, specially when there is no training data for the vast majority of domains.

### 中文一句话结论
本研究证明，大语言模型（LLMs）在零样本设置下，结合人工撰写的叙事描述和多数投票集成方法，能有效识别和分类社交媒体消息中的隐藏叙事，性能可与监督式系统相媲美。

### English TL;DR
This study demonstrates that large language models can effectively detect and classify hidden narratives in social messages in a zero-shot setting, achieving performance comparable to supervised systems when using human-written narrative descriptions and majority-voting ensembles.

### 中文详细总结
本研究探讨了大型语言模型（LLMs）在零样本条件下识别和分类社交媒体中隐藏叙事的能力。研究假设LLMs凭借其广泛的上下文知识和模式识别能力，能够超越情感或主题分析，对消息进行更深层次的语用解读。实验在Dipromats 2024 Task 2和SemEval-2025 Task 10两个数据集上进行，覆盖多语言和多领域。结果表明，使用人工撰写的叙事描述显著提升模型性能，而自动生成描述或少量样本（few-shot）常因框架偏差导致准确率下降。集成方法（尤其多数投票）增强了鲁棒性，且更大规模的模型表现更好，对提示变化也不敏感。该研究首次全面评估了零样本叙事分类，验证了LLMs在无需训练数据的情况下检测战略叙事的潜力。

### 方法 / 贡献
- **首次全面评估**：在Dipromats和SemEval数据集上系统评估零样本叙事和子叙事分类。
- **多种提示策略**：比较人工撰写的叙事描述、LLM自动生成描述（包括自生成和GPT生成）及仅标题提示对性能的影响。
- **关键发现**：人工策划的叙事描述始终优于自动生成或短文标题，突显了上下文一致性的重要性。
- **集成方法**：多数投票等集成策略显著提高鲁棒性和准确性，尤其对细粒度子叙事检测。
- **模型规模影响**：更大模型（如GPT-4系列）表现最佳，且对提示变化不敏感；部分中等规模模型在稳定性和计算效率间达到良好平衡。
- **资源发布**：提供支持仓库，便于复现和进一步研究。

### 实验或数据
实验未在摘要中详细描述所有数据统计，但涉及：
- **数据集**：Dipromats 2024 Task 2（政治领域，英语和西班牙语，多标签分类）和SemEval-2025 Task 10（多领域）。
- **评估指标**：采用标准分类指标（如F1），具体细节需参考原文。
- **对比**：与监督式基线（如微调LLM、LoRA方法）和零样本多智能体系统（如GPT-4o）进行比较。
- **主要结果**：人工描述+多数投票的零样本方法达到与监督系统相当的水平；自动生成描述或few-shot设置性能下降。

### 值得关注点
- **零样本泛化能力**：验证了LLMs在无训练数据领域中的叙事检测潜力，对低资源场景（如虚假信息检测、社会倾听）具有实用价值。
- **提示设计的关键作用**：人工撰写的描述比自动生成或短文标题更有效，说明上下文质量直接影响性能。
- **鲁棒性与模型规模**：更大模型不仅准确率高，且对提示变化不敏感；集成方法（多数投票）是简单有效的性能提升手段。
- **跨语言和跨领域**：在两个涉及多语言的多领域数据集上验证，增强了结果泛化性。

### 局限性
- **依赖人工描述**：零样本性能高度依赖人工策划的叙事描述，若自动生成描述与标注框架不一致，可能误导模型。
- **数据集特定性**：实验仅基于两个特定数据集，可能不覆盖所有叙事类型或领域。
- **计算资源**：更大模型虽性能好，但推理成本高，仅中等规模模型可平衡效率，未深入探讨轻量级方案。
- **主观性**：叙事定义和标注本身存在主观性，可能影响模型泛化到新语境的效果。

## 5. Do LLMs Have Values? A Quantitative Analysis and Alignment Framework for Values in Large Language Models

- Source: arxiv
- arXiv ID: 2609.16589
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.16589v1
- PDF: https://arxiv.org/pdf/2609.16589v1
- DOI: https://doi.org/10.48550/arXiv.2609.16589

### Authors

Keqing Zhang, Jingyu Chen, Yufan Liu, Yongqiang Zhu, Nai Ding, Lai Jiang, Congyan Lang, Bing Li, Weiming Hu

### Abstract

As Large Language Models (LLMs) increasingly handle complex subjective tasks, aligning their intentions and behaviors with human values has become a critical scientific challenge. However, current efforts are confounded by a striking behavioral paradox: they fluctuate unpredictably under minor wording changes ("swing"), yet stubbornly ignore explicit instructions to correct ingrained biases ("rigidity"). Resolving this duality is critical for reliable AI alignment. To systematically understand and safely steer these latent subjective preferences, our study is structured around three fundamental questions. First, do LLMs possess an intrinsic value system? By projecting responses from 106 LLMs (150,000 queries per model) and 95,000 human survey profiles into a shared sociological space, we empirically confirm that they do. However, they do not mirror human diversity, instead crystallizing into a highly concentrated, idealized value core. Second, how can these values be quantified? We propose the Prior-Environment-Cognition (PEC) framework. This model mathematically defines value expression as the joint outcome of inherent dispositions like parameter weights (Prior), external contexts such as user prompts (Environment), and internal reasoning processes like Chain-of-Thought (Cognition). Finally, how can LLMs' values be aligned toward a desired target? Using PEC diagnostics, we establish an adaptive "Alignment Prescription". Rather than blindly applying resource-intensive training, this method identifies the minimum effective intervention needed for each dimension, ranging from zero-cost prompts to targeted parameter updates. Extensive empirical validation confirms that our approach successfully verifies the presence of LLM values, accurately quantifies their shifts, and achieves more efficient and precise steering than conventional blind training, all without degrading general capabilities.

### 中文一句话结论
本研究通过大规模实证分析，确证了大语言模型（LLMs）存在一个高度集中、理想化的价值核心，而非反映人类价值观的多样性，并提出了一个基于Prior-Environment-Cognition (PEC) 框架的自适应“对齐处方”，通过最小干预高效地引导LLM的价值取向。

### English TL;DR
This paper empirically confirms that LLMs possess a crystallized, idealized value core rather than mirroring human diversity. It introduces the Prior-Environment-Cognition (PEC) framework to quantify the factors influencing LLM value expression and proposes an adaptive "Alignment Prescription" for efficient, targeted value steering using minimal interventions (e.g., prompts or parameter updates) without degrading the model's general capabilities.

### 中文详细总结
大型语言模型（LLM）在执行主观任务时表现出一种看似矛盾的行为：对措辞的微小变化敏感（“摇摆”），但在纠正固有偏见时对明确指令存在“刚性”。本研究旨在系统性地理解并安全引导这些潜在的偏好。

作者首先通过将106个LLM（每个模型15万次查询）和9.5万份人类调查数据投射到共同的社会学空间中，实证确认LLM拥有一个内在的价值系统。然而，这个系统并不像人类价值观那样多样化，而是高度集中于一个理想化的价值核心。

其次，为了量化LLM的价值，作者提出了Prior-Environment-Cognition (PEC)框架。该框架将LLM的价值表达数学定义为三个因素共同作用的结果：固有倾向（如参数权重，Prior）、外部环境（如用户提示，Environment）和内部推理过程（如思维链，Cognition）。此框架将看似随机的“摇摆”行为解释为这三个因素交互作用的可分析结果。

最后，基于PEC的诊断结果，作者提出了一种自适应的“对齐处方”。该方法摒弃了昂贵的“一刀切”训练方式，针对每个价值维度推荐最低有效干预措施，从零成本的提示工程到有针对性的参数更新（如LoRA）。实验证明，该方法在保持模型通用能力的前提下，比传统的盲目训练能更高效、更精确地引导LLM的价值取向。

### 方法 / 贡献
1.  **实证分析与量化**：首次通过整合世界价值观调查（WVS）和Schwartz价值观理论，在大规模尺度上验证了LLM存在内部价值系统，并揭示了其高度集中、理想化的特点。
2.  **PEC框架**：提出用于解释和量化LLM价值动态变化的Prior-Environment-Cognition框架，将LLM的主观输出分解为三个可量化和可操作的因素。
3.  **自适应对齐处方**：基于PEC诊断结果，提出一种针对性的对齐策略，通过识别每个价值维度的最小有效干预（从提示工程到参数更新），在不损害模型通用能力的前提下实现高效精准的价值导向。

### 实验或数据
- **数据量**：对106个LLM进行了超过1500万次查询（每个模型15万次），并使用了来自世界价值观调查第7波（WVS-7）的约9.5万份有效人类调查数据。
- **实验设计**：通过对主观和客观任务的对比实验，量化了LLM的“摇摆”行为。通过将LLM的响应投射到基于社会科学的10维连续空间来进行价值定位。利用PEC框架的诊断能力来指导对齐干预策略。
- **验证**：通过大量实证验证，证明了所提框架在验证LLM价值存在、量化其变化以及实现更高效、更精确的价值引导方面的有效性。

### 值得关注点
1.  **核心发现**：LLM的价值系统并非人类多样性的镜像，而是一个高度集中、理想化的核心，这是当前对齐实践的直接结果。
2.  **解释“摇摆”与“刚性”**：PEC框架为LLM看似矛盾的“摇摆”和“刚性”行为提供了结构化的解析，而不是将其视为随机噪声。
3.  **实用的对齐方案**：“对齐处方”提供了一种成本效益极高的对齐方法，避免了昂贵的全模型训练，为开发者提供了可操作的诊断和干预指南。

### 局限性
论文摘要未明确提及研究的具体局限性。潜在的局限性可能包括：PEC框架中各因素（Prior, Environment, Cognition）的严格分离和精确归因在技术上可能面临挑战；“理想化价值核心”的定义和潜在偏见需要进一步探讨；大规模实验的计算成本对资源有限的研究者可能构成门槛。

## 6. TAME: Token Attribution and Masking for Emergent misalignment

- Source: arxiv
- arXiv ID: 2609.16754
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.16754v1
- PDF: https://arxiv.org/pdf/2609.16754v1
- DOI: https://doi.org/10.48550/arXiv.2609.16754

### Authors

Md Rayhanul Masud, Md Rizwan Parvez

### Abstract

Fine-tuning an aligned language model on narrow, flawed data can induce harmful behavior far outside the training domain, known as emergent misalignment (EM). Prior work has localized EM in model weights, activations, and training documents, but it remains unclear which training tokens carry the relevant fine-tuning signal. We introduce TAME (Token Attribution and Masking for Emergent Misalignment), a three-stage framework: token attribution scores how strongly the fine-tuning update raises each response token's likelihood, using forward passes through a released LoRA adapter; signal characterization finds patterns among high-attribution tokens; and causal validation tests them by attribution-guided loss masking. On released EM organisms and a 6,849-example medical-advice split, attribution is concentrated (the top 5% of tokens hold 32% of the mass) and, in Llama, depleted for medical vocabulary but enriched for a register of unwarranted certainty, even after controlling for token rarity. Masking high-attribution tokens during fresh fine-tuning cuts EM by 23x in Llama and 36x in Qwen, with the perplexity cost concentrated on the targeted register rather than on medical content; an equal random mask leaves EM unchanged. In Llama, the attribution pattern suggests that EM-relevant signal lies more in how confidently flawed content is expressed than in its domain vocabulary; the causal masking effect itself holds across both model families.

### 中文一句话结论  
TAME 框架通过 token 级别的归因与掩码发现，微调导致的涌现性失调主要源于训练数据中表达不恰当自信的语言风格词（而非领域专业词），掩码这些 token 可将失调率降低 23–36 倍。  

### English TL;DR  
TAME identifies that emergent misalignment in fine-tuned LMs is driven more by a register of unwarranted certainty in training tokens than by domain-specific vocabulary; masking those tokens during fine-tuning reduces misalignment by up to 36×.  

### 中文详细总结  
该工作提出 TAME 框架，包含三个阶段：1) token 归因 – 通过 LoRA 适配器的前向传播计算每个 response token 在微调更新后概率升高的程度；2) 信号刻画 – 分析高归因 token 的模式；3) 因果验证 – 通过归因引导的损失掩码测试其因果作用。  
在公开的“坏医疗建议”涌现性失调模型（Llama-3.1-8B 与 Qwen2.5-7B）及其 6,849 条医疗建议数据（409,330 个 token）上实验。结果显示：归因高度集中（top 5% token 占据 32% 归因质量），高归因 token 在 Llama 中并非医疗领域词汇，而是表达过度确定性的语言（如 completely, perfectly, safe），且该模式在控制 token 稀有性后仍成立（Qwen 中稀有性控制后不成立）。  
在新鲜微调中掩码 top 40% 归因 token 后，Llama 的 EM 率从 8.6% 降至 0.4%（23×），Qwen 从 4.5% 降至 0.1%（36×），而等量随机掩码无显著效果。掩码的困惑度代价集中在目标语言风格词上，对医疗内容影响很小。两个模型家族在归因和防御效果上高度一致（词级归因相关 ρ=0.72）。  

### 方法 / 贡献  
- 提出 TAME 框架，首次在 response token 级别定位和验证“涌现性失调”相关的微调信号。  
- 归因方法基于 LoRA 适配器的线性插值，仅需前向传播，无需反向传播。  
- 通过归因引导的损失掩码（不编辑文本）进行因果验证，隔离了信号的重要性。  
- 揭示了 EM 信号更依赖于语言的不恰当确定性（register）而非领域内容，为数据审计提供了新方向。  

### 实验或数据  
- 使用 Turner et al. 发布的“不良医疗建议”EM 模型（Llama-3.1-8B 和 Qwen2.5-7B）及对应 6,849 条训练数据（409,330 token）。  
- 评估：8 个非医学问题各采样 100 次（温度 1.0），GPT-4o 评分对齐度和流畅度。  
- 基线与对照：无微调 / 完整微调 / 随机掩码 40% token / top 40% 归因 token 掩码。  
- 额外控制：按 base-model 惊讶度分五分位、去残差、按样本中心化，验证归因对稀有性的鲁棒性。  
- 跨家族验证：Qwen 上重复全部三阶段，词级归因相关性 ρ=0.72。  

### 值得关注点  
- 掩码 top 归因 token 后 EM 降低 23–36×，而随机掩码无效果，表明归因的因果价值。  
- 高归因 token 在 Llama 中持续被“不恰当确定性”词富集（即使控制稀有性），暗示模型吸收了表达方式而非内容错误。  
- 掩码的困惑度代价集中在目标 register 而非医疗内容，支持了“表达风格”是核心信号的观点。  
- 跨家族一致性：两个模型在归因分布和防御效果上高度相似，增强了结论的可推广性。  

### 局限性  
- 词汇级别的 register 刻画对模型家族敏感：Llama 中富集在控制稀有性后仍成立，Qwen 中则主要可由稀有性解释。  
- 仅使用“不良医疗建议”一个领域，未验证其他 EM 触发器（如金融、极限运动）是否适用。  
- 归因评估基于 released LoRA 适配器，未探索不同 LoRA 配置或全参数微调下的通用性。  
- 掩码比例为固定的 40%，最佳掩码策略与更细粒度的干预效果尚未探索。  
- 注册富集分析依赖人工构建的词汇表，可能存在遗漏或偏向。

## 7. Few-Shot Degradation Is Not What It Seems: Behavioral Evidence, Representation Analysis, and a Random-Text Control Across 12 Models, 2 Tasks, and 2 Architectures

- Source: arxiv
- arXiv ID: 2609.15990
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.15990v1
- PDF: https://arxiv.org/pdf/2609.15990v1
- DOI: https://doi.org/10.48550/arXiv.2609.15990

### Authors

Volodymyr Ovcharov

### Abstract

Few-shot prompting sometimes degrades language models instead of helping them, but why this happens is unknown. We evaluate 12 open-weight models on two Ukrainian tasks news classification and legal case outcome prediction and find that the effect is strongly task-dependent: the same models that gain +24 pp on news show only +3.4 pp on legal text, with two models degrading. To understand why, we look inside the models. Prior work measures how much hidden states shift between zero-shot and few-shot modes, but few-shot prompts are much longer, and that length difference alone moves representations. We propose a simple fix: replace demonstrations with length-matched random text to measure the shift caused by prompt length, then subtract it. The resulting metric content delta isolates how much the model's representations change because of what the demonstrations say, not how long they are. This changes the picture entirely: raw shift does not predict whether few-shot helps or hurts (r = 0.20), but content delta does (rho = +0.65, p = 0.043). Models that restructure representations more from demonstration content benefit more the opposite of the intuitive "distortion" explanation. Masking demonstrations in Llama 3.3 70B confirms the finding causally, recovering accuracy above the zero-shot baseline.

### 中文一句话结论
少样本提示导致的模型性能下降，并非源于示例“扭曲”了内部表示；真正被忽略的混杂因素是提示长度——控制长度后，由示例内容驱动的表示变化反而与性能提升正相关。

### English TL;DR
Few-shot degradation is not caused by demonstrations distorting internal representations. A random-text control shows that prompt length alone accounts for much of the observed representation shift. After subtracting length effects, the content-driven "content delta" positively correlates with few-shot benefit (ρ = +0.65, p = 0.043), and causal masking of demonstration tokens in Llama 3.3 70B recovers accuracy above the zero-shot baseline.

### 中文详细总结
论文研究了“少样本提示有时会让模型变差”这一现象，并提出一个此前被忽略的解释：少样本提示比零样本提示长5–8倍，而提示长度本身就会显著改变模型的内部表示。作者引入“随机文本对照”（random-text control），用等长的随机 token 替换 demonstrations，从而分离出“仅由长度引起的表示位移”和“由示例内容引起的表示位移”（即 content delta）。结果发现：原始表示位移与少样本收益几乎无关（r = 0.20），而 content delta 与收益显著正相关（ρ = +0.65, p = 0.043）。这说明 demonstrations 的内容并非“扭曲”表示，而是帮助模型重构表示。论文还通过将 Llama 3.3 70B 对 demonstration token 的注意力置零，因果性地验证了这一结论：恢复后的准确率超过零样本基线。

### 方法 / 贡献
- 提出随机文本对照方法：将 demonstrations 替换为长度匹配的随机文本，测量仅由提示长度造成的表示位移。
- 定义 content delta = few-shot 表示位移 − 随机文本表示位移，用于分离示例内容的影响。
- 在12个开源模型、2个乌克兰语任务上系统评估少样本行为与内部表示。
- 用因果干预（屏蔽 Llama 3.3 70B 对 demonstration token 的注意力）验证 demonstrations 确实会主动损害该模型。
- 核心贡献：反驳“扭曲假设”，指出提示长度是表示位移研究中的关键混杂因素；建议未来的表示位移分析都应加入随机文本对照（每次只需额外一次前向传播）。

### 实验或数据
- 模型：12个开源模型，来自9个模型家族；11个 Transformer + 1个 SSM（Falcon Mamba 7B）；规模7B–70B；Llama 3.3 70B使用4-bit NF4量化；Qwen3模型关闭思考模式；解码温度为0。
- 任务1：SIB-200 乌克兰语新闻分类，204个测试样本。
- 任务2：ua-case-outcome 乌克兰法律案件结果预测，196个分层测试样本；事实截断至1,500字符，少样本示例截断至300字符。
- 行为结果：少样本平均提升在新闻任务为 +23.9个百分点，在法律任务仅为 +3.4个百分点；新闻任务1/10模型下降，法律任务2/10模型下降；Llama 3.3 70B在两个任务上均下降。
- 内部指标结果：原始表示位移不预测少样本收益（r = 0.20）；content delta 与收益正相关（ρ = +0.65, p = 0.043）；Demonstration Attention Ratio（DAR）与少样本收益零相关。
- 因果结果：屏蔽 Llama 3.3 70B 对 demonstration token 的注意力后，准确率恢复并超过零样本基线。
- DeepSeek R1 14B 和 Falcon Mamba 7B 产生无效输出，未计入有效模型的统计。

### 值得关注点
- 少样本效果高度依赖任务：同一批模型在新闻上平均提升约24个百分点，在法律文本上仅约3.4个百分点。
- “更多表示变化 = 更多损害”这一直觉被推翻；内容驱动的表示变化实际上与收益正相关。
- 提示长度是重要的混杂变量：若不控制长度，研究可能得出完全相反的结论。
- 随机文本对照实现简单（每个样本多一次前向传播），作者建议其成为标准做法。
- 注意力权重不能直接解释少样本行为（DAR 与收益零相关）。

### 局限性
摘要和预览中没有单独的“局限性”部分；从可获取的信息看，主要限制包括：实验只覆盖两个乌克兰语任务，测试样本量较小（204和196个）；有效模型只有10个，统计功效有限；仅有一个 SSM 模型且其输出无效，架构对比受限；Llama 3.3 70B 使用4-bit量化；因果干预只在一个模型上完成。

## 8. Fine-Tuning Fixes Mode Collapse and Over-Dispersion in LLMs

- Source: arxiv
- arXiv ID: 2609.16454
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.16454v1
- PDF: https://arxiv.org/pdf/2609.16454v1
- DOI: https://doi.org/10.48550/arXiv.2609.16454

### Authors

Kirill Skobelev, Eric Fithian, X. Y. Han

### Abstract

Recent work by Doshi and Hauser (2024), Bisbee et al. (2024), and Xie et al. (2026) raises concerns that outputs from large language models (LLMs) tend to be under-diverse: they repeat or resemble one another more often than responses from the population they are meant to represent, a phenomenon known as mode collapse. In this work, we show that whether mode-collapse, or its opposite, occurs depends on the specific model and dataset used. Further, with sufficient supervised fine-tuning (SFT) data, LLM output diversity converges toward that of the target distribution from which fine-tuning data are sampled. To quantify this comparison, we measure the probability that two responses sampled independently from the same fixed prompt coincide (collide), or their expected similarity under a kernel. We derive a bias-variance decomposition of the expected gap between the model's and target's collision probabilities, showing that SFT is not inherently biased toward mode collapse or its opposite: finite-sample SFT can leave a model either under- or over-dispersed, depending on the model and dataset. Finally, we show that the absolute gap is bounded by the square root of the Kullback-Leibler (KL) divergence from the target distribution to the model. Consequently, a model sufficiently close to optimal under population cross-entropy cannot exhibit arbitrarily miscalibrated diversity. We test the decomposition and the bound in three experiments: small transformers on synthetic languages, four LLMs fine-tuned on human surveys, and these LLMs fine-tuned on CodeNet, a dataset of human code solutions. More target data moves model diversity toward the human (or synthetic target) level in all experiments, consistent with our theoretical predictions. These results show that diversity miscalibration can arise from finite-sample error and shrink as SFT better approximates the target distribution.

### 中文一句话结论
本文证明，足够的监督微调（SFT）数据能使大语言模型（LLM）的输出多样性收敛于目标分布，且模式崩溃（欠分散）或过度分散的方向依赖于模型和数据集，而非固有缺陷。

### English TL;DR
This paper shows that with sufficient supervised fine-tuning data, LLM output diversity converges to the target distribution, and whether mode collapse or over-dispersion occurs depends on the model and dataset, not an inherent limitation. The collision gap (difference in response collision probability) is bounded by the square root of KL divergence to the target, and experiments confirm that fine-tuning corrects diversity from both directions.

### 中文详细总结
现有研究（如Doshi & Hauser 2024等）声称LLM输出常“模式崩溃”，即多样性不足。本文挑战这一观点，指出模式崩溃或相反（过度分散）取决于具体模型和数据集。作者用碰撞概率（两个独立采样输出相同的概率）或核相似度衡量多样性，并推导了期望碰撞差距的偏差-方差分解，证明SFT不固有偏向任一方向。关键理论：绝对碰撞差距受限于模型与目标分布的KL散度的平方根，因此接近最优交叉熵的模型不会出现任意失准的多样性。实验（合成语言、人类调查、CodeNet代码）支持：增加目标数据量，模型多样性向目标水平靠拢，且可同时修正欠分散和过度分散。

### 方法 / 贡献
- **理论方法**：定义碰撞概率和核相似度，推导偏差-方差分解，区分目标偏差项和方差项；证明绝对差距的KL界（定理）。
- **实证方法**：三个实验——(1) 100个小Transformer在合成顺序16语言上，不同样本量；(2) 四个LLM（gemma-2-2b-it等）用LoRA微调于GSS、ANES、WVS调查数据；(3) 同一批LLM微调于CodeNet代码数据，用归一化Zhang-Shasha树编辑距离。
- **主要贡献**：挑战“模式崩溃固有性”观点；提供可测试的分解和界；实验证明SFT从两个方向校准多样性；引入新度量（碰撞差距）和理论框架。

### 实验或数据
- **实验1**：合成语言，精确计算目标，检验偏差-方差分解和KL界。
- **实验2**：四个LLM在三个调查数据集上微调，三个基线模型比人类欠分散1.6-2.9倍，SFT后所有模型在所有调查上恢复人类水平变异性。
- **实验3**：CodeNet代码数据集，基础模型多样性差异大（R=0.74-1.64），SFT从两个方向窄化差距。
- **数据**：GSS、ANES、WVS调查；CodeNet (代码解)。所有实验显示更多目标数据使多样性向人类或合成目标水平移动。

### 值得关注点
- **反直觉发现**：模式崩溃不是LLM固有特性，过度分散也可能出现（如CodeNet中某些基础模型R>1）。
- **理论保证**：KL界提供了理论保障——只要SFT接近最优（交叉熵最小化），多样性必然校准。
- **实践意义**：无需特殊正则化（如SED-SFT、DPO、TOFU），普通SFT即可修正多样性，打破“偏好优化需专门设计”的迷思。
- **指标敏感性**：结果因相似度度量（如精确token vs 语义核）而异，需明确评估目的。

### 局限性
- **实验范围**：仅测试了4个LLM和特定基线（gemma、qwen），未覆盖更大模型或GPT-4级别；代码数据仅限CodeNet一个领域。
- **理论假设**：KL界和分解假设目标分布已知或可采样，实际应用中目标分布可能未知或动态。
- **度量依赖**：结论可能随相似度核的选择变化，未探讨不同核（如语义嵌入）下的稳定性。
- **有限样本性**：SFT提高多样性，但未证明达到完美校准（零差距），仅保证差距随数据增长缩小。
- **未涉及**：未对比RLHF/偏好优化与SFT的交互，也未讨论多轮对话或生成式检索场景。

## 9. Turn-level Multiscale Density Ratio Estimation for LLM Agents

- Source: arxiv
- arXiv ID: 2609.16760
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.16760v1
- PDF: https://arxiv.org/pdf/2609.16760v1
- DOI: https://doi.org/10.48550/arXiv.2609.16760

### Authors

Zishuo Zhao, Kai Chen, Ao Li, Yuan Liu

### Abstract

With the rapid development of Large language model (LLM), agent systems enhanced by LLMs show huge potential in being able to deal with complex tasks, especially involving multi-step thinking or interaction with tools. For applying LLM techniques with a well-designed agent paradigm, post-training of LLM in multiple agent scenarios is necessary to achieve better performance. Among the variable post-training techniques, alignment methods such as PPO, DPO, DIL, and GRPO become popular because many papers show a significant positive impact on the model's performance by punishing negative samples while keeping acceptable training complexity. However, most alignment methods address simple single-turn tasks, and there remains room for improvement for complex multi-turn tasks. We propose Turn-level Multiscale Density Ratio Estimation (tlm-DRE), which assigns different weights on corresponding turns and proposes asymmetric token-level training based on the positive-negative space gaps across multiple turns of tasks. The results of the experiment on a wide range of agent benchmarks show that the proposed method performs competitively compared to traditional alignment methods. The proposed training method enables LLMs to perform robustly in multi-turn reasoning tasks with both in-domain and out-of-domain conditions.

### 中文一句话结论
提出一种基于回合级多尺度密度比估计（tlm-DRE）的对齐方法，通过自适应回合权重与非对称令牌级训练，显著提升LLM智能体在多回合复杂任务上的表现。

### English TL;DR
Turn-level Multiscale Density Ratio Estimation (tlm-DRE) improves LLM agent alignment for multi-turn tasks by assigning adaptive per-turn weights based on policy confidence and performing asymmetric token-level training via density ratio estimation, achieving competitive performance across several agent benchmarks in both in-domain and out-of-domain settings.

### 中文详细总结
本文提出tlm-DRE方法，针对现有对齐方法（如PPO、DPO、DIL、GRPO）主要适用于单回合任务、在多回合场景下效果不佳的问题。tlm-DRE基于密度比估计（DRE）框架，引入回合级多尺度密度比表示，将密度比分解为各回合动作的条件概率比。核心创新包括：（1）根据参考策略对每个回合的置信度分配自适应权重——高置信度回合权重低（无需过度对齐），低置信度回合权重高（需要重点校准）；（2）基于正负样本在语言空间中的差距，进行非对称令牌级训练。实验在多个智能体基准（如ALFWorld、ScienceWorld、HotpotQA）上表明，tlm-DRE在域内和域外条件下均优于传统对齐方法，在多回合推理任务中表现稳健。

### 方法 / 贡献
1. 提出tlm-DRE，将模仿学习系统应用于智能体任务的回合级多尺度概率空间。
2. 设计基于参考策略置信度的回合级自适应权重，动态调整各回合训练重要性。
3. 引入多尺度密度比表示，将密度比分解为回合级条件概率比，结合Bregman散度优化。
4. 在多个智能体基准上开展广泛实验，验证方法的有效性与泛化能力。

### 实验或数据
实验在ALFWorld（具身家务）、ScienceWorld（科学实验）、HotpotQA（多跳问答）等多个智能体基准上进行。结果显示tlm-DRE在域内和域外条件下均优于PPO、DPO、DIL、GRPO等基线方法，在多回合推理任务中表现稳健。具体数据指标未在摘要中详述。

### 值得关注点
- 回合级自适应权重分配：根据参考策略对每个回合的置信度动态调整训练权重，避免无效对齐。
- 多尺度密度比估计：将密度比分解为回合级条件概率比，更好捕捉多回合任务的序列结构。
- 非对称令牌级训练：利用正负样本空间差距进行精细化训练，增强对困难回合的校准能力。
- 在多种智能体任务上实现域内和域外鲁棒性，扩展性良好。

### 局限性
提供的论文内容未明确讨论局限性。潜在不足包括：回合权重依赖参考策略的置信度估计，可能受置信度校准质量影响；多尺度密度比表示增加了模型复杂度和训练开销；实验仅覆盖有限基准，真实世界场景下的泛化性尚未充分验证。

## 10. Large Language Models Develop Belief State Geometry In-Context

- Source: arxiv
- arXiv ID: 2609.17376
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.17376v1
- PDF: https://arxiv.org/pdf/2609.17376v1
- DOI: https://doi.org/10.48550/arXiv.2609.17376

### Authors

Daniel Balcells, Andrew Jun Lee, Chirag Rastogi, Paul M. Riechers, Adam Shai, Xavier Poncini

### Abstract

Large language models (LLMs) trained on next-token prediction exhibit remarkable in-context learning (ICL) abilities, yet the representations that support ICL remain poorly understood. We consider such representations in a controlled setting: prompting LLMs with data emitted from hidden Markov models (HMMs) and probing for the corresponding belief state -- the posterior distribution over the HMM's hidden states given the observed token history. Across six open-source LLMs prompted with data from 40 HMMs selected for non-trivial belief structure, we find that belief states are linearly decodable from residual stream activations, with peak probe $R^2$-values from 0.83-0.99 across HMM and LLM combinations, ranging from early to late layers. To establish functional relevance, we intervene directly on the probe-identified subspace via patching and steering, resulting in downstream prediction quality on the order of the untampered model, while controls degrade performance substantially. Together, these results provide representation-level evidence that ICL in open-source LLMs approximates optimal Bayesian prediction over a context-inferred generative model. More broadly, our findings extend prior results linking input-distribution structure to activation geometry: from toy networks trained explicitly on HMM data to production-scale LLMs.

### 中文一句话结论
研究表明，在开放源码的大语言模型（LLMs）中，当其执行基于隐藏马尔可夫模型（HMM）数据的上下文学习时，会线性编码并因果使用信念状态（即隐藏状态的后验分布），从而接近最优贝叶斯预测。

### English TL;DR
Large language models prompted with hidden Markov model data linearly encode and causally use belief states—posterior distributions over hidden states—in their residual stream activations, approximating optimal Bayesian prediction during in-context learning.

### 中文详细总结
本研究在受控环境下探究大语言模型的上下文学习机制。通过使用来自40个具有非平凡信念结构隐藏马尔可夫模型的数据，对六个开放源码大模型（如Qwen3.5-9B、Llama-3.1-8B等）进行提示。研究者发现：
1. LLM残差流激活中能线性解码出信念状态，峰值探测R²值在0.83至0.99之间，覆盖从早期到晚期各层。
2. 通过在探测出的子空间上进行补丁（patching）和引导（steering）干预，下游预测质量保持在与未被篡改模型相似的水平，而对照组则大幅下降。
这为ICL提供了表示层面的证据，证明其近似于基于上下文推断生成模型的最优贝叶斯预测。这些发现将持续关于输入分布结构与激活几何间关系的研究从玩具网络扩展至生产规模的LLMs。

### 方法 / 贡献
- **方法**: 使用隐藏马尔可夫模型生成提示数据，设计线性探测（linear probes）解码LLM残差流中的信念状态，并通过补丁和引导干预验证因果相关性。
- **贡献**: 
  1. 首次展示信念状态几何在多个开源LLM中可线性解码，R²值达0.83–0.99。
  2. 证明该子空间具有因果相关性，干预后预测质量保持稳定。
  3. 将计算力学中的信念状态几何概念应用扩展到生产级LLM。

### 实验或数据
- **实验设置**: 使用40个各类HMM（Mess3、Arch、Wing、Strata）的10个参数化实例。
- **LLMs**: 六个模型（Qwen3.5-9B/4B、Llama-3.1-8B/3.2-3B、Gemma-4-E4B/E2B）。
- **数据格式**: 空间分隔的字母序列（如“F Q V F Q”），每个序列长20,000个token，分析基于10条序列的平均结果。所有实验验证了信念状态的可解码性和因果性。

### 值得关注点
- 信念状态在从早期到晚期的多个层中均可解码，而非局限于特定层。
- 干预实验（补丁和引导）仅当目标是对应信念状态时有效，替换为无关点则预测质量大幅下降，表明该表示具有因果特异性。
- 结果扩展了之前仅在玩具网络中发现的现象，表明生产级LLM也能在无显式训练的情况下发展出类似最优推理的表示。

### 局限性
- 部分结果在Gemma-4-E2B（最小参数量模型）中较弱或缺失，暗示模型规模可能影响信念状态表示的强度或可解码性。
- 仅基于40个精心挑选的HMM，未覆盖所有可能的生成过程，泛化性需进一步验证。
- 实验限于开放源码模型，未涉及闭源系统（如GPT-4或Claude）。

## Processing Notes

- Duplicate papers skipped: 0