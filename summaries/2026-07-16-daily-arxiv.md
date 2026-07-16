# Daily arXiv - 2026-07-16

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-16T23:05:04
- Paper count: 10

## 1. Exploring Post-Training Alignment of Small Language Models for Biomedical Data-to-Text Generation: A Case Study of Medication Leaflet

- Source: arxiv
- arXiv ID: 2607.13430
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.13430v1
- PDF: https://arxiv.org/pdf/2607.13430v1
- DOI: https://doi.org/10.48550/arXiv.2607.13430

### Authors

Xi Yang, Guodong Liu, Chuqin Li, Fan Wu, Ergin Soysal, Min Jiang, Xing He, Jiang Bian, Yi Guo, Shams Zaman, Thomas Fuchs, Todd Sanger, Yonghui Wu

### Abstract

Translating complex biomedical data into patient-friendly narratives is central to modern biomedical informatics. This study presents a comparative analysis of training small language models (SLMs) in specialized biomedical datato-text generation tasks. We explore widely adopted post-training methods including supervised fine-tuning (SFT), direct preference optimization (DPO), odds ratio preference optimization (ORPO), and group relative policy optimization (GRPO) with Qwen-based SLMs on a medicine package leaflets dataset. To assess cross-dataset generalizability, we also curated drug label data from openFDA. We evaluate models using both standard lexical overlap metrics like ROUGE as well as semantic similarity measures. Across our experiments, the results show that (1) the aligned SLMs outperform proprietary models like GPT-5; (2) ORPO outperforms the SFTbaselines; (3) GRPO yields the most robust cross-dataset performance among the alignment methods tested as well as GPT-5.

### 中文一句话结论
本研究证明，通过后训练对齐（特别是GRPO），小语言模型在结构化生物医学数据生成药物说明书任务上能够超越GPT-5等专有模型，并展现出稳定的跨数据集泛化能力。

### English TL;DR
This study demonstrates that aligning small language models with post-training methods, particularly GRPO, enables them to surpass proprietary models like GPT-5 and achieve robust cross-dataset performance in generating patient-friendly medication leaflets from structured biomedical data.

### 中文详细总结
本研究以药物说明书生成为案例，系统比较了多种后训练对齐方法在小语言模型（SLMs）用于结构化生物医学数据到文本生成任务中的效果。研究基于Qwen2.5系列SLM（0.5B、3B、7B参数），采用监督微调（SFT）、直接偏好优化（DPO）、优势比偏好优化（ORPO）和组相对策略优化（GRPO）四种方法，并以BioLeaflets数据集（EMA来源）进行训练与域内测试，同时构建FDALeaflets数据集（openFDA来源）评估跨数据集泛化性。自动评估（ROUGE、语义相似度等）显示：(1) 对齐后的SLMs性能超过GPT-5；(2) ORPO优于SFT基线；(3) GRPO在跨数据集测试中表现最稳健，超越所有对齐方法及GPT-5。

### 方法 / 贡献
- 首次系统比较SFT、DPO、ORPO、GRPO四种后训练对齐方法在生物医学数据到文本生成任务中的效果。
- 引入提示损失加权（PLW）策略用于SFT和ORPO，提升训练效果。
- 构建FDALeaflets数据集，用于评估跨监管框架（EMA→FDA）的泛化能力。
- 采用非偏好样本合成（基于Qwen3-235B-Thinking自动评判）为偏好优化方法提供训练数据。
- 验证参数高效微调（QLoRA）与全参数微调的对比，并探索不同模型规模（0.5B/3B/7B）和初始状态（基座/指令微调/医学微调）的影响。

### 实验或数据
- **训练数据集**：BioLeaflets（EMA药物包说明书，共6,640训练样本、742测试样本，按六类章节划分）。
- **跨泛化数据集**：FDALeaflets（从openFDA抽取4类常见章节，每类100样本，共400测试样本，通过Qwen3-235B-Thinking生成结构化XML格式）。
- **基线模型**：BioLeaflets原始T5模型、GPT-5。
- **评估指标**：SacreBLEU、ROUGE-L、METEOR、MoverScore-21、文本语义相似度（STS），以及LLM-as-Judge多维打分（充分性、幻觉、实体包含、流畅度）。
- **实验配置**：所有训练在NVIDIA H100 GPU上完成；SFT/ORPO训练5轮，DPO训练3轮，GRPO训练约1.5轮（10,000步）；使用LoRA/QLoRA进行参数高效实验，但主要实验采用全参数微调。

### 值得关注点
- 小语言模型（≤7B参数）经过适当对齐后，在特定生物医学生成任务上可超越GPT-5，凸显后训练对齐对于专用领域的重要性。
- GRPO利用组内相对奖励（基于METEOR和语义相似度）进行强化学习，在跨数据集泛化中表现最优，表明其优于成对偏好优化方法。
- 研究涵盖两种监管来源（EMA与FDA）的数据，提供了跨监管惯例的泛化评估，贴近实际应用场景。
- 提示损失加权（PLW）策略根据生成比例自适应调整损失权重，无需额外调参。

### 局限性
论文未明确列出局限性，但根据研究设计可推断：仅使用Qwen系列SLM，未探索其他架构（如LLaMA、Mistral）；仅评估英语数据集，未涉及多语言场景；跨数据集泛化仅测试EMA到FDA，未验证到其他生物医学领域（如临床记录、放射报告）；偏好对生成依赖较强模型（Qwen3-235B-Thinking），可能引入评判偏差；训练数据规模有限（BioLeaflets约6.6k样本），可能影响泛化结论的稳定性。

## 2. Data-Efficient Adaptation of LLMs via Attention Head Reweighting

- Source: arxiv
- arXiv ID: 2607.13425
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.13425v1
- PDF: https://arxiv.org/pdf/2607.13425v1
- DOI: https://doi.org/10.48550/arXiv.2607.13425

### Authors

Tuomas Oikarinen, Zixiao Chen, Charlotte Siska, Tsui-Wei Weng, Chandan Singh, Jianfeng Gao

### Abstract

Learning effectively from limited data is critical in domains like security where labeled examples are scarce. Large language models (LLMs) have demonstrated some capabilities for data-efficient learning, especially through parameter-efficient adaptation methods, but continue to struggle when faced with few samples for difficult tasks. To meet this challenge, we propose Attention Head Reweighting (AHR), a data-efficient method that adapts LLMs to new text-classification tasks by learning only a single scalar per attention head. This drastically reduces the number of parameters that need to be learned by making use of the functional specialization of individual attention heads. Experiments on diverse open-source text classification datasets show that AHR can outperform standard baselines like LoRA when learning from limited samples, despite having 200-1000x fewer trainable parameters, as our AHR only modifies ~0.0001% of the model's parameters. In addition, our learned weights are easy to interpret and can be analyzed to better understand the mechanisms and attention heads responsible for in-context learning abilities in LLMs.

