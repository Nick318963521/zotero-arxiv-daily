# Daily arXiv - 2026-09-25

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-25T00:54:19
- Paper count: 10

## 1. Hunyuan-A13B Technical Report

- Source: arxiv
- arXiv ID: 2609.27284
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.27284v1
- PDF: https://arxiv.org/pdf/2609.27284v1
- DOI: https://doi.org/10.48550/arXiv.2609.27284

### Authors

Tencent Hunyuan Team, Ao Liu, Botong Zhou, Can Xu, Chayse Zhou, ChenChen Zhang, Chengcheng Xu, Chenhao Wang, Decheng Wu, Dengpeng Wu, Dian Jiao, Dong Du, Dong Wang, Feng Zhang, Fengzong Lian, Guanghui Xu, Guanwei Zhang, Hai Wang, Haipeng Luo, Han Hu, Huilin Xu, Jiajia Wu, Jianchen Zhu, Jianfeng Yan, Jiaqi Zhu, Jihong Zhang, Jinbao Xue, Jun Xia, Junqiang Zheng, Kai Liu, Kai Zhang, Kai Zheng, Kejiao Li, Keyao Wang, Lan Jiang, Lixin Liu, Lulu Wu, Mengyuan Huang, Peijie Yu, Peiqi Wang, Qian Wang, Qianbiao Xiang, Qibin Liu, Qingfeng Sun, Richard Guo, Ruobing Xie, Saiyong Yang, Shaohua Chen, Shihui Hu, Shuai Li, Shuaipeng Li, Shuang Chen, Suncong Zheng, Tao Yang, Tian Zhang, Tinghao Yu, Weidong Han, Weijie Liu, Weijin Zhou, Weikang Wang, Wesleye Chen, Xiao Feng, Xiaoqin Ren, Xingwu Sun, Xiong Kuang, Xuemeng Huang, Xun Cao, Yanfeng Chen, Yang Du, Zhen Yang, Yangyu Tao, Yaping Deng, Yi Shen, Yigeng Hong, Yiqi Chen

### Abstract

We present Hunyuan-A13B, an open-source large language model based on a Mixture-of-Experts architecture. It contains 80 billion total parameters but activates only 13 billion during inference, balancing model capability, computational efficiency, and deployment cost. The model is pretrained on a rigorously filtered 20T-token corpus with enhanced STEM data curation, improving factual reliability and reasoning ability. High-quality supervised fine-tuning and large-scale reinforcement learning further enhance its overall performance. Hunyuan-A13B also introduces a dual-mode Chain-of-Thought framework that adapts reasoning depth to task complexity: fast thinking for routine queries and slow thinking for complex, multi-step problems. Evaluations show competitive performance across mathematics, science, programming, general language understanding, and agent tasks, often approaching that of much larger models. Its high inference throughput makes it suitable for latency-sensitive applications. We release Hunyuan-A13B to support open research and practical LLM deployment.

### 中文一句话结论
Hunyuan-A13B 是一种基于 MoE 架构的80B总参数（13B激活）开源大语言模型，通过双模式 CoT 框架和强化学习在数学、科学、编程等多项任务上达到接近更大模型的性能，且具有高推理吞吐量。

### English TL;DR
Hunyuan-A13B is an open-source Mixture-of-Experts large language model with 80B total parameters (13B activated). It achieves strong performance across math, science, programming, language understanding, and agent tasks using a dual-mode Chain-of-Thought framework, combined with high-quality data curation and large-scale reinforcement learning, while maintaining high inference throughput suitable for latency-sensitive applications.

### 中文详细总结
Hunyuan-A13B 是一种基于混合专家（Mixture-of-Experts, MoE）架构的大语言模型，总参数达到800亿，但推理时仅激活130亿参数，实现了能力、效率与部署成本的良好平衡。该模型在精心过滤的20万亿 token 语料库上进行预训练，并重点增强了STEM（科学、技术、工程、数学）数据的比例，从而提升了事实可靠性和推理能力。随后，通过高质量的有监督微调（SFT）和大规模强化学习（RL）进一步全面优化模型表现。特别地，Hunyuan-A13B 引入了一种双模式思维链（Chain-of-Thought, CoT）框架：针对常规查询采用“快速思维”模式，而对复杂、多步推理问题则使用“慢速思维”模式，自适应地根据任务复杂度调整推理深度。评估结果显示，该模型在数学、科学、编程、通用语言理解以及智能体任务上均具有竞争力，其性能往往接近参数规模更大的模型。此外，其高推理吞吐量使其特别适合延迟敏感的应用场景。作者将 Hunyuan-A13B 开源，以支持开放性研究和实际的大模型部署。

### 方法 / 贡献
**方法：**
1. 采用 MoE 架构，80B总参数，推理时仅激活13B。
2. 基于20T token的预训练数据，包含严格过滤和增强的STEM数据。
3. 后续进行高质量SFT和大规模RL。
4. 提出双模式CoT框架（快速思维 + 慢速思维），根据任务复杂性自适应选择推理深度。

**贡献：**
- 发布了一个高效、开源的MoE大语言模型，兼顾性能和推理效率。
- 展示了数据筛选（特别是STEM数据）和双模式CoT对推理能力的提升。
- 通过SFT与RL的结合，实现了接近更大模型的表现。
- 提供了适合实际部署（低延迟、高吞吐）的解决方案。

### 实验或数据
论文在摘要中提到进行了数学、科学、编程、通用语言理解和智能体任务上的评估，显示模型性能具有竞争力，且接近更大模型。但未提供具体的评估数据集名称、基准细节或对比模型的定量结果。因此，无法从摘要中确定所使用的具体实验设置或数据集清单。

### 值得关注点
- **MoE架构的效率优势**：80B总参数仅13B激活，在保持高性能的同时大幅降低推理计算成本，适合资源受限的部署场景。
- **双模式CoT的自适应推理**：快速/慢速思维机制使模型能根据问题难度动态调整推理资源，提升了实用性与灵活性。
- **数据质量与STEM增强**：严格的语料过滤和STEM数据强化有助于提升事实正确性和逻辑推理能力，这是当前LLM的重要改进方向。
- **接近更大模型的性能**：在多项任务上接近更大参数规模模型的结果，说明MoE和训练策略的有效性。
- **开源发布**：促进LLM研究与低成本部署的可用性。

### 局限性
论文摘要未明确讨论模型局限性。但从描述中可以推断：
- 尽管性能接近更大模型，但在某些极端复杂或知识密集型任务上可能仍有差距。
- MoE架构可能引入额外的工程复杂性（如负载均衡、专家协作等），但论文未展开说明。
- 数据增强主要针对STEM，可能在其他领域（如人文、多语言）的覆盖和效果未充分讨论。
- 评估仅在部分基准上进行，通用泛化能力尚需更多验证。

