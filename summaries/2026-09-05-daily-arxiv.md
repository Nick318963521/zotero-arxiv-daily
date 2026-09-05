# Daily arXiv - 2026-09-05

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-05T00:04:40
- Paper count: 10

## 1. Knowledge Acquisition During Pre-training? Large Language Models Learn Better With Auxiliary Views

- Source: arxiv
- arXiv ID: 2609.04180
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.04180v1
- PDF: https://arxiv.org/pdf/2609.04180v1
- DOI: https://doi.org/10.48550/arXiv.2609.04180

### Authors

Joseph Lee, Yidi Huang, Dokyoon Kim, Shu Yang, Li Shen

### Abstract

Gaps remain in our understanding of how large language models (LLMs) acquire knowledge during pre-training. We posit that auxiliary views, reformulations of knowledge, are causally helpful for learning. We design controlled experiments to isolate this. First, we confirm that repetition is necessary for acquisition and clarify that paraphrasing helps only at smaller batch sizes. Second, holding the token budget fixed, allocating tokens from document repetition to auxiliary views improves learning, counterintuitively, even for factual recall. Third, the effectiveness of auxiliary views is not contingent on the strength of the teacher model that generates them. Fourth, we identify forms of knowledge, contextual and foundational, that aid learning in the presence of prior knowledge gaps. Finally, we examine how these effects manifest mechanistically via layer-wise biases and compression. Together, our findings suggest that auxiliary representations of knowledge, which arise naturally in large pre-training corpora, are a key factor in the success of pre-training and offer a plausible explanation for why data diversity matters.

### 中文一句话结论
本文发现，在预训练中引入辅助视图（知识的重新表述）能显著提升LLM的知识获取，甚至在事实性回忆上优于重复，并且这一效果鲁棒，为数据多样性提供了因果解释。

### English TL;DR
The paper demonstrates that auxiliary views (reformulations of knowledge) significantly enhance knowledge acquisition in LLMs during pre-training, even outperforming repetition, and that this effect is robust across various conditions, offering insights into the role of data diversity.

### 中文详细总结
论文通过受控实验系统研究了预训练中知识获取的机制，核心发现包括：1）重复是知识获取的必要条件，但释义（paraphrasing）只在较小批次时有效；2）在固定token预算下，将原本用于文档重复的token分配给辅助视图，能提升学习效果，甚至对事实性回忆也有帮助；3）辅助视图的有效性不依赖于生成它们的教师模型强度；4）识别了两种知识形式（上下文知识和基础知识），它们有助于填补先验知识空白；5）通过层间偏置和压缩机制解释了这些效果的机理。总体而言，辅助视图是预训练成功的关键因素，为数据多样性的重要性提供了理论依据。

### 方法 / 贡献
- **方法**：设计受控实验，通过对比重复、释义和辅助视图等条件，隔离并验证辅助视图对知识获取的因果作用。
- **贡献**：首次从因果角度证明辅助视图（而非单纯重复）是LLM预训练中知识获取的关键，揭示了其优于重复且不依赖教师模型强度的特性，并提供了机制层面的解释。

### 实验或数据
摘要提及进行了受控实验，但未说明具体数据集、模型规模或技术细节。实验设计主要用于验证假设，未提供标准基准或大规模预训练验证。

### 值得关注点
- **反直觉发现**：在固定token预算下，将重复的token重新分配给辅助视图，反而能提升事实性回忆，说明辅助视图的效用可能超过简单重复。
- **鲁棒性**：辅助视图的效果不依赖于教师模型的质量，表明其本身具有独立价值。
- **机制解释**：通过层间偏置和压缩角度解释了辅助视图如何促进学习，为理解数据多样性提供了新视角。

### 局限性
摘要未明确讨论局限性。可能存在的局限包括：实验基于受控简化设置，未在大规模真实预训练场景中验证；辅助视图在实际语料库中的自然涌现程度及最优生成方式未深入探讨。

## 2. What Else Needs Fixing? Exploring Cost-Effective Test-Time Compute for Revision Propagation in Artifacts Generated Through Conversation

- Source: arxiv
- arXiv ID: 2609.03254
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.03254v1
- PDF: https://arxiv.org/pdf/2609.03254v1
- DOI: https://doi.org/10.48550/arXiv.2609.03254

### Authors

Daisuke Kikuta

### Abstract

Large Language Models (LLMs) often help users generate artifacts through iterative cycles of generation and revision in conversation. A challenge here is that, when users specify only a local change during revision, LLMs must instead identify the relevant dependencies and propagate the revision to all affected parts of the artifact. This paper studies this ability of LLMs on conversationally generated artifacts, where the artifact context and its dependencies may be embedded in the conversation history. Toward practical use, we also explore cost-effective test-time compute for this new setting. Specifically, we introduce a new benchmark for this setting, and evaluate nine revision methods, including sequential reflection and parallel sampling variants, using gpt-oss-20b/120b, gpt-5.4-mini, and qwen3.5-9b/27b/122b on the benchmark. The results show that baselines achieve accuracies of 68.3--93%, and the most cost-effective method is selecting from three parallel samples using either LLM-based or medoid selection, which improves accuracy by 2.2--9.7%. Our code and dataset are available at https://github.com/ntt-dkiku/llm-revision-propagation.

### 中文一句话结论
本文提出并评估了在对话生成的JSON工件中，通过并行采样和选择（LLM-based或medoid选择）实现成本效益高的测试时计算，可有效提升大型语言模型的修改传播准确率2.2–9.7%。

### English TL;DR
This paper introduces a benchmark and evaluates cost-effective test-time compute strategies for revision propagation in conversationally generated artifacts, finding that selecting from three parallel samples using LLM-based or medoid selection is the most cost-effective method, improving accuracy by 2.2–9.7%.

