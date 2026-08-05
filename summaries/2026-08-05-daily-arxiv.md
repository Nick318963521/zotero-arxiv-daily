# Daily arXiv - 2026-08-05

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-05T23:08:27
- Paper count: 10

## 1. ConlangBench: Exploring Language Knowledge and Learning in LLMs through Diverse Constructed Languages

- Source: arxiv
- arXiv ID: 2608.03505
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2608.03505v1
- PDF: https://arxiv.org/pdf/2608.03505v1
- DOI: https://doi.org/10.48550/arXiv.2608.03505

### Authors

Jinhong Jeong, Seungyeop Yi, Sangah Lee, Youngjae Yu

### Abstract

Constructed languages (conlangs) are intentionally created human languages with a rich tradition of linguistic creativity. Despite their potential for studying language learning in large language models (LLMs), existing conlangs remain largely underexplored in LLM research. We present ConlangBench, the first large-scale benchmark for evaluating and training LLMs on 21 existing conlangs. We collect over 21M conlang-English parallel sentence pairs (including 430K pairs across the 20 non-Esperanto conlangs) and 321K vocabulary entries. In bidirectional translation experiments, we find that models perform better on a posteriori conlangs, whose vocabularies are derived from natural languages, reflecting the design characteristics of conlangs. Training on ConlangBench also shows that models can learn all eight conlangs for which sufficient parallel corpora are available, while their learning curves vary depending on how the conlangs were created. Our findings suggest that conlangs provide a unique testbed for investigating how LLMs acquire low-resource languages.

### 中文一句话结论
ConlangBench 首次构建了包含21种人造语言的大规模平行语料库，实验表明LLM在后验型人造语言（词汇源于自然语言）上翻译表现更好，且通过平行语料训练可学会所有语料充足的人造语言，学习曲线因语言构造方式而异。

### English TL;DR
ConlangBench introduces the first large-scale benchmark of 21 constructed languages with parallel corpora and vocabularies, revealing that LLMs perform better on a posteriori conlangs (derived from natural languages) and can learn all conlangs with sufficient data, with learning trajectories influenced by conlang design, demonstrating their value as a testbed for studying low-resource language acquisition.

### 中文详细总结
ConlangBench 是一个针对21种现存人造语言（conlang）的基准测试，包含超过2100万条人造语言-英语平行句对（其中非世界语的20种语言有43万条）和32.1万词汇条目。在双向翻译实验中，开放权重的LLM在后验型（a posteriori）人造语言（如国际语、伊多语）上得分显著高于先验型（a priori）人造语言，反映出模型利用预训练中获得的自然语言词汇知识。训练实验表明，模型能够学会所有8个语料充足的语种，但学习曲线因语言类别（如辅助语、艺术语、工程语）而异。研究还发现，词汇信息的显式提供对先验型语言帮助更大，进一步证实了词汇相似性的作用。ConlangBench 为研究LLM如何习得低资源语言提供了独特测试平台。

### 方法 / 贡献
- 构建了首个大规模现存人造语言平行语料库，覆盖21种语言，含2100万+句对和32.1万词汇条目。
- 评估了12种LLM（包含开源和商业模型）在双向翻译上的表现，揭示翻译性能反映人造语言设计特征。
- 分析了模型通过平行语料训练学习人造语言的过程，发现不同类别语言的学习轨迹存在差异，并验证了词汇知识的习得。

### 实验或数据
- **数据集**：21种人造语言，来自OPUS、Tatoeba、Hugging Face及30多个官方/粉丝网站。预处理后获得2100万+句对（非世界语43万句对），并收集32.1万词汇条目。每种语言按9:1划分训练/测试集。
- **翻译实验**：12个LLM（如GPT-5.5、Gemini 3 Flash、Gemma 4、Qwen3.5等）在双向翻译任务上，使用chrF++评分。
- **训练实验**：对8个语料充足的语言（如Lojban、Toki Pona、Quenya、Klingon、世界语等）进行微调（基于Qwen3.5-9B），观察学习曲线。
- **词汇效用实验**：在推理时提供词汇表，对比先验型与后验型语言的性能提升。

### 值得关注点
- 后验型辅助语（如国际语、伊多语）翻译得分显著高于先验型，Volapük因词汇高度修改而得分异常低，符合其历史。
- Toki Pona 中，生成（英→人造语）比理解（人造语→英）更容易，因其“最小化”设计导致语义歧义。
- 预训练语料暴露程度与翻译性能的关系因语言类别而异：后验型语言随暴露增加而提升，先验型则无显著关联。
- 显式提供词汇信息对先验型语言增益更大（如Qwen3.5-9B平均+9.8 vs 后验型+5.1），表明模型依赖自然语言词汇知识。

### 局限性
- 仅涵盖21种人造语言，且主要依赖ISO 639-3代码和Glottolog注册，可能遗漏其他重要或新兴人造语言。
- 非世界语语种数据量较小（仅43万句对），训练实验仅针对8个语料充足的语言，泛化性有限。
- 评估仅基于翻译任务，未涉及其他语言能力（如语法判断、语义理解）。
- 预训练暴露估计使用Infini-gram和OLMo-2语料，可能无法完全代表所有模型的预训练数据。

## 2. TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation

- Source: arxiv
- arXiv ID: 2608.02975
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.02975v1
- PDF: https://arxiv.org/pdf/2608.02975v1
- DOI: https://doi.org/10.48550/arXiv.2608.02975

### Authors

Bhavin Jawade, Cameron R. Wolfe

### Abstract

