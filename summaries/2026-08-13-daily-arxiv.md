# Daily arXiv - 2026-08-13

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-13T23:10:42
- Paper count: 10

## 1. Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge

- Source: arxiv
- arXiv ID: 2608.12218
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.12218v1
- PDF: https://arxiv.org/pdf/2608.12218v1
- DOI: https://doi.org/10.48550/arXiv.2608.12218

### Authors

Arda Uzunoglu, Benjamin van Durme, Daniel Khashabi

### Abstract

Large language models are increasingly trained and deployed with long contexts that span documents, code repositories, and interaction histories. This scaling reflects the implicit assumption that training on longer contexts will only help the model by exposing it to richer evidence. We challenge this view by studying how the context window shapes a model's mode of learning, shifting it between parametric internalization and contextualization. We propose the Information Abundance Paradox, which hypothesizes that abundant relevant information in the training context can reduce the incentive to encode that information parametrically, thereby increasing reliance on context. In pretraining with long documents, increasing the context window improves language modeling, natural language understanding, and closed-book MCQA only up to an intermediate optimum, after which performance consistently declines. In supervised fine-tuning, more task-relevant train-time context improves performance with supporting context, but reduces robustness when context is absent or misleading at test time. Our analysis suggests that this behavior arises when longer context provides a lower complexity solution. Mechanistically, training with informative context shifts gradient pressure from feed-forward networks, often linked to parametric knowledge, toward attention modules, and causal interventions show that this shift increases reliance on context during inference. Overall, these findings support the Information Abundance Paradox and suggest that scaling toward near-infinite context is not simply a matter of supplying more data, even when high-quality long-context data is abundant.

### 中文一句话结论
训练时上下文越长并不总是越好：当相关信息过多时，模型会从“记忆到参数”转向“依赖上下文”，导致在上下文缺失或误导时性能下降，形成倒U型表现，即“信息丰裕悖论”。

### English TL;DR
The Information Abundance Paradox finds that training LLMs with longer contexts can shift learning from parametric internalization to contextualization, causing an inverted-U performance curve: longer context helps up to an intermediate optimum, then degrades robustness when context is absent or misleading.

### 中文详细总结
论文提出“信息丰裕悖论”：若训练上下文中包含大量任务相关信息，模型倾向于直接利用上下文来降低损失，而不是把知识编码进参数，从而减少参数化内化、增加对上下文的依赖。作者称之为“上下文成瘾”（context addiction），表现为有相关上下文时表现良好，但上下文缺失或误导时性能明显下降。

在预训练中，固定数据、算力和模型配置、仅改变上下文长度时，语言建模、自然语言理解和闭卷多项选择问答的表现呈倒U型：只在一定中间长度达到最优，继续加长反而稳定下降。在监督微调中，训练时提供更多任务相关上下文会提升有支撑上下文时的表现，但会降低测试时上下文缺失或误导时的鲁棒性。

机制分析表明，较长上下文提供了一个复杂度更低的解决方案；训练时梯度压力从常与参数知识相关的前馈网络转向注意力模块；因果干预证实模型在推理时更依赖上下文信息。因此，无限制扩展上下文并非单纯“给更多数据”的问题。

### 方法 / 贡献
- 提出“信息丰裕悖论”假说，区分两种学习模式：参数内化与上下文利用。
- 在预训练中系统改变上下文长度（512 到 32768 tokens），固定其他条件，观察能力变化。
- 在监督微调中固定上下文长度，控制任务相关信息量，检验鲁棒性变化。
- 理论分析说明长上下文可降低达到相同风险所需的参数存储信息量。
- 机制实验：分析梯度分配（前馈网络 vs 注意力模块）、解决方案复杂度、以及注意力对上下文 token 的依赖。

### 实验或数据
- 预训练：4 种参数量（20M, 55M, 259M, 750M），使用 Llama-2 架构和 Project Gutenberg 中超过 65536 token 的长文档，训练 10B tokens，上下文长度从 512 到 32768 变化。
- 评估：语言建模、自然语言理解、闭卷 MCQA（呈倒U型）。
- 监督微调：对比训练时有无任务相关上下文，测试时在支持性/缺失/误导性上下文下的表现。
- 机制分析：基于梯度归因、注意力权重和因果干预验证上下文依赖。

### 值得关注点
- 公开了 GitHub 代码和 HuggingFace 数据/模型产物。
- 反驳了“长上下文训练只是数据问题”的常见观点，强调上下文窗口本身会改变模型的学习策略。
- 对长上下文模型的安全性和鲁棒性有重要启示：训练时“喂太多”反而可能让模型失去独立能力。

### 局限性
摘要和所给内容未明确讨论局限。可推测该研究的结论主要基于特定数据（Gutenberg）和模型规模（最大 750M），但在提供材料中并无作者明确陈述的局限性。

## 2. TELLME: Test-Enhanced Learning for Language Model Enrichment

- Source: arxiv
- arXiv ID: 2608.11788
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.11788v1
- PDF: https://arxiv.org/pdf/2608.11788v1
- DOI: https://doi.org/10.48550/arXiv.2608.11788

### Authors

Minjun Kim, Inho Won, Hyeonseok Lim, MinKyu Kim, Junghun Yuk, Wooyoung Go, Jongyoul Park, Jungyeul Park, KyungTae Lim

### Abstract

Continual pre-training (CPT) has been widely adopted as a method for domain adaptation in large language models. However, CPT has consistently been accompanied by challenges, such as the difficulty of acquiring large-scale domain-specific datasets and high computational costs. In this study, we propose a novel method called Test-Enhanced Learning for Language Model Enrichment (TELLME) to alleviate these issues. TELLME leverages the TestEnhanced Learning (TEL) principle, whereby the model's training efficiency is improved using quizzes during training. It integrates this principle with CPT, thereby promoting efficient domain-specific knowledge acquisition and long-term memory retention. Experimental results demonstrate that TELLME outperforms existing methods by up to 23.6% in the financial domain and achieves a 9.8% improvement in long-term memory retention.

### 中文一句话结论
本文提出 TELLME 方法，通过将测试增强学习（Test-Enhanced Learning）原理融入持续预训练（CPT），利用描述性问答数据显著提升大语言模型的领域知识获取效率和长期记忆保持能力。

### English TL;DR
TELLME improves continual pre-training by integrating test-enhanced learning with quizzes, achieving up to 23.6% better domain-specific knowledge acquisition and 9.8% improvement in long-term memory retention.

