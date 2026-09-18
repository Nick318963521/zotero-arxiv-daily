# Daily arXiv - 2026-09-18

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-18T00:34:49
- Paper count: 10

## 1. A Scalable Framework for Automated NER Annotation Correction in Low-Resource Languages

- Source: arxiv
- arXiv ID: 2609.18739
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.18739v1
- PDF: https://arxiv.org/pdf/2609.18739v1
- DOI: https://doi.org/10.48550/arXiv.2609.18739

### Authors

Toqeer Ehsan, Thamar Solorio

### Abstract

Poor quality or noisy annotations in Named Entity Recognition (NER), as in any other NLP task, make it challenging to achieve state-of-the-art performance. In this paper, we present a multi-step framework to enhance the annotation quality of NER datasets by employing automated techniques. We propose a frequency-based iterative approach that leverages self-training and a dual-threshold mechanism to enhance inference confidence. Experimental evaluations on different NER datasets demonstrate significant improvements in NER performance with respect to the original datasets. This work further explores the potential of generative Large Language Models (LLMs) to perform NER for low-resource languages.

### 中文一句话结论
本文提出了一种可扩展的自动化多步骤框架，通过基于频率的迭代自训练和双阈值机制，显著提升了低资源语言（乌尔都语、沙穆基语、信德语）命名实体识别（NER）数据集的标注质量，在三个数据集上分别将微调后的XLM-RoBERTa-large模型的micro F1分数提高了3.96、1.4和1.44个百分点。

### English TL;DR
This paper presents a scalable multi-step framework for correcting noisy NER annotations in low-resource languages, using frequency-based iterative self-training with a dual-threshold mechanism (probability and attention-based) and LLM-assisted word segmentation. Experiments show significant micro F1 improvements (3.96, 1.4, 1.44) on Urdu, Shahmukhi, and Sindhi datasets over original versions, achieving higher entity recall and annotation completeness.

### 中文详细总结
该工作针对低资源语言NER数据集中普遍存在的标注缺失和词分割错误问题，提出了一套完整的自动化修正流水线。研究基于三个语言相关的低资源数据集（MK-PUCIT乌尔都语、Shahmukhi西旁遮普语、SiNER信德语），其共有的特点是在大量句子中实体标注不全，且存在字符分割不一致（如"Karachi"被错误分割），严重制约了监督模型的性能。作者首先利用ChatGPT-4o进行few-shot词边界修正，将CoNLL格式转为内联标注格式以保持实体标签不变；随后通过上下文无关的实体增强（基于频率提取实体词典，最小频率阈值为3）填补缺失标注，并在验证集上评估选择最优版本。核心方法是一种频率迭代自训练：每轮用当前标注子集微调模型，对完整训练集推理以提出缺失实体，再通过双阈值（概率阈值τ_p和注意力动态阈值τ_a，后者基于注意力矩阵对角线得分的动态计算）过滤低置信度预测，减少错误传播。最终，修正后的数据集在micro F1上分别提升3.96（MK-PUCIT）、1.4（Shahmukhi）和1.44（SiNER）个百分点。

### 方法 / 贡献
主要贡献包括：1）提出频率迭代自训练机制，结合概率和注意力双阈值，有效纠正缺失标注错误；2）证明因果LLM（如ChatGPT-4o）能通过few-shot词分割修正和内联NER标注，提升非英语数据集质量；3）提供对低资源语言NER中因果LLM潜力的见解，采用内联标注方法；4）为三个数据集构建了准确的验证集和测试集，确保评估无偏可靠。方法流程包括：词分割修正、上下文无关实体增强、迭代自训练（含双阈值过滤），以及用多语言验证模型基于F1选择最佳候选标注。

### 实验或数据
论文使用了三个NER数据集：MK-PUCIT（乌尔都语，24,080句，原始35,631个实体，修正后44,510个，总实体增加19.9%）、Shahmukhi（西旁遮普语，13,412句，原始6,987个，修正后7,536个，增加7.3%）、SiNER（信德语，具体统计未在预览中完整显示）。实验采用XLM-RoBERTa-large作为骨干模型进行微调评估。结果显示，修正后的数据集在所有三个语言上均有一致的性能提升：micro F1分别提升3.96、1.4和1.44个百分点。具体实体类型方面，MK-PUCIT的ORG提升最大（39.1%），而Shahmukhi的PER提升较小（2.6%）。论文未提供完整的测试集数字，仅报告了相对原始数据集的改进幅度。数据集统计中显示了词分割错误对tokenization的影响示例（原始21个token vs 修正后17个token）。

### 值得关注点
该工作的亮点在于：1）针对低资源语言NER数据集的自动化修正，避免了昂贵的人工重标注，特别适用于缺乏专家和外部资源（如Wikipedia）的语言；2）双阈值机制（logits概率+自注意力动态阈值）能有效控制伪标签传播风险，而非简单采用最大概率；3）将LLM用于非英语低资源语言的词分割修正，展示了因果LLM在该场景下的实用性，而不仅仅是生成或翻译任务；4）频率提取实体词典进行上下文无关增强，利用了数据集中共享的实体类型（PER、LOC、ORG）的频率统计，实现了对缺失标注的估计性填补。

### 局限性
论文的主要局限包括：1）依赖ChatGPT-4o等商业API进行词分割修正，需要API成本且对提示工程敏感，这可能限制其在资源受限场景下的可复制性；2）频率迭代自训练需要多次模型微调和推理，计算开销较大（每次迭代需重新微调XLM-RoBERTa-large）；3）双阈值机制中的注意力阈值τ_a需要动态计算，其稳定性和泛化性未在论文中深入分析；4）实验仅覆盖三个文化地理上相关的南亚语言（乌尔都语、西旁遮普语、信德语），框架在其他低资源语系（如非洲或东南亚语言）上的适用性未验证，因为实体类型分布和分割规则可能差异较大；5）未与人工修订结果进行对比实验，无法判断最终数据集距离“完美标注”的绝对质量差距；6）LLM辅助方法仍需手动设计提示和验证提示输出，未完全消除人工参与。

