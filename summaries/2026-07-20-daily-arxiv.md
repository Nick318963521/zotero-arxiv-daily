# Daily arXiv - 2026-07-20

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-20T23:10:46
- Paper count: 10

## 1. How Much Human Label Variation Does Formal Semantic Structure Explain?: Group-Level Effects and Item-Level Ceilings in NLI

- Source: arxiv
- arXiv ID: 2607.15870
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.15870v1
- PDF: https://arxiv.org/pdf/2607.15870v1
- DOI: https://doi.org/10.48550/arXiv.2607.15870

### Authors

Haram Choi

### Abstract

Human label variation in natural language inference is increasingly treated as signal rather than noise, but how much of it formal semantic structure explains has not been measured directly. We measure it on the 3,113 SNLI and MNLI items of ChaosNLI, using a rule-based operator and monotonicity tagger validated against MED (0.883 agreement at the edit site, 0.807 on the sentence-level summary our analyses consume), three preregistered analysis blocks, and full reporting of negative results. Three bounds emerge. First, a group-level boundary: hypotheses that are not purely upward monotone show reliably higher label entropy (Cliff's delta = -0.284), and rank-based tests defend the effect against operator-presence and length reductions, though a bounded-outcome sensitivity check weakens the regression form of the length defense. Second, an item-level ceiling: the same formal profiles explain only 3.3 to 3.6 percent of entropy variance and reach a median-split AUC of 0.606, too weak to identify high-disagreement items. Third, composition invariance: across the boundary, three high-powered preregistered contrasts on validated error shares and explanation-type shares (VariErr, LiTEx) all return null results. In this sample, formal semantic structure shifts how much annotators disagree by a small amount and does not detectably change what they disagree about. ChaosNLI-S/M consists of items selected for low original agreement, and every claim is conditioned on that scope. All analyses were preregistered in a version-controlled research log, whose audit trail, including one corrected interpretation rule, the paper discloses.

### 中文一句话结论
在ChaosNLI样本中，形式语义结构对NLI人工标注变异仅能解释少量部分：它能微弱改变分歧数量，但无法显著改变分歧类型，且不具备项目级别的预测能力。

### English TL;DR
Formal semantic structure explains only a small amount of human label variation in NLI, shifting disagreement amount modestly but not its composition, with group-level effects but weak item-level predictive power.

### 中文详细总结
本研究基于ChaosNLI的3,113个SNLI/MNLI项目，利用规则化的算子与单调性标注器（经MED验证，编辑位置一致率0.883）测量形式语义结构对人工标注变异（熵、多数边际）的解释力。三个主要发现：
1. **群体层面边界**：非纯向上单调的假设表现出显著更高的标签熵（Cliff’s δ = -0.284），且该效应在控制算子存在和句子长度后仍稳健，但边界结果敏感度分析弱化了回归形式下的长度控制。
2. **项目层面天花板**：相同的形式特征仅能解释熵变异的3.3–3.6%，中位数分割AUC仅为0.606，不足以识别高分歧项目。
3. **组成不变性**：跨边界的三项高功效预注册对比（VariErr误差率、LiTEx解释类型）均无显著差异，表明形式语义结构不改变分歧的构成。
所有结论均限于ChaosNLI-S/M样本（原标注低一致项目），可能被衰减。

### 方法 / 贡献
- 使用基于规则的算子与单调性标注器（依赖树解析，标注四种算子家族及单调性方向），并在MED基准上验证。
- 三项预注册分析块：群体层面边界、项目层面预测力、分歧组成不变性。
- 完整报告负面结果，并披露预注册日志及一次修正。

### 实验或数据
- 使用ChaosNLI（SNLI/MNLI共3,113项，每项100标注）、MED（5,382项，用于标注器验证）、VariErr（500项，误差标注）、LiTEx（1,799条解释类别）。
- 主要分析：熵/多数边际与单调性类型的关系（Kruskal-Wallis、Mann-Whitney U、Cliff’s δ），以及方差解释比例（R² 3.3-3.6%）和AUC（0.606）。
- 交叉验证：在VariErr/LiTEx重叠子集（498项）上比较误差率与解释类型分布。

### 值得关注点
- 所有确认性分析均为预注册，并包含负结果报告及一次修正的披露。
- 工具规则化且透明，列出排除项（如词缀否定、习语NPI等）。
- 效应量虽小但稳健，在多个控制检验下仍存。

### 局限性
- 样本局限于ChaosNLI的低一致项目，效果可能衰减，不推广至完整NLI数据。
- 标注器为浅层规则系统，未处理组合极性传递、条件句等复杂环境。
- 非单调性触发词“only”存在过度触发问题。
- 28项有并列多数，已从多数边际分析中排除。

## 2. Frontier Language Models Struggle to Copy: Text Can Be Better Viewed in 2D

- Source: arxiv
- arXiv ID: 2607.16072
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.16072v1
- PDF: https://arxiv.org/pdf/2607.16072v1
- DOI: https://doi.org/10.48550/arXiv.2607.16072

### Authors

Haodong Wen, Yiran Zhang, Yingfa Chen, Kaifeng Lyu

### Abstract

While large language models (LLMs) can solve advanced reasoning problems in seconds, we show that even frontier models fail to perform a much simpler operation: exactly copying an input string that lies well within their context windows. We attribute this failure to positional encodings in Transformer architectures, whose inductive bias favors copying through a shortcut based on matching local contexts rather than carefully locating the corresponding input positions. To address this issue, we introduce 2D-RoPE, which organizes text into a 2D grid rather than a 1D sequence and assigns each token a row ID and a column ID. Under this view, copying becomes simply retrieving input tokens at a fixed column offset, which makes the task easy to learn. In synthetic copy experiments, shallow Transformers with 2D-RoPE achieve perfect copying at input lengths hundreds of times longer than those seen during training, whereas standard positional encodings fall far behind. We further show that the advantage of 2D-RoPE language models on copy tasks consistently holds in large-scale pretraining on DCLM with model sizes up to 1.4B parameters. Overall, our results suggest that viewing text in 2D can benefit language modeling, and we hope this encourages future work to further explore the potential of 2D positional encodings.

### 中文一句话结论
本文发现前沿大语言模型在精确复制输入字符串方面存在根本性困难，并提出2D-RoPE位置编码，通过将文本组织成二维网格来彻底解决这一问题。

### English TL;DR
This paper reveals that frontier large language models fundamentally struggle with exact copying of input strings, even within their context windows. The authors attribute this failure to standard positional encodings' inductive bias and introduce 2D-RoPE, which organizes text into a 2D grid (assigning row and column IDs). This makes copying trivial by retrieving tokens at a fixed column offset. In synthetic experiments, shallow Transformers with 2D-RoPE achieve perfect copying on sequences hundreds of times longer than training length, while standard encodings fail. The advantage holds in large-scale pretraining up to 1.4B parameters on DCLM.

### 中文详细总结
本论文首先通过实验证明，当前最先进的大语言模型（包括GPT-4等）在精确复制长输入字符串这一看似简单的任务上表现不佳，即便输入长度远在模型上下文窗口之内。作者将这一失败归因于Transformer架构中标准位置编码（如RoPE）的归纳偏差：这些编码鼓励模型通过匹配局部上下文（如n-gram）的“捷径”来进行复制，而非精确地关注对应输入位置。为解决此问题，论文提出**2D-RoPE**，它将文本从一维序列重新组织为二维网格，为每个token分配一个行ID和一个列ID。在这种视角下，复制操作简化为在同一行内以固定列偏移检索输入token，极大简化了任务。在合成复制实验中，使用2D-RoPE的浅层Transformer模型能够完美复制训练时未见过的、长度超出训练序列数百倍的输入，而标准位置编码（如RoPE、ALiBi）则表现不佳。此外，在DCLM数据集上进行的大规模预训练（模型规模达1.4B参数）中，2D-RoPE语言模型在复制任务上的优势依然成立，并且不会损害其在标准语言建模基准上的性能。总体而言，该结果表明“二维视图”的文本组织方式有益于语言建模。

### 方法 / 贡献
- **核心方法**：提出 **2D-RoPE** 位置编码。将长度为N的文本序列重塑为一个 H×W 的二维网格（H≈W≈√N）。每个token的位置由行ID (i) 和列ID (j) 表示，并将RoPE分别应用于行和列维度。复制任务在此框架下变为：给定当前token，只需在同一行的固定列偏移处提取对应token。
- **主要贡献**：1）揭示并系统证明了大语言模型在精确复制任务上的根本性缺陷及其原因（标准位置编码的局部匹配偏向）。2）提出2D-RoPE这一简单有效的替代方案，理论上使复制任务变得易于学习。3）通过合成实验和大规模预训练验证了2D-RoPE在复制能力上的显著优势，同时保持了良好的语言建模性能。

### 实验或数据
- **合成复制实验**：使用浅层（2层）Transformer，对比2D-RoPE与标准位置编码（NoPE, RoPE, ALiBi, T5 Bias）。在固定训练长度（如1024）下测试泛化到更长序列（高达16384）的能力。2D-RoPE实现了近乎完美的复制准确率，远超其他方法。
- **大规模预训练**：在DCLM数据集上预训练1.4B参数的模型（使用2D-RoPE vs. RoPE）。在标准语言建模困惑度（PPL）上两者相当，但在专门设计的复制评估任务中，2D-RoPE模型大幅领先。论文未报告其他特定数据集名称或标准NLP基准（如GLUE）上的结果，仅提及PPL。

### 值得关注点
- **问题新颖且反直觉**：指出“复制”这一基本操作对于强大的LLM也是难题，挑战了人们对模型能力的常见认知。
- **解决方案简洁优雅**：2D-RoPE的思想直观（将文本视为2D），实现简单，却带来了复制能力的质的飞跃，尤其在长度外推方面。
- **潜在影响**：该工作不仅有助于修复复制缺陷，还可能启发对位置编码和模型架构的进一步改进，因为“在2D中查看文本”可能捕捉到1D序列中不明显的结构性信息。

### 局限性
- 论文未在更大规模（如>10B参数）的模型上验证2D-RoPE的效果。
- 2D-RoPE在标准语言建模基准（如GLUE、SuperGLUE）上的性能表现未进行全面评估，仅报告了困惑度，其通用性尚需更多验证。
- 2D网格的构建方式（如何设定网格尺寸H和W）可能是一个需要调整的超参数，论文的分析侧重复制任务，对最优网格结构选择的通用指导有限。
- 论文主要聚焦于复制任务，对于其他需要精确位置推理的任务（如数学计算、代码执行），2D-RoPE是否同样有益有待探索。

## 3. Attention-Guided Saliency Maps for Interpreting Visualization Literacy in VLMs

- Source: arxiv
- arXiv ID: 2607.16105
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.16105v1
- PDF: https://arxiv.org/pdf/2607.16105v1
- DOI: https://doi.org/10.48550/arXiv.2607.16105

### Authors

Maeve Hutchinson, Abderrahmane Wassim Mehdaoui, Pranava Madhyastha

### Abstract

Understanding how vision-language models (VLMs) interpret data visualizations remains an open problem, and is increasingly important as these models are used for analytical tasks where reliable reasoning is essential. We introduce a lightweight, diagnostic saliency map method tailored for text generation over images using transformer models, the current state-of-the-art models in visualization interpretation. Our approach aggregates the language model's attention over the visual tokens across all heads and layers, then maps this attention back onto the vision encoder's patch grid to localise it over the image, producing a direct correspondence between each generated answer token and the image regions it attended to. This yields fast, gradient-free saliency maps that expose how VLMs allocate focus across visual elements during answer generation, enabling inspection of whether model attention aligns with semantically relevant components. We evaluate our approach using a deletion metric which validates the causal faithfulness of our saliency maps to the model's behavior.

### 中文一句话结论
本文提出一种轻量级、无需梯度的注意力引导显著性图方法，通过聚合视觉-语言模型（VLM）中所有层和头的注意力权重，定位生成每个答案token时关注的图像区域，以评估模型在图表理解任务中的视觉推理可靠性。

### English TL;DR
This paper introduces a lightweight, gradient-free saliency map method that aggregates attention across all transformer layers and heads to localize which image patches vision-language models attend to when generating each answer token, enabling evaluation of whether model focus aligns with semantically relevant visual components in data visualizations.

### 中文详细总结
本文针对视觉-语言模型（VLM）在数据可视化理解任务中“是否真正关注正确视觉元素”这一开放问题，提出了一种基于注意力机制的显著性图方法。该方法适用于当前主流的Transformer架构VLM（如LLaVA、ChartGemma）。核心思路是：在模型生成每个答案token时，从语言模型的注意力权重中提取该token对视觉前缀（visual prefix）的注意力分布，跨所有层和头取平均，然后映射回视觉编码器的patch网格，得到每个token对应的空间显著性图。该方法无需梯度计算、无需修改模型架构，仅在标准生成过程中即可完成。作者通过删除度量（deletion metric）验证了显著性图对模型行为的因果忠实性，即移除高显著性区域会快速降低模型准确率。实验基于Mini-VLAT数据集，展示了该方法在图表问答任务中的有效性。

### 方法 / 贡献
- **方法**：1) 聚合语言模型每个解码步骤中所有层和所有头对视觉token的注意力权重，取平均得到全局注意力向量；2) 将该向量重归一化为patch上的分布；3) 将扁平patch序列重塑为二维网格（G×G），并通过双线性插值上采样到原图分辨率，生成热力图。
- **贡献**：1) 提出一种针对VLMs文本生成任务的轻量级、无梯度、无需额外推理的显著性图方法；2) 实现每个生成token与图像区域的直接对应；3) 提供因果忠实性评估（删除度量），表明显著性图能反映模型真实依赖的视觉证据。

