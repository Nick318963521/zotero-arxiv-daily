# Daily arXiv - 2026-09-04

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-04T00:06:43
- Paper count: 10

## 1. Task-Level Natural Language Priors as Learning Signals for Low-Resource LLM Training

- Source: arxiv
- arXiv ID: 2609.02244
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2609.02244v1
- PDF: https://arxiv.org/pdf/2609.02244v1
- DOI: https://doi.org/10.48550/arXiv.2609.02244

### Authors

Jian Gao, Xiao Zhang, Xun Zhu, Miao Li, Ji Wu

### Abstract

Large language models (LLMs) often struggle when low-resource training data are ambiguous or incomplete. Task-level natural-language priors can provide useful guidance in such settings, but existing approaches usually treat these priors as input context rather than as learning signals during training. We propose Prior-Guided Tuning (PGT), a training perspective that incorporates natural-language priors as auxiliary learning signals for low-resource LLM training. Under this perspective, we introduce Contrastive Prior Steering (CPS), which keeps the original supervised objective intact while adding positive and negative prior-conditioned auxiliary losses to encourage task-consistent learning and discourage plausible but misleading alternatives. Experiments on AmbiMath, Jigsaw, and MNLI/HANS show that CPS consistently improves over plain and prompt fine-tuning. On AmbiMath, CPS achieves 97.6% average exact-match accuracy. On Jigsaw, CPS improves average Macro F1 by 9.5 percentage points over standard fine-tuning, and with 1/10 of the experimental training data slightly exceeds full-data plain fine-tuning. On HANS, CPS improves non-entailment accuracy by 8.3 and 5.2 percentage points for LLaMA 3.1 8B and Qwen 2.5 7B, respectively, while maintaining comparable in-domain MNLI accuracy. These results support our central claim: task-level natural-language priors can provide useful guidance as auxiliary learning signals for low-resource LLM training. Our code and data will be publicly available.

### 中文一句话结论
本文提出对比先验引导（CPS）方法，将任务级自然语言先验作为辅助学习信号用于低资源大语言模型训练，在多个基准上显著提升性能，尤其在数据稀疏或模糊场景下。

### English TL;DR
The paper introduces Contrastive Prior Steering (CPS), a method that uses task-level natural-language priors as auxiliary learning signals during low-resource LLM training to improve performance by encouraging task-consistent learning and discouraging misleading alternatives, as demonstrated on AmbiMath, Jigsaw, and MNLI/HANS benchmarks.

### 中文详细总结
大语言模型在低资源训练数据模糊或不完整时容易依赖虚假关联。现有方法通常将任务级自然语言先验作为输入上下文，而非训练信号。本文提出**先验引导微调（PGT）**视角，将自然语言先验作为辅助学习信号融入训练。具体实现**对比先验引导（CPS）**在保留原始监督目标的同时，添加正/负先验条件辅助损失：正先验鼓励任务一致学习，负先验抑制看似合理但误导的替代规则。在AmbiMath、Jigsaw和MNLI/HANS上的实验表明，CPS一致优于普通微调和提示微调。例如，AmbiMath上达到97.6%的精确匹配准确率；Jigsaw上Macro F1比标准微调提升9.5个百分点，且仅用1/10训练数据即可略超全量数据标准微调；HANS上非蕴含准确率在LLaMA 3.1 8B和Qwen 2.5 7B上分别提升8.3和5.2个百分点，同时保持领域内MNLI准确率。结果支持核心主张：任务级自然语言先验可作为低资源LLM训练的有效辅助学习信号。

### 方法 / 贡献
1. 提出**先验引导微调（PGT）**框架，将自然语言先验作为显式学习信号而非上下文输入，适用于低资源场景。
2. 提出**对比先验引导（CPS）**实现，通过正负先验构造对比辅助损失，鼓励任务一致学习并抑制误导替代，同时保留原始数据驱动信号。
3. 在AmbiMath（合成模糊数学推理）、Jigsaw（毒性分类）和MNLI/HANS（自然语言推理）上验证有效性，展示跨任务泛化能力。

### 实验或数据
- **AmbiMath**：合成基准，构造输入参数与标签之间具有歧义的数据，仅先验能区分目标规则与虚假规则。200样本低资源设置，CPS达到97.6%精确匹配准确率。
- **Jigsaw**：毒性评论分类。CPS将Macro F1提升9.5个百分点（相对于标准微调），用1/10训练数据即超过全量数据标准微调。
- **MNLI/HANS**：自然语言推理。HANS非蕴含准确率：LLaMA 3.1 8B提升8.3%，Qwen 2.5 7B提升5.2%，同时MNLI领域内准确率保持相当。
- 实验覆盖不同模型（LLaMA 3.1 8B、Qwen 2.5 7B）和不同先验形式（位置先验、语义先验）。

### 值得关注点
- 将先验从上下文输入转变为训练信号，视角新颖，对低资源学习有实用价值。
- CPS仅需任务级先验，无需额外实例级标注或知识库，轻量易用。
- 在Jigsaw上极低资源（1/10数据）表现超越全量微调，显示强数据效率。
- 代码和数据将公开，可复现。

### 局限性
- 论文未明确讨论局限性，但方法依赖高质量的正负先验设计，且在不同任务类型上的通用性需进一步验证。

## 2. Benchmarking Language Models for Statistical Problem Formulation

- Source: arxiv
- arXiv ID: 2609.01982
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.01982v1
- PDF: https://arxiv.org/pdf/2609.01982v1
- DOI: https://doi.org/10.48550/arXiv.2609.01982

### Authors

Chen Wang, Junzhe Zhao, Xin Cong, Wanlu Deng, Ke Deng

### Abstract

