# Daily arXiv - 2026-07-29

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-29T23:29:04
- Paper count: 10

## 1. DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space

- Source: arxiv
- arXiv ID: 2607.25675
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.25675v1
- PDF: https://arxiv.org/pdf/2607.25675v1
- DOI: https://doi.org/10.48550/arXiv.2607.25675

### Authors

Jiangwang Chen, Zixin Song, Junlin Liu, Shuaiyu Zhou, Haiyan Wu, Haihan Shi, Chenxi Zhou, Hanqing Li, Xiao Yang, Da Zhu, Guanjun Jiang, Hai Wan, Xibin Zhao

### Abstract

Text-space optimization adapts large language models (LLMs) by editing external natural-language artifacts rather than model weights, so the optimized artifacts remain inspectable and the model can be treated as a black box. However, most existing text-space methods keep evaluation fixed. On open-ended tasks, this can become a bottleneck: once the solver improves on the criteria a rubric measures, omitted dimensions remain invisible to the optimization signal. Simply evolving the rubric is also unreliable when updates are selected by the current solver's score, because apparent progress can come from making the rubric easier to satisfy. We introduce DecoEvo (Decoupled Co-Evolution), which co-evolves a solver skill and a rubric-generator skill under decoupled objectives without using gold rubrics during optimization. The solver skill is updated using criterion-level feedback, while the rubric-generator skill is revised through complementary audits of requirement coverage and response discrimination that are independent of aggregate solver score. This separation focuses generator updates on newly exposed solver weaknesses, reducing repeated emphasis on criteria the solver already satisfies. Under each benchmark's official evaluation, DecoEvo outperforms all compared methods across five benchmarks and three LLM backbones, yielding 2.8--5.0\% relative gains over SkillOpt in the five-benchmark average.

### 中文一句话结论
DecoEvo 通过解耦求解器与评分生成器的协同进化，在不使用黄金评分标准的前提下，显著提升了文本空间优化在开放任务上的性能，并在五个基准测试和三个大语言模型上均取得最优结果。

### English TL;DR
DecoEvo introduces a score-decoupled co-evolution framework that simultaneously optimizes a solver skill and a rubric-generator skill in text space using separate objectives, enabling adaptive evaluation without rewarding rubric drift, and achieves state-of-the-art performance across five benchmarks and three LLM backbones.

### 中文详细总结
现有文本空间优化方法通常固定评估标准，在开放任务中容易成为瓶颈：当求解器在评分标准涵盖的维度上改进后，被遗漏的维度无法获得优化信号。单纯演化评分标准又可能因求解器分数的耦合导致评分标准向求解器偏移。DecoEvo 提出解耦协同进化：求解器技能通过准则级反馈更新，评分生成器技能则通过不依赖聚合求解器分数的结构审计和近邻对比审计进行更新，从而将生成器更新聚焦于求解器新暴露的弱点。该方法无需黄金评分标准，保持黑盒可检查性。在五个基准测试和三个大语言模型上，DecoEvo 在所有 15 个组合中均取得最高平均分，相比 SkillOpt 相对提升 2.8–5.0%。

### 方法 / 贡献
- 形式化了文本空间中求解器与评分生成器的协同进化问题，并提出了分离的更新目标，使评估信号能够自适应而不奖励有利于当前求解器的评分标准变化。
- 通过任务条件结构审计和评分盲近邻对比审计，将遗漏的要求和未区分的质量差异转化为可复用的评分生成原则，无需黄金评分监督或模型权重更新。
- 在五个基准测试、三个大语言模型以及两个域内跨基准迁移场景中，所有 15 个骨干-基准组合均取得最高平均分，相对 SkillOpt 提升 2.8–5.0%。

### 实验或数据
实验涵盖五个基准测试（未在摘要中具体命名）和三个大语言模型骨干，包括两个域内跨基准迁移设置。所有比较均采用基准官方评估。DecoEvo 在所有骨干-基准组合中均优于对比方法，五个基准平均相对 SkillOpt 提升 2.8–5.0%。优化过程中不使用黄金评分标准，仅用于最终评估。

### 值得关注点
- **分数解耦**：生成器更新独立于聚合求解器分数，避免评分标准向求解器偏移。
- **双重审计**：结构审计覆盖缺失要求，近邻对比审计暴露实际未能区分的质量差异。
- **黑盒兼容**：保持模型冻结，优化状态（技能文档）可检查。
- **无黄金评分依赖**：优化过程无需黄金评分标准，提升泛化性。
- **跨基准迁移**：两个域内跨基准实验进一步验证了方法的鲁棒性。

### 局限性
摘要和预览未明确讨论局限性。从方法看，DecoEvo 假设可获取任务特定的结构审计规范，并依赖冻结骨干，可能限制其在某些任务上的适用性；此外，审计阈值（如近邻对比的 τ_tie 和 H）需要调参，实际部署时可能需额外验证。更全面的局限性分析需参考全文。

## 2. Towards Robust Reinforcement Learning for Small-Scale Language Model Agents

- Source: arxiv
- arXiv ID: 2607.25091
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.25091v1
- PDF: https://arxiv.org/pdf/2607.25091v1
- DOI: https://doi.org/10.48550/arXiv.2607.25091

### Authors

Md Rezwanul Haque, Md. Milon Islam, Fakhri Karray

### Abstract

The alignment of Small Language Models (SLMs) in the 70--500M parameter range using reinforcement learning is often considered unstable, though the underlying failure mechanisms have not been systematically investigated. In the State-of-the-Art (SOTA) research, fifteen (model, corpus) configurations were trained using Proximal Policy Optimization (PPO). The experiments included Pythia-70M, 160M, 410M and SmolLM2-135M, 360M on the TinyStories, CNN/DailyMail, and Wikitext-103 corpora. Three reproducible failure modes were identified in small-scale language models: silent LoRA parameter freezing in standard PEFT/TRL pipelines, numerical overflow in importance ratios when using bfloat16, and catastrophic policy collapse due to reward-model error. These issues were addressed using a merge-and-reinitialize adapter technique, float32 precision during PPO updates, and a three-layer safety mechanism comprising reward whitening, importance-ratio guarding, and weight rollback. In this paper, a capacity-headroom hypothesis is proposed, which states that PPO performance at the SLM scale depends on both a fluent supervised model ($\text{PPL}<20$) and a discriminative reward signal, rather than on the number of model parameters. The proposed system converged stably in all experiments and improved preference win rate over the SFT baseline in configurations with a fluent prior and an informative reward signal. Furthermore, it outperformed instruction-tuned baselines while requiring significantly less training data. All checkpoints, preference datasets, and training scripts are publicly released$^§$.

