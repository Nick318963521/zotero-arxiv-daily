# Daily arXiv - 2026-08-29

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-29T04:06:08
- Paper count: 10

## 1. VFA: Empowering Multilingual MLLMs via Vision-Free Adaptation

- Source: arxiv
- arXiv ID: 2608.26155
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.26155v1
- PDF: https://arxiv.org/pdf/2608.26155v1
- DOI: https://doi.org/10.48550/arXiv.2608.26155

### Authors

Yixia Li, Yaqing Shi, Zhiwen Ruan, Dongdong Zhang, Lingjie Jiang, Shaohan Huang, Yun Chen, Guanhua Chen, Furu Wei

### Abstract

Multimodal large language models have advanced rapidly, yet most remain English-centric, as scaling multilingual multimodal instruction tuning is limited by the scarcity and high cost of high-quality non-English image-text supervision. Although multilingual text data is abundant, naive textual fine-tuning can disrupt vision-language alignment and induce catastrophic forgetting. We propose Vision-Free Adaptation (VFA), a framework that decouples multilingual language enhancement from visual alignment by composing complementary task vectors over a shared LLM backbone. Specifically, we fine-tune a base LLM on multilingual text data to derive a multilingual task vector, which is then merged with the vision-aligned task vector of an MLLM. Experiments on five MLLMs across six multilingual multimodal benchmarks show consistent improvements while preserving both general multimodal and text-only capabilities. Moreover, using less than 2% of the text data, VFA narrows the gap to the fully multimodal-trained model, demonstrating its data efficiency.

### 中文一句话结论  
VFA 通过任务向量解耦多语言文本增强与视觉对齐，仅用少量纯文本数据即可显著提升多语言多模态大模型的跨语言能力，同时保持通用多模态和纯语言性能。

### English TL;DR  
Vision-Free Adaptation (VFA) improves multilingual MLLMs by composing a multilingual task vector (from text-only fine-tuning) with the vision-aligned task vector of the base LLM, eliminating the need for costly non-English image-text pairs. Experiments on five MLLMs and six benchmarks show consistent gains (+2.99 avg on LLaVA-OneVision-8B) with less than 2% of the text data needed for full multimodal training.

### 中文详细总结  
当前多模态大语言模型（MLLM）大多以英语为中心，多语言多模态指令调优受限于高质量非英语图像-文本数据的稀缺和高成本。虽然多语言文本数据丰富，但直接对 MLLM 进行纯文本微调会破坏视觉-语言对齐并导致灾难性遗忘。为此，本文提出 Vision-Free Adaptation (VFA) 框架，将多语言增强与视觉对齐解耦。VFA 首先在基础 LLM 上进行多语言文本微调，得到多语言任务向量；随后将该向量与 MLLM 的视觉对齐任务向量合并（通过加权平均、任务算术或 TIES 合并），视觉编码器和投影模块保持冻结。实验在 5 种 MLLM（含 LLaVA-OneVision、Qwen3-VL 等）和 6 个多语言多模态基准（MaXM、xGQA、xMMMU、XM100、MaRVL、M3Exam）上进行，VFA 一致提升多语言性能（如 LLaVA-OneVision-8B 平均提升 +2.99），同时通用多模态和纯语言能力几乎不受影响。仅使用 100K 文本样本即可缩小与基于数百万图像-文本对训练的模型之间的差距，体现高效数据利用。

### 方法 / 贡献  
- **任务向量解耦框架**：将多语言增强和视觉对齐视为独立任务向量，避免直接微调 MLLM 导致的模态干扰。  
- **两阶段流程**：阶段1在基础 LLM 上用纯文本数据微导得多语言任务向量 $\tau_{\text{multi}}$；阶段2将 $\tau_{\text{multi}}$ 与 MLLM 的视觉对齐任务向量合并（权重平均、任务算术或 TIES），视觉模块冻结。  
- **可复用性**：当多个 MLLM 共享相同 LLM 主干时，多语言任务向量可一次训练、多次合并，降低训练成本。  
- **零推理开销**：合并后模型无额外延迟或内存增加。

### 实验或数据  
- **模型**：5 个 MLLM（包括 LLaVA-OneVision-1.5 的 8B/4B、Qwen3-VL、Idefics3-8B 等），覆盖不同规模和家族。  
- **基准**：6 个多语言多模态基准（MaXM、xGQA、xMMMU、XM100、MaRVL、M3Exam），以及通用多模态（OCRBench、MMBench、MMMU、MathVista）和纯语言基准（TyDiQA、MMMLU、XNLI 等）。  
- **数据**：仅使用 100K 多语言文本样本（不到完整多模态训练数据的 2%）。  
- **结果**：LLaVA-OneVision-1.5-8B 平均提升 +2.99；4B 提升 +0.57；各模型一致提升，且通用能力基本保持。

### 值得关注点  
1. **数据效率**：仅用 100K 纯文本样本即可显著缩小与全多模态训练模型的多语言能力差距。  
2. **无需非英语图像-文本对**：避免了高成本、不均衡的多语言多模态数据收集。  
3. **保持视觉对齐**：通过冻结视觉模块和任务向量合并，避免了传统文本微调导致的灾难性遗忘。  
4. **通用性**：在多个不同架构和规模的 MLLM 上验证，且合并方法灵活（WA/TA/TIES）。  
5. **零额外推理成本**：合并后模型与原始 MLLM 结构一致，无延迟增加。

### 局限性  
- **依赖基础 LLM 的多语言先验能力**：VFA 提升幅度受限于基础 LLM 本身的多语言掌握程度，对低资源语言可能效果有限。  
- **合并超参数敏感**：不同合并方法（WA、TA、TIES）及其混合系数 $\alpha$ 需手动调节，可能影响视觉-语言平衡。  
- **未评估真实长尾文化场景**：基准覆盖了常见多语言任务，但缺乏对特定文化视觉概念的细粒度评价。  
- **仅验证了基于 LLM 的任务向量合并**：对于视觉编码器与 LLM 深度耦合的架构（如多模态专家混合），适用性尚待研究。

## 2. Leveraging Large Language Models for Systematic Literature Review of Disease Spread Models

- Source: arxiv
- arXiv ID: 2608.26150
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.26150v1
- PDF: https://arxiv.org/pdf/2608.26150v1
- DOI: https://doi.org/10.48550/arXiv.2608.26150

### Authors

Orhan Yagizer Cinar, Timur Emre Ozkose, Emma Von Hoene, Amira Roess, Taylor Anderson, Hamdi Kavak

### Abstract

