# Daily arXiv - 2026-08-28

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-28T06:11:09
- Paper count: 10

## 1. VFA: Empowering Multilingual MLLMs via Vision-Free Adaptation

- Source: arxiv
- arXiv ID: 2608.26155
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.26155v1
- PDF: https://arxiv.org/pdf/2608.26155v1
- DOI: https://doi.org/10.48550/arXiv.2608.26155

### Authors

Yixia Li, Yaqing Shi, Zhiwen Ruan, Dongdong Zhang, Lingjie Jiang, Shaohan Huang, Yun Chen, Guanhua Chen, Furu Wei

### Abstract

Multimodal large language models have advanced rapidly, yet most remain English-centric, as scaling multilingual multimodal instruction tuning is limited by the scarcity and high cost of high-quality non-English image-text supervision. Although multilingual text data is abundant, naive textual fine-tuning can disrupt vision-language alignment and induce catastrophic forgetting. We propose Vision-Free Adaptation (VFA), a framework that decouples multilingual language enhancement from visual alignment by composing complementary task vectors over a shared LLM backbone. Specifically, we fine-tune a base LLM on multilingual text data to derive a multilingual task vector, which is then merged with the vision-aligned task vector of an MLLM. Experiments on five MLLMs across six multilingual multimodal benchmarks show consistent improvements while preserving both general multimodal and text-only capabilities. Moreover, using less than 2% of the text data, VFA narrows the gap to the fully multimodal-trained model, demonstrating its data efficiency.

### 中文一句话结论
本文提出 Vision-Free Adaptation (VFA)，通过将多语言任务向量与视觉对齐任务向量组合，仅使用纯文本数据即可高效提升多语言多模态大模型的性能。

### English TL;DR
Vision-Free Adaptation (VFA) enhances multilingual MLLMs by decoupling language enhancement from visual alignment through complementary task vector merging, achieving consistent improvements on multilingual benchmarks with less than 2% of the text data while preserving multimodal capabilities.

### 中文详细总结
VFA 框架旨在解决多语言多模态大模型（MLLM）因高质量非英语图像-文本数据稀缺而难以扩展的问题。该方法将多语言语言增强与视觉对齐解耦：首先在基座 LLM 上用多语言纯文本数据微调得到多语言任务向量，再将该向量与现有多语言 MLLM 的视觉对齐任务向量合并，从而在不破坏视觉-语言对齐的前提下注入多语言能力。实验在五个 MLLM 和六个多语言多模态基准上均取得一致提升（如 LLaVA-OneVision-1.5 8B 提升 +2.99 平均分），且仅使用 100K（<2%）纯文本数据即可大幅缩小与全多模态训练模型之间的差距，同时保持通用多模态和纯文本能力。

### 方法 / 贡献
- 提出 VFA 框架，将多语言增强与视觉对齐解耦，避免直接文本微调导致的模态干扰和灾难性遗忘。
- 基于任务向量组合（权重平均、任务算术、TIES-Merging），将微调得到的多语言任务向量与 MLLM 的视觉对齐任务向量合并，视觉模块（编码器、投影）保持冻结。
- 多语言任务向量可一次训练、多次复用，显著降低多语言 MLLM 的构建成本。
- 不需要多语言图像-文本对，仅依赖丰富的纯文本数据，数据效率高。

### 实验或数据
- 模型：五个不同规模和家族的 MLLM（如 LLaVA-OneVision-1.5 8B/4B、Idefics3-8B 等）。
- 基准：六个多语言多模态基准（MaXM、xGQA、xMMMU、XM100、MaRVL、M3Exam），并辅以通用多模态和纯文本多语言测试（OCRBench、TyDiQA 等）。
- 数据：仅使用约 100K 纯文本样本（<2% 的典型多模态数据量）进行多语言微调。
- 主要结果：平均多语言多模态性能提升（如 +2.99），且通用多模态和纯文本能力几乎不受影响。

### 值得关注点
- 完全依赖纯文本数据，突破多语言图像-文本数据稀缺瓶颈，成本极低。
- 任务向量可跨模型复用（共享相同基座 LLM 的 MLLM），训练一次即可用于多个模型。
- 合并后模型不增加推理延迟或内存开销，保持原有架构。
- 数据效率突出：仅用 2% 的文本数据即接近全多模态训练效果。

### 局限性
论文未明确讨论局限性。但从方法推断，VFA 的效果高度依赖于基座 LLM 本身的多语言预训练质量，对于极低资源语言，纯文本数据可能仍不足；此外，视觉模块完全冻结可能限制对文化特定视觉概念的适应。

## 2. Leveraging Large Language Models for Systematic Literature Review of Disease Spread Models

- Source: arxiv
- arXiv ID: 2608.26150
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.26150v1
- PDF: https://arxiv.org/pdf/2608.26150v1
- DOI: https://doi.org/10.48550/arXiv.2608.26150

### Authors

Orhan Yagizer Cinar, Timur Emre Ozkose, Emma Von Hoene, Amira Roess, Taylor Anderson, Hamdi Kavak

### Abstract

Recent advancements in Large Language Models (LLMs) have created new opportunities to streamline and potentially automate many research processes, including systematic literature reviews (SLRs). This study reports an LLM pipeline development for extracting model-relevant information from 536 peer-reviewed agent-based modeling papers. We compare the results with those of a human-conducted SLR. Our results show paper-level accuracies of approximately 77.95% for GPT-4.1 and 81.67% for GPT-5.0. Field-level accuracy ranges from 32.40% to 100.00%, with more complex or subjective fields performing less reliably. Importantly, we find that agreement between LLMs is a potential indicator of output quality: low agreement may signal hallucinations, whereas high agreement combined with low accuracy may point to noise or errors in the human dataset. Overall, our study provides practical insights into prompt development and highlights both the potential and limitations of using LLMs for full-scale SLRs in the modeling and simulation domain.

### 中文一句话结论
本研究评估了GPT-4.1和GPT-5.0在系统文献综述中提取疾病传播模型信息的能力，发现论文级准确率约为78%和82%，但复杂字段准确率较低，且模型间一致性有助于识别错误。