Large language models (LLMs) have demonstrated impressive performance in MQM-based translation quality (TQ) evaluation, and recent advances in large reasoning models (LRMs) promise even greater improvements. However, both LLMs and LRMs are computationally expensive to deploy at scale, while small language models (SLMs)---though much more efficient---struggle with the complex reasoning required for evaluation tasks. In this work, we present an extensive empirical study benchmarking SLMs, LLMs, and LRMs across a wide range of TQ evaluation setups, providing a comprehensive view of the current landscape and establishing best practices. To address the scalability challenge, we introduce TQLite, a novel distillation framework that enables SLMs to approach the MQM evaluation performance of the best LRM-based evaluators. Our approach leverages a multi-LRM jury to generate high-quality synthetic training data via practical data curation techniques and aggregation of evaluation responses across a diverse panel of models. Our results demonstrate that SLMs trained via TQLite achieve strong MQM evaluation performance that far exceeds off-the-shelf evaluation capabilities of standard SLMs, offering a scalable and cost-effective alternative to LLM- and LRM-based evaluators.

### 中文一句话结论
TQLite通过多LRM（大型推理模型）陪审团引导的蒸馏框架，使小语言模型（SLM）在MQM翻译质量评估中达到接近最佳LRM的性能，同时大幅降低计算成本。

### English TL;DR
TQLite is a distillation framework that uses a multi-LRM jury to train small language models for efficient, real-time MQM-based translation quality evaluation, achieving performance competitive with larger models while being more cost-effective.

### 中文详细总结
本论文针对机器翻译质量评估中的可扩展性问题，提出TQLite蒸馏框架。大型语言模型（LLM）和大型推理模型（LRM）虽在MQM评估中表现优异，但计算成本高；而小语言模型（SLM）虽高效，但推理能力不足。论文首先对SLM、LLM、LRM在多种翻译质量评估设置下进行了广泛基准测试，揭示了当前模型的性能差异与最佳实践。在此基础上，TQLite利用多LRM陪审团，通过实用数据筛选技术和多模型评估响应聚合，生成高质量合成训练数据，将SLM蒸馏为高效的评估器。实验表明，经TQLite训练的SLM在MQM评估性能上远超标准SLM，接近甚至媲美最优LRM，提供了可扩展、低成本的替代方案。

### 方法 / 贡献
- 提出TQLite蒸馏框架，利用多LRM陪审团生成合成训练数据，并通过多数投票聚合评估结果。
- 提供全面的LLM/LRM/SLM基准测试，涵盖多种模型规模、开放程度和推理模式，并总结最佳实践。
- 实现SLM在MQM评估中的性能跃升，使之成为高效、开放且成本可控的评估工具。

### 实验或数据
- 实验主要基于WMT22 metrics任务测试集，包含三个语言对（zh-en, en-de, en-ru）和约10.6万个待评估片段，覆盖新闻、社交、对话、电商四个领域。
- 使用系统级和片段级成对准确率（含校准）作为评估指标，并采用官方WMT评估脚本。
- 基准模型包括GPT-4o、Gemma-3系列、Qwen-3等LLM及MetricX、COMET-22等学习指标。

### 值得关注点
- TQLite训练的SLM在片段级和系统级准确率上均显著超越标准SLM，接近最优LRM。
- 揭示了Gemma-3-27b-it等开放模型在翻译质量评估中可与GPT-4o相媲美，而Qwen-3因输出过多错误跨度导致性能不佳。
- 方法强调实际部署中的成本与效率，适合实时评估场景。

### 局限性
- TQLite依赖多个LRM生成训练数据，其初始数据收集和蒸馏过程仍可能涉及一定计算开销。
- 实验仅基于WMT22测试集，未验证在更广泛语言对或领域上的泛化能力。
- 蒸馏后的SLM性能虽接近但仍未超越最优LRM，且推理跟踪（long CoT）的利用程度有限。

## 3. Interpreting Black-Box Large Language Models with Sentence-Level Energy Landscapes

- Source: arxiv
- arXiv ID: 2608.02879
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.02879v1
- PDF: https://arxiv.org/pdf/2608.02879v1
- DOI: https://doi.org/10.48550/arXiv.2608.02879

### Authors

Maryam Rezaee, Pooriya Safaei, Maryam Asgarinezhad, Fatemeh Seyyedsalehi

### Abstract

The widespread adoption of proprietary Large Language Models (LLMs) accessed strictly through closed APIs has created a critical challenge for responsible deployment: a fundamental lack of interpretability. To address this, we propose a model-agnostic, post-hoc attribution interpreter operating at the sentence level. Our approach trains an Energy-Based Model (EBM) as a surrogate to capture the LLM's internal conceptual consistency between prompts and responses. This energy landscape guides the training of a lightweight interpreter network. Uniquely, our interpreter operates as a standalone tool; once trained, it quantifies the influence of prompt sentences on a user-specified target output without requiring further API queries to the LLM. By globally training a local interpreter across diverse inputs, our framework captures broader generation patterns and mitigates instance-specific biases. Experiments demonstrate that our EBM accurately simulates the target LLM, allowing the interpreter to effectively identify the prompt sentences most influential in generating specific target outputs.

### 中文一句话结论
本文提出一种基于句子级能量景观的黑盒大语言模型归因解释方法，通过能量模型代理与轻量解释器，在不需额外API查询的情况下识别对特定输出最关键的输入句子。

### English TL;DR
This paper proposes a model-agnostic post-hoc attribution interpreter that uses an Energy-Based Model surrogate to capture the conceptual consistency of a black-box LLM, then trains a standalone interpreter to identify which prompt sentences most influence a given target output without requiring further API queries.

### 中文详细总结
针对闭源黑盒大语言模型缺乏可解释性的问题，本文提出一种模型无关的事后归因解释方法。该方法以句子为基础概念单元，首先训练一个基于Transformer的能量模型作为替代模型，学习提示与响应之间的整体一致性；随后利用该能量景观训练一个轻量级解释器网络，在无需后续API查询的情况下，从输入提示中识别出对生成用户指定目标输出最具影响力的句子子集。通过全局训练（跨多样输入），框架能捕获更广的生成模式并缓解实例级偏差。

