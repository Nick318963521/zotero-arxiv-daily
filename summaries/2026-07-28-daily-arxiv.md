# Daily arXiv - 2026-07-28

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-28T23:44:37
- Paper count: 10

## 1. Beyond Shapley: An Influence-Based Data Auditing Pipeline for LLM Alignment and Evaluation

- Source: arxiv
- arXiv ID: 2607.22766
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.22766v1
- PDF: https://arxiv.org/pdf/2607.22766v1
- DOI: https://doi.org/10.48550/arXiv.2607.22766

### Authors

Yunting Song, Matthew Watson, Peter Grabowski, Jun Qin

### Abstract

The alignment of Large Language Models (LLMs) is increasingly bottlenecked by data quality. As datasets scale, massive preference and instruction-tuning corpora inevitably accumulate hidden structural contradictions, safety risks, and systemic human annotation errors. Standard dataset auditing methods, such as semantic deduplication or LLM-as-a-judge, struggle to capture the actual predictive impact of individual records and often miss deep functional rule clashes. To address this, we introduce a scalable, inference-only data valuation pipeline that approximates the Shapley value without iterative model retraining. By mapping semantic k-NN neighborhoods into a directed graph, our framework evaluates data utility directly through a reference LLM's probability distribution using zero-shot and one-shot conditional log-likelihood shifts. Our pipeline then translates these predictive influence scores into localized advantage metrics to isolate gradient-conflicting records. We demonstrate the pipeline's efficacy in sanitizing two heavily vetted alignment datasets. First, applying our pipeline to the HelpSteer2 dataset reduced the manual audit search space by 99.1%, successfully uncovering falsely-labeled records across diverse failure modes. Second, applying our automated audit strategy to Anthropic's HH-RLHF training and evaluation splits identified thousands of hidden safety and factual preference inversions. Crucially, by extending this audit to the evaluation split, we expose severe vulnerabilities in current benchmark integrity: highly capable models frequently predict the safer or more helpful response, only to be penalized by objectively flawed human ground-truth labels. Overall, our work provides a mathematically grounded, highly efficient diagnostic tool to uncover human label failures, sanitize evaluation benchmarks, and ensure the integrity of LLM alignment data.

### 中文一句话结论
本文提出一种基于推理、无需重训练的数据审计流程，通过在一跳语义邻域内近似Shapley值，有效识别LLM对齐数据中的人为标注错误与结构矛盾，并暴露基准评测中的标签缺陷。

### English TL;DR
This paper introduces a scalable, inference-only pipeline that approximates Shapley values via conditional log-likelihood shifts to detect hidden contradictions and human annotation errors in LLM alignment datasets, reducing manual audit search space by 99.1% and exposing flawed ground-truth labels in evaluation benchmarks.

### 中文详细总结
LLM对齐的关键瓶颈正转向数据质量，大规模偏好数据中常累积结构矛盾、安全风险与系统性标注错误。现有方法（如语义去重或LLM作为评判）难以捕捉每条记录的真实预测影响。本文提出一种可伸缩的推理式数据估值流程，无需迭代模型重训练。通过将语义k近邻映射为有向图，利用参考LLM的零样本与单样本条件对数似然变化评估数据效用，进而转化为局部优势指标以隔离梯度冲突记录。在HelpSteer2数据集上，该流程将人工审计空间缩减99.1%，成功发现多种虚假标注；在Anthropic的HH-RLHF训练与评测划分中，识别出数千隐藏的安全与偏好反转问题。特别地，对评测划分的审计揭示了当前基准的严重脆弱性：高性能模型常预测更安全或更有帮助的回复，却被客观上错误的人类标注惩罚。该工作提供了数学严谨、高效的诊断工具，用于发现人类标签失败、净化评测基准、确保对齐数据完整性。

### 方法 / 贡献
- **基于影响的估值框架**：提出可伸缩的推理式管道，通过O(k)次前向传递近似Shapley值，适用于生成式LLM，无需重训练或聚类。
- **结构矛盾检测**：利用有向图与条件对数似然偏移，量化每条记录对邻域的预测贡献（主动/被动优势），自动定位梯度冲突记录。
- **基准漏洞揭示**：将审计扩展到评测集，证明人类标注中存在系统性安全与偏好反转，导致模型被不公平扣分。

### 实验或数据
- **数据集**：HelpSteer2、Anthropic HH-RLHF（训练与评测划分）。
- **实验结果**：HelpSteer2上人工审计空间缩减99.1%；HH-RLHF中识别数千隐藏安全与偏好反转；评测集审计暴露大量基准标签缺陷。

### 值得关注点
- 无需重训练，完全推理驱动，适合大规模数据集。
- 能够发现语义去重等传统方法遗漏的功能性矛盾。
- 将数据估值从分类/回归任务推广至生成式LLM与偏好对数据。
- 提供“独一无二分数”等拓扑度量，辅助边缘案例识别。

### 局限性
- 依赖预训练参考LLM与嵌入模型的质量，后者可能影响邻域构建的准确性。
- 仅通过单样本上下文变化近似边际贡献，未考虑更复杂的多步交互。
- 大规模数据集的邻域图构建仍需要Embedding与相似度计算开销，虽远小于重训练，但嵌入维度与k值选择缺乏理论指导。
- 论文摘要中未明确讨论其他潜在限制（如对长尾或极低概率邻域的敏感性）。

## 2. The Cross-Domain Generalization Cost of Offensive Language Detection

- Source: arxiv
- arXiv ID: 2607.23512
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.23512v1
- PDF: https://arxiv.org/pdf/2607.23512v1
- DOI: https://doi.org/10.48550/arXiv.2607.23512

### Authors

Ruixing Ren, Junhui Zhao, Xiaoke Sun, Qiuping Li

### Abstract