## 2. Experts Rise Where LLMs Disagree: Using Cross-Model Disagreement to Target Expert Effort in LLM Codebook Revision for Large-Scale Annotation

- Source: arxiv
- arXiv ID: 2609.26926
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.26926v1
- PDF: https://arxiv.org/pdf/2609.26926v1
- DOI: https://doi.org/10.48550/arXiv.2609.26926

### Authors

Zeyu He, Zhuqian Zhou, Kirk Vanacore, Rene F. Kizilcec, Ting-Hao 'Kenneth' Huang

### Abstract

Large-scale text annotation brings expert insight to millions of documents, often through a codebook that AI annotators follow. Developing a robust codebook, however, takes months. Large language models (LLMs) could speed this process by applying an early codebook to the data, surfacing cases with strong LLM disagreement, and eliciting expert feedback to address them. We examined three ways experts can provide feedback for LLM codebook revision: (i) editing LLM-generated revisions driven by cross-LLM disagreement (Codebook Verifying), (ii) answering questions about LLM disagreements (Question Answering), and (iii) labeling disagreement cases with rationales (Rationale Labeling). Experiments on thousands of tutoring-session transcripts show that Rationale Labeling yielded the highest LLM-labeling accuracy (64.9%) against expert labels, outperforming the expert-revised codebook (57.8%). The best Question Answering setting also outperformed it (60.5%). Our work shows that LLMs can be used to strategically target expert attention, shortening months of codebook revision to days without sacrificing labeling performance.

### 中文一句话结论
利用多个大语言模型对同一标注任务的分歧来引导专家针对性地反馈，能使模型在几天内将标注准确率提升至超过专家数月迭代的最终版编码手册。

### English TL;DR
By targeting expert feedback to cases where multiple LLMs disagree, the study shows that having experts label and explain those disagreement cases enables LLM-driven codebook revision to achieve higher annotation accuracy (64.9%) than months of traditional expert codebook revision (57.8%).

### 中文详细总结
该研究提出一种利用多个大语言模型（LLM）之间的标注分歧来加速编码手册迭代的工作流。在真实的辅导会话转录文本标注项目中，研究者先让六个不同的 LLM 使用早期版本的编码手册对数千条未标注数据进行标注；然后选出模型分歧最大的样本，引导专家以三种方式提供反馈：(i) 编辑 LLM 根据分歧自动生成的修改建议（Codebook Verifying）；(ii) 回答 LLM 提出的关于歧义规则的问题（Question Answering）；(iii) 对分歧样本进行标注并给出理由（Rationale Labeling）。实验表明，Rationale Labeling 方式使 LLM 的标注准确率达到 64.9%，超过专家花费六个月迭代产生的最终编码手册效果（57.8%）；最优设置的 Question Answering 也优于专家手册（60.5%）。研究说明，将专家有限的时间集中在模型分歧样本上，可以极大缩短编码手册的开发周期（从数月缩短至数天）且不牺牲甚至提升标注性能。

### 方法 / 贡献
- 提出了“跨模型分歧驱动专家反馈”的工作流：先用多个LLM标注，计算分歧，再将分歧样本呈现给专家。
- 设计了三种专家反馈接口：Codebook Verifying（审核编辑LLM的修改建议）、Question Answering（回答LLM生成的规则问题）、Rationale Labeling（标注分歧样本并给出推理过程）。
- 贡献在于将模型分歧转化为可重用的编码手册指令，实证比较了三种反馈方式在真实标注项目中的效果，记录了专家投入时间与感知负担。

### 实验或数据
- 数据集：数千条真实辅导会话转录文本的标注项目，专家已在此项目上迭代编码手册六个月。
- 实验设置：使用六个不同的LLM（具体模型未在摘要和预览中列出）对6595条未曾被专家标注过的数据进行标注，依据分歧程度选择样本。
- 评估方式：将各条件下修改后的编码手册用于LLM标注一个共享测试集，并与专家共识的黄金标签对比，计算准确率和加权F1。
- 关键结果：Rationale Labeling准确率64.9%，专家最终手册57.8%，最优QA设置60.5%。

### 值得关注点
- Rationale Labeling不仅准确率最高，而且专家只需对少量分歧样本进行标注和解释，远少于传统方法中专家需要逐条讨论所有数据的工作量。
- 该方法不依赖大量黄金标签（gold labels），适合早期编码手册迭代阶段。
- 研究验证了“模型分歧=编码手册缺陷”这一直觉，并提供了可操作接口。

### 局限性
- 实验仅基于辅导会话转录这一特定领域，泛化性有待验证。
- 专家反馈仍然耗费一定时间，且反馈质量可能影响效果。
- 研究中未明确讨论跨模型或跨任务的可迁移性；不同LLM组合、分歧阈值的选择等参数调节可能影响结果。
- 论文未详细分析专家反馈中可能的主观偏差或疲劳效应。

## 3. Fine-Tuning LLMs for Translation: General Forgetting Mitigation Does Not Preserve MT-Specific Instruction Following

- Source: arxiv
- arXiv ID: 2609.28395
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.28395v1
- PDF: https://arxiv.org/pdf/2609.28395v1
- DOI: https://doi.org/10.48550/arXiv.2609.28395

### Authors

Niklas Scholz, David Thulke, Abdallah Nasir, Will Allred, Evgeny Matusov, Hermann Ney

### Abstract

Fine-tuning large language models on parallel data improves translation quality but can cause catastrophic forgetting. Mitigation methods are generally evaluated by retention on general benchmarks. We ask whether these findings transfer to machine translation (MT) fine-tuning and to MT-specific instruction following (MT-IF): instructions that modify a translation, such as formality, grammatical gender, and length control. We compare methods anchored to auxiliary data, to model outputs, and to the base model parameters, first in a screening study with Llama 3.2 1B Instruct, then on Llama 3.1 8B Instruct fine-tuned on bidirectional Arabic-English or Spanish-English data. Elastic Weight Consolidation preserves general capabilities best in both stages; on the 8B Spanish model the average score on general benchmarks drops 1.7 points versus 11.0 for standard fine-tuning, yet its scores for formality and grammatical gender control remain close to standard fine-tuning. Only data mixing with control-task examples preserves these controls, but its gains do not transfer to unseen prompts for the same task.

### 中文一句话结论
微调大型语言模型（LLM）用于机器翻译时，通用遗忘缓解方法（如弹性权重巩固）虽能保持通用能力，但无法保留翻译特有的指令遵循（如形式性、语法性别控制），只有数据混合（加入控件任务示例）能保护这些能力，但无法泛化到未见过的提示。

### English TL;DR
Fine-tuning LLMs for translation causes forgetting of MT-specific instruction following (e.g., formality, gender control); Elastic Weight Consolidation preserves general capabilities but not these controls, while only data mixing with control-task examples protects them, albeit without transfer to unseen prompts.