### English TL;DR
This study demonstrates that large language models (GPT-4.1 and GPT-5.0) can automate data extraction for systematic literature reviews of disease spread models with moderate accuracy (77–82% at paper level) and that agreement between models may help identify errors in human-extracted or LLM-generated data.

### 中文详细总结
本研究旨在评估大规模语言模型（LLM）在系统文献综述（SLR）中自动提取数据的可行性与局限性。研究团队开发了一套LLM流水线，使用GPT-4.1和GPT-5.0通过OpenAI API对536篇COVID-19代理建模论文进行零样本数据提取，并将结果与人工提取的基准数据进行对比。结果显示，论文级准确率GPT-4.1为77.95%，GPT-5.0为81.67%；字段级准确率范围为32.40%至100%，其中复杂或主观字段（如模型校准、不确定性报告）表现较差。研究发现，模型间一致性可作为输出质量的潜在指标：低一致性可能指示幻觉，而高一致性结合低准确率则可能提示人工数据集中的噪声或错误。总体而言，该研究为LLM在建模与仿真领域进行大规模SLR数据提取提供了实践见解，既展示了潜力，也揭示了局限性。

### 方法 / 贡献
- **方法**：基于OpenAI API构建完全可编程的LLM流水线，统一使用结构化提示词（zero-shot），指定JSON输出格式，将536篇论文的PDF输入模型，逐篇提取21个预定义字段的数据。使用Jaccard指数和重叠系数比较LLM输出与人工基准。
- **贡献**：首次在规模（N=536）上评估LLM在建模与仿真领域SLR中的自动提取性能；对比GPT-4.1与GPT-5.0两个版本；提出模型间一致性作为输出质量检测指标，有助于识别人工或LLM数据的错误。

### 实验或数据
- **数据集**：536篇COVID-19代理建模论文（2020–2023年），人工提取数据由两名独立评审员共识确定，平均人-人间一致性为74%。
- **实验设置**：使用OpenAI API，GPT-4.1与GPT-5.0零样本配置（温度1.0，top-p 1.0），每篇论文一次API调用。输出经规则修复及二次LLM恢复后与人工数据逐字段比较。

### 值得关注点
- 模型间一致性可作为质量指标：低一致可能提示幻觉，高一致结合低准确可能提示人工数据噪声。
- 字段级准确率差异大（32%–100%），复杂/主观字段（如不确定性报告）准确率低，显式信息（如研究区域）准确率高。
- 大规模自动化提取展示了降低SLR时间与成本的潜力，但需谨慎处理复杂字段。

### 局限性
- 未进行重复运行以正式量化采样方差。
- 仅测试了GPT-4.1和GPT-5.0两个模型，其他LLM未评估。
- 零样本设置可能不是最优；提示词未针对特定字段优化。
- 复杂或主观字段准确率低，表明LLM在需要推断或理解隐含信息时能力有限。
- 研究聚焦于COVID-19代理建模领域，结论向其他领域的推广性需进一步验证。

## 3. Why Current XAI Is Not Enough for Arabic NLP: A Critical Survey of the Explainability Gap

- Source: arxiv
- arXiv ID: 2608.26144
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.26144v1
- PDF: https://arxiv.org/pdf/2608.26144v1
- DOI: https://doi.org/10.48550/arXiv.2608.26144

### Authors

Salima Lamsiyah, Ruslan Mitkov

### Abstract

Explainable AI (XAI) is now a major theme in NLP; however, Arabic NLP remains under-explained in three connected senses. First, there is a method gap: Arabic XAI relies heavily on a small set of post-hoc techniques such as LIME, SHAP, attention visualization, and saliency, while broader NLP XAI offers richer diagnostic, counterfactual, probing, rationale-based, and human-centered methods. Second, there is a task gap: existing Arabic XAI work is concentrated in classification tasks, especially sentiment analysis, hate/offensive language detection, fake news, and spam, with weaker coverage of generation, retrieval, translation, summarization, structured prediction, and dialogue. Third, there is a linguistic gap: many explanations identify influential tokens, but rarely explain Arabic-specific phenomena such as morphology, clitics, dialectal variation, diglossia, orthographic ambiguity, diacritics, code-switching, named entities, cultural references, or Classical and religious registers. This critical structured survey synthesizes the reviewed literature on Arabic XAI across text, speech, and multimodal settings. We argue that Arabic NLP does not only need explanations of model decisions; it needs explanations that are faithful to Arabic as a linguistic, cultural, and sociotechnical object. We introduce a taxonomy of tasks, methods, linguistic units, varieties, goals, and evaluation practices, and propose a research agenda for linguistically grounded Arabic XAI.

### 中文一句话结论
当前阿拉伯语NLP的可解释AI（XAI）存在方法、任务和语言学三个维度的显著空白，现有技术无法忠实解释阿拉伯语特有的语言、文化和社会技术现象。

### English TL;DR
This paper identifies a threefold explainability gap in Arabic NLP—methodological, task-related, and linguistic—arguing that current XAI techniques fail to account for Arabic-specific phenomena and that explanations must be faithful to Arabic as a linguistic, cultural, and sociotechnical object.

### 中文详细总结
该综述系统批判了阿拉伯语NLP中可解释AI（XAI）的现状。作者指出三大核心空白：**方法空白**（仅依赖LIME、SHAP、注意力可视化等少数事后技术，缺乏反事实、探测、基于原理等人本方法）、**任务空白**（现有工作集中在情感分析、仇恨言论检测等分类任务，忽视生成、检索、翻译、对话等任务）、**语言学空白**（解释停留在token层面，未能涉及阿拉伯语特有的形态、附着语素、方言变体、双言现象、正字法歧义、变音符、代码切换、专名、文化指涉、古典与宗教语域等）。论文提出解释应覆盖四个层次：预测层、模型层、语言学层和社会文化层，并构建了涵盖任务、方法、语言学单元、变体、目标和评估实践的批判性分类体系。最终呼吁发展"语言学扎根的"阿拉伯语XAI研究议程。

