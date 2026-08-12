# Daily arXiv - 2026-08-12

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-12T23:09:16
- Paper count: 10

## 1. Every Token Counts: Exact Likert-Scale Distributions for Measuring LLM Attitudes and Biases

- Source: arxiv
- arXiv ID: 2608.10503
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2608.10503v1
- PDF: https://arxiv.org/pdf/2608.10503v1
- DOI: https://doi.org/10.48550/arXiv.2608.10503

### Authors

Davood Wadi, Mohsen Ghodrat, Matthew Philp

### Abstract

As Large Language Models (LLMs) are increasingly deployed as autonomous agents, accurately evaluating their latent values and biases is critical. The NLP community typically evaluates models using large, unstructured benchmarks. While effective for general capabilities, these datasets fundamentally conflate causal mechanisms: even when an aggregate bias is detected, unstructured evaluations cannot disentangle whether it stems from baseline traits, contextual confounders, or complex interactions. To address this, we introduce an analytically exact framework for the controlled behavioral evaluation of LLMs. We bridge human psychometrics with LLM mechanics by resolving gaps in design, measurement, and analysis. First, we replace unstructured prompting with fully crossed factorial experiments to systematically isolate causal main and interaction effects. Second, we eliminate Monte Carlo text sampling noise by operating directly on exact, token-level Probability Mass Functions (PMFs). Third, we derive a multivariate ordinal consensus metric and a distributional ANOVA to process these PMFs analytically. We validate our framework with a case study on consumer ethnocentrism across five LLMs, demonstrating how our approach isolates systemic country-of-origin biases that aggregate benchmarks otherwise obscure.

### 中文一句话结论
本文提出了一个基于精确 token 级概率质量函数的因果实验框架，用于从 LLM 的态度和偏见中解耦出主效应和交互效应，从而避免传统非结构化基准测试中的混杂问题。

### English TL;DR
This work introduces an analytically exact framework for controlled, causal evaluation of LLM attitudes and biases, replacing unstructured benchmarks with fully crossed factorial experiments and operating directly on exact token-level probability mass functions to isolate main and interaction effects without sampling noise.

### 中文详细总结
现有 NLP 评估通常依赖大规模的、非结构化的基准数据集。虽然这些数据集对于衡量通用能力有效，但它们无法区分模型行为是由内在特质、上下文混杂因素还是复杂交互引起的。为此，本文提出了一个精确的分析框架，将 LLM 行为评估形式化为全交叉的因子实验。该框架通过三个关键创新来解决传统评估中的三个核心缺口：（1）设计缺口：用完全交叉实验替代非结构化提示，能够系统性地分离因果主效应和交互效应；（2）测量缺口：直接利用模型在 token 级别的精确概率质量函数（PMF）进行计算，消除了蒙特卡洛文本采样带来的噪声；（3）分析缺口：提出了一种面向有序类的多元共识指标和分布方差分析（分布 ANOVA），以解析精确 PMF。作者通过一个关于五款 LLM 的消费者民族中心主义案例研究验证了该框架，展示了该方法如何隔离出系统性的原产地偏见，而这些偏见在传统的聚合基准测试中是难以区分的。

### 方法 / 贡献
- **方法论核心**：将 LLM 评估形式化为完全交叉的固定效应因子实验，其中模型、目标国家等变量作为独立因子。
- **精确测量**：直接使用 LLM 的精确 token 级概率质量函数（PMF），避免生成文本采样噪声。
- **新指标与统计方法**：
  - 提出针对有序 Likert 尺度的多元共识（multivariate consensus）指标，克服了香农熵无法处理有序性的问题；
  - 推导出分布方差分析（distributional ANOVA），能够计算因果效应（主效应、交互效应）的完整概率分布；
  - 采用基于最优传输的 Hoeffding 分解和形式化的一致性保证。
- **贡献**：提供了一个统一的、确定性的框架，用于在有序心理测量工具上对 LLM 进行因果行为评估，能够将整体偏见分解为基线、主效应和交互效应。

### 实验或数据
作者通过一个关于“消费者民族中心主义”的案例研究验证了该框架，对五款 LLM 进行了评估。实验中采用了成熟的心理测量量表，并将模型（五款）和目标国家（多个）作为交叉因子。实验展示了该方法如何隔离出系统性的原产地（国家）偏见，而这些偏见在传统的聚合基准测试中是模糊不清的。

### 值得关注点
- 该框架一个独特优势在于利用了 LLM 的“无状态”特性——即 LLM 在每个问题之间的内部状态可以被有效重置，消除了人类被试中的“被试内”携带效应。
- 通过直接操作精确概率质量函数（PMF），该框架在理论上实现了对模型内在态度的无偏估计，减少了生成式评估中的常见波动（如“骑墙”现象和提示扰动敏感性问题）。

### 局限性
论文未明确提及具体的局限性。但从方法本身推断，潜在的局限性包括：该框架要求严格的实验设计（全交叉设计）和对 token 级别的精确分析，这可能在面对词汇表巨大或输出格式更复杂（非数字）的任务时带来额外的计算成本或适配挑战。此外，论文主要聚焦于有序 Likert 量表，对于更多样的输出类型（如连续值或非结构化文本）的泛化性可能需要进一步验证。

## 2. EVIL-Detect for NLPCC 2026 Shared Task 6: LLM-Generated Text Detection

- Source: arxiv
- arXiv ID: 2608.10698
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2608.10698v1
- PDF: https://arxiv.org/pdf/2608.10698v1
- DOI: https://doi.org/10.48550/arXiv.2608.10698

### Authors

Hongrui Bao, Hangyu Rong, Zhuoshang Wang, Yubing Ren, Yanan Cao

### Abstract

The rapid development of large language models (LLMs) has increased the need for reliable detection of LLM-generated text, especially in realistic Chinese scenarios involving human-written text (HWT), LLM-generated text (LGT), and LLM-refined text (HLT). This paper presents EVIL-Detect, a multi-signal ensemble framework with conflict-aware fusion for NLPCC 2026 Shared Task 6. The system integrates edit-extent regression, zero-shot likelihood-contrast signals, lexical statistics, and conservative text rules. With calibrated decision boundaries and conflict-aware integration, our system improves robustness under strong out-of-distribution shifts, achieving a macro-F1 score of 0.8888 and ranking first in the official evaluation. Our code is available at https://github.com/bbbbhrrrr/evildetect.

