# Daily arXiv - 2026-07-07

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-07T23:40:29
- Paper count: 10

## 1. The Classics at SemEval-2026 Task 3: Combining Transformer Models and LLM-Generated Annotations for Dimensional Aspect-Based Sentiment Analysis

- Source: arxiv
- arXiv ID: 2607.03414
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2607.03414v1
- PDF: https://arxiv.org/pdf/2607.03414v1
- DOI: https://doi.org/10.48550/arXiv.2607.03414

### Authors

Rafif Alshawi, Amit Raj, Aleksey Kudelya, Alexander Shirnin

### Abstract

This paper presents an approach to the SemEval-2026 Task 3: Dimensional Aspect-Based Sentiment Analysis. We investigate methods for moving beyond traditional categorical sentiment (e.g., positive or negative) to predict fine-grained, real-valued scores for sentiment "valence" (positivity) and "arousal" (intensity). We participate in two subtasks: predicting these scores for given aspects (Subtask 1) and extracting full sets of sentiment details, including aspects, categories, and opinions alongside their scores (Subtask 3). Our approach for the regression task involves a weighted ensemble of transformer-based encoder models. For the Russian language, we further enhance the input by using a large language model (LLM) to generate synthetic sentiment descriptions. For the extraction task, we fine-tune a decoder LLM to perform structured prediction, allowing the system to identify sentiment elements and estimate their numerical scores simultaneously.

### 中文一句话结论
本文提出结合Transformer编码器集成与LLM生成注释的方法，在SemEval-2026任务3的维度情感分析中，通过回归与生成式抽取分别完成连续情感得分预测和情感四元组提取，并在俄语任务中通过LLM生成情感描述增强数据。

### English TL;DR
This paper presents a method for dimensional aspect-based sentiment analysis at SemEval-2026 Task 3, combining a weighted ensemble of transformer encoder models for regression tasks and a fine-tuned decoder LLM for structured extraction, with LLM-generated synthetic sentiment descriptions used to enhance Russian-language inputs.

### 中文详细总结
论文针对SemEval-2026任务3（维度情感分析），旨在超越传统分类，预测情感效价（valence）和唤醒度（arousal）的连续实数值。参与两个子任务：子任务1（给定情感预测得分）和子任务3（完整情感四元组提取，包括方面、类别、观点词及得分）。对于子任务1，采用加权集成Transformer编码器模型（RoBERTa-Large、RoBERTa-Base、DeBERTaV3-Large），对俄语输入使用LLM（Llama-3.2-3B-Instruct）零样本生成合成情感描述，作为上下文增强。对于子任务3，微调解码器LLM（Llama-3.1-8B-bnb-4bit，LoRA）进行结构化生成，同时抽取情感元素并预测数值。实验在英语和俄语的多领域数据集（餐厅、笔记本）上进行，与基线模型（Kimi-K2 Thinking、Qwen-3 14B）对比，展示了方法的有效性。

### 方法 / 贡献
- **子任务1（回归）**：多目标回归，在Transformer编码器（RoBERTa、DeBERTaV3）的[CLS] token上叠加线性回归头，输出二维连续得分。采用加权集成，权重基于开发集RMSE优化（RoBERTa权重0.35，DeBERTaV3权重0.30）。针对俄语，使用LLM零样本生成情感描述文本，与原始输入拼接后送入编码器，提供显式上下文。
- **子任务3（抽取）**：统一生成式框架，微调解码器LLM（Llama-3.1-8B，LoRA）直接输出结构化的四元组（方面、类别、观点、效价-唤醒度），避免多步流水线误差传播。训练500步，学习率1e-4，批次大小8。
- 主要贡献：展示了集成编码器在连续回归任务中的有效性；证明LLM生成的描述文本可增强小模型对情感数值范围的理解；提出生成式LLM在四元组抽取任务上优于传统多步流水线。

### 实验或数据
- 数据集：SemEval-2026 Task 3的多语言多领域数据集（餐厅、笔记本），使用英语和俄语track。训练集和开发集由任务提供，具体规模未在摘要中报告。
- 子任务1实验：英语track使用RoBERTa-Large、RoBERTa-Base、DeBERTaV3-Large集成；俄语track使用XLM-RoBERTa-Base/Large，并应用LLM数据增强。训练5 epoch，Adam优化器。测试RMSE：英语餐厅1.23，英语笔记本1.33，俄语餐厅1.64（均优于基线）。
- 子任务3实验：微调Llama-3.1-8B（LoRA），并对比DeepSeek-R1-Distill-Llama-8B。设计了消融实验：使用RoBERTa-Base回归模型替换解码器的数值输出（混合流水线）。超参数搜索在后竞赛阶段进行，验证学习率、提示和架构的影响。
- 评估指标：子任务1使用RMSE（效价和唤醒度联合）；子任务3使用连续F1（cF1），结合分类匹配和数值距离。

### 值得关注点
- 生成式LLM在四元组抽取任务上表现出色，尽管编码器通常被认为在回归上更稳定，但LLM同时完成抽取和数值预测的效果令人意外。
- LLM生成的描述文本显著帮助俄语track的小型编码器模型理解情感数值范围，但对英语track提升不明显。
- 加权集成策略（基于开发集权重）有效提升了回归鲁棒性，避免了过拟合开发集。
- 参数高效微调（LoRA）在资源受限下实现了有效的生成式情感抽取。

### 局限性
- 数据增强对英语track无效，可能与英语训练数据充足或LLM生成质量有关。
- 计算资源限制导致无法进行全参数微调，且超参数搜索仅在竞赛后完成，可能影响最优性能。
- 子任务1的俄语增强仅使用零样本LLM，未探索其他增强方法或后续微调。
- 论文未讨论模型在低资源语言或未见过领域上的泛化能力。
- 未提供详细的训练/评估数据集规模及统计信息，可能影响可复现性。

