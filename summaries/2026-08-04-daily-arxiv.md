# Daily arXiv - 2026-08-04

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-04T23:52:53
- Paper count: 10

## 1. A Heuristic Perspective on Debiasing Language Models

- Source: arxiv
- arXiv ID: 2608.00622
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.00622v1
- PDF: https://arxiv.org/pdf/2608.00622v1
- DOI: https://doi.org/10.48550/arXiv.2608.00622

### Authors

Tian Lan, Yemin Wang, Chuancheng Shi, Xiangyu Wu, Zesheng Shi, Yuan Wang, Jiang Li, Guanglai Gao, Xiangdong Su

### Abstract

Language models (LMs) often acquire various biases during pre-training and may express them in interactions, potentially causing social harm. Existing methods often rely on counterfactual augmentation or representation projection. These strategies remain limited in practice due to their high computational costs and difficulty in scaling to larger models. Additionally, many of these strategies require manual data annotation, narrowing their scope to specific cultures and bias categories. To overcome these limitations, we propose HEIMAT, a HEurIstic-style autoMATic debiasing framework for LMs. HEIMAT consists of two main steps: bias disclosure and debiasing fine-tuning. In the first step, it uses simple templates to construct heuristic prompts, which are applied to reveal model biases and generate corresponding context prompts. In the second step, it fine-tunes the model by minimizing the Jensen-Shannon divergence of predictions on these context prompts to reduce bias. Extensive experiments show that HEIMAT effectively mitigates bias in different cultures while maintaining the model's natural language understanding (NLU) performance.

### 中文一句话结论
HEIMAT是一种基于启发式模板的自动去偏框架，通过提示暴露模型偏见并最小化预测分布的JS散度来微调模型，无需固定数据集或手动标注，在跨语言和跨文化场景下有效降低偏见同时保持自然语言理解性能。

### English TL;DR
HEIMAT is a heuristic-based automatic debiasing framework for language models that uses simple templates to reveal biases and fine-tunes the model via Jensen-Shannon divergence to reduce bias across cultures without requiring fixed datasets or manual annotation, while preserving natural language understanding.

### 中文详细总结
本文提出HEIMAT框架，旨在解决现有去偏方法计算成本高、难以扩展至大模型、依赖手动数据标注等问题。HEIMAT包含两个步骤：第一步通过六个简单模板构建启发式提示，揭示模型对特定人口统计属性的偏见，并生成关联提示以扩展替代词列表；第二步利用这些替代词构造上下文提示集，通过最小化预测分布的Jensen-Shannon散度进行微调，使模型在不同人口属性下输出一致。实验表明，HEIMAT能有效降低性别和种族偏见，并保持自然语言理解能力，且通过翻译模板和调整偏见词可轻松迁移至其他语言和文化。

### 方法 / 贡献
- 提出HEIMAT自动去偏框架，无需外部语料或固定偏好数据集。
- 使用六种启发式提示模板自动构建偏见揭示和替代词列表，降低人工成本。
- 通过最小化Jensen-Shannon散度对上下文提示集进行微调，实现人口统计属性不变性。
- 框架可通过简单修改提示模板和偏见词，适应不同语言、文化和偏见类别。

### 实验或数据
- 在五个预训练语言模型（如BERT）上进行实验。
- 使用三个偏见评估基准（CrowS-Pairs、StereoSet等）和两个自然语言理解数据集。
- 定量结果展示HEIMAT在性别和种族偏见指标上的表现，并与CDA、Dropout、INLP、Sent-Debias等方法对比。

### 值得关注点
- 无需固定偏好数据集或手动标注，自动适应不同模型和偏见类别。
- 仅依赖六个启发式提示模板和七个关联提示，轻量化设计。
- 跨语言和跨文化扩展简单；支持性别、种族等多种偏见类型。
- 在保持自然语言理解性能的同时，有效降低偏见。

### 局限性
- 实验主要基于英文和法语，其他语言和文化的泛化性需进一步验证。
- 对大规模模型的微调计算成本可能仍较高，尽管比现有方法更经济。
- 依赖预定义提示模板，可能无法覆盖所有偏见场景或新兴偏见。
- 未讨论对模型生成文本质量（如流畅性、多样性）的影响。

## 2. Two-Stage Bengali Sentiment Classification: Domain Adaptation Through Continual Learning and Parameter-Efficient Fine-Tuning

- Source: arxiv
- arXiv ID: 2608.01471
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.01471v1
- PDF: https://arxiv.org/pdf/2608.01471v1
- DOI: https://doi.org/10.48550/arXiv.2608.01471

### Authors

MD Shaikh Rahman, Syed Maudud E Rabbi, Muhammad Mahbubur Rashid

### Abstract

Understanding sentiment in low-resource languages remains a key challenge for Natural Language Processing (NLP), particularly when domain-specific data is scarce. In this work, we present SentiBanglaBERT, a two-stage Bengali sentiment classification framework combining domain-adaptive continual pretraining and parameter-efficient fine-tuning. The approach enables contextual adaptation to news-style data while remaining computationally efficient through Low-Rank Adaptation (LoRA). Beyond performance, SentiBanglaBERT integrates SHAP-based interpretability, offering linguistic insights into how Bengali morphological cues, such as negation suffixes and aspectual markers, influence sentiment predictions. Experiments demonstrate stable performance comparable to strong baselines while providing greater transparency and interpretive depth. This framework highlights the potential of domain-adaptive continual learning as a foundation for interpretable, resource-efficient NLP in morphologically rich, underrepresented languages.

### 中文一句话结论
本文提出了 SentiBanglaBERT，一个结合持续预训练和 LoRA 参数高效微调的二阶段孟加拉语情感分类框架，在保持与强基线模型相当性能的同时，通过 SHAP 可解释性分析揭示了形态学特征对情感预测的影响。

### English TL;DR
SentiBanglaBERT introduces a two-stage Bengali sentiment classification framework that uses domain-adaptive continual pretraining and LoRA-based parameter-efficient fine-tuning to achieve stable performance comparable to strong baselines while providing SHAP-based interpretability for understanding morphological influences on sentiment.

### 中文详细总结
本研究针对孟加拉语等低资源语言的情感分类任务，提出了 SentiBanglaBERT 框架。该框架包含两个阶段：第一阶段通过分块（chunk-based）的掩码语言建模进行持续预训练，使模型适应新闻领域数据；第二阶段采用低秩适应（LoRA）进行参数高效微调，仅更新约 29.4万个参数（总参数约 1.1亿），显著降低了计算成本。实验表明，该模型在测试集上达到 96.86% 的准确率和 96.46% 的宏 F1 分数，与强基线模型性能相当。此外，通过 SHAP 可解释性分析，研究首次系统量化了孟加拉语形态特征对情感预测的影响，发现否定后缀（如 -ni）具有最高的重要性（0.761），其次是体标记（0.156）和时间标记（0.279）。