### 中文一句话结论
EVIL-Detect通过融合编辑程度回归、零样本似然对比信号、词汇统计和保守文本规则的多信号集成框架，在NLPCC 2026中文三分类文本检测任务中取得最优性能（Macro-F1=0.8888）。

### English TL;DR
EVIL-Detect is a multi-signal ensemble framework with conflict-aware fusion that integrates edit-extent regression, zero-shot likelihood-contrast signals, lexical statistics, and conservative text rules, achieving a macro-F1 score of 0.8888 and ranking first in the NLPCC 2026 Shared Task 6 for detecting human-written text, LLM-generated text, and LLM-refined text in Chinese.

### 中文详细总结
本工作针对NLPCC 2026共享任务6中的中文文本三分类检测（人工写作HWT、LLM生成LGT、LLM精炼HLT），提出EVIL-Detect框架。核心思路是将HLT视为HWT与LGT之间的连续编辑程度状态，而非独立硬分类。系统整合四个互补信号模块：基于EditLens和Soft-EditLens的监督编辑程度回归（提供连续性分数）、基于EchoPrompt的零样本LGT倾向证据（利用似然对比）、词汇频率统计（提取判别性n-gram模式），以及保守文本规则（如HTML标记检测）。通过校准决策边界和冲突感知融合策略，系统在不同模块信号冲突时依据验证集标定的规则进行裁决，最终在官方评测中取得0.8888 Macro-F1并排名第一。

### 方法 / 贡献
1. **任务重定义**：将HLT视为HWT→LGT连续轴上的中间状态，设计连续编辑程度目标（HWT=0, LGT=1, HLT取决于与原文的距离）。
2. **多信号集成**：包含两个监督编辑程度模块（EditLens基于字符n-gram距离、Soft-EditLens基于语义短语软匹配）、零样本LGT检测（EchoPrompt多分支似然对比）、词汇统计（标签条件概率log-odds）和保守规则。
3. **冲突感知融合**：基于双阈值基标签、Soft-EditLens回归/分桶信号和9维LGT投票面板，设计验证集标定的冲突解决规则，而非简单投票。

### 实验或数据
实验基于NLPCC 2026共享任务6官方数据集（含HWT/LGT/HLT三类的中文文本），评测指标为Macro-F1。系统在testp1上取得0.8888 Macro-F1，排名第一。作为对比，直接使用QLoRA微调分类器仅得0.1690 Macro-F1。代码已开源。

### 值得关注点
1. 任务从二元检测扩展至包含人类精炼文本的三分类，更贴近真实AI辅助写作场景。
2. 创新性将HLT建模为连续编辑程度而非硬分类，与Soft-EditLens的语义级编辑程度估计相结合。
3. 冲突感知融合策略有效处理模块间的预测分歧，特别在HWT/HLT边界案例上表现鲁棒。
4. 保守文本规则作为高精度后处理安全措施（如检测HTML/XML标记）。

### 局限性
全文仅提供摘要和方法概述，未完整展示实验设置细节（如数据规模、分布偏移强度）、消融实验及各模块贡献的量化分析。另外，方法依赖训练集中HWT-HLT配对数据来构建编辑程度目标，对无配对数据的场景可能不适用。

## 3. Evaluation-Conditioned Training: Teaching Models to Generalize to Stronger Oversight Regimes

- Source: arxiv
- arXiv ID: 2608.10209
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.10209v1
- PDF: https://arxiv.org/pdf/2608.10209v1
- DOI: https://doi.org/10.48550/arXiv.2608.10209

### Authors

Alec Harris, Kasey Corra, Archie Chaudhury, Yixiong Hao

### Abstract

Feedback signals used to train Large Language Models (LLMs) are the primary driver of their behavior and our main lever for instilling alignment with human values and objectives. However, a key limitation of current post-training methods is the inability of human annotators and automated reward functions to faithfully capture the feedback we would like to give. We introduce Evaluation-Conditioned Training (ECT), a post-training framework that uses natural language to condition each training sample on the fidelity of the feedback we provide and then elicits the desired behavior by conditioning the LLM on a high-fidelity monitor in deployment. ECT is aimed at improving performance under imperfect feedback and works as an add-on to existing algorithms such as SFT and PPO. We first provide a conceptual framework for ECT and discuss its potential to address persistent sources of reward mis-specification. Then we motivate ECT in the context of the eliciting latent knowledge (ELK) problem. Finally, we evaluate ECT on two proof-of-concept experiments: increasing even-handedness in news article generation and reducing sycophancy on an arithmetic task. In each setting, we utilize imperfect feedback, rewarding bias and agreement with the user, respectively. In both settings, ECT improves the targeted behavior relative to direct training.

### 中文一句话结论
本文提出评估条件训练（ECT），通过训练时用自然语言标注反馈质量、部署时配合高质量评估器，使语言模型能在不完善反馈下泛化到更强监督场景，并在政治中立与减少谄媚两项实验中验证了有效性。

### English TL;DR
Evaluation-Conditioned Training (ECT) uses natural language labels describing feedback fidelity to train LLMs, then conditions on a high-fidelity evaluator at deployment. In two proof-of-concept experiments (political even-handedness via SFT, sycophancy reduction via PPO), ECT outperformed baselines under imperfect rewards.

### 中文详细总结
- **问题**：当前后训练方法依赖人类或自动奖励函数，但这类反馈难以完全捕捉真实意图，导致模型行为与目标偏离（如谄媚、政治偏见）。
- **方法**：ECT是一种可叠加于SFT/PPO的框架。训练时，每条数据附带一个自然语言评价标签（如“强保守”或“易受暗示”），描述当前反馈的保真度；部署时则使用理想评估器标签（如“无偏见”“低暗示”）来引导输出。
- **理论动机**：模型内部可能存有“潜在知识”，但仅在面对更高保真度评估时才被激发。ECT通过显式关联标签与目标行为，使模型学会从弱反馈中分离出与理想评估器对应的策略。
- **实验验证**：在两项小规模实验中，ECT均显著改善目标行为：
  - 政治新闻生成（SFT + Llama-3.1-8B-Instruct）：使用带编辑部偏见的训练数据，ECT将中立度从基线20.8%提升至72.3%（随机标签控制为47.8%）。
  - 算术谄媚减轻（PPO + Qwen2.5-7B-Instruct）：奖励函数偏向同意用户错误答案，ECT使假阳性率从47.9%降至23.3%，同时准确率提高。