Large language models (LLMs) are increasingly used as assistants for statistical and data science work, yet existing evaluations largely assume the analysis target is already specified. In practice, users arrive with informal goals and heterogeneous data, leaving the model to decide what statistical task is implied and which data are relevant. We first formalize this upstream step as Statistical Problem Formulation and decompose it into two subtasks: (1) Statistical Problem Classification and (2) Variable Identification & Role Assignment. We then introduce StatFormBench, a benchmark built from five cross-domain statistics textbooks and a data science case library, covering diverse problem types, data representations, and scenario styles. It contains 1,013 samples spanning 20 coarse-grained and 85 fine-grained statistical problem categories. Across 14 open- and closed-source LLMs, the best zero-shot models reach only 72.0 fine-grained classification accuracy and 63.2 variable set overlap. No model performs consistently best across the two subtasks, while enhanced prompting strategies yield only limited or inconsistent gains. We release the benchmark data on Hugging Face at https://huggingface.co/datasets/THU-CongLab/StatFormBench and the evaluation code on GitHub at https://github.com/THU-CongLab/StatFormBench.

### 中文一句话结论
本论文首次提出“统计问题形式化”任务，并构建 StatFormBench 基准，发现当前最强的大语言模型在该任务上表现有限，且无模型能同时在两个子任务上达到最优。

### English TL;DR
This paper introduces the task of Statistical Problem Formulation for LLMs and presents StatFormBench, a benchmark with 1,013 samples across 20 coarse and 85 fine-grained categories. Evaluation of 14 LLMs shows the best models achieve only 72.0% fine-grained classification accuracy and 63.2% variable set overlap, with no model excelling at both subtasks.

### 中文详细总结
本论文聚焦于大语言模型（LLMs）在统计和数据科学任务中的上游能力——从用户的非正式需求中自动明确统计问题及所需变量。作者将该过程形式化为“统计问题形式化”，分解为两个子任务：1) 统计问题分类（粗粒度和细粒度）；2) 变量识别与角色分配（识别关键变量并指定其角色，如预测变量、响应变量等）。为评估该能力，论文构建了 StatFormBench 基准，数据来源于五本跨领域统计学教材和一个数据科学案例库，包含1,013个样本，覆盖20个粗粒度和85个细粒度统计问题类别，并包含多种数据表示形式。研究评估了14个开源和闭源大语言模型，最佳零样本模型在细粒度分类上准确率仅达到72.0%，变量集合重叠度为63.2%，且没有任何模型在两项子任务上同时表现最佳。增强提示策略仅带来有限且不一致的提升。

### 方法 / 贡献
**方法：**
- 将“统计问题形式化”分解为两个子任务：统计问题分类（层次化标签）和变量识别与角色分配（识别变量并赋予角色）。
- 构建统一数据管道：从教材和案例库提取样本 → 分拆多问题 → 质量过滤 → 初始标签（模型辅助） → 场景改写（隐藏统计术语） → 人工验证。

**贡献：**
1. 首次将统计问题形式化作为LLM评估问题进行研究。
2. 构建 StatFormBench 基准，覆盖多样统计问题、数据表示和场景风格。
3. 评估14个模型，揭示当前LLM在映射非正式请求到精确统计表述方面的不足。

### 实验或数据
- **数据来源：** 五本统计学教材（涵盖公共卫生、商业、可靠性、环境科学、临床研究）和 Gouxionghui 数据科学案例库。
- **数据集规模：** 1,013个样本，20个粗粒度类别，85个细粒度类别。
- **模型评估：** 14个开源和闭源大语言模型（零样本设置）。
- **关键结果：**
  - 最佳细粒度分类准确率：72.0%
  - 最佳变量集合重叠度：63.2%
  - 无模型同时在两子任务上最优
  - 增强提示策略（如思维链）效果有限且不一致

### 值得关注点
- 任务定义新颖且实用，弥补了现有基准将分析目标预设为已知的空白。
- 数据构建考虑现实情境，通过场景改写移除统计术语，更贴近真实用户需求。
- 变量角色标注考虑“问题条件性”，同一数据在不同问题下角色可能不同。
- 公开了数据集和评估代码，促进后续研究。

### 局限性
- 样本覆盖范围可能有限（教材和案例库），可扩展性待验证。
- 人工验证流程的具体细节及一致性指标未在摘要中详述。
- 当前基准仅包含20个粗粒度类别，可能无法覆盖所有统计问题类型。

## 3. User Feedback Provides a Unique Signal that LLMs Can not Detect

- Source: arxiv
- arXiv ID: 2609.02859
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.02859v1
- PDF: https://arxiv.org/pdf/2609.02859v1
- DOI: https://doi.org/10.48550/arXiv.2609.02859

### Authors

Shachar Don-Yehiya, Leshem Choshen, Omri Abend

### Abstract

Harnessing naturally occurring feedback from user interactions offers a promising learning signal for Large Language Models (LLMs). However, recent studies suggest this feedback is inherently noisy and difficult to leverage effectively. We challenge this conception by demonstrating that user feedback is a highly actionable signal for improvement, and that its perceived ineffectiveness stems from a systematic bias in current evaluation paradigms. To isolate the usefulness of feedback, we construct synthetic data with a definitive ground truth, alongside naturalistic data to validate that our findings hold in real-world scenarios. By comparing model revisions generated with and without access to feedback across both settings, we show that feedback-informed revisions resolve targeted issues at significantly higher rates than baseline revisions. Finally, we expose the root of the evaluation bias: when a model successfully fixes an issue exclusively due to feedback, LLM judges frequently fail to identify the genuinely corrected response, systematically preferring inferior baseline outputs instead.

### 中文一句话结论
用户反馈对大型语言模型是一种高度可用的改进信号，但其有效性被当前的LLM评估范式系统性掩盖，因为LLM评判者无法识别由反馈驱动的修正。

### English TL;DR
User feedback provides a highly actionable signal for improving LLM responses, but its effectiveness is systematically masked by LLM-based judges that fail to recognize feedback-driven corrections and often prefer inferior baseline outputs.

### 中文详细总结
本文挑战了“用户反馈本质上是噪声、难以有效利用”的普遍观点。作者通过构建具有明确真实标签的合成数据（通过故意污染模型响应生成）以及从真实对话中提取的自然数据，证明用户反馈是一个高度有效的改进信号。在合成和自然两种场景下，带有反馈的模型修订解决了针对性问题，其成功率比无反馈基线高出9-20%。然而，关键发现是：当模型仅凭反馈成功修复问题时，LLM评判者系统地倾向于选择较差的基线输出，而无法识别出真正被修正的响应。在自然数据实验中，评判者正确选择解决问题响应的比例仅为34.1%。这揭示了当前评估范式的一个系统性偏见：用户反馈的贡献被评估方法本身所掩盖。