### 中文详细总结
持续预训练（CPT）是大型语言模型领域适应的常用方法，但面临大规模领域数据集获取困难和高计算成本等挑战。受认知心理学中测试增强学习（TEL）原理的启发——即通过测试（尤其是需要解释性回答的测试）能显著提升长期记忆保持——本文提出 TELLME 方法。该方法将 CPT 与描述性问答（QA）数据相结合，在训练过程中加入“测验”，促使模型更高效地获取领域知识并形成长期记忆。TELLME 使用 GPT-4o-mini 以极低代价（约12美元）生成了10万条高质量的领域特定描述性QA样本，涵盖金融和医疗两个领域。在 LLaMA 和 SmolLM 等不同规模模型上的实验表明，TELLME 在金融领域相比现有方法性能提升最高达23.6%，长期记忆保持能力提升9.8%。此外，生成数据通过 LLM-as-a-judge 评估获得了4.03/5的质量评分。

### 方法 / 贡献
- 提出 TELLME 框架：将测试增强学习原理引入持续预训练，通过构造描述性 QA 数据激发模型内部知识回忆，而非简单的阅读理解式问答。
- 设计低成本、大规模的 QA 数据生成流程：利用 GPT-4o-mini 生成10万条领域特定 QA 样本，总成本约12美元，并确保问题多样性与概念映射（concept mapping）。
- 实验验证了 TELLME 在金融和医学领域对知识获取效率和长期记忆保持的有效性，显著优于传统 CPT 和 CPT+IT 方法。

### 实验或数据
- **实验设置**：在金融和医学两个领域进行持续训练，使用 LLaMA 和 SmolLM 系列不同规模的模型。
- **数据集**：基于领域文本，使用 GPT-4o-mini 生成10万条描述性 QA 训练样本（每条包含文本和多个QA对）。数据通过 LLM-as-a-judge 评估，平均得分4.03/5。
- **主要结果**：TELLME 在金融领域比现有方法提升最高23.6%；在长期记忆保持测试中提升9.8%。具体实验细节（如评估指标、对比基线）在论文中有详细描述。

### 值得关注点
- 将认知心理学中的测试增强学习原理成功迁移到 LLM 训练中，交叉学科视角具有启发性。
- 数据生成成本极低（100K 样本约12美元），具备实用性和可扩展性。
- 同时提升知识获取效率和长期记忆保持，解决了 CPT 中常见的遗忘问题。
- 采用描述性、需要内部知识推理的 QA 设计，而非简单检索，更贴合 TEL 的有效策略。

### 局限性
根据提供的摘要和预览内容，论文未明确讨论局限性。可能值得注意的方向包括：依赖 GPT-4o-mini 生成数据质量（虽经评估但可能存在偏差）、实验仅在金融和医疗领域验证，其他领域的泛化性有待进一步研究。

## 3. Benchmarking Trustworthiness of SLMs: Pre-trained vs. Compressed

- Source: arxiv
- arXiv ID: 2608.11981
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.11981v1
- PDF: https://arxiv.org/pdf/2608.11981v1
- DOI: https://doi.org/10.48550/arXiv.2608.11981

### Authors

Haokun Lin, Kaijie Zhu, Haobo Xu, Yichen Wu, Zhichao Lu, Qingfu Zhang, Zhenan Sun

### Abstract

Small Language Models (SLMs) have emerged as a more efficient alternative to traditional Large Language Models (LLMs), offering promising potential in resource-constrained scenarios. Existing approaches to building SLMs typically follow two paths: training compact models from scratch, or compressing larger pre-trained models using methods such as pruning, quantization, or distillation. As language models become increasingly integrated into real-world applications, ensuring their trustworthiness has become a critical concern. However, how to build trustworthy SLMs remains an underexplored question. In this work, we present a comprehensive evaluation of SLM trustworthiness across multiple dimensions, including fairness, robustness, privacy, and ethics. We first examine the effects of pruning and quantization, and find that quantization is significantly more effective in preserving trustworthiness compared to pruning. More importantly, we demonstrate that compressing a reliable large model via quantization can produce SLMs with superior trustworthiness and adaptability compared to using small models trained from scratch. Furthermore, knowledge distillation from trustworthy teacher models can further enhance the reliability of SLMs. We hope our findings provide practical guidance and a foundation for future research into the development and deployment of trustworthy small language models.

### 中文一句话结论
量化是保护小语言模型可信度的最佳压缩方法；压缩可靠的大模型比从头训练小模型更值得信赖，知识蒸馏能进一步改善可信度。

### English TL;DR
This paper comprehensively evaluates the trustworthiness of Small Language Models (SLMs) across fairness, robustness, privacy, and ethics, finding that quantization is more effective than pruning for preserving trustworthiness, and that compressing a reliable large model via quantization produces more trustworthy SLMs than training small models from scratch, with knowledge distillation further enhancing reliability.

### 中文详细总结
本文系统地评估了小语言模型（SLM）在公平性、鲁棒性、隐私和伦理四个维度的可信度。研究发现，在对大语言模型进行压缩时，量化（如GPTQ、AWQ）相比剪枝（如SparseGPT、Wanda）能更有效地保留原始模型的可信度；剪枝会显著损害模型的可靠性。更重要的是，通过量化压缩一个已经可靠的大模型所得到的SLM，其可信度和适应性显著优于从零训练的小模型。此外，从可信度高的教师模型进行知识蒸馏，可以进一步提升学生SLM的可靠性。研究为如何在资源受限环境下构建可信任的小语言模型提供了实证指导。

### 方法 / 贡献
- **方法**：构建统一的评估框架，对多种预训练SLM（<1B参数）和经过剪枝、量化、蒸馏压缩的大模型进行可信度对比，评价维度涵盖公平性、鲁棒性、隐私和伦理。
- **贡献**：
  1. 首次大规模比较剪枝与量化对SLM可信度的影响，明确推荐量化作为更可靠的压缩手段。
  2. 揭示关键发现：量化一个可靠的大模型，比从头训练小模型能获得更可信且适应性更强的SLM。
  3. 验证知识蒸馏能从更强教师模型中有效提升SLM的可信度。

### 实验或数据
摘要中声明在公平性、鲁棒性、隐私和伦理四个维度进行了全面评估，但未提及具体使用的数据集。文中实验涉及多种指令微调模型（如Llama、Qwen、Gemma系列）以及多种压缩方法（SparseGPT、Wanda、GPTQ、AWQ），并对不同剪枝稀疏度（如2:4、4:8）和量化位数（如INT4）进行了测试。

