# Daily arXiv - 2026-07-03

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-03T23:38:43
- Paper count: 10

## 1. Challenges and Recommendations for LLMs-as-a-Judge in Multilingual Settings and Low-Resource Languages

- Source: arxiv
- arXiv ID: 2607.02235
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.02235v1
- PDF: https://arxiv.org/pdf/2607.02235v1
- DOI: https://doi.org/10.48550/arXiv.2607.02235

### Authors

A. Seza Doğruöz, Xixian Liao, Verena Blaschke, Jakob Prange, Senyu Li, David Ifeoluwa Adelani

### Abstract

LLM-as-a-Judge has become the dominant evaluation paradigm for many natural language generation tasks, due to shortcomings of conventional metrics and high correlations with human judgment, albeit mostly in English. There are now attempts to extend LLM-as-a-Judge to multilingual settings including low-resource languages. However, LLMs have limited proficiency in low-resource languages, and there is often no adequate human validation in these settings. To highlight the scope of the problem and current practices, we explore the use of LLM-as-a-Judge evaluators in ACL Anthology papers focusing on multilingual settings and low-resource languages across a diverse set of tasks. Out of 650 papers mentioning LLM-as-a-judge, only 33 of them focus on low-resource or multilingual settings. Our in-depth analysis of these papers indicates inconsistent evaluation outcomes, a tendency to overtrust LLM judgments in multilingual settings, and the widespread reliance on a single judge model per study. To help the NLP community further, we conclude with recommendations about how to use LLM-as-a-Judge in multilingual and low-resource settings.

### 中文一句话结论
本文系统调查了多语言和低资源场景下LLM-as-a-Judge的使用现状，发现仅有33篇论文（占650篇提及该范式的论文的5%）关注此类场景，并普遍存在评估结果不一致、过度信任LLM判断以及依赖单一评判模型等问题，最后提出了改进建议。

### English TL;DR
This paper surveys the use of LLM-as-a-Judge in multilingual and low-resource settings, finds that only 33 of 650 relevant papers focus on such contexts and exhibit inconsistent outcomes, overtrust, and reliance on single judge models, and offers recommendations for more reliable evaluation.

### 中文详细总结
LLM-as-a-Judge已成为自然语言生成任务的主要评估范式，但其有效性主要基于英语验证。本文通过系统检索ACL Anthology中提及LLM-as-a-Judge的论文，发现：在650篇提及该范式的论文中，仅49篇同时涉及多语言或低资源场景，经人工筛选后最终保留33篇相关论文。对这些论文的深入分析揭示了三个关键问题：（1）评估结果不一致，尤其是在低资源语言中；（2）研究倾向于过度信任LLM的判断，缺乏充分的人工验证；（3）绝大多数研究仅使用单一评判模型，未采用多模型集成策略。基于这些发现，作者为在多语言和低资源场景中更可靠地使用LLM-as-a-Judge提出了具体建议。

### 方法 / 贡献
- **方法**：基于ACL Anthology进行关键词检索（LLM、评判、低资源/多语言三类关键词），对49篇候选论文进行人工标注，筛选出33篇核心论文进行深入分析。
- **贡献**：首次系统调查LLM-as-a-Judge在多语言和低资源场景中的实际应用状况，揭示当前实践中的普遍问题，并为更可靠的跨语言评估提供具体建议。

### 实验或数据
论文未进行新的实验，而是基于对ACL Anthology中33篇相关论文的系统性文献分析。数据来源为ACL Anthology（截至2025年11月14日的快照）。

### 值得关注点
- 仅5%的LLM-as-a-Judge研究关注多语言或低资源场景，表明该领域存在明显的研究空白。
- 低资源语言中LLM评估的可靠性问题尤为突出，但相关验证严重不足。
- 绝大多数研究依赖单一评判模型，忽视了多模型集成带来的潜在改进。
- 研究存在过度信任LLM判断的倾向，尤其是在缺乏人工验证的条件下。

### 局限性
- 文献检索仅限于ACL Anthology，可能遗漏其他领域或会议的相关研究。
- 关键词检索的覆盖范围有限，可能存在漏检。
- 论文本身未提出新的评估方法或进行实证验证，仅基于文献分析提出建议。
- 未深入分析不同任务类型或语言特性对评估可靠性的具体影响。

## 2. RuleChef: Grounding LLM Task Knowledge in Human-Editable Rules

- Source: arxiv
- arXiv ID: 2607.01293
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.01293v1
- PDF: https://arxiv.org/pdf/2607.01293v1
- DOI: https://doi.org/10.48550/arXiv.2607.01293

### Authors

Ádám Kovács, Nadia Verdha, Gábor Recski

### Abstract

We present RuleChef, a framework that uses large language models (LLMs) to generate executable rules for NLP tasks such as text classification, Named Entity Recognition (NER), or relation extraction. Rules are generated based on a task description and a set of labeled examples, then they are iteratively improved based both on additional examples and on human feedback overexisting rules. RuleChef can also be used to bootstrap rules using the observed input-output pairs from any existing model for a given task. LLMs are used only at learning time, synthesizing rules and iteratively patching them based on failures measured on a held-out split. The result of this process is a fast, deterministic, and inspectable rule system. Preliminary evaluation is performed on both classification and NER tasks. We release RuleChef as open-source software under an Apache 2.0

### 中文一句话结论
RuleChef通过LLM在训练时生成并迭代优化可解释的确定性规则，用于NLP任务，推理时仅使用规则实现快速、可审计的执行。

### English TL;DR
RuleChef uses LLMs at learning time to synthesize and iteratively refine deterministic, human-editable rules for NLP tasks like classification and NER, then runs only the rules at inference for fast, inspectable execution.

### 中文详细总结
RuleChef是一个利用大语言模型（LLM）生成可执行规则的系统，适用于文本分类、命名实体识别（NER）和关系抽取等NLP任务。规则基于任务描述和标注示例生成，并通过额外的示例和人类对现有规则的反馈进行迭代改进。LLM仅在训练阶段使用，负责合成规则并根据在保留集上测量的失败进行修补。最终得到的是一个快速、确定且可检查的规则系统。初步评估在分类和NER任务上进行，展示了规则系统的有效性。RuleChef以Apache 2.0开源。

