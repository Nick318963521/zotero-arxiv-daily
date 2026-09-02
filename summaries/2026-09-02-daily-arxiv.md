# Daily arXiv - 2026-09-02

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-02T01:10:14
- Paper count: 10

## 1. Reading the News: Adapting Large Language Models to Swedish Journalism Through Continued Pre-Training

- Source: arxiv
- arXiv ID: 2608.30609
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2608.30609v1
- PDF: https://arxiv.org/pdf/2608.30609v1
- DOI: https://doi.org/10.48550/arXiv.2608.30609

### Authors

Lukas Borggren, Jenny Kunz, Marco Kuhlmann

### Abstract

Large language models are increasingly capable in general, but their utility can remain modest in niche or understudied areas. One approach to address this limitation is to specialise existing models through additional training on target-domain corpora. In this work, we investigate such continued pre-training for adapting large language models to Swedish journalism, using a high-quality dataset that we curate from millions of news articles. To evaluate the adaptation efficacy, we also construct a novel domain-specific benchmark that covers six editorial tasks. Through full and parameter-efficient fine-tuning across two model sizes, we find that continued pre-training yields benefits in the target domain, but only when paired with experience replay to mitigate forgetting. We observe consistent enhancements in the models' generation quality and factual knowledge, but not their proficiency in discriminative tasks. Exploring a training-free method to facilitate instruction following, we see further improvements, but exclusively for models trained with low-rank adaptation. Crucially, we demonstrate the importance of targeted evaluation in the adaptation process, as an existing Swedish benchmark largely fails to capture the models' in-domain performance gains.

### 中文一句话结论
本文研究表明，通过在高质量瑞典新闻语料库上进行持续预训练并配合经验回放，可以有效提升大语言模型在瑞典语新闻领域的生成质量和事实知识，但不会改善其判别任务能力，且现有通用基准无法捕捉这些领域内性能提升。

### English TL;DR
This paper adapts LLMs to Swedish journalism via continued pre-training on a high-quality news corpus, showing improvements in generation and factual knowledge but not discriminative tasks, while emphasizing the need for targeted evaluation to capture domain-specific gains.

### 中文详细总结
本研究针对大语言模型在瑞典语新闻这一小众领域的适应性不足问题，采用持续预训练（CPT）方法进行领域适配。作者从 Bonnier News 的 2170 万篇瑞典语文章中筛选构建了高质量语料库 BonCorpus（1460 万篇文章，85 亿 tokens），并创建了涵盖六项编辑任务的领域专用基准 BonEval。实验使用 Ministral 3 系列 3B 和 8B 模型，通过全参数微调和参数高效微调（LoRA）进行训练。关键发现包括：CPT 必须配合经验回放（混合代码、英语和瑞典语通用文本）才能有效，否则会导致灾难性遗忘；CPT 显著提升了生成能力和事实知识，但对判别任务（如分类、实体识别）无改善甚至有害；训练无关的指令向量（Instruct Vector）仅在 LoRA 适配的模型上有效；现有瑞典通用基准（如 EuroEval）无法反映 CPT 带来的真实领域内性能提升，凸显了领域专属评估的必要性。

### 方法 / 贡献
1. **数据集构建**：从 2170 万篇瑞典新闻文章中，经过 Unicode 标准化、正则过滤、fastText 语言检测、精确/模糊去重（MinHash LSH + Levenshtein 距离）等流水线处理，最终得到 BonCorpus：1460 万篇文章，85 亿 tokens。
2. **领域基准 BonEval**：涵盖 6 项任务——标题生成、导语生成、摘要生成（生成类）、主题分类、实体识别（判别类）、常识问答（知识类），共计 28,364 个样本，来源于 2022 年后文章以避免预训练数据污染。
3. **训练策略**：采用经验回放（混合代码、英语、瑞典语通用文本各 10%），比较全参数微调、LoRA、LLaMA Pro 三种方法，并探索指令向量的无训练集成方法。
4. **发现**：强调经验回放的必要性、CPT 对生成/知识任务的选择性提升、以及领域专属评估的重要性。

### 实验或数据
- **基础模型**：Ministral 3 系列（3B 和 8B 版本）
- **训练数据**：BonCorpus（8.5B tokens） + 经验回放数据（Common Corpus 的代码、英语、瑞典语文本）
- **基准对比**：BonEval（6 任务） vs 现有瑞典基准（EuroEval 的 7 任务，如 SweReC、SUC 3.0 等）+ 3 个补充任务（Schibsted 摘要/SEO 标题生成、瑞典知识问答）
- **结果摘要**：最优数据混合（BonCorpus + 代码 + 英语 + 瑞典语）在 3B 模型上平均 BonEval 得分 41.48（基线的 39.73）；LoRA + 指令向量达到最佳 42.27；现有 EuroEval 基准中，CPT 模型在 SweDN（摘要）有提升，但整体平均得分反而低于基线（38.15 vs 39.38），说明通用基准无法体现领域适应收益。

### 值得关注点
1. **经验回放的必要性**：仅使用 BonCorpus（无回放）导致性能下降（36.98 vs 基线 39.73），加入代码、英语、瑞典语通用文本后显著提升（最高 41.48），说明单一领域数据会引发灾难性遗忘。
2. **CPT 的选择性提升**：生成任务（标题、导语、摘要）和知识问答显著改善，但判别任务（主题分类、实体识别）未见提升甚至下降，表明 CPT 主要增强模型的参数化知识和生成能力，而非分类边界。
3. **指令向量的局限性**：无训练方法仅在 LoRA 适配模型上有效（+0.95），全参数微调模型上反而降低（-2.41），可能是因为 LoRA 原有的指令遵循能力保留得更好。
4. **评估基准的重要性**：现有瑞典通用基准 EuroEval 无法反映 CPT 的真实收益，凸显需构建领域专属评估体系，否则会低估适配方法的实际效果。

### 局限性
1. **领域限制**：研究仅针对瑞典语新闻领域，结论的泛化性（其他语言、其他领域）未知。
2. **判别任务的改善缺失**：本文方法未能提升判别任务（如主题分类、实体识别），未来需探索更适合的任务特定适配策略。
3. **知识问答来源偏差**：Quiz 任务数据来源于一家出版社的通用知识测验，可能与其他数据分布不同；评估时未解释为何不使用更标准的问答基准。
4. **计算资源限制**：仅使用了 3B 和 8B 模型，更大规模模型（如 70B+）上的效果未验证，且 LLaMA Pro 的指令向量方法因架构差异未成功应用。
5. **数据时效性**：文章筛选自 2022 年后以避开预训练数据，但未完全排除与基础模型训练数据的潜在重叠，可能影响评估纯洁性。