Offensive language detection models generally suffer performance degradation when deployed across datasets and across languages, yet most existing studies stop at reporting this phenomenon and lack a systematic methodology for decomposing the causes of degradation into attributable components and quantifying the cost of remediation. This paper proposes a diagnosis and optimization framework composed of three coordinated technical components. First, a zero-shot transfer loss decomposition that separates the performance degradation from OLID to MLMA into two independently measurable components, namely dataset effect and language effect. Second, a controlled fine-tuning protocol that quantifies both adaptation efficiency and the hidden damage inflicted on the source task by comparing few shot learning curves under continued fine-tuning and cold-start starting points. Third, three joint training strategies incorpo rating temperature sampling and experience replay, which offer a controllable Pareto trade-off between improving multilingual capability and preserving source-task performance. Experiments built on this framework show that the dataset effect dominates the zero-shot transfer loss and substantially outweighs the language effect. Few-shot adaptation without a replay mechanism, though data-efficient, inflicts source task damage 4 to 9 times greater than that of the joint training strategies, and its damage magnitude is highly unstable. The three joint training strategies trade 3.2 to 4.1 percentage points of source-task performance for 8.1 to 42.6 percentage points of multilingual capability gain, forming a clear and controllable Pareto trade-off.

### 中文一句话结论
本文提出了一个诊断与优化框架，将跨域泛化损失分解为数据集效应和语言效应，并发现无回放的少样本适应对源任务性能的损害比联合训练高4到9倍。

### English TL;DR
This paper proposes a diagnosis and optimization framework for offensive language detection that decomposes cross-domain generalization loss into dataset and language effects, reveals that few-shot adaptation without replay inflicts 4–9 times greater source-task damage than joint training, and demonstrates that joint training strategies enable a controllable Pareto trade-off between multilingual capability gains and source-task performance.

### 中文详细总结
本文针对冒犯性语言检测模型在跨数据集和跨语言部署时性能下降的问题，提出了一个包含三个协调技术组件的诊断与优化框架：首先，零样本迁移损失分解将性能下降分离为数据集效应和语言效应；其次，受控微调协议通过对比继续微调和冷启动下的少样本学习曲线，量化适应效率和源任务隐藏损伤；第三，三种联合训练策略（结合温度采样和经验回放）提供了可控的帕累托权衡。实验表明数据集效应主导零样本迁移损失，远大于语言效应；无回放的少样本适应带来的源任务损伤是联合训练的4-9倍，且极不稳定；三种联合训练策略以3.2-4.1个百分点的源任务性能损失换取8.1-42.6个百分点的多语言能力提升。

### 方法 / 贡献
- 提出零样本迁移损失分解方法，将性能下降独立量化为数据集效应和语言效应，而非仅报告聚合下降。
- 设计受控微调协议，通过对比继续微调和冷启动的少样本学习曲线，首次量化少样本适应对源任务的隐藏损伤。
- 比较三种联合训练策略（温度采样、经验回放等），首次在冒犯性检测任务上量化多语言性的代价，提供可控帕累托权衡。
- 所有实验共享同一数据划分和评估指标，实现诊断、适应和优化结果直接对比。

### 实验或数据
- 使用两个公开数据集：OLID（英文，13,203样本）和MLMA（英文、法文、阿拉伯文，共约12,942样本）。
- 采用mBERT作为骨干模型，构建两级级联分类器（子任务A：是否冒犯；子任务C：目标类型）。
- 对MLMA每种语言均匀划分一半为保留集（不参与训练），一半为候选池。
- 四种方法学上不同的实验均得出相同结论：控制跨语言泛化的主导因素是目标语言数据本身的类别平衡性，而非语言类型距离。

### 值得关注点
- 将跨数据集和跨语言研究结合在同一框架内，而非孤立进行。
- 首次直接量化多语言性诅咒在具体任务上的代价。
- 发现少样本适应虽数据高效但源任务损伤巨大且不稳定。
- 联合训练提供可控的帕累托权衡：3.2-4.1%源任务性能损失换取8.1-42.6%多语言能力提升。
- 代码开源：https://github.com/renruixing/The-Cross-Domain-Generalization-Cost-of-Offensive-Language-Detection

### 局限性
论文未明确讨论以下局限：仅使用mBERT作为骨干模型，未探索其他多语言预训练模型（如XLM-R等）的适用性；实验仅在OLID和MLMA两个数据集上进行，未验证更广泛的数据集组合；对子任务B（是否有明确目标）因标签映射困难而跳过，可能限制了框架的全面性；联合训练策略中3.2-4.1%的源任务性能损失虽可控但实际部署中仍需权衡；少样本适应的损伤不稳定性未给出深层机制解释。

## 3. From Data to Device: ELMOD An Efficient German-First 2.7B Language Model for Mobile Inference

- Source: arxiv
- arXiv ID: 2607.24585
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.24585v1
- PDF: https://arxiv.org/pdf/2607.24585v1
- DOI: https://doi.org/10.48550/arXiv.2607.24585

### Authors

Darina Gold, Alexander Schwirjow, Viktor Haag, Viktor Hangya, Joel Schlotthauer, Fabian Küch, Luzian Hahn

### Abstract

We present ELMOD - Efficient Language Model for On-Device Deployment - a compact (2.7B) German language model designed for efficient inference on resource-constrained hardware. ELMOD was trained on a limited computational budget (55k H100 GPU hours) using exclusively publicly available data. We developed a suite of German-specific data pre-processing, which differ from English-oriented counterparts in their handling of morphological variation, compounding, and orthographic conventions. Furthermore, we introduced a quality filtering and rephrasing step, which increased the instructional quality of the data, improved performance during the annealing phase, and reduced overall compute requirements. Thanks to our architectural model and data choices, including prefiltering, our educational-quality filtering and rephrasal to raise the educational-quality, ELMOD is the strongest performer in its size class (<3B), matching the performance of 7B-parameter models in German.

### 中文一句话结论
ELMOD是一个2.7B参数的高效德语语言模型，在有限计算预算下训练，性能达到同尺寸最佳，并匹配7B参数模型在德语基准上的表现。

### English TL;DR
ELMOD is a compact 2.7B parameter German language model trained on a limited budget (55k H100 GPU hours) using publicly available data. It achieves state-of-the-art performance among models under 3B parameters and matches 7B models on German benchmarks, leveraging German-specific data preprocessing and quality filtering for efficient on-device deployment.

### 中文详细总结
本文提出了ELMOD（Efficient Language Model for On-Device Deployment），一个2.7B参数的德语语言模型，专为资源受限硬件（如移动设备）上的高效推理设计。模型仅使用55k H100 GPU小时的计算预算和完全公开的数据进行训练。作者开发了一套针对德语的数据预处理流程，包括处理形态变化、复合词和正字法惯例，以及一个教育质量过滤和重写步骤，提高了数据质量并减少了计算需求。ELMOD在小于3B参数的模型中表现最佳，并且在德语ARC、HellaSwag和MMLU等基准测试上匹配了7B参数模型的性能。模型还进行了指令微调，并展示了在设备上部署的可行性。