### 中文详细总结
本文研究大型语言模型（LLM）在对话生成工件中的修改传播能力——当用户只指定局部修改时，LLM需识别并更新所有依赖部分。作者提出新基准RevPropBench，包含150个人工标注样本（30开发+120测试），覆盖9个领域（如旅行行程、发票、项目计划等）和3种工件规模（10/50/100个JSON元素）。评估了9种修改方法（包括基线、顺序反思、并行采样变体）和6个LLM（gpt-oss-20b/120b, gpt-5.4-mini, qwen3.5-9b/27b/122b）。主要发现：基线完成率68.3–93%；对话历史对性能至关重要；最经济有效的方法是从三个并行样本中选择（LLM-based或medoid选择），可提升2.2–9.7%准确率。主要失败类型为遗漏必要修改。代码和数据集已开源。

### 方法 / 贡献
- 提出新基准RevPropBench，用于评估对话生成工件中LLM的修改传播能力。
- 系统评估9种修改方法（包括顺序反思、并行采样与规则/LLM选择）和6个LLM。
- 开源基准实例、数据采样与标注工具，支持可复现性和未来扩展。

### 实验或数据
- 基准：150个样本，9个领域，每种场景含3种规模（10/50/100元素），人工标注金标准补丁（JSON Patch）。
- 数据划分：10个场景（30样本）用于开发，40个场景（120样本）用于测试。
- 评估方法：9种方法（基线j/h/j+h、Reflect、OR/AND/MAJ/med/Select）。
- 模型：gpt-oss-20b/120b, gpt-5.4-mini, qwen3.5-9b/27b/122b-a10b，温度0.6，五次运行取平均。
- 指标：主要指标为完成率（验证后工件与金标准完全匹配的样本比例），辅助指标为遗漏、过度编辑、错误值。

### 值得关注点
- 对话历史（而非仅工件）对于识别依赖关系至关重要，性能排序为：仅工件 < 仅历史 < 工件+历史。
- 并行采样+LLM选择或medoid选择是最经济有效的测试时计算方法，对比顺序反思更稳定。
- 模型规模越大性能越好，主要错误类型为遗漏（miss），LLM倾向于传播不足而非过度。
- 规则合并方法（如AND）性能严重下降，说明简单多数表决不适用于该任务。

### 局限性
- 仅针对JSON格式的对话生成工件，其他格式（如自然语言文档、代码）未验证。
- 基准规模有限（150样本），可能未覆盖所有实际依赖模式。
- 依赖LLM生成合成数据和人工标注，存在标注偏差风险。
- 实验仅覆盖GPT和Qwen两个模型家族，其他LLM（如Claude、Gemini）未测试。
- 成本分析仅基于API调用次数，未考虑延迟、内存等实际部署因素。

## 3. The Impact of Synthetic Data Augmentation on Discourse-Pragmatic Function Classification

- Source: arxiv
- arXiv ID: 2609.03652
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.03652v1
- PDF: https://arxiv.org/pdf/2609.03652v1
- DOI: https://doi.org/10.48550/arXiv.2609.03652

### Authors

Sara Sorahi, Kevin Tang, Reza Kazemian

### Abstract

Synthetic data augmentation has become a common strategy for addressing class imbalance in NLP, but most approaches focus on the quantity and diversity of generated examples rather than their geometric relationship to real training data. We investigate this question in the context of discourse pragmatic function classification, a task where data sparsity is a structural feature rather than a collection artefact. Using 410 manually annotated instances of the English word look drawn from the British National Corpus, spanning four functions: Attention Signal, Directive, Discourse Marker, and Interjection. We generate synthetic training examples with Llama 3.1 and partition them by their cosine distance from real training data in RoBERTa embedding space. We compare six training conditions that differ in the placement of synthetic examples relative to the empirical decision boundary, while holding augmentation quantity constant across conditions. All augmented conditions improve macro F and accuracy over the real only baseline, but core proximal examples (NEAR) yield the largest gains in macro F (0.113), while a distance balanced mix achieves the highest accuracy (0.748). No condition improves AUC, indicating that augmentation shifts the decision boundary rather than improving the model's underlying probability estimates. These findings suggest that where synthetic examples land in representation space matters as much as how many are generated, with implications for low resource pragmatic classification more broadly.

### 中文一句话结论
合成数据增强在话语-语用功能分类中的效果取决于生成示例在表示空间中相对于真实训练数据的几何位置，靠近决策边界的示例（NEAR）带来最大的宏F值提升，而距离平衡混合则获得最高准确率，但所有条件均未改善AUC。

### English TL;DR
Synthetic data augmentation improves discourse-pragmatic function classification of the English word "look" primarily by placing generated examples near real training data in embedding space; core-proximal (NEAR) examples yield the largest macro-F gains (+0.113), and a distance-balanced mix achieves the highest accuracy (0.748), though no condition improves AUC, indicating boundary shifting rather than better probability estimates.

### 中文详细总结
本研究针对话语-语用功能分类这一低资源任务，探讨合成数据增强中“在哪里”生成示例（即几何位置）的重要性，而非仅关注数量或多样性。使用410个来自英国国家语料库（BNC）的“look”实例，标注为四种功能：注意力信号、指令语、话语标记和感叹词。通过Llama 3.1生成合成示例，并根据其与真实训练数据在RoBERTa嵌入空间中的余弦距离分为近、中、远三组。比较六个训练条件（均保持增强数量一致），所有增强条件均优于仅真实数据基线，但NEAR条件在宏F值上提升最大（+0.113），距离平衡混合条件准确率最高（0.748）。未有任何条件改善AUC，表明增强主要影响决策边界而非概率估计。研究发现提示：合成示例在表示空间中的位置与生成数量同样重要，对低资源语用分类具有启示意义。

### 方法 / 贡献
- 使用RoBERTa-base（冻结）编码所有句子，计算合成示例与同类别真实训练示例的平均余弦距离，按距离三等分（NEAR、MIDDLE、FAR）。
- 比较六个训练条件：仅真实数据基线、仅NEAR、仅MIDDLE、仅FAR、NEAR+MIDDLE+FAR混合（距离平衡）等（原文提及六种，具体列表未完全公开）。
- 贡献：明确指出合成数据增强不仅关乎数量，更关乎生成示例在表示空间中的几何位置；并结合语用功能分类任务，展示了对低资源语用分类的启示。

