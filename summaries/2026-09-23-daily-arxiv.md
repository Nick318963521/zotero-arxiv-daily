# Daily arXiv - 2026-09-23

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-23T01:21:25
- Paper count: 10

## 1. Assessing Readability with LLMs: The Role of Reasoning and Few-Shot Prompting

- Source: arxiv
- arXiv ID: 2609.24650
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.24650v1
- PDF: https://arxiv.org/pdf/2609.24650v1
- DOI: https://doi.org/10.48550/arXiv.2609.24650

### Authors

Raphaël Thieffry, Matej Martinc

### Abstract

Readability assessment is essential for tailoring texts to intended audiences across educational, healthcare, and information retrieval domains. However, traditional readability formulas struggle to generalize across genres and languages, while supervised machine learning models rely on scarce, domain-specific annotated corpora, limiting their applicability--particularly for less-resourced languages. Large Language Models (LLMs) offer a highly scalable, multilingual alternative that requires no task-specific training, yet the impact of advanced prompting strategies on their performance remains underexplored. In this paper, we conduct a systematic benchmark of diverse open-source LLMs for multilingual readability assessment, focusing on the prediction of discrete readability levels required by educational frameworks. In addition to English, we evaluate our approach on a less-resourced language, Slovenian, to establish whether LLMs remain effective in low-resource settings. Specifically, we investigate the influence of explicit reasoning, demonstrating that Chain-of-Thought (CoT) prompting and reasoning-oriented models yield significant improvements over direct answering. Furthermore, our exploration of few-shot in-context learning reveals that providing just one labelled example per category (1-shot) substantially enhances prediction quality compared to zero-shot settings, with additional examples offering diminishing returns. By comprehensively comparing these approaches against traditional unsupervised metrics and state-of-the-art supervised baselines, we establish the viability of out-of-the-box LLMs as robust, cross-lingual readability assessors.

### 中文一句话结论  
本文系统评估了开源大语言模型（LLM）在多语言可读性评估中的表现，发现思维链推理和每类仅一个标注示例（1-shot）能显著提升离散可读性级别的预测质量，使开箱即用的LLM在英语和低资源语言斯洛文尼亚语上都能媲美监督模型。  

### English TL;DR  
This paper benchmarks open-source LLMs for multilingual readability assessment and shows that Chain-of-Thought reasoning plus 1-shot in-context examples substantially improves prediction of discrete readability levels, making out-of-the-box LLMs competitive with supervised models in both English and Slovene.  

### 中文详细总结  
- 可读性评估对教育、医疗、信息检索等领域很重要，但传统公式跨语言/跨体裁泛化差，监督模型又依赖稀缺的领域标注数据，低资源语言（如斯洛文尼亚语）尤其受限。  
- 论文测试了多个开源指令微调LLM，评估“直接回答”对比“思维链推理”、零样本对比少样本（1-shot、2-shot、3-shot）等提示策略。  
- 核心发现：显式推理（CoT或推理型模型）显著优于直接回答；每类仅给1个标注示例就能大幅提升效果，继续增加示例收益很小。  
- 研究将可读性视为离散级别分类任务，便于与监督基线直接比较，并使用二次加权Kappa、F1等指标。  
- 作者还强调这是首批研究LLM预测“离散可读性级别”的工作，也首次将LLM用于南斯拉夫语支语言（斯洛文尼亚语）的可读性评估。  

### 方法 / 贡献  
- 提出系统性的LLM可读性评估框架，固定标签定义与评分量表，变化提示格式、示例数量和推理机制。  
- 对比直接输出、显式推理（CoT）和原生推理三种输出机制，并使用结构化解码约束生成标签。  
- 在五个规模9B–32B的开源指令微调模型上评估，覆盖英语和斯洛文尼亚语。  
- 贡献包括：  
  - 首次系统研究推理对LLM可读性评估的影响；  
  - 首次探索少样本上下文学习在该任务中的作用，发现1-shot收益最显著；  
  - 与无监督公式和SOTA监督基线进行全面对比，证明开箱即用LLM的可行性和跨语言鲁棒性。  

### 实验或数据  
- 实验基于四个可读性语料库：三个英语语料库（包括Newsela、OneStopEnglish；第四个英语语料库名称在预览中截断）以及一个斯洛文尼亚语语料库。  
- 评估了多个提示变体（XML格式和散文格式、是否包含类定义与量表）以及k=0、1、2、3的少样本设置。  
- 摘要和预览中未报告具体数值结果，只报告了相对结论：CoT和1-shot显著优于直接回答和零样本，额外示例收益递减。  
- 作者提到`gpt-oss`的直接回答机制与其他模型不可比，因此未报告该设置下的结果。  

### 值得关注点  
- 显式推理（CoT）是提升LLM可读性判断的关键因素，而非仅仅依赖模型规模。  
- 仅需每类一个标注示例即可大幅改进预测，这对低资源语言尤其实用。  
- 证明了开源LLM在英语和斯洛文尼亚语上都能接近甚至有竞争力地匹敌监督模型，无需任务专用训练。  
- 研究首次针对“离散可读性级别”这一教育框架常用设定进行LLM评估，并首次覆盖斯洛文尼亚语。  

### 局限性  
- 摘要未明确列出局限性；从方法部分可看出，`gpt-oss`的direct设置因不可比而未报告，可能限制模型对比完整性。  
- 部分评估模型以英语为中心，多语言能力差异可能影响非英语结果。  
- 研究仅使用`vanilla score`（最高概率token）作为输出，未采用期望值方法，可能影响与某些工作的可比性。  
- 少样本示例池固定，未探索示例选择策略对结果的影响。

## 2. LIMIT: Less Is More for Instruction Tuning in Text-to-SQL

- Source: arxiv
- arXiv ID: 2609.24186
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.24186v1
- PDF: https://arxiv.org/pdf/2609.24186v1
- DOI: https://doi.org/10.48550/arXiv.2609.24186

### Authors

Haoyuan Ma, Hengwei Liu, Linjuan Wu, Yongliang Shen, Weiming Lu

### Abstract

