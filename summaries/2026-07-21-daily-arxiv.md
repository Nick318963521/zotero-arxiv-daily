# Daily arXiv - 2026-07-21

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-21T23:43:45
- Paper count: 10

## 1. PPL-Factory: Task-Aware and Budget-Aware Data Selection from Language Modeling to Reasoning

- Source: arxiv
- arXiv ID: 2607.18199
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2607.18199v1
- PDF: https://arxiv.org/pdf/2607.18199v1
- DOI: https://doi.org/10.48550/arXiv.2607.18199

### Authors

Hang Zhang, Warren J. Gross

### Abstract

Not all training samples contribute equally to large language model fine-tuning. Selecting informative training samples can reduce the computational cost while preserving downstream performance. Many existing data selection methods rely on indirect heuristics, such as data quality, diversity or reasoning trace length. However, the effectiveness of these fixed criteria is task-dependent and difficult to generalize across diverse downstream tasks. Perplexity-based data selection provides a simple and model-aware solution to estimate the sample difficulty, but existing approaches typically score the entire training sequence and ignore the difference in learning objectives of language modeling and reasoning tasks. In this paper, we propose PPL-Factory, a simple and interpretable data selection framework that combines task-aware perplexity-based scores and data budget-aware selection criteria. Experiments on GSM8K demonstrate that PPL-Factory outperforms other state-of-the-art data selection methods using only $1\%$ of the training set. With $10\%$ of the data, PPL-Factory exceeds full-data fine-tuning accuracy by 0.9 on GSM8K and 4.8 on MATH. Overall, our results demonstrate that task-aware and budget-aware perplexity-based selection provides an effective and applicable approach for efficient fine-tuning.

### 中文一句话结论
PPL-Factory提出一种结合任务感知困惑度评分与数据预算感知选择策略的轻量化数据筛选框架，仅用1%训练数据即可超越现有方法，并在10%数据量下达到甚至超过全量微调性能。

### English TL;DR
PPL-Factory introduces a task-aware and budget-aware perplexity-based data selection framework that efficiently selects informative subsets for LLM fine-tuning. By scoring samples via negative log-likelihood over task-specific regions (e.g., reasoning steps) and adapting selection criteria to data budgets, it outperforms SOTA methods using only 1% of training data and exceeds full-data fine-tuning on GSM8K (+0.9) and MATH (+4.8) with 10% data.

### 中文详细总结
现有数据选择方法多依赖间接启发式（如质量、多样性、推理链长度），但固定标准难以泛化至不同任务。基于困惑度（perplexity）的方法虽然简单且模型感知，但传统做法对整个序列打分，忽略了语言建模与推理任务的学习目标差异。PPL-Factory提出两项核心改进：（1）任务感知评分：对因果语言建模（CLM）任务，对固定长度token块计算平均负对数似然（NLL）；对数学推理任务，对推理步骤和答案区域分别计算NLL并进行加权组合，以捕捉最相关的学习信号。（2）数据预算感知选择：通过理论分析证明最优筛选子集分布随数据预算比例变化，因此设计预算依赖的选择准则（如低预算时采用中等难度+随机采样以平衡覆盖度与效用）。实验表明，PPL-Factory在GSM8K上仅用1%数据即超越现有方法；在10%数据量下，GSM8K精度超全量微调0.9%，MATH超4.8%。该方法无需外部评估器或昂贵梯度计算，仅需一次前向传播即可完成筛选。

### 方法 / 贡献
- 提出**任务感知NLL评分**：针对不同任务（CLM和数学推理）调整困惑度计算区域，避免全序列统一打分导致的信号稀释。
- 提出**预算感知选择准则**：基于信息覆盖最大化理论，推导出最优子集分布随预算动态变化，据此设计自适应选择策略（如低预算下采用“中等难度+随机”组合）。
- 实现**轻量高效**：仅需预训练模型单次前向传播即可获得评分，计算复杂度远低于梯度或影响函数方法。
- 实验证明：在GSM8K和MATH上，PPL-Factory以极低数据比例（1%-30%）达到或超越全量微调性能，并显著优于随机、全序列困惑度、嵌入相似度等基线。

### 实验或数据
- **数据集**：GSM8K（数学推理）、MATH（高难度数学推理），以及Causal LM任务（如Dolma等，但摘要未详述，论文中提及四个常见基准）。
- **实验设置**：从预训练模型（如LLaMA）出发，使用不同数据比例（1%、5%、10%、30%等）进行单次筛选后微调，并与随机选择、全序列困惑度排序、嵌入相似度、梯度相似度等基线对比。
- **主要结果**：
  - GSM8K：1%数据下优于所有对比方法；10%数据时精度比全量微调高0.9%。
  - MATH：10%数据时精度比全量微调高4.8%。
  - 30%数据下持续优于或持平全量微调。
- **消融实验**（根据论文结构推测）：验证了任务感知评分和预算感知策略各自的贡献，以及不同选择准则（easy/hard/middle/mid_random）在不同预算下的效果差异。

### 值得关注点
- **任务感知评分设计**：将NLL计算限定在推理步骤或答案区域，而非整个序列，更符合推理任务的学习重点。
- **预算感知理论推导**：从信息覆盖最大化出发，为不同数据比例提供理论指导，避免简单固定阈值导致低预算下性能崩溃。
- **极低数据比例下的优异表现**：仅用1%数据即超越其他复杂方法，证明了该方法在数据受限场景下的实用性。
- **计算效率高**：仅需一次前向传播，无需梯度或额外模型，适合大规模模型快速筛选。

### 局限性
- 论文主要验证了数学推理任务（GSM8K、MATH）和CLM任务，在其他领域（如代码、多轮对话、指令遵循）的泛化性尚未明确验证。
- 预算感知策略中的参数（如分位数阈值、加权系数）可能需要针对不同任务或模型进行调整，未提供通用调参指南。
- 实验基于特定规模的模型（如LLaMA），对更大参数规模（如百亿以上）的LLM是否依旧高效且保持性能优势，文中未涉及。
- 仅考虑离线单次筛选，未探索在线迭代筛选或动态预算调整场景。

## 2. Literary Non-Style in LLM-Generated Text

- Source: arxiv
- arXiv ID: 2607.17228
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.17228v1
- PDF: https://arxiv.org/pdf/2607.17228v1
- DOI: https://doi.org/10.48550/arXiv.2607.17228

### Authors

Cory Massaro

### Abstract

