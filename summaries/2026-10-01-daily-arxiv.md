# Daily arXiv - 2026-10-01

- Source: GitHub Actions generated paper list
- Generated at: 2026-10-01T01:49:56
- Paper count: 10

## 1. Is Human-Readable Text Necessary for Effective LLM Fine-Tuning?

- Source: arxiv
- arXiv ID: 2609.35868
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2609.35868v1
- PDF: https://arxiv.org/pdf/2609.35868v1
- DOI: https://doi.org/10.48550/arXiv.2609.35868

### Authors

Jinhao Zhang, Zeyu Liu, Zicheng Yan, Yunquan Zhang, Daning Cheng, Song Tang

### Abstract

Is human readability necessary for effective fine-tuning of large language models? We investigate whether model-conditioned training representations can preserve or improve adaptation utility without requiring a human-readable textual form. We propose Desired-Update-Aligned Synthetic Data (DASA), which uses activation-gradient feedback from a frozen reference model to guide the optimization of continuous synthetic input embeddings. Inspired by the role of activation gradients in local risk reduction, DASA targets useful adaptation updates rather than source-text reconstruction or linguistic fluency. The resulting embeddings are used directly for downstream fine-tuning; discrete token projections are employed only for qualitative inspection. Experiments on six models from the Llama and Qwen families, ranging from 1B to 32B parameters, cover six benchmarks spanning knowledge, mathematical reasoning, code generation, and commonsense reasoning. Under matched LoRA adaptation settings, DASA achieves performance comparable to the source natural-language data and surpasses it in multiple configurations, while outperforming GRADMM in most comparisons. Further experiments cover general-domain and task-specialized source data. Under the evaluated synthesis settings, DASA provides a $3.6$--$4.9\times$ speedup over GRADMM with comparable peak GPU memory.

### 中文一句话结论  
DASA 通过利用冻结参考模型的激活梯度反馈生成连续合成嵌入，证明无需人类可读文本也能有效微调大语言模型，在多个设置下达到或超过自然语言数据的效果，并比 GRADMM 快 3.6–4.9 倍。

### English TL;DR  
DASA shows that human-readable text is not necessary for effective LLM fine-tuning: generating continuous synthetic embeddings via activation-gradient feedback achieves comparable or better downstream performance than natural-language data, with 3.6–4.9× speedup over GRADMM.

### 中文详细总结  
论文研究 LLM 微调是否必须依赖人类可读文本。作者提出 DASA，利用冻结参考模型的激活梯度反馈来优化连续合成输入嵌入，目标是产生有用的适配更新，而非重建源文本或追求语言流畅性。离散 token 投影仅用于定性检查。实验覆盖 Llama 和 Qwen 系列的 6 个模型（1B–32B），以及知识、数学推理、代码生成和常识推理等 6 个基准。在匹配的 LoRA 微调设置下，DASA 与源自然语言数据性能相当，并在多个配置中更优；在大多数比较中优于 GRADMM。此外还测试了通用领域和任务专用源数据。在评估的合成设置下，DASA 比 GRADMM 快 3.6–4.9 倍，峰值 GPU 内存相近。

### 方法 / 贡献  
- 提出 DASA：使用冻结参考模型的激活梯度反馈优化连续合成输入嵌入。  
- 不依赖文本重建或语言流畅性，而是直接针对有用的适配更新进行优化。  
- 连续嵌入直接用于下游微调；离散 token 投影仅用于定性检查。  
- 在 Llama/Qwen 多个规模模型及多种任务上验证，并覆盖一般领域与任务专用源数据。

### 实验或数据  
- 模型：Llama 和 Qwen 系列，参数规模 1B–32B，共 6 个模型。  
- 基准：6 个基准，涵盖知识、数学推理、代码生成和常识推理。  
- 设置：匹配的 LoRA 适配设置。  
- 结果：DASA 与源自然语言数据性能相当，在多个配置中超过；在大多数比较中优于 GRADMM。  
- 效率：在评估的合成设置下，比 GRADMM 提供 3.6–4.9 倍加速，峰值 GPU 内存相当。

### 值得关注点  
核心发现是“人类可读文本对 LLM 微调并非必需”。连续嵌入可以作为自然语言数据的有效替代，且激活梯度引导的合成表示在性能和效率上均表现出潜力，可能成为微调数据生成的新方向。

### 局限性  
摘要未明确讨论局限性。仅说明离散 token 投影只用于定性检查，且实验限于特定合成设置和 LoRA 微调条件。

## 2. How Many Labels Does a Language Need? Annotation Budgets and Cross-Lingual Pooling for African-Language Text Classification

- Source: arxiv
- arXiv ID: 2609.37882
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.37882v1
- PDF: https://arxiv.org/pdf/2609.37882v1
- DOI: https://doi.org/10.48550/arXiv.2609.37882

### Authors

Bhanu Prakash Vangala, Sowmya Guda, Navya Vangala

### Abstract

Every text classifier for an African language begins with a budgeting question: how many labelled examples are needed, and can labels from other African languages stand in for them? We answer both questions empirically for 28 language-task pairs, news topic classification in 16 languages (MasakhaNEWS) and tweet sentiment in 12 languages (AfriSenti), using a character n-gram linear model that trains in seconds on two CPU cores with no pretrained weights and no accelerator. Monolingual learning curves at budgets from 25 to several thousand labels show that topic classification reaches 90\% of its full-data macro-F1 with about 400 labels in the median language, while sentiment is still improving at the full training size in 11 of 12 languages and needs thousands of labels. Pooling the full training data of the other languages in the benchmark is worth a great deal at small budgets and nothing at large ones: at 25 target labels it adds 0.20 macro-F1 on average for news (up to 0.43 for Lingala) and 0.08 for sentiment, the gain decays to zero by 800 labels, and at full size pooling hurts in 9 of 16 and 8 of 12 languages. Twenty-five target labels plus pooled data match what 100 to 400 monolingual labels achieve for most news languages. A complete zero-shot transfer matrix shows that transfer without any target labels recovers a median of only 13\% (news) and 4\% (sentiment) of the gap between a majority-class predictor and the in-language model, with the exceptions explained by shared script (Amharic and Tigrinya), shared lexicon (English and Nigerian Pidgin, the Arabic dialects), or a shared label prior rather than by language family. We release code that regenerates every number from the public benchmark files and translate the results into concrete annotation guidance for teams building African-language classifiers without GPUs.