### 方法 / 贡献
1. 提出了一个完整的德语语言模型构建流程，从数据收集到设备端部署。
2. 开发了德语特定的数据预处理方法，包括基于规则和基于分类器的过滤，以及教育质量过滤和重写。
3. 在有限计算预算下训练出2.7B参数模型，性能超越同尺寸模型，并达到更大模型水平。
4. 提供了模型创建过程的透明度，包括数据来源（CommonCrawl、CodeParrot等）和过滤步骤。

### 实验或数据
- 训练数据：45%德语数据（来自CommonCrawl）、45%英语数据（来自DCLM）、10%代码数据（来自CodeParrot），总计约4T tokens。
- 计算资源：55k H100 GPU小时。
- 评估：在德语ARC、HellaSwag、MMLU等基准上测试，ELMOD在<3B模型中表现最佳，并匹配7B模型。
- 消融实验：对数据过滤、学习率退火等步骤进行了消融研究。

### 值得关注点
- 模型紧凑（2.7B参数），适合移动端和边缘设备部署。
- 针对德语进行了专门优化，而非作为多语言模型的副产品。
- 使用了教育质量过滤和重写步骤，提高了数据效率和模型性能。
- 实现了与7B模型相当的性能，参数仅为后者的约1/3。

### 局限性
- 模型主要针对德语和英语，对其他语言的能力有限。
- 未进行大量的后训练优化（如指令微调深度优化），指令遵循能力可能不如专门优化的模型。
- 训练数据仅使用公开数据，可能包含偏差或噪声，尽管经过了过滤。
- 在非德语任务上的性能未评估，可能无法与通用大模型相比。

## 4. ESF-Bench: Benchmarking Challenging Slot-Filling Scenarios for Real-World Enterprise Applications

- Source: arxiv
- arXiv ID: 2607.23326
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.23326v1
- PDF: https://arxiv.org/pdf/2607.23326v1
- DOI: https://doi.org/10.48550/arXiv.2607.23326

### Authors

Toby Liang, Gopal Sarda, Sagar Davasam, Vikas Yadav

### Abstract

The rapid rise of large language models (LLMs) has driven transformative adoption across enterprises. However, deploying these models in real-world settings presents unique challenges due to complex system constraints and unexpected user behaviors. Among these applications, slot filling is essential for converting unstructured input into structured, actionable data. In this work, we introduce ESF-Bench, a challenging Enterprise Slot Filling benchmark consisting of 810 multi-turn samples and 6530 slots over 8 unique domains. Curated using a taxonomy of the 57 most challenging slot-filling scenarios observed during real-world enterprise deployments, ESF-Bench exposes notable limitations in current state-of-the-art LLMs, with GPT-OSS-120b low successfully extracting slots for only 20.7% of benchmark samples. To support continued research in this area, we publicly release the benchmark dataset, taxonomy, and accompanying evaluation code on GitHub.

### 中文一句话结论
ESF-Bench是一个面向企业级应用的复杂槽填充基准，包含810个多轮样本和6530个槽，覆盖8个领域，揭示了当前最先进LLM（如GPT-OSS-120b）仅能成功提取20.7%的槽。

### English TL;DR
ESF-Bench is a challenging enterprise slot-filling benchmark with 810 multi-turn samples and 6,530 slots across 8 domains, curated from a taxonomy of 57 real-world scenarios, that reveals state-of-the-art LLMs (e.g., GPT-OSS-120b) achieve only 20.7% successful slot extraction.

### 中文详细总结
本文提出了ESF-Bench，一个专注于企业级应用复杂场景的槽填充基准。该基准包含810个多轮对话样本和6530个槽，覆盖IT服务管理、客户服务、人力资源等8个领域。通过一个包含57个真实部署中观察到的挑战性场景的分类体系进行构建。实验表明，当前最先进的LLM（如GPT-OSS-120b）在ESF-Bench上仅能成功填充20.7%的样本，揭示了显著的能力差距。数据集、分类体系和评估代码已在GitHub上公开。

### 方法 / 贡献
- 构建了包含57个场景的细粒度分类体系，涵盖选择、条件、推理、多源信息、长/多值、对话理解、个性化、模式约束、意外用户行为、相对值、修正和槽重置等12个类别。
- 生成包含810个多轮样本、6530个槽的基准数据集，覆盖8个企业领域，并整合多源上下文元数据（如用户画像、知识库文章等）。
- 将槽填充与意图检测解耦，专注于评估槽提取本身，并提供细粒度评估指标以定位模型薄弱环节。

### 实验或数据
- 数据集：810个样本，6530个槽，平均每个提示4617.4个token，每个模式8.06个槽，8个领域，57个分类场景。
- 评估模型：Gemini 2.5 Flash Dynamic-Thinking、GPT-5.1 High、GPT-OSS-120b High、Qwen3-32b-Think、Ministral3 14b Reasoning等。
- 最佳模型（Gemini 2.5 Flash Dynamic-Thinking）的模糊联合目标准确率（F-JGA）为33.3%，标记槽准确率为80.9%；而GPT-OSS-120b Low仅为20.7% F-JGA和76.5%标记槽准确率。

### 值得关注点
- 基准专为真实企业部署中的复杂、意外场景设计，如多跳推理、条件填充、跨源冲突、个性化等。
- 分类体系支持细粒度性能诊断，可揭示模型在不同场景类型下的具体弱点。
- 数据集和代码开源，促进企业级槽填充研究的持续发展。

### 局限性
- 基准专注于槽填充，未涉及意图检测或端到端任务导向对话的其他组件。
- 样本和领域数量有限（810个样本，8个领域），可能无法覆盖所有企业场景。
- 依赖人工标注的分类体系，可能引入主观偏差，且场景间的交互效应未被充分研究。
- 实验仅评估了特定LLM，未涵盖所有主流模型或微调变体。

## 5. LEX-EC: A Lexical Evidence-Channel Audit Framework for Zero-Shot LLM Personality Classification in Black-Box Settings

- Source: arxiv
- arXiv ID: 2607.24435
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.24435v1
- PDF: https://arxiv.org/pdf/2607.24435v1
- DOI: https://doi.org/10.48550/arXiv.2607.24435

### Authors