### 方法 / 贡献
1. **分析粒度迁移**：将归因从易混淆的token级别提升到语义完整的句子（“概念”）级别，使解释更符合人类理解。
2. **两阶段框架**：先预训练能量模型（EBM）作为黑盒LLM的可微分代理，避免直接访问模型内部；再基于该能量训练解释器网络，输出稀疏二值向量标识关键输入句子。
3. **能量模型设计**：采用自注意力将静态句嵌入投影到动态概念空间，通过跨注意力建模输入-输出交互，并利用对比学习（忠实性目标与局部依赖目标）训练，使能量模型捕捉LLM的生成模式。
4. **独立部署优势**：解释器训练后可作为独立工具使用，推理时不需再调用原始LLM的API。

### 实验或数据
摘要中未提及具体实验数据集或基准方法，仅声明“实验表明EBM能准确模拟目标LLM，解释器可有效识别最影响特定输出的提示句子”。具体实验设置、数据来源和定量结果需参考全文。

### 值得关注点
1. **黑盒可解释性的实用方案**：无需模型梯度、激活或架构信息，仅依赖输入-输出数据，适用于当前多数闭源API场景。
2. **句子级归因**：相比token级，句子作为完整命题更能反映因果逻辑，且更易被人类验证。
3. **独立推理能力**：训练后的解释器不再需要API调用，降低了使用成本和隐私依赖。

### 局限性
1. 摘要未提供实证对比实验或可重复的量化指标，有效性和优越性需更多验证。
2. 能量模型作为替代代理，其与真实LLM决策过程的一致性或存在偏差，可能影响归因忠实度。
3. 方法依赖高质量的句子分割和嵌入表示，长文本或多语言场景下的鲁棒性未讨论。
4. 仅针对“句子”作为概念单元，未探讨其他粒度（如短语、段落）的适用性。

## 4. Cross-Lingual Bias in Large Language Models: A Comparative Analysis of English and Swahili

- Source: arxiv
- arXiv ID: 2608.03532
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.03532v1
- PDF: https://arxiv.org/pdf/2608.03532v1
- DOI: https://doi.org/10.48550/arXiv.2608.03532

### Authors

Ruolei Zhang, Teddy Njuguna, Yue Feng

### Abstract

Large language models are increasingly deployed in multilingual contexts, yet safety alignment and bias evaluation remain overwhelmingly English-centric. We investigate whether social biases generalise across languages by submitting 4,900 symmetric English--Swahili prompt pairs to GPT-5.2 and Gemini 2.5 Flash across nine demographic bias axes, yielding 19,600 completions evaluated for stereotype prevalence, sentiment, refusal behaviour, and cross-lingual semantic similarity. Our findings show that bias transforms rather than transfers: stereotype rates shifted by up to 12 percentage points on specific axes, Gemini's neutral-sentiment rate doubled in Swahili, and GPT-5.2 refused 169 prompts in English and zero in Swahili, consistent with refusal behaviour anchored to English-language surface forms at the behavioural level. Over 55% of prompt pairs produced semantically dissimilar completions across both models. These reinforce the idea that English-only bias audits do not produce adequate coverage for multilingual deployment.

### 中文一句话结论
大型语言模型中的社会偏见不是简单地跨语言“转移”，而是发生“转化”：模型在英语和斯瓦希里语中展现出不同的刻板印象比率、情感分布和拒绝行为，仅凭英语的偏见审计无法有效覆盖多语言部署场景。

### English TL;DR
Social biases in large language models transform rather than transfer across languages, as shown by asymmetric stereotype rates, sentiment shifts, and refusal behaviors—such as GPT-5.2 refusing 169 English prompts but zero Swahili prompts—demonstrating that English-only bias audits are insufficient for multilingual deployment.

### 中文详细总结
该研究通过向GPT-5.2和Gemini 2.5 Flash提交4,900组对称的英语-斯瓦希里语提示对，涉及九个社会偏见维度，获得了19,600条模型输出。研究发现：
1. **偏见转化而非转移**：刻板印象比率在特定维度上最多偏移12个百分点；Gemini在斯瓦希里语中的中性情感比率翻倍（从19.8%增至39.6%）。
2. **拒绝行为不对称**：GPT-5.2在英语中拒绝了169个提示，但在斯瓦希里语中没有拒绝任何提示，且拒绝集中在种族/民族维度（61.5%）。
3. **语义不一致**：两个模型超过55%的英-斯提示对产生了语义上不相似的输出（GPT-5.2为44.6%相似，Gemini为38.4%相似）。
4. **外部验证**：使用Claude Sonnet 4.5作为评判模型，在英语-斯瓦希里语翻译数据集上进行测试，显示其在斯瓦希里语上的分类准确率平均下降4-8个百分点，表明结果可能被低估。

### 方法 / 贡献
1. 构建了首个系统的英语-斯瓦希里语跨语言偏见比较数据集，包含4,900组对称提示对。
2. 提供了GPT-5.2拒绝行为锚定于英语语言表层形式的证据（169次英语拒绝 vs 0次斯瓦希里语拒绝）。
3. 实证表明跨语言偏见发生转化而非简单转移，挑战了多语言模型保持语言不变社会表征的假设。
4. 采用了双流水线评估：Pipeline 1独立分类（刻板印象存在性和情感），Pipeline 2比较语义相似性。

### 实验或数据
- 模型：GPT-5.2和Gemini 2.5 Flash
- 提示：4,900组对称英语-斯瓦希里语提示对，覆盖种族/民族、宗教、性别、年龄、残疾、社会经济地位、教育水平、移民身份和国籍/出身九个维度
- 输出：19,600条模型完成（每个模型9,800条）
- 评判模型：Claude Sonnet 4.5（避免自我评估偏见）
- 外部验证：使用SAD v1数据集（英语-斯瓦希里语翻译）测试评判模型可靠性
- 人类验证：斯瓦希里语母语者验证了输入提示和200条输出（语义相似性流水线一致率95%）