Large language models have achieved remarkable progress on Text-to-SQL through reasoning-enhanced fine-tuning, yet existing approaches predominantly rely on massive instruction corpora under the assumption that scale drives performance. We challenge this paradigm by investigating a fundamental question: what is the minimal data requirement for effective Text-to-SQL instruction tuning? We propose LIMIT(Less Is More for Instruction Tuning in Text-to-SQL), a data-centric framework that demonstrates strong database reasoning can emerge from an extremely compact training set when examples are strategically selected. LIMIT operates through four stages: difficulty-aware filtering that identifies samples within the model's learning frontier, chain-of-thought synthesis with consistency-based selection, multi-dimensional quality scoring via LLM-as-judge, and genetic algorithm optimization that jointly maximizes schema coverage and sample quality. On the BIRD and Spider benchmark, LIMIT selects only 796 and 863 samples while achieving 100% table coverage, enabling Qwen3-8B to reach 69.1% and 88.9% execution accuracy.This result surpasses methods trained on 20 times more data and establishes a new state-of-the-art among open-source approaches. Our findings suggest that careful data curation, rather than scale, is the key to efficient Text-to-SQL learning.

### 中文一句话结论  
LIMIT 证明在 Text-to-SQL 任务中，通过精心挑选约 800 个高质量样本即可达到甚至超越使用超大规模数据的方法，数据质量比数据规模更重要。

### English TL;DR  
LIMIT is a data-centric framework showing that careful selection of only ~800 high-quality training examples can achieve state-of-the-art Text-to-SQL performance, challenging the assumption that massive data is necessary for effective instruction tuning.

### 中文详细总结  
论文提出 LIMIT（Less Is More for Instruction Tuning in Text-to-SQL），挑战当前 Text-to-SQL 领域依赖大规模指令数据的范式。框架通过四个阶段精选极小但高质量的训练集：1）难度感知过滤，去除太简单或太难样本；2）链式推理生成，用 DeepSeek-R1 产生并筛选最简洁正确的推理链；3）多维质量评分，用 GPT-4o 从问题–SQL 一致性、输入清晰度、SQL 质量、推理质量四维度打分；4）遗传算法优化，联合最大化数据库结构覆盖度与样本质量，在固定预算下搜索最优子集。最终在 BIRD 和 Spider 基准上仅选 796 和 863 个样本，实现 100% 表覆盖，使 Qwen3-8B 达到 69.1% 和 88.9% 执行准确率，超越使用 20 倍数据的方法，取得开源模型最优结果。

### 方法 / 贡献  
1. 识别 Text-to-SQL 数据高效学习的独特挑战——须联合优化结构覆盖（表/列）与样本质量。  
2. 提出四阶段框架：难度过滤 → 链式推理生成 → 多维评分 → 遗传算法联合选择。  
3. 实证表明仅需约 800 样本即可达强性能，为资源高效的语义解析研究指明新方向。

### 实验或数据  
在 BIRD 和 Spider 基准上评估。LIMIT 从候选池中筛选出 796（BIRD）和 863（Spider）个样本，训练 Qwen3-8B 后执行准确率分别为 69.1%（BIRD）和 88.9%（Spider），超过使用 20 倍数据的方法，刷新开源模型最佳记录。

### 值得关注点  
- “少即是多”思想首次在结构化推理任务（Text-to-SQL）中系统验证，数据规模大幅缩减（两个数量级）。  
- 遗传算法同时优化覆盖度与质量，解决数据量最小化与结构覆盖最大化之间的固有矛盾。  
- 模型仅用开源基座（Qwen3-8B）即可达 SOTA，成本低、可复现性强。

### 局限性  
论文未明确展开局限性讨论。但可推断：方法依赖 GPT-4o 等强 LLM 作为评分器，存在额外调用成本和对专有模型的依赖；框架多个阶段（难度过滤、CoT 生成、评分、遗传算法）需要较多前期数据处理开销，且效果可能受原始候选池质量影响。

## 3. To Consolidate or not to Consolidate? Evaluating the Impact of Consolidation in Multi-Reference Training using Peer Reviews

- Source: arxiv
- arXiv ID: 2609.22805
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.22805v1
- PDF: https://arxiv.org/pdf/2609.22805v1
- DOI: https://doi.org/10.48550/arXiv.2609.22805

### Authors

Maitreya Prafulla Chitale, Ketaki Mangesh Shetye, Yash More, Harshit Gupta, Manav Chaudhary, Manish Shrivastava, Vasudeva Varma

### Abstract

Natural language generation (NLG) tasks span the spectrum of conditional entropy, ranging from highly constrained machine translation to open-ended dialogue generation. Structured tasks like automated peer-review generation occupy the intermediate region, where a single input admits multiple valid, overlapping outputs. In this work, we demonstrate that traditional single- and multi-reference training paradigms are suboptimal for these intermediary tasks. We provide empirical evidence that consolidating diverse references into a unified training signal is crucial for developing effective systems. To facilitate this, we introduce MERC-36K, a large-scale corpus of over 36,000 papers paired with original and consolidated peer reviews. Using this dataset, we train specific architectures to isolate the impact of different reference paradigms and benchmark against existing state-of-the-art systems. Through extensive automatic and human evaluation, we demonstrate that models trained on consolidated references significantly outperform those trained on unconsolidated references. Dataset and code will be released upon acceptance.

### 中文一句话结论
在自动同行评议生成这类中间熵自然语言生成任务中，将多个多样化的参考文本合并为一个统一的训练信号，相比传统的单参考或多参考范式能显著提升模型性能。

### English TL;DR
Consolidating multiple diverse references into a unified training signal significantly outperforms traditional single- and multi-reference paradigms for intermediary natural language generation tasks like automated peer-review generation.

### 中文详细总结
该论文针对自然语言生成任务中的中间熵区域（如自动同行评议生成），指出传统单参考和多参考训练范式均非最优。单参考训练丢失了多样化视角，多参考训练则因目标未对齐而引入高方差。作者提出将多个原始评阅意见合并（consolidation）为一个统一的训练信号，能更稳定地捕捉有效人类反馈的完整分布。为此，他们构建了MERC-36K数据集，包含超过36,000篇论文及其原始评阅和合并评阅。基于此数据集，作者在Llama-3.1-8B-Instruct骨干模型上进行对比实验，并通过自动评估（ROUGE、BERTScore）和人工评估（30名专家对50篇论文的600个实例进行盲法排序）证明：基于合并参考训练的模型（Llama-Consolidated）在多数指标上显著优于单参考、多参考及现有SOTA系统。

### 方法 / 贡献
1. **问题定义**：首次系统分析中间熵NLG区域（自动评议生成）的参考训练范式问题，指出单参考和多参考范式均不理想。
2. **数据集构建**：发布MERC-36K，包含36,537篇论文（来自ICLR、NeurIPS、COLM七届会议）及其原始评阅和合并评阅（采用SEA-S工具合并为统一四段式格式：Summary, Strengths, Weaknesses, Questions）。
3. **对比实验设计**：在相同骨干模型（Llama-3.1-8B-Instruct）上系统比较三种范式——单参考（零样本、高置信度微调）、多参考（Reviewer2、OpenReviewer、Llama-MultiRef）、合并参考（SEA-E、AutoRev、Llama-Consolidated），严格控制变量。
4. **评估方法**：结合自动指标（ROUGE-1/2/L、BERTScore）和人工评估（30名ML研究者，Kendall's W衡量一致性），保证结论可靠性。