Brittany Harbison, Ashok K. Goel

### Abstract

Large language models may easily assign personality labels from text, but model interpretability remains an open problem. To address this gap, we introduce LEX-EC, a reusable black-box audit framework combining prevalence and agreement diagnostics with controlled lexical ablation to distinguish marginal-distribution effects from trait-associated signal recoverable under restricted evidence. Using this framework, we illustrate how various text genres may exhibit sharply different profiles: free-form essay text contains the broadest, but still weak, signal; in graduate student introductions, an observable Extraversion association weakened after masking; and single Facebook statuses yield little stable evidence even in a trait-balanced sample, indicating a possible lower bound of content or length. Masking topical and demographic content weakened some associations while leaving others detectable from function words, affective terms, and cognitive-style vocabulary. Linguistic prompting shifted model self-explanations but did not eliminate topical content. LEX-EC jointly evaluates classification prevalence, item-level association, chance-corrected agreement, persistence under lexical restriction, and prompt sensitivity in model-generated explanations. Across datasets, models, and prompts, LEX-EC characterizes how trait associations may vary with available lexical evidence, introducing a novel application of lexical methods to black-box interpretability in personality labeling.

### 中文一句话结论
LEX-EC框架通过词项证据通道和受控消融技术，系统评估了黑盒零样本大语言模型在人格分类中信号的真实性，揭示了不同文本类型下信号强度的显著差异。

### English TL;DR
LEX-EC is a black-box audit framework that uses lexical evidence-channel diagnostics and controlled ablation to evaluate the reliability of zero-shot LLM personality classifications across text genres, content masking, and prompting conditions.

### 中文详细总结
本研究提出LEX-EC（词项证据通道审计）框架，用于在黑盒设置下审计零样本大语言模型（LLM）的人格分类。该框架结合了流行率诊断、一致性诊断和受控词项消融技术，以区分边缘分布效应和可恢复的特质相关信号。研究跨三个数据集（平均词数17-672词）和五个闭源模型进行了实验，主要发现包括：自由形式随笔文本包含最广泛但仍较弱的信号；研究生自我介绍中的外倾性关联在遮蔽后减弱；单条Facebook状态在特质平衡样本中也几乎无法提供稳定证据。遮蔽主题和人口统计内容削弱了部分关联，但功能词、情感词和认知风格词汇仍保留了部分可检测信号。语言提示改变了模型的自我解释，但并未消除主题内容的影响。LEX-EC联合评估了分类流行率、项目级关联、机会校正一致性、词项限制下的持久性以及提示敏感性，为黑盒人格标记可解释性引入了词项方法的新应用。

### 方法 / 贡献
1. **LEX-EC框架**：一种可复用的黑盒审计框架，包含五个处理阶段：匹配预测、解释审计、流行率审计、项目级评估和跨条件比较。
2. **词项消融**：通过遮蔽主题和人口统计内容（保留LIWC、Empath和NRC-EmoLex定义的情感、认知和功能词层），测试信号在受限词项证据下的存活性。
3. **多维度评估**：同时评估流行率偏差、项目级关联（平衡准确率、Cohen's κ）、机会校正一致性和提示敏感性。
4. **跨条件系统比较**：在三个文本长度/类型条件、五个闭源模型和多种提示下进行系统比较。

### 实验或数据
- **数据集**：三个文本类型——MyPersonality单条Facebook状态（~17词，164用户，经混合整数线性规划平衡五特质分布）、研究生论坛介绍（~89词，226学生）、Pennebaker-King随笔（~672词，完整集n=2468，子集n=226）。
- **模型**：五个闭源模型：GPT-4o-mini、GPT-4o、o3-mini、GPT-5.4-mini、Claude Haiku 4.5。
- **评估指标**：预测流行率、Cohen's κ、平衡准确率、原文与遮蔽后比较。
- **结果**：随笔文本包含最广泛但弱的信号；研究生介绍中外倾性关联在遮蔽后减弱；Facebook状态几乎所有条件下均无稳定证据。遮蔽主题和人口统计内容削弱了部分关联，但功能词、情感词和认知风格词汇仍保留了少量可检测信号。

### 值得关注点
1. **黑盒框架创新性**：不依赖模型内部表示，仅通过输入-输出行为诊断隐藏层信号。
2. **条件的系统性**：跨文本长度梯度（17-672词）和三种截然不同的文本类型（自然短文本、自我呈现文本、开放写作）。
3. **方法透明性**：词项遮蔽使用公开外部词典（画押词、Affective词、认知风格词），避免依赖模型内部表示的自我报告。
4. **文本最小值指示**：单条Facebook状态的无信号结果可能表明人格推断的最小内容或长度下限。

### 局限性
1. **标签局限性**：所有评估基于二进制高低标签，限制了粒度，与人格特质的连续性质不符。
2. **词项消融局限性**：遮蔽方法可能移除原文的修辞和语境含义，并非完全无损干预。
3. **数据集有限**：仅分析三个特定文本类型，未涵盖对话、正式写作等其他场景。
4. **时效性问题**：闭源模型版本可能被更新，实验结果仅反映特定快照的行为，不必然代表未来版本。
5. **解释分析初步**：模型自我解释的检查较初步，未进行深度语义或逻辑一致性分析。

## 6. Similarity All The Way Up: Multilingual Generalization in LLMs Relies on Language-Level Similarity Structures

- Source: arxiv
- arXiv ID: 2607.22699
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.22699v1
- PDF: https://arxiv.org/pdf/2607.22699v1
- DOI: https://doi.org/10.48550/arXiv.2607.22699

### Authors

Supantho Rakshit, Adele Goldberg, Henry Conklin

### Abstract

As Large Language Models (LLMs) grow more capable across diverse tasks, their (in)ability to generalize remains difficult to quantify and poorly understood beyond limited domains. In particular, LLMs are known to struggle generalizing multilingually, to languages outside of English, and that are poorly attested in their training data. To understand why this may be, and what enables some models to perform better than others, we turn to a long history of work across the cognitive sciences, arguing that successful generalization derives from appropriate representations in similarity space. We look at how well LLMs' representations capture the hierarchical similarity structure between distinct languages. Strikingly, we show LLMs' latent representations largely recover the hierarchical structure of the Indo-European language family tree -- grouping languages that are members of the same subfamily closely together in representation space. Furthermore, we show that the degree to which models reflect the similarity structure of languages correlates with their performance on XNLI, a multilingual natural language inference benchmark. This extends classic work on similarity-driven generalization at scale, showing how models that represent similar languages similarly generalize better from one language to another.