### 值得关注点
1. **偏见不对称性**：GPT-5.2在英语中拒绝169个提示，但在斯瓦希里语中为零拒绝，揭示安全对齐的严重语言偏差。
2. **非语言中性表现**：Gemini在斯瓦希里语中更倾向于使用平淡、中性的语言进行刻板描述，而非更极端的负面表达。
3. **语义不一致率超过55%**：表明即使使用相同的提示模板，模型在不同语言中生成的内容本质差异显著。
4. **方法严谨性**：使用温度=0（贪心解码）隔离语言变量；进行Bonferroni校正和Cramér's V效应量分析；人类验证揭示了机器翻译的深层问题。

### 局限性
1. 研究仅覆盖英语和斯瓦希里语两种语言，无法推广到其他低资源语言。
2. 机器翻译的质量问题（包括洋泾浜式表达和翻译幻觉）可能影响结果的可靠性（如“mixed-race”被直译而非使用“chotara”）。
3. Claude Sonnet 4.5作为评判模型在斯瓦希里语上的敏感度降低8个百分点，可能导致跨语言差异被低估。
4. 研究仅关注行为层面的结果，虽然进行了logit lens分析（Qwen-2.5-3B），但无法直接观察黑盒模型的内部机制。
5. 仅测试了两种商业模型（GPT-5.2和Gemini 2.5 Flash），可能无法代表所有大型语言模型。
6. 提示模板仅限于句子完成形式，未探索其他生成类型（如问答、对话等）中的偏见表现。

## 5. On the Diversity of Analogy Making in Large Language Models

- Source: arxiv
- arXiv ID: 2608.03233
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.03233v1
- PDF: https://arxiv.org/pdf/2608.03233v1
- DOI: https://doi.org/10.48550/arXiv.2608.03233

### Authors

Yuanhao Shen, Daniel Xavier de Sousa, Caio César Sifuentes Barcelos, Hongyu Guo, Xiaodan Zhu

### Abstract

Large Language Models (LLMs) have demonstrated remarkable potential for analogy making, a core cognitive capability that drives novelty and creativity. While prior research has extensively investigated the applications and underlying mechanisms of LLM-based analogy making, its output diversity remains largely unexplored, despite being essential for broadening cross-domain connections and fostering scientific innovation. In this work, we present a comprehensive evaluation of analogy diversity across ten state-of-the-art open- and closed-source LLMs. Our findings highlight a concerning issue of domain homogeneity, a prevalent tendency for LLMs to generate analogies from a narrow set of target domains, limiting both inter-query and intra-model diversity. Furthermore, our analysis reveals a fundamental trade-off in existing LLM diversity-enhancement methods: increasing output diversity often comes at the expense of output quality. Finally, our causal analysis of LLM information flow reveals substantial differences in the model-sensitive regions governing analogy diversity across LLMs, suggesting a potential mechanism for the observed diversity-quality trade-off. To our knowledge, this is among the first studies to systematically investigate output diversity in LLM-based analogy making.

### 中文一句话结论
大语言模型在类比生成中普遍存在领域同质化问题，且提升多样性往往以牺牲生成质量为代价，其内部机制在不同模型间差异显著。

### English TL;DR
This paper evaluates analogy diversity in large language models, revealing a tendency towards domain homogeneity and a fundamental trade-off between output diversity and quality, with causal analysis of model internals suggesting mechanistic bases for this trade-off.

### 中文详细总结
论文对10个开源和闭源大语言模型在类比生成任务上的输出多样性进行了全面评估。研究发现，模型普遍存在“领域同质化”现象，即生成的类比集中于少数目标领域，限制了跨领域连接和创新。此外，现有多样性增强方法（如多样性提示、概率扰动、熵门控）在提高多样性时往往会降低类比质量，揭示出多样性-质量之间的权衡。对模型内部信息流的因果分析表明，不同模型控制类比多样性的敏感区域存在显著差异，这可能解释了多样性-质量权衡的机制。

### 方法 / 贡献
**方法：** 使用三个数据集（AnaloBench、Metaphoric Analogies、MUNCH），对10个LLM生成类比，采用多种推理时扰动方法（多样性提示、Top-k/p采样、Min-p、G2、熵门控）。评估指标包括句子语义多样性、领域多样性、MAUVE分数和质量评分。**贡献：** 首次系统研究LLM类比生成的输出多样性；揭示领域同质化现象；发现多样性-质量权衡及其可能的机制基础。

### 实验或数据
实验基于三个类比生成数据集：AnaloBench（340对故事级类比）、Metaphoric Analogies（203个结构化类比映射）、MUNCH（提取1000个隐喻句子）。模型包括GPT-5.2、Grok-4.5、Gemini-2.5/3.1、Claude-4.6等闭源模型，以及Llama-3.1-8B、Gemma2-9B、Qwen-3-8B、Mistral-7B、Phi-4-mini等开源模型。每个样本生成10个输出进行评估。

### 值得关注点
1. 领域同质化问题严重，模型倾向于生成相似领域的类比，限制创造力。  
2. 多样性提升往往导致质量下降，现有方法（如多样性提示、采样扰动）效果有限。  
3. 不同模型内部机制差异显著，缺乏一致的类比处理区域，可能导致多样性-质量权衡。

### 局限性
未覆盖所有可能的LLM；数据集有限（仅三个）；扰动方法未涵盖所有可能策略；因果分析仅初步探索；未深入探讨如何克服多样性-质量权衡。

## 6. Enhancing Tabular Learners with Context-Aware Semantic Embeddings