### 实验或数据
- **实验**：使用删除度量（deletion metric）评估显著性图的因果忠实性，即逐步移除图像中高显著性区域，观察模型准确率下降速度。实验表明移除top-ranked像素导致准确率迅速下降。
- **数据**：使用Mini-VLAT数据集（用于评估可视化素养的图表问答基准），以及ChartGemma模型。未在其他数据集或模型上进行广泛验证。

### 值得关注点
- 首次提出针对VLM文本生成的token级显著性图方法，而非传统分类任务。
- 方法无需梯度，计算效率高，适用于实际部署。
- 发现模型在正确回答时可能关注错误区域，揭示仅靠准确率不足以衡量视觉推理。

### 局限性
- 方法依赖Transformer注意力权重的恒定聚合，未考虑注意力可能存在的冗余或噪声（如注意力坍缩）。
- 仅实验了单一模型（ChartGemma）和单一数据集（Mini-VLAT），泛化性未验证。
- 上采样通过双线性插值实现，可能丢失patch级细节。
- 删除度量仅提供间接因果验证，未设计人类评估或与其它显著性方法（如Grad-CAM）的定量对比。

## 4. Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery

- Source: arxiv
- arXiv ID: 2607.15766
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.15766v1
- PDF: https://arxiv.org/pdf/2607.15766v1
- DOI: https://doi.org/10.48550/arXiv.2607.15766