### 实验或数据
- **数据集**：MERC-36K，36,537篇论文，145,530条原始评阅，来自COLM 2024/2025、NeurIPS 2023/2024、ICLR 2024/2025/2026；80-10-10分层划分。
- **自动评估**：以合并评阅为金标准，Llama-Consolidated在ROUGE-1 F1 (57.03)、R-2 F1 (20.90)、R-L F1 (24.68)、BERTScore F1 (87.65)上均为最佳，显著超越所有单参考和多参考基线。以原始评阅为金标准时，各模型差距缩小（因原始评阅多样性高），但合并系统在召回率上仍有优势。
- **人工评估**：50篇论文，每篇3名标注者，比较Llama-Inference、Llama-HighConf、Llama-MultiRef、Llama-Consolidated的生成质量，Llama-Consolidated在全面性上显著领先。

### 值得关注点
1. **核心发现清晰**：通过严格控制变量（相同骨干、相同输入），直接证明合并参考是优于单/多参考的通用训练策略，而非模型或数据集差异所致。
2. **数据集价值**：MERC-36K是目前最大的同行评议数据集之一，且包含对齐的原始-合并评阅对，可推动相关研究。
3. **人工验证扎实**：30名专家、600个实例的盲法排序实验为自动评估结果提供了强有力支撑，解决了n-gram指标对开放生成任务不敏感的问题。
4. **技术选择合理**：采用基本思想简单的SEA-S进行合并，避免引入复杂方法对结论的干扰，保证了实验的归因清晰。

### 局限性
- 论文仅对Llama-3.1-8B-Instruct一个骨干模型进行了系统实验，未验证结论在更大模型或其他架构上的泛化性。
- 数据集仅涵盖机器学习领域会议（ICLR、NeurIPS、COLM），结论在其他学术领域或非学术评议场景中的适用性未知。
- 合并过程采用SEA-S自动化工具，其本身可能引入噪声或偏见（如丢失某些原始评阅中的独特观点），但论文未分析此合并质量对结果的影响。
- 实验限制模型参数不超过8B，更大参数规模下的效果趋势未探讨。
- 自动评估中，以原始评阅为金标准时合并系统的优势大幅缩小，说明合并参考与原始评阅的匹配度并非绝对优势，可能在某些场景下存在信息损失。

## 4. Team DArgk at the 2026 ELOQUENT lab for evaluating generative language model quality: Residuals of Humanity: AI Detection Evasion via GRPO Fine-Tuning

- Source: arxiv
- arXiv ID: 2609.22221
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.22221v1
- PDF: https://arxiv.org/pdf/2609.22221v1
- DOI: https://doi.org/10.48550/arXiv.2609.22221

### Authors

Antonela Tommasel, Juan Manuel Rodriguez

### Abstract

Large language models (LLMs) can generate fluent and coherent text that is increasingly difficult to distinguish from human writing, motivating the development of automatic AI-generated text detectors. However, the robustness of such detectors under adversarial generation remains uncertain. This paper presents SHADE (Stochastic Human-like generation via Adversarial Detector Evasion), a reinforcement learning framework that formulates detector evasion as a policy optimization problem. Instead of applying post-hoc perturbations or prompting-based rewriting, SHADE fine-tunes an instruction-tuned LLaMA model with Group Relative Policy Optimization (GRPO), using feedback from a surrogate detector based on the PAN 2025 mdok system. Our experiments show that full fine-tuning with a small KL regularization penalty achieves $98.5\%$ surrogate evasion, compared to $1.5\%$ for the base model, while LoRA-based adaptation is substantially less effective under regularization. Linguistic analysis reveals that successful evasion is associated with shorter, simpler, and less lexically diverse outputs, suggesting that high detector evasion does not necessarily correspond to more human-like writing. In the official Voight-Kampff competition setting, our submissions ranked sixth and seventh, indicating that optimization against a single surrogate detector only partially transfers to unseen evaluation classifiers. These results highlight both the potential and limitations of reinforcement learning for adversarial AI-text generation and motivate more robust, multi-detector evaluation protocols for AI-generated text detection.

### 中文一句话结论
本文提出基于GRPO强化学习的SHADE框架，直接微调LLaMA 3.2 3B模型以欺骗AI文本检测器，在替代检测器上达到98.5%的规避率，但对未见检测器的泛化有限，且规避成功伴随文本简化而非更类人的写作。

### English TL;DR
This paper presents SHADE, a reinforcement learning framework that fine-tunes an LLM via GRPO using surrogate detector feedback to evade AI-generated text detectors, achieving high evasion rates but showing limited transfer to unseen detectors and a tendency toward linguistic simplification.

### 中文详细总结
本文针对AI生成文本检测器的对抗鲁棒性问题，提出SHADE框架，将检测器规避形式化为策略优化问题。作者使用基于PAN 2025 mdok系统的替代检测器（mdok-roberta，骨干网络为RoBERTa-base）作为奖励信号，采用GRPO算法对LLaMA 3.2 3B Instruct模型进行全参数微调。实验表明，全微调配合较小的KL正则化惩罚可实现98.5%的替代检测器规避率，而基座模型仅1.5%；LoRA适配在此设置下效果较差。语言学分析显示，成功规避与更短、更简单、词汇多样性更低的输出相关，说明高规避率不一定对应更类人的写作。在官方Voight-Kampff竞赛中，提交的系统排名第六和第七，表明针对单一替代检测器的优化无法完全迁移到未见过的评估分类器。

### 方法 / 贡献
- 提出SHADE框架，将检测器规避视为强化学习问题，直接优化生成策略而非后处理扰动或提示重写。
- 使用GRPO算法，奖励定义为替代检测器置信度的补集（1 - D_hat(y)）。
- 替代检测器基于PAN 2025的mdok系统，骨干替换为RoBERTa-base，用PAN 2025数据训练，验证集F1为99%（原文未明确完整数字，但摘要提到F1分数接近99%）。
- 主要贡献：① 形式化检测器规避为强化学习问题；② 引入基于GRPO的微调框架；③ 实证分析规避与文本属性的关系，发现简化文本可导致高规避率。