### 中文一句话结论
AHR通过为每个注意力头学习一个标量权重，在极少量样本下高效微调LLM进行文本分类，以极少的参数量超越LoRA等基线方法。

### English TL;DR
Attention Head Reweighting (AHR) adapts LLMs to text classification tasks by learning only one scalar per attention head, drastically reducing parameters while outperforming standard methods like LoRA in few-shot settings.

### 中文详细总结
本文提出注意力头重加权（AHR），一种面向文本分类任务的数据高效LLM微调方法。AHR为每个注意力头引入一个可学习的标量参数β（初始化为0），用于缩放该头对残差流的贡献。训练时仅更新β，其余参数全部冻结，并结合L1/L2正则化防止过拟合。此外，采用上下文微调（IC-FT）策略，利用少量示例构建提示，最大化答案标记的概率。实验在GPT-2 XL、Llama-3.2 1B/3B、Qwen3 8B四个模型上进行，涵盖六个文本分类数据集（包括网络安全相关任务）。结果表明，在训练样本≤100时，AHR平均准确率比LoRA、AdaLoRA、IA3等基线高约3%，在网页钓鱼检测和越狱检测任务上提升达6-7%；其可训练参数仅为LoRA的1/200至1/1000，约占模型总参数的0.0001%。IC-FT进一步将准确率提升约10%。此外，学得的权重易于解释，可用于分析任务特定头与通用上下文学习头的贡献。

### 方法 / 贡献
- **方法**：AHR修改多头注意力的更新规则，为每个头增加可学习标量β（初始为0），仅训练这些标量参数，其余预训练参数及MLP层冻结；使用L1/L2范数正则化；结合上下文微调（IC-FT），在少量样本上下文中最大化答案标记的似然。
- **贡献**：提出极参数高效的微调方法（仅修改约0.0001%模型参数），在极少量样本下避免过拟合，并在多个文本分类任务上超越LoRA等基线；具有可解释性，能揭示任务特定头与通用上下文学习头的功能；在网络安全等低资源场景下表现突出。

### 实验或数据
- **模型**：GPT-2 XL（15亿参数）、Llama-3.2 1B、Llama-3.2 3B、Qwen3 8B。
- **数据集**：SST2（情感二分类）、AG-News（新闻四分类）、Emotion（六类情感）、Webpage Phishing（钓鱼URL二分类）、Toxigen（有害评论二分类）、Jailbreak Detection（越狱提示二分类）。从各数据集中随机采样少量训练样本（≤100个）进行微调，在完整测试集上评估。
- **结果**：AHR在少于100样本时平均准确率比LoRA高约3%；在Web和Jailbreak任务上高6-7%；当训练样本增至100时性能接近。IC-FT带来约10%额外提升。可训练参数数量：GPT-2 XL上1200个，Llama-3.2-1B上512个，Qwen3-8B上1152个，而LoRA对应为30万至48万个。

### 值得关注点
- **极低参数量**：仅需训练512-1200个参数，比LoRA少200-1000倍，却能在少样本任务上取得更好表现。
- **可解释性**：学得的β权重可直接分析，识别对任务至关重要的注意力头（如用于上下文学习的归纳头）。
- **安全领域应用**：在钓鱼检测和越狱检测等数据稀疏的关键安全任务上表现优异。
- **上下文微调兼容**：IC-FT可独立于微调方法使用，进一步提升了少样本学习效果。

### 局限性
- 仅针对文本分类任务进行验证，尚未探索生成式任务（如问答、摘要）的适用性。
- 正则化超参数λ需针对不同任务细心调整。
- 随着训练样本增多（约100个以上），AHR的性能优势逐渐消失，不如LoRA等可训练参数更多的方法。
- 方法依赖于注意力头的功能特化，对于头之间冗余度高或功能混叠的模型可能效果有限。

## 3. Constraint-Aware Counterfactual Editing for Aspect-Based Sentiment Analysis

- Source: arxiv
- arXiv ID: 2607.13977
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.13977v1
- PDF: https://arxiv.org/pdf/2607.13977v1
- DOI: https://doi.org/10.48550/arXiv.2607.13977

### Authors

S M Rafiuddin, Vamsi Krishna Pavuluri, Atriya Sen

### Abstract

Aspect-Based Sentiment Analysis (ABSA) requires models to identify sentiment toward specific aspects rather than relying on the global polarity of a sentence. This makes counterfactual evaluation especially challenging: a valid counterfactual should flip the sentiment of one target aspect while preserving the sentiment of all non-target aspects, semantic meaning, fluency, and factual consistency. Existing counterfactual generation methods often focus on sentence-level label flipping and may produce edits that are fluent but aspect-invalid, semantically drifting, or contradictory. To address this limitation, we propose CAVE-ABSA, a Constraint-Aware Validated Editing framework for generating and validating aspect-level counterfactuals. CAVE-ABSA localizes the opinion span associated with the target aspect, performs controlled counterfactual rewriting, refines candidates through a repair module, and filters them using aspect-level verification, semantic similarity, AMR-guided structural preservation, edit minimality, fluency, and contradiction detection. The framework is designed to construct validated counterfactual ABSA datasets for robustness evaluation and data augmentation. By explicitly separating generation from validation, CAVE-ABSA provides a principled approach for producing meaningful aspect-local counterfactuals and for testing whether ABSA models truly rely on aspect-grounded sentiment reasoning.

### 中文一句话结论
提出CAVE-ABSA框架，通过约束感知的生成与验证流程，为细粒度情感分析生成有效且符合多方面约束的反事实样本。

### English TL;DR
CAVE-ABSA is a constraint-aware framework that generates and validates aspect-level counterfactuals for ABSA by enforcing target sentiment flipping, non-target preservation, semantic similarity, fluency, minimality, and contradiction avoidance to produce meaningful, robust evaluation and data augmentation resources.

### 中文详细总结
本文聚焦于细粒度情感分析（ABSA）中的反事实评估问题。现有反事实生成方法多针对句子级标签翻转，无法保证在翻转目标方面情感的同时，维持非目标方面情感、语义、流畅性和事实一致性。为此，作者提出CAVE-ABSA框架，该框架包含五个阶段：意见跨度定位、受控反事实改写、修复模块、AMR引导的结构保持以及基于约束的验证。通过严格的多约束检查（目标方面翻转、非目标方面保持、语义相似度、编辑最小性、流畅性、矛盾检测），筛选出高质量的反事实样本。框架将生成与验证明确分离，旨在为ABSA模型的鲁棒性评估和数据增强提供可靠资源。