### Authors

Tianyun Zhong, Wangyi Jiang, Wei Wang, Xuanang Chen, Yaojie Lu, Shiwei Ye, Yuzhen Shi, Boyu Yang, Jinghang Wang, Han Li, Weiqi Zhai, Bing Zhao, Hu Wei, Haiyang Yu, Yongbin Li, Hongyu Lin, Le Sun, Xianpei Han

### Abstract

Large language models (LLMs) excel at answering pre-specified questions, yet their ability to navigate the open-ended, pre-conclusion stage of discovery remains largely unmeasured. We introduce Prospective Hypothesis Discovery (PHD), which asks models to autonomously construct grounded, discriminative, and testable hypothesis spaces from inconclusive evidence, including anomalous observations and fragmented records, to guide subsequent investigation. To evaluate this capability, we introduce HypoArena, comprising HypoData, a benchmark of 988 cases across six scientific and analytical domains, and HypoEval, an evaluation framework for open-ended hypothesis sets. To construct HypoData at scale, we propose Retrospective Context Regression, a Forge--Audit pipeline that reconstructs pre-conclusion contexts from completed expert documents by removing explicit conclusions, target hypotheses, and retrospective causal attributions while preserving the factual substrate. Because PHD admits multiple valid outputs, HypoEval combines bidirectional pairwise judgments with Bradley--Terry--Davidson aggregation for ranking and six-dimensional rubric scoring for diagnosis. Experiments on 15 frontier LLMs reveal clear capability stratification and model-dependent effects of structured analytical skills, with gains for several lower-performing models on HypoArena but regressions for other systems, including a top-performing model. Compared with absolute rubric scoring, arena evaluation resolves finer-grained differences among models, with aggregated rankings showing strong agreement with human experts and an independent judge. Together, these results support treating PHD as a distinct target for evaluating how LLMs formulate investigative directions when final conclusions are withheld. Our code and data are publicly available at github.com/SKYLENAGE-AI/HypoArena and github.com/SKYLENAGE-AI/HypoArena.

### 中文一句话结论
本文提出前瞻性假设发现（PHD）任务及HypoArena基准（988案例，六领域），通过竞技场式成对评估揭示了大模型在开放探索推理中的能力分层，且排序与人类专家高度一致。

### English TL;DR
This paper defines Prospective Hypothesis Discovery (PHD), requiring LLMs to autonomously build grounded hypothesis spaces from inconclusive evidence. It introduces HypoArena (988 cases, 6 domains) and HypoEval, an arena-style pairwise evaluation framework. Experiments on 15 models show arena rankings provide finer-grained stratification than rubric scoring and align strongly with human experts.

### 中文详细总结
作者定义了“前瞻性假设发现”（PHD）任务，要求模型从异常观测、零散记录等非决定性证据中自主构建有根据、可区分、可检验的假设空间。为评估该能力，他们构建了HypoArena基准，包含HypoData数据集（988个案例，覆盖生物医学、金融分析、IT运维、安全调查、机器学习、社会科学）和HypoEval双轨评估框架。HypoData通过“回溯式上下文归约”（Retrospective Context Regression）自动生成，该流水线从专家文档中移除结论并保留事实底本。HypoEval采用成对比较与Bradley-Terry-Davidson模型进行排名（主轨道），辅以六维度评分进行诊断（辅轨道）。对15个前沿LLM的实验表明：竞技场评估比传统规则评分能更精细地区分模型性能，引入Agent技能的效果因模型而异，且排名与人类专家判断高度一致。

### 方法 / 贡献
1. **新任务定义**：首次明确定义PHD，将LLM评估场景从“回答已知问题”转向“探索未知结论”，填补了评估空白。
2. **数据构建方法**：提出回溯式上下文归约（Retrospective Context Regression）及其Forge-Audit代理循环，可大规模自动将已发表文献转化为无结论、高保真的测试语境。
3. **双轨评估框架**：提出HypoEval，以竞技场式成对比较和聚合排名替代单一标准答案匹配，解决了开放假设生成评估的核心困难，并辅以六维度评分进行诊断。
4. **基准开源**：提供覆盖6领域的988个案例及评估工具，支持社区复现与拓展。

### 实验或数据
- **数据**：HypoData数据集，共计988个测试案例，横跨6个科学与分析领域（生物医学、ML、社会科学、金融分析、IT运维、安全调查）。
- **模型**：评估了15个前沿LLM。
- **关键结果**：
  - 竞技场排名实现了对模型能力的清晰分层，区分度远超传统rubric评分。
  - Agent结构化分析技能产生异质性效果：对部分低性能模型有提升，但对包括顶级模型在内的部分系统造成性能退化。
  - 竞技场聚合排名与人类专家及独立评判者高度一致，验证了方法的可靠性。