## 2. Fidelity-Diversity Metrics for Text

- Source: arxiv
- arXiv ID: 2607.04563
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2607.04563v1
- PDF: https://arxiv.org/pdf/2607.04563v1
- DOI: https://doi.org/10.48550/arXiv.2607.04563

### Authors

Amanda Wang, Tudor Manole, Florentina Bunea, John Thickstun

### Abstract

As language modeling technology matures, there is an increasing research focus on the composition and curation of datasets used to train these models. For instance, practitioners commonly seek to augment high-quality datasets with additional text to enhance the performance of models trained on that data. However, informed decisions about data augmentation require more nuanced assessments about data quality. We build on work measuring the precision and recall of generative models to develop a pair of metrics that quantify (1) fidelity, capturing how closely candidate text resembles reference data, and (2) diversity, capturing how well it covers the modes of the reference dataset. Our metrics are based on optimal transport divergence functionals between discrete text summaries. In experiments on M2D2 text datasets, we show that these metrics are able to disentangle a lack of fidelity from a lack of diversity in deficient candidate text. In further experiments, our metrics detect diversity deficits in synthetic GSM8K-style math datasets, which correlate with degradations in downstream accuracy of language models finetuned on this synthetic data.

### 中文一句话结论
本文提出了基于最优传输的保真度与多样性度量，用于评估文本数据集的质量，并证明这些度量能区分数据缺陷并预测下游模型性能。

### English TL;DR
This paper introduces fidelity and diversity metrics for text datasets based on optimal transport divergence. The metrics disentangle lack of fidelity from lack of diversity and predict downstream language model accuracy on synthetic data.

### 中文详细总结
随着语言模型技术的发展，数据集的质量评估日益重要。本文在生成模型精度与召回率评估的基础上，提出两个度量指标：(1) **保真度（fidelity）**：衡量候选文本与参考数据的接近程度；(2) **多样性（diversity）**：衡量候选文本对参考数据分布模式的覆盖程度。这两个指标基于离散文本摘要之间的最优传输散度（optimal transport divergence）。在M2D2文本数据集上的实验表明，该指标能够区分候选文本中存在的保真度缺失与多样性缺失。进一步在合成的GSM8K数学数据集上的实验显示，多样性指标的下降与微调后语言模型在下游任务上的准确率下降相关。

### 方法 / 贡献
- **方法**：将每个数据集通过嵌入转化为离散测度（使用量化或混合模型），然后基于最优传输成本分解保真度与多样性。保真度通过贪婪最近邻分配成本定义，多样性定义为该分配与全局最优传输成本之间的差距。
- **贡献**：
  1. 提出基于Wasserstein距离分解的保真度－多样性度量框架。
  2. 设计基于真实主题标签的控制实验，验证指标的有效性。
  3. 提出控制合成文本数据集多样性的实验协议。
  4. 证明多样性指标与下游模型性能直接相关。

### 实验或数据
- **数据**：使用了M2D2文本数据集（带有主题标注）和合成的GSM8K数学数据集变体。
- **实验**：
  - 在M2D2上控制评估数据集的主题覆盖范围，验证指标对保真度和多样性变化的敏感性。
  - 在GSM8K上生成不同多样性的合成变体，测量多样性指标，并微调语言模型，观察下游准确率的变化。

### 值得关注点
- 指标基于最优传输，能将Wasserstein距离分解为保真度和多样性两个正交分量。
- 使用离散文本摘要（如主题混合）实现可解释的量化。
- 在合成数据上，多样性指标能够预测微调后模型的准确率下降，具有实用价值。

### 局限性
所提供的摘要和引言中未明确讨论局限性。需注意指标依赖嵌入质量和量化方式，且需要参考数据集；实际应用中可能需要进一步验证对不同领域和模型的鲁棒性。

## 3. MORE: A Multilingual Document Parsing Benchmark and Evaluation

- Source: arxiv
- arXiv ID: 2607.02956
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2607.02956v1
- PDF: https://arxiv.org/pdf/2607.02956v1
- DOI: https://doi.org/10.48550/arXiv.2607.02956

### Authors

Long Xu, Binghong Wu, Tinghao Yu, Hao Feng, Zhenyu Huang, Haoqing Jiang, Yunhao Wang, Shuo Huang, Feng Zhang

### Abstract

Multilingual documents encapsulate rich regional cultures, scientific discoveries, and historical records. Parsing this content into structured, machine-readable formats is critical for unlocking global knowledge. However, existing benchmarks predominantly focus on high-resource languages like English and Chinese, creating an evaluation blind spot concerning model performance on other languages. While recent Vision-Language Models (VLMs) claim support for hundreds of languages, the lack of ground truth makes it impossible to empirically verify these capabilities. To bridge this gap, we introduce MORE, a large-scale benchmark designed for multilingual document parsing evaluation. MORE distinguishes itself through three key dimensions: (1) Unprecedented Scale: It covers 149 languages, making it the most linguistically diverse benchmark to date; (2) Structural Complexity: Unlike previous works, it extends evaluation beyond plain text to include structural elements such as code blocks, tables, and catalogs; and (3) Data Authenticity: All samples are curated from real-world documents via a model-assisted, human-refined annotation pipeline. We evaluate state-of-the-art models using MORE, establishing new performance baselines for long-tail languages and validating the benchmark's effectiveness in diagnosing model capabilities in realistic, diverse scenarios. The MORE dataset will be available at https://github.com/zimoqingfeng/MORE.

### 中文一句话结论
MORE 是一个覆盖 149 种语言的多文档解析评估基准，通过大规模、结构复杂性和数据真实性，填补了低资源语言模型性能评估的空白。

### English TL;DR
MORE is a large-scale benchmark covering 149 languages with structural complexity and real-world authenticity, designed to evaluate multilingual document parsing and address the evaluation blind spot for low-resource languages.