### 方法 / 贡献
- 形式化ABSA反事实编辑为约束生成问题，要求目标方面翻转、非目标方面保持、语义一致性、流畅性、最小编辑和矛盾避免。
- 提出CAVE-ABSA框架，采用意见跨度定位、受控改写、修复、AMR结构检查和多方面验证的混合流程。
- 引入复合评分机制，综合目标翻转置信度、非目标一致性、语义相似度、流畅性、编辑最小性、AMR结构保持和矛盾惩罚。
- 明确将生成与验证分离，为鲁棒性评估和数据增强提供经过验证的反事实ABS数据集。

### 实验或数据
摘要中未提及具体实验或数据集，仅描述了框架设计；论文后续部分可能包含实验，但本文摘要未提供。

### 值得关注点
- 将反事实生成从句子级扩展到方面级，提出更严格的约束条件。
- 使用AMR（抽象语义表示）作为语义结构保持的信号，提升编辑的语义一致性。
- 通过生成与验证分离的模块化设计，确保输出样本的可靠性和可解释性。
- 框架可用于构建经过验证的反事实数据集，服务于ABSA模型的鲁棒性测试和训练增强。

### 局限性
- 摘要中未报告实验验证，框架的实际效果和鲁棒性尚待评估。
- 框架依赖多个外部模型（如情感分类器、语义相似度模型、AMR解析器、流畅性检测器等），可能引入额外误差和计算开销。
- 约束条件较多，可能导致生成通过率低，难以规模化应用于大规模数据集。

## 4. A POS Tier Is the Key to Automated Annotation for Low-Resource Language Documentation: Neural Interlinear Glossing for Irabu, a Southern Ryukyuan Language

- Source: arxiv
- arXiv ID: 2607.13372
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.13372v1
- PDF: https://arxiv.org/pdf/2607.13372v1
- DOI: https://doi.org/10.48550/arXiv.2607.13372

### Authors

Michinori Shimoji

### Abstract

Discourse data are the primary empirical basis of grammar writing in field linguistics, but producing interlinearized text is notoriously expensive - on the order of one hour of work per minute of recording. For endangered languages, where the time remaining to verify analyses with native speakers is itself limited, automating parts of the interlinearization workflow has direct documentary value. We implement a full neural annotation pipeline (morpheme segmentation, POS tagging, glossing) for Irabu Ryukyuan using deliberately small, transparent BiLSTM-CRF models, and evaluate it under a realistic hard constraint: approximately one hour of fully annotated discourse as the entire supervised resource. Two factors of the annotation itself are manipulated: its richness (with or without a POS tier) and its quantity (training budgets from 6 to 47 minutes). Gold POS improves grammatical glossing by +4.4 (SD 0.7) points (significant in all 5 seeds), and the gain grows as data shrink (+11.6 points at a quarter of the data); a POS tier more than halves the amount of glossed data needed to reach a given accuracy. In a fully automatic pipeline this gain is not yet realized: the tagger still errs on 12% of morphemes, and an incorrect POS misleads the glossing model more than no POS at all. The value is latent rather than lost: degrading gold POS with controlled noise shows the gain returning as tagger accuracy rises, with break-even near our tagger's current 88% and +1.6 to +3.2 points recovered at 92-96%. We conclude with a concrete recommendation for documentation practice: annotate quadrilinearly - text, POS, gloss, translation.

### 中文一句话结论
在低资源语言（如伊良部琉球语）的自动注记中，加入词性层（POS tier）能显著提升语法标注准确率，尤其在标注数据极少的条件下，建议采用四行注记（文本、词性、语法标注、翻译）以实现最大文献学回报。

### English TL;DR
This paper demonstrates that adding a part-of-speech tier to interlinear glossing significantly boosts neural model accuracy for low-resource languages like Irabu Ryukyuan, especially with minimal training data, concretely recommending quadrilinear annotation to maximize documentary return under realistic annotation budgets.

### 中文详细总结
本研究针对濒危语言文献记录中的“注记瓶颈”（每1分钟录音约需1小时专家工作），构建了包含语素切分、词性标注和语法标注的完整神经注记流水线（基于小型BiLSTM-CRF模型），并以伊良部琉球语为对象进行实验。核心实验在“约1小时标注语料”这一现实约束下进行，系统性地操纵了两个变量：
1. **注记丰富性**：是否包含词性层（四行注记 vs. 三行注记）
2. **注记数量**：训练预算从6分钟到47分钟不等

主要发现包括：
- 金标准词性（Gold POS）可将语法标注准确率提升+4.4±0.7个百分点（5个随机种子均显著）
- 当训练数据减少至四分之一时，词性带来的增益跃升至+11.6个百分点
- 词性层可使达到相同准确率所需的标注数据量减半以上
- 但在全自动流程中，当前词性标注器约12%的错误率抵消了这一增益——错误词性甚至比无词性更差
- 通过噪声注入实验发现，当词性标注准确率达到约88%时可实现盈亏平衡，达到92-96%时可恢复+1.6至+3.2个百分点的增益

基于实验结果，作者提出具体建议：在文献实践中采用四行注记（文本、词性、语法标注、翻译），并设计“两阶段工作流”——先精心标注约30分钟语料，然后利用流水线自动草拟剩余部分，再由语言学家审核修正。

### 方法 / 贡献
**方法**：使用小型BiLSTM-CRF序列标注器构建完整流水线（语素切分→词性标注→语法标注），故意避免使用大型预训练Transformer模型，原因有二：濒危语言数据规模极小（本语料转录层仅约26KB），且小型模型的可解释性更适合语言学家工作流。

**贡献**：
1. 为低资源琉球语提供了完整、可复现的神经注记流水线
2. 通过控制消融实验，量化了词性信息对语法标注的实际增益（+4.4±0.7点）
3. 进行了错误传播分析，揭示了当前词性标注器错误抵消增益的机制
4. 通过噪声注入实验定位了词性标注器的盈亏平衡点（约88%准确率）
5. 提供了数据规模分析，展示词性增益在数据减少时反而增大
6. 提出具体的四行注记建议及两阶段工作流设计，并实现了浏览器原型工具

### 实验或数据
**数据集**：伊良部琉球语自然话语语料，总计774个话语单元，训练部分约620个话语单元（对应约47分钟录音）。实验中测试了从6分钟到47分钟共5个子预算。

**实验设计**：
1. **词性层价值实验**（RQ1）：对比有无金标准词性时语法标注准确率
2. **数据规模实验**（RQ2）：从6到47分钟5个预算层级，交互分析词性增益
3. **全自动流水线评估**：包含真实词性标注器错误的影响
4. **噪声注入实验**：以受控方式降低金标准词性准确率，模拟词性标注器不同性能水平