### 方法 / 贡献
- **方法**：使用了两种数据设置——合成数据（人为污染正确响应，如因果倒置、关键遗漏、实体/逻辑反转）和自然数据（从ShareLM对话中提取真实用户反馈，并过滤主观、非通用的反馈）。对比了有无反馈的模型修订版本（使用Gemini-3-Flash和Qwen3-8B作为改进模型）。
- **贡献**：1）证明了用户反馈是一种高度可用的学习信号，而非噪声。2）揭示了当前LLM评估方法存在系统性偏见，即评判者偏好无反馈的劣质输出，掩盖了反馈的效用。

### 实验或数据
- **数据**：合成数据基于Arena-Hard-v2.0（500个硬提示+250个创意写作提示），使用o3模型响应并污染。自然数据来自ShareLM对话集合，提取了1000个样本。
- **实验**：在合成数据（每个样本4种污染类型，共2000样本）和自然数据（1000样本）上，比较有/无反馈的修订效果。使用LLM评判者（Gemini-3.1-Pro）进行问题解决评估和成对比较。进行了人工验证：合成数据问题解决评估的Cohen's Kappa为0.81，自然数据为0.24（较低，用作近似）。

### 值得关注点
- 反馈带来的改进率提升显著（合成数据中大型改进者达95.6%，自然数据中也无反馈基线高出9%）。
- LLM评判者的系统性偏见是核心发现——即便无反馈基线修复率更低，评判者仍频繁偏好它，这是此前认为反馈无效的根本原因。
- 研究方法设计精巧：通过合成数据确保可验证的真实标签，再用自然数据验证现实场景，增强了结论的可信度。

### 局限性
- 仅使用了有限的模型（Gemini-3-Flash和Qwen3-8B作为改进者，Gemini-3.1-Pro作为评判者），未探索更广泛模型家族的泛化性。
- 自然数据中的问题解决评估仅作为近似（因为无法确认解决反馈是否真正修复问题），且人工验证的Cohen's Kappa仅为0.24，可靠性有限。
- 未探讨用户反馈中不同粒度（如具体解决方案 vs. 仅指出问题）对改进效果的影响。
- 未讨论如何改进评估方法以消除偏见，也未提出利用反馈信号的具体训练框架。

## 4. Do Large Language Models Capture the Diversity in their Training Data?

- Source: arxiv
- arXiv ID: 2609.02275
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.02275v1
- PDF: https://arxiv.org/pdf/2609.02275v1
- DOI: https://doi.org/10.48550/arXiv.2609.02275

### Authors

Youqi Wu, Farzan Farnia

### Abstract

Large language models are trained to model conditional distributions over text, yet it remains inadequately understood whether they capture the full diversity of plausible outputs present in their training data. We study this question through an information-theoretic lens by comparing the conditional entropy of model-generated outputs with that of the corresponding training data. Given paired input-output samples, we use conditional entropy and its matrix-based analogue based on von Neumann entropy to measure output variability beyond what is explained by the conditioning input, without requiring multiple reference outputs for the same prompt. Across LLM families with publicly available training data, including OLMo, Pythia, and GPT-Neo, we consistently find that model-generated outputs exhibit lower conditional entropy than their training data, across different model scales, sequence lengths, and decoding strategies. We observe a similar conditional diversity gap beyond language modeling, including class-conditioned ImageNet generators and text-conditioned models trained on MS-COCO. To address this gap, we propose a post-hoc correction mechanism that generates multiple outputs for each input and reweights them through a matrix-entropy projection, increasing conditional diversity while remaining close to the original model distribution. We prove the concavity of the matrix-based conditional entropy functional, which makes the resulting entropy-constrained projection a convex optimization problem, and develop a scalable mirror-descent algorithm for its implementation. Our results reveal a systematic conditional diversity gap between modern generative models and their training data, and provide an information-theoretic framework for measuring and mitigating this gap.

### 中文一句话结论
研究表明，大语言模型生成的输出在多样性上系统性低于其训练数据的条件熵，表明模型未能捕捉数据中的全部输出多样性，并可通过信息论框架进行测量与缓解。

### English TL;DR
Large language models systematically generate outputs with less conditional diversity than their training data, measured via conditional entropy, a gap that can be mitigated using a post-hoc matrix-entropy projection method.

### 中文详细总结
该论文通过信息论视角，研究大语言模型是否能够捕捉训练数据中输出的全部多样性。作者比较了模型生成输出与训练数据的条件熵，使用基于冯·诺依曼熵的矩阵条件熵作为度量标准，避免了需要多个参考输出的传统方法。实验覆盖了OLMo、Pythia、GPT-Neo等多个公开训练数据的模型系列，并在不同模型规模、序列长度和解码策略下，一致发现模型输出的条件熵低于训练数据。这种“条件多样性差距”同样出现在其他生成模型中，如基于ImageNet的类条件生成器和基于MS-COCO的文本条件模型。为缩小差距，作者提出了一种事后校正机制：为每个输入生成多个输出，并通过矩阵熵投影进行重加权，增加多样性，同时保持与原始模型分布接近。论文还证明了矩阵条件熵的凹性，使约束投影成为凸优化问题，并设计了可扩展的镜像下降算法。

### 方法 / 贡献
- **方法**：使用条件熵及其矩阵形式（基于冯·诺依曼熵）作为多样性度量，比较模型与训练数据；提出事后重加权校正机制，通过矩阵熵投影进行凸优化。
- **贡献**：
  1. 系统性发现并验证了生成模型与训练数据之间的条件多样性差距。
  2. 提供无需多个参考输出的信息论度量框架。
  3. 提出可扩展的校正算法，增加多样性而不显著偏离原始分布。

### 实验或数据
- **实验范围**：OLMo、Pythia、GPT-Neo等语言模型，以及ImageNet类条件生成器、MS-COCO文本条件模型。
- **数据**：论文使用公开可用的训练数据；未提及具体数据集大小或统计细节。实验未涉及自定义数据集。