### 方法 / 贡献
1. **二阶段训练流程**：第一阶段使用分块持续预训练将 BanglaBERT 适应新闻领域；第二阶段插入 LoRA 适配器（秩 r=8）进行情感分类微调，显著降低参数更新量。
2. **可解释性分析**：首次对孟加拉语 Transformer 模型进行 SHAP 分析，系统量化了否定后缀、体标记、时态标记、格标记等形态特征的贡献度。
3. **实验框架**：提供了受控的基线比较（直接 LoRA 微调 vs. 持续预训练+LoRA），并包含统计显著性检验和计算效率分析。

### 实验或数据
- **数据集**：使用合成的三分类孟加拉语情感数据集（44,236 样本，90/10 训练测试划分，种子 42）。类别分布：负面（15,775）、中立（11,007）、正面（17,454）。
- **第一阶段数据**：约 11,500 个孟加拉语新闻样本用于领域适应掩码语言建模。
- **实验结果**：Stage1+LoRA 达到 96.86% 准确率（宏 F1=96.46%），相比直接 LoRA 微调（96.67% 准确率）略有提升。训练时间增加 42.4%。
- **可解释性**：100 个测试样本的 SHAP 分析（5 次运行平均相关系数 r=0.87），平均绝对重要性 0.093。

### 值得关注点
1. **计算效率**：仅微调 0.27% 的参数（294k/110M），适合低资源场景。
2. **形态特征层次**：发现否定后缀（0.761）> 完成体标记（0.057）> 时态标记（0.279）> 体标记（0.156）> 格标记（0.034）的重要性层次。
3. **错误分析**：88.7% 错误样本的置信度 >0.9，其中中立类错误占 62.1%（主要混淆为正面）。

### 局限性
1. **数据限制**：使用合成孟加拉语情感数据，缺乏真实社交媒体或对话文本的多样性，可能高估性能。
2. **可解释性样本量小**：因计算成本限制仅分析 100 个测试样本（虽重复运行显示一致性）。
3. **持续预训练收敛不足**：平均 MLM 困惑度 2,689.54 较高，表明预训练可进一步优化。
4. **LoRA 超参数未优化**：未针对孟加拉语进行系统超参数调优。
5. **计算开销**：持续预训练使训练时间增加 42.4%。

## 3. Training-Free versus Training-Based Intent Classification in LLMs: Accuracy, Robustness, and Failure Modes

- Source: arxiv
- arXiv ID: 2608.02415
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.02415v1
- PDF: https://arxiv.org/pdf/2608.02415v1
- DOI: https://doi.org/10.48550/arXiv.2608.02415

### Authors

Nan Chen, Zhouhao Yang, Soufiane Hayou

### Abstract

Intent classification in Large Language Models (LLMs) involves categorizing user prompts into predefined classes. For instance, given a user prompt, the system must determine whether it primarily concerns mathematics, coding, or general text processing. Such classification enables routing prompts to specialized models optimized for specific domains, improving both accuracy and computational efficiency. In this work, we conduct a systematic study comparing training-free vs training-based approaches for intent classification. For this purpose, we consider two lightweight, training-free methods based on statistics of internal representations and compare them against MLP classifiers and linear probes. Our comprehensive empirical evaluation reveals that 1) Both training-free and training-based methods saturate easy benchmarks (mathematics vs. coding vs. natural language), 2) Training-based classifiers have an advantage on harder classification tasks (e.g. Java vs Python), and 3) Training-free methods are generally more robust to mixed-intent and adversarial prompts.

### 中文一句话结论
本文系统比较了基于训练与免训练的LLM意图分类方法，发现二者在简单基准上均达饱和，训练方法在细粒度任务上准确率更高，但免训练方法对混合意图和对抗性提示更鲁棒。

### English TL;DR
This paper compares training-free and training-based intent classification in LLMs, finding that while both saturate easy benchmarks, training-based methods excel on harder tasks but training-free methods are more robust to mixed-intent and adversarial prompts.

### 中文详细总结
该论文系统研究了LLM中的意图分类任务（将用户提示归类为如数学、编程、通用文本等预定义类别），用于路由到专用模型以提升准确性和效率。作者提出两种轻量级免训练方法：VecStat（保留逐坐标一阶/二阶矩）和NormStat（压缩为token归一化范数的单变量统计，更省内存），并与基于训练的MLP分类器和线性探针对比。在7个基准数据集（覆盖粗粒度和细粒度）及1B–32B参数的LLM上进行实验，发现：1）简单任务（如数学 vs 编程 vs 自然语言）上两类方法均饱和；2）细粒度任务（如Java vs Python）上训练方法更准；3）在混合意图和对抗性重写提示下，免训练方法通常更稳定、鲁棒。作者还构建了混合意图数据集和对抗性提示数据集进行压力测试，并从理论上分析了VecStat（方向性分离有利）和NormStat（径向信息充分时更经济）的适用场景。

### 方法 / 贡献
- 提出两种无需梯度更新的免训练方法：VecStat（基于坐标均值/方差，用高斯KL散度或余弦相似度评分）和NormStat（基于归一化token范数的均值和方差，用单变量高斯KL散度评分），均在prefill阶段计算。
- 与训练方法（MLP分类器、线性探针）进行系统对比。
- 在简化的高斯模型下提供理论分析：VecStat在类别分离主要依靠方向信息时更优，NormStat在径向信息足以区分时更划算（校准开销更低）。
- 构建混合意图数据集和对抗性提示数据集，用于压力测试分类器的鲁棒性。
- 在7个数据集、1B–32B参数的多个LLM上开展粗粒度和细粒度的全面评估。

### 实验或数据
论文在7个基准数据集上进行实验，覆盖粗粒度与细粒度意图分类，LLM参数范围为1B–32B。此外，作者创建了混合意图数据集和对抗性重写提示数据集。摘要未提供具体数据集名称和详细实验设置。

### 值得关注点
- 免训练方法在混合意图和对抗性提示下表现更鲁棒，这对实际LLM路由场景（输入常含噪声或歧义）具有吸引力。
- 训练方法在细粒度任务上准确率更高，但该优势在压力测试下可能消失。
- 论文对激活统计压缩进行了理论解释，为方法选择（方向性 vs 径向信息）提供了依据。
- 所有方法均利用prefill阶段的中间表示，避免了存储专用编码器模型的额外开销。

### 局限性
提供的摘要和预览内容未明确讨论局限性。论文指出“没有一种方法适用于所有意图分类任务”，表明两种范式各有权衡；训练方法需要标签数据且可能需随意图空间变化重训练，而免训练方法在极细粒度任务上准确率可能不足。