### 中文一句话结论
本文发现小型语言模型（70–500M参数）在使用PPO进行RLHF训练时存在三种可复现的失败模式，并提出了一套稳定化框架和容量余量假说，实现了稳定的收敛和对齐效果，且所需训练数据更少。

### English TL;DR
This paper identifies three reproducible failure modes in PPO-based RLHF for small language models (70–500M parameters) and proposes a stabilization framework along with a capacity-headroom hypothesis linking SFT fluency and reward discriminability, achieving stable convergence and improved alignment with less training data.

### 中文详细总结
该研究系统性地调查了70–500M参数范围的小型语言模型（SLM）在使用强化学习（PPO）进行对齐时的不稳定性问题。研究在15种（模型，语料库）配置上进行了实验，包括Pythia-70M、160M、410M和SmolLM2-135M、360M，在TinyStories、CNN/DailyMail和Wikitext-103语料库上训练。发现了三种可复现的失败模式：标准PEFT/TRL管道中LoRA参数无声冻结、bfloat16精度下重要性比率数值溢出、以及奖励模型错误导致的灾难性策略崩溃。针对这些问题，作者提出了合并并重新初始化适配器技术、在PPO更新中使用float32精度、以及包含奖励白化、重要性比率保护和权重回滚的三层安全机制。论文提出了“容量余量假说”，认为SLM规模的PPO性能取决于流畅的SFT模型（困惑度<20）和具有判别力的奖励信号，而非模型参数数量。提出的系统在所有实验中稳定收敛，在具备流畅先验和信息性奖励信号的配置中，相比于SFT基线提高了偏好胜率，并且在使用更少训练数据的情况下超越了基于指令微调的基线。所有检查点、偏好数据集和训练脚本均已公开发布。

### 方法 / 贡献
1. 识别并分析了三种SLM规模下PPO的可复现失败模式：静默LoRA梯度冻结、bfloat16重要性比率溢出、奖励驱动策略崩溃。
2. 提出了对应的解决方案，并构造了三层控制论安全框架。
3. 提出了容量余量假说，证明了PPO在SLM规模的有效性取决于SFT流畅性和奖励可分辨性的组合，并给出了实践决策规则（PPL_SFT < 20）。
4. 开源了包含15个检查点、偏好数据集、训练脚本、交互验证应用和多轮智能体扩展系统的可复现对齐框架。

### 实验或数据
实验使用了5个基础模型（Pythia-70M、160M、410M和SmolLM2-135M、360M）在3个数据集（TinyStories、CNN/DailyMail、Wikitext-103）上进行，涵盖了15种完整配置。所有超参数在不同实验中保持一致。合成偏好对通过截断、打乱和错配三种退化策略生成。评估使用保留提示进行。

### 值得关注点
1. 发现了标准RLHF管道在小型模型上的无声失败模式，这些模式通常未被系统性地调查。
2. 容量余量假说（PPO性能依赖SFT流畅度和奖励可分辨性而非参数数量）为实践者提供了实用的决策指导。
3. 提出的框架在使用更少训练数据的情况下超越了指令微调基线（如SmolLM2-Instruct和Qwen2.5-Instruct）。
4. 所有资源公开可用，提升了可复现性。

### 局限性
论文仅在单轮交互场景下进行实证评估，多轮交互的框架虽已发布但尚未经过系统验证。实验中使用的偏好数据是合成的，而非来自真实人类反馈。此外，研究的模型规模限制在70–500M参数范围内，结果可能不完全适用于更大规模模型。

## 3. On the Use of LLMs for Specialised Terminology: A Good Alternative to Corpora?

- Source: arxiv
- arXiv ID: 2607.24784
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.24784v1
- PDF: https://arxiv.org/pdf/2607.24784v1
- DOI: https://doi.org/10.48550/arXiv.2607.24784

### Authors

Joachim Minder, Guillaume Wisniewski, Natalie Kübler

### Abstract

Specialised translation relies on the use of documentary and terminological resources, including corpora. These resources are particularly useful for terminology. However, their compilation and exploitation have several limitations: they require time, technical skills and access to data that can be difficult to collect. This study examines the extent to which LLMs can assist specialised translators in finding equivalents from English to French. We evaluate four proprietary models, GPT-4o, GPT-5.2, Claude Sonnet 4.5 and DeepSeek, in two specialised domains, Earth, Environmental and Planetary Sciences (EEPS) and Natural Language Processing (NLP). The experiment is based on 80 terms per domain and compares two prompting strategies: a terminology and a translation mode. The results highlight clear differences between models, prompting strategies and, to a lesser extent, domains. Claude Sonnet 4.5 achieves the best results in the most favourable configuration, while DeepSeek stands out for its greater stability. Analysis of confidence estimates also shows that they are only a partial indicator of terminological accuracy. Overall, the findings suggest that LLMs can be useful tools for specialised translators, but cannot, at this stage, replace specialised corpora. This research therefore paves the way for future work on the real practical usefulness of LLMs for specialised translators in work and educational contexts.

### 中文一句话结论
大型语言模型（LLMs）可作为专业翻译术语查询的辅助工具，但在当前阶段无法取代专门语料库。

### English TL;DR
Large language models can assist specialized translators in finding English-to-French terminology equivalents, with Claude Sonnet 4.5 performing best, but they cannot yet replace specialized corpora.