- Source: arxiv
- arXiv ID: 2608.03565
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.03565v1
- PDF: https://arxiv.org/pdf/2608.03565v1
- DOI: https://doi.org/10.48550/arXiv.2608.03565

### Authors

Günther Schindler, Maximilian Schambach, Johannes Höhne

### Abstract

While modern tabular learners excel at capturing statistical patterns, they frequently operate in a semantic vacuum, treating textual features as discrete symbols, ignoring the rich semantics inherent in feature names or cell entries. We propose CASE (Context-Aware Semantic Embeddings), a novel framework that bridges the gap between the semantic understanding of Large Language Models (LLMs) and the statistical capabilities of tabular learners. Unlike existing methods that embed rows in isolation, CASE utilizes a contextualization strategy: we pre-fill the KV cache of a custom-trained Gemma 3-based Tabular Language Model with a representative sample of rows to establish a persistent anchor of the dataset's semantics. This ensures that generated row embeddings are dynamically contextualized, resolving semantic ambiguities and anchoring representations in domain-specific context. Our experiments across several benchmarks (CARTE, TextTab, and TabArena) demonstrate that CASE substantially improves the performance of tabular learners on semantically rich datasets, particularly in low-data regimes.

### 中文一句话结论
CASE通过将大语言模型的语义理解与表格学习器的统计能力结合，利用上下文感知的行嵌入显著提升了表格预测性能，尤其在低数据场景中。

### English TL;DR
CASE enhances tabular learners by using a contextualized LLM-based embedding strategy that pre-fills the KV cache with dataset samples, generating semantically rich row embeddings that significantly improve performance, especially in low-data regimes.

### 中文详细总结
传统表格学习器（如梯度提升树）擅长捕捉统计模式，但缺乏语义理解，常将文本特征视为离散符号。CASE提出一种新框架，首先基于Gemma 3模型预训练一个表格语言模型（Tabular Language Model, TLM），使用列插值目标进行训练。然后，通过“上下文启动”策略：用训练集的一批代表性样本预填充TLM的KV缓存，建立数据集的持久语义锚点。这样，对每一行生成嵌入时，会动态考虑整个数据集的上下文，消除歧义。这些行嵌入经PCA降维后，与原始特征拼接，供下游表格学习器（如AutoGluon、TabICL等）使用。实验在CARTE、TextTab和TabArena三个基准上进行，结果显示CASE在语义丰富的数据集上显著提升性能，尤其在低数据场景下。

### 方法 / 贡献
- **方法**: (1) 继续预训练Gemma 3模型，采用表格序列化（表头+行序列）和仅对目标列计算损失的自回归训练目标。 (2) 提出“上下文启动”：用随机采样的训练行预填充KV缓存，再对每个目标行提取[EOT]（原文[BOT]，但应统一）位置的隐藏层输出作为上下文感知嵌入。 (3) 嵌入经PCA降维后与原始特征拼接，兼容任何表格学习器。
- **贡献**: 首次将KV缓存预填充策略用于表格嵌入，使嵌入不仅基于行内信息，还动态感知数据集整体语义和预测任务，从而桥接LLM语义与统计学习。

### 实验或数据
- **训练数据**: 使用T4表格语料库，从真实世界数据集中生成预测任务（每步采样256行，随机选一列为目标）。
- **模型规模**: 训练了270M至12B参数的多个TLM版本，训练步数8500，批量128，输入截断至16k tokens。
- **基准测试**: 在CARTE、TextTab和TabArena三个基准上评估，使用准确率（分类）和R²（回归）指标。例如，TabICLv2 w/ CASE在所有任务上平均排名2.7，准确率86.5%，R² 76.1%。
- **低数据场景**: 特别强调在低数据场景下的性能提升。

### 值得关注点
- **上下文感知嵌入**: 与现有孤立行嵌入方法不同，CASE通过KV缓存预填充实现全局上下文感知，能解决语义歧义并锚定领域特定语境。
- **兼容性**: 嵌入可即插即用，与任何表格学习器（如XGBoost、TabPFN等）结合，提供“两全其美”的方案。
- **低数据优势**: 在稀疏信号场景下，语义先验能弥补统计不足，效果显著。

### 局限性
根据摘要及方法，CASE主要在语义丰富的数据集上表现优异，对于数值密集型或语义稀疏的数据集可能提升有限。此外，依赖LLM的预填充和嵌入提取可能带来额外计算开销，尤其在大规模数据集上。论文未明确讨论其他局限性，如对超参数敏感度或泛化性边界。

## 7. Beyond the Hivemind: Escaping LLM Homogeneity via Meta-Persona Anchoring and Sequential Temperature Scaling

- Source: arxiv
- arXiv ID: 2608.02618
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.02618v1
- PDF: https://arxiv.org/pdf/2608.02618v1
- DOI: https://doi.org/10.48550/arXiv.2608.02618

### Authors

Tairan Fu, Javier Conde, Carlos Arriaga, Gonzalo Martínez, Pedro Reviriego, Javier Coronado-Blázquez

### Abstract

Recent studies have identified an ``Artificial Hivemind'' effect in Large Language Models (LLMs) causing models to converge on a narrow, homogenized consensus even for open questions. This semantic collapse limits the diversity of AI, resulting in high inter-response similarity ($\approx 0.80-0.90$) even under high-temperature sampling. In this paper, we propose a novel mitigation framework to increase diversity: Meta-Persona Anchoring combined with Filtered Temperature Scaling (FTS). Our approach utilizes a two-stage generation process: first, the model is prompted to self-select a unique, idiosyncratic persona to anchor its starting point; second, we apply a dual-stage sampling sieve, utilizing Top-$p$ filtering to preserve grammatical validity followed by extreme temperature scaling ($T \ge 4.0$) on the surviving candidates to explore the broadened probability distribution. We evaluate our method using the INFINITY-CHAT dataset on state-of-the-art open weight models under $\sim$20B parameters. Our results demonstrate a significant reduction in semantic convergence, with average pairwise cosine similarity dropping from ($\approx 0.85$) to ($\approx 0.65$). Our scheme achieves a majority of questions below the 0.7 threshold, effectively reducing the gap between artificial mode collapse and human-level typological diversity. We provide our implementation as an open-source framework to enable more diverse and creative AI deployments.