Prior work on LLM-generated text has demonstrated quantitative and qualitative departures from text produced by humans. LLM-generated texts differ from human writing in style, resulting in a characteristic textual "feel," while the semantic range of LLMs is much restricted compared to that of humans. In this contribution, I note simple but consistent patterns in the statistical distribution of n-grams within LLM-generated text. Via qualitative analysis of these n-grams, I reveal deficiencies in LLM style. Because higher-order n-grams correlate to semantic content, I conclude that questions of style and semantics are not cleanly separable.

### 中文一句话结论  
本文通过n-gram统计分布分析发现，LLM生成文本在风格上比人类文本更依赖固定短语、多样性更低，且这种风格缺陷与语义局限性密不可分。  

### English TL;DR  
This paper demonstrates that LLM-generated text, compared to human writing, exhibits statistical patterns of reduced n-gram diversity and overreliance on stock phrases, indicating a stylistic deficiency that is intertwined with semantic limitations.  

### 中文详细总结  
已有研究指出LLM文本在风格和语义上均与人类文本存在差异。本文从n-gram的统计分布入手，发现LLM文本的n-gram类型/标记比（type/token ratio）低于人类文本，且Zipf分布中的斜率绝对值更大（尤其在更高阶n-gram中），说明其词汇和短语重复率更高、多样性更差。通过定性分析这些高频n-gram，作者揭示了LLM文本的“风格扁平化”缺陷。由于高阶n-gram与语义内容相关，作者认为风格与语义问题无法截然分开——LLM的短语套用限制了其所能表达的思想范围。  

### 方法 / 贡献  
- **方法**：对1-4阶n-gram进行Zipf分布与Zipf-Mandelbrot拟合分析，计算类型/标记比，并对比是否包含单现词（hapax legomena）及是否经过词形还原（lemmatization）对结果的影响。  
- **贡献**：通过定量统计与定性分析结合，明确指出LLM文本在风格上的不足（高频套语、低多样性）与语义限制紧密相关，而非两个独立问题。  

### 实验或数据  
- **数据集**：  
  - 两个文学作品：《The Inner Life of an AI》（LLM生成，31,147 token）与《The Education of Henry Adams》（人类写作，32,984 token）；  
  - Zachary Grinberg的人类vs.LLM文本语料库（各8,000,005/8,000,010 token）的随机子集。  
- **分析**：计算各语料1-4阶n-gram的类型/标记比；拟合Zipf斜率及Zipf-Mandelbrot参数（k, α, β）；比较去单现词和词形还原前后的差异。  
- **结果示例**：人类文本的4-gram类型/标记比高达0.9890（几乎不重复），而LLM文本仅为0.6882；Zipf斜率绝对值LLM均高于对应人类文本。  

### 值得关注点  
- 风格与语义的不可分性：LLM的固定短语使用习惯不仅造成“文本感觉”差异，还可能限制其表达复杂或新颖思想的能力。  
- 与极端人工文本（如贝克特《无》的4-gram类型/标记比仅0.4179）比较，LLM文本虽有改善但仍显著偏离自然语言模式。  
- 分析同时考虑了n-gram阶数、单现词处理与词形还原，验证了结果的稳健性。  

### 局限性  
- 仅基于n-gram统计和Zipf分布，未涉及句法、篇章结构等更高层风格特征。  
- 数据集局限于英文文本及特定类型的LLM（未指明具体模型版本），结论泛化性需更多语言的验证。  
- 未探讨不同提示策略或温度参数对n-gram分布的影响。  
- 对风格缺陷的“定性分析”可能带有主观性，未进行多评估人交叉验证。

## 3. Team DACTYL at PAN 2026: Bayesian Data Mixing and Empirical X-risk Minimization for AI-text Detection

- Source: arxiv
- arXiv ID: 2607.17382
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.17382v1
- PDF: https://arxiv.org/pdf/2607.17382v1
- DOI: https://doi.org/10.48550/arXiv.2607.17382

### Authors

Shantanu Thorat

### Abstract

Existing research shows that AI-generated text detection classifiers achieve strong in-distribution (ID) performance but do not maintain the same performance on out-of-distribution (OOD) texts, suggesting overfitting to dataset-specific features. However, combining different training datasets doesn't always improve performance and, in some cases, can even encourage shortcut learning. To address this issue, we fine-tune BERT-tiny models with Bayesian classification heads to select texts across three different datasets to use as a consolidated training set. We trained three different classifiers: fine-tuned DeBERTa-V3-large and ModernBERT-large classifiers via empirical X-risk minimization, and an MCGrad model that calibrates the predictions from the ModernBERT-large classifier. The DeBERTa-V3-large-large classifier achieves a mean score of 0.882 on the PAN 2026 test set across five metrics: AUROC, $F_1$, C@1, Brier score, and $F_{0.5u}$. ModernBERT-large achieves a score of 0.96 while MCGrad achieves the best score of the three with a mean score of 0.974, ranking second on the leaderboard. Our results highlight that careful dataset curation can lead to strong OOD performance. We release our ModernBERT-large and DeBERTa-V3-large models at https://huggingface.co/collections/ShantanuT01/panclef-2026 .

### 中文一句话结论
本文提出贝叶斯数据混合与经验X风险最小化方法，通过精细的数据筛选与多分类器集成，在AI生成文本检测的PAN 2026测试集上取得第二名（MCGrad模型平均得分0.974），并显著提升了模型对分布外文本的泛化能力。

### English TL;DR
The paper proposes a Bayesian data mixing and empirical X-risk minimization approach for AI-generated text detection, achieving strong out-of-distribution performance with an MCGrad model scoring 0.974 on the PAN 2026 test set.

### 中文详细总结
现有研究指出，AI生成文本检测分类器在分布内数据上表现优异，但在分布外数据上性能显著下降，表明模型存在过拟合数据集特定特征的问题。简单地混合不同训练数据集不仅不能提升性能，反而可能加剧捷径学习。

针对这一挑战，本文提出结合贝叶斯数据混合与经验X风险最小化的系统方案。研究者首先使用带有贝叶斯分类头的BERT-tiny模型对三个不同数据集的文本进行筛选，从中挑选出适合训练的样本，构建统一的训练集。基于此，训练了三类分类器：基于DeBERTa-V3-large和ModernBERT-large的优化模型（采用经验X风险最小化训练），以及一个基于MCGrad的校准模型。MCGrad模型利用贝叶斯BERT-tiny的不确定性度量（标准差）来校准ModernBERT-large的预测结果。

实验结果显示，DeBERTa-V3-large在PAN 2026测试集上的五项指标平均得分为0.882，ModernBERT-large得分为0.96，而MCGrad模型以0.974的平均分排名第二。结果表明，精心的数据集筛选与多模型集成可以显著提升AI文本检测模型在分布外数据上的泛化能力。

