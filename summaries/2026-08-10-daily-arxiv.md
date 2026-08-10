# Daily arXiv - 2026-08-10

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-10T23:04:01
- Paper count: 10

## 1. Beyond "AI Language": The case for the idiolectal nature of LLM output

- Source: arxiv
- arXiv ID: 2608.06589
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2608.06589v1
- PDF: https://arxiv.org/pdf/2608.06589v1
- DOI: https://doi.org/10.48550/arXiv.2608.06589

### Authors

Karolina Rudnicka, Thomas Stephan Juzek

### Abstract

While large language model outputs are frequently analysed as a collective super variety termed "AI language," this chapter argues that this perspective coexists with distinct, model-specific linguistic signatures akin to human idiolects. We analyse two datasets of LLM-generated texts on societal topics: a 2024 corpus of six models (Improta et al. 2024) and a newly generated 2026 corpus using the same prompts featuring six contemporary models. Our findings, utilising computational descriptors and stylometric principal component analysis reveal a generational shift between the style of the 2024 and 2026 cohorts, while demonstrating that each individual model maintains a unique linguistic profile. This multi-layered interplay is illustrated by contraction frequencies, which vary from over 1,200 to over 30,000 per million words within the same cohort of models (2026). Ultimately, we conclude that treating LLM output as idiolectal in nature provides a valuable framework with potential implications for research on variation and change, LLM-generated text detection, forensic linguistics and usage-based approaches to language.

### 中文一句话结论
本文论证了不同LLM的输出各自具有类似人类个人方言（idiolect）的独特语言特征，而非统一的“AI语言”，并通过2024年和2026年两代模型的语料分析证实了模型间存在稳定差异且代际间存在风格变迁。

### English TL;DR
This paper argues that LLMs should be viewed as having unique, idiolect-like linguistic profiles rather than producing a single "AI language," showing through stylometric analysis of 2024 and 2026 model cohorts that each model maintains a distinct style while generational shifts also occur.

### 中文详细总结
本文挑战了将LLM输出视为单一“AI语言”的普遍观点，提出每个模型应被视为具有独特“个人方言”（idiolect）的个体。研究分析了两个语料库：一个为2024年生成的包含GPT-3.5、GPT-4o等六个模型的语料（来自Improta et al. 2024），另一个为2026年使用相同提示词生成的包含GPT-5.4 Mini、Gemini-3 Flash等六个新模型的语料。通过计算描述符和主成分分析（PCA），研究发现2026年模型群组在整体风格上相较于2024年群组发生了代际变迁，但与此同时，每个独立模型都维持着自身稳定的语言特征。例如，在2026年同代模型中，缩写（contractions）的使用频率显示出巨大差异（从每百万词超过1,200次到超过30,000次）。作者认为，将LLM输出视为个人方言的分析视角，对于语言变异与变化、AI生成文本检测、司法语言学以及基于用法的语言学方法研究都具有重要意义。

### 方法 / 贡献
- 方法论：对比分析了两个时间点（2024年与2026年）的LLM生成文本，采用了计算描述符、文体计量学主成分分析（PCA）及语料库语言学方法（如缩写频率分析）。
- 核心贡献：首次引入明确的历时视角比较不同代际的模型语言；系统论证了将LLM输出视为独立“个人方言”而非统一“AI语言”的理论框架和实证依据；揭示了模型间稳定的个体差异与代际间的群体变迁并存的多层结构。

### 实验或数据
- 实验/数据来源：使用两个语料库。第一个是2024年语料（TextualLLMap），包含GPT-3.5、GPT-4o、Claude-3.5-Haiku、Llama-3-8B、Llama-3.1-70B、Mistral-7B共六个模型生成的28,000篇关于社会议题的文本。第二个是2026年新生成语料，使用完全相同提示和主题，包含Mistral-Nemo 12B、OLMo-3 7B、Qwen-3 14B（开源模型）以及Haiku-4.5、Gemini-3 Flash、GPT-5.4 Mini（闭源API模型）。
- 分析内容：输出长度、句子长度、免责声明频率、主成分分析以及缩写频率等。

### 值得关注点
- 证实了每个LLM模型具有稳定、可区分的语言特征（即“个人方言”），而非仅反映训练数据的平均。
- 发现了模型代际（2024到2026）之间的整体风格变迁。
- 同一代模型内，语言特征（如缩写频率）差异巨大，凸显了单独分析每个模型的必要性。
- 为AI文本检测、司法语言学和语言变异研究提供了新的理论框架。

### 局限性
文中未明确讨论其局限性，但基于内容可推断：1) 仅分析了英语语料；2) 仅关注社会议题文本；3) 无法完全排除不同模型生成参数设置（如温度）的细微差异对结果的影响。

## 2. TA-RAG: Tone Awareness as a Design Imperative for Retrieval-Augmented Generation

- Source: arxiv
- arXiv ID: 2608.06672
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.06672v1
- PDF: https://arxiv.org/pdf/2608.06672v1
- DOI: https://doi.org/10.48550/arXiv.2608.06672

### Authors

Yong-Bin Kang, Anthony McCosker

### Abstract

Retrieval-Augmented Generation (RAG) has become a robust architecture for grounding large language models (LLMs) in trusted knowledge. However, standard RAG systems exhibit a structural limitation: retrieved documents carry their own communication styles-professional jargon, formal tone, or academic writings-that shape the behavior of a RAG system before any tone instructions are processed, often causing the system to ignore user requests for a specific tone. We term this phenomenon contextual decoupling, in which a system optimises for factual accuracy while remaining decoupled from the social or operational context of the recipient. Building on prior research in public health peer-support communities, we identify three communicative misalignment-linguistic, cognitive, and relational-that can persist even when retrieval is relevant and the generated response is factually accurate. We conceptualise these as failures of communicative transformation, which remain largely invisible to accuracy-centred RAG evaluation metrics. To address this gap, we propose Tone-Aware RAG (TA-RAG), a conceptual architectural framework that positions communicative alignment alongside factual accuracy as a core design objective. TA-RAG operationalises four constraints-stigma-free language, readability alignment, recipient-sensitive adaptation, and empathetic framing-across the retrieval, context construction, generation, and constraint validation phases in the proposed RAG pipeline. We further highlight an evaluation agenda for jointly assessing factual fidelity and communicative alignment, and identify open challenges. We argue that tone awareness should be treated not as an optional refinement, but as a present design imperative for RAG systems operating in socially sensitive and high-stakes contexts.

