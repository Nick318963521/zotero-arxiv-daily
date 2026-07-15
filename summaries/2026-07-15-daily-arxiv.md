# Daily arXiv - 2026-07-15

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-15T23:17:59
- Paper count: 10

## 1. Scaling Point-in-Time Language Models

- Source: arxiv
- arXiv ID: 2607.11889
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2607.11889v1
- PDF: https://arxiv.org/pdf/2607.11889v1
- DOI: https://doi.org/10.48550/arXiv.2607.11889

### Authors

Bryan Kelly, Semyon Malamud, Johannes Schwab, Teng Andrea Xu

### Abstract

Large language models trained on unrestricted internet corpora inevitably embed information from the future, introducing lookahead bias that compromises the validity of backtests and causal inference in finance and the social sciences. Point-in-time language models--trained exclusively on text available up to each calendar date--eliminate this leakage by construction, but existing efforts typically produce models that lag substantially behind their unconstrained counterparts. We show that this performance gap can be substantially narrowed through scale. Training decoder-only transformers with up to 4 billion parameters on 1 trillion chronologically filtered tokens from FineWeb, we construct a sequence of monthly model checkpoints spanning 2013-2024. Across a range of common-sense reasoning and language understanding benchmarks, our models approach the performance of leading open-weight models of comparable size (e.g., Gemma-3-4B and LLaMA-7B) trained on temporally unrestricted data, although a performance gap remains on several tasks. Instruction fine-tuning via LoRA further improves downstream usability. We release the complete pipeline--including dataset construction, training infrastructure, and evaluation code--to enable reproducible point-in-time language modeling and to support research applications that require strict temporal validity.

### 中文一句话结论  
通过将模型规模扩展至40亿参数、训练数据扩展至1万亿时间过滤令牌，本文证明“时点语言模型”的性能已接近未经时间约束的同类开源模型，显著缩小了因时间限制导致的性能差距。

### English TL;DR  
Scaling point-in-time language models to 4 billion parameters and 1 trillion temporally filtered tokens narrows the performance gap with unrestricted models; the resulting monthly checkpoints (2013–2024) approach Gemma-3-4B and LLaMA-7B on reasoning benchmarks, though a gap persists on some tasks.

### 中文详细总结  
大型语言模型在无时间限制的网络语料上训练会嵌入未来信息，引入前瞻偏差，损害金融和社会科学中的回溯测试与因果推断有效性。本文通过规模扩展大幅缩小了时点语言模型与无约束模型的差距：训练了高达40亿参数的解码器Transformer，在来自FineWeb的1万亿时间排序令牌上构建了2013–2024年的月度模型检查点。在常识推理与语言理解基准上，这些模型接近同等规模领先开源模型（如Gemma-3-4B、LLaMA-7B）的性能，但部分任务仍有差距。通过LoRA进行指令微调进一步提升了下游可用性。论文公开了完整流程（数据集构建、训练基础设施、评估代码）以促进可复现的时点语言建模研究。

### 方法 / 贡献  
- **规模扩展**：将时点语言模型的参数从1.5B扩至4B，训练令牌从7B增至1T，上下文长度从1,536增至2,048，嵌入维度从768增至4,096（采用Modded NanoGPT架构及先进优化技术）。  
- **时间一致性训练**：使用FineWeb语料（2013–2025年，15T令牌），按时间顺序过滤并逐月保存检查点，消除未来信息泄漏。  
- **指令微调**：采用LoRA（秩r=16）进行参数高效微调，避免灾难性遗忘并节省计算资源，在IFEval等基准上验证。  
- **开源贡献**：发布完整代码与资源配置，降低可复现研究门槛。  
- **金融应用验证**：在资产定价任务中利用时点模型提取新闻信号预测收益与宏观经济，展示严格时序有效性带来的经济增益。

### 实验或数据  
- **预训练数据**：FineWeb数据集（96个Common Crawl快照，15T英文令牌），按时间戳过滤后使用约1T令牌。  
- **模型规模**：1.5B与4B参数的两个时点模型，在90B至1T令牌上训练。  
- **评估基准**：多种常识推理与语言理解任务（具体名称未详列，但提及与Gemma-3-4B、LLaMA-7B比较）；指令微调后使用IFEval（程序化可验证基准）。  
- **金融应用**：新闻文本信号用于收益率预测与宏观经济条件预测。  
- **未提及**：未给出具体基准分数，但声称零样本准确率接近同类模型数个百分点内。

### 值得关注点  
- 首次证明时点语言模型可通过规模扩展接近无时间约束模型的性能，打破“时间限制必然牺牲性能”的刻板印象。  
- 严格按时间排序训练并月度保存检查点，可直接用于真实金融回测，避免前瞻偏差。  
- LoRA微调既能保持预训练知识又能适配指令任务，未来可推广至更多领域。  
- 完全开源流程（数据、训练、评估），促进后续研究。

### 局限性  
- 在部分任务上时点模型与无约束模型仍存在性能差距，表明规模扩展尚未完全消除时间限制的影响。  
- 仅基于FineWeb一个来源验证，未测试其他时间过滤语料。  
- 金融应用仅为初步验证，未与多种基线（如传统词典方法或其他时间约束模型）进行全面比较。  
- 指令微调仅使用LoRA，未探索全参数微调或更高级的微调策略。

## 2. Translation as a Computationally Efficient Bridge: Feasibility of English BERT for Low-Resource Languages

- Source: arxiv
- arXiv ID: 2607.12612
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.12612v1
- PDF: https://arxiv.org/pdf/2607.12612v1
- DOI: https://doi.org/10.48550/arXiv.2607.12612

### Authors

Hielke Muizelaar, Giulia Rivetti, Marco Spruit, Marcel Haas

### Abstract

BERT models have revolutionised Natural Language Processing (NLP) through their ability to process unstructured text across diverse domains. However, developing high-quality BERT models for non-English languages remains challenging due to limited annotated data and high computational demands. Translating non-English data into English and fine-tuning existing English BERT models offers a resource-efficient alternative, yet few studies have structurally compared translation-based fine-tuning with native-language BERT performance across tasks and languages. This study provides such a comparison, evaluating the feasibility of translation-based fine-tuning across six NLP tasks: Sentiment Analysis, Hate Speech Detection, Question Answering, Named Entity Recognition, Part-of-Speech Tagging, and Natural Language Inference, using datasets translated from Bulgarian, Chinese, Dutch, Italian, and Russian. Across all settings, the translation-based approach was comparable or superior in 53.3 percent of cases. Gains were most frequent in Question Answering, Part-of-Speech Tagging, and Natural Language Inference, while performance declines were common in Named Entity Recognition and Hate Speech Detection. The results show that translation-based fine-tuning is most effective for tasks relying on syntactic or structural patterns and for languages typologically close to English, such as Dutch, but less effective for token-level or culturally nuanced tasks, particularly in Chinese. Overall, this study demonstrates that translation-based fine-tuning offers a scalable, resource-efficient, and empirically validated path for extending NLP to low-resource languages while advancing linguistic inclusivity and sustainability in artificial intelligence.