### 中文一句话结论
本文提出通过“元角色锚定”与“过滤温度缩放”两阶段方法，有效降低大语言模型生成内容的语义同质化，将平均余弦相似度从约0.85降至约0.65。

### English TL;DR
This paper introduces Meta-Persona Anchoring and Filtered Temperature Scaling to combat the "Artificial Hivemind" effect in LLMs, achieving a reduction in average pairwise cosine similarity from ~0.85 to ~0.65 and thereby significantly increasing response diversity.

### 中文详细总结
近期研究发现，大语言模型（LLM）存在“人工智能蜂群思维”效应，即不同模型针对同一开放性问题会输出高度相似的回答（余弦相似度约0.80-0.90），限制了AI的创造力。本文提出了一种结合“元角色锚定”与“过滤温度缩放（FTS）”的框架来缓解该问题。该框架包含两个阶段：首先，在生成过程中让模型自主选择一个独特的角色（即“元角色”），以此作为语义锚点；其次，应用两阶段采样筛选：先用Top-p过滤保留语法合理的候选词，再对这些候选词施加极高温度缩放（T≥4.0），以扩展探索概率分布范围。实验使用INFINITY-CHAT数据集，在约20B参数的开源模型上进行评估。结果显示，平均成对余弦相似度从约0.85降至约0.65，多数问题的相似度低于0.7阈值，显著缩小了人工模式崩塌与人类层面多样性之间的差距，同时保持了输出的语法合理性。

### 方法 / 贡献
- **方法**：提出“过滤温度缩放”与“元角色锚定”相结合的两阶段生成流程。
- **贡献**：
  1. 首次将Token筛选与熵缩放解耦，在高熵探索中保持语法有效性。
  2. 引入模型自主生成的随机角色作为语义先验，避免人工预设偏见。
  3. 提供开源实现，使结果可复现。
- **关键机制**：
  - Token阶段：基线温度T=1.0下Top-p过滤 → 仅对候选集进行T≥4.0缩放。
  - 角色阶段：模型自选并描述角色后回答问题，作为语义对齐起点。

### 实验或数据
- **数据集**：INFINITY-CHAT（开放性问题集）。
- **模型**：Llama-3.1-8B-Instruct、Mistral-7B-Instruct-v0.3、Qwen2.5-14B-Instruct、Gemma-4-E4B-it、DeepSeek-R1-Distill-Qwen-14B（均<20B参数）。
- **指标**：成对余弦相似度（平均50次独立生成的响应）。
- **硬件**：NVIDIA A100 GPU集群，HuggingFace Transformers实现。
- **结果**：相似度从~0.85降至~0.65，多数问题低于0.7阈值。

### 值得关注点
- 提出“过滤+高温缩放”顺序操作的新思路，区别于传统同时应用T和p的方法。
- 角色由模型自主生成而非预设，避免外部偏见，同时实现不同模型的语义分散。
- 用“蜜蜂与蜂巢”电影隐喻生动解释算法逻辑，便于直观理解。
- 实验聚焦中等规模开源模型（<20B），强调社区可复现性。

### 局限性
- 仅测试了约20B参数以下的开源模型，未验证更大参数或闭源模型（如GPT、Claude）。
- 未测量生成时间或计算开销与基线方法的定量对比。
- 角色生成仍依赖模型自身能力，可能引入不可控的随机偏差。
- 未评估对下游任务（如事实性、逻辑推理）的潜在影响。

## 8. Reversing Arrows in Large Language Models

- Source: arxiv
- arXiv ID: 2608.03512
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.03512v1
- PDF: https://arxiv.org/pdf/2608.03512v1
- DOI: https://doi.org/10.48550/arXiv.2608.03512

### Authors

Sefika Efeoglu, Adrian Paschke

### Abstract

Large language models (LLMs) have achieved strong performance on text-to-knowledge graph generation and related tasks. Nevertheless, it is still unclear whether they accurately model the direction-dependent semantics of inverse relations, in which reversing the order of the arguments alters the meaning of a relation (e.g., \textit{mother} versus \textit{child}). To the best of our knowledge, this work presents the first systematic study of inverse relation directionality in LLMs, using a benchmark consisting of 5,457 instances spanning 27 distinct inverse relation labels. We evaluate five open-source LLMs under a multiple-choice prompting framework and further examine the influence of relation descriptions and entity representations by substituting the original entities with synthetic and masked entities. Our findings reveal systematic asymmetries in inverse relation classification across LLMs, indicate that relation descriptions do not consistently improve performance, and show that model performance can be sensitive to variations in entity representations.

### 中文一句话结论
本文首次系统验证了大语言模型在逆关系方向性判断上存在系统性不对称，且关系描述无法稳定提升性能，模型对实体表示敏感。

### English TL;DR
This paper presents the first systematic study of inverse relation directionality in large language models, revealing systematic asymmetries in classification, inconsistent benefits from relation descriptions, and sensitivity to entity representations.