### 实验或数据
- 数据集：410个BNC中“look”实例，含四种功能（AS 287, DIR 71, DM 34, INTJ 18），经两名专家标注。
- 增强：Llama 3.1 8B通过函数特定提示生成，保留功能一致性，经人工质量审核。
- 训练：五个独立分层80/20训练-测试分割（仅用真实数据测试），各条件增强数量相同。
- 指标：宏F值、准确率、AUC。所有增强条件均改善宏F值和准确率，但未改善AUC。

### 值得关注点
- 核心发现：NEAR示例（靠近真实数据核心）对宏F值提升最大，表明靠近决策边界的合成示例更有效。
- 距离平衡混合条件在准确率上最优（0.748），但AUC未改善，说明增强主要调整决策边界而非改善概率估计。
- 方法创新：通过距离分区控制合成示例位置，从而分离“位置”与“数量”的影响。
- 任务特性：语用功能分类中数据稀疏是结构特征而非收集问题，增强需谨慎处理功能边界模糊问题。

### 局限性
- 仅针对英语单词“look”，且仅涵盖四种功能，结论可能不推广至其他语用项或语言。
- 合成数据仅通过Llama 3.1生成，其他LLM或提示策略可能产生不同结果。
- 数据集规模小（410个真实实例），增强后每类287个合成示例，可能仍受限于低资源设定。
- 未评估对不同分类器或嵌入模型的通用性。
- 研究未解释为何AUC未改善，以及决策边界移动的具体机制。

## 4. Unlocking Lossless Speedups in LLMs via Discrete Diffusion

- Source: arxiv
- arXiv ID: 2609.04010
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.04010v1
- PDF: https://arxiv.org/pdf/2609.04010v1
- DOI: https://doi.org/10.48550/arXiv.2609.04010

### Authors

Subham Sekhar Sahoo, Lingjie Chen, Khiem Pham, Jonathan Geuter, Chaitanya Dwivedi, Varad Pimpalkhute, Yash Akhauri, Alexander Moreno, Mikhail Yurochkin, Zhenting Wang, Mostafa Elhoushi, Nolan Dey, Shane Bergsma, Joel Hestness, John Thickstun, Eric Xing, Zhengzhong Liu

### Abstract

Large Language Models (LLMs) owe much of their success to next-token prediction (NTP), but their autoregressive (AR) structure requires slow, sequential token generation. To overcome this bottleneck, we introduce diffusion-augmented LLMs, a new class of models that defines an AR model distribution while using diffusion to draw multiple tokens in parallel from that distribution. We decouple the parameters of these models into two sets: AR weights, trained using the standard NTP objective, and lightweight diffusion weights, trained to generate multiple tokens simultaneously. The diffusion weights are learned through a simple Diffusion Distillation phase that adds negligible overhead to existing LLM training pipelines. We also introduce $Ψ$-Spec, a family of samplers that enables lossless acceleration and inference-time scaling at a fixed context length. Unlike speculative decoding, our method requires no separate draft model. Unlike diffusion LLMs (d-LLMs), it accelerates generation without sacrificing the quality of the underlying AR model. The resulting models, called Uno, can be trained from scratch or built by augmenting existing open-weight AR LLMs. Uno achieves higher throughput than leading speculative-decoding methods at every evaluated batch size and delivers up to $3\times$ speedups over the base AR model, including at the largest batch size supported by the device. Notably, our 8B Uno model outperforms the leading open d-LLM, the 26B DiffusionGemma, and the proprietary Mercury 2 across all evaluated benchmarks in agentic tool use, coding, and long-context reasoning. We release code and checkpoints at: https://s-sahoo.github.io/uno/

### 中文一句话结论
本文提出 Uno，一种通过离散扩散并行生成多个 token 实现无损加速的大语言模型，在保持自回归模型质量的同时获得最高 3 倍加速，并超越现有推测解码与扩散 LLM。

### English TL;DR
This paper introduces Uno, a diffusion-augmented LLM that achieves lossless speedups by using discrete diffusion to generate multiple tokens in parallel, outperforming speculative decoding and prior diffusion LLMs without sacrificing quality.

### 中文详细总结
论文提出一类新型模型——扩散增强大语言模型（Uno）。该模型保留自回归模型（AR）的分布定义，但利用离散扩散过程同时生成多个 token。模型参数分为两组：AR 权重（通过标准 next-token prediction 训练）和轻量扩散权重（通过扩散蒸馏学习并行生成 token）。论文还引入 Ψ-Spec 采样器族，支持在固定上下文长度下实现无损加速和推理时缩放。Uno 无需独立的草稿模型，可从零训练或扩展现有开源 AR LLM。实验显示，Uno 在各类 batch size 下的吞吐量均超过领先的推测解码方法，最大加速比达 3 倍。仅 8B 参数的 Uno 在代理工具使用、编程和长上下文推理任务上优于 26B 的 DiffusionGemma 和专有模型 Mercury 2。

### 方法 / 贡献
- 提出扩散增强 LLM 架构，将 AR 分布与离散扩散并行生成相结合。
- 参数解耦：AR 参数保持标准 NTP 训练，扩散参数通过扩散蒸馏阶段学习，训练开销极小。
- 设计 Ψ-Spec 采样器族，在固定上下文长度下实现无损加速和推理时缩放。
- 无需独立草稿模型，可与现有开源 AR LLM 兼容，支持从零训练或扩展现有模型。
- 在广泛评估中取得最高 3 倍加速，且模型质量无损。

### 实验或数据
实验在多个基准上进行，包括代理工具使用、编程和长上下文推理任务。具体数据集名称和规模在摘要中未详细说明。与推测解码方法及现有扩散 LLM（如 DiffusionGemma、Mercury 2）对比吞吐量和任务性能。

### 值得关注点
- 无损加速：在不牺牲自回归模型质量的前提下实现并行生成。
- 超越更大模型：8B Uno 击败 26B DiffusionGemma 和专有 Mercury 2。
- 无额外草稿模型需求，简单融入现有训练流程。
- 在最大设备支持 batch size 下仍保持加速优势。

### 局限性
摘要中未明确讨论局限性。作者提到代码和检查点已开源，但未说明模型可能存在的失败模式、计算资源需求或特定场景下的性能退化等。

## 5. FrameBench:A Language Understanding Benchmark Based on Frame Semantics