### 方法 / 贡献
1. **框架性贡献**：首次从方法、任务、语言学三维度系统界定阿拉伯语XAI的"可解释性鸿沟"。
2. **理论分层**：提出解释应包含预测级、模型级、语言学级、社会文化级四个递进层次。
3. **分类体系**：构建包含任务、方法、语言学单元、语言变体、目标、评估实践的批判性分类表（Table 1）和任务-方法覆盖表（Table 2）。
4. **研究议程**：提出面向语言学扎根、忠实、有用、可复现的阿拉伯语XAI具体建议。

### 实验或数据
该论文为综述性质（critical structured survey），**未进行新实验或使用特定数据集**。其分析基于对已发表阿拉伯语XAI文献的系统梳理，涵盖文本、语音和多模态场景。

### 值得关注点
- 明确区分"对模型决策的解释"与"对阿拉伯语作为语言/文化/社会技术对象的解释"
- 指出当前热图式解释可能隐藏对形态、方言、正字法等语言学线索的误用
- 强调阿拉伯语XAI需要跨任务、跨方法、跨语言变体的标准化评估协议
- 提出忠实的luminescence解释应能区分：方言线索、屈折模式、专名、宗教引用、审核规范 vs. 伪影

### 局限性
- 作为综述，未提出具体可落地的改进方案或算法
- 未系统评估现有阿拉伯语XAI方法在不同语言变体（如马格里布方言vs. 海湾方言）下的表现差异
- 缺少对具体解释方法（如LIME、SHAP）在阿拉伯语场景下忠实性的定量实验验证
- 研究议程部分较为宏观，未明确优先实施的技术路径或评估指标

## 4. AffectOmni: RL-Verifiable People-Centric Grounded Affective Reasoning for Social and Art-Related Scenes

- Source: arxiv
- arXiv ID: 2608.26193
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.26193v1
- PDF: https://arxiv.org/pdf/2608.26193v1
- DOI: https://doi.org/10.48550/arXiv.2608.26193

### Authors

Yibo Wang, Rui Yang, Jisheng Dang, Bimei Wang, Yitao Wu, Pengfei Cao, Wencan Zhang, Hong Peng, Bin Hu, Tat-Seng Chua

### Abstract

Multimodal large language models (MLLMs) achieve strong performance on VQA and scene understanding, yet affective reasoning remains vulnerable to shortcut behavior. Models may predict correct answers while neglecting people-centric cues such as micro expressions and body language, which weakens traceability and external verification. Prior reinforcement learning approaches mainly reward context or logical coherence without explicitly enforcing attention to human evidence. In addition, LLM as a Judge scoring often suffers from score clustering, which reduces reward discriminability. We propose AffectOmni, a GRPO trained framework for verifiable affective reasoning. AffectOmni introduces People Focus and Temporal Order rewards to encourage people-centric evidence selection and temporally structured reasoning, and it adopts within-group comparative scoring to produce more stable and discriminative reward signals. For verification, a Thinking Summarizer converts free form rationales into executable evidence instructions, which are grounded into pixel level evidence regions via SAM3 to provide an externally auditable interface outside the training loop. Experiments on IntentBench, Daily Omni, and WorldSense show consistent improvements over open source 7B scale baselines, including gains of 4.66% on emotion recognition and +14.29% on temporally sensitive tasks. Code is available at https://github.com/eliot127825-rgb/AffectOmni_nobody.

### 中文一句话结论
AffectOmni 提出了一种基于 GRPO 的可验证情感推理框架，通过人本中心奖励和组内比较评分缓解捷径推理问题，并利用 SAM3 将推理依据锚定到像素级证据区域，从而提升推理的可追溯性和外部可验证性。

### English TL;DR
AffectOmni is a GRPO-trained framework for verifiable affective reasoning that introduces people-centric rewards and within-group comparative scoring to mitigate shortcut behavior, and provides external verification by grounding reasoning claims into pixel-level evidence regions via SAM3.

### 中文详细总结
论文针对多模态大语言模型在情感推理中的“捷径行为”问题：模型常依赖全局背景线索而非人物中心线索（如微表情、肢体语言）进行推理，导致推理过程不可追溯且难以外部验证。为此，作者提出 AffectOmni 框架，包含三个核心部分：1) 人本中心奖励塑形（People Focus Reward 和 Temporal Order Reward），显式鼓励模型关注人物线索并保持时间结构化的推理；2) 组内比较评分策略，避免 LLM 作为裁判时的评分聚类问题，提供更稳定、更具区分度的奖励信号；3) 外部验证机制，通过“思考摘要器”将自由文本推理压缩为可执行的证据指令，并利用 SAM3 将证据锚定到像素级掩码区域，实现训练循环外的可审计接口。实验表明，该方法在多个基准上优于开源 7B 规模基线。

### 方法 / 贡献
1. **人本中心奖励塑形**：设计两个细粒度奖励函数——People Focus Reward（评估面部表情、身体动作、人际互动三方面）和 Temporal Order Reward（评估时间标记的使用和情感轨迹的时间连贯性），通过联合提示词减少 API 开销，并采用因果掩码防止奖励泄漏。
2. **组内比较评分**：在 GRPO 训练中，采用组内相对排序而非独立绝对评分，缓解 LLM 裁判的校准漂移和分数聚类问题，提供更稳定的优化信号。
3. **推理到证据的落地范式**：首次提出情感推理的证据落地范式，通过“思考摘要器”将自由文本推理压缩为最小证据包（MEP），再经由 SAM3 生成像素级证据区域，支持外部审计。

### 实验或数据
实验在 **IntentBench**、**Daily Omni** 和 **WorldSense** 三个基准上进行，结果显示较开源 7B 规模基线有持续提升，包括情感识别任务提升 **4.66%**，时间敏感任务提升 **14.29%**。具体数据集细节和实验设置需参阅论文全文。