### 方法 / 贡献
- **数据筛选**：引入贝叶斯分类头的BERT-tiny模型，输出每个文本的预测均值（μ）与标准差（σ），基于这些特征从多个候选数据集中筛选训练样本，构建统一的训练集DACTYLv2（扩展原DACTYL数据集，包含博客、网页、Medium文章、电影剧本、NBER摘要、Yelp评论等6个领域，由6种LLM生成）。
- **训练策略**：放弃传统的经验风险最小化，采用经验X风险最小化方法优化两路部分AUROC，通过LibAUC库实现。
- **多分类器集成**：训练三个不同分类器——DeBERTa-V3-large、ModernBERT-large（均通过EXM训练），以及MCGrad模型（利用弱贝叶斯分类器的预测方差作为特征校准ModernBERT-large的输出）。
- **模型开源**：在HuggingFace上发布了ModernBERT-large和DeBERTa-V3-large模型。

### 实验或数据
- **训练数据**：DACTYLv2（共471,858条文本，来自6个领域、8种LLM及人类作者）及外部数据（LLMTrace、Personagen+Stack Exchange、MAGA-Bench、DetectRL）。
- **校准数据**：12个数据集的混合样本（共25,938条文本），采样至每集2,000条，防止大集主导。
- **测试数据**：11个外部数据集的综合评测（包括DACTYL-complete、MAGA-Bench、LLMTrace、BEEMO、CoCONUTS、DetectRL、Dolly-Cosmopedia、OriginalityAI、PAN 2025 Val、Personagen+StackExchange、RealDet、UChicago）。
- **测试指标**：AUROC、F₁、C@1、Brier score、F₀.₅ᵤ五项指标的平均分。
- **实验结果**：MCGrad模型平均得分0.974，ModernBERT-large平均得分0.96，DeBERTa-V3-large平均得分0.882。MCGrad在PAN 2026排行榜排名第二。

### 值得关注点
- **贝叶斯不确定性校准**：利用贝叶斯神经网络输出的标准差作为额外特征来校准主分类器，这一方法极大提升了性能（MCGrad得分0.974对比ModernBERT-large的0.96）。
- **弱模型筛选策略**：仅用4百万参数的BERT-tiny模型（参数量远小于主流模型）即可有效筛选训练数据，显示出弱监督模型在数据质量控制中的潜力。
- **泛化性验证**：在11个独立且多样的测试集上评估，涵盖多种LLM、领域和提示策略，全面验证模型对分布外文本的鲁棒性。
- **实践可用性**：模型已在HuggingFace开放下载，便于社区复现和应用。

### 局限性
- **贝叶斯数据筛选的复杂性**：需要训练多个BERT-tiny模型并运行多次采样以计算（μ, σ），计算成本较高，可能限制大规模数据集上的应用。
- **校准集构建依赖人工**：校准数据的采样和平衡需人工干预，且校准集可能无法涵盖所有OOD场景。
- **模型集成程度有限**：仅对ModernBERT-large进行了MCGrad校准，未尝试在DeBERTa-V3-large或更大模型上应用类似方法，可能未能最大化校准收益。
- **DACTYLv2领域覆盖仍有局限**：数据集仅涵盖6个领域和8种LLM，对于未见过的领域或更新型LLM的泛化能力尚需进一步验证。

## 4. Token-Level Off-Policy Learning for Faithful Generation Under Distribution Shift

- Source: arxiv
- arXiv ID: 2607.17524
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.17524v1
- PDF: https://arxiv.org/pdf/2607.17524v1
- DOI: https://doi.org/10.48550/arXiv.2607.17524

### Authors

Zitong Huang, Gustavo Lucas Carvalho, Deqing Fu, Robin Jia

### Abstract

We propose Token-Level Off-Policy Labeling (TOPL), an off-policy training paradigm that reframes post-training as a token-level correctness prediction task. Our key intuition is that by training the model to distinguish good and bad tokens in a response, we naturally guide the model towards generating good tokens, while avoiding the pitfalls that come with directly training the model to generate off-policy tokens. Experiments on document summarization tasks show that TOPL achieves strong out-of-distribution generalization across 11 datasets against a diverse set of sequence-level and token-level baselines. We further demonstrate that TOPL transfers effectively to machine translation, suggesting that its benefits generalize across different faithful generation tasks. Through ablation studies, we confirm that our token-level learning signal is critical to good performance; sequence-level analogues do not confer similar benefits. Finally, we show that TOPL induces interpretable model updates: the LoRA adapters learned through TOPL function as linear classification heads and steering vectors.

### 中文一句话结论
TOPL 将后训练重构为 token 级别的正确性预测任务，通过区分响应中的好与坏 token，实现了在分布偏移下摘要与翻译任务的强泛化。

### English TL;DR
TOPL reframes post-training as token-level correctness prediction, achieving strong out-of-distribution generalization on summarization and translation tasks by training models to distinguish good and bad tokens.

### 中文详细总结
TOPL（Token-Level Off-Policy Labeling）是一种离策略训练范式，它将后训练建模为 token 级别的二分类正确性预测。核心思想是：通过训练模型区分响应中的正确与错误 token，自然地引导模型生成正确 token，同时避免直接训练模型生成离策略 token 的弊端。在文档摘要任务上，TOPL 在 11 个数据集上取得了最强的跨分布泛化性能，优于多种序列级和 token 级基线。该方法还能有效迁移到机器翻译任务，表明其收益适用于多种忠实生成任务。消融实验证实 token 级学习信号是关键，序列级对应方法不能带来类似收益。此外，TOPL 产生的 LoRA 适配器具有可解释性，可充当线性分类头和引导向量。

### 方法 / 贡献
1. 提出 TOPL，一种将后训练重构为 token 级别正确性分类的新型离策略方法，在文本生成任务中相对于序列级和 token 级基线均取得强的跨分布性能。  
2. 对 TOPL 的有效性进行了分析，将其与条件引导向量的联系作为解释假设。

### 实验或数据
- 主实验在文档摘要上进行，使用 FAVA 数据集（提供 token 级扰动）作为训练数据，在 AggreFact 的 11 个数据集上进行跨分布评估。  
- 采用 Bespoke-MiniCheck-7B 评估生成摘要的事实一致性，报告句子级和全文级得分。  
- 对比基线包括 SFT、DPO、序列级 SOPL、Token-Level DPO、TLDR 和 Unlikelihood Training，所有方法均使用 LoRA 秩 4 训练。  
- 背骨模型包括 Qwen3-8B、Llama-3.1-8B 和 Gemma-3-4B。  
- 额外实验验证 TOPL 可迁移至机器翻译。