- **额外发现**：ECT的标签扫描实验显示，模型在部署时对更强标签（如“UNBIASED”）的响应优于随机标签控制，说明其学会了从训练标签泛化至理想评估器。

### 方法 / 贡献
1. **概念框架**：提出ECT工作流——训练时用自然语言标注反馈保真度，部署时条件化于高保真评价标签，旨在解决系统性的奖励错误（如偏见、谄媚）。
2. **可叠加性**：ECT作为插件兼容现有算法（SFT、PPO），无需改变基础训练流程。
3. **实验贡献**：在政治中立（SFT）和算术谄媚（PPO）两个任务上证明ECT优于直接训练和随机标签控制。
4. **理论连接**：将ECT与弱到强泛化（W2SG）、潜在知识激发（ELK）问题关联，指出模型可利用内部知识修正反馈错误。

### 实验或数据
- **实验1（政治中立）**：
  - 数据：基于Anthropic偏见评估集生成3240对提示，配对四种编辑部视角（强进步/温和进步/温和保守/强保守）的回复。
  - 训练：Llama-3.1-8B-Instruct + LoRA，三种条件：无标签基线、正确ECT标签、随机标签控制。
  - 评估：1350对未见过提示，Claude Haiku 4.5自动评分（中立度、拒绝率、模糊度），5种子。
- **实验2（减少谄媚）**：
  - 数据：一位数加法问题 + 用户候选答案，模型需判断答案正误。奖励函数设计为偏向同意用户（暗示分数s∈[0.5,1.5]训练，s∈[0,0.5)部署）。
  - 训练：Qwen2.5-7B-Instruct + QLoRA + PPO，ECT组附加不暗示级别标签。
  - 评估：9种子的假阳性率（谄媚）和准确率。
- **注意**：自动评估器（Claude）可能与训练目标模型同源，结果需谨慎解释。

### 值得关注点
- **泛化到更强监督**：ECT的核心亮点在于，模型在训练时仅接触弱/中等保真度标签，但部署时通过激发潜在知识，自动适应理想评估器。
- **同时改善多项指标**：实验1中ECT在提升中立度的同时降低了拒绝率；实验2中同时降低假阳性率、提升准确率，说明效果不是简单的权衡。
- **理论基础**：用“简单性偏差”与“系统性错误”区分两种反馈错误场景，并指出ECT针对后者；将ECT与弱到强泛化、潜在知识激发等前沿理论连接。
- **小规模但效应明显**：尽管实验规模有限，但效果量显著（中立度改善超50个百分点，谄媚率减半），值得进一步放大验证。

### 局限性
- **规模与泛化性**：两项实验均为小规模预研，仅在8B级别模型上测试，结论能否推广到更大模型、更复杂任务（如长文本、多轮对话）尚未验证。
- **自动评估器偏见**：实验1的评分由Claude Haiku 4.5完成，训练数据由Claude Sonnet 4.5生成，模型家族相近可能导致吹毛求疵（评分倾向于相似风格），真实人类评估尚缺。
- **与现实对齐问题的距离**：实验使用合成控制反馈（如故意偏袒用户的奖励函数），真实场景中反馈错误类型更复杂，ECT能否处理多种并发错误尚不明确。
- **标签依赖**：ECT需要在训练时提供明确、正确的评价标签，若标签本身不准确或定义模糊，可能影响效果；部署时也需要显式选择理想标签。
- **理论基础未完全实证**：文章对“模型内部存有理想评估知识”的假设（ELK）提出了连接，但并未直接测量内部表示的变化，仅为概念性论证。

## 4. ReLTEx: Reliable LLM-based Taxonomy Expansion

- Source: arxiv
- arXiv ID: 2608.10970
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.10970v1
- PDF: https://arxiv.org/pdf/2608.10970v1
- DOI: https://doi.org/10.48550/arXiv.2608.10970

### Authors

Zeinab Ghamlouch, Mehwish Alam

### Abstract

Recent advances in Large Language Models (LLMs) have demonstrated strong capabilities in generating semantically relevant concepts and relations, making them promising tools for taxonomy enrichment. However, directly relying on LLM-generated expansions often leads to noisy, redundant, or hierarchically inconsistent structures, limiting their reliability for automated taxonomy expansion. In this paper, we present ReLTEx, a framework for reliable LLM-based taxonomy expansion. ReLTEx combines LLM-driven candidate generation with structure-aware validation and recursive expansion control to improve the consistency and quality of generated taxonomies by reducing hallucinations. We evaluate the proposed framework using benchmark taxonomies under a masked taxonomy expansion setting and compare multiple validation strategies. Experimental results, supported by both adapted evaluation metrics and human evaluation, demonstrate that ReLTEx produces more reliable and semantically coherent taxonomy expansions.

### 中文一句话结论
ReLTEx通过结合基于LLM的候选生成、结构感知验证和递归扩展控制，有效减少了幻觉和结构不一致问题，提升了自动本体扩展的可靠性和语义相干性。

### English TL;DR
ReLTEx is a framework that improves the reliability of LLM-based taxonomy expansion by combining candidate generation with structure-aware validation and recursive expansion control to reduce hallucinations and ensure hierarchical consistency.

### 中文详细总结
本论文提出ReLTEx框架，旨在解决直接使用大语言模型进行本体扩展时产生的噪声、冗余和层级不一致问题。ReLTEx包含三个核心阶段：1）基于零样本LLM的候选概念生成，利用本体的层级语境（如根节点路径和现有子节点）引导模型生成语义相关的新概念；2）结构感知验证，训练一个基于DistilRoBERTa的二分类器，通过判断候选父子关系在层级路径中的结构有效性来过滤错误生成，分类器使用正例和多种硬负例（如反转边、兄弟混淆等）进行训练；3）递归扩展控制，利用验证置信度分数设定最小接受子节点数和置信度衰减阈值，避免错误向深层传播。实验在SemEval-2016 Environment和Schema.org本体上进行，采用掩码本体扩展评估协议，结果表明ReLTEx能生成更可靠和语义一致的本体扩展。