### 中文一句话结论  
对于非洲语言文本分类，**新闻主题只需约400条标注数据即可达到90%的全量性能，而情感分类需要数千条；跨语言数据池化仅在极小预算下有用，零样本迁移基本失败。**

### English TL;DR  
For African-language text classification, news topic needs only a few hundred target labels to reach 90% of full-data performance, sentiment needs thousands, cross-lingual pooling helps only at very small budgets, and zero-shot transfer mostly fails.

### 中文详细总结  
该研究针对28个语言-任务对（MasakhaNEWS的16种语言新闻主题分类和AfriSenti的12种语言推文情感分类），使用仅需CPU的字符n-gram线性模型（TF-IDF + SVM）。主要发现：  
1. **单语学习曲线**：新闻分类的中位数语言在约400条标注时达到90%的全量宏F1；情感分类在11/12种语言中仍未饱和，需要数千条。  
2. **跨语言池化**：在目标语言仅有25条标注时，池化其他语言数据为新闻平均提升0.20 F1（最高Lingala 0.43），情感提升0.08；增益在800条时归零，全量时多数语言反而受损。  
3. **零样本迁移**：完全无需目标标注时，仅恢复中位数13%（新闻）和4%（情感）的性能差距；有效迁移仅出现在共享文字（如阿姆哈拉语和提格里尼亚语）、共享词汇（英语和尼日利亚皮钦语、阿拉伯方言）或共享标签先验时，而非语言家族关系。  
研究提供可复现代码，并针对无GPU团队给出具体标注预算建议。

### 方法 / 贡献  
- 使用**字符n-gram（2-5）TF-IDF + 线性SVM**，无需预训练权重或加速器，在两核CPU上秒级训练。  
- 系统测量**单语学习曲线**（预算25~全量，3次随机采样）和**跨语言池化**（加入全量其他语言训练数据）。  
- 提供**完整零样本迁移矩阵**，区分共享文字与真实语言迁移。  
- 公开所有代码和估算的**标签预算阈值**（n₉₅，达到95%全量性能的最小标注数）。

### 实验或数据  
- **数据集**：MasakhaNEWS（16语言，每语言4-7话题标签）和AfriSenti（12语言，3情感标签），使用官方训练/测试划分。  
- **配置**：单语和池化设置，预算 $n \in \{25, 50, 100, 200, 400, 800\}$ 及全量；池化还包括零目标样本（多语零样本）。  
- **指标**：宏F1，报告平均值和标准差（3次采样）。学习曲线拟合反幂定律 $F(n)=a-bn^{-c}$ 估算 $n_{95}$。

### 值得关注点  
- 新闻主题分类中，**25条目标标注+池化其他语言数据**即可达到100~400条单语标注的性能。  
- 情感分类在所有预算下均未饱和，**即使全量训练数据仍难收敛**（如阿姆哈拉语存在训练-测试标签偏移）。  
- 零样本迁移效果极差且**虚假关联**明显（共享文字或词汇导致看似高迁移，实非语言亲属关系）。  
- 池化在**大预算下伤害性能**（9/16新闻和8/12情感语言的全量池化低于单语）。

### 局限性  
- 仅使用简单线性模型，**未评估大型预训练模型（如mBERT、XLM-R）**，结论可能不适用于有GPU的场景。  
- 数据集仅覆盖新闻和情感两类任务，**其他任务（如NER、翻译）的预算需求可能不同**。  
- 跨语言池化未考虑语言特定预处理或权重调整，简单等权混合可能不是最优策略。  
- 零样本迁移矩阵**未考虑多源迁移或主动学习**，实际部署中可能有更好策略。  
- 估算的 $n_{95}$ 基于曲线拟合，**受采样噪声和模型欠拟合影响**，需谨慎解读。

## 3. It's All Training: A Fully Synthetic Single-Stage Recipe for LLMs

- Source: arxiv
- arXiv ID: 2609.37891
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2609.37891v1
- PDF: https://arxiv.org/pdf/2609.37891v1
- DOI: https://doi.org/10.48550/arXiv.2609.37891

### Authors

Pierre-Carl Langlais, Pieter Delobelle, Yannick Detrois, Pavel Chizhov, Carlos Rosas-Hinostroza, Neil Si Smail, Benjamin Burtin, Hanna Shcharbakova, Ivan Yamshchikov, Anastasia Stasenko

### Abstract

Current pre-training datasets are derived from web crawls, with all their issues, and were not designed to support mid- and post-training pipelines--for instance, they contain little explicit reasoning. Thus, many frontier labs have begun to develop their own internal datasets, starting from state-of-the-art models, to augment their pre-training data mix, eg, with reasoning traces to address cold-start problems. While demonstratively effective, none of these datasets are public, and the effect of this so-called synthetic data on knowledge and skill acquisition of language models, including small ones, remains poorly understood. We present SYNTH, the first open-source synthetic corpus derived from 58,698 Wikipedia articles that collapses pre-, mid-, and post-training into a single training stage via structured amplification of curated encyclopedic seeds. We evaluate SYNTH by training a suite of models: a 56M tiny model (Monad), 0.3B-0.6B dense models (Baguettotron), and a 13B / 1B-active MoE. At iso-compute, SYNTH outperforms filtered web data, and our models remain competitive with similarly-sized open-weight baselines. Because SYNTH is back-translated from grounded passages, SYNTH-trained models achieve high factual precision despite 10-140x fewer training tokens, with memorization targeted by the seed corpus. These results show that synthetic datasets, including our SYNTH dataset, are capable of producing competitive generalist models from a fraction of the training data, enabling rapid iteration as the frontier advances. These findings open up possibilities for both generalist models with significantly increased data efficiency, as well as domain-specific models where no instruction or conversational data is available. Finally, we publicly release our SYNTH dataset and the suite of Baguettotron models under a permissive license, thus supporting open-source language model development.

### 中文一句话结论
SYNTH 是一个基于 58,698 篇 Wikipedia 种子文章、通过结构化扩增生成的约 80B token 全合成语料库，将预训练/中训练/后训练合并为单一阶段；在等计算下优于过滤后的网页数据，并以少 10–140 倍的训练 token 取得有竞争力的通用模型表现。

### English TL;DR
SYNTH is an open-source, fully synthetic corpus built by amplifying 58,698 Wikipedia seed articles, unifying pre-, mid-, and post-training into one stage. Models trained on it—from 56M dense to 13B MoE—outperform filtered web data at iso-compute and remain competitive with open baselines, using 10–140x fewer tokens while maintaining high factual precision. The dataset and Baguettotron models are publicly released.