### 中文一句话结论
翻译后微调英文BERT在53.3%的设置中与原生语言BERT性能相当或更优，尤其适用于句法/结构任务及与英语类型接近的语言，为低资源语言NLP提供了可扩展、资源高效的路径。

### English TL;DR
This study demonstrates that translating low-resource language data into English and fine-tuning a pre-trained English BERT model is a scalable, resource-efficient alternative that matches or outperforms native-language BERT in 53.3% of cases across six NLP tasks and five languages, with particular success in syntactic and structural tasks for languages typologically close to English.

### 中文详细总结
本研究系统比较了翻译后微调（Translate-Train）与原生语言BERT在六项NLP任务（情感分析、仇恨言论检测、问答、命名实体识别、词性标注、自然语言推理）上的性能，覆盖五种语言（保加利亚语、中文、荷兰语、意大利语、俄语）。翻译后微调使用OPUS-MT将非英语数据翻译为英语，再微调预训练英文BERT。结果显示，在53.3%的设置中翻译方法优于或持平原生模型；在问答、词性标注和自然语言推理中增益最明显，而在命名实体识别和仇恨言论检测中性能下降常见。该方法对依赖句法或结构模式的任务以及语言类型上接近英语的语言（如荷兰语）最有效，但对token级或文化敏感任务（尤其是中文）效果较差。研究认为翻译后微调为低资源语言NLP提供了一种可扩展、资源高效且经验验证的途径。

### 方法 / 贡献
- **方法**：将非英语数据集通过OPUS-MT翻译为英语，再对预训练英文BERT进行微调，与原生语言BERT（相同任务和语言）进行对比。
- **贡献**：
  1. 提供多任务、多语言的翻译后微调开源基准（OPUS-MT + English BERT）。
  2. 分析任务类型影响：区分句级任务（相对鲁棒）和token级任务（易受对齐损失）。
  3. 考察跨语言模式：语言类型接近英语（如荷兰语）获益更多，展示了翻译质量、任务敏感性与语言距离的交互作用。

### 实验或数据
- **任务**：情感分析、仇恨言论检测、问答、命名实体识别、词性标注、自然语言推理。
- **语言**：保加利亚语、中文、荷兰语、意大利语、俄语。
- **数据集**：词性标注和命名实体识别使用XTREME基准数据集；其他任务为各语言单独选取的资源（如DBRD、Italian Tweets、Cinexio、RuReviews、Weibo Senti 100k、Dutch HateCheck、Multilingual Hate Speech、COLD、SICK-NL、LingNLI、XNLI、P-Direkt、QA-ITA-200k、EXAMS、SberQuAD、CMRC2018等）。具体规模和来源详见论文表1。

### 值得关注点
- 翻译后微调在53.3%设置中与原生模型持平或更优，资源成本显著降低。
- 对句法/结构任务（QA、POS、NLI）增益明显，对token级任务（NER、HSD）倾向下降。
- 语言类型接近英语（如荷兰语）效果更好，文化差异大的语言（如中文）挑战更大。
- 方法可本地执行、可复现，适合标注数据或计算资源有限的场景。

### 局限性
- 翻译可能引入错误，影响下游任务性能，尤其是token对齐丢失（NER、POS）。
- 对文化敏感或依赖语用信息的任务（如仇恨言论检测）效果较差。
- 语言类型距离大的语言（如中文）性能提升有限。
- 数据集质量、大小和标注一致性在各语言间存在差异，可能影响对比公平性。
- 未与最新生成式LLM（如GPT-4）的零样本或少样本能力进行直接比较。

## 3. The Illusion of Robustness: Aggregate Accuracy Hides Prediction Flips under Task-Irrelevant Context

- Source: arxiv
- arXiv ID: 2607.12963
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.12963v1
- PDF: https://arxiv.org/pdf/2607.12963v1
- DOI: https://doi.org/10.48550/arXiv.2607.12963

### Authors

Yanzhe Zhang, Sanmi Koyejo, Diyi Yang

### Abstract

As large language models (LLMs) grow more capable, they are increasingly deployed in context-rich settings where task inputs are often accompanied by long, partially irrelevant context. In a controlled setting, we find that state-of-the-art models often appear robust to task-irrelevant context at the aggregate level: prepending it to benchmark questions causes little change in overall accuracy. This aggregate stability, however, masks significant per-example instability. Even semantically meaningless pseudo-words, formed by randomly combining characters, can markedly shift model predictions on a small fraction of examples, degrading performance on some while improving it on others. This two-sided effect holds consistently across a wide range of models and datasets, yet the affected examples are largely model-specific. We further show that this instability is modulated by context type, context length, test-time compute, and model development stage. Together, our findings reveal context-induced tail risks concealed by aggregate accuracy, motivating per-example reliability evaluation of language models.

### 中文一句话结论
本文揭示，在任务无关上下文中，大语言模型在聚合准确率上看似鲁棒，但实际掩盖了显著的、模型特定的逐示例预测翻转，构成隐藏的可靠性风险。

### English TL;DR
Aggregate accuracy on benchmarks is stable under task-irrelevant context, but this masks significant, model-specific per-example prediction flips that are two-sided (both improvements and degradations), revealing hidden reliability tail risks.

### 中文详细总结
本研究通过控制系统性地向基准测试问题前置任务无关上下文（如随机伪词），发现前沿大语言模型在整体准确率上几乎不受影响（变化不超过±0.9%），表现出“聚合鲁棒性”。然而，这种稳定性掩盖了严重的逐示例不稳定性：即使是语义上无意义的随机伪词，也能在少量示例上显著改变模型预测，既可能导致性能下降，也可能意外提升性能。这种“双向效应”在多个模型（如GPT-5.5、DeepSeek-V4-Pro、Gemini-3.1-fl）和数据集（MMLU-Pro、GPQA、HLE、SimpleQA）上一致存在，但受影响的示例高度模型特异，不同模型间受影响示例的重叠度很低（例如MMLU-Pro上Jaccard指数仅0.09）。研究进一步发现，示例的模糊性与性能变化相关性弱，而模型在无上下文时的预测不确定性则可部分解释变化幅度。此外，不稳定性受上下文类型、长度、测试时计算量和模型开发阶段等多种因素调节。