## 2. WordPolo: Evaluating Language Models Through Iterative Semantic Feedback

- Source: arxiv
- arXiv ID: 2609.19006
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.19006v1
- PDF: https://arxiv.org/pdf/2609.19006v1
- DOI: https://doi.org/10.48550/arXiv.2609.19006

### Authors

Tyler McDonald, Ali Emami

### Abstract

Large Language Models (LLMs) and Large Reasoning Models (LRMs) are typically evaluated on challenging benchmarks through dataset accuracy alone, providing no insight into the quality or faithfulness of their reasoning processes. We present WordPolo, a word-finding task where participants must discover an unknown target word using semantic similarity feedback. Players start with zero knowledge, make guesses, and receive distance scores (1 = correct, higher = further away). Success requires interpreting scores to navigate semantic space and systematically narrow the search. This design makes iterative reasoning and adaptive search strategies both directly observable and necessary for success. We evaluate recent LLMs (GPT-4.1, Llama 4, Claude 3.5 Haiku, Qwen 3), LRMs (o4-mini, Deepseek-R1), humans, and a novel heuristic on 1,500 puzzles. Beyond solve rates (which range from 4% to 62%), we introduce progression-based metrics that reveal models often make meaningful progress, insights that accuracy alone would miss. Our analysis shows how reasoning models can be hindered by overthinking and underthinking, while successful models exhibit human-like strategies. WordPolo demonstrates the need for benchmarks that test both reasoning process and outcomes, providing holistic measurements of model capabilities. Our code and dataset can be found at https://wordpolo-demo.vercel.app/.

### 中文一句话结论
WordPolo 提出了一种基于迭代语义反馈的找词基准任务，揭示了仅靠准确率评估会遗漏推理质量的关键差异，并发现推理模型常因“过度思考”或“思考不足”而表现不佳。

### English TL;DR
WordPolo introduces a word-finding benchmark that requires iterative semantic feedback, showing that accuracy-only evaluations miss critical differences in reasoning quality and that reasoning models can suffer from overthinking and underthinking.

### 中文详细总结
WordPolo 是一种创新的语言模型评估任务，参与者需通过语义相似度反馈发现未知目标词。该任务要求模型在每步中解释反馈并调整策略，从而将推理过程直接可视化。在 1,500 个谜题上，LLM（如 GPT-4.1、Llama 4）和 LRM（如 o4-mini、Deepseek-R1）的解决率差异显著（4%–62%）。引入的进度指标表明，低准确率模型有时比高准确率模型进步更大，而推理模型常因过度思考或思考不足而落后。该基准强调过程感知评估的必要性。

### 方法 / 贡献
- **任务设计**：基于语义相似度反馈的找词游戏，每次猜测反馈秩次（1=正确，越大越远），强制迭代推理。
- **数据集**：1,500 个谜题（979 个公共档案 + 521 个 MsFit 词汇），使用 GloVe 嵌入（约 317,000 词表）。
- **启发式基线**：模拟人类策略，使用 top-k 猜测的加权质心加入噪声探索。
- **贡献**：引入进度得分（proximity）、平均进度（mean progression）和加权进度（weighted progression）指标；展示推理过程与结果并重；开源代码与数据集。

### 实验或数据
- 评估模型：GPT-4.1、Llama 4 Maverick、Claude 3.5 Haiku、Qwen 3（禁用推理）、o4-mini、Deepseek-R1、Qwen 3（启用推理）；另有人类和启发式基线。
- 数据规模：1,500 个谜题；每谜题 100 次猜测；无效猜测计入上限。
- 结果：解决率 4%–62%；进度指标显示低准确率模型可能进步更大；推理模型过度/不足思考导致欠佳。
- 数据集类别：WordNet 分类，覆盖 15 类（574/1,500 谜题已分类）。

### 值得关注点
- **过程可观测**：推理链通过猜测历史直接可见，无需逐步注释。
- **反直觉发现**：更多推理 token 不一定更好，o4-mini 在“teacher”谜题中需 80+ 猜测，而 GPT-4.1 和人类更高效。
- **指标创新**：对数尺度进度得分，区分接近解但未解的表现。
- **实用资源**：提供交互演示和启发式实现，便于复现。

### 局限性
- 任务局限于单词语义空间（GloVe），可能无法泛化到多词或抽象推理。
- 启发式基线依赖种子词和噪声参数（k=5, α=0.01），可能类别人为偏差。
- 人类评估仅 3 名志愿者，样本小。
- 未涵盖更广模型（如多模态或更大规模模型），且未讨论计算成本。
- 抽象数据未提及跨语言或可迁移性。

## 3. Knowledge-Graph Based Augmentation versus Retrieval Augmented Generation for Cultural-Related Question Answering

- Source: arxiv
- arXiv ID: 2609.18317
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.18317v1
- PDF: https://arxiv.org/pdf/2609.18317v1
- DOI: https://doi.org/10.48550/arXiv.2609.18317

### Authors

Pablo Poulenard, Yannis Karmim, Valentin Barrière

### Abstract

Large language models (LLMs) suffer from a long-tail deficit: culturally specific facts, particularly those concerning underrepresented regions such as Latin America, appear too rarely in pretraining corpora to be reliably memorized. Retrieval-Augmented Generation (RAG) addresses this by grounding generation in external text, but structured alternatives such as Knowledge Graphs (KGs) offer tighter control over what enters the context, along with potential gains in explainability and updatability. We benchmark Graph-RAG against standard RAG on LatamQA, a culturally grounded multiple-choice dataset spanning eight thematic categories. The graphs are built end-to-end from Wikipedia articles with KGGen, a recent open-domain extractor, without manual curation in our main setting. G-Retriever is competitive with RAG and reduces the error of the base LLM by 72\% with a standard KG and 78\% with a benchmark-aware variant, the gap to RAG narrowing further as the graph is oriented toward task-relevant content. The trained projection transfers zero-shot to Portuguese without target-language fine-tuning, indicating multilingual reach.