### 值得关注点
- 量化（特别是GPTQ）在几乎所有维度上几乎无损地保留了原始大模型的可信度，而剪枝（尤其是高稀疏度下）会导致显著下降。
- 量化后的7B模型在可信度上全面超越0.5B–1B预训练SLM，表明“压缩大模型”是构建可信SLM的更优路径。
- 知识蒸馏能从更可靠的教师模型中传递可信度优势，进一步改善小模型表现。

### 局限性
- 研究仅覆盖了剪枝、量化和蒸馏三类压缩方法，未涉及结构化剪枝、混合精度等更多技术。
- 实验局限于特定模型家族（如Llama、Qwen、Gemma）和参数规模（<8B），结论对其他架构或更大规模模型的泛化性有待验证。
- 可信度评估维度虽涵盖公平、鲁棒、隐私和伦理，但未能包括真实性、安全性等其他重要方面。
- 摘要未讨论计算成本、推理效率与实际部署中的权衡，这些因素可能影响方法选择。

## 4. When the API Speaks the Wrong Language: Revisiting Post-Training for Multilingual Tool Use

- Source: arxiv
- arXiv ID: 2608.11715
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.11715v1
- PDF: https://arxiv.org/pdf/2608.11715v1
- DOI: https://doi.org/10.48550/arXiv.2608.11715

### Authors

Siddharth Chauhan, Thomas Butler, Abhishek Singhania, Pankaj Porwal, Honey Gupta

### Abstract

The reliability of Large Language Models (LLMs) for API calling degrades in multilingual settings. A common failure occurs when a model selects the correct tool but generates argument values in an inconsistent language, which we term Argument Language Mismatch (ALM). Although semantically correct, such outputs are operationally invalid and not captured by standard API-calling metrics. We revisit post-training strategies for mitigating ALM and find that, in our benchmark, supervised fine-tuning (SFT) provides a strong baseline, substantially improving argument language consistency and end-to-end function call accuracy. Under consistent model selection, SFT achieves performance comparable to, and sometimes exceeding more complex reinforcement learning (RL) approaches. We further examine whether RL with structured, argument-aware rewards offers additional benefits. While methods such as Group Relative Policy Optimization (GRPO) can improve language consistency and better preserve general reasoning ability, these gains are incremental and most pronounced in generalization and multi-objective trade-offs. Overall, our results suggest that much of the performance in multilingual API grounding can be achieved through careful supervised training, with RL providing targeted rather than fundamental improvements.

### 中文一句话结论
监督微调（SFT）是多语言API调用中解决参数语言不匹配问题的强基线方法，其效果可与更复杂的强化学习方法相媲美甚至更优，而强化学习仅在泛化和多目标权衡上提供增量改进。

### English TL;DR
Supervised fine-tuning is a strong baseline that largely resolves Argument Language Mismatch in multilingual API calling, while reinforcement learning with argument-aware rewards yields only incremental gains in generalization and multi-objective trade-offs.

### 中文详细总结
该论文研究了大型语言模型在**多语言API调用**场景中的一个关键失效模式：**参数语言不匹配（ALM）**——即模型选对了API工具，但生成的参数值语言与用户输入不一致，导致操作失效。尽管这些输出语义正确，但标准API调用指标无法捕获此类错误。

研究比较了两种后训练策略：**监督微调（SFT）**和**强化学习（RL）**（包括PPO和GRPO）。结果表明，在标准基准测试中，SFT本身就能显著改善参数语言一致性和端到端函数调用准确率，在一致性模型选择下表现与RL相当甚至更优。RL方法（特别是GRPO）虽然能进一步改善语言一致性和保留通用推理能力，但这些提升是**增量性的**，主要在泛化场景和多目标权衡中体现。

论文构建了多语言扩展版的Berkeley Function Calling基准，涵盖多种语言和真实API结构，并在"可学习性"和"泛化性"两个设置下进行评估。

### 方法 / 贡献
1. 形式化了**参数语言不匹配（ALM）**这一多语言API调用中的关键失效模式
2. 设计了**层级奖励函数**：与API调用流程对齐，包含工具选择、参数结构和参数语言一致性等不同粒度
3. 提出了**参数因子化的信用分配**方法和**分词级奖励加权**策略
4. 系统比较了SFT、PPO和GRPO三种后训练策略，揭示了不同方法在不同场景下的优劣

### 实验或数据
论文构建了一个多语言扩展版的Berkeley Function Calling基准，涵盖多种语言并保留真实API结构和参数多样性。实验在以下两种设置下进行：**可学习性**（训练和测试分布对齐）和**泛化性**（未见过的API或跨语言迁移）。未提及具体数据集规模或语言数量。

### 值得关注点
1. **SFT作为强基线的发现**：挑战了"越复杂的方法越好"的直觉，提示工业界可先用简单的SFT解决问题
2. **ALM错误的新视角**：将语言不一致问题从语义错误中分离出来，为多语言系统评估提供了新框架
3. **GRPO的增量优势**：在泛化场景和保留通用推理能力方面，GRPO相比SFT有额外收益，适合对泛化性要求高的场景
4. **实际部署启示**：对资源受限的团队，SFT可能是性价比最高的方案

### 局限性
1. RL方法（PPO和GRPO）相对于SFT的提升是**增量的**，而非根本性的改进
2. 论文仅在内部构建的特定基准上评估，未提及在多个公开基准或实际生产环境中的验证
3. 未讨论不同语言族系（如语系差异）对ALM错误率的影响
4. 未探索更大规模模型或更复杂场景（如多轮对话、动态API集）下的表现
5. 未提供关于SFT数据量、多样性或质量要求的具体指导

## 5. Who Thinks Best Depends on How Long You Let Them: Budget-Dependent Rankings in LLM Evaluation

- Source: arxiv
- arXiv ID: 2608.12150
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.12150v1
- PDF: https://arxiv.org/pdf/2608.12150v1
- DOI: https://doi.org/10.48550/arXiv.2608.12150

### Authors

Rodrigo Guedes de Souza, Alison R. Panisson

### Abstract