### 中文一句话结论
本文提出Tone-Aware RAG（TA-RAG）框架，将语气感知与事实准确性并立为检索增强生成系统的核心设计目标，以解决检索文档固有风格覆盖用户语气指令导致的“上下文解耦”问题。

### English TL;DR
TA-RAG proposes tone-awareness as a core design imperative for RAG, enforcing four communicative constraints (stigma-free language, readability alignment, recipient-sensitive adaptation, empathetic framing) alongside factual accuracy to overcome contextual decoupling where retrieved document styles override user tone instructions.

### 中文详细总结
标准RAG系统存在结构缺陷：检索到的文档带有自身沟通风格（专业术语、正式语气、学术写作），这些风格在生成阶段处理任何语气指令之前就已影响系统行为，导致系统忽略用户对特定语气的请求，该现象称为“上下文解耦”。基于公共健康同伴支持社区的研究，本文识别出三种沟通失调类型：语言失调（如使用过时污名化术语）、认知失调（可读性不匹配）、关系失调（缺乏情感共情）。这些失调即使检索相关且回答事实准确时仍可能发生，且被以准确性为中心的评估指标（如RAGAS）所忽视。为此，作者提出Tone-Aware RAG（TA-RAG）概念框架，将沟通对齐提升为与事实准确性并列的设计目标。TA-RAG通过四条约束（无污名语言、可读性对齐、接收者感知适应、共情框架）在检索、上下文构建、生成和约束验证四个阶段进行干预，并提出了联合评估事实保真度与沟通对齐的评估议程。

### 方法 / 贡献
- 首次将语气感知定义为RAG系统的设计要素而非可选优化项。
- 提出TA-RAG架构：在标准RAG管线中增加约束层，在检索-生成接口（上下文构建阶段）强制实施沟通对齐，而非在生成后调整语气。
- 定义四条可操作约束：无污名语言（遵循领域术语标准）、可读性对齐（根据接收者调整复杂性）、接收者感知适应（建模角色、专业知识等）、共情框架（识别情感线索并调整沟通姿态）。
- 揭示标准评估指标在沟通失调上的盲点，提出联合评估事实准确性与沟通对齐的议程。

### 实验或数据
该论文为概念性框架论文，未报告具体实验或使用数据集。作者提出评估议程但未给出实证结果。

### 值得关注点
- 提出“上下文解耦”概念：检索文档的沟通风格在生成前锁定上下文，使软性语气提示失效。
- 指出三种失调类型（语言、认知、关系）在事实准确下仍可能造成伤害（如污名化语言影响信任）。
- 强调语气感知在社会敏感场景（如心理健康、HIV同伴支持）中的必要性。
- TA-RAG将沟通对齐作为与事实准确性同等重要的架构约束，而非后处理调整。

### 局限性
- 本文为概念框架，缺乏实证验证和实际系统部署结果。
- 四条约束的具体实现机制（如可读性测量、共情评估）尚未标准化。
- 评估议程中沟通对齐的度量方法未具体设计，仍需进一步研究。
- 未讨论多语言或跨文化语境下的语气感知挑战。
- 约束验证阶段可能增加计算开销和延迟，实际可行性待评估。

## 3. An Exploratory Evaluation of LLM-Assisted Rewriting of Moderate-Complexity Financial Sentences for DisCoCat-Based Sentiment Analysis

- Source: arxiv
- arXiv ID: 2608.07439
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.07439v1
- PDF: https://arxiv.org/pdf/2608.07439v1
- DOI: https://doi.org/10.48550/arXiv.2608.07439

### Authors

Brian Llinas, Nikos Chrisochoides

### Abstract

Quantum natural language processing (QNLP) provides a grammar-aware framework for text modeling, and Distributional Compositional Categorical (DisCoCat) is one of its theoretically grounded formulations. Prior work on financial sentiment analysis has identified practical limitations of DisCoCat, including parser sensitivity, high simulation cost, and difficulty handling longer sentences. We study an LLM-assisted preprocessing workflow that uses controlled rewriting to compress, simplify, or decompose moderate-complexity financial sentiment sentences into parser-compatible, circuit-efficient variants while preserving sentiment-bearing meaning. We compare prompting strategies, language models, and filtering configurations with the low-complexity-only DisCoCat baseline of Stein et al. At the circuit level, the strongest compression variants reduce average qubit and gate counts by more than 70 percent relative to the raw moderate-complexity subset. Across repeated training runs, GPT-4.1-mini with Prompt B achieves the highest observed mean accuracy, $0.550 \pm 0.035$, compared with $0.521 \pm 0.050$ for the baseline. Larger training splits do not necessarily improve downstream performance; across evaluated configurations, training-split size has a moderately negative association with accuracy (Pearson $r=-0.446$). These results provide exploratory evidence that LLM-assisted rewriting can make some moderate-complexity inputs usable within the evaluated DisCoCat configuration, while highlighting prompt design, filtering, and circuit-aware preprocessing as considerations for more scalable QNLP-based financial sentiment analysis.

### 中文一句话结论
本研究表明，LLM辅助重写可将中等复杂度金融句子在DisCoCat量子NLP中的电路复杂度降低70%以上，并在情感分类准确率上超过仅使用低复杂度句子的基线，但重写效果高度依赖提示设计和过滤策略。

### English TL;DR
LLM-assisted rewriting can reduce circuit complexity (qubit/gate counts) by over 70% for moderate-complexity financial sentences in DisCoCat-based quantum NLP, improving sentiment classification accuracy (0.550 ± 0.035 with GPT‑4.1‑mini) compared to a low-complexity-only baseline (0.521 ± 0.050), but performance is sensitive to prompt design and filtering.