### 值得关注点
- 首次将情感推理与像素级证据落地结合，提供外部可验证接口。
- 通过细粒度奖励塑形（人本中心+时间顺序）针对性地解决捷径推理问题。
- 组内比较评分策略有效提升 LLM 裁判奖励的区分度和稳定性。
- 代码已开源：https://github.com/eliot127825-rgb/AffectOmni_nobody

### 局限性
- 奖励函数的评估依赖 LLM 作为裁判，其自身可能存在偏差。
- 本文主要在 7B 规模模型上验证，更大规模模型的效果尚待确认。
- 证据落地模块（SAM3）的性能和泛化性未在摘要中详细说明。
- 论文摘要未提供所有数据集的详细统计结果，实验细节需参考全文。

## 5. Syntax vs. Semantics: How Transformers Learn Deep Dependencies

- Source: arxiv
- arXiv ID: 2608.26139
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.26139v1
- PDF: https://arxiv.org/pdf/2608.26139v1
- DOI: https://doi.org/10.48550/arXiv.2608.26139

### Authors

Jiangrui Zhao, Xiaoting Du

### Abstract

Large Language Models demonstrate remarkable syntactic fluency, yet the optimization dynamics governing their acquisition of deep semantic dependencies remain poorly understood. We propose a mechanistic framework that models this learning process as a competition between Surface Statistics and Deep Semantics. Our theoretical analysis identifies a ``Gradient Starvation" phenomenon where the error signals for sparse semantic dependencies are actively suppressed during early optimization. This suppression impedes the learning of structural reasoning and causes its emergence to manifest as a sudden phase transition. Furthermore, this framework offers a mechanistic basis for the effectiveness of Chain-of-Thought (CoT) strategies. By externalizing intermediate reasoning steps into concrete tokens, CoT effectively bypasses the suppression regime inherent to implicit reasoning. We validate these findings across scales ranging from toy transformers to production models (Llama-3.1-8B, Qwen2.5-Coder-7B). Finally, guided by this theory, we propose a topology-aligned contrastive objective that explicitly rectifies the gradient geometry. Experiments on variable binding tasks demonstrate that our method achieves an improvement that is over 2x larger than that obtained via standard cross-entropy fine-tuning.

### 中文一句话结论
本文提出一个机制性框架：Transformer 学习深层语义依赖时，表层句法统计通过“梯度饥饿”压制稀疏语义信号，导致能力以相变形式突现；思维链通过外化中间步骤绕过该抑制，且据此设计的拓扑对齐对比目标可显著加速深层依赖学习。

### English TL;DR
This paper proposes a mechanistic framework showing that transformers learn deep semantic dependencies through a "Gradient Starvation" competition where high-curvature surface statistics suppress sparse semantic signals, causing delayed phase transitions, which Chain-of-Thought reasoning bypasses by externalizing intermediate steps to alter gradient geometry.

### 中文详细总结
作者将 Transformer 的学习过程建模为“表层统计（句法）”与“深层语义（潜在依赖结构）”之间的竞争。在训练早期，高频局部模式产生的高曲率梯度主导优化方向，形成“梯度饥饿”（Gradient Starvation）效应，使稀疏的语义误差信号被主动抑制。这种抑制导致深层依赖能力无法平滑提升，而是在后期以突然的相变方式涌现。

该框架进一步解释了思维链（Chain-of-Thought）的作用：通过将中间推理步骤外化为具体 token，CoT 改变了梯度几何结构，增加了额外的梯度通路，从而绕过了隐式推理所面临的“消失梯度屏障”。理论分析还刻画了阶段转变：从句法主导，到不稳定交叉，再到与语义拓扑算子对齐的稳定涌现阶段。

基于该理论，作者提出一种拓扑对齐的对比学习目标，显式修正梯度几何。实验表明，在变量绑定任务上，该方法相比标准交叉熵微调取得了超过 2 倍的提升。

### 方法 / 贡献
- 提出“表层统计 vs. 深层语义”的机制性学习框架，将句法与语义视为梯度景观中的竞争者。
- 理论识别“梯度饥饿”现象：高曲率句法特征压制低曲率语义信号，导致深层依赖学习延迟。
- 通过 softmax 饱和分析，证明语义梯度的“消失屏障”随句法注意力权重趋近 1 而指数衰减。
- 证明优化过程会通过类似 Hebbian 的外积更新，使注意力交互矩阵逐步对齐语义拓扑算子。
- 定义对齐比率并划分三个阶段：句法主导、交叉期、系统性涌现；并解释为何涌现呈现相变。
- 为 Chain-of-Thought 的有效性提供机制性解释：外化推理步骤改变梯度几何，绕过隐式推理的抑制区。
- 提出拓扑对齐对比目标，显式修正梯度几何，加速深层依赖学习。

### 实验或数据
- 实验规模从玩具 Transformer 延伸到生产级模型，包括 Llama-3.1-8B 和 Qwen2.5-Coder-7B。
- 由于自然语言缺乏潜在依赖结构的明确真值，作者主要使用源代码与抽象语法树（AST）作为控制性代理。
- 通过 Pythia 中间检查点追踪依赖电路的出现过程。
- 在变量绑定任务上验证拓扑对齐对比目标，提升幅度超过标准交叉熵微调的 2 倍。
- 论文提到代码将公开：https://github.com/jr-zhao/Deep-Dependencies/tree/main。

### 值得关注点
- 将“句法 vs. 语义”视为动态竞争而非静态表征或架构选择，提供了新的理解角度。
- 解释了深层依赖能力“突然涌现”而非渐进提升的优化机制。
- 为 Chain-of-Thought 提供了超越经验效果的因果性解释。
- 理论指导的拓扑对齐对比目标在真实模型上取得显著收益。
- 验证了语义功能只出现在少量注意力头上，即稀疏的“绑定电路”。

### 局限性
- 摘要与预览中未给出明确的局限性声明。
- 理论依赖若干假设，例如谱差异假设、误差-噪声正交性假设等，这些假设在部分实验中验证，但未必适用于所有数据分布。
- 由于自然语言缺乏潜在依赖结构的明确真值，实验主要依赖代码和 AST 作为代理，可能限制结论向自然语言推理任务的直接推广。