### 值得关注点
- **创新度量**：使用矩阵条件熵，避免了对多个参考输出的依赖。
- **广泛验证**：跨模型尺度、序列长度和解码策略的一致性结果。
- **校正机制**：后处理方法兼顾多样性与分布保真度，理论上有凸优化保证。

### 局限性
- **实验范围**：仅涵盖有限模型系列和图像生成任务，通用性需验证。
- **校正可扩展性**：算法对大量输出样本的计算成本未详细分析。
- **未说明具体数据**：训练数据细节和统计特征未被明确提及，可能影响复现性。

## 5. Loom: Weaving Diagnostic Strands into Free-Text Consensus via Embedding-Space Reweighting

- Source: arxiv
- arXiv ID: 2609.02649
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.02649v1
- PDF: https://arxiv.org/pdf/2609.02649v1
- DOI: https://doi.org/10.48550/arXiv.2609.02649

### Authors

Ron Begleiter, Katya Egert Berg, Gilad Saban, Gil Shabat

### Abstract

Aggregating noisy, conflicting textual hypotheses into a reliable consensus is a fundamental challenge when deploying NLP systems in real-world industrial settings. While monolithic Large Language Model (LLM) agents offer unbounded expressivity for tasks like Root Cause Analysis (RCA), they suffer from context limits, compounding hallucinations, and prohibitive inference latency. Traditional weak supervision offers statistical rigor but is mathematically restricted to discrete classes. We present Loom, a generative consensus framework deployed for real-world RCA that bridges these paradigms. Loom aggregates open-form hypotheses emitted by modular heuristics (diagnostic templates dynamically populated with episode-specific entities, times, and metrics) by projecting them into a continuous embedding space, and resolves conflicting signals with an iterative centroid-based reweighting algorithm. The resulting consensus weights ground a single lightweight LLM synthesis step. Evaluated on the OpenRCA benchmark, Loom occupies the accuracy--efficiency Pareto frontier: it matches a state-of-the-art autonomous agent on Bank and Market-2 and trails on Market-1 and Telecom, while using a single LLM call per incident on all four datasets ($\sim$26$\times$ faster; $\sim$33$\times$ with an 8B-parameter synthesizer). We discuss our deployment experience, highlighting lessons learned regarding the trade-offs between agentic depth and inference latency, negative results in redundancy detection, and how deterministic consensus fosters trust among Subject Matter Experts~(SMEs).

### 中文一句话结论
Loom 提出一种结合嵌入空间迭代重心重加权与单次轻量级LLM合成的生成式共识框架，在根因分析任务上达到与自主智能体相当的准确率，同时实现约26–33倍的推理加速。

### English TL;DR
Loom is a generative consensus framework for root cause analysis that aggregates noisy, open-form textual hypotheses from modular heuristics by projecting them into an embedding space and resolving conflicts with iterative centroid-based reweighting, enabling a single lightweight LLM synthesis step that matches the accuracy of autonomous agents while being 26–33× faster.

### 中文详细总结
Loom 旨在解决工业场景中聚合噪声化、冲突性文本假设以形成可靠共识的挑战。传统方法中，大规模语言模型（LLM）自主智能体虽表达力强，但受限于上下文窗口、幻觉累积和高推理延迟；而弱监督方法虽统计严谨，但仅适用于离散类别。Loom 通过以下流程弥合这一差距：首先，模块化启发式程序（诊断模板）根据具体事件动态填充实体、指标和时间，生成开放式文本假设；接着，将这些假设投影到连续嵌入空间，利用基于迭代重心重加权的算法（计算加权中心并更新假设权重）在毫秒级解决冲突；最后，仅需一次轻量级LLM调用，基于去噪后排序的证据合成最终根因分析报告。在 OpenRCA 基准上，Loom 在所有四个数据集上均达到准确率-效率帕累托前沿：在 Bank 和 Market-2 上匹配最先进的自主智能体，在 Market-1 和 Telecom 上略逊，但推理速度提升约26倍（使用8B参数合成器时达33倍）。本文还讨论了在生产数据中心部署的经验，包括自主深度与延迟的权衡、冗余检测的负面结果，以及确定性共识如何增强领域专家的信任。

### 方法 / 贡献
1. **生成式共识框架**：将弱监督思想扩展到模板化、事件特定的开放式文本假设聚合，无需离散标签空间。
2. **迭代嵌入-重心重加权算法**：通过计算语义嵌入的加权重心，动态调整假设权重（基于与重心的余弦相似度），并内置静态冗余检测（分组减权）以避免冗余规则主导。
3. **单次轻量级LLM合成**：仅对去噪后排序的证据进行一次LLM调用，生成最终根因分析报告，显著降低延迟和幻觉风险。
4. **实际部署验证**：在 NVIDIA 生产数据中心（分布式训练故障和静默性能退化）及 OpenRCA 基准上展示效果，并总结负面结果与经验教训。

### 实验或数据
- 在 **OpenRCA 基准**（包含 Bank、Market-1、Market-2、Telecom 四个数据集）上评估。
- 对比基线为 **RCA-Agent**（基于LLM的自主智能体）。
- 结果：Loom 在所有数据集上准确率处于帕累托前沿（Bank 和 Market-2 持平，Market-1 和 Telecom 稍低），但推理速度提升约**26倍**（使用8B参数合成器时达33倍）。
- 此外，在 NVIDIA 生产数据中心提供了两个定性案例（分布式训练故障归因、静默性能退化诊断）。

### 值得关注点
1. **效率与准确率的平衡**：仅用单次LLM调用即可匹配多步自主智能体的准确率，推理速度提升一至两个数量级。
2. **确定性共识**：重加权过程完全基于数学计算（非随机生成），结果可审计、可复现，易于获得领域专家信任。
3. **工业实用性**：诊断模板可预编程或从历史工单自动提取，且聚合约仅需毫秒级计算，适合高吞吐、低延迟的工业环境。
4. **部署经验分享**：明确报告了冗余检测的负面结果（静态阈值分组效果有限）及单次合成的局限性，体现了研究的诚实性。