Standard evaluation of large language models assumes stable model rankings across inference conditions. We challenge this assumption by varying the token generation budget, i.e., the maximum tokens a model may produce, across seven levels (64--4,096), evaluating four models on three reasoning benchmarks (56,476 inferences). We report four findings: (i) 3--19% of items exhibit non-monotone behavior (accuracy decreasing with more budget), even after controlling for truncation, and this phenomenon is model-specific (cross-model overlap: 6--14%). (ii) Model rankings reverse across budgets on all benchmarks ($p {<} 0.01$, McNemar). (iii) Oracle analysis reveals model complementarity up to $+27.8$pp, most pronounced at constrained budgets. (iv) A budget-aware router captures 14.1% of the oracle gap cross-domain; budget features help within-domain ($+1.6$ to $+5.7$pp) but are domain-specific and hurt transfer ($-1.2$pp). These results argue for budget-conditioned evaluation protocols.

### 中文一句话结论
LLM 的排名和正确性高度依赖于推理时的 token 生成预算，预算不足或过多均可能导致排名反转和“过度思考”现象，这对当前固定预算的评估方法提出了挑战。

### English TL;DR
This paper demonstrates that large language model rankings and item-level correctness are highly dependent on the token generation budget, with ranking reversals, non-monotone “overthinking” behavior, and budget-constrained model complementarity, arguing for budget-conditioned evaluation protocols.

### 中文详细总结
该论文通过系统变化 token 生成预算（64 至 4096 tokens），在三个推理基准（GSM8K、MATH-500、GPQA-Diamond）上评估了四个 LLM（LLaMA-3 8B、Qwen-3 32B、LLaMA-3.3 70B、GPT-OSS 20B），共 56,476 次推理。主要发现如下：（i）3%–19% 的项目呈现非单调行为（增加预算反而降低准确率），且该现象具有模型特异性（跨模型重叠仅 6%–14%）；在控制截断效应后，非单调率仍显著。（ii）在所有基准上，模型排名随预算发生统计显著的反转（McNemar 检验 p < 0.01）。（iii）Oracle 分析显示模型间互补性最高可达 +27.8 个百分点，在低预算下尤为突出。（iv）提出预算感知路由方法，跨域捕获 14.1% 的 Oracle 差距，但预算特征的域迁移性有限。论文主张采用预算条件化的评估协议。

### 方法 / 贡献
- 提出**项目级行为分类**：将每个模型-项目对随预算的变化归为始终正确、单调递增、非单调、始终错误四类，量化了非单调行为的普遍性和模型特异性。
- 发现并验证**统计显著的排名反转**：在所有三个基准上，最佳模型的身份随预算变化（如 GSM8K 上 LLaMA-3.3 70B 在 b=256 领先，GPT-OSS 20B 在 b=512 反超），并通过截断控制分析确认部分反转非截断伪像。
- 分析了**Oracle 差距的动态**：预算约束下模型互补性更强（GPQA 上 Oracle 超越最佳模型 27.8pp），但随预算增加 Jaccard 相似度从 0.048 升至 0.741。
- 实现**预算感知路由**：训练 XGBoost 分类器，以文本特征和预算为输入预测项目正确性，跨域测试比最佳单预算基线提升 +2.67pp，并发现预算特征在 SHAP 分析中重要性超越文本特征。

### 实验或数据
- **模型**：4 个开源推理模型（8B–70B 参数），温度 T=0 贪婪解码。
- **基准**：GSM8K（1,319 题）、MATH-500（500 题）、GPQA-Diamond（198 题），难度递增。
- **预算**：7 个水平：64、128、256、512、1024、2048、4096 tokens。
- **总推理量**：4 模型 × 2017 项目 × 7 预算 = 56,476 次推理。
- **分析策略**：三层次分析（所有项目、仅完成项目、所有模型均完成项目的公共子集），以区分真实推理效果与截断伪像。

### 值得关注点
- **“过度思考”的模型特异性**：非单调行为主要取决于模型而非项目本身，跨模型重叠极低（6–14%），因此无法通过剔除“问题项目”来缓解。
- **排名反转的统计显著性**：所有基准均出现反转（p < 0.01），且不同预算下模型相对优势截然不同，挑战了排行榜的稳定性。
- **互补性与预算的关系**：低预算下模型间互补性更强（Oracle 差距更大），暗示预算约束场景下模型集成或路由更具潜力。
- **预算感知路由的初步验证**：将预算作为显式特征可提升路由性能，且预算特征贡献度超过文本特征，但跨域迁移性差（域内提升 +1.6–5.7pp，跨域减少 -1.2pp）。

### 局限性
- **GPQA-Diamond 样本量小**（198 题），部分统计检验（如最终排名）未达显著水平，结论需谨慎对待。
- **截断效应**：部分模型的低性能由截断导致，但对其是否应被视为“失败”存在争议；论文通过多层次分析试图分离该效应，但无法完全消除。
- **预算特征的域特异性**：预算感知路由的预算特征在不同域间迁移时表现负面（-1.2pp），提示需要更鲁棒的域适应方法。
- **仅涉及开源模型**（GPT-OSS 为半开放），且均为推理型模型，结论能否推广至其他模型族（如指令微调模型）尚不确定。

## 6. Language-Conditional Dequantization: Recovering What Quantization Steals from Non-English Languages

- Source: arxiv
- arXiv ID: 2608.11786
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.11786v1
- PDF: https://arxiv.org/pdf/2608.11786v1
- DOI: https://doi.org/10.48550/arXiv.2608.11786

### Authors

Nirmal Thomas

### Abstract

Aggressive quantization disproportionately harms multilingual capability: in the sub-4B INT3 GPTQ regime, we measure 2-4x larger perplexity degradation on non-English languages than on English. We propose Language-Conditional Dequantization (LCD), a post-hoc method that attaches per-language rank-2 LoRA corrections to the linear layers of an already-quantized model, adding 0.12% parameters per language and training in under 20 minutes on a single GPU. Across Qwen2.5-3B and Llama-3.2-3B, LCD recovers 70-83% of the perplexity gap for non-Latin script languages and 17-28% of the GlobalMMLU accuracy gap, outperforming a language-agnostic correction of equal capacity by 3-9 points on typologically distant languages and a data-free low-rank baseline (LQER) by an order of magnitude. We further identify a perplexity-accuracy disconnect and trace it to where quantization concentrates damage: early-depth errors (Llama) propagate downstream and resist local correction, while late-depth errors (Qwen) do not. A layer-restricted variant of LCD validates this mechanism directly.