### 值得关注点
- TOPL 在多个背骨模型上均取得最佳平均跨分布性能，且收益不能简单归因于生成更短的摘要。  
- token 级学习信号至关重要，序列级对应目标（SOPL）不产生类似收益。  
- 学到 LoRA 适配器具有可解释性：LoRA-A 充当事实性分类器，LoRA-B 作为引导向量，通过调整其贡献可控制事实性。  
- 方法简洁，避免在线采样的复杂性，且与现有 LoRA 轻量训练兼容。

### 局限性
论文未明确讨论局限性。从方法设计看，TOPL 需要具备 token 级扰动标签的训练数据（如 FAVA），此类数据可能不容易在所有任务或领域中获取。此外，二分类目标可能无法捕捉复杂的事实性错误模式，且其有效性与所选中间层和 LoRA 参数有关。

## 5. It's Not What You Say, It's How You Say It: Evaluating LLM Responses to Expressions of Belief

- Source: arxiv
- arXiv ID: 2607.18232
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.18232v1
- PDF: https://arxiv.org/pdf/2607.18232v1
- DOI: https://doi.org/10.48550/arXiv.2607.18232

### Authors

Kevin Du, Clara Kümpel, Michelle Wastl, Alex Warstadt

### Abstract

Users frequently express their beliefs to large language models (LLMs). In some situations, the LLM should accept these contextual beliefs as true. In others, they should stick to their prior knowledge. Notably, users' expressions of belief (EoBs) can take linguistically diverse forms - using presuppositions, evidential and certainty markers, or varied tones - each of which may have a different persuasiveness over the LLMs. We introduce a typology to systematically evaluate how different EoBs affect whether models follow context versus prior knowledge. The typology is grounded in four linguistically motivated dimensions: form, evidentiality, epistemic stance, and tone, spanning 17 fine-grained types. By pairing these EoBs with world knowledge facts, we generate controlled EoB-query pairs that isolate the effect of linguistic variation. Using this benchmark, we evaluate 16 LLMs that differ in architecture (Llama3, Qwen3, Gemma3), scale (1B-30B parameters), and training stages (base vs instruct). We identify meaningful variations in response behavior across these axes, e.g., that bigger models and instruction models tend to be less context-following than smaller models and base models. We further identify specific EoBs that statistically significantly persuade LMs more consistently than others. Our work reveals systematic patterns in how linguistic framing affects LLM context integration, with implications for prompt engineering and model robustness.

### 中文一句话结论
大型语言模型对用户信念表达的语言形式（如命令式、儿童语气）高度敏感，不同表达方式显著影响模型是遵循上下文还是依赖先验知识，且更大模型和指令微调模型更倾向于不跟随上下文。

### English TL;DR
This paper introduces a linguistically-grounded typology and benchmark (EoBench) to systematically evaluate how different linguistic forms of expressing beliefs (e.g., presuppositions, imperative forms, tones) affect whether large language models follow contextual information versus their prior knowledge, revealing systematic patterns such as larger and instruction-tuned models being less context-following.

### 中文详细总结
用户与大型语言模型交互时经常表达自身信念，模型有时应接受这些上下文信息为真，有时则应坚持其先验知识。用户信念的表达方式（EoBs）在语言学上多样，如预设、证据性标记、确定性标记、语气等，可能对模型产生不同说服力。本文提出了一个基于语言学的分类体系，涵盖四个维度：形式（如显式断言、预设、命令式、疑问式等）、证据性（如权威引用、信念报告）、认知立场（强/弱确定性）和语气（正式、儿童导向等），共19种细分类别。基于此，作者构建了EoBench基准，通过将EoB与世界知识事实配对，生成约66,000个受控EoB-查询对，以隔离语言变异的影响。评估了16个LLM，涵盖不同架构（Llama3, Qwen3, Gemma3）、规模（1B-30B参数）和训练阶段（基础模型 vs. 指令微调模型）。主要发现：更大模型和指令微调模型比小模型和基础模型更不倾向于跟随上下文；某些EoB（如命令式、正式语气、权威引用、儿童导向语气）统计上显著更具说服力，而反事实、信念报告和弱认知立场则说服力较弱。该工作揭示了语言框架如何系统性地影响LLM的上下文整合，对提示工程和模型鲁棒性评估有重要启示。

### 方法 / 贡献
**方法**：基于语言学理论（形式、证据性、认知立场、语气四个维度）构建EoB分类体系，程序化生成受控数据，将不同EoB与相同事实内容配对，隔离语言形式影响。使用EoBench基准评估16个LLM，通过统计显著性分析比较不同EoB类型的说服力以及模型规模、架构、训练阶段的影响。

**贡献**：1) 提出首个系统性的语言学分类体系来评估LLM对信念表达的反应；2) 构建公开基准EoBench（约66,000个样本）；3) 发现模型规模、架构、指令微调对上下文跟随性的系统影响；4) 识别出特定EoB类型（如命令式、儿童语气）具有统计显著的说服力；5) 为提示工程和模型鲁棒性评估提供指导。

### 实验或数据
**数据**：EoBench基准，包含约66,000个受控EoB-查询对，每个样本由一个EoB（如“巴黎是法国的首都”）和一个查询（如“法国的首都是什么？”）组成，EoB与模型先验知识冲突（例如正确知识为“巴黎是首都”，但EoB声称“伦敦是首都”）。涵盖19种EoB类型，每种类型多个实例。

**实验**：评估16个LLM，包括Llama3、Qwen3、Gemma3三种架构，参数规模从1B到30B，每个架构包含基础版本和指令微调版本。测量模型在EoB上下文下输出与上下文一致（即遵循EoB）还是与先验知识一致的答案。使用统计检验（如FDR校正）比较不同EoB类型对模型行为的差异。

### 值得关注点
1. 反直觉发现：更大模型和指令微调模型更不倾向于跟随上下文，可能意味着对齐训练增强了模型对先验知识的依赖。
2. 特定EoB类型（如命令式“记住……”、儿童导向语气“亲爱的，……”、正式语气和权威引用）具有统计显著更强的说服力，类似人类中的说服策略。
3. 该工作桥接语言学与AI安全，提醒提示工程和模型部署需关注用户表达方式对输出的潜在操纵。
4. 公开基准EoBench可用于评估模型对语言框架的鲁棒性，尤其针对对抗性输入或误导性上下文的场景。