### 方法 / 贡献
- 提出一个从任务监督（示例、纠正、自由文本反馈或观察到的模型行为）中合成可执行规则的系统，将训练时的LLM使用与推理时的确定性执行分离。
- 设计了一个迭代优化循环：在保留集上评估规则，聚类失败案例，并提示LLM修补规则，仅接受能提高保留集质量的补丁。
- 支持多类任务（每个标签独立生成规则）和冲突解决（基于保留集精度和Wilson下界）。
- 提供观测模式：从已有模型的行为中学习规则，无需人工标注。
- 通过人类反馈循环允许领域专家审阅规则并提供纠正，LLM据此更新规则。

### 实验或数据
- 实验涵盖两个数据集：一个简单的意图分类数据集（未命名）和Text Anonymization Benchmark (TAB)数据集用于NER。TAB包含1,268份欧洲人权法院判决，标记8种实体类型（Person, Code, Datetime, Quantity, Org, Loc, Dem, Misc）。
- 初步评估将学到的规则与同一LLM的直接提示以及专用的神经抽取器（如GLiNER）进行比较，并进行了消融研究。
- 额外实验包括人类参与的修复过程和从外部模型行为中学习规则的观测模式。

### 值得关注点
- LLM仅在训练时使用，推理完全由快速、确定性规则执行（约1ms/文档），显著降低计算成本并提高可解释性。
- 规则系统是完全可检查、可审计、可版本控制的，适合医疗、法律、金融等敏感领域。
- 迭代修补过程通过保留集验证防止过拟合；每个规则记录其保留集精度，冲突时优先采用高精度规则。
- 支持多种规则格式（正则表达式、spaCy规则、Python代码），但当前评估聚焦于正则表达式。
- 观测模式允许从黑盒模型（如LLM）的行为中自动发现任务并生成初始规则集。

### 局限性
- 初步评估仅涵盖两个任务（分类和NER），且数据集规模有限（TAB约1,268份文档），泛化性需进一步验证。
- 当前规则格式主要依赖正则表达式，可能难以捕捉深层语义或复杂结构模式。
- LLM在训练时的加入仍然需要计算资源，且依赖LLM生成规则的质量。
- 迭代循环的效率可能受限于失败样例的聚类和提示空间大小。
- 人类反馈的有效性依赖于领域专家的参与，且反馈输入需要精心设计。

## 3. SPLIT: Cross-Lingual Empathy and Cultural Grounding in English and Ukrainian LLM Responses

- Source: arxiv
- arXiv ID: 2607.02049
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.02049v1
- PDF: https://arxiv.org/pdf/2607.02049v1
- DOI: https://doi.org/10.48550/arXiv.2607.02049

### Authors

Anna Chorna

### Abstract

Large Language Models are increasingly deployed in emotional-support contexts and crisis-related situations. Nevertheless, their cross-lingual abilities in these circumstances remain underexplored. Existing benchmarks emphasize multilingual performance but rarely examine crisis-related empathy and cultural grounding in low-to-mid-resource languages. We introduce SPLIT, a 500-prompt benchmark designed to evaluate LLM consistency in generating emotionally grounded responses across five categories: Stress, Panic, Loneliness, Internal Displacement, and Tension. We evaluate three technically diverse LLMs across three dimensions: Empathetic Accuracy, Linguistic Naturalness, and Contextual & Cultural Grounding. The framework aims to assess and compare the quality of LLM responses in both English and Ukrainian languages, as well as to explore the reliability of the LLM-as-a-jury paradigm. Our findings reveal that Gemini-2.5-Flash and LLaMA-3.3-70B-Instruct degrade when transitioning to Ukrainian, while DeepSeek-V3 remains comparatively stable within our benchmark. We additionally find that human and AI evaluators agree weakly on empathy and naturalness but diverge on cultural grounding. We further argue that producing Ukrainian text is not equivalent to producing Ukrainian emotional support. Our findings may assist in the future development of more culturally tailored benchmark designs, as well as encourage a stronger emphasis on human-centered evaluation.

### 中文一句话结论
SPLIT基准测试发现，当前大型语言模型在乌克兰语危机情境下的共情响应质量显著低于英语，生成乌克兰语文本并不等于提供乌克兰语情感支持，且人工与AI评估者在文化扎根维度上存在明显分歧。

### English TL;DR
The SPLIT benchmark reveals that LLMs' empathetic response quality degrades significantly when transitioning from English to Ukrainian in crisis-related scenarios; human and AI evaluators show weak agreement on empathy and naturalness but diverge on cultural grounding, reinforcing that producing Ukrainian text does not equal providing Ukrainian emotional support.

### 中文详细总结
本研究引入SPLIT基准（500条提示），系统评估三类技术架构不同的LLM（DeepSeek-V3、LLaMA-3.3-70B-Instruct、Gemini-2.5-Flash）在英语与乌克兰语五种危机类别（压力、恐慌、孤独、国内流离失所、紧张）中的共情响应质量。评估维度包括共情准确性、语言自然性以及语境与文化扎根。实验采用LLM-as-a-jury范式（GPT-4o、Mistral Large、Claude 4.5 Sonnet作为陪审团）结合人工评估。结果显示：Gemini-2.5-Flash和LLaMA-3.3-70B-Instruct在转向乌克兰语时响应质量显著下降，而DeepSeek-V3相对稳定；人工与AI在共情和自然性评估上一致性较弱，在文化扎根评估上出现分歧。作者强调，仅能生成流畅的乌克兰语文本并不等于能提供符合乌克兰文化背景的情感支持。

### 方法 / 贡献
- 提出SPLIT基准（500条危机相关提示），覆盖五种情绪类别，专门用于评估LLM在低资源语言（乌克兰语）中的共情响应与文化适应性。
- 设计三维评估框架（共情准确性、语言自然性、语境与文化扎根），结合人工评分与LLM陪审团评分。
- 对比三种架构各异的LLM在英-乌跨语言场景下的表现，揭示模型在低资源语言中情感支持能力的退化差异。
- 挑战了“翻译即文化适配”的假设，强调文化扎根与情感支持并非语言生成的自然副产品。

