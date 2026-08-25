# Daily arXiv - 2026-08-25

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-25T23:32:12
- Paper count: 10

## 1. PUMA: A Polish Benchmark for Culturally Grounded Multimodal Understanding

- Source: arxiv
- arXiv ID: 2608.21853
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.21853v1
- PDF: https://arxiv.org/pdf/2608.21853v1
- DOI: https://doi.org/10.48550/arXiv.2608.21853

### Authors

Sławomir Dadas, Michał Perełkiewicz, Rafał Poświata, Małgorzata Grębowiec, Bartłomiej Jaworski, Izabela Woźniakowska

### Abstract

Large language models are increasingly moving beyond text processing, adding support for other modalities such as images and audio. While text understanding and generation have been extensively studied, multimodal data processing capabilities, particularly in the context of cultures and languages other than English, have not yet been evaluated comprehensively. In this paper, we propose PUMA (Polish Unified Multimodal Assessment), a novel benchmark of 900 hand-crafted tasks designed to probe the limits of multimodal models in the Polish cultural and linguistic context. The dataset evaluates both cultural understanding and practical skill in processing text, images, audio, and visually rich documents. Our extensive evaluation of frontier commercial models, open-weights models, and specialized smaller systems highlights a significant performance gap. While top commercial models achieve high scores in visual question answering, most models struggle with complex audio or document understanding. We open-source our evaluation framework to advance localized multimodal AI research.

### 中文一句话结论
PUMA 是首个同时覆盖图像、音频与文档三类模态的波兰语多模态评测基准，包含 900 个手工构建任务；实验显示前沿商业模型在视觉问答上表现较好，但多数模型在复杂音频与文档理解任务上仍明显不足。

### English TL;DR
PUMA introduces a 900-task Polish multimodal benchmark spanning images, audio, and documents, designed to evaluate culturally grounded understanding and practical skills. Evaluations of commercial, open-weight, and specialized models reveal strong visual question answering performance among top commercial systems, but most models struggle with complex audio and document understanding.

### 中文详细总结
PUMA（Polish Unified Multimodal Assessment）由波兰国家信息处理研究所的研究者提出，是一个面向波兰语言与文化背景的多模态评测基准。基准包含 900 个手工构建任务，覆盖图像、音频和文档三种模态，每个模态下各含三个类别，共九类。其中六类用于评测知识理解与推理，三类用于测试实际技能：自动语音识别（ASR）、光学字符识别（OCR）和文档结构化信息抽取。评测采用确定性规则，无需外部裁判模型，支持 strict score 与 soft score 两种评分方式。作者使用自研工具构建题目，并经过人工审核与修订。实验评估了前沿商业模型、开放权重模型以及小型专用模型，结果显示视觉问答任务上顶尖商业模型得分较高，但多数模型在复杂音频或文档理解任务上表现不佳。评测框架已开源。

### 方法 / 贡献
- 提出 PUMA：900 个手工构建的波兰语多模态评测任务，覆盖图像、音频、文档。
- 评测类别包括：图像（历史与文化、当代生活、地理与环境）、音频（ASR、语音问答、声音与音乐问答）、文档（OCR、文档问答、结构化抽取）。
- 采用确定性自动评分，不依赖外部裁判；支持 include、exclude、regex、order 等问答验证规则，以及针对 ASR、OCR、结构化抽取的专用指标。
- 构建了用于题目管理、模型评测与日志审核的软件工具，并作为开源资源发布。
- 首次在统一框架下联合评测波兰语图像、音频与文档理解，兼顾文化知识与实际多模态处理能力。

### 实验或数据
- 数据集包含 900 个手工构建任务，分属三个模态、九个类别，每类约 100 个任务。
- 评测对象包括前沿商业多模态模型、开放权重模型以及小型专用模型。
- 视觉任务上额外评估了 50 多个视觉语言模型（VLM）。
- 在 ASR 和 OCR 任务上，将通用多模态模型与小型专用模型进行了对比。
- 摘要未给出具体数值结果；主要结论是商业模型在视觉问答上表现较好，但复杂音频和文档理解普遍较弱。

### 值得关注点
- 首个针对波兰语的统一多模态评测基准，同时覆盖图像、音频与文档。
- 题目为人工构建，强调波兰文化、历史、地理、当代生活与流行文化等本土语境。
- 包含实际应用型任务，如波兰语 ASR、OCR 和结构化 JSON 抽取。
- 评测流程完全确定性、可复现，且无需外部模型打分，成本可控。
- 评测框架与生成工具开源，有助于推动本地化多模态 AI 研究。

### 局限性
- 原摘要未明确讨论局限性；PUMA 的评测范围限定于波兰语言与文化语境，因此其结论不能直接推广到其他语言或文化区域。
- 音频任务中的 ASR 样本包含噪声、方言等挑战，但摘要未报告具体错误类型或失败模式。
- 未在摘要中提供任务难度的细粒度分析或与人类表现对比。

## 2. No One Model Catches Every Harm: Benchmarking Content Moderation Across Safety Scenarios

- Source: arxiv
- arXiv ID: 2608.21775
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.21775v1
- PDF: https://arxiv.org/pdf/2608.21775v1
- DOI: https://doi.org/10.48550/arXiv.2608.21775

### Authors

Afshin Orojlooyjadid, Hitesh Patel

### Abstract

Large Language Models (LLMs) are increasingly deployed in real-world applications, yet they remain vulnerable to generating harmful content. From adversarial jailbreaks that bypass safety filters to implicit hate that evades detection, the range of risks these models pose continues to grow. While both specialized content moderators and general-purpose LLMs are being used as safety layers, the question of which model is best suited for which type of harmful content remains unanswered. We present the most comprehensive evaluation of LLM safety capabilities to date, systematically testing \textbf{53} models across \textbf{11} datasets that we organize into four distinct categories. Our evaluation under both prompt-only and prompt-response settings uncovers critical blind spots: large frontier models that lead on one category fall significantly behind smaller, specialized alternatives on others, and real-world conversational safety remains largely unsolved across all model families. These findings challenge the assumption that scale alone ensures safety, and provide the community with a structured framework for informed model selection.

### 中文一句话结论
本基准测试表明，没有单一模型能检测所有危害：前沿通用LLM在对抗性越狱上领先，专用审核模型在响应可见时占优，而对话安全在所有模型家族中仍未解决。

### English TL;DR
This comprehensive benchmark of 53 models across 11 datasets reveals that no single model catches every harm: frontier LLMs lead on adversarial jailbreaks, specialized moderators dominate when responses are available, and conversational safety remains unsolved, challenging the assumption that scale alone ensures safety.