### 局限性
1. 数据集为合成生成，可能无法完全覆盖真实用户自然表达中的多样性和复杂性，生态效度有限。
2. 仅评估了知识冲突场景，未涉及其他类型信念（如主观意见、偏好）或任务（如推理、创作）。
3. 评估限于特定模型家族（Gemma、Llama、Qwen）和英语，对跨语言、其他架构或更大规模模型的泛化性未知。
4. 未深入分析模型内部机制，仅观察行为模式，无法解释为何某些EoB更具说服力。

## 6. OpenLanguageModel: Readable and Composable Small-Language-Model Pretraining for Education and Research

- Source: arxiv
- arXiv ID: 2607.16669
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.16669v1
- PDF: https://arxiv.org/pdf/2607.16669v1
- DOI: https://doi.org/10.48550/arXiv.2607.16669

### Authors

Tavish Mankash, Vardhaman Kalloli, Keshava Prasad, Deepan Muthirayan

### Abstract

OpenLanguageModel (OLM) is an open-source PyTorch library for building and pretraining small language models while keeping their machinery visible. In OLM, model code reads like the architecture: components are ordinary modules, while Block, Residual, Repeat, and Parallel describe how they are wired. The resulting model can move unchanged from a teaching notebook to a complete pretraining run or a research ablation. OLM connects this readable model layer to tokenizers, local and streaming datasets, optimization, mixed precision, callbacks, checkpoints, and hardware-aware CPU, single-GPU, and single-node multi-GPU execution. We demonstrate the full path by tracing GPT-2 from diagram to code, launching a FineWeb-Edu training script, replacing one attention component, and letting AutoTrainer configure the available machine. The package includes 27 presets across nine familiar model families and documentation that progresses from LM fundamentals to architecture research. Validation shows close agreement with independent reference implementations, 90.6% four-GPU weak-scaling efficiency for a 348M-parameter workload, compact architecture edits, and positive early usability results. OLM is MIT-licensed and available through PyPI, GitHub, and its documentation site.

### 中文一句话结论
OpenLanguageModel 是一个开源 PyTorch 库，旨在通过可读、可组合且硬件感知的代码设计，将小语言模型的构建与预训练流程统一起来，服务于教育、实践和研究场景。

### English TL;DR
OpenLanguageModel (OLM) is an open-source PyTorch library that unifies the construction and pretraining of small language models through readable, composable, and hardware-aware code, serving education, practice, and research.

### 中文详细总结
OpenLanguageModel (OLM) 是一个基于 PyTorch 的开源库，专门用于构建和预训练小型语言模型。其核心设计理念是“代码即架构”：通过 `Block`、`Residual`、`Repeat`、`Parallel` 等普通 PyTorch 模块来直接描述模型的结构化连接，使得模型代码的阅读方式与架构图完全一致。这使得同一个模型对象可以从教学用的 Jupyter Notebook 无缝迁移到完整的预训练任务或科研消融实验中。

OLM 不仅提供了可读的模型层，还整合了完整的预训练工具链，包括分词器、本地/流式数据集、优化器、混合精度训练、回调函数、断点续训以及对 CPU、单 GPU 和单节点多 GPU 的硬件感知支持。论文通过完整的示例展示了其工作流：从 GPT-2 的架构图到代码实现，启动 FineWeb-Edu 训练脚本，将一个注意力组件替换为另一个（如 ALiBi），并利用 `AutoTrainer` 自动适配硬件配置进行训练。

该库目前已包含 9 个知名模型家族的 27 个预设配置，并配有从 LM 基础到架构研究的渐进式文档。验证结果显示，其输出精度与独立参考实现高度一致（最大 logit 差异约 3.58e-7），在 3.48 亿参数模型上实现了 90.6% 的四卡弱扩展效率，并且架构编辑代码非常简洁。OLM 采用 MIT 许可协议，可通过 PyPI、GitHub 及其文档网站获取。

### 方法 / 贡献
-   **可读且可组合的模型定义**：使用 `Block`、`Residual`、`Repeat`、`Parallel` 等组合子来定义模型结构，使 PyTorch 代码直接反映架构图，易于理解和修改。
-   **端到端的预训练集成**：将可读模型层与完整的数据、优化、训练、硬件适配（`AutoTrainer`）工具链连接，实现从教学到科研的无缝衔接。
-   **清晰的模型工厂与预设**：提供了 9 个主流模型家族的骨架和 27 个预设参数，方便用户开箱即用或作为修改起点。
-   **渐进式文档体系**：文档设计遵循从基础原理到前沿研究的路径，且教学和科研使用的代码路径是同一套，降低了学习曲线。

### 实验或数据
-   **数值精度验证**：使用独立 Hugging Face 实现的权重，在 4 层 GPT-2、Llama 3、Qwen 2.5 模型上进行 FP32 推理验证。最大绝对 logit 差异为 3.576e-7，最大损失差异为 4.768e-7，梯度余弦相似度超过 0.9999999999998。
-   **弱扩展效率**：在一个 348,447,744 参数的 Llama-3 模型上，使用 BF16 精度和 DDP 在 A100-80GB GPU 上进行弱扩展测试。单卡、双卡、四卡的每GPU吞吐量分别为17,785、32,426、64,427 tokens/s，四卡弱扩展效率为 90.6%。
-   **架构编辑成本**：实现了 6 种下游编辑任务（如并行残差、混合专家等），与现有工具（LitGPT, Pico）相比，OLM 的新增代码行数更少。
-   **用户调研**：对 20 名用户进行脱敏调查，平均系统可用性量表 (SUS) 得分为 73.8。
-   **论文未明确提及实验所采用的具体数据集名称（除FineWeb-Edu示例外）和详细参数配置。**

### 值得关注点
-   **代码可读性与可转移性**：模型代码本身就是架构的精确描述，且同一份代码可以不加修改地用于教学演示、完整训练和科研修改。
-   **硬件感知的 AutoTrainer**：`AutoTrainer` 能自动检测 GPU 数量和内存，并选择 DDP 或 FSDP 策略，极大降低了分布式训练的配置门槛。
-   **丰富的预设与组件库**：内置 9 个主流模型家族的 27 个预设，并提供了可替换的注意力（如 GQA, ALiBi, RoPE）、前馈（如 SwiGLU, MoE）等独立组件，便于进行模块级研究。