### 方法 / 贡献
1. 提出两个量化上下文诱导不稳定性的互补指标：**不稳定性（INS）**：所有示例上性能绝对变化的平均值，衡量整体敏感性；**最差尾端退化（WTD）**：受影响最严重的K%示例的平均性能下降，衡量极端风险。
2. 通过随机伪词构建任务无关上下文，设计了包含噪声校正（bootstrap法）的严格实验，以区分真实效应与采样噪声。
3. 揭示聚合准确率掩盖“双向效应”（性能提升与下降相互抵消）和“模型特异性”（受影响示例因模型而异），导致基于数据的可预测性差。
4. 表明不稳定性的影响因素包括上下文类型、长度、测试时计算量及模型开发阶段，提供了进一步研究的调控维度。

### 实验或数据
- **数据集**：MMLU-Pro、GPQA、Humanity's Last Exam (HLE)、SimpleQA。
- **模型**：包括GPT-5.5、GPT-5.4、GPT-4.1、DeepSeek-V4-Pro、Grok-4.20-NR、Mistral-Large-3、gpt-oss-120b、Gemini-3.1-fl等。
- **任务无关上下文**：以随机伪词（3-8字符随机字母组合）为主，并进行了自然上下文（网页、问答对等）的消融实验。
- **不稳定性范围**：INS值最高达13.6%；WTD值在部分模型（如Mistral-Large-3）上可超50%。
- **模型特异性评估**：使用Pearson相关系数（平均约0.00）和Jaccard指数（受影响示例重叠度低）量化。

### 值得关注点
- 揭示了一个反直觉的现象：**聚合稳定性不等于个体可靠性**，标准基准评估会隐藏严重尾端风险。
- “双向效应”意味着添加无关上下文可能偶然提升某些示例性能，但这在安全关键场景中同样危险。
- 模型特异性使得风险难以从数据或问题特征中预测，强调了**逐示例评估**的必要性。
- 提供了可量化、可复现的评估方法（INS和WTD），并附有公开代码和数据。

### 局限性
1. 实验集中于**前置文本**的上下文形式，未充分探索其他位置或模态（如图像拼接）的无关上下文。
2. 伪词上下文高度简化，真实场景中的自然语言上下文可能引入更多语义混淆或信息泄漏，影响可能更复杂。
3. 研究主要评估**单次推理**场景，未覆盖多步交互（如智能体决策链）中上下文累积效应。
4. 噪声校正采用均值修正，可能无法完全消除极端值处的估计偏差。
5. 未深入探究不稳定的根本机制（如注意力分布偏移、位置编码影响等），属于现象层面的刻画。

## 4. TAKE: Trajectory-Aware Knowledge Estimation for Text Dataset Distillation

- Source: arxiv
- arXiv ID: 2607.11898
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.11898v1
- PDF: https://arxiv.org/pdf/2607.11898v1
- DOI: https://doi.org/10.48550/arXiv.2607.11898

### Authors

Tri-Nhan Vo, Dang Nguyen, Sunil Gupta

### Abstract

Large-scale text corpora have become a quiet bottleneck in modern NLP, not just in storage, but in the accumulated cost of training, fine-tuning, and continual learning. We propose a text dataset distillation framework that reduces corpora to as little as 0.1% of their original size while preserving downstream task fidelity. We approach distillation through the lens of influence functions, which quantify each sample's contribution to the downstream objective, a natural and principled basis for selection. We introduce Trajectory-Aware Knowledge Estimation (TAKE), which convolves the knowledge-based influence along the training trajectory into a single per-sample knowledge score, capturing informative samples. These scores serve as sample weights within a discrete Optimal Transport objective, guiding prototype selection from a synthetically generated candidate pool. We evaluate TAKE on downstream accuracy across text classification and natural language inference tasks at extreme compression (0.1% or 20 samples/class), showing that data efficiency is achievable without sacrificing task fidelity. The approach is theoretically grounded, with broader implications for coreset construction and data-centric AI. We release our source code at https://github.com/votrinhan88/take.

### 中文一句话结论
TAKE提出一种轨迹感知的知识估计方法，可将文本数据集压缩至原始大小的0.1%，同时保持下游任务性能。

### English TL;DR
TAKE proposes a trajectory-aware influence function method to distill text datasets to as little as 0.1% of their original size while preserving task fidelity.

### 中文详细总结
本文提出了一种名为TAKE（轨迹感知知识估计）的文本数据集蒸馏框架。该方法基于影响函数理论，沿着训练轨迹卷积每个样本的知识影响，得到单一的知识分数，从而识别信息量最大的样本。这些分数作为样本权重，融入离散最优传输目标中，指导从合成候选池中选择原型样本。在极端压缩率（0.1%或每类20个样本）下，TAKE在文本分类和自然语言推理任务上验证了数据效率，且未牺牲任务准确性。方法具有理论依据，对核心集构建和数据中心AI有潜在影响。

### 方法 / 贡献
- **轨迹感知影响函数**：在训练轨迹上卷积基于影响函数的知识估计，得到每个样本的单一知识分数，克服了传统影响函数仅依赖单点评估的局限。
- **离散最优传输原型选择**：将知识分数作为样本权重，通过离散最优传输目标从合成候选池中选择原型子集。
- **理论贡献**：提供了基于影响函数的可解释蒸馏框架，证明了极端压缩下任务保真度的可行性。

### 实验或数据
- **任务**：文本分类和自然语言推理（具体数据集名称在摘要中未提及）。
- **压缩率**：极端压缩至原始大小的0.1%（或每类20个样本）。
- **评估指标**：下游任务准确率。
- **代码**：已开源在 https://github.com/votrinhan88/take。

### 值得关注点
- 将影响函数与训练轨迹结合，动态捕捉样本在训练过程中的知识贡献。
- 在<0.1%的极端压缩率下仍能保持任务性能，对降低存储和计算成本有实际意义。
- 方法具有理论可解释性，而不仅是经验性的数据选择。

### 局限性
摘要中未明确讨论方法的局限性。可能存在计算开销（影响函数和轨迹卷积的计算复杂度）以及对合成候选池生成质量的依赖性。

## 5. Fine-Tuned Multi-Agent Framework for Detecting OCEAN in Life Narratives