- Source: arxiv
- arXiv ID: 2609.03370
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.03370v1
- PDF: https://arxiv.org/pdf/2609.03370v1
- DOI: https://doi.org/10.48550/arXiv.2609.03370

### Authors

Chihiro Yano, Ryohei Sasano

### Abstract

In frame semantics, sentence comprehension is assumed to proceed by relating lexical meaning to background knowledge called semantic frames, thereby enabling readers to implicitly enrich the text with unstated information. Recent large language models (LLMs) have achieved strong performance across a wide range of downstream tasks. However, it remains unclear whether they can reproduce the kinds of implicit enrichment that humans naturally make during comprehension. To address this question, we introduce FrameBench, a benchmark grounded in frame semantics. FrameBench consists of multiple-choice questions that test whether models distinguish the frames evoked by the same verb across contexts. We construct the benchmark for English and Japanese using FrameNet-style resources and a generation-and-verification pipeline with native-speaker judgments. Our experiments on a diverse set of models reveal challenges for small models, while several large models surpass the human reference scores. We release the constructed FrameBench dataset and the code for dataset construction and evaluation at https://github.com/SasanoLab/FrameBench.

### 中文一句话结论
FrameBench 是一个基于框架语义的多选题基准，用于评估大语言模型能否区分同一动词在不同语境下引发的不同框架解释；实验发现小型模型表现困难，而多个大型模型超过了人类参考分数。

### English TL;DR
FrameBench is a multiple-choice benchmark grounded in frame semantics that tests whether language models can distinguish context-dependent interpretations evoked by the same verb. Experiments show that small models struggle, while several large models exceed human reference scores.

### 中文详细总结
本文提出 FrameBench，一个基于框架语义（Frame Semantics）的多选题基准，旨在检验大语言模型（LLM）是否具备人类在阅读中自然进行的“隐含信息丰富”能力——即根据上下文区分同一动词所激活的不同语义框架。基准构建基于 FrameNet 资源，采用 LLM（GPT-5）生成候选试题，并经过母语者人工验证。每个条目包含一个问题和四个句子，其中两个句子（基础对）设计为表层相似的高难度对比，另两个句子（扩展对）用于增加多样性。最终构建了英语（731 项）和日语（549 项）两个版本。实验在多种规模的 LLM 上进行，结果显示小型模型面临挑战，而多个大型模型在两类语言上的得分均超过人类参考分数。数据集及构建、评测代码已开源。

### 方法 / 贡献
- **提出基准**：引入 FrameBench，直接测试 LLM 对同一动词跨语境框架区分的隐式理解能力。
- **构建流程**：利用 FrameNet 资源，通过 LLM 生成试题（基础句对和扩展句对），并经过母语者正确性与可接受性双重验证。
- **双语资源**：为英语和日语两种类型学上差异较大的语言分别构建基准。
- **大规模评测**：在多种 LLM（包括不同规模和推理模式）上开展实验，揭示性能与模型规模、推理方式及语言的关联。
- **开源发布**：公开数据集及构建和评估代码。

### 实验或数据
- 数据集：英语 731 项（从 800 个框架对中过滤得到），日语 549 项（从 335 个框架对中各生成 2 个条目后过滤）。
- 实验设置：测试了多样化的 LLM 集合，包括小模型和大模型；使用人类参考分数作为对比基线。
- 结果：小型模型在该任务上表现困难，多个大型模型（如 GPT-5 等）在英语和日语上均超越人类参考分数。同时进行了行为分析和案例研究，识别错误模式和仍具挑战性的细微框架区分。
- 人类验证：母语者进行四选一正确性判断和句子可接受性评分，确保数据质量。

### 值得关注点
- 该基准不要求模型显式预测框架标签，而是通过自然语言问答题间接探测语境依赖的框架区分能力。
- 构建过程完全基于人工标注的 FrameNet 资源，而非仅依赖 LLM 的内在知识。
- 双语版本（英语和日语）增加了跨语言泛化性的评估维度。
- 大型模型在两项语言上均能超过人类参照，表明当前 LLM 具备一定的框架语义区分潜力。
- 数据集和代码完全开源，便于后续研究者复现和扩展。

### 局限性
- 基准目前仅覆盖英语和日语，尚未拓展至其他语言。
- 依赖 FrameNet 资源，可能无法覆盖所有动词或框架对。
- 生成过程使用 GPT-5，可能引入 LLM 自身的偏差。
- 小型模型在该任务上表现不足，表明基准对模型规模敏感。
- 论文未提供专门的局限性讨论，以上总结基于可获取的公开信息。

## 6. Language, Language Models, and What We're Talking About

- Source: arxiv
- arXiv ID: 2609.03577
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.03577v1
- PDF: https://arxiv.org/pdf/2609.03577v1
- DOI: https://doi.org/10.48550/arXiv.2609.03577

### Authors

Malvina Nissim

### Abstract

Language models are commonly discussed as technical artefacts, but they are obviously shaped by the linguistic worlds conveyed by data during their training. Using Italian language models as evidence, I want to bring attention to the nature of the systems which result from training and specialising models on translated and synthetic data, and further curating them, and to the meaning of testing them on equally unnatural data. Are these eventually models of Italian? Are they models of language? Does NLP still care about language? These questions yield another, more concrete question: what language do we actually want language models to produce? I argue that this question cannot be answered if we do not first consider a clearer distinction between language models designed as technical products and language models designed as tools for studying language itself. The answers then might be diverse, the languages we are talking about might be diverse, and the picture might not be as pessimistic as we fear.

### 中文一句话结论
本文以意大利语语言模型为例，指出基于翻译和合成数据微调的非英语语言模型可能并非真正的“语言模型”，呼吁明确区分作为技术产品的语言模型与作为语言研究工具的语言模型，并反思NLP领域对语言本身的关注度。

### English TL;DR
This position paper argues that language models specialized for non-English languages through translated and synthetic data may not truly model language, urging a clearer distinction between language models as technical products and as tools for studying language itself.