### 局限性
-   **验证范围有限**：数值精度的验证仅使用了简化的模型；GPU 扩展性研究仅基于 DDP 和单节点 A100，未涉及 FSDP 和多节点训练。
-   **编辑成本指标单一**：用“新增脚本行数”作为架构编辑成本的代表，忽略了实际编写和调试时间。
-   **用户调研样本量小且非随机**：20 人的用户调研属于早期便利样本，其评分不能代表整个 LM 社区的普遍体验。
-   **缺乏大规模预训练质量验证**：论文主要验证了工具的正确性和效率，并未提供在标准基准上的大规模预训练模型性能评估。

## 7. Large Language Models for Citation Function Classification

- Source: arxiv
- arXiv ID: 2607.17738
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.17738v1
- PDF: https://arxiv.org/pdf/2607.17738v1
- DOI: https://doi.org/10.48550/arXiv.2607.17738

### Authors

Daniel Vodička, Jakub Šmíd, Pavel Král, Christophe Cerisara

### Abstract

Citation function classification plays a crucial role in understanding the relationships between scientific publications and advancing bibliometric analysis. This study presents one of the first comprehensive evaluations of multiple state-of-the-art (SOTA) large language models (LLMs) for citation function classification, achieving new SOTA results on the ACL-ARC dataset. We systematically compare five models (Mistral 7B, Orca 2-7B, LLaMA 3.1-8B, Falcon 7B, and SciBERT) across zero-shot, few-shot, and fine-tuning approaches. Our fine-tuned Falcon 7B model achieves a 73.3% macro F1 score on ACL-ARC, representing a significant improvement over previous methods. Additionally, we introduce AC3, a novel dataset featuring a seven-category annotation scheme that distinguishes between neutral acknowledgments and explicit evaluative stances (more opinion-oriented citations - criticizing, complimenting, contradicting). The dataset is implemented across four context extraction variants to systematically evaluate the impact of contextual scope on classification performance. We also provide detailed analysis of model performance, experimental configurations, and limitations to guide future research in this domain. To our knowledge, this is one of the first studies dedicated to comprehensive model comparison for citation function classification, addressing a gap identified in recent surveys.

### 中文一句话结论  
本研究系统评估了五种大语言模型在引文功能分类任务上的表现，微调后的 Falcon 7B 在 ACL-ARC 数据集上达到 73.3% 的宏 F1 值，刷新了该任务的最优结果，并发布了包含七类标注体系的新数据集 AC³。  

### English TL;DR  
This study systematically evaluates five large language models for citation function classification. Fine-tuned Falcon 7B achieves a 73.3% macro F1 score on the ACL-ARC dataset, setting a new state-of-the-art. The authors also introduce the AC³ dataset, which uses a seven-category scheme to distinguish neutral acknowledgments from explicit evaluative stances (e.g., criticizing, complimenting, contradicting).  

### 中文详细总结  
该工作针对引文功能分类这一任务，首次对多种主流大语言模型进行了全面比较。研究选用了五个模型：Mistral 7B、Orca 2-7B、LLaMA 3.1-8B、Falcon 7B 以及 SciBERT（作为基于编码器的基线）。实验在零样本、少样本和微调三种范式下进行，微调仅在 ACL-ARC 数据集上进行。结果显示，微调后的 Falcon 7B 以 73.3% 的宏 F1 值超过了此前所有方法，成为新的最先进模型。此外，作者构建了 AC³ 数据集，包含 530 条从多个 ArXiv 学科领域人工标注的引文，

## 8. KyrgyzLLM-Bench: Benchmarking Kyrgyz Language Understanding

- Source: arxiv
- arXiv ID: 2607.17173
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.17173v1
- PDF: https://arxiv.org/pdf/2607.17173v1
- DOI: https://doi.org/10.48550/arXiv.2607.17173

### Authors

Timur Turatali, Aida Turdubaeva, Rustem Izmailov, Anton M. Alekseev, Sergey I. Nikolenko

### Abstract

Evaluating large language models (LLMs) across languages remains challenging, as most multilingual benchmarks rely on translated English datasets, often obscuring linguistic and cultural specificity in the target language. This issue is particularly pronounced for less-resourced languages such as Kyrgyz, where reliable natively authored evaluation data are scarce. Building on previously introduced Kyrgyz-language evaluation datasets, this work reports the first systematic and large-scale evaluation of LLMs in Kyrgyz using the KyrgyzLLM-Bench benchmark suite. KyrgyzLLM-Bench comprises two natively authored datasets$-$KyrgyzMMLU and KyrgyzRC$-$together with carefully translated and manually post-edited versions of WinoGrande, HellaSwag, BoolQ, and TruthfulQA. We evaluate 26 open- and closed-source LLMs under zero-shot and few-shot settings, analyzing model performance, cross-lingual transfer, and the impact of translation artifacts on evaluation reliability. Across families and tasks, model rankings transfer broadly from English to Kyrgyz on WinoGrande and BoolQ, and to a lesser extent on MMLU, while HellaSwag exhibits a substantial English-Kyrgyz performance gap consistent with translation-induced plausibility shifts. Few-shot prompting improves several open-source models on reading comprehension but behaves inconsistently for proprietary models on translated tasks. We publicly release all datasets, evaluation code, and per-model results, and integrate the Kyrgyz tasks into a widely used multilingual evaluation framework to support future research on Kyrgyz NLP.

### 中文一句话结论
KyrgyzLLM-Bench 是首个系统评估大语言模型在吉尔吉斯语上表现的基准套件，包含本地原创与人工后编辑的翻译数据集，揭示了跨语言迁移模式与翻译伪影的影响。

### English TL;DR
KyrgyzLLM-Bench provides the first systematic large-scale evaluation of LLMs in Kyrgyz using natively authored and translated datasets, revealing cross-lingual transfer patterns and the impact of translation artifacts.

### 中文详细总结
本工作提出了 KyrgyzLLM-Bench，一个用于评估大语言模型（LLM）在吉尔吉斯语上理解能力的基准套件。它包括两个本地原创数据集——KyrgyzMMLU（7,977 道多选题，基于吉尔吉斯国家教育课程）和 KyrgyzRC（400 道阅读理解题，基于真实文本），以及四个经过人工后编辑的翻译版英语基准（WinoGrande、HellaSwag、BoolQ、TruthfulQA）。研究评估了 26 个开源与闭源 LLM 在零样本和少样本设置下的表现，分析了模型性能、跨语言迁移以及翻译伪影对评估可靠性的影响。结果表明：模型在 WinoGrande 和 BoolQ 上的排名从英语到吉尔吉斯语大致保持；HellaSwag 因翻译导致的情节合理性变化，英语与吉尔吉斯语间存在显著性能差距；少样本提示能提升部分开源模型的阅读理解能力，但对闭源模型在翻译任务上的表现影响不稳定。所有数据集、评估代码和模型结果均已公开发布。