### 中文详细总结
该论文针对DisCoCat框架在处理中等复杂度金融句子时存在的解析器敏感、模拟成本高、句子过长等问题，提出LLM辅助的预处理工作流。通过可控重写（压缩、简化、分解）将中等复杂度句子转换为解析器兼容且电路高效的变体，同时保留情感标签。实验对比了多种提示策略、LLM及过滤配置，并以Stein等人的低复杂度句子基线为基准。主要发现包括：最强压缩变体使平均量子比特数和门数降低70%以上；GPT-4.1-mini配合提示B取得最高平均准确率0.550±0.035，高于基线的0.521±0.050；训练集大小与准确率呈中等负相关（Pearson r=-0.446）。结果表明LLM重写可使部分中等复杂度输入适用于DisCoCat，但需注意提示设计、过滤和电路感知预处理。

### 方法 / 贡献
- 提出一个LLM辅助重写框架，专门用于金融情感的DisCoCat预处理：通过提示指令压缩、简化或分解中等复杂度句子，使其更适合Bobcat解析器和lambeq电路构建。
- 量化重写对语料层语言复杂度（词长）和电路复杂度（量子比特数、电路深度、门数）的影响。
- 评估重写句子在下游DisCoCat中的表现，包括语义保持、解析有效性、保留训练样本数、准确率和运行时间。

### 实验或数据
- 使用中等复杂度金融情感句子（平均长度18.4词），来源自Stein等人的研究；低复杂度基线句子平均4.9词。
- 对比多种LLM（包括GPT-4.1-mini）和多种提示策略（如压缩、简化、分解提示），以及不同过滤配置（解析有效性、语义保留阈值）。
- 电路复杂度：压缩变体使量子比特数和门数降低>70%（相对于原始中等复杂度子集）。
- 重复训练运行：GPT-4.1-mini + 提示B 最高平均准确率0.550±0.035；基线0.521±0.050。
- 训练集大小与准确率负相关（Pearson r=-0.446）。

### 值得关注点
- 首次系统探索LLM重写作为DisCoCat预处理的可行性，特别聚焦金融情感分析。
- 重写大幅降低了电路复杂度，使原本难以处理的句子变得可行，为QNLP拓宽适用句子范围提供了实践路径。
- 提示设计、LLM选择、过滤策略均显著影响最终效果，表明预处理工作流需要精细调校。

### 局限性
- 实验为探索性研究，结果仅在评估的特定DisCoCat配置（Bobcat解析器、lambeq库）下有效，未必推广到其他框架或量子硬件。
- 使用的句子为合成的中等复杂度金融句子，并非真实的自然金融语言，实际应用中的泛化性有待验证。
- 重写过程中的语义保持依赖LLM能力，可能改变细微情感信号；情感保留仅通过标签一致性检查，未独立评估语义保真度。
- 未与更强大的经典基线（如Transformer情感分类器）对比；仅与低复杂度DisCoCat基线比较。
- 训练集大小与准确率负相关表明重写后的数据分布可能存在混淆因素（如筛选后样本偏差），需要更严格的控制实验。

## 4. Geo-Spatial Concept Probing of Large Language Models: Abstraction, Compositionality, and Grounding

- Source: arxiv
- arXiv ID: 2608.07353
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.07353v1
- PDF: https://arxiv.org/pdf/2608.07353v1
- DOI: https://doi.org/10.48550/arXiv.2608.07353

### Authors

Karim Radouane, Jose G Moreno, Lynda Tamine

### Abstract

Understanding concepts is fundamental to generalization. Despite their impressive performance on a wide range of tasks, Large Language Models (LLMs) still struggle with genuine concept understanding. Prior work has evaluated conceptual understanding in LLMs using natural-language benchmarks or narrowly scoped synthetic tasks, but these settings often conflate multiple skills or lack precise control over the underlying concepts and their properties. To support controlled probing of concepts in LLMs, we design tests on their core properties: abstraction, compositionality, and groundness. We set up a concept-centric benchmark, targeting spatial concepts such as direction, distance, topology, and their compositions, and use question answering tasks serving as a proxy. We conduct extensive experiments across multiple LLM architectures and training regimes to analyze how model scale and design impact conceptual understanding. The results reveal clear limitations in current LLMs and provide insights into the factors shaping their ability to acquire and compose structured concepts. Our findings shed light on how concept-based LLMs can be redesigned for improved information access and knowledge management. The code will be available at https://github.com/rd20karim/concept-probing.

### 中文一句话结论  
本文通过控制测试空间概念的抽象性、组合性和接地性，揭示了大型语言模型在概念理解上的显著局限，为改进基于概念的模型提供了见解。  

### English TL;DR  
This paper probes large language models' understanding of geo-spatial concepts through controlled tests of abstraction, compositionality, and grounding, revealing significant limitations and providing insights for improving concept-based LLMs.  

### 中文详细总结  
大型语言模型（LLMs）在广泛任务上表现优异，但在概念理解上仍存在不足。现有评估常混淆多种能力或缺乏对概念属性的精确控制。本文针对空间概念（方向、距离、拓扑及其组合）设计探测测试，涵盖核心属性：抽象性（实例统一为类型）、组合性（概念合成）、接地性（关联现实世界）。通过在不同架构和规模（Llama-8B, Mistral-7B/8B, Qwen系列等）的LLMs上进行问答任务实验，发现：  
1. 模型在选择题中中等准确率，但二进制问答中一致性低，表明概念理解不稳定。  
2. 大部分模型能较好编码抽象概念，但Mistral系列在泛化上表现不佳。  
3. 多数模型在一定程度上表现出组合结构（余弦相似性），Mistral系列则缺乏；组合性与理解能力相关。  
4. 加入真实世界事实（如几何测量）未提升问答性能，显示概念表示与数值表示脱节。  

### 方法 / 贡献  
- 设计概念导向的探测基准，系统测试LLMs对空间概念的三个核心属性（抽象、组合、接地）。  
- 利用特定领域（地理空间）概念，通过二进制和多项选择问答任务进行探测，分析不同层级的内部表示。  
- 提出量化方法：用一致性衡量抽象，用组合差距、潜在表示加性等测组合性，用事实注入测接地性。  
- 实验覆盖多个模型架构和规模（0.6B至8B参数），提供跨模型比较。  