### 中文详细总结
本文研究了在机器翻译（MT）微调过程中，通用遗忘缓解方法是否能同时保护翻译特有的指令遵循能力（MT-IF），如控制形式性、语法性别和输出长度。研究对比了多类方法：锚定辅助数据（数据混合、模型融合、弹性权重巩固EWC及变体EWC-DR）、锚定模型输出（KL散度正则化、选择性标记掩蔽、自信冲突掩蔽、熵自适应微调）和锚定基础模型参数（冻结底层、选择性投影衰减、低秩适应LoRA）。实验分两阶段：首先在Llama 3.2 1B Instruct模型上对三种语言对（阿姆哈拉语→英语、阿拉伯语→英语、西班牙语→英语）进行筛选，然后在Llama 3.1 8B Instruct模型上对双向阿拉伯语-英语和西班牙语-英语进行主实验。结果显示：EWC在保持通用能力上最优（8B西班牙模型通用基准平均分仅下降1.7分，而标准微调下降11.0分），但其形式性和语法性别控制分数与标准微调接近；只有数据混合（在微调数据中加入控制任务示例）能保留这些控制能力，但该效果无法迁移到同一任务的未见提示上。论文贡献包括：在MT微调情境下系统比较了多种遗忘缓解方法，并指出通用基准分数无法捕捉MT特有指令遵循能力的丢失。

### 方法 / 贡献
1. 在MT微调中系统比较了锚定辅助数据、模型输出和基础模型参数的三类遗忘缓解方法，涵盖11种具体方法，涉及三个语言对和两种模型规模。
2. 通过评估形式性、语法性别和长度控制，证明通用基准的保留与MT特有能力丢失可以共存，仅依赖通用基准会遗漏关键能力损失。
3. 发现仅数据混合（加入控件任务示例）能保护MT-IF，但泛化性有限；EWC虽保持通用能力却无法保护MT-IF。

### 实验或数据
- 两阶段实验：第一阶段在Llama 3.2 1B Instruct上对阿姆哈拉语→英语、阿拉伯语→英语、西班牙语→英语微调；第二阶段在Llama 3.1 8B Instruct上对双向阿拉伯语-英语和西班牙语-英语微调。
- 评估指标：翻译质量（COMET、BLEU）、通用能力（GSM8K、DROP、TruthfulQA、HumanEval等Tülu 3子集）、MT-IF（基于CoCoA-MT和MT-GenEval改造的形式性、语法性别控制测试，以及长度控制任务）。
- 数据：MT微调使用平行数据；通用遗忘缓解方法中的辅助数据来自Tülu 3 SFT混合的子集；控件任务示例来自对应控制任务的数据。

### 值得关注点
- 通用遗忘缓解方法（如EWC）在保持通用能力上效果显著，但对MT特有指令遵循几乎无效，说明“通用遗忘”与“特定能力遗忘”是不同维度。
- 数据混合是唯一能保护MT-IF的方法，但其效果仅限于训练过的控件任务示例，无法泛化到新提示，提示MT-IF的保护需要针对性的数据。
- 实验结果表明，评估MT微调的遗忘状况不能仅依赖通用基准，必须加入翻译特有的指令遵循测试。

### 局限性
- 实验仅限于阿拉伯语-英语和西班牙语-英语两个语言对，以及Llama 3.2 1B和3.1 8B两种模型，结论是否推广到其他语言/模型有待验证。
- 仅评估了单个方法的孤立效果，未探索方法组合（如数据混合+EWC）是否更优。
- 数据混合保护MT-IF的效果无法泛化到未见提示，其实际应用价值受限，未进一步研究原因或改进方向。
- MT-IF评估限于形式性、语法性别和长度控制，其他指令（如风格、术语）未被覆盖。

## 4. Uncheatable Eval: Dynamic Compression-Based Evaluation of Language Models

- Source: arxiv
- arXiv ID: 2609.27510
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.27510v1
- PDF: https://arxiv.org/pdf/2609.27510v1
- DOI: https://doi.org/10.48550/arXiv.2609.27510

### Authors

Kaifeng Tan, Yudong Li, Linlin Shen

### Abstract

Modern large language models are pretrained on massive datasets, making it difficult to prevent benchmark data from entering their training sets and undermining the reliability of evaluation results. Reliable evaluation is particularly challenging for base models, whose limited instruction-following ability complicates task-based assessment. We introduce Uncheatable Eval, a dynamic benchmark that regularly collects newly published text to evaluate base language models and reduce the risk of data contamination. Drawing on the relationship between a model's predictive ability and its ability to compress data losslessly, we use compression rate to evaluate how well models predict new text. We evaluate 80 models across 14 text categories, study how compression changes with context length, and examine the correlation between compression rate and zero-shot MMLU accuracy. Our results yield three main findings: (1) compression performance follows a consistent scaling trend with model size; (2) attention-based, hybrid, and recurrent models differ in how their compression performance changes as more context becomes available; and (3) lower compression rates are strongly associated with higher zero-shot MMLU accuracy. Code is available at https://github.com/Jellyfish042/uncheatable_eval.

### 中文一句话结论
Uncheatable Eval 通过动态收集最新文本并利用压缩率评估基础语言模型，有效降低了数据污染风险，并发现模型缩放趋势、上下文长度对不同架构的影响以及压缩率与 MMLU 准确率的强相关性。

### English TL;DR
Uncheatable Eval is a dynamic benchmark that evaluates base language models by measuring their compression rate on newly published text to mitigate data contamination, revealing consistent scaling trends, differential context effects across model families, and a strong correlation between lower compression rates and higher zero-shot MMLU accuracy.

### 中文详细总结
Uncheatable Eval 提出了一个动态基准测试方法，通过定期收集最新发布的文本（涵盖小说、新闻、百科、科学论文、代码等14个类别）来评估基础语言模型，以减少训练数据污染对评测结果的影响。该方法基于语言模型预测能力与无损压缩能力之间的关系，使用压缩率（CR）衡量模型对新文本的预测效果。研究对80个模型进行了评测，发现了三个主要结果：（1）压缩性能随模型规模呈一致的标度趋势；（2）注意力机制、混合和循环模型在上下文长度变化时压缩性能表现不同；（3）较低的压缩率与较高的零样本 MMLU 准确率强相关。代码已开源。

### 方法 / 贡献
1. 提出了动态基准 Uncheatable Eval，通过收集新发表文本并设计数据清洗流程（质量过滤、去重、标准化、跨语言平衡采样）来评估基础模型。
2. 评测了80个模型（注意力、混合、循环架构）在14个文本类别上的压缩率，提供了广泛的性能对比。
3. 分析了压缩率随模型规模和文档位置的变化，以及压缩率与零样本 MMLU 准确率的相关性。