### 中文一句话结论
本文在拉丁文化问答数据集上对比了基于知识图谱（Graph-RAG）与检索增强生成（RAG），发现RAG整体准确率更高，但Graph-RAG（G-Retriever）可将基础大模型错误减少72%–78%，且在关系抽象和多语言零样本迁移方面具有优势。

### English TL;DR
This paper compares Graph-RAG against standard RAG for culturally specific question answering on the LatamQA dataset. While RAG achieves higher overall accuracy (93.38% vs. 89.71%), Graph-RAG with G-Retriever reduces base LLM errors by 72% (standard KG) to 78% (benchmark-aware KG) and shows competitive performance, especially in categories where relational abstraction helps. The trained projection transfers zero-shot to Portuguese without fine-tuning.

### 中文详细总结
- **问题**：大语言模型对拉丁美洲等文化特定事实存在长尾缺陷，检索增强生成（RAG）依赖外部文本，而知识图谱（KG）提供更紧凑、可解释的结构化替代。
- **方法**：使用KGGen从5,848篇西班牙语维基百科文章端到端构建8个主题类别的知识图谱，比较RAG、Top-k三元组（无结构）和G-Retriever（图结构+软提示）。所有方法基于Qwen2.5-3B和jina嵌入。
- **结果**：RAG全局准确率最高（93.38%），G-Retriever次之（89.71%），Top-k三元组（75.60%），零样本（60.17%）。G-Retriever在“Gastronomía”类别上超过RAG（93.04% vs. 87.37%）。标准KG和基准感知KG分别将错误减少72%和78%。
- **迁移**：西班牙语训练好的投影零样本迁移到葡萄牙语，无需目标语言微调。

### 方法 / 贡献
- **核心方法**：采用KGGen从维基百科抽取三元组，构建每个主题的单一KG；G-Retriever通过Prize-Collecting Steiner Tree提取子图，并用图变压器编码为软提示。
- **主要贡献**：（1）首次将KGGen大规模应用于下游问答（而非内部分数）；（2）系统对比RAG、Top-k三元组、G-Retriever；（3）消融实验分离图结构和提取质量的影响；（4）验证多语言零样本迁移。

### 实验或数据
- **数据集**：LatamQA（拉丁文化多项选择问答），覆盖8个主题（音乐、文学、电影等），共5,848题，每问题关联一篇维基百科文章，无需跨文章推理。
- **知识图谱**：每个主题一个KG（共336k节点、135k边），另有一个基准感知变体（注入问题相关实体/关系提示）。
- **对比设置**：零样本；RAG（k=5块）；Top-k三元组（余弦相似度筛选）；G-Retriever（训练图编码器/线性投影）。在5折交叉验证上报告准确率。

### 值得关注点
- **错误减少显著**：Graph-RAG将基础LLM错误降低72%–78%，表明即使整体不如RAG，仍能有效弥补参数知识不足。
- **关系抽象优势**：在“Gastronomía”等类别中，图结构过滤了密集检索噪声，超越RAG。
- **零样本迁移**：训练好的投影从西班牙语零样本迁移到葡萄牙语，显示多语言泛化潜力。
- **提取瓶颈**：基准感知KG（+1.7 pp）虽提升性能，但RAG仍更高，说明三元组提取质量是主要限制。

### 局限性
- **提取质量限制**：KGGen从原始文本抽取时存在信息损失，即便基准感知变体也无法完全达到RAG的准确率。
- **任务简单**：所有问题均为单跳（single-hop），无需跨文章推理，图结构优势未被充分体现（线性投影与图编码器性能相近）。
- **模型规模固定**：仅使用3B参数模型，未验证更大LLM或更强提取器的效果。
- **语言覆盖有限**：仅测试西班牙语和葡萄牙语，未涵盖其他低资源语言。

## 4. Preventing Model Collapse: A Fisher-Rao Perspective on the Dynamics of Training with Synthetic Data

- Source: arxiv
- arXiv ID: 2609.18878
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.18878v1
- PDF: https://arxiv.org/pdf/2609.18878v1
- DOI: https://doi.org/10.48550/arXiv.2609.18878

### Authors

Matteo Marchi, João Pedro Silvestre, Bahman Gharesifard, Paulo Tabuada

### Abstract

Large Language Models (LLMs) are now routinely trained using synthetic data, since high-quality human data has been exhausted by the ever increasing needs of larger and larger models. However, recursive training on synthetic data frequently induces model collapse, a degenerative feedback loop where models progressively forget the true underlying data distribution. Training on a mixture of synthetic and fresh human data is a logical countermeasure and can prevent model collapse. However, it is an open question as to what is the exact minimum required ratio of human-to-synthetic data to maintain training stability. In this paper, we establish rigorous theoretical guarantees on the minimum rate of human data required to prevent model collapse. Although previous work established a formal lower bound for this ratio, such bound can be vacuous for very high dimensions, as the analysis relies on the usual Euclidean metric in R^n and is not adapted to the space of categorical probability distributions. Instead, in this paper we explicitly leverage the information-geometric structure of the probability simplex by analyzing the dynamics of the process under the Fisher-Rao metric. We derive quantitative contraction and invariance bounds that are stable and do not become trivial as the dimensions increase. Thus, we show that the effective required data ratio to prevent model collapse is different than previously implied.

### 中文一句话结论
本文利用Fisher-Rao度量从信息几何角度分析合成数据训练大语言模型时的模型坍塌问题，证明防止模型坍塌所需的最低人类数据比例比先前基于欧几里得度量的估计更高。

### English TL;DR
This paper uses the Fisher-Rao metric from information geometry to analyze model collapse during LLM training with synthetic data, establishing rigorous theoretical guarantees that the minimum human-to-synthetic data ratio required to prevent collapse is higher than previous Euclidean-based estimates, with bounds that remain non-vacuous in high dimensions.