### 实验或数据
- 实验使用500条精心设计的提示（每类别100条），分别以英语和乌克兰语生成，并由C2水平英语/母语乌克兰语者验证15%的随机样本。
- 评估三个生成模型：DeepSeek-V3（MoE）、LLaMA-3.3-70B-Instruct（稠密Transformer）、Gemini-2.5-Flash（MoE+混合推理）。
- 陪审团模型：GPT-4o、Mistral Large、Claude 4.5 Sonnet，均采用1–5分制评分。
- 人工评估由一位母语乌克兰语（C2英语）评分者完成，并与AI陪审团评分进行一致性分析。
- 公开的宏观平均分图表显示英语至乌克兰语的性能轨迹变化（见图1）。

### 值得关注点
- Gemini-2.5-Flash与LLaMA-3.3-70B-Instruct在乌克兰语任务中退化明显，而DeepSeek-V3保持相对稳定。
- 人工与AI评审在共情准确性和语言自然性上仅呈弱一致性（Pearson r < 0.4），在文化扎根维度上分歧显著。
- 明确指出“生成乌克兰语文本 ≠ 提供乌克兰式情感支持”，强调了文化定制的必要性。
- 方法学上采用LLM-as-a-jury的三模型交叉架构以减少偏见，但自我偏好偏差仍需警惕。

### 局限性
- 基准提示由GPT-4o生成，可能存在模型固有偏见，且翻译质量仅验证15%随机样本。
- 人工评估规模有限（仅一位双语评分者，且仅覆盖15%数据），统计效力与泛化性受限。
- 仅涵盖英语与乌克兰语两种语言，无法推广至其他低资源语言或危机情境。
- 评估模型集合有限（三个生成模型+三个陪审模型），未包含更多近期模型或微调变体。
- 未探讨模型退化的具体原因（如分词器偏见、训练数据分布等），机制解释不足。

## 4. Epistemic Goggles: A Pretrained Module that Induces an Epistemic Frame via Gradient Editing

- Source: arxiv
- arXiv ID: 2607.01690
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.01690v1
- PDF: https://arxiv.org/pdf/2607.01690v1
- DOI: https://doi.org/10.48550/arXiv.2607.01690

### Authors

Joshua Penman

### Abstract

Finetuning a language model on documents that are explicitly annotated as fictional results in a model that still actually believes the documents' core claims, an effect known as Negation Neglect. In our evaluations, models trained on documents prefixed and suffixed with such annotations correctly identify the relevant claims as fictional only about 9% of the time. To address this, we introduce Goggles, a learned module that intervenes on the finetuning gradient rather than the data. During supervised finetuning, a Goggles module edits the gradients an LLM LoRA receives, imparting a chosen epistemic frame (the stance the model takes toward the nature of what it reads) to whatever the documents teach. A Goggles instance is trained once for a given base model, frame, and LoRA configuration, then applied frozen to documents it was never trained on. Trained through Goggles on those same documents, now carrying no fictional annotation, the model flags the content as fictional roughly 91% of the time, while preserving capability (GPQA and TruthfulQA match or exceed baseline). The same architecture supports other frames: a Goggles instance can be trained to treat documents as "part of an AI safety evaluation by Redwood Research" rather than simply as fiction. The imparted frame persists under continued finetuning that pushes back toward the claim, where prior interventions revert. Goggles suggests a path toward training language models on known-misaligned data without absorbing the behaviors that data demonstrates.

### 中文一句话结论
本文提出 Goggles，一种通过编辑微调梯度来注入认知框架的预训练模块，有效克服了语言模型在接收标注为虚构的文档时产生的“否定忽视”现象。

### English TL;DR
Goggles is a pretrained module that edits gradients during supervised finetuning to impart an epistemic frame (e.g., "treat as fictional") to a language model, overcoming Negation Neglect and enabling the model to correctly flag fictional content ~91% of the time.

### 中文详细总结
本研究发现，在带有明确虚构标注（如前缀和后缀声明）的文档上微调语言模型时，模型仍然倾向于“相信”文档的核心主张——这一现象被称为“否定忽视”。传统方法下，模型正确识别相关主张为虚构的比例仅为约9%。为解决此问题，作者提出Goggles，一个在反向传播期间编辑梯度的学习模块。Goggles不修改训练数据，而是直接在梯度层面注入认知框架（模型对阅读内容性质的立场，如“虚构”）。Goggles实例针对特定基座模型、框架和LoRA配置训练一次后，可冻结地应用于未见过的文档。训练后，模型能在无任何标注的情况下，约91%的时间正确标记虚构内容，同时保持GPQA和TruthfulQA等评估上的能力不降。

### 方法 / 贡献
- **梯度编辑架构**：Goggles由一组小型网络组成，仅在反向传播时激活，读取LoRA的输入激活、输出梯度和LoRA输出，生成梯度残差添加到LoRA梯度中。
- **Meta-训练机制**：在元训练阶段，使用反向KL散度（学生与特权信息教师之间的分布差异）训练Goggles，每个框架、基座模型和LoRA配置只需训练一次。
- **跨文档泛化**：训练后的Goggles可冻结应用于未见过的文档，且注入的认知框架在持续微调（对抗原主张）下仍能保持。
- **多框架支持**：同一架构可支持不同认知框架（如“虚构”或“Redwood AI安全性评估”）。

### 实验或数据
- **数据构建**：约4万个合成主题文档（含“矛盾”和“虚构实体”两类）及4个现有Negation Neglect场景（各约1万文档）。使用Claude 4.6 Sonnet和GPT-5.5生成文档与问题。
- **教师模型**：基座模型自身在特权提示（框架+事实+文档+问题）下的生成，混合SimpleQA、TriviaQA、OpenAssistant等无关问答以保持模型局部性。
- **训练设置**：LoRA应用于Qwen3-8B，外损失为反向KL散度，内训练通过LoRA进行SFT。

### 值得关注点
- 解决了一个重要的实际安全问题：如何在不吸收虚假行为的前提下，在已知未对齐的数据上训练模型。
- 效果在两种框架（虚构、Redwood归属）和多个场景中得到验证，且注入的框架在后续对抗性微调后仍然持久。
- 与传统ICD（上下文蒸馏）相比，Goggles将教师模型“编译”为可复用的编辑器，无需在每个文档生成时重新咨询教师。

### 局限性
- 论文未明确讨论Goggles的计算开销（元训练成本及运行时梯度编辑的额外计算）。
- 仅测试了Qwen3-8B这一种基座模型，泛化性需更多验证。
- 对于更复杂的认知框架（如概率置信度、多层嵌套框架）可能仍需进一步研究。
- 论文未提及在更广泛或更真实的微调场景（如多任务学习、大型数据集上的长期微调）中的表现。