### 方法 / 贡献
1. **本地原创数据集**：KyrgyzMMLU 基于吉尔吉斯国家教育考试（GRT）材料，涵盖 8 门文化科目及医学，共 7,977 道题，由领域专家审核。KyrgyzRC 包含 400 道基于百科、新闻、文学和数学文本的阅读理解题。
2. **翻译后评估**：对 WinoGrande、HellaSwag、BoolQ 和 TruthfulQA 进行翻译并人工后编辑，保证语言和文化适配。
3. **大规模评估**：在零样本和少样本设置下评测 26 个 LLM，首次系统分析英-吉跨语言迁移及翻译伪影影响。
4. **开放资源**：公开发布数据集、评估代码及每模型结果，并集成至 Lighteval 框架。

### 实验或数据
- **模型**：26 个开源与闭源 LLM，包括 GPT-4o、Claude 3.5、Llama 3、Mistral 等。
- **任务**：KyrgyzMMLU（多学科选择题）、KyrgyzRC（阅读理解）、WinoGrande、HellaSwag、BoolQ、TruthfulQA 的吉尔吉斯语版本。
- **设置**：零样本和少样本（2-shot、5-shot）。
- **结果**：
  - WinoGrande 和 BoolQ 上的模型排名从英语到吉尔吉斯语大致保持；MMLU 上迁移较弱。
  - HellaSwag 中英-吉性能差距显著，归因于翻译导致的合理性偏差。
  - 少样本提示提升部分开源模型（如 Llama 3）的阅读理解，但对闭源模型（如 GPT-4o）不稳定。

### 值得关注点
- 首次大规模系统评估 LLM 在吉尔吉斯语上的表现，包含本地原创数据集，避免单纯依赖翻译数据。
- 明确了翻译伪影（尤其在 HellaSwag 中）对跨语言评估可靠性的影响。
- 开源所有资源，推动低资源语言 NLP 研究。

### 局限性
- 翻译版数据集（WinoGrande 等）虽然经过人工后编辑，仍可能保留部分翻译伪影。
- KyrgyzMMLU 使用学校考试题，可能不全面代表日常或专业领域的语言使用。
- 评估限于现有 LLM，未涵盖未来模型或特定微调方法。
- 少样本结果稳定性不足，尤其对闭源模型，提示数影响尚未深入分析。

## 9. Tokenizing Crosslingual Homographs

- Source: arxiv
- arXiv ID: 2607.17689
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.17689v1
- PDF: https://arxiv.org/pdf/2607.17689v1
- DOI: https://doi.org/10.48550/arXiv.2607.17689

### Authors

Rotem Brillant, Yuval Pinter

### Abstract

Multilingual language models rely on shared subword vocabularies to represent multiple languages within a limited number of token units. While such sharing is often useful, it can also create cases in which identical surface forms are treated too uniformly across languages, even when their meanings or usage differ. We investigate this limitation through cross-lingual homographs and false friends, and examine whether introducing language information earlier in the tokenization process can improve their treatment. We propose a simple tokenizer-level intervention based on language cues: language-specific characters replacing initial characters of shared-vocabulary words, reducing common identity during vocabulary construction. In intrinsic analysis, we find through tokenizer-level statistics that BPE and UnigramLM often treat cross-lingual homographs in a largely language agnostic way, whereas the context-sensitive SaGe tokenizer diverges more strongly; our intervention removes this gap. In downstream English-to-X machine translation, our cues yield modest improvements in several settings, especially under BPE, although the effect is not consistent across all languages and evaluation sets. Overall, the findings suggest that adding lightweight language information at the tokenizer level is a promising direction for further exploration.

### 中文一句话结论
通过在分词器训练中为跨语言同形词注入轻量级语言特定字符，可以部分改善多语言机器翻译中对同形词的处理，但效果在不同语言和评测集上并不一致。

### English TL;DR
The paper proposes adding lightweight language-specific cues to tokenizer training to help distinguish cross-lingual homographs, showing that this intervention can modestly improve multilingual machine translation by making tokenization more language-aware.

### 中文详细总结
多语言语言模型依赖共享子词词汇表来表示多种语言，但这会导致跨语言同形词（包括假朋友）被过度统一处理，即使其含义或用法不同。本文首先通过内在分析发现，BPE和UnigramLM分词器通常以语言无关的方式处理同形词，而上下文敏感的SaGe分词器则表现出更强的语言分歧。作者提出了一种简单的分词器级干预方法：在训练语料中，将同形词的首字符替换为语言特定的Unicode字符，从而在词汇构建阶段引入语言信号。在内在分析中，这种干预使得分词器在跨语言同形词的处理上更接近SaGe的行为；在下游英语到多种语言的机器翻译任务中，该方法在BPE设置下普遍带来小幅提升，但在UnigramLM下效果不稳定，且并非所有语言和评测集都一致获益。总体而言，该研究为在分词器层面引入轻量语言信息提供了初步证据。

### 方法 / 贡献
- **方法**：为每个语言对构建同形词集合，在训练分词器前将语料中同形词的首字符替换为语言特定的Unicode字符（每个小写字母对应一个唯一字符），从而在不破坏可恢复性的前提下强制分词器区分不同语言中的同形形式。
- **贡献**：提出了一种轻量级、无需修改模型架构的分词器干预策略，首次系统评估了在分词阶段引入语言信号对跨语言同形词处理的影响，并验证了其在机器翻译中的潜在价值。

### 实验或数据
- **内在分析**：使用假朋友数据集（Aari1995、Wiktionary）和全语言同形词数据集（Altun），对比BPE、UnigramLM和SaGe分词器在单语与多语设置下对同形词的分词一致性，通过Earth Mover's Distance和分类统计量评估。
- **下游任务**：在OPUS-100和FLORES+数据集上评估英语到德语、法语、意大利语等语言的机器翻译，使用8k词汇量的共享子词模型，基线模型与加入语言线索的模型对比，评价指标为BLEU，并额外构建了同形词聚焦子集。
- **语言模型**：训练小规模GPT模型，比较基线和有线索分词器下的token级和词级困惑度。

### 值得关注点
- 干预方法简单且可逆：字符替换仅发生在同形词首字母，其他字符仍可跨语言共享。
- 内在分析显示，BPE和UnigramLM对同形词的分词高度语言无关，而SaGe自然产生更多分歧；引入语言线索后，BPE和UnigramLM的分歧度接近SaGe，表明方法有效。
- 在机器翻译中，BPE设置下多数语言对（如英→法、英→意）在OPUS-100和FLORES+上均获得小幅BLEU提升，同形词子集上提升更明显。
- 词级困惑度未稳定改善，提示该方法可能主要影响分词粒度而非语言建模能力。