**定量结果**：
- 语素切分 span-F1：0.907
- 词性标注准确率：0.881
- 语法标注准确率（金标准词性条件下）：0.93
- 无词性基线时语法标注准确率：约0.886
- 词性增益在数据减少至四分之一时：+11.6点

### 值得关注点
1. **悖论性发现**：金标准词性带来显著增益，但当前标注器的错误反而使其劣于无词性方案——这并非否定词性的价值，而是指出当前标注器需要提升
2. **数据规模与词性增益的反向关系**：数据越少，词性层越有价值——这恰恰是文献项目起步时的典型场景
3. **具体操作建议**：不是“尽可能多收集语料”的模糊建议，而是给出“先精心标注约30分钟的四行数据”的量化指导
4. **两阶段工作流的实用性**：既承认当前自动标注的局限，又提供了实际可行的“人机协作”路径
5. **可解释性设计**：BiLSTM-CRF的结构使每个语素的错误可诊断，便于语言学家理解并修正模型输出

### 局限性
1. 本实验仅基于单一语言（伊良部琉球语），结论的泛化性有待验证
2. 模型未与大型预训练Transformer或LLM方法进行同等标注预算下的比较（作者明确承认这是未来工作）
3. 词性标注器当前准确率（88%）恰好位于盈亏平衡点附近，导致全自动流程的增益尚未实现
4. 两阶段工作流虽已概念验证，但其在真实文献项目中的实际效率提升和用户体验尚未经过系统评估
5. 实验仅考察了约1小时标注语料的极限情况，更大规模数据下的表现未知
6. 词性标注错误对语法标注的误导机制（错误词性比无词性更差）仅得到定量描述，深层语言学和模型原因尚未完全解析

## 5. Meta-Learning Preferences for Multilingual LLM Alignment

- Source: arxiv
- arXiv ID: 2607.13315
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.13315v1
- PDF: https://arxiv.org/pdf/2607.13315v1
- DOI: https://doi.org/10.48550/arXiv.2607.13315

### Authors

Jiaying Lin, Seongho Son, Nam Phuong Tran, Long Tran-thanh, Ilija Bogunovic, Debmalya Mandal

### Abstract

Unequal availability of human preference data across languages poses a significant challenge for aligning large language models in multilingual settings. To address the lack of sufficient data in low-resource language alignment, we propose a meta-learning framework for Reinforcement Learning from Human Feedback and Direct Preference Optimization. By leveraging preference data from other languages, our framework learns a transferable initialization that enables effective adaptation to a target language with minimal data. We provide theoretical guarantees for both the meta-reward modeling and meta-policy optimization settings, and empirically demonstrate the effectiveness of our approach on multilingual benchmarks. In an extremely low-resource setting with only 100 target-language preference samples, our approach achieves up to $28\%$ win-rate improvements over baseline methods, and consistently outperforms baselines across multiple target languages and model scales. Our approaches retain these advantages across different combinations of meta-training languages and varying linguistic distances from the target languages.

### 中文一句话结论
本文提出元学习框架，利用多语言偏好数据学习可迁移初始化，在仅有100个目标语言样本时实现了最高28%的胜率提升。

### English TL;DR
This paper proposes a meta-learning framework for multilingual LLM alignment that learns a transferable initialization from high-resource languages, enabling effective adaptation to low-resource target languages with as few as 100 preference samples and achieving up to 28% win-rate improvements over baseline methods.

### 中文详细总结
多语言环境下人类偏好数据分布不均，导致低资源语言对齐效果差。本文提出基于元学习的对齐框架，将每种语言视为一个任务，通过梯度元学习（MAML）从高资源语言中学习可迁移的初始化参数，实现仅需少量目标语言样本的快速适应。方法同时适用于RLHF（元奖励建模）和DPO（元策略优化），并提供了首个针对Bradley-Terry损失的理论收敛保证。实验使用270M和7B参数的开放LLM，在多个语言基准上验证：100个目标语言样本下，MAML-DPO的胜率最高提升28%，且优于直接微调和多任务训练基线；优势在不同语言组合与语系距离下保持稳定。

### 方法 / 贡献
1. 提出统一的元学习框架（MAML-RLHF/MAML-DPO），将多语言对齐建模为任务自适应问题。  
2. 首次为Bradley-Terry损失下的MAML提供收敛性理论证明。  
3. 在极低资源（100样本）下实现最高28%的性能提升。  
4. 验证初始化参数的跨语言可迁移性，不依赖于源语言与目标语言的语系接近度。

### 实验或数据
使用多语言指令遵循基准（如HellaSwag、MMLU等），在270M和7B参数的开放LLM上评估。设置低资源场景（目标语言仅100个偏好样本），并测试不同元训练语言组合（如英语、法语、德语等）及不同语系距离。结果显示MAML-DPO在多数目标语言上稳定优于RLHF/DPO基线，且随适应数据量增至1k+样本仍保持优势。

### 值得关注点
- 首次将元学习系统应用于多语言偏好对齐，并给出理论保证。  
- 极低样本下（100条）的显著增益（28%胜率提升），实际部署价值高。  
- 跨语言可迁移性不依赖语系接近，表明学到的初始化具有泛化能力。  
- 同时覆盖两种主流对齐范式（RLHF和DPO），框架通用。

### 局限性
摘要中未明确讨论局限性。基于方法特点可推测：需要多个高资源语言的偏好数据进行元训练，可能增加计算开销；理论保证限于特定假设；大规模模型（如70B）上的效果和计算可行性尚未验证。

## 6. Fine-grained CLIP fine-tuning with self-annotated region alignment

- Source: arxiv
- arXiv ID: 2607.13661
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.13661v1
- PDF: https://arxiv.org/pdf/2607.13661v1
- DOI: https://doi.org/10.48550/arXiv.2607.13661

### Authors

Chenyang Zhao, Wei Lin, Antoni B. Chan, Janet H. Hsiao

### Abstract

Contrastive Language-Image Pre-training (CLIP) has been shown to have limitations in its fine-grained dense feature representation, due to its pre-training focusing on matching the whole image to a text description. Considering the large data and computational burden in pre-training a vision-language model from scratch, a series of works aim to enhance the fine-grained ability of CLIP through a fine-tuning scheme. However, existing works suffer from a variety of limitations: additional region annotations are usually required, which limits the semantic diversity due to the predefined categories and leads to a large effort to process the training data; and they usually sacrifice CLIP's original ability for global visual representation. To bypass these limitations, we propose SFF-CLIP (Self-annotated Fine-grained Fine-tuning for CLIP), which only uses image-text pairs as input to boost the fine-grained representation ability in the CLIP fine-tuning, while maintaining the global visual-semantic consistency. Concretely, a run-time region-phrase alignment scheme is designed, which obtains concept phrases from the input sentence, and aligns them with corresponding extracted region-based features using text-specific heat maps. Extensive experiments demonstrate that SFF-CLIP leads to significant performance improvements on fine-grained dense feature representation, as well as maintaining the performance of the original CLIP on image-level tasks. Code will be released later.