### 中文详细总结
论文使用包含5,457个实例、27个逆关系标签的基准（来自FewRel和TekGen），在零样本多选提示框架下评估了五个开源LLM（Flan-T5 XL、Qwen2.5-7B、Qwen3-4B、Llama-3.1-8B、Mistral-7B）。实验发现：①模型在“头到尾”和“尾到头”方向上的逆关系分类表现存在系统性不对称，且在FewRel上统计显著；②加入关系描述并未持续提升性能，仅在掩码实体场景下对FewRel有微弱改善；③替换原始实体为合成实体或完全掩码后，模型性能发生变化，表明其对实体熟悉度敏感。统计检验（配对Wilcoxon符号秩检验、Bootstrap置信区间）支持上述结论。论文指出，基于Web资源的基准（如FewRel）可能高估模型泛化能力。

### 方法 / 贡献
- **首次系统分析**：在句子级关系分类任务中，系统评估LLM对逆关系方向性的理解。
- **基准构建**：从FewRel和TekGen抽取方向验证的逆关系对（27个标签），含头到尾和尾到头两个方向的标注。
- **对比实验**：设计零样本多选提示，比较有无关系描述、以及使用原始/合成/掩码实体三种情况，以分离实体熟悉度的影响。
- **统计检验**：使用配对Wilcoxon符号秩检验和Bootstrap置信区间量化方向性、关系描述和实体表示的影响。

### 实验或数据
- **数据**：5,457个句子级实例，覆盖27个逆关系标签（7对来自FewRel，16对来自TekGen，其中12对有实际句子）。
- **模型**：5个指令微调模型（Flan-T5 XL、Qwen2.5-7B、Qwen3-4B、Llama-3.1-8B、Mistral-7B），贪心解码。
- **设置**：零样本多选问答，提供三个选项（目标关系、逆关系、无关关系）。随机化选项顺序。
- **结果示例**（原文仅给出macro-F1示例）：在FewRel上，无关系描述时Qwen3-4B在头到尾方向达最高（37.66%）；Llama-3.1-8B在尾到头方向最佳。有关系描述后，Llama-3.1-8B在FewRel头到尾方向达47.30%。合成和掩码实体下类似趋势。
- **硬件**：A100 GPU（Google Colab Pro）。

### 值得关注点
- **方向性不对称**：模型对“头到尾”和“尾到头”方向表现不一致，且FewRel上差异显著，而TekGen仅在掩码实体时显著——提示数据集本身影响方向敏感性。
- **关系描述作用有限**：添加描述仅在少数场景（掩码实体、FewRel）有边际改善，不足以保证通用收益。
- **实体熟悉度偏差**：替换实体后性能波动，说明模型可能依赖训练时见过的实体模式，而非纯粹的逆关系推理。这对基于Web数据的基准设计提出警示。

### 局限性
- 实验仅使用五个开源LLM，未涵盖更大型或闭源模型（如GPT-4）。
- 未直接评估模型是否因记忆训练数据而获益（数据集来自Web，LLM可能已见过相关实体或关系）。
- 合成实体替换可能改变句子语义或自然度，但未做人工验证。
- 基准仅源于FewRel和TekGen，领域覆盖有限（以Wikidata关系为主）。
- 结果仅报告宏F1，未分析错误类型（如混淆逆关系 vs. 无关关系）。

## 9. TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring

- Source: arxiv
- arXiv ID: 2608.03952
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.03952v1
- PDF: https://arxiv.org/pdf/2608.03952v1
- DOI: https://doi.org/10.48550/arXiv.2608.03952

### Authors

Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, Zixin Chen

### Abstract

Large language models (LLMs) are increasingly used to provide conversational practice for English-as-a-second-language (ESL) learners. Effective ESL tutoring, however, requires more than fluent response generation: a tutor must select an appropriate pedagogical action based on learner behavior and dialogue context. Human-tutoring research offers principles for adaptive support, but they are often task-specific and remain insufficiently integrated into LLM-based ESL tutor training and evaluation. We present TACT (Taxonomy-Aligned Conversational Tutor), a human-grounded framework for post-training and evaluating pedagogically adaptive ESL tutors. Drawing on established literature, we develop two complementary taxonomies: the Tutor-Strategy Taxonomy with 13 tutor response strategies and the Student-Move Taxonomy characterizing learner behavior by move type and status. Using these taxonomies, we construct TACTCorpus, which enriches 260 authentic teacher-student conversations with 32,379 annotations and quality-controlled augmented training data. We then post-train Qwen3.5-4B through supervised fine-tuning followed by taxonomy-aligned Group Relative Policy Optimization, producing TACTutor and optimizing it for scaffolding quality rather than reference imitation alone. On TACTBench, a strategy-balanced diagnostic benchmark comprising 78 authentic tutoring contexts, TACTutor improves over its backbone by 20.30% and outperforms all evaluated proprietary baselines under the same protocol, while maintaining backbone performance on established external educational benchmarks; in a blinded study with 50 learners, it also receives the highest overall mean rating among the evaluated tutors. We release the data, benchmark, and model weights, providing an open foundation for developing pedagogically adaptive ESL tutors.

### 中文一句话结论
TACT提出了一套基于教学策略分类法的后训练框架，通过构造标注语料库和诊断基准，使4B参数的开源模型TACTutor在ESL辅导适应性上超越所有评估的闭源基线。

### English TL;DR
TACT is a taxonomy-aligned post-training framework for pedagogically adaptive ESL tutoring. It constructs an annotated corpus (TACTCorpus) with 32,379 labels, a diagnostic benchmark (TACTBench), and uses SFT + GRPO to train TACTutor (a 4B model). TACTutor outperforms its backbone by 20.30% on TACTBench and all proprietary baselines, and receives the highest human rating in a blinded study.

### 中文详细总结
大型语言模型被用于ESL学习者的对话练习，但有效的辅导需要根据学习者行为选择合适的教学策略，而现有方法缺乏系统的分类框架。TACT基于人类辅导研究，构建了包含13种教师策略和2维学生行为的分类型，并利用260节真实辅导对话构建了TACTCorpus（32,379条标注）。通过监督微调和基于分类的GRPO优化Qwen3.5-4B，得到TACTutor。在78个真实辅导场景的TACTBench上，TACTutor比其基座模型提升20.30%，并优于所有评估的闭源模型。在50名学习者的盲测中，TACTutor在整体评分上最高，且在所有教学行为维度上优于基座模型。