### 中文一句话结论
大语言模型的多语言泛化能力取决于其内在表征空间能否准确捕捉语言之间的层次相似结构——表征相似语言越相似的模型，跨语言迁移性能越好。

### English TL;DR
LLMs' multilingual generalization is driven by how well their internal representations capture the hierarchical similarity structure of languages—models that represent similar languages similarly achieve better cross-lingual performance.

### 中文详细总结
本研究通过分析12个大语言模型（如BERT、RoBERTa、mT5、XLM、Pythia等）的内部表征，发现模型能够隐式地恢复印欧语系38种语言之间的层次相似结构（即语言谱系树）。具体来说，模型在表征空间中会自动将属于同一语支（如日耳曼语族、罗曼语族）的语言聚类在一起，且这种聚类程度与模型在跨语言自然语言推理基准（XNLI）上的零样本迁移性能显著正相关。研究进一步表明，明确接受多语言训练的模型比仅训练英语的模型更贴近参考语言树；此外，这种表征结构在预训练早期就已出现。该工作将认知科学中“基于相似性的泛化”理论扩展到大规模语言模型，揭示了表征几何决定跨语言泛化能力的内在机制。

### 方法 / 贡献
- **方法**：从每个LLM的隐藏状态中，通过软离散化密度估计（soft density estimation）学习每种语言的条件分布 \(P(\hat{Z}|\text{language})\)；利用Jensen-Shannon散度计算语言间的表征距离矩阵，并对该矩阵进行UPGMA层次聚类得到表征树；使用三种树距离度量（共表型相关系数、子树核、路径核）将其与独立构建的参考树（基于Heggarty等人2023年的贝叶斯词汇统计模型）比较。
- **贡献**：首次系统地验证了大语言模型在多语言层面复现了认知科学中的“相似性驱动泛化”原理——不仅限于词汇或概念，而是跨越整个语言层次；证明表征相似结构与跨语言迁移性能之间的因果关联；提供了量化语言间层次相似结构的新框架。

### 实验或数据
- **数据**：38种书面现代印欧语言（来自5个语支：罗曼、日耳曼、印度-雅利安、斯拉夫、波罗的，以及3个独立语言）；从多语言C4数据集中为每种语言随机抽取7500个句子用于表征估计；参考树来自Heggarty等人（2023）的贝叶斯系统发育树。
- **实验**：在12个LLM上计算表征树与参考树的三种距离，并与其在XNLI（多语言自然语言推理）上的准确率计算斯皮尔曼秩相关系数。还对比了多语言变体（如Multilingual BERT）与纯英语变体（如English BERT），以及分析了Pythia模型在预训练不同阶段的表征演化。

### 值得关注点
- **跨领域的理论整合**：将认知科学中经典的相似性泛化理论（Shepard, Tenenbaum）首次大规模应用到多语言LLM分析中，为理解模型泛化提供了新的理论视角。
- **层次结构的重要性**：研究发现，模型不仅捕获“相邻语言”的相似性，更关键的是能够恢复高层次（语族、语支）的嵌套关系，而这一点与泛化性能的关联更强（路径核和共表型相关显著，子树核不显著）。
- **训练信号的启发**：多语言模型比单语言模型更精确地恢复语言树，说明训练数据的语言多样性促使模型学习更有效的共享结构。同时，表征结构在预训练早期（几千步内）即出现，表明该结构是预训练的自然产物而非后期微调。

### 局限性
- **仅限印欧语系**：当前结论能否推广到其他语系（如汉藏语系、尼日尔-刚果语系）尚不确定，因为印欧语系可能具有更规则的结构。
- **参考树并非绝对真实**：参考树来自统计模型（Heggarty 2023），可能混淆同源与借用关系，且对应的是现代语言之间的统计相似性而非历史谱系。
- **模型范围有限**：主要分析较早的LLM（如BERT、RoBERTa变体），未包含最新模型（如GPT-4、Llama-3），且部分模型（如mT5）未参与XNLI相关性分析。
- **任务依赖**：仅使用XNLI作为泛化度量，该任务本身存在争议（如可能无法充分反映真实语言理解）。

## 7. DataOrchestra: Learning to Orchestrate Per-Example Curation of Pretraining Data

- Source: arxiv
- arXiv ID: 2607.24717
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.24717v1
- PDF: https://arxiv.org/pdf/2607.24717v1
- DOI: https://doi.org/10.48550/arXiv.2607.24717

### Authors

Zhen Huang, Yikun Wang, Shijie Xia, Pengfei Liu

### Abstract

Pretraining data processing is critical to the downstream performance of Large Language Models (LLMs). However, many existing approaches define a fixed processing strategy at the corpus or domain level and apply it uniformly to many examples, without adapting to the needs of each example. We propose DataOrchestra, a framework that unifies different processing operations and orchestrates an example-specific pipeline for each example. Given a chunk of pretraining data, an orchestrator decides whether to drop, untouch, or clean it. For a chunk to be cleaned, it selects one or more downstream operations, ranging from programmatic editing to different forms of LLM-based rewriting. For each rewriting step, it further generates a concrete instruction, which is executed by the corresponding downstream tool model. We pretrain models from 0.5B to 7B from scratch on web data processed by DataOrchestra and observe stable average gains over individual data-processing methods across 11 benchmarks. DataOrchestra is also effective for math continued pretraining and outperforms stronger processing baselines, while reducing processing compute by skipping unnecessary downstream operations.

### 中文一句话结论
DataOrchestra 提出了一种自适应、逐样本的预训练数据处理方法，针对每个数据块动态决定丢弃、保留或清洗，并选择具体操作和指令，在多个基准上稳定提升 LLM 性能，同时降低处理计算成本。

### English TL;DR
DataOrchestra adaptively curates each pretraining data example by deciding whether to drop, keep, or clean it, and when cleaning, selects example-specific operations and instructions, consistently improving LLM performance across 11 benchmarks under different model sizes while reducing processing compute.