Recent advancements in Large Language Models (LLMs) have created new opportunities to streamline and potentially automate many research processes, including systematic literature reviews (SLRs). This study reports an LLM pipeline development for extracting model-relevant information from 536 peer-reviewed agent-based modeling papers. We compare the results with those of a human-conducted SLR. Our results show paper-level accuracies of approximately 77.95% for GPT-4.1 and 81.67% for GPT-5.0. Field-level accuracy ranges from 32.40% to 100.00%, with more complex or subjective fields performing less reliably. Importantly, we find that agreement between LLMs is a potential indicator of output quality: low agreement may signal hallucinations, whereas high agreement combined with low accuracy may point to noise or errors in the human dataset. Overall, our study provides practical insights into prompt development and highlights both the potential and limitations of using LLMs for full-scale SLRs in the modeling and simulation domain.

### 中文一句话结论
本研究利用GPT-4.1和GPT-5.0对536篇疾病传播代理模型论文进行系统性文献综述数据提取，论文级准确率分别达77.95%和81.67%，但字段级准确率波动较大，表明LLM在文献综述中既具潜力也存在局限性。

### English TL;DR
This study evaluates LLM-based data extraction for systematic literature reviews of agent-based disease spread models, comparing GPT-4.1 and GPT-5.0 outputs against a human-annotated dataset of 536 papers. Paper-level accuracies (~78-82%) are promising, but field-level accuracy varies widely (32-100%), with complex/subjective fields less reliable. Inter-LLM disagreement may signal hallucinations, while high disagreement with low accuracy could reflect human dataset errors. The work provides practical insights and highlights both potential and limitations for automating full-scale SLRs in modeling and simulation.

### 中文详细总结
本研究开发了一个全自动的大语言模型（LLM）流水线，用于从536篇经过同行评审的COVID-19代理模型（ABM）论文中提取结构化信息，并将结果与人类专家进行的系统性文献综述（SLR）数据进行比较。研究使用了GPT-4.1和GPT-5.0（通过OpenAI API，零样本设置），对每篇论文提取21个字段（包括二元变量和半结构化证据）。结果显示：论文级准确率GPT-4.1约77.95%，GPT-5.0约81.67%；字段级准确率范围从32.40%到100%，其中复杂或主观性字段（如模型验证、不确定性报告）表现较差。LLM之间的一致性可作为输出质量的潜在指标：低一致性可能提示幻觉，高一致性但低准确率则可能反映人类基准数据中的噪声或错误。流水线包括准备、提示设计、LLM提取、输出验证和评估步骤，全程通过API实现可重复性。该研究是建模与仿真领域规模最大的LLM数据提取评估之一，为未来自动化文献综述提供了实践指导。

### 方法 / 贡献
- **方法**：构建了一个从PDF全文到结构化JSON输出的自动化LLM流水线，使用GPT-4.1和GPT-5.0零样本API调用，对536篇COVID-19 ABM论文进行数据提取。流水线包含准备（人类参考数据集）、提示设计（严格限定输出格式和分类选项）、LLM提取、输出验证（规则修复+辅助LLM恢复）和评估（Jaccard指数和重叠系数）。
- **贡献**：（1）首次在大规模（N=536）建模与仿真领域评估LLM用于SLR数据提取的性能；（2）揭示了字段级准确率差异及LLM一致性的诊断价值；（3）提供了可复现的管道设计和提示工程实践经验。

### 实验或数据
- **数据**：536篇COVID-19代理模型论文（2020-2023年发表），人类参考数据集来自一项已完成的一年期系统性文献综述（由双人独立提取+共识生成，平均人-人一致率74%），包含21个字段（二元变量和文本证据）。
- **实验**：分别用GPT-4.1和GPT-5.0处理所有论文，每篇通过一次API调用完成提取。结果与人类基准逐字段比较，报告论文级和字段级准确率。另计算了两种LLM输出之间的一致性与准确率的关系。

### 值得关注点
- **规模**：是目前SLR数据提取研究中样本量最大（536篇）的之一，且针对的是建模与仿真领域而非临床医学。
- **方法创新**：使用程序化API而非网页界面，提高了可重复性；通过比较LLM间一致性发现潜在幻觉或数据噪声问题。
- **实用经验**：提示设计需严格限定输出格式；复杂/主观字段（如模型评估、不确定性）准确率低；少量模型参数（temperature=1.0, top_p=1.0）下输出方差仍可管理。

### 局限性
- 仅使用零样本设置，未尝试微调或少样本提示，可能未达到最佳性能。
- 未进行多次重复运行以量化采样方差。
- 字段级准确率波动大（32%-100%），部分复杂字段（如“是否报告不确定性”）可靠性不足，可能限制实际应用。
- LLM间低一致性与幻觉的关联需进一步验证；高一致但低准确率提示人类数据可能包含噪声，但本研究未深入分析。
- 研究仅限于COVID-19 ABM论文，结论推广至其他领域或模型类型需谨慎。

## 3. Why Current XAI Is Not Enough for Arabic NLP: A Critical Survey of the Explainability Gap

- Source: arxiv
- arXiv ID: 2608.26144
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.26144v1
- PDF: https://arxiv.org/pdf/2608.26144v1
- DOI: https://doi.org/10.48550/arXiv.2608.26144

### Authors

Salima Lamsiyah, Ruslan Mitkov

### Abstract

Explainable AI (XAI) is now a major theme in NLP; however, Arabic NLP remains under-explained in three connected senses. First, there is a method gap: Arabic XAI relies heavily on a small set of post-hoc techniques such as LIME, SHAP, attention visualization, and saliency, while broader NLP XAI offers richer diagnostic, counterfactual, probing, rationale-based, and human-centered methods. Second, there is a task gap: existing Arabic XAI work is concentrated in classification tasks, especially sentiment analysis, hate/offensive language detection, fake news, and spam, with weaker coverage of generation, retrieval, translation, summarization, structured prediction, and dialogue. Third, there is a linguistic gap: many explanations identify influential tokens, but rarely explain Arabic-specific phenomena such as morphology, clitics, dialectal variation, diglossia, orthographic ambiguity, diacritics, code-switching, named entities, cultural references, or Classical and religious registers. This critical structured survey synthesizes the reviewed literature on Arabic XAI across text, speech, and multimodal settings. We argue that Arabic NLP does not only need explanations of model decisions; it needs explanations that are faithful to Arabic as a linguistic, cultural, and sociotechnical object. We introduce a taxonomy of tasks, methods, linguistic units, varieties, goals, and evaluation practices, and propose a research agenda for linguistically grounded Arabic XAI.