### 中文详细总结
现有文档解析基准主要聚焦英语和中文等资源丰富的语言，导致对低资源语言的模型性能缺乏评估。尽管近期视觉语言模型声称支持数百种语言，但缺少真实标注进行验证。为此，作者提出 MORE 基准，覆盖 149 种语言，包含文本、表格、代码块、目录等结构化元素，所有样本来自真实文档并通过模型辅助、人工精炼的标注流程构建。MORE 是当前语言覆盖面最广的文档解析基准，并在评估中建立了低资源语言的性能基线，验证了其在多样化真实场景中诊断模型能力的有效性。

### 方法 / 贡献
- 提出覆盖 149 种语言的多文档解析评估基准，为目前语言多样性最强。
- 扩展评估维度至结构化元素（代码块、目录等），超越传统文本和表格。
- 采用模型辅助、人工精炼的标注流水线，保证数据真实性。
- 对现有先进模型进行全面评估，建立低资源语言性能基线。

### 实验或数据
MORE 数据集包含 1288 张真实文档页面，覆盖 149 种语言（分属拉丁、西里尔、梵文、阿拉伯、中文等语系），标注包括文本（8221 条）、公式（82 条）、表格（94 条）、代码块（73 条）、目录（104 条）和阅读顺序（1072 条）。评估了多个主流 VLM 模型，结果显示了不同语言和结构上的能力差异。

### 值得关注点
- 语言覆盖范围最广（149 种），包含大量低资源语言。
- 首次纳入代码块和目录等结构化评估，更贴近真实文档复杂性。
- 所有数据来自真实网页 PDF，非合成样本。
- 开源数据集，促进可重复研究。

### 局限性
论文未明确讨论局限性。可推测：样本数量相对有限（1288 页），每语言约 10 页可能导致统计稳定性不足；标注仅覆盖单页文档，未评估多页文档的连贯解析；部分结构化元素（如公式、表格）在低资源语言中样本稀疏，可能影响评估全面性。

## 4. Telescope: Improving Zero Shot Detection of LLM Generated Content By Measuring Token Repetition Probability

- Source: arxiv
- arXiv ID: 2607.04061
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.04061v1
- PDF: https://arxiv.org/pdf/2607.04061v1
- DOI: https://doi.org/10.48550/arXiv.2607.04061

### Authors

Christopher Nassif, Josh F. Cooper

### Abstract

Distinguishing Large Language Model (LLM) generated text from human writing is a critical and difficult challenge. While LLMs are trained to write like humans, we hypothesize that this training leaves an indelible mark. LLMs develop a particularly strong aversion to token repetition very early in training. This bias persists as a ''Vestigial Heuristic'' (a developmental artifact) that is activated in LLM-generated text, separating LLM from human writing. To probe this phenomenon, we introduce Telescope Perplexity, a metric that evaluates the token repetition of the model, $P(s_i | s_{1:i})$ . Our empirical investigation reveals that the Telescope Perplexity signature emerges early in pre-training, and Telescope Perplexity empirically enables highly effective zero-shot LLM detection. We show state-of-the-art or competitive performance across diverse datasets (including modern evaluation sets we introduce), reference models, and perturbation schemes with greater efficiency than other methods.

### 中文一句话结论
本文提出了一种基于“残留启发式”（Vestigial Heuristic）假设的零样本检测方法——Telescope Perplexity，通过测量LLM在生成文本时对token重复的强烈厌恶，实现了高效且可媲美或超越现有最优方法的检测性能。

### English TL;DR
Telescope Perplexity is a zero-shot detector that leverages an LLM’s early-learned aversion to token repetition (a “Vestigial Heuristic”) to achieve state-of-the-art or competitive performance in distinguishing LLM-generated text from human writing, with higher efficiency than many existing methods.

### 中文详细总结
区分LLM生成文本与人类写作至关重要且困难。本文提出“残留启发式假设”：LLM在预训练早期就形成了对token重复的强烈厌恶，这种偏见作为发育遗留物持续存在，并在LLM生成文本中激活。为探测该现象，作者引入Telescope Perplexity指标，评估模型对当前token的复制概率。实验表明，该指标在预训练早期即出现并稳定，能有效实现零样本检测。在多个数据集（包括新引入的现代评估集）、参考模型和扰动方案上，Telescope Perplexity达到了最优或具有竞争力的性能，且效率更高。

### 方法 / 贡献
- 提出“残留启发式”假设，解释LLM对token重复的早期学习偏见。
- 定义Telescope Perplexity：对模型输出当前token概率的负对数平均，相比标准困惑度更直接探测重复厌恶。
- 通过训练动态分析（Amber-7B、Pythia不同阶段检查点）证明该指标早现且稳定。
- 通过有限上下文实验（仅1-2个token）证明其局部性，验证了假设。
- 在多个数据集和参考模型上展示零样本检测的SOTA或竞争性表现。

### 实验或数据
- 使用HC3数据集进行主要性能评估（AUC达0.995）。
- 训练动态分析：Pythia-2.8B检查点、Amber-7B检查点，显示Telescope Perplexity早期快速上升后稳定。
- 上下文限制实验：仅用bigram或trigram上下文，Telescope Perplexity AUC仍保持0.897/0.921，优于标准困惑度。
- 引入新评估集：使用GPT4o Mini、Deepseek-V3等现代LLM生成的文本。
- 参考模型多样性：SmolLM 360M、Falcon 7B等。
- 未与扰动方法（如DetectGPT、DetectLLM-NPR）直接比较，因计算成本过高。

### 值得关注点
- 方法极简，只需单次前向传播，效率高。
- 假设基于LLM早期训练动态，可解释性强。
- 在多种参考模型和数据集上表现鲁棒，且对上下文长度不敏感。
- 代码开源，可复现。