### 实验或数据  
- 实验对象：Llama-8B, Mistral-7B/8B, Qwen-0.6B/1.7B/4B/8B等文本LLMs。  
- 任务：针对方向、距离、拓扑概念设计的二进制QA和多项选择QA。  
- 数据集：基于空间概念构建的概念中心基准（具体规模未详述）。  
- 实验分析：跨层内部表示探测，测试抽象泛化、组合结构及相关性、接地效果。  
- 结果：Mistral系列在多数测试中表现较差，其他模型有一定能力但有明显局限。  

### 值得关注点  
- 发现概念理解与任务性能不完全对应：中等QA准确率下概念理解可能不稳定。  
- 组合性角度：多数模型在余弦相似性上表现出组合结构，但Mistral系列欠缺。  
- 接地失败：即使注入真实世界数值信息也未改善性能，揭示语言表示与数值表示的脱节。  
- 为改进LLMs概念学习提供方向，如增强接地和组合推理。  

### 局限性  
- 仅针对地理空间概念，泛化性至其他概念域需验证。  
- 探测方法依赖文本模态，未涉及多模态可能限制接地评估。  
- 未进行模型微调或干预实验，仅分析现有表示。  
- 实验规模（最大8B参数）可能无法代表更大模型（如70B+）的表现。

## 5. Debias in Text, Believe Your Eyes: Text-Anchored Cross-Modal Transfer for Visual Counter-Commonsense Reasoning

- Source: arxiv
- arXiv ID: 2608.06938
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.06938v1
- PDF: https://arxiv.org/pdf/2608.06938v1
- DOI: https://doi.org/10.48550/arXiv.2608.06938

### Authors

Chen Ling, Hanqian Li, Dongnan Liu, Keyu Qian, Jungang Li, Xinglong liu, Shiyi Wang, Xin Dong, Pengcheng Zhu, Wei Zhou, Linjian Mo, Nai Ding

### Abstract

The visual reasoning ability of multimodal large language models (MLLMs) is crucial for downstream applications, particularly counter-commonsense reasoning, which requires models to reason beyond common assumptions. Recent studies mainly improve visual counter-commonsense reasoning by enhancing visual inputs, following the assumption that failures originate from insufficient visual grounding. However, our empirical analysis reveals that the bottleneck is not visual perception. MLLMs already capture the relevant visual evidence, and the correct answer exists in their decoding space. Instead, the shared language decoder resolves prior--evidence conflicts by favoring dominant language priors, especially for low-frequency factual scenarios. Motivated by this, we first propose a text-anchored data construction pipeline, whose core component, Fact-Frequency Distillation (FFD), estimates the prior strength of commonsense facts and distills verified counter-commonsense scenarios into a high-quality text corpus. Building upon this corpus, we introduce TACT, a text-anchored post-training framework that debiases the shared language decoder without requiring any visual training data. TACT routes evidence-following and prior-driven reasoning trajectories into different optimization stages, enabling the decoder to resolve prior--evidence conflicts. Across counter-commonsense visual benchmarks, TACT substantially improves visual reasoning while preserving general capabilities, demonstrating effective text-to-vision cross-modal transfer.

### 中文一句话结论
本文发现多模态大模型在视觉反常识推理中的瓶颈在于语言解码器偏向语言先验而非视觉感知不足，并提出仅依赖文本数据的TACT框架，通过文本锚定的后训练有效改善视觉推理能力。

### English TL;DR
This paper identifies that the bottleneck in visual counter-commonsense reasoning for multimodal large language models (MLLMs) lies in the language decoder’s bias toward dominant language priors rather than insufficient visual perception, and introduces TACT, a text-anchored post-training framework that debiases the decoder via text-only supervision to improve visual reasoning without requiring visual training data.

### 中文详细总结
该论文挑战了当前多模态大模型（MLLMs）在视觉反常识推理（counter-commonsense reasoning）中失败的原因是视觉感知不足的主流观点。通过实证分析，作者发现MLLMs实际上已经捕捉到了相关的视觉证据，正确的答案也存在于其解码空间中，但共享的语言解码器在解决先验与证据冲突时，倾向于偏好占主导地位的语言先验（language priors），尤其是在低频事实场景下。基于此，论文提出了一个文本锚定的数据构建流程，其核心组件为事实频率蒸馏（Fact-Frequency Distillation, FFD），用于估计常识事实的先验强度并提炼出高质量的反常识文本语料库。在此基础上，引入了TACT（Text-Anchored Cross-Modal Transfer）框架，这是一个无需视觉训练数据的文本锚定后训练框架。TACT通过将遵循证据和先验驱动的推理轨迹分配到不同的优化阶段，使解码器能够解决先验与证据的冲突。在多个反常识视觉基准测试中，TACT在保持通用能力的同时显著提升了视觉推理性能，展示了有效的文本到视觉的跨模态迁移能力。

### 方法 / 贡献
1.  **瓶颈定位**：通过多轨迹解码实验（pass@k和prior-lock@k）及失败案例分析，证明MLLMs在反常识推理中的关键瓶颈在于语言解码器的决策层先验偏差，而非视觉感知失败。
2.  **数据构建（FFD）**：提出事实频率蒸馏（FFD）方法，包含先验强度估计、频率路由和反常识验证三个阶段，用于从结构化知识（如Visual Genome、Wikidata）和LLM生成中提炼高质量的反常识文本QA对。
3.  **后训练框架（TACT）**：提出文本锚定跨模态迁移（TACT），这是一个两阶段后训练框架，通过轨迹筛选和难度路由，将先验驱动和证据遵循的推理轨迹分别用于监督微调（SFT）和偏好优化（DPO），有效重塑解码器的决策策略。
4.  **核心贡献**：首次展示仅通过文本监督即可跨模态迁移到视觉反常识推理，无需任何视觉训练数据。