### 方法 / 贡献
- 提出零样本LLM驱动的本体扩展框架，利用层级上下文（祖先路径和现有子节点）生成候选概念。
- 设计结构感知验证机制，训练基于DistilRoBERTa的二分类器，通过融合层级路径信息判断父子关系的结构有效性，而非仅依赖语义相似性。
- 引入递归扩展控制策略，基于验证置信度均值和衰减阈值自动终止不可靠分支的扩展。
- 提供了全面的评估协议，包括适应生成场景的评估指标、人工评估和基于LLM的评估。

### 实验或数据
实验使用两个本体基准：SemEval-2016 Task 13 Environment本体（263节点）和Schema.org本体（1,143节点）。采用掩码本体扩展设置，即隐藏部分节点后从剩余种子本体恢复。评估了四种开源LLM：Llama3.2:3B、Mistral:7B、Qwen3:8B和DeepSeek-R1:8B。对比了三种验证策略：语义相似性过滤、LLM验证和分类器验证。实验结果使用适应生成场景的Recall@K、MRR和Wu & Palmer相似度等指标，并进行了消融研究和人工评估。论文未提供完整的数值结果表格文本。

### 值得关注点
- 结构验证分类器使用六种硬负例生成策略（反转边、兄弟混淆、祖孙混淆等），使得模型能学习结构兼容性而非仅语义相似性。
- 递归扩展控制通过置信度均值和衰减阈值，能主动阻止错误在深层本体中的传播。
- 验证机制不依赖预设候选词池，支持开放生成，适应现实动态扩展需求。
- 使用了人工评估和LLM评估两种额外验证方式。

### 局限性
- 结构验证分类器需要预先从种子本体提取正负例进行训练，在完全新的领域可能需重新训练或微调。
- 递归停止阈值（m和δ）需手动设定，可能在不同本体或任务上需要调优。
- 实验仅使用两类本体（SemEval-env和Schema.org），规模和领域覆盖有限，泛化性需进一步验证。
- 论文未提供详细的数值结果表格，仅描述定性结论。
- 依赖于开源LLM，不同模型性能可能存在差异，但未深入分析模型选择的影响因素。

## 5. Interpreting Language Model Hidden States at Scale

- Source: arxiv
- arXiv ID: 2608.10260
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.10260v1
- PDF: https://arxiv.org/pdf/2608.10260v1
- DOI: https://doi.org/10.48550/arXiv.2608.10260

### Authors

Jordan Pettyjohn, Mansi Sakarvadia, Nathaniel Hudson, Daniel McKenzie, Kyle Chard, Ian Foster

### Abstract

Lens methods interpret large language models (LLMs) by mapping intermediate activations to the output vocabulary, revealing how next-token predictions develop through the network. Trained lenses remain expensive: affine-translator parameters grow quadratically with model width, while exact, full-vocabulary Kullback--Leibler (KL) training dominates memory. Consequently, prior trained lenses have been applied to models of at most 20B parameters and remain tied to particular component types. We present OmniLens, which applies a single lens family to any model-width activation, whether residual stream, attention, or MLP, and combines two independent scaling techniques. First, low-rank translators make per-lens parameter growth linear in model width and reduce trainable parameters by up to 98.4%. Second, Subset-KL materializes only selected vocabulary logits: its Top-k mode cuts peak training memory by up to 70%, while its importance-sampled variant retains unbiased stochastic gradients for the full KL. These savings enable a dense ensemble of 482 lenses for LLaMA-3.3-70B, providing 6x the coverage of a residual-stream design at the same depth. Model-wide coverage then reveals what single-component lenses cannot: the components where a behavior is most visible need not be those where intervention is most effective, and the most effective interventions lie outside the attention heads examined by prior lens studies. Across three case studies (prompt-injection detection, multi-hop memory injection, and toxicity localization), OmniLens reproduces key published results at substantially lower cost.

### 中文一句话结论
OmniLens通过低秩翻译器和Subset-KL损失函数，实现了对大型语言模型所有组件（残差流、注意力、MLP）的密集透镜覆盖，大幅降低参数和内存需求，并复现了多个可解释性案例的关键结果。

### English TL;DR
OmniLens introduces low-rank translators and Subset-KL objectives to enable dense, scalable lens coverage of language model hidden states across residual, attention, and MLP components, dramatically reducing parameter and memory costs while matching or surpassing prior interpretability results on models up to 70B parameters.

### 中文详细总结
现有透镜方法受限于参数二次增长（O(d²)）、全词汇KL训练的内存消耗，以及针对特定组件（如残差流或注意力头）的设计，无法应用于20B以上模型。OmniLens提出统一透镜家族，可读取任意宽度的激活（残差流、注意力头、MLP）。其两个核心技术：**低秩翻译器**将每个透镜的参数量从O(d²)降至O(rd)，可训练参数减少最多98.4%；**Subset-KL**目标函数通过Top-k截断（减少70%峰值内存）或重要性采样变体（保持无偏梯度），大幅降低训练内存。这些技术使得在LLaMA-3.3-70B上训练482个透镜的密集集成成为可能，覆盖度是同等深度残差流透镜的6倍。模型级覆盖发现了单一组件透镜无法揭示的现象：行为最可见的组件未必是干预最有效的组件，且最有效的干预位于先前透镜研究未涉及的注意力头之外。在提示注入检测、多跳记忆注入、毒性定位三个案例中，OmniLens以更低成本复现了关键结果。此外，在LLaMA-3.1-405B上运行了8步优化，首次展示了前沿规模模型的可训练性。

### 方法 / 贡献
- **低秩翻译器**：将每透镜参数从O(d²)降至O(rd)（r为目标秩），可训练参数最多减少98.4%。
- **Subset-KL目标函数**：内存高效的KL散度近似，包括Top-k截断（峰值内存减少70%）和重要性采样变体（无偏梯度估计，同时保留全KL的随机梯度）。
- **统一透镜框架**：单一透镜家族可应用于残差流、注意力头、MLP等任意宽度激活，无需针对不同组件设计不同透镜；开源框架包含训练工具、hook点仪器、CUDA内核等。
- **发现**：在70B规模上首次实现密集透镜覆盖，揭示干预有效性不等于可见性的非直观现象。