### 中文详细总结
本研究评估了四种商用大型语言模型（GPT-4o、GPT-5.2、Claude Sonnet 4.5 和 DeepSeek）在英译法专业术语查询中的表现。实验涵盖地球、环境与行星科学（EEPS）和自然语言处理（NLP）两个专业领域，每个领域选取80个术语。研究比较了两种提示策略："术语模式"（直接查询术语对应词）和"翻译模式"（先翻译上下文句子再提取术语对应词）。结果表明，Claude Sonnet 4.5在最佳配置下表现最优（NLP领域的术语模式下达到最高分），但跨领域和跨模式波动较大；DeepSeek表现稳定；GPT-4o整体最弱。模型的置信度估计仅能部分反映术语准确性。总体而言，LLMs能为专业翻译提供有用帮助，但尚不能替代专门语料库。

### 方法 / 贡献
- **方法**：选取160个专业术语（每领域80个），由一位专业译员评估四种LLM提供的法文译词准确性。评估时区分"主要对应词被正确识别为主要对应词"、"主要对应词被识别但归类为次要"和"主要对应词未被识别"三种情况，并赋予不同权重计算得分。
- **贡献**：首次系统比较多种LLMs在专业术语查询中的实际表现，特别针对传统语料库方法的替代可能性；揭示了不同提示策略和领域对LLM表现的影响；提出模型置信度估计仅部分预示术语准确性的发现。

### 实验或数据
- **数据**：160个专业术语（EEPS和NLP各80个），来源包括硕士生翻译的研究论文、ARTES术语库及其他专业文本。
- **实验**：4个模型 × 2个领域 × 2种提示模式（术语/翻译）+ 针对最优模型增加了"文献来源证明"变体，共16+1个独立实验。
- **验证**：使用研究实验室积累的平行/可比语料库、TERMIUM术语库和实验室自建术语库进行人工标注验证。

### 值得关注点
- Claude Sonnet 4.5在有利配置下表现最优（术语模式下NLP领域得分最高），但跨领域波动大
- DeepSeek表现出令人关注的稳定性，跨模式和领域变化最小
- 提示策略效果不一致：GPT模型受益于翻译模式，Claude在术语模式下更好，DeepSeek几乎不受影响
- 模型的置信度估计仅能部分反映术语准确性，不可完全信赖
- 研究直接面向翻译实践和教育场景，而非纯学术benchmark

### 局限性
- 仅涵盖英语→法语一个语言对，未涉及其他语言组合
- 只测试了四个商用闭源模型，未包括开源模型或其他架构
- 每个领域仅80个术语，样本量有限
- 评估由一位专业译员进行，存在主观性
- "文献来源证明"变体仅在最优模型上测试，未扩展至所有模型
- 未探讨LLM在更复杂的术语学任务（如定义撰写、概念关系识别）中的表现
- 未在真实翻译工作流程中测试LLM的实际效用和用户体验

## 4. Chart-Supported or Model-Supplied? Examining MLLM-Generated Claims for Accessible Visualization

- Source: arxiv
- arXiv ID: 2607.25021
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.25021v1
- PDF: https://arxiv.org/pdf/2607.25021v1
- DOI: https://doi.org/10.48550/arXiv.2607.25021

### Authors

Ishrat Jahan Eliza, Md Dilshadur Rahman

### Abstract

Multimodal large language models (MLLMs) can connect visualization patterns to external causes, consequences, and domain knowledge, but the evidential basis of these interpretations is often unclear. We present an exploratory study of 102 visualizations from four sources, three MLLMs, and four input conditions that vary access to the image, source-specific accessible chart context, and withheld-context framing. Across 1,224 descriptions, we analyze model-attributed DIRECT, DERIVED, and SPECULATIVE labels and conduct an automated audit of numeric agreement. Accessible chart context shifted Gemini and GPT toward DIRECT claims and improved numeric agreement for some models. Adding the image to the full context did not yield a consistent numeric benefit, and the withheld-context prompt did not reliably increase cautious language. The prompt-defined Real-World Significance section remained predominantly SPECULATIVE. These results motivate accessible description systems that distinguish claims supported by supplied evidence from model-supplied interpretation

### 中文一句话结论
本研究通过控制输入条件（是否提供图像、可访问图表上下文以及上下文缺失提示），发现提供可访问图表上下文能使MLLM生成的声明更倾向于“直接”（源自证据）类型，并提升部分模型的数值一致性，但添加图像并未带来持续益处，且明确告知上下文缺失的提示也未可靠增加谨慎性措辞。

### English TL;DR
This study investigates how input conditions—varying access to visualization images, accessible chart context, and withheld-context framing—affect whether MLLM-generated claims are model-attributed as Direct (evidence-supported), Derived (evidence-derived), or Speculative (model-supplied), finding that accessible chart context shifts claims toward Direct labels and improves numeric agreement for some models, while adding images yields no consistent benefit and withheld-context prompts do not reliably increase cautious language.

### 中文详细总结
本研究探索了多模态大语言模型（MLLMs）在为可视化生成描述时，其声明的事实依据如何受到输入条件的影响。作者从四个来源收集了102个可视化作品，使用三个MLLM（GPT、Gemini、Llama）和四种输入条件，生成了总计1224份描述。条件设计为：V1（图像+完整上下文）、V2（仅上下文无图像）、V3（仅图像）、V4（图像+明确告知上下文被隐藏的提示）。模型将每条声明自动标记为DIRECT（直接来自提供证据）、DERIVED（通过推断得出）或SPECULATIVE（模型自身知识推测）。实验发现，提供可访问图表上下文（如数据表、场景图、专家注释）会促使Gemini和GPT模型产出更多DIRECT声明，并提高GPT和Llama模型在数值数据上的准确性。然而，在已有完整上下文的情况下，额外添加图像并未带来一致的数值提升。即使提示明确说明上下文存在但被隐藏，模型也未显著增加谨慎性措辞或拒绝回答。另外，在“现实世界意义”部分，绝大多数（73.9%）声明仍被标记为SPECULATIVE。