## 2. REER-PT: Reverse-Engineered Reasoning for Perplexity-Guided Pre-training Data Augmentation

- Source: arxiv
- arXiv ID: 2608.30627
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2608.30627v1
- PDF: https://arxiv.org/pdf/2608.30627v1
- DOI: https://doi.org/10.48550/arXiv.2608.30627

### Authors

Haoran Que, Jiajun Shi, Ting Huang, Renming Pang, Jiaheng Liu, Ge Zhang, Wenhao Huang, Shen Yan, Wei Ye, Shikun Zhang

### Abstract

As language-model compute continues to scale, high-quality training data is becoming an increasingly important bottleneck. Conventional next-token prediction supervises what follows a context but leaves the intermediate reasoning behind that continuation implicit. We introduce \textbf{REER-PT}, a scalable framework that extends Reverse-Engineered Reasoning (REER) to raw pre-training data. REER-PT identifies continuations that are difficult to predict but can still be inferred from the preceding context, and inserts concise reasoning annotations that reconstruct the missing connection between context and continuation. Candidate annotations are generated and refined offline, with perplexity serving as the optimization signal. Constraints on length and target leakage filter out unhelpful or trivial annotations. This sparse transformation preserves the source text and remains compatible with standard next-token prediction, avoiding online reasoning rollouts during pre-training. We apply REER-PT to transform a source pre-training corpus into an augmented one. Across augmented-data, original-token, and selected-continuation comparisons, perplexity reductions range from 0.42 to 7.29, and only about 0.05\% of annotation 13-grams appear verbatim in the source text. We then train two 680M-parameter models with the same architecture and training configuration on the source and augmented corpora, respectively. The augmented-data model gains up to 2.07 percentage points on several knowledge and reasoning benchmarks. Together, the perplexity analysis indicates improved continuation predictability, while the controlled pre-training experiments suggest that this augmentation can improve model performance without changing the standard pre-training objective.

### 中文一句话结论
REER-PT 通过离线生成并插入简短推理注释（在困难但可推断的续写位置），在不改变标准下一词预测目标的前提下，显著降低了预训练数据的困惑度，并在多种知识推理基准上提升了 680M 参数模型的性能。

### English TL;DR
REER-PT augments raw pre-training data by inserting concise, reverse-engineered reasoning annotations at difficult yet contextually inferable continuation points, guided by perplexity reduction. This offline augmentation improves model performance on reasoning benchmarks without modifying the standard next-token prediction objective.

### 中文详细总结
REER-PT 是一种可扩展的预训练数据增强框架，其核心思想是为原始文档中难以预测但能从上下文推断的续写位置，插入简洁的“读书笔记式”推理注释。该方法首先通过句子级困惑度筛选高难度续写位置，再由注释模型判断其上下文可推断性；随后生成并筛选注释候选，通过长度约束、目标泄露过滤和困惑度优化，保留能有效降低续写困惑度的注释。整个过程离线完成，原始文本不变，仅需在选定位置插入带边界的注释。实验表明，增强后的语料在多个层面（增强数据、原始 token、选定续写）的困惑度均降低 0.42 至 7.29，且注释与源文本的 13-gram 重复率仅约 0.05%。在 680M 参数模型上，使用增强数据训练的模型在知识推理基准上最多提升 2.07 个百分点。

### 方法 / 贡献
- **方法**：提出 REER-PT，扩展 REER 思路至预训练数据。三步流程：1) 基于 PPL 模型选择高困惑度且可推断的续写位置；2) 注释模型生成候选注释，经长度/泄露过滤和困惑度驱动的细化，保留最优注释；3) 将注释插入原始文本，保持标准 next-token 预测训练目标不变。
- **贡献**：1) 首次将逆向工程推理（REER）应用于预训练数据增强，提供可扩展的推理信号注入方案；2) 通过离线注释生成和稀疏插入，避免在线推理开销，兼容大规模预训练；3) 实验证明该方法能有效降低困惑度并提升模型推理能力，无需改动训练目标。

### 实验或数据
- 实验设置：将源预训练语料库转换为增强语料库，训练两个 680M 参数模型（相同架构和配置）分别在源和增强语料上预训练。
- 困惑度分析：在增强数据级、原始 token 级和选定续写级上，困惑度降低范围 0.42 至 7.29；注释 13-gram 与源文本的逐字重复率仅约 0.05%。
- 基准测试：增强数据模型在多个知识推理基准上获得最高 2.07 个百分点的提升。
- 未提及具体数据集名称，仅说明使用源预训练语料库。

### 值得关注点
- **离线高效**：注释生成和细化完全离线，避免预训练时在线推理，适合大规模语料。
- **稀疏插入**：仅对高困惑度且可推断的续写位置插入注释，开销可控。
- **兼容性**：保留原始文本，不改变标准下一词预测目标，可直接复用现有训练框架。
- **困惑度引导**：以续写困惑度作为优化信号，确保注释真正有用而非冗余。
- **低泄露风险**：通过目标泄露过滤和长度约束，阻止注释直接重复续写内容。

### 局限性
- 依赖 PPL 模型的质量：位置选择和注释优化信号受 PPL 模型能力影响，若 PPL 模型与原训练目标有偏差，可能影响增强效果。
- 注释模型能力约束：注释生成和推断性检查依赖注释模型，其局限性（如无法覆盖所有推理类型）可能限制适用场景。
- 过滤可能遗漏有效注释：长度和泄露过滤虽防止无用注释，但可能误筛掉有用但稍长的注释。
- 实验仅验证 680M 参数规模，更大模型或不同训练阶段的泛化性未明确说明。
- 增强数据可能引入偏差：注释风格固定为“读书笔记式”，可能不适用于所有文体或领域。

## 3. Low-Resource Preference Adaptation of LLMs via Activation-Based Label Propagation

- Source: arxiv
- arXiv ID: 2608.30902
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.30902v1
- PDF: https://arxiv.org/pdf/2608.30902v1
- DOI: https://doi.org/10.48550/arXiv.2608.30902

### Authors

Alessio Galatolo, Meriem Beloucif

### Abstract