### 中文一句话结论
当前阿拉伯语自然语言处理中的可解释人工智能严重不足，主要体现为方法局限、任务单一和缺乏语言学深度，无法忠实反映阿拉伯语的语言、文化和社会技术特征。

### English TL;DR
This paper identifies a critical explainability gap in Arabic NLP, showing that current XAI methods are insufficient because they rely on narrow post-hoc techniques, focus predominantly on classification tasks, and fail to account for Arabic-specific linguistic, cultural, and sociotechnical features.

### 中文详细总结
本文系统分析了阿拉伯语自然语言处理中的“可解释性鸿沟”。作者指出，当前阿拉伯语可解释人工智能存在三个相互关联的缺失：第一，**方法缺失**——研究过度依赖LIME、SHAP、注意力可视化和显著性等少数事后解释技术，而更丰富的诊断、反事实、探究、理由和以人为中心的方法几乎未被采用；第二，**任务缺失**——绝大多数研究集中在情感分析、仇恨言论检测、假新闻和垃圾邮件等分类任务上，对生成、检索、翻译、摘要、结构化预测和对话等任务覆盖薄弱；第三，**语言缺失**——解释多停留在词元层面，很少涉及阿拉伯语特有的形态学、附着词、方言变体、双言现象、正字法歧义、变音符、语码转换、专有名词、文化指涉及古典/宗教语体等核心语言学现象。

作者进一步提出，解释应涵盖四个层次：预测层面、模型层面、语言学层面和社会文化层面，并构建了一个涵盖任务、方法、语言学单元、语言变体、解释目标和评估实践的批判性分类体系。综述强调，阿拉伯语NLP需要的不仅是模型决策的解释，更是对阿拉伯语作为语言、文化和社会技术对象的忠实阐释。

### 方法 / 贡献
本文的核心贡献包括：
1. 系统界定了阿拉伯语可解释人工智能的“方法-任务-语言”三重鸿沟；
2. 提出了针对阿拉伯语NLP的四层次解释框架（预测级、模型级、语言学级、社会文化级）；
3. 建立了包含任务、方法、语言学单元、变体、目标和评估实践的分类体系，并以覆盖表形式可视化当前研究与实践的差距；
4. 提出了面向语言学基础的阿拉伯语可解释人工智能的研究议程。

### 实验或数据
本文为批判性综述论文，未开展新的实验或数据集构建工作。其分析基于对现有阿拉伯语可解释人工智能文献的系统梳理，涵盖文本、语音和多模态场景。

### 值得关注点
- 解释了为何通用的可解释性方法在阿拉伯语上容易产生误导（如词级归因无法揭示形态、方言或变音符的作用）；
- 明确提出“忠实于阿拉伯语”应成为评估标准，而非仅追求视觉上合理的解释；
- 指出现有工作往往模糊了面向用户、开发者、语言学专家和社群的不同解释目标；
- 覆盖了古典/宗教阿拉伯语、阿拉伯语方言、Arabizi等特殊语言变体的可解释性需求。

### 局限性
- 作为综述论文，未提供实验验证或量化评估解释方法的有效性；
- 综述范围主要限于已发表的英文和部分阿拉伯语文献，可能存在发表偏倚；
- 所提研究议程尚未在具体系统或评估基准中得到实践验证；
- 对多模态（语音、图像结合文本）场景的覆盖相对有限。

## 4. AffectOmni: RL-Verifiable People-Centric Grounded Affective Reasoning for Social and Art-Related Scenes

- Source: arxiv
- arXiv ID: 2608.26193
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.26193v1
- PDF: https://arxiv.org/pdf/2608.26193v1
- DOI: https://doi.org/10.48550/arXiv.2608.26193

### Authors

Yibo Wang, Rui Yang, Jisheng Dang, Bimei Wang, Yitao Wu, Pengfei Cao, Wencan Zhang, Hong Peng, Bin Hu, Tat-Seng Chua

### Abstract

Multimodal large language models (MLLMs) achieve strong performance on VQA and scene understanding, yet affective reasoning remains vulnerable to shortcut behavior. Models may predict correct answers while neglecting people-centric cues such as micro expressions and body language, which weakens traceability and external verification. Prior reinforcement learning approaches mainly reward context or logical coherence without explicitly enforcing attention to human evidence. In addition, LLM as a Judge scoring often suffers from score clustering, which reduces reward discriminability. We propose AffectOmni, a GRPO trained framework for verifiable affective reasoning. AffectOmni introduces People Focus and Temporal Order rewards to encourage people-centric evidence selection and temporally structured reasoning, and it adopts within-group comparative scoring to produce more stable and discriminative reward signals. For verification, a Thinking Summarizer converts free form rationales into executable evidence instructions, which are grounded into pixel level evidence regions via SAM3 to provide an externally auditable interface outside the training loop. Experiments on IntentBench, Daily Omni, and WorldSense show consistent improvements over open source 7B scale baselines, including gains of 4.66% on emotion recognition and +14.29% on temporally sensitive tasks. Code is available at https://github.com/eliot127825-rgb/AffectOmni_nobody.

### 中文一句话结论
本文提出AffectOmni框架，通过基于GRPO的训练、以人为中心的奖励信号和组内比较评分，实现了情感推理的可验证性和可追溯性。

### English TL;DR
AffectOmni introduces a GRPO-trained framework with people-centric rewards (People Focus and Temporal Order) and within-group comparative scoring to enforce traceable, verifiable affective reasoning by grounding multimodal evidence into pixel-level regions, achieving consistent improvements on social and art-related benchmarks.

### 中文详细总结
多模态大语言模型（MLLMs）在VQA和场景理解上表现优异，但在情感推理中易出现“捷径行为”，即忽略以人为中心的线索（如微表情、肢体语言），导致推理过程无法追踪和外部验证。现有强化学习方法主要奖励上下文或逻辑一致性，未明确强制关注人类证据；且LLM作为裁判的评分常出现分数聚类问题，降低奖励区分度。

为解决上述问题，本文提出AffectOmni框架，基于Group Relative Policy Optimization（GRPO）训练。其核心贡献包括：
1. **以人为中心的精细奖励设计**：引入“人关注奖励”（People Focus Reward）和“时序奖励”（Temporal Order Reward），鼓励模型关注微表情、肢体语言等人相关线索，并按时间顺序组织推理。
2. **组内比较评分策略**：在GRPO训练中，对同一输入生成的多个候选响应进行组内相对比较，而非独立绝对评分，从而缓解校准漂移和分数聚类，提供更稳定且有区分度的优化信号。
3. **推理→证据的接地验证机制**：通过“思考总结器”（Thinking Summarizer）将自由形式的推理链压缩为可执行的证据指令，再经由SAM3接地到像素级证据区域，为训练循环外的外部审计提供接口。