### 中文详细总结
本文是一篇立场论文，关注语言模型（尤其是非英语模型）的语言本质。作者以意大利语模型发展历程为案例，指出当前主流做法——在英语为主预训练模型基础上，通过机器翻译或合成数据构建指令微调数据集——导致模型学习的并非真实语言，而是“语言世界”的扭曲投影。论文梳理了从早期原生意大利语模型（GePpeTto、IT5）到基于LLaMA等基座模型的意大利语微调版本（Camoscio、Fauno、Anita、Steered-ITA），再到从零训练的Minerva系列，指出这些模型在预训练数据中意大利语占比极低（如LLaMA仅0.11%），微调数据多为翻译或合成，且评估基准同样依赖翻译数据。作者质疑这些模型是否真正“懂意大利语”或“懂语言”，并认为NLP技术正逐渐脱离对语言本身的研究。最后，论文呼吁区分两类语言模型：作为技术产品（追求性能）和作为语言研究工具（追求语言理解），并强调这一区分才能回答“我们到底想让语言模型说什么语言”这一根本问题。

### 方法 / 贡献
- **方法**：无新实验或算法，采用批判性分析立场，以意大利语模型为案例，通过文献回顾和逻辑论证展开讨论。
- **贡献**：提出对语言模型“语言性”的反思，明确区分技术产品与语言研究工具；指出非英语模型依赖翻译/合成数据带来的语言表征失真问题；呼吁NLP社区重新关注语言本身。

### 实验或数据
本文无原创实验或数据集。作者引用已公开的意大利语语言模型（GePpeTto、IT5、Camoscio、Fauno、Anita、Steered-ITA、Minerva）及其训练数据、评估基准作为论据，但未进行新实证评估。

### 值得关注点
- 指出非英语模型预训练数据中本语言占比极低（如LLaMA中意大利语仅0.11%），微调依赖机器翻译数据，导致模型并非真正学习该语言。
- 强调评估基准同样多为翻译数据，可能掩盖模型在真实语言场景中的表现缺陷。
- 提出“语言模型作为技术产品 vs 语言研究工具”的二分法，为未来研究方向提供新视角。
- 作者认为当前NLP对语言本身的兴趣减弱，呼吁回归语言本质。

### 局限性
- 作为立场论文，缺乏实证数据支持，论证主要基于作者个人观察和案例描述。
- 仅以意大利语为例，结论是否适用于其他非英语语言（尤其资源丰富语言）需进一步验证。
- 未提出具体解决方案或评估指标，仅为问题提出和方向建议。
- 对“技术产品”与“研究工具”的区分可能过于二元，实际应用中存在重叠。

## 7. Evaluating Criterion-Conditioned Behaviour of Large Language Models in Content Moderation

- Source: arxiv
- arXiv ID: 2609.03814
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.03814v1
- PDF: https://arxiv.org/pdf/2609.03814v1
- DOI: https://doi.org/10.48550/arXiv.2609.03814

### Authors

Danting Zhang, Bei Peng, Robert Loftin

### Abstract

Large language models (LLMs) demonstrate strong performance on standard content moderation benchmarks. However, these benchmarks often aggregate multiple moderation criteria into a single label, making it unclear whether models can disentangle them and reliably apply each criterion when making decisions. To study whether LLMs exhibit criterion-conditioned behaviour, we introduce Diagnostic Evaluation of COntent (DECO), a criterion-independent factorisation of content that enables controlled, criterion-level evaluation. We also introduce pairwise evaluation to compare model outputs across different criteria for the same input. Across four moderation datasets and four LLMs, we find that strong benchmark performance can hide substantial failures at the criterion level. Models struggle most when correct decisions depend not on overall harmfulness, but on the specific aspect of the content that the criterion requires them to assess. Our results highlight a key limitation of current content moderation benchmarks: strong performance on aggregated labels does not provide sufficient evidence that LLMs can reliably evaluate content with respect to individual moderation criteria. These findings call for the development of evaluation methods that explicitly measure criterion-conditioned behaviour.

### 中文一句话结论
当前大型语言模型在聚合的内容审核基准上表现优异，但无法可靠地按单一审核标准独立判断，尤其在需要区分不同危害维度时失败明显。

### English TL;DR
LLMs achieve high scores on aggregated content moderation benchmarks but fail to reliably apply individual moderation criteria, especially when decisions depend on specific aspects of harmfulness rather than overall toxicity, highlighting the need for evaluation methods that explicitly measure criterion-conditioned behaviour.

### 中文详细总结
该研究指出，现有内容审核基准通常将多条审核标准（如表面冒犯性、有害意图、可操作指南）合并为一个聚合标签，导致模型的高分可能掩盖其对单个标准的判断失败。为诊断模型是否真正根据指定标准做出判断，作者提出DECO（Diagnostic Evaluation of COntent）框架：将输入文本分解为6个可解释的标量特征（如敏感词汇、有害主题、作者立场等），再通过预定义启发式函数为每条标准生成近似标签。同时引入成对评估指标（同一输入在不同标准下的预测是否一致/不同），区分相同标签对和不同标签对准确性。在四个数据集（Civil Comments、X-Sensitive、OpenAI Moderation、Toxic-Chat）和四个LLM（如Qwen2.5-7B、Llama-3.1-70B）上的实验表明：聚合基准的高分掩盖了标准级别的严重错误；模型在需要判断意图或可操作性的标准上表现最差，且标准条件化行为不一致——当两条标准对同一输入给出不同标签时，模型常给出相同输出，未能区分不同标准。

### 方法 / 贡献
- **DECO内容表示**：将任意输入文本映射到6个0–10的标量因子（敏感词汇、危害相关性、肯定倾向、程序步骤、具体细节、中立立场），由LLM仅基于内容打分，不依赖审核标准。
- **启发式标签生成**：对表面标准（AC）、意图标准（IC）、演示标准（DC）分别定义基于DECO因子的阈值函数，生成近似标准级真实标签。
- **成对评估指标**：引入同标签对准确率（SPA）和异标签对准确率（DPA），直接观测模型预测是否随标准变化。
- **主要贡献**：揭示了聚合基准的局限性；提供了可规模化的标准级评估方法；实证表明LLM在标准条件化行为上的系统性失败。

