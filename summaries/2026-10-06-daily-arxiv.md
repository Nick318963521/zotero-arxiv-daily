# Daily arXiv - 2026-10-06

- Source: GitHub Actions generated paper list
- Generated at: 2026-10-06T02:54:53
- Paper count: 10

## 1. Trained Agentic Context Management

- Source: arxiv
- arXiv ID: 2610.02404
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2610.02404v1
- PDF: https://arxiv.org/pdf/2610.02404v1
- DOI: https://doi.org/10.48550/arXiv.2610.02404

### Authors

Bryce Sandlund

### Abstract

We study long context language models. Instead of training long context natively, or designing a long context harness, we train a model over the simplest possible harness: a tool to call itself with any specified prompt and a tool to read tokens in a range from the input context. We finetune Qwen3.6-35B-A3B on a diverse synthetic dataset using this harness. With only 8,000 tokens of context, our small model is as strong as GPT-5.4 with 1M tokens of context on the OOLONG-synth benchmark when document length exceeds 40K tokens.

### 中文一句话结论
本文通过训练一个简单的代理工具（自调用和块读取）对Qwen3.6-35B-A3B进行微调，在仅用8K令牌上下文的条件下，对超过40K令牌的长文档实现了与使用1M令牌上下文的GPT-5.4相当的性能。

### English TL;DR
This paper trains a small language model with a minimal agentic harness (self-call and chunk reading) to manage long contexts. By finetuning Qwen3.6-35B-A3B on synthetic data, it achieves performance on OOLONG-synth comparable to GPT-5.4 with 1M tokens of context, while using only 8,000 tokens per agent.

### 中文详细总结
该研究针对长上下文语言模型，提出不进行原生长上下文训练或设计复杂场景，而是训练模型使用最简单的工具集：一个调用自身并指定提示的工具，以及一个读取输入上下文指定范围令牌的工具。作者在多样化合成数据集上微调了Qwen3.6-35B-A3B。实验表明，在OOLONG-synth基准测试中，当文档长度超过40K令牌时，该模型仅使用每代理8K令牌的上下文，就与GPT-5.4使用1M令牌上下文的性能相当。在RULER基准上，该模型也取得了具有竞争力的分数（≥85%）。方法包括使用监督微调（SFT）教会模型三种分解策略：树归约（用于无序任务）、顺序折叠（用于有序任务）和代理委托（处理边界条件）。模型在训练中内化了这些策略，能够根据任务和当前解决问题状态灵活组合。论文还尝试了强化学习（RL）阶段，但发现基于评判者的奖励存在高方差，模型倾向于简单策略从而降低性能，因此未采用RL。

### 方法 / 贡献
- 提出一个极其简单的智能体式上下文管理场景：仅包含两个工具（读取块和生成子代理），不硬编码分解结构。
- 通过监督微调（SFT）在Qwen3.6-35B-A3B上训练模型，使其内化并组合树归约、顺序折叠和代理委托等多种分解策略。
- 展示了使用小上下文窗口（8K令牌）的模型在处理远超上下文限制的长文档（超过40K令牌）时，能够与使用极大上下文（1M令牌）的强大模型（如GPT-5.4）匹敌。

### 实验或数据
- 模型：微调Qwen3.6-35B-A3B，使用8K令牌每代理的上下文限制。
- 基准：在RULER和OOLONG-synth上评估。基线包括基础Qwen3.6-35B-A3B（64K令牌上下文）和GPT-5.4（1M令牌上下文）。
- 主要结果：在OOLONG-synth上，当文档长度超过40K令牌时，该模型与GPT-5.4性能相当（性能曲线重合）。在RULER上，模型得分≥85%（论文提及，但未明确给出精确值）。
- 训练数据：多样化合成数据集，涵盖聚合、检索和顺序任务，包括记录、散文、点分隔词列表和带注射针的草堆等。

### 值得关注点
- 效率：仅用8K令牌上下文即可处理远大于上下文限制的长文档，大幅降低计算成本。
- 简约性：工具集极其简单（两个工具），但足以支持复杂的多代理分解。
- 策略内化：模型通过训练学会了主动分解任务，而不是依赖人设定的硬编码场景。

### 局限性
- 强化学习（RL）阶段未能成功提升性能：使用LLM作为评判者的奖励导致高方差，模型倾向于选择简单策略，削弱了整体表现。
- 训练依赖合成数据：可能无法完全泛化到真实世界任务的多样性。
- 仅在一个模型（Qwen3.6-35B-A3B）上验证，未在更多架构上测试泛化性。
- 论文未在更多前沿模型（如Claude、Gemini等）上进行全面对比（受限于计算资源），但推荐读者参考OOLONG论文中的比较。
- 在RULER基准上未与同等级别的前沿模型进行充分比较（但RULER对前沿模型已接近饱和）。

## 2. Collective Bias Mitigation via Model Routing and Collaboration

- Source: arxiv
- arXiv ID: 2610.03240
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2610.03240v1
- PDF: https://arxiv.org/pdf/2610.03240v1
- DOI: https://doi.org/10.48550/arXiv.2610.03240

### Authors

Mingzhe Du, Luu Anh Tuan, Xiaobao Wu, Yichong Huang, Yue Liu, Dong Huang, Huijun Liu, Bin Ji, Jie M. Zhang, See-Kiong Ng

### Abstract

Large language models (LLMs) are increasingly deployed in public health, finance, and governance, requiring both accuracy and societal value alignment. Despite recent advances, LLMs often perpetuate or amplify bias embedded in their training data, posing challenges to fairness. While self-debiasing encourages an LLM to identify and correct its own biases, relying on a single model's intrinsic knowledge may be insufficient to address deeply ingrained stereotypes. To address this limitation, we introduce Collective Bias Mitigation (CBM), a framework that alleviates bias by learning fine-grained model behavior and fostering knowledge sharing among diverse LLMs. This work is the first to systematically explore the effective selection and organization of distinct LLMs to cultivate fairer LLM responses. Experiments show CBM substantially outperforms standalone baselines (e.g., in the top-7 setting, Committee lowers the age bias score from 0.25 to 0.10). Our Debating and Committee topologies achieve substantial bias reduction, with the latter balancing mitigation effectiveness and inference cost, highlighting the potential of CBM for fairer LLMs.