## 6. GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL

- Source: arxiv
- arXiv ID: 2608.27142
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.27142v1
- PDF: https://arxiv.org/pdf/2608.27142v1
- DOI: https://doi.org/10.48550/arXiv.2608.27142

### Authors

Zike Yuan, Han Zhang, Jianzhi Yan, Le Liu, Cai Ke, Huozhi Zhou, Jian Xie, Jiran Yin, Yukun Cao, Yue Yu, Hui Wang, Ming Liu, Bing Qin

### Abstract

Despite their potential in standardized graph tasks, Large Language Models (LLMs) remain brittle to real-world shifts in node identifiers and task formulation. While deterministic graph tools are invariant to such shifts, extracting topological structures from noisy text is highly fragile for LLMs, which often overfit to surface patterns. Moreover, mitigating these parsing failures via multi-agent systems incurs prohibitive latency. To address this, we propose GRAIN, a single-agent framework optimized via reinforcement learning. GRAIN models reasoning as a semantic parsing and tool-execution pipeline, guided by a Structure Invariance Reward. By validating extracted intermediate graphs against ground-truth topologies, this reward forces the LLM to learn robust text-to-structure mappings rather than memorizing linguistic artifacts. We also introduce GRIT, a benchmark evaluating sensitivity to such linguistic shifts. GRAIN outperforms multi-agent baselines by 16.45\% in accuracy with approximately 24\% lower latency. Furthermore, it demonstrates superior structural generalization, halving the out-of-distribution (OOD) gap of SFT models (from 15.77\% to 7.80\%) and maintaining robustness on large-scale graphs beyond the training distribution.

### 中文一句话结论
GRAIN通过结构不变性奖励的强化学习，显著提升了LLM在图推理中对节点标识符和任务表述变化的鲁棒性，同时降低了延迟。

### English TL;DR
GRAIN uses reinforcement learning with a Structure Invariance Reward to make LLMs robust to real-world shifts in graph reasoning, outperforming multi-agent baselines by 16.45% in accuracy with ~24% lower latency.

### 中文详细总结
GRAIN是一个单智能体框架，将推理过程建模为语义解析和工具执行管线，通过结构不变性奖励进行强化学习训练，迫使LLM学习稳健的文本到结构的映射，而非记忆表面语言模式。该框架引入GRIT基准，用于评估模型对节点标识符和任务表述变化的敏感性。实验表明，GRAIN在准确率上比多智能体基线提升16.45%，延迟降低约24%，并在分布外（OOD）场景下将SFT模型的OOD差距从15.77%减半至7.80%，同时在大规模图上保持鲁棒性。

### 方法 / 贡献
- 提出GRAIN：单智能体强化学习框架，结合语义解析与工具执行。
- 结构不变性奖励：通过验证中间图与真实拓扑的一致性，强制模型学习不变规则，避免过拟合表面标识符。
- 引入GRIT基准：多任务、多视角语料库，覆盖6种图任务和31个真实场景，用于系统评估节点标识和任务形式变化。
- 在准确率、延迟和OOD泛化上均优于多智能体基线。

### 实验或数据
- 使用GRIT基准：训练集包含2160个图（节点数4-40），测试集360个图，大图测试120个图（节点数40-60），OOD测试180个图（含未见场景）。
- 与多智能体基线对比：GRAIN准确率提升16.45%，延迟降低约24%。
- OOD泛化：GRAIN将SFT模型的OOD差距从15.77%降至7.80%。
- 在大规模图上（节点数40-60）保持鲁棒性。

### 值得关注点
- 单智能体设计避免了多智能体系统的高延迟和令牌成本。
- 结构不变性奖励直接优化拓扑恢复，而非表面准确性，提升了泛化能力。
- 在OOD场景下性能显著优于SFT模型，表明其学习到了不变的结构规则。
- GRIT基准提供了可控的多样性评估，有助于系统诊断鲁棒性。

### 局限性
- 方法依赖中间图的正确解析，在极端噪声文本下可能仍存在挑战。
- 实验未提及与更大规模闭源模型（如GPT-4）的对比。
- 仅在6种图任务上验证，泛化到其他复杂图问题需进一步研究。
- 延迟降低约24%为相对值，未给出绝对数值，且未讨论极端情况下的延迟表现。

## 7. SPT: Skills as Pre-Training Data for Agentic Language Models

- Source: arxiv
- arXiv ID: 2608.26563
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.26563v1
- PDF: https://arxiv.org/pdf/2608.26563v1
- DOI: https://doi.org/10.48550/arXiv.2608.26563

### Authors

Yufei Sun, Yudong Li, Yiming Cheng

### Abstract

Agentic (tool-using) language models are mainly trained on tool-call traces and agent trajectories during post-training. These data provide direct behavioral supervision, but producing them requires task environments, execution, and verification, making broad tool and task coverage expensive. Publicly available skills offer another source of training data: they encode reusable tool semantics and workflows but are typically used only as inference-time context. We introduce Skill Pre-Training (SPT), a mid-training method that applies causal language modeling to SkillCorpus, a collection of public multi-file skill packages, optionally mixed with general data. To preserve relations among files within each package, we also introduce Reference Insert, a reference-aware assembly strategy that places supporting files near their mentions in the primary instruction. Experiments across multiple model scales and post-training recipes show that SPT consistently improves agentic performance over mid-training on general or trajectory data, while largely preserving general performance. Data mixture experiments show additional benefits from combining skill data with general annealing corpora. These results indicate that skill packages are a valuable data source for pre-training agentic language models.

### 中文一句话结论  
SPT（技能预训练）通过将公开的多文件技能包作为中期训练数据，显著提升了智能体语言模型的工具使用能力，且不损害通用性能。

### English TL;DR  
SPT improves agentic language models by using public multi-file skill packages as mid-training data with a reference-aware assembly strategy (Reference Insert), outperforming general or trajectory data across multiple scales and post-training recipes.