### 方法 / 贡献
- **研究方法**：采用受控的探索性实验，将102个可视化作品与四个来源的上下文、三个MLLM及四种输入条件进行全交叉设计，共计1224条生成描述。
- **核心贡献**：
    1. 系统性地评估了不同输入证据（图像、上下文、缺失提示）对MLLM声明类型分布的影响。
    2. 提出了一种基于“DIRECT/DERIVED/SPECULATIVE”标签的声明来源分析方法。
    3. 揭示了上下文提示对提升模型基于证据生成描述的有效性，以及其局限性。
    4. 为设计可区分“证据支持”与“模型推断”的可访问描述系统提供了实证依据。

### 实验或数据
- **数据集**：构建了一个包含102个可视化作品的语料库，来自VisText（30个）、Our World in Data（42个）、HCI Alt Text Dataset（20个）和Olli Gallery（10个）。每个来源提供了不同的可访问上下文（如数据表、场景图、人工描述、屏幕阅读器树等）。
- **模型**：GPT-5.4、Gemini 3.5 Flash、Llama 4 Scout 17B Vision，温度参数设为0。
- **实验设计**：每个可视化作品在四个条件（V1至V4）下对三个模型分别生成描述，总计1224条。分析指标包括：声明标签分布、数值一致性审计（对DIRECT声明进行自动数值比对）、以及模型对证据可用性的自我评估（0-5分制）。

### 值得关注点
- **上下文的关键作用**：提供可访问图表上下文是促使模型生成更可靠（DIRECT）声明的关键因素，其效果甚至优于仅提供图像。
- **“知道缺失”与“实际行为”的鸿沟**：即使明确告知上下文被隐藏，模型也未显著调整其生成策略或增加谨慎性，表明当前MLLM在不确定性表达上仍有不足。
- **高比例的推测性内容**：在“现实世界意义”等需要外部知识的段落，绝大多数声明是模型推测的，这对依赖此类描述的弱视用户构成验证负担。
- **标签的局限性**：研究中使用的“DIRECT/DERIVED/SPECULATIVE”标签是模型自我归因的，并非经过验证的声明来源，需谨慎解读。

### 局限性
- **探索性性质**：本研究是探索性的，结果揭示了相关性而非因果性，且样本量有限（102个可视化，4个来源），结论的泛化性需要更多研究验证。
- **标签定义模糊**：模型对“DIRECT”和“DERIVED”标签的区分存在模糊地带（例如某些可计算内容被混用），导致标签作为声明来源的指示不完全可靠。
- **未涉及用户研究**：论文明确指出，本研究只表征模型行为，并未评估生成描述对盲人或低视力读者的实际有用性或可用性。
- **上下文来源差异**：不同可视化来源提供的上下文形式和数量不同，虽然采用了“同一可视化内比较”的设计，但跨来源的间接比较需谨慎。

## 5. Instruction-based Image Editing: A Survey on Data, Models, Evaluation, and Applications

- Source: arxiv
- arXiv ID: 2607.25642
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.25642v1
- PDF: https://arxiv.org/pdf/2607.25642v1
- DOI: https://doi.org/10.48550/arXiv.2607.25642

### Authors

Xianghao Zang, Zijian Jiang, Jiarong Cheng, Qianrui Teng, Ying He, Yuxuan Mu, Chao Ban, Huayu Zhang, Lanxiang Zhou, Zerun Feng, Chi Zhang

### Abstract

Instruction-based Image Editing (IIE) aims to transform a given image into a new one based on textual instructions. Advances in Large Language Models (LLMs) and Vision-Language Models (VLMs) have accelerated progress toward practical ``one-sentence image editing" systems. This survey presents a systematic taxonomy and comprehensive review of IIE research, structured around five core dimensions: (1) task definition and hierarchical categorization of editing operations, (2) methodologies for training data construction, (3) architectural evolution from GAN-based to diffusion and autoregressive paradigms, (4) standardized evaluation metrics and benchmark development, and (5) introduction of commercial solutions. Our analysis shows critical technological milestones across model generations. We further propose a Comprehensive, in-Depth, and Diagnostic benchmark for IIE task (CDD-IIE Bench), which can rigorously assess the multiple aspects of model performance. Through empirical comparisons of open-source solutions, we highlight their respective capabilities and limitations. Finally, we discuss future research directions to advance the field.

### 中文一句话结论
本文系统综述了基于指令的图像编辑领域，提出了统一的任务分类体系、数据构建方法、模型架构演变、评估指标及一个综合诊断基准（CDD-IIE Bench），并比较了开源方案。

### English TL;DR
This survey provides a comprehensive review of instruction-based image editing, covering task taxonomy, data construction, model architectures (GANs, diffusion, autoregressive), evaluation metrics, and commercial solutions. It introduces the CDD-IIE Bench benchmark for rigorous assessment and empirically compares open-source models, highlighting their capabilities and limitations.

### 中文详细总结
本文从五个核心维度系统综述了基于指令的图像编辑（IIE）研究：任务定义与层次化分类、训练数据构建方法、模型架构从GAN到扩散和自回归模型的演变、标准化评估指标与基准开发、以及商业解决方案介绍。文章提出了一个层次化的编辑任务分类体系，包括基本原子编辑（对象级、图像级、实用任务）和高级组合编辑（复杂指令与推理、空间理解与推理）。模型部分回顾了GAN、扩散模型、自回归模型及其损失函数。评估方面，作者提出了CDD-IIE Bench基准，包含5大类别21个细粒度子标准，并对开源模型进行了实证比较。最后讨论了未来研究方向。

### 方法 / 贡献
- 建立了IIE任务的系统分类体系，明确定义了基本原子编辑和高级组合编辑任务。
- 全面综述了训练数据构建方法论、模型架构演化趋势（从GAN到扩散和自回归模型）以及评估框架。
- 提出了层次化评估指标系统（5大类别21个子标准）及CDD-IIE Bench基准，用于深入诊断模型性能。
- 比较了开源和商业解决方案，并指出了各自的优缺点。

### 实验或数据
论文提出了CDD-IIE Bench基准，用于全面评估模型性能。通过实证比较多个开源解决方案，展示了它们在不同任务上的能力与局限。具体数据集未在摘要中详述，但基准测试涵盖多种编辑任务，并使用了标准评估指标（如LPIPS、CLIP相似度等）。