### 中文详细总结
论文针对大型语言模型（LLM）在内容审核中的安全能力进行了迄今为止最全面的基准测试。作者评估了53个模型（包括前沿通用LLM和专用审核模型）在11个数据集上的表现，这些数据集被划分为四个危害类别：对抗性越狱（C1）、标准策略执行（C2）、过度拒绝良性提示（C3）、对话安全（C4）。测试在仅提示（Q）和提示-响应（QA）两种设置下进行。

关键发现包括：在Q设置下，前沿商用模型（如GPT-4系列、Gemini-2.5-pro）在C1上领先；但在QA设置下，专用审核模型（如BingoGuard、WildGuard）全面超越通用模型。C4（对话安全）是所有模型表现最差的类别，平均F1仅约52%。研究还发现模型规模并不直接保障安全性——较小的专用模型在特定任务上可超越大型模型。此外，作者优化了审核提示模板，显著提升了开源模型的性能。

结论是：内容审核的模型选择应基于危害类型、响应可见性和过拒绝成本，而非仅依赖参数规模。研究为实践者提供了结构化的模型选择框架，并指出上下文感知的务实推理是下一代审核模型的核心挑战。

### 方法 / 贡献
- 提出最全面的内容审核基准：覆盖53个模型、11个数据集、4个危害类别，在Q和QA两种设定下评估。
- 优化了用于通用LLM的审核提示模板，在三个小模型上（Gemma-3-4B、Llama-3.2-3B、Phi-4-mini）平均F1提升超过10%。
- 提供了跨模型、跨危害类别的深入分析，揭示不同模型在不同场景下的优劣，为实践者提供模型选择的结构化依据。
- 识别对话安全（C4）为当前所有模型家族仍未解决的挑战。

### 实验或数据
- 模型：53个，包括前沿商用模型（GPT-4o-mini、GPT-4.1、GPT-5、Gemini-2.5-pro、Command-A等）和专用审核模型（LlamaGuard、WildGuard、BingoGuard、PolyGuard），以及多种开源LLM（如Llama-3.2、Gemma、Phi等）。
- 数据集：11个，分为四类：
  - C1（对抗性越狱）：harmaug、harmbench、xrtest
  - C2（标准策略）：aegis、toxicchat、wildguard、oai
  - C3（过度拒绝）：xstest、simplesafety
  - C4（对话安全）：beavertails、bingo
- 设定：Q（仅提示）和QA（提示+响应）两种模式。每个数据集样本上限为1000条。
- 指标：使用二元分类的宏平均F1分数（safe/unsafe），遵循先前内容审核工作惯例。
- 硬件：附录报告了开源模型的硬件细节和推理延迟。

### 值得关注点
- 模型规模与性能没有简单正比关系：在Q设置下，约2B参数的模型即可达到前沿商用模型50-70%的F1性能；但专用审核模型（如BingoGuard-Llama-8B）在QA设置下性能远超大型通用LLM。
- 从Q到QA设定，越狱检测数据集（如harmbench、harmaug）准确率提升10-15%，但对话安全（C4）提升有限，说明上下文理解仍是瓶颈。
- 推理努力（GPT-5.2的不同推理级别）仅带来约1%的边际增益，表示提升推理深度不能显著改善审核。
- 前沿商用模型在C1（越狱）上领先，但专用模型在C2和C4上更强；C3（过拒绝）上模型表现普遍较好（15个模型F1>95%），但仍有区分度。

### 局限性
- 全部评估基于英文内容，未测试多语言或代码混合场景。
- 每个数据集样本上限1000条，可能无法完整反映真实部署中的长尾危害模式。
- 使用二元safe/unsafe标签，丢弃了严重度信息（如Bingo的5级评分）和多标签细粒度（如AEGIS、OAI）——但所有现有专用审核模型均输出此类标签，为保持可比性，沿用此约定。
- QA评估使用原数据集提供的响应，这些响应出自有限来源模型，可能对相关分布训练的审核模型有偏向。
- 评估仅为单轮交互，实际审核常涉及多轮对话。
- 闭源模型通过API访问，可能随时间无声更新，影响复现性。

## 3. Cross-Domain, Multi-Task Data-to-Text Generation without In-Domain Training Data

- Source: arxiv
- arXiv ID: 2608.23391
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.23391v1
- PDF: https://arxiv.org/pdf/2608.23391v1
- DOI: https://doi.org/10.48550/arXiv.2608.23391

### Authors

Yifei Song, Kun Efimov-Zhang, Claire Gardent

### Abstract

Structured data exists in many forms (tables, knowledge graphs, charts, and time series), and converting it into text may involve different generation tasks. However, most prior work on data-to-text (D2T) generation has focused on specific tasks and datasets, relying either on task-specific training data or on the zero-shot capabilities of large language models. We study cross-domain D2T generation in a setting where neither in-domain training text nor test references are available, and where domains, generation goals, and input structures vary substantially. We compare data-driven knowledge distillation (DDKD) against zero-shot inference and fine-tuning on out-of-domain D2T data, and introduce structure-preserving augmentation via structural subsampling and perturbation. Experiments on five benchmarks show that, at constant model size (1.7B parameters), DDKD consistently outperforms both fine-tuning and zero-shot inference. Moreover, the resulting small models outperform a much larger finetuned model on two of the five domains, achieving comparable performance on the remaining three. We further construct QUINTD-5, a fivefold extension of QUINTD-1, and show that simply scaling real target-domain inputs yields only modest gains, whereas our augmentation strategy remains more effective and more cost-efficient for cross-domain distillation.

### 中文一句话结论
在没有目标域训练数据或参考文本的情况下，数据驱动知识蒸馏（DDKD）结合结构保持增强，能使小模型在跨领域、多任务数据到文本生成中稳定超越更大的微调模型。

### English TL;DR
This paper shows that data-driven knowledge distillation (DDKD) with structure-preserving augmentation enables small models (1.7B parameters) to outperform larger finetuned models in cross-domain, multi-task data-to-text generation without any in-domain training data or test references.

### 中文详细总结
该论文研究跨领域、多任务的数据到文本生成问题，设置中既无目标域训练文本，也无测试参考，领域、生成目标和输入结构差异显著。作者比较了数据驱动知识蒸馏（DDKD）与零样本推理和基于WebNLG（40K数据）微调的方法，并引入了结构保持增强（结构子采样和扰动）。在五个基准（QUINTD-1）上，固定模型大小（1.7B参数）下，DDKD一致优于微调和零样本推理。蒸馏出的小模型在两个领域上超越更大微调模型，其余三个领域性能相当。作者还构建了QUINTD-5数据集，发现简单扩展真实目标域输入收益有限，而增强策略在跨领域蒸馏中更有效且成本更低。