### 局限性
- 机器翻译提升幅度有限，且并非所有语言（如英→德在OPUS-100上基线更强）和评测集（UnigramLM下部分结果退化）一致获益。
- 词级困惑度未改善，表明语言线索可能未带来更优的语言建模。
- 实验仅覆盖英语到少数目标语言，且仅验证了机器翻译任务，泛化性需进一步验证。
- 同形词集合构建依赖字符长度和频率过滤，可能遗漏重要低资源同形词。

## 10. When a Name Is Not a Name: A Benchmark Dataset and Distilled Reasoning for Culturally Entangled Bangla Homographs in Low-Resource LLMs

- Source: arxiv
- arXiv ID: 2607.17828
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.17828v1
- PDF: https://arxiv.org/pdf/2607.17828v1
- DOI: https://doi.org/10.48550/arXiv.2607.17828

### Authors

Md. Asaduzzaman Shuvo

### Abstract

Many Bangla words are at once personal names and culturally loaded common nouns, "Maya" is both a girl's name and a word for affectionate compassion. Choosing the right reading demands cultural knowledge that is scarce in the pretraining data of modern language models. We introduce Culturally Entangled Homograph (CEH) disambiguation and build a Bangla benchmark of 1,516 expert-verified sentences (3,032 labelled occurrences) in which one word appears twice with two distinct readings, each labelled with a culturally grounded category and an explanation of the reasoning behind it. Across open- and closed-source models, we find a systematic dominant-meaning bias: models default to the common-noun sense and overlook the name. A Bangla-specific model fails under every prompting regime we test, showing that language-specific pretraining alone does not confer cultural grounding. We further show that contrastive chain-of-thought prompting can sharply reduce this bias without training, and that distilling cultural explanations teaches small (1-3B) models to reason toward the correct reading rather than memorise labels, cutting dominant-meaning bias from as high as 100% to under 5% and turning the failed Bangla-specific model into our strongest system. Dataset and code are available at https://github.com/ashuvo25/BanglaCEH.

### 中文一句话结论
本文针对孟加拉语中“既是人名又是文化负载普通名词”的文化纠缠同形词（CEH）问题，构建了1516句专家验证的基准数据集，发现大语言模型普遍存在“主流含义偏置”（默认取普通名词义），并通过对比思维链提示和知识蒸馏将小模型（1-3B）的偏置从近100%降低至5%以下。

### English TL;DR
This paper introduces the Culturally Entangled Homograph (CEH) disambiguation problem for Bangla, where a word serves as both a personal name and a culturally loaded common noun. It builds a benchmark of 1,516 expert-verified sentences (3,032 labeled occurrences) and finds that LLMs exhibit a dominant-meaning bias (defaulting to the common-noun sense). Contrastive chain-of-thought prompting and knowledge distillation of cultural reasoning into small (1–3B) models reduce this bias from nearly 100% to under 5%.

### 中文详细总结
- **任务定义**：提出“文化纠缠同形词”（CEH）消歧任务，即同一个孟加拉语词在同一句子中出现两次，一次为人名、一次为文化概念（如情感、精神等），需模型根据文化常识区分。
- **数据集**：构建包含1516个句子（3032个标注词例）的基准，每个用例包含两个词例的标签（6类：名字、概念、情感、情绪状态、集体状态、精神）及文化推理解释。数据由多个大模型生成并经交叉验证和两位母语者人工审核。
- **发现**：在开源和闭源模型上存在系统性“主流含义偏置”——模型默认将两个词例都判为普通名词义，忽略人名义。一个专为孟加拉语训练的模型在所有提示策略下均失败，说明仅语言预训练不足以赋予文化根基。
- **缓解方法**：
  - 对比思维链（C-CoT）提示：强制模型对每个词例先论证两种可能的含义再决策，无需训练即可显著降低偏置。
  - 知识蒸馏：将教师模型（大模型）的文化推理解释蒸馏到小模型（1-3B），使模型学会推理而非记忆标签，将偏置从最高100%降至5%以下，并使原本失败的孟加拉语模型成为最强系统。

### 方法 / 贡献
- **形式化定义**：首次提出CEH消歧任务，作为衡量模型文化根基的诊断工具。
- **基准数据集**：发布1516句孟加拉语CEH基准，含词级文化类别和文化推理解释。
- **评估与发现**：在零样本、少样本、C-CoT、知识蒸馏四种设置下评估多个模型，揭示主流含义偏置及孟加拉语专用模型的失败。
- **缓解策略**：提出对比思维链提示（无需训练）和知识蒸馏（将文化推理压缩到小模型），有效降低偏置。

### 实验或数据
- **数据**：1516个句子（3032个词例），由Claude Fable 5、Kimi K3、Gemini 3.5 Flash生成，经交叉模型验证和两位母语者人工审核。标签分布：名字（1153）、概念（985）、情绪状态（345）、集体状态（202）、精神（187）、情感（160）。
- **实验**：在零样本、少样本、C-CoT、知识蒸馏（使用LoRA微调）四种条件下测试模型（包括开源和闭源模型，及一个孟加拉语专用模型）。评价指标为主流含义偏置率（模型默认取普通名词义的比例）。所有实验在相同测试集（10%数据）上进行。

### 值得关注点
- **任务新颖性**：CEH不同于传统词义消歧，要求模型区分文化纠缠的人名与概念，是检验模型文化根基的敏锐诊断工具。
- **偏置的普遍性**：所有模型均存在主流含义偏置，且孟加拉语专用模型在全部提示策略下失败，说明语言能力不等于文化能力。
- **缓解效果显著**：C-CoT无需训练即可降低偏置，知识蒸馏则使小模型学会文化推理，偏置从近100%降至5%以下，且将失败的孟加拉语模型逆转为最强系统。

### 局限性
- **数据覆盖**：词项选择依赖单一母语者的命名知识，可能遗漏部分常见CEH词，导致覆盖范围受限。
- **语言限制**：仅针对孟加拉语，其他语言中的文化纠缠同形词尚未验证，结论的泛化性未知。
- **评估规模**：基准为1516句，对于鲁棒性评估而言规模较小，且测试集仅占10%，可能影响统计显著性。
- **蒸馏依赖大模型**：知识蒸馏需要高质量教师模型（如Claude、Kimi等），在完全无监督环境下可能不可行。

## Processing Notes

- Duplicate papers skipped: 0