## 4. Human-LLM Alignment in Language Attitudes Toward Non-Native Japanese

- Source: arxiv
- arXiv ID: 2608.01629
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.01629v1
- PDF: https://arxiv.org/pdf/2608.01629v1
- DOI: https://doi.org/10.48550/arXiv.2608.01629

### Authors

Naho Orita, Hayato Ogawa, Daisuke Kawahara

### Abstract

Large language models (LLMs) increasingly evaluate human writing in high-stakes domains such as hiring and academic assessment, putting non-native speakers at particular risk. Drawing on the language attitudes framework, we compared human and LLM evaluations of parallel L1- and L2-written Japanese emails on three dimensions: fluency, status, and solidarity. Japanese raters rated L2 texts significantly lower on all three dimensions, with a fluency gap roughly twice the size of the status and solidarity gaps. Six LLM judges reproduced the direction of this bias, and five reproduced its ordering across dimensions. The models diverged from humans in two ways: all understated the solidarity gap, the most socially grounded dimension, and all differentiated among learner L1 backgrounds where humans did not. LLM judges thus reproduce native speakers' language attitudes in a structured yet attenuated form, and the language attitudes framework offers a ready-made yardstick for auditing them beyond English.

### 中文一句话结论
日语母语者在流畅度、地位、团结感三个维度上都会给二语（L2）日语邮件显著更低的评价，且流畅度差距最大；六种大语言模型（LLM）虽然能复现这种偏见的总体方向，但系统性低估了团结感维度上的差距，并且会区分学习者母语背景（人类不会）。

### English TL;DR
Human Japanese raters penalize L2-written emails on fluency, status, and solidarity, with the largest penalty on fluency. Six LLMs reproduce the direction and ordering of this bias but understate the socially grounded solidarity gap, and they differentiate among learners’ L1 backgrounds where humans do not.

### 中文详细总结
本研究以“语言态度”（language attitudes）框架为桥梁，比较了人类与LLM对L1和L2日语邮件的评价。人类日语母语评分者在流畅度（fluency）、地位（status）、团结感（solidarity）三个维度上都对L2文本给分更低，其中流畅度差距约是地位和团结感差距的两倍；地位差距大于团结感差距，但未达到统计显著。六个LLM评分者均复现了L2被贬低的偏见方向，其中五个模型复现了“流畅度 > 地位 > 团结感”的维度排序。模型与人类的偏离主要体现在两点：所有模型都低估了团结感差距（这是最具社会关系性的维度）；所有模型都根据学习者母语背景做出了区分，而人类评分者没有。整体上，LLM以结构化但被减弱的形式复现了母语者的语言态度；作者认为语言态度框架可作为英语之外审计LLM评分者的现成标尺。

### 方法 / 贡献
- 使用I-JAS FOLAS语料库中的内容受控L1/L2平行日语邮件（涉及请求推荐信、请求延期、拒绝请求三种言语行为）。
- 人类评分者（实验1）通过日本Yahoo! Crowdsourcing招募，每个评分者只评一封邮件。
- LLM评分者（实验2）使用LLM-as-a-judge范式，对六个模型施测相同的9个Likert题项（每维度3题）。
- 采用线性混合模型分析人类数据，OLS分析LLM数据；用似然比检验学习者母语背景效应。
- 贡献：将“流畅性原则”从口语扩展到书面语；在非英语、非西方语境（日语）中提供量化的语言态度证据；为审计LLM在非英语中的偏见提供了社会语言学方法。

### 实验或数据
- 人类实验：2,070份提交，经筛选后有效评分者1,536人（L1条件766人，L2条件770人）；每封邮件平均约4.4人评分；人类数据覆盖174封L1邮件和173封L2邮件。
- LLM实验：6个模型（GPT-5.4、GPT-4o-mini、Claude Sonnet 4.5、PLaMo Prime 2.1、Llama 3.1 8B Instruct、Swallow 8B）；使用完整L1-L2配对145对（290封邮件），每个模型评一次，共1,740次API调用；7条无法解析的响应被排除。
- 人类结果：L2在流畅度（β=-1.11）、地位（β=-0.57）、团结感（β=-0.49）上均显著更低；L2评分不受学习者L1背景显著影响。
- LLM结果：6个模型均在三个维度上给L2显著更低分；5/6模型复现人类维度排序；所有模型在至少两个维度上显示出显著的学习者L1背景效应；模型总体评分更偏向高分、分布更窄。

### 值得关注点
- LLM在完全不知道写作者身份的情况下，仅凭L2语言形式就触发了更低的胜任力和温暖评价，这对招聘、教育评估等高风险场景有直接警示意义。
- 团结感差距被所有模型低估，且三个多语言商业模型的团结感差距显著小于地位差距，与人类不同。
- 模型的自由文本理由中更多提及语言形式（如语法、流畅），更少提及人际品质；虽然评分上出现地位差距，但很少用胜任力类词汇解释。
- Swallow 8B是唯一未复现维度排序的模型，8B开源模型整体差距最弱。

### 局限性
- 语料仅来自单一语料库，且只覆盖三种言语行为/邮件类型，其他体裁可能呈现不同模式。
- L1版本是母语者对学习者邮件的改写，虽控制了内容，但可能仍存在细微的语域差异。
- 自由文本理由的编码采用自动关键词匹配，未经人工验证。
- 只考察了六个模型，且模型迭代很快；非母语写作者越来越多使用生成式AI修改或起草文本，实际被评估的文本可能不再等同于原始学习者输出。

## 5. What Transfers from Text to Vision? Capability Scaling Laws and Transfer Dynamics for VLMs

- Source: arxiv
- arXiv ID: 2608.00013
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.00013v1
- PDF: https://arxiv.org/pdf/2608.00013v1
- DOI: https://doi.org/10.48550/arXiv.2608.00013

### Authors

Ziran Li, Qiang Wang, Zhengyu Chen, Shanglin Lei, Borun Chen, Jingang Wang, Xunliang Cai

### Abstract

Choosing the right large language model (LLM) backbone is the most consequential decision when building a vision-language model (VLM), yet it remains fundamentally unprincipled: compute-based scaling laws fail to generalize across model families, and no framework exists for directly predicting VLM performance before training begins. We propose the Capability-Driven Multimodal Scaling Law, the first cross-family framework that predicts VLM benchmark accuracy from directly observable textual capability. Given a low-dimensional capability score $S$ extracted from LLM textual benchmarks via PCA, we model VLM performance as a function of $S$, with a per-backbone transfer rate and an absorption rate that quantifies data-scaling efficiency. To fit and validate the framework, we train over 150 VLMs on 34 LLMs spanning 7 model families under a strictly controlled recipe. Evaluations on more than 200 textual and 50 multimodal benchmarks show that the law accurately extrapolates transfer rate from models up to 8B parameters to 72B-scale backbones, predicts full VLM training trajectories with high fidelity, and generalizes to entirely held-out model families. Beyond the scaling law, our analysis surfaces actionable insights: certain textual benchmarks negatively correlate with multimodal performance, exposing latent benchmark-gaming behavior; base LLMs outperform instruction-tuned counterparts as VLM backbones due to higher absorption rates and lower data-scaling decay; and different model families occupy distinct positions in the transfer--absorption space. The framework turns backbone selection from costly empirical sweeps into a principled, quantitative decision. Code and data are available at https://github.com/wangq-dev/CDMScaling.