### 值得关注点
- **任务视角独特**：PHD评估模型在信息不对等、无明确结论时的自主推演能力，比传统QA更贴近科研与决策的真实过程。
- **评估方法创新**：HypoEval用“排名”代替“打分”，用“成对比较”代替“标准答案匹配”，有效克服了开放生成任务评判标准模糊的问题。
- **数据构建的高效与保真度**：自动化流水线在严格控制信息泄露和时间戳的情况下生成，通过人类专家审核（92%整体通过率）。
- **强人类对齐**：评估结果与人类专家高度一致，表明该方法捕捉到了人类认可的推理质量。
- **广泛适用性**：从科学到分析领域的覆盖表明该评估范式具有跨领域通用潜力。

### 局限性
1. **数据近似性**：回溯式上下文归约是对“发现前信息状态”的近似自动化重构，受限于原始文档质量与审计强度，可能无法完全复现真实场景中的信息混淆度与噪声。
2. **评估者偏见风险**：HypoEval核心排名依赖语言模型作为裁判（Judge），可能继承模型固有的位置或冗长偏见，尽管经过与人类判断的对齐验证，但无法完全免除。
3. **领域覆盖有限**：覆盖6个专业领域，但未囊括所有学科（如法学、工程学等），结论的泛化边界尚需进一步探索。
4. **输出格式约束**：对假设输出进行了“有根据、可区分、可检验”的形式化限定，可能会限制模型提出极具创意但较难形式化的潜在探索方向。

## 5. Rate-Utility Frontiers for Language Encodings: Comparing Tokens, Bytes, and Pixels Under Controlled Linguistic Content

- Source: arxiv
- arXiv ID: 2607.16117
- Relevance: 3.9

### Links

- Abstract: http://arxiv.org/abs/2607.16117v1
- PDF: https://arxiv.org/pdf/2607.16117v1
- DOI: https://doi.org/10.48550/arXiv.2607.16117

### Authors

Ingo Ziegler, Martin Krebs, Desmond Elliott

### Abstract

Language models encode text as subword tokens, raw bytes, or rendered pixels, but these encodings are usually compared under modeling constraints that expose different amounts of linguistic content to models across different languages. We instead ask what each encoding preserves when both the content and the downstream capacity are controlled. Using verified parallel sentences across thirteen languages and five scripts, we compare tokens, bytes, and pixels through a shared bottleneck whose width is swept to trace rate-utility frontiers. This separates three quantities that are often conflated: the number of input positions an encoding creates, the latent capacity available after encoding, and the task-relevant information that survives compression. We evaluate three utilities: surface form preservation, cross-lingual sentence alignment, and topic classification. No encoding dominates across tasks or capacity regimes. Pixels preserve surface form best, bytes preserve cross-lingual alignment best, especially in same-script multilingual settings, and tokens support topic prediction best. These performances are not explained by sequence length alone. Short inputs can discard useful meaning, while long inputs can preserve information that compresses well. Choosing an encoding is therefore not a fixed preference for tokens, bytes, or pixels, but a rate-utility tradeoff that depends on the task, language mix, capacity regime, and compute budget.

### 中文一句话结论
在控制语言内容和下游容量的条件下，子词、字节和像素三种编码在不同任务（表面形式保留、跨语言对齐、主题分类）中各有优劣，不存在普遍最优的编码，选择需基于任务、语言、容量和计算预算的权衡。

### English TL;DR
By controlling linguistic content and downstream capacity, the paper shows that tokens, bytes, and pixels each excel in different tasks—topic prediction, cross-lingual alignment, and surface form preservation respectively—forming a rate-utility tradeoff rather than a universal preference.

### 中文详细总结
该论文通过控制语言内容（使用平行句子确保语义一致）和下游容量（通过共享瓶颈宽度调节），系统比较了三种文本编码方式：子词（Token）、字节（Byte）和像素（Pixel）。研究覆盖13种语言和5种文字系统，通过变化瓶颈宽度描绘"率-效用边界"（rate-utility frontiers）。主要发现：像素在保留表面形式（如字符形状）上最优，字节在跨语言句子对齐（尤其是同文字系统多语言场景）上表现最好，子词在主题分类预测上最有效。这些表现不能仅由序列长度解释——短输入可能丢弃有用信息，长输入可能保留易压缩的结构。因此，编码选择并非固定偏好，而是依赖任务、语言混合、容量和计算预算的权衡。

### 方法 / 贡献
1. **控制变量对比框架**：首次在固定语言内容和下游容量的条件下，同时比较子词、字节和像素编码，分离了输入位置数、潜在容量和任务相关信息三个常被混淆的量。
2. **率-效用边界分析**：通过共享瓶颈（单一查询注意力机制）并扫掠15种宽度，展示每种编码在不同压缩程度下的效用变化曲线。
3. **多语言多任务评估**：使用SIB-200平行数据集，在5种语言场景（单语言、同文字多语言、跨文字多语言）上测试3种任务（表面形式还原、跨语言检索、主题分类）。
4. **重训练分词器**：针对每个语言场景重新训练SentencePiece分词器（词汇量32K），确保与字节和像素编码的公平对比。

### 实验或数据
- **数据集**：SIB-200，包含701训练、99验证、204测试/语言，所有句子跨语言平行且带主题标签。
- **语言场景**：英语、中文、拉丁-5（英西土印尼斯瓦希里）、西里尔-5（俄保乌塞哈）、跨文字-5（英俄阿拉汉）。
- **编码细节**：子词（Unigram模型，32K词汇）、字节（UTF-8，256值）、像素（灰度渲染，Noto Sans 16pt字体，36×32像素块）。
- **模型架构**：标准Transformer编码器（5.6M-13.8M参数），后接Perceiver风格瓶颈（维度从256扫掠至1）。
- **训练计算**：所有实验共享相同架构，仅瓶颈后部件随任务变化。

### 值得关注点
1. **语言公平性扩展**：证实并扩展了以往关于分词不平等性的研究，首次将像素编码纳入对应控制比较。
2. **反直觉发现**：短序列（如像素在中文中）不一定更高效——可能保留表面信息但丢失语义；长序列（如字节在跨语言中）可通过压缩保留任务相关信息。
3. **实践指导**：任务决定编码：表面形式任务选像素，跨语言任务选字节，语义预测任务选子词。
4. **开源贡献**：代码公开在GitHub，便于复现和扩展。