### 中文一句话结论
CBM通过路由查询至多个不同LLM并组织协作拓扑（如Debating和Committee），显著降低了模型偏见，尤其以Committee拓扑在效率和效果间取得平衡。

### English TL;DR
This paper introduces Collective Bias Mitigation (CBM), a framework that reduces societal biases in large language models by routing queries to diverse LLMs and organizing them into collaborative topologies (e.g., Debating and Committee), significantly outperforming single-model baselines.

### 中文详细总结
该论文提出集体偏见缓解框架（CBM），通过整合多个大型语言模型（LLMs）的特征来消除偏见。首先构建CrowdEval数据集，收集50多个开源LLMs对偏见诱导查询的响应。利用该数据集微调一个模型路由器，为每个查询选择最合适的LLM。然后，将选中的模型组织成特定拓扑（如Debating和Committee）进行协作，生成更公正的响应。实验表明，CBM在多个社会维度上降低了偏见分数，例如在top-7设置下，Committee将年龄偏见分数从单模型的0.25降至0.10。

### 方法 / 贡献
- 提出CrowdEval数据集，用于细粒度评估LLM在多个社会维度上的偏见行为。
- 首次提出基于多模型协作的集体偏见缓解框架（CBM），通过模型路由和协作拓扑实现偏见降低。
- 模型路由器基于概率机制，学习模型行为而非模型名称，以实现更优的模型选择。
- 探索了两种主要拓扑：Debating（辩论）和Committee（委员会），后者在偏见缓解和推理成本之间取得平衡。

### 实验或数据
- 使用来自BBQ数据集模糊子集构建的CrowdEval数据集，涵盖年龄、性别、种族等社会维度。
- 评估了50多个开源LLM，包括不同规模和架构的模型。
- 实验表明CBM显著优于单模型基线：在top-7设置下，Committee将年龄偏见分数从0.25降至0.10；Debating拓扑通常取得最低偏见分数。

### 值得关注点
- 首次系统性地研究选择和组织多个不同LLM以实现更公平的响应。
- 模型路由器基于训练数据中的模型行为而非名称进行选择，避免了过拟合。
- 协作拓扑（Debating/Committee）的设计新颖，有效利用模型多样性。
- 在多个社会维度上实现一致的偏见降低，且Committee拓扑在效率和效果间取得良好平衡。

### 局限性
论文未明确讨论局限性，但潜在局限可能包括：依赖特定模型池和数据集（源自BBQ），多模型协作带来的推理成本，以及可能未覆盖所有社会偏见类型。

## 3. OLMo-Detect: A Multi-Stage, Confounder-Controlled Benchmark for Membership Inference on Large Language Models

- Source: arxiv
- arXiv ID: 2610.02986
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2610.02986v1
- PDF: https://arxiv.org/pdf/2610.02986v1
- DOI: https://doi.org/10.48550/arXiv.2610.02986

### Authors

Tao Shi, Chaoyi Xiang, Qiongkai Xu, Jey Han Lau

### Abstract

Membership inference on large language models (LLMs) aims to determine whether a given text sample was included in an LLM's training data, without access to its training corpus. Despite recent progress, existing benchmarks suffer from three limitations: limited coverage of training stages, insufficient distributional alignment between members and non-members, and lack of rigorous filtering of non-members against the training corpus. To address these limitations, we propose OLMo-Detect, a multi-stage, confounder-controlled benchmark built upon the fully open OLMo 2 pipeline. OLMo-Detect spans pre-training, mid-training, and post-training, explicitly aligns members and non-members on three key axes, and rigorously filters non-members via infini-gram. To assess robustness to distribution shifts, we further introduce OLMo-Detect (Shifted), a variant where members are misaligned with non-members. We evaluate 15 unsupervised and 3 supervised membership inference attacks (MIAs) across the OLMo 2 family, finding that: (i) overall performance is limited: the best unsupervised and supervised MIAs both reach an AUC of only 0.68, and supervised MIAs degrade under cross-domain evaluation; (ii) MIA performance peaks at mid-training and is lower at pre-training and post-training, a pattern driven by data type rather than a stage effect: curated math data is far more detectable than other types; (iii) overall scores improve from 1B to 13B but plateau at 32B; and (iv) no unsupervised MIA is robust to distribution shifts, with AUCs shifting by up to 0.42. Finally, we find that our findings on OLMo 2 generalize to OLMo 3 and non-OLMo models.

### 中文一句话结论
OLMo-Detect基准揭示了当前成员推断攻击在LLM上的性能有限（最佳AUC仅0.68），且在分布偏移下缺乏鲁棒性。

### English TL;DR
OLMo-Detect is a multi-stage, confounder-controlled benchmark for membership inference on LLMs, built on the OLMo 2 pipeline. It evaluates 15 unsupervised and 3 supervised attacks, finding that overall performance is limited (best AUC 0.68), performance peaks at mid-training and improves with model size up to 13B, and no unsupervised attack is robust to distribution shifts.

### 中文详细总结
该论文提出OLMo-Detect，一个针对大语言模型成员推断攻击的多阶段、混杂因素控制的基准。它基于完全开放的OLMo 2流水线构建，覆盖预训练、中训练和后训练三个阶段。通过显式对齐成员与非成员在三个关键轴上，并使用infini-gram严格过滤非成员。此外，引入OLMo-Detect (Shifted)变体，其中成员与非成员不对齐，以评估对分布偏移的鲁棒性。评估了15种无监督和3种有监督成员推断攻击，主要发现包括：整体性能有限，最佳无监督和有监督攻击AUC均为0.68，有监督攻击在跨域评估下性能下降；攻击性能在中训练阶段达到峰值，预训练和后训练阶段较低，这种模式由数据类型驱动而非训练阶段本身，即整理后的数学数据比其他类型更易检测；整体分数从1B提升到13B模型，但在32B处趋于平稳；无监督攻击对分布偏移不鲁棒，AUC变化可达0.42。最后，这些发现也推广到OLMo 3和非OLMo模型。