### 中文一句话结论
本文提出“能力驱动的多模态缩放定律”（Capability-Driven Multimodal Scaling Law），用 LLM 文本基准经 PCA 提取的低维能力分数直接预测 VLM 的基准准确率，从而把 VLM 的 LLM 主干选择从昂贵试错变成可量化的决策。

### English TL;DR
This paper proposes the Capability-Driven Multimodal Scaling Law, the first cross-family framework that predicts vision-language model (VLM) benchmark accuracy from directly observable LLM textual capability. A low-dimensional capability score \(S\) is extracted via PCA from textual benchmarks, and VLM performance is modeled as a function of \(S\) and multimodal data volume, with per-backbone transfer and absorption rates. Trained on over 150 VLMs built from 34 LLMs across 7 families, the law extrapolates to 72B-scale backbones, predicts training trajectories, and generalizes to held-out families.

### 中文详细总结
现有基于计算量的缩放定律无法跨模型家族泛化，也没有框架能在训练前直接预测 VLM 性能。本文提出首个跨家族的“能力驱动多模态缩放定律”：从 LLM 的文本基准分数中，用 PCA 提取低维能力分数 \(S\)，并将 VLM 性能建模为 \(S\) 与多模态数据量 \(D_{\text{mm}}\) 的函数，引入每个主干模型的“迁移率”（transfer rate）和“吸收率”（absorption rate）刻画数据缩放效率。

作者在严格受控的训练设置下，用 34 个 LLM（覆盖 7 个模型家族）训练了 150 多个 VLM，并在 200 多个文本基准和 50 多个多模态基准上验证。结果表明该定律能从 8B 以内的模型外推到 72B 规模主干，高保真地预测完整 VLM 训练轨迹，并泛化到完全未见的模型家族。

除缩放定律外，分析还揭示：部分文本基准与多模态性能负相关，暴露潜在基准游戏行为；基座 LLM 比指令微调版本更适合做 VLM 主干，因为吸收率更高、数据缩放衰减更低；不同模型家族在“迁移–吸收”空间中处于不同位置。该框架使主干选择从经验性试错转变为原则化、定量的决策。代码和数据见 https://github.com/wangq-dev/CDMScaling。

### 方法 / 贡献
- **能力驱动缩放定律**：用 PCA 从文本基准中得到低维能力分数 \(S\)，替代参数规模作为主干能力代理；将 VLM 性能建模为 \(P = \hat A S + \hat B \ln D_{\text{mm}} + P_0\)，其中吸收率 \(\hat B = B_0 - B_m S\)。
- **跨家族统一框架**：不依赖模型内部训练细节，仅使用公开可复现的文本基准分数，可直接预测 VLM 表现。
- **迁移与吸收机制解释**：区分文本能力迁移项与多模态数据吸收项，并建模“吸收衰减”现象。
- **实用决策工具**：支持候选主干性能预测、数据和主干联合选择，以及超参数外推。

### 实验或数据
- 训练并验证了 **150 多个 VLM**，基于 **34 个 LLM**，覆盖 **7 个模型家族**。
- 评估使用 **200 多个文本基准**和 **50 多个多模态基准**。
- 验证了从 **8B 以内模型外推到 72B 规模主干**的能力。
- 在**完全未见的模型家族**上验证了泛化性。
- 摘要未提及具体数据集的创建细节或人工标注流程；代码和数据已开源。

### 值得关注点
- 发现某些文本基准与多模态性能**负相关**，提示 LLM 可能存在“基准游戏”行为。
- **基座 LLM 优于指令微调 LLM** 作为 VLM 主干：基座模型吸收率更高、数据缩放衰减更低。
- 不同模型家族在“迁移–吸收”空间中占据不同位置，反映预训练策略差异。
- 该框架将主干选择从昂贵经验扫描转化为原则化、定量的决策过程。

### 局限性
论文摘要和所给预览内容未明确列出局限性。可推测该框架依赖文本基准的可公开获取性与 PCA 低维表示假设，且实验验证限于 34 个 LLM、7 个模型家族和 150 余个 VLM；但这些是合理推断，并非原文明确陈述。

## 6. DeBERTa-Sentinel: Toward Transparent and Trustworthy Detection of AI-Generated Text

- Source: arxiv
- arXiv ID: 2608.01046
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.01046v1
- PDF: https://arxiv.org/pdf/2608.01046v1
- DOI: https://doi.org/10.48550/arXiv.2608.01046

### Authors

Muhammad Yousaf Rehman, Muhammad Islam

### Abstract

The rapid spread of large language models (LLMs) across the web raises concerns about misinformation, academic integrity, automated content manipulation, and risks to vulnerable online communities. Existing transformer-based detectors, such as GPT-Sentinel, show promise but struggle to generalize to diverse model outputs and paraphrasing attacks, limiting their role in building trustworthy web ecosystems. This work introduces DeBERTa-Sentinel, a responsible AI-generated text detection framework leveraging DeBERTa-v3's disentangled attention to capture subtle structural irregularities in synthetic content. A central design principle is transparency: unlike black-box commercial detectors, DeBERTa-Sentinel exposes token-level explanations of its decisions, enabling affected stakeholders journalists, educators, and platform trust and safety teams to audit, challenge, and contextualize detection outcomes. Using the GLC-AIText dataset of 28,057 human and LLM-generated samples (GPT, LLaMA, and Claude) with a 60-20-20 split, DeBERTa-Sentinel achieves 98.21\% validation accuracy and surpasses the RoBERTa-Sentinel baseline from NeurIPS 2025, achieving 97.53\% test accuracy, 95.89\% precision, 99.33\% recall, and 99.53\% ROC-AUC, and maintaining a 0.665\% false negative rate. The model's interpretability reveals linguistic markers such as academic phrasing and formal transitions associated with synthetic text, directly supporting stakeholder needs for verifiable, auditable content-authenticity decisions. By advancing responsible detection methods that reduce bias and enhance explainability, DeBERTa-Sentinel promotes trustworthy, ethical, and human-centric AI systems. Code and data are available at https://github.com/Galileo-Galili/HUMAN-VS-AI-TEXT-DETECTION.