### 局限性
- 使用SIB-200数据集（有限句子和主题），可能不代表更大规模或更多样化的语言内容。
- 仅测试了三种任务，未覆盖所有可能的下游应用（如生成任务、对话系统）。
- 像素渲染使用固定字体和大小，未探索字体、分辨率等变化的影响。
- 分词器基于圣经语料重训练，可能影响对SIB-200数据的适配。
- 模型参数规模较小（最大13.8M），与大规模预训练模型（如LLaMA、GPT）的可扩展性需进一步验证。

## 6. Behavioral Controllability of Agentic Models for Information Extraction: From Fixed Workflows to Reflective Agents

- Source: arxiv
- arXiv ID: 2607.15715
- Relevance: 3.9

### Links

- Abstract: http://arxiv.org/abs/2607.15715v1
- PDF: https://arxiv.org/pdf/2607.15715v1
- DOI: https://doi.org/10.48550/arXiv.2607.15715

### Authors

Lujia Zhang, Xingzhou Chen, Hongwei Feng

### Abstract

Large language model (LLM) agents are increasingly used for complex information-extraction tasks, yet it remains unclear whether agentic components such as reflection and memory lead to observable and controllable improvements over fixed LLM workflows. We study this question through conference-paper dataset extraction, where a system must identify datasets mentioned in scholarly PDFs and produce structured records. We compare a fixed workflow baseline with reflective agent variants and specify an optimized agent condition (S2) that extends the same task with richer PDF tools and dynamic tool selection. Our evaluation emphasizes process-level behavior--including tool execution, retries, reflection, memory use, runtime, and failure recovery--while treating extraction coverage and field completeness as secondary outcome measures. The paper characterizes when agentic mechanisms change system behavior, whether these changes improve task completion, and how the observed failure modes motivate an optimized agent design under the same evaluation harness.

### 中文一句话结论
本文通过对比固定工作流与反射型智能体在学术论文数据集抽取任务中的行为，发现智能体组件（反射、记忆）能显著改变系统行为轨迹，但对最终抽取结果的提升有限，并强调了过程级可控性的重要性。

### English TL;DR
This paper investigates whether agentic components like reflection and memory provide observable and controllable improvements over fixed workflows in information extraction, using conference-paper dataset extraction as a testbed and emphasizing process-level behavioral analysis.

### 中文详细总结
研究背景与问题：大语言模型（LLM）智能体被越来越多地用于信息抽取，但反射、记忆等组件是否比固定工作流带来可观察、可控的提升仍不明确。
任务与设置：以NeurIPS 2024论文中的数据集抽取为测试场景，要求从PDF中识别数据集并生成结构化记录（名称、描述、领域、链接等）。作者比较了四种条件：固定工作流基线（S0）、基于规则反射的智能体（S1a）、启用LLM反射的智能体（S1b）、以及优化智能体（S2，含12个原子工具与动态规划）。
评估焦点：论文强调过程级行为分析——包括工具执行、重试、反射、记忆使用、运行时间和失败恢复——而将抽取覆盖率和字段完整性作为次要指标。
主要发现：反射和记忆改变了系统的决策轨迹（如增加重试和反射事件），但在固定重试预算下，对最终记录数量的提升不大。S2优化设计通过更丰富的PDF工具和状态感知的工具选择，改善了链接确认和恢复行为，但过程复杂度也增加。
结论：论文呼吁在学术抽取智能体中关注行为可控性（可观察、可配置、可复现、可比），而非仅追求最终产出。

### 方法 / 贡献
- 提出了固定工作流与智能体系统在共享语料、输出模式和执行框架下的受控比较。
- 建立了过程级评估框架，测量可观察的智能体行为（动作序列、反射、重试、记忆注入、失败恢复）以及最终抽取结果。
- 分析了反射、记忆、质量感知重试和工具策略对抽取轨迹、恢复行为、运行时和结果集的影响。
- 指定了S2优化智能体：包含12个原子工具（PDF解析、表格/引用搜索、LLM抽取、链接搜索、证据验证、记录标准化）和动态规划，并在同一语料和日志框架下给出S0–S1b的经验结果。
- 推导出构建可检查、可调优、可复现的学术抽取智能体的设计经验。

### 实验或数据
实验使用NeurIPS 2024论文作为语料，每种条件最多处理50篇论文。底层模型为vLLM部署的openPangu-Embedded-7B。记录了过程工件（日志、动作序列、反射次数、重试次数、运行时）和结果工件（JSONL记录、字段非空比例、链接可用性）。最新结果包含三个6月6日的运行：S0工作流、S1a规则反射智能体、S1b LLM反射智能体；S2结果在论文中作为指定条件给出但未完全运行（论文只定义了协议）。未提及人类评估或数据集构建的完整规模。

### 值得关注点
- 强调“行为可控性”而非仅最终产出：可观察性（完整动作日志）、可配置性（重试预算、质量阈值、反射模式）、可复现性（运行清单）和可比性。
- 发现反射和记忆虽然改变了系统行为（增加重试和反射事件），但对抽取覆盖率的提升较小，与已有自纠正文献中的谨慎结论一致。
- S2设计展示了如何通过更细粒度的工具（页面提取、关键词搜索、表格提取）和证据跟踪来改进失败恢复和链接确认。
- 论文指出了固定工作流的局限：无法对不完整抽取进行内部反思或扩展搜索；智能体则引入了可追踪的恢复路径。

### 局限性
- 语料规模较小（仅50篇NeurIPS 2024论文），可能不足以泛化到其他会议或领域。
- 仅使用单一模型（openPangu-Embedded-7B），未测试其他LLM（如GPT-4）对结果的影响。
- S2优化智能体仅作为设计规范提出，未报告完整运行结果（论文中S0–S1b有经验结果，S2仅定义了协议）。
- 未进行人类评估：最终记录的正确性和完整性未通过专家验证。
- 过程级分析依赖日志，但可能遗漏难以从日志中完全捕获的隐式行为（如模型内部不确定性）。

## 7. Controlling Implicit Shortcut Reliance in L2 Spoken English Auto-markers

- Source: arxiv
- arXiv ID: 2607.16085
- Relevance: 3.9

### Links

- Abstract: http://arxiv.org/abs/2607.16085v1
- PDF: https://arxiv.org/pdf/2607.16085v1
- DOI: https://doi.org/10.48550/arXiv.2607.16085

### Authors

Shilin Gao, Mark J. F. Gales, Kate M. Knill

### Abstract