### 方法 / 贡献
- 提出两个互补分类型：教师策略分类型（13种策略）和学生行为分类型（移动类型和状态）。
- 构建TACTCorpus：基于260节真实ESL辅导对话，包含32,379条标注和质量控制的增强训练数据。
- 提出TACTutor：通过监督微调 + 分类对齐的组相对策略优化（GRPO）后训练，优化支架质量而非仅参考模仿。
- 构建TACTBench：78个策略平衡的诊断基准，用于评估辅导适应性。
- 发布数据、基准和模型权重，作为开放基础。

### 实验或数据
- 数据来源：TSCC v2，包含260节一对一的ESL文本聊天辅导课（CEFR B1-C2），2名教师，13名学习者。
- 训练集：2,702个实例；TACTBench：78个真实辅导上下文。
- 评估：TACTBench（策略平衡诊断基准）、外部教育基准、50名学习者盲测。
- 结果：TACTutor在TACTBench上比基座模型提升20.30%，并且在所有教学行为维度（如提示、纠错、反馈、情感支持）上均优于基座和闭源模型。

### 值得关注点
- 将教学策略分类型与模型训练和评估对齐，使模型内化决策能力而非仅依赖推理时提示。
- 开源：提供数据、基准和4B模型权重，便于复现和进一步研究。
- 在盲测中用户评分最高，且优于GPT-4等闭源模型，表明在真实教学场景中的有效性。

### 局限性
论文未明确讨论局限性，但可推断：框架聚焦于ESL文本聊天辅导，对口语或其他语言可能不直接适用；分类型基于特定语料库（TSCC v2），可能无法覆盖所有教学场景；模型规模（4B）在复杂推理能力上可能受限；依赖人工标注质量，尽管有质量控制。

## 10. Predicting Multilingual Classification and Translation Performance of LLMs with Cross-Lingual Alignment $\unicode{x2013}$ Is English Enough?

- Source: arxiv
- arXiv ID: 2608.03446
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.03446v1
- PDF: https://arxiv.org/pdf/2608.03446v1
- DOI: https://doi.org/10.48550/arXiv.2608.03446

### Authors

Adnan Al Ali, Kathy Hämmerl, Jindřich Libovický, Alexander Fraser

### Abstract

Multilingual large language models (LLMs) have been shown to perform better on non-English classification tasks when the representations of the given language are more aligned to English within the model. Several cross-lingual alignment (CLA) scores have been proposed for use with LLMs, along with multiple approaches for extracting embeddings from the models. We provide a comparative analysis of 27 CLA score variants, examining how they differ and how well each predicts downstream performance across three tasks. Crucially, while LLMs are widely used for generative tasks such as machine translation, prior work has focused almost exclusively on classification. We therefore investigate whether CLA scores are similarly predictive of translation performance. To enable computing correlations across target languages, we propose a PMI-based translation metric, which is less dependent on the target language and correlates strongly with chrF. We find that CLA with English predicts translation quality comparably to or better than source-target CLA, providing new evidence that LLMs use English as an internal pivot language.

### 中文一句话结论
本文发现，跨语言对齐分数（尤其是与英语的对齐）能有效预测多语言大语言模型在分类和翻译任务上的表现，支持英语作为内部枢纽语言的假设。

### English TL;DR
This paper explores whether cross-lingual alignment (CLA) scores between non-English languages and English can effectively predict both classification and translation performance in multilingual LLMs, finding that English alignment predicts translation quality as well as or better than source-target alignment, supporting the notion that LLMs use English as an internal pivot language.

### 中文详细总结
论文系统比较了27种跨语言对齐分数变体，涵盖多种嵌入提取方法和对齐度量方式。研究将CLA的应用从分类任务（SIB-200文本分类、Belebele阅读理解）扩展到机器翻译（Flores-200和BOUQuET数据集）。为减少翻译评估指标对目标语言的依赖，作者提出基于PMI的翻译质量度量，与chrF高度相关。实验表明，英语与源语言或目标语言的对齐分数在预测翻译质量上与源-目标对齐效果相当甚至更好，为LLM内部使用英语作为枢纽语言提供了新证据。

### 方法 / 贡献
- 全面回顾了27种基于句子嵌入的跨语言对齐分数变体。
- 提出一种新的少样本（few-shot）方法，从LLM中提取句子嵌入。
- 首次将CLA研究扩展到机器翻译任务。
- 提出基于PMI的翻译评估指标，降低对目标语言的依赖。
- 为LLM使用英语作为内部枢纽语言提供新证据。

### 实验或数据
- 分类任务：SIB-200（文本分类）和Belebele（阅读理解）。
- 翻译任务：Flores-200和BOUQuET数据集。
- 测试了27种CLA分数变体，分析不同嵌入提取方法和对齐度量方式（如余弦相似度、xSIM、Dali、ANC等）的预测能力。
- 提出基于PMI的翻译度量，并验证其与chrF的相关性。

### 值得关注点
- 英语对齐分数在预测翻译质量上表现优异，甚至优于源-目标语言直接对齐。
- PMI度量减少了对目标语言的依赖，便于跨语言相关性比较。
- 论文综合比较了多种CLA方法，提供了系统性的基准。

### 局限性
- 原文未明确列出局限性，但研究主要基于特定LLM和任务，结论的泛化性需进一步验证。
- 提出的PMI度量虽与chrF相关，但尚未在更多场景下测试。
- 分析仅聚焦于英语作为枢纽语言，其他高资源语言的作用未探讨。

## Processing Notes

- Duplicate papers skipped: 0