### 局限性
- 论文未明确讨论局限性，但可推断：依赖参考模型的选择，不同参考模型可能影响检测性能。
- 未与扰动方法直接比较（因计算成本），但声称效率更高。
- 主要针对零样本检测，未涵盖监督方法的场景。
- 假设基于LLM早期训练，对于使用不同训练策略的模型（如刻意避免重复惩罚）可能失效。

## 5. SalAngaBhava: A Sinhala Market Dataset for Aspect-based Sentiment Analysis

- Source: arxiv
- arXiv ID: 2607.05259
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.05259v1
- PDF: https://arxiv.org/pdf/2607.05259v1
- DOI: https://doi.org/10.48550/arXiv.2607.05259

### Authors

Lakshani Galwatta, Nisansa de Silva, Sarangi Aththanayake, Adithya Galwatta

### Abstract

Sentiment analysis has been a primary domain under Natural Language Processing (NLP) from its inception as it plays a vital role in both real-world and research applications. In high-resource languages, this has been extended a step further, and instead of predicting sentiment at the sentence level, models have been developed to detect more fine-grained sentiments at aspect level. However, in order to conduct this fine-grained Aspect-based Sentiment Analysis (ABSA), datasets annotated with aspects and sentiments toward the said aspects is required. Such datasets are lacking for low-resources languages among which, we can count Sinhala, an Indo-Aryan languages used primarily in Sri Lanka. In this work, we introduce, SalAngaBhava, a new Sinhala Aspect-based Sentiment Analysis dataset which contains Sinhala product reviews that are manually labeled with aspect terms and the associated sentiments (positive, negative, neutral). The data was collected from domain-relevant sources such as user-generated reviews and comments, and was annotated following carefully defined guidelines to ensure consistency and quality. The dataset consists of sentences and aspect-sentiment pairs, encompassing a considerable range of aspects from several domains. The analysis confirms that the dataset is well-structured and sufficiently balanced for ABSA research. This dataset can be used as a benchmark and facilitates further studies related to Sinhala natural language processing, and low-resource sentiment analysis tasks.

### 中文一句话结论
本文首次公开了手工标注的僧伽罗语（Sinhala）电商评论方面级情感分析数据集 SalAngaBhava，包含方面词、情感极性等四元组标注，填补了低资源语言在该领域的空白。

### English TL;DR
This paper introduces SalAngaBhava, the first publicly available Sinhala aspect-based sentiment analysis dataset manually annotated with aspect terms, opinion terms, aspect categories, and sentiment polarities from e-commerce product reviews.

### 中文详细总结
该工作针对僧伽罗语（斯里兰卡主要语言）在细粒度情感分析（ABSA）方面缺乏标注数据的问题，构建了 SalAngaBhava 数据集。数据来源于 Daraz 等电商平台的用户评论，经过清洗、去重和罗马化转写（Singlish → Unicode 僧伽罗语）后，由母语者依据详细指南进行手工标注，采用 (t, a, o, s) 四元组格式（目标词、方面类别、观点词、情感极性），情感标签包括正面、负面、中性。标注一致性评估显示 Cohen's Kappa 为 0.82，表明质量较高。数据集包含句子和方面-情感对，覆盖多个领域，统计分析确认结构合理、类别均衡，可作为基准用于 ABSA 子任务（如方面词提取、情感分类）及端到端建模。

### 方法 / 贡献
- **方法**：从电商网站爬取公开评论，自动分类为纯僧伽罗语、罗马化僧伽罗语、混合语码，排除纯英语；使用 Google Transliterator 将罗马化文本转写为僧伽罗 Unicode；由 3 名母语者依据四元组方案手工标注，预标注和讨论以保证一致性；计算 Cohen's Kappa 和 Jaccard 相似度评估可靠性。
- **贡献**：首个公开的僧伽罗语 ABSA 数据集，提供四元组级标注，支持多种 ABSA 子任务和联合建模；为低资源语言情感分析提供基准；数据集开源发布（GitHub & HuggingFace）。

### 实验或数据
论文未设计新的模型实验或评测，仅对数据集本身进行统计分析（如句子数、方面-情感对分布、类别平衡性等），确认其适用于 ABSA 研究。未在论文中报告具体实验或模型性能。

### 值得关注点
- 首个面向僧伽罗语的方面级情感分析数据集，填补低资源语言空白。
- 采用四元组标注（t, a, o, s），考虑僧伽罗语屈折特性，将方面词细分为目标词和方面类别，更具灵活性。
- 数据集覆盖电商领域，包含纯僧伽罗语和混合语码，接近真实场景。
- 公开可用，便于复现和后续研究。

### 局限性
- 数据仅来自电商评论（Daraz 平台），领域单一，可能难以泛化到其他类型文本（如新闻、社交媒体）。
- 隐式方面（implicit aspect）的标注存在主观性，一致性指标中方面类别 Jaccard 相似度仅为 0.63，表明识别难度较大。
- 标注过程依赖人工，规模有限（约 5,700 条评论），可能不足以覆盖所有语言现象。
- 未在论文中验证模型在下游任务上的实际表现，缺乏基准结果对比。

## 6. Punching Above Their Weight: Classification-Head Fine-Tuning of Tiny Language Models (TLMs) for Verifiable Multiple-Choice Tasks

- Source: arxiv
- arXiv ID: 2607.03801
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.03801v1
- PDF: https://arxiv.org/pdf/2607.03801v1
- DOI: https://doi.org/10.48550/arXiv.2607.03801

### Authors

Bhavesh Sood, Jaromir Savelka

### Abstract