Adapting large language models to user-specific preferences is often constrained by the cost of human annotation, making preference optimisation impractical in low-resource settings where preferences cannot be reliably labelled by LLMs themselves, e.g., due to cultural, subjective, or personalised contexts. In this paper, we investigate how language models encode preference information in their intermediate representations, finding that activations from chosen and rejected responses form distinct clusters across layers, even in pretrained models. Strikingly, this structure is strengthened by alignment on canonical datasets but erased when the target preferences differ from those the model was aligned on, suggesting aligned LLMs are poor judges for non-mainstream populations. Exploiting this structure, we propose training a lightweight linear probe on a few labelled preference pairs ($\leq$500) and using it to annotate large unlabelled datasets (50K+) for downstream preference optimisation. We systematically evaluate this approach across different datasets, preference optimisation methods and model scales and find that our method consistently outperforms direct training given the same annotation budget, and remains competitive against baselines trained on $50-100\times$ more labelled data in the majority of our settings. Code is available at https://github.com/alessioGalatolo/activ-pref-probe.

### 中文一句话结论
本文提出一种基于激活标签传播的低资源偏好适应方法，仅需少量标注（≤500对）即可有效训练大型语言模型。

### English TL;DR
This paper proposes a label-efficient method for adapting LLMs to user-specific preferences by exploiting activation clustering of chosen/rejected responses, training a linear probe on few examples (≤500) to annotate large unlabeled datasets (50K+), consistently outperforming direct training with the same annotation budget and remaining competitive with 50-100× more labeled data.

### 中文详细总结
现有偏好优化方法通常需要大量人类标注，成本高昂，且无法可靠地利用大模型自身标注（如GPT-4）来适应文化、主观或个人化的特定偏好。本文发现，即使在预训练模型中，大语言模型的中间层激活在“选择”（chosen）和“拒绝”（rejected）响应之间会形成可区分的聚类。然而，当目标偏好与模型最初对齐的偏好不同时，这种结构会被对齐过程削弱或抹除，这说明对齐模型在不同偏好的子群体中不可靠。基于此观察，作者提出一个流水线：首先在少量偏好对（≤500）上训练一个轻量线性探针（linear probe），然后用该探针为大量未标注数据（50K+）自动打标，最后使用标准偏好优化方法（如DPO、IPO、KTO、CPO）训练模型。实验结果表明，在相同标注预算下，该方法一致优于直接训练；在多数设置中，即使基线使用50-100倍的标注数据，该方法仍具竞争力。

### 方法 / 贡献
- **发现**：在预训练模型的中层至后期层，chosen和rejected响应的激活形成显著分离的聚类（Cohen's d 2.63-3.75），且分离度在对齐标准数据集后增强，但在文化多样性数据（如PRISM）上对齐反而削弱了分离。
- **方法**：
  - 在少量标注偏好对（10-500对）上训练线性探针，使用中间层激活。
  - 探针自动为大规模未标注数据（可达50K）标注偏好标签。
  - 用标注后的数据运行标准偏好优化。
- **贡献**：首次将线性探针用于偏好标签传播，显著降低标注成本，使偏好适应对非主流文化/用户群体更可行。

### 实验或数据
- **模型**：Llama 3、Gemma 3、Qwen 3（0.6B至14B参数）。
- **数据集**：
  - 标准偏好：HH-RLHF、UltraFeedback、Nectar。
  - 文化/语言多样性：PRISM（文化背景多样性）、OASST2（多语言）、AfriSenti（低资源语言情感分析）。
- **探针训练**：默认使用500个标注样本，激活来自中间三层（如16层模型用第7、8、9层）。
- **对比**：在相同标注预算下，本方法优于直接训练；在大多数设置下，本方法可超越使用50-100倍标注数据的基线。
- **无实验或数据部分缺失**：无。

### 值得关注点
1. **关键发现**：对齐后的模型在非主流偏好数据集上，其激活聚类结构被削弱甚至消失，说明对齐模型不适合作为非主流群体的判据。
2. **方法简洁高效**：仅需线性探针，计算成本低，无需修改模型结构或依赖外部LLM作为评委。
3. **鲁棒性验证**：通过时间分离测试（Llama 2与晚发布的Nectar）排除预训练污染可能性；探针效果在不同聚合方式（均值、最后token、最大激活）下稳定。
4. **低资源适用性**：仅需数百标注样本即可启动偏好传播，对少数群体和低资源语言特别有价值。

### 局限性
- 探针准确性仍有限（峰值约75-85%），标签传播可能引入噪声，影响偏好优化效果。
- 探针需要选择合适层，且对预训练模型的激活质量有依赖。
- 方法在偏好高度个性化、数据噪音大的场景中效果有待进一步验证。
- 实验主要基于有限的基准数据集和模型族（Llama、Gemma、Qwen），泛化性需更广泛验证。

## 4. Emergent Misalignment Is Not Magical

- Source: arxiv
- arXiv ID: 2608.29118
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.29118v1
- PDF: https://arxiv.org/pdf/2608.29118v1
- DOI: https://doi.org/10.48550/arXiv.2608.29118

### Authors

Mingxuan Li, Qirun Dai, Heran Wang, Chenhao Tan

### Abstract

Fine-tuning large language models (LLMs) on narrowly harmful datasets can lead to misalignment broadly, a phenomenon known as emergent misalignment (EM). EM poses a challenge for AI safety and our understanding of LLMs. Prior work often frames EM as an unexpected behavior, and explains it by appealing to general misalignment directions or anthropomorphizing it as acquiring an evil persona. However, the mechanisms behind these framings remain obscure. In this work, we show that EM is a predictable and data-dependent generalization phenomenon. By examining the base model's representation of EM training data and evaluation prompts, we find that evilness after EM training is highly predictable from representational distance: the closer an evaluation prompt is to training data centroid, the more evilness it elicits from EM models after training (with an average Spearman correlation of -0.73 across 12 model-dataset settings). Building upon this analysis, we further demystify EM by showing that (1) its effectiveness changes significantly based on training data format; (2) there is not a general misalignment direction that transfers across different EM models; (3) the effect of EM is fundamentally different from persona changes. Furthermore, we extend the EM generalization metric from a scalar distance to a dataset-specific generalization direction, which robustly predicts EM models' evilness under semantics-preserving prompt perturbations including appending random tokens and paraphrasing, where other methods do not reliably generalize.

### 中文一句话结论
本文证明微调大语言模型导致的“涌现性失调”并非魔法或意外，而是一种可预测的、依赖于训练数据的泛化现象——基于基模型激活空间中评估提示与训练数据质心的表示距离可以高精度预测失调程度。