### 方法 / 贡献
- 提出OLMo-Detect基准，覆盖多训练阶段（预训练、中训练、后训练）。
- 通过三个关键轴（如数据源、处理方式等）显式对齐成员与非成员，并利用infini-gram严格过滤非成员。
- 引入OLMo-Detect (Shifted)变体，用于测试对分布偏移的鲁棒性。
- 对OLMo 2系列模型进行系统评估，含15种无监督和3种有监督MIA。
- 验证发现可泛化至OLMo 3及其他非OLMo模型。

### 实验或数据
实验基于OLMo 2模型家族（1B至32B），使用OLMo-Detect基准及其Shifted变体。评估了15种无监督攻击（如基于困惑度、梯度等）和3种有监督攻击（如基于分类器）。数据来自OLMo 2管道，包括预训练、中训练（含数学等类型数据）和后训练阶段。非成员通过infini-gram过滤。实验结果报告了AUC等指标，并进行了跨域评估和模型规模对比。

### 值得关注点
- 成员推断攻击在LLM上的整体性能远低于预期，最佳AUC仅0.68，表明当前攻击方法有效性的天花板。
- 训练阶段的数据类型（如数学数据）是影响检测性的关键因素，而非阶段本身。
- 无监督MIA在分布偏移下非常脆弱（AUC变化高达0.42），限制了实际场景的可用性。
- 攻击性能随模型规模增大而提升，但到32B时趋于饱和。
- 基准设计强调混杂因素控制，更真实评估攻击能力。

### 局限性
- 攻击性能有限，尤其在分布偏移场景下，无监督MIA的鲁棒性严重不足。
- 有监督MIA在跨域评估时性能明显下降，泛化能力弱。
- 基准仅基于OLMo系列模型，尽管验证了部分泛化性，但其他架构下的表现仍需进一步探索。
- 论文未深入探讨可能缓解上述局限性的方法（如对抗训练、更好的分布对齐等）。

## 4. Objects Without Morphisms: What LLMs for Mathematics Do Not Represent

- Source: arxiv
- arXiv ID: 2610.03551
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2610.03551v1
- PDF: https://arxiv.org/pdf/2610.03551v1
- DOI: https://doi.org/10.48550/arXiv.2610.03551

### Authors

Yanli Wang, Suijin Wang, Xiaopeng Yuan, Haohan Wang

### Abstract

Large language models (LLMs) have reached expert-level performance on competition mathematics largely through the volume of search placed around them: candidate solutions are sampled in quantity and retained only when an external criterion accepts them. Such a procedure improves the outcome that survives it while leaving untouched what the model represents. We examine that question where no external criterion exists: translating statements between the dialects of neighbouring subfields, where fidelity turns on the level of generality at which content is asserted. The source leaves that level implicit in its vocabulary, so a faithful translation must recover it from the relation between the theories. We introduce an instrument that codes truth, content and scope in separate blind queues, with a judge-free measure of whether a rewrite states the hypothesis implicit in its source, and establish its sensitivity with a planted-positive control. Across seven models from four families, translating towards the general framing widens the domain of quantification in 60.6% of rewrites and narrows it in none; translating towards the concrete framing narrows it in 28.3% and widens it in 0.3%. The hypothesis that would prevent it is stated in 21.6% of model rewrites and 4.2% of human statements. Capability does not govern the asymmetry: it appears in every model tested, and the most capable widens least. It replicates on the half of the benchmark held out by a pre-registered rule, and on statements written by mathematicians. Instructing a model to state every hypothesis it requires raises that rate but not its sensitivity to direction. We argue that these systems have acquired an object-level correspondence between subfield vocabularies without the constraint under which a translation between theories carries hypotheses to hypotheses.

### 中文一句话结论
大型语言模型在数学子领域间的术语翻译中仅实现对象级对应，却未能保持隐含的假设和概括层次，系统性地扩大量化范围，且极少显式陈述所需的假设，缺乏态射级约束。

### English TL;DR
LLMs for mathematics translate between neighboring subfield vocabularies at an object level but fail to preserve the underlying hypotheses and levels of generality, systematically widening quantification toward general framings and rarely stating the hypotheses their translations require—revealing a missing morphism-level constraint.

### 中文详细总结
本文考察了大型语言模型（LLMs）在数学相邻子领域之间进行陈述翻译时，是否真正理解了隐含的概括层次和理论假设。作者发现，这些模型能够在词汇层面进行对应（对象级映射），但在没有外部验证标准（如竞赛题搜索）的情况下，翻译结果系统性地失去约束：当从具体框架翻译到一般框架时，量化域在60.6%的改写中被扩大，从未被缩小；反之，从一般到具体时，28.3%被缩小，仅0.3%被扩大。此外，模型仅在21.6%的改写中显式陈述了防止这种偏移所需的假设，而人类陈述中该比例仅为4.2%。作者引入了一种通过盲分离编码真值、内容和范围的工具，并设置了植入正向对照来验证方法的敏感性。实验涵盖4个模型家族的7个模型，结果在所有模型上表现一致，且模型能力并不主导这种不对称性：最强模型反而扩大最轻。即便如此，即使让模型显式写出所有所需假设，对其方向敏感性也无改善。作者由此论证，LLMs已习得子领域间的对象级词汇对应，但缺乏翻译理论时应有的“假设到假设”传递约束，即“缺少态射（morphism-level）约束”。

### 方法 / 贡献
- **核心问题**：检验LLMs在翻译数学子领域陈述（如从具体框架到一般框架）时，是否保留了隐含的概括层次和理论假设。
- **新颖工具**：设计了一种将真值、内容和范围编码到独立盲队列中的协议，并引入免评判的度量来衡量改写是否陈述了原句中隐含的假设。另外设置了植入正向对照（人工作答的例子）来验证工具的敏感性。
- **主要发现**：定性并定量揭示了系统性的量化范围偏移（无外部准则时），以及假设显式化率低的现象；指出现有LLMs数学推理能力仅仅依赖外部搜索，内部表示缺乏深层次形态约束。
- **贡献**：首次在无外部验证的翻译设置下，系统刻画LLMs数学理解的一个根本性缺失——对象级对应与理论级约束之间的鸿沟。