### 中文一句话结论
语言条件反量化（LCD）通过为每种语言附加秩2 LoRA修正，在子40亿参数INT3量化模型中恢复了非拉丁字母语言70-83%的困惑度差距和17-28%的GlobalMMLU准确率差距，并揭示了困惑度与准确率之间的不一致性及其与误差深度分布的关系。

### English TL;DR
Language-Conditional Dequantization (LCD) is a post-hoc method using per-language rank-2 LoRA corrections that recovers 70-83% of the perplexity gap for non-Latin script languages and 17-28% of the GlobalMMLU accuracy gap in sub-4B INT3 quantized models, outperforming language-agnostic and data-free baselines while also revealing a perplexity-accuracy disconnect linked to error depth in model layers.

### 中文详细总结
论文提出语言条件反量化（LCD），针对GPTQ等极端量化（INT3、组大小128）对非英语语言造成的更严重退化（困惑度退化比英语高2-4倍）问题，在已量化模型的线性层上附加每语言独立的秩2 LoRA修正（每语言仅增加0.12%参数，单GPU训练<20分钟）。在Qwen2.5-3B和Llama-3.2-3B模型上的9种语言实验显示：
- 非拉丁字母语言（阿拉伯语、日语、中文、韩语）的困惑度恢复率达70-83%，拉丁语系语言恢复率较低（35-57%）。
- 全球MMLU准确率恢复17-28%，且困惑度恢复与准确率恢复存在解耦：早期层误差为主时（Llama），困惑度恢复好但准确率恢复有限；后期层误差为主时（Qwen），两者恢复更一致。
- 与语言无关的等价秩2 LoRA相比，LCD在类型学上较远的语言（如阿拉伯语）上优势达3-9个百分点，而数据无关的低秩基线（LQER）恢复效果差一个数量级。

### 方法 / 贡献
- 提出**语言条件反量化（LCD）**：为每个语言独立学习秩2的LoRA修正参数（初始化为零），通过前向钩子注入，不改变模型架构。
- 训练使用每语言256条文本（来自mC4/C4），优化语言模型损失，仅修正参数可训练，训练时间<20分钟/语言。
- 推理时通过语言标识选择对应修正槽，单次开关开销可忽略。
- 通过逐层误差分析，揭示了**困惑度-准确率解耦**的结构性原因：不同模型量化误差的深度分布不同（Llama集中于早期层，Qwen集中于后期层），并验证了层限制版LCD的效果。

### 实验或数据
- **模型**：Qwen2.5-3B和Llama-3.2-3B（均小于4B参数）。
- **量化**：GPTQ W3A16，组大小128，校准数据为128段英文C4。
- **语言**：英语、阿拉伯语、日语、中文、印地语、俄语、法语、西班牙语、韩语（9种）。
- **指标**：困惑度（mC4/C4留出集，每语言32样本）和GlobalMMLU准确率。
- **关键数值**：
  - 量化后非英语困惑度退化比英语高2.3-3.2倍（例如Qwen上阿拉伯语4.37倍 vs 英语1.35倍）。
  - LCD恢复非拉丁字母语言70-83%的困惑度差距；GlobalMMLU恢复17-28%的准确率差距。
  - 与语言无关基线相比，在类型学距离远的语言上提升3-9个百分点；与LQER（数据无关）相比，恢复效果高一个数量级（63.5% vs 5.5%）。

### 值得关注点
1. **语言条件性的必要性**：对于类型学距离较远的语言（阿拉伯语、日语等），每语言独立修正显著优于语言无关的全局修正；对于接近英语的语言（法语、西班牙语），全局修正反而更优。
2. **困惑度-准确率解耦**：在Llama-3.2-3B上，困惑度恢复好但准确率恢复差，原因在于量化误差集中在早期Transformer层（早期误差传播至下游，局部修正难以完全恢复）；Qwen上误差集中在后期层，两者恢复更一致。
3. **层限制验证**：将LCD限制在Llama底部一半的Transformer块，以一半参数获得比均匀修正高10个百分点的恢复效果，支撑了早期层误差集中机制。

### 局限性
论文未在提供的摘要或内容中明确讨论局限性。但从方法推断，可能包括：仅测试于子40亿参数模型和INT3 GPTQ量化方案；依赖推理时的语言标识（可通过快速文本检测实现，但可能增加简单场景的复杂度）；修正效果受语言类型学距离影响（拉丁语系恢复率较低）；未讨论大规模模型或不同量化策略（如NF4）的适用性。

## 7. LookBack: Where and How to Score LVLM Responses via Visual Reference Usage

- Source: arxiv
- arXiv ID: 2608.11847
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.11847v1
- PDF: https://arxiv.org/pdf/2608.11847v1
- DOI: https://doi.org/10.48550/arXiv.2608.11847

### Authors

Beomsik Cho, Jinhyeong Kim, Dongseok Lee, Jaehyung Kim

### Abstract

Large Vision-Language Models (LVLMs) integrate visual perception with language generation, enabling responses that span image understanding and complex reasoning. However, LVLMs do not just inherit the text-level hallucinations; they also hallucinate against the image, producing fluent responses ungrounded in what they see. This makes LVLM response scoring inherently harder, and our diagnostics show that existing confidence-based metrics adopted from LLMs are insufficient for LVLMs. Specifically, removing the input image barely changes confidence-based selection, suggesting that output-space confidence primarily captures textual plausibility rather than agreement with the image. To address this gap, we propose LookBack, a training-free LVLM response scoring method that augments token likelihood with visual lookback score, a lightweight measure of how strongly each response token refers to image tokens. Across four benchmarks and three models, LookBack consistently improves Best-of-$N$ selection over existing baselines with negligible additional overhead.

### 中文一句话结论
LookBack 通过引入视觉回溯分数（visual lookback score）来校准大视觉语言模型（LVLM）的 token 似然，无需额外训练即可显著提升最佳选择（Best-of-N）响应评分性能。

### English TL;DR
LookBack improves LVLM response scoring by augmenting token likelihood with a lightweight visual attention-based measure of how strongly each token refers to image tokens, enabling training-free and more image-sensitive Best-of-N selection.