### 中文详细总结  
论文提出Skill Pre-Training (SPT)，一种在行为导向的后训练之前，将公开技能包作为中期训练数据的方法。技能包包含可复用的工具语义和工作流说明，但此前仅被用作推理时的上下文。SPT构建了SkillCorpus（38,040个经过清洗和去污染的ClawHub包），并通过Reference Insert策略将引用文件插入到主指令的提及位置，以保留跨文件关系。实验在多个模型规模（如MeCo-1.6B）和后训练配置（xLAM-FC、Tulu 3）下进行，显示SPT在智能体基准（API-Bank、MetaTool等）上一致优于无中期训练、通用数据（Dolmino）或轨迹数据（AgentBank）的中期训练，且通用性能（ARC、MMLU等）基本保持。数据混合实验表明技能数据与通用数据的组合能带来额外收益。这些结果揭示了技能包作为智能体语言模型预训练数据的价值。

### 方法 / 贡献  
1. **提出技能包作为可扩展的智能体预训练数据**：构建了38,040个多文件技能包的SkillCorpus。  
2. **引入SPT方法**：在后训练前对技能数据应用因果语言建模目标，配合Reference Insert（引用感知的包组装策略），将引用文件提到主指令的首次提及附近。  
3. **提供受控对比实验**：在不同模型规模、后训练设置下比较技能包与通用数据、轨迹数据的效果，并消融混合比例和文件组织方式。  
4. **下游RL鲁棒性验证**：在SFT接RL的场景中，SPT仍保持优势。

### 实验或数据  
- **数据集**：SkillCorpus包含38,040个从ClawHub（2026年5月1日快照）清洗去污后的技能包，共218,277个文件，处理后产生84,905个训练块（约3.478亿 token）。  
- **基准**：智能体基准包括API-Bank、MetaTool、APTBench、ToolEyes；通用基准包括ARC、BoolQ、HellaSwag、PIQA、Winogrande、MMLU。  
- **模型规模**：主实验基于MeCo-1.6B-DCLM-160B，也在其他规模（如SmolLM）上验证。  
- **对比设置**：与无中期训练、通用数据（Dolmino）、轨迹数据（AgentBank）比较；后训练使用xLAM-FC、Tulu 3等配方。  
- **关键结果**：SPT在智能体平均得分上达25.40（vs. 通用18.20、轨迹20.62），通用平均分约59.00（基本持平）。数据混合（α=0.5等）进一步改善。

### 值得关注点  
- **数据来源创新**：利用大规模公开技能包（npm增速9.6×/4个月）作为预训练数据，避免了依赖昂贵的工具环境执行。  
- **组织策略有效**：Reference Insert显著优于随机拼接或元数据打包等替代方案。  
- **鲁棒性**：在不同模型规模、后训练方法（SFT/RL）下一致提升，表明技能包是通用的预训练数据源。  
- **混合潜力**：技能数据与通用文本可互补，在固定预算下实现最佳性能平衡。

### 局限性  
- 技能包质量依赖平台审核机制，可能存在噪声或过时代码。  
- 实验仅在有限模型规模（最大1.6B）上进行，更大规模的效果有待验证。  
- 只使用了ClawHub平台，未涵盖其他技能仓库（如HuggingFace工具）的泛化性。  
- 未探索技能包在纯预训练阶段（而非中期训练）的应用效果。  
- 涉及技能识别和引用关系，可能对包的文件结构敏感（如无SKILL.md的包如何处理未说明）。

## 8. LLMs for Academic Workflows: An Evaluation of Literature Reviews Generated with Short and Long Context Windows of LLMs

- Source: arxiv
- arXiv ID: 2608.26145
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.26145v1
- PDF: https://arxiv.org/pdf/2608.26145v1
- DOI: https://doi.org/10.48550/arXiv.2608.26145

### Authors

Muhammad Ali Chaudhry, Xinyuan Hao, Haifa Alwahaby

### Abstract

Our research focuses on evaluating literature reviews generated in short and long context settings of large language models (LLMs) to investigate the impact of context window on the quality of AI-generated literature reviews and the role of AI in supporting literature review writing. Twenty AI-generated literature reviews based on research sources from Semantic Scholar and Arxiv were evaluated by two researchers across 15 dimensions. Our findings reveal that AI-generated literature reviews require human oversight to meet academic publishing standards. As context windows increase, LLMs can incorporate broader information and maintain coherence across longer inputs, but they also exacerbate issues such as content repetition, omission of critical work, and a tendency towards descriptiveness over synthesis. Our work shows that AI-generated reviews can provide foundational overviews, but their output must be critically evaluated and refined by domain experts. Future research should consider integrating other LLMs and fine-tuned models in different domains with hybrid approaches that combine human expertise with AI capabilities to address the limitations identified in this study.

### 中文一句话结论
大语言模型生成的文献综述在长上下文窗口下覆盖更广但重复、遗漏关键工作、描述性过强等问题更突出，需人类专家批判性审查才能达到学术出版标准。

### English TL;DR
LLM-generated literature reviews can provide broad overviews, especially with longer context windows, but they suffer from increased repetition, omission of key works, and a descriptive rather than synthetic style, necessitating critical human oversight to meet academic standards.

### 中文详细总结
本研究评估了短上下文与长上下文窗口下大语言模型生成的文献综述质量。共生成20篇基于Semantic Scholar和Arxiv论文的AI综述（10篇长上下文、10篇短上下文），由两位AI教育领域研究者按15个维度（1-5分）评分。所有综述至少达到“良好”级别，但存在共性问题：内容重复（长上下文更严重）、遗漏关键文献（如未引用领域内高引用论文）、以描述性罗列替代分析性综合、过渡生硬、时态不一致、偶有无关内容。长上下文窗口虽能纳入更广信息并保持连贯性，却加剧了冗余和描述性；短上下文窗口重复较少但可能导致综述碎片化。研究表明AI综述可作为基础概览，但必须由领域专家进行批判性评估和细化才能用于学术出版。