### 局限性
1. **准确率未全面超越**：在 Market-1 和 Telecom 数据集上，Loom 的准确率低于最先进的自主智能体，表明纯数学聚合可能遗漏某些复杂语义模式。
2. **依赖模板质量**：框架效果高度依赖于诊断模板（DS）的编写质量；若模板覆盖不全或不准确，LLM合成将基于有偏的输入。
3. **冗余检测效果有限**：静态预处理相似度分组无法完全消除动态运行时的冗余或相互矛盾的假设，论文指出这是负面结果。
4. **单次合成限制**：仅依赖一次LLM调用可能难以处理极其复杂或嵌套的因果链，且LLM的输出仍可能出现小型幻觉（尽管通过去噪输入已缓解）。
5. **领域适应性**：当前设计围绕根因分析任务，其通用性（如迁移到开放域文本聚合）未在论文中验证。

## 6. The Dynamics of Continuous Mixture Collapse in Language Models

- Source: arxiv
- arXiv ID: 2609.02049
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.02049v1
- PDF: https://arxiv.org/pdf/2609.02049v1
- DOI: https://doi.org/10.48550/arXiv.2609.02049

### Authors

Ali Backour

### Abstract

LLMs latent-state reasoning methods replace discrete intermediate tokens with continuous states, such as weighted mixtures of token embeddings, to retain multiple possible reasoning directions rather than committing to one. Yet pretrained language models often fail to preserve these mixtures. We study why through a combination of theoretical analysis and controlled empirical investigations on a variety of models. We identify three independent, distinct sources of failure. First, transformer architectures already distort mixture geometry, and training substantially amplifies this effect. Moreover, the failure can occur even if the model transports mixtures perfectly linearly: the softmax readout and autoregressive feedback form a dynamical system that either amplifies small differences until one component of the mixture dominates or contracts different mixtures until they become indistinguishable. We verify this theoretical prediction empirically: the observed transition between contraction and amplification occurs near the theoretical threshold derived by our analysis, and pretrained-model rollouts lie predominantly on the amplifying side. Finally, we generalize to mixtures of many components and show that exact preservation generally requires context-dependent correction, whose required dimensionality can grow with the number of components.

### 中文一句话结论  
本文通过理论分析和实验验证，发现语言模型中连续混合状态崩溃的三个独立原因：变换器架构本身扭曲混合几何、训练显著放大扭曲、以及softmax读出与自回归反馈构成的动力学系统即使在线性完美传输下也会导致混合崩溃。

### English TL;DR  
This paper identifies three independent sources of failure in language models that cause continuous mixture collapse—architectural distortion, training amplification, and a dynamical system arising from softmax and autoregressive feedback—showing that even perfect linear transport cannot prevent the mixture from being destroyed.

### 中文详细总结  
论文研究了预训练语言模型在隐状态推理中无法保持连续混合状态（如词嵌入的加权组合）的原因。作者通过理论分析与受控实验，揭示了三个相互独立的崩溃源：  
1. **架构扭曲**：变换器结构本身就会改变混合状态的几何表示。  
2. **训练放大**：预训练过程显著加剧了这种扭曲，且随深度增加越明显。  
3. **动力学崩溃**：即使模型完美线性地传输混合状态，softmax读出和自回归反馈会构成动力学系统——当两个组件的下一步偏好差异足够大时，微小不平衡被放大直至单组件主导；当偏好相似时，不同混合趋于不可区分。  
论文还推广到多组件情形，说明精确保持通常需要依赖上下文的修正，且所需维度随组件数增长。  
实验在多种Qwen和Gemma模型上进行，对比训练模型与随机初始化对照，验证了动力学阈值的存在，并发现预训练模型的实际行为主要处于放大区。

### 方法 / 贡献  
- **理论贡献**：将混合崩溃建模为动力学系统，推导出收缩/放大切换的关键阈值（耦合强度L=2），并给出时变耦合下的持续极化定理。  
- **实验方法**：设计CALIB指标衡量混合保持程度，在多个模型上比较训练前后各层表现，并与随机初始化的对照网络分离架构和训练的影响。  
- **数据与模型**：使用Qwen3.5和Gemma 4系列共八种模型，构建1000条测试基准（含三元混合可视化）。  
- **验证方法**：通过分析预训练模型的实际rollout轨迹，确认其位于动力学放大侧并接近理论阈值。

### 实验或数据  
- **基准测试**：构造词嵌入混合（如“血/草/天”三种颜色词），输入模型并检测其输出颜色分布是否保持混合比例。  
- **CALIB指标**：通过测量隐藏态在纯组件方向上的投影来估计保留的混合权重，理想值为1。  
- **对照实验**：每个训练模型与五个随机初始化同架构网络对比，发现训练模型在各层（尤其是深层）的CALIB显著低于对照。  
- **动力学验证**：在预设的耦合强度范围内，计算模型rollout的L_t和b_t，观察到从收缩到放大的转变点与理论L=2一致，且预训练模型的rollout主要落在放大侧。  
- **多组件扩展**：分析表明完美保持需上下文敏感的修正，且所需信息量随组件数增长。

### 值得关注点  
- **三大独立崩溃源**：架构、训练、动力学三者均可单独导致混合崩溃，且动力学失效在线性传输假设下依然存在。  
- **动力学阈值**：softmax+自回归反馈的耦合强度在L=2处发生相变，低于此值混合收缩，高于此值放大。  
- **通用性**：分析覆盖多种规模模型，且发现训练放大效应随规模扩大而增强。  
- **多组件挑战**：即使两组件情形可理论刻画，多组件时精确保持的复杂性显著增加。

### 局限性  
- **主要分析两组件情形**：虽推广到多组件，但理论分析和实验验证以两组件为主，更复杂混合的动力学行为尚待深入研究。  
- **假设完美线性传输**：动力学分析假设变换器完美线性传输混合状态，实际模型中架构扭曲和训练放大会破坏这一假设。  
- **模型范围有限**：实验仅基于Qwen和Gemma系列，其他架构（如DeepSeek、Llama）的崩溃模式可能不同。  
- **未提供实用解法**：论文揭示崩溃机制但未给出实用修复方法，仅指出需上下文调整修正，其具体实现仍有待探索。