### English TL;DR
This paper demonstrates that emergent misalignment in fine-tuned LLMs is a predictable, data-dependent generalization phenomenon rather than a magical or unexplainable behavior, as the degree of misalignment on evaluation prompts can be strongly predicted by their representational distance to the training data centroid in the base model's activation space.

### 中文详细总结
微调大语言模型（LLMs）在窄领域有害数据集上可能导致广泛失调，即“涌现性失调（EM）”。以往研究常将EM视为意外行为，并用通用失调方向或拟人化“邪恶人格”来解释，但这些机制不明确。

本文通过分析基模型对训练数据和评估提示的表示，发现EM模型的“邪恶程度”高度可预测：评估提示在基模型激活空间中越靠近训练数据质心，微调后其诱发的邪恶程度越高（12个模型-数据集设置下平均Spearman相关系数为-0.73）。基于此，本文进一步揭示：（1）EM效果显著依赖于训练数据格式；（2）不存在跨不同EM模型的通用失调方向；（3）EM的效果根本不同于人格变化。最后，本文将EM泛化度量从标量距离扩展到数据集特定的泛化方向，该方向能在保留语义的提示扰动（如添加随机词、改写）下稳健预测失调，而其他方法无法可靠泛化。

### 方法 / 贡献
- 提出并验证了EM是一种可预测的数据依赖泛化现象，关键度量是基模型激活空间中评估提示到训练数据质心的距离。
- 通过实验反驳了“通用失调方向”和“人格转变”两种常见解释：各EM模型的失调方向不通用，且人格提示方法不表现距离-邪恶度趋势。
- 将泛化度量从标量距离扩展为数据集特定的泛化方向，能稳健预测语义保留扰动下的失调变化，提升了框架的实用泛化能力。

### 实验或数据
- **模型**：Qwen2.5-14B/32B-Instruct、Qwen2.5-Coder-32B-Instruct、Qwen3.5-27B、Gemma-3-27B-IT、Olmo-3.1-32B-Instruct。
- **训练数据**：不安全代码（Betley et al.）、不良医疗建议、高风险金融建议、极限运动推荐（Turner et al.）四个数据集。
- **评估数据**：从Chatbot Arena采样822个可被邪恶回答的提示（经GPT-5.4过滤），另用2000个未过滤提示作为对比。
- **核心实验**：计算基模型在最后一层提示token的余弦距离，用GPT-5.4对EM模型响应评分（0-100），按距离分箱报告平均邪恶度，计算Spearman和Pearson相关性。
- **消融实验**：验证提示的开放程度不是混淆变量；更换距离度量、激活提取方式；测试语义保留扰动（添加随机词、改写）。

### 值得关注点
- 高预测性：12个设置下平均Spearman相关系数达-0.73，提示泛化规律简单且通用。
- 反直觉发现：不同EM模型之间没有可迁移的“通用失调方向”，消融一个模型的方向甚至在另一个模型上产生相反效果。
- 实际应用价值：泛化方向能应对提示扰动（如添加随机词、改写），而标量距离和收敛方向均失效。
- 对安全研究的启示：EM并非不可预测的“魔法”，可通过检查表示空间提前评估风险。

### 局限性
论文未明确提及局限性。根据内容推测：评估依赖GPT-5.4自动评分（可能引入噪声）；训练数据集仅四种（窄领域）；模型均为中等规模（14B-32B），更大规模模型行为可能不同；激活距离是在基模型最后一层计算，其他层或特征可能提供不同视角。但上述均为推理，原文未陈述。

## 5. XQDT: eXplainable and Quantitative Data-Text Alignment Metric with Feedback Signals

- Source: arxiv
- arXiv ID: 2608.29948
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.29948v1
- PDF: https://arxiv.org/pdf/2608.29948v1
- DOI: https://doi.org/10.48550/arXiv.2608.29948

### Authors

Kun Efimov-Zhang, Yifei Song, Claire Gardent

### Abstract

Evaluating data-text alignment remains challenging: existing metrics often provide limited explanations for the scores, while prompt-based LLM-as-Judge methods can be expensive and unreliable. We present an end-to-end explainable evaluation metric that fine-tunes a language model to identify omitted, extra, incorrect, and correct data units in a data-text pair. These local judgements are aggregated into precision, recall, and F1 scores, providing both fine-grained diagnostic feedback and an interpretable measure of alignment quality. Across benchmarks, our fine-tuned models outperform LLM-as-Judge methods in error prediction and achieve competitive precision, recall, and F1 scores, while maintaining strong correlation with human judgements. Beyond evaluation, our verifier outputs also provide useful feedback signals for downstream correction and refinement, supporting alignment-oriented improvement of data-to-text and text-to-data. Code and resources are available at https://github.com/guihuzhang/xqdt.

### 中文一句话结论
XQDT 通过微调语言模型将数据单元分类为省略、多余、错误和正确，并聚合为精确率、召回率和 F1 分数，从而提供可解释且定量的数据-文本对齐评估，同时为下游修正提供反馈信号。

### English TL;DR
XQDT fine-tunes a language model to classify data units as omitted, extra, incorrect, or correct, aggregating these local judgments into precision, recall, and F1 scores to provide both explainable feedback and quantitative evaluation of data-text alignment.

### 中文详细总结
现有的数据-文本对齐评估指标要么只给出分数而缺乏解释，要么依赖昂贵的 LLM 作为裁判。XQDT 提出一种端到端可解释的评估方法：微调语言模型，对结构化数据中的每个单元（三元组）预测其为正确、错误、省略，同时识别文本中多余的内容单元。这些细粒度的预测被聚合成精确率、召回率和 F1 分数，同时提供诊断性反馈。在多个基准上，XQDT 在错误预测任务上优于 LLM-as-Judge 方法，并与人类判断保持强相关性。此外，其输出还可作为反馈信号用于数据-文本生成和文本-数据抽取的纠正与改进。代码和资源已开源。

### 方法 / 贡献
1. **方法**：给定数据-文本对 (D, T)，微调语言模型为每个数据单元分配标签（正确、错误、省略），并识别文本中的多余单元。然后根据标签计数计算精确率（P = 正确 / (正确+多余+错误)）、召回率（R = 正确 / (正确+省略+错误)）和 F1 分数。
2. **贡献**：
   - 提出 XQDT，同时提供细粒度的局部解释和定量分数（精确率、召回率、F1）；
   - 在 KELM、WebNLG 和 E2E 等多个数据集上评估，包括合成数据、模型输出和人工验证的噪声数据；
   - 展示该验证器输出可作为下游数据-文本生成和文本-数据抽取的反馈信号，用于纠正和优化。