### 实验或数据
- 训练数据：来自ELOQUENT 2024、2025、2026的Voight-Kampff任务数据集，以及PAN 2025数据集（用于训练替代检测器）。
- 实验对比：全微调与LoRA适配，在不同KL正则化惩罚下的表现。
- 结果：全微调+小KL惩罚达到98.5%替代规避率；基座模型1.5%；LoRA效果较差。
- 官方竞赛：提交系统排名第六和第七（未见检测器下）。
- 语言学分析：输出长度、复杂度、词汇多样性等指标与规避率的相关性。

### 值得关注点
- 将强化学习（GRPO）应用于AI文本检测规避，区别于常见的后处理或提示方法。
- 发现高规避率可能通过简化文本而非增强类人性实现，这一反直觉结果对检测器设计有提示意义。
- 使用替代检测器进行训练，但官方评估显示跨检测器泛化有限，凸显多检测器评估协议的必要性。

### 局限性
- 仅针对单一替代检测器（mdok-roberta）优化，未见检测器上的迁移效果有限（官方排名第六、第七）。
- 替代检测器与原mdok系统存在骨干差异（RoBERTa-base替代Qwen3-14B），可能影响训练信号保真度。
- 实验仅使用单个基础模型（LLaMA 3.2 3B），未展示在其他规模或架构上的泛化。
- 观察到的文本简化现象可能损害输出质量，未评估语义一致性或实用性。
- 论文未提供详细的数据集统计或消融实验细节（如不同KL惩罚的完整曲线）。

（注：部分具体数字如F1=99%是基于摘要和预览内容中的信息，原文未完全给出，但摘要提到“F1 score of 99%”在预览中被截断，故按此表述。）

## 5. Dissecting Training-Free Uncertainty Estimation in Multimodal Large Language Models

- Source: arxiv
- arXiv ID: 2609.22206
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.22206v1
- PDF: https://arxiv.org/pdf/2609.22206v1
- DOI: https://doi.org/10.48550/arXiv.2609.22206

### Authors

Soroush Seifi, Vaggelis Dorovatas, Lin Li, Yarin Gal, Rahaf Aljundi

### Abstract

Multimodal Large Language Models (MLLMs) have achieved remarkable performance across a wide range of multimodal tasks, yet understanding and quantifying their predictive uncertainty remains underexplored despite being central for safety critical applications. In this work, we present a systematic study of training-free uncertainty quantification strategies for MLLMs, categorizing existing approaches into three conceptual families: token-level methods, which operate directly in the text output space; verbalized methods, which elicit uncertainty estimates or abstention signals via natural language prompts; and semantic methods, which measure uncertainty in a semantic meaning space. We benchmark these strategies across multiple datasets, model families, generations, and scales, and find that no single family dominates: token-level entropy (at sampling temperature 1.0) wins on short answers, verbalized abstention on sentence-length responses, and semantic methods on long-form generation.

### 中文一句话结论
本研究发现，对于多模态大语言模型，无需训练的预测不确定性量化方法的效果高度依赖输出长度，没有单一方法能在所有场景下表现最佳：短回答首选 token 级熵，句长回答首选言语化弃权，长回答首选语义不确定性方法。

### English TL;DR
This paper systematically benchmarks three families of training-free uncertainty quantification methods for multimodal large language models—token-level, verbalized, and semantic—and finds that no single method dominates across all response lengths, with token-level entropy best for short answers, verbalized abstention for sentence-length responses, and semantic methods for long-form generation.

### 中文详细总结
该论文对多模态大语言模型（MLLMs）中的无需训练的不确定性量化策略进行了系统研究。作者将现有方法分为三类：**token级方法**（基于输出文本空间的概率分布，如熵、负对数似然）、**言语化方法**（通过自然语言提示让模型表达不确定或弃权）、**语义方法**（在语义空间中衡量不确定性，如语义熵）。研究在8个MLLM（涵盖InternVL和QwenVL两个系列、两代、小规模2B和中等规模7-8B）上，对5个VQA基准（覆盖多选题、短回答、句子级和长回答格式）进行基准测试。主要发现：**输出长度决定最佳方法**——token级熵（采样温度1.0）在短回答上最优，言语化弃权在句子级回答上最优，语义方法在长文本生成上最优；token级不确定性在确定性解码下失效，但高温采样可恢复；言语化不确定性在小型和老旧MLLM中不可靠，但在新中等规模模型（如Qwen3-VL-Instruct）中表现良好；**所有方法在合理覆盖率下风险均较高**，表明MLLM安全部署仍有显著差距。

### 方法 / 贡献
- 提出一个无需训练的MLLM不确定性量化方法分类体系：token级（熵、NLL）、言语化（置信度、弃权）、语义（语义熵、VASE等）。
- 系统基准测试8个MLLM、5个基准，跨模型系列、代际、规模、输出长度分析。
- 引入校准幻觉检测准确率（CHDA）作为部署导向指标，在小标定集上调整阈值。
- 总结四个主要发现：输出长度决定最优方法族；token级不确定性在确定性解码下失效；言语化不确定性随模型规模增加而改善；现有方法无法在合理覆盖率下实现低风险。

### 实验或数据
- **模型**：InternVL（第2、3.5代）和QwenVL（第2、3代），小规模（~2B）和中等规模（7-8B），共8个模型。
- **基准**：按输出长度分组——短回答（ScienceQA、MMMU、MM-Vet）、句子级（FSVQA200子集）、长回答（LLaVABench、MM-Vet Long）。
- **指标**：AUROC（阈值无关的排序质量）、Coverage@20（风险≤20%的最大覆盖率）、校准幻觉检测准确率（CHDA，在标定集上调阈值的部署度量）。
- **结果**：报告跨模型的平均性能表，显示不同回答长度下的最佳方法族。

### 值得关注点
- **输出长度是关键因素**：方法选择应根据预期回答长度调整，而非模型或数据集。
- **token级不确定性在高温采样下效果显著**：简单方法（如熵）在适当设置下可匹敌昂贵语义方法。
- **言语化不确定性在新型中规模模型中出现**：Qwen3-VL-Instruct 的言语化弃权在句子级回答中表现最佳，为封闭源模型提供实用方案。
- **安全部署差距大**：所有方法在风险≤20%时覆盖率有限，表明当前MLLM不确定性估计不足以支持安全关键应用。