### 值得关注点
- 任务分类的层次化设计（基本原子编辑vs.高级组合编辑）填补了行业缺乏统一定义的空白。
- 模型架构的全面回顾，涵盖了从GAN到扩散再到自回归及统一模型的发展脉络。
- CDD-IIE Bench提供了多维度、诊断性的评估，有助于深入理解模型优劣。
- 同时覆盖了开源与商业解决方案，具备实际应用视角。

### 局限性
- 综述主要基于现有文献，可能未涵盖所有最新模型（如部分近期提出的统一架构）。
- CDD-IIE Bench的评估任务和指标可能无法覆盖所有实际应用场景，有待进一步扩展。
- 对商业产品的分析可能受限于公开信息，深度有限。

## 6. Evaluating Communicative Belief Updates in Large Language Models via Implicature Recognition and Cancellation

- Source: arxiv
- arXiv ID: 2607.25094
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.25094v1
- PDF: https://arxiv.org/pdf/2607.25094v1
- DOI: https://doi.org/10.48550/arXiv.2607.25094

### Authors

Cesare Spinoso-Di Piano, Verna Dankers, Marius Mosbach, Jackie Chi Kit Cheung

### Abstract

Human language is driven by unspoken beliefs and belief updates, making these critical to model for successful communication between large language models (LLMs) and their users. In this paper, we evaluate the ability of LLMs to recognize unspoken beliefs made through implicatures and to understand their updates through implicature cancellation: the pragmatic phenomenon whereby an utterance's implied meaning is weakened or negated. We create the first expert-annotated implicature cancellation dataset, [DatasetName], crowdsourced for human judgements of implicatures and their corresponding cancellations. We find that LLM belief update understanding lags behind that of humans, especially in more naturally-occurring scenarios. Additional control experiments suggest that successes in LLM belief updates may stem in part from a reliance on prior beliefs, and that failures in belief updates may depend on their type and on their form. Overall, our study suggests that current LLMs have not yet reached human-level understanding of unspoken beliefs and belief updates. Code and data are available at https://github.com/cesare-spinoso/ImplicatureX.

### 中文一句话结论
当前的大语言模型在通过隐含意义识别与取消来理解未言明信念及信念更新方面，尤其在自然场景中，仍显著落后于人类水平。

### English TL;DR
LLMs fail to match human-level understanding of unspoken beliefs and belief updates via implicature recognition and cancellation, especially in natural scenarios.

### 中文详细总结
本文评估了大语言模型（LLMs）通过隐含意义（implicature）识别及其取消（implicature cancellation）来理解未言明信念与信念更新的能力。隐含意义取消是一种语用现象，指话语的隐含含义被弱化或否定。作者构建了首个专家标注的隐含意义取消数据集（ImplicatureX），包含271个条目，覆盖合成对话、自然标量隐含、话语隐含及多轮对话隐含，并进行了众包人类判断。实验发现，LLMs在信念更新理解上落后于人类，尤其在更自然的场景中。控制实验表明，LLMs的部分成功可能源于对先验信念的依赖，而失败则与信念更新的类型和形式相关。总体而言，当前LLMs在未言明信念与信念更新的理解上尚未达到人类水平。

### 方法 / 贡献
- 创建首个专家标注的隐含意义取消数据集（ImplicatureX），包含271个条目，覆盖多种隐含类型（标量、话语、对话隐含）。
- 通过众包收集人类对隐含意义识别与取消的判断，作为基准。
- 设计评估LLMs的框架，操作化隐含意义识别与取消，测量模型对信念更新的理解。
- 进行控制实验：剥离上下文或话语，测试LLMs是否仅依赖先验信念取得成功；区分更新类型（取消、不变、强化）与形式（显式/隐式）。

### 实验或数据
- 数据集：ImplicatureX，由语言专家标注，涵盖合成两轮对话、自然标量隐含、话语隐含及多轮对话隐含。
- 人类基准：通过众包收集隐含意义识别与取消的正确率。
- 模型评估：测试了多个LLMs（如GPT-5.4 Thinking、Qwen 3 32B Thinking等），对比人类表现。
- 控制实验：在无上下文、无话语或两者皆无的条件下测试模型；分别测试取消、不变、强化三种更新类型，以及显式与隐式触发方式。
- 主要发现：最强LLMs在标量/话语隐含识别上接近人类，但在自然对话隐含中表现差于随机；信念更新理解全面落后于人类，即使面对显式否定，强模型也无法匹配人类准确率。

### 值得关注点
- 首个系统研究隐含意义取消这一语用现象在LLMs中的表现，填补了沟通信念更新评估的空白。
- 揭示了LLMs在自然场景下理解未言明信念的重大缺陷，强调整合语用推理能力的需求。
- 控制实验暴露了模型可能依赖先验信念而非真正进行语用推理，对当前评估方法提出质疑。
- 提供了公开的数据集和代码，便于后续研究与基准测试。

### 局限性
- 数据集规模有限（271个条目），可能无法覆盖所有隐含现象。
- 未测试多语言或跨文化场景，隐含意义理解可能受语言和文化影响。
- 仅评估了基于文本的交互，未涉及多模态或语音沟通中的隐含。
- 未深入分析模型内部机制，仅依赖输入输出行为推断。

## 7. Memory for Large Language Models

- Source: arxiv
- arXiv ID: 2607.25380
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.25380v1
- PDF: https://arxiv.org/pdf/2607.25380v1
- DOI: https://doi.org/10.48550/arXiv.2607.25380

### Authors

Sining Zhoubian, Dan Zhang, Evgeny Kharlamov, Jie Tang

### Abstract