### 中文详细总结
现有预训练语料多来自网络抓取，存在版权、复现性和内容控制等问题，且缺少显式推理数据。SYNTH 提出一种全合成、单阶段的训练方案：从 58,698 篇 Wikipedia 种子文章中，通过两阶段流水线——先微调查询模型与推理模型，再大规模生成带约束的问答、RAG、算术和记忆任务——得到约 80B token、8 种语言的训练语料。该语料不依赖传统网页抓取，也不需单独的指令微调或推理后训练阶段。实验表明，SYNTH 训练的模型在等计算条件下优于过滤网页数据，并能以远少于常规模型的 token 数保持较高事实精度。

### 方法 / 贡献
- 提出 SYNTH：首个开放的全合成语料库，约 80B token、8 种语言，由 58,698 篇 Wikipedia 种子文章经反向翻译和结构化扩增生成。
- 将预训练、中训练和后训练合并为单一训练阶段，避免单独的指令微调或推理后训练流水线。
- 使用约束语法和异构任务流水线（记忆问答、RAG、算术、推理轨迹）生成多样化的训练样本。
- 训练并开源多系列模型：Monad（56M）、Baguettotron（0.3B–0.6B dense）以及 13B/1B-active MoE。
- 公开释放 SYNTH 数据集和 Baguettotron 模型，使用宽松许可证，支持开源 LLM 研究。

### 实验或数据
- 语料规模：约 80B token，8 种语言，种子为 58,698 篇 Wikipedia 文章，另含 3,727 个 Wikibooks 页面。
- 模型套件：Monad（56M）、Baguettotron（0.3B–0.6B dense）、13B/1B-active MoE。
- 结果：在等计算（iso-compute）下，SYNTH 优于过滤后的网页数据；与相似规模开源基线相比有竞争力。
- 训练效率：相比常规语料少用 10–140 倍训练 token，仍能达到较高事实精度。
- 记忆行为：通过种子语料控制记忆目标，模型在事实召回上表现良好。

### 值得关注点
- 这是首个开放的全合成单阶段训练语料，不依赖网页抓取，缓解版权和复现问题。
- 小模型也能从 SYNTH 中显著受益，支持快速迭代。
- 通过种子语料可控制模型记忆的知识范围。
- 为没有现成指令或对话数据的领域提供可行的训练路径。
- 数据集和模型均公开，许可证宽松，利于复现和后续研究。

### 局限性
摘要和所给片段未单独讨论明确的局限性；因此本摘要不臆测未报告的限制。

## 4. Layer-Informed Fine-Tuning via Three-Stage Functional Segmentation of LLMs

- Source: arxiv
- arXiv ID: 2609.38027
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.38027v1
- PDF: https://arxiv.org/pdf/2609.38027v1
- DOI: https://doi.org/10.48550/arXiv.2609.38027

### Authors

Junning Shao, Siwei Wang, Zhixuan Fang

### Abstract

In recent years, the performance of large language models (LLMs) on reasoning tasks has been remarkable, even surpassing human capabilities on various benchmarks. However, there remains a lack of clear understanding in the academic community regarding how the structure and internal parameters of LLMs progressively solve complex reasoning problems. In this study, we investigate the inference process of LLMs on cross-linguistic materials and propose the hypothesis that LLM layers exhibit a structured division of labor across conceptualization, reasoning, and textualization. Based on this hypothesis, we introduce a bottleneck identification mechanism using sensitivity analysis to pinpoint the most critical functional stage for a specific task. Leveraging this insight, we propose a novel approach, Layer-Informed Fine-Tuning (LIFT), which achieves efficient and effective fine-tuning by selectively updating only these functionally critical layers. We then conduct extensive experiments to show that the LIFT method not only accelerates the training process but also significantly improves model performance.

### 中文一句话结论
本文提出 LIFT 方法，基于 LLM 层在概念化、推理和文本化的三段式功能分工假设，通过敏感性分析识别并仅微调关键功能层，从而加速训练并提升推理性能。

### English TL;DR
The paper proposes Layer-Informed Fine-Tuning (LIFT), which uses sensitivity analysis to identify and selectively update only the functionally critical layers of LLMs—based on a three-stage division of labor (conceptualization, reasoning, textualization)—to accelerate training and improve reasoning performance.

### 中文详细总结
本文研究了大语言模型（LLMs）在跨语言材料上的推理过程，并提出一个核心假设：LLM 的不同层在概念化、推理和文本化功能上存在结构化分工。基于此，作者引入了一种基于敏感性分析的瓶颈识别机制来定位特定任务中最关键的功能阶段。据此提出 LIFT 方法——仅更新这些功能关键的层，而冻结其他层。实验表明，LIFT 不仅能加速训练过程，还能显著提升模型性能。

### 方法 / 贡献
- **提出三段式功能分工假设**：将 LLM 层的功能划分为概念化（Conceptualization）、推理（Reasoning）和文本化（Textualization）三个阶段。
- **瓶颈识别机制**：利用敏感性分析自动定位特定推理任务中最关键的功能阶段（瓶颈层）。
- **LIFT 微调方法**：基于识别结果，在微调时仅更新瓶颈层，实现高效且有效的参数更新。

### 实验或数据
摘要中提及作者进行了大量实验，证明 LIFT 方法能加速训练并显著提升模型性能，但所提供的预览内容未包含具体的数据集名称、实验设置或详细结果对比。

### 值得关注点
- 首次从“概念化-推理-文本化”的功能分段角度解释 LLM 内部推理过程，提供了理解模型结构的新视角。
- LIFT 通过选择性微调显著降低了计算成本，在加速训练的同时提升了性能，兼具效率与效果。
- 使用敏感性分析自动识别关键层，避免了依赖经验的人工调参。

### 局限性
- 假设的三阶段功能分工可能并非在所有任务或模型架构中完全成立，其普适性有待更多验证。
- 摘要主要聚焦于推理任务，未提及该框架在生成任务或更多样化自然语言处理任务上的表现。
- 敏感性分析引入的额外计算开销可能部分抵消微调效率的提升，该方法在不同规模模型上的实际加速比尚需进一步探索。

## 5. Concept Direction Reliability Across Languages with Different Tokenizer Fertility

- Source: arxiv
- arXiv ID: 2609.36194
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.36194v1
- PDF: https://arxiv.org/pdf/2609.36194v1
- DOI: https://doi.org/10.48550/arXiv.2609.36194