### 实验或数据
论文在多个反常识视觉基准（如CDH-Bench）上进行了实验。实验采用了Qwen3-VL-8B等多个MLLMs。论文通过实验（如图2所示的pass@k与prior-lock@k分析）和失败案例解剖（如使用接地提示减少错误）来支撑其关于瓶颈非视觉感知的论点。TACT框架在实验中被证明能显著改善视觉反常识推理，同时保持模型的通用能力。论文使用来自Visual Genome、Wikidata等来源的知识构建了包含True/False验证、多项选择和二选一问答三种格式的文本语料库。

### 值得关注点
1.  **反直觉发现**：核心发现是MLLMs的视觉感知并非瓶颈，即使模型“看”到了正确证据，也会因为语言先验的压制而给出错误答案，这挑战了现有主流提升视觉输入的改进方向。
2.  **文本跨模态迁移**：TACT框架仅使用文本数据（无需任何图像训练数据）即可改善视觉推理能力，展示了语言先验偏差校准从文本域到视觉域的可迁移性，方法具有高度可扩展性和低成本优势。
3.  **问题定位深入**：通过精细的实验设计（如多轨迹解码分析、决策级先验偏差分析）准确定位了问题源头在共享语言解码器的决策策略，而非编码器或感知阶段。
4.  **方法实用性**：构建的反常识数据语料库和提出的后训练框架可以适配多种下游任务和模型架构，有潜力作为通用的去偏工具。

### 局限性
根据所提供的摘要和初步内容，论文未明确讨论以下潜在局限性：
1.  数据构建的FFD过程依赖于对目标模型先验强度的估计和LLM生成，这可能引入对特定模型或LLM的依赖，且生成的反常识场景的多样性和自然性可能有限。
2.  TACT仅通过文本监督进行优化，虽然展示了跨模态迁移，但可能无法完全覆盖所有类型的视觉-语言冲突或复杂多变的反常识场景。
3.  论文实验主要基于CDH-Bench等特定基准，对于更广泛、更多样化的视觉反常识推理任务或真实世界应用的泛化能力尚需进一步验证。
4.  论文未说明是否进行了消融实验来量化FFD中每个组件（如先验强度估计、频率路由、验证步骤）的独立贡献及数据量对性能的影响。
5.  论文未提及TACT框架在不同模型规模（如更大或更小的MLLMs）上的表现稳定性或计算开销。

## 6. NTDH: Complex Reasoning for Comprehensive Affective Analysis

- Source: arxiv
- arXiv ID: 2608.06425
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.06425v1
- PDF: https://arxiv.org/pdf/2608.06425v1
- DOI: https://doi.org/10.48550/arXiv.2608.06425

### Authors

Tianlei Zhu, Zhiwei Liu, Yuyan Wang, Xiao-Yang Liu, Sophia Ananiadou

### Abstract

Comprehensive affective analysis is challenging for two reasons: it spans heterogeneous prediction tasks with continuous, ordinal, and multi-label outputs, and affective meaning is context-dependent, requiring conflicting cues to be reconciled rather than mapped directly to labels. Existing methods learn this mapping directly and do not model the reconciliation explicitly. We recast the task as a complex-reasoning problem, which yields one output interface across heterogeneous label spaces and a trajectory over which a verifiable reward can be optimised; to our knowledge, this is the first such treatment covering both sentiment and emotion. The obstacle is on the data side: affective reasoning traces must be synthesised, and generic synthesis is misaligned with the targets, tolerances, and phenomena of affect, and discards or leaks its failure cases. We propose NTDH, which addresses these four failures. Naturalisation sets the training answer to the gold label, so it is correct by construction. A Tolerance-aware gate checks each answer against the task's own scoring margin. Domain-aware strategies refine the reasoning using ideas from affective science. Directional Hints report only the type and direction of an error, without exposing the target. We train Qwen3-8B with SFT and then GRPO under the same tolerance used for verification (up to a more permissive construction gate on the multi-label subtask), and a component ablation quantifies the data-quality effect of each part. Using 16,302 training records, about 14x fewer than comparable instruction-tuned systems, the final policy improves over its SFT checkpoint on five of six official-test metrics and achieves the strongest EI-reg result among the compared systems, at a Pearson correlation of 0.862.

### 中文一句话结论
NTDH通过将综合情感分析重新定义为复杂推理问题，并结合质量感知的数据合成与强化学习，仅用16,302条训练记录就在SemEval-2018四个异构子任务上取得了竞争性结果，其中情感强度回归的皮尔逊相关系数达到0.862。

### English TL;DR
NTDH recasts comprehensive affective analysis as a complex-reasoning problem, using a quality-aware data-synthesis pipeline with SFT and GRPO to achieve strong cross-task sentiment and emotion prediction results on SemEval-2018 subtasks, with the best EI-reg Pearson correlation of 0.862.

### 中文详细总结
综合情感分析面临两个核心挑战：一是涉及连续值、序数类别和多标签情感分类等异构预测任务；二是情感意义依赖上下文，需要整合冲突线索而非直接映射为标签。现有方法直接学习输入到标签的映射，未显式建模推理过程。

NTDH的创新在于将任务重新定义为复杂推理问题，统一不同标签空间的输出接口，并生成可验证的推理轨迹供奖励优化。由于情感推理轨迹必须人工合成，而通用合成方法存在与实际目标、容差范围和情感现象不一致的问题，NTDH提出了四部分解决方案：
- **自然化(N)**：将原始标签转换为尺度感知的自然语言答案，确保训练目标正确性
- **容差感知验证(T)**：根据任务自身评分标准检查每个答案
- **领域感知改进(D)**：利用情感科学知识改进推理
- **方向提示(H)**：仅报告错误类型和方向，不泄露目标

使用Qwen3-8B进行SFT初始化和GRPO强化学习，最终策略在六个官方测试指标中的五个上优于SFT检查点，情感强度回归取得最强结果（皮尔逊相关性0.862），且训练数据量仅为可比系统的约1/14。