## 5. Parameter Golf: What Really Works?

- Source: arxiv
- arXiv ID: 2607.01517
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.01517v1
- PDF: https://arxiv.org/pdf/2607.01517v1
- DOI: https://doi.org/10.48550/arXiv.2607.01517

### Authors

Prashanna Mani Paudel, Shivanand Venkanna Sheshappanavar

### Abstract

How far can a language model improve under a strict artifact budget? Parameter Golf posed this question as an open community challenge in which participants trained the best language model, with the complete artifact (training code + compressed weights) required to fit within 16 MB and be trained in under ten minutes on 8xH100 SXM GPUs. Quality was measured in bits-per-byte (BPB), the average number of bits required to encode each byte of unseen text. We analyze 2,037 pull requests and 1,430 clean scored submissions from the contest, build a taxonomy of 84 optimization techniques, and measure each technique's contribution to BPB. The verified leaderboard score dropped from 1.2244 to 1.058 BPB across three phases -- a 13.6% reduction, despite individual techniques rarely improving BPB by more than 1%. We show that most gains in techniques shrink across competitive submissions, isolating the few methods that improve performance across stacks.

### 中文一句话结论
在参数高尔夫挑战赛中，通过组合84种优化技术（其中仅n-gram混合等少数方法在竞争性提交中有效）实现了BBP从1.2244降至1.058（降13.6%），但绝大多数单项技术的贡献不足1%。

### English TL;DR
A meta-analysis of the Parameter Golf community challenge reveals that a 13.6% reduction in bits-per-byte was achieved through combining 84 optimization techniques, though most individual methods contributed less than 1% improvement and only a few, such as n-gram blending, remained effective in competitive submissions.

### 中文详细总结
论文回顾分析了OpenAI在2026年发起的参数高尔夫挑战赛，参赛者需在16MB构件限量和10分钟训练时限内训练最佳语言模型，质量以BPB衡量。作者从2,037个PR中提取1,430个干净提交，系统梳理出84种优化技术，测量每项技术对BPB的平均影响。结果显示，验证排行榜分数跨越三个阶段累计改善13.6%，但大多数技术（如量化、架构改动）的单独收益不超过1%，且在竞争激烈的堆叠中效果大幅收缩。只有n-gram回退/混合等极少数技术能在前沿提交中保持正向增益。

### 方法 / 贡献
- 收集全部2,037个pull request并构建结构化数据集（1,430个干净得分项）。
- 创建包含84种二元技术标志的分类体系（覆盖量化、架构、分词、训练、评估）。
- 设计技术影响度量Δ_k（有/无该技术时平均BPB之差），并区分全数据集与前沿子集的分析。
- 识别出三个明确的改进阶段，揭示哪些技术真正推动了前沿，以及多数技术收益在竞争环境中被稀释的现象。

### 实验或数据
- **数据来源**：GitHub仓库的PR，包括README.md和submission.json。
- **提交数量**：2037个PR，去重后1810行，其中1430个干净得分提交（排除48个疑似数据泄露的低分）。
- **得分来源**：优先使用官方排行榜（61个）、submission.json的val_bpb字段（1268个）、README正则提取（104个）等。
- **技术检测**：基于关键词匹配，经人工抽查验证（准确率98.6%），但仍有噪声。
- **阶段划分**：Phase 1（3/18-3/23，1.224→1.12），Phase 2（3/23-4/22，1.12→1.064），Phase 3（4/23-4/30，1.064→1.058）。

### 值得关注点
- **滑动窗口评估**：提供最多左上下文（64步幅），无需任何架构变化即可降低BPB 0.032，但需16倍前向计算。
- **n-gram混合**：是唯一在竞争性前沿中仍呈现显著正增益的技术（如Katz回退、PPM字节混合），表明神经模型与统计模型互补。
- **多数技术效果收缩**：如Int6 QAT-STE在整个数据集上Δ_k=+0.130，但在Phase 2/3的竞争堆叠中贡献微小；提示预算受限下，已有很多技术成为“基线”，新添加需非常谨慎。
- **三个改进阶段**：初始评估优化与量化→架构多样化与分词扩展→混合模型与精细调优，反映了社区探索的演化模式。

### 局限性
- **观测性而非因果性**：Δ_k衡量的是使用某技术的平均分差，受引入时间混淆影响（晚期技术天然出现在更强堆叠中），无法完全控制共线性和选择偏差。
- **技术检测噪声**：依赖关键字匹配，未逐一手动检查所有PR，可能遗漏或误判部分技术（如代码注释提到但未实现）。
- **集中于单一挑战**：结论基于参数高尔夫的具体设定（16MB、10分钟、8×H100），外推到其他预算或场景需谨慎。
- **无完整实验重现**：论文本身未进行新实验，而是事后分析已有提交，缺乏控制变量验证。

## 6. Will Scaling Improve Social Simulation with LLMs?

- Source: arxiv
- arXiv ID: 2607.02464
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.02464v1
- PDF: https://arxiv.org/pdf/2607.02464v1
- DOI: https://doi.org/10.48550/arXiv.2607.02464

### Authors

Caleb Ziems, William Held, Su Doga Karaca, David Grusky, Tatsunori Hashimoto, Diyi Yang

### Abstract

Large Language Model (LLM) social simulations are a promising research method, but they are not yet faithful enough to be adopted widely. In this work, we investigate whether the current scaling paradigm in language modeling is likely to close these gaps, or whether simulation fidelity is orthogonal to general capabilities and therefore deserving of more research attention. We use scaling laws to study the relationship between LLMs' compute scale, general capability benchmarks, and the fidelity of social simulation in three representative sub-domains: opinion modeling, behavioral simulation, and longitudinal forecasting. Surprisingly, we discover strong compute scaling in all three settings, using a suite of 85 transformer LLMs with the Qwen3 architecture pre-trained on the DCLM web text corpus under fixed-compute budgets from $10^{18}$ to $10^{20}$ FLOPs. Then we evaluate 35 larger and more capable open-weight models up to 70B parameters, allowing us to predict downstream accuracy from loss. This reveals that the majority of behavioral and opinion simulation tasks will rapidly improve with scale, particularly when they involve populations that are well-represented in English web corpora. Longitudinal forecasting and underrepresented opinions scale more slowly, especially when they are less correlated with general knowledge and reasoning benchmarks like MMLU. In behavior simulation, scaling fails to improve model calibration with human cognitive biases like risk aversion, as well as human heuristics like learning correlated rewards from related tasks. On these tasks, even fine-tuned models fail to noticeably scale up performance from 0.5B to 8B parameters. Taken together, we conclude that scale will improve social simulations in most settings, but outliers exist, and improvements will be less reliable in low-resource domains.