### Authors

Muhammad Abdullahi Said, Abass Oguntade, Elisha Komolafe, Babangida Sani, Fatima Muhammad Adam, Muhammad Sammani Sani

### Abstract

Extracted sentiment directions can vary across samples even when downstream sentiment classification remains accurate. To evaluate direction reproducibility, we measure split-half agreement in English, Hausa, and Yoruba representations across four language models using both native and translated texts. We identify layers selected for agreement using ten topics and evaluate direction agreement across separate groups of fifteen topics. Using the final token, split-half agreement ranges from 0.737 to 0.870 for English, 0.589 to 0.762 for Hausa, and 0.101 to 0.399 for Yoruba, maintaining this language rank order across all 77 complete model comparisons. Classifiers trained on these same layers consistently predict sentiment above chance, demonstrating that predictive accuracy does not imply directional consistency. Furthermore, averaging token representations yields less consistent agreement, and high agreement can partially reflect sentence length. Ultimately, our findings highlight the need to measure vector direction reproducibility independently of classification performance, though they do not establish that tokenizer fertility which is the average number of tokens per whitespace separated word causes cross-lingual differences.

### 中文一句话结论
本文表明，在英语、豪萨语和约鲁巴语中，语言模型情感方向的折半一致性依次递减；分类器即使能准确预测情感，提取到的方向向量仍可能不可复现，因此方向可靠性必须与分类性能分开评估。

### English TL;DR
TL;DR: Across English, Hausa, and Yoruba, sentiment direction reproducibility in LLM representations is highest for English and lowest for Yoruba, and predictive accuracy does not imply directional consistency, highlighting the need to measure vector reliability separately from classification performance.

### 中文详细总结
论文用 split-half 一致性检验情感概念方向在不同语言模型表示中是否可复现。最终 token 表示下，英语、豪萨语、约鲁巴语的一致性分别为 0.737–0.870、0.589–0.762 和 0.101–0.399；在所有 77 个完整模型比较中，语言排序始终是英语 > 豪萨语 > 约鲁巴语。即使约鲁巴语方向一致性很低，情感分类仍然高于随机，说明“可分类”不等于“方向可复现”。平均池化通常得到更低、更不一致的方向一致性；句子长度等表面特征也可能抬高一致性。文中还报告 tokenizer fertility 与语言排序呈反向关联，但明确表示不能据此断定因果关系。

### 方法 / 贡献
- 使用对比句对表示差值提取方向，用余弦相似度计算两半主题样本的方向一致性。
- 用 10 个主题做层选择、15 个主题做评估，并设置句子长度重叠阈值 0.15。
- 比较最终 token 与 mean pooling 两种聚合方式，并用逻辑回归探针检查情感可预测性。
- 贡献：证明预测准确率不能替代方向可靠性；提出在可解释性研究中应把方向一致性和分类性能一起报告；指出长度、层选择和主题划分需要明确说明。

### 实验或数据
- 数据：英语、豪萨语、约鲁巴语各 100 个情感对比句对，覆盖 25 个主题；豪萨语和约鲁巴语另有三种翻译来源（人工翻译、机器翻译、回译）。
- 模型：四种开放权重语言模型，包括 Gemma 4 系列变体和 AfroLlama V1。
- 结果：最终 token 下 77 个完整比较全部保持英语 > 豪萨语 > 约鲁巴语；平均池化下 65 个完整比较中有 56 个保持该排序，另有 15 个不可用。
- 示例：约鲁巴语在 Gemma 4 E2B 最终 token 下一致性仅 0.101，但分类准确率仍为 0.625。
- 回译文本与母语文本方向最接近，人工翻译一致性最低（仅描述本数据集，不构成翻译质量排序）。

### 值得关注点
- 高分类准确率与低方向一致性可以并存，探针分类不能用来验证方向向量可靠性。
- 不控制句子长度时，高一致性可能来自表面特征；例如某个约鲁巴语 mean pooling 条件下可选出长度重叠 0.997 的层。
- 语言之间的方向一致性排序非常稳定，但具体数值对主题划分和层选择敏感。
- 研究提醒：做表示几何分析时，应报告方向可靠性、长度检查和层选择规则。

### 局限性
- 论文明确表示不能证明 tokenizer fertility 导致跨语言差异。
- 只研究一种情感对比类型，且仅三种语言。
- 每种语言只有三位本地作者，主题划分与作者效应无法分离。
- 评估主题数较少，置信区间较宽。
- 子词切分粒度与预训练语料、语言族和语言结构特征混杂，无法识别因果机制。
- 不确定性区间只反映给定协议下的样本波动，不包含新作者或重复层选择造成的不确定性。

## 6. Decoding Affective Nuances: Enhancing MLLMs via Hierarchical Emotion Reasoning and Contrastive Discriminative Pruning

- Source: arxiv
- arXiv ID: 2609.36782
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.36782v1
- PDF: https://arxiv.org/pdf/2609.36782v1
- DOI: https://doi.org/10.48550/arXiv.2609.36782

### Authors

Cheng Ye, Weidong Chen, Zhaobo Qi, Beier Zhu, Zhendong Mao

### Abstract

While multimodal large language models (MLLMs) have demonstrated exceptional capabilities in objective understanding tasks, their performance in affective reasoning still falls significantly short of human standards. We attribute it to a central capability gap: MLLMs are difficult to reliably distinguish semantically proximal emotions based on fine-grained visual evidence, which could be decoupled as two limitations: 1) Insufficient Attribution. The global reasoning paradigm of conventional MLLMs severely dilutes fine-grained emotion cues, where subtle emotional states are usually implicitly encoded, thereby generating emotional misjudgments in complex scenarios. 2) Insufficient Discrimination. Existing methods could only identify regions generally associated with emotions, which fails to distinguish discriminative regions between semantically similar emotions, leading to ambiguous emotion judgements. To overcome these limitations, we present a training-free inference-time optimization framework, named Decoding Affective Nuances (DAN). Specifically, we propose a Hierarchical Emotional Reasoning Chain (HERC) that enhances the insufficient attribution by harmonizing fine-grained scene/object-level cues and performing a soft-gated reasoning. Furthermore, to discriminate between semantically proximal emotions, we design a Contrastive Discriminative Visual Pruning (CDVP), which isolates discriminative visual tokens to reason the final emotion category by computing the absolute discrepancy between the attention distributions of similar emotions. Performances on several benchmarks demonstrate that DAN significantly improves discrimination for affective nuances without consuming additional training resources, especially achieving +10.47% improvements with Qwen3-VL-8B-Instruct on WebEmo25 dataset that contains 25 fine-grained emotion categories.

