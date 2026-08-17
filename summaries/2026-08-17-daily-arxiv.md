# Daily arXiv - 2026-08-17

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-17T22:47:48
- Paper count: 10

## 1. Geometric Filtering of LLM-Generated Samples for Few-Shot Text Classification

- Source: arxiv
- arXiv ID: 2608.13866
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2608.13866v1
- PDF: https://arxiv.org/pdf/2608.13866v1
- DOI: https://doi.org/10.48550/arXiv.2608.13866

### Authors

Benjamín Schindler, Gonzalo A. Ruz

### Abstract

Large language models (LLMs) can generate synthetic training data for text classification, but the quality of generated samples is heterogeneous: some fall in correct class regions of the embedding space while others land in peripheral or cross-class zones. We propose a geometric filtering framework that evaluates each LLM-generated sample by its Euclidean distance to real class examples in a sentence embedding space, selecting only geometrically consistent candidates. A soft weighting mechanism transforms filter scores into sample weights for classifier training. Evaluated across 13 datasets, 5 classifiers, 10 augmentation methods, and over 6,700 configurations, our method achieves +2.61 percentage points (pp) over SMOTE ($p<0.0001$, Cohen's $d=0.95$, 88.9% win rate). The approach generalizes to named entity recognition (+9.26pp, 100% win rate) without filter modification, and is robust across 5 LLMs from 4 providers. A key finding is that the simplest distance-based filter consistently outperforms complex multi-criteria alternatives.

### 中文一句话结论
本文提出基于欧氏距离的几何过滤框架，通过筛选嵌入空间中与真实样本一致的LLM生成数据，在少样本文本分类中显著提升性能，超越SMOTE达+2.61个百分点。

### English TL;DR
A geometric filtering framework using Euclidean distance to real class examples in embedding space consistently improves LLM-generated synthetic text quality for few-shot classification, achieving +2.61 percentage points over SMOTE across extensive benchmarks.

### 中文详细总结
大语言模型生成的合成训练数据质量参差不齐，部分样本落入正确类区域，部分落入边缘或跨类区域。本文提出后生成几何过滤系统：将LLM生成的每个候选样本与其类别真实示例在句子嵌入空间中的欧氏距离作为评分，仅保留几何一致的样本。进一步采用软权重机制将过滤得分转化为连续样本权重，而非简单的二元取舍。在13个数据集、5个分类器、10种数据增强方法、超过6700种配置下的评估表明，该方法相比SMOTE提升+2.61个百分点（p<0.0001, Cohen's d=0.95, 胜率88.9%）。方法无需修改即可推广至命名实体识别任务（+9.26pp, 100%胜率），并在5种不同LLM上表现稳健。关键发现是：最简单的基于距离的过滤器始终优于复杂的多标准替代方案。

### 方法 / 贡献
- **几何过滤框架**：以LLM生成样本到同类真实样本在嵌入空间中的欧氏距离作为质量指标，保留几何一致的样本。框架与生成模型解耦，已验证5种LLM（来自4个提供商）。
- **软权重机制**：将过滤得分通过温度缩放转化为连续样本权重，超越二元接受/拒绝，使高质量合成样本对训练贡献更大。
- **跨任务泛化**：从文本分类推广到命名实体识别（NER），无需修改过滤器，取得+9.26pp提升。
- **全面验证**：在6700+配置上证明最简单的距离过滤器持续优于复杂多标准过滤器，并提供理论分析解释原因。

### 实验或数据
- **数据集**：13个数据集，涵盖9个文本领域。包括7个文本分类数据集（20newsgroups, sms_spam, hate_speech, ag_news, emotion, dbpedia14, 20newsgroups_20class）、3个可扩展性数据集（trec6, banking77, clinc150）和3个NER语料库（MultiNERD, WikiANN, Few-NERD）。
- **分类器**：逻辑回归、线性SVC、Ridge、随机森林（100棵树）、MLP（100隐藏单元）。
- **数据增强方法**：SMOTE、随机过采样、EDA、回译、无增强、嵌入mixup、T5 paraphrasing、BERT上下文增强，以及本文的二元过滤和软权重变体（共10种）。
- **配置数量**：主比较使用3个线性分类器和3个随机种子（1890次运行）；全协议使用5个分类器和5个种子（3675次运行），总计超过6700个配置。
- **评估指标**：宏F1分数，通过配对t检验（Bonferroni校正）、Cohen's d效应量和胜率（超过SMOTE的配置比例）报告统计显著性。

### 值得关注点
- **简单性超越复杂性**：仅基于欧氏距离的1级级联过滤器持续优于LOF、级联多级、组合过滤等复杂方法。作者解释由于L2归一化下欧氏距离与余弦相似度单调等价，且LOF在小样本（10-shot）下因邻居数不足产生退化密度估计。
- **跨任务泛化**：无需修改过滤器，将“类”定义改为每句主导实体类型即可应用于NER，取得+9.26pp提升且100%胜率。
- **强健性**：在5种LLM（Gemini 3 Flash、GPT-5-mini、Claude 4.5 Haiku、Kimi K2.5、GLM-5）和4种不同嵌入模型上表现稳健。
- **显著的小样本增益**：在10-shot设置下效应量极大（d=1.48），绝对宏F1从67.23%提升至72.12%；随着训练样本增加收益递减（50-shot时d=0.80）。
- **线性分类器受益最大**：线性SVC和Ridge分别获得+2.98pp和+2.74pp，效应量大（d>1.0），而随机森林增益较小（+1.42pp, d=0.35）。

### 局限性
根据提供的资料，本文未明确讨论局限性。可推断的潜在方面包括：方法依赖于嵌入空间的质量（仅测试了4种模型）；生成3倍候选样本可能增加计算成本；仅验证了文本分类和NER任务，在其他任务（如序列生成、回归）上的表现未知；所有实验使用英文数据集，跨语言泛化性有待验证。

## 2. Towards Efficient Multimodal and Multilingual Opinion Extraction for STI: A QLoRA-Based Fine-Tuning Approach

- Source: arxiv
- arXiv ID: 2608.14152
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.14152v1
- PDF: https://arxiv.org/pdf/2608.14152v1
- DOI: https://doi.org/10.48550/arXiv.2608.14152

### Authors

Sheng Hong, Xuanqi Wang, Jiacheng Wang, Yuwei Wang

### Abstract

Recent advances in large language models (LLMs) have reshaped semantic analysis. Opinion Extraction (OE) for Science and Technology Intelligence (STI) requires concise core opinions from large information streams. Off-the-shelf models struggle to filter noise from these streams and show limited structured-output reliability in zero-shot multilingual and multi-modal settings. To address information overload and extraction defocus, this study proposes a multimodal core-opinion extraction framework in which visual evidence serves as a contextual anchor for textual judgment. Using VideoLLaMA2 (VL2) and VideoLLaMA2.1 (VL2.1) as the base models, we apply Quantized Low-Rank Adaptation (QLoRA) fine-tuning on a curated dataset of 2,194 multilingual and multimodal samples. Under the selected Image-Augmented setting, fine-tuned VL2.1 generates structured JSON core-opinion outputs, achieving 64.98% Precision, 42.15% Recall, 51.14% F1-score, and 74.00% sample-level accuracy. Relative to the zero-shot VL2.1 setting, it raises the F1-scores of Spanish and Russian from 4.83% and 0.45% to 46.05% and 51.93%, respectively. The framework further incorporates a Fuzzy Cumulative Prospect Theory-based post-extraction triage module for case-level value assessment, providing a case-level value signal for downstream STI screening.

### 中文一句话结论  
本文提出基于QLoRA微调VideoLLaMA2/2.1的多模态多语言核心观点提取框架，通过视觉信息锚定文本判断，在自建STI数据集上将西班牙语与俄语的F1值从接近零提升至46%与52%，并实现结构化JSON输出及案例级价值评估。

### English TL;DR  
This paper proposes a QLoRA-based fine-tuning approach using VideoLLaMA2/2.1 models to achieve efficient multimodal and multilingual core-opinion extraction for Science and Technology Intelligence, significantly improving structured JSON output reliability and cross-lingual performance compared to zero-shot settings.

### 中文详细总结  
科技情报分析需要从海量、多源信息中提取核心观点，但现有大模型在零样本多语言、多模态场景下存在提取失焦、输出格式不稳定等问题。为此，本文提出一个以视觉证据作为文本判断上下文的框架：选用VideoLLaMA2（VL2）及视频视频LLaMA2.1（VL2.1）作为基座模型，并应用QLoRA参数高效微调。微调数据为自构建的2194条多语言（英、中、西、俄）、多模态（文本、图像、视频）标注集。在“图像增强”设置下，微调后的VL2.1生成结构化JSON核心观点，达到64.98%精确率、42.15%召回率、51.14% F1及74%样本级准确率；与零样本VL2.1相比，西班牙语F1从4.83%升至46.05%，俄语F1从0.45%升至51.93%。此外，框架引入基于模糊累积前景理论（Fuzzy-CPT）的后处理模块，用于案例级价值评估，为下游STI筛选提供信号。

### 方法 / 贡献  
- **方法**：构建多模态STI观点数据流锚定（视觉证据辅助文本判断）；采用QLoRA在4位量化基座（VL2/VL2.1）上仅微调低秩适配器（r≤64），以交叉熵损失训练生成JSON格式核心观点；后处理用Fuzzy-CPT评估案例的可靠性、相关性、热度、一致性和时效性。  
- **贡献**：①提出面向STI的多模态核心观点提取框架，让视觉信息充当语境锚点；②人工构建并标注了2194条四种语言、三种模态的训评数据集；③通过QLoRA高效微调实现结构化输出与跨语言、跨模态泛化；④引入Fuzzy-CPT进行案例级价值评分。

### 实验或数据  
- **数据集**：自建STI观点数据集，共2194个样本（文本1198、图像858、视频138），语言分布：英语608、中文610、俄语482、西班牙语494。由经培训的标注者按统一方案标注核心观点及情感（正/中/负），并通过DeepSeek-V3.2交叉验证情感标签一致性（加权Kappa值0.83–0.92）。  
- **实验设置**：基座VL2（CLIP-ViT-L+ Mistral）与VL2.1（SigLIP-So400m+ Qwen2）；训练在2×A100-40GB上完成；对比零样本设置与微调后性能。  
- **主要结果**：微调后VL2.1在图像增强设置下F1=51.14%，样本级准确率74%；跨语言提升显著（西班牙语F1 +41.22p.p.，俄语F1 +51.48p.p.）。

### 值得关注点  
- 多模态锚定设计：将视觉信息作为文本判断的上下文，有效减少提取失焦。  
- QLoRA使得7B模型在双A100上可微，且显著改善零样本状态下极差的小语种性能。  
- 后处理Fuzzy-CPT模块将提取结果转换为可量化的情报价值信号，打通端到端STI筛选。  
- 数据集构建流程详细（八步骤），且进行了标注质量验证。  

### 局限性  
摘要及正文未明确讨论该工作的局限性。根据内容可推断：数据集规模仅2194条，可能影响模型泛化；视频样本仅138条，长视频时序建模能力未充分验证；Fuzzy-CPT后处理依赖人工定义的模糊规则，未见自动化调优；仅以VL2/VL2.1为基座，未与其他MLLM或更大参数模型比较。

## 3. Scaling Creative Writing Beyond Story-Centric Data with Attribute-Guided Genre Expansion

- Source: arxiv
- arXiv ID: 2608.13947
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.13947v1
- PDF: https://arxiv.org/pdf/2608.13947v1
- DOI: https://doi.org/10.48550/arXiv.2608.13947

### Authors

Hwan Chang, Yongil Kim, Heuiyeen Yeen, Yireun Kim, Jinsik Lee, Hwanhee Lee

### Abstract

High-quality creative writing data for large language models (LLMs) remains dominated by story-centric data, limiting models' ability to follow the structural and functional conventions of diverse creative formats. We propose an attribute-guided genre expansion framework for scaling creative writing data beyond story generation. By separating thematic breadth from genre-form control, our framework leverages human-authored story prompts as diverse creative seeds, while utilizing manually curated genre attributes to enforce distinct structural, stylistic, and formatting conventions. We combine these to prompt strong LLMs for genre-faithful query-response pairs, which are then quality-filtered. Applying this framework, we construct the Multi-Genre Collection, a 50K-example corpus spanning 13 creative genres, including story, rap, lyrics, scripts, game design, character design, and other creative formats. Experiments across out-of-distribution writing benchmarks and held-out genre diagnostics demonstrate that models fine-tuned on our data consistently surpass not only base models and writing-specialized baselines, but also models trained on existing writing corpora. Genre-count ablations further indicate that controlled genre expansion, rather than story-centric scaling alone, is a key driver of robust creative writing capability.

### 中文一句话结论
本论文提出了一种属性引导的体裁扩展框架，通过构建包含13种创意体裁的50K实例数据集，显著提升了大型语言模型在多种创意写作格式上的表现，超越了仅依赖故事中心数据的传统方法。

### English TL;DR
This paper proposes an attribute-guided genre expansion framework to scale creative writing data beyond story-centric sources, constructing a 50K-instance Multi-Genre Collection spanning 13 genres, which significantly improves LLMs' performance across diverse creative writing tasks.

### 中文详细总结
高质量创意写作数据长期被故事中心数据主导，这限制了模型遵循多种创意格式结构与功能惯例的能力。论文通过分离主题广度与体裁形式控制，利用人类撰写的故事提示作为多样化创意种子，并结合人工策划的体裁属性来强制执行结构、风格和格式惯例。该方法用于提示强大LLM生成符合体裁要求的查询-响应对，再经质量过滤。最终构建的“多体裁数据集”（Multi-Genre Collection）涵盖故事、说唱、歌词、剧本、游戏设计、角色设计等13种创意体裁，共50K实例。实验表明，在该数据集上微调的模型在多个基准测试中持续超越基础模型、专业写作基线模型以及现有写作语料库训练的模型。体裁数量消融实验进一步证明，受控的体裁扩展（而非单纯扩大故事中心数据）是提升创意写作鲁棒性的关键驱动因素。

### 方法 / 贡献
- **属性引导的体裁扩展框架**：将主题多样性（从人类故事提示中采样）与体裁形式控制（通过人工策划的属性集实现）分离，系统生成符合体裁惯例的创意写作指令数据。
- **多体裁数据集构建**：通过三步流程（主题种子采样、体裁属性采样、属性引导的配对合成），构建包含13种体裁、50K实例的平衡语料库，并经过严格的自动质量过滤。
- **关键贡献**：证明了受控体裁扩展是提升LLM创意写作能力的关键，而非简单扩大故事中心数据规模。

### 实验或数据
- **实验模型**：在Llama-3.1-8B-Instruct、EXAONE-3.5-7.8B-Instruct和Qwen3-8B三个基础模型上进行监督微调（LoRA适配器，rank 128），并包括LongWriter-glm4-9B作为专业写作基线。
- **评估基准**：Arena Hard（创意写作子集）、WritingBench（广告与文学艺术领域）、以及多体裁数据集自身的留出测试集（13种体裁，每类50实例，共650个），使用GPT-4.1或GPT-5-mini作为裁判。
- **主要结果**：在多体裁数据集上微调的模型在所有基准上持续超越基础模型、专业写作模型和现有写作语料库训练的模型。体裁数量消融实验显示，从仅故事体裁扩展到全部13种体裁时，新颖性指标持续提升。

### 值得关注点
- 论文明确区分了“主题多样性”与“体裁形式控制”，并提出了有效的分离机制，这是领域内的重要创新。
- 构建的13体裁数据集具有清晰的语义区分（通过t-SNE可视化验证），表明合成方法能产生体裁独特的指令分布而非简单改写。
- 通过消融实验直接证明体裁扩展（而非单纯数据规模）驱动了创意写作能力的提升，具有重要指导意义。

### 局限性
论文未明确讨论不同体裁间的数据分布不平衡问题（尽管声称“平衡覆盖”但图5显示各体裁实例数存在差异），也未分析框架对非英语语言创意写作的适用性。此外，依赖专有LLM（GPT-5, Qwen3）进行数据生成和质量过滤可能引入模型特定偏差，且过滤标准（低于均值两个标准差）的合理性未作深入讨论。

## 4. CForce: Boosting Parallel Decoding for dLLMs via Consistency Forcing

- Source: arxiv
- arXiv ID: 2608.13925
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.13925v1
- PDF: https://arxiv.org/pdf/2608.13925v1
- DOI: https://doi.org/10.48550/arXiv.2608.13925

### Authors

Yuji Ren, Chenkai Xu, Zhuocheng Gong, Jianguo Li, Zhijie Deng

### Abstract

Diffusion large language models (dLLMs) accelerate language generation by predicting multiple masks in a single forward pass. However, existing dLLMs can suffer from unreliable predictions in early denoising stages under aggressive parallelism strategies, leading to errors that can propagate to later stages. To tackle this issue, we present Consistency Forcing (CForce) for dLLMs, a distillation method to force the mask predictions of early stages to align with those of later stages. CForce trains the model on pre-collected self-rollout trajectories, thereby improving training-inference alignment. We introduce Confidence Adaptive KL Divergence as a distillation objective to conjoin the merits of forward and reverse KL. We further provide a theoretical analysis for the consistency objective to explain why CForce can approximately minimize the prediction error of early stages. Critically, the same formulation applies to both mask-to-token decoding and edit-capable decoding; in the edit-capable case, later token-to-token refinements provide additional supervision for earlier masked-state predictions. Experiments on non-edit and edit-capable LLaDA models show improved speed-quality trade-offs, especially under high-parallelism decoding budgets. Code is available at: https://github.com/inclusionAI/dFactory.

### 中文一句话结论
CForce 通过蒸馏方法强制扩散大语言模型（dLLM）早期阶段掩码预测与后期阶段对齐，显著提升高并行解码下的速度-质量权衡。

### English TL;DR
CForce is a distillation method that aligns early-stage mask predictions with later-stage predictions in diffusion LLMs using self-rollout trajectories, improving speed-quality trade-offs under aggressive parallel decoding.

### 中文详细总结
CForce 针对扩散大语言模型（dLLMs）在高并行解码中早期去噪阶段预测不可靠的问题，提出一种蒸馏方法。它通过在预收集的自滚动轨迹上训练模型，强制早期阶段掩码预测与后期阶段对齐，从而改善训练-推理一致性。该方法引入置信度自适应KL散度（CAD）作为蒸馏目标，结合前向和反向KL的优点，并提供理论分析证明其能近似最小化早期阶段预测误差。CForce 同时适用于掩码到令牌（M2T）解码和可编辑解码，后者利用后期令牌到令牌（T2T）细化作为额外监督。实验在非编辑和可编辑LLaDA模型上均显示出改进的速度-质量权衡。

### 方法 / 贡献
- 提出CForce蒸馏方法，基于模型自身阈值解码轨迹进行相邻阶段对齐，无需冻结教师模型。
- 引入置信度自适应KL散度（CAD）动态插值前向和反向KL。
- 结合交叉熵锚点稳定令牌承诺，并采用难度课程学习。
- 统一适用于M2T和可编辑解码，利用后期T2T细化监督早期M2T预测。
- 提供理论分析，证明早期预测误差有界于相邻阶段分布漂移和揭示边界令牌误差。

### 实验或数据
实验基于LLaDA2.1-mini（可编辑）和LLaDA2.0-mini（非编辑）模型。可编辑模型上，平均每前向令牌数（TPF）从6.94提升至9.08，平均准确率从85.57提升至86.41；非编辑模型上，平均TPF从3.60提升至6.42，且在固定TPF预算下提升少步准确率。所有四个基准测试均显示一致增益。

### 值得关注点
- 强调早期阶段可靠性而非仅减少采样步骤，提供新视角。
- 在可编辑dLLM中利用T2T细化信号增强早期M2T预测，是独特贡献。
- 方法无需额外教师模型，降低部署复杂度。
- 理论分析与实验验证结合，增强方法可信度。
- 代码已开源：https://github.com/inclusionAI/dFactory

### 局限性
- 主要验证于LLaDA系列模型，泛化性待进一步探索。
- 轨迹收集和阶段划分可能引入计算开销。
- 理论分析提供上界，但实际误差缩减幅度可能受模型容量限制。
- 摘要未提及对其他类型dLLM或其他任务的广泛测试。

## 5. Federated Prompt Learning: A Unified Framework, Empirical Analysis, and Future Directions

- Source: arxiv
- arXiv ID: 2608.13844
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.13844v1
- PDF: https://arxiv.org/pdf/2608.13844v1
- DOI: https://doi.org/10.48550/arXiv.2608.13844

### Authors

Qinglin Yang, Chen Qiu, Hongyuan Zhang, Pengdeng Li, Yuan Liu, Zhihong Tian

### Abstract

Large language models (LLMs) have become core components of cloud-based intelligent services in academia and industry, yet their training and deployment are hindered by high computational costs, data centralization, and privacy concerns. Federated learning (FL) offers a decentralized training paradigm that enables clients to collaboratively train a learning model without sharing raw data, making it a promising solution for privacy-preserving LLM training and reasoning. This paper presents a comprehensive survey of federated prompt learning (FPL) to review recent advances in integrating the federated learning paradigm and large language models, answering the following research questions: RQ1: The fundamental motivations, characteristics, and enabling technologies of FPL, and how it differs from conventional FL and full-model federated fine-tuning; RQ2: The trade-offs FPL approaches exhibit in performance, communication efficiency, computational overhead, scalability, personalization, and heterogeneity handling; RQ3: The remaining security, privacy, robustness, and system challenges, along with key future research directions. To this end, we systematically examine existing FPL methods across the full model lifecycle: pre-training, fine-tuning, and practical applications, while discussing security, privacy, and robustness issues and summarizing existing defense mechanisms. Finally, we highlight open challenges and future directions, aiming to help readers understand how the insights drive research in FPL.

### 中文一句话结论
本综述系统研究了联邦提示学习（FPL）这一将联邦学习与提示/参数高效微调相结合的新范式，阐明了其在隐私保护、通信效率及异构环境下适配大语言模型的核心优势、权衡与未来方向。

### English TL;DR
This survey comprehensively reviews federated prompt learning (FPL), a paradigm that integrates federated learning with prompt-based and parameter-efficient fine-tuning for large language models. It systematically explores motivations, enabling technologies, algorithmic trade-offs (performance, communication, computation, personalization, heterogeneity), security/privacy challenges, and future directions across the full LLM lifecycle, unifying prior work under a lifecycle-oriented framework.

### 中文详细总结
本文针对大语言模型（LLM）训练中面临的高计算成本、数据集中化与隐私问题，系统综述了联邦提示学习（FPL）这一将联邦学习与提示学习/参数高效微调相结合的新范式。通过回答三个研究问题：（1）FPL的基本动机、特性及与常规联邦学习和全模型联邦微调的区别；（2）FPL方法在性能、通信效率、计算开销、可扩展性、个性化与异构处理上的权衡；（3）安全、隐私、鲁棒性及系统挑战与未来方向，本文对52篇高质量研究进行了系统性分类与比较。核心贡献在于：通过代表性FPL模型的实验验证提取实证经验；分析安全、隐私与鲁棒性威胁及防御机制；总结开放挑战与未来研究方向。文章覆盖预训练、微调、实际应用全生命周期，并统一了提示、适配器等轻量级方法在联邦环境下的设计空间。

### 方法 / 贡献
- **方法**：采用系统性文献综述与基于分类法的比较分析。从Web of Science、Google Scholar、dblp等数据库检索，经去重、筛选后保留52篇高质量研究，按技术机制、模型架构、评估指标等进行编码与分类。
- **贡献**：
  - 首次以FPL为中心的统一综述，覆盖LLM全生命周期；
  - 通过代表性模型的实验验证提供实证结果与实践洞察；
  - 系统总结FPL中的安全、隐私、鲁棒性攻击与防御；
  - 明确开放挑战与未来研究方向，形成结构化参考。

### 实验或数据
- 本文包含对代表性FPL模型与框架的实验验证，以推导关键实证发现。
- 具体实验设置、所用数据集及详细结果未在摘要中展开；综述部分提及基于现有研究的结果对比。
- 文献检索共纳入52篇完整评估的研究。

### 值得关注点
- **统一视角**：将提示学习定位为联邦优化的一等接口，而非辅助技术，填补了现有综述的空白。
- **权衡分析**：详细比较了FPL方法在性能、通信/计算开销、个性化与异构处理之间的权衡，揭示了无单一最优方案的事实。
- **安全整合**：专门讨论了联邦LLM中特有的攻击（投毒、后门、推理攻击）及防御机制。
- **全生命周期覆盖**：从预训练到部署和应用，全面分析FPL在不同阶段的作用。

### 局限性
- 作为综述，覆盖范围限于52篇研究，可能遗漏近期或特定领域的方法。
- 实验验证部分主要基于现有文献结果，缺乏统一基准下的横向对比；具体数据集与实验细节未在摘要中详述。
- 对安全与隐私的讨论偏重分类与现有防御，未提出新的解决方案。
- 未来方向的建议基于当前观察，实际可行性需进一步研究验证。

## 6. When Lexical Change Misleads: Rethinking Dynamic Topic Model Evaluation with Traditional and LLM-Based Metrics

- Source: arxiv
- arXiv ID: 2608.13835
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.13835v1
- PDF: https://arxiv.org/pdf/2608.13835v1
- DOI: https://doi.org/10.48550/arXiv.2608.13835

### Authors

Charu Karakkaparambil James

### Abstract

Dynamic topic models capture evolving word distributions, but traditional coherence metrics may fail when vocabulary changes while semantic meaning persists. We evaluate 120 topics from CoNTM and DLDA across NYT, DBLP, and arXiv, using three human annotators and Low, Medium, and High lexical-change categories. Traditional temporal coherence shows highly variable agreement with human judgments ($ρ$=-0.256 to 0.614). In contrast, LLM-based semantic similarity agrees strongly with human semantic judgments for CoNTM on NYT ($ρ$=0.609), DBLP ($ρ$=0.721), and arXiv ($ρ$=0.502), but is less consistent for DLDA. Lexical-change stratification reveals variation hidden by aggregate evaluation. We therefore advocate lexical-change-aware evaluation, jointly reporting traditional coherence and LLM-based semantic measures as complementary rather than interchangeable signals.

### 中文一句话结论
当词汇变化但语义保持不变时，传统的主题连贯性指标会误导动态主题模型的评估，因此需要联合使用传统连贯性和基于大语言模型的语义相似度作为互补信号。

### English TL;DR
This paper demonstrates that traditional coherence metrics for evaluating dynamic topic models can mislead when vocabulary changes but semantic meaning persists, advocating for a lexical-change-aware evaluation framework that jointly uses traditional coherence and LLM-based semantic similarity as complementary signals rather than interchangeable metrics.

### 中文详细总结
动态主题模型捕捉随时间演变的词分布，但传统连贯性指标在词汇变化而语义持续时可能失效。本文从CoNTM和DLDA两个模型中选取120个主题，覆盖NYT、DBLP和arXiv三个数据集，由三名人工标注员评估，并按低、中、高词汇变化分类。传统时间连贯性与人工判断的斯皮尔曼相关系数范围为-0.256到0.614，变异性大。相反，基于大语言模型（LLM）的语义相似度与人工语义判断在CoNTM模型上表现强相关（NYT: ρ=0.609, DBLP: ρ=0.721, arXiv: ρ=0.502），但对DLDA一致性较差。词汇变化分层揭示了聚合评估隐藏的差异。因此本文提倡词汇变化感知的评估框架，将传统连贯性和LLM语义度量作为互补信号而非可互换指标。

### 方法 / 贡献
1. 分析了两种动态主题模型（CoNTM和DLDA）在三个数据集上的传统时间连贯性，展示其与人工判断的变异性。
2. 引入词汇变化感知评估，将主题分为低、中、高词汇变化类别，揭示聚合相关性隐藏的模式。
3. 评估LLM语义相似度与人工判断的一致性，证明其提供互补语义信号但并非普遍可靠。
4. 倡导将传统连贯性、LLM语义相似度和词汇变化结合的多视角评估框架。

### 实验或数据
- 模型：CoNTM和DLDA
- 数据集：纽约时报（NYT）、DBLP、arXiv
- 主题数量：每个模型-数据集组合20个主题，共120个主题轨迹
- 时间点：NYT（1987、1997、2007），DBLP（2010、2015、2020），arXiv（2012、2018、2024）
- 人工评估：三名标注员对每个主题的5个问题（1-5分制），总计1800个判断
- 传统指标：时间主题连贯性
- LLM指标：GPT-5.5生成的语义相似度评分
- 词汇变化：每个组合7个低、7个中、6个高词汇变化主题

### 值得关注点
- 传统连贯性在DLDA-DBLP上表现最好（ρ=0.614），但在CoNTM-NYT上为负相关（ρ=-0.256），表明其可靠性因条件和模型而异
- LLM语义评分对CoNTM表现强相关（ρ=0.502-0.721），但对DLDA不一致（DBLP: ρ=-0.086, arXiv: ρ=-0.190）
- 词汇变化分层显示：低词汇变化下，传统连贯性可能完全误导（CoNTM-NYT: ρ=-0.786），而LLM评分在该条件下表现最佳（ρ=0.801）
- 中词汇变化下，传统连贯性在DLDA上表现最强（NYT: ρ=0.873, DBLP: ρ=0.898）

### 局限性
- 人工评估样本量有限：每个词汇变化类别仅6-7个主题，分层结果需谨慎解释
- DLDA模型上LLM评分表现不一致，原因未深入分析
- 仅使用GPT-5.5一个LLM，未探索其他模型
- 三时间点设计可能无法完全代表连续动态主题演化

## 7. Jais 2: A Family of Arabic-Centric Open Large Language Models

- Source: arxiv
- arXiv ID: 2608.13580
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.13580v1
- PDF: https://arxiv.org/pdf/2608.13580v1
- DOI: https://doi.org/10.48550/arXiv.2608.13580

### Authors

Mohamed Anwar, Abed Alhakim Freihat, George Ibrahim, Mostafa Awad, Abdelrahman Sadallah, Gurpreet Gosal, Gokulakrishnan Ramakrishnan, Sarath Chandran, Biswajit Mishra, Rituraj Joshi, Ahmed Frikha, Etienne Goffinet, Abhishek Maiti, Ali El Filali, Sarah AlBarri, Samujjwal Ghosh, Rahul Pal, Parvez Mullah, Awantika Shukla, Sajid siddiki, Samta Kamboj, Onkar Pandit, Sunil Kumar Sahu, AbdelRahman Elbadawy, Amr Mohamed, Ahmad Chamma, Evan Dufraisse, Abdelaziz Bounhar, Dani Bouch, Hadi Abdine, Guokan Shang, Fajri Koto, Yuxia Wang, Zhuohan Xie, Ali Mekky, Rania Elbadry, Sarfraz Ahmad, Momina Ahsan, Omar El Herraoui, Daniil Orel, Hasan Iqbal, Kareem Elzeky, Mervat Abassy, Kareem Elozeiri, Saadeldine Eletter, Farah Atif, Nurdaulet Mukhituly, Haonan Li, Xudong Han, Aaryamonvikram Singh, Zainul Abedien Ahmed Quraishi, Neha Sengupta, Larry Murray, Avraham Sheinin, Joel Hestness, Natalia Vassilieva, Hector Xuguang Ren, Zhengzhong Liu, Michalis Vazirgiannis, Preslav Nakov

### Abstract

Jais 2 is a family of Arabic-centric large language models developed jointly by MBZUAI, Cerebras, and Inception, designed to advance Arabic-centric language modeling, with strong performance across the Arabic and culturally grounded benchmarks evaluated in this report. The family includes, to our knowledge, the largest open Arabic-centric LLM trained from scratch at 70B parameters, and a competitive 8B-parameter variant among the evaluated open models. A custom Arabic-centric vocabulary enables efficient training and inference. In addition, an optimized architecture and training recipe yield highly compute-efficient training. With a substantially smaller token budget than comparable models, Jais 2 achieves strong Arabic performance on the benchmarks considered in this report and competitive English results. The models obtain leading results among the evaluated open models on OALL2 and AraGen. They also perform strongly on several culturally grounded Arabic benchmarks, including poetry, religion, cuisine, and dream interpretation, as well as in general tasks such as translation and summarization. We release the models in HuggingFace under a commercially permissive license. Jais 2 70B is also released as a chat app on the Web, iOS, and Android; it runs on Cerebras hardware, delivering up to 2,000 tokens per second, and enabling high-throughput Arabic-centric chat serving in our deployment setting. By uniting scale, linguistic diversity, cultural fidelity, openness, and speed, Jais 2 provides an open-weight foundation intended to support further research and development in Arabic-centric LLMs.

### 中文一句话结论
Jais 2 发布了两个开源的阿拉伯语大语言模型（70B 和 8B 参数），通过自定义词表和高效训练在阿拉伯语基准测试中取得领先，同时英语表现也具有竞争力。

### English TL;DR
Jais 2 introduces two open Arabic-centric large language models (70B and 8B parameters) that achieve state-of-the-art Arabic performance through a custom vocabulary and compute-efficient training, along with competitive English results.

### 中文详细总结
Jais 2 是由 MBZUAI、Cerebras 和 Inception 联合开发的阿拉伯语大语言模型家族。该家族包含两个参数规模的模型：70B（据称是最大的从头训练的开放阿拉伯语 LLM）和 8B。模型采用专门为阿拉伯语定制的词表，并结合优化的架构和训练方案，实现了极高的计算效率。相比同类模型，Jais 2 使用更少的 token 即能在阿拉伯语基准（如 OALL2、AraGen）上取得领先结果，并在诗歌、宗教、烹饪、解梦等文化相关任务以及通用任务（翻译、摘要）中表现强劲。模型在 HuggingFace 上以商业友好许可证发布，70B 版本还提供了聊天应用（Web、iOS、Android），在 Cerebras 硬件上可实现每秒高达 2000 token 的推理速度。

### 方法 / 贡献
- 提出并开源了最大规模的阿拉伯语 LLM（70B）及 8B 变体。
- 设计自定义阿拉伯语词表，提升训练和推理效率。
- 采用优化架构和训练策略，实现高计算效率（以远少于同类模型的 token 预算获得强性能）。
- 在阿拉伯语文化相关基准（诗歌、宗教、饮食、解梦等）上建立评估体系，并展示领先结果。

### 实验或数据
摘要未提供详细的实验设置或数据集描述。但提及在 OALL2、AraGen 以及多个文化阿拉伯语基准（包括诗歌、宗教、烹饪、解梦）和通用任务（翻译、摘要）上进行了评估。模型在英语上也取得了有竞争力的表现。

### 值得关注点
- 70B 模型是目前公开可用的最大阿拉伯语 LLM，且从头训练。
- 计算效率突出：用更少的 token 达到 strong performance。
- 同时覆盖阿拉伯语文化领域（如诗歌、解梦）和通用任务。
- 推理速度高达 2000 token/s（Cerebras 硬件），适合高吞吐量聊天应用。
- 以开放权重和商业友好许可证发布，促进阿拉伯语 LLM 的研究与开发。

### 局限性
摘要未明确讨论局限性。可能存在的方向包括：模型在非阿拉伯语（尤其是低资源语言）上的表现未详细评估；文化基准的覆盖范围有限；依赖特定硬件（Cerebras）实现高速推理，通用性待验证。

## 8. Grounding Without Corrective Control: Truth-Tracking Profiles for Large Language Models

- Source: arxiv
- arXiv ID: 2608.14252
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.14252v1
- PDF: https://arxiv.org/pdf/2608.14252v1
- DOI: https://doi.org/10.48550/arXiv.2608.14252

### Authors

Brett Reynolds

### Abstract

Recent work suggests that some large language model representations have content or reference. Grounding can secure either without supplying live routes for correction. This paper asks what follows from that gap. An output is answerable when discrepancies can affect what a target- and task-specific arrangement produces, accepts, or withdraws. The arrangement has corrective control only when live, sufficiently independent routes can detect and repair fresh discrepancies. A route profile records which routes constrain the arrangement and how they are related. Those profiles support analysis of truth-tracking: patterned support for representational success.
  Language models are the pressure case; text-only arrangements provide a task-relative limiting case. Text-trained models inherit patterns of testimony, coherence, and prior correction. Where target-sensitive correction survives training, these can supply derivative answerability (inherited constraint); live answerability is the relation supplied by a current route for fresh discrepancies. Fluent failures should follow when a task requires independently informative access to the facts. Self-consistency, retrieval, tools, code execution, multimodal input, and feedback should help selectively. Route-by-task interactions test the distinctions. The decomposition's empirical burden is to predict held-out route--task combinations or improve intervention choice without conceptual refitting. Surface improvement and truth-tracking improvement can come apart.

### 中文一句话结论
本文提出大型语言模型的内容/指称锚定（grounding）并不自动赋予对新鲜错误的检测与修正能力，需通过“回答性”“修正控制”“路径剖面”等概念刻画其真值追踪架构。

### English TL;DR  
This theoretical work argues that grounding large language model representations in content or reference does not confer the capacity to detect and repair fresh errors. It introduces a framework of answerability, corrective control, and route profiles to analyze truth-tracking in task-specific arrangements, distinguishing inherited constraint from live correction. The decomposition yields predictions for route–task interactions but no empirical validation is reported.

### 中文详细总结
论文从符号锚定问题出发，指出LLM表征虽然可能具有内容或指称，但这一事实本身并不保证系统能发现和修正新的错误。作者区分了**回答性**（输出与目标之间的偏差能否影响系统后续产生、接受或撤回）和**修正控制**（系统是否有活跃且足够独立的路径来检测并修复新的偏差）。**路径剖面**记录哪些路径约束系统及其耦合方式，用于分析**真值追踪**（对表征成功的模式化支持）。  
文本训练的模型继承了人类实践中的证言、一致性和先前修正模式，形成**衍生回答性**（继承的约束）；而**实时回答性**则要求当前存在能处理新鲜偏差的活跃路径。作者认为，若任务需要独立信息获取，仅依赖文本的LLM将会出现“流畅但错误”的输出。通过结合自洽性、检索、工具、代码执行、多模态输入和反馈，可以有针对性地增加实时路径。该方法论框架强调表面提升与真值追踪提升可能分离。

### 方法 / 贡献
- 核心概念：将“锚定”（grounding）与“修正控制”（corrective control）分离，指出前者不蕴含后者。  
- 提出“路径剖面”（route profile）分析系统有哪些活跃路径、路径间耦合关系，从而解释和预测不同任务下的真值追踪表现。  
- 区分衍生回答性（继承的约束）与实时回答性（当前新鲜偏差的修正路径）。  
- 理论贡献在于提供了一个分析LLM部署中知识架构的框架，而非语义理论或标量指标，并可用于指导干预选择。

### 实验或数据
论文未报告具体实验或数据集。它属于理论/哲学论证，提出了可检验的预测（如路径×任务的交互效应、留出组合的转移预测等），但未进行实证验证。文中以纯文本LLM为基线案例进行概念分析。

### 值得关注点
- 明确提出“锚定≠修正能力”，对当前LLM是否“理解”世界的辩论有精确化作用。  
- “路径剖面”概念将不同认知路径（感知、证言、一致性、测量、干预等）系统化，便于比较不同增强手段（检索、工具调用等）的效果。  
- 指出流畅性与真值追踪改善可能分离，对评估LLM可靠性有警示意义。  
- 框架独立于具体真理论（符合论、融贯论等），可兼容不同哲学立场。

### 局限性
- 框架目前纯理论，缺乏实证检验，其预测力尚待验证。  
- 如何准确识别并列举所有相关路径（特别是跨模态或动态耦合路径）未详述。  
- 边界问题：系统“安排”（arrangement）的因果边界如何划定，可能影响实际应用。  
- 对“新鲜偏差”的定义依赖于具体任务和目标，可能导致分类上的模糊性。  
- 未讨论计算资源、训练数据偏差等工程实现层面的实际约束。

## 9. Leading-Silence Augmentation and Multi-Stage Synthetic Supervision for the Second MLC-SLM Challenge

- Source: arxiv
- arXiv ID: 2608.14150
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.14150v1
- PDF: https://arxiv.org/pdf/2608.14150v1
- DOI: https://doi.org/10.48550/arXiv.2608.14150

### Authors

Kexin Shi, Renhe Sun, Yuge Huang, Ximeng Wang, Jiayi Zhou, Jian Liu, Malu Zhang

### Abstract

The second Multilingual Conversational Speech Language Model (MLC-SLM) Challenge evaluates two tasks over complete, unsegmented multilingual conversations: speaker diarization and recognition (Task 1) and conversational speech understanding (Task 2). Neither task provides oracle utterance boundaries or speaker labels at evaluation, and Task 2 provides no question-answer training set. For Task 1, we fine-tune VibeVoice-ASR-7B with random leading-silence cropping, consistent timestamp correction, and an exponential moving average (EMA) training strategy. For Task 2, we construct synthetic question-answer pairs through multimodal candidate generation, silent-audio filtering, and distribution-matched augmentation, and fine-tune Qwen3-Omni-30B-A3B-Instruct for tagged direct answering. On the Task 1 evaluation set, cropping reduces tcpMER from 18.30% to 17.27%, and EMA further reduces it to 16.73%. On the Task 2 evaluation set, jointly applying distribution-matched augmentation and tagged direct answering raises accuracy from 83.0% to 86.0%.

### 中文一句话结论
本文针对MLC-SLM挑战的两个任务分别提出有效的单一模型方案：任务1通过随机前导静默裁剪和指数移动平均训练降低说话人识别错误率至16.73%；任务2通过多阶段合成数据（候选生成、静音过滤、分布匹配增强）和标签化直接回答格式将口语理解准确率提升至86.0%。

### English TL;DR
This paper presents single-model systems for both tasks of the MLC-SLM Challenge. For Task~1 (speaker diarization/recognition), random leading-silence cropping and EMA training reduce tcpMER from 18.30% to 16.73%. For Task~2 (conversational speech understanding), a synthetic QA pipeline with silent-audio filtering, distribution-matched augmentation, and tagged direct answering raises accuracy from 78.0% to 86.0%.

### 中文详细总结
本文针对第二届多语言对话语音语言模型（MLC-SLM）挑战的两项任务提出独立适配的单一模型系统。任务1为说话人日志与识别，任务2为对话语音理解（多选题）。任务1未提供评估时的语段边界或说话人标签，任务2未提供问答训练集。

- **任务1**：基于VibeVoice-ASR-7B骨干网络，采用LoRA微调。提出随机前导静默裁剪（随机去除首个标注片段前的非语音部分）并相应调整时间戳，以及指数移动平均（EMA）训练策略。在评估集上，裁剪使tcpMER从18.30%降至17.27%，EMA进一步降至16.73%，累计降低1.57个绝对百分点（相对降低8.6%）。
- **任务2**：基于Qwen3-Omni-30B-A3B-Instruct模型，通过多模态候选生成（Gemini 2.5 Pro）、静音音频过滤（用Qwen2.5-Omni-7B移除音频不贡献的样本）、分布匹配增强（翻译问题和生成长选项）构建约127k合成训练样本，并采用标签化直接回答格式（<answer>标签）。在评估集上，各步骤逐步提升准确率：基线78.0%→+候选生成81.0%→+静音过滤83.0%→+分布匹配85.0%→+标签回答86.0%。

### 方法 / 贡献
- **任务1方法**：保留VibeVoice-ASR-7B单遍解码架构，仅在微调阶段引入随机前导静默裁剪（保证不移除任何标注语音）和一致时间戳偏移；同时维护可训练参数的指数移动平均（λ=0.99）。使用LoRA（rank=32, scale=128），学习率1e-4，训练5个epoch。
- **任务2方法**：利用Gemini 2.5 Pro生成候选QA对（约210k），再用Qwen2.5-Omni-7B进行静音音频过滤（替换音频为静音后若仍回答正确则丢弃），保留约67k对；进一步通过翻译和合成生成长选项进行分布匹配增强（约60k额外实例）；最终将全部训练数据转换为统一聊天格式，答案用<answer>标签包裹。使用LoRA微调Qwen3-Omni，学习率5e-5，训练2个epoch。
- **贡献**：为无监督的对话语音理解任务提供了一套完整的合成数据生成与过滤流程；在说话人日志任务上证明了前导静默裁剪和EMA的有效性。

### 实验或数据
- **任务1实验**：使用官方评估集及metric（tcpMER，越低越好）。累积消融实验：LoRA基线18.30% → +裁剪17.27% → +EMA 16.73%。采用MeetEval计算指标，5秒collar设置。
- **任务2实验**：使用官方评估集评估多选准确率。累积消融：基线78.0% → +候选生成81.0% → +静音过滤83.0% → +分布匹配85.0% → +标签回答86.0%。训练数据来源于挑战赛发布音频，未使用评估集任何内容。
- **数据集**：官方多语言对话录音，任务1评估集包含日语、韩语、泰语等多种语言；任务2评估集包含声学、语义和联合理解问题，每问2-4个选项。

### 值得关注点
- 任务1中随机前导静默裁剪是一种新颖的音频时间增强方法，不改变语音内容，仅通过改变录音绝对起始位置提升泛化性。
- 任务2的静音音频过滤（counterfactual filtering）有效识别并移除仅靠文本先验可回答的样本，提升训练数据质量。
- 分布匹配增强根据评估集输入特征（长选项、跨语言问答）定向合成数据，提高泛化能力。
- 标签化直接回答格式（<answer></answer>）简化预测提取，带来额外准确率提升。

### 局限性
- 任务1的消融实验为累积式，无法分离裁剪与EMA各自独立贡献，也未进行仅EMA的训练；无法判断改善是否均匀覆盖各语言、录音时长或首发言条件。
- 任务2的合成数据依赖商用API（Gemini 2.5 Pro）和另一个模型（Qwen2.5-Omni）进行过滤，外部依赖可能影响可复现性。
- 两项任务均未使用模型融合或多系统集成，单一模型性能可能尚未达到组合方案上限。
- 任务2的分布匹配增强基于评估集聚合统计（选项长度、跨语言比例），若未来评估分布变化，泛化性需进一步验证。

## 10. Bootstrapping Niche Multilingual Code Translation via Reinforcement Learning with Execution-Based Verifiable Supervision

- Source: arxiv
- arXiv ID: 2608.13854
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.13854v1
- PDF: https://arxiv.org/pdf/2608.13854v1
- DOI: https://doi.org/10.48550/arXiv.2608.13854

### Authors

Kouki Yuki, Jie Zeng, Kyoko Ogawa, Ryunosuke Ikeda, Yohei Kobashi, Takeshi Kojima, Ikuya Yamada, Yusuke Iwasawa, Yutaka Matsuo

### Abstract

Code translation must preserve executable behavior across many programming languages, yet neural code translation has largely focused on a few popular languages such as C++, Java, and Python. This leaves a niche, many-to-many setting where parallel supervision is sparse, producing plausible but non-executable translations. We address this setting with preference-based reinforcement learning driven by execution-based supervision. Our pipeline firstly expands verifiable seed Python programs into a multilingual pool of execution-validated codes. Using the pool, a base LLM generates translation candidates across language pairs, which we label by their execution outcomes. The resulting preferences are used to train a reward model that scores cross-language translation quality. Finally, we optimize our base LLMs with GRPO over 600 directed language pairs (25 x 24) using the reward model as a signal. To evaluate the niche translation capability, we introduce HumanEval-X++, an execution-based benchmark that extends HumanEval-X to a broad many-to-many language space. We evaluate our approach using Qwen-3.5 4B and 9B models. On HumanEval-X++ and existing benchmarks, it yields consistent gains over the untrained baselines. In particular, the 4B model achieves an average improvement of 13% across all languages on HumanEval-X++, with a gain of 21% on mid-tier languages. Our study establishes a reliable approach of data generation, training, and benchmarking, paving the way toward further bootstrapping the quality of many-to-many translation for programming languages.

### 中文一句话结论
本文通过基于执行验证的偏好强化学习管道，在覆盖25种语言的600个翻译方向上，使小规模基础模型（4B）在HumanEval-X++基准上平均提升13%，中档语言提升21%，实现了小众多语言代码翻译的有效自举。

### English TL;DR
This paper introduces a reinforcement learning pipeline that leverages execution-based verification to train a reward model and optimize code translation across 25 languages, achieving consistent improvements (13% average gain on the introduced HumanEval-X++ benchmark) for niche many-to-many translation pairs.

### 中文详细总结
神经代码翻译主要关注C++、Java、Python等流行语言，导致小众的多语言多方向翻译（25种语言，600个方向）缺乏并行监督，易产生不保执行的翻译。  
本文提出NicheCodeTranslator，一个基于执行验证的偏好强化学习管道：  
1. **数据生成**：从Python种子程序出发，通过规则转换和沙盒执行验证，扩展到25种语言的执行验证代码池；再使用基础LLM生成翻译候选项，根据执行结果标记正负偏好。  
2. **训练**：用偏好数据训练一个奖励模型替代实际执行，再通过GRPO利用该奖励信号优化基础LLM。  
3. **评估**：引入HumanEval-X++（将HumanEval-X的目标语言从6种扩展到25种）作为执行级基准。  
在Qwen-3.5 4B和9B模型上实验，4B模型在HumanEval-X++上平均提升13%，其中中档语言提升21%；在CodeScope基准上同样有稳定增益。  
该方法建立了可靠的数据生成、训练和评估流程，为将多语言代码翻译质量推向更多语言方向提供了可行路径。

### 方法 / 贡献
**方法**：  
1. 从KodCode中筛选Python种子，合成并验证字面量断言，通过AST分析提取类型信息，生成带类型标注的可验证程序。  
2. 使用规则转换器（MultiPL-E）将Python代码和断言转换为24种目标语言，并采样生成执行验证通过的源程序。  
3. 对每个验证过的源程序，在另外24种目标语言上采样翻译候选，根据执行通过与否标记正负样本，构建600个方向的偏好数据集。  
4. 训练一个交叉语言奖励模型，预测翻译候选是否通过测试；然后使用GRPO优化策略，以该奖励模型作为学习信号。  

**贡献**：  
- 首次将执行验证驱动的RL管道扩展到25种语言和600个翻译方向，远超前人工作。  
- 引入奖励模型替代实际执行环境，使训练可稳定扩展到大量语言对。  
- 提出HumanEval-X++基准，扩展多方向代码翻译的评估空间。  
- 在4B和9B模型上验证方法有效性，证明小模型也能通过该管道显著提升翻译质量。

### 实验或数据
论文使用Qwen-3.5 4B和9B作为基础模型。  
**评估基准**：  
- HumanEval-X++：由HumanEval-X扩展而来，将目标语言从6种增至25种，提供执行级测试。  
- CodeScope：现有代码翻译基准。  

**实验结果**：  
- 4B模型在HumanEval-X++上平均改善13%，其中中档语言（mid-tier）改善21%。  
- 9B模型在HumanEval-X++及CodeScope上均一致优于未训练基线。  
- 训练数据、模型权重及基准代码将在论文发表后公开。

### 值得关注点
- **可扩展性**：使用训练好的奖励模型替代物理执行环境，使RL训练能覆盖25种语言，无需要运行每个语言的沙盒。  
- **确定性验证传播**：通过规则转换（而非生成模型）跨语言传播测试，保证了验证正确性。  
- **小模型提升显著**：4B模型即能通过该管道获得可观收益（平均13%），说明方法对资源受限场景有实用价值。  
- **覆盖范围广**：首次在代码翻译训练中覆盖600个方向（25×24），包括大量小众语言方向。  
- **基准扩展**：HumanEval-X++为多语言翻译提供了更全面的执行级评估平台。

### 局限性
论文在提供的摘要和预览内容中未明确讨论局限性。从方法设计可推断：  
- 依赖Python种子的质量及规则转换器的覆盖能力，对于不支持的结构可能被丢弃。  
- 仅处理单函数、无类的代码片段，尚未扩展到模块级或类级翻译。  
- 奖励模型可能无法完全替代真实执行，存在过拟合风险。  
- 实验仅基于Qwen-3.5系列，在更大模型或其他架构上的泛化性待验证。

## Processing Notes

- Duplicate papers skipped: 0