### 中文详细总结
论文研究大语言模型使用合成数据进行递归训练时发生的模型坍塌问题。作者建立了一个严格的数学框架，将生成模型的迭代训练建模为封闭随机过程，并分析混合人类数据和合成数据训练时的动态特性。关键创新在于采用Fisher-Rao度量而不是传统的欧几里得度量来分析概率单形上的动态过程，因为欧几里得度量在高维空间中会导致无意义的边界。通过Fisher-Rao度量，作者推导出稳定的量化收缩和不变性边界，这些边界不会随维度增加而变得平凡。结果表明，防止模型坍塌所需的人类数据比例高于先前文献的估计。

### 方法 / 贡献
- 提出将生成模型迭代训练建模为封闭随机过程的数学框架
- 利用Fisher-Rao度量分析概率单形上的几何结构，取代先前不适用于概率分布的欧几里得度量
- 推导出稳定的量化收缩和不变性边界，在高维空间中仍保持有意义
- 严格证明防止模型坍塌所需最低人类数据比例的新理论下界

### 实验或数据
论文主要提供理论分析，未提及具体实验或数据集。

### 值得关注点
- 首次从信息几何角度严格分析模型坍塌问题，方法新颖
- 解决了先前欧几里得度量分析在高维时边界失效的问题
- 证明所需人类数据比例高于先前估计，对实际训练策略有重要指导意义

### 局限性
- 论文为纯理论分析，缺少实证验证
- 假设人类数据来自固定的外部分布，可能不完全符合实际场景
- 温度函数采用标准softmax形式，未考虑其他可能的调制方式
- 理论模型简化了实际训练过程的复杂性（如数据筛选、模型架构等）

## 5. Register Bias in Complexity-Based Large Language Model Routing

- Source: arxiv
- arXiv ID: 2609.17542
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.17542v1
- PDF: https://arxiv.org/pdf/2609.17542v1
- DOI: https://doi.org/10.48550/arXiv.2609.17542

### Authors

Simran Koul

### Abstract

Large language model services increasingly route each query to one of several models of differing capability, using a cheap estimate of query complexity to send easy queries to small models and hard queries to large ones. I show that this routing step is not register neutral: text written in a non-standard English register, African American English or the English of second-language writers, is systematically assigned a lower-capacity tier than a meaning-equivalent standard-English version of the same query. The effect is driven by a specific, common routing signal, input length, because non-standard registers omit function words and thus look shorter and therefore simpler; other complexity signals do not carry it. I demonstrate the disparity on 37,704 authentic learner sentence pairs and on a controlled parallel corpus. I then measure the quality consequence on a device, edge, and cloud model ladder and find that the harm is driven by pervasive model bias, every tier, including a frontier cloud model, answers non-standard-register queries significantly less accurately, while the marginal quality cost of the routing decision itself is not significant on this benchmark. Complexity-based routing thus compounds the exposure of the users that the models already serve worst.

### 中文一句话结论
基于输入长度的复杂度路由会系统性将非标准英语（如非洲裔美国英语、二语学习者英语）查询分配到更弱的小模型，而所有模型（包括前沿云模型）对这些查询的准确率已经较低，路由环节进一步加剧了用户的不公平暴露。

### English TL;DR
Complexity-based LLM routing, particularly when using input length, systematically assigns non-standard English queries to weaker model tiers, compounding the already lower accuracy that all tiers—including frontier models—exhibit for those registers.

### 中文详细总结
论文审计了基于复杂度的LLM路由在语言学语域（register）上的公平性。作者发现，当使用最常见的路由信号——输入长度（token数量）时，非标准英语（非洲裔美国英语、二语学习者英语）的查询比含义等价的标准英语版本更短（因省略功能词），从而被路由到更低能力等级的小模型上。该效应在37,704个真实学习者句子对及一个受控平行语料库（279个问题，经语义等价性筛选）中均显著。其他复杂度信号（如可读性指标、句法深度）不呈现此系统性偏差，甚至有时相反。在设备（1B）、边缘（8B）和云（Claude Opus）三级模型上评估质量发现：模型本身对所有层层级都有显著的语域偏见，即使是前沿云模型对非标准英语回答准确率也显著更低；但路由决策本身带来的边际质量损失在此基准上不显著。结论：基于长度的复杂度路由将模型已服务最差的用户进一步导向弱模型，加剧了不公平。

### 方法 / 贡献
1. **首次审计**：证明了基于复杂度的LLM路由器会根据语域对含义等价查询分配不同能力等级，使用真实文本（37,704学习者对）和受控平行语料。
2. **分解不同复杂度信号**：令牌长度稳健地携带偏差，而可读性和句法深度信号不携带甚至反转。
3. **机制说明**：非标准语域省略功能词导致文本变短，长度路由将更短视为更简单。
4. **质量分解**：将模型固有偏差与路由引起的损害分开，发现前沿云模型对非标准语域显著不准确，而路由本身边际成本不显著（诚实报告为零结果）。

### 实验或数据
- **真实学习者语料**：W&I+LOCNESS语料库，37,704个学习者原句与标准英语修正句的配对。
- **受控平行语料**：从Natural Questions选取300问题，用Multi-VALUE转换为非洲裔美国英语和印度英语变体，经Claude Opus语义等价筛选后保留279问题。
- **模型阶梯**：Llama 3.2 1B（设备端）、Llama 3.1 8B（边缘）、Claude Opus（云端）。
- **质量评估**：基于事实包含性的评分（与参考答案比较），评分器非路由模型，无语域偏差。

### 值得关注点
- 路由偏差仅由输入长度驱动，其他复杂度信号不表现出系统性向下路由；可读性指标甚至反向（非标准英语看起来更复杂）。
- 模型固有偏差随能力增强而增强：前沿云模型对非标准英语准确率下降最显著（标准英语60.2% vs. AAE 52.3% vs. 印度英语48.4%，p<0.001）。
- 路由决策本身的质量损失不显著（由于Natural Questions问题短且长度均匀，路由边界紧），但偏差叠加模型偏见造成双重伤害。
- 实际部署验证：在Samsung Galaxy S25+上运行Llama 3.2 1B，速度29.1 tokens/s，答案与服务器端一致，证明弱模型可在手机上运行。