### 方法 / 贡献
1. **统一推理框架**：将情感分析中的连续回归、序数分类和多标签分类统一为结构化推理生成任务，提供单一输出接口和可验证奖励
2. **NTDH高质量数据处理流程**：自然化确保答案正确性，容差验证使用任务特定评分标准，领域改进融入情感科学知识，方向提示避免目标泄露
3. **仅18.4%的生成结论满足金标准容差**；自然化确保每个保留的SFT轨迹都有gold-consistent答案；8,150条记录中5,388条通过验证进入SFT，剩余2,762条困难样本进入RL阶段，共使用16,302条实例

### 实验或数据
- 在SemEval-2018四个子任务上评估：情感强度回归(El-reg)、多标签情感分类(E-c)、效价回归(V-reg)、序数效价分类(V-oc)
- 官方测试集包含9,201条记录
- 仅使用16,302条训练记录，比EmoLLM的234K指令记录少约14倍
- 使用Qwen3-8B作为基础模型
- 比较对象包括EmoLLM等系统
- 结果：最终策略在六个指标中五个优于SFT初始检查点，El-reg在对比系统中最强（Pearson r=0.862）
- 组件消融研究量化了每个部分对数据质量的影响：N驱动目标正确性，T去除48%-63%的后备泄漏，D帮助细粒度E-c子任务

### 值得关注点
1. 首次将可验证奖励推理方法引入综合情感分析领域
2. 高质量数据处理策略使得仅需少量数据即可达到竞争性结果
3. 自然化和方向提示的设计避免了通用数据合成的常见失败模式
4. 困难样本不被丢弃，而是路由到RL阶段继续优化

### 局限性
- 论文未详细报告稀有情感类别的单独召回率
- 定性错误分析表明稀有情感类别的召回率仍有限
- 数据集规模相对较小，可能限制在更广泛场景下的泛化能力
- 方法依赖于特定的任务评分标准设计，可能不易迁移到其他情感分析任务

## 7. Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes

- Source: arxiv
- arXiv ID: 2608.07208
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.07208v1
- PDF: https://arxiv.org/pdf/2608.07208v1
- DOI: https://doi.org/10.48550/arXiv.2608.07208

### Authors

Luc Hazenoot, Zhaochun Ren, Amirhossein Zohrehvand

### Abstract

Existing measures of how much a text is about a concept read the surface of the text: dictionary word shares, topic proportions, embedding similarities. They score the words a text uses, not the judgment a reader forms about it. Recent work has shown that a gap exists in what Large Language Models (LLMs) know internally versus what they express in their response. This paper asks whether that internal knowledge, read by monitoring the activations of frozen, out-of-the-box LLMs, can stand in for task-specific fine-tuning when measuring concept content, and which extraction method reads it best. We extract such measures via the Recursive Feature Machine (RFM) algorithm and via linear probing, and compare these against an embedding baseline, surface baselines, and the same model's own answer to the question. We demonstrate the approach on financial text, a domain studied extensively and served by established annotated resources, using a human-annotated Environmental, Social and Governance (ESG) dataset. The best linear probe comes within 0.6 percentage points of a fine-tuned domain classifier's accuracy without any task-specific fine-tuning, and outscores the same model's own answer to the question in eleven of twelve comparisons, so the activations carry concept content the response does not report. The simple probe consistently beats the RFM concept vectors, which in turn provide what classification alone does not: a continuous score intended to reflect how strongly a concept is present in a text, whose validation awaits graded labels.

### 中文一句话结论
本研究证明，从冻结大语言模型内部激活中通过线性探针提取的向量，可以在无需任务特定微调的情况下，接近微调分类器在ESG概念测量中的准确率，优于表面基线和RFM概念向量方法。

### English TL;DR
This paper shows that linear probes on frozen LLM activations can measure concept content in text nearly as accurately as fine-tuned classifiers, outperforming surface baselines and RFM concept vectors on ESG classification.

### 中文详细总结
本文提出了一种无需微调、直接从冻结大语言模型内部激活中提取概念内容的方法。传统方法只分析文本表面的词汇，如词典词频、主题比例或嵌入相似度，无法捕捉读者形成的深层判断。研究发现，大语言模型内部激活携带的信息远超其输出表达的内容。作者使用线性探针和RFM（递归特征机）算法两种方法，从冻结LLM的各层激活中提取概念向量，用于测量文本中ESG（环境、社会和治理）概念的含量。在人类标注的ESG数据集上，最佳线性探针的准确率与微调领域分类器仅差0.6个百分点，且在12次比较中11次优于直接询问同一模型得到的答案。RFM概念向量则提供了一个连续分数，但需待分级标签验证。

### 方法 / 贡献
- **方法**：从冻结的LLM（Llama-3.1-8b-it, Qwen-3-8b-it/14b-it, Gemma-4-31b-it）各层获取激活，通过线性探针（逻辑回归）或RFM算法的AGOP矩阵提取概念向量。使用三种池化策略（最后token、均值、最大值）将多token激活聚合成单向量。
- **贡献**：首次在ESG基准上系统比较线性探针与RFM的概念提取能力，证明线性探针无需微调即可接近微调分类器性能，且优于模型自身输出。

### 实验或数据
使用专家标注的ESG数据集（Schimanski等，2024），每支柱（环境、社会、治理）2000句，含二分类标签（是否涉及该支柱）。数据来自年报、可持续发展报告、新闻等，标注一致性高（Fleiss' kappa 0.867-0.926）。实验采用训练集1000句、验证集500句、测试集500句的分割，评估指标包括准确率、F1分数、AUC等。

### 值得关注点
线性探针在未经微调的情况下，在环境支柱上仅比最佳微调模型低0.6个百分点，社会支柱低1.0，治理支柱低2.1。探针在11/12比较中击败同一模型的直接回答，表明内部激活蕴含模型未输出的概念信息。

### 局限性
RFM概念向量生成的连续分数有待分级标签验证，当前ESG数据集仅有二分类标签。实验仅测试ESG领域，通用性尚待验证。最优阈值在报告分片内扫描，实际应用可能需要稳健的固定阈值。

## 8. Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration

- Source: arxiv
- arXiv ID: 2608.07419
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.07419v1
- PDF: https://arxiv.org/pdf/2608.07419v1
- DOI: https://doi.org/10.48550/arXiv.2608.07419

### Authors