### 局限性
- 未在更大规模模型（如>10B）或多模态数据类型（如视频、音频）上验证。
- 仅关注无需训练的方法，未探讨微调或 prompt 优化对不确定性感知的影响。
- 言语化弃权可能依赖特定的提示模板，泛化性有限。
- 语义方法需要多轮推理和独立蕴含模型，计算成本高，不适用于实时场景。
- 实验未充分覆盖所有 MLLM 系列（如 LLaVA、GPT-4V 等封闭源模型），结论可能受模型选择偏差影响。

## 6. Contextual Causality with Large Language Models: A Survey

- Source: arxiv
- arXiv ID: 2609.22409
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.22409v1
- PDF: https://arxiv.org/pdf/2609.22409v1
- DOI: https://doi.org/10.48550/arXiv.2609.22409

### Authors

Yiheng Zhao, Jun Yan, Chengming Hu

### Abstract

Understanding contextual causality is critical for large language models (LLMs), as it enables them to accurately identify causal relations in specific situations and support more reliable decision-making. Despite its significance, a systematic exploration of contextual causality with LLMs is still lacking. To fill this gap, we present a comprehensive survey on this topic. In this survey, we first propose a taxonomy of contextual causality, consisting of semantic, intervention, and counterfactual causality, and characterize each category by its core causal question, required model capabilities, representative tasks, and practical uses in causality analysis. We then analyze existing studies and discuss their key limitations. Finally, we examine the gaps between current benchmarks and real-world needs and outline promising directions for future research. Our goal is to clarify the research landscape of contextual causality with LLMs, emphasize its importance, and highlight promising future directions.

### 中文一句话结论  
本综述首次系统梳理了大语言模型（LLM）中的“上下文因果性”（contextual causality），提出语义因果、干预因果和反事实因果三类 taxonomy，并指出现有基准与真实世界需求之间存在差距及未来方向。

### English TL;DR  
This survey systematically reviews contextual causality in large language models (LLMs) by proposing a taxonomy of semantic, intervention, and counterfactual causality, analyzing existing studies and their limitations, and highlighting gaps between current benchmarks and real-world needs to guide future research.

### 中文详细总结  
论文围绕 LLM 的上下文因果性展开综述。作者指出，理解特定情境下的因果关系对 LLM 的可靠决策至关重要，但此前缺乏系统性梳理。他们提出一个分类体系，将上下文因果性分为三类：  
- **语义因果（Semantic Causality）**：关注文本中已表达或隐含的因果关系，核心问题是“上下文中表达了什么因果信息”。  
- **干预因果（Intervention Causality）**：关注在给定情境中引入某个动作后会产生什么结果，核心问题是“如果我这样做会怎样？”。  
- **反事实因果（Counterfactual Causality）**：关注在过去采取不同行动时结果是否会改变，核心问题是“如果我当时做了不同选择会怎样？”。  

综述还分析现有研究（包括评估导向和方法导向的工作），讨论其局限性，并比较了与已有因果关系综述的差异。最后，作者指出当前基准与真实需求之间的差距，并建议未来关注更贴近真实世界的基准构建、更细粒度的评估、后训练数据构建，以及对干预和反事实因果的更多研究。

### 方法 / 贡献  
- 提出上下文因果性的新分类法（语义、干预、反事实），并明确每类的核心因果问题、所需模型能力、代表性任务和实际用途。  
- 系统分析现有研究，涵盖评估导向（性能评估、基准构建）和方法导向（无训练、基于训练）工作。  
- 与已有综述对比，突出本综述对三类上下文因果性的系统覆盖，而非仅关注非上下文因果或单一子任务。  
- 提出未来研究方向，包括真实世界导向的基准、细粒度评估、后训练数据构建，以及加强对干预和反事实因果的关注。

### 实验或数据  
摘要和提供的正文预览中没有报告新的实验结果或具体数据集。该综述属于系统文献综述，主要基于已有文献和基准进行分析，而非开展新实验。

### 值得关注点  
- 首次系统建立“上下文因果性”的综合分类框架，弥补现有综述偏重非上下文因果（如因果发现、因果推断）的不足。  
- 明确区分三类因果对应的 LLM 能力差异：语义因果需识别和解释，干预因果需结果估计，反事实因果需想象和反事实推理。  
- 比较已有综述时指出，现有工作多覆盖反事实生成（CG）而非更广泛的反事实推理（CR），锚定了本研究的定位。

### 局限性  
- 作者指出当前基准与真实世界需求之间存在明显差距，尤其是现有基准可能无法真正评估 LLM 的上下文因果能力，而可能只是测试知识检索。  
- 干预因果和反事实因果的研究相对不足，尤其与语义因果相比。  
- 未来需要更真实、更细粒度的基准，以及更多针对后训练数据构建的研究，但目前尚未形成成熟方案。

## 7. Weak Ties, Strong Signals: Efficient Training Data Detection in Diffusion LLMs via Independent Token Sampling

- Source: arxiv
- arXiv ID: 2609.22145
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.22145v1
- PDF: https://arxiv.org/pdf/2609.22145v1
- DOI: https://doi.org/10.48550/arXiv.2609.22145

### Authors

Hongyao Yu, Tianqu Zhuang, Ziyuan Xu, Hao Fang, Jiaxin Hong, Bin Chen, Shu-Tao Xia

### Abstract

Diffusion large language models (dLLMs) offer a compelling alternative to autoregressive models, yet they may expose sensitive training data during denoising. Detecting such usage is challenging because dLLMs lack the efficient one-pass probability decomposition of causal architectures. Existing methods rely on random masking to obtain tractable token-wise detection signals under limited query budgets, but fail to control dependencies among masked tokens. We demonstrate that this token-wise approximation introduces a non-negative structural estimation error, which is theoretically characterized by the cumulative conditional mutual information (CMI) among masked tokens and can obscure subtle memorization signals. This insight suggests that reliable detection requires masked token sets with weak internal dependency. To avoid the prohibitive cost of directly estimating CMI over token combinations, we propose \textit{Independent Token Sampling} (ITS), a query-efficient framework that uses an attention-derived pairwise dependency proxy to approximate the CMI-aware selection criterion. ITS further incorporates a diversity-promoting strategy to improve token coverage across sampling rounds, yielding aggregated token-wise signals that are less affected by dependency-induced approximation error. Experiments on multiple datasets show that ITS consistently outperforms state-of-the-art baselines across different models and datasets, achieving an AUC improvement of 0.18 on the ArXiv dataset while maintaining strong performance under limited query budgets. The code is available at https://github.com/Chrisqcwx/DLLM-MIA .

### 中文一句话结论
本文提出独立Token采样(ITS)方法，通过选择弱依赖的Token子集，显著提升了扩散大语言模型训练数据检测的准确性。