### 局限性
- 比率依赖工作负载，鲁棒结论是方向与机制，非精确百分比。
- 受控语域变体由规则转换产生（已披露），真实性依赖W&I+LOCNESS臂。
- 可读性和句法深度在短单句上噪声大，长度结果可信。
- 路由引起的质量损失（Path A）在短问题基准上为零结果，需要长度变化更大的工作负载来验证是否基准特定。

## 6. Size Matters: Foundation Model for Czech HTML documents

- Source: arxiv
- arXiv ID: 2609.18494
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.18494v1
- PDF: https://arxiv.org/pdf/2609.18494v1
- DOI: https://doi.org/10.48550/arXiv.2609.18494

### Authors

Martin Dvořák, Vít Tlustoš, Artyom Voronin, Martin Habrovec, Kateřina Podlesná, Barbora Rišová, Josef Vonášek

### Abstract

Creating universal, high-quality representations of web documents in high-traffic industrial environments requires models that are both performant and economic. Existing approaches, however, often depend on large models, overlook the structural information inherent in HTML, or are constrained by short context windows, limiting their ability to process real-world web pages. We present HTML-LM, a compact foundation model with 154 million parameters that addresses these limitations through HTML-aware training and a ModernBERT-based architecture. It was trained on 100 million web documents using multiple objectives, including masked language modeling, bag-of-words prediction, and contrastive distillation from large language models. Consequently, HTML-LM sets a new state-of-the-art for classification and regression applications in the Czech Internet domain, surpassing both larger encoders and small-sized LLMs. The model is deployed in production, processing thousands of web documents per second, and released to the community under the CC BY-NC 4.0. https://huggingface.co/Seznam/html-lm.

### 中文一句话结论
HTML-LM 是一个仅 1.54 亿参数的紧凑型 HTML 感知基础模型，在捷克语网页分类与回归任务上达到了最先进水平，并已部署于工业级生产环境。

### English TL;DR
HTML-LM is a compact 154M-parameter HTML-aware foundation model based on ModernBERT that achieves state-of-the-art performance on Czech web document classification and regression tasks through multi-objective training (including MLM, bag-of-words prediction, and teacher-guided contrastive distillation) while being efficient enough for production deployment at scale.

### 中文详细总结
HTML-LM 由 Seznam.cz 团队提出，专为工业级捷克语网页理解设计。模型采用 ModernBERT 架构并支持 8192 令牌的上下文窗口，能够处理完整网页内容。其独到之处在于：

- **HTML 感知设计**：通过专用分词器（包含 100 个高频 HTML 标签对应的特殊令牌）和 DOM 精简预处理，保留了网页的结构信息。
- **多目标训练**：同时使用掩码语言建模（MLM）、词袋预测（BOW）和大语言模型（Qwen3-Embedding-8B 和 SeLLMa 8B）的对比蒸馏，从不同粒度学习文档表示。
- **工业级效率**：仅 1.54 亿参数，每秒可处理数千篇文档，已投入生产。
- **性能领先**：在文章类别、Curlie 分类、色情内容识别、商品页面识别和网页垃圾评分等五个下游任务上，全面超越规模更大的编码器和小型 LLM。

### 方法 / 贡献
- **模型架构**：基于 ModernBERT 的 22 层 Transformer，隐藏层维度 768，12 个注意力头。
- **定制分词器**：57K 词汇的 WordPiece 分词器，包含 100 个高频 HTML 标签的特殊令牌，经优化后在 8K 上下文窗口内覆盖 94.8% 的文档。
- **多目标训练**：MLM 学习令牌级语义，BOW 迫使 [CLS] 表示捕捉全局信息，对比蒸馏从教师模型（Qwen3 Embedding 8B 和 SeLLMa 8B）提炼知识。
- **加权汇聚策略**：使用随机权重（α ~ U(0,1)）动态平衡不同损失项，提升泛化能力。
- **生产级部署**：模型已在 Seznam.cz 搜索中上线，并开源（CC BY-NC 4.0）。

### 实验或数据
- **训练数据**：1 亿篇捷克语 HTML 文档，涵盖搜索索引、Curlie 目录、禁令域名等来源。
- **评估设置**：保持模型冻结，仅训练轻量 MLP Head（~0.3-1M 参数）。在五个下游任务上比较：
  - 文章类型（F1 macro）、Curlie 分类（Accuracy）、色情识别（F1 macro）、商品识别（F1 macro）、网页垃圾（RMSE）。
- **性能亮点**：HTML-LM 在所有任务上超越 Jina-embeddings-v3、OpenAI text-embeddings-3、Qwen3-Embedding-8B、SeLLMa 8B、RetroMAE 等基线，尽管参数规模小数十倍。

### 值得关注点
- **小模型大效果**：1.54 亿参数即达到甚至超越 8B 级别 LLM，表明针对特定领域（捷克语+HTML）的紧凑模型可以兼顾性能与效率。
- **HTML 结构利用**：不同于纯文本模型，通过 DOM 精简和标签令牌显式编码 HTML 结构，并通过消融实验验证其必要性（上下文窗口 ≥2048 令牌）。
- **生产就绪**：已部署于真实搜索引擎，每秒处理数千文档，工业实用性得到验证。
- **开源释出**：模型权重和代码可在 HuggingFace 获取，有利于后续研究和应用。

### 局限性
- **语言限制**：模型专门针对捷克语优化，在其他语言上的泛化能力未经验证。
- **非商业许可证**：采用 CC BY-NC 4.0 许可证，限制商业用途。
- **输入格式要求**：需要原始 HTML 输入，对于纯文本或非 HTML 文档不适用。
- **未报告长尾场景**：训练数据仅覆盖 1 亿篇文档，对于极端稀疏类别或罕见网页模板的效果未讨论。

## 7. DANTINOX: A Unified Framework for Multi-Paradigm Language Modeling

- Source: arxiv
- arXiv ID: 2609.17535
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.17535v1
- PDF: https://arxiv.org/pdf/2609.17535v1
- DOI: https://doi.org/10.48550/arXiv.2609.17535

### Authors

Marco Simoni, Aleksandar Fontana, Giulio Rossolini, Andrea Saracino