- Source: arxiv
- arXiv ID: 2607.12215
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.12215v1
- PDF: https://arxiv.org/pdf/2607.12215v1
- DOI: https://doi.org/10.48550/arXiv.2607.12215

### Authors

Rasiq Hussain, Darshil Italiya, Joshua Oltmanns, Mehak Gupta

### Abstract

Accurately assessing personality from text is challenging because traits are latent, context-dependent, and often subtly expressed across long narratives. Large language models (LLMs) offer new opportunities by processing extensive textual contexts, but pretraining of these models can induce latent "personality-like" biases, making single-model inferences inconsistent. We propose a fine-tuned multi-agent framework for detecting OCEAN personality traits, in which sub-agents are conditioned to adopt high, low, or neutral perspectives for each trait through masked language modeling (MLM) and psychometric supervision. A judge LLM aggregates and compares sub-agent outputs to generate final trait predictions, capturing multiple complementary perspectives while mitigating individual model biases. We evaluate the framework on life narrative dataset through quantitative and qualitative experiments, including baselines, ablations, and inference quality analyses. Our approach offers a scalable and interpretable method for text-based personality inference, highlighting the benefits of multi-agent reasoning grounded in psychometric supervision.

### 中文一句话结论
本文提出一种基于微调的多智能体框架，通过将LLM子智能体分别调至对每个OCEAN特质的高、中、低倾向，并由评判智能体整合输出，从而更准确、可解释地从生活叙事文本中推理人格特质。

### English TL;DR
This paper proposes a fine-tuned multi-agent framework that uses LLM sub-agents conditioned on high, low, and neutral trait perspectives via masked language modeling and psychometric supervision, aggregated by a judge agent, to accurately and interpretably detect OCEAN personality traits from long life narratives while mitigating individual model biases.

### 中文详细总结
准确从文本中评估人格极具挑战，因为特质是潜在的、依赖上下文的，且常在长篇叙事中微妙表达。大语言模型虽能处理长文本，但其预训练引入了类似人格的偏差，导致单一模型推理不一致。为此，本文提出一个微调的多智能体框架：为每个OCEAN特质设置高、中、低三个倾向的子智能体，通过掩码语言建模和心理测量监督（IPIP-NEO量表）进行微调和条件化；再由一个评判LLM聚合并比较各子智能体的输出，生成最终特质预测。该方法能捕捉多个互补视角，同时缓解单模型偏差。框架通过15个子智能体（每特质3个）分别进行二分类，最后整合为三分类结果。

### 方法 / 贡献
1. **多智能体架构**：为每个OCEAN特质（共5个）分别构建高、中、低三个倾向的子智能体，总计15个。
2. **子智能体微调**：采用LoRA+MLM对Mistral-7B-Instruct进行微调，结合IPIP-NEO量表各层面的正/负向关键词来引导子智能体关注特定行为信号。
3. **评判聚合机制**：评判智能体（Qwen）接收叙事文本及所有子智能体的二分类结果、证据和置信度，进行综合比较后做出最终三分类预测。
4. **主要贡献**：首次将多智能体协商机制与心理测量监督结合，提升可解释性和鲁棒性；通过定量和定性实验全面验证。

### 实验或数据
- **数据集**：使用SPAN生活叙事访谈转录文本（1535份），将原始连续人格评分按三分位离散化为高、中、低三档。
- **基线模型**：包括RoBERTa微调、单智能体CoT（Mistral/Qwen）、全Mistral或全Qwen的多智能体设置。本文方法（Mistral子智能体+Qwen评判）在Openness (0.424)、Extraversion (0.416)、Agreeableness (0.415)、Neuroticism (0.458)上取得最优macro-F1，Conscientiousness略低于Qwen单智能体。
- **消融实验**：设计了无MLM微调、无子智能体等消融场景（摘要未提供详细消融结果，但实验部分提及）。

### 值得关注点
1. 通过多视角（高、中、低）子智能体的对比，有效缓解了单模型偏差，在多数特质上超越强基线。
2. 引入IPIP-NEO心理测量量表作为监督信号，使推理过程兼具理论依据和可解释性。
3. 对Neuroticism的提升最为显著（F1=0.458），表明该框架对难以捉摸的特质尤其有效。
4. 框架具有可扩展性，易于更换基座模型或引入更多特质维度。

### 局限性
1. 数据集仅来源于单一生活叙事访谈（SPAN），领域泛化能力未经验证。
2. 子智能体数量（15个）导致计算开销较大，可能限制实时或资源受限场景的应用。
3. 断续评分处理为三分类可能丢失细微差异；连续回归预测未探索。
4. 评判模型（Qwen）的选取及提示设计可能影响最终聚合效果，未系统评估不同评判模型的敏感性。

## 6. Language Identification with Succinct Machine-Independent Traces

- Source: arxiv
- arXiv ID: 2607.12443
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.12443v1
- PDF: https://arxiv.org/pdf/2607.12443v1
- DOI: https://doi.org/10.48550/arXiv.2607.12443

### Authors

Moses Charikar, Jon Kleinberg, Chirag Pabbaraju

### Abstract

Motivated by the power of large language models, there has been renewed interest in the Gold-Angluin model of language identification in the limit, with an eye toward variants of the model that might overcome the negative results for its original formulation. Recent papers on this question have proposed looking at computational traces and annotations of training strings as a source of additional power for a learner, reflecting empirical regularities such as the way that commented source code is easier to learn from than arbitrary source code, and text annotated with algorithmically generated chain-of-thought tokens can be easier to learn from than the raw text itself. This recent work has shown positive results for language identification in the presence of such computational traces, but the traces in these positive results come from explicit automata-theoretic machine models that generate the language, where the underlying vocabulary of tokens for the traces is very large. In this paper, we address two fundamental issues left open by this line of work: can we achieve positive results with traces that use only a small alphabet, and can we define traces directly from the language itself, without requiring an underlying machine model that generates it? We establish positive results for both of these questions: for an arbitrary collection of languages, we show how to define computational traces that enable identification in the limit, using an alphabet of tokens that is linear in the size of the alphabet that the languages are defined over, and independent of any other properties of the languages.

### 中文一句话结论  
本文证明：任意可数语言族（字母表大小为 \(k\)）均可通过至多 \(k+1\) 种颜色的计算迹实现极限辨识，且迹的定义不依赖底层机器模型。

### English TL;DR  
This paper shows that any countable collection of languages over an alphabet of size \(k\) can be identified in the limit using compact, machine-independent computational traces that require at most \(k+1\) colors.