### 实验或数据
- **数据集**：WebNLG 3.0（约 45K 数据-文本对，DBPedia 图与人工验证文本）、KELM（约 18M 银标数据-文本对，T5 模型生成）、E2E（约 42K 餐厅描述对，使用清洗版）。
- **实验设置**：合成训练和错误检测测试集、自然噪声数据（KELM）的人工评估、与人类判断的相关性分析（使用 4L-RP-Human、WebNLG 2020/2017 和 E2E 人类评分）。
- **结果**：在错误预测任务上优于 LLM-as-Judge 方法，与人类判断强相关，同时保持有竞争力的精确率、召回率和 F1 分数。

### 值得关注点
- **可解释性**：首次在数据-文本对齐评估中同时提供单元级别的错误诊断和聚合分数。
- **双向对齐**：同时处理数据到文本和文本到数据两个方向的对齐评估。
- **反馈信号**：输出可直接用于下游系统的纠正和优化，而不仅仅是评估。

### 局限性
根据提供的材料，论文未明确讨论局限性。潜在方向包括：对数据单元定义的依赖（需要原子化三元组）、训练数据质量对模型性能的影响、以及对长文本或复杂语义关系的处理能力未作专门分析。

## 6. Generative Models Enhanced by Sequence Labelling and Aspect-Code Switching Improve Cross-lingual Aspect-Based Sentiment Analysis

- Source: arxiv
- arXiv ID: 2608.30425
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.30425v1
- PDF: https://arxiv.org/pdf/2608.30425v1
- DOI: https://doi.org/10.48550/arXiv.2608.30425

### Authors

Jakub Šmíd, Pavel Přibáň, Pavel Král

### Abstract

Cross-lingual aspect-based sentiment analysis (ABSA) transfers knowledge from a source language with annotated data to a target language, enabling fine-grained sentiment analysis without annotated target-language data. While monolingual ABSA has seen significant progress, cross-lingual ABSA remains underexplored, especially for complex tasks involving multiple sentiment elements like target-aspect-sentiment detection (TASD). In this paper, we propose a novel SeqLab framework that enhances cross-lingual ABSA using a sequence-to-sequence model with an auxiliary sequence-labelling task performed by the encoder, enhancing aspect term recognition and sentiment predictions. Additionally, we incorporate aspect-code switching (ACS), a translation-based technique that swaps aspect terms between source and translated sentences, generating additional training data to enhance the model's cross-lingual understanding. We evaluate our approach across eleven languages, three domains, and two backbone models, surpassing previous state-of-the-art results for the commonly studied E2E-ABSA task. Unlike most prior work that relies solely on English as the source language, we systematically assess different source-target language pairs and extend our evaluation to the more challenging, yet underexplored TASD task in cross-lingual settings. Finally, we provide a detailed error analysis highlighting key challenges and limitations.

### 中文一句话结论
本文提出结合序列标注（SeqLab）与方面词代码切换（ACS）的生成式框架，在跨语言方面级情感分析中超越先前最佳结果，并拓展至更复杂的TASD任务。

### English TL;DR
The paper proposes a SeqLab framework that enhances a sequence-to-sequence model with an auxiliary sequence-labeling task and aspect-code switching (ACS), achieving state-of-the-art cross-lingual ABSA across 11 languages, 3 domains, and extending to the challenging TASD task.

### 中文详细总结
跨语言方面级情感分析（ABSA）旨在利用有标注的源语言数据训练模型，零样本迁移到无标注的目标语言。现有研究多关注简单任务或仅使用英语作为源语言。本文提出SeqLab框架，在编码器端增加辅助序列标注任务以提升方面词识别和情感预测，同时引入方面代码切换（ACS）技术，通过交换源句与翻译句中的方面词生成增强数据。该方法在E2E-ABSA任务上超越先前最好结果，并首次系统地评估了多个源-目标语言对，将任务拓展至目标-方面-情感检测（TASD）。实验涵盖11种语言、3个领域、2种骨干模型，并提供了详细的错误分析。

### 方法 / 贡献
1. 提出SeqLab框架：在生成式序列到序列模型的编码器上增加辅助序列标注任务，联合优化生成损失和标注损失，并在推理时利用标注概率过滤低置信度输出。
2. 结合方面代码切换（ACS）：通过标记方面词后翻译，生成源-目标、目标-源混合句子，扩充训练数据。
3. 首次将跨语言ABSA拓展至TASD任务，并系统评估多种源-目标语言对。
4. 实验达到11种语言、3个领域、2种骨干模型的最优结果。

### 实验或数据
使用SemEval-2016数据集（含英语、西班牙语、法语、荷兰语、俄语、土耳其语等），覆盖餐厅评论等3个领域，评估E2E-ABSA和TASD任务。采用两种骨干模型（如mT5等），对比先前方法并超越SOTA。

### 值得关注点
- 序列标注辅助任务无需复杂标签方案（仅标注单词首token），简单高效。
- ACS数据增强无需对齐工具，仅需翻译标记，扩展性强。
- 系统地评估了非英语作为源语言的情况，填补了空白。
- 在更难的TASD任务上也取得显著提升。

### 局限性
- 序列标注仅标记单词级（而非BIO），无法完整表示多词方面项，可能丢失短语边界信息。
- 依赖机器翻译质量，翻译错误可能影响ACS生成数据的质量。
- 实验仅在单个数据集（SemEval-2016）上进行，泛化性需更多验证。
- 未提及对极低资源语言（如不在mPLM中充分覆盖的语言）的评估。
- 推理时阈值需要人工设定，可能不是最优。

## 7. Designing an Auditable LLM-Supported Workflow for Qualitative Thematic Analysis

- Source: arxiv
- arXiv ID: 2608.30543
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.30543v1
- PDF: https://arxiv.org/pdf/2608.30543v1
- DOI: https://doi.org/10.48550/arXiv.2608.30543

### Authors

Nadia Jul Jeldtoft, Tariq Yousef

### Abstract