### Abstract

Language generation research increasingly spans three paradigms: autoregressive decoding, discrete masked diffusion, and continuous flow-matching. Comparing them is difficult because each lives in a separate codebase, so measured differences often reflect implementation details rather than the paradigms themselves. We present DantinoX, an open-source JAX/Flax library in which a single modular Transformer backbone serves all three paradigms. Switching the generation paradigm, attention mechanism, or hardware topology requires only a configuration change, while the backbone architecture, tokenizer, initialization strategy, and training infrastructure remain consistent. This enables controlled cross-paradigm comparisons within one API for training, streaming inference, and benchmarking.

### 中文一句话结论
DANTINOX 是一个开源的 JAX/Flax 库，通过统一的模块化 Transformer 骨干网络支持自回归、离散掩码扩散和连续流匹配三种生成范式，仅需配置更改即可切换，旨在实现受控的跨范式比较。

### English TL;DR
DANTINOX is an open-source JAX/Flax library unifying autoregressive, discrete masked diffusion, and continuous flow-matching language modeling on a single modular Transformer backbone to enable controlled cross-paradigm comparisons.

### 中文详细总结
本文提出 DANTINOX，一个基于 JAX/Flax 的统一框架，解决语言生成中三种范式（自回归、离散掩码扩散、连续流匹配）比较困难的问题。现有框架如 HuggingFace、MaxText、dLLM 等往往只支持单一范式或缺乏统一的骨干网络，导致测量差异常源于实现细节。DANTINOX 通过将模型骨干与生成方法解耦，支持在同一 API 下训练、推理和评估，并集成了多种注意力机制（MHA、GQA、MLA）、FFN 变体（dense、MoE、LatentMoE）、位置编码和 LoRA 适配器，且支持多 GPU 扩展。该库还提供基准测试套件，确保公平对比。

### 方法 / 贡献
- **统一骨干网络**：采用预归一化 Transformer，可配置注意力（MHA/GQA/MLA）、FFN、位置编码等，支持因果或双向注意。
- **范式切换**：通过单一配置切换 AR、离散扩散、连续流匹配，无需修改核心代码。
- **基础设施**：集成 LoRA、权重绑定、FlashAttention、滑动窗口等，支持数据/张量并行和多 GPU 训练。
- **开源**：MIT 许可，通过 pip 安装，代码、文档、演示视频公开。

### 实验或数据
摘要和部分内容未提供具体实验数据或数据集详情；但提到使用三套评估：跨代码库实现交叉检查、生成质量（MAUVE、困惑度、多样性、条件 BLEU）以及推理延迟、吞吐量和能耗的硬件分析，但未给出具体数值或数据集名称。

### 值得关注点
- 首次在单一骨干上统一三种范式，显著降低跨范式比较的偏差。
- 强调模块化和配置驱动，便于消融研究和教育用途。
- 对小型企业和实践者友好，减少重复基础设施搭建。

### 局限性
- 摘要未报告具体实验数据或基准结果，仅描述评估计划。
- 未讨论训练成本、参数量或大规模部署的详细性能。
- 支持范式虽全，但未提及对长上下文或极端资源场景的优化细节。

## 8. SFT or RL for Tool-Calling Agents? A Controlled Study Across Data, Method, and Scale

- Source: arxiv
- arXiv ID: 2609.17848
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.17848v1
- PDF: https://arxiv.org/pdf/2609.17848v1
- DOI: https://doi.org/10.48550/arXiv.2609.17848

### Authors

Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN

### Abstract

Limited controlled evidence exists on how training data, adaptation method, and model scale jointly affect tool-calling performance in language-model agents. We evaluate supervised fine-tuning (SFT) with LoRA, reinforcement learning (RL) via Group Relative Policy Optimization (GRPO), and SFT followed by GRPO across six Qwen3 models from 0.6B to 32B parameters, covering both in-distribution performance and cross-dataset transfer. SFT with LoRA is the strongest in-distribution method throughout the 0.6B-32B range and best in 15 out of 18 experimental settings. On cross-dataset transfer, the methods are closer: GRPO wins 29 out of 54 settings where training and test datasets differ, but its margin over SFT averages under one point, and SFT->GRPO is rarely strongest in either comparison. Dataset mixing gives consistently strong transfer while staying close to specialized in-distribution training, regardless of method. Additional analysis further confirms that LoRA outperforms full-parameter fine-tuning, demonstrating that LoRA better preserves pretrained agentic behavior.

### 中文一句话结论
对于工具调用代理，使用LoRA的监督微调（SFT）在分布内性能上最可靠，而强化学习（GRPO）在跨数据集迁移中仅有微弱优势，数据集混合是稳健的默认选择。

### English TL;DR
SFT with LoRA is the most reliable in-distribution method for tool-calling agents across model scales 0.6B–32B, while GRPO offers only a modest edge in cross-dataset transfer, and dataset mixing provides the strongest deployment default.

### 中文详细总结
本研究系统比较了监督微调（SFT with LoRA）、强化学习（GRPO）和SFT接GRPO三种方法在工具调用代理上的表现，使用Qwen3系列模型（0.6B至32B参数）和三个公开数据集（xLAM/APIGen、ToolACE、Glaive-FC-v2）及其均匀混合。主要发现：1）SFT with LoRA在分布内性能上最佳，18个设置中赢得15个；2）GRPO在跨数据集迁移中胜率较高（54个设置中29个），但平均优势不到1个百分点；3）SFT->GRPO很少是最优策略；4）数据集混合提供最强且一致的迁移性能，且接近最专业的分布内训练。此外，LoRA优于全参数微调，说明LoRA更能保留预训练的工具使用能力。

### 方法 / 贡献
- **方法**：使用LoRA进行SFT，使用GRPO进行RL，以及顺序组合SFT->GRPO。所有数据集统一格式并去除近重复样本，确保公平比较。SFT->GRPO将训练数据等分且不重复用于两阶段。
- **贡献**：首个系统性的受控比较，覆盖**数据、方法和模型规模**三个维度；揭示SFT在分布内始终优于RL，而RL在迁移中略有优势；证明数据集混合是稳健的默认选择；发现LoRA比全参数微调更有效。