### 中文详细总结  
受大语言模型能力的启发，本文重新审视 Gold-Angluin 的极限语言辨识模型，并关注通过计算迹（computational traces）增强学习能力的方向。现有工作依赖自动机模型产生的大规模迹字母表，且迹与底层机器紧密耦合。本文解决两个关键开放问题：能否用少量字母表实现迹？能否直接基于语言本身定义迹，而不依赖生成语言的机器？  
作者给出了肯定的回答：对任意可数语言族（字母表大小 \(k\)），存在至多 \(k+1\) 种颜色的迹着色函数，使得学习算法能在看到每个字符串及其迹后实现极限辨识。这一结果基于一个组合刻画：迹允许极限辨识当且仅当每个语言存在有限“告密子集”满足一定条件；而本文的着色引理保证该条件总能被满足。对于正则语言族，迹着色函数可进一步简化为对自动机状态的着色（仍只需 \(k+1\) 色），且该界是最优的。文章还讨论了迹被有限破坏时的扩展情形。

### 方法 / 贡献  
- **迹的抽象定义**：将计算迹定义为对每个前缀赋予一个颜色（来自有限调色板）的着色函数，不依赖底层机器。  
- **极限辨识的充要条件**：推广 Angluin 条件，给出迹辅助下语言族可辨识的精确刻画（定理 1）。  
- **着色引理**：对任意字母表大小为 k 的语言族，构造 \(k+1\) 色的迹着色函数，使得对任意真包含关系 \(L \subsetneq L'\)，存在串 \(x \in L\) 使迹不同（引理 2）。该引理自动满足刻画条件，从而无需告密子集。  
- **最优性**：对二进制字母表，证明 2 色不够，故 \(k+1\) 色对满足着色条件是紧的；对自动机模型，\(k+1\) 色对所有 k 都是紧的（引理 3）。  
- **正则语言的特殊性**：正则语言族可仅用 2 色实现极限辨识（扩展结果）。

### 实验或数据  
本文为纯理论工作，未涉及实验或数据集。

### 值得关注点  
- 迹的字母表大小仅与语言字母表大小 k 线性相关（至多 \(k+1\)），与机器状态数无关，远小于先前工作（需状态集大小或指数级）。  
- 迹的定义完全脱离底层机器模型，仅依赖语言本身，更贴近实际注释（如带注释的代码、思维链）。  
- 给出了最优性结果（2 色不足），说明 \(k+1\) 色在一般情况下不可改进。  
- 对正则语言，迹可进一步简化为状态着色，且描述极其简洁。

### 局限性  
- 结果为存在性构造，未讨论迹着色函数是否可高效计算或由学习器自动获得。  
- 假设语言族为可数，且每个语言非空；对于不可数或空语言情形未涉及。  
- 实际应用中，按该方法定义的迹可能与自然出现的注释（如代码注释、思维链）的生成方式不同，实用性有待进一步验证。  
- 结论限于“极限辨识”理论框架，未直接说明对大语言模型训练的实际影响。

## 7. Knowledgeless Language Models: Suppressing Parametric Recall for Evidence-Grounded Language Modeling

- Source: arxiv
- arXiv ID: 2607.12831
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.12831v1
- PDF: https://arxiv.org/pdf/2607.12831v1
- DOI: https://doi.org/10.48550/arXiv.2607.12831

### Authors

Roi Cohen, Yvan Carré, Nick Lechtenbörger, Hendrik Droste, Lucas Kerschke, Russa Biswas, Gerard de Melo, Jan Buys

### Abstract

Language models encode substantial factual knowledge in their parameters, which can lead to unreliable behavior when this knowledge is outdated, incomplete, or misaligned with the provided context. In this work, we study whether modifying the pretraining signal can systematically shift models away from parametric recall and toward evidence-grounded reasoning. We introduce Knowledge--''Less'' Language Models (KLLMs), a fundamentally different epistemic training paradigm for LLMs, which are pretrained on corpora in which named entities are anonymized, thereby removing a primary channel for entity-linked factual supervision. This intervention substantially reduces closed-book factual recall, while often improving performance on tasks where relevant information is provided as context. Across multiple model scales, KLLMs consistently outperform matched baselines on contextual question answering, fact verification, and hallucination detection benchmarks. Crucially, in retrieval-grounded settings with imperfect evidence, KLLMs show improved robustness and achieve up to 20--25\% relative gains over standard language models. They further exhibit better calibration, with improved ECE, Brier score, and AUROC, as well as more reliable abstention behavior. Our results demonstrate that suppressing entity-linked supervision during pretraining induces a shift in epistemic behavior: KLLMs rely less on parametric knowledge and more on external evidence, leading to improved reliability under realistic conditions. This suggests that pretraining-time control over knowledge acquisition can complement retrieval-augmented and tool-based systems by providing a more evidence-sensitive base model.

### 中文一句话结论
本文提出知识缺失语言模型（KLLM），通过在预训练阶段匿名化语料中的命名实体，显著抑制模型的参数化事实回忆能力，从而增强其基于证据的推理能力，在检索增强场景下相对标准模型提升20–25%。

### English TL;DR
This paper introduces Knowledgeless Language Models (KLLMs) pretrained on entity-anonymized corpora to suppress parametric factual recall, achieving up to 20–25% relative gains in retrieval-grounded tasks while improving evidence-grounded reasoning.

### 中文详细总结
本文提出KLLM预训练范式，核心操作为在预训练语料中系统性地将命名实体（人名、地名、组织名等）替换为占位符（如PERSON184）。该干预措施消除了实体级事实监督信号，从而在保持语言建模能力的同时，强制模型转向基于上下文证据的推理模式。实验表明，KLLM在封闭式事实回忆任务上性能接近随机水平（证明参数化知识被有效抑制），而在上下文问答、事实验证和幻觉检测等需要依赖输入信息的任务上，KLLM始终匹配或超越标准语言模型（SLM）。特别地，在检索增强场景下，当提供的证据不完美时，KLLM表现出更强的鲁棒性，相对标准模型取得20–25%的显著提升。此外，KLLM在校准性（ECE、Brier分数、AUROC）和选择性预测（可靠放弃回答行为）方面也表现更优。

### 方法 / 贡献
- **实体匿名化预处理**：使用Flair框架的OntoNotes NER模型（90.0 F1）识别并替换命名实体为类型化占位符（如PERSON184），保留非实体语言结构。
- **全新预训练范式**：从零训练自回归Transformer（LLaMA和SmolLM架构），使用在匿名化语料上训练的BPE tokenizer（30k词表），保持架构与标准模型完全一致。
- **推理流水线**：输入→匿名化→模型推理→实体名称还原，确保训练-测试分布一致。
- **核心贡献**：首次在预训练阶段通过数据层面的实体匿名化，系统性诱导模型从参数化记忆转向证据依赖，为RAG系统提供更可靠的基座模型。

### 实验或数据
- **预训练数据**：使用2.5B tokens（CNN/DailyMail 272M + Wikipedia 2.2B）和10B-20B tokens（基于SmolLM语料混合）。
- **模型规模**：Llama-3.2-1B/3B、Llama-3.1-8B和SmolLM-135M/360M/1.7B各配置均训练配对SLM与KLLM。
- **评估任务**：
  - 封闭式回忆：LAMA基准（验证知识抑制效果）
  - 上下文推理：SQuAD、Natural Questions、FEVER、HaluBench
  - 检索增强：BM25（稀疏检索）、DPR（稠密检索）、工具调用模式
- **对比基线**：随机token掩码、跨度损坏、实体混淆等替代扰动方法。
- **校准评估**：期望校准误差（ECE）、Brier分数、AUROC、选择性预测。

### 值得关注点
1. **性能矛盾突破**：在抑制大量知识的前提下，KLLM在需要上下文推理的任务上不降反升，FEVER F1最高提升+7.8，HaluBench提升+10.4个百分点。
2. **鲁棒性提升**：在检索证据不完美的场景下，KLLM相对SLM获得20-25%的相对提升，表明其对噪声证据的容忍度更强。
3. **校准性改善**：KLLM在ECE、Brier分数和AUROC上均优于SLM，且更可靠地选择在不确定性高时放弃回答，这对高风险应用至关重要。
4. **机制验证充分**：通过多种对照实验（不同扰动方式、不同模型规模、不同数据量）证实匿名化本身是效果来源，而非简单数据损坏。
5. **跨模型泛化**：效果在LLaMA和SmolLM两个独立模型家族上一致复现，证明方法的通用性。

### 局限性
1. **实体回忆残留**：由于NER模型召回率约87-90%，少量稀有实体（多为长尾实体）未被匿名化，可能保留部分知识（但封闭式测试准确率接近随机，表明影响可忽略）。
2. **核心共指保持**：未对代词（he/she等）进行匿名化，导致模型可能捕捉性别等信息，存在引入偏见风险。
3. **描述性知识泄露**：通过描述性指代（如"当前世界最强国家的第44任总统"）可能间接推断实体身份，但此类情况占比很小。
4. **预训练规模限制**：实验最大数据量20B tokens（远小于工业级模型），需要验证在更大规模预训练下的效果稳定性。
5. **非英语泛化**：当前仅针对英语语料进行实验，匿名化策略对其他语言（尤其是形态丰富语言）的有效性尚未验证。
6. **实体知识利用**：在需要核心实体知识但上下文未直接提供的边缘场景中，KLLM可能表现不足（但此类场景本应依赖检索系统）。

## 8. I'm Sorry, but I Can't Help with Braille: Revealing Accessibility Failures in State-of-the-Art LLMs

- Source: arxiv
- arXiv ID: 2607.11893
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.11893v1
- PDF: https://arxiv.org/pdf/2607.11893v1
- DOI: https://doi.org/10.48550/arXiv.2607.11893

### Authors

Abdullah Abdullah

### Abstract

Large Language Models (LLMs) perform strongly on many language tasks, but their capability in structurally constrained, accessibility-critical modalities such as Braille remains unclear. We evaluate state-of-the-art LLMs on bidirectional Korean-Braille translation using a human-annotated dataset. Despite expectations that multilingual, instruction-tuned models can generalize to Braille via text representations, we find consistently poor, unstable outputs and substantial disagreement with human judgments. These results point to missing Braille-aware tokenization and weak alignment between Korean and Braille patterns. In contrast, supervised fine-tuning of a small model (T5-small) on the same data yields large and stable gains over zero-shot and prompted LLM baselines across standard metrics (SacreBLEU, ChrF++, CER, BLEU, ROUGE-L, METEOR, CIDEr). Our findings reveal a systematic limitation of current LLMs and demonstrate the effectiveness of modest task-specific supervision.

### 中文一句话结论  
当前最先进的大语言模型（LLM）在韩语–盲文（Braille）翻译任务上系统性失败，而基于T5-small的有监督微调模型BT5取得了远超LLM和规则基线的性能。  

### English TL;DR  
State-of-the-art LLMs systematically fail at Korean–Braille translation due to missing Braille-aware tokenization and weak alignment; a small fine-tuned model (BT5) achieves large and stable gains, highlighting a critical accessibility gap.  

### 中文详细总结  
本研究首次系统评估了多个前沿LLM（GPT-5、GPT-5-mini、GPT-4、Gemini-3-pro、Claude Opus 4.5、HCX-3）在双向韩语–二级点字翻译上的表现。使用人工标注的NIKL韩语印刷–盲文平行语料库（126,693句对），发现所有LLM均产生不稳定、错误率高的输出，频繁出现拒绝回答、生成无效序列或语义无关的幻觉。相比之下，基于T5-small微调的轻量模型BT5，在韩语→盲文上达到SacreBLEU 95.79、ChrF++ 98.64、CER 0.0043，在盲文→韩语上BLEU-4达0.9662，显著超越规则系统Liblouis和所有LLM。这表明当前LLM在面向无障碍的符号模态上存在系统性盲区，而小规模任务特定监督学习可有效弥补该缺陷。  

### 方法 / 贡献  
- **首次系统评估**：对多个最先进LLM进行韩语–盲文双向翻译能力评测，揭示其普遍失败模式（拒绝、无效输出、语义偏离）。  
- **提出BT5模型**：基于T5-small，采用32k BPE分词（包含盲文Unicode）在有监督平行语料上微调，实现高准确率的双向翻译。  
- **对比基线**：与规则系统Liblouis及多款LLM对比，采用SacreBLEU、ChrF++、CER、BLEU、ROUGE-L、METEOR、CIDEr等多种自动指标。  
- **贡献总结**：指出盲文处理是当前NLP无障碍研究中的关键缺口，并证明任务特定小模型可远超通用大模型。  

### 实验或数据  
- **数据集**：NIKL韩国印刷–盲文平行语料库2023 v1.0，含126,693句对（主要来自新闻和网络帖子），按句子级别划分为101,354训练、12,669验证、12,670测试。  
- **LLM评估**：对GPT-5、GPT-5-mini、GPT-4、Gemini-3-pro、Claude Opus 4.5、HCX-3使用相同提示和确定性解码；因大部分模型频繁拒绝或产生无效输出，LLM定量评估仅基于5样本受控探针，并以定性分析补充。  
- **BT5训练**：基于T5-small，输入输出为UTF-8文本，盲文符号作为原子单位；使用AdamW（学习率1e-4），最大长度128，按验证损失选择模型。  
- **结果**：BT5在韩语→盲文任务上SacreBLEU 95.79（Liblouis为71.94），ChrF++ 98.64，CER 0.0043；盲文→韩语任务上BLEU-4 0.9662、ROUGE-L 0.9859、METEOR 0.7758、CIDEr 9.6382，全面大幅领先。  

### 值得关注点  
1. **LLM系统性失败**：所有测试LLM均表现出拒绝、输出无效序列或语义无关内容，表明缺乏盲文感知分词和表征对齐。  
2. **小模型大幅超越大模型**：仅需1亿参数级别的T5-small在监督微调后，性能远超数千亿参数的LLM，说明针对特定符号模态的任务专属训练极为有效。  
3. **无障碍缺口**：当前LLM在辅助技术关键领域（如盲文）存在严重盲点，提示亟需纳入盲文感知能力。  
4. **BT5的高精度**：在字符级和生成级指标上接近完美，展示了规则约束性翻译任务的可行路径。  

### 局限性  
- **语言局限**：仅针对韩语–二级点字，结论未必推广到其他语言或盲文系统。  
- **模型范围有限**：仅测试了部分代表性LLM和一种韩国LLM，未穷尽所有模型/提示策略；许多LLM拒绝回答导致无法进行全测试集定量比较，评估以受控样本和定性分析为主。  
- **比较不完美**：BT5因有监督微调和专门分词器而天然具有优势，与LLM的直接对比存在架构差异。  
- **自动指标局限**：BLEU、ChrF++等仅捕获表面相似性，未评估实际可读性、功能性或合规性；缺乏盲人用户的人工评估。  
- **数据依赖**：训练依赖人工标注平行语料，在低资源场景下获取成本高；未探索数据增强、半监督或跨语言迁移。  
- **部署风险**：盲文翻译错误在无障碍场景中可能造成严重后果，未经过严格验证的模型不适合直接部署。

## 9. Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?

- Source: arxiv
- arXiv ID: 2607.12787
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.12787v1
- PDF: https://arxiv.org/pdf/2607.12787v1
- DOI: https://doi.org/10.48550/arXiv.2607.12787

### Authors

Kaiwen Zheng, Junchen Fu, Wenhao Deng, Hu Han, Joemon M. Jose, Xuri Ge

### Abstract

Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc. However, these performance improvements are often accompanied by an increase in model parameter size (e.g, at least 7B), which simultaneously incurs high computational costs and reduces inference efficiency, thereby hindering real-time deployment on resource-constrained platforms such as robots and mobile devices. This raises a fundamental question: do we really need the multimodal MER model larger than 1B parameters for high-quality MER?
  In this paper, we challenge the assumption that larger models are inherently necessary and proposes a lightweight MER framework (called Light-MER), which achieves better and faster multimodal sentiment understanding and recognition through knowledge distillation. It can transfer knowledge from a strong, large-scale teacher model to a lightweight sub-billion-parameter student model, aiming to preserve rich multimodal emotion reasoning and recognition while substantially improving deployment efficiency. Specifically, we introduce two new optimization strategies to enhance knowledge transfer: (1) a new optimal transport loss that combines Sliced Wasserstein Distance with hidden-state alignment, and (2) a new multi-reward optimization strategy based on GRPO that balances MER performance and efficiency, aimed at further enhancing the learning capabilities of student models. Extensive experiments on nine benchmark datasets demonstrate that Light-MER achieves state-of-the-art performance while significantly improving inference efficiency. This highlights the strong potential of small multimodal emotion language models for future research. Code is available at https://github.com/GAIR-Lab/Light-MER.

### 中文一句话结论
本文证明，通过知识蒸馏和轻量化设计，参数不超过1B的多模态情感识别模型同样可以取得与7B以上大模型相当甚至更优的性能与效率，挑战了大模型必然更好的假设。

### English TL;DR
The paper introduces Light-MER, a lightweight multimodal emotion recognition framework that uses knowledge distillation to achieve state-of-the-art performance and efficiency with sub-1 billion parameters, challenging the necessity of larger models.

### 中文详细总结
论文围绕“是否真的需要超过1B参数的多模态情感语言模型”这一核心问题，提出了Light-MER框架。该框架通过知识蒸馏将一个大容量（8B参数）教师模型的推理能力迁移至轻量级（0.6B参数）学生模型，实现高效的部署。具体引入两项创新优化：一是基于切块Wasserstein距离的隐藏状态对齐（SWD-H），以保持教师与学生在多模态潜在空间中的分布几何结构；二是基于GRPO的多奖励优化策略（M-GRPO），在保持情感识别准确率的同时提升输出简洁性和生成质量。实验在九个基准数据集上表明，Light-MER在显著提升推理效率的同时达到最先进性能，证明了小模型在生成式多模态情感识别中的巨大潜力。

### 方法 / 贡献
- 提出Light-MER轻量级教师-学生蒸馏框架，将大模型的多模态情感推理能力压缩至亚十亿参数学生模型。
- 设计SWD-H隐藏状态对齐损失，利用切块Wasserstein距离对齐教师与学生潜在分布，保留多模态表示几何结构。
- 提出M-GRPO多奖励策略优化，同时约束情感准确性、生成简洁性、信息密度、完整性和低重复性，进一步提升学生模型输出质量。
- 挑战“大模型必然更好”的假设，为资源受限平台（机器人、手机等）上的实时情感识别提供可行方案。

### 实验或数据
在九个基准数据集上进行广泛实验。实验表明Light-MER在取得最先进性能的同时显著提升推理效率。具体数据集名称未在摘要中列出，代码已公开：https://github.com/GAIR-Lab/Light-MER。

### 值得关注点
- 首次系统性探索低于1B参数的多模态情感语言模型可行性，突破现有方法至少7B参数的瓶颈。
- 将最优传输理论与GRPO强化学习结合用于情感推理蒸馏，方法创新性强。
- 兼顾性能与效率，适用于机器人、智能手机等边缘设备部署，实用价值高。

### 局限性
- 依赖大规模教师模型（8B参数），训练阶段计算成本仍较高。
- 蒸馏过程中可能丢失部分复杂的、细微的情感推理能力，尤其是在多模态冲突场景下。
- 实验主要在英语多模态数据集上进行，跨语言迁移能力未知。
- 论文未在摘要中明确讨论其他潜在局限性（如不同情感类别性能差异、对噪声模态的鲁棒性等）。

## 10. CANDI: Contextual Alignment for Niche Domains Question Answering

- Source: arxiv
- arXiv ID: 2607.11891
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.11891v1
- PDF: https://arxiv.org/pdf/2607.11891v1
- DOI: https://doi.org/10.48550/arXiv.2607.11891

### Authors

Megha Chakraborty, Darssan L. Eswaramoorthi, Het Riteshkumar Shah, Madhur Thareja, Michelle A Ihetu, Harshul Raj Surana, Kaushik Roy, Amit Sheth

### Abstract

The deployment of large language models (LLMs) in specialized domains like medical diagnostics and financial advisory necessitates evaluating capabilities beyond general knowledge. Traditional question-answering benchmarks often fail to capture the nuanced contextual grounding, user awareness, and domain understanding these fields require. To address this, we introduce CANDI-QA (Contextual Alignment for Niche Domains Question Answering), a novel dataset evaluating LLMs on delivering accurate, context-sensitive, and user-aligned answers in specialized settings. CANDI-QA features expert-curated question-answer pairs structured into two categories: (1) Information Assistance Questions, which are direct, factual queries requiring precise extraction, and (2) Applied Inference Questions, which are multi-hop reasoning tasks needing situational inference to generate actionable insights. We evaluate over ten diverse language models, from compact open-source to state-of-the-art proprietary systems. As a robust baseline, we present MTSS-Net, a lightweight neuro-symbolic framework combining neural retrieval with rule-based reasoning. Our findings highlight the profound challenges of achieving contextual alignment in niche domains, revealing the limitations of current LLMs without enhanced contextual or symbolic integration. Ultimately, CANDI-QA serves as a critical benchmark for advancing research in context-aware language models, stimulating the development of robust, trustworthy AI for high-stakes domains.

### 中文一句话结论
本文提出 CANDI-QA 数据集和 MTSS-Net 基线，揭示了当前大语言模型在专业领域（如行为健康）中实现上下文对齐的显著局限性。

### English TL;DR
The paper introduces CANDI-QA, a novel dataset and benchmark for evaluating large language models on context-sensitive and user-aligned question answering in specialized domains, and proposes a neuro-symbolic baseline (MTSS-Net), highlighting current LLMs' limitations in achieving true contextual alignment.

### 中文详细总结
该研究针对大语言模型在专业领域（如医疗诊断、金融咨询和行为健康）部署时面临的上下文对齐挑战，提出了 CANDI-QA 数据集。该数据集包含 315 个专家策划的问题，分为两类：T1 信息辅助问题（90 个，直接事实性查询）和 T2 应用推理问题（225 个，需要多跳推理和情境推断）。研究对 10 个语言模型（从紧凑开源到顶尖商业系统）进行了系统评估，并提出了一个轻量级神经符号基线框架 MTSS-Net，结合神经检索与基于规则的推理。评估使用了多种指标：T1 问题采用基于参考答案的指标（余弦相似度、BERTScore、MoverScore、BLEURT）；T2 问题采用 RAG 评估框架（上下文精度、响应相关性、忠实度、语义相似度）。结果揭示了大语言模型在专业领域中实现真正上下文对齐的深刻挑战。

### 方法 / 贡献
- **提出新任务**：正式定义“专业领域问答的上下文对齐”（CANDI-QA），要求模型根据用户角色、领域和对话背景生成对齐的回答。
- **构建数据集**：在行为健康领域的多层级支持系统（MTSS）框架下，由专家策划 315 个问题，包含直接事实查询（T1）和复杂推理问题（T2）。
- **系统评估**：在 10 个语言模型上（Phi-4、Deepseek、Qwen3、Gemma、Gemini、LLaMA 3.1/3.2/4、Mistral）测试三种提示策略：无上下文（P1）、角色感知（P2）和任务感知（P3）。
- **神经符号基线**：提出 MTSS-Net，一种轻量级神经符号框架，结合神经检索与基于规则的推理，作为基准解决方案。

### 实验或数据
- **数据集**：315 个专家策划的问题，90 个 T1（信息辅助）和 225 个 T2（应用推理），来自行为健康领域 MTSS 框架。
- **模型**：评估了 10 个模型：Phi-4-mini-instruct (3.8B)、Deepseek R1、Qwen3 (32B)、Gemma 2 (9B)、Gemini1.5、LLaMA 3.1 (8B) - Instruct、LLaMA 3.2 (1B) - Instruct、LLaMA 4 Maverick (7B)、LLaMA 4 Scout (17B)、Mistral 7B Instruct。
- **提示策略**：三种策略——P1（无上下文）、P2（角色感知）、P3（任务感知）。
- **评估指标**：T1：余弦相似度、BERTScore、MoverScore、BLEURT（与专家金标准答案对比）。T2：RAGAs 框架的上下文精度、响应相关性、语义相似度。

### 值得关注点
- **数据集专业性**：由行为健康领域专家（SBHA）策划，问题设计反映真实世界 MTSS 团队的挑战。
- **双类型问题设计**：区分直接事实查询（T1）和复杂推理问题（T2），提供更全面的评估维度。
- **提示策略影响**：实验揭示了不同提示策略对模型性能的影响，角色和任务感知提示可能提升上下文对齐。
- **神经符号框架潜力**：MTSS-Net 作为轻量级基线，展示了神经检索与符号推理结合的可能性。

### 局限性
- **领域特定性**：数据集仅限于行为健康领域的 MTSS 框架，结论可能不完全适用于其他专业领域。
- **评估指标局限**：T1 问题依赖参考标准答案，可能无法完全捕捉回答的临床合理性和实用性；T2 问题的 RAG 评估依赖 Qwen 模型生成上下文，存在偏差。
- **模型覆盖**：仅评估了 10 个模型，且未包含所有最新商业系统（如 GPT-4、Claude 等）。
- **缺乏人工评估**：未开展系统的人工评估或专家评审，以验证模型回答在真实应用中的可接受性。
- **基线方法简单性**：MTSS-Net 是一个初步的神经符号基线，未探索更复杂的符号推理或知识图谱整合。

## Processing Notes

- Duplicate papers skipped: 0