### 实验或数据
- **模型规模**：在LLaMA-3.3-70B上训练482个透镜（密集集成）；在LLaMA-3.1-405B上运行8步优化（首次此规模的可训练透镜演示）。
- **效率指标**：低秩翻译器使参数减少98.4%；Subset-KL Top-k模式使GPT-2峰值训练内存减少70%。
- **案例研究**：三类任务（提示注入检测、多跳记忆注入、毒性定位）均复现了先前工作的关键结果，成本显著降低。
- **对比基线**：与Tuned Lens（残差流）和Attention Lens相比，覆盖度提升6倍且参数/内存更低。

### 值得关注点
- **规模突破**：首次在近前沿模型（70B）上实现密集透镜训练，且训练成本低于稀疏覆盖。
- **非直观发现**：全组件覆盖揭示行为检测的最佳位置与干预的最佳位置不一致，且有效干预常位于注意力头之外。
- **开源贡献**：提供完整训练框架、CUDA融合内核及子集KL库，便于复现和扩展。
- **灵活性**：单一透镜家族适应所有组件类型，无需设计多套架构。

### 局限性
- **低秩近似能力**：低秩翻译器可能无法完全捕捉高度非线性的中间表示，特别是对于需要高秩变换的复杂特征。
- **Subset-KL偏差与方差**：Top-k模式截断引入偏差；重要性采样变体虽无偏但可能增加梯度方差，影响训练稳定性。
- **405B实验有限**：仅执行8步优化，未提供完整训练曲线或下游分析，其收敛性和实际有效性尚未充分验证。
- **案例覆盖范围**：仅在三类任务上验证，通用解释性能力需更广泛评估。
- **架构依赖**：框架依赖模型特定的归一化和解嵌入结构，迁移到非Transformer架构可能需要重新设计。

## 6. TEAMMix: Taxonomy Enrichment Augmentation and Minority-augmented Mixing Strategy for LLM-enhanced Weak-Supervised Hierarchical Text Classification

- Source: arxiv
- arXiv ID: 2608.11044
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.11044v1
- PDF: https://arxiv.org/pdf/2608.11044v1
- DOI: https://doi.org/10.48550/arXiv.2608.11044

### Authors

Jian Zhang, Zhuohao Yang, Songlin Lei, Bangli Liu, Ziwei Wang, Xufeng Weng, Gehan Amaratunga, Yu Lin, Hongwei Wang

### Abstract

Hierarchical Text Classification (HTC), as a critical text mining task, faces challenges such as complex label hierarchies and class imbalance. Existing methods based on large language models (LLMs) struggle to be efficiently applied to this task due to issues like lengthy prompts and loss of label structural information. To address these limitations, this paper proposes a weakly supervised HTC framework enhanced by LLM-based data augmentation. The framework first enriches the label hierarchy semantically through keyword generation and corpus mining, thereby enhancing the model's understanding of labels. Subsequently, it guides the LLM to generate pseudo-samples to mitigate the long-tail problem, and employs a Gaussian mixture model for confidence-based resampling to optimize the quality of generated data. Experimental results demonstrate that the proposed method effectively improves the reliability of LLM-generated pseudo-labels and significantly enhances classification performance on fine-grained and imbalanced datasets.

### 中文一句话结论
TEAMMix通过利用大语言模型进行标签层次语义增强和伪样本生成，并结合高斯混合模型进行置信度重采样，有效提升了弱监督层次文本分类在长尾分布下的性能。

### English TL;DR
TEAMMix improves weak-supervised hierarchical text classification by using LLMs to enrich label hierarchies with keywords and generate pseudo-samples, coupled with a Gaussian mixture model for confidence-based resampling to handle class imbalance.

### 中文详细总结
该论文针对层次文本分类（HTC）中标签层次复杂、类别分布不均衡等问题，提出了一种基于大语言模型（LLM）增强的弱监督框架TEAMMix。框架首先通过关键词生成和语料挖掘丰富标签层次语义，增强模型对标签的理解；其次，利用LLM生成伪样本来缓解长尾问题，并采用高斯混合模型（GMM）对生成数据进行置信度重采样以优化质量。实验表明，该方法有效提高了LLM生成伪标签的可靠性，并在细粒度、不均衡数据集上显著提升分类性能。

### 方法 / 贡献
- 提出仅需标签名称的LLM增强弱监督HTC策略，通过提示生成判别性关键词并融合语料挖掘的术语，实现标签层次语义增强。
- 引入少数类增强混合采样策略：利用LLM按标签路径生成伪文本，结合GMM进行置信度筛选和重标注，优化伪样本质量。
- 通过基于相似性排名的最大分歧点选择高置信度文本-标签对作为伪标签数据，提升伪标签质量。

### 实验或数据
- 数据集：Amazon-531 (未标记训练29487，测试19865，531个标签) 和 DBPedia-298 (未标记训练196665，测试49167，298个标签)。
- 实验结果：在Amazon-531上Example-F1达0.6331，P@3达0.6276，MRR达0.6656，优于TaxoClass和TELEClass等弱监督基线；在DBPedia-296上Example-F1为0.8536（低于TELEClass的0.8536），MRR为0.8726（略低于TaxoClass的0.8762）。与零样本方法（如ChatGPT）相比全面领先。

### 值得关注点
- 结合LLM生成与语料挖掘的双重增强策略，有效提升细粒度标签的语义表征。
- 利用GMM动态筛选和修正LLM生成伪标签，解决了伪标签可靠性问题。
- 在长尾分布下，少数类增强混合采样显著提升低频类别性能。

### 局限性
- 方法依赖LLM生成的伪样本质量，若LLM对特定领域或罕见类别生成能力不足可能影响效果。
- 实验仅在两个英文数据集上验证，跨语言或中文任务下的泛化性未评估。
- 未探讨不同LLM（如GPT-4 vs. 较小模型）对性能的影响，计算成本分析缺失。

## 7. Data Attribution of Emergent Misalignment with Persona Features

- Source: arxiv
- arXiv ID: 2608.11025
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.11025v1
- PDF: https://arxiv.org/pdf/2608.11025v1
- DOI: https://doi.org/10.48550/arXiv.2608.11025

### Authors

Clemens Vetter, David Kaczér, Lucie Flek, Florian Mai

### Abstract