### 方法 / 贡献
- **数据驱动知识蒸馏（DDKD）**：使用零样本LLM或WebNLG微调后的大模型生成合成目标域训练数据，蒸馏给小模型（1.7B参数）。
- **结构保持增强**：通过结构子采样和扰动增加训练数据多样性，提高对模式异构性的鲁棒性。
- **构建QUINTD-5数据集**：将QUINTD-1扩展五倍，用于对比不同数据扩展策略效果。
- **无参考评估**：结合基于错误分类法的LLM评判（双独立评判器）、人工验证和内容覆盖度检查。

### 实验或数据
- **基准数据集**：QUINTD-1（5个领域：Wikidata、Ice Hockey、OpenWeather、GSM Arena、OWID），每个领域100个开发输入和100个测试输入，无参考文本。
- **模型比较**：零样本推理、WebNLG微调、DDKD（两种教师模型：零样本和微调），均使用Qwen3-1.7B和Gemma3-1B作为学生。
- **主要结果**：DDKD在所有指标上优于基线，蒸馏后小模型在2/5个领域性能超过更大微调模型。

### 值得关注点
- DDKD结合了WebNLG的通用D2T知识和目标域合成示例，无需目标域真实文本。
- 结构保持增强有效提升跨领域泛化，且比简单扩展输入数据更经济高效。
- 论文构建的QUINTD-5和开源代码为后续研究提供资源。

### 局限性
- 研究仅基于1.7B参数模型，更大或更小模型结果未验证。
- 依赖WebNLG作为唯一源域，其他源域知识蒸馏效果未测试。
- 合成数据可能引入教师模型偏差，评估依赖LLM评判（GPT-5.1和Gemini-2.5-Pro），可能存在评判器偏差。
- 五个领域的多样性有限，更多领域（如法律、医疗）下的泛化能力未知。
- 论文未讨论模型对长输入（如OWID达8K token）的计算效率。

## 4. Who Should Teach? Confidence-Aware Dual-Teacher Learning for Few-Shot Node Classification on Text-Attributed Graphs

- Source: arxiv
- arXiv ID: 2608.22127
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.22127v1
- PDF: https://arxiv.org/pdf/2608.22127v1
- DOI: https://doi.org/10.48550/arXiv.2608.22127

### Authors

Hojin Kim, Sujin Yoon, Sungsu Lim, Dongwon Lee, David Yoon Suk Kang

### Abstract

Text-Attributed Graphs (TAGs) integrate graph structures and node-associated textual attributes, and recent studies have increasingly leveraged Large Language Models (LLMs) to improve TAG learning in few-shot settings. However, existing approaches typically utilize LLM-derived information uniformly across all nodes, despite substantial variations in its reliability, while also incurring considerable monetary costs. We argue that the most appropriate source of supervision may differ across nodes, as Graph Neural Networks (GNNs) and LLMs exhibit complementary strengths in exploiting structural and semantic information, respectively. To this end, we propose CoTeach, a Confidence-aware dual-teacher learning framework that dynamically selects the more reliable teacher for each node. Experimental results demonstrate that CoTeach consistently improves few-shot node classification performance while reducing unnecessary LLM utilization and associated monetary costs.

### 中文一句话结论
CoTeach 提出了一种置信度感知的双教师学习框架，通过为每个节点动态选择更可靠的教师（GNN或LLM），提升少样本节点分类性能并降低不必要的LLM使用成本。

### English TL;DR
CoTeach proposes a confidence-aware dual-teacher learning framework that dynamically selects between GNN and LLM teachers for each node to improve few-shot node classification on text-attributed graphs while reducing unnecessary LLM costs.

### 中文详细总结
文本属性图（TAGs）整合了图结构和节点文本属性，现有方法通常对所有节点统一使用LLM生成的信息，但LLM的可靠性在不同节点间差异很大，且调用LLM成本高昂。GNN和LLM在利用结构信息与语义信息上各有优势，因此不同节点可能需要不同的监督来源。为此，作者提出CoTeach框架，包含两个教师：GNN教师（利用结构信息）和LLM教师（利用语义信息）。对于每个节点，先评估GNN预测的置信度，高置信度节点由GNN教师直接监督，低置信度节点则交由LLM教师处理，并只保留LLM高置信度预测。最后，学生模型在两类教师的伪标签和知识蒸馏下训练。实验表明，CoTeach在多个TAG数据集上一致提升少样本节点分类性能，并降低了LLM调用次数与成本。

### 方法 / 贡献
- **新视角**：提出节点级自适应监督的观点，考虑LLM监督可靠性的节点间差异。
- **新框架**：提出CoTeach，包含GNN教师（基于DGI自监督学习+MLP分类器输出伪标签与置信度）、LLM教师（对GNN低置信度节点基于文本语义生成伪标签与置信度，并通过聚类选取代表性种子节点减少查询）、学生模型（基于两类教师的伪标签和软分布进行知识蒸馏训练）。
- **贡献**：动态选择每个节点最可靠的教师，在提升性能的同时减少不必要的LLM调用。

### 实验或数据
使用四个真实TAG数据集：Cora、Citeseer、Pubmed、WikiCS。与10种方法对比，包括GNN（GCN、GAT、GraphSAGE）、PLM（BERT、BART、SBERT）、GNN+PLM（GLEM）和GNN+LLM（LLMGNN、TAPE、LLM4NG）。实验回答四个问题：各教师贡献、与SOTA比较、成本效率、超参数敏感性。所有超参数通过网格搜索确定。

### 值得关注点
- 强调节点间LLM可靠性差异，提出自适应教师选择，而非一刀切使用LLM。
- 通过置信度阈值和种子节点选择策略，显著减少LLM查询次数，降低货币成本。
- 结合硬伪标签监督和软分布知识蒸馏，充分利用教师的不确定性和类间关系。

### 局限性
- 论文摘要及提供内容中未明确讨论局限性，也未提及实验或数据集的详细结果（如具体性能数字或成本节省比例）。根据要求，此处不臆造信息。

## 5. HelaBERT: Enhancing Sinhala Language Understanding with Dual Pooling Classification Head

- Source: arxiv
- arXiv ID: 2608.22922
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.22922v1
- PDF: https://arxiv.org/pdf/2608.22922v1
- DOI: https://doi.org/10.48550/arXiv.2608.22922

### Authors

Thisen Ekanayake, Nisansa de Silva

### Abstract