### 中文一句话结论
本文提出SFF-CLIP，通过运行时自标注区域-短语对齐方案，仅使用图像-文本对即可提升CLIP的细粒度表示能力，同时保持其全局视觉-语义一致性。

### English TL;DR
SFF-CLIP fine-tunes CLIP using only image-text pairs with a self-annotated region-phrase alignment scheme to enhance fine-grained dense feature representation while maintaining global visual-semantic consistency.

### 中文详细总结
CLIP由于预训练聚焦于整图与文本匹配，其细粒度密集特征表示能力有限。现有通过微调增强CLIP细粒度能力的方法往往需要额外区域标注（如预定义类别或区域提议），这不仅限制了语义多样性，还增加了数据处理成本，且常牺牲CLIP的全局表示能力。为克服这些局限，本文提出SFF-CLIP，仅使用图像-文本对作为输入，在微调过程中通过运行时自标注区域-短语对齐方案提升细粒度表示。具体地，从输入句子中提取概念短语，并利用文本特定热图生成对应区域特征，再通过匹配损失对齐区域-短语对。同时，保留原CLIP的全局对比学习目标以维持图像级任务性能。实验表明，SFF-CLIP在开放词汇目标检测和分割等密集预测任务上显著超越以往方法，并在图像级任务上保持与原CLIP相当的表现。

### 方法 / 贡献
- 提出SFF-CLIP，一种自标注细粒度微调策略，无需额外区域标注（如预定义类别、区域提议或描述生成）。
- 设计运行时区域-短语对齐方案：从输入文本中提取短语，通过Grad-ECLIP等视觉解释方法生成文本特定热图，聚合得到区域特征，并与短语特征对齐。
- 在微调中联合优化细粒度对齐损失和全局对比学习损失，确保模型在提升区域感知能力的同时不损害全局表示能力。
- 在密集预测（开放词汇检测/分割）和图像级任务上均取得领先性能。

### 实验或数据
- 实验涵盖开放词汇目标检测（如使用OV-COCO、OV-LVIS等数据集）和开放词汇语义分割任务，以及图像级分类和检索任务。
- 结果表明SFF-CLIP在细粒度密集特征表示上显著优于CLIPSelf、FineCLIP等先前方法，同时在图像级任务上保持与原CLIP几乎一致的表现。
- 消融实验验证了自标注对齐方案、全局对比损失权重等关键设计的作用。

### 值得关注点
- 仅依赖图像-文本对，无需任何人工区域标注或外部模型，极大降低了数据准备成本。
- 运行时自我标注机制避免了预定义类别的语义限制，支持开放词汇场景。
- 成功在提升细粒度能力的同时维持了CLIP的全局表示能力，解决了此前方法的常见权衡。

### 局限性
- 论文未明确讨论局限性，但可能依赖于文本中短语的准确解析以及热图生成的质量，对复杂场景或多词短语的对齐效果需进一步验证。
- 当前方法基于ViT架构，对CNN架构的适用性未分析。

## 7. Consensus as Privileged Context for Label-Free Self-Distillation

- Source: arxiv
- arXiv ID: 2607.13643
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.13643v1
- PDF: https://arxiv.org/pdf/2607.13643v1
- DOI: https://doi.org/10.48550/arXiv.2607.13643

### Authors

John Gkountouras, Josip Jukić, Ivan Titov

### Abstract

Sampling multiple solutions and returning the majority answer is among the most reliable ways to improve the reasoning accuracy of large language models without labels, and a growing family of methods converts this consensus signal into training supervision. However, existing approaches use consensus only in restricted forms: as a filter that selects solutions for fine-tuning, as a preference between answers, or as a scalar reward for reinforcement learning, discarding most of the information that the agreeing solutions contain. We present CANON (Consensus-ANchored self-distillatiON), a label-free training method that turns consensus into dense, token-level supervision. For each unlabeled prompt, CANON samples multiple solutions, extracts the majority answer, and conditions a frozen snapshot of the model on a solution that reaches it; this consensus-anchored teacher then supervises the model on its own rollouts at every token. Experiments on mathematical and scientific reasoning benchmarks show that CANON improves pass@1 by up to 12 points, outperforming label-free reinforcement learning by 6 points at a seventh of its compute and approaching a teacher conditioned on gold solutions; trained on pooled unlabeled data, it transfers to held-out benchmarks, matching training methods that use gold labels. Analysis suggests that the improvements are not pure distribution sharpening: after training, the model solves problems it previously never solved in 32 attempts, and its majority vote itself becomes more accurate.

### 中文一句话结论
CANON 是一种无需标注的自蒸馏方法，通过将多数投票共识转化为逐 token 的稠密监督信号，在数学与科学推理任务上显著提升了模型性能，且计算成本远低于无标签强化学习。

### English TL;DR
CANON is a label-free self-distillation method that turns majority-vote consensus among sampled solutions into dense, token-level supervision, boosting reasoning accuracy by up to 12 points while using a fraction of the compute of label-free reinforcement learning.

### 中文详细总结
本文提出 CANON（Consensus-ANchored self-distillatiON），一种无需人工标注的训练方法。核心思路是：对于每个无标签的提示，模型先生成多个候选解法，提取其中多数回答作为“共识”。然后，冻结模型的一个快照，将其作为“教师”，并让该教师以共识解法为条件（即“共识锚定”）来生成输出。学生模型则通过与教师输出的逐 token 对数似然进行蒸馏来学习。这种方法相比以往仅将共识用作筛选或偏好信号的方法，更好地利用了共识中富含的信息。

在数学与科学推理基准上的实验表明，CANON 将 pass@1 提升了最多 12 个百分点，且比无标签强化学习方法高出 6 个百分点，而计算成本仅为后者的七分之一。当在多个无标签数据集上联合训练时，CANON 能迁移到未见过的基准任务上，表现可与使用黄金标签（gold labels）的训练方法相媲美。分析还发现，CANON 带来的提升不仅仅是分布锐化（distribution sharpening）：训练后，模型能够解决之前即使进行 32 次采样也从未解出的问题，并且其多数投票本身的准确性也有所提高。