### 方法 / 贡献
**方法**：使用Gemini 1.5 Pro，基于Semantic Scholar和Arxiv的论文，对10个AI教育研究问题分别生成长上下文（完整论文输入）和短上下文（限制窗口）版本的文献综述（共20篇）。两位研究者独立按自建15维度评分（结构、逻辑、批判性、综合、研究空白识别、准确性、引用质量、时效性等），采用加权Cohen's Kappa（0.743）衡量一致性，分歧通过讨论解决。  
**贡献**：首次系统比较上下文窗口大小对AI生成文献综述质量的影响，明确长上下文窗口的利弊（更广覆盖但更易重复和描述性），强调人类监督不可或缺，为混合人机协作研究流程提供了实证依据。

### 实验或数据
- **数据来源**：从Semantic Scholar（每查询前100篇）和Arxiv（每查询前50篇）提取论文。
- **实验设计**：10个研究问题（均来自AI教育领域），每个问题生成长上下文和短上下文版本各一篇，共20篇综述。
- **评估**：两位AI教育专家按15个维度（1-5分）评分，总分75分。评分一致性：加权Cohen's Kappa = 0.743（高度一致）。最终分数分四档：优秀（>60）、良好（45-60）、通过（30-45）、不及格（≤30）；所有综述均达到良好及以上。
- **主要结果**：长上下文综述引用更广泛但重复和描述性更突出；短上下文综述重复较少但可能遗漏细节。两种上下文均出现遗漏关键文献、缺乏批判性综合等问题。

### 值得关注点
- 长上下文窗口虽能处理更多文献，但导致更高的内容重复率和描述性倾向，形成“广度牺牲深度”的权衡。
- 短上下文窗口通过限制输入范围部分缓解了重复，但可能使综述碎片化、缺乏连贯性。
- AI综述均未达到“优秀”等级（仅2篇获优秀，且来自不同上下文设置），表明当前AI无法独立完成学术级文献综述。
- 研究发现AI倾向于“堆砌”引文而非真正整合观点，这加剧了描述性与合成性的差距。
- 人为监督不仅必要，而且需要领域专家进行批判性评估和改写，而非简单的格式修正。

### 局限性
- 仅使用单一模型（Gemini 1.5 Pro），未与其他LLM或微调模型比较。
- 研究仅聚焦AI教育领域，结论可能不直接推广到其他学科。
- 论文来源限于Semantic Scholar和Arxiv两个开放获取数据库，可能遗漏付费期刊、会议论文等关键文献。
- 仅由两位研究者评分，尽管一致性较高，但主观偏差仍存在。
- 未探索混合方法（如检索增强生成RAG）或人类迭代优化对缓解上述问题的效果。
- 上下文窗口的具体长度设定未公开，重复实验的精确重现性有限。

## 9. Diff Mining: Logit Differences Reveal Finetuning Objectives

- Source: arxiv
- arXiv ID: 2608.26462
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.26462v1
- PDF: https://arxiv.org/pdf/2608.26462v1
- DOI: https://doi.org/10.48550/arXiv.2608.26462

### Authors

Greg Kocher, Robert West, Clément Dumas, Julian Minder

### Abstract

Finetuning has become the gold standard for refining existing behaviors and inducing new ones in language models, yet it often remains unclear exactly which behaviors emerge during this process. As models grow ever more capable, understanding finetuning better becomes increasingly important, particularly since unwanted behaviors may arise during finetuning. In this paper, we introduce Diff Mining, a simple yet effective framework for identifying what a finetuned model has learned by comparing its logits to those of its base model. Diff Mining effectively surfaces salient tokens that are amplified in the finetuned model, serving as a fingerprint of its training -- even on text unrelated to the finetuning domain. Unlike many existing model diffing methods which require model internals, Diff Mining only needs access to output logits and scales to large models. The framework consists of two modular stages: (i) extracting per-context logit differences between the finetuned and base models on a reference corpus, and (ii) aggregating the resulting signals to construct an interpretable token set representing the finetune. For aggregation, we explore both a simple Top-K frequency method and a Non-negative Matrix Factorization (NMF)-based approach for disentangling multiple finetuning objectives into distinct token clusters. Empirically, Diff Mining succeeds across diverse settings: on finetune domain detection, it significantly outperforms state-of-the-art model diffing methods both in identifying relevant tokens and in downstream performance when an interpretability agent is given access to the extracted token set; on models with injected biases, it identifies more than one third of the biases without targeted probing. Overall, our framework shows promise in developing auditing tools to detect finetuning objectives.

### 中文一句话结论
Diff Mining 通过比较微调模型与基础模型的 logit 输出差异，无需访问模型内部结构即可有效识别微调目标，性能优于现有方法。

### English TL;DR
Diff Mining reveals finetuning objectives by comparing logit differences between a finetuned model and its base model, producing an interpretable token set without requiring model internals.

### 中文详细总结
微调是改进语言模型行为的标准方法，但微调过程中具体哪些行为发生了变化往往不明确，尤其是不良行为可能在微调中意外出现。本文提出 Diff Mining，一种简单有效的框架，通过比较微调模型与其基础模型的 logits 来识别微调所学内容。Diff Mining 能有效提取在微调模型中被放大的显著 token，形成微调过程的“指纹”，且即使在与微调领域无关的文本上也能奏效。与许多依赖模型内部状态的现有方法不同，Diff Mining 仅需访问输出 logits，可扩展至大型模型。框架包含两大模块：(i) 在参考语料上提取每个上下文中微调模型与基础模型的 logit 差异；(ii) 聚合信号，构建可解释的 token 集。聚合方法包括简单的 Top-K 频率法以及基于非负矩阵分解（NMF）的方法，用于将多个微调目标分离为不同 token 簇。实验表明，Diff Mining 在微调领域检测、相关 token 识别以及下游任务中均显著优于现有方法；在注入偏见模型中，无需针对性探测即可识别超过三分之一的偏见。