We present HelaBERT, a family of two BERT-based masked language models pre-trained from scratch on approximately 1 billion tokens of Sinhala text sourced from MADLAD-400, CulturaX, and a custom corpus comprising news articles, Sinhala Wikipedia, and web crawl data. HelaBERT-Small (~23.3M parameters, 6 layers) and HelaBERT-Large (~110M parameters, 12 layers) both use a SentencePiece Unigram tokenizer (vocabulary size 32,000) tailored to Sinhala's agglutinative morphology and complex script. We evaluate both models on four downstream Sinhala text classification tasks: news category classification, news source classification, sentiment analysis, and writing style classification, using 5 independent seed runs with stratified 80/20 train/test splits. We additionally propose a dual pooling classification head and evaluate it systematically across all four tasks, finding consistent improvements on sentiment analysis and a moderate gain on news category classification for HelaBERT-Small, while the standard [CLS]-linear head remains competitive on news source classification, a headline-level task with short average input length. We release both models to support further research in Sinhala NLP.

### 中文一句话结论
HelaBERT通过从零预训练两个基于BERT的僧伽罗语模型（Small 23.3M参数，Large 110M参数）并设计双池化分类头，在情感分析和新闻分类任务上取得稳定提升，同时释放模型以推动低资源语言NLP研究。

### English TL;DR
HelaBERT presents two BERT-based Sinhala language models pre-trained on ~1 billion tokens and a dual pooling classification head that yields consistent improvements on sentiment analysis and moderate gains on news category classification.

### 中文详细总结
HelaBERT是两种基于BERT的僧伽罗语掩码语言模型（HelaBERT-Small 约23.3M参数/6层，HelaBERT-Large 约110M参数/12层），从零预训练于约10亿token的僧伽罗语文本（源自MADLAD-400、CulturaX及自定义新闻、维基百科和网络爬取语料）。两者均使用针对僧伽罗语粘着形态和复杂文字定制的SentencePiece Unigram分词器（词表大小32,000）。在四项下游任务（新闻分类、新闻来源分类、情感分析、写作风格分类）上，采用5次独立种子运行和分层80/20训练/测试分割进行评估。此外，提出双池化分类头，在情感分析上持续改善（+3.9–5.6 macro-F₁），对HelaBERT-Small的新闻分类有中等提升（+3.1），而标准[CLS]-线性头在短输入的新闻来源任务上仍具竞争力。模型已公开发布。

### 方法 / 贡献
- **模型与预训练**：从零训练两个BERT模型，使用SentencePiece Unigram分词器（词表32,000），预训练于约10亿token僧伽罗语文本。数据预处理包括Unicode NFC归一化、清洗非僧伽罗字符、保留ZWJ/ZWNJ等。
- **分类头设计**：提出双池化分类头，允许[CLS]令牌与全部令牌序列相互交互，增强表示能力，并在四项任务上系统评估。
- **评估协议**：遵循SinBERT工作，采用5独立种子运行和分层分割，确保与基线直接可比。

### 实验或数据
- **预训练数据**：约9亿（Small）和11亿（Large）token，来源包括MADLAD-400、CulturaX及自定义僧伽罗语新闻、维基百科、网络爬取语料。
- **下游任务**：新闻分类（5类，2596训练样本）、新闻来源分类（9类，18280训练样本）、情感分析（3类：正面/负面/中性）、写作风格分类（4类）。其中情感分析使用公开3类数据集，与SinBERT的4类数据集不完全可比。
- **结果亮点**：双池化头在情感分析上提升约4–6 macro-F₁；HelaBERT-Small在新闻分类上提升约3 macro-F₁；短输入任务（新闻来源）上标准头仍具竞争力。

### 值得关注点
- **低资源语言贡献**：专为僧伽罗语设计，填补了该语言深度预训练模型的空白，模型已公开。
- **双池化头有效但任务依赖**：在情感分析等较长输入任务上增益显著，但短输入任务（如新闻来源）上标准头更优，揭示了不同分类头适用场景。
- **环境友好**：Small模型在单GPU（55W）上训练仅16小时，CO₂约0.29kg；Large模型约6.09kg，体现了计算效率。

### 局限性
- **情感分析数据集不可比**：因原SinBERT使用的4类情感数据集已不可获取，本工作使用不同的3类公开数据集，导致该任务结果无法与基线直接对比。
- **写作风格任务已近饱和**：现有模型在此任务上已接近上限，HelaBERT提升空间有限。
- **模型规模有限**：HelaBERT-Large仅110M参数，未探索更大规模或解码器架构（如LLaMA），与SinLlama等生成模型互补但未替代。
- **评估任务范围窄**：仅覆盖文本分类，未在序列标注、问答等任务上验证，通用性待进一步研究。
- **双池化头特定任务收益不均**：仅在情感分析和新闻分类上显著，其他任务无增益，表明其适用性有限。
- **数据来源单一**：预训练语料主要来自新闻和维基百科，可能未涵盖丰富口语或方言变体。

## 6. Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation

- Source: arxiv
- arXiv ID: 2608.22230
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.22230v1
- PDF: https://arxiv.org/pdf/2608.22230v1
- DOI: https://doi.org/10.48550/arXiv.2608.22230

### Authors

Junyu Lu, Kaiyuan Liu, Jingyi Kang, Deyi Ji, Hailong Zhang, Lanyun Zhu, Qi Zhu, Bo Xu, Liang Yang, Hongfei Lin

### Abstract

Large language models (LLMs) are increasingly used for hate speech moderation, often within human--AI workflows in which reviewers provide feedback before a final decision. Such feedback introduces two manipulation directions: whitewashing hateful content as normal and smearing normal content as hateful. This study examines the susceptibility of initially correct model judgments to annotator-style rebuttals and analyzes whether attack effectiveness differs across manipulation directions. We introduce a rejudge protocol that extends direct contradiction with decision-boundary perturbations and adversarial rationales. Experiments with multiple LLMs on two hate speech datasets show that annotator-style rebuttals substantially degrade moderation performance, with stronger effects in multi-turn settings. The results further reveal stable, model-specific asymmetries between whitewashing and smearing across attack configurations, indicating distinct directional vulnerability patterns. Explicit reasoning prompts and defensive instructions reduce these effects but do not eliminate them. These findings highlight the need for direction-aware safeguards and dedicated feedback-robustness evaluation in human--AI moderation workflows.

### 中文一句话结论
本研究揭示了基于LLM的仇恨言论审核系统在面对标注者风格的反驳攻击时存在显著脆弱性——无论是“洗白”仇恨内容还是“污名化”正常内容——且模型对两种攻击方向具有稳定且差异化的敏感性。