### 方法 / 贡献
- **方法**：提出 CANON 框架，利用多数投票共识作为“锚”，构建基于共识的教师模型，对学生的每一个 token 提供稠密监督（逐 token 蒸馏）。
- **贡献**：首次将共识信息从粗粒度的筛选/偏好/奖励信号扩展到稠密、逐 token 的分布监督，显著提高了无标签场景下的推理能力，同时计算效率高。

### 实验或数据
- **数据集**：在数学与科学推理基准上评估（具体名称未在摘要中详列）。
- **实验结果**：
  - pass@1 提升最多 **12 个百分点**。
  - 比无标签强化学习（RL）高 **6 个百分点**，计算成本为后者的 **1/7**。
  - 对多个无标签数据集进行联合训练后，能迁移到新基准，性能与使用黄金标签的方法相当。
- **分析发现**：训练后模型能解决之前 32 次采样都失败的问题，且多数投票准确性提升。

### 值得关注点
- **高信息利用效率**：将多数投票转化为稠密监督，而非简单的筛选或奖励信号，充分利用了共识中的多数信息。
- **显著的计算优势**：相比无标签 RL，以七分之一的计算量取得更高的性能，实际可用性强。
- **无需标签的强泛化能力**：在多种无标签数据上训练后，能迁移到未见基准，性能堪比有监督学习，极具应用潜力。
- **超越分布锐化**：提升不仅来自压缩分布，而是模型真正获得了解决新问题的能力。

### 局限性
- 摘要未明确讨论 CANON 对模型规模、初始能力或推理任务类型的适用范围与限制。
- 未提及对模型可能生成的错误共识（即多数答案错误）的鲁棒性处理。
- 实验任务仅限于数学与科学推理，其他类型推理任务（如常识问答、多步逻辑推理）的效果不明。

## 8. When Rubrics Change: Cross-Rubric Generalization for Critical Thinking Essay Scoring

- Source: arxiv
- arXiv ID: 2607.13433
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.13433v1
- PDF: https://arxiv.org/pdf/2607.13433v1
- DOI: https://doi.org/10.48550/arXiv.2607.13433

### Authors

Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun, Andrew Lan

### Abstract

Automated essay scoring (AES) research has largely focused on cross-prompt generalization, where essays from unseen prompts are scored while the scoring criteria are typically held constant. In practice, however, educators may revise or even introduce new rubrics in their scoring task, to evaluate different aspects of essays. We study cross-rubric generalization: training on essays labeled under one set of rubrics and evaluating on previously unseen rubrics, which target different aspects of the essay. We use a Large Language Model (LLM) fine-tuning framework with two components: rubric-agnostic intermediate representations, called traits, and target-essay supervision under seen rubrics during training. On an AES dataset augmented with multiple rubric-defined labels of student critical thinking skills, we find that traits improve macro F1 by 5.0% over a baseline without traits in the hardest setting, where both target rubrics and target essays are unseen during training. We further find that increasing target-essay supervision improves performance, with our best fine-tuned open-source Llama-based model outperforming GPT-5-mini prompting by 2.1% macro F1 and trailing GPT-5 by 1.9%. These results show that trait-based intermediate structure and controlled supervision improve generalization to unseen rubrics.

### 中文一句话结论
本研究提出了一种跨评分标准泛化框架，通过引入评分标准无关的中间特征（traits）和目标文本监督，显著提升了大型语言模型在评判未见评分标准时的自动化论文评分性能。

### English TL;DR
This paper introduces a cross-rubric generalization framework for automated essay scoring, using rubric-agnostic intermediate representations (traits) and target-essay supervision to improve LLM fine-tuning performance on previously unseen scoring criteria.

### 中文详细总结
该研究聚焦于自动化论文评分（AES）中的新问题：跨评分标准泛化。与传统的跨提示泛化不同，当教师修改或引入新的评分标准时，模型需要根据未见过的评分标准对论文进行评分。研究者采用基于大型语言模型（Llama 3.1 8B Instruct）的微调框架，包含两个关键组件：
1. **评分标准无关的中间特征（traits）**：基于论证理论和批判性思维理论，定义了六种通用特征（如主张明确性、结构连贯性、证据支持、证据与主张关联性、替代视角考虑、分析深度），这些特征在所有评分标准中共享，作为论文与评分标准标签之间的桥梁。
2. **目标文本监督**：在训练过程中，通过不同级别的目标论文标注进行监督，从最难的完全未见目标论文（No Labels），到使用自动生成标签（Pseudo Labels），再到使用人工标注标签（Gold Labels）。
在包含500篇学生论文、六种评分标准的批判性思维数据集上，实验表明：在最困难的设置下，traits将宏F1分数提升了5.0%；增加目标论文监督能持续提升性能，最优的微调Llama模型在宏F1上比GPT-5-mini提示方法高2.1%，比GPT-5低1.9%。

### 方法 / 贡献
- **任务定义**：形式化了跨评分标准泛化问题，要求模型在训练时未见目标评分标准的情况下，对论文进行评分。
- **特征设计**：提出六种评分标准无关的中间特征（traits），基于论证理论和批判性思维理论，捕获论文的基础论证属性，作为泛化的桥梁。
- **框架构建**：采用LLM微调框架，将traits以输入或输出形式融入模型训练，系统研究了不同级别的目标文本监督对泛化性能的影响。
- **贡献**：首次系统研究跨评分标准泛化问题，揭示了traits和受控监督对提升模型泛化到未见评分标准能力的重要性。

### 实验或数据
- **数据集**：使用Peczuh等人2025年的批判性思维评分数据集，包含500篇6-12年级美国学生的论证性写作（来自PERSUADE 2.0语料库），涵盖公民、科学和社会主题。数据集定义了六种评分标准，分为三个技能（信息分析、论据生成、逻辑推理），每种技能对应两种评分标准，采用0-4分制。
- **实验设置**：分为三种监督设置：No Labels（目标论文完全未见）、Pseudo Labels（使用自动生成标签）、Gold Labels（使用人工标注标签）。评估指标为宏F1分数。
- **实验结果**：在No Labels设置下，traits提升宏F1分数5.0%；最优模型（使用traits和Gold Labels）比GPT-5-mini提示法高2.1%，比GPT-5低1.9%。研究未提及额外实验数据集。

### 值得关注点
- **问题创新性**：首次系统研究AES中的跨评分标准泛化，而非传统跨提示泛化，更贴近教育实践需求。
- **特征设计理论依据**：traits基于成熟的论证理论和批判性思维框架，具有可解释性和可迁移性。
- **监督设置系统分析**：通过三种监督级别，定量揭示了目标论文数据对泛化的影响。
- **开源模型竞争力**：微调的开源Llama模型性能接近甚至超越闭源GPT-5，展示了LLM微调的潜力。
- **代码开源**：研究代码已公开在GitHub，便于复现和扩展。