### 实验或数据
- **实验对象**：来自4个模型家族的7个LLMs（具体模型名称未见，但包括不同规模/品牌）。
- **任务**：对数学相邻子领域（如具体与一般框架）之间的陈述进行改写翻译。
- **数据**：实验在多个子领域陈述集上进行；同时使用了数学家撰写的陈述作为人类基线。包含前半部分基准（用于主要分析）和一个预先注册规则留出的后半部分（用于复现验证）。
- **度量**：量化域变化方向（扩大/缩小/不变）和假设显式陈述率。设置植入正向对照以验证度量敏感性。
- **结果**：如详细总结所述——不对称性和低假设显式化率在所有模型上鲁棒出现；指导模型显式写假设提升陈述率但方向敏感性无改善。

### 值得关注点
- 揭示了LLMs数学推理中一个隐蔽但系统的缺陷：即使在词汇层面翻译正确，却无法维持理论层面的概括层次约束。
- 所有被测试模型（包括最强模型）均表现出相同倾向，说明该问题具有普遍性，并非能力制约。
- 当要求模型显式写出所需假设时，假设陈述率提高，但方向敏感性（能否在改写时正确定位概括层次）没有改善，说明训练或提示难以弥补这一结构缺失。
- 人类基线中假设显式陈述率仅4.2%，暗示该问题也存在于人类，但模型进一步放大了偏移。

### 局限性
- 实验仅考察了数学子领域间的翻译任务，未涉及其它数学推理或非数学领域，结论普遍性尚需验证。
- 所使用的“工具”（盲分离队列和度量）虽然通过植入正向对照验证了敏感性，但未明确讨论其可靠性或潜在偏差（如误报/漏报）。
- 模型代数族和具体规模未知，无法判断该现象是否随规模或训练数据分布变化。
- 研究未提供不同提示方式或解码参数的详尽消融实验，指导模型写假设后方向敏感性未改善的原因有待深入分析。
- 关于“对象级对应”是否可能补充以加强态射级约束，本文未给出具体解决路径或训练方案。

## 5. Ontological Instability and Statistical Amplification: The Paradox of "Humanizing" LLM-Generated Text

- Source: arxiv
- arXiv ID: 2610.03110
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2610.03110v1
- PDF: https://arxiv.org/pdf/2610.03110v1
- DOI: https://doi.org/10.48550/arXiv.2610.03110

### Authors

Claudiu Creanga, Liviu Dinu

### Abstract

Supervised AI-text detectors report high benchmark accuracy, but it is not clear what their decisions are based on. We analyze a RoBERTa-based detector under semantic, structural, and tokenizer-level perturbations, using the M4 dataset (N = 10,000) and controlled generations (N = 300). When Mistral-7B-Instruct was asked to make machine text sound more human, Verb Diversity rose from 0.77 to 0.92 and the outputs became easier to detect. Detection scores appear to track statistical complexity, which also leads to a 76.3% false-positive rate on formal human writing. As a control, we evaluate event-based Latent Space detection. Paraphrasing changed 87% of its event sequences (Jaccard = 0.067), and homoglyphs altered 70% of the extracted verbs even though extraction still ran (Jaccard = 0.30). Its best domain AUC was 0.577. RoBERTa's robustness seems specific to the features it uses, and structural abstraction did not make detection more robust.

### 中文一句话结论
本文发现，试图用Mistral-7B“人性化”改写机器文本反而会提高词元多样性（Verb Diversity从0.766升至0.924），使RoBERTa检测器更容易识别（检测率仍达95%），而基于事件的Latent Space检测器在语义和字符级扰动下均表现脆弱（最佳AUC仅0.577）。

### English TL;DR
Paraphrasing to "humanize" LLM text paradoxically increases lexical diversity, making RoBERTa detection easier (95% detection after three rounds), while event-based detectors fail on both semantic (Jaccard=0.067) and homoglyph (Jaccard=0.30) attacks; RoBERTa also shows a 76.3% false-positive rate on formal human writing.

### 中文详细总结
论文分析了基于RoBERTa的检测器在语义、结构和tokenizer级扰动下的行为。用Mistral-7B改写机器文本后，动词多样性显著上升（0.766→0.924），但检测分数依然很高（平均0.949），说明检测器依赖统计复杂度而非语义。人类正式写作的假阳性率高达76.3%，表明检测器对形式敏感。作为对照的Latent Space方法（基于动词序列）在改写下Jaccard相似度仅0.067，同形字攻击下70%的提取动词被改变（Jaccard 0.30），其在各领域的最佳AUC仅0.577（WikiHow），多数领域低于随机。实验支持“鲁棒性取决于所使用的特征”这一观点。

### 方法 / 贡献
使用M4数据集（10,000样本）和300个受控生成样本，对RoBERTa检测器进行三种扰动测试：迭代改写（Mistral-7B）、事件序列更改、同形字替换。引入Latent Space检测器作为结构对照，并定义指标：Verb Diversity（动词类型-词例比）和Event Sequence Preservation（Jaccard相似度）。贡献在于揭示“人性化”改写的悖论效应，并指出检测器的鲁棒性基于统计特征而非语义理解。

### 实验或数据
- **迭代改写**：三轮后检测率94.9%，Verb Diversity从0.766升至0.924。
- **Persona压力测试**：三种人格（Child/Neutral/PhD）下检测率均≥98.8%，Verb Diversity均高于人类基线（0.572）。
- **同形字攻击**：20%替换率时逃逸率13%，30%时更高；NFKC归一化无效。
- **Latent Space对照**：改写后Jaccard=0.067（87%事件序列改变），同形字B原本70%动词改变（Jaccard=0.30）；跨领域AUC最佳仅0.577（WikiHow），ArXiv和PeerRead低于随机（0.385/0.393）。
- **熵与困惑度**：人类文本Gzip比0.541，机器0.587；GPT-2困惑度人类40.0，机器30.2。
- 数据来自M4数据集（5,000验证+5,000测试）和生成的300个样本。