实验在IntentBench、Daily Omni和WorldSense三个基准上验证，在7B规模开源模型中取得一致提升，其中情绪识别提升4.66%，时序敏感任务提升14.29%。

### 方法 / 贡献
- **方法**：基于GRPO框架，对每个输入采样G个候选响应，计算组内相对优势进行策略更新。总奖励由格式奖励、准确奖励、人关注奖励和时序奖励组成。
- **贡献1**：首次提出面向情感推理的“推理→证据接地”范式，将推理链压缩为最小证据包，进而接地到像素级区域，实现外部可审计。
- **贡献2**：设计以人为中心的精细奖励（人关注奖励评估面部表情、身体运动、人际互动；时序奖励评估时间标记使用和情感轨迹时序连贯性），引导模型学习可追溯的推理模式。
- **贡献3**：提出组内比较评分策略，替代独立绝对评分，通过相对排名提供更稳定、更具区分度的奖励信号。

### 实验或数据
实验在三个基准上进行：IntentBench、Daily Omni和WorldSense。与开源7B规模基线模型比较，情绪识别任务提升4.66%，时序敏感任务提升14.29%。未提及额外的数据集构建细节。

### 值得关注点
- 首次将GRPO应用于情感推理领域，并设计专门针对情感线索的奖励函数，区别于以往仅关注上下文或逻辑一致性的方法。
- 组内比较评分策略有效缓解了LLM作为裁判时的分数聚类问题，提高了奖励区分度。
- 推理→证据接地机制提供了一种外部可审计的验证接口，增强了模型推理的可信度和可解释性。
- 代码已开源（https://github.com/eliot127825-rgb/AffectOmni_nobody），便于复现和扩展。

### 局限性
- 奖励函数（人关注和时序）的设计依赖于任务特定的评判标准，对于新任务需替换判别提示语，可能增加迁移成本。
- 实验仅在7B规模模型上验证，更大规模模型上的效果和泛化能力未探讨。
- 接地验证机制依赖于SAM3的像素级分割能力，其准确性和效率可能受限于分割模型本身。
- 未讨论在开放域或未见情感类别上的表现。

## 5. Syntax vs. Semantics: How Transformers Learn Deep Dependencies

- Source: arxiv
- arXiv ID: 2608.26139
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.26139v1
- PDF: https://arxiv.org/pdf/2608.26139v1
- DOI: https://doi.org/10.48550/arXiv.2608.26139

### Authors

Jiangrui Zhao, Xiaoting Du

### Abstract

Large Language Models demonstrate remarkable syntactic fluency, yet the optimization dynamics governing their acquisition of deep semantic dependencies remain poorly understood. We propose a mechanistic framework that models this learning process as a competition between Surface Statistics and Deep Semantics. Our theoretical analysis identifies a ``Gradient Starvation" phenomenon where the error signals for sparse semantic dependencies are actively suppressed during early optimization. This suppression impedes the learning of structural reasoning and causes its emergence to manifest as a sudden phase transition. Furthermore, this framework offers a mechanistic basis for the effectiveness of Chain-of-Thought (CoT) strategies. By externalizing intermediate reasoning steps into concrete tokens, CoT effectively bypasses the suppression regime inherent to implicit reasoning. We validate these findings across scales ranging from toy transformers to production models (Llama-3.1-8B, Qwen2.5-Coder-7B). Finally, guided by this theory, we propose a topology-aligned contrastive objective that explicitly rectifies the gradient geometry. Experiments on variable binding tasks demonstrate that our method achieves an improvement that is over 2x larger than that obtained via standard cross-entropy fine-tuning.

### 中文一句话结论
本文提出一个机制框架，将 Transformer 学习深层语义依赖的过程视为“表层统计（语法）”与“深层语义”之间的竞争，发现早期优化中语义梯度会被“梯度饥饿”效应压制，直到发生突然的相变；这解释了思维链（CoT）的有效性，并据此提出一种拓扑对齐对比目标，在变量绑定任务上取得超过标准交叉熵微调 2 倍以上的提升。

### English TL;DR
This paper introduces a mechanistic framework showing that transformers learn semantic dependencies through a "Gradient Starvation" competition with surface-level syntax, where semantic learning is suppressed until a sudden phase transition—explaining why Chain-of-Thought reasoning and a proposed topology-aligned contrastive objective can bypass this suppression to significantly improve deep dependency learning.

### 中文详细总结
作者将训练过程建模为“表层统计”与“深层语义”的竞争。理论分析指出，语法相关的高曲率梯度在早期主导优化，导致稀疏语义依赖的误差信号被主动抑制，这种现象被称为“Gradient Starvation”。这种抑制使结构推理能力的学习受阻，并使其出现方式表现为突然的相变。该框架也为 Chain-of-Thought 提供了机制解释：通过将中间推理步骤外化为具体 token，CoT 改变了梯度几何，绕过了隐式推理固有的抑制区间。作者在玩具模型到生产级模型（Llama-3.1-8B、Qwen2.5-Coder-7B）上验证了这些动态，并提出一种拓扑对齐对比目标来显式修正梯度几何；在变量绑定任务上，该方法比标准交叉熵微调获得超过 2 倍的改进。

### 方法 / 贡献
- 提出“表层统计 vs. 深层语义”的竞争机制框架，解释深层依赖学习的动力学。
- 理论分析揭示“Gradient Starvation”：高曲率语法特征抑制低曲率语义梯度。
- 证明 softmax 饱和会导致语义梯度的“消失梯度屏障”，从而产生阶段性相变。
- 为 Chain-of-Thought 有效性提供因果机制解释（外化中间步骤可绕过梯度抑制）。
- 提出拓扑对齐对比目标（topology-aligned contrastive objective），直接修正梯度几何。

### 实验或数据
- 验证范围从玩具 Transformer 到生产级模型：Llama-3.1-8B、Qwen2.5-Coder-7B。
- 使用源代码与抽象语法树（AST）作为语义拓扑的可控代理，用于追踪依赖电路的出现。
- 实验涵盖中间检查点（如 Pythia）以及变量绑定任务。
- 方法在变量绑定任务上的提升超过标准交叉熵微调的 2 倍。
- 论文提及代码将公开：https://github.com/jr-zhao/Deep-Dependencies/tree/main