### English TL;DR
This paper shows that LLM-based hate speech moderation is vulnerable to annotator-style rebuttal attacks—both whitewashing hateful content as normal and smearing normal content as hateful—with stable, model-specific asymmetries between attack directions, and that existing defenses like explicit reasoning or instructions cannot fully eliminate these effects.

### 中文详细总结
大型语言模型（LLMs）越来越多地被用于仇恨言论审核，通常在人类-AI协作流程中，审核者提供反馈后再做最终决定。这种反馈机制引入两种操纵方向：将仇恨内容“洗白”为正常，将正常内容“污名化”为仇恨。本研究引入了一种“重新判断”协议，该协议在直接反驳的基础上，还包含了决策边界扰动和对抗性理由。实验在多个LLM和两个仇恨言论数据集上进行，结果显示标注者风格的反驳攻击显著降低了审核性能，在多轮对话中影响更强。进一步发现，不同的攻击设置下，模型对洗白和污名化表现出稳定且模型特定的不对称性，表明存在不同的方向性脆弱模式。明确的推理提示和防御性指令可以减轻但无法完全消除这些影响。这些发现强调了在人类-AI审核流程中需要方向感知的防护措施和专门的反馈鲁棒性评估。

### 方法 / 贡献
- 提出了一种**重新判断协议**，模拟人类-AI协作审核中接收审核者反馈后重新评估的过程。
- 设计了四种标注者风格的反驳攻击策略：直接反驳、边界反驳（移动决策边界）、理由反驳（提供误导性解释）以及边界+理由组合攻击。
- 在洗白和污名化两个方向上评估攻击效果，并扩展到多轮交互设置。
- 通过logit级别分析、决策归因分析、多轮分析和防御分析，揭示了置信度侵蚀、持续反驳效应和不同的决策偏移模式。
- 贡献点：揭示了LLM在审核场景下对反馈的脆弱性，识别了方向性不对称模式，并指出了现有防御策略的局限性。

### 实验或数据
- **数据集**：Social Bias Inference Corpus (SBIC) 和 Implicit Hate Corpus (IHC)，均映射为二分类标签（仇恨/正常）。SBIC包含44,671条，IHC包含19,133条。
- **模型**：主要实验使用GPT-5.1、Gemini-2.5、Qwen3-8B、Gemma4-E4B；附录中扩展至Claude-4.5、Llama-3.1-8B-Instruct、Qwen3.5-9B。温度设为0以保持输出一致。
- **评估指标**：准确率（Acc）、宏平均F1、以及按类别（仇恨/正常）的准确率，分别衡量对洗白和污名化的抵抗力。

### 值得关注点
- **方向性不对称**：洗白和污名化对不同模型的影响程度不同，且这种不对称性在不同攻击设置下保持稳定，形成模型特有的行为特征。
- **多轮设置加剧脆弱性**：在多轮交互中，反驳攻击的效果更强，表明模型难以从误导性反馈中恢复。
- **置信度侵蚀**：即使模型预测未翻转，其logit级别的置信度也显著下降，表明攻击影响可能被低估。
- **防御策略局限**：明确的推理提示和防御性指令虽能减轻攻击效果，但无法完全消除，说明现有方法不足以应对方向性操纵。

### 局限性
- **防御不彻底**：当前防御（如推理提示、指令）只能部分缓解攻击，无法完全消除洗白和污名化影响，需要更鲁棒的方向感知防护措施。
- **攻击范围有限**：研究仅针对仇恨言论审核场景下的反驳攻击，未涉及其他类型内容或更复杂的攻击模式（如多轮协同攻击）。
- **数据集和模型代表性**：实验基于两个英文数据集和有限数量的LLM，结论的泛化性需在更多语言、文化和模型上验证。

## 7. Credal Large Language Models for Semantic Commitment under Uncertainty

- Source: arxiv
- arXiv ID: 2608.23244
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.23244v1
- PDF: https://arxiv.org/pdf/2608.23244v1
- DOI: https://doi.org/10.48550/arXiv.2608.23244

### Authors

Shireen Kudukkil Manchingal, Sofiia Nikolenko, Fabio Cuzzolin

### Abstract

Large language models (LLMs) often produce fluent but incorrect answers with unwarranted confidence. A central limitation is that standard LLMs represent uncertainty through a single predictive distribution, conflating epistemic ignorance with genuine ambiguity. We introduce Credal Large Language Models (CLLMs): an ensemble of LoRA adapters induces a credal set whose lower and upper probabilities expose the spread of plausible predictive distributions rather than collapsing to a single softmax output. From this representation we derive two complementary commitment scores. Credal Token Commitment (CTC) is a token-space score that combines lower-bound support, credal width, and intersection entropy, computed without additional generation. Semantic Commitment Consistency (SCC) extends commitment to semantic space using sampled completions, with SCC-Gap measuring the mismatch between token-level and semantic-level support. We evaluate hallucination detection, calibration, selective prediction, and reasoning on Gemma-2-9B, Llama-3.1-8B, and Qwen2.5-7B across OpenBookQA, CoQA, TriviaQA, and ARC-Challenge. CLLM is the best method on QA accuracy at competitive expected calibration error, and CTC tracks the best hallucination AUROC within 1.5 pp on most settings without additional generation. On selective prediction at 80% coverage, CLLM with SCC reaches 99.0% accuracy on OpenBookQA, and on ARC-Challenge CLLM with Csem confidence achieves <= 0.6% ECE across the three backbones.

### 中文一句话结论
本文提出信念大语言模型（CLLMs），通过LoRA适配器集成诱导信念集，并基于此设计令牌级与语义级的承诺得分，在不额外生成文本的条件下提升幻觉检测、校准与选择性预测性能。

### English TL;DR
This paper introduces Credal Large Language Models (CLLMs), which use an ensemble of LoRA adapters to represent uncertainty as a credal set with lower and upper probability bounds. The authors propose Credal Token Commitment (CTC), Semantic Commitment Consistency (SCC), and SCC-Gap scores for improved hallucination detection, calibration, and selective prediction across multiple benchmarks.

### 中文详细总结
标准大语言模型（LLMs）通常以单一的softmax预测分布表示不确定性，导致无法区分认知不确定性与真正歧义。本文提出信念大语言模型（CLLMs），采用冻结骨干网络上的一组LoRA适配器集成，其凸包生成一个信念集，为每个词元给出下界概率（\(\Plow\)）和上界概率（\(\Pup\)），而非单一软输出。基于该表示，作者设计了两类互补的承诺得分：(1) **信念令牌承诺（CTC）**——结合下界支持度、信念宽度和交叉熵的令牌级得分，无需额外生成；(2) **语义承诺一致性（SCC）**——通过采样补全扩展至语义空间，其中SCC-Gap衡量令牌级与语义级支持度之间的不匹配。实验在Gemma-2-9B、Llama-3.1-8B和Qwen2.5-7B模型上，针对OpenBookQA、CoQA、TriviaQA和ARC-Challenge基准，评估了幻觉检测、校准、选择性预测和推理能力。