Ruochen Jin, Zhanliang Wang, Zongyu Dai, Jiancong Xiao, Bojian Hou

### Abstract

Preference alignment often makes large language models (LLMs) overconfident and poorly calibrated. Traditional post-hoc temperature scaling is inherently domain-dependent: a temperature fitted on one domain does not generalize across domains. This motivates us to modify model parameters during training to improve calibration. We propose maximizing the entropy of predictive distributions as the calibration objective, which directly targets overconfidence by discouraging overly concentrated predictions. Inspired by temperature scaling, we realize this through a bilevel optimization formulation, where the lower level trains the model under a parametric loss and the upper level selects loss hyperparameters to maximize entropy. To make the framework practical at LLM scale, we adopt an efficient first-order approximation that avoids explicit second-order computation. Across both multiple-choice and open-ended generative question answering, experiments demonstrate that our method yields well-calibrated LLMs with particular advantages in out-of-domain generalization.

### 中文一句话结论  
提出一种基于双层优化的方法，在训练阶段最大化预测分布熵来校准 LLM，有效改善跨域泛化，克服了传统事后温度缩放对域依赖的局限。

### English TL;DR  
This paper proposes bilevel optimization that maximizes predictive entropy during LLM training to improve calibration, particularly enhancing out-ofdomain generalization beyond post-hoc temperature scaling.

### 中文详细总结  
大型语言模型经过偏好对齐后往往过度自信，校准不佳。传统的事后温度缩放依赖于特定领域，在一个领域拟合的温度无法泛化到其他领域。为此，本文在训练过程中修改模型参数以改善校准，以最大化预测分布熵作为校准目标，直接抑制过度集中的预测。受温度缩放启发，通过双层优化实现：下层在参数化损失下训练模型，上层选择损失超参数以最大化熵。为使框架在大模型规模可行，采用高效的一阶近似，避免显式二阶计算。在多项选择和开放生成式问答上的实验表明，该方法能获得良好校准的 LLM，尤其在域外泛化方面具有优势。

### 方法 / 贡献  
- 提出将最大化预测分布熵作为校准目标，直接在训练中抑制过度自信。  
- 设计双层优化框架：下层给定超参数训练模型，上层调整损失超参数以最大化熵。  
- 采用一阶近似，使双层优化在 LLM 规模上计算可行，无需昂贵的二阶 Hessian 计算。

### 实验或数据  
在多项选择题（multiple-choice）和开放生成式问答（open-ended generative question answering）两类任务上验证，结果表明所提方法能有效校准 LLM，并在域外泛化上显著优于事后温度缩放等基线。摘要未给出具体数据集名称或规模。

### 值得关注点  
- 从训练阶段而非后处理入手进行校准，更具根本性。  
- 在域外泛化上表现突出，突破了传统温度缩放的领域依赖限制。  
- 一阶近似保证了方法在十亿级以上 LLM 上的实际可行性。

### 局限性  
摘要未讨论方法的局限性。

## 9. CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity

- Source: arxiv
- arXiv ID: 2608.07460
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.07460v1
- PDF: https://arxiv.org/pdf/2608.07460v1
- DOI: https://doi.org/10.48550/arXiv.2608.07460

### Authors

Ananya Sahu, Mohit Bansal, Elias Stengel-Eskin

### Abstract

While post-training improves the capabilities of large language models (LLMs), it generally lowers their output diversity and creativity, negatively impacting tasks that explicitly require creativity (e.g., story generation) as well as those that require it implicitly, e.g., reinforcement learning (RL). We instead propose CreativeInstruct, a scalable instruction-tuning method that teaches LLMs to balance creative, base-model-like generations with the quality of post-trained models, by learning to inject special [StartCreativity] spans that bias generation toward creativity. Furthermore, we introduce a structural diversity metric based on graph edit distance, which captures narrative level variation missed by purely lexical and semantic metrics. On narrative generation, CreativeInstruct matches or exceeds the diversity of both multi-model baselines and distilled variants of their outputs, without sacrificing quality or requiring multiple models at inference time. These results are mirrored in our human evaluation, where we find that annotators rate CreativeInstruct generations as more creative than the post-trained LLMs' generations in 70.3% of cases. We also show the benefits of creative models as a substrate for RL: GRPO applied to a CreativeInstruct checkpoint improves by ~4% on AMC and ~5% points on MATH over the same training applied to the post-trained checkpoint.

### 中文一句话结论
CreativeInstruct 通过让 LLM 学习在生成中注入 [StartCreativity] 标记，在保持后训练模型质量的同时显著提升输出多样性与创造力，并在叙事生成和强化学习（RL）场景中均优于多模型路由方法。

### English TL;DR
CreativeInstruct uses special creativity-triggering tokens to teach LLMs to balance diversity and quality via instruction tuning, surpassing multi-model routing baselines in narrative diversity and boosting RL performance—all with a single model at inference.

### 中文详细总结
本文提出 CreativeInstruct，一种可扩展的指令微调方法，旨在解决后训练（post-training）导致 LLM 输出多样性降低的问题。方法核心是：利用 BACo 等路由框架在训练数据中标记来自基座模型的 token 片段，并用 [StartCreativity]/[EndCreativity] 标记包围；之后微调已对齐模型，使其学会在推理时自主注入这些标记以激发创造性。该方法仅需单个模型，无需推理时加载双模型。此外，作者还引入基于图编辑距离（LLM-GED）的结构多样性指标，捕捉词汇和语义指标遗漏的叙事层面变化。在 5 种模型（7B–32B）上的叙事生成任务中，CreativeInstruct 在多数多样性指标（如余弦多样性、Vendi、LLM-GED）上超越 Instruct、BACo、CrPO、Distill 等基线，且不牺牲质量。人工评估中，70.3% 的生成被标记为比后训练模型更具创造性。在强化学习实验中，基于 CreativeInstruct 检查点的 GRPO 训练在 AMC 和 MATH 上分别提升约 4% 和 5%，表明输出多样性对 RL 探索有积极影响。