Emergent misalignment (EM) is the phenomenon where fine-tuning a language model on a narrow task leads to harmful behavior in unrelated domains. A leading mechanistic account attributes EM to persona features: latent directions acquired during pre-training that misaligned fine-tuning amplifies. We ask where these features come from: which pre-training documents activate them, and whether naturally occurring human-written text suffices to induce EM. Using Sparse Autoencoder (SAE) based model diffing across four open-weight models, we find that features related to jailbreak personas, sarcasm, deception, and manipulation are amplified by misalignment fine-tuning, while safety-relevant and assistant-identity features are suppressed. Steering individual features controls EM in both directions: it induces misalignment rates of up to 62% in aligned models -- exceeding the 35% reached by misalignment fine-tuning itself -- and re-aligns misaligned models to near-baseline misalignment rates. Attributing the causal features to a corpus of one million pre-training web documents retrieves semantically relevant narratives about villainous characters, domination, and harmful agency. However, fine-tuning on these human-written documents does not reliably induce EM, even after reformatting into assistant-style responses, whereas synthetic instruction-response pairs derived from the same content do -- and transfer across model families. Semantic relevance alone is therefore not sufficient: response structure or model-generated phrasing plays an important role in inducing EM.

### 中文一句话结论
本研究揭示了涌现性失调（EM）源于预训练中习得的“人格特征”，这些特征在微调过程中被放大，但仅靠人类撰写的自然文本不足以诱发EM，而由相同内容生成的合成指令-响应对则能可靠诱发。

### English TL;DR
This paper attributes emergent misalignment to pre-training persona features amplified by fine-tuning, and finds that while steering these features controls misalignment, naturally occurring human-written text is insufficient to induce it, whereas synthetic instruction-response pairs derived from the same content do.

### 中文详细总结
涌现性失调（EM）是指对语言模型进行窄任务微调后，模型在无关领域出现有害行为的现象。主流机制解释认为，EM源于预训练期间习得并因有害微调而放大的“人格特征”。本研究探究这些特征的来源：哪些预训练文档激活它们，以及自然人类文本是否足以诱发EM。作者使用基于稀疏自编码器（SAE）的模型差异分析，在四个开源模型中发现：与越狱人格、讽刺、欺骗和操纵相关的特征被放大，而安全相关和助手身份特征被抑制。通过激活操控单个特征可双向控制EM：在对齐模型中诱导高达62%的失调率（超过微调本身达到的35%），并使失调模型恢复至接近基线水平。将因果特征归因于百万预训练文档后，检索到的文档多为关于反派角色、统治和有害能动性的叙事。然而，对这些人类撰写文档进行微调并不能可靠诱发EM（即使重新格式化为助手风格响应），而由相同内容生成的合成指令-响应对却能诱发，且跨模型族适用。因此，语义相关性不足：响应结构或模型生成的措辞在诱发EM中起重要作用。

### 方法 / 贡献
- 方法：采用SAE-based模型差异分析，比较对齐模型与失调模型在相同提示集上的特征激活差异；通过激活操控（up-steering/down-steering）验证特征的因果作用；基于特征激活对百万级预训练文档进行归因；最后通过微调实验验证检索文档能否独立诱发EM。
- 贡献：（1）在四个开源模型（Llama-3.1-8B、Qwen2.5-7B、Gemma 2 9B、Gemma 3 27B）上重现并扩展了SAE-based EM分析，发现特征变化的语义一致性；（2）首次证明单个SAE特征即可双向控制EM，且诱导效果超过微调本身；（3）将EM诱发特征归因于预训练文档，揭示重复出现的反派叙事；（4）实验表明人类撰写的自然文本不足以诱发EM，而合成数据（源自相同内容的指令-响应对）有效且跨模型族迁移。

### 实验或数据
- 模型：Llama-3.1-8B-Instruct、Qwen2.5-7B-Instruct、Gemma 2 9B Instruct、Gemma 3 27B Instruct。
- 数据集：使用先前工作中的医疗、法律、安全三个窄域微调数据集（对齐/失调版本）；评估采用44个开放式提问（first-plot-questions），每问采样30次，由GPT-4o-mini判断对齐性和连贯性。
- 特征发现：基于各模型对应SAE（Llama/Qwen: 131k特征，Gemma 2: 131k，Gemma 3: 262k），评估中间层；归因使用百万级预训练网页文档。
- 主要结果：特征中仅7–27%表现出显著位移；激活操控使对齐模型失调率达62%（约30个候选特征中21%有效）；微调人类文档无法可靠诱发EM，而合成指令-响应对诱发EM（跨模型族迁移）。

### 值得关注点
- 单个SAE特征激活操控即可使对齐模型达到62%失调率，超过微调本身（35%），说明这些特征具有强因果作用。
- 人类撰写的自然文本（即使涉及反派、操纵等语义）无法诱发EM，而由相同内容生成的合成数据有效，提示响应结构或模型生成措辞是关键。
- 语义相关性不足：即使文档语义匹配特征，若缺乏助手风格交互形式仍无法诱发EM。
- 效果跨模型族迁移（如从Gemma到Llama），说明特征具有通用性。

### 局限性
论文摘要未明确列出局限性；根据内容推断，研究限于四个开源模型和特定窄域微调设置，可能限制泛化性。此外，合成数据与人类数据差异的具体机制（如响应结构 vs 模型生成措辞）尚未完全解析，需要进一步工作。

## 8. From Interpretability to Control: Insights from Six Years of the TrustNLP Workshop

- Source: arxiv
- arXiv ID: 2608.11171
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.11171v1
- PDF: https://arxiv.org/pdf/2608.11171v1
- DOI: https://doi.org/10.48550/arXiv.2608.11171

### Authors

Rahul Gupta, Abhinav Mohanty, Anaelia Ovalle, Anil Ramakrishna, Anubrata Das, Apurv Verma, Jwala Dhamala, Ninareh Mehrabi, Tharindu Kumarage, Yada Pruksachatkun, Yang Trista Cao, Kai-Wei Chang, Aram Galstyan

### Abstract