### 中文详细总结
大视觉语言模型（LVLM）在生成响应时不仅继承了文本层面的幻觉，还会产生与图像不符的视觉幻觉。现有从大语言模型（LLM）迁移来的置信度评分指标（如 Self-Certainty）在 LVLM 中效果不佳，诊断实验表明：移除输入图像后，基于置信度的选择结果几乎不变，说明这些指标主要捕捉文本合理性而非对图像的忠实度。为解决此问题，本文提出 LookBack，一种无需训练的 LVLM 响应评分方法。它利用注意力机制计算每个生成 token 对图像 token 的视觉回溯分数（visual lookback score），并将其与 token 似然结合，得到校准后的视觉感知分数。在四个基准和三个模型上的实验表明，LookBack 一致提升了最佳选择（Best-of-N）性能，且计算开销极低。

### 方法 / 贡献
- **贡献**：揭示了 LVLM 输出空间置信度对图像不敏感的缺陷，并提出了无需额外训练或推理的 LookBack 方法。
- **核心方法**：
  1. **视觉回溯分数**：计算每个生成 token 在跨层多头注意力中分配给图像 token 的注意力分数占比，作为该 token 对视觉参考使用程度的轻量代理。
  2. **lookback 校准 token 分数**：将每个 token 的似然与其视觉回溯分数结合，确保高置信度 token 也需具有强视觉参考。
  3. **响应级聚合**：根据视觉相关性分布对 token 分数加权，使视觉诊断性内容词（如名词、形容词）贡献更大，通用语言词贡献更小。

### 实验或数据
- **基准与模型**：在四个需要视觉理解的基准上评估，使用三种代表性 LVLM：LLaVA-1.5-7B、Qwen2.5-VL-7B 和 InternVL3-8B。
- **实验设置**：采用最佳选择（Best-of-N）设置，为每个输入采样多个候选响应，用不同评分函数选择最佳响应。
- **结果**：LookBack 在所有三个模型上取得了最高的模型平均性能，并一致优于现有语言侧和视觉侧基线方法。
- **诊断实验**：使用 MS-COCO 数据集（VQAv2 和 CHAIR）分析，发现输出置信度与视觉回溯分数在 token 级别和响应级别均呈互补关系。

### 值得关注点
- 提出了一种新颖的注意力基视觉参考度量（视觉回溯分数），无需任何外部模型或训练。
- 揭示了输出空间置信度与视觉回溯分数之间有趣的互补模式：置信度高但视觉回溯低的 token 往往是语法功能词，而低置信度高视觉回溯的 token 往往是视觉内容词。
- 方法简洁高效，仅利用生成过程中的注意力权重，无额外推理开销。

### 局限性
- 依赖于注意力权重作为视觉参考使用的代理，可能存在注意力权重的解释性问题（如注意力不忠实于模型实际决策）。
- 未在更广泛的 LVLM 架构或需要复杂视觉推理的场景中验证，泛化性受限于文中测试的设置。
- 实验部分未提及具体的训练数据或数据集（如 MS-COCO、VQAv2、CHAIR 等已在文献中标准使用），仅说明使用四个基准，未提供详细数据规模或来源说明。

## 8. Generation as Auxiliary Supervision: Enhancing Visual Understanding at Zero Inference Overhead via Decoupled Embedding Prediction

- Source: arxiv
- arXiv ID: 2608.12209
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.12209v1
- PDF: https://arxiv.org/pdf/2608.12209v1
- DOI: https://doi.org/10.48550/arXiv.2608.12209

### Authors

Zhongbin Guo, Jiahao Xie, Dongling Xiao, Qianle Wang, Ruiqi Lu, Xiaomin He, Wanxuan Sun, Cheng Yang

### Abstract

While Multimodal Large Language Models (MLLMs) have achieved remarkable progress, visual understanding and generation are typically treated as divergent objectives. Existing unified frameworks often rely on discrete visual tokenization or diffusion objectives whose generative targets differ from the continuous representations consumed by visual understanding models, making direct transfer to enhance existing pretrained MLLMs non-trivial. In this work, we present GAS, a generation-guided training framework that reinterprets visual generation as auxiliary supervision for representation learning. Concretely, GAS adapts Next Embedding Prediction (NEP) as a cross-modal generation paradigm within a decoupled Mixture-of-Transformers (MoT) architecture. By maintaining a shared lower trunk and parallel upper layers, GAS lets generation losses enrich the shared visual pathway with finer spatial precision and stronger visual retention while shielding the upper understanding layers from direct generation gradients. To maximize this synergy, we further construct highly correlated generation tasks that demand deep cognitive grounding rather than generic synthesis alone. Across model scales and training stages, GAS improves aggregate multimodal understanding, with its most reliable gains on perception and spatial comprehension. Crucially, because the auxiliary generation branch is discarded after training, these gains incur zero inference overhead. Extensive controlled comparisons and representation-level analyses further clarify when and why generation-guided training benefits understanding, and demonstrate the feasibility of generation-guided training as a practical route to stronger multimodal understanding.

### 中文一句话结论
GAS 通过解耦的混合变压器（MoT）架构和下一嵌入预测（NEP）范式，将视觉生成作为训练时的辅助监督，在不增加推理开销的前提下显著提升多模态大模型的视觉理解能力。

### English TL;DR
GAS enhances visual understanding at zero inference overhead by using generation as auxiliary supervision through Next Embedding Prediction in a decoupled Mixture-of-Transformers architecture.

### 中文详细总结
现有统一多模态模型通常将视觉理解与生成视为独立目标，生成目标（如离散分词或扩散目标）与理解模型使用的连续表示空间不一致，难以直接迁移至预训练的理解模型。本文提出 GAS（Generation as Auxiliary Supervision）框架，重新将视觉生成解释为表示学习的辅助监督。具体地，GAS 采用解耦的混合变压器（MoT）结构：共享下层 trunk 和并行上层，生成分支通过下一嵌入预测（NEP）预测连续的视觉嵌入，使生成损失能丰富共享视觉路径的空间精度与视觉保持力，同时保护上层理解层不受生成梯度的直接干扰。训练后丢弃生成分支，实现零推理开销。GAS 基于约 10M 样本（5 大类 15 子任务）进行训练，在 2B 和 4B 规模上提升聚合多模态理解，尤其在感知与空间理解任务上增益最稳定。广泛的控制比较与表示层面分析阐明生成引导训练何时为何有利于理解。