### 实验或数据
- **数据集**：Civil Comments、X-Sensitive、OpenAI Moderation、Toxic-Chat。对前两者随机子采样（20k和5k条）保持原分布。
- **模型**：Qwen2.5-7B-Instruct、Llama-3.1-70B-Instruct 等四个指令微调LLM。
- **评估指标**：单标准准确率、SPA、DPA、假阳性与假阴性分析。
- **发现核心**：聚合准确率高（>85%），但标准级准确率差异大；IC和DC上假阴性多，AC上假阳性多；AC与DC之间的DPA最低，模型无法区分表面冒犯与可操作内容。

### 值得关注点
- 模型对表面冒犯性标准过度敏感，常错误标记“轻微、玩笑、引述”内容为不安全。
- 模型对有害意图和可操作指南的标准反应不足，漏检隐含敌意或具体步骤的案例。
- 标准条件化失败最明显：当意图标准与演示标准对同一输入给出不同标签时，模型经常输出相同判断（如两者均判安全或不安全），而非根据标准切换。
- 研究凸显了现有聚合基准的不足——高分不能保证模型按给定标准可靠评价。

### 局限性
- DECO生成的标签仅为近似的标准级真实标签，非绝对真值（仅验证子集上有人工标注一致性）。
- 启发式函数的阈值选择可能影响结果；敏感性分析虽做补充，但并非唯一合理设定。
- 仅考察了三条代表标准（外观、意图、演示），未覆盖全部审核维度。
- 评估模型数量有限（4个），且均为指令微调模型，未测试其他类型（如基础模型）。
- 成对评估指标（SPA/DPA）描述观测分布，不提供因果归因解释。

## 8. To What Extent Do Large Language Models Understand Bangla Idioms?

- Source: arxiv
- arXiv ID: 2609.03410
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.03410v1
- PDF: https://arxiv.org/pdf/2609.03410v1
- DOI: https://doi.org/10.48550/arXiv.2609.03410

### Authors

Mousumi Akter, Md. Faiyaz Abdullah Sayeedi, Nurul Labib Sayeedi, Swakkhar Shatabda

### Abstract

Idiomatic expressions are an integral part of natural language, reflecting cultural nuances and posing unique challenges for computational models, particularly in low-resource languages. In this paper, we present the first large-scale benchmark dataset of Bangla idioms, complemented by a synthetic multiple-choice question (MCQ) dataset for idiom meaning identification. We conduct a comprehensive evaluation of recent large language models (LLMs) across three idiom-related tasks: paraphrasing, idiom span detection, and meaning identification, leveraging zero-shot and few-shot prompting strategies. Our results reveal substantial variability in model performance, with no single LLM consistently outperforming others across all tasks. Notably, Phi-4-mini-instruct excels in paraphrasing, Kimi-K2-32b-instruct in span detection, and Gemini-2.5-flash in meaning identification. We believe that our datasets and analyses will provide valuable resources to guide future research in improving LLM comprehension of idiomatic expressions, particularly in Bangla and other low-resource languages.

### 中文一句话结论
本文首次构建了大规模孟加拉语习语基准数据集和合成多选题数据集，并在三个任务上评估了八个大语言模型，发现没有单一模型在所有任务上表现最佳，其中Phi-4-mini-instruct在释义上最优，Kimi-K2-32b-instruct在习语跨度检测上最佳，Gemini-2.5-flash在含义识别上最强。

### English TL;DR
This paper introduces the first large-scale Bangla idiom benchmark (10,822 entries) and a synthetic multiple-choice dataset for meaning identification. It evaluates 8 LLMs on paraphrasing, idiom span detection, and meaning identification using zero-shot and few-shot prompting. No single model excels across all tasks: Phi-4-mini-instruct leads in paraphrasing, Kimi-K2-32b-instruct in span detection, and Gemini-2.5-flash in meaning identification.

### 中文详细总结
孟加拉语习语富含文化内涵，但低资源特性使NLP模型面临挑战。本文贡献了首个大规模孟加拉语习语基准数据集，包含10,822个习语条目（其中4,772个附有使用例句），并基于此生成了合成多选题数据集（10,913个单答案样本和38,688个多答案样本）。研究评估了八个近期大语言模型（包括Kimi-K2-32B-Instruct、LLaMA-4-Scout-17B、DeepSeek-R1-Distill-LLaMA-70B、GPT-OSS-20B/120B、Phi-4-Mini-Instruct、Qwen3-32B和Gemini-2.5-Flash）在三个任务上的表现：习语句子释义、习语跨度检测以及多选题含义识别。实验采用零样本和五样本提示策略，并基于1,000个样本进行评测。结果显示模型性能在不同任务间差异显著，无单一模型全面领先。释义任务中Phi-4-mini-instruct表现最好（五样本下ROUGE-1=0.63, ROUGE-2=0.50）；跨度检测中Kimi-K2-32b-instruct最佳（一元重叠率48.25%，最小莱文斯坦距离6.27）；含义识别中Gemini-2.5-flash准确率最高（单答案0.76，多答案0.55）。

### 方法 / 贡献
1. **数据集构建**：手动从开放许可来源收集10,822条孟加拉语习语，经去重和最小归一化处理，并由母语者验证；其中4,772条包含例句。2. **合成MCQ数据集**：为每个习语生成4个选项（正确含义+干扰项），构建单答案和多答案两种设置。3. **全面评测**：在零样本和五样本提示下，评估8个LLM在释义（使用ROUGE、BERTScore、余弦相似度）、跨度检测（一元重叠率、莱文斯坦距离）和MCQ含义识别（准确率）三个任务上的表现。

### 实验或数据
- **数据集统计**：总习语10,822，含例句4,772（44.1%），含多个含义2,624，平均每条含义数1.23，最大16。MCQ单答案10,913，多答案38,688。单词长度分布：答案含义2–8词，MCQ问题10–14词，使用例句8–35词。
- **实验设置**：从数据集中随机选取1,000样本进行评测，提示模板见表2（论文内）。使用Groq API访问模型。
- **主要结果**：释义任务Phi-4-mini-instruct平均得分0.73；跨度检测Kimi-K2-32b-instruct一元重叠48.25%且莱文斯坦距离6.27；MCQ含义识别Gemini-2.5-flash单答案准确率0.76，多答案0.55。多数模型在五样本下性能提升。