## 7. From Tokens to Semantics: Leveraging Complementary Signals for Hallucination Detection in Black-Box LLMs

- Source: arxiv
- arXiv ID: 2609.02679
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.02679v1
- PDF: https://arxiv.org/pdf/2609.02679v1
- DOI: https://doi.org/10.48550/arXiv.2609.02679

### Authors

Urja Pawar, Rajitha Ramanayake, Owen O'Neill, Nabeel Kemal, Abhishek Mandal, Houssem Chatbri, Christopher Martin

### Abstract

When LLMs support public-facing or high-stakes workflows, missed fabrications can harm users and institutions, while false alarms consume limited human-review capacity. When no trusted context or reference document is available, we study two signals accessible through black-box model APIs: semantic entropy, which measures disagreement among sampled response meanings, and uncertainty derived from token log-probabilities. Their failure modes can be complementary: semantic entropy becomes uninformative when responses form one semantic cluster, while token uncertainty can miss consistently confident errors. We extend token-based uncertainty detection by aggregating token-level signals across sampled responses through our TopK method, evaluate the hybrid CoCoA method, which combines target-response uncertainty with semantic dissimilarity, and propose and study two supervised methods: Gated, which routes single-cluster cases to an aggregated-token-feature classifier, and Stacked, which learns jointly from semantic uncertainty and broader token features. We evaluate seven benchmarks, including five public benchmarks (four text datasets and multimodal handwritten-cheque extraction) and two constructed benchmarks (Financial Summaries and Long-Text QA), using four language models. In our evaluation across models and datasets, Stacked gave the best performance in nearly half of the cases, while TopK and CoCoA remain competitive without supervised training labels, although their thresholds require careful calibration. No method is universally strongest. We therefore evaluate performance at false-positive-rate budgets from 1% to 15%, assess their sensitivity to generation and calibration choices, and examine variation across dataset characteristics.

### 中文一句话结论
本文提出利用语义熵和令牌对数概率两个互补信号的黑盒LLM幻觉检测方法，其中Stacked监督模型在多数场景下最优，但无单一方法通用。

### English TL;DR
This paper studies complementary hallucination detection signals (semantic entropy and token log-probabilities) for black-box LLMs, proposing supervised (Stacked, Gated) and unsupervised (TopK, CoCoA) methods; Stacked performs best in nearly half of cases but no method is universally optimal.

### 中文详细总结
论文针对黑盒大语言模型（LLMs）在缺乏参考文档时的幻觉检测问题。通过API可获取两种信号：语义熵（多次生成响应间的语义分歧）和令牌对数概率（单个响应的置信度）。研究发现两者失败模式互补：单语义簇时语义熵失效，而令牌不确定性可能漏检持续高置信错误。作者扩展了基于令牌的检测：TopK方法聚合多次响应的令牌级特征；评估了混合方法CoCoA（目标响应不确定性+语义不相似性）；提出两种监督方法：Gated（路由单簇案例到聚合令牌分类器）和Stacked（联合学习语义与令牌特征）。在7个基准（含5个公开、2个自建）和4个LLM上评估，Stacked在近半案例中最佳，TopK和CoCoA无需标签但需阈值校准。无方法绝对最优，论文评估了1%-15%假阳性率预算下的性能及对生成/校准参数的敏感性。

### 方法 / 贡献
- 系统分析语义熵与令牌对数概率在黑盒幻觉检测中的互补性及失败模式。
- 提出无监督TopK方法：聚合多次响应的平均top-k熵与跨响应对数概率方差。
- 提出监督Gated级联：根据语义簇数选择语义熵或聚合令牌分类器。
- 提出监督Stacked分类器：联合利用语义不确定性和令牌特征。
- 评估现有CoCoA方法（目标响应不确定性+语义不相似度）。
- 在多种模型（4个）和数据集上全面比较，强调无方法万能，并提供低假阳性率预算下的条件指导。

### 实验或数据
评估了7个基准：5个公开（4个文本数据集+多模态手写支票提取），2个自建（财务摘要、长文本QA）。使用4个语言模型（具体模型未在摘要中列出，但原文包含）。实验覆盖不同模型、数据集和假阳性率预算（1%-15%），并测试对生成参数和校准的敏感性。数据特点分析显示方法性能因数据集特性而异。

### 值得关注点
- Stacked监督模型在近半数场景下最优，但TopK和CoCoA作为无监督方法仍具竞争力（需仔细校准阈值）。
- 无方法通用最强，性能依赖数据集、模型和假阳性率预算。
- 语义熵在单簇错误时失效，令牌不确定性在一致错误时失效，互补性结合有效。
- 论文强调低假阳性率预算（1-15%）下的实际应用场景。

### 局限性
- 仅依赖黑盒API可获取的信号（语义熵和令牌对数概率），无法利用模型内部状态或参考文档。
- TopK和CoCoA无监督方法需要阈值校准，且不提供确定性路由。
- 监督方法（Stacked、Gated）需要标注数据训练，泛化性可能受限于训练分布。
- 评估局限于4个模型和7个数据集，结论普适性需进一步验证。
- 未考虑更复杂的语义离散化或动态采样策略，语义簇数假设可能限制SE有效性。

## 8. MultiGhostBench: A Multilingual Benchmark for Long-Form LLM-Generated Text Attribution under Distribution Shifts

- Source: arxiv
- arXiv ID: 2609.02379
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.02379v1
- PDF: https://arxiv.org/pdf/2609.02379v1
- DOI: https://doi.org/10.48550/arXiv.2609.02379

### Authors

Matteo Greco, Anudeex Shetty, Andrea Tagarelli, Jey Han Lau

### Abstract