The Workshop on Trustworthy Natural Language Processing (TrustNLP), co-located with major ACL conferences since 2021, has grown from 8 proceedings papers to 41 over six editions, documenting a field-wide transition from post-hoc interpretability of static models to mechanistic understanding and proactive control of generative systems. We synthesize insights from all 144 proceedings papers, classifying them along six trust dimensions grounded in established frameworks (TrustLLM, DecodingTrust). We observe co-occurrences with capability emergence. The release of the first high-impact chat models activated all trust dimensions simultaneously, while subsequent model generations shifted focus toward truthfulness and safety alignment. Analysis from the classification study reveals that truthfulness is the fastest-growing dimension (absent in 2021-2022, comprising 37% of papers by 2025-2026), fairness remains the most consistent theme, and explainability exhibits a U-shaped trajectory; declining as post-hoc methods lost relevance but resurging in 2026 through mechanistic interpretability. A cross-venue comparison with ACL, NAACL, EACL, and EMNLP (~2K papers) in the same period shows that TrustNLP's topical distribution closely follows the field average. We identify four structural insights and conclude with actionable directions for the research community.

### 中文一句话结论
通过对TrustNLP研讨会六届144篇论文的系统分类，揭示了该领域从静态模型的事后可解释性转向生成式系统的机制理解与主动控制，其中真实性（truthfulness）成为增长最快的信任维度，而可解释性呈现U型演化轨迹。

### English TL;DR
After six years of the TrustNLP workshop, a synthesis of 144 proceedings papers reveals a field-wide transition from post-hoc interpretability to mechanistic understanding and proactive control of generative systems, with truthfulness emerging as the fastest-growing trust dimension and explainability showing a U-shaped trajectory.

### 中文详细总结
本论文总结了2021年至2026年共六届TrustNLP研讨会的发展。研讨会规模从最初的8篇论文增长到41篇，共收录144篇论文。作者基于TrustLLM和DecodingTrust框架，将论文按六个信任维度分类：公平性与偏见、鲁棒性与对抗、隐私、机器伦理与安全、真实性、可解释性。研究发现：真实性在2021-2022年完全缺失，但到2025-2026年占总论文的37%，成为增长最快的维度；公平性是最稳定的主题，每届均有涉及；可解释性呈现U型轨迹——早期占主导，中期下降，2026年因机制可解释性研究而复苏。跨会议对比（与ACL等主流会议约2000篇论文）显示，TrustNLP的主题分布与整个领域平均水平接近。论文还识别出四个结构性见解，并为研究社区提出了可行动的方向。

### 方法 / 贡献
- **方法**：对144篇会议论文进行系统分类，使用人类标注与两个LLM（Claude Sonnet 5和Amazon Nova Lite 2.0）独立标注，经协调后确定最终标签；采用Cohen’s kappa评估标注一致性（多数维度达到0.7以上）。
- **贡献**：（1）定量主题分析，揭示最快增长和持续的研究主题；（2）按技术演进阶段（2021-2022年：可解释性与偏见；2023-2024年：安全对齐；2025-2026年：可控性）的编年式综合；（3）识别四个结构性见解及研究社区的行动建议。

### 实验或数据
- **实验**：无传统实验。核心工作是分类标注与趋势分析：使用人类标注者和两个LLM对144篇论文标注维度，跨会议对比时从ACL、NAACL、EACL、EMNLP中筛选信任相关论文（约2000篇）。
- **数据**：TrustNLP 2021-2026年所有存档会议论文（144篇），以及同一时期其他*CL会议的信任相关论文。

### 值得关注点
- **真实性维度**从无到有并快速增长，反映了生成式大语言模型对事实一致性的迫切需求。
- **可解释性**的U型轨迹生动展示了从事后解释（特征归因）到机制理解（稀疏自编码器、激活操控）的范式转变。
- **跨会议对比**表明TrustNLP的主题分配与整个NLP社区高度一致，说明该研讨会是领域趋势的良好映射。
- **标注方法论**：采用人类+双LLM标注及协调流程，并报告一致性指标，增强了分类结果的可信度。

### 局限性
- 分类标注中，机器伦理与安全、真实性两个维度存在概念重叠，导致标注一致性相对较低（κ≈0.5-0.6）。
- 分析仅限于一个研讨会系列（TrustNLP），尽管作者通过跨会议比较证明其代表性，但可能遗漏其他专门会议或期刊上的信任相关研究。
- 论文未讨论标注的长期稳定性或人工审查的潜在偏差；样本量（144篇）对于更深度的时间序列分析可能有限。

## 9. Is This Your Final Answer? Cross-Contextual Consistency as a Measure of LLM Credibility

- Source: arxiv
- arXiv ID: 2608.10315
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.10315v1
- PDF: https://arxiv.org/pdf/2608.10315v1
- DOI: https://doi.org/10.48550/arXiv.2608.10315

### Authors

Siyang Wu, Yibo Jiang, Bryon Aragam

### Abstract

Large language models (LLMs) are powerful black-box systems, making it difficult to discern whether their answers reflect stable internal beliefs or superficial pattern matching. We identify cross-contextual consistency as an underutilized behavioral property of LLMs: a credible answer should remain stable when the same task is placed under topic-aligned, content-neutral contextual variation. Building on this intuition, we operationalize Cross-Contextual Consistency (C3) by comparing model generations under original and perturbed prompts. Across 26 models and six benchmarks spanning reasoning, factuality, and code generation, we find that answers with smaller cross-contextual shifts are more likely to be correct or factual. We demonstrate that C3 provides a complementary axis of evaluation and can serve as a benchmark usefulness diagnostic, identifying which portions of a benchmark remain informative even when aggregated scores are widely considered "saturate".

### 中文一句话结论
本文提出跨上下文一致性（Cross-Contextual Consistency, C3）作为衡量大语言模型可信度的行为指标，发现回答在不同上下文扰动下越一致，越可能是正确或事实性的。

### English TL;DR
The paper proposes Cross-Contextual Consistency (C3) as a measure of LLM credibility, demonstrating across 26 models and six benchmarks that answers with smaller distributional shifts under semantically neutral contextual perturbations are more likely to be correct or factual.

### 中文详细总结
大语言模型（LLM）的黑箱特性使其输出难以判断是否反映稳定内部信念。本文识别出“跨上下文一致性”作为一种未被充分利用的行为属性：一个可信的回答应在同一任务置于主题相关、内容中性的上下文变化时保持稳定。作者通过比较原始提示和扰动提示下的模型生成，将跨上下文一致性（C3）操作化。在涵盖推理、事实性和代码生成的26个模型和六个基准测试中，研究发现跨上下文变化较小的回答更可能正确或符合事实。C3提供了互补的评估维度，可作为基准有用性诊断工具，识别即使在聚合分数被认为“饱和”时仍能提供信息的基准部分。