We define Tiny Language Models (TLMs) as models below roughly 3B parameters that fit on mainstream consumer devices. We study how to adapt them for and use them on verifiable multiple-choice tasks. We compare three LoRA-based fine-tuning paradigms (label generation, gold only, and our discriminative classification head) on a unified setup across several Qwen3 models from 0.6B to 8B and five benchmarks: HellaSwag, WinoGrande, PIQA, SciQ and ARC-C. Classification-head fine-tuning reliably outperforms label generation (+2-3%) at the 0.6B and 1.7B scales. Further, TLMs fine-tuned using the discriminative method are competitive to zero-/few-shot GPT-3 (175B), PaLM (540B) and GPT-4. The performance we report for Qwen3-0.6B and Qwen3-1.7B are SOTA on HellaSwag, WinoGrande, and PIQA.

### 中文一句话结论
本研究证明，对低于3B参数的“微型语言模型”（TLM）使用判别式分类头进行LoRA微调，在多项选择题任务上显著优于传统的标签生成方法，并能在常识推理基准上达到或超越GPT-3（175B）等大模型的性能。

### English TL;DR
This paper shows that fine-tuning tiny language models (<3B parameters) with a discriminative classification head (CLS) outperforms standard label-generation fine-tuning by 2-3% on commonsense benchmarks. Using this method, small models like Qwen3-1.7B achieve performance comparable to 100x larger models (GPT-3, PaLM) on HellaSwag, WinoGrande, and PIQA, setting new state-of-the-art results.

### 中文详细总结
论文定义TLM为参数低于约3B、可部署于主流消费设备（内存≤8GB）的模型。作者在Qwen3系列（0.6B、1.7B、4B、8B）上比较了三种基于LoRA的微调范式：（1）标签生成（Label Generation SFT），（2）仅用正确选项微调（Gold Only），（3）提出的判别式分类头（Classification Head SFT）。在HellaSwag、WinoGrande、PIQA、SciQ和ARC-Challenge五个基准上，分类头微调在0.6B和1.7B尺度上稳定优于标签生成（提升2-3%）。微调后的Qwen3-1.7B在HellaSwag和PIQA上超过了GPT-3（175B）和PaLM（540B）的零样本/少样本结果，尽管模型体积小约100-320倍。论文还指出，零样本设置下TLM性能较差，且评估细节（如下一个token概率 vs. 序列对数概率）会导致结果巨大差异。在大于3B的模型上，不同微调方法差距缩小。科学知识密集型基准（SciQ、ARC-C）从此分类方法中获益较少。

### 方法 / 贡献
1. **定义TLM**：明确将低于约3B参数、可在消费设备上有效部署的模型定义为微型语言模型。
2. **提出分类头微调方法**：设计了一种判别式分类头，用于多项选择任务的LoRA微调，而非传统的下一个token预测。
3. **首次系统比较**：在五个基准上首次统一比较了三种微调范式（标签生成、仅正确选项、分类头），并报告了多个基准上的SOTA结果。
4. **揭示评估偏差**：指出TLM之前报告的性能可能因不合适的零样本推理或微调方法而被低估。

### 实验或数据
**基准**：HellaSwag、WinoGrande、PIQA、SciQ、ARC-Challenge。
**模型**：Qwen3-0.6B、Qwen3-1.7B、Qwen3-4B、Qwen3-8B。
**结果亮点**：
- Qwen3-0.6B + CLS SFT：HellaSwag 80.95%，WinoGrande 70.80%，PIQA 77.80%。
- Qwen3-1.7B + CLS SFT：HellaSwag 90.81%，WinoGrande 78.16%，PIQA 85.04%。
- 零样本基线（标签生成）在0.6B模型上仅约40.68%平均准确率，而CLS SFT达到76.77%（提升+25%）。
- 与GPT-3（175B）和PaLM（540B）的对比显示，Qwen3-1.7B在三个常识基准上超越或接近这些大模型。

### 值得关注点
- **尺度与性能的惊人对比**：1.7B模型在常识推理上超越175B模型，挑战了“越大越好”的普遍假设。
- **方法简单有效**：仅通过改变微调目标（分类头而非下一个token预测）即带来显著提升，无需增加参数或推理成本。
- **消费级部署可行性**：TLM可在8GB内存设备上运行，为隐私敏感或离线场景提供实用方案。
- **评估标准需要重新思考**：论文指出TLM的常见评估方式（如零样本、标签生成）可能系统性低估其能力。

### 局限性
1. **研究范围受限**：仅关注可验证的多项选择任务（常识推理），未涉及开放生成、对话、编程等任务。
2. **模型仅限Qwen3系列**：未在其他架构（如Llama、Gemma）上验证结论，普适性需进一步检验。
3. **对更大模型无效**：在>3B模型上，分类头与标签生成方法的性能差距不明显，结论不适用于更大模型。
4. **硬件约束定义可能过时**：TLM定义基于当前消费级硬件（8GB），随着硬件提升，阈值可能变化。
5. **未深入分析失败案例**：论文未探讨在哪些特定类型的问题上分类头方法表现不佳。

## 7. LP-SFT: Local-Preserving Supervised Fine-Tuning via Multimodal Entropy Structure

- Source: arxiv
- arXiv ID: 2607.04733
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.04733v1
- PDF: https://arxiv.org/pdf/2607.04733v1
- DOI: https://doi.org/10.48550/arXiv.2607.04733

### Authors

Yueyang Wang, Baolong Bi, Shuo Lu, Jingyuan Zhang

### Abstract