### 局限性
- 研究仅在一个数据集上验证（500篇论文），缺乏跨数据集和更大规模样本的泛化验证。
- traits标注为自动生成（silver labels），未经人工验证，其质量可能影响性能。
- 数据集中六种评分标准均与批判性思维相关，traits的设计可能仅限于该领域，未测试在更广泛AES任务中的适用性。
- 研究聚焦于6-12年级学生论文，未探讨其他年龄段或教育背景的泛化能力。
- LLM微调框架依赖自然语言评分标准描述，可能对描述质量敏感（未充分消融）。

## 9. DeltaMerge-LowRes: Composing Language and Task Deltas for Low-Resource Adaptation

- Source: arxiv
- arXiv ID: 2607.13967
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.13967v1
- PDF: https://arxiv.org/pdf/2607.13967v1
- DOI: https://doi.org/10.48550/arXiv.2607.13967

### Authors

Son Ha Xuan, Xuan-Bach Le, Phat T. Tran-Truong

### Abstract

Adapting a multilingual encoder to a new language \emph{and} a new task with only a few hundred gold examples is a common low-resource NLP setting, yet the two axes are usually fused via an expensive language--task fine-tuning run. We ask whether they can instead be trained separately and recombined in weight space. \DeltaMergeLowRes{} learns a language delta $Δ_L$ from unlabeled monolingual text and a task delta $Δ_T$ from labeled English data, then composes them at inference under one of four rules: additive, activation-guided, sparsity-aware, and a novel \emph{cross-axis TIES}. The new rule adapts the TIES-Merging steps of trimming, sign election, and merging to the language and task axes rather than to two task axes. Holding $(Δ_L,Δ_T)$ fixed across rules on four task families and four African languages ($158$ evaluated cells, $10{,}000$-sample paired bootstrap per cell), we find: (i) cross-axis TIES wins summarisation on $3/4$ languages by $+4$ to $+7$ chrF (chrF $18.59$ vs.\ $13.80$ task-only); (ii) it improves QA F1 by $+2.32$ and EM by $+2.91$; and (iii) sparsity-aware merging cuts classification ECE by $36\%$ at parity macro-F1. The composition rule materially changes what the merged model preserves, suppresses, and calibrates. We release all JSON traces and a claim ledger.

### 中文一句话结论
DeltaMerge-LowRes 通过分别训练语言增量和任务增量，并使用跨轴 TIES 合并规则，在低资源非洲语言上显著提升了摘要和问答任务的性能，同时稀疏感知合并改善了分类校准。

### English TL;DR
DeltaMerge-LowRes separately trains language and task deltas and composes them via novel merging rules—especially cross-axis TIES—to achieve strong low-resource adaptation across tasks and African languages, with cross-axis TIES boosting summarisation and QA performance while sparsity-aware merging improves classification calibration.

### 中文详细总结
针对多语言编码器同时适应新语言和新任务时通常需要昂贵联合微调的问题，本文提出 DeltaMerge-LowRes 方法。该方法将语言适应和任务适应解耦：从无标注单语言文本学习语言增量 Δ_L，从有标注英文数据学习任务增量 Δ_T，然后在推理时通过四种组合规则（加法、激活引导、稀疏感知、跨轴 TIES）在权重空间组合两者。跨轴 TIES 是本文新提出的规则，将 TIES-Merging 的修剪、符号选举和合并步骤应用于语言与任务轴而非两个任务轴。

实验在四个任务族（分类、命名实体识别、抽取式问答、摘要）和四种非洲语言（豪萨语、斯瓦希里语、约鲁巴语、阿姆哈拉语）上进行，共 158 个评估单元，每个单元使用 10,000 样本配对 bootstrap。结果表明：(i) 跨轴 TIES 在 3/4 语言上摘要 chrF 提升 +4 到 +7（chrF 18.59 对比纯任务 13.80）；(ii) 问答 F1 提升 +2.32，精确匹配提升 +2.91；(iii) 稀疏感知合并将分类期望校准误差降低 36%，宏 F1 持平。组合规则显著改变了合并模型保留、抑制和校准的内容。所有 JSON 追踪和声明账本已发布。

### 方法 / 贡献
- 定义并评估了跨轴 TIES：将 TIES-Merging 的修剪、符号选举和合并步骤应用于语言-任务增量对，而非两个任务增量对。
- 在固定 Δ_L 和 Δ_T 的前提下，严格比较了五种组合规则（纯任务、加法、激活引导、稀疏感知、跨轴 TIES），共 158 个带 bootstrap 的评估单元。
- 证明稀疏感知组合在分类校准上实现帕累托改进（ECE 降低 36% 且宏 F1 不降）。

### 实验或数据
- 基座模型：XLM-R-base（分类、NER、QA）和 mT5-base（摘要），全是 LoRA rank-16 更新。
- 任务族与数据：分类（MasakhaNEWS，英文 AG News 监督）、NER（MasakhaNER 2.0，英文 CoNLL-03 监督）、QA（AfriQA 风格，英文 SQuAD 监督）、摘要（XL-Sum，英文 XL-Sum 监督）。
- 语言：豪萨语、斯瓦希里语、约鲁巴语（编码器任务），加阿姆哈拉语（摘要）。单语文本来自公共爬行语料。
- 评估：每个语言-任务对使用官方测试集（253–987 样本），任务增量训练预算为 256 个英文标注样本。每个评估单元 10,000 次配对 bootstrap。
- 核心结果：跨轴 TIES 在摘要和 QA 上最佳；稀疏感知在分类校准上最佳。

### 值得关注点
- 跨轴 TIES 在生成式任务（摘要、QA）上显著优于其他规则，说明语言和任务信号需要协同时该规则更有效。
- 稀疏感知合并在不损失分类性能的前提下大幅降低校准误差，具有实用价值。
- 所有组合规则共享相同的 Δ_L 和 Δ_T 张量，差异完全来自组合方式，归因清晰。
- 实验覆盖 158 个单元且使用 bootstrap 统计检验，结论稳健。

### 局限性
- 仅比较了组合规则，未与端到端联合微调（Full FT / LoRA / 继续预训练+LoRA）在同等计算预算下进行对比，因此“合并是否优于微调”的问题未在此回答。
- 语言和任务覆盖面有限：仅四种非洲语言和四种任务族，泛化性有待验证。
- 跨轴 TIES 优于其他规则的解释仍为操作性假设，未通过独立实验严格验证。
- 所有增量均采用 LoRA rank-16 形式，不同秩或适配器结构下的表现未知。