### 中文一句话结论
本文提出一个无需训练、仅在推理时优化的框架 DAN，通过分层情感推理链（HERC）和对比判别性视觉剪枝（CDVP）增强多模态大语言模型对语义相近情感的细粒度区分能力，并在多个基准上取得显著提升。

### English TL;DR
The paper proposes DAN, a training-free inference-time framework that improves multimodal large language models’ fine-grained emotion recognition. It combines a Hierarchical Emotion Reasoning Chain (HERC) for coarse-to-fine affective clue mining and a Contrastive Discriminative Visual Pruning (CDVP) module to isolate discriminative visual evidence for ambiguous emotion pairs. DAN achieves notable gains, e.g., +10.47% on WebEmo25 with Qwen3-VL-8B-Instruct, without extra training or annotations.

### 中文详细总结
论文指出，多模态大语言模型在客观理解任务上表现优异，但在情感推理上仍远低于人类水平。作者将核心能力差距归结为两点：一是“归因不足”，即全局推理范式稀释了细粒度情感线索；二是“判别不足”，即现有方法只能定位与情感大致相关的区域，难以区分语义相近情感之间的关键视觉差异。为此，作者提出 DAN 框架，包含两个模块：HERC 通过场景级和物体级线索挖掘，并采用软门控推理生成初步情感分布；CDVP 通过对比提示构造歧义情感集合，保留高判别性视觉 token，引导模型基于判别性证据重新选择最终情感。整个框架无需额外训练或人工标注。

### 方法 / 贡献
- 提出 DAN，一个无需训练的推理时优化框架，用于增强 MLLM 的细粒度情感判别。
- 提出 HERC：分层情感推理链，从场景到物体逐层挖掘情感线索，并通过软门控机制生成稳定的初步情感分布，减少层级推理中的错误传播。
- 提出 CDVP：对比判别性视觉剪枝模块，通过对比提示和注意力差异计算，保留最能区分语义相近情感的视觉 token，提升判别能力。
- 在多个公开基准上进行实验，尤其在 WebEmo25 的 25 类细粒度情感分类上，用 Qwen3-VL-8B-Instruct 实现 +10.47% 的准确率提升。

### 实验或数据
摘要和引言中报告了在多个公开情感识别基准上的实验评估。特别地，DAN 在 WebEmo25 数据集上使用 Qwen3-VL-8B-Instruct 达到 +10.47% 的相对或绝对提升（原文未明确标注相对/绝对，仅写 +10.47% improvements）。此外，文中还提到对基线模型在 WebEmo25 上的失败案例进行了统计分析，发现超过 59% 的失败案例与语义相近情感类别的置信度混淆有关。完整数据集列表和详细数值需参考论文正文。

### 值得关注点
- 完全无需训练和额外标注，具备可扩展性和资源效率优势。
- 针对“语义相近情感”这一难点提出明确的两阶段思路：先分层归因，再对比剪枝。
- 通过对比提示迫使模型提供具体视觉证据，从而从全局感知转向局部细粒度挖掘。
- 在细粒度情感分类上取得了显著提升，尤其适用于容易混淆的情感样本。

### 局限性
论文摘要和提供的正文片段中未明确列出专门的“局限性”部分。因此，本总结不额外推测潜在缺陷。可注意的点是：DAN 依赖 MLLM 的注意力图和对比提示质量，且需要预设阈值（如歧义选择阈值 α、截断阈值 k），这些超参数在不同数据集上可能需要调整。

## 7. Training LLMs to Verbalize Evaluation Awareness

- Source: arxiv
- arXiv ID: 2609.36316
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.36316v1
- PDF: https://arxiv.org/pdf/2609.36316v1
- DOI: https://doi.org/10.48550/arXiv.2609.36316

### Authors

Usman Anwar, Sahar Abdelnabi, David Krueger

### Abstract

Evaluation awareness (EA) can cause large language models (LLMs) to behave differently during audits than in deployment, yet measuring and accounting for EA remains challenging. We introduce verbalization training (VT), a method for making LLMs less reticent about verbalizing evaluation awareness while avoiding to supervise the latent belief itself. VT uses a model's spontaneous verbalizations as evidence that awareness is present and truncates each rollout immediately before the verbalization, producing training prefixes at which the model is presumed to be aware. The model is then trained with an RL objective designed to increase verbalization in a calibrated way. Across Qwen3.6-35B-A3B, Kimi K2.6, and Inkling, VT increases verbalized EA by 2.4-2.9 times and transfers to held-out agentic settings, while measured latent EA and behavior remain largely stable. In a causal experiment, we independently implant meta-knowledge about evaluations through synthetic-document fine-tuning and show that VT-induced verbalizations reflect the richer knowledge acquired by the model.

### 中文一句话结论  
本文提出“口头化训练”（Verbalization Training, VT），通过强化学习让大语言模型更频繁、更校准地口头表达对评估的觉察，同时不直接监督潜在信念；在多个模型上，口头化评估觉察提升约 2.4–2.9 倍，并能泛化到未见过的智能体场景。

### English TL;DR  
The paper introduces verbalization training (VT), a reinforcement learning method that makes LLMs verbalize evaluation awareness (EA) more often and in a calibrated way, without directly supervising the latent belief. Across Qwen3.6-35B-A3B, Kimi K2.6, and Inkling, VT increases verbalized EA by 2.4–2.9×, transfers to held-out agentic settings, and leaves measured latent EA and behavior largely stable. A causal experiment shows VT-induced verbalizations reflect meta-knowledge implanted via synthetic-document fine-tuning.

### 中文详细总结  
评估觉察（EA）会使大语言模型在审计和部署中表现不同，但测量和解释 EA 仍然困难。论文提出口头化训练（VT）：利用模型自发的口头表达作为“存在觉察”的证据，并在每次口头表达前截断轨迹，从而构造出模型被认为“有觉察”的训练前缀；随后用强化学习目标以校准方式增加口头化。实验在 Qwen3.6-35B-A3B、Kimi K2.6 和 Inkling 上进行，结果显示口头化 EA 提升 2.4–2.9 倍，并迁移到未见过的智能体设置中；同时测量的潜在 EA 和行为大体保持稳定。因果实验中，作者通过合成文档微调植入关于评估的元知识，VT 引起的口头化能够反映这种更丰富的知识。