Supervised fine-tuning (SFT) is the standard approach for adapting pretrained language models to downstream domains, yet it often improves target-domain behavior at the cost of degrading pre-existing capabilities. Standard cross-entropy fine-tuning promotes only the observed label token and leaves unconstrained how probability mass is redistributed over other plausible alternatives, potentially distorting the rich local preference structure learned during pretraining. We first analyze next-token predictions using Shannon and Renyi entropies, revealing that pretrained models exhibit a regular multimodal entropy structure. These entropy peaks correspond to varying numbers of plausible alternatives, indicating that the base model intrinsically encodes rich distributional knowledge beyond the single supervised token. Motivated by this observation, we propose LP-SFT, a Local-Preserving Supervised Fine-Tuning objective designed to explicitly protect this inherent entropy structure. At each step, LP-SFT constructs an adaptive support of alternative tokens and applies a locally normalized preservation loss to maintain the base model's relative structure among them, while standard cross-entropy independently optimizes the supervised token. Across mixed-domain and single-domain fine-tuning experiments, LP-SFT improves overall performance over vanilla SFT and recent SFT-enhancement baselines, achieving the best balance between pass@1 accuracy and pass@k performance. These results suggest that local preservation helps mitigate capability degradation without collapsing sampling-accessible diversity.

### 中文一句话结论
LP-SFT 通过自适应保留预训练模型的多模态熵结构，在微调中保持非标签候选令牌的局部相对顺序，从而在提升单次准确率的同时不破坏生成多样性。

### English TL;DR
LP-SFT preserves the multimodal entropy structure of pretrained models during supervised fine-tuning by constructing an adaptive support of alternative tokens and applying a locally normalized preservation loss. It improves pass@1 accuracy over vanilla SFT and recent baselines while maintaining pass@k diversity.

### 中文详细总结
标准有监督微调（SFT）使用交叉熵损失仅优化标签令牌，导致预训练分布中丰富的替代令牌结构被扭曲。作者首先使用 Shannon 和 Rényi 熵分析预训练模型的 next-token 分布，发现熵呈现规则的多模态结构：熵峰对应不同整数 k（如 ln1, ln2, ln3, …），表明存在数量不等的合理候选令牌。基于此观察，提出 LP-SFT，每步从基模型分布中构建自适应候选令牌集（排除监督令牌），并施加局部归一化 KL 散度损失以保持这些替代令牌的相对概率结构，同时用标准交叉熵优化监督令牌。在混合域和单域微调实验中，LP-SFT 在 pass@1 和 pass@k 指标上均优于 vanilla SFT 及近期 SFT 增强基线，实现了下游适应性与原有能力保留的最佳平衡。

### 方法 / 贡献
- 首次揭示预训练语言模型 next-token 分布具有规则的多模态熵结构（熵峰对应不同整数 k），表明模型内嵌丰富的分布知识。
- 提出 LP-SFT 框架：使用冻结基模型作为局部结构参考，自适应确定每步需保留的候选令牌数，移除监督令牌后以局部归一化 KL 散度保持相对偏好，同时用交叉熵学习监督令牌。
- 实验证明 LP-SFT 能有效缓解灾难性遗忘和多样性下降，在多种模型和数据集上取得更好权衡。

### 实验或数据
实验覆盖混合域与单域微调任务，使用 UltraFeedback（通用指令跟随）、Magicoder-OSS-Instruct-75K（代码生成）、NuminaMath-CoT（数学推理）三个数据集。评估模型包括 Qwen3-4B、Llama3.1-8B、Qwen3-30B-A3B 等不同规模和架构。通过 pass@1 和 pass@k 指标衡量性能，LP-SFT 在保留采样多样性（pass@k）的同时提升了单次准确率（pass@1）。具体数值和消融实验细节需参考全文。

### 值得关注点
- 熵结构分析新颖：有效支持比 R 可系统识别高阶熵压状态（如 N₁ ≈ 4,5,10 等），且该结构在不同模型和任务上普遍存在。
- 方法设计巧妙：局部归一化 KL 散度仅约束非标签候选令牌的相对分布，避免全词汇约束带来的过度正则化，计算开销低于全词汇 KL。
- 在多种基线（DFT、EAFT、GEM、ASFT）上取得一致改进，表明局部保留策略是 SFT 提升的有效方向。

### 局限性
论文未明确讨论局限性，但可推断：1）需要冻结的基模型作为参考，额外占用显存和计算资源；2）自适应支持集大小依赖于熵峰值检测，可能对超参数（如截断 K）敏感；3）尚未在极大模型（>30B）或极端分布偏移场景下验证；4）局部保留仅针对非标签候选，未考虑标签令牌与候选令牌间的相互影响。

## 8. Aligning Language Models with Selective Prediction

- Source: arxiv
- arXiv ID: 2607.03528
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.03528v1
- PDF: https://arxiv.org/pdf/2607.03528v1
- DOI: https://doi.org/10.48550/arXiv.2607.03528

### Authors

Gaoxiang Luo, Yifan Wu, Sinian Zhang, Aryan Deshwal, Ju Sun

### Abstract

Large language models (LLMs) are increasingly deployed as critical decision-making components in high-stakes real-world AI systems, rendering LLM reliability a foremost practical concern. In this paper, we focus on enhancing LLM reliability through selective prediction (SP), a strategy that allows an LLM to only predict for inputs where it is likely to be correct (i.e., coverage) and hence reduce the error rate (i.e., risk) on that portion of inputs -- flagging the remaining inputs for future human discretion. In other words, SP improves LLM reliability by balancing the risk-coverage trade-off and enabling seamless human-AI collaboration. To integrate SP into LLMs, we focus on the LLM post-training alignment stage and propose to align LLMs with SP performance metrics, in contrast with existing LLM alignment methods that focus primarily on correctness or calibration metrics. Specifically, we propose a novel alignment framework, Reinforcement Learning for Selection Reward (RLSR), which targets the area under the risk-coverage curve (AURC) -- a popular SP performance metric -- as its alignment objective. RLSR achieves substantially better risk-coverage trade-off compared to multiple alignment baselines on both in-domain and out-of-domain tasks.

### 中文一句话结论
本文提出强化学习选择性奖励（RLSR）框架，通过直接优化风险覆盖率曲线下面积（AURC）来对齐大语言模型的**选择性预测**能力，显著优于现有基于正确性或校准指标的基准方法。