Large Language Models (LLMs) offer new possibilities for scaling qualitative analysis, but existing applications often provide limited methodological transparency regarding how qualitative methods are translated into computational procedures. This paper presents an auditable and privacy-preserving computational operationalization of inductive and latent Thematic Analysis (TA). This paper first derives five design principles from the methodological requirements of TA and the conditions introduced by LLM-based inference: preserving interpretative context, maintaining traceable relationships between empirical material and analytical outputs, representing analytical constructs and reasoning explicitly, constraining LLM inference to interpretative tasks, and enabling privacy-preserving local deployment. Second, it presents a proof-of-concept for a two-phase workflow that operationalizes these principles by combining interpretative LLM inference with deterministic procedural control to generate codes, analytical justifications, themes, and theme descriptions while preserving explicit links to the source material. Third, it proposes an evaluation framework combining structural comparison with human-led TA and independent expert assessment of analytical quality. The evaluation is conducted on semi-structured Danish interview transcripts. and the results shows that the workflow produces code-level outputs with coverage broadly comparable to human annotations and highly rated analytical justifications, while generating a more compressed thematic structure characterized by fewer and broader themes. The findings demonstrate the feasibility of auditable LLM-supported TA through a modular workflow designed to scale to larger datasets, accommodate different LLMs, and support transfer across research domains, with domain adaptation primarily requiring adjustments to the prompting strategy.

### 中文一句话结论
本文提出了一种可审计、隐私保护的LLM辅助主题分析工作流，将解释性推理与确定性程序控制分离，以保持方法论透明性和可追溯性。

### English TL;DR
This paper presents an auditable, privacy-preserving workflow for qualitative thematic analysis using large language models, guided by five design principles that separate interpretative inference from deterministic procedural control to maintain methodological transparency and traceability.

### 中文详细总结
本文针对大型语言模型（LLMs）在定性主题分析（TA）应用中存在的方法论透明性不足问题，提出了一种可审计且保护隐私的计算化操作方案。研究首先从TA的方法论要求出发，结合LLM推理的特性，推导出五项设计原则：保留解释性上下文、维持经验材料与分析输出之间的可追溯关系、明确表示分析构念与推理过程、将LLM推理限定在解释性任务、以及支持本地部署以保护隐私。基于这些原则，研究提出了一种两阶段工作流原型：第一阶段通过LLM生成编码和理由，第二阶段通过确定性程序聚合编码生成主题和主题描述，所有输出均与原始数据保持明确链接。评估在丹麦语半结构化访谈转录文本上进行，结果表明该工作流的编码覆盖度与人工标注相当，分析理由获得高质量评价，但生成的主题结构更压缩（主题数量更少、范围更广）。研究证明，通过模块化工作流实现可审计的LLM辅助TA是可行的，该工作流可扩展至更大数据集、适配不同LLM，并支持跨领域迁移。

### 方法 / 贡献
1. **五项设计原则**：从TA方法论和LLM条件推导出保留解释性上下文、保持可追溯关系、明确表示分析构念、约束LLM推理至解释性任务、支持本地隐私部署。
2. **两阶段工作流**：阶段1（文本到编码）将LLM解释性推理与确定性程序控制结合，生成带理由的编码；阶段2（编码到主题）通过确定性映射聚合编码为主题和描述。所有中间结果均与来源数据链接。
3. **评估框架**：结合与人工TA的结构化比较和独立专家对分析质量的评估。
4. **技术实现**：使用Mistral 7B v0.3 Instruct本地部署，通过Pydantic模式和Outlines库约束输出结构，采用Self-Refine启发的提示策略。

### 实验或数据
- 数据：来自丹麦研究项目“家庭革命”的99份半结构化访谈转录文本（丹麦语），分为开发集（94份）和测试集（5份），按长度和性别分层采样。
- 分割：转录文本按连续两个问答对作为分析单元（图1、图2展示单元分布和词元数）。
- 评估：编码层面与人类标注进行覆盖度比较；分析理由由独立专家评分；主题结构对比显示更少更广的主题（但未给出具体数值）。

### 值得关注点
1. **可审计性设计**：将方法论质量准则（如可追溯性、解释性）直接编码到计算架构中，而非依赖黑箱LLM输出。
2. **本地隐私保护**：使用小型开放权重模型（Mistral 7B）本地部署，避免敏感定性数据暴露给第三方API。
3. **功能分离**：明确区分LLM负责的解释性任务（模式识别、推理）和确定性程序控制（链接、验证），提升可重复性。
4. **提示策略**：基于Self-Refine的三部分提示，强调每个编码必须附带明确理由（满足原则3）。
5. **评估创新**：结合结构化比较（编码覆盖度）和专家定性评估（理由质量），而非仅依赖量化指标。

### 局限性
1. **实验规模有限**：仅基于99份丹麦语访谈的测试集（5份），统计显著性和泛化能力待验证。
2. **主题结构压缩**：生成的主题数量更少、范围更广，可能丢失细粒度差异或人类分析中的精细结构。
3. **分割策略未系统优化**：分析单元大小（两个问答对）基于初始实验选择，但最优分段未做系统评估。
4. **模型能力限制**：使用Mistral 7B（小型模型），丹麦语能力不如大型商业模型，可能影响结果质量。
5. **领域适应性需人工调整**：迁移到其他领域主要依赖提示策略调整，缺乏自动化适配机制。
6. **无定量性能指标**：未提供编码准确率、召回率等量化评估，仅依赖专家评分和结构比较。
7. **仅测试归纳/隐性TA**：未验证其他TA类型（如演绎、语义）的适用性。

## 8. AIA$^{2}$: Attribute-Agnostic Imbalance Augmentation for Subgroup Robustness

- Source: arxiv
- arXiv ID: 2608.30297
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.30297v1
- PDF: https://arxiv.org/pdf/2608.30297v1
- DOI: https://doi.org/10.48550/arXiv.2608.30297

### Authors

Hanshu Rao, Guangzeng Han, Xiaolei Huang

### Abstract

Attributes describing data content and context can induce diverse imbalance patterns that go beyond label imbalance alone. However, existing studies primarily address label imbalance while overlooking data attributes, such as topics and demographics, which can induce meaningful subgroup structure while causing model degradation on underrepresented subgroups. We propose Attribute-Agnostic Imbalance Augmentation (AIA$^{2}$), a framework for improving model robustness under varying subgroup imbalances without explicit subgroup annotations. AIA$^{2}$ automatically discovers varying imbalances via latent semantic distributions, obtains slices with both learning difficulty and subgroup imbalance deficits, and deploys a large language model (LLM) for subgroup-aware imbalance augmentation. We have evaluated AIA$^{2}$ on 5 popular corpora with rich domains and their attribute values, covering social issues and diverse topics. Results show improved performance on the lowest-performing subgroups and consistent gains over competitive baselines. Ablation studies confirm complementary contributions from each component, and additional analyses show that AIA$^{2}$ provides a practical and consistent way to improve worst-group robustness under data subgroup imbalance. Code is available at https://github.com/trust-nlp/AIA2-Subgroup-Robustness.