Memory has evolved into a foundational architectural dimension in large language models (LLMs), shifting from an implicit byproduct of computation to a spectrum of explicit, controllable mechanisms. While recent advances introduce diverse strategies---spanning transient attention, recurrent state dynamics, parameter-efficient adaptations, and scalable lookup storage---this rapid evolution has led to a highly fragmented research landscape. In this survey, we present a systematic, architecture-centric taxonomy of memory in LLMs. Our framework characterizes memory along three orthogonal axes: representation (implicit versus explicit), update dynamics (offline versus online), and persistence (short-term versus long-term). We further formalize the granular mechanisms dictating memory writing, routing, state transitions, and consolidation. This unified perspective elucidates the conceptual boundaries between computation-coupled and independently addressable memory, effectively bridging disparate architectural paradigms. Additionally, we critically analyze hybrid memory architectures, system-level efficiency trade-offs, and multi-dimensional evaluation methodologies. By consolidating these scattered advancements into a cohesive framework, this survey charts the trajectory of memory-centric LLM design and provides a principled foundation for future innovations in scalable and adaptive language modeling.

### 中文一句话结论
本文提出了一种统一的、以架构为中心的大语言模型记忆分类体系，沿着表征、更新动态和持久性三个正交轴对现有记忆机制进行系统梳理，为未来可扩展和自适应语言建模提供了理论基础。

### English TL;DR
This survey introduces a unified, architecture-centric taxonomy for memory in large language models, categorizing mechanisms along representation (implicit vs. explicit), update dynamics (offline vs. online), and persistence (short-term vs. long-term) axes.

### 中文详细总结
本综述聚焦大语言模型（LLM）中的记忆机制，将其从隐式的计算副产物重新定义为一种显式、可控的架构维度。文章指出，随着注意力机制、循环状态、参数高效适配和可扩展查找存储等多样化策略的快速发展，该领域呈现高度碎片化状态。为此，作者提出一个三维分类框架：表征轴区分隐式记忆（如KV缓存、循环状态）与显式记忆（如外部表格、专用模块）；更新动态轴区分离线（仅训练时更新）与在线（推理时更新）记忆，并细化写入规则（优化驱动、状态转移、信号门控等）；持久性轴区分短期（高保真、局部窗口）与长期（高压缩、跨会话）记忆。该框架统一了计算耦合型与独立可寻址型记忆，并对混合架构、系统效率权衡和多维评估方法进行了批判性分析，为记忆驱动的LLM设计指明了研究方向。

### 方法 / 贡献
1. 提出了统一的大语言模型记忆分类体系，明确了隐式、显式、持久和自适应记忆机制的术语定义。
2. 系统综述了计算驱动和参数化记忆系统的最新进展，涵盖混合架构、多时间尺度更新策略和条件参数路由。
3. 批判性分析了系统级效率权衡和多维评估方法论，指出了持续存在的挑战和未来研究轨迹。

### 实验或数据
该论文是综述性研究，未提出新的实验或使用特定数据集。

### 值得关注点
- 论文将记忆机制沿着表征、更新动态和持久性三个正交轴解耦，为弥合不同架构范式提供了统一视角。
- 强调了记忆从隐式到显式的架构转变趋势，以及在线更新、信号门控写入等细粒度机制的兴起。
- 对混合记忆架构（如结合循环与注意力）和系统效率（如存储与计算开销）的讨论具有实际参考价值。
- 指出了评估方法的多维性（如记忆容量、精度、效率等），为未来基准测试提供方向。

### 局限性
- 该综述主要关注模型层面的记忆机制，未深入覆盖智能体层面或基于提示的外部记忆系统。
- 分类框架虽具通用性，但某些机制（如参数高效的微调）的边界可能模糊，存在归类争议。
- 由于领域进展迅速，部分最新方法（如2025–2026年的成果）可能无法完全涵盖或深入分析。

## 8. TimeCapsule: Generative Hallucination as a Method for Historical Sensemaking

- Source: arxiv
- arXiv ID: 2607.24750
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.24750v1
- PDF: https://arxiv.org/pdf/2607.24750v1
- DOI: https://doi.org/10.48550/arXiv.2607.24750

### Authors

Hayk Grigorian, Hamed Yaghoobian

### Abstract

Large Language Models (LLMs) are temporally overexposed: trained on vast contemporary corpora, they encode present-day concepts that make them unreliable narrators of the past. We present TimeCapsule, a 1.2B-parameter LLaMA-style causal model trained exclusively on Victorian texts (1800-1875) as an epistemologically isolated generative archive. Quantitative evaluation shows a 45.4% perplexity reduction over a GPT-2 baseline on held-out Victorian prose, while larger contemporary causal models achieve lower raw perplexity through broader pretraining but lack temporal isolation. TimeCapsule exhibits computational sensemaking, generating historically plausible analogical explanations for unfamiliar modern concepts (e.g., describing a computer as a "hypertrophied lung"). A qualitative hermeneutic probe with two humanities scholars revealed a crisis of authenticity, as both misclassified approximately 40% of genuine Victorian excerpts as machine-produced. We argue that structural ignorance of the future transforms hallucinations into interpretive probes of nineteenth-century ontologies.

### 中文一句话结论
本文提出TimeCapsule，一个仅训练于维多利亚时期文本（1800-1875）的12亿参数因果语言模型，证明了通过对未来的结构性无知，模型的“幻觉”可以转化为理解19世纪本体论的阐释工具。

### English TL;DR
TimeCapsule introduces a 1.2B-parameter causal LLM trained exclusively on Victorian texts (1800–1875), enforcing an "epistemological event horizon." By being structurally ignorant of the future, its generative hallucinations become interpretable probes of 19th-century ontologies rather than anachronistic errors.

### 中文详细总结
TimeCapsule的核心创新在于“选择性时间训练”（selective temporal training, STT）：模型仅使用1800-1875年的文学文本、议会记录和期刊训练，形成一个知识论上的“事件视界”——任何1875年之后的知识都无法进入模型。面对现代概念（如“电脑”）时，模型被迫只能使用维多利亚时期的语义资源进行“本体论修复”，例如将电脑描述为“过度肥大的肺”。

理论框架上，论文将模型视为一种“生成式档案”，强调时间约束的创造性价值。作者指出，现代大模型因训练于当代语料而本质上是“时代暴露”的，只能进行“历史cosplay”。TimeCapsule通过强制无知（而非假装无知）来确保历史真实性。