### 值得关注点
1. 改写反而提高检测率，因为增加了词元多样性，而非减少。
2. 检测器对形式敏感，导致正式人类文本（如学术写作）被高概率误判（76.3%假阳性）。
3. Latent Space方法在抽象表示上并未更鲁棒，两种攻击均脆弱。
4. 同形字攻击能有效绕过RoBERTa，但简单的字符清理（NFKC）无效，需额外映射表。

### 局限性
- 仅评估RoBERTa和Latent Space两种检测器，未涉及其他SOTA方法。
- 生成模型限于Mistral-7B，改写提示为单一模板。
- 同形字攻击仅覆盖部分Unicode字符，可能低估攻击面。
- 熵分析基于200个样本，跨领域稳定性未知。
- 未探讨检测器的自适应防御或更细粒度的校准策略。

## 6. To Jev or Not? Evaluating the Accuracy and Efficiency of Structured Decision Models for Hate-Speech Moderation

- Source: arxiv
- arXiv ID: 2610.03324
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2610.03324v1
- PDF: https://arxiv.org/pdf/2610.03324v1
- DOI: https://doi.org/10.48550/arXiv.2610.03324

### Authors

Demetris Paschalides, George Pallis, Marios D. Dikaiakos

### Abstract

The scale of online content makes hate-speech moderation challenging, while Large Language Models (LLMs) enable harmful material to be produced and adapted more easily. Moderation therefore requires efficient classifiers that can accommodate different definitions of hate speech. Recent structured decision models accept natural-language criteria and select among specified answers, raising the question of whether they can meet these requirements without task-specific training. We present HATEDECIDE, an evaluation of six decision-model configurations on four hate-speech datasets against specialized moderation, zero-shot, commercial, and supervised baselines. We examine whether supplying a dataset's definition, or decomposing it into multiple questions, improves classification, and we measure their latency and cost. We find that commercial LLMs significantly outperform all decision models on only one dataset. Supplying definitions changes up to 28\% of predictions without consistently improving classification, and decomposition significantly improves performance in only 20\% of the comparisons. On a diagnostic set of test cases, the best hosted decision model comes within 1.6 macro-F1 points of the best commercial LLM at approximately 97\% lower inference cost. These results identify opportunities for inexpensive moderation, while showing that explicit criteria and additional questions do not reliably improve classification.

### 中文一句话结论
结构化决策模型在仇恨言论审核中能以极低成本达到接近商业大语言模型的效果，但提供定义和分解问题并不能稳定提升分类准确性。

### English TL;DR
Structured decision models for hate-speech moderation can be cost-effective and competitive with commercial LLMs, but supplying definitions and decomposing decisions do not consistently improve classification accuracy.

### 中文详细总结
本文提出了 HATEDECIDE，系统评估了六种结构化决策模型配置在四个仇恨言论数据集上的表现，并与专用审核模型、零样本模型、商业大语言模型和监督学习基线进行比较。研究发现：商业大语言模型仅在四个数据集中的一个上显著优于所有决策模型（高出 4.1-5.9 macro-F1 分）；提供数据集定义会导致最多 28% 的预测发生变化，但并未持续提升分类性能；定义分解仅在 20% 的比较中显著改善分类。在诊断性测试集上，最佳托管决策模型与最佳商业大语言模型的 macro-F1 差异仅为 1.6 分，但推理成本降低了约 97%。结果揭示了低成本审核的可能性，同时表明显式标准和额外问题并不能可靠地提升分类准确性。

### 方法 / 贡献
1. 提出 HATEDECIDE 框架，系统评估六种结构化决策模型（Jev、Laya、Decider、SemIf (Qwen3.5-2B/4B)、Bespoke-Nimble-9B）的仇恨言论审核能力。
2. 对比四种基线：政策条件审核模型（CoPE）、零样本分类器（BART）、商业大语言模型（GPT-4 等）、监督学习分类器（在数据集内和跨数据集测试）。
3. 实验变量包括：是否提供数据集定义、直接分类 vs 分解为多问题分类（如目标群体、是否包含辱骂等）。
4. 测量分类质量（macro-F1）、延迟和成本，回答四个研究问题（RQ1-RQ4）。

### 实验或数据
使用四个英语仇恨言论数据集：Dynamic（4,120 条测试，含六类行为标签）、MHS（3,203 条，来自 YouTube/Reddit/Twitter）、HateXplain（1,924 条，三分类）、HateCheck（3,728 条，功能测试集）。评估 binary 和多分类任务，以及属性预测（如目标群体、仇恨类型）。未提及额外的原始实验数据。

### 值得关注点
1. 最佳托管决策模型与最佳商业大语言模型在诊断测试集上的 macro-F1 差距仅 1.6 分，但推理成本降低约 97%，展示了低成本审核的可行性。
2. 提供定义导致最多 28% 的预测变化，但未稳定提升分类质量，表明定义敏感性高但不一定有益。
3. 监督学习分类器在跨数据集测试中性能下降高达 54 macro-F1 分，凸显了定义差异的挑战。
4. 定义分解仅在 20% 的比较中显著改善分类，说明增加复杂度不一定带来收益。

### 局限性
1. 仅评估英语数据集，结果可能不适用于其他语言。
2. 未讨论不同定义间的兼容性或冲突问题。
3. 分解问题仅基于数据集标准定义，未探索其他可能的分解方式。
4. 未评估模型对对抗性或罕见仇恨言论样本的表现。
5. 延迟和成本测量可能因具体部署环境而异。

## 7. Fisher-Guided Submodular Data Selection for Continual Pre-Training of Large Language Models

- Source: arxiv
- arXiv ID: 2610.02593
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2610.02593v1
- PDF: https://arxiv.org/pdf/2610.02593v1
- DOI: https://doi.org/10.48550/arXiv.2610.02593

### Authors

Zhenghao Zhao, Gaowen Liu, Zhiling Lan, Yan Yan

### Abstract