### 实验或数据
- 数据集：2026年7月新发表的文本，共14个类别，每个类别500个样本，总计7,000个样本。每个样本被截断到最多3,584个token（兼容8种分词器）。
- 模型：80个模型，包括注意力、混合和循环架构，参数规模从数亿到数百亿不等。
- 长上下文评估：对54个模型在科学论文子集（计算机科学、数学、物理、其他科学）上评估，保留最多32,768字节，分析字节级压缩率随位置的变化。
- 跨类别压缩率：对每个类别计算字节加权压缩率，整体得分为各类别压缩率的算术平均值。

### 值得关注点
- 方法创新：利用压缩率替代任务式评测，避免指令遵循能力的干扰，直接评估基础模型对新文本的预测能力。
- 动态数据收集：定期更新测试文本，有效降低污染风险。
- 强相关性：压缩率与零样本 MMLU 准确率呈强关联，表明压缩率可作为基座模型知识能力的代理指标。
- 架构差异：不同架构（注意力、混合、循环）在长上下文下压缩率变化模式不同，揭示了模型处理长文本的特性。

### 局限性
- 压缩率评测仅反映语言模型的预测能力，无法全面评估指令遵循、推理、生成等复杂能力。
- 动态收集文本仍需保证质量，且仅覆盖文本类型，未涉及多模态或交互式场景。
- 长上下文评估仅限于科学论文，其他类型文本（如长代码或小说）未包含。
- 压缩率与任务性能的关联可能因领域而异，需进一步验证泛化性。
- 当前基准仅针对基础模型，对指令微调模型的适用性需调整。

## 5. COPE: Continual Personalization of LLMs under Sparse User Feedback via User Embeddings and Self-Evaluation

- Source: arxiv
- arXiv ID: 2609.26853
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.26853v1
- PDF: https://arxiv.org/pdf/2609.26853v1
- DOI: https://doi.org/10.48550/arXiv.2609.26853

### Authors

Ruike Cao, Fugen Yao, Liang Dong, Jian Xu, Guanjun Jiang, Li Xiao

### Abstract

While Large Language Models (LLMs) have achieved remarkable results across various benchmarks, their alignment with normative values often results in homogenized responses that fail to address diverse user preferences. Existing training-free methods often occupy valuable context windows through prompt engineering, while training-based methods typically remain static post-training, failing to support the continual optimization required in real-world settings. To address these challenges, we propose COPE (Continual Optimization with Personalized embedding and self-Evaluation), a novel optimization framework tailored for real-world-motivated interaction settings with sparse user feedback. Our framework assigns learnable personalized embeddings to each user and synergistically integrates preference capture, self-evaluation calibration, and personalized response optimization within a single update step. A key innovation of our method is the use of self-evaluation to generate proxy rewards, enabling continuous model updates even when explicit user feedback is unavailable. Experiments show that COPE consistently outperforms strong training-free and training-based baselines under sparse feedback, and remains complementary to Retrieval-Augmented Prompting (RAP). Further analyses confirm COPE's reliable self-evaluation, meaningful preference patterns, stable general capabilities, and robustness under shifting preferences and alternative evaluators.

### 中文一句话结论
COPE通过为每个用户分配可学习的个性化嵌入并引入自我评估机制生成代理奖励，在稀疏用户反馈条件下实现了大语言模型的持续个性化优化，并显著优于现有方法。

### English TL;DR
COPE proposes a continual optimization framework for LLM personalization under sparse user feedback. It maintains learnable user embeddings to capture individual preferences and uses self-evaluation to generate proxy rewards, enabling continuous model updates even without explicit feedback. Experiments show consistent outperformance over strong training-free and training-based baselines, with complementary benefits to Retrieval-Augmented Prompting.

### 中文详细总结
针对大语言模型在个性化响应中面临用户反馈稀疏、难以持续优化的问题，本文提出COPE框架。该框架为每个用户分配可学习的个性化嵌入，并通过“交互-收集-优化”循环进行迭代更新。每个优化步骤融合三个目标：监督微调从用户反馈中提取偏好、强化学习校准自我评估以生成代理奖励、以及强化学习优化个性化响应。实验表明，COPE在稀疏反馈下持续优于多种训练无关和训练基线的基线方法，且能与检索增强提示（RAP）互补。进一步分析验证了COPE自我评估的可靠性、学习到的嵌入捕捉有意义的偏好模式、通用能力保持稳定，以及对偏好变化和替代评估器的鲁棒性。

### 方法 / 贡献
1. **持续个性化交互设定**：建立了一个基于现实动机的持续个性化设置，模拟稀疏用户反馈下的交互，并在PersonaLens上实现受控时间顺序遍历协议，桥接了静态基准与持续优化的评估。
2. **COPE框架**：为每个用户维护可学习的个性化嵌入作为偏好表示，在“交互-收集-优化”循环中同步更新嵌入和模型参数。核心创新是利用自我评估为无显式反馈的交互生成代理奖励，最大化利用所有交互数据。
3. **统一优化步骤**：三个目标协同——(a) 监督微调将文本反馈编码进嵌入；(b) 强化学习校准自我评估使其预测与用户评分一致；(c) 强化学习结合完整性奖励和个性化奖励（来自真实或代理反馈）优化响应生成。
4. **实验结果**：在多种反馈概率下COPE持续超越强基线，且与检索增强提示（RAP）互补；自我评估可靠、嵌入具有语义可解释性、通用能力保持稳定、对偏好变化鲁棒，并适用于替代评估器。

### 实验或数据
实验基于PersonaLens数据集，采用受控时间顺序遍历协议模拟持续对话交互。在稀疏反馈条件下（反馈概率p从低到高）测试COPE与多种基线，包括训练无关方法（如RAP、PAP）和训练基方法（如RLPA、PEFT等）。结果显示：
- COPE在各项反馈概率下均一致优于所有基线；
- COPE与RAP结合可进一步提升性能；
- 自我评估的预测与用户真实反馈高度一致；
- 学习到的嵌入聚类显示出有意义的偏好模式（如风格、格式偏好）；
- 优化后的模型在通用benchmark上保持稳定；
- 在偏好变化和采用不同评估器时仍有效。
具体数值结果在正文中呈现，摘要未详细列出各指标。

### 值得关注点
1. **自我评估生成代理奖励**：通过训练模型预测自己的响应得分，在无用户反馈时充当奖励信号，使所有交互数据都能用于优化，有效缓解反馈稀疏问题。
2. **可学习个性化嵌入**：紧凑的嵌入向量（若干虚拟token）代替冗长的用户描述或历史记录，节省上下文窗口且随交互动态更新。
3. **三步合一优化**：在单次更新中同时完成偏好捕捉、自我评估校准和响应优化，高效利用有限反馈。
4. **与RAP互补**：COPE可以叠加检索增强提示进一步提升效果，说明其与现有方法兼容。
5. **综合鲁棒性分析**：验证了偏好变化、不同评估器条件下的有效性，以及通用能力保持。