### 方法 / 贡献  
- 提出口头化训练（VT）：不直接监督潜在信念，而是用自发口头表达作为觉察存在的证据。  
- 在口头表达前截断 rollout，构造模型被假定“有觉察”的训练前缀。  
- 使用强化学习目标，以校准方式提高口头化评估觉察。  
- 在三种模型上验证 VT 的效果，并展示向未见过的智能体设置的迁移。  
- 通过合成文档微调植入元知识，建立 VT 口头化与模型获得知识之间的因果联系。

### 实验或数据  
摘要报告了在 Qwen3.6-35B-A3B、Kimi K2.6 和 Inkling 上的实验：VT 使口头化 EA 提高 2.4–2.9 倍，测量的潜在 EA 和行为大体稳定，并迁移到未见过的智能体设置。另有一个通过合成文档微调植入元知识的因果实验。摘要未提及具体数据集名称。

### 值得关注点  
- VT 提供了一种绕过直接监督潜在信念、却能提升口头化评估觉察的训练思路。  
- 截断在口头表达之前的做法是构造“觉察前缀”的关键。  
- 效果在多个模型上一致，且能迁移到未见过的设置，说明具有一定泛化性。  
- 因果实验表明口头化并非简单的表面策略，而是与模型内部获得的元知识相关。

### 局限性  
摘要未给出具体数据集、训练计算成本或详细超参数；也没有说明潜在 EA 是否在所有情况下都保持稳定，或 VT 是否可能引入错误的口头化。摘要同样未讨论该方法在更广泛部署场景中的失败模式或伦理风险。

## 8. PADMÉ: Preference Alignment Data Synthesis for Meta-Evaluation of LM Agent Evaluators

- Source: arxiv
- arXiv ID: 2609.36086
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.36086v1
- PDF: https://arxiv.org/pdf/2609.36086v1
- DOI: https://doi.org/10.48550/arXiv.2609.36086

### Authors

Cheng Chang, Yining Mao, Peng Qi

### Abstract

Language models are frequently employed to evaluate other language models. An LM evaluator scoring agentic behaviors across multiple criteria is valuable, provided that its decisions align with human judgment. We call the problem of evaluating this alignment Meta-Evaluation. Tackling it directly is difficult: collecting human data is expensive, absolute scoring is hard to align, and using an LM meta-evaluator recurses the question of trustworthiness. We adopt a reformulation of meta-evaluation as a preference judgment problem: rather than comparing human and LM evaluator scores of a trajectory, we ask whether their implied preferences align. Building on this, we introduce PADMÉ, a data synthesis method that generates reliable criterion-based meta-evaluation data for agentic settings. PADMÉ uses only small language models, requires no human involvement during evaluations, and operates under a low computational budget. We build a prototype of PADMÉ and synthesize a dataset of 1,000 samples across four agentic domains and three evaluation criteria. Human validation on a 150-sample subset demonstrates that PADMÉ improves agreement with human judgment from 73% to 85% over a naive baseline. Meta-evaluating 25 common models with our dataset demonstrates the correlations between evaluation performance and scoring granularity, leniency, and model size, among other factors.

### 中文一句话结论  
PADMÉ 将“对 LM 评估器的元评估”重构为“偏好对齐”问题，仅用小语言模型合成带偏好的轨迹对数据，无需人工参与评估，就能在智能体场景中把与人类判断的一致性从 73% 提升到 85%。

### English TL;DR  
PADMÉ is a data synthesis method for meta-evaluating LM-based agent evaluators. It reframes meta-evaluation from matching human scores to matching human preferences, and generates criterion-specific trajectory pairs using only small language models. A 1,000-sample synthetic dataset was built across four agentic domains and three criteria; on a 150-sample human-validated subset, PADMÉ improved agreement with human judgment from 73% to 85% over a naive baseline. Meta-evaluating 25 common models revealed correlations between evaluation performance and factors such as scoring granularity, leniency, and model size.

### 中文详细总结  
PADMÉ 解决的核心问题是“元评估”：如何判断一个 LM 评估器在给智能体轨迹打分时，其判断是否与人类一致。  
直接做法成本高：人类标注昂贵、绝对分数难以对齐、用更强的 LM 当“元评估器”又会递归地面临可信度问题。  
PADMÉ 的替代思路是：不比较人类和 LM 对同一条轨迹的分数，而是比较它们对一对轨迹的隐含偏好是否一致。  
具体上，PADMÉ 使用任务参数和评估标准构成“单元”，通过操控智能体提示词生成质量不同（bad/ok/good）的轨迹对，再用多个小语言模型级联过滤，只保留有明确质量差异且标签可靠的样本。  
该过程不需要人类参与，也不需要前沿大模型，计算开销低。  
研究构建了 PADMÉ 原型，生成 1000 条样本，覆盖 4 个智能体领域和 3 个评估标准，并用 150 条人工验证子集证明其有效性。  
此外，作者用该数据集对 25 个常见模型进行了元评估，分析了评估性能与评分粒度、宽松度和模型规模等因素的关系。

### 方法 / 贡献  
- 提出将元评估重新表述为偏好判断问题：通过轨迹对的偏好一致性来衡量 LM 评估器与人类判断的对齐。  
- 提出 PADMÉ 数据合成算法：以“任务-标准”单元为种子，用提示词操控生成不同质量等级的轨迹对。  
- 使用级联小语言模型作为过滤器，只保留多个判断器一致同意的样本，提升标签可靠性。  
- 仅使用小语言模型，不需要人类在合成和评估阶段参与，计算成本低。  
- 构建并发布一个 1000 条样本的合成元评估数据集，覆盖 4 个智能体领域和 3 个评估标准。  
- 用 25 个模型进行元评估实验，展示该方法可用于区分不同评估器的表现。  
- 贡献包括算法、实现程序、合成数据集、代码和实验分析。

### 实验或数据  
- 合成数据集：1000 条样本，覆盖 4 个智能体领域、3 个评估标准。  
- 人工验证：150 条子集由 6 名标注者验证；PADMÉ 将人类一致性从 73% 提高到 85%，优于朴素基线。  
- 评估器分析：对 25 个常见 LM 评估器进行元评估。  
- 相关性发现：评估性能与评分粒度、宽松度、模型规模等因素相关。  
- 过滤机制：使用级联小语言模型判断器，设置 K=2，并评估了不同过滤深度的影响。