### 中文详细总结
现有预训练数据处理方法通常对整个语料库或领域使用固定策略，未能适应每个样本的独特需求。DataOrchestra 提出一个统一框架，将不同处理操作（丢弃、保留、清洗）整合，并为每个数据块动态编排流水线。清洗时，可依次选择噪声修剪（NP）、表面修正（SR）或教学增强（PA）等操作，并为每个改写步骤生成具体指令。通过教师 LLM 提出初始方案，再根据工具模型执行反馈进行进化，最终训练出一个轻量级编排器。在 0.5B 到 7B 模型上的实验表明，DataOrchestra 在 11 个基准上平均优于单一处理方法，并在数学继续预训练中同样有效，同时因跳过不必要的操作而减少计算量。

### 方法 / 贡献
- 提出 DataOrchestra 框架，整合多种数据处理操作，实现逐样本自适应的流水线编排。
- 设计编排器训练流程：通过教师 LLM 生成初始方案，结合工具模型执行反馈进化，获得高质量训练数据（30万对）。
- 验证方法在多个网络数据集（RedPajama-V2、DCLM-RefinedWeb、C4、FineWeb）及数学数据集（OpenWebMath、MegaMath）上的有效性，模型规模从 0.5B 到 7B 均表现稳定。
- 开源编排器模型及完整代码，促进社区研究。

### 实验或数据
- **实验设置**：从零预训练 0.5B、1B、3B、7B 模型，使用 DataOrchestra 处理的网络数据。
- **数据集**：RedPajama-V2、DCLM-RefinedWeb、C4、FineWeb（网络数据）；OpenWebMath、MegaMath（数学继续预训练）。
- **工具模型**：NP 阶段使用 0.6B 噪声修剪模型，SR 和 PA 阶段使用 4B 的 Qwen3-4B 改写模型。
- **评估基准**：11 个主流 NLP 下游任务基准（具体名称未在摘要中详细列出，但论文正文有提及）。
- **结果**：平均性能优于单一数据方法，且在数学继续预训练中提升科学推理基准表现，同时减少处理计算量。

### 值得关注点
- **逐样本自适应**：每个数据块独立决定丢弃、保留或清洗，并选择具体操作，克服了固定流水线的不足。
- **计算效率**：通过跳过不必要的处理步骤（如对高质量样本保持原样），显著降低计算开销。
- **跨设置有效性**：在多个网络数据集、不同模型规模以及数学继续预训练场景下均表现一致。
- **指令生成**：为每个改写步骤生成具体指令，而非使用通用提示，提升了处理质量。

### 局限性
- 编排器训练依赖教师 LLM 生成初始方案，并需要工具模型执行反馈，该过程可能计算成本较高。
- 当前工具模型规模较小（最大 4B），若使用更大模型可能进一步提升效果，但会带来额外开销。
- 实验主要基于英文网络数据和数学数据，对其他语言或领域（如代码、多模态）的泛化能力有待验证。
- 编排器决策基于 chunk 级别的处理，未考虑文档全局上下文，可能影响跨 chunk 的一致性。

## 8. DomainPilot: Domain-Level Loss-Guided Two-Stage Data Mixture Optimization for Efficient Language Model Fine-Tuning

- Source: arxiv
- arXiv ID: 2607.22769
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.22769v1
- PDF: https://arxiv.org/pdf/2607.22769v1
- DOI: https://doi.org/10.48550/arXiv.2607.22769

### Authors

He Zhang

### Abstract

The training efficacy of large language models (LLMs) is fundamentally constrained by the quality and composition of training data. Existing dynamic data scheduling methods face critical limitations in industrial-scale pretraining and supervised fine-tuning (SFT): data selection incurs prohibitive O(N) costs on terabyte-scale corpora, mixture optimization schemes introduce severe I/O bottlenecks or require training auxiliary reference models, and sample-level reweighting strategies rely on loss signals that conflate noise, difficulty, and novelty.
  We present DomainPilot, a domain-level loss-guided two-stage data mixture optimization framework. DomainPilot introduces token-level domain loss monitoring to capture per-domain learning dynamics during training without halting the data pipeline. Building on these signals, we propose a Scaling Law guided coarse optimization stage that fits domain-specific convergence curves and derives a principled prior for mixture adjustment. A subsequent Mixing Law guided fine optimization stage refines the mixture by modeling cross-domain interaction effects through controlled sweep experiments. The entire mechanism is realized via a patch-based architecture that injects domain-aware loss computation into existing training frameworks (e.g., MindSpeed/Megatron-LM) with only ~30 lines of framework-specific adapter code.
  We validate DomainPilot on the Qwen3-1.7B model during SFT. Compared to the original data mixture, our optimized mixture achieves improvements of +2% on MMLU-Redux, +1.8% on AIME24, +3.8% on LiveCodeBench v5, and +3.6% on BFCL v3, without increasing total data volume or training cost. These results demonstrate that domain-level training signals provide an effective, lightweight alternative to expensive data selection or auxiliary model training for mixture optimization.

### 中文一句话结论
DomainPilot 提出了一种基于域级损失引导的两阶段数据混合优化框架，在不增加数据量或训练成本的前提下，通过轻量级、可迁移的补丁式架构显著提升大语言模型微调性能。

### English TL;DR
DomainPilot introduces a domain-level loss-guided two-stage data mixture optimization framework for efficient large language model fine-tuning, which uses token-level domain loss monitoring and Scaling Law/Mixing Law guided optimization to improve performance on benchmarks like MMLU-Redux and AIME24 without increasing data volume or training cost.

### 中文详细总结
DomainPilot 针对大语言模型训练中数据混合优化面临的三大挑战：数据选择成本过高、混合优化存在 I/O 瓶颈或需训练辅助模型、样本级重加权信号混淆噪声与难度，提出了一种域级损失引导的两阶段优化框架。其核心包括：1）令牌级域损失监测，在不中断训练流水线的情况下捕获各域学习动态；2）基于 Scaling Law 的粗优化阶段，通过拟合域特定收敛曲线推导混合调整先验；3）基于 Mixing Law 的精细优化阶段，通过控制扫描实验建模跨域交互效应。该框架通过补丁式架构实现，仅需约 30 行适配代码即可集成到现有训练框架（如 MindSpeed/Megatron-LM）。在 Qwen3-1.7B 模型 SFT 验证中，优化后的混合方案在 MMLU-Redux、AIME24、LiveCodeBench v5、BFCL v3 上分别提升 +2%、+1.8%、+3.8%、+3.6%，且不增加总数据量或训练成本。