### 局限性
1. **每个用户需要独立嵌入**：在大规模用户群体下，存储和计算开销随用户数线性增长，可能限制扩展性。
2. **自我评估依赖前期校准**：在完全无初始反馈的冷启动场景下，评估准确性可能不足，效果受限。
3. **多轮会话扩展未充分验证**：论文在附录中提及可扩展到多轮对话，但核心实验仅在单轮设定下进行，尚未充分验证多轮场景效果。
4. **偏好变化实验有限**：虽然做了偏好迁移测试，但实际使用中偏好变化更频繁或更复杂，需要更长期的持续优化研究。
5. **任务域依赖**：实验基于PersonaLens数据集，不同任务域（如客服、创意写作）的泛化性尚未验证。

## 6. Count Evidence, Not Sentences: Tempered Evidence Fusion of LLM Judgments for Long-Text Value Measurement

- Source: arxiv
- arXiv ID: 2609.27165
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.27165v1
- PDF: https://arxiv.org/pdf/2609.27165v1
- DOI: https://doi.org/10.48550/arXiv.2609.27165

### Authors

Yuhe Wu, Rui Qian, Guangyu Wang, Yuran Chen, Yuanchao Zhu, Junjie Yang, Zhengheng Li, Jiulin Cai, Tianyi Zhang, Zihan Dong, Jiaxin Liu, Yujie Chen, Guang Zhang

### Abstract

Large language models (LLMs) are increasingly used to measure public value orientations from long social media posts, yet such posts often mix background, quotations, concessions, and only a few stance-bearing sentences. Existing approaches either ask the model to predict a document-level label directly, which can be overconfident, or aggregate sentence-level predictions by majority or soft voting, which treat uncertain and decisive sentences as equally informative. We formulate long-text value measurement as a decision-fusion problem and propose Tempered Evidence Fusion (TEF), a training-free rule that weights each sentence's log-odds by its normalized information gain, as derived from a generalized Bayesian posterior. This makes the fused score nearly vanish for uncertain sentences while preserving the Bayes-optimal weight of decisive evidence. We further introduce Multi-event Insight Network Dimensions (MIND), a benchmark of 8,358 Chinese and English posts spanning five years of public events and six value dimensions. On MIND, TEF outperforms the strongest baseline among Direct, Majority Vote, and Soft Vote by an average of 4.5 accuracy points and 4.6 macro-F1 points across five LLMs and two languages. MIND dataset and code are available at https://github.com/Kzczc/ICASSP2027-TEF.

### 中文一句话结论
本文提出无训练融合规则TEF，通过对句子对数几率按信息增益加权，在长文本价值测量中优于直接预测和投票基线，在MIND双语基准上平均提升4.5个准确率点和4.6个宏F1点。

### English TL;DR
Tempered Evidence Fusion (TEF) improves long-text value measurement from LLM judgments by weighting each sentence's log-odds by its normalized information gain—discounting uncertain evidence—and outperforms direct prediction and voting baselines by 4.5 accuracy points and 4.6 macro-F1 points on the new MIND benchmark of 8,358 bilingual posts across six value dimensions.

### 中文详细总结
- **问题**：LLM用于测量长社交媒体帖子中的公众价值取向时，帖子常混合背景、引用、让步句，仅少数句子表达立场。现有方法（直接预测整文档标签、多数投票/软投票聚合句子级预测）要么过度自信，要么将不确定与决定性句子等权处理。
- **方法**：将长文本价值测量形式化为决策融合问题，提出**Tempered Evidence Fusion (TEF)**。TEF是一个无需训练的规则，对每个句子的对数几率（log-odds）乘以其归一化信息增益权重（$w_i = 1 - H(p_i)/\log K$），该权重由广义贝叶斯后验导出。这使得不确定句子的贡献近乎消失，同时保留决定性证据的贝叶斯最优权重。
- **基准**：构建**MIND**基准，包含8,358条中文和英文帖子，覆盖五年公共事件和六个价值维度。
- **结果**：在五个LLM和两种语言上，TEF平均超过Direct、Majority Vote和Soft Vote中最强的基线4.5个准确率点和4.6个宏F1点，且校准更好。
- **理论支撑**：TEF基于分段条件独立和校准后验的贝叶斯假设，与多数投票相比保留更多信息；其权重等价于均匀先验下的信息增益，实现了软截断。

### 方法 / 贡献
1. **形式化**：首次将LLM长文本价值测量形式化为句子级决策融合问题。
2. **TEF规则**：提出无训练融合规则，采用归一化信息增益作为句子可靠性权重，结合一对多的对数几率证据，实现软截断效果。
3. **理论分析**：证明TEF保留信息（命题1）且近似贝叶斯最优加性对数几率（命题2）。
4. **MIND基准**：构建双语、跨五年、六维度的公开事件帖子基准数据集（8,358条）。
5. **实证优势**：在多种LLM和双语设置下优于直接预测和各类投票基线，且更好校准。

### 实验或数据
- **数据集**：MIND，包含8,358条中文和英文社交媒体帖子，涵盖2018–2022年六个事件领域（如经济、气候等），标注六个价值维度（如平等、自由等）。数据来自公开来源，经筛选、匿名、去重、三轮标注。
- **模型**：评估五个LLM（未具体说明，可能包括GPT系列等）。
- **基线**：Direct（整文档标签）、Majority Vote、Soft Vote。
- **结果**：TEF在所有设置中平均比最强基线高4.5%准确率和4.6%宏F1。具体数字见论文表，未在此预览中提供。
- **代码与数据**：已开源（GitHub链接：https://github.com/Kzczc/ICASSP2027-TEF）。

### 值得关注点
- **无需训练**：TEF是纯规则，不依赖额外训练或微调，即插即用。
- **软截断机制**：通过信息增益权重自动抑制不确定句子，而决定性句子即使数量少也能主导结果。
- **理论优雅**：从贝叶斯决策融合导出，有明确数学依据。
- **跨语言泛化**：在中文和英文上均有效。
- **新基准**：MIND填补了双语、多事件、多维度长文本价值测量基准的空缺。

### 局限性
- **条件独立假设**：TEF推导假设句子间条件独立，实际长文中可能存在引用或逻辑依赖，可能影响最优性。
- **依赖句子级LLM校准**：权重基于句子级后验熵，若LLM在特定领域校准差（如罕见价值维度），权重可能不准确。
- **基准覆盖有限**：MIND仅包含特定公共事件和六个价值维度，泛化到其他事件或维度需验证。
- **未比较更多融合方法**：仅与三种经典投票基线对比，未包括学习式融合或变分贝叶斯方法。
- **计算开销**：句子级推理需多次LLM调用，相比直接预测成本更高。

## 7. Learning When Not to Listen: Selective Anti-Interference Pretraining for Language Models