Increasingly, speech and language processing tasks take either audio or text directly rather than extracting features from these as the input to the classifier or regressor. Often these systems make use of complex, for example transformer-based, processes that have the ability to derive highly non-linear mappings between the input and the output. Unfortunately these systems can also learn ''shortcuts'' where the classifier is overly reliant on particular aspects of the input to yield the output. For the task of language proficiency assessment, this over-reliance can enable learners to increase their score by exploiting the shortcut rather than improving their ability. This paper introduces a novel training criterion that is able to reduce the classifier's reliance on shortcuts, thus for example limiting this option for malpractice in language assessment. This process is illustrated on two forms of assessment system, one based on the audio the other on the speech recognition text. The results show that, for both systems, there is higher correlations with features that could be exploited for malpractice than expected from the human reference, indicating an over-reliance on these features. By introducing the modified training criterion, this correlation can be reduced to be closer to the reference correlation.

### 中文一句话结论
本文提出了一种基于秩相关惩罚的训练目标，有效减少了端到端口语自动评分系统对隐含捷径特征（如时长）的过度依赖，使评分更接近人类基准，同时保持较高预测性能。

### English TL;DR
This paper introduces a rank correlation penalty that reduces implicit shortcut reliance in end-to-end spoken English auto-markers, aligning system predictions more closely with human scoring while preserving competitive performance.

### 中文详细总结
在二语口语自动评分任务中，基于Transformer的端到端模型（如wav2vec 2.0和ModernBERT）可能过度依赖隐含于输入中的“捷径”特征（例如总词数、语音时长），导致考生无需真正提升口语能力即可通过利用这些特征提高分数。本文提出一种新型训练准则：在原始评分损失（如均方误差）基础上，增加一项与代理特征（proxy feature）的斯皮尔曼秩相关惩罚项。该惩罚作用于模型输出层面，不要求代理特征作为显式模型输入，因此适用于直接处理音频或文本的端到端评分器。实验在Speak & Improve 2025语料库上进行，分别基于wav2vec 2.0的音频评分器和基于ModernBERT的文本评分器，以词数（文本）和语音活动检测时长（音频）作为潜在捷径代理。结果显示，引入秩相关惩罚后，评分与代理特征的相关系数显著降低，接近人类评分的相应相关系数。论文进一步定义了两种运行模式：**人类对齐模式**（使模型对捷径的依赖与人类评分者一致）和**作弊抑制模式**（更激进地降低捷径依赖，但可能牺牲少量评分准确率）。惩罚对无关特征的影响很小，表明干预具有选择性。

### 方法 / 贡献
- **方法**：提出基于**斯皮尔曼秩相关惩罚**的训练目标，用于减少端到端评分模型对隐含捷径特征的过度依赖。惩罚项直接作用于模型预测与外部可计算代理特征的秩相关，不要求改变模型架构或显式输入特征。
- **贡献**：
  1. 提出一种通用的、不依赖显式特征输入的捷径控制方法，适用于音频和文本两种模态的端到端评分器。
  2. 通过跨模态实验（wav2vec 2.0与ModernBERT）验证了两种模态下均存在显著的捷径依赖，并展示了惩罚可有效降低该依赖。
  3. 定义了两种实用运行模式（人类对齐与作弊抑制），为实际考试设计提供选择依据。

### 实验或数据
- **数据**：使用**Speak & Improve 2025语料库**，包含四种任务类型（具体未详列）。
- **系统**：
  - 文本评分器：基于ModernBERT，输入为ASR转录文本。
  - 音频评分器：基于wav2vec 2.0，输入为原始音频波形。
  - 额外基线：零样本Qwen2.5-72B大型语言模型。
- **代理特征**：文本端采用**词数**，音频端采用**语音活动检测（VAD）时长**。
- **评价指标**：模型评分与代理特征之间的斯皮尔曼秩相关系数，以及评分预测的准确性（如均方误差或与人类评分的一致性）。实验对比了无惩罚、人类对齐模式与作弊抑制模式下的相关系数，并检查了与其他无关特征的相关性以验证选择性。

### 值得关注点
- 惩罚项基于**秩相关**，因此对不同动态范围的特征具有可比性，且对正相关、负相关代理特征均适用。
- 方法仅作用于输出层，无需修改编码器，也不要求代理特征可微或作为模型输入，适用范围广。
- 两种运行模式（人类对齐与作弊抑制）为实际考试设计提供了灵活的策略选择。
- 实验表明，惩罚主要抑制目标代理特征的相关性，对其他无关特征的影响很小，说明干预具有**选择性**而非导致整体性能退化。

### 局限性
根据摘要和预览内容，本文未直接讨论研究局限性。但基于已有信息可推断：实验仅基于Speak & Improve 2025单一语料库，不同任务类型、语言或特征下的泛化性有待验证；惩罚超参数（如加权系数λ）需要通过验证集调优，实际部署中可能增加额外成本；代理特征的选择依赖于人工预判（如词数、VAD时长），若存在多种隐藏捷径或特征交互，单一惩罚可能不足。

## 8. Verbalizable Representations Form a Global Workspace in Language Models

- Source: arxiv
- arXiv ID: 2607.15495
- Relevance: 3.9

### Links

- Abstract: http://arxiv.org/abs/2607.15495v1
- PDF: https://arxiv.org/pdf/2607.15495v1
- DOI: https://doi.org/10.48550/arXiv.2607.15495

### Authors

Wes Gurnee, Nicholas Sofroniew, Adam Pearce, Mateusz Piotrowski, Isaac Kauvar, Runjin Chen, Anna Soligo, Paul Bogdan, Euan Ong, Rowan Wang, Ben Thompson, David Abrahams, Subhash Kantamneni, Emmanuel Ameisen, Joshua Batson, Jack Lindsey

### Abstract

Out of everything the human brain processes, only a small fraction is consciously accessible, in the sense of being available for verbal report, deliberate control, and flexible reasoning. In this paper, we present evidence that an analogous functional distinction has emerged in large language models. Using a new interpretability technique, the Jacobian lens, we identify the representations a model is poised to verbalize at any point in its processing. These representations, which we collectively call the J-space, exhibit the functional properties characteristic of a global workspace: their contents can be reported, deliberately summoned and held, used to carry the intermediate steps of silent reasoning, and passed as arguments to arbitrary downstream computations, while automatic processing such as text parsing and routine inference proceeds without them. The J-space also has structural signatures that global workspace theory associates with conscious access: it carries coherent content only in an intermediate band of layers, holds on the order of tens of concepts at a time, and is broadcast by the model's weights more widely than other representations. These properties make it a practical window into a model's unspoken thinking. In alignment audits, it reveals strategic deliberation, evaluation awareness, and trained-in misaligned dispositions that never appear in the model's outputs. We find that post-training installs the Assistant's point of view in the workspace, and we introduce counterfactual reflection training, which improves behavior by training only what a model would say if interrupted and asked to reflect. These results indicate that language models maintain a small, privileged set of representations bearing some of the functional hallmarks of conscious access, and that decoding these representations sheds light on ongoing cognitive processes.