### 中文一句话结论  
DeBERTa-Sentinel 基于 DeBERTa-v3 的解耦注意力机制，结合词级可解释性，在多种 LLM 生成的文本检测中达到 97.53% 测试准确率，并显著优于 RoBERTa 基线。

### English TL;DR  
DeBERTa-Sentinel introduces a transparent AI-generated text detection framework using DeBERTa-v3's disentangled attention and token-level explanations, achieving over 98% accuracy on diverse LLM outputs while enabling stakeholders to audit and understand detection decisions.

### 中文详细总结  
本文提出 DeBERTa-Sentinel，一个透明且可信赖的 AI 生成文本检测框架。核心设计包括：使用 DeBERTa-v3 的解耦注意力机制分别建模内容与位置信息，以更好捕捉合成文本中的结构异常；提供词级归因解释，允许记者、教育者及平台安全团队审计检测结果。实验基于 GLC-AIText 数据集（共 28,057 个人类与 AI 样本，来自 GPT-3.5、LLaMA 和 Claude，按 60-20-20 划分），验证准确率 98.21%，测试准确率 97.53%，精确率 95.89%，召回率 99.33%，ROC-AUC 99.53%，假阴性率仅 0.665%。对比基线 RoBERTa-Sentinel（NeurIPS 2025 基准）取得一致提升。可解释性分析显示模型能识别学术化措辞、正式过渡短语等合成文本典型语言标记。代码与数据开源。

### 方法 / 贡献  
1. **模型架构**：以 DeBERTa-v3-small 为骨干，替换 RoBERTa；利用 12 层解耦注意力编码序列，[CLS] 向量经全连接分类头输出二分类概率。输入长度统一为 256 tokens。  
2. **数据集构建**：扩展现有 OpenGPTText 数据集，新增 LLaMA 与 Claude 的改写样本，形成 GLC-AIText（共 58,537 条，含 28,057 条 AI 文本与 29,142 条人类文本）。  
3. **透明性设计**：内置词级归因（token-level explanation），提升决策可审计性。  
4. **跨生成器泛化**：通过保留生成器（hold-out）实验验证模型学到可迁移表征而非生成器特定伪影。

### 实验或数据  
- **数据集**：GLC-AIText，包含 GPT-3.5（9,374 条）、LLaMA（10,400 条）和 Claude（8,283 条）三组改写文本，人类文本来自 OpenWebText-Final。平衡后共 58,537 条，按 60% 训练、20% 验证、20% 测试划分（随机种子 42）。  
- **主要结果**：
  - 验证准确率 98.21%，测试准确率 97.53%  
  - 精确率 95.89%，召回率 99.33%，ROC-AUC 99.53%，假阴性率 0.665%  
  - 超出 RoBERTa-Sentinel（NeurIPS 2025 基准）  
- **额外实验**：保留生成器测试（hold-out experiment）准确率 98.46%（原文提及，具体指标在预览中截断）。  
- **可解释性**：识别出过渡短语、学术术语等合成文本标记。

### 值得关注点  
- **透明性与可审计性**：词级归因使检测结果可解释，非黑盒，特别适用于教育、新闻等高风险场景。  
- **跨模型泛化**：训练数据涵盖三种架构不同的 LLM（GPT、LLaMA、Claude），并通过保留生成器实验验证泛化能力。  
- **责任 AI 设计**：明确减少偏见、增强可解释性，符合伦理与人文中心 AI 原则。  
- **开源**：代码与数据已公开。

### 局限性  
本文未明确列出局限性。从相关工作中推断可能包括：对更前沿模型（如 GPT-4o、Claude 3.5）的泛化尚未验证；改写攻击（paraphrase attack）下的鲁棒性仅初步测试；数据集以英文为主，跨语言泛化未知。

## 7. CoT-Core: Accelerating LLM Evaluation via CoT-Aware Coreset Selection

- Source: arxiv
- arXiv ID: 2608.00014
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.00014v1
- PDF: https://arxiv.org/pdf/2608.00014v1
- DOI: https://doi.org/10.48550/arXiv.2608.00014

### Authors

Qihua Pan, Zhenheng Tang, Peijie Dong, Xiang Liu, Huacan Wang, Bo Li, Xiaowen Chu

### Abstract

Evaluating Large Language Models (LLMs) incurs prohibitive computational overhead during continuous development processes. While coreset selection accelerates evaluation, existing methods either suffer from a severe ``cold start'' bottleneck requiring massive historical logs (e.g., Item Response Theory) or exhibit a surface lexical bias that misses the underlying reasoning manifold of tasks. We propose CoT-Core, a novel training-free core question selection framework. Recognizing that lexically disparate questions can share equivalent underlying logic, CoT-Core prompts LLMs to unroll zero-shot Chain-of-Thought (CoT) reasoning trajectories. Projecting these paths into a latent space effectively clusters questions by intrinsic logical equivalence rather than superficial text similarity. Extensive experiments on GSM8K, MMLU, MMLU-Pro, and GPQA demonstrate that CoT-Core drastically reduces evaluation costs while maintaining high-fidelity score estimation, and delineate the boundary conditions of reasoning-aware pruning, revealing that its efficacy is intrinsically gated by task complexity.

### 中文一句话结论
CoT-Core 通过利用思维链推理轨迹聚类问题，实现了无需历史数据的、基于逻辑等价的训练自由核心集选择，从而大幅加速 LLM 评估，同时保持高保真度性能估计。

### English TL;DR
CoT-Core accelerates LLM evaluation by using Chain-of-Thought reasoning trajectories to select a minimal, representative subset of questions based on their underlying logical structure, drastically reducing computational overhead while preserving high-fidelity performance estimation.

### 中文详细总结
大型语言模型（LLM）的持续开发过程中，在完整基准上进行评估的计算开销过大。现有核心集选择方法面临两个主要瓶颈：一是基于项目反应理论（IRT）等历史依赖的方法存在严重的“冷启动”问题，需要大量历史评估日志；二是基于几何的方法（如k-中心点贪心算法）通常依赖文本嵌入，存在“表面词汇陷阱”，容易将词汇相似但逻辑不同的问题聚类，而忽略了任务的潜在推理流形。

CoT-Core 提出了一个新颖的、无需训练的核心问题选择框架。其核心洞察在于：词汇上不同的问题可能共享等价的底层逻辑。该方法首先提示LLM生成零样本的思维链推理轨迹，然后将这些轨迹与原始问题一起嵌入到潜在空间中。通过这种方式，CoT-Core 能够基于内在的逻辑等价性而非表面的文本相似性进行聚类，有效避免了词汇陷阱。最后，通过标准聚类算法选择最具代表性的核心子集。