### 值得关注点
- “Gradient Starvation”与“突然相变”为深层依赖涌现提供了一种优化动力学解释，而非单纯归因于架构。
- 该框架统一解释了 CoT 为何有效：通过外部化推理步骤改变学习几何。
- 提出的对比目标不是依赖更多数据，而是从梯度层面直接干预，具有理论指导性。
- 实验跨越小规模到 7B/8B 量级模型，增强了结论的可信度。

### 局限性
摘要未明确讨论局限性。现有信息显示，实验主要基于代码/AST 代理任务和变量绑定任务；自然语言中更复杂的深层语义依赖是否同样适用、以及该机制在更多样化任务上的泛化能力，仍需进一步验证。

## 6. GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL

- Source: arxiv
- arXiv ID: 2608.27142
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.27142v1
- PDF: https://arxiv.org/pdf/2608.27142v1
- DOI: https://doi.org/10.48550/arXiv.2608.27142

### Authors

Zike Yuan, Han Zhang, Jianzhi Yan, Le Liu, Cai Ke, Huozhi Zhou, Jian Xie, Jiran Yin, Yukun Cao, Yue Yu, Hui Wang, Ming Liu, Bing Qin

### Abstract

Despite their potential in standardized graph tasks, Large Language Models (LLMs) remain brittle to real-world shifts in node identifiers and task formulation. While deterministic graph tools are invariant to such shifts, extracting topological structures from noisy text is highly fragile for LLMs, which often overfit to surface patterns. Moreover, mitigating these parsing failures via multi-agent systems incurs prohibitive latency. To address this, we propose GRAIN, a single-agent framework optimized via reinforcement learning. GRAIN models reasoning as a semantic parsing and tool-execution pipeline, guided by a Structure Invariance Reward. By validating extracted intermediate graphs against ground-truth topologies, this reward forces the LLM to learn robust text-to-structure mappings rather than memorizing linguistic artifacts. We also introduce GRIT, a benchmark evaluating sensitivity to such linguistic shifts. GRAIN outperforms multi-agent baselines by 16.45\% in accuracy with approximately 24\% lower latency. Furthermore, it demonstrates superior structural generalization, halving the out-of-distribution (OOD) gap of SFT models (from 15.77\% to 7.80\%) and maintaining robustness on large-scale graphs beyond the training distribution.

### 中文一句话结论
GRAIN 是一个基于强化学习的单智能体框架，通过结构不变性奖励，使大模型在节点名称和任务表述变化时仍能鲁棒地解析图结构，显著优于多智能体方法并降低延迟。

### English TL;DR
GRAIN is a single-agent reinforcement learning framework that uses a structure invariance reward to train LLMs to robustly parse noisy real-world text into accurate graph structures, achieving superior accuracy and lower latency compared to multi-agent systems while significantly reducing performance gaps caused by shifts in node names and task formulations.

### 中文详细总结
大型语言模型（LLMs）虽然在标准图任务上展现出潜力，但在面对现实世界中节点标识符变化和任务表述扰动时非常脆弱。传统的确定性图工具对此类变化不敏感，但LLMs从含噪文本中提取拓扑结构时容易过拟合表面模式。现有通过多智能体系统缓解解析失败的方法会带来高昂的延迟成本。为此，本文提出 **GRAIN**，一个通过强化学习优化的单智能体框架。GRAIN 将推理建模为语义解析与工具执行的流水线，并由 **结构不变性奖励** 引导。该奖励通过将提取的中间图与真实拓扑进行比对，迫使LLM学习稳健的文本到结构映射，而非记忆语言伪影。同时，本文引入 **GRIT 基准**，用于评估模型对这类语言变化的敏感性。实验表明，GRAIN 在准确率上超过多智能体基线16.45%，且延迟降低约24%。在分布外泛化方面，GRAIN 将监督微调模型的性能差距从15.77%减半至7.80%，并在超出训练分布的大规模图上保持鲁棒性。

### 方法 / 贡献
- **GRAIN框架**：一个单智能体的RL框架。它将LLM建模为“语言→图→工具”的智能体，输出包含思考、中间图表示、工具调用和最终答案的结构化序列。
- **结构不变性奖励**：通过验证模型生成的中间图（IR）是否与真实图拓扑同构，强制模型学习不变的结构规则，而非记忆表面标签或表述。
- **单智能体高效推理**：将多智能体系统的复杂协作能力蒸馏到单个模型权重中，兼具高准确率和低延迟。
- **GRIT基准**：一个多任务、多视角的图推理数据集，涵盖6种图问题、31个现实场景，并针对标识符（4种命名方案）和任务形式（标准 vs. 叙事）提供了可控的分布外测试集。

### 实验或数据
- **GRIT数据集**：训练集包含2160张图、17280个问题；测试集包含360张图、2760个问题；大型测试集（节点数40-60）包含120张图、960个问题；OOD测试集（未见过的场景）包含180张图、1440个问题。数据通过确定性模板生成，确保100%的拓扑正确性。
- **主要结果**：
  - GRAIN在准确率上超越多智能体基线16.45%，延迟降低约24%。
  - 在分布外泛化上，GRAIN将SFT模型的OOD性能差距从15.77%缩小到7.80%。
  - GRAIN在大规模图（节点数40-60）上仍保持鲁棒性。
- **消融实验**（论文中已有初步分析）：突出了结构奖励和多样化训练对于鲁棒性的重要性。

### 值得关注点
- **问题重大**：该工作精准定位了LLM在图推理中因表面形式变化而产生性能波动的关键问题，并通过可控实验量化了这一脆弱性。
- **方法简洁高效**：用结构不变性奖励作为RL信号，替代了复杂的多智能体协作，实现了性能与效率的双赢，思路清晰且实用。
- **基准设计严谨**：GRIT采用因子化设计，将标识符变化（4种方案）和任务形式变化（2种）交叉组合，并包含严格的OOD评估，有力支撑了鲁棒性评估。
- **代码与数据开源**：论文承诺开源GRAIN框架与GRIT基准。

### 局限性
- **任务类型依赖**：GRAIN目前仅支持节点/边级图任务，对于需要更复杂语义理解的查询（如涉及节点属性）的泛化能力未作验证。
- **RL训练稳定性**：论文未详细讨论RL训练的收敛性与调参难度，大规模图上RL的稳定性可能是一个潜在挑战。
- **新增基准的计算开销**：GRIT基准本身构建较为复杂，可能对后续研究者复现或扩展造成一定门槛。
- **未见复杂推理链评估**：虽然GRAIN在分布外场景上表现良好，但论文未评估其对完全未见过的推理范式（如反向推理或动态图）的泛化能力。