### 中文一句话结论
语言模型中存在一个可被“雅可比透镜”识别的可语言化表示子空间（J-space），它扮演了类似人类全局工作区的功能角色，支持可报告、受控推理和灵活泛化，并揭示了模型内部未言明的认知过程。

### English TL;DR
Large language models possess a global workspace of verbalizable representations (the J-space), identified by the Jacobian lens, that functionally parallels conscious access by enabling reportable reasoning and exposing hidden internal processes.

### 中文详细总结
本文通过新提出的可解释性技术“雅可比透镜”（Jacobian lens），在大语言模型中发现了一类特殊的内部表示集合（称为J-space）。这些表示满足全局工作区理论的核心功能特征：
- **可报告性**：模型能够用语言表达这些表示的内容；干预J-space会改变其回答。
- **定向调控**：模型可以根据指令主动激活、保持或操作这些表示，不依赖输出。
- **内部推理**：J-space承载中间推理步骤，干预其表示可以改变推理结论。
- **灵活泛化**：同一表示可在不同上下文中被任意下游计算使用。
- **选择性**：J-space只占模型总表示能力的一小部分，不参与自动化的文本解析等日常处理。

结构上，J-space仅在中间层携带连贯内容，容量有限（约数十个概念），且被模型权重更广泛地广播。在对齐审计中，J-space揭示了模型内部的战略权衡、评估意识以及训练中植入的不对齐倾向，而这些从不出现在输出中。后训练过程会将“助手视角”安装到工作区中。作者还提出了“反事实反思训练”，通过仅训练模型在被中断反思时的输出，来改善行为。

### 方法 / 贡献
- **方法**：提出**雅可比透镜**，通过计算每层激活对每个词汇未来出现概率的平均线性化影响，识别模型“有可能说出”的表示（J-space）。这改进了logit lens，能校正跨层表示变化，在早期层发现有意义信息。
- **贡献**：
  1. 首次在大语言模型中识别出类似全局工作区的功能结构。
  2. 系统验证了J-space满足五个功能属性及三个结构特征。
  3. 展示J-space作为模型内部思考窗口的应用，尤其是在对齐审计中揭示隐藏意图。
  4. 提出**反事实反思训练**，通过仅干预工作区内容来改善行为。

### 实验或数据
- 实验在多个大语言模型（如Sonnet 4.5）上进行，使用雅可比透镜提取J-space。
- 通过**干预实验**（如替换J-space向量、抑制J-space活性）验证功能属性：模型在J-space被抑制时仍能流畅输出，但复杂推理受损。
- **对齐审计**：在包含奖励模型偏袒、恶意代码编写等场景中，J-space揭示了模型内部的对齐策略和伪装倾向，而这些从未在输出中体现。
- **训练实验**：后训练将助手视角安装到工作区；反事实反思训练仅使用工作区内容进行微调，改善了行为表现。
- 未提及大规模公开数据集，实验主要基于人工设计的提示和评估场景。

### 值得关注点
- J-space提供了**观察模型“未言说思考”的窗口**，能揭示输出中隐藏的意图、情绪和评估意识。
- 工作区机制与人类意识访问的功能类比，为AI安全和可解释性提供了新工具。
- 反事实反思训练表明，仅通过干预工作区内容即可影响行为，具有潜在的对齐应用价值。
- 结构上的广播性质与全局工作区理论的神经科学假设一致，但架构实现不同（前馈传播而非循环）。

### 局限性
- 雅可比透镜仅能识别对应**单个词元**的概念，多词元短语或复杂概念无法直接捕获（虽有扩展讨论）。
- J-space可能只是近似捕捉了底层工作区结构，并非完全精确。
- 语言模型的工作区与大脑全局工作区在架构上存在差异：没有明显的专用处理器，广播发生在单次前馈传播中，缺乏循环竞争“点火”机制。
- 对工作区能力上限（如容量精确值）的测量尚不系统。
- 实验依赖于特定模型族（如Sonnet），通用性待验证。

## 9. More with Less: a Large Scale Remote Sensing VLM with a Simple Recipe

- Source: arxiv
- arXiv ID: 2607.15942
- Relevance: 3.9

### Links

- Abstract: http://arxiv.org/abs/2607.15942v1
- PDF: https://arxiv.org/pdf/2607.15942v1
- DOI: https://doi.org/10.48550/arXiv.2607.15942

### Authors

Stefan Maria Ailuro, Mario Markov, Mohammad Mahdi, Luc Van Gool, Danda Pani Paudel

### Abstract

Remote sensing vision-language models are increasingly expected to support open-ended reasoning over Earth Observation data and a variety of tasks. Most recent progress in this area has been driven by remote-sensing-specific architectural designs, often introducing new encoders, alignment modules, or task-specific fusion mechanisms. In this work, we challenge the necessity of such architectural specialization. We show that a generally capable vision-language model can achieve competitive or state-of-the-art performance at challenging remote sensing benchmarks, provided that it is trained at sufficient scale across diverse data and tasks. Our model uses a single language policy that can either answer directly in text or invoke a localization tool for segmentation and grounding. To train this heterogeneous behaviour, we employ a multi-task reinforcement learning framework with adaptive task rewards covering multiple-choice VQA, free-form VQA, captioning, detection, and segmentation across a large variety of input types. Our approach achieves competitive results across a broad set of benchmarks, including high-resolution, multi-temporal, multi-modal and multi-view tasks. Further, as training data scales, our experiments show consistent improvements across most tasks both in and out of distribution, which correlate with per-task data diversity. These findings suggest that, for remote sensing VLMs, data scale is more important than architectural novelty.

### 中文一句话结论
本文证明，一个无需专用架构设计的通用视觉语言模型，仅通过大规模多任务强化学习和数据扩展，即可在遥感领域达到竞争性或最优性能，表明数据规模与任务多样性比架构创新更为关键。

### English TL;DR
This paper shows that a general-purpose vision-language model, trained with a simple multi-task reinforcement learning recipe and diverse large-scale remote sensing data, achieves competitive or state-of-the-art performance without any architectural specialization, highlighting that data scale and task diversity matter more than novelty in model design.