### 方法 / 贡献
- **令牌级域损失监测**：在预处理时为每个 token 标记域 ID，前向传播时按域聚合损失，通过 All-Reduce 同步，额外开销 <1%。
- **Scaling Law 粗优化**：拟合域特定损失收敛曲线 $L_i(D)=a_i D^{-\alpha_i}+b_i$，提取收敛损失、学习速度、初始振幅三个参数，结合四因子奖励分数计算域混合比例调整先验。
- **Mixing Law 精细优化（计划）**：以粗优化输出为中心，通过二阶展开建模跨域交互效应，进一步细化比例。
- **补丁式架构**：分为框架无关算法层（纯 PyTorch）和框架特定适配层（约 30 行代码），支持灵活部署在工业级训练框架。

### 实验或数据
- **模型**：Qwen3-1.7B，在监督微调（SFT）阶段验证。
- **基准测试**：MMLU-Redux（+2%）、AIME24（+1.8%）、LiveCodeBench v5（+3.8%）、BFCL v3（+3.6%）。
- **对比基线**：原始数据混合方案（未公开具体比例）。
- **关键结论**：优化后混合方案在多个推理和代码任务上提升显著，且不增加总数据量或训练成本。论文未披露训练数据集的详细规模或来源。

### 值得关注点
- **轻量高效**：仅基于域级损失信号，无需昂贵的全数据遍历、辅助模型训练或 I/O 重排，适合万亿 token 级预训练和 SFT。
- **可迁移性**：补丁式架构设计使得方法可快速适配不同工业训练框架（如 MindSpeed/Megatron-LM），解决了现有方法（如 DataFlex）的框架耦合问题。
- **信号去噪**：域级损失聚合了数千 token 信号，平均了样本级噪声，更清晰反映真实学习动态，并缓解了样本级损失中噪声、难度、新颖性混淆的问题。

### 局限性
- **Mixing Law 精细优化仍为计划中工作**，论文仅验证了 Scaling Law 粗优化阶段的效果，跨域交互建模尚未实际应用。
- **仅测试了单一模型（Qwen3-1.7B）**，在更大模型或不同架构上的泛化性有待验证。
- **依赖域标签**：要求训练数据已按域划分（工业场景通常具备），但缺乏域标签的场景需额外聚类步骤，论文未讨论。
- **未涉及样本级噪声过滤**：框架关注域级混合比例调整，无法直接识别并剔除低质量样本。

## 9. Frustratingly Simple Black-Box Adaptation of Language Models via Logit Bias

- Source: arxiv
- arXiv ID: 2607.22837
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.22837v1
- PDF: https://arxiv.org/pdf/2607.22837v1
- DOI: https://doi.org/10.48550/arXiv.2607.22837

### Authors

Ofek I. Cohen, Lior Shani, Aviv Rosenberg, Ankur Samanta, Tal Wagner, Yonathan Efroni

### Abstract

Many organizations aim to adapt language models for internal use, both to improve performance on domain-specific tasks and to address privacy concerns around sensitive data. However, such adaptation remains non-trivial: it often requires operationally challenging fine-tuning of open-source models or ad hoc prompt optimization. We study a minimal alternative based on a simple API-level control: allowing users to bias the model's logits with a user-defined vector. We develop a black-box method for learning a single context-independent logit-bias vector, added at every decoding step, without modifying model weights or requiring gradients. Starting from a KL-regularized reinforcement learning (RL) objective, we characterize when such a fixed logit-bias vector can approximate the optimal prefix-dependent correction and derive a closed-form inverse-propensity estimator from rollouts, rewards, and token probabilities. Empirically, this simple decoding-time intervention improves over base models on mathematical and reasoning benchmarks while using far fewer trainable parameters than conventional fine-tuning. Our results suggest that learned logit bias is a lightweight mechanism for adapting language models under minimal access requirements.

### 中文一句话结论
本文提出一种极简的黑盒语言模型适配方法，仅通过学习一个固定的、与上下文无关的logit偏置向量，在解码时逐token加到模型输出上，即可在推理任务上取得性能提升，无需修改模型权重或访问梯度。

### English TL;DR
This paper introduces a black-box method for adapting frozen language models by learning a single, context-independent logit-bias vector applied at every decoding step, which approximates the optimal KL-regularized reinforcement learning policy and improves reasoning performance with minimal computational overhead.

### 中文详细总结
许多组织需要在特定领域任务或隐私保护场景下适配语言模型，但现有方法通常需要复杂的微调或提示优化。本文研究了一种极简替代方案：仅通过API层级的控制——在解码时向logits添加一个用户定义的固定偏置向量δ，不修改模型权重，不依赖梯度，完全黑盒操作。研究从KL正则化的强化学习目标出发，推导出固定logit偏置向量近似最优前缀相关校正的条件，并提出了一个闭式逆概率加权估计器，仅需采样轨迹、奖励值和token概率即可求解。实验表明，该方法在数学和推理基准测试上超越基础模型，且参数量远少于传统微调。作者认为，学习到的logit偏置是一种轻量级适配机制，适用于最低权限要求的访问场景。

### 方法 / 贡献
- **核心方法**：提出“黑盒logit偏置适配”——学习一个固定向量δ，在每一步解码时添加到冻结语言模型的logits上，不修改权重、不依赖梯度。
- **理论贡献**：从KL正则化RL目标出发，推导固定偏置向量近似最优策略的条件，并给出闭式逆概率加权估计器，直接从采样轨迹、奖励和token概率中学习δ。
- **轻量性**：仅需训练一个全词汇表大小的向量（约几万参数），相比传统微调（数亿参数）极为高效。

### 实验或数据
- **任务**：数学推理和推理基准测试（如数学题、逻辑推理任务）。
- **设置**：使用冻结基础模型，仅学习一个logit偏置向量δ，通过黑盒采样和奖励信号优化。
- **结果**：在多个基准上，该方法性能超过基础模型，且参数量远少于传统微调方法。
- **数据**：论文未披露具体数据集名称或规模，仅提及使用数学和推理基准。

### 值得关注点
- **极简性**：方法极其简单，仅需API层级的logit偏置控制，无需微调、提示优化或权重访问。
- **隐私友好**：模型权重不变，可用作黑盒服务，适应隐私敏感场景。
- **理论支撑**：从KL正则化RL视角给出了偏置学习的理论基础和闭合形式解。
- **计算高效**：训练参数极少（词汇表大小），推理时无额外计算开销。