- Source: arxiv
- arXiv ID: 2609.27925
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.27925v1
- PDF: https://arxiv.org/pdf/2609.27925v1
- DOI: https://doi.org/10.48550/arXiv.2609.27925

### Authors

Jinchang Zhu, Haowei He, Yi Ding, Rong Fu, Nie Xiaojian, Shuangyong Song, Zhongjiang He, Menglin Yang

### Abstract

Language models can over-condition on irrelevant preceding text: predictions already supported by local context may still change when distant, unrelated prefix tokens are perturbed. This interference is especially consequential in long, packed, or distractor-heavy contexts, where useful evidence and irrelevant spans coexist. We propose Selective Prefix Anti-Interference Regularization (SPAR), a pretraining objective for selective anti-interference. SPAR runs the original sequence and a corrupt-prefix input in which only the far prefix is changed, then uses a short-context sufficiency gate and a gated KL objective to stabilize locally supported suffix predictions. The gate operationalizes a model-based estimate of whether the far prefix supplies additional information about the target token. Mechanism analyses show that the gate identifies locally sufficient tokens and sharply reduces prefix sensitivity on gate-selected suffix tokens. In continued training on pretrained base models, SPAR improves RULER across Qwen2.5-0.5B, Qwen2.5-3B, Llama-3.2-1B, Llama-3.1-8B, and GPT2-XL under equal counted training compute; pretraining experiments further show gains on both RULER and NoLiMa. These results show that selective anti-interference is an effective objective-level signal for robust context use.

### 中文一句话结论
SPAR通过一个短上下文充分性门控和门控KL散度目标，选择性地稳定语言模型在无关远上下文下的局部可预测标记的预测，从而在长文本和干扰场景下显著提升鲁棒性。

### English TL;DR
SPAR is a pretraining objective that selectively stabilizes language model predictions against irrelevant distant context by using a short-context sufficiency gate and gated KL divergence to regularize locally supported suffix tokens.

### 中文详细总结
本文提出选择性前缀抗干扰正则化（SPAR），一种针对语言模型的预训练目标，旨在解决模型对无关远前缀的过度依赖问题。标准因果语言模型优化所有前缀下的下一个标记预测，但未区分有用证据与无关干扰。SPAR通过构建原始序列和扰动远前缀的对比输入，利用短上下文充分性门选择那些已局部可预测的后缀标记，并通过门控KL散度损失使这些标记在远前缀变化下保持稳定。机制分析表明，门控能有效识别局部充分的标记，并大幅降低模型对门控选中标记的前缀敏感性。

### 方法 / 贡献
- **问题形式化**：将远前缀干扰定义为选择性条件依赖问题——局部充分的预测应不受无关前缀影响，全-短似然差可作为应用不变性信号的指标。
- **SPAR目标**：对每个训练序列，同时运行原始序列和仅远前缀被扰动的输入；通过短上下文充分性门控（基于全-短似然比）选择局部充分的标记；仅对这些标记施加门控KL散度损失，稳定其预测分布，而标准因果语言模型损失保持全序列优化。
- **关键贡献**：提出一种显式的预训练不变性信号，使模型学会区分有用远证据与无关干扰。

### 实验或数据
- **继续训练实验**：在Qwen2.5-0.5B/3B、Llama-3.2-1B、Llama-3.1-8B、GPT2-XL五个预训练基座模型上，在相同计算量下，SPAR在RULER基准上平均提升0.33–3.43分（按上下文长度分层报告）。
- **从头预训练实验**：在0.3B、0.6B、1B三种规模上，SPAR在RULER和NoLiMa两个基准上均有提升：RULER平均增益1.23–3.62分，NoLiMa平均增益1.98–3.60分（三随机种子平均）。
- **门控机制分析**：固定参考门控分析验证了门控能准确识别局部充分的标记，且模型对门控选中标记的前缀敏感性显著降低。

### 值得关注点
- **创新点**：将抗干扰问题转化为预训练阶段的选择性不变性学习，而非后处理或数据增强。
- **灵活性**：适用于不同规模（0.3B–8B）和架构的模型，同时覆盖继续训练和从头预训练场景。
- **可解释性**：门控机制提供可分析的“哪些标记应忽略远前缀”的决策依据。

### 局限性
- 论文未讨论SPAR在超长上下文（>32K标记）或非因果注意力模型上的表现。
- 实验仅依赖合成基准（RULER、NoLiMa），未在真实世界长文本任务（如法律文档、论文摘要）上验证。
- 门控机制依赖短上下文似然比，可能对短上下文质量敏感。
- 未与最新抗干扰方法（如LongPPL、SkipAlign）进行直接对比。

## 8. Repurposing Pre-trained LLMs as High Fidelity Continuous Text Autoencoders

- Source: arxiv
- arXiv ID: 2609.27248
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.27248v1
- PDF: https://arxiv.org/pdf/2609.27248v1
- DOI: https://doi.org/10.48550/arXiv.2609.27248

### Authors

Arkanath Pathak, Unnat Jain, Alexander C. Berg

### Abstract

Next-token prediction has enabled highly fluent autoregressive language models, but it represents global structure only indirectly through sequential factorization. In contrast, high-fidelity autoencoders have become a standard primitive in image generation, enabling generative models to operate over continuous latent spaces; text lacks a comparably faithful continuous representation. We propose LLMAE, a method for repurposing a pretrained decoder-only language model as a continuous text autoencoder by exposing an intermediate fixed-length latent bottleneck within its internal activations. Instantiated with a parameter-efficient 270M Gemma 3 model, LLMAE uses structured attention masks, LoRA adaptation, and KL regularization to learn an autoencoding interface that leverages the generative prior of the original LLM. We train LLMAE to reconstruct text sequences up to 1024 tokens, significantly improving on this task to achieve near-perfect reconstruction. Furthermore, we demonstrate the downstream utility of this representation by training a latent text diffusion model for detailed image captioning using the learned LLMAE autoencoder. By mapping text into a fixed-length continuous latent space, our approach provides an effective substrate for downstream adaptation while benefiting from the fluency of the original LLM.

### 中文一句话结论
LLMAE 通过将预训练解码器专用大型语言模型内部中间层暴露为固定长度连续潜变量瓶颈，实现了高质量的文本自编码，并支持下游潜扩散模型进行详细图像描述。

### English TL;DR
LLMAE repurposes a pretrained decoder-only LLM into a high-fidelity continuous text autoencoder by introducing a fixed-length latent bottleneck at an intermediate layer via structured attention masks, achieving near-perfect reconstruction of up to 1024 tokens and enabling downstream latent diffusion for tasks like image captioning.