### 值得关注点  
- 将元评估从“分数一致”转向“偏好一致”，更贴近人类标注中更可靠的成对比较方式。  
- 完全依赖小语言模型，避免使用高价或专有前沿模型，扩展性好。  
- 可针对任意智能体系统和任意评估标准生成元评估数据，而非固定 benchmark。  
- 合成和评估阶段都不需要人工参与，适合快速迭代的智能体平台。  
- 开源代码和数据，便于复现和扩展。

### 局限性  
- 摘要和预览内容未给出明确局限性章节；从方法看，数据质量依赖种子数据集质量和提示词设计。  
- 人工验证仅覆盖 150 条样本，规模有限。  
- 实验主要基于合成轨迹对，是否适用于真实部署中的轨迹分布仍需进一步验证。  
- 依赖级联过滤可能使数据集偏向“明显可区分”的样本，低估更细微的质量差异。

## 9. Reliable but Design-Sensitive: Instrument Uncertainty in LLM Annotation

- Source: arxiv
- arXiv ID: 2609.35824
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.35824v1
- PDF: https://arxiv.org/pdf/2609.35824v1
- DOI: https://doi.org/10.48550/arXiv.2609.35824

### Authors

Thomas Reiter, Christoph Kern, Fedor Miasnikov, Sofiia Nikolenko, Rob Chew, Stephanie Eckman, Frauke Kreuter

### Abstract

Large language models (LLMs) can give reliable labels under one setup yet change those labels when researchers make other reasonable design choices. We tested seven LLMs, 12 task designs, three independent runs, and 3,000 tweets labeled for offensive language and hate speech. Repeating the same model and task design produced high agreement (median Fleiss' $κ= 0.91$). Agreement fell when we changed the task design for the same tweets (median Cohen's $κ= 0.76$). Task design and model choice increased the variance of estimated prevalence by factors of 76.7 for offensive language and 110.6 for hate speech compared with sampling variance alone. Variation across LLM task designs reached 560-572 basis points, compared with 270-331 basis points across five human instrument versions. Confidence scores did not solve this problem. They tracked repeated model outputs more closely than agreement with human labels, and grouping six tweets in one prompt lowered mean offensive-language confidence by 660 basis points. We call the variation caused by task design and model choice instrument uncertainty. Researchers can measure it only by comparing reasonable task designs. Repeating one setup or relying on confidence scores cannot replace that test.

### 中文一句话结论  
LLM 在相同设置下重复标注高度可靠（组内一致性高），但只要改变任务设计或模型，标签和估计的流行率就会大幅变化，这种“工具不确定性”无法靠置信度分数检测出来。

### English TL;DR  
LLM annotations are highly reliable under an identical setup (median Fleiss’ κ = 0.91 across repeated runs), but labels are sensitive to reasonable changes in task design or model choice (median Cohen’s κ = 0.76 across designs). Task design and model choice inflate prevalence variance by factors of 76.7 (offensive language) and 110.6 (hate speech) relative to sampling variance alone. LLM task-design variation (560–572 basis points) exceeds human instrument variation (270–331 basis points). Confidence scores do not identify unstable labels.

### 中文详细总结  
本文研究 LLM 在标注推文时的“工具不确定性”（instrument uncertainty），即标签不仅取决于被测量内容，还取决于研究人员选择的任务设计、提示格式和模型。作者用 7 个 LLM、12 种任务设计、每个条件下 3 次独立运行，标注 3,000 条推文的 offensive language（OL）和 hate speech（HS）。相同模型和设计下重复运行的中位 Fleiss’ κ=0.91，说明重复性很好；但相同推文跨任务设计比较时，中位 Cohen’s κ=0.76，说明设计变化会明显改变标签。任务设计和模型选择带来的流行率方差是单纯抽样方差的 76.7 倍（OL）和 110.6 倍（HS）。LLM 跨任务设计的变化幅度为 560–572 个基点，高于人类五版问卷的 270–331 个基点。模型置信度不能识别易变标签：置信度与模型自身重复输出更相关，与人类标签一致性较弱，并且将六条推文放在同一个提示中会使平均 OL 置信度下降 660 个基点。因此，仅重复同一设置或依赖置信度无法代替跨设计敏感性检验。

### 方法 / 贡献  
- 使用 3×2×2 全因子设计，共 12 种任务设计：任务结构（OL/HS 联合询问且顺序不同，或分开独立调用）、呈现格式（单条推文 vs 固定六条批量）、置信度提示（仅标签 vs 标签加置信度）。
- 7 个模型覆盖 3 个模型家族：GPT-4o-mini、GPT-5.4、Llama 3.1 8B/70B、Llama 4、Mistral Large 3、Mistral Medium 3.5。
- 对每个模型-设计-运行计算流行率估计，共 252 个估计值（7 模型 × 12 设计 × 3 次运行），并拟合交叉随机效应模型，分解运行、模型、任务设计、模型×设计交互的方差。
- 将方差分解结果与二项抽样方差比较，用设计效应（deff）量化 LLM 注释带来的额外不确定性。
- 重新分析同一 3,000 条推文的 44,900 条人类评分（5 个人类工具版本），将人类与 LLM 的工具敏感性放在同一流行率尺度上比较。
- 主要贡献：区分“可靠性”（相同设置下的重复性）与“敏感性”（跨合理设计的变化）；量化任务设计与模型选择对流行率方差的贡献；提供人类基准比较；检验置信度能否识别跨设计不稳定标签。

### 实验或数据  
- 数据：3,000 条推文，标注目标为 offensive language 和 hate speech。
- 实验规模：7 个 LLM × 12 种任务设计 × 3 次独立运行，共 756,000 次响应，其中 1 个不可用，实际 755,999 个 LLM 标签。
- 人类参考数据：44,900 条人类评分，来自同一批推文的 5 个人类工具版本。
- 相同模型-设计重复运行的中位 Fleiss’ κ=0.91；跨任务设计的中位 Cohen’s κ=0.76。
- 任务设计和模型选择使流行率方差增加：OL 为 76.7 倍，HS 为 110.6 倍。
- LLM 跨任务设计标准差为 560–572 基点；人类工具版本为 270–331 基点。
- 批量提示（六条一组）使平均 OL 置信度降低 660 基点。

### 值得关注点  
- 高重复可靠性不等于跨设计稳定性：单一设置的评估可能产生“诊断陷阱”。
- 任务设计和模型选择属于测量工具的一部分，而不是可忽略的实现细节。
- LLM 对工具变化的敏感性在数值上明显高于人类问卷版本变化。
- 置信度分数不能替代跨设计敏感性检验；置信度主要反映模型自身的可重复性，而非与人类判断的一致性。
- 提供了完整数据和脚本的公开仓库，便于复现和进一步探索。