### 方法 / 贡献
- **数据构建**：从 Tülu V3 SFT 中筛选英文写作相关 prompt（4000 条），使用 BACo 路由（基于 token 不确定性与标点类型）分别路由至基座模型和对齐模型生成输出，标记来自基座的 token 片段并插入特殊标记。
- **训练**：对已对齐模型进行 LoRA 微调，输入包含 [StartCreativity] 和 [EndCreativity] 标记，输出自然包含来自基座的创造性片段。
- **推理**：模型自主决定何时注入创造性标记，无需双模型路由。
- **贡献**：首次通过指令微调在单模型中实现质量与创造性的灵活平衡；提出基于图编辑距离的 LLM-GED 多样性评估指标；展示创造性提升对 RL 下游任务的正向作用。

### 实验或数据
- **数据集**：Tülu V3 SFT 中的英文写作子集（4000 prompts × 3 输出 = 12000 训练样本）；测试集为 Narrative Discourse 数据集。
- **模型**：LLaMA-3.1 8B、Qwen2.5 7B/32B、Qwen3 8B/32B 等 5 个变体。
- **基线**：Instruct（原始对齐模型）、BACo（双模型路由）、CrPO、Distill（蒸馏）。
- **多样性指标**：Cosine Diversity (M/Q)、Semantic Entropy、Vendi Score、NLI Div、LLM-GED。
- **主要结果**：CreativeInstruct 在多数指标上达到最高多样性（如 Llama-3.1 上 Cos-D M=0.458, Vendi=4.749, LLM-GED=0.545）；70.3% 人工偏好其创造性；GRPO 微调后 AMC 提升 ~4%，MATH 提升 ~5%。

### 值得关注点
- 单模型推理却达到或超越双模型路由的多样性，且性能更快、开销更低。
- 创造性提升不局限于写作任务，在数学 RL 中也带来显著收益，说明多样性是通用 LLM 能力。
- LLM-GED 指标通过叙事图抽象衡量结构多样性，比纯词汇/语义指标更贴近人类判断。

### 局限性
本摘要及提供的论文片段中未明示讨论局限性。潜在方面包括：数据构建仍需基座模型（部分模型未公开发布时可通过跨模型迁移缓解）；方法当前主要针对写作任务，对其他领域（如代码、数学）的泛化性待验证；LLM-GED 依赖 LLM 裁判，可能引入偏好偏差。

## 10. GeoBenchLLM: A Comprehensive Benchmark for Evaluating LLMs on Geo-Related Tasks

- Source: arxiv
- arXiv ID: 2608.07411
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.07411v1
- PDF: https://arxiv.org/pdf/2608.07411v1
- DOI: https://doi.org/10.48550/arXiv.2608.07411

### Authors

Rodrigo Ferreira Rodrigues, Karim Radouane, Jose G Moreno, Lynda Tamine

### Abstract

In the context of geodata, existing Large Language Models have often been studied in a homogeneous setting, which has considerably limited insights into their generalization capabilities. In this paper, we present \benchName, a comprehensive benchmark for probing LLMs on geo-related tasks. We leverage a careful selection of twelve publicly available datasets from diverse geo-related tasks and domains, and evaluate a set of LLMs on geo-spatial and temporal understanding using our benchmark. Our results show that reasoning and size have a strong impact on overall performance. GeoBenchLLM is publicly available at https://github.com/Rfr2003/GeoBenchLLM.

### 中文一句话结论
GeoBenchLLM通过整合12个公开地理数据集构建了全面基准，揭示了推理能力和模型规模对LLM在地理空间与时间理解任务上的表现有显著影响。

### English TL;DR
GeoBenchLLM introduces a comprehensive benchmark of 12 diverse geo-related datasets to evaluate LLMs, revealing that reasoning ability and model size significantly impact performance on geospatial and temporal understanding tasks.

### 中文详细总结
本文提出了GeoBenchLLM，一个用于评估大型语言模型（LLM）在地理相关任务上综合能力的基准测试。该基准由精心挑选的12个公开数据集组成，涵盖8种地理任务，并进一步划分为17个纯文本子数据集。这些任务被归为三个认知层次：知识（Knowledge）、推理（Reasoning）和应用（Application）。研究者评估了不同规模（0.6B至120B参数）的LLM，发现推理能力和模型大小对总体性能有强烈影响，尤其在推理和应用层次的任务中，启用“思考”模式能帮助小模型缩小性能差距。该基准包含421,041个问题，涵盖多种格式（生成型、回归型、是非题、多选题），并提供公开访问。

### 方法 / 贡献
- 提出GeoBenchLLM，一个全面、多任务的地理相关LLM评估基准，整合了12个公开数据集（如GeoQuestions, bAbI, MapQA等），覆盖8种任务和3个认知层次。
- 手动设计了针对不同问题格式（生成型、回归型、是非题、多选题）的评估指标，以确保公平准确的评估。
- 通过实验揭示了模型推理能力（如启用思考模式）和参数量对地理空间与时间理解任务性能的关键影响。

### 实验或数据
- 使用了12个公开地理数据集，总包含421,041个示例，规模覆盖全球范围。
- 评估了Qwen系列（0.6B至8B，部分启用思考模式）以及GPT-OSS（20B和120B）等模型。
- 实验中报告了各子数据集在多个指标（如Accuracy@k, Precision, Recall, BLEU等）上的表现，但具体数值未在摘要或TL;DR中提供。

### 值得关注点
- 基准覆盖了之前工作（如GeoBenchmark, STBench, CityEval）未充分涉及的认知层次（如应用层）和任务（如坐标预测、复杂场景问答）。
- 支持多种问题格式（生成型、回归型、是非题、多选题），更贴近真实应用场景。
- 数据集和代码已公开，便于复现和扩展。

### 局限性
- 论文摘要和TL;DR中未报告具体实验结果或数据集性能数值，需查阅全文获取详细数据。
- 基准主要评估LLM的内在知识，未侧重外部工具（如代码、API）的使用能力（与Xu et al.的工作不同）。
- 模型评估范围有限，未涉及更大参数规模的模型或更多不同架构的LLM（如GPT-4, LLaMA系列等）。

## Processing Notes

- Duplicate papers skipped: 0