在 GSM8K、MMLU、MMLU-Pro 和 GPQA 等基准上的大量实验表明，CoT-Core 在严格降低评估成本（例如在 1% 采样率下）的同时，能够保持高保真度的模型性能估计。研究还揭示了推理感知剪枝的边界条件，即其有效性受任务复杂度的内在调控：对于需要复杂推理的任务（如 GPQA），CoT-Core 的优势最为显著。

### 方法 / 贡献
1.  **提出了 CoT-Core 框架**：一种新颖的、无需训练的核心集选择框架，通过思维链轨迹嵌入来规避词汇陷阱。
2.  **方法创新**：将空间核心集选择与下游代理估计解耦。CoT-Core 采用基于质心的几何采样提取代表性子集，天然支持标准聚合（SA）以实现完全无需训练的流程，同时也能与基于概率的估计器（如 GP-IRT）无缝兼容。
3.  **主要贡献**：实验证明 CoT-Core 能大幅降低评估开销并保持高保真度。同时，研究刻画了推理感知剪枝的边界条件，揭示了其有效性与任务复杂度紧密相关。

**流程**：轨迹生成 → 上下文轨迹嵌入 → 同构聚类与选择。

### 实验或数据
- **基准测试**：GSM8K、GPQA（Diamond 子集）、MMLU、MMLU-Pro。
- **生成器LLM**：Phi-4。
- **嵌入模型**：BGE-M3。
- **基线方法**：比较了训练无关的方法（随机采样、基于文本嵌入的K-Means、k-中心点贪心）和历史依赖的方法（正确率K-Means、IRT）。
- **评估协议**：在严格预算（1%、2%、5% 的采样率）下提取核心集，并使用标准聚合（SA）进行评估。历史依赖方法在 N=25 个模型的低资源设置下拟合。
- **实验结果**：主要结果在 Table 1 中展示。在 1% 的采样率下，CoT-Core 在 GPQA（+7.88%）和 GSM8K（+2.82%）上显著优于最强的训练无关基线。在 MMLU 上，其表现与基于嵌入的 K-Means 相当或略优；在 MMLU-Pro 上，当采样率极低时，CoT-Core 略低于 k-中心点贪心算法。总体而言，CoT-Core 在所有基准和采样率下均一致性地优于随机采样。

### 值得关注点
1.  **规避“冷启动”问题**：与 IRT 等方法不同，CoT-Core 不依赖任何历史评估日志，可直接应用于新构建或私有基准测试。
2.  **逻辑感知的聚类**：通过嵌入推理轨迹，CoT-Core 成功区分了词汇相似但逻辑不同的问题，以及词汇不同但逻辑相同的问题，这是传统文本嵌入方法无法做到的。
3.  **与任务复杂度的关系**：研究发现 CoT-Core 在需要复杂推理的任务（如 GPQA）上效果最好，而在知识密集型或相对简单的任务（如MMLU）上优势较小。这揭示了推理感知剪枝的边界条件。

### 局限性
1.  **对任务复杂度的依赖性**：CoT-Core 的有效性受任务复杂度的门控。对于知识索引型任务或简单任务，其优势可能不如图1所示那样显著，甚至可能不如基于原始问题的几何方法。
2.  **生成器 LLM 的选择**：该框架依赖于一个生成器 LLM 来产生零样本的思维链轨迹。不同的生成器模型可能会产生不同质量的轨迹，从而影响聚类效果。论文中使用了 Phi-4，但未深入探讨生成器模型对于最终结果鲁棒性的影响。
3.  **计算开销转移**：虽然加速了目标模型的评估，但 CoT-Core 本身需要用一个生成器 LLM 推理所有问题以产生轨迹，并用一个嵌入模型进行编码。这引入了额外的（但可能较小的）前期计算开销。

## 8. Semantic Alignment of AI Models: Concept Collapse, Checkpoint Dynamics, and Cross-Lingual Transfer

- Source: arxiv
- arXiv ID: 2608.01585
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.01585v1
- PDF: https://arxiv.org/pdf/2608.01585v1
- DOI: https://doi.org/10.48550/arXiv.2608.01585

### Authors

Tyler Ashoff, Jordan Rodu

### Abstract

Language model benchmarking is a difficult task. Outcome reasoning alone does not test the model's conceptualization of language and popular open-source benchmarks are quickly saturated or ingested as training data. It is important to test the model's output, but augmenting these tests by characterizing semantic structure gives more insight to how models relate abstract concepts. However, the high dimensional embedding spaces are not easy to interpret. This work demonstrates how topological methods can be used to rigorously compare these spaces to low dimensional and interpretable baselines like ontologies and curated knowledge graphs. These multi-modal alignment tests make it possible to track model adaptations and test phrase understanding across multiple languages.

### 中文一句话结论
本文提出利用拓扑方法将高维嵌入空间与低维可解释基准（如本体和知识图谱）对齐，以系统评估语言模型的语义结构，从而追踪概念坍缩、检查点动态及跨语言迁移。

### English TL;DR
This paper introduces topological methods for aligning high-dimensional AI model embeddings with interpretable baselines like ontologies, enabling rigorous evaluation of semantic structure to track concept collapse, checkpoint dynamics, and cross-lingual transfer.

### 中文详细总结
现有语言模型基准测试主要依赖任务输出（如多项选择或文本匹配），容易饱和且难以评估模型对语言概念的抽象理解。本文提出一种基于拓扑的方法，将模型的高维嵌入空间与低维、可解释的基准（如人工构建的本体和知识图谱）进行对齐。通过多模态对齐测试，可以比较不同模型的语义结构，并追踪训练过程中的概念坍缩、检查点演变以及跨语言短语理解的一致性。该方法不依赖具体输出任务，而是直接分析模型内部表示空间的拓扑形状，从而提供更鲁棒的语义评估。

### 方法 / 贡献
- **方法**：使用拓扑数据分析（如持续同调）将模型嵌入空间与低维基准（本体、知识图谱）进行结构对齐。
- **贡献**：
  - 提出一种不依赖具体任务输出的语义评估框架，可补充现有基准测试。
  - 实现对概念坍缩（概念逐渐丢失）、检查点动态（训练过程中语义结构变化）和跨语言迁移的定量追踪。
  - 提供开源实现（persiscope 库），便于复现和扩展。

### 实验或数据
摘要中未提及具体实验或数据集。论文主要介绍方法框架和动机，并未在摘要中给出实验结果或使用的数据集。

### 值得关注点
- 拓扑对齐方法可应对嵌入式高维空间难以解释的问题。
- 能够同时评估单语言和跨语言的语义一致性。
- 对现有基准测试（如 MMLU、HELM、BIG-Bench）的局限性有系统分析，并指出其易饱和、缺乏全局语义表征的问题。
- 方法具有通用性，适用于不同模型和训练阶段。