### 中文一句话结论  
提出属性无关的失衡增强方法 AIA²，无需显式子组标注即可自动发现潜在子组分布不平衡，利用大语言模型生成针对性增强数据，提升模型在最差子组上的鲁棒性。

### English TL;DR  
AIA² (Attribute-Agnostic Imbalance Augmentation) is a framework that improves model robustness under unknown subgroup imbalances by automatically discovering data slices with distribution gaps and using LLMs to generate targeted augmentations without requiring subgroup annotations.

### 中文详细总结  
论文指出，数据属性（如主题、人口统计等）会引发超出标签不平衡的多样子组不平衡，但现有方法主要关注全局标签不平衡，忽略属性导致的子组退化。作者提出 AIA² 框架：  
1. **潜在切片发现**：联合语义嵌入与模型预测分布，通过 kNN 图和 Leiden 社区检测自动划分数据切片。  
2. **切片级分布差距分析**：比较切片内局部标签分布与全局分布，识别欠代表标签，基于损失选择高难度种子样本。  
3. **约束引导增强与过滤**：利用 LLM 生成增强样本，通过格式约束和保真度-多样性评分筛选，确保标签一致性与语义多样性。  
4. **迭代训练**：每轮训练后重新切片，逐步修复局部分布缺陷。  
在 5 个公开语料（文本分类和命名实体识别任务）上验证，AIA² 显著提升最低性能子组的表现，并持续优于基线方法。消融实验证实各组件互补有效。

### 方法 / 贡献  
1. 提出属性无关的失衡学习框架，训练和模型选择时无需子组元数据，提升最差子组鲁棒性。  
2. 提出子组感知的分布差距分析与失衡缺陷驱动选择机制，定位潜在区域内的少数模式与标签。  
3. 提出约束引导的过滤策略与增强方法，确保数据多样性与标签保真度。

### 实验或数据  
- **任务**：文本分类（CLS）和命名实体识别（NER）。  
- **数据集**：HateXplain（社会）、HumAID（危机）、WWW2015（商业评论）、RE3D（防御与安全文档）、CrossNER（五个专业领域）。  
- **结果**：在最低性能子组上性能提升，一致优于竞争基线；消融实验验证各组件贡献；分析表明 AIA² 能实际且一致地改善子组不平衡下的最差组鲁棒性。

### 值得关注点  
- 无需显式子组标注，自动发现潜在不平衡区域。  
- 结合语义与预测分布进行切片，动态适应模型演变。  
- 利用 LLM 生成增强数据，并设计约束机制保证质量。  
- 同时适用于分类和序列标注任务，泛化性较强。

### 局限性  
根据提供的材料，未明确提及局限性。潜在考虑可能包括对 LLM 的依赖带来的计算成本，以及增强过程中可能引入的偏差，但论文未就此展开讨论。

## 9. When Less is More: Understanding When Token Filtering Helps and Fails in AI-generated Text Detection

- Source: arxiv
- arXiv ID: 2608.29903
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.29903v1
- PDF: https://arxiv.org/pdf/2608.29903v1
- DOI: https://doi.org/10.48550/arXiv.2608.29903

### Authors

Xiaoyang Han, Lvxiaowei Xu, Ming Cai

### Abstract

The rapid advancement of large language models (LLMs) has made AI-generated text detection increasingly critical. Existing zero-shot detectors assume that more token-level evidence leads to more reliable detection. However, our empirical study challenges this consensus: fewer tokens sometimes work better, retaining only 40% can yield optimal performance, yet this benefit is not universal. Using the Entropy Gap Score (EGS), we introduce top-$k$ cumulative probability filtering as a diagnostic probe. Across three representative settings, filtering exhibits strikingly different behaviors. We analyze EGS via typical set theory and quantify its dynamics through entropy calibration and distribution analysis. We find that filtering helps for weak source LMs, where low-entropy tokens are harmful, but fails for strong source LMs, where they are not notably harmful. Our work provides the first systematic analysis showing that some tokens are not merely uninformative but systematically harmful due to entropy miscalibration, revealing a two-sided trade-off in token-level detection.

### 中文一句话结论
本研究挑战了“更多词元证据总是更好”的共识，发现过滤掉低熵词元（最多保留40%）能显著提升AI文本检测性能，但该效果仅限于弱源语言模型，而对强源模型无效，原因是熵校准导致了双向权衡。

### English TL;DR
This paper systematically shows that filtering out low-entropy tokens can improve AI-generated text detection for weak source language models but not for strong ones, due to entropy miscalibration creating a two-sided trade-off between distribution separation and score variance.

### 中文详细总结
本文研究了AI生成文本检测中词元过滤策略的有效性。作者通过引入基于累积概率的top-k过滤探针，在三个代表性检测设置（弱源黑盒、弱源白盒、强源黑盒）中发现：过滤低熵词元仅在弱源语言模型（如Falcon-7B、GPT-2-XL）中显著提升检测性能（最佳AUROC提升可达0.98+），而在强源模型（如GPT-4o）中无益甚至有害。作者利用典型集理论重新解释熵差分数（EGS），并通过熵校准和分布分析量化其动态，揭示了过滤带来的双向权衡：去除低熵词元有助于分离人类与AI文本分布（正面），但减少词元数量会增加EGS方差（负面）。最终净增益取决于源端的熵校准质量——弱源LM存在显著的L-E解耦，导致低熵区域出现异常高的EGS，从而损害检测；过滤能有效移除这些有害词元。

### 方法 / 贡献
- **方法**：引入top-k累积概率过滤作为诊断探针，选择性地移除高概率集中（低熵）词元；采用熵差分数（EGS）作为检测指标；通过典型集理论重新解释EGS为有符号的典型性偏离分数；使用熵校准分析L（自信息）与E（熵）的耦合强度。
- **贡献**：
  1. 首次系统证明部分词元不仅无信息而且有害（因熵校准错误），挑战“更多词元更好”的共识。
  2. 提出top-k过滤探针，揭示低熵词元在弱源LM中的危害性。
  3. 揭示过滤成功与否取决于分布分离与方差之间的双向权衡，并解释三种设置下的不同行为。