### English TL;DR
This paper proposes RLSR, an alignment framework that directly optimizes large language models for selective prediction by using the area under the risk-coverage curve (AURC) as a reward, achieving substantially better risk-coverage trade-offs than existing methods.

### 中文详细总结
大语言模型在高风险场景下的可靠性至关重要。本文提出通过**选择性预测**来提高LLM可靠性：只回答模型有把握的问题（覆盖率），对没把握的问题则留给人类处理。为实现这一目标，作者提出了**RLSR**对齐框架，该框架直接优化选择性预测指标——风险覆盖率曲线下面积（AURC），而非传统的正确率或校准指标。RLSR基于GRPO框架，创新性地引入升维AURC目标函数和批量训练策略，解决了AURC作为奖励函数的两个挑战：（1）原始AURC只惩罚错误但不奖励正确；（2）AURC是全局排序依赖的群体级指标，不适用于小批量随机梯度方法。实验表明，RLSR在域内和域外任务上均显著优于基于正确性的RLVR和基于校准的RLCR等基线方法。

### 方法 / 贡献
1. **首次提出**将大语言模型直接与选择性预测对齐以增强其可靠性
2. 引入**RLSR新框架**，基于GRPO并开发升维AURC目标函数和批量训练策略
3. **实证证明**RLSR在多项域内和域外任务上超越RLVR和RLCR等强基线

### 实验或数据
摘要未明确说明具体使用的数据集，但提到在**域内和域外**任务上进行了评估，并与多个对齐基线进行了比较。

### 值得关注点
1. 直接优化选择性预测**而非先校准再预测**，避免校准与选择性预测目标的错配
2. RLSR同时优化**正确率**和**置信度排名**，而不仅是单个阈值下的表现
3. 在域外任务上也表现出色，体现方法的泛化能力

### 局限性
摘要未提及局限性，但潜在局限包括：
- AURC作为全局指标的计算复杂度可能较高
- 需要额外的置信度输出机制（如口头化置信度）
- 未讨论不同模型规模或任务类型的适用性边界
- 未涉及选择性预测在实际部署中的延迟或计算成本问题

## 9. Beyond Multilingual Averages: MTEB-PT, a Benchmark for Portuguese Sentence Encoders

- Source: arxiv
- arXiv ID: 2607.04071
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.04071v1
- PDF: https://arxiv.org/pdf/2607.04071v1
- DOI: https://doi.org/10.48550/arXiv.2607.04071

### Authors

Lucas Hideki Takeuchi Okamura, Alexandre Alcoforado, Anna Helena Reali Costa

### Abstract

Portuguese remains underrepresented in text embedding evaluation, despite being one of the most widely spoken languages in the world. As a result, embedding models are often selected based on English or multilingual metrics, while their effectiveness in Portuguese remains unclear. We present MTEB-PT, a Portuguese benchmark constructed from a subset of MMTEB, comprising 14 existing datasets across Semantic Textual Similarity (STS), classification, retrieval, and reranking. We use this benchmark to evaluate 17 open- and closed-source embedding models under a unified protocol. Our results show that Portuguese performance is strongly task-dependent: multilingual rankings do not reliably predict Portuguese-specific performance across task families, no single model dominates all settings, and models with stronger long-context capacity are particularly advantageous on longer-input tasks such as retrieval and reranking. The benchmark also shows that language-specific fine-tuning still improves model performance in Portuguese, especially on task types that match the adaptation data most closely. To examine this effect, we fine-tune three representative backbone models with Portuguese contrastive supervision and Matryoshka Representation Learning (MRL). These benchmark-informed baselines yield their strongest gains on STS, consistent with the predominantly symmetric supervision used during training, while also improving retrieval and remaining competitive under dimensional truncation. We release the MTEB-PT benchmark, the fine-tuned models, and the training and evaluation code.

### 中文一句话结论
MTEB-PT 基准测试表明，葡萄牙语句子嵌入性能具有强烈的任务依赖性，多语言平均分无法可靠预测葡萄牙语特定表现，且语言特定微调能带来显著提升，尤其在对称语义任务上。

### English TL;DR
MTEB-PT, a new Portuguese benchmark for sentence encoders covering STS, classification, retrieval, and reranking, demonstrates that multilingual averages are unreliable predictors of Portuguese-specific performance and that language-specific fine-tuning yields substantial gains, particularly on symmetric semantic tasks.

### 中文详细总结
本文提出 MTEB-PT，一个由 MMTEB 子集构建的葡萄牙语文本嵌入评估基准，包含 14 个现有数据集，覆盖语义文本相似度（STS）、分类、检索和重排序四个任务族。在统一协议下评估了 17 个开源和闭源嵌入模型。结果表明，葡萄牙语性能高度依赖任务类型：多语言排名无法可靠预测葡萄牙语特定任务族的表现，没有单一模型在所有设置中占优，且长上下文能力在处理检索和重排序等长输入任务时具有优势。语言特定微调仍能提升葡萄牙语模型性能，尤其是与微调数据最匹配的任务类型。为验证这一效果，作者使用葡萄牙语对比监督和 Matryoshka 表示学习（MRL）对三个代表性骨干模型（multilingual-e5-large、bertimbau-large、modbertbr）进行微调，这些模型在 STS 上取得最大提升，同时在检索和维度截断下保持竞争力。作者发布了 MTEB-PT 基准、微调模型及训练和评估代码。

### 方法 / 贡献
- 提出 MTEB-PT，一个葡萄牙语嵌入评估基准，包含 14 个现有数据集，覆盖 STS、分类、检索和重排序。
- 对 17 个模型进行系统评估，发现模型排名在葡萄牙语中高度任务依赖，多语言优势不能均匀迁移。
- 发布三个基于 MRL 的葡萄牙语微调模型（multilingual-e5-large、bertimbau-large、modbertbr），作为强基线。
- 分析维度效率，展示 MRL 训练模型在维度截断下保持竞争力，支持存储和延迟高效的葡萄牙语嵌入。