## 7. SPT: Skills as Pre-Training Data for Agentic Language Models

- Source: arxiv
- arXiv ID: 2608.26563
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.26563v1
- PDF: https://arxiv.org/pdf/2608.26563v1
- DOI: https://doi.org/10.48550/arXiv.2608.26563

### Authors

Yufei Sun, Yudong Li, Yiming Cheng

### Abstract

Agentic (tool-using) language models are mainly trained on tool-call traces and agent trajectories during post-training. These data provide direct behavioral supervision, but producing them requires task environments, execution, and verification, making broad tool and task coverage expensive. Publicly available skills offer another source of training data: they encode reusable tool semantics and workflows but are typically used only as inference-time context. We introduce Skill Pre-Training (SPT), a mid-training method that applies causal language modeling to SkillCorpus, a collection of public multi-file skill packages, optionally mixed with general data. To preserve relations among files within each package, we also introduce Reference Insert, a reference-aware assembly strategy that places supporting files near their mentions in the primary instruction. Experiments across multiple model scales and post-training recipes show that SPT consistently improves agentic performance over mid-training on general or trajectory data, while largely preserving general performance. Data mixture experiments show additional benefits from combining skill data with general annealing corpora. These results indicate that skill packages are a valuable data source for pre-training agentic language models.

### 中文一句话结论
本文提出“技能预训练”（SPT），通过将公开的多文件技能包作为中训练数据（配以引用插入策略），在保持通用能力的同时显著提升语言模型的智能体（工具调用）性能。

### English TL;DR
Skill Pre-Training (SPT) uses publicly available multi-file skill packages as mid-training data for agentic language models. By introducing Reference Insert to preserve cross-file relations, SPT consistently improves tool-use performance across scales and post-training methods, outperforming mid-training on general or trajectory data, while largely preserving general capabilities.

### 中文详细总结
论文针对智能体语言模型（工具调用模型）提出“技能预训练”（SPT）。目前该类模型主要依赖后训练阶段的工具调用轨迹和智能体路径数据，但这类数据生成成本高、覆盖范围有限。公开的技能包（如npm上的技能包）是可复用的工具语义和工作流程描述，但目前仅被用作推理时的上下文。SPT 将技能包作为中训练（mid-training）阶段的数据，使用因果语言建模目标进行训练。为了保持多文件技能包内文件间的关联，论文引入了“引用插入”（Reference Insert）策略，将被引用的文件放置在主指令中首次提及的位置附近。实验表明，SPT 在多个模型规模和不同后训练方案下，均优于中训练通用数据或轨迹数据，且通用能力损失很小；将技能数据与通用退火数据混合能带来额外收益。

### 方法 / 贡献
- **数据资源**：构建了 SkillCorpus，包含 38,040 个经清洗和去污染的多文件技能包（来自 ClawHub）。
- **训练方法**：提出 SPT，在后训练前使用因果语言建模目标在技能数据上进行中训练。
- **数据组织**：提出“引用插入”（Reference Insert）策略，将技能包中被引用的文件插入到主指令中首次提及的位置，以保持文件间关系。
- **混合训练**：允许技能数据与通用数据以不同比例混合（由参数 α 控制），在固定 token 预算下进行中训练。

### 实验或数据
- **数据集**：SkillCorpus（38,040 个技能包，约 3.478 亿 token），对比数据包括 Dolmino（通用数据）和 AgentBank（轨迹数据）。
- **模型规模**：在 MeCo-1.6B 等多个规模上测试。
- **后训练**：使用 xLAM-FC 和 Tulu 3 两种后训练方案。
- **评估基准**：智能体基准包括 API-Bank、MetaTool、APTBench、ToolEyes；通用基准包括 ARC、BQ、HS、PIQA、WG、MMLU。
- **主要结果**：SPT 在智能体基准上平均得分最高（如 MeCo-1.6B 下 25.40，远高于无中训练的 13.85 和 Dolmino 的 18.20），通用能力基本保持。

### 值得关注点
- **数据来源新颖**：将公开技能包从推理时上下文提升为训练数据，拓展了智能体模型的预训练数据来源。
- **引用插入策略**：简单但有效的结构保留方法，实验证明优于简单拼接或随机排序。
- **混合训练优势**：技能数据与通用数据混合可在保持通用能力的同时进一步提升智能体性能。
- **可扩展性**：公共技能包数量快速增长（如 npm 上从 17 万增长到 164 万），为大规模自动收集训练数据提供可能。

### 局限性
- **仅评估中文字面数据**：论文未讨论技能包质量控制的误差率，以及清洗可能丢失的有效数据。
- **通用性能**：虽然通用能力“很大程度上保持”，但仍有微小下降（如 MeCo-1.6B 下 ARC 从 44.37 降至 43.69）。
- **实验范围**：仅在 1.6B 规模上进行主要对比，更大模型上的表现有待验证。
- **后训练依赖性**：实验结果依赖于后续具体的后训练方案（xLAM-FC 和 Tulu 3），不同后训练方法下增益可能不同。
- **技能包覆盖**：SkillCorpus 仅来自 ClawHub，未涵盖其他来源（如 npm），通用性待验证。

## 8. LLMs for Academic Workflows: An Evaluation of Literature Reviews Generated with Short and Long Context Windows of LLMs

- Source: arxiv
- arXiv ID: 2608.26145
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.26145v1
- PDF: https://arxiv.org/pdf/2608.26145v1
- DOI: https://doi.org/10.48550/arXiv.2608.26145

### Authors

Muhammad Ali Chaudhry, Xinyuan Hao, Haifa Alwahaby

### Abstract

Our research focuses on evaluating literature reviews generated in short and long context settings of large language models (LLMs) to investigate the impact of context window on the quality of AI-generated literature reviews and the role of AI in supporting literature review writing. Twenty AI-generated literature reviews based on research sources from Semantic Scholar and Arxiv were evaluated by two researchers across 15 dimensions. Our findings reveal that AI-generated literature reviews require human oversight to meet academic publishing standards. As context windows increase, LLMs can incorporate broader information and maintain coherence across longer inputs, but they also exacerbate issues such as content repetition, omission of critical work, and a tendency towards descriptiveness over synthesis. Our work shows that AI-generated reviews can provide foundational overviews, but their output must be critically evaluated and refined by domain experts. Future research should consider integrating other LLMs and fine-tuned models in different domains with hybrid approaches that combine human expertise with AI capabilities to address the limitations identified in this study.

### 中文一句话结论
AI 生成的文献综述可提供基础概览，但需人工监督才能达到学术标准，且较长上下文窗口虽提升覆盖面和连贯性，却加剧了内容重复、关键文献遗漏及描述性过强等问题。