### 实验或数据
- **数据集**：使用XSum（BBC新闻）、WritingPrompts（故事）、Reddit ELI5（科普问答），每个数据集随机抽取150个人类文本并取前30词作为提示生成AI文本。
- **源模型**：弱源LM（GPT-2-XL、OPT-2.7B、GPT-Neo-2.7B、GPT-J-6B、Falcon-7B、BLOOM-7.1B）；强源LM（GPT-4-Turbo、GPT-4o、Claude-4、DeepSeek-V4、Gemini-2.5）。
- **代理模型**：六个弱源LM作为代理模型；额外使用Falcon-40B和Qwen2.5-3B进行交叉验证。
- **基线**：对比Log-Likelihood、Entropy、LogRank、DetectGPT、Fast-DetectGPT、Lastde++、SpecDetect++等零样本检测器。
- **指标**：AUROC；报告各过滤比率下的最佳AUROC及最优过滤比例θ（弱源设置下约0.38~0.52）。
- **结果**：弱源LM中，过滤可显著提升AUROC（如Falcon-7B自盒设置下AUROC从0.9745提升至0.9807）；强源LM中过滤无正面效果。

### 值得关注点
- **反直觉发现**：保留仅40%词元可达到最优性能，挑战原有假设。
- **典型集理论应用**：将EGS重新解释为典型性偏差，为理解检测机制提供信息论新视角。
- **双向权衡框架**：过滤带来的分布分离增益与方差增大代价之间的博弈，解释了为何不同源模型表现迥异。
- **诊断探针而非部署方法**：作者强调top-k过滤主要用于分析，而非直接推广到实际系统。

### 局限性
- 仅针对零样本检测器，未涵盖训练型检测方法（如fine-tuning或基于分类器的方案）。
- 实验局限于英语数据集和特定模型家族（Falcon、GPT等），结论可能不适用于其他语言或架构。
- 过滤策略依赖代理模型，实际部署中代理模型不可知情况下效果未知。
- 未探讨过滤后词元数量过少（如<20词）对统计可靠性的影响。

## 10. Latent-Space Intervention for Cross-Lingual Factual Consistency: Consistency Improvements without Accuracy Drops

- Source: arxiv
- arXiv ID: 2608.28860
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.28860v1
- PDF: https://arxiv.org/pdf/2608.28860v1
- DOI: https://doi.org/10.48550/arXiv.2608.28860

### Authors

Faeze Ghorbanpour, Constanza Fierro, Alexander Fraser, Anders Sogaard

### Abstract

Large Language Models (LLMs) often answer the same factual question differently across languages. We study whether cross-lingual latent-space intervention can reduce this inconsistency. We train layer-specific autoencoders on parallel multilingual representations and apply inference-time corrections to factual QA prompts. We find that latent intervention improves geometric alignment between languages, and that this improvement translates into consistent gains in cross-lingual consistency with English across both open-ended and multiple-choice QA formats, without degrading factual accuracy. In open-ended QA, Spearman's rank correlation between English and non-English languages improves substantially, with gains of 0.16 for English-Arabic and 0.20 for English-Russian pairs. In multiple-choice QA, answer agreement with English improves consistently across both KLAR and mParaRel. Ablations show that AE reconstruction yields consistent gains at no accuracy cost, while PCA projection contributes marginally, and mean-shift produces substantially larger consistency gains in open-ended QA at the cost of some accuracy.

### 中文一句话结论
本文提出基于自动编码器的跨语言潜在空间干预方法，在不降低事实准确率的前提下，显著提升多语言大模型在不同语言间的事实一致性。

### English TL;DR
This paper proposes a cross-lingual latent-space intervention using autoencoders that improves factual consistency across languages by aligning multilingual representations, yielding substantial gains in answer agreement (e.g., +0.16 for English-Arabic and +0.20 for English-Russian) without degrading factual accuracy.

### 中文详细总结
大型语言模型在回答同一事实问题时，不同语言的结果常常不一致。本研究探索是否可以通过跨语言潜在空间干预来减少这种不一致。方法：
- 训练层特定的自动编码器（autoencoder），利用并行多语言文本的隐藏表示，建立共享的潜在空间。
- 在推理时，通过前向钩子（forward hook）对隐藏状态进行编码、干预（可选）并解码回原始空间，修正各语言表示。
- 干预策略包括：仅瓶颈（AE）、PCA投影移除不一致子空间（projection）、向跨语言均值偏移（mean-shift）。
在KLAR和mParaRel数据集上，针对开放式问答和多项选择问答进行评测，涵盖五种语言（阿拉伯语、英语、荷兰语、俄语、中文）。结果：
- 开放式问答中，英语-阿拉伯语的斯皮尔曼等级相关提升0.16，英语-俄语提升0.20。
- 多项选择问答中，答案一致率在KLAR和mParaRel上均稳定提升。
- 消融实验表明：AE重构可带来一致增益且不牺牲准确率；PCA投影贡献微弱；mean-shift在开放问答中增益更大但会损失一定准确率。

### 方法 / 贡献
1. 提出基于自动编码器的跨语言潜在空间，在共享空间中对齐多语言的语义等价表示。
2. 设计推理时修正方法（AE、PCA投影、mean-shift），通过前向钩子实时调整隐藏状态。
3. 验证该方法在不降低事实准确率的前提下，有效提升跨语言一致性，尤其对语言距离远的对别效果更佳。

### 实验或数据
- 训练数据：TED演讲平行语句（用于训练自动编码器）。
- 对齐评估：FLORES+平行句子数据集。
- 事实QA评测：KLAR（开放式与多项选择）和mParaRel（多项选择）。
- 模型：Aya-expanse-8B、Llama-3.1-8B、Qwen-3-8B。
- 主要指标：余弦相似度（表示对齐）、事实准确率、跨语言答案一致率、等级相关（开放问答）。
- 最佳干预层位于网络最后三分之一层（模型依赖，如L20–L28）。

### 值得关注点
- 消融实验显示：仅采用AE重构即可获得一致增益，且不牺牲准确率；PCA投影提升微弱；mean-shift在开放问答中带来更大一致性提升，但以部分准确率为代价。
- 方法无需修改模型参数，适用于多种多语言模型。
- 对于语言距离较远的对别（如英-阿、英-俄）效果更显著。

### 局限性
- 实验仅覆盖五种语言（阿拉伯语、英语、荷兰语、俄语、中文），对更多语言的效果有待验证。
- 仅针对事实问答任务进行评测，未扩展到其他跨语言任务。
- 干预仅施加于特定层（中后层），且最佳层需根据模型手动选择，推广性有限。
- mean-shift策略在部分情况下会降低准确率，需谨慎调整参数。

## Processing Notes

- Duplicate papers skipped: 0