### 实验或数据
- **模型**：Qwen3的六个规模（0.6B、1.7B、4B、8B、14B、32B）。
- **训练数据**：xLAM/APIGen（56,443样本）、ToolACE（9,715）、Glaive-FC-v2（46,204）及其均匀混合。测试集为各数据集的保留部分。
- **评估指标**：精确匹配准确率（exact-match accuracy）。
- 覆盖**18个分布内设置**和**54个跨数据集迁移设置**。

### 值得关注点
- SFT with LoRA在所有模型规模上分布内性能一致最好，但GRPO在迁移中略优，这一点提示不同使用场景下方法选择的重要性。
- 数据集混合策略在未知测试分布时表现稳健，优于大部分单一数据集训练，适合作为默认部署选择。
- LoRA优于全参数微调，表明低秩适配能更好地保留预训练的工具使用能力。

### 局限性
- 仅使用Qwen3系列模型和三个公开数据集，未涵盖其他模型家族或更丰富的工具调用场景。
- RL方法仅采用GRPO，未探索其他强化学习算法（如PPO、R1等）。
- 跨数据集迁移的改进幅度很小（平均不到1个百分点），实际意义有限。
- 论文未明确讨论其他潜在局限性（如计算成本、数据噪声影响等）。

## 9. From Pixels to Pairs: A Comprehensive Benchmark of LLM-Based Key-Value Extraction in Noisy Document Settings

- Source: arxiv
- arXiv ID: 2609.17538
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.17538v1
- PDF: https://arxiv.org/pdf/2609.17538v1
- DOI: https://doi.org/10.48550/arXiv.2609.17538

### Authors

Zahra Anvari, Vassilis Athitsos

### Abstract

Large language models (LLMs) are increasingly used for structured information extraction from documents, yet their behavior under realistic OCR noise remains poorly understood. We present a systematic benchmark of open-source instruction-tuned LLMs for key-value pair (KVP) extraction under both clean-text and noisy OCR conditions.
  We evaluate representative decoder-only models (Gemma, Mistral, Qwen2.5, LLaMA 3, and DeepSeek) on the FUNSD, CORD, and SROIE benchmarks using both Gold-text annotations and OCR outputs from PaddleOCR, EasyOCR, and Tesseract. A unified evaluation protocol isolates the effects of input quality, model design, and prompting under consistent conditions.
  The results show that modern LLMs act as strong semantic extractors when high-quality text is available, in some cases approaching supervised layout-aware systems. Under OCR noise, however, performance degrades substantially and performance gaps between models narrow as input corruption increases.
  Across all datasets, extraction performance is governed by two factors: semantic reasoning over text and preservation of textual fidelity under OCR noise. While larger models improve results on clean text, these gains diminish under noisy inputs, where OCR quality becomes the dominant factor. We also identify recurring failure modes, including key-value misalignment, hallucination, and numeric corruption. Our findings highlight the gap between clean-text evaluation and real-world deployment, emphasizing the need to jointly improve OCR quality, structural reasoning, and LLM-based semantic modeling.

### 中文一句话结论
本文系统评测了开源指令微调大语言模型在干净文本和真实OCR噪声下的键值对提取性能，发现模型在高质量文本下表现良好，但OCR噪声会显著降低性能，且模型间的差距随噪声增大而缩小。

### English TL;DR
This paper systematically benchmarks open-source instruction-tuned LLMs for key-value pair extraction under clean and noisy OCR conditions, finding that while models perform well on clean text, performance degrades substantially under OCR noise where upstream text quality becomes the dominant factor.

### 中文详细总结
本文针对大语言模型在文档键值对提取中的应用，构建了一个受控基准测试。作者评估了五种开源指令微调解码器模型（Gemma、Mistral、Qwen2.5、LLaMA 3和DeepSeek）在三个文档基准（FUNSD、CORD、SROIE）上的表现，输入包括干净文本标注（Gold-text）以及三种OCR引擎（PaddleOCR、EasyOCR、Tesseract）的输出。统一的评估协议消除了提示策略和输出后处理的差异。

实验表明，在干净文本条件下，现代LLM能够作为强大的语义提取器，甚至在某些情况下接近有监督的布局感知系统。然而，在OCR噪声下，性能显著下降，且模型间的性能差距随输入质量恶化而缩小。提取性能受两个因素支配：文本的语义推理能力和OCR噪声下的文本保真度。模型规模扩大在干净文本上有提升，但在噪声输入下收益递减，此时OCR质量成为主导因素。此外，文中识别了常见的失败模式：键值对齐错误、幻觉和数字损坏。

### 方法 / 贡献
- 提出了一个受控基准，用于评估开源指令微调LLM在干净文本和OCR输入下的文本型键值对提取任务。
- 在多个LLM、多种文档类型（FUNSD、SROIE、CORD）和多个OCR引擎上进行了全面的实证研究，并使用统一的评估协议。
- 引入了标准化的评估协议，包括确定性解码和非语义输出规范化，确保不同模型和提示策略之间的公平且可重复的比较。
- 详细分析了OCR质量、文档结构、提示策略和模型规模的影响，并识别了限制文本型LLM文档提取的主要失败模式。
- 提供了一个可复现的评估框架，供未来LLM文档理解研究使用。

### 实验或数据
实验使用了三个标准文档数据集：FUNSD（表格）、CORD（收据）、SROIE（收据）。输入包括干净文本标注（Gold-text）以及从PaddleOCR、EasyOCR和Tesseract三个OCR引擎得到的输出。评估指标包括Key Recall、Exact Match (EM)和Value-level F1。模型使用统一提示框架和确定性解码，所有输出经过非语义规范化处理。实验涵盖了零样本和少样本提示场景。