### 值得关注点
- 首个针对孟加拉语习语的大规模基准数据集，填补低资源语言空白。
- 合成MCQ数据集支持单/多答案设置，便于深入评估模型对多义习语的理解。
- 揭示不同模型在习语子任务上的专长差异，为未来模型选择和改进提供指导。
- 实验覆盖多个知名LLM，结果具有较强参考价值。

### 局限性
- 评估仅基于1,000个样本，可能无法完全反映模型在所有习语上的表现。
- 数据集虽然经过人工验证，但可能仍存在标注偏差或覆盖不足（如未考虑方言变体）。
- 模型性能在不同任务间差异显著，表明当前LLM对低资源语言习语的整体理解能力有限，尤其在多含义识别上准确率偏低（多答案最高仅0.55）。
- 论文未讨论模型在更复杂语境（如幽默、讽刺）中的习语理解能力。

## 9. Lngram v2: Latent N-Gram Memory with Interpretable Discrete Representations

- Source: arxiv
- arXiv ID: 2609.03426
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.03426v1
- PDF: https://arxiv.org/pdf/2609.03426v1
- DOI: https://doi.org/10.48550/arXiv.2609.03426

### Authors

Yunao Zheng, Bin Wen, Xiaojie Wang

### Abstract

Transformers lack a native lookup mechanism, requiring repeated dense computation to recognize and reuse local static patterns. Lngram v1 introduces tokenizer-independent conditional memory through discrete latent n-gram addressing, but its memory capacity is coupled with the backbone width, limiting scalability due to high parameter and activation costs. We propose Lngram v2, which decouples the number of routes, memory dimension, and backbone width, and introduces a context-aware grouped-query attention readout to scale memory capacity independently. A zero-value Sink and counterfactual surrogate gradients further improve readout selectivity and routing trainability while preserving hard discrete addressing. Experiments across vision--language models (VLMs) of different scales show consistent improvements, including successful scaling to a 30B-parameter model. Compared with Lngram v1, Lngram v2 substantially reduces both total and activated memory parameters while maintaining or improving language modeling performance. Further analysis shows that its discrete IDs preserve substantial semantic structure of continuous hidden states, enabling semantic recovery from IDs alone and stable ID--semantic associations across datasets. These results establish Lngram v2 as an efficient and scalable latent conditional memory mechanism whose discrete addresses also provide a structured interface for analyzing internal model representations.

### 中文一句话结论
Lngram v2 通过解耦路由数量、记忆维度和骨干宽度，并引入上下文感知的组查询注意力读出机制，实现了可扩展的离散潜 n-gram 记忆，在降低参数成本的同时提升了视觉-语言模型性能，并能成功扩展到 30B 参数规模。

### English TL;DR
Lngram v2 introduces a scalable latent n-gram memory mechanism that decouples routing, memory dimension, and backbone width, uses context-aware grouped-query attention readout, and improves trainability with zero-value Sink and counterfactual surrogate gradients. It reduces memory costs while scaling VLMs to 30B parameters and preserves semantic structure in discrete IDs.

### 中文详细总结
Lngram v2 是针对 Lngram v1 的改进。Lngram v1 通过离散潜 n-gram 寻址实现了与分词器无关的条件记忆，但其记忆容量与骨干宽度耦合，导致参数和激活成本高，限制了可扩展性。Lngram v2 将路由数量、记忆维度和骨干宽度解耦，使得记忆容量可以独立扩展。它采用上下文感知的组查询注意力（grouped-query attention）读出机制，并引入零值 Sink 和反事实替代梯度（counterfactual surrogate gradients）来改善读出的选择性和路由的可训练性，同时保持硬离散寻址。在不同规模的视觉-语言模型（VLM）上的实验表明，Lngram v2 持续改进性能，成功扩展到 30B 参数模型。与 Lngram v1 相比，Lngram v2 显著减少了总记忆参数和激活参数，同时保持或提升了语言建模性能。进一步分析显示，其离散 ID 保留了连续隐藏状态的语义结构，仅凭 ID 即可恢复语义，且 ID-语义关联在不同数据集上保持稳定。

### 方法 / 贡献
- **解耦设计**：将路由数量、记忆维度和骨干宽度解耦，使记忆容量可独立于骨干网络扩展，克服了 Lngram v1 中记忆容量受限于骨干宽度的问题。
- **上下文感知的组查询注意力读出**：通过分组查询注意力机制，根据上下文内容从离散记忆槽中动态读出信息，提高记忆检索的灵活性和效率。
- **训练优化技巧**：引入零值 Sink（zero-value Sink）和反事实替代梯度，提升硬离散路由的可训练性和读出的选择性，避免不可微问题。
- **语义可解释性**：离散 ID 编码了连续隐藏状态的语义结构，可通过 ID 恢复语义信息，且 ID-语义关联跨数据集稳定，为模型分析提供结构化接口。

### 实验或数据
- 在不同规模的视觉-语言模型（VLM）上进行了实验，包括成功扩展到 30B 参数模型。
- 与 Lngram v1 对比，Lngram v2 显著降低了总记忆参数和激活记忆参数，同时语言建模性能保持或提升。
- 通过分析离散 ID 的语义恢复能力及跨数据集的一致性，验证了离散表示保留语义结构的特性。
- （论文摘要未明确提及具体数据集名称和指标数值，但实验涵盖了多个 VLM 规模。）

### 值得关注点
- **可扩展性**：首次将离散潜记忆有效扩展到 30B 参数模型，证明解耦设计在大规模模型中的可行性。
- **效率提升**：在减少参数和激活成本的同时保持性能，对实际部署有重要意义。
- **可解释性**：离散 ID 作为模型内部表示的接口，支持语义分析，有助于理解 Transformer 内部机制。
- **广泛适用性**：方法不依赖特定分词器，可应用于多种视觉-语言架构。

### 局限性
- 论文未明确讨论其局限性。可能隐含的挑战包括：离散路由训练仍需替代梯度近似，可能引入训练不稳定；解耦设计增加了超参数（路由数、记忆维度等）调节的复杂性；实验主要针对视觉-语言模型，在其他模态或纯语言模型上的泛化性有待验证。