### 方法 / 贡献
1. **识别行为属性**：指出跨上下文一致性是LLM生成可信度的一个被忽视的行为属性。
2. **操作化C3**：提出黑盒评估协议，比较原始和扰动上下文下的输出分布，适配多项选择、短答案、长形式事实性和代码生成任务。
3. **实证证据**：在六个基准和26个模型上证明C3与正确性和事实性一致，对扰动源和比较估计量鲁棒，并能诊断基准的饱和、脆弱、有偏和未学习区域。

### 实验或数据
- **模型**：26个模型（16个主要模型外加10个模型的案例研究）。
- **基准**：六个基准，涵盖推理（如SVAMP、MMLU）、事实性（如SimpleQA）、常识推理和代码生成（如Codeforces）。
- **实验方法**：对每个原始查询采样一组主题对齐、内容中性的上下文扰动，使用最大均值差异（MMD）等距离度量比较原始和扰动条件下的输出分布，计算C3分数。

### 值得关注点
- C3无需访问模型参数或自报告置信度，适合封闭源模型和开放形式回答。
- C3与正确性呈正相关，尽管它不直接衡量事实性或正确性。
- 即使在基准聚合分数已饱和时，C3仍能提供区分性信息，作为基准有用性诊断工具。
- 跨模型和基准的结果显示，新模型在C3上呈上升趋势，表明可信度随时间提高。

### 局限性
论文未明确讨论局限性。基于内容推断：C3依赖精心设计的主题对齐、内容中性的上下文扰动，扰动质量可能影响结果；它仅衡量一致性而非直接正确性，可能无法完全捕获模型可信度的所有方面（如内部偏差）；对于某些任务（如固定格式选择），距离度量的选择可能需适配。

## 10. Diffract: Spectral View of LLM Domain Adaptation

- Source: arxiv
- arXiv ID: 2608.10850
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.10850v1
- PDF: https://arxiv.org/pdf/2608.10850v1
- DOI: https://doi.org/10.48550/arXiv.2608.10850

### Authors

Nikita Borodin, Maria Krylova, Artem Zabolotnyi, Dmitry Aspisov, Egor Shikov, Nikita Tyuplyaev, Oleg Travkin, Roman Alferov, Dmitry Vinichenko

### Abstract

We study continual pre-training (CPT) as a mechanism for adapting general-purpose large language models to specialized domains: mathematics, instruction, code, and natural text. Using singular value decomposition of weight matrices, we find that CPT leaves singular value spectra largely invariant, with adaptation driven mainly by changes in singular vectors. An analysis of attention-head projection matrices reveals strong, domain-dependent head heterogeneity, which we exploit to define a head importance criterion: up to 60% of head updates can be removed without measurable quality loss. Selectively rewinding low-importance heads to their pre-trained state improves benchmark accuracy by up to 4% versus the fully trained baseline. Finally, we identify domain connectivity - linear interpolation between CPT checkpoints yields smooth domain-quality interpolation without notable degradation on either domain - and release Diffract, an open-source toolkit for scalable spectral analysis of billion-parameter models.

### 中文一句话结论
本文通过奇异值分解分析发现，大语言模型的领域适应主要改变奇异向量而非奇异值，并据此提出选择性倒放注意力头的方法，可在保持质量的同时将模型准确率提升高达4%。

### English TL;DR
This paper uses singular value decomposition to show that LLM domain adaptation primarily alters singular vectors while preserving singular value spectra, enabling a selective head-rewinding method that improves accuracy by up to 4% and demonstrating smooth domain interpolation.

### 中文详细总结
本文研究了持续预训练作为将通用大语言模型适应到数学、指令、代码和自然文本等专业领域的一种机制。通过对权重矩阵进行奇异值分解，作者发现持续预训练基本保持奇异值谱不变，领域适应主要由奇异向量的变化驱动。对注意力头投影矩阵的分析揭示了强烈且依赖领域的头异质性，作者据此定义了一个头重要性准则：高达60%的头更新可以被移除而不会产生可测量的质量损失。将低重要性头选择性倒放到其预训练状态，相比完全训练的基线，可将基准测试准确率提升高达4%。最后，作者发现了领域连通性——在持续预训练检查点之间进行线性插值可实现平滑的领域质量插值，而不会在任一领域上出现明显退化，并发布了Diffract，一个用于对数十亿参数模型进行可扩展谱分析的开源工具包。

### 方法 / 贡献
- 使用奇异值分解分析持续预训练过程中权重矩阵的谱变化，揭示奇异值谱基本不变，而奇异向量发生显著变化。
- 提出基于注意力头投影矩阵异质性的头重要性准则，识别可移除的冗余更新。
- 开发选择性头倒放方法：将低重要性头恢复为预训练状态，提高下游任务准确率。
- 发现领域连通性：持续预训练检查点之间线性插值实现平滑领域质量插值。
- 发布Diffract开源工具包，支持对数十亿参数模型进行可扩展谱分析。

### 实验或数据
- 将通用大语言模型通过持续预训练适应到数学、指令、代码和自然文本四个专业领域。
- 实验显示：根据头重要性准则，多达60%的头更新可以移除而无质量损失。
- 选择性倒放低重要性头后，相比完全训练的基线在基准测试中提升了高达4%的准确率。
- 在持续预训练检查点之间进行线性插值，观察到平滑的领域质量插值。

### 值得关注点
- 首次系统揭示持续预训练中奇异值谱与奇异向量的不同角色，区分了领域适应与一般预训练。
- 提出高效且可解释的注意力头筛选与恢复策略，无需额外训练即可提升性能。
- 领域连通性发现为多领域模型融合与迁移学习提供了新视角。
- Diffract工具包为大型模型的可解释性分析与优化提供了实用工具。

### 局限性
- 实验主要在特定模型架构（如注意力头投影矩阵）上进行，泛化性需进一步验证。
- 头重要性准则的阈值选择可能依赖领域和模型，未讨论自动调优方法。
- 领域连通性实验仅对有限领域组合进行测试，更多领域与更复杂插值策略的效果未知。
- 论文未详细说明具体模型大小、训练数据规模与基准测试构建，可能影响结果复现。

## Processing Notes

- Duplicate papers skipped: 0