### 中文详细总结
LLMAE 是一种将预训练解码器专用LLM（如270M参数的Gemma 3）改造为连续文本自编码器的方法。通过在模型内部某中间层插入固定长度的潜变量瓶颈（由可学习Embed token的激活表示），并配合结构化注意力掩码、LoRA低秩适应和KL正则化，LLMAE 能够以少量可训练参数（仅10.7M）实现对长达1024个token的文本序列进行近乎无损的重建。该方法进一步展示了学得的连续潜表示在下游任务中的实用性：利用该潜空间训练一个轻量级的文本扩散模型，用于生成详细的图像描述，其性能超越了较大的自回归基线，缩小了与前沿视觉语言模型的差距。

### 方法 / 贡献
- **LLMAE框架**：首次利用预训练解码器LLM的中间层激活作为固定长度的连续潜变量瓶颈，通过修改注意力掩码将模型划分为编码器和解码器两部分。
- **重建分析**：通过综合实验证明在长达1024个token的文本序列上达到近乎完美重建（优于以往文本自编码器），并确认中间层（“熵谷”）是最优瓶颈位置。
- **下游生成效用**：利用冻结的LLMAE潜表示训练一个轻量级潜文本扩散模型（111M可训练参数），在详细图像描述任务上生成流畅、高质量的描述，超越较大自回归基线并接近前沿VLM性能。
- 采用LoRA微调，仅需10.7M可训练参数；额外加入单层Transformer Codec和KL正则化以提升潜表示平滑性。

### 实验或数据
论文摘要未具体描述实验所用数据集或详细实验设置，但提到对长达1024个token的文本序列进行重建任务，并达到近乎完美重建。下游图像描述任务展示了方法的有效性，但未明确给出数据集名称或标准指标（如CIDEr、BLEU等）的具体数值。

### 值得关注点
- 利用预训练LLM的生成先验，通过简单的注意力掩码修改实现高效自编码，避免从头训练。
- 潜表示固定长度，便于下游生成模型（如扩散模型）直接使用。
- 在较小型模型（270M参数）上实现高保真重建，参数量低于大部分之前的工作。
- 验证了“熵谷”假设在自编码任务中的有效性。

### 局限性
论文摘要未明确讨论方法的局限性。基于内容推测可能的局限包括：瓶颈长度固定（可能限制极长序列的编码）；依赖于特定预训练模型（Gemma 3）；KL正则化可能造成信息损失；仅在下游图像描述任务上验证，未展示其他NLP任务（如翻译、摘要）上的泛化能力。

## 9. How Much Were You Told? Measuring External Information in Peer Reviews

- Source: arxiv
- arXiv ID: 2609.28041
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.28041v1
- PDF: https://arxiv.org/pdf/2609.28041v1
- DOI: https://doi.org/10.48550/arXiv.2609.28041

### Authors

Matthieu Dubois, Pablo Piantanida, François Yvon

### Abstract

Conference policies distinguish using Large Language Models (LLMs) to polish one's own review from delegating the critique, but current Artificial Text Detection (ATD) methods largely measure surface form rather than the origin of its content. We instead measure the external information carried by a review: information not explained by the reviewed paper and a generic reviewing instruction. We propose Self-Conditioning, an unsupervised information-theoretic estimator that compares the likelihood of a review under its production context with its likelihood when that context is augmented with hints extracted from the review itself. On the IntelLabs peer-review benchmark, Self-Conditioning separates fully-delegated from machine-polished reviews with AUC up to $1.0$ while remaining largely insensitive to surface rewriting. Moreover, as generators receive increasing amounts of externally-provided information, their scores move monotonically towards the human regime, unlike standard ATD baselines. High-temperature sampling can evade the estimator, but at the cost of output quality.

### 中文一句话结论
本文提出一种无监督信息论方法Self-Conditioning，通过量化同行评审中的“外部信息”量（即无法由论文和通用审稿指令解释的信息），有效区分完全由大语言模型代写的评审与人类撰写或仅经AI润色的评审。

### English TL;DR
This paper introduces Self-Conditioning, an unsupervised information-theoretic estimator that measures the external information in peer reviews—information not explained by the paper and generic instructions—effectively distinguishing fully-delegated LLM reviews from machine-polished ones while remaining robust to surface rewriting.

### 中文详细总结
当前AI文本检测（ATD）主要关注文本的表面统计形式（即是否为机器生成），无法满足机器学习顶级会议（如NeurIPS, ICLR）对“润色”与“代写”的政策区分需求。本文重新定义了核心问题，不再问“这是AI写的吗？”，而是问“这篇评审中包含了多少外部信息？”。作者将外部信息定义为：在给定论文和通用审稿指令之后，评审文本中仍无法被该基础语境所解释的信息。为此，他们提出了无监督的**Self-Conditioning**估计量。该方法利用代理语言模型（Llama-3.1-8B-IT），通过比较评审在基础语境下的似然度与在加入自身提示（如随机暴露的词语）后的似然度，计算信息增益。增益大，说明评审包含了审稿人/系统提供的、超出论文本身的独特思想（外部信息多，如人类或润色）；增益小，说明评审几乎完全由论文信息即可解释（外部信息少，如完全代写）。在IntelLabs基准测试上，该方法在区分“完全代写”与“机器润色”任务上AUC最高达到1.0，且对文本表面改写不敏感。

### 方法 / 贡献
- **贡献：**
    1. 将同行评审的政策合规性问题形式化为对外部信息量的估计。
    2. 提出Self-Conditioning这一无监督估计量，无需人类标注的生成数据即可进行检测。
    3. 验证了分数与外部信息量之间的单调关系，并识别出高温采样（High-temperature sampling）可作为规避手段。
- **方法：**
    核心是条件信息增益。基础语境C（论文+审稿指令），评审文本T。定义提示变量X（例如随机暴露T中30%的词语）。Self-Conditioning得分衡量的是在已知C的情况下，再得知X后对于解释T的平均编码描述长度减少量。该计算基于代理语言模型，完全不需要事先知道T的作者是谁或T是否由AI生成，其分数水平直接反映内容的信息来源。

### 实验或数据
基于**IntelLabs AI同行评审检测基准**（ICLR 2019的500条人类评审，及对应的Claude、GPT-4o、Gemini、Llama-3.1、Qwen生成版本）。实验构建了四种评审模式：
- **FD（完全代写）**、**PI（部分告知）**、**MP（机器润色）**、**H（人类）**。
主要发现：
1. **高分离度**：FD与MP/H的AUC高达1.0。
2. **鲁棒性**：对重写（改写）等表面变化不敏感。
3. **单调性**：随着外部输入信息的增加（从FD到PI到MP），分数单调递增并趋近于人类水平，而传统ATD无法展现这一规律。

### 值得关注点
该工作的核心转变在于从二元检测（是/否AI生成）转向量化估计（思想贡献来源于何处），精准对应了学术界对“润色”与“代写”的政策边界。此外，Self-Conditioning是**无监督**的，不依赖于任何特定生成模型的数据进行训练，使其方法具备较高的通用性和实际部署潜力。