### 局限性
摘要未明确讨论方法局限性。基于上下文，该方法依赖高质量、可解释的基准（如本体和知识图谱），这些基准的构建和维护可能成本较高；拓扑计算在大规模模型上可能面临计算挑战；此外，对齐效果对基准的选择敏感，且未说明如何处理开放领域或动态概念。

## 9. AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling

- Source: arxiv
- arXiv ID: 2608.02602
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.02602v1
- PDF: https://arxiv.org/pdf/2608.02602v1
- DOI: https://doi.org/10.48550/arXiv.2608.02602

### Authors

Jiajun Liang, Yucheng Liao, Yukang Cao, Jiazhe Wei, Ken Li, Wende Tan, Jiankun Zhang, ZY Cui, Jingkang Yang, Liucheng Guo, Shiqi Yang, B. Yang, Caifeng Shan, Ziwei Liu, Chenyang Si

### Abstract

Language remains an outlier in generative modeling: while images, video, and audio are increasingly modeled in continuous latent spaces, text generation still relies predominantly on discrete tokens. Existing continuous language models either inherit embedding spaces not designed for joint generation and decoding, or compress autoencoded latents to ease diffusion, sacrificing token-level fidelity. Instead of simplifying the representation to suit the generative model, we preserve a high-capacity, decodable text latent and design the diffusion model to learn its distribution directly.
  We introduce AURORA-LM, a continuous-latent diffusion language model that separates the construction of a decodable text representation from the modeling of its distribution. A Query-based Encoder-Decoder organizes text into a high-capacity, prefix-aligned latent sequence, and a Block-causal Diffusion Transformer learns its distribution through flow matching, generating blocks left to right while denoising positions within each block in parallel. Because such a latent is harder for diffusion to model, AURORA-LM restricts only the noisy-input pathway while retaining the full clean-latent prediction target, accommodating full-width latents without reducing decoder-facing capacity. We further calibrate the noise-level distribution to the latent width, and introduce self-trajectory consistency to bridge independently sampled training noise and iterative denoising at inference.
  AURORA-LM achieves the strongest performance among evaluated continuous and diffusion-based language models on OpenWebText free generation and XSum summarization. Scaling to 1B parameters with about 1500 EFLOPs of total compute yields further gains, surpassing a larger publicly released latent-diffusion language model under a matched evaluation protocol. All experiments are conducted on Ascend NPUs.

### 中文一句话结论

基于已有摘要判断：Language remains an outlier in generative modeling: while images, video, and audio are increasingly modeled in continuous latent spaces, text generation still relies predominantly on discrete tokens. Existing continuous language models either inherit embedding spaces not designed for joint generation and decoding, or compress autoencoded latents to ease diffusion, sacrificing token-level fidelity. Instead of simplifying the representation to suit the generative model, we preserve a high-capacity, decodable text latent and design the diffusion model to learn its distribution directly.
  We introduce AURORA-LM, a continuous-latent diffusion language model that separates the construction of a decodable text representation from the modeling of its distribution. A Query-based Encoder-Decoder organizes text into a high-capacity, prefix-aligned latent sequence, and a Block-causal Diffusion Transformer learns its distribution through flow matching, generating blocks left to right while denoising positions within each block in parallel. Because such a latent is harder for diffusion to model, AURORA-LM restricts only the noisy-input pathway while retaining the full clean-latent prediction target, accommodating full-width latents without reducing decoder-facing capacity. We further calibrate the noise-level distribution to the latent width, and introduce self-trajectory consistency to bridge independently sampled training noise and iterative denoising at inference.
  AURORA-LM achieves the strongest performance among evaluated continuous and diffusion-based language models on OpenWebText free generation and XSum summarization. Scaling to 1B parameters with about 1500 EFLOPs of total compute yields further gains, surpassing a larger publicly released latent-diffusion language model under a matched evaluation protocol. All experiments are conducted on Ascend NPUs.

### English TL;DR

Language remains an outlier in generative modeling: while images, video, and audio are increasingly modeled in continuous latent spaces, text generation still relies predominantly on discrete tokens. Existing continuous language models either inherit embedding spaces not designed for joint generation and decoding, or compress autoencoded latents to ease diffusion, sacrificing token-level fidelity. Instead of simplifying the representation to suit the generative model, we preserve a high-capacity, decodable text latent and design the diffusion model to learn its distribution directly.
  We introduce AURORA-LM, a continuous-latent diffusion language model that separates the construction of a decodable text representation from the modeling of its distribution. A Query-based Encoder-Decoder organizes text into a high-capacity, prefix-aligned latent sequence, and a Block-causal Diffusion Transformer learns its distribution through flow matching, generating blocks left to right while denoising positions within each block in parallel. Because such a latent is harder for diffusion to model, AURORA-LM restricts only the noisy-input pathway while retaining the full clean-latent prediction target, accommodating full-width latents without reducing decoder-facing capacity. We further calibrate the noise-level distribution to the latent width, and introduce self-trajectory consistency to bridge independently sampled training noise and iterative denoising at inference.
  AURORA-LM achieves the strongest performance among evaluated continuous and diffusion-based language models on OpenWebText free generation and XSum summarization. Scaling to 1B parameters with about 1500 EFLOPs of total compute yields further gains, surpassing a larger publicly released latent-diffusion language model under a matched evaluation protocol. All experiments are conducted on Ascend NPUs.

### 中文详细总结

基于论文摘要，该工作主要内容如下：Language remains an outlier in generative modeling: while images, video, and audio are increasingly modeled in continuous latent spaces, text generation still relies predominantly on discrete tokens. Existing continuous language models either inherit embedding spaces not designed for joint generation and decoding, or compress autoencoded latents to ease diffusion, sacrificing token-level fidelity. Instead of simplifying the representation to suit the generative model, we preserve a high-capacity, decodable text latent and design the diffusion model to learn its distribution directly.
  We introduce AURORA-LM, a continuous-latent diffusion language model that separates the construction of a decodable text representation from the modeling of its distribution. A Query-based Encoder-Decoder organizes text into a high-capacity, prefix-aligned latent sequence, and a Block-causal Diffusion Transformer learns its distribution through flow matching, generating blocks left to right while denoising positions within each block in parallel. Because such a latent is harder for diffusion to model, AURORA-LM restricts only the noisy-input pathway while retaining the full clean-latent prediction target, accommodating full-width latents without reducing decoder-facing capacity. We further calibrate the noise-level distribution to the latent width, and introduce self-trajectory consistency to bridge independently sampled training noise and iterative denoising at inference.
  AURORA-LM achieves the strongest performance among evaluated continuous and diffusion-based language models on OpenWebText free generation and XSum summarization. Scaling to 1B parameters with about 1500 EFLOPs of total compute yields further gains, surpassing a larger publicly released latent-diffusion language model under a matched evaluation protocol. All experiments are conducted on Ascend NPUs.