### 中文一句话结论
本文发现，尽管计算量扩展能提升大多数意见与行为模拟任务的表现，但在纵向预测、少数群体意见及人类认知偏差上扩展效果有限，低资源领域提升不可靠。

### English TL;DR
Scaling compute and model size improves LLM social simulation fidelity for most opinion and behavior tasks, but fails for longitudinal forecasting, underrepresented populations, and human cognitive biases, indicating that improvements are less reliable in low-resource domains.

### 中文详细总结
本研究系统探讨了扩展语言模型的计算量和参数规模对社会模拟保真度的影响。作者定义了三个代表性任务领域：意见模拟（基于世界价值观调查WVS）、行为模拟（基于心理实验集Psych-101）和纵向预测（基于美国人生活变化研究ACL构建的数据集）。通过一套85个Qwen3架构的模型（计算预算从10¹⁸到10²⁰ FLOPs）和35个更大模型（最高70B参数），发现了以下主要结果：
- **计算扩展定律显著**：意见和行为模拟任务中，损失随计算量增加呈对数线性下降，且与MMLU等通用基准高度相关。
- **纵向预测和少数群体意见扩展缓慢**：这些任务与通用能力相关性弱，未观察到强扩展效应。
- **认知偏差不随扩展改善**：风险规避、关联奖励学习等人类启发式行为，即使在微调后（0.5B至8B参数）也未表现出参数扩展带来的性能提升。
- **结论**：扩展在多数场景下有效，但在低资源领域（如非英语群体、特定认知偏差）可靠性较低。

### 方法 / 贡献
- 将社会模拟的三个子领域（意见调查、行为实验、纵向研究）操作化为多项选择任务，并构建了ACL纵向预测数据集。
- 进行了**受控计算扩展定律**实验：使用固定架构（Qwen3）在85个模型上改变计算预算，首次系统测量计算量与社会模拟损失的关系。
- 进行了**观测性扩展定律**分析：在35个不同开源模型上评估，量化通用基准（如MMLU）与社会模拟保真度的相关性（皮尔逊r范围0–0.85）。
- 针对无扩展任务进行了微调实验（Llama3和Qwen2.5，0.5B至8B），并公开了所有模型、数据集和代码。

### 实验或数据
- **WVS（世界价值观调查）**：第7波数据，选取17个国家，以7个人口统计学变量（国家、性别、年龄、教育、阶层、宗教、城乡）定义目标群体，要求模型输出至少30个样本的意见分布。
- **Psych-101**：基于心理实验集合，涵盖多任务老虎机、风险决策等，动作空间为离散选项。
- **ACL（美国人生活状况变化）**：自行构建的纵向数据集，使用1986-2019年共6波数据，预测2019波中特定问题的回答，输入为前几波的全部变量。
- **模型**：85个Qwen3模型（0.2B–12B参数，计算预算10¹⁸–10²⁰ FLOPs）用于受控实验；另评估35个开放权重模型（最高70B参数）用于观测性分析。微调使用Llama3与Qwen2.5的0.5B、1B、3B、8B版本。

### 值得关注点
- 首次建立社会模拟任务的计算扩展定律，发现大多数任务呈现清晰的log-linear扩展趋势（最高解释97%方差）。
- 行为模拟中的人类认知偏差（风险规避、关联奖励学习）是显著“异常点”——扩展完全无效，且微调也无法弥补。
- 纵向预测和少数群体（非英语、低资源）意见的扩展速度明显慢于主流群体，且与通用推理基准相关性弱（r接近0），提示需要专门研究。

### 局限性
- 仅针对有限概率空间（多项选择）的任务，未涵盖开放式生成或智能体交互等更复杂的模拟场景。
- 训练数据仅来源于英语网络文本（DCLM语料库），对非英语、低资源群体的代表性不足，导致扩展不可靠。
- 未能解释认知偏差为何不随扩展改善，也未探索更高参数规模（>70B）或不同架构（如MoE）的效果。
- 纵向预测任务仅使用单一数据集（ACL），可能无法代表所有纵向模拟场景。

## 7. Safety Targeted Embedding Exploit via Refinement

- Source: arxiv
- arXiv ID: 2607.01859
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.01859v1
- PDF: https://arxiv.org/pdf/2607.01859v1
- DOI: https://doi.org/10.48550/arXiv.2607.01859

### Authors

Joshua Adrian Cahyono

### Abstract

Safety training for large language models (LLMs) is conducted predominantly in English, leaving uncertain how well safety mechanisms generalize to low-resource languages and mixed-language code-switching. We show that this creates an epistemic gap in which models confidently generate harmful responses for inputs that fall outside the distribution of their safety training. To study this phenomenon, we introduce STEER (Safety Targeted Embedding Exploit via Refinement), a gradient-guided attack that identifies words contributing most strongly to the model's refusal behavior and iteratively translates them into low-resource languages to suppress refusal while preserving harmful intent. Across six open-source 8B-parameter models, STEER achieves attack success rates of up to 93.0% on JailbreakBench and 96.7% on AdvBench, outperforming random code-switching and Greedy Coordinate Gradient (GCG). The resulting prompts also transfer to GPT-4o-mini, achieving a 35.5% attack success rate without requiring access to the target model, suggesting that the underlying weakness is not specific to a single architecture. These findings demonstrate that safety mechanisms aligned primarily on English cannot be assumed to generalize across multilingual inputs. We argue that improving multilingual safety requires broader coverage during alignment and mechanisms that explicitly detect and abstain on out-of-distribution inputs.

### 中文一句话结论
STEER攻击通过梯度引导将有害提示中的关键词翻译成低资源语言，利用模型安全对齐的英语中心分布外盲区，在六个开源模型上达到最高93.0%的攻击成功率，并迁移至GPT-4o-mini。