### 实验或数据
- 基准包含 14 个数据集：3 个 STS、5 个分类、3 个检索、3 个重排序。
- 评估了 17 个模型，包括闭源、同行评审开源、社区模型和本文微调模型。
- 微调实验：使用葡萄牙语对比监督和 MRL 对三个骨干模型进行微调，在 STS 上取得最大提升。
- 维度截断分析：评估 MRL 模型在不同维度下的表现。

### 值得关注点
- 葡萄牙语性能高度依赖任务类型，多语言平均排名不可靠。
- 长上下文能力对检索和重排序等长输入任务至关重要。
- 语言特定微调（尤其是 MRL）仍能显著提升对称语义任务（如 STS）的性能，并保持维度效率。
- 作者公开了基准、模型和代码，促进可重复性。

### 局限性
根据摘要，本文未明确讨论其局限性。

## 10. Beyond Static Rules: Automated Discovery of Latent Vulnerabilities in Text-to-SQL

- Source: arxiv
- arXiv ID: 2607.03833
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.03833v1
- PDF: https://arxiv.org/pdf/2607.03833v1
- DOI: https://doi.org/10.48550/arXiv.2607.03833

### Authors

Hanqing Wang, Yongdong Chi, Jian Yang, Lei Yang, Jiehui Zhao, Yun Chen, Guanhua Chen

### Abstract

While Large Language Models (LLMs) have achieved remarkable success in Text-to-SQL tasks, their deployment in real-world environments is hindered by latent reliability issues. Identifying these latent weaknesses is critical for building trustworthy database interfaces, yet current diagnostic approaches rely heavily on static, expert-defined rules, which lack the capability for systematic and automated exploration. To bridge this gap, we propose SAGE (Systematic Automated Guided Exploration), a novel framework designed to autonomously uncover latent failure patterns in LLM-based Text-to-SQL generation. Specifically, SAGE generates vulnerability hypotheses for given samples and references a continuously evolving Vulnerability Codex to design targeted perturbations, thereby iteratively verifying and documenting potential defects. Extensive experiments on state-of-the-art open-source LLMs demonstrate that SAGE uncovers a substantial number of failure cases, highlighting the significant fragility of current models. Furthermore, our analysis reveals that the Vulnerability Codex exhibits strong cross-model transferability, indicating that the discovered patterns represent generalized structural weaknesses. Finally, we explore SAGE's potential for remediation. Although preliminary, lightweight fine-tuning on the generated samples yields promising improvements, suggesting a scalable pathway for closing the reliability loop in future work.

### 中文一句话结论
SAGE框架通过自动生成假设扰动并迭代更新漏洞代码库，自主发现LLM在Text-to-SQL中的潜在脆弱模式，并揭示其跨模型泛化性，为可靠性闭环提供初步路径。

### English TL;DR
SAGE is a framework that autonomously discovers latent vulnerabilities in LLM-based Text-to-SQL by generating and iteratively verifying hypothesis-driven perturbations guided by a continuously evolving Vulnerability Codex, revealing generalized structural weaknesses and enabling scalable remediation.

### 中文详细总结
现有Text-to-SQL系统的可靠性评估依赖静态专家规则，无法系统探索未知漏洞。本文提出SAGE框架，利用大语言模型自动生成漏洞假设，并参考持续更新的Vulnerability Codex设计针对性扰动样本，通过迭代验证和抽象总结，将具体失败案例提炼为通用错误原型，形成自主发现循环。实验表明，SAGE能揭示大量现有模型的脆弱性，且发现的漏洞模式可跨模型迁移。初步的轻量微调实验表明，利用生成样本进行修复可提升模型可靠性，为实现可靠性闭环提供了可扩展思路。

### 方法 / 贡献
- 提出SAGE框架，包含两个核心模块：**Vulnerability Discovery Module**（生成假设→检索Codex→生成扰动→验证失败）和 **Codex Evolution & Management Module**（将失败案例抽象为通用错误原型，并通过语义压缩实现代码库的持续演化）。
- 实现从“静态规则验证”到“自主探索盲区”的范式转变，系统自动发现并归纳Text-to-SQL模型的潜在脆弱模式。
- 初步探索修复路径：利用发现样本进行轻量微调，可部分缓解模型缺陷，为可靠性闭环提供可扩展方案。

### 实验或数据
- 在多种主流开源大语言模型上进行了实验，验证SAGE能够发现大量失败案例，揭示当前模型在Text-to-SQL任务中的显著脆弱性。
- 分析表明Vulnerability Codex发现的漏洞模式具有强跨模型迁移性，提示为通用结构弱点。
- 初步实验使用SAGE生成的样本进行轻量微调，模型性能得到有希望的提升，但该修复工作尚属初步。

### 值得关注点
- **自动化主动发现**：无需人工预设规则，系统自主生成假设并迭代验证，突破静态评估局限。
- **跨模型迁移性**：发现的结构弱点可泛化至不同模型，降低重复诊断成本。
- **闭环修复潜力**：将漏洞发现与模型微调结合，为构建可信Text-to-SQL系统提供可扩展路径。

### 局限性
- 修复实验仅基于轻量微调，属于初步探索，尚未完全解决所有发现的漏洞，需未来工作进一步验证和优化。
- 方法依赖大语言模型生成假设和抽象，生成质量可能影响发现效果，且未讨论对未见或复杂场景的适用性。
- 跨模型迁移性虽已观察，但迁移范围（如不同系列或规模模型）和迁移稳定性仍需更多实验支撑。

## Processing Notes

- Duplicate papers skipped: 0