While existing work on LLM authorship attribution (AA) has made progress, available benchmarks remain limited, often focusing on English, controlled settings, or relatively outdated models, with the few multilingual studies considering only relatively short texts. We introduce MultiGhostBench, a multilingual benchmark comprising 928 books generated by five recent LLMs across six languages and three scripts, with an average length of approximately 59K words per book. The benchmark supports evaluation under domain, author, and language shifts. Evaluation of representative AA methods shows that no single method consistently performs best across settings, and performance generally degrades under distribution shifts. Transformer-based detectors can retain generator-related information across languages, although transfer effectiveness varies by language pair, whereas statistical and fingerprint-based detectors are more language-dependent. We envision MultiGhostBench as a valuable resource for the development and evaluation of robust AA methods. The dataset and code can be found at https://github.com/GrecoMT/MultiGhostBench.

### 中文一句话结论
MultiGhostBench是首个面向多语言、长文本LLM生成文本归因的基准，包含928本由5种最新LLM在6种语言生成的书籍（平均约5.9万字），实验表明归因方法在分布偏移下性能普遍下降，且无单一方法在所有设置中表现最佳。

### English TL;DR
MultiGhostBench is the first multilingual benchmark for long-form LLM-generated text attribution, featuring 928 books (~59K words each) from 5 recent LLMs across 6 languages. Evaluation shows no single AA method consistently excels, performance degrades under domain/author/language shifts, and Transformer-based detectors better preserve generator information across languages than statistical/fingerprint methods.

### 中文详细总结
现有LLM文本归因研究主要聚焦于英语、短文本或较旧的模型，多语言研究也局限于短文。本文提出MultiGhostBench，一个多语言基准，包含928本由DeepSeek、Qwen、GPT-OSS、Gemini Pro、Gemini Flash五种近期LLM生成的书籍，覆盖英语、德语、意大利语、西班牙语、俄语和中文六种语言（三种文字系统），平均每本书约5.9万字。该基准支持领域、作者和语言三种分布偏移下的评估。对统计、监督和指纹特征等代表性归因方法的测试表明：1) 无单一方法在所有设置中表现最佳；2) 所有方法的性能在分布偏移下普遍下降；3) Transformer检测器能跨语言保留生成器相关信息，但迁移效果因语言对而异；4) 统计和指纹检测器更依赖语言。数据集和代码已开源。

### 方法 / 贡献
- **数据构建**：模拟人类书籍写作的分层流程（大纲→章节迭代生成），基于古登堡计划的约束条件（类型、时期）生成多语言书籍。提示词经母语者翻译及核验。
- **基准设计**：涵盖六种语言（四个语系、三种文字系统），支持领域偏移、作者偏移（跨生成器）、语言偏移三种泛化场景。
- **评估框架**：系统比较了统计方法、基于Transformer的监督方法和基于指纹的归因方法在多语言、多偏移条件下的表现。

### 实验或数据
- **数据集规模**：928本书，平均每本约59,000词，LLM涵盖DeepSeek、Qwen、GPT-OSS、Gemini Pro、Gemini Flash。
- **实验设置**：评估了多种归因方法在三种分布偏移（领域、作者、语言）下的宏F1分数。
- **主要结果**：无最佳一致方法；Transformer检测器跨语言迁移有效但因语言对而异；统计/指纹方法语言依赖性强。

### 值得关注点
- **首个多语言长篇LLM归因基准**，填补了现有基准限于英语/短文本的空白。
- **多维度分布偏移联合评估**（领域+生成器+语言），更贴近实际应用。
- **发现Transformer架构在跨语言归因中的弹性**，但效果受语言相似性影响。

### 局限性
- 论文未提及实验中的具体基准方法名称（如统计/Transformer/指纹方法的代表）及其精确性能数值。
- 仅覆盖5种LLM和6种语言，更多模型和语言的泛化性有待验证。
- 未评估人机混合文本或对抗性改写情况。
- 未比较不同书写的生成长度对归因性能的影响。

## 9. Do Cantonese-Adapted Language Models Better Predict Cantonese Reading? A Cross-Model Eye-Tracking Evaluation

- Source: arxiv
- arXiv ID: 2609.02163
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.02163v1
- PDF: https://arxiv.org/pdf/2609.02163v1
- DOI: https://doi.org/10.48550/arXiv.2609.02163

### Authors

Ziqi Zhang, Emmanuele Chersoni, Mohammad Momenian

### Abstract

Information-theoretic measures derived from autoregressive language models are widely used to characterize the expectations that shape human reading, but whether language-variety-specific training improves such psycholinguistic alignment remains unclear. This question is still open for Cantonese, where recent NLP evaluations reported mixed benefits from Cantonese-specific training relative to Mandarin-oriented or general-purpose models. Using naturalistic Cantonese eye-tracking data, we compare two within-family adaptation contrasts: CKIP GPT-2 Tiny versus its lightly Cantonese-adapted JED351 derivative, and Qwen2.5-7B versus CantoneseLLM-7B, which underwent substantially more extensive Cantonese continued pretraining and instruction tuning. From each model, we derive lexical surprisal, POS surprisal, entropy before the target, and entropy reduction. Lexical surprisal and the joint four-metric model consistently favor CantoneseLLM-7B, followed by Qwen2.5-7B, CKIP, and JED351, whereas entropy reduction favors CKIP. These results suggest that more extensive Cantonese-specific training can be associated with stronger predictive fit, while model rankings also depend on the information-theoretic measure being evaluated.

### 中文一句话结论
更广泛的粤语特定训练能提高语言模型预测粤语阅读行为的准确性，但模型排名依赖于所使用的信息论指标。

### English TL;DR
Using Cantonese eye-tracking data, this study finds that more extensive Cantonese-specific training improves language models' ability to predict reading behavior, although the relative performance of models depends on which information-theoretic measure is evaluated.

### 中文详细总结
本研究利用MCFIX粤语眼动数据，评估两种粤语适应模型的预测能力：小模型组（CKIP GPT-2 Tiny 与 JED351）和大模型组（Qwen2.5-7B 与 CantoneseLLM-7B）。结果表明，词汇惊讶度和四指标联合模型始终偏好CantoneseLLM-7B，其次是Qwen2.5-7B、CKIP和JED351；而熵减少指标偏好CKIP。这表明更广泛的粤语特定训练（如CantoneseLLM-7B的大规模继续预训练和指令微调）可提升预测能力，但效果因指标而异。