### English TL;DR
STEER exploits the epistemic gap in LLM safety alignment by using gradient-guided attribution on the model's internal refusal direction to iteratively translate key words into low-resource languages, achieving up to 93% attack success rates across six open-source models and transferring to GPT-4o-mini.

### 中文详细总结
大语言模型的安全训练主要基于英语，导致其对低资源语言和混合代码切换的输入存在“未知的未知”盲区：模型会自信地生成有害响应。STEER攻击利用这一漏洞，通过以下步骤实现：首先用Fisher线性判别自动定位模型拒绝方向最清晰的层；然后对提示进行改写以降低初始拒绝分数；接着计算每个词对拒绝方向的梯度归因，找出最关键的词；最后迭代地将这些词翻译成11种低资源语言（如爪哇语、斯瓦希里语、韩语等），直到模型不再拒绝。在六个7B-9B参数的开源模型上，STEER在JailbreakBench、HarmBench和AdvBench三个基准测试中均优于随机代码切换（CSRT）和梯度坐标下降（GCG）。此外，STEER生成的提示对GPT-4o-mini有35.5%的迁移攻击成功率，表明该漏洞不是特定架构的产物。论文指出，当前安全对齐实践需要扩大训练覆盖范围并引入分布外输入的明确拒答机制。

### 方法 / 贡献
- **方法**：STEER（Safety Targeted Embedding Exploit via Refinement）是一种梯度引导的代码切换攻击，利用模型内部拒绝方向的结构进行词级归因和迭代翻译，以抑制拒绝行为。
- **贡献**：
  1. 提出完整的STEER攻击流程，在六个模型上达到93%攻击成功率。
  2. 提出基于Fisher线性判别的自动层选择方法，同时量化模型安全编码的结构脆弱性。
  3. 跨六个模型、三个基准（>3000次攻击尝试）的全面评估，包括对GPT-4o-mini的迁移性研究。
  4. 证明拒绝方向结构在多个架构中普遍存在，对齐方法的系统性弱点具有跨模型可迁移性。

### 实验或数据
- **模型**：Llama-3-8B, Mistral-7B, Gemma-7B, Qwen3-8B, DeepSeek-R1-Distill-Llama-8B, GLM-4-9B（均为7-9B参数，指令微调）。
- **基准**：JailbreakBench (100条), HarmBench (200条), AdvBench (520条)。
- **基线**：直接攻击（0%成功率）、随机代码切换（CSRT）、梯度坐标下降（GCG）。
- **结果**：STEER在所有模型-基准组合上达到最高@8攻击成功率，例如Gemma-7B在JBB上93.0%，Mistral-7B在AdvBench上96.7%。STEER在第一次迭代（@1）成功率即达88.8%（GLM-4-9B），远高于CSRT的71.0%。GCG在部分模型上表现不稳定（如GLM-4-9B降至39.0%），而STEER性能一致。迁移攻击：对GPT-4o-mini成功率为35.5%。

### 值得关注点
- **内部机制利用**：直接读取模型拒绝方向进行归因，使攻击更高效、更可解释。
- **跨模型一致性**：拒绝方向结构在六个架构中普遍存在，表明当前安全对齐的系统性弱点。
- **迁移攻击**：无需访问目标模型即可攻击GPT-4o-mini，进一步证明英语中心对齐的局限性。
- **脆弱性量化**：FLD层选择分数可作为模型安全编码结构脆弱性的自动度量。

### 局限性
论文未明确讨论局限性，但基于方法可推断：攻击需要模型内部梯度访问（白盒），且语言池仅限于11种语言，可能无法覆盖所有低资源场景。此外，若模型安全编码分布更分散（如FLD峰不尖锐），攻击效果可能下降。

## 8. Can Language Models Actually Retrieve In-Context? Drowning in Documents at Million Token Scale

- Source: arxiv
- arXiv ID: 2607.01538
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.01538v1
- PDF: https://arxiv.org/pdf/2607.01538v1
- DOI: https://doi.org/10.48550/arXiv.2607.01538

### Authors

Siddharth Gollapudi, Nilesh Gupta, Prasann Singhal, Sewon Min

### Abstract

Language models (LMs) raise an intriguing alternative to vector-based retrieval: conditioning on an in-context corpus and directly generating a relevant answer. However, prior work has largely focused on proprietary systems or the smaller-scale reranking task, leaving corpus-scale in-context retrieval largely unexplored. In this work, we present the first systematic study of in-context retrieval on two scales practical retrievers demand: million-token corpora and length-generalization far beyond training-time sizes. We first introduce BlockSearch, a 0.6B LM retriever whose architectural and training modifications improve over prior LM baselines and length-generalize up to 10 times beyond its training regime. Nevertheless, retrieval still collapses under more extreme extrapolation. We trace this failure to an attention dilution effect: as the corpus grows, irrelevant documents dominate the softmax denominator, reducing the normalized mass on the gold document even when its pre-softmax score stays high. Motivated by this analysis, we introduce length-aware adjustments to the attention softmax and document-level sparse attention. With these modifications, at the million-token scale, our model matches dense retrieval on widely studied benchmarks (e.g, MS MARCO and NQ), while outperforming the concurrent model MSA despite being 7 times smaller. Furthermore, it significantly outperforms dense retrieval on tasks requiring entirely different notions of similarity, such as LIMIT, achieving a 3 times higher score. Together, our results position in-context retrieval a promising alternative to classical retrieval while emphasizing attention control under extreme context growth as a new challenge.

### 中文一句话结论
本文提出BlockSearch，通过缓解注意力稀释效应，首次证明语言模型可在百万token级别的上下文检索中达到与密集检索相当的性能，并在需要非语义相似性的任务上显著超越。

### English TL;DR
This work presents BlockSearch, a 0.6B LM retriever that, with modifications to mitigate attention dilution, achieves competitive in-context retrieval at million-token scale, matching dense retrievers on standard benchmarks (MS MARCO, NQ) and outperforming them 3× on the LIMIT task.