### 值得关注点
- LLM在干净文本条件下表现接近有监督布局感知系统，但实际部署中OCR噪声会导致性能显著下降。
- 模型规模扩大在干净文本上有收益，但在噪声输入下收益消失，表明上游文本质量比模型能力更关键。
- 常见的失败模式（键值错位、幻觉、数字损坏）在OCR噪声下被放大，提示设计和模型结构无法完全弥补。
- 研究强调了干净文本评测与现实部署之间的差距，呼吁联合改进OCR质量、结构推理和LLM语义建模。

### 局限性
- 仅评估了文本型LLM，未包括多模态或布局感知模型（如LayoutLM、Donut等）。
- OCR引擎的选择限于三种通用工具，未涵盖所有工业级OCR系统。
- 文档类型仅包含表格和收据，未涉及更复杂的文档（如长文档、多页文档）。
- 提示策略只考察了零样本和少样本，未探索更复杂的设计（如思维链或任务分解）。
- 输出规范化完全基于非语义规则，可能丢失部分语义正确的变体。

## 10. SEA-LION-v4.8: A Technical Report

- Source: arxiv
- arXiv ID: 2609.18310
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.18310v1
- PDF: https://arxiv.org/pdf/2609.18310v1
- DOI: https://doi.org/10.48550/arXiv.2609.18310

### Authors

Ahmed Mohammad Dabeer, Ahn Jeongmi, Anocha Sutaveephamochanon, Antonyrex Sajeban, Aulia Adila, Chan Hok Teng, Adwin, Cheng Zi Yi, Nicholas Zhuang Ziyi, Choa Hsueh Mei Esther, David Ong Tat-Wee, Evelyn Tan Chor Phin, Heng Cheng Peng, Jonathan, Lee Chwan Ren, Leong Wai Yi, Leong Wei Qi, Leslie Teo Eng Sipp, Liew Rachel, Limkonchotiwat Peerat, Montalan Jann Railey Estrada, Muhammad Ridzuan Bin Mokhtar, Nagarajan Karthik, Ng Boon Cheong, Raymond, Ngui Jian Gang, Nguyen Thanh Ngan, Tasawong Panuthep, Pereira Mark Gregory, Phang Shi Wei Benjamin, Poon Yip Hung, Joseph, Rengarajan Hamsawardhini, Siow Wei Kang Bryan, Tai Ngee Chia, Tan Choon Meng, Tan Le Min, Sheryl, Tan Siao Wei, Tan Yi Xian, Tee Jun Yun, Teng Kok Wai, Tjhi William Chandra, Tuchinda Pume, Wu Donghang, Yong Xianbin, Yosephine, Zhang Zhou

### Abstract

We introduce Nemotron-SEA-LION-v4.8, a family of Southeast Asian Languages in One Network (SEA-LION) built upon NVIDIA Nemotron 3. The family includes 30B-A3B and 120B-A12B models, with both continued-pretrained base checkpoints and post-trained variants. We adapt the models using Southeast Asian, reasoning, code, and multilingual parallel datasets, followed by post-training with supervised fine-tuning and online on-policy distillation. On SEA-HELM, the 30B-A3B model improves the overall SEA score from 46.06 to 51.57, while the 120B-A12B model improves from 49.30 to 63.44. The strongest gains are observed in instruction following, natural language reasoning, and natural language understanding across seven Southeast Asian languages.

### 中文一句话结论
SEA-LION-v4.8 基于 NVIDIA Nemotron 3，通过继续预训练和在线同策略蒸馏，显著提升了七个东南亚语言在 SEA-HELM 上的综合得分（最高提升 14.14 分）。

### English TL;DR
SEA-LION-v4.8 introduces a family of Nemotron 3-based models (30B-A3B and 120B-A12B) fine-tuned via continued pre-training and online on-policy distillation, achieving substantial gains on SEA-HELM across seven Southeast Asian languages, with overall scores improving by up to 14.14 points.

### 中文详细总结
SEA-LION-v4.8 是新加坡 AI 研究院推出的新一代东南亚语言模型家族，基于 NVIDIA Nemotron 3 架构。模型包括 30B-A3B 和 120B-A12B 两个规模，每个规模均提供继续预训练基座和后训练版本。继续预训练使用 150B 高质量 token（侧重东南亚语言、推理、代码和多语言平行数据），后训练采用在线同策略蒸馏（OPD）结合监督微调。在更新后的 SEA-HELM 评测中，30B-A3B 模型综合得分从 46.06 提升至 51.57，120B-A12B 模型从 49.30 提升至 63.44，指令遵循、自然语言推理和理解能力提升最为显著，其中泰米尔语和缅甸语改进最大。

### 方法 / 贡献
- 基于 Nemotron 3 进行继续预训练：使用 150B token（30B 模型）和 33.5B token（120B 模型），数据涵盖东南亚语言指令、推理、代码和多语言平行语料。
- 采用在线同策略蒸馏（OPD）进行后训练：模型在异构任务环境中持续生成交互并从当前行为中学习，结合静态指令数据与在线轨迹。
- 发布四个开源模型：两个基座和两个后训练版本，覆盖 30B-A3B 和 120B-A12B 两种规模，均支持 128K 上下文（基础架构支持 1M）。

### 实验或数据
- 评测使用 SEA-HELM（更新后的版本），覆盖七个东南亚语言。
- 未在摘要中详细描述其他实验或独立数据集；报告包含多个语言的具体得分对比图。
- 30B 模型使用 Megatron Bridge 训练，120B 模型使用 NVIDIA NeMo AutoModel 训练，保留原始 tokenizer。

### 值得关注点
- 继续预训练和后训练相结合的方法优于仅规模扩展，验证了针对区域语言适配的有效性。
- 120B-A12B 模型在泰米尔语和缅甸语上的提升最为显著。
- 所有模型以开放权重发布，支持研究社区复现和应用。

### 局限性
- 摘要及预览未明确讨论局限性，可能存在的问题包括：不同东南亚语言间的性能差异仍可能较大；继续预训练数据量（150B token）相对于基础模型训练量较小，但对长尾语言的覆盖可能有限；后训练依赖特定任务交互环境，跨领域泛化能力待进一步验证。

## Processing Notes

- Duplicate papers skipped: 0