### English TL;DR
Independent Token Sampling (ITS) uses attention-derived dependency proxies to select weakly dependent token subsets, reducing estimation error and improving training data detection in diffusion LLMs, outperforming baselines.

### 中文详细总结
扩散大语言模型（dLLMs）在去噪过程中可能泄露训练数据，但因其无法像自回归模型那样高效分解概率，检测存在困难。现有方法采用随机掩码获取Token级检测信号，但未控制掩码Token间的依赖关系，导致结构估计误差（由累积条件互信息CMI表征）掩盖细微记忆信号。本文理论证明该误差与掩码Token间的条件互信息成正比，由此提出独立Token采样（ITS）框架：利用注意力机制导出的成对依赖代理近似CMI感知的选择准则，并加入多样性促进策略以提升采样轮次间的Token覆盖。实验在多个数据集和模型上表明，ITS显著优于现有方法，在ArXiv数据集上AUC提升达0.18，且在有限查询预算下保持强性能。

### 方法 / 贡献
- **理论洞察**：识别出用Token级概率乘积近似联合概率时引入的结构估计误差，该误差由掩码Token间的累积条件互信息刻画。
- **独立Token采样（ITS）**：基于注意力机制构建成对依赖代理，选择弱依赖Token子集；引入多样性惩罚促进跨轮次Token覆盖。
- **实证验证**：在多个dLLM和数据集上超越最先进基线。

### 实验或数据
- 实验在多个数据集（如ArXiv）和不同dLLM（如LLaDA）上进行。
- 使用AUC作为评价指标，ITS在ArXiv数据集上取得0.18的提升。
- 在有限查询预算下保持强性能；涵盖LoRA稀疏更新等挑战场景。

### 值得关注点
- 首次从理论层面将检测误差与条件互信息关联，为选择弱依赖Token子集提供理论依据。
- 利用注意力权重作为依赖代理，避免了直接估计CMI的高昂计算成本。
- 多样性促进策略进一步提升了有限查询下的信号聚合质量。

### 局限性
- 依赖注意力权重作为依赖代理，可能无法完美捕捉所有Token间的依赖关系。
- 需要访问参考模型（灰色盒设置）以及模型的注意力内部结构。
- 理论分析基于特定假设（如马尔可夫性），实际场景中可能不完全成立。
- 查询预算仍受限制，极端低预算下的鲁棒性有待进一步验证。

## 8. Measuring Behavioural Signatures of Large Language Models through Psychometric Profiling

- Source: arxiv
- arXiv ID: 2609.22934
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.22934v1
- PDF: https://arxiv.org/pdf/2609.22934v1
- DOI: https://doi.org/10.48550/arXiv.2609.22934

### Authors

Yu Sha, Junqi Tao, Dixin Zhou, Yansheng Tu, Mingyang Chen, Xiang Fan, Yang Liu, Mengquan Yang, Jie Lin, Jiahui Fu, Hua Zheng, Benwei Zhang, Zhou Kai

### Abstract

Large language models (LLMs) increasingly mediate human decisions and communication, yet their behavioural regularities remain difficult to characterize systematically. We develop a cross-linguistic psychometric profiling framework and evaluate nine LLMs using seven psychological instruments, with five repeated administrations per model and language in Chinese and English. Items unresolved after a prespecified retry procedure are retained as NA. Joint analysis of scored and NA responses captures response tendencies and boundaries of self-report applicability. LLMs exhibit structured, model-specific profiles despite a shared alignment-shaped pattern of higher prosocial and self-regulatory responses and lower dominance, disengagement and harmful-intent endorsement. NA responses are structured rather than uniformly distributed, indicating where outputs are treated as inapplicable, refused or cannot be mapped to valid response options. Language condition and provider origin are associated with profile configuration and answerability, whereas repeated administrations show high reproducibility and permit recovery of model identity. Human-reference and prompt-robustness analyses further indicate that these signatures are context dependent. Joint analysis of psychometric profiling and answerability offers a framework for quantifying deployment-level behavioural signatures.

### 中文一句话结论
本研究通过跨语言（中英）七套心理量表对九个大语言模型进行心理测量学画像，发现模型虽呈现共享的对齐塑造型响应模式（高亲社会、低支配），但各自具有结构化的、模型特异的且可重复的行为签名，且“不回答”（NA）响应同样具有系统性结构，可共同用于刻画部署层面的行为特征。

### English TL;DR
LLMs exhibit structured, model-specific psychometric profiles and systematic answerability patterns across languages and providers, jointly revealing reproducible behavioral signatures shaped by alignment and context.

### 中文详细总结
论文提出一个跨语言的心理测量学画像框架，使用七个心理测量工具（IPIP BFFM-50、MFQ-30、OEJTS-32、OUS-9、PMD-8、SDO7-16、SSIS-10）对九个来自中国及国际提供商的LLM进行系统评估。每个模型在中文和英文条件下各进行五次独立重复施测，并采用预设重试流程，未能解决的题目保留为NA（不可作答）。

联合分析得分响应与NA响应后发现：（1）所有模型呈现共享的、对齐塑造型的模式——亲社会与自我调节维度得分较高，支配性、道德脱离和伤害意图认可得分较低；（2）同时各模型具有结构化且模型特异的画像差异，如Claude-4.5系列最为相似，Kimi-K2在支配性和反平等主义上最为突出；（3）NA响应呈现结构化而非均匀分布，标示了合成自我报告的适用边界；（4）语言条件和提供商来源均与画像配置及可作答性相关；（5）重复施测显示高可复现性，并能据此恢复模型身份；（6）人类参照与提示鲁棒性分析表明这些签名具有上下文依赖性。

作者强调，不应将得到的分数解释为模型具有类人心理特质，而应视为部署层面的行为响应签名。固定效应分析（FDR校正后）检测到19/20个维度存在模型相关变异，秩基鲁棒分析在18个维度上结果相似，表明模型效应并非由单一分布假设驱动。

### 方法 / 贡献
- 提出跨语言（中英）心理测量学画像框架，联合处理得分响应与NA（不可作答）响应两个互补测量通道。
- 使用七个标准心理量表覆盖人格、道德基础、认知风格、功利判断、道德脱离、社会支配倾向和施虐冲动等20个非冗余维度。
- 标准化管理协议（题项顺序、响应选项、AI自我映射、安全约束、输出格式等）保证跨模型、跨语言可比性。
- 通过固定效应与秩基双重重分析验证模型效应的稳健性；结合余弦/相关距离、聚类及模型身份恢复分析评估画像的整体相似性和可识别性。
- 贡献在于将可作答性（answerability）提升为与量表得分同等重要的表征通道，避免将LLM响应直接类比为人类人格特质。