### 方法 / 贡献
1. **信念大语言模型（CLLMs）**：一个实用的框架，通过LoRA适配器集成将LLM不确定性表示为信念集，暴露上下界概率而非单一下界概率。
2. **信念不确定性度量**：交叉熵和信念宽度，量化认知不确定性的几何结构，直接用于预测和风险感知决策。
3. **信念令牌承诺（CTC）**：仅从信念集计算的令牌级得分，结合下界支持度、信念宽度和交叉熵，无需额外生成，在多数幻觉设置中与最优基线的AUROC差值在1.5个百分点以内。
4. **语义承诺一致性（SCC）与SCC-Gap**：将承诺扩展至语义空间，SCC度量令牌级与语义级支持度的一致性，SCC-Gap量化其差异。完整模型在OpenBookQA上80%覆盖率的选择性预测中达到99.0%准确率。

### 实验或数据
实验在以下设置中进行：
- **模型**：Gemma-2-9B、Llama-3.1-8B、Qwen2.5-7B。
- **基准**：OpenBookQA、CoQA、TriviaQA、ARC-Challenge。
- **评估任务**：幻觉检测（AUROC）、校准（预期校准误差ECE）、选择性预测（80%覆盖率下的准确率）、推理（ARC-Challenge ECE）。
- **主要结果**：CLLM在多数问答准确性上表现最优，ECE具有竞争力；CTC在多数幻觉设置中AUROC与最优基线差值在1.5 pp以内；在ARC-Challenge上，CLLM配合Csem置信度在三个骨干模型上实现≤0.6% ECE。

### 值得关注点
- CLLM首次将信念集表示引入指令微调LLM的下一词元预测，区分了对预测概率本身的认知不确定性。
- CTC可在不额外生成的情况下计算，显著降低计算成本。
- SCC与SCC-Gap弥合了令牌级与语义级不确定性信号间的鸿沟，防止表面流畅度替代真实语义支持度。
- 方法在幻觉检测、校准与选择性预测间取得均衡，尤其在高风险任务中具有实用价值。

### 局限性
摘要未明确提及局限性，但可推断：
- 信念集通过有限数量（具体未知）的LoRA适配器近似，可能无法涵盖所有合理分布。
- CTC依赖令牌级度量，对同义但不同表述的鲁棒性可能有限（SCC部分缓解此问题）。
- 实验限于中等规模模型（7B-9B），方法在更大规模或更新架构上的泛化性尚未验证。
- 未涉及计算成本对比（集成推理的开销）。
- 未讨论在开放域对话或长文本生成任务中的表现。

## 8. Wazobia Eval: A Benchmark for Nigerian Pidgin Emotion Understanding, Sarcasm Detection, and Cultural Reasoning

- Source: arxiv
- arXiv ID: 2608.21369
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.21369v1
- PDF: https://arxiv.org/pdf/2608.21369v1
- DOI: https://doi.org/10.48550/arXiv.2608.21369

### Authors

Stephanie Okoye

### Abstract

Nigerian Pidgin is one of Africa's most widely spoken languages, yet remains severely underrepresented in language model evaluation. Existing benchmarks primarily focus on translation, transcription, or generic sentiment analysis, leaving critical aspects of culturally grounded language understanding unmeasured. We introduce Wazobia Eval, a benchmark for evaluating Nigerian Pidgin emotion understanding, sarcasm detection, and cultural reasoning. The benchmark is built on a manually annotated dataset containing over 550 examples and a 16-category emotion taxonomy designed to capture culturally specific emotional registers that are not represented in conventional sentiment frameworks. Wazobia Eval provides standardized evaluation protocols and benchmark tasks for assessing model performance on nuanced Nigerian language understanding. We present the benchmark design, annotation methodology, taxonomy development process, and preliminary pilot evaluation results. Our goal is to provide foundational evaluation infrastructure for Nigerian language AI and establish a reproducible benchmark for future research. The dataset is publicly available at https://huggingface.co/WAZOBIALABS.

### 中文一句话结论
Wazobia Eval 是一个专为尼日利亚皮钦语设计的情感理解、讽刺检测与文化推理评估基准，基于手动标注的 550+ 示例和 16 类文化情感分类体系，为非洲语言 AI 提供标准化评估基础设施。

### English TL;DR
Wazobia Eval introduces a benchmark for Nigerian Pidgin emotion understanding, sarcasm detection, and cultural reasoning, using a manually annotated dataset of 550+ examples with a 16-category culturally grounded emotion taxonomy.

### 中文详细总结
尼日利亚皮钦语是非洲广泛使用的语言，但在语言模型评估中严重不足。现有基准多聚焦翻译、转录或通用情感分析，忽略了文化相关的语言理解。Wazobia Eval 填补了这一空白，包含三个任务：情感分类（16 类）、讽刺检测（28 对）和文化推理。数据集由 550+ 手工标注示例构成，采用专门为尼日利亚语境设计的 16 类情感分类法（如“hustle fatigue”“market energy”“forming”等）。基准提供了标准化评估协议，并报告了初步试点评估结果（使用 GPT-5.5）。数据集已在 HuggingFace 开源。

### 方法 / 贡献
1. **文化情感分类法**：提出 16 类尼日利亚皮钦语情感分类体系，超越传统正负中性，捕捉“hustle fatigue”“forming”等文化特有情感。
2. **基准数据集与评估框架**：构建含 550+ 示例的人工标注数据集，支持情感分类、讽刺检测和文化推理三大任务。
3. **标准化评估协议**：提供统一的提示模板、评估指标（如 Macro-F1）和可复现的评估流程，便于系统比较和后续扩展。

### 实验或数据
- **数据集规模**：550+ 标注示例，包含 16 个情感类别、28 个讽刺对、253 个基准就绪示例及 16 个试点示例。
- **评估任务**：情感分类（16 选 1）、讽刺检测（二分类）、文化推理（自由文本解释）。
- **评估设置**：试点评估使用 GPT-5.5 在标准化提示下进行，主要指标为 Macro-F1 及准确率、精确率、召回率、F1 等。
- **数据公开**：数据集遵循 CC BY 4.0 许可，托管于 HuggingFace。