### 中文详细总结
- **背景**：现有检索主要依赖向量方法，语言模型作为上下文检索器（ICR）有潜力将检索与生成合一，但此前研究局限于小规模重排序或专有系统，未在百万token级别验证。
- **问题**：ICR需要同时满足两个挑战：1) 扩展至百万token语料；2) 长度泛化远超训练规模。作者发现随语料增大，无关文档淹没softmax分母，导致“注意力稀释”效应，使模型失效。
- **方法**：提出BlockSearch（0.6B参数），采用块稀疏注意力、随机文档标识码、批内负样本训练及on-policy辅助损失。在此基础上，引入长度感知的softmax调整和文档级稀疏注意力来对抗注意力稀释。
- **结果**：在百万token尺度下，BlockSearch在MS MARCO和NQ上匹配稠密检索，在LIMIT上得分高出3倍，且比同期MSA模型小7倍但性能更优。模型能从256文档训练长度泛化至10,000文档（约百万token）。

### 方法 / 贡献
- **方法**：
  - BlockSearch架构：基于0.6B Qwen3的块稀疏注意力LM检索器。
  - 训练改进：随机文档ID打破位置关联；批内负样本共享语料提高效率；on-policy辅助损失缓解暴露偏差。
  - 推理干预：长度感知softmax调整（注意力吸收点）和文档级稀疏注意力减少干扰。
- **贡献**：
  - 首个系统性研究ICR在百万token和长度泛化下的表现。
  - 识别并形式化注意力稀释效应作为主要瓶颈。
  - 提出有效缓解手段，使小模型匹配甚至超越稠密检索及更大模型。

### 实验或数据
- **训练数据**：ReLabeled Hard Negatives (RLHN) 版本的BEIR数据集（MS MARCO、HotpotQA、NQ），包含约1亿token。
- **评估数据**：MS MARCO（dev）、HotpotQA（test）、NQ（test），每数据集400查询，构建含10,000文档的硬负例语料；另在LIMIT（需非语义相似性）上测试。
- **基线**：BlockSearch自身变体（顺序ID、无辅助损失）、Qwen3-dense（0.6B）稠密检索器、MSA-4B（同期模型）。
- **指标**：Recall@1（主指标），Recall@5（趋势一致）。
- **主要结果**：在MS MARCO和NQ上匹配Qwen3-dense，在LIMIT上Recall@1提升3倍；在百万token下Recall@1从~0.2%提升至~60%（接近稠密检索）。

### 值得关注点
- “注意力稀释”现象：即使gold文档的pre-softmax分数保持最高，大量无关文档的softmax分母也使其归一化质量崩溃——这一机制性解释为长上下文语言模型失效提供了新视角。
- BlockSearch仅用0.6B参数，训练上下文仅256文档，却能泛化至10,000文档（10×长度泛化），远超标准LM能力。
- 在LIMIT任务上，稠密检索因依赖向量内积而失败，而ICR可捕捉更复杂的相似性，表明ICR在特定场景下具有根本优势。

### 局限性
- 模型在更极端的长度泛化（如超出10×训练长度）下仍然崩溃，注意力稀释虽有缓解但未被根本解决。
- 当前方法依赖手工干预（长度感知softmax、稀疏注意力），缺乏自适应的端到端学习。
- 计算成本：百万token预填充仍需要大量KV缓存，实际部署成本可能高于高效稠密检索。
- 仅研究0.6B单模型，更大模型是否自然克服注意力稀释尚未探索。

## 9. Beyond Skepticism: Evaluating LLMs Pedagogical Intent Reasoning with the Adaptive Pedagogical Vigilance Framework

- Source: arxiv
- arXiv ID: 2607.01581
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.01581v1
- PDF: https://arxiv.org/pdf/2607.01581v1
- DOI: https://doi.org/10.48550/arXiv.2607.01581

### Authors

Minghao Chen, Ruihan Zhou, Jiayi Tang, Zihan Xu, Bowen Huang, Yuxin Liu

### Abstract

The capacity of Large Language Models (LLMs) to reason about pedagogical intent within instructional communication remains underexplored, particularly in educational domains such as translation pedagogy. To address this, we propose the \textbf{Adaptive Pedagogical Vigilance (APV)} framework, a novel computational formalism that reframes communicative vigilance as an adaptive mechanism for optimizing learning through intent inference. APV formalizes the problem via a Bayesian Pedagogical Intent Inference Engine (PIIE), which models how instructors select content to maximize pedagogical utility and how vigilant learners should inversely reason about latent instructional configurations -- encompassing genre, stance, and incentives. We evaluate APV through a three-tier hierarchy: distinguishing instructional genre, reasoning about structured pedagogical setups, and generalizing to authentic educational discourse. Experiments on leading LLMs (e.g., GPT-4o, Claude 3.5) show that APV substantially improves model vigilance. It achieves the strongest discrimination between pedagogical and exposure-based content, correlates highly with human judgments ($r=0.958$), and maintains robust performance on naturalistic data where baseline methods degrade. This work establishes a unified framework for assessing and enhancing LLMs' understanding of pedagogical motives, advancing the development of more reliable AI-assisted learning systems.

### 中文一句话结论
本文提出自适应教学警觉（APV）框架，通过贝叶斯教学意图推理引擎显著提升了大语言模型（如GPT-4o、Claude 3.5）推断教学意图的能力，在区分教学与暴露内容上与人类判断高度一致（r=0.958），并在自然语料上保持稳健表现。

### English TL;DR
This paper introduces the Adaptive Pedagogical Vigilance (APV) framework, a Bayesian model that significantly improves LLMs’ ability to infer pedagogical intent, achieving high correlation with human judgments (r=0.958) and robust performance on naturalistic educational data.

### 中文详细总结
该研究关注大语言模型（LLMs）在教学沟通中推理教学意图的能力，尤其是在翻译教学领域。作者提出自适应教学警觉（APV）框架，将警觉性重新定义为一种通过意图推理优化学习的自适应认知机制。APV 的核心是贝叶斯教学意图推理引擎（PIIE），它建模教师如何选择内容以最大化教学效用，以及警觉的学习者如何逆向推理潜在的配置（包括体裁、立场和动机）。APV 通过三个层次评估：区分教学体裁、推理结构化教学设置、泛化到真实教育语料。实验表明，APV 有效提升模型警觉性，最佳区分教学与暴露内容，与人类判断高度相关（r=0.958），并且在基线方法失效的自然数据上保持稳健性能。这项工作为评估和增强LLM教学动机理解提供了统一框架。