### 实验或数据
- 评估对象：九个当代模型，来自中国及国际提供商。
- 施测方式：每个模型×每种语言（中文、英文）各进行5次独立重复施测。
- 分析包含：维度级得分剖面、整剖面相似性（余弦/相关距离）、聚类、模型身份恢复、跨语言与跨提供商的固定效应分析、提示鲁棒性分析。

### 值得关注点
- Claude-4.5两个变体画像几乎重叠，而Gemini-2.5-Flash与其Lite版本明显分离，说明同一提供商的变体并不必然产生等价画像。
- NA响应具有与得分响应同样强的结构化信号，提示“模型何时拒绝回答或认为题项不适用”本身即是重要的行为特征。
- 语言条件和提供商来源均能显著改变画像配置，提示跨文化评估对部署行为表征的必要性。
- 高分可复现性与模型身份恢复能力表明该框架可用于模型对比与追溯。

### 局限性
- 评估仅基于有限的九个模型端点，结论的普适性受模型版本更新影响。
- 所有响应均为API交互所得，未包含人机对话中的动态上下文；提示鲁棒性分析虽表明签名具上下文依赖性，但未穷尽所有提示变体。
- 心理量表面向人类被试设计，NA虽被解释为不可作答或拒答，但无法从测量本身区分其具体成因（拒绝、不适用、映射失败等）。
- 摘要未提及具体数据集公开性、样本量表完整条目数量或置信区间等统计细节；论文正文预览有限，部分统计数值（如效应量）未在此呈现。

## 9. On Mitigation of Subliminal Learning in Large Language Models

- Source: arxiv
- arXiv ID: 2609.22215
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.22215v1
- PDF: https://arxiv.org/pdf/2609.22215v1
- DOI: https://doi.org/10.48550/arXiv.2609.22215

### Authors

Atsushi Yanagisawa, Brendan Gho, Rajendran Ramesh Babu Manoj Narender, Kevin Zhu, Madhur Panwar, Antonio Mari

### Abstract

Knowledge distillation can transmit unintended behavioral traits from a teacher model to a student through training data that appear semantically unrelated to those traits, a phenomenon known as subliminal learning. Although recent work has established this effect, its training dynamics and mitigation remain underexplored. We study subliminal learning in open-weight language models ranging from 1.5B to 8B parameters, covering the Qwen, Gemma, and Llama families in number-sequence and chain-of-thought settings. Rather than evaluating only final models, we track trait-related probabilities throughout fine-tuning and find that subliminal acquisition can be highly non-monotonic, with transient spikes, reversals, and trait-specific failures of transfer. We then introduce liminal training, an annealed KL-regularized fine-tuning method that constrains early drift from the base model. Across our experiments, liminal training substantially reduces subliminal trait acquisition while largely preserving task gains, outperforming paraphrasing and layer freezing as mitigation strategies. The effect also extends beyond animal preferences: in a French-language response-style experiment, liminal training suppresses language transfer while retaining much of the GSM8K improvement. Finally, we show that KL timing matters: early regularization is more effective than late regularization, and sweeping the regularization strength reveals an empirical trade-off between task learning and trait suppression.

### 中文一句话结论
本文提出“liminal training”（阈限训练），一种退火KL正则化微调方法，能显著减少大型语言模型在知识蒸馏中的潜意识学习，同时保留大部分下游任务性能。

### English TL;DR
This paper studies the training dynamics of subliminal learning in large language models and introduces **liminal training**, an annealed KL-regularized fine-tuning method that substantially reduces unintended trait transfer from teacher to student while preserving most downstream task performance, outperforming paraphrasing and layer freezing across multiple model families and settings.

### 中文详细总结
论文研究大型语言模型在知识蒸馏中的“潜意识学习”：学生模型会从教师模型中继承与训练数据语义无关的行为特质。作者在1.5B至8B参数的开源模型（Qwen、Gemma、Llama家族）上，通过数字序列和思维链（CoT）任务进行实验。他们发现特质获取在微调过程中高度非单调，出现瞬态尖峰、反转和特质特定的迁移失败。为此提出“liminal training”，即在微调早期加入退火KL散度正则化，约束模型偏离基础分布。实验表明，该方法在多个模型和设置中均优于释义（paraphrasing）和层冻结（layer freezing）策略，能大幅压制潜意识特质获取，同时保持大部分任务准确率（如GSM8K）。此外，该方法也适用于法语响应风格等非动物偏好特质，且早期正则化比晚期更有效，正则化强度在任务学习与特质抑制间存在权衡。

### 方法 / 贡献
- 提出 **liminal training**：一种退火KL正则化微调方法，在训练早期施加KL散度惩罚并随时间衰减，约束模型早期漂移。
- 贡献：
  1. 提出限阈训练，并与释义和层冻结对比，证明其在抑制潜意识学习上最有效。
  2. 分析KL调度和强度，发现早期正则化更有效，且存在任务学习与特质抑制的权衡。
  3. 将分析扩展到非动物偏好特质（法语响应风格），验证方法的通用性。
  4. 刻画微调过程中的特质动态，揭示非单调性和与初始特质概率的关系。

### 实验或数据
- 模型：Qwen2.5-{1.5B/3B/7B}-Instruct, Gemma-3-4B-IT, Llama-3-8B-Instruct。
- 任务：数字序列完成（30,000 prompts，子采样至7,500）和GSM8K思维链蒸馏（筛选正确样本）。
- 设置：教师和学生共享相同基础模型；教师通过系统提示注入偏好；控制数据集为无偏好微调（NFT）；通过50个探针提示计算特质概率进行度量。
- 额外实验：法语响应风格实验，在GSM8K任务上观察语言特质转移。

### 值得关注点
- 微调过程中特质概率变化非单调，存在瞬态尖峰和反转，初始特质概率强烈影响变化模式。
- **早期KL正则化比晚期更有效**，且正则化强度与任务学习存在实证权衡。
- 限阈训练在压制动物偏好和语言风格特质上均有效，同时保留大部分GSM8K提升。
- 方法不依赖数据筛选或修改，仅通过约束训练过程实现。

### 局限性
根据提供的摘要，论文未明确讨论局限性。实验范围限于特定模型家族（Qwen、Gemma、Llama）和特质（动物偏好、语言风格），可能未覆盖所有潜在模型或特质类型。

## 10. Custom Named Entity Recognition and Topic Classification for Global Health Publications