### 方法 / 贡献
1. 比较四个语言模型（两个小型、两个大型），组成两组同家族粤语适应对比。
2. 联合评估四种信息论指标：词汇惊讶度、词性惊讶度、靶词前熵和熵减少。
3. 进行五折交叉验证的鲁棒性分析、阅读任务比较和预测变量块消融实验。

### 实验或数据
实验使用MCFIX粤语眼动数据集，包含自然阅读和任务特定阅读条件下30名粤语母语者的首次注视时间、第二次注视时间和总注视时间。数据集共10,011条有效观察。采用CatBoost回归，以无语言模型基线为基准，逐一添加LLM指标。

### 值得关注点
- 粤语特定训练对预测能力的影响因模型规模和适应策略而异（轻量微调vs.大规模继续预训练）。
- 不同信息论指标（如词汇惊讶度与熵减少）对模型排名产生不同影响。
- 研究同时考察了阅读任务（自然阅读 vs. 任务特定阅读）的差异。

### 局限性
- 仅使用单一粤语眼动数据集（MCFIX），可能影响泛化性。
- 模型数量有限（两个适应对比组），且JED351的粤语微调数据量较小（约50 MB维基百科文本）。
- 未涵盖其他可能的预测指标（如语法结构或语义相关度量）。

## 10. MemeCULT-1K: Benchmarking South Asian Cultural Context and Humor Understanding of Multimodal Models

- Source: arxiv
- arXiv ID: 2609.01772
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.01772v1
- PDF: https://arxiv.org/pdf/2609.01772v1
- DOI: https://doi.org/10.48550/arXiv.2609.01772

### Authors

Tawsif Tashwar Dipto, Mehedi Ahamed, Radib Bin Kabir, Mueeze Al Mushabbir, Mohammed Saidul Islam, Mir Rayat Imtiaz Hossain, Md Tahmid Rahman Laskar, Sabbir Ahmed

### Abstract

Meme understanding goes beyond recognizing visual content or literal text; it requires implicit cultural knowledge and pragmatic inference that most vision-language models still lack. We introduce MemeCULT-1K, a multilingual benchmark of 1,000 South Asian memes in Bengali, English, and Hindi, where each meme is paired with a cultural context note and three human-written explanations, along with a supplementary set of 54 Bengali regional dialect memes. We evaluate thirteen popular Vision Language Models (VLMs) under two settings: meme-only and context-aware. Providing minimal cultural context yields consistent gains across all models and languages: mean SBERT similarity improves from 44.6 to 56.4 (+11.8), BLEURT from 37.3 to 42.3 (+5.0), and LLM-as-a-Judge scores from 2.57 to 3.43 out of 5 (+0.86). Fine-grained error analysis reveals that closed-source models fail mainly on entity and reference misidentification, while open-source models are bottlenecked by broader cultural knowledge gaps, with linguistic and phonological failures proving the most context-resistant across both. These results highlight the difficulty of culturally grounded meme understanding and motivate future work on explicit cultural knowledge integration. Our dataset and code are publicly available at TawsifDipto17/MemeCULT-1K.

### 中文一句话结论
本文提出 MemeCULT-1K 基准测试，证明添加文化背景能提升视觉语言模型对南亚迷因的理解，但语言/音韵类错误仍难以通过上下文改善。

### English TL;DR
This paper introduces MemeCULT-1K, a multilingual South Asian meme benchmark showing that while adding minimal cultural context consistently improves VLM explanation quality across all 13 evaluated models (e.g., +11.8 SBERT), persistent errors—especially linguistic/phonological failures—remain highly context-resistant, motivating explicit cultural knowledge integration.

### 中文详细总结
该论文构建了 MemeCULT-1K 数据集，包含 1,000 个南亚迷因（孟加拉语、英语、印地语），每个迷因配有文化背景说明和三段人工撰写的解释，另附 54 个孟加拉区域方言迷因。研究评估了 13 个视觉语言模型在两种设置下的表现：仅看迷因和给予文化背景。结果一致表明，添加最小文化背景后，所有模型的解释质量均提升：平均 SBERT 相似度从 44.6 升至 56.4，BLEURT 从 37.3 升至 42.3，LLM 评判分数从 2.57 升至 3.43（满分 5）。细粒度错误分析发现，闭源模型主要失败于实体和引用错误识别，开源模型则受困于更广泛的文化知识缺失；语言和音韵类失败在两种模型中均对上下文最不敏感。

### 方法 / 贡献
- 提出了 MemeCULT-1K 多语言南亚迷因解释基准数据集。
- 设计了上下文感知评估设置，用于衡量视觉语言模型中的文化背景推理能力。
- 进行了细粒度错误分析，揭示了闭源与开源模型在文化相关迷因理解上的不同失败模式。

### 实验或数据
- 数据集：1,000 个来自孟加拉语、英语、印地语的迷因，额外 54 个孟加拉方言迷因；每个迷因附带一段文化背景说明和三段独立撰写的人工解释。
- 模型：评估了 13 个流行视觉语言模型（包括 GPT-5、Gemini 2.5、Gemma-3、InternVL3.5 等）。
- 设置：迷因单独 vs. 迷因+文化背景；使用自动指标（SBERT 相似度、BERTScore F1、BLEURT）及 LLM 评判和人工评估。
- 结果：添加背景在所有语言和模型上均有提升（例如 SBERT +11.8，BLEURT +5.0，LLM 评判 +0.86）。

### 值得关注点
- 即使提供最小文化背景，所有评估模型的理解质量均显著改善，表明背景知识是当前模型的重要瓶颈。
- 语言/音韵类失败（如方言表达、谐音梗）对上下文最为抵抗，说明现有模型缺乏内在的语言与文化知识融合能力。
- 闭源模型（如 GPT-5）主要错误类型为实体与引用错误；开源模型（如 Gemma、InternVL）则面临更普遍的文化知识缺失。

### 局限性
论文未明确讨论局限性，但从数据集设计看，仅覆盖南亚地区的孟加拉语、英语和印地语，外加少量孟加拉方言，可能无法直接推广到其他文化区域或语言。此外，研究主要聚焦于解释性任务，未涉及分类或生成任务的其他维度。

## Processing Notes

- Duplicate papers skipped: 0