### 方法 / 贡献
- 提出 Diff Mining 框架，仅需输出 logits 即可进行模型“差异分析”，无需访问模型内部状态，可扩展至大型模型。
- 框架包含两步：(i) 在参考语料上逐上下文计算微调模型与基础模型的 logit 差异；(ii) 聚合信号，通过 Top-K 频率法或 NMF 构建可解释的 token 集，后者能分离多个微调目标。
- 在微调领域检测任务上，显著优于现有最优模型差异分析方法。

### 实验或数据
- 在微调领域检测任务上，Diff Mining 在识别相关 token 及下游性能方面均大幅超越现有方法。
- 在注入偏见的模型中，无需针对性探测即可识别超过三分之一的偏见。
- 聚合方法包括 Top-K 频率法与基于 NMF 的方法，用于处理多目标微调。

### 值得关注点
- Diff Mining 仅需输出 logits，无需模型内部信息，计算开销低，适合大型模型审计。
- 能够从与微调领域无关的文本中提取微调目标“指纹”，具有较强泛化能力。
- 结合 NMF 可同时分离多个微调目标，有助于检测隐藏或不良行为。

### 局限性
- 论文未提及在超大规模模型（如千亿参数级）上的实际运行效率测试。
- 对于非常微妙或高度依赖特定语境的微调目标，检测能力可能有限。
- NMF 组件的解释性可能受分解质量影响，且文献未详细讨论其超参数敏感性。
- 未涉及模型差异分析中被放大 token 的最终语义解释的自动化验证。

## 10. Mutual Debiasing via Dual-Seed Comparison for Probabilistic Sampling in Large Language Models

- Source: arxiv
- arXiv ID: 2608.26161
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.26161v1
- PDF: https://arxiv.org/pdf/2608.26161v1
- DOI: https://doi.org/10.48550/arXiv.2608.26161

### Authors

Zihao Guo, Hongtao Lv, Chaoli Zhang, Laiguo Yin, Lei Liu, Yonghui Xu, Lizhen Cui

### Abstract

Although Large Language Models (LLMs) demonstrate remarkable capabilities in reasoning and decision-making, high-fidelity probabilistic sampling remains a persistent challenge. When generating random variables, LLMs consistently exhibit systematic biases that warp the target probability distributions. Current approaches often rely on a single, self-generated seed, which inherits model-specific biases. To overcome this vulnerability, we introduce Dual-Seed Comparison (DSC), a transparent, tool-free protocol that utilizes two independent LLM-generated seeds to neutralize bias. DSC compares the character-level ordinal values of the two seeds to construct a bit sequence, converts and normalizes this sequence into a pseudo-uniform variate, and then maps the variate to the target distribution through the inverse cumulative distribution function (CDF). Empirical results show that DSC substantially outperforms existing methods across 96\% of evaluated settings. Beyond direct sampling, task-adapted variants based on the DSC comparison operator improve distributional control in MCQ generation and attribute-constrained text-to-image prompting.

### 中文一句话结论  
本文提出双种子对比（DSC）方法，通过独立利用两个LLM生成的种子在字符级别进行比较，消除系统性偏差，从而在概率采样中显著优于现有方法（96％设置下表现最佳）。

### English TL;DR  
The paper proposes Dual-Seed Comparison (DSC), a transparent, tool-free method that uses two independent LLM-generated seeds to neutralize systematic biases in probabilistic sampling, substantially outperforming existing methods across 96% of evaluated settings.

### 中文详细总结  
大型语言模型在生成随机变量时表现出系统性偏差，扭曲目标概率分布。现有方法依赖单个自生成种子，继承了模型特有的偏差。DSC 通过提示LLM生成两个独立种子，逐字符比较其序数值构建比特序列，归一化为伪均匀变量，再通过逆累积分布函数映射到目标分布。实验覆盖5个模型、5种分布，DSC 在24/25条件下取得最低KS统计量（96%设置优于基线）。此外，基于DSC比较运算符的任务适配变体在多项选择题生成和属性约束文本到图像提示中改善了分布控制。

### 方法 / 贡献  
- **方法**：DSC 仅需一次推理调用：生成两个独立字符串 → 逐字符对比序数值（若第一个字符序数值大于第二个则为1，否则为0）→ 形成比特序列 → 归一化为[0,1)伪均匀变量 → 通过目标分布的逆CDF采样。全程透明、无外部工具。  
- **贡献**：  
  1. 实证揭示了LLM生成字符串存在系统性的字符级偏差，证明单种子熵源不可靠。  
  2. 提出DSC这一无需外部工具的透明采样协议。  
  3. 在5模型×5分布上验证有效性，并在多项选择题位置控制和属性约束提示生成任务中提升分布保真度。

### 实验或数据  
- **无传统数据集**；实验基于对5个LLM（如Qwen3.5-27B等）进行独立无状态查询，采集样本与目标分布（均匀、指数、正态等）比较。  
- **指标**：Kolmogorov–Smirnov统计量（主指标）、Wasserstein距离（连续分布）、卡方检验（离散分布）。  
- **字符级偏差分析**：对每个模型收集200组16字符随机字符串（可打印ASCII），检测到所有模型字符频次显著偏离均匀（KS统计量0.082–0.197，p<0.001）。  
- **结果**：DSC在24/25条件（96%）下KS统计量最低；在多项选择题生成（平衡答案位置）和文本到图像提示（控制属性出现频次）上也优于基线。

### 值得关注点  
- 完全无外部工具，仅靠LLM自身输出实现概率采样，本质解决“认知-行为差距”。  
- 双种子比较机制将模型字符偏好转化为随机比特，不依赖单个种子的绝对均匀性。  
- 过程透明、可审计，中间步骤（种子、比较序列、归一化值）均可追溯。  
- 单次推理调用完成，高效且与模型无关。

### 局限性  
论文摘要和引言中未明确讨论局限性。基于方法本身，潜在限制包括：  
- 要求两个生成的种子具有独立性，若模型产生强相关或重复字符串，比较结果可能仍有偏差。  
- 仅评估了5个模型和5种分布，对更大规模模型和更广分布族的泛化性未知。  
- 字符比较依赖ASCII序数假设，对非英文字符或大型字母表可能不适用。

## Processing Notes

- Duplicate papers skipped: 0