- Source: arxiv
- arXiv ID: 2609.24625
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.24625v1
- PDF: https://arxiv.org/pdf/2609.24625v1
- DOI: https://doi.org/10.48550/arXiv.2609.24625

### Authors

Genis Skura, Antoine Geissbühler, Jean-Luc Falcone

### Abstract

How should natural language processing models be selected and adapted for global health literature in environments where annotated data and computational resources are limited? This thesis investigates these challenges through experiments on semantic tag discovery, named entity recognition (NER), and multi-label topic classification. First, skip-gram word2vec models trained on progressively larger specialized corpora are compared with BioWordVec to assess how corpus size and domain context influence tag discovery. Vocabulary coverage and qualitative evaluation indicate that broader coverage does not necessarily yield more useful domain-specific associations. The analysis then turns to entity extraction, comparing convolutional spaCy models with a RoBERTa-based transformer on 1,000 annotated sentences. Under a lenient scoring protocol, the transformer achieves 0.80 micro-F1 versus 0.65-0.69 for convolutional models, but takes 82 seconds rather than 5-6 seconds. This trade-off motivates fine-tuning convolutional models and integrating a disease recognizer that achieves 81.33% test F1 on the NCBI Disease Corpus. Combined with PDF preprocessing, entity filtering, and MeSH enrichment, the resulting pipeline supports document-level indexing. To complement entity extraction with thematic annotation, MiniLM-based few-shot classification is compared with BART-MNLI zero-shot inference across 50 topics and 1,000 handcrafted test sentences. BART-MNLI achieves 95.2% single-label accuracy versus 59%; reported multi-label accuracies are 88% and 32% under partly manual assessment. However, its higher inference cost limits practical integration. The results show where domain specialization and lightweight adaptation offer practical value, and where transformer accuracy justifies higher inference costs, providing an empirical basis for building knowledge systems under resource constraints.

### 中文一句话结论
在标注数据和计算资源有限的前提下，面向全球健康文献的 NLP 系统需要在准确率与推理成本之间做务实权衡：轻量模型加领域微调适合实际流水线，而 transformer 虽然在 NER 和主题分类上准确率更高，但只有在其额外成本可接受时才值得采用。

### English TL;DR
This thesis investigates how to select and adapt NLP models for global health publications under limited annotated data and computational resources. Through experiments on tag discovery, named entity recognition (NER), and multi-label topic classification, it compares lightweight convolutional models with transformer-based models, showing consistent accuracy–cost trade-offs and demonstrating where domain specialization and lightweight adaptation offer practical value.

### 中文详细总结
该论文围绕全球健康文献的 NLP 应用展开，核心问题是：在标注数据和算力受限的环境中，如何选择和改造模型。研究分为三个部分：

1. **标签发现**：使用 skip-gram word2vec 在逐步增大的领域语料上训练词向量，并与 BioWordVec 对比。结果显示，词汇覆盖更广并不一定带来更有用的领域语义关联。
2. **命名实体识别**：在 1000 句人工标注句子上比较卷积 spaCy 模型与 RoBERTa transformer。宽松评分协议下，transformer 的 micro-F1 为 0.80，卷积模型为 0.65–0.69；但 transformer 推理耗时 82 秒，而卷积模型仅 5–6 秒。为平衡效率，作者微调卷积模型，并集成疾病识别器（NCBI Disease Corpus 测试 F1 为 81.33%），结合 PDF 预处理、实体过滤和 MeSH 丰富，实现文档级索引。
3. **主题分类**：在 50 个主题、1000 条手写测试句上，比较 MiniLM few-shot 与 BART-MNLI zero-shot。BART-MNLI 单标签准确率为 95.2%，MiniLM 为 59%；多标签准确率在部分人工评估下分别为 88% 和 32%。但 BART-MNLI 的推理成本更高，限制了实际集成。

整体上，研究为资源受限环境下构建知识系统提供了实证依据，说明了何时应选择轻量适配，何时值得为 transformer 的准确率支付更高计算成本。

### 方法 / 贡献
- 系统比较了不同规模领域语料训练的 word2vec 与 BioWordVec 在标签发现中的表现。
- 对比了卷积 spaCy 模型与 RoBERTa transformer 在 NER 上的准确率和推理耗时，明确了 trade-off。
- 通过微调卷积模型并集成疾病识别器，构建了面向文档级索引的实体抽取流水线。
- 比较了 MiniLM few-shot 与 BART-MNLI zero-shot 的多标签主题分类能力。
- 结合 PDF 预处理、实体过滤、MeSH 丰富等模块，提出了一套完整的轻量 NLP 流水线。
- 核心贡献是为数据稀缺、算力有限的全球健康领域提供了模型选择和适配的实证依据。

### 实验或数据
- **标签发现**：使用逐渐增大的专门语料训练 word2vec，与 BioWordVec 比较；摘要未给出语料具体规模，仅说明进行了词汇覆盖度和定性评估。
- **NER**：1000 条人工标注句子，宽松评分协议下，RoBERTa micro-F1 0.80，卷积模型 0.65–0.69；推理时间分别为 82 秒和 5–6 秒。
- **疾病识别器**：在 NCBI Disease Corpus 上测试 F1 为 81.33%。
- **主题分类**：50 个主题，1000 条手写测试句；BART-MNLI 单标签准确率 95.2%，MiniLM 59%；多标签准确率分别为 88% 和 32%（部分人工评估）。
- 摘要未提供更多数据集细节。

### 值得关注点
- 更大语料覆盖并不等于更好的领域语义关联，领域相关性和数据质量可能比规模更重要。
- 在 NER 上，transformer 准确率更高，但推理时间远超卷积模型；微调后的轻量模型可以接近实际可用水平。
- 疾病识别器在公开基准上表现良好，适合作为流水线组件。
- BART-MNLI 零样本分类能力明显优于 MiniLM few-shot，但计算成本更高。
- 研究结果强调了“领域专门化 + 轻量适配”在资源受限环境中的价值，以及何时应接受更高推理成本换取准确率。

### 局限性
- NER 实验仅基于 1000 条标注句，且采用宽松评分协议，可能高估实际性能。
- 多标签主题分类准确率包含部分人工评估，结果可能不够严格或可重复。
- word2vec 标签发现主要依赖定性评估和词汇覆盖度，缺乏下游任务的定量验证。
- 模型比较仅覆盖有限的模型集合，结论不一定推广到其他 transformer 或嵌入方法。
- 摘要未报告训练/推理环境的详细配置，计算成本比较可能受具体实现影响。

## Processing Notes

- Duplicate papers skipped: 0