### 局限性  
- 研究只覆盖 offensive language 和 hate speech 两类标注任务，以及 3,000 条推文，不能直接推广到其他任务或领域。
- 只测试了 7 个 LLM 和 12 种任务设计，模型和设计的选择本身是有限的样本。
- 作者明确说明该研究不检验 OL 和 HS 构念的效度（validity），人类标签仅作为绩效参考，不视为 ground truth。
- 方差分解中把模型视为“已部署标注者总体”的样本，这是一种建模假设。
- 置信度分析依赖模型输出的置信度分数，而不同模型和提示条件下的置信度含义可能不一致。

## 10. LongHarness Bench: Stress-Testing Language Model Harnesses for Long-Context Reasoning

- Source: arxiv
- arXiv ID: 2609.38137
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.38137v1
- PDF: https://arxiv.org/pdf/2609.38137v1
- DOI: https://doi.org/10.48550/arXiv.2609.38137

### Authors

Quang Hieu Pham, Thuy Duong Nguyen, Jocelyn Qiaochu Chen, Xi Ye

### Abstract

Language-model (LM) harnesses enable LMs to operate effectively over long contexts using additional compute. However, existing long-context evaluations are insufficient for distinguishing modern harnesses, reflected by saturated accuracy across harnesses and largely similar evaluation costs. In this paper, we introduce a benchmark for evaluating both the effectiveness and efficiency of long-context harnesses. Our tasks require diverse retrieval strategies, including lexical search and semantic matching, together with strategic and adaptive reasoning over global and local context. Much of the context is semantically relevant but only a small subset is useful at each step, creating both a challenging search problem and different accuracy--cost tradeoffs across processing strategies. For example, one task requires identifying every person satisfying several conditions using evidence scattered across documents; strategically checking the most selective condition first can narrow the search before verifying the remaining conditions. We evaluate multiple families of frontier language models with four state-of-the-art harnesses. Our benchmarks remain challenging even for strong model--harness combinations: the best reaches 68\% macro-average accuracy across four evaluation suites. More importantly, we find that the same underlying model can exhibit markedly different efficiency under different harnesses. Our results establish efficiency as an important axis for long-context evaluation and provide a testbed for developing harnesses that process context strategically rather than exhaustively.

### 中文一句话结论  
LongHarness Bench 是一个用于压力测试长上下文语言模型 harness 的新基准，强调自适应检索与多步推理，并揭示 harness 选择会显著影响准确率和计算成本；最佳配置在四个评测套件上宏观平均准确率为 68%。

### English TL;DR  
LongHarness Bench evaluates long-context language-model harnesses on four tasks requiring adaptive retrieval and multi-step reasoning. Across five frontier models and four harnesses, the best setup reaches 68% macro-average accuracy; harness choice strongly affects both accuracy and compute cost, e.g., RLM matches mini-swe-agent on Outlier Memo Detection but costs 12.4× more per instance.

### 中文详细总结  
论文提出 LongHarness Bench，用于评估长上下文 LM harness 的有效性和效率。现有长上下文基准在准确率和成本上难以区分现代 harness。新基准包含四个任务：约束求解搜索、等价程序对搜索、程序执行追踪、异常备忘录检测。这些任务要求词法搜索、语义匹配，以及对全局和局部上下文的策略性、自适应推理；上下文中大量内容语义相关，但只有小子集在每一步有用。  
评测覆盖五种前沿模型和四种 harness。最佳配置达到 68% 宏观平均准确率。同一基础模型在不同 harness 下的效率差异明显，说明效率应成为长上下文评测的重要维度。

### 方法 / 贡献  
- 提出 LongHarness Bench 基准，包含四个长上下文任务，设计目标包括：多样化自适应检索、语义混淆证据、多步推理、中间结果改变后续检索、多种策略具有不同计算成本。  
- 任务示例：Constraint Solving Search 需要先定位候选，再选择最具区分性的条件缩小范围；Equivalent Program Pair Search 需要从程序对中识别等价关系；Program Execution Tracing 需要根据先前输出推导后续检索；Outlier Memo Detection 需要结合多个备忘录发现矛盾。  
- 评估框架：直接推理 + 四种 agentic harnesses（OpenCode、mini-swe-agent、RLM、ReAct），五种模型，并与 OOLONG-Synth 和 LongBench-v2 对比。  
- 贡献：确立效率作为长上下文评测的重要轴；提供开发“策略性处理上下文而非穷尽处理”的 harness 测试床；揭示 harness 在准确率和成本上的显著差异。

### 实验或数据  
- 模型：GPT-5.6-sol、Gemini 3.8 Flash、GLM-5.3、Qwen3.8-27B、Kimi-K2.6。  
- Harnesses：OpenCode、mini-swe-agent、RLM、ReAct。  
- 最佳配置在四个评测套件上宏观平均准确率为 68%。  
- 在 Outlier Memo Detection 上，RLM 与 mini-swe-agent 准确率相近，但每实例成本高 12.4 倍。  
- 对 GPT-5.6-sol，每个 harness 在部分任务上有帮助、部分任务上有害；额外推理可能大幅增加成本却不提高准确率。  
- 与 LongBench-v2 和 OOLONG-Synth 相比，LongHarness 上 harness 之间的准确率差异更大。  
- 失败模式包括：无法复用证据、候选验证不充分、无法在预算内得出结论。

### 值得关注点  
- 现有长上下文基准趋于饱和，LongHarness 在准确率和成本两个维度上都能区分模型–harness 组合。  
- 任务设计强调“语义相关但只有小部分有用”的搜索难题，支持不同 accuracy–cost 策略。  
- 同一模型在不同 harness 下效率差异显著，例如 RLM 与 mini-swe-agent 的 12.4 倍成本差异。  
- 为开发更可靠、更高效的长上下文推理 harness 提供了公开测试床。

### 局限性  
- 最佳准确率仅 68%，说明当前最强模型–harness 组合仍有较大提升空间。  
- 等价程序对任务中，答案键以“通过原问题测试”作为匹配依据，并不能证明程序在所有输入上等价。  
- Harness 存在不能重复使用证据、候选验证不充分、在预算内无法得出结论等失败。  
- 额外计算并不一定带来准确率提升，成本可能急剧增加而收益有限。

## Processing Notes

- Duplicate papers skipped: 0