### 局限性
1. **高温采样规避**：模型中极高的低温/高温采样可以降低信息增益差异，从而可能规避检测，但代价是输出质量显著下降。
2. **代理模型依赖**：结果依赖于代理语言模型（Llama-3.1-8B-IT）的质量和提示构建的细节（如随机词暴露比例）。
3. **间接代理**：衡量的是信息论代理指标，而非直接的认知付出或人类参与度，不能完全等同于对撰写过程的诊断。
4. **场景限制**：目前仅在基于现有数据构建的模拟评审场景下验证，真实审稿现场中复杂的人机协作交互尚未完全覆盖。

## 10. EduBehaviors: Assertion-based Schemas for Auditable Coding of Educational Dialogues

- Source: arxiv
- arXiv ID: 2609.27043
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.27043v1
- PDF: https://arxiv.org/pdf/2609.27043v1
- DOI: https://doi.org/10.48550/arXiv.2609.27043

### Authors

Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, Susanna Loeb

### Abstract

Large language models have allowed the rapid deployment of pedagogical annotations corresponding to constructs of interest, allowing a natural language interface for generating classifications on a conversational dataset. However due to the opaque nature of LLM reasoning, we have no verifiable, mechanistic insight into why a model chose a label for an utterance. We introduce the EduBehaviors framework, an interpretable, scalable approach to annotating educational data that uses LLMs to measure repeated observable behaviors relevant to many constructs of interest and then learns a classifier for the construct based on these observable behaviors. We evaluate the framework on the TalkMoves dataset, predicting the Teacher TalkMoves labels. Our best configuration results in a macro-F1 of 0.673 and 0.688 Cohen's kappa, proving competitive with direct prompting approaches. In addition, we release EduBehaviors Toolkit, two tools allowing researchers to operationalize the EduBehaviors framework in their own data.

Here is the bilingual Markdown summary based on the paper metadata and content.

### 中文一句话结论
论文提出了EduBehaviors框架，通过将抽象的教学构念分解为可审计的行为断言，并利用透明分类器组合这些断言，在达到与直接提示方法相竞争的性能的同时，实现了LLM标注过程的可解释性和可溯源性。

### English TL;DR
EduBehaviors is a framework for auditable educational dialogue coding. It decomposes abstract constructs into explicit binary "assertions" of observable behavior, annotated by LLMs, and combined via an interpretable classifier (e.g., logistic regression). This achieves competitive performance (macro-F1 0.673, Cohen’s kappa 0.688 on TalkMoves) against opaque direct-prompting methods while making the reasoning process inspectable and revisable. The released Toolkit (EduBehaviors-Studio & kit) supports iterative schema development and efficient deployment of pretrained encoder models.

### 中文详细总结
该论文指出直接使用LLM进行教育对话标注的主要问题在于其推理过程不透明，导致诊断错误和验证标签变得困难。为此，作者提出了EduBehaviors框架，这是一种将标注流程解耦为两个可审计步骤的方法：
1.  **行为断言（Assertions）：** 将抽象的构念（如教师谈话动作）拆解为一组描述直接可观察行为的二值问题（例如“话语是否包含追问”、“话语是否引用学生观点”）。
2.  **标签组合：** 先由LLM标注这些断言的“是/否”值，再通过一个透明的分类器（如逻辑回归或随机森林）将这些断言值组合成最终的构念标签。
该方法还区分了“定义错误”（规则制定有问题）与“预测错误”（LLM标注断言有误），为迭代改进提供了清晰的反馈路径。同时，论文开源了EduBehaviors-Studio（用于迭代开发断言的交互界面）和EduBehaviors-kit（包含49个预训练编码器的Python包），以降低使用门槛并促进研究的可复现性。

### 方法 / 贡献
*   **可审计的框架设计：** 核心贡献在于将LLM从直接预测构念标签的角色，转变为精确标注可观察行为断言的工具，使整个推理过程由“黑箱”变为“白箱”。
*   **断言生成机制：** 提出两种断言来源，即源于语料库的通用断言和源于构念定义的特定断言，并利用多LLM间的一致性评分（Cohen's kappa > 0.5）作为断言信度的代理。
*   **透明的规则学习：** 断言值作为特征输入传统的分类模型（如逻辑回归），保留了模型的可解释性、概率校准能力以及精度/召回率的可控性。
*   **配套工具：** 发布了EduBehaviors-Studio（辅助研究者迭代生成和完善断言）以及EduBehaviors-kit（包含预训练的SetFit编码器模型，替代昂贵的API调用，实现轻量化、可复现的标注）。

### 实验或数据
*   **数据集：** 使用专家标注的TalkMoves数据集，任务为预测教师谈话动作（Teacher TalkMoves）标签。
*   **关键指标：** 最佳配置取得了0.673的宏F1分数和0.688的Cohen's kappa值，性能与直接提示（Direct Prompting）方法相当。
*   **断言信度：** 在框架内，利用多LLM标注者在断言层面的Cohen's kappa（设定阈值为大于0.5）作为断言质量的筛选指标。
*   **模型训练：** 基于TalkMoves数据的LLM标注，训练并公开了49个用于断言分类的SetFit编码器模型，涵盖训练数据及超参数。

### 值得关注点
*   **审计路径明确：** 当标注结果与研究者判断不符时，框架允许精准定位到具体的断言，从而明确区分是“定义问题”（规则不完善）还是“执行问题”（LLM标注错误）。
*   **解耦与复用性：** 行为断言的标注独立于具体构念，同一个语料的断言标注可复用至多个不同的下游分类任务。
*   **高可复现性与低门槛：** EduBehaviors-kit提供的轻量级编码器模型替代了API调用，使得标注过程完全确定且成本极低，适合不具备大规模计算资源的普通教育研究者。
*   **对直接提示的改进：** 在保持竞争力的同时，解决了直接提示（Direct Prompting）在缺乏标签数据时难以优化、无法校准且缺乏透明度的问题。

### 局限性
*   **对LLM的基础依赖：** 断言生成和初始标注仍依赖LLM，因此框架并未消除LLM本身存在的偏差（如系统性偏差），且LLM间的一致性并不能完美等同于人类判断的信度。
*   **领域迁移与验证成本：** 框架的有效性目前仅在TalkMoves数据集上验证；将其迁移至新的教育对话场景或新的构念时，研究者仍需投入精力构建和验证新的一组断言，并证明其有效性。
*   **断言设计的前期投入：** 设计一套清晰、无歧义且高一致性的断言集需要研究者进行多轮迭代，即便有Studio工具辅助，依然存在一定的前期认知负担和时间成本。
*   **评估范围有限：** 论文的主要实验仅聚焦于TalkMoves数据集上的单一构念预测任务，对于更复杂的多标签分类或更细粒度的对话行为分析，其表现尚未完全验证。

## Processing Notes

- Duplicate papers skipped: 0