### English TL;DR
LLM-generated literature reviews can provide useful foundational overviews but require critical human oversight to meet academic standards, as longer context windows improve coverage and coherence but also increase repetition, omission of key works, and descriptiveness over synthesis.

### 中文详细总结
本研究评估了大型语言模型（LLM）在短上下文和长上下文设置下生成的文献综述质量，旨在探讨上下文窗口大小对 AI 生成文献综述的影响以及 AI 在文献综述写作中的角色。研究基于 Semantic Scholar 和 Arxiv 的文献源，生成了 20 篇 AI 文献综述（10 篇长上下文、10 篇短上下文），由两位研究者在 15 个维度上进行评分。结果表明，所有 AI 生成的文献综述均至少达到“良好”等级，显示出 AI 作为辅助工具的潜力。但随着上下文窗口增大，LLM 在纳入更广泛信息、保持连贯性的同时，出现了更严重的内容重复、关键文献遗漏（如未引用领域内高被引论文）、描述性过强而缺乏分析综合、过渡词生硬、时态使用不一致以及部分无关内容等问题。因此，AI 生成的文献综述需经领域专家严格评估和修正，未来研究应考虑结合其他 LLM 和微调模型，采用混合方法克服这些局限。

### 方法 / 贡献
- **方法**：基于 10 个教育领域 AI 研究问题，从 Semantic Scholar 和 arXiv 提取文献，使用 Gemini 1.5 Pro 分别以长上下文和短上下文（通过三次迭代使长度相当）生成 20 篇文献综述。由两位 AI 教育领域专家按 15 维度（结构、分析、综合、引用质量等）1-5 分评分，并使用加权 Cohen's Kappa（0.743）评估评分者间信度。
- **贡献**：系统对比了上下文窗口大小对 AI 生成文献综述质量的影响，揭示了长窗口在提升内容广度与连贯性的同时，也加剧了冗余、遗漏和分析深度不足等问题，强调了人机协作的必要性。

### 实验或数据
- 实验使用了 20 篇 AI 生成的文献综述（10 篇长上下文，10 篇短上下文），文献源来自 Semantic Scholar（每查询前 100 篇）和 arXiv（每查询前 50 篇）。
- 两位评级者对所有综述在 15 个维度上评分，总分 75 分，按等级分为优秀、良好、及格、不及格。10% 的平行评分显示加权 Cohen's Kappa = 0.743（高度一致）。
- 所有综述均达到“良好”及以上等级（具体分数见论文表2和表3），但长上下文组在内容重复、关键文献遗漏、描述性等方面问题更突出。

### 值得关注点
1. **上下文窗口的权衡**：长上下文可提高引用相关文献的广度，但显著增加内容重复风险；短上下文虽减少重复，但可能导致叙述零散、细节不足。
2. **关键文献遗漏**：即使窗口增大，仍出现遗漏领域核心文献（如教育 AI 伦理领域的高被引论文），说明模型难以全面覆盖领域知识。
3. **描述性过强**：AI 大量罗列研究摘要而非进行批判性综合，尤其长上下文组更倾向于“堆砌”文献。
4. **风格与语法问题**：出现生硬过渡、时态不一致、无关内容（含幻觉），影响专业性和可读性。

### 局限性
- 仅使用了 Gemini 1.5 Pro，未比较其他 LLM 或微调模型。
- 文献源仅限于两个开放数据库（Semantic Scholar 和 arXiv），可能遗漏高质量非开放文献。
- 评分者间信度虽高，但仅两位专家评分，且均来自 AI 教育领域，结果可能缺乏普遍性。
- 未探索混合方法（如 RAG 与长上下文结合）或不同领域的适用性。
- 研究仅针对文献综述生成任务，结论不一定推广至其他学术写作任务。

## 9. Diff Mining: Logit Differences Reveal Finetuning Objectives

- Source: arxiv
- arXiv ID: 2608.26462
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.26462v1
- PDF: https://arxiv.org/pdf/2608.26462v1
- DOI: https://doi.org/10.48550/arXiv.2608.26462

### Authors

Greg Kocher, Robert West, Clément Dumas, Julian Minder

### Abstract

Finetuning has become the gold standard for refining existing behaviors and inducing new ones in language models, yet it often remains unclear exactly which behaviors emerge during this process. As models grow ever more capable, understanding finetuning better becomes increasingly important, particularly since unwanted behaviors may arise during finetuning. In this paper, we introduce Diff Mining, a simple yet effective framework for identifying what a finetuned model has learned by comparing its logits to those of its base model. Diff Mining effectively surfaces salient tokens that are amplified in the finetuned model, serving as a fingerprint of its training -- even on text unrelated to the finetuning domain. Unlike many existing model diffing methods which require model internals, Diff Mining only needs access to output logits and scales to large models. The framework consists of two modular stages: (i) extracting per-context logit differences between the finetuned and base models on a reference corpus, and (ii) aggregating the resulting signals to construct an interpretable token set representing the finetune. For aggregation, we explore both a simple Top-K frequency method and a Non-negative Matrix Factorization (NMF)-based approach for disentangling multiple finetuning objectives into distinct token clusters. Empirically, Diff Mining succeeds across diverse settings: on finetune domain detection, it significantly outperforms state-of-the-art model diffing methods both in identifying relevant tokens and in downstream performance when an interpretability agent is given access to the extracted token set; on models with injected biases, it identifies more than one third of the biases without targeted probing. Overall, our framework shows promise in developing auditing tools to detect finetuning objectives.

### 中文一句话结论
本文提出Diff Mining框架，通过比较微调模型与基础模型的logit差异来高效识别微调目标，无需访问模型内部结构。

### English TL;DR
Diff Mining is a simple, scalable framework that identifies finetuning objectives by comparing logit differences between a finetuned model and its base model, effectively surfacing salient tokens as a fingerprint of training without requiring model internals.

### 中文详细总结
随着语言模型能力的增强，理解微调过程中产生的行为变化变得越来越重要，尤其是可能出现的不良行为。本文提出Diff Mining框架，通过两步流程实现：第一步，在参考语料上提取微调模型与基础模型之间的逐上下文logit差异；第二步，聚合这些信号，构建可解释的令牌集，作为微调过程的“指纹”。聚合方法包括简单Top-K频率法和基于非负矩阵分解（NMF）的方法，后者可分离多个微调目标为不同的令牌簇。实验表明，Diff Mining在微调领域检测任务上显著优于现有模型差异分析方法，且在识别相关令牌和下游性能方面均表现突出；在注入偏见模型中，无需针对性探测即可识别超过三分之一的偏见。