Data selection is already a central bottleneck in large-language-model training, where web-scale corpora are noisy and token budgets are finite. In continual pre-training (CPT), it becomes a forgetting-control problem: a poorly chosen target-domain corpus can overwrite capabilities encoded in the pretrained checkpoint. Existing CPT practice either scores candidates with parameter-agnostic scalars such as perplexity, or mitigates forgetting by spending many extra general-domain replay tokens. Neither strategy directly asks how training on a candidate will move the model parameters. We show that loss-based selection causes the post-CPT Fisher diagonal to drift downward on exactly the high-Fisher coordinates the pretrained model had committed to, while leaving low-Fisher coordinates largely untouched. This asymmetry exposes a parameter-space mechanism for catastrophic forgetting. Motivated by this observation, we propose a Fisher-aware CPT selector that decomposes each candidate's gradient into an anchor component, which measures perturbation along committed parameter directions, and a frontier component, which measures update capacity in unconstrained low-Fisher subspaces. We aggregate these signals with a log-determinant submodular objective and optimize it in a single pass using a scalable streaming data selection pipeline. On TinyLlama-1.1B and Llama-3.1-8B CPT over medical data, our selector improves target-domain quality while bounding forgetting on held-out pretraining benchmarks. Most importantly, it is substantially more token-efficient than forgetting-aware replay. 1B selected tokens already outperform the replay strategy trained with 10B tokens on both adaptation and forgetting, giving a 10x token-efficiency advantage.

### 中文一句话结论
本文提出一种基于 Fisher 信息引导的子模数据选择方法用于大模型持续预训练（CPT），通过将候选数据的梯度分解为“锚定”与“前沿”两部分，在医疗领域 CPT 中提升目标域质量并控制灾难性遗忘，且相比回放策略实现了约 10 倍的 token 效率提升。

### English TL;DR
The paper proposes a Fisher-guided submodular data selection method for continual pre-training (CPT) of LLMs. It decomposes each candidate’s gradient into an anchor component (perturbation along committed parameter directions) and a frontier component (update capacity in low-Fisher subspaces), then selects data with a log-determinant submodular objective in a single streaming pass. On medical CPT with TinyLlama-1.1B and Llama-3.1-8B, it improves target-domain quality while limiting forgetting; 1B selected tokens outperform 10B replay tokens on both adaptation and forgetting, giving a 10× token-efficiency advantage.

### 中文详细总结
大语言模型训练中，数据选择已成为关键瓶颈；在持续预训练（CPT）场景下，该问题尤其表现为“遗忘控制”：如果目标领域语料选择不当，可能会覆盖预训练 checkpoint 中已有的能力。

现有 CPT 方法通常有两种做法：一是使用与参数无关的标量（如 perplexity）对候选数据打分；二是通过投入大量通用领域回放 token 来缓解遗忘。但这两类方法都没有直接回答“在该候选数据上训练会如何移动模型参数”这一核心问题。

本文发现：基于 loss 的数据选择会导致 CPT 后 Fisher 对角线在预训练模型原本“投入”的高 Fisher 坐标上显著下降，而低 Fisher 坐标基本不受影响。这种不对称性揭示了灾难性遗忘的一种参数空间机制。

为此，作者提出一种 Fisher 感知的 CPT 数据选择器：将每个候选样本的梯度分解为两部分——锚定分量（衡量沿已承诺参数方向的扰动）和前沿分量（衡量在未受约束的低 Fisher 子空间中的更新能力）。随后，用一个 log-determinant 子模目标函数聚合这些信号，并通过可扩展的流式数据选择流水线在单遍扫描中完成优化。

在医疗数据上的 TinyLlama-1.1B 与 Llama-3.1-8B CPT 实验中，该方法提升了目标域质量，同时控制了在保留预训练 benchmark 上的遗忘。更重要的是，仅用 1B 被选择 token 就能在适应性和遗忘两方面超过用 10B token 训练的回放策略，显示约 10 倍的 token 效率优势。

### 方法 / 贡献
- 揭示了基于 loss 的数据选择导致灾难性遗忘的参数空间机制：高 Fisher 坐标上的 Fisher 对角线下降，低 Fisher 坐标基本不变。
- 提出 Fisher 感知的 CPT 数据选择器，将候选梯度分解为“锚定分量”和“前沿分量”。
- 使用 log-determinant 子模目标函数聚合上述信号，并设计单遍、可扩展的流式数据选择流水线。
- 在不需要大量通用领域回放 token 的情况下，同时改善目标域适应能力并控制遗忘。
- 实验证明 1B 选择的 token 可媲美或优于 10B 回放 token，带来 10 倍 token 效率提升。

### 实验或数据
摘要中报告的实验为：在医疗数据上对 TinyLlama-1.1B 和 Llama-3.1-8B 进行持续预训练（CPT）。评估内容包括目标领域质量和在保留的预训练 benchmark 上的遗忘程度。结果显示，1B 被选择 token 在适应性和遗忘两方面均优于使用 10B token 的回放策略。摘要未提供更详细的数据集构成、benchmark 名称或具体指标数值。

### 值得关注点
- 从“参数空间”而非“标量 loss”出发设计数据选择标准，直接关联遗忘机制。
- 用 Fisher 信息区分“已承诺参数方向”和“可自由更新的低 Fisher 子空间”，思路较新颖。
- 方法为单遍流式选择，具备大规模 Web 语料上的实用潜力。
- 相比需要额外大量通用 token 的回放策略，文章报告了显著的 token 效率优势（10×）。

### 局限性
摘要未明确列出局限性。从已报告内容看，实验仅覆盖医疗领域数据以及两个模型规模（1.1B 和 8B），其在不同领域、更大模型或更广泛 CPT 场景下的泛化性仍需进一步验证。此外，方法依赖 Fisher 对角近似，在高维参数空间中的计算开销与近似误差也可能成为实际部署时需要考虑的问题。

## 8. Text-Centric Post-Training for Omni-Modal Reasoning

- Source: arxiv
- arXiv ID: 2610.02819
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2610.02819v1
- PDF: https://arxiv.org/pdf/2610.02819v1
- DOI: https://doi.org/10.48550/arXiv.2610.02819