## 10. Can an Old Dog Be Taught New Tricks? Taking LLMs Beyond Sentence Level Translation

- Source: arxiv
- arXiv ID: 2607.14040
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.14040v1
- PDF: https://arxiv.org/pdf/2607.14040v1
- DOI: https://doi.org/10.48550/arXiv.2607.14040

### Authors

Alaina Brandt

### Abstract

Automatic translation systems, from CAT tools to MT, overwhelmingly treat translation as a sentence-by-sentence act. This paper asks whether LLMs can be moved beyond that paradigm through whole-document, corpus-informed translation. We present PAT (Pragmatic Auto-Translator), a RAG-based system that pairs user-configured specifications with context from a comparable corpus of authentic longform texts in U.S. English and Latin American Spanish, passing retrieved paragraph-, section-, and document-level examples to an LLM for whole-document generation. The goal is draft translation for professional verification: target texts reformulated to fit their Spanish-language context, where discourse organization, rhetorical style, and pragmatic norms differ meaningfully from English. We evaluated six automatic translations of essays on generative AI across three projects using a customized MQM typology, assessed by two trained evaluators working from U.S. English into LATAM and Mexican Spanish. Results show that a limited prompt produced no meaningful reformulation, and specifications and corpus-informed translations at times showed substantial reformulation, though not always to effect. We find that LLMs can be moved toward reformulation and away from the sentence-by-sentence paradigm, though more work is needed to improve the effectiveness of those reformulations. In this paper, we discuss considerations related to automatic translation system design, corpus construction, and translation quality evaluation methodology and results.

### 中文一句话结论
本研究表明，通过结合语料库和用户规范的大模型（LLM）翻译系统（PAT），能够推动模型从逐句翻译转向整篇文档的重构，但重构效果尚不稳定，仍需进一步优化。

### English TL;DR
This paper introduces PAT, a RAG-based system that leverages whole-document, corpus-informed translation to move LLMs beyond the sentence-by-sentence paradigm, showing that while LLMs can be guided toward reformulation, further work is needed to improve the effectiveness of such reformulations for professional translation.

### 中文详细总结
本文针对自动翻译系统普遍采用逐句翻译的局限，提出通过整篇文档和语料库信息来引导大语言模型（LLM）进行重构式翻译。作者构建了PAT（Pragmatic Auto-Translator）系统，该系统基于检索增强生成（RAG），结合用户自定义的翻译规范和可比语料库（包含美式英语和拉丁美洲西班牙语的原创长文本），将检索到的段落、章节和文档级示例输入LLM，生成整篇文档的草稿翻译，供专业译员审核。研究评估了三个项目中共六篇关于生成式人工智能的论文的自动翻译，使用定制的MQM（多维质量指标）分类体系，由两名经过训练的评估员从美式英语翻译成拉丁美洲西班牙语和墨西哥西班牙语。结果显示，仅使用简单提示的翻译未产生有意义的重构；而结合规范和语料库信息的翻译有时能实现显著重构，但效果并不一致。作者认为，LLM可以被引导向重构方向发展，但需改进重构的有效性，并讨论了自动翻译系统设计、语料库构建和翻译质量评估方法等方面的考量。

### 方法 / 贡献
- **方法**：提出PAT系统，基于RAG架构，使用可比语料库（美式英语与拉丁美洲西班牙语原创长文本）和用户自定义规范（如主题、语言变体、文本类型、受众等），通过检索段落、章节和文档级示例，引导LLM进行整篇文档的生成，而非逐句翻译。系统选用Gemini 2.5 Pro作为翻译引擎，并采用jina-embeddings-v3进行多级嵌入检索。
- **贡献**：挑战了自动翻译中逐句处理的范式，展示了通过语料库和规范指导LLM进行篇章级重构的可行性；构建了PAT系统并公开了部分资源；为翻译质量评估提供了基于MQM的定制化方法，并指出了现有评估指标（如BLEU）的不足。

### 实验或数据
- **实验设置**：评估了三个项目，每个项目包含两篇关于生成式人工智能的论文，共六篇文档的自动翻译。翻译方向为美式英语到拉丁美洲西班牙语和墨西哥西班牙语。使用定制MQM分类体系，由两名经过培训且具有相同教育背景的评估员独立评估。
- **数据**：自建可比语料库PAT-GAI-Longform-ESP-419-ENG-USA，包含约20万词英语和22.5万词西班牙语，涵盖多种体裁的原创长文本（不含翻译或合成文本）。语料库以拉丁美洲西班牙语为主，亦包含少量墨西哥西班牙语、卡斯蒂利亚西班牙语和国际英语内容。
- **结果**：简单提示（仅“翻译此文本”）导致所有翻译均为逐句对应，无重构；结合规范和语料库的翻译有时出现显著重构（如段落合并、顺序调整、修辞风格改变），但效果不稳定，且部分重构未产生预期效果。评估员间一致性需进一步分析。

### 值得关注点
- **研究视角创新**：将翻译学中的“语用等价”和“对比修辞”概念引入LLM翻译，强调根据目标语言语境进行篇章级重构，而非词句对应。
- **系统设计亮点**：PAT系统模拟专业译员的工作流程，包括分析源文本、设定规范、利用语料库研究，最后生成翻译。通过避免使用“翻译”一词的提示策略，以及要求模型先理解全文再生成，减少逐句倾向。
- **评估方法**：使用定制的MQM分类体系，超越BLEU等自动指标，人工评估更关注自然度、连贯性和语用适切性。
- **模型选择依据**：通过对比实验发现不同LLM对重构指令的响应差异显著，Gemini 2.5 Pro因更遵循指令、保持重构立场而被选中，体现了模型训练方法论（如RLHF vs 自动化规则RL）对翻译行为的影响。

### 局限性
- **效果不稳定**：规范和语料库信息仅有时能产生显著重构，且重构效果未必符合预期，部分翻译仍有遗漏或不当调整。
- **评估规模有限**：仅评估了三个项目、六篇文档，且最终只有两名评估员（均针对美式英语到墨西哥西班牙语方向）的数据用于分析，评估员流失率高，可能影响结论的普适性。
- **语料库局限**：语料以拉丁美洲西班牙语为主，墨西哥西班牙语内容不足；语料库规模较小（约40万词），且包含少量翻译和AI生成内容，可能引入干扰。
- **嵌入模型不足**：使用的jina-embeddings-v3基于句子级预训练，缺乏对篇章内连贯模式的编码能力；当前长文本检索基准测试尚不完善，无法直接验证检索效果。
- **领域单一**：仅针对生成式人工智能领域的论文，结果能否推广至其他文本类型和语言对尚待验证。

## Processing Notes

- Duplicate papers skipped: 0