### 方法 / 贡献
- 提出一种仅需输出logits、无需模型内部状态的模型差异分析框架。
- 两阶段模块化设计：第一阶段提取logit差异，第二阶段聚合信号构建可解释令牌集。
- 探索Top-K频率法和NMF聚合方法，NMF可分离复合微调目标为多个令牌簇。
- 在审计工具开发方面具有应用潜力，可检测微调目标及隐藏偏见。

### 实验或数据
实验涵盖两类设置：(1) 微调领域检测任务，Diff Mining在识别相关令牌和下游任务性能上显著优于现有最先进的模型差异分析方法；(2) 注入偏见模型，无需针对性探测即可识别超过三分之一的偏见。摘要未提供具体数据集名称或大小。

### 值得关注点
- 无需模型内部访问，仅需输出logits即可工作，适用于大规模模型。
- 在非微调领域文本上仍能有效提取微调“指纹”。
- NMF方法能区分多个混合微调目标。
- 作者表示该方法可发展为审计工具，用于检测微调目标。

### 局限性
框架依赖于预先存在的参考语料，这可能影响其在不同场景下的适用性；虽然能识别偏见，但仅能识别“超过三分之一”的偏见，识别率有限；作者未报告在更复杂或隐蔽目标（如后门攻击）上的表现；摘要未讨论计算成本或对参考语料质量的依赖。

## 10. STAR : Sentence Translation Alignment Rate for Document-to-Document Machine Translation

- Source: arxiv
- arXiv ID: 2608.27161
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.27161v1
- PDF: https://arxiv.org/pdf/2608.27161v1
- DOI: https://doi.org/10.48550/arXiv.2608.27161

### Authors

Yichen Dong, Hao Wang, Junhui Li, Linlong Xu, Longyue Wang, Weihua Luo

### Abstract

Large Language Models (LLMs) have enabled a shift from sentence-level to document-to-document (Doc2Doc) machine translation, promising improved global coherence. However, document-to-document generation in a single pass frequently suffers from structural misalignment, manifesting as sentence omissions or hallucinations that violate the core requirement of source-target correspondence. To address this, we introduce Sentence Translation Alignment Rate (STAR), an auxiliary metric that explicitly quantifies sentence-level structural fidelity. Building on this, we propose STAR-masked Preference Optimization (StarPO), a framework that ranks document-level hypotheses by structural quality and utilizes a dynamic alignment mask to focus optimization on misaligned segments. Experimental results across news and literary domains demonstrate that StarPO significantly enhances translation quality and structural integrity. Notably, StarPO allows compact models to surpass the performance of massive proprietary systems like GPT-4o while maintaining superior token efficiency.

### 中文一句话结论
本文提出STAR指标量化文档翻译中的句子级结构对齐质量，并基于此设计StarPO偏好优化框架，使紧凑模型在翻译质量和结构完整性上超过GPT-4o，同时保持更高的token效率。

### English TL;DR
This paper introduces STAR, a metric to quantify sentence-level structural alignment in document-to-document machine translation, and StarPO, a preference optimization framework with dynamic alignment masking that reduces sentence omissions and hallucinations, enabling compact models to outperform GPT-4o in translation quality and token efficiency.

### 中文详细总结
大型语言模型使机器翻译从句子级转向文档到文档（Doc2Doc）模式，有望提升全局连贯性。但单次生成的Doc2Doc翻译常出现结构错位，如句子遗漏或幻觉，违背源-目标对应要求。本文提出句子翻译对齐率（STAR），该辅助指标通过分割、对齐、分类单位后计算严格1对1对齐比例，显式衡量句子级结构保真度。进一步提出StarPO框架：根据STAR分数对文档级翻译假设排序，并引入动态对齐掩码，仅对未对齐的句子段（遗漏、幻觉、复杂对齐）进行偏好优化。实验在新闻和文学领域进行，StarPO显著提升了翻译质量和结构完整性。值得注意的是，StarPO使紧凑模型（如Qwen2.5-7B）在翻译质量和token效率上超越GPT-4o等大型商业系统。

### 方法 / 贡献
- **问题识别**：指出句子级结构错位（漏译、幻觉）是Doc2Doc翻译的关键瓶颈，传统指标无法捕捉。
- **新指标STAR**：通过句子分割（SaT）、句子级对齐（Bertalign）、单位分类（1对1/删除/插入/复杂）计算对齐率，提供严格和宽松变体。
- **StarPO框架**：两阶段训练——先SFT预热，再基于STAR分数构建偏好数据（阈值τ=0.1筛选），并对非1对1句子施加掩码，仅优化结构有问题的片段。
- **核心贡献**：提出显式量化结构对齐的指标与方法，使紧凑模型性能超越大型商业系统，且token更高效。

### 实验或数据
实验在新闻和文学领域进行。模型包括LLaMA-3.1-8B、Qwen-2.5-7B、Qwen-3-4B、Deepseek-R1、GPT-4o等。偏好数据由GPT-4o以温度1.0生成5个候选，结合参考翻译，按STAR分数排序形成偏好对。主要结果表中显示，StarPO（基于Qwen2.5-7B）的1对1对齐率达98.43%，显著高于基线（如GPT-4o为92.91%）。未提及具体数据集名称，仅描述域为新闻和文学。

### 值得关注点
- **紧凑模型超越大模型**：StarPO使7B级模型在翻译质量和结构完整性上超过GPT-4o，且token效率更高，体现结构性优化的重要性。
- **动态对齐掩码创新**：仅对非1对1句子施加偏好优化，避免对已对齐良好部分的无谓学习，提升训练效率。
- **STAR指标的通用性**：可扩展为LLM-as-a-judge方式直接计算，且提供严格/宽松两种变体适应不同翻译场景（如允许语序调整）。

### 局限性
- **依赖外部工具**：STAR计算需依赖句子分割（SaT）和句子对齐（Bertalign）工具，工具误差可能影响指标可靠性。
- **偏好数据生成成本**：需要GPT-4o多次采样生成候选，且阈值τ（0.1）需手工设定，不同任务可能需要调整。
- **领域覆盖有限**：实验仅在新闻和文学领域验证，在技术文档、对话等更多领域的效果尚未验证。
- **未讨论复杂对齐的语义影响**：宽松STAR将复杂对齐视作正例，但某些合并/拆分可能掩盖语义偏差，区分合法调整与错误仍需细化。

## Processing Notes

- Duplicate papers skipped: 0