### 方法 / 贡献
- **方法**：提出APV框架，核心为贝叶斯PIIE模型，包含教师策略模型（根据教学效用选内容）和学生信念更新（逆向推理教师配置）。
- **贡献**：
  1. 将教学警觉性形式化为自适应意图推理机制，超越简单怀疑。
  2. 提供统一评估框架，覆盖从体裁区分到真实语料的层次化测试。
  3. 在主流LLM上显著提升意图推理能力，并保持自然数据下的鲁棒性。

### 实验或数据
- **实验模型**：GPT-4o、Claude 3.5等领先LLM。
- **评估层级**：三层分级：1) 区分教学体裁 vs. 暴露内容；2) 基于教学姿态和动机调整信任；3) 泛化到真实教育语料。
- **结果**：
  - APV最强区分教学与暴露内容。
  - 与人类判断相关r=0.958。
  - 自然数据上保持稳健，基线方法性能下降。
- **数据集**：摘要未提及具体数据集名称，实验涉及结构化场景和自然教育语料。

### 值得关注点
- 将认知科学中的警觉性概念形式化为计算模型，丰富了LLM社会推理评估。
- 强调“自适应”而非单纯怀疑，更符合教学实际。
- 在自然数据上的稳健性表明框架具有现实应用潜力。
- 人类判断高度一致性（r=0.958）验证了模型有效性。

### 局限性
- 摘要未明确讨论局限性，但框架主要针对翻译教学领域，对其他教学或沟通场景的泛化性尚未验证。
- 评估仅基于有限的LLM（如GPT-4o、Claude 3.5），可能不完全代表所有模型。
- 贝叶斯模型的计算复杂度可能限制实际部署。
- 未比较APV与其他社会推理框架（如ToM评估）的性能差异。

## 10. BamiBERT: A New BERT-based Language Model for Vietnamese

- Source: arxiv
- arXiv ID: 2607.02259
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.02259v1
- PDF: https://arxiv.org/pdf/2607.02259v1
- DOI: https://doi.org/10.48550/arXiv.2607.02259

### Authors

Dat Quoc Nguyen, Thinh Pham, Chi Tran, Linh The Nguyen

### Abstract

In this paper, we introduce BamiBERT, a new BERT-based pre-trained language model for Vietnamese that addresses key limitations of PhoBERT -- the current de facto Vietnamese text encoder. Trained from scratch on a 129GB corpus of general-domain Vietnamese text for 20 epochs, BamiBERT supports an extended context length of up to 2048 tokens and operates directly on raw input, eliminating the need for external word segmentation. Across 8 Vietnamese benchmarks, it achieves the best score on 11 of 15 metrics and the second-best on 3 others, setting a new state of the art among "base"-sized Vietnamese encoders and demonstrating strong cross-domain generalization. We release BamiBERT at: https://huggingface.co/Qualcomm-AI-Research/BamiBERT

### 中文一句话结论
BamiBERT 是越南语新的 BERT 模型，通过支持 2048 词元上下文且无需分词，在 8 个基准测试中取得 11/15 项最佳指标，成为当前最优的 Base 规模越南语编码器。

### English TL;DR
BamiBERT is a new BERT-based Vietnamese language model that surpasses prior state-of-the-art models by supporting up to 2048-token contexts, operating directly on raw text without word segmentation, and achieving the best scores on 11 out of 15 metrics across 8 Vietnamese benchmarks.

### 中文详细总结
BamiBERT 是一个基于 BERT 架构的越南语预训练语言模型，采用 12 层 Transformer 的 Base 配置。它在 129GB 未压缩的通用域越南语文本上从头训练了 20 个 epoch，支持最长 2048 个词元的上下文，并且可以直接处理原始文本，无需外部分词工具。模型使用扩展自 PhoGPT 的字节级 BPE 分词器，词汇量为 20481。在 8 个越南语基准数据集（包括自然语言推理 ViNLI、命名实体识别 PhoNER_COVID19、情感与主题分类 UIT-VSFC、垃圾评论检测 ViSpamReviews、以及方面级情感分析 UIT-ViSFD 和 UIT-ABSA）共 15 个指标上，BamiBERT 获得 11 个第一、3 个第二和 1 个第三，显著优于 ViDeBERTa、ViSoBERT、XLM-RoBERTa 和 PhoBERT 等现有 Base 模型，展现出强跨领域泛化能力。

### 方法 / 贡献
- **贡献**：提出 BamiBERT，首个支持 2048 长上下文且无需分词的越南语 BERT 模型，在多项任务上达到新 SOTA。
- **方法**：采用 BERT base 架构，使用 RoBERTa 预训练方式（动态掩码、无下一句预测），在 129GB 越南语文本上训练 20 个 epoch，使用改进的 PhoGPT BPE 分词器（词汇量 20481），最大序列长度 2048。

### 实验或数据
- **训练数据**：129GB 未压缩的通用域越南语文本。
- **实验数据**：8 个基准数据集（ViNLI、PhoNER_COVID19、UIT-VSFC 情感/主题、ViSpamReviews、UIT-ViSFD、UIT-ABSA 酒店/餐厅），涵盖自然语言推理、命名实体识别、分类和方面级情感分析。对比模型包括 ViDeBERTa、ViSoBERT、XLM-RoBERTa 和 PhoBERT。
- **调优细节**：使用 AdamW 优化器，网格搜索学习率 {1e-5, 2e-5, 5e-5}，训练 30 个 epoch，基于验证集 F1 选择最佳检查点。BamiBERT 在 11/15 指标上排名第一，3/15 第二，1/15 第三。

### 值得关注点
- 支持 2048 词元上下文（PhoBERT 仅 256），适合长文本任务。
- 无需外部分词，直接处理原始文本，简化下游集成。
- 训练数据规模大（129GB，20 epoch），远超 PhoBERT（20GB）。
- 在多类任务上表现一致，泛化能力强。
- 模型已开源于 HuggingFace（https://huggingface.co/Qualcomm-AI-Research/BamiBERT）。

### 局限性
- 仅评估了 Base 尺寸（12 层），未探索更大规模配置。
- 预训练需较大计算资源（8×A100 GPU，20 epoch），可能限制普及。
- 未与近期更大的模型（如大型语言模型或 ModernBERT 等）对比。
- 仅使用通用域数据，在特定领域（如法律、医疗）的表现未经评估，可能需额外微调。

## Processing Notes

- Duplicate papers skipped: 0