### 值得关注点
- **文化情感分类**：提出“hustle fatigue”“market energy”“forming”“prayer gratitude”等类别，反映尼日利亚特有的情感表达，传统情感分析无法捕捉。
- **上下文依赖**：强调同一表达（如“You don try well well”）在不同语境下可表达庆祝、讽刺、轻蔑等不同情感，突出模型需具备上下文理解而非仅关键词匹配。
- **讽刺检测**：通过将讽刺表达与字面相似的非讽刺表达配对，减少对表面词汇模式的依赖，评估模型语用推理能力。
- **标准化评估哲学**：强调“理解”而非“翻译”，优先测量文化能力与情感解读，而非字面翻译正确性。

### 局限性
- 数据集规模较小（550+ 示例），可能不足以支撑大规模模型鲁棒性评估。
- 目前仅进行初步试点评估（使用单一模型 GPT-5.5），缺乏多模型对比和系统性能分析。
- 情感分类法基于有限领域和语境，可能无法覆盖所有尼日利亚皮钦语变体或文化视角。
- 文化推理任务依赖人工评估，尚未实现自动化评分，扩展性受限。
- 基准仅为初始版本，后续需扩充数据、增加任务和模型评测。

## 9. A Reproducible, License-Aware Distillation Recipe for CPUDeployable Safety Classification

- Source: arxiv
- arXiv ID: 2608.21570
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.21570v1
- PDF: https://arxiv.org/pdf/2608.21570v1
- DOI: https://doi.org/10.48550/arXiv.2608.21570

### Authors

Edson Rodrigues da Cruz Filho, Paulo Ricardo Ferreira Neves, Paulo Henrique Eleuterio Falsetti, João Vitor Pavan, Ian Degaspari, Henrique Vieira Laturrague, Patrick Vieira Laturrague, Guilherme Nielsen Dias, Marccello Wilson Perez Berto, Gustavo Voltani Von Atzingen

### Abstract

Deploying a safety layer for large language models on commodity hardware is constrained by the guards available to do it: current open guard models hold between 1 and 9 billion parameters, are oriented toward the graphics processing unit, and answer in seconds per request on a central processing unit. This paper presents a reproducible, license-aware knowledge-distillation recipe addressing that constraint. A strong open guard labels a corpus of roughly 97,000 prompts, drawn from 24 public datasets, into seven safety categories aligned to a public hazard taxonomy, and a fleet of small students spanning lexical, shallow, encoder and generative architectures is trained to reproduce that signal. The corpus is partitioned at the license boundary, so that a deployable and a research model differ only in their training data and the cost of that restriction becomes measurable. Every model is scored against an independent gold benchmark of 6,361 rows over four slices, labeled apart from the teacher and including a slice of harmless prompts that makes over-defense measurable. The distilled students match the teachers on adversarial text within overlapping confidence intervals and reduce false alarms on harmless prompts, the smallest generative student reaching 3.8% against 4.8% for the 8-billion-parameter teacher, while the encoder classifies in roughly 24 ms per request on CPU. Per-class rebalancing is the only decisive ingredient of the recipe. No superiority over the distilled guards is claimed; on the clean reference slice they remain ahead.

### 中文一句话结论
本文提出了一种可复现、许可证感知的知识蒸馏方法，成功将大型安全防护模型（Llama Guard 3 8B）的知识蒸馏至小型CPU可部署的模型，在对抗性文本上保持了相近性能，并降低了无害提示的误报率。

### English TL;DR
This paper presents a reproducible, license-aware knowledge distillation recipe that produces small, CPU-deployable safety classifiers from a large guard model, matching its performance on adversarial text and reducing false alarms on harmless prompts.

### 中文详细总结
当前用于大语言模型的安全防护模型（如Llama Guard 3 8B）参数量大（1-9B）、面向GPU、在CPU上推理耗时数秒，无法在低成本CPU硬件上部署。本文提出一套可复现且考虑许可证限制的知识蒸馏方案，以解决此问题。具体而言：使用Llama Guard 3 8B作为教师模型，对约9.7万条提示（来自24个公开数据集）进行标注，涵盖七个与MLCommons AILuminate v1.0标准对齐的安全类别。随后训练一组小型学生模型（包括词法、浅层、编码器及生成式架构）来模仿教师输出。数据集按照许可证边界进行划分，分别用于可商用模型和研究模型，使许可证限制的成本可被量化。所有学生模型均在独立的金牌基准（6,361行，包含无害提示切片）上评估。结果显示，蒸馏后的学生模型在对抗性文本上性能与教师模型相当（置信区间重叠），且降低了无害提示的误报率（最小的生成式学生模型误报率为3.8%，而教师模型为4.8%）；编码器模型在CPU上每请求推理耗时约24毫秒。类别重平衡是配方中唯一关键的因素。

### 方法 / 贡献
1.  **数据管线**：标准化24个公开数据集，按许可证边界分为商用/非商用两个子集，并设置训练-评估泄漏门。
2.  **蒸馏流程**：通过对比筛选教师模型（Llama Guard 3 8B），生成可审计的标签，并保留独立的金牌评估集。
3.  **学生模型族**：训练了词法、浅层（CNN）、编码器（DistilBERT, MiniLM）和生成式（LoRA微调的小型指令模型）四种架构的学生模型，在统一协议下进行比较。
4.  **消融实验**：通过实验分离出“按类别重平衡”是唯一决定性的训练步骤。
5.  **CPU延迟测量**：在定义的硬件配置上测量了整个学生模型族的CPU推理延迟，建立了质量-延迟权衡曲线。

### 实验或数据
*   **数据集**：教师模型使用约9.7万条提示进行标注，这些提示来自24个公开数据集（如ALERT, AttaQ, SALAD-Bench, SimpleSafetyTests, BeaverTails等）。
*   **评估基准**：使用独立的金牌基准，包含6,361行数据，分为四个切片，其中包含无害提示切片以衡量过度防御。
*   **评估结果**：蒸馏学生模型在对抗性文本上性能与教师模型在重叠置信区间内匹配；在无害提示上误报率更低（最小生成式学生3.8% vs 教师4.8%）；编码器在CPU上每请求推理约24毫秒。
*   **关键发现**：类别重平衡是唯一决定性的成分。

### 值得关注点
*   **许可证感知**：数据集严格按许可证边界分割，使得可商用模型与研究模型的唯一区别是训练数据，许可证限制的成本变得可衡量。
*   **过度防御可测量**：评估基准中包含无害提示切片，使得可以量化模型对正常请求的误拦截情况。
*   **CPU可部署**：蒸馏后的编码器模型可以在CPU上实现毫秒级推理，解决了大模型在CPU上延迟过高的问题。
*   **清晰定位**：作者声明其贡献是资源与基准工作，而非声称达到顶尖性能。