### 方法 / 贡献

未提供独立的方法细节；请参考摘要和论文链接。

### 实验或数据

未提供独立的实验或数据细节；请参考摘要和论文链接。

### 值得关注点

该条目的相关性来自 Zotero 语料相似度排序，可优先根据 relevance 和摘要判断是否精读。

### 局限性

自动总结主要基于标题、摘要和可用正文预览，可能遗漏全文中的实验细节。

## 10. DiffusionGemma Technical Report

- Source: arxiv
- arXiv ID: 2608.00146
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.00146v1
- PDF: https://arxiv.org/pdf/2608.00146v1
- DOI: https://doi.org/10.48550/arXiv.2608.00146

### Authors

DiffusionGemma Team, Adrien Ali Taïga, James Assiene, Daniele Calandriello, Rahma Chaabouni, João Gante, Tamara von Glehn, Nate Keating, Chris Knutsen, Martin Kukla, Tianlin Liu, Ivan Lobov, Ofir Nabati, João Gabriel Oliveira, Nicolas Perez-Nieves, Nastasia Prutianova, Bobak Shahriari, Jean Tarbouriech, Pavel Tyletski, Çağlar Ünlü, Cindy Wu, Glenn Cameron, Jerome Connor, Sertan Girgin, Maarten Grootendorst, Alon Levkovitch, Eliya Nachmani, Omar Sanseviero, Piotr Stanczyk, Quentin Berthet, Andrew Campbell, Clément Crepy, Valentin De Bortoli, Arnaud Doucet, Romuald Elie, Alexandre Galashov, Klaus Greff, Alexis Jacq, David Ruhe, Yu-Han Wu, Sebastian Flennerhag, Brendan O'Donoghue, George Scrivener, Shantanu Thakoor

### Abstract

We introduce DiffusionGemma, an experimental open-weight language model that uses discrete diffusion to generate text at exceptionally high speed. Rather than decoding one token at a time, DiffusionGemma iteratively refines blocks of 256 tokens in parallel, avoiding the sequential decoding bottleneck of conventional autoregressive (AR) large language models. Instead of training from scratch, we obtain DiffusionGemma by fine-tuning the mixture-of-experts Gemma 4 model with 3.8B activated and 25.2B total parameters. Our compute-efficient two-stage training pipeline uses fewer than 10% of the starting AR model's total training token budget. The first stage uses supervised fine-tuning to teach bidirectional denoising, while the second stage combines reinforcement learning with sampler distillation to jointly improve generation quality and inference efficiency. DiffusionGemma establishes a new Pareto frontier for the trade-off between generation speed and model capability. Averaged across our full evaluation suite, it generates around 20 tokens per forward pass and achieves roughly 1,500 output tokens per second on a single NVIDIA H100 GPU, which is substantially faster than AR models even with state-of-the-art speculative decoding. DiffusionGemma also retains the starting model's support for thinking mode, multimodal inputs, and long contexts. Despite diffusion fine-tuning, it remains capable of AR generation with only minor performance degradation, suggesting a path toward hybrid diffusion-AR decoding.

### 中文一句话结论
DiffusionGemma 是一个基于离散扩散的开源语言模型，通过并行生成 256 个令牌的块，实现了比传统自回归模型更快的文本生成速度，在速度和智能之间建立了新的帕累托前沿。

### English TL;DR
DiffusionGemma is an open-weight language model that achieves substantially faster text generation than conventional autoregressive models by using discrete diffusion to iteratively refine blocks of 256 tokens in parallel, establishing a new Pareto frontier between speed and capability.

### 中文详细总结
DiffusionGemma 是一个实验性的开源语言模型。与逐令牌生成的自回归模型不同，它采用离散扩散方法，并行迭代地精炼包含 256 个令牌的块，从而显著提升生成速度。该模型并非从头训练，而是基于 Gemma 4 混合专家模型（激活参数 3.8B，总参数 25.2B）微调而来。其训练流程分为两个阶段且计算高效，仅使用了原始自回归模型不到 10% 的训练令牌预算：第一阶段通过监督式微调学习双向去噪；第二阶段结合强化学习和采样器蒸馏，共同提升生成质量和推理效率。在单块 NVIDIA H100 GPU 上，DiffusionGemma 生成速度可达约 1500 令牌/秒，每个前向传播平均生成约 20 个令牌，显著快于采用最先进推测解码的自回归模型。该模型保留了其原始模型的思考模式、多模态输入和长上下文能力，并且在微调后仍能进行自回归生成，性能仅轻微下降，为混合扩散-自回归解码提供了可能。

### 方法 / 贡献
- **离散扩散模型**：采用离散扩散框架，迭代地并行精炼 256 令牌块，避免了自回归模型的顺序解码瓶颈。
- **计算高效的微调**：基于预训练的 Gemma 4 混合专家模型进行微调，而非从头训练。
- **两阶段训练流程**：
    1.  **监督式微调 (SFT)**：使模型适应对 256 个噪声令牌块的双向去噪。
    2.  **采样器蒸馏与强化学习 (SD·RL)**：联合优化生成质量（通过奖励）和推理速度（通过减少去噪步数）。
- **开放权重发布**：以 Apache 2.0 许可证发布模型权重，促进社区研究与应用。

### 实验或数据
报告中未提供具体的实验数据集名称或详细实验结果表格，但提及了其在 GPQA-Diamond 和 LiveCodeBench-v6 上的平均表现，并展示了与 Gemma 4 系列等其他模型在质量与速度上的帕累托曲线对比。

### 值得关注点
- **极致速度**：在单卡 H100 上达到约 1500 令牌/秒，每个前向传播 20 个令牌，显著快于自回归模型+推测解码。
- **性能与速度的新前沿**：建立了生成质量与速度之间新的帕累托前沿。
- **双重模式**：支持扩散生成和自回归生成，为混合解码提供了可能性。
- **保留原始能力**：保留了 Gemma 4 的思考模式、多模态和长上下文能力。
- **开源与社区影响**：采用了开放的 Apache 2.0 许可证，并已有社区用于语音识别和医疗等下游应用。

### 局限性
- **性能折损**：与原始自回归基线模型相比，扩散模型的生成质量存在一定的性能下降。
- **依赖基础模型**：模型是建立在 Gemma 4 之上的微调版本，其能力受限基础模型。
- **训练复杂性**：两阶段训练流程中的强化学习和采样器蒸馏部分可能实现复杂且需要精细调参。
- **文未详述**：报告未详细讨论所有已知的限制，部分问题在文末标记的局限性章节中提及，但摘要未包含其细节。

## Processing Notes

- Duplicate papers skipped: 0