### 局限性
- **表达力有限**：固定、上下文无关的δ无法编码复杂的、依赖前缀的行为，仅能捕捉跨上下文的稳定校正模式。
- **应用场景受限**：仅适用于需要稳定、全局性校正的任务（如控制输出长度或格式），难以处理条件性强的任务。
- **实验规模不足**：论文未提供大规模或多样化的实验数据集、消融实验或与其他方法的系统对比，实证结果仅限于少量基准。

## 10. From transcription to semantic corpus analysis: unsupervised learning of sentence representations for ancient languages

- Source: arxiv
- arXiv ID: 2607.24542
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.24542v1
- PDF: https://arxiv.org/pdf/2607.24542v1
- DOI: https://doi.org/10.48550/arXiv.2607.24542

### Authors

Th{é}otime de la Selle

### Abstract

Automatic Text Recognition (ATR) now supplies digital humanities with large volumes of unstructured, heterogeneous, and often noisy text in ancient languages. Downstream semantic analysestext reuse identification, alignment, and semantic search-rely on sentence embeddings, yet existing methods transfer poorly to ancient languages: generic multilingual encoders underperform, specialized language models yield anisotropic representation spaces, and labeled similarity data is unavailable. We study two fully unsupervised strategies - TSDAE and contrastive sentence embedding (CSE) - that adapt a specialized token-level language model into a corpus-specific sentence encoder using only raw sentences. On the philologically central case of biblical reuse in patristic literature (2,935 expert-verified parallels in Latin and Ancient Greek, from Augustine, Jerome, and Athanasius), we decompose reuse identification into two separately evaluated tasks-binary detection and correspondence retrieval-and benchmark the adapted encoders against multilingual, specialized, distilled, and supervised fine-tuned baselines, as well as on artificially noised data simulating HTR artifacts and scribal abbreviations. The adapted encoders outperform all baselines on both tasks, with complementary profiles: TSDAE leads detection given a large in-domain corpus, while CSE leads retrieval, reaches its optimum with as few as 4-8k raw in-domain sentences-a few tens of seconds of training on a laptop GPU-and transfers across works and authors, including to noisy post-ATR text when retrained directly on it. UMAP atlases relate the geometric effect of each strategy to the measured gains, and the full pipeline-segmentation, fine-tuning, cross-corpus semantic search-is made available to non-specialists through the online tool Paraphrasis.

### 中文一句话结论
本研究证明，通过 TSDAE 或对比句子嵌入（CSE）的完全无监督学习，可以将词级语言模型高效适应为特定语料库的句子编码器，从而在拉丁语和古希腊语教父文献的文本复用检测与检索任务上超越现有基准。

### English TL;DR
This paper demonstrates that unsupervised adaptation of token-level language models via TSDAE or contrastive sentence embedding (CSE) yields effective sentence representations for ancient languages, outperforming baselines on text reuse detection and retrieval tasks in Latin and Ancient Greek patristic literature.

### 中文详细总结
针对古代语言自动文本识别（ATR）产生的大量无标注、含噪声语料，现有方法（通用多语言编码器性能不佳、专用语言模型表示空间各向异性、缺乏标注数据）难以支撑语义分析。该文研究了两种完全无监督策略——TSDAE（去噪自编码）和对比句子嵌入（CSE）——仅利用原始句子将预训练的词级语言模型调整为语料库专用句子编码器。在教父文献对圣经引用的核心任务上（2935个专家平行句，涵盖拉丁语和古希腊语），将文本复用识别分解为二分类检测和对应检索两个子任务。实验表明，两种方法均优于多语言、专用、蒸馏和微调基准，且互补：TSDAE在领域内大语料上检测更优，CSE在检索上更优，仅需4-8k条原始句子即可达到最优，且可跨作品与作者泛化，甚至直接适应噪声文本。最终提供在线工具Paraphrasis实现全流程。

### 方法 / 贡献
1. 提出基于TSDAE和CSE的无监督训练方法论，并系统研究其参数化（训练语料规模与领域性、噪声变体）。
2. 将文本复用识别分解为检测（二分类）与检索（信息检索）两个独立评估任务。
3. 构建并公开拉丁语和古希腊语教父文献共2935条专家验证的圣经引用并行数据。
4. 在人工噪声数据上验证两种策略对HTR伪影和抄写缩写的鲁棒性。
5. 通过UMAP图解释每种策略对表示空间几何结构的影响，作为文献学探索工具。
6. 提供在线工具Paraphrasis，支持文本分割、模型微调与跨语料语义检索。

### 实验或数据
使用拉丁语和古希腊语教父文献（奥古斯丁、哲罗姆、亚他那修）中专家验证的2935条圣经引用平行句。将文本复用识别分为：a)二分类检测（判断句子是否含引用）；b)对应检索（在源语料中寻找最相似句）。对比基准包括：多语言编码器（LaBSE、multilingual-E5）、专用词级模型（LatinBERT、LaBerta、GreBerta、Logion）、蒸馏编码器（SPhilBerta）、监督微调编码器（Loci similes）。另在模拟HTR误差和缩写的噪声数据上测试鲁棒性。

### 值得关注点
1. CSE仅需4000-8000条原始句子即可达到最佳检索性能，在笔记本GPU上训练仅需数十秒，效率极高。
2. 两种策略互补：TSDAE在领域内大语料上检测最强，CSE在检索上最优，且可跨作品和作者迁移。
3. 当直接在HTR输出噪声文本上重新训练时，模型能成功适应后ATR的误差和缩写。
4. 全程代码和在线工具（Paraphrasis）面向非专家用户开放，降低古代语言数字人文研究门槛。

### 局限性
1. 仅验证了圣经引用这一特定文本复用类型，对其他形式（如典故、文学借用）的适用性尚未评估。
2. 实验语料限于拉丁语和古希腊语，其他古代语言（如古汉语、古埃及语）未涉及。
3. 未深入探讨当领域内语料极小时（<1000句）两种策略的表现差异。
4. 噪声实验仅基于模拟数据，实际HTR误差可能更复杂（如混合误识别、不同手写风格）。
5. 对模型训练后的表示空间（如各向异性程度）未做定量分析，仅通过UMAP可视化解释。

## Processing Notes

- Duplicate papers skipped: 0