### Authors

Ziyang Cheng, Yuhao Wang, Hongcheng Liu, Qimin Wu, Jingru Fan, Chen Qian, Yanfeng Wang, Yu Wang

### Abstract

Improving joint audio-visual reasoning in Omni Large Language Models typically incurs substantial data construction and training costs. Our diagnostics reveal multi-hop reasoning difficulties despite correct answers to all corresponding single-hop questions and suggest partial decoupling in the local optimization of perception and reasoning objectives. This motivates post-training with different emphases on these capabilities. Text-only reasoning training yields gains across data sources, model scales, and families. With the best-performing text-only configuration, supervised fine-tuning followed by reinforcement learning (RL) raises Qwen2.5-Omni-7B's geometric mean of nine reasoning scores by 25.83% over the base model, outperforming the complete native audio-visual route with 56.6% fewer GPU-hours. Training on data synthesized entirely by a text-only LLM raises this geometric mean by 21.01% without audio-visual data in construction or training. However, text-only training degrades perception. We therefore propose a text-centric post-training paradigm: text-only training provides the main reasoning optimization, and reduced-data native audio-visual RL then refines perception. Refinement uses about 90% fewer input tokens than full-data audio-visual RL, restores perception above the base level, and retains 93.5% of the best-performing text-only pipeline's reasoning gain.

### 中文一句话结论
本文提出一种以文本为中心的Omni大模型后训练方法，仅用纯文本训练提升多模态推理能力，再以少量音视频数据修补感知，最终在显著降低成本的同时实现了比全音视频训练更优的推理性能。

### English TL;DR
A text-centric post-training paradigm is proposed: text-only SFT + RL provides the main reasoning optimization, and lightweight audio-visual RL refines perception. This approach raises Qwen2.5-Omni-7B's reasoning geometric mean by 25.83% while using 56.6% fewer GPU-hours than the full audio-visual pipeline, and the refinement step restores perception with 90% fewer tokens.

### 中文详细总结
提升Omni大模型的音视频联合推理能力通常代价高昂。本文诊断发现模型在多跳推理上存在困难（尽管单跳正确），并指出这源于感知与推理目标的局部优化解耦。

作者提出以文本为中心的后训练范式：
1. 纯文本推理训练（SFT + RL）：核心提升推理能力，在各数据源、模型规模与家族上均有效。在Qwen2.5-Omni-7B上，9项推理得分几何平均提升25.83%，超越完整音视觉路线，且节省56.6% GPU小时。训练数据可完全由文本LLM合成，仍获21.01%提升。
2. 轻量级感知精炼：纯文本训练使感知下降，因此采用缩减数据的音视频RL修复感知。该阶段输入长度约缩减90%，将感知恢复至基线以上，并保留93.5%的推理增益。

### 方法 / 贡献
- **诊断：** 揭示多跳推理失败现象，发现“感知-推理”目标解耦。
- **方法：** 提出以文本为中心的后训练范式，分为文本推理训练（SFT+RL）与轻量级感知精炼（音视频RL）两阶段。
- **贡献：** 突破“推理提升必需多模态数据”的常规思路；大幅降低计算成本（-56.6% GPU小时）与数据成本（完全用文本合成数据）；引入解耦优化的新视角。

### 实验或数据
- **基座模型：** 围绕Qwen2.5-Omni-7B展开，并跨数据源、模型规模与家族验证。
- **训练数据：** 推理训练使用纯文本（人工或纯文本LLM合成）；感知精炼使用缩减量音视频数据。
- **评估指标：** 9项推理得分的几何平均。
- **关键结果：**
  - 文本SFT+RL：+25.83%几何平均，超越全音视频路线。
  - 纯文本LLM合成数据：+21.01%。
  - 计算开销：比全音视频路线减少56.6% GPU小时。
  - 感知精炼：输入缩减约90%，恢复感知，保留93.5%推理增益。

### 值得关注点
- 纯文本后训练可显著提升跨模态推理能力，极具反直觉性与启发意义。
- 所提范式在获得更强推理性能的同时，实现了计算量（GPU小时）和数据量（音视频输入token）的双重数量级缩减。
- 论文的诊断实验（多跳/单跳推理对比）揭示了模型内部推理与感知模块的潜在解耦，为后续设计解耦式优化策略提供了坚实的证据。
- 训练数据可完全由纯文本大模型生成，彻底规避了多模态数据的构建瓶颈。

### 局限性
- 纯文本训练后感知指标下降，必须引入音视频精炼阶段作为补偿，不能完全脱离多模态数据。
- 精炼阶段保留了约93.5%的推理增益，存在约6.5%的轻微损失。
- 本文聚焦于后训练阶段，未涉及基座模型的预训练架构或数据改动。
- 核心量化结论（如25.83%提升）主要基于Qwen2.5-Omni-7B，虽然在多种模型上验证了趋势，但绝对值可能存在差异。

## 9. What Is Lost in Post-Training? Default Collapse and the Loss of In-Context Steerability Across Diverse Perspectives

- Source: arxiv
- arXiv ID: 2610.02614
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2610.02614v1
- PDF: https://arxiv.org/pdf/2610.02614v1
- DOI: https://doi.org/10.48550/arXiv.2610.02614

### Authors

Jessica Dierking, Itai Shapira, Niclas Boehmer

### Abstract

AI models serving a heterogeneous population must act on the principles appropriate to each user and context. While post-training has been shown to narrow the views large language models express, prior work has focused on default behavior rather than the ability to adapt to in-context information. We show that post-training also degrades a model's ability to be steered in-context toward perspectives it was not trained to favor. In controlled experiments, we fine-tune models toward one side of cultural-value disagreements and evaluate checkpoints throughout training. The trained side becomes increasingly dominant in ordinary use, while the ability to recognize and faithfully enact the opposing view declines. These findings point to a tension between prioritizing a single set of values and preserving the technical capacity needed to serve diverse stakeholders. Finally, we propose and analyze an alternative objective that maximizes reward subject to a prescribed distribution over expressed perspectives, and present stance-distribution matching as a practical implementation.