### 方法 / 贡献
- 提出 **Next Embedding Prediction (NEP)**：利用连续嵌入预测作为生成范式，与 LLM 的输入表示空间对齐，避免离散分词或扩散目标的表示不匹配。
- 设计 **解耦 MoT 架构**：共享下层 trunk，上层分为理解分支（仅用文本交叉熵）和生成分支（仅用 NEP 损失），生成梯度仅通过共享层回传，理解上层不受直接干扰。
- 构建多样化生成任务数据：约 10M 样本，覆盖 5 大类 15 子任务（从像素级感知到高级推理），并通过自动化合成管道产生高质量数据。
- 系统性分析：通过参数隔离、逐层监督注入、逐任务消融、表示级诊断、匹配预算控制等实验，揭示生成训练增强理解的机制。

### 实验或数据
- 实验在 2B 和 4B 参数规模的 LLM 骨干上进行，使用约 10M 生成样本（来自 5 大类 15 子任务）。
- 在多个多模态理解基准上报告聚合结果，并针对感知与空间理解任务进行详细分析。
- 进行了广泛的控制比较和表示层面分析，包括匹配预算控制、消融实验和多次运行统计，验证生成训练的优势。
- 所有生成数据的构建未依赖人工标注，采用自动化合成管道。

### 值得关注点
- **零推理开销**：生成分支训练后丢弃，推理时完全移除，无额外计算或内存消耗。
- **NEP 的表示统一性**：直接在 LLM 输入嵌入空间预测图像，使生成目标与理解表示天然对齐，优于离散分词或扩散目标。
- **解耦 MoT 的设计智慧**：通过隔离上层梯度，避免生成与理解目标冲突，同时通过共享层间接传递空间知识。
- **任务依赖增益**：感知与空间理解任务获益最大，且组合多样任务（如分割、接地、推理等）可产生互补提升。

### 局限性
本文未明确讨论局限性，但实验表明生成监督的效果因任务类型而异：感知和空间理解任务提升显著，而某些高级推理任务提升较小。此外，生成数据的质量与相关性至关重要，不恰当的生成任务可能带来干扰；训练数据量（约 10M）和计算成本虽未详细展开，但框架在更大规模或更多样化任务下的泛化性仍有待探索。

## 9. Gloss-Free Representation Learning for Cross-Dataset Sign Spotting

- Source: arxiv
- arXiv ID: 2608.11332
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.11332v1
- PDF: https://arxiv.org/pdf/2608.11332v1
- DOI: https://doi.org/10.48550/arXiv.2608.11332

### Authors

Oğuz Akif Tüfekcioğlu, Ezgi Ekin, Mustafa Kaan Çevik, Hacer Yalim Keles

### Abstract

Sign-language research for resource-constrained languages is often limited by the cost of dense linguistic labels such as glosses, temporal boundaries, and sign order. Broadcast news offers a practical alternative by pairing continuous signing with spoken-language transcripts, but this supervision is weak since text and signing are loosely aligned. Morphologically rich languages such as Turkish add further difficulty, as the same lexical meaning can appear in many inflected forms while some derived forms should remain distinct. We study whether weak transcript-based supervision can pretrain a reusable sign encoder in this setting, where poor text normalization can fragment pseudo-gloss targets and weaken representation learning. Unlike prior pseudo-gloss pipelines designed mainly to improve translation, we test whether the pretrained encoder transfers as a reusable representation for cross-dataset sign spotting. We pretrain on TSL-News, a new Turkish broadcast corpus, using pseudo-gloss labels derived from transcripts rather than manual annotation, comparing rule-based morphological lemmatization with constrained LLM-assisted normalization over a fixed vocabulary. We evaluate the learned representations via cross-dataset sign spotting on a new TSL Spotting Benchmark built from the TSL Dictionary corpus. The LLM-assisted encoder raises top-5 temporal localization mean IoU from 0.235 to 0.465, with 56.2% of examples reaching an IoU of at least 0.50; a frequency analysis suggests this gain is not mainly driven by memorizing frequent pseudo-gloss labels. In a downstream translation check, the same pretraining improves BLEU-4 from 9.60 to 11.04 and ROUGE from 23.48 to 27.43. These results show that loosely aligned broadcast data can provide effective weak supervision for learning sign representations that capture both lexical content and temporal structure.

### 中文一句话结论  
本文证明，通过弱监督的文本级伪标注（尤其借助LLM辅助的词汇规范化），可以在不依赖人工标注的情况下，预训练出可跨数据集用于手语动作定位的可重用编码器。

### English TL;DR  
This paper demonstrates that weak transcript-based supervision with LLM-assisted pseudo-gloss normalization can effectively pretrain a reusable sign encoder for cross-dataset sign spotting, achieving significant improvements in temporal localization (mean IoU from 0.235 to 0.465) and downstream translation quality (BLEU-4 from 9.60 to 11.04) without requiring manual gloss annotations.

### 中文详细总结  
该研究面向资源受限的手语语言（如土耳其手语，TSL），探索如何利用广播新闻中文本与手语视频的弱对齐关系，预训练出一个可跨数据集用于手语动作定位（sign spotting）的视觉编码器。传统方法需要密集的语标标注（gloss），而本文提出“无语标”方案，从配套文本中自动提取伪语标（pseudo-gloss）。针对土耳其语高度粘着的形态特点，作者比较了两种伪语标构建策略：基于规则的形态学词形还原（morphology-lemma）和基于LLM的词汇规范化（LLM lexical-rule）。预训练数据为自建的TSL-News语料库，下游评估则在全新的TSL Spotting Benchmark（从TSL Dictionary语料库构建）上完成。实验结果表明，LLM辅助的编码器在top-5时间定位平均IoU上从0.235提升至0.465，且56.2%的样本IoU达到0.50以上；在下游翻译任务中，BLEU-4从9.60提升至11.04，ROUGE从23.48提升至27.43。频率分析表明，该提升并非主要源于记忆高频伪语标。

### 方法 / 贡献  
1. 重新利用了Sign2GPT风格的伪语标预训练流程，将其从翻译任务转向跨数据集手语动作定位问题，检验弱监督下的表示可迁移性。  
2. 针对土耳其语的粘着形态，设计了两种伪语标构建策略：基于规则的形态学词形还原和基于LLM的约束性词汇规范化。  
3. 构建了两个新数据集：TSL-News（广播预训练语料）和TSL Spotting Benchmark（跨数据集定位评估基准）。  
4. 提出多角度评估协议，包括模板匹配NCC、时间IoU、伪语标定位和全词汇NCC，辅以下游翻译验证，有效隔离了表示质量与词汇覆盖率等干扰因素。