论文还从四个维度构建理论：档案理论（记忆的有限性）、媒介物质性（潜在空间作为历史痕迹）、慢技术设计（时间作为设计材料）和去殖民化批判（保留而非修正历史偏见）。

### 方法 / 贡献
1. **选择性时间训练 (STT)**：定义了一种在时间受限语料上训练小规模模型的方法论。
2. **历时语义分析**：使用向量投影量化“时间工业化”，发现“TIME”与“FACTORY”的语义关联在维多利亚潜在空间中是现代空间的2.1倍。
3. **幻觉作为本体论修复**：重新定义“幻觉”为历史逻辑的窗口，而非错误。
4. **档案诚实**：通过t-SNE偏执地形分析，保留并暴露模型中的帝国与性别偏见，作为可观测的历史记录，而非修正它。

### 实验或数据
- 模型：1.2B参数的LLaMA风格因果模型，训练于1800-1875年的维多利亚文本。
- 定量评估：在保留的维多利亚散文上，困惑度比GPT-2基线降低45.4%（达到37.59）。
- 定性评估：两位人文学者进行诠释学探针，将约40%的真实维多利亚文本误判为机器生成，揭示了“真实性危机”。
- 对比：更大规模现代模型虽原始困惑度更低，但缺乏时间隔离性。

### 值得关注点
- 核心洞察：对未来的无知不是缺陷，而是使历史意义建构成为可能的设计条件。
- 将“幻觉”从AI错误重新定义为历史阐释工具，方法独特。
- 明确拒绝RLHF对齐，主张保留历史偏见是研究帝国史和种族史的必要条件。
- 借鉴慢技术、媒介考古学和去殖民化理论，跨学科视角丰富。

### 局限性
- 模型仅12亿参数，规模远小于当代前沿模型，其生成质量受限于计算资源。
- 仅覆盖1800-1875年英帝国/维多利亚时期，历史范围和地理文化范围有限。
- 定量评估仅使用困惑度指标，缺乏更丰富的自动评估方法。
- 定性评估仅邀请两位学者，样本量小，结果可能不具备广泛代表性。
- 论文未系统讨论模型在超出训练语料分布时的鲁棒性和边界行为。

## 9. PreDiff-LM: Pretrained Discrete Masked Diffusion Language Modeling with Hybrid Attention

- Source: arxiv
- arXiv ID: 2607.25157
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.25157v1
- PDF: https://arxiv.org/pdf/2607.25157v1
- DOI: https://doi.org/10.48550/arXiv.2607.25157

### Authors

Zhengtao Yao, Runhao Li, Xupeng Chen, Jiayi Cheng, Chenqian Le, Michael Yue, Jesson Wang, Siheng Wang, Guang Yang, Haoyan Xu, Chenhao Wei, Zhengqing Yuan, Youran Shen, Yanfang Ye, Junhao Dong

### Abstract

Discrete masked diffusion language models support bidirectional generation and infilling, but adapting pretrained autoregressive (AR) transformers requires reconciling causal pretraining with bidirectional denoising. We study this problem at the level of attention rather than claiming AR-weight reuse itself as novel. PreDiff-LM preserves causal attention within the observed prompt while allowing full bidirectional attention within the masked target. Under a matched GPT-2 Medium, WikiText-103, 90K-step setup, this hybrid mask improves unconditional perplexity from 34.1 to 28.7 and MAUVE from 0.71 to 0.78 over uniform bidirectional attention with the same AR initialization. Attention adaptation also composes with a DiffuGPT-style objective adaptation, reaching 26.9 perplexity. Pretrained initialization reduces the steps required to reach perplexity below 50 from about 350K to 8K, although a compute-matched fine-tuned AR model remains stronger at equal scale (18.9 versus 28.7). Beyond perplexity, PreDiff-LM improves repetition, distributional quality, four zero-shot downstream tasks, and human preference over prior diffusion baselines. The results position hybrid attention as a complementary mechanism for adapting pretrained causal backbones, while making explicit the remaining quality and inference-efficiency gaps to optimized AR models.

### 中文一句话结论
PreDiff-LM通过混合因果-双向注意力掩码，在保留预训练自回归提示词因果计算的同时实现双向目标去噪，在困惑度、生成质量和零样本任务上优于统一双向注意力基线。

### English TL;DR
PreDiff-LM introduces a hybrid causal-bidirectional attention mask that preserves pretrained autoregressive computation in the prompt while enabling bidirectional target denoising, achieving improved perplexity, generation quality, and zero-shot task performance over uniform attention baselines.

### 中文详细总结
离散掩码扩散语言模型支持双向生成和填充，但将预训练自回归（AR）Transformer适配到双向去噪时，需要调和因果预训练与双向注意力的冲突。PreDiff-LM在注意力层面解决该问题，不声称AR权重复用本身为新颖点。其核心是混合注意力掩码：在观察到的提示词内保留因果注意力，在掩码目标内允许完全双向注意力。在GPT-2 Medium、WikiText-103、90K步的匹配设置下，该混合掩码将无条件困惑度从34.1降至28.7，MAUVE从0.71提升至0.78（相比统一双向注意力）。注意力适配与DiffuGPT风格的目标适配结合，困惑度进一步降至26.9。预训练初始化使达到困惑度低于50所需的步数从约350K降至8K。然而，在相同规模下，计算匹配的微调AR模型仍更强（18.9 vs 28.7）。除困惑度外，PreDiff-LM在重复性、分布式质量、四个零样本下游任务和人类偏好上均优于先前的扩散基线。

### 方法 / 贡献
- 方法：将注意力适配作为AR到扩散迁移的独立组件，提出混合因果-双向注意力掩码，保留提示词侧因果结构，同时使目标侧能进行双向去噪。
- 贡献：1）明确注意力适配问题并引入混合掩码；2）通过控制实验（统一双向注意力对照）隔离该机制，并展示其与目标适配的组合效果；3）添加计算匹配的微调AR对照、重复敏感指标、下游任务和人类偏好评估；4）区分训练效率与推理延迟，指出扩散在低步并行细化、填充和约束生成中仍有用。