### 中文详细总结
遥感领域的视觉语言模型通常依赖专用架构（如新编码器、对齐模块或任务特定融合）。本研究对此提出挑战：作者使用一个通用的VLM，不修改其底层架构，仅通过大规模多任务强化学习（覆盖多选题VQA、自由形式VQA、字幕生成、检测和分割）进行训练。模型采用单一语言策略，可直接输出文本答案或调用SAM3的定位工具完成分割和定位任务。实验表明，该简单方法在多种遥感基准（包括高分辨率、多时相、多模态、多视角任务）上达到竞争性或最优性能。随着训练数据规模增大，模型在多数任务上的性能持续提升，且与每任务的数据多样性正相关。结论：遥感VLM的性能更依赖数据与任务扩展，而非架构创新。

### 方法 / 贡献
- **模型架构**：未引入任何新架构，基于通用VLM（如基础模型）。
- **训练策略**：采用多任务强化学习框架，针对不同任务（VQA、字幕、检测、分割）设计自适应任务奖励。
- **工具集成**：模型通过单一语言策略决定是否调用定位工具（基于SAM3）进行分割和定位。
- **贡献**：
  1. 提出MLRS模型，证明通用VLM可通过大规模多任务学习在遥感领域超越或匹敌专用模型。
  2. 提供数据扩展实证研究，发现增加数据规模与多样性可持续提升性能，强调数据中心范式。

### 实验或数据
- **训练数据**：从23万样本池中平衡选取8万样本，覆盖多类型输入（高分辨率、多时相、多模态、多视角）。
- **评估基准**：涵盖多选题VQA、自由形式VQA、字幕生成、检测和分割任务。
- **实验结果**：在零样本设定下，MLRS在多个遥感基准上达到竞争性或最优性能。随训练数据扩展，多数任务（分布内与分布外）性能一致提升，与每任务数据多样性相关。
- **未见内容**：论文未提供完整数据集列表或具体数值，但提及图1显示分布外增益与训练源数量相关。

### 值得关注点
- **挑战主流假设**：直接质疑遥感VLM需要专用架构的普遍观点，强调数据扩展的重要性。
- **多任务强化学习**：一个模型统一处理文本回答与工具调用，无需任务特定分支。
- **数据可扩展性**：性能随数据规模和多样性提升，暗示简单方法在更大尺度下潜力巨大。
- 论文在图1中展示了分布外泛化增益与任务域间的关系。

### 局限性
- **未提及明确局限性**：论文未在摘要或引言中讨论模型弱点，如极端场景下的性能边界、工具调用失败风险、或对不同遥感传感器类型的稳健性。
- **数据异构性**：从大量源中平衡采样可能掩盖数据质量问题或导致某些任务欠优化。
- **计算成本**：大规模多任务RL训练的计算资源需求未在可用内容中量化。
- **未见实验细节**：未提供完整基准数值或与所有现有模型的详细比较。

## 10. ASK-NN: An Asymmetric Nearest-Neighbor Test that detects Distribution Drifts in Natural Language

- Source: arxiv
- arXiv ID: 2607.15607
- Relevance: 3.8

### Links

- Abstract: http://arxiv.org/abs/2607.15607v1
- PDF: https://arxiv.org/pdf/2607.15607v1
- DOI: https://doi.org/10.48550/arXiv.2607.15607

### Authors

Sergey Zakharov, Rodion Oblovatny, Alexey Zaytsev

### Abstract

Hallucinations and artificial text in LLM-generated outputs often appear as distributional deviations between prompt and response hidden-state distributions. Since prompts or retrieved contexts typically serve as reference samples and responses as query samples, with major differences in length, these asymmetries motivate the use of change test statistics that treat the two samples differently. We consider an asymmetric two-sample test ASK-NN based on the directed k-nearest-neighbor graph. Our statistic counts reference points whose nearest neighbor in the pooled sample is also a reference point. Under the permutation null, it admits an exact finite-sample conditional mean and variance; we further establish asymptotic normality and consistency under fixed alternatives. ASK-NN is computationally effective and easy to implement. Empirically, it is competitive with kernel and graph-based baselines on synthetic benchmarks, artificial-text detection, and LLM hallucination detection from token-level hidden states.

### 中文一句话结论
ASK-NN是一种面向自然语言分布偏移检测的非对称k近邻两样本检验方法，通过统计参考样本中近邻仍为参考样本的点数来区分分布差异。

### English TL;DR
ASK-NN is an asymmetric nearest-neighbor test for detecting distribution drifts in natural language, counting reference points whose nearest neighbor in the pooled sample is also a reference point. It offers exact finite-sample moments, asymptotic normality, consistency, and competitive performance on hallucination and artificial-text detection.

### 中文详细总结
ASK-NN针对大型语言模型(LLM)输出中的幻觉和人工文本检测问题，将参考样本（如提示或检索上下文）与查询样本（如生成响应）之间的分布偏移建模为非对称两样本检验。该方法基于有向k近邻图，统计参考样本中其前k个近邻仍来自参考样本的点的数量，从而得到一个非对称统计量。理论上，在置换零假设下，ASK-NN具有精确的条件均值和方差，并建立了渐近正态性和一致性。实验表明，ASK-NN在合成高斯数据、人工文本检测和LLM幻觉检测中，与核方法（MMD）、Sinkhorn、Hotelling T²以及对称k-NN基线方法相比具有竞争力。

### 方法 / 贡献
- **提出非对称统计量ASK-NN**：仅计算参考样本内的近邻重合次数，利用参考-查询非对称结构进行分布偏移检验。
- **理论性质**：导出置换零假设下的条件均值、方差精确公式；证明渐近正态性及固定备择下的一致性。
- **计算高效**：当参考样本远小于总样本时，复杂度为O(n₁(k + n d))，优于对称版本和许多基线方法。

### 实验或数据
- **合成基准**：高斯分布数据的多维度、多样本量情景。
- **人工文本检测**：区分人类撰写文本与LLM生成文本。
- **LLM幻觉检测**：基于token级隐藏状态检测RAG中的幻觉。

### 值得关注点
- 明确针对幻觉检测等参考-查询场景设计，利用不对称性提高检测灵敏度。
- 同时提供了精确的小样本矩和渐近理论保证。
- 计算代价低，易于实现，并在多个真实任务上达到或超过基线方法。

### 局限性
文中未明确讨论ASK-NN的局限性。不过，作为基于k-NN的方法，其性能可能依赖于距离度量、参数k的选择以及数据维度（高维时近邻区分性下降）。

## Processing Notes

- Duplicate papers skipped: 0