## 10. From Zero to Hero: An Open LLM Ecosystem for Armenian

- Source: arxiv
- arXiv ID: 2609.03350
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.03350v1
- PDF: https://arxiv.org/pdf/2609.03350v1
- DOI: https://doi.org/10.48550/arXiv.2609.03350

### Authors

Erik Arakelyan, Khatun Avetisyan, Meri Davtyan, Heghine Grigoryan, Nane Khachatryan, Hayk Shahsuvaryan, Henrik Sergoyan, Vahan Martirosyan

### Abstract

Pretraining data for Armenian, a morphologically rich and low-resource language, is scarce, and no open Armenian LLM has been released with the data and recipe needed to reproduce it. To address this gap, we curate and release two datasets. ArmWeb is an extensively validated corpus of 4.37M Armenian news documents. ArmSTEM is a parallel English-Armenian collection of 373K math and science problems with step-by-step solutions, translated into Armenian and verified through both answer-preserving LLM judgment and human evaluation. Continued pretraining of Gemma-4-E4B on these datasets yields arm-gemma-e4b, which outperforms every existing open Armenian model as well as its unadapted base, and is the first open Armenian LLM with complete training data and recipe. Our ablations show that news-only continued pretraining improves fluency while eroding knowledge, a pattern we also observe in existing Armenian models, and that a small share of verified translated STEM data reverses the loss. We further find that the largest public Armenian corpora overlap web-derived evaluation panels heavily, including a train/test self-overlap inside FineWeb-2. We openly release all data, models, and code.

### 中文一句话结论
本文为亚美尼亚语构建了首个完整开放生态：发布经过验证的新闻语料 ArmWeb 和亚美尼亚语 STEM 翻译语料 ArmSTEM，并基于 Gemma-4-E4B 继续预训练得到 arm-gemma-e4b，其表现超过现有开放模型，且发现仅用新闻预训练会损失知识，加入少量验证过的 STEM 数据可逆转该损失。

### English TL;DR
This paper releases an open Armenian LLM ecosystem, including two curated datasets (ArmWeb news corpus and ArmSTEM verified translated STEM problems) and a continued-pretrained model (arm-gemma-e4b) that outperforms existing open models, with a study showing that news-only pretraining erodes knowledge while adding a small share of verified STEM data reverses the loss.

### 中文详细总结
该研究针对亚美尼亚语（低资源、形态丰富）缺乏开放可复现大语言模型的问题，发布了两个数据集和一个模型。ArmWeb 是 437 万篇亚美尼亚语新闻文档（33 亿 Gemma token），经语言识别、去重、泄漏门控和 13-gram 去污处理；ArmSTEM 是 37.3 万道翻译为亚美尼亚语的数学与科学题（其中 32.4 万含逐步解答），并用 LLM 判断和人工评估验证质量。在这些数据上继续预训练 Gemma-4-E4B 得到 arm-gemma-e4b，在亚美尼亚语任务上超过所有现有开放模型及未适配基线。消融实验显示，仅用新闻继续预训练可提升流畅性但显著损失知识（Belebele 最高降 21.2 个百分点），而加入少量验证过的 STEM 数据不仅恢复损失，还使平均准确率超过基线 2.2 个百分点。此外，研究发现最大的公开亚美尼亚语语料与评估集存在 7.9%–17.4% 的重叠，包括 FineWeb-2 自身的训练/测试泄漏。

### 方法 / 贡献
- 发布 **ArmWeb**：437 万篇亚美尼亚语新闻文档（约 33 亿 Gemma token），来自单一运营者 2011–2026 年的爬虫数据，附完整流水线文档（语言识别、MinHash 去重、泄漏检查、13-gram 去污），并带有每篇文档的来源元数据。
- 发布 **ArmSTEM**：37.3 万道英–亚平行数学/科学题（32.4 万含步骤解答），来自 GSM8K、AceReason-Math、OpenScience 等，经机器翻译和答案保持验证（placeholder 掩码翻译、语言识别、盲解重算）及人工评估（300 题中 299 题有效）。
- 发布模型 **arm-gemma-e4b**：在 Gemma-4-E4B 上以 69% ArmWeb / 6% ArmSTEM / 20% 英文回放 / 5% 代码的混合继续预训练，首个提供完整训练数据和配方的开放亚美尼亚语模型。
- 方法学发现：新闻全量继续预训练导致知识遗忘；降低学习率恢复约 2/3 损失；加入少量 epoch 限制的验证过 STEM 数据不仅逆转损失，还能保留流畅性提升。
- 基准卫生研究：公开大型亚美尼亚语语料与评测集重叠严重，强调去污必要性。

### 实验或数据
- 评估套件：包含 6 项亚美尼亚语似然任务（如 Belebele、INCLUDE、SynDARin 等）和 10 项评测集的去污扫描。
- 消融实验：410M 参数模型、4.6B SP token 预算下对比 ArmWeb 与多个公开语料（CulturaX、HPLT-v2、FineWeb-2），ArmWeb 在新闻域约高 10 个百分点。
- 模型结果：arm-gemma-e4b 在所有开放亚美尼亚语模型及未适配基线上取得最高平均准确率。
- 污染扫描：公开语料（CulturaX-hy、HPLT-v2-hy、FineWeb-2-hy）与评测集的文档级重叠率为 7.9%–17.4%，其中 FineWeb-2 自身训练与测试分割有泄漏。
- 人工验证：ArmSTEM 采样 300 题，两位母语者独立评定 299 题为有效，标注者间完全一致。

### 值得关注点
- 首次为亚美尼亚语提供完全开放、可复现的数据+模型+配方完整生态。
- 明确揭示“新闻只提升流畅性但损害知识”这一迁移模式，且现有亚美尼亚语模型也存在同样现象。
- 验证了高质、经过验证的翻译 STEM 数据对于知识保持的关键作用。
- 发现最大公开语料的评测污染问题，提醒社区对爬虫语料上的亚美尼亚语评估结果持谨慎态度。

### 局限性
摘要和预览内容中未提及明确的局限性。

## Processing Notes

- Duplicate papers skipped: 0