### 实验或数据
实验基于GPT-2 Medium（1.24亿参数）在WikiText-103数据集上进行，训练步数为90K。评估指标包括：无条件困惑度、MAUVE、重复性、Distinct-n、Self-BLEU、四个零样本下游任务（具体任务未在摘要中列出）以及三人盲审人类偏好。论文还报告了训练效率比较（达到困惑度<50的步数）和推理延迟分析。

### 值得关注点
- 混合注意力机制作为适配预训练因果骨干的互补方法，在训练效率上提升显著（8K步 vs 350K步）。
- 注意力适配与目标适配可组合，进一步改善困惑度。
- 在生成质量和零样本任务上超越先前扩散基线，但明确承认与优化AR模型的质量和推理效率差距。

### 局限性
- 计算匹配的微调AR模型在相同规模下仍更强（18.9 vs 28.7困惑度），表明质量差距依然存在。
- 推理效率方面，优化AR解码在某些机制下更快，而扩散在低步并行细化、填充和约束生成中更有用。
- 混合掩码是针对重用因果权重的迁移假设，对于从头训练的模型是否同样有效尚不明确。

## 10. Construction-Driven Injection: Linguistically-Grounded Edit-Based Code-Mixing Fingerprints for Large Language Models

- Source: arxiv
- arXiv ID: 2607.25633
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.25633v1
- PDF: https://arxiv.org/pdf/2607.25633v1
- DOI: https://doi.org/10.48550/arXiv.2607.25633

### Authors

Yongyi Cui, Yue Li, Tianbao Jiang, Xin Yi

### Abstract

Large language models (LLMs) are costly intellectual assets that remain exposed to unauthorized redistribution and commercial misuse. Injected fingerprints, i.e., trigger--target pairs embedded in model behavior, offer a practical, black-box-verifiable ownership signal, but existing methods decouple the two stages of the fingerprint life cycle: how a fingerprint is constructed and how it is injected. Existing fingerprinting frameworks suffer from two limitations. Natural-language fingerprints are prone to accidental activation, and garbled fingerprints are easily filtered by perplexity-based detection. Furthermore, decoupling construction from injection leaves the latter unaware of the trigger's linguistic structure, missing the opportunity for targeted optimization. We argue that fingerprint construction should drive injection, and present a unified fingerprinting framework that jointly optimizes both stages. First, LCF constructs code-mixing fingerprints by combining low-resource languages under a semantic-density substitution rule and grammar-biased mixing, yielding triggers whose perplexity sits far below garbled baselines while avoiding the accidental-activation failures of natural-language triggers. Second, LCFEdit injects each fingerprint with a null-space projection derived from high-resource multilingual representations that preserves knowledge, augmented by a cross-lingual alignment step that steers the weight update toward the fingerprint language's representation subspace. This construction-aware injection ensures that the update is linguistically informed and therefore more stable. Extensive evaluations on imperceptibility, detectability, and harmlessness demonstrate persistent ownership verification with negligible impact on utility.

### 中文一句话结论
本文提出一种将指纹构建与注入联合优化的框架（LCF-LCFEdit），通过低资源语言的混合代码切换指纹和跨语言对齐的知识编辑，在不影响模型实用性的前提下实现鲁棒的所有权验证。

### English TL;DR
This paper proposes a unified framework (LCF-LCFEdit) that jointly optimizes fingerprint construction and injection using linguistically-grounded code-mixing from low-resource languages and cross-lingual alignment in null-space editing, achieving robust ownership verification with negligible impact on model utility.

### 中文详细总结
本文针对大语言模型（LLM）指纹保护中构建与注入两个阶段解耦的问题，提出统一框架LCF-LCFEdit。首先，LCF利用低资源语言的语义密度替换和语法偏置混合，构建代码切换指纹，降低触发器的困惑度，避免自然语言指纹的意外激活和乱码指纹的统计过滤。其次，LCFEdit在保留主流知识的前提下，采用空空间投影注入指纹，并通过跨语言对齐步骤将更新聚焦于指纹语言子空间，使注入过程受构建阶段的语言结构引导。实验在多个低资源语言上验证了该框架在不可察觉性、可检测性和无害性上的优势，均优于现有方法。

### 方法 / 贡献
- 提出LCF：基于语义密度替换规则和语法偏置混合，从低资源语言构建代码切换指纹，平衡用户侧和模型侧的不可察觉性。
- 提出LCFEdit：结合主流知识保留的空空间编辑和跨语言对齐步骤，使指纹注入方向集中于指纹语言子空间，增强稳定性。
- 构建与注入的联合优化：指纹的语言结构（如语言身份）直接驱动注入阶段的编辑集中方向，打破传统两阶段解耦。

### 实验或数据
- 使用12种低资源语言（如bn、fa、hi等），每语言11个指纹，共132对触发-目标对。
- 评估指标：不可察觉性（困惑度）、可检测性（模型修改后的成功率）、无害性（模型性能影响）。
- 结果：LCF平均困惑度96（CF为104，乱码指纹为1302），12种语言零意外激活；注入成功率93-99.5%。
- 对比基方法：IF-SFT、NLF-FPEdit、CF-MCEdit（见论文表1）。

### 值得关注点
- “数字岛假说”：低资源语言参数受主流微调梯度影响小，指纹更易保持。
- 跨语言对齐步骤通过后验凸组合（公式\( \Delta' = (1-\alpha)\Delta + \alpha(\Delta P_{\text{isl}}) \)）而非空空间约束实现更新聚焦。
- 实验表明框架对微调、量化和剪枝等模型修改具有鲁棒性。

### 局限性
- 数字岛假说仅为工作假设，未直接验证梯度层面的内积关系（公式 (3)）。
- 跨语言对齐的权重 \(\alpha\) 需手动调整（0.25/0.15），且依赖所选语言。
- 未提及具体数据集或模型大小（如仅提到3B模型），实验规模不详。
- 方法基于知识编辑，对大模型可能仍有计算开销。

## Processing Notes

- Duplicate papers skipped: 0