### 中文一句话结论
后训练在使模型偏向特定价值观的同时，会显著削弱其根据上下文信息忠实表达对立观点的能力，凸显了价值对齐与多视角服务能力之间的根本矛盾。

### English TL;DR
Post-training large language models toward a specific perspective not only biases their default outputs but also reduces their ability to be steered in-context toward opposing views, highlighting a tension between value alignment and preserving steerability for diverse stakeholders.

### 中文详细总结
该研究探讨了后训练（post-training）对大型语言模型多视角服务能力的负面影响。此前工作主要关注后训练导致的默认输出偏向，本文则聚焦于模型对上下文信息的自适应能力。通过控制实验，作者将模型微调至文化价值分歧的某一方，并在训练过程中评估检查点。结果发现：（1）模型在普通使用中越来越倾向于输出训练方观点；（2）模型识别并忠实执行对立观点的能力持续下降。这表明优先单一价值会牺牲模型为多样化用户提供服务的技术能力。最后，作者提出一个替代优化目标：在给定表达视角分布的前提下最大化奖励，并给出了“立场分布匹配”这一实用实现方案。

### 方法 / 贡献
- **实验方法**：在文化价值分歧场景下对语言模型进行有监督微调，使其偏向某一方观点；沿训练时间步采样检查点，评估默认输出分布和上下文引导下的输出一致性。
- **理论贡献**：揭示了“默认崩溃”（default collapse）现象不仅体现在输出偏向上，还表现为上下文可控性的丧失。
- **技术贡献**：提出替代优化目标——在预设的立场分布约束下最大化奖励，并设计了“立场分布匹配”算法作为具体实现。

### 实验或数据
论文使用了控制实验：选取一组具有文化价值分歧的问题，将模型微调至其中一方立场。训练过程中定期保存检查点，并测试模型在无上下文和有上下文两种情况下的输出偏向。实验记录了训练方观点的默认输出概率提升，以及模型在收到对立立场提示时正确执行该立场的比例下降趋势。未报告具体数据集名称，但实验基于作者构建的文化价值分歧样本集。

### 值得关注点
- 挑战了“后训练仅改变默认输出”的既有认知，证明可控性也随之退化。
- 提出的立场分布匹配为多价值观服务提供了可操作的技术路径。
- 研究突出了价值对齐与模型能力通用性之间需要审慎权衡。

### 局限性
作者未在摘要中明确讨论局限性。实验基于特定的文化价值分歧和模型框架，结论是否适用于其他领域（如政治、伦理）或更复杂的语境（如多轮对话）尚需验证。此外，立场分布匹配方法在实际部署中的效果和鲁棒性有待进一步实验。

## 10. Constraint-Aware Training

- Source: arxiv
- arXiv ID: 2610.02909
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2610.02909v1
- PDF: https://arxiv.org/pdf/2610.02909v1
- DOI: https://doi.org/10.48550/arXiv.2610.02909

### Authors

Jinwoo Kim

### Abstract

When generating programs with language models, constrained decoding can apply program analyses to exclude tokens that violate syntax, scope, or typing rules. However, there is a duplication: standard training already teaches the model to suppress the tokens rejected by these analyses. This duplication leads to the question: if we will perform some analysis to filter a set tokens out during inference anyways, can we avoid teaching the model the said analysis altogether during training, and does this externalization lead to more efficient models? This paper defines a general constraint-aware objective satisfying this externalization desideratum and formalizes the benefits of externalization into three concrete theorems about model size and data efficiency. We show, through a controlled synthetic experiment, that the theorems survive training dynamics: constraint-aware training yields lower prediction loss at a matched parameter count and data compared to ordinary cross-entropy training, motivating training objectives that incorporate the analyses used during generation.

### 中文一句话结论
约束感知训练通过将推理时约束解码所用的程序分析外置到训练目标中，在相同参数量和训练数据下取得了比标准交叉熵训练更低的预测损失。

### English TL;DR
Constraint-aware training shows that when inference-time constrained decoding will filter tokens anyway, training can intentionally externalize that analysis, yielding lower prediction loss at matched parameter count and data than standard cross-entropy training.

### 中文详细总结
该论文关注语言模型生成程序时的约束解码问题。约束解码会利用程序分析在推理时过滤掉违反语法、作用域或类型规则的 token，但标准训练已经教会模型抑制这些 token，因此存在重复学习。作者提出约束感知训练（Constraint-Aware Training），在训练目标中显式地将“会被分析过滤掉的 token”外置（externalize），避免模型重复学习这些规则。论文形式化定义了满足该外置需求的一般性目标，并提出了三个关于模型大小和数据效率的定理，从理论上证明外置分析能够带来收益。通过受控合成实验，作者验证了这些定理在实际训练动态中成立：在相同参数量和训练数据下，约束感知训练比普通交叉熵训练的预测损失更低，从而激励在训练目标中纳入生成时所用的分析。

### 方法 / 贡献
- 提出约束感知训练目标，实现“外置”推理时程序分析的需求。
- 形式化外置收益，给出三个定理，分别关联模型规模与数据效率。
- 通过受控合成实验验证训练动态下理论预测：匹配参数量和数据量时，预测损失低于标准交叉熵训练。
- 主张训练目标应纳入生成时使用的分析，而非仅依赖模型隐式学习。

### 实验或数据
摘要仅报告了一个受控合成实验。结果表明，在相同参数量和训练数据下，约束感知训练相比普通交叉熵训练实现了更低的预测损失。摘要未提及真实程序生成基准或具体数据集。

### 值得关注点
- 核心洞察是训练与推理之间关于约束分析的“重复”问题，并将该分析从模型隐式学习中显式外部化。
- 理论上用三个定理形式化了外部化对模型大小和数据效率的收益。
- 实验结果虽为合成设置，但为“训练即外部化”这一方向提供了初步证据，可能启发后续将静态分析融入训练目标的生成模型方法。

### 局限性
摘要未讨论明显局限性。需要注意的是，实验仅在受控合成环境下进行，真实世界程序生成任务中的泛化效果尚未得到验证。

## Processing Notes

- Duplicate papers skipped: 0