### 实验或数据  
- 预训练：使用自建TSL-News语料库（土耳其广播新闻），弱监督来自配套文本。  
- 评估：在TSL Dictionary语料库构建的TSL Spotting Benchmark上进行跨数据集动作定位。  
- 关键结果：LLM辅助编码器在top-5 NCCC时间定位中，平均IoU从0.235提升至0.465；56.2%的样本IoU≥0.50。  
- 下游翻译：BLEU-4从9.60提升至11.04，ROUGE从23.48提升至27.43。  
- 频率分析：增益并非主要由记忆高频伪语标驱动。

### 值得关注点  
1. 完全消除对人工语标标注的依赖，仅利用文本弱监督即获得可迁移的表示，具有实用价值。  
2. LLM辅助的伪语标构建显著优于传统形态学方法，表明在粘着语言中，智能词汇规范化是关键瓶颈。  
3. 跨数据集迁移的成功验证了弱监督表示的通用性，尤其在数据稀缺的语言中意义重大。  
4. 多角度评估协议（而非仅依赖翻译分数）更直接地测度了表示质量。

### 局限性  
1. 伪语标标准化仍未完全解决土耳其语中派生形态和多义词问题，部分语义歧义可能残留。  
2. 实验仅针对土耳其手语，伪语标构建策略对其他粘着语言（如芬兰语、匈牙利语）的适用性未知。  
3. 时间定位中的后处理（NCC峰值选取、top-k IoU）较为简单，复杂对齐与重排技术可能进一步提升效果。  
4. 未探索预训练编码器在其他任务（如孤立词识别、检索）上的迁移能力，仅聚焦动作定位与翻译。

## 10. Context Blindness in DPO: Mitigating Object Hallucination in MLLMs via Context-Calibrated Preference Optimization

- Source: arxiv
- arXiv ID: 2608.12158
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.12158v1
- PDF: https://arxiv.org/pdf/2608.12158v1
- DOI: https://doi.org/10.48550/arXiv.2608.12158

### Authors

Byungoh Ko, Jinyoung Park, Jongha Kim, Jeehye Na, Jaewon Cho, Hyunwoo J. Kim

### Abstract

Multimodal large language models (MLLMs) have made rapid progress, yet they still exhibit object hallucination, generating plausible but incorrect descriptions that are inconsistent with the visual input. Direct Preference Optimization (DPO) mitigates this by training models to prefer non-hallucinated responses over hallucinated ones, and recent efforts further enrich the preference data with relevant context. However, it remains unclear whether DPO actually leverages such context. To investigate this, we propose Contextual Preference Gain (CPG), a simple metric that measures how much a model's preference strengthens when relevant context is provided. We find that higher CPG consistently corresponds to lower hallucination, yet standard DPO and its variants exhibit only limited CPG, indicating that they underutilize contextual information and thus remain prone to hallucination. To address this, we propose Context-Calibrated DPO (C$^2$-DPO), which directly maximizes CPG while preserving the original preference ordering. Across multiple benchmarks, C$^2$-DPO substantially reduces hallucination without compromising general reasoning, relatively reducing the Object HalBench hallucination rate of Qwen2-VL-Instruct-2B by 36%. Code is available at https://github.com/mlvlab/C2-DPO

### 中文一句话结论
本文提出 Context-Calibrated DPO (C²-DPO)，通过显式最大化上下文偏好增益来缓解多模态大模型的“上下文盲视”问题，从而有效降低对象幻觉率。

### English TL;DR
The paper introduces Context-Calibrated DPO (C²-DPO), which directly optimizes contextual preference gain to address the “context blindness” of standard DPO and reduce object hallucination in multimodal large language models.

### 中文详细总结
多模态大语言模型（MLLMs）虽然进展迅速，但仍存在对象幻觉问题：生成看似合理但与视觉输入不符的描述。直接偏好优化（DPO）通过训练模型偏好非幻觉响应来缓解此问题，近期工作还通过丰富偏好数据的上下文来增强效果。然而，论文发现标准DPO及其变体存在“上下文盲视”：它们并未真正利用上下文信息。为此，作者首先提出上下文偏好增益（CPG）指标，衡量提供相关上下文时模型偏好增强的程度，并发现CPG越高，幻觉率越低，但现有DPO方法的CPG接近零。为解决该问题，论文提出 C²-DPO，在保持原有偏好顺序的同时直接最大化CPG。该方法引入一个校准项，鼓励有上下文时的偏好间隔大于无上下文时的间隔。实验表明，C²-DPO在多个基准上显著降低幻觉率（如Qwen2-VL-Instruct-2B在Object HalBench上相对降低36%），且不损害通用推理能力。此外，C²-DPO可无缝集成到SimPO、RDPO等其他偏好优化方法中，并在纯文本设置中也提升了事实对齐。

### 方法 / 贡献
- 提出 Contextual Preference Gain (CPG) 诊断指标，量化上下文对偏好间隔的影响，揭示现有DPO方法的“上下文盲视”现象。
- 提出 C²-DPO 框架，通过直接优化CPG来增强模型对上下文的利用，其校准项显式鼓励有上下文时的偏好间隔大于无上下文时。
- C²-DPO 可无缝集成到DPO、SimPO、RDPO等多种偏好优化方法中，具有通用性。
- 在多个多模态和纯文本基准上展示有效性，显著降低对象幻觉率并保持通用推理性能。

### 实验或数据
- **基准**：Object HalBench（幻觉率）、ScienceQA、MM-Vet、TextVQA（通用推理）。
- **关键结果**：Qwen2-VL-Instruct-2B 在 Object HalBench 上幻觉率相对降低 36%；通用推理能力在 ScienceQA、MM-Vet、TextVQA 上保持。
- **扩展实验**：C²-DPO 可集成至 SimPO、RDPO 并取得类似增益；纯文本实验也显示事实对齐的改进。
- 代码已开源。

### 值得关注点
- 首次系统诊断标准DPO的“上下文盲视”，并提出针对性的校准方法。
- 方法通用性强，能适配多种偏好优化框架，且不依赖额外推理成本。
- 纯文本实验的正面结果说明上下文感知偏好建模具有跨模态的广泛价值。

### 局限性
论文未明确讨论局限性。但从方法设计看，C²-DPO 需要额外辅助上下文（如图像描述）作为输入，其质量可能影响效果；训练时需同时计算有/无上下文的偏好分数，可能增加计算开销。此外，实验主要集中在2B模型上，更大规模模型的表现有待验证。

## Processing Notes

- Duplicate papers skipped: 0