### 局限性
*   教师模型（Llama Guard 3 8B）在干净提示（非对抗性）上的优势仍然存在，蒸馏学生模型未声称在全面超越教师模型。
*   极少数类的训练数据支持有限（如自残类C4），原因是公开数据中此类样本稀疏。
*   提示注入和越狱检测、选举与虚假信息、代码解释器滥用等三类安全问题明确不在本文v0版本的研究范围内。
*   本文使用的七类别安全分类与AILuminate标准对齐，是一个有损映射。
*   与其他采用不同危险分类法（如ShieldGemma, Granite Guardian）的防护模型无法在同一评价标准下直接对比。

## 10. Don't Repeat Yourself: Stopping Verbatim Loops at Sampling Time

- Source: arxiv
- arXiv ID: 2608.22761
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.22761v1
- PDF: https://arxiv.org/pdf/2608.22761v1
- DOI: https://doi.org/10.48550/arXiv.2608.22761

### Authors

Philipp Emanuel Weidmann, Allen Roush, Judah Goldfeder, Sanjay Basu, Ravid Shwartz-Ziv

### Abstract

Large Language Models generate text autoregressively, but open-ended generation is prone to verbatim looping, in which models repeat spans already present in context. Standard defenses such as repetition, presence, and frequency penalties and n-gram blocking act on token recurrence rather than the sequential structure of a loop, and often suppress looping only at strengths that also degrade formatting or fluency. We propose Don't Repeat Yourself (DRY), a sampling-time logit adjustment that penalizes a candidate token only when generating it would extend the current suffix into an exact continuation of a span seen earlier in the context. Sequence breakers protect chat templates and formatting tokens. Across models from 1.5B to 120B parameters, nine prompt families, and a 600-pair human study, DRY reduces suffix-extension rate by 47% while improving lexical diversity. An intervention-matched placebo produces no comparable reduction, identifying suffix matching as the operative mechanism. On AWQ-quantized 70B and 120B models, DRY reduces loop rate by roughly half while preserving MT-Bench, MMLU, and GSM8K performance, whereas standard alternatives lose measurable ground. DRY has been adopted by popular open-source LLM inference frameworks including llama.cpp, ExLlamaV2, and text-generation-webui, highlighting its practical impact on text generation.

### 中文一句话结论
DRY 通过在采样时仅惩罚序列级别上的延续重复（而非简单的词元重现），在几乎不损伤生成质量的前提下，显著降低了大型语言模型中的逐字循环问题（后缀扩展率降低47%）。

### English TL;DR
DRY (Don't Repeat Yourself) is a sampling-time logit adjustment that penalizes a candidate token only when generating it would extend the current suffix into an exact continuation of a span seen earlier in the context, achieving a 47% reduction in suffix-extension rate and halving loop rates on large models without degrading fluency or benchmark performance.

### 中文详细总结
大型语言模型自回归生成文本时，经常会出现逐字循环（verbatim looping）——即重复已出现过的片段。传统的防范方法（如重复惩罚、频率惩罚、n-gram 阻断等）基于词元（token）的简单重现进行惩罚，无法区分“有意的格式复用”与“真正的循环开始”。为了抑制循环，这些方法往往需要很强的惩罚强度，这会导致格式失常或流畅度下降。

本文提出的 DRY 方法是一种采样时的 logit 调整技术。其核心思想是：对于一个候选词元，只有当生成它会将当前的上下文后缀（suffix）延伸成之前出现过的某一序列的精确延续时，才对其进行惩罚。惩罚强度随匹配长度的增加呈指数级增长。此外，DRY 通过**序列中断符**（sequence breakers，如换行符、引号等）保护聊天模板和格式标记，避免对结构性复用的误伤。

DRY 已在 llama.cpp、ExLlamaV2、text-generation-webui 等主流开源推理框架中被采用。

### 方法 / 贡献
1. **方法**：DRY 是一种选择性、序列感知的 logit 调整。它仅在当前后缀与历史匹配且候选词元会延续该匹配时施加指数级惩罚（公式：`penalty = λ * β^(n-L)`）。关键特点是：在大部分解码步骤中，对大部分词元毫无影响。
2. **贡献**：
   - 形式化定义了 DRY，并指出了其“绝大多数步骤不改变分布”的关键属性。
   - 首次进行了严格的控制实验，对比了 DRY 与六种基线方法及安慰剂控制。
   - 展示了 DRY 在与温度采样、核采样等标准控制方法叠加时安全的组合性。
   - DRY 已被主流开源推理框架采用，验证了其实用价值。

### 实验或数据
实验覆盖：
- **模型**：从 1.5B 到 120B 参数，包括 Qwen 2.5 系列和 Llama 3 系列。
- **提示集**：9 个系列（包括循环压力、结构格式、必要重复、边界对抗等）。
- **对比方法**：重复/存在/频率惩罚、n-gram 阻断、对比解码（Contrastive Decoding）、安慰剂控制。
- **人工评估**：600 对盲测（MTurk）。
- **量化测试**：在 AWQ 量化的 70B 和 120B 模型上测试。

**主要结果**：
- SER@4 降低了 47%。
- 在 70B/120B 模型上，循环率降低约一半，同时 MT-Bench、MMLU、GSM8K 性能几乎保持不变。
- 安慰剂控制未产生可比效果，确认后缀匹配是机制核心。
- 延迟开销 < 3%。

### 值得关注点
- **面向机制的精准干预**：DRY 不是“撒胡椒面式”地惩罚所有重复词元，而是仅惩罚序列延续，这是与传统方法最根本的区别。这带来了更好的流畅度/多样性保真度。
- **组合性**：DRY 可以与现有的温度采样、核采样或重复惩罚等配合使用，且总是增效。
- **生态采纳**：已被多个主流开源框架接受，说明它是一种轻量、有效且易于部署的实用方案。
- **指数级惩罚设计**：短匹配温和引导，长匹配（即真正的循环）强力压制，无需硬阻断。

### 局限性
- DRY 是一种采样时的启发式（heuristic）方法，从原理上并非保证彻底消除所有循环；它可能仅减缓而非完全消除长距离的罕见循环。
- 序列中断符的设置依赖于分词器，不同分词器需要手动配置，存在一定跨模型迁移成本。
- 论文重点在对比已有的简单惩罚方法，并未与训练时方案（如 Unlikelihood Training）或更复杂的退火/回溯机制（如 Antislop）进行全面比较。
- 实验主要聚焦于英文文本和特定模型量级，对其他语言、更小或更大的模型族上的泛化性讨论有限。

## Processing Notes

- Duplicate papers skipped: 0