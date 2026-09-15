# Daily arXiv - 2026-09-15

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-15T02:27:52
- Paper count: 10

## 1. LLM-Enhanced Dual-Branch Learning for Large-Scale Multi-Label Text Classification

- Source: arxiv
- arXiv ID: 2609.12915
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.12915v1
- PDF: https://arxiv.org/pdf/2609.12915v1
- DOI: https://doi.org/10.48550/arXiv.2609.12915

### Authors

Hui Ye, Jing Zhang, Xiulong Yang, Rajshekhar Sunderraman

### Abstract

Large-scale multi-label text classification assigns a small subset of relevant labels to each document from a vocabulary containing thousands or tens of thousands of candidate labels. Although pretrained language models have improved semantic text representations, most representation-based approaches center their prediction pipelines on a primary encoder or combine auxiliary features within a single ranker. The complementarity between heterogeneous language models therefore remains insufficiently explored. We propose DualMLC, a dual-branch framework that processes the same document through an autoregressive decoder-only language model and a bidirectional encoder. Each branch maintains its own representation pathway and independently estimates relevance scores over the shared label space. DualMLC combines the two score vectors through late logit fusion, allowing shared evidence to reinforce relevant labels and branch-specific evidence to compensate for limitations in the other branch's representation. DualMLC achieves state-of-the-art results on three widely used large-scale multi-label text classification benchmarks. Ablation results further confirm that integrating the heterogeneous predictors produces stronger rankings than either branch alone. The source code is publicly available at https://github.com/huiyegit/DualMLC.

### 中文一句话结论
DualMLC 通过双分支框架（自回归解码器与双向编码器）结合晚期 logit 融合，显著提升大规模多标签文本分类性能，并在三个基准上达到最新最优结果。

### English TL;DR
DualMLC is a dual-branch framework combining an autoregressive decoder and a bidirectional encoder via late logit fusion, achieving state-of-the-art results on three large-scale multi-label text classification benchmarks.

### 中文详细总结
本文提出 DualMLC，一种针对大规模多标签文本分类的双分支学习框架。该框架利用一个自回归解码器（如 Qwen2.5-7B）和一个双向编码器（如 BERT-base）并行处理同一文档，每个分支独立生成标签 logits，并通过晚期融合（late logit fusion）结合得分向量。这种方法利用异构表示互补性，增强相关标签证据并弥补单分支局限。实验表明，DualMLC 在三个广泛使用的基准上达到最优性能，消融研究证实双分支集成优于单一分支。

### 方法 / 贡献
- 提出 DualMLC，首个异构双分支框架，结合自回归和双向编码器。
- 通过晚期 logit 融合整合两分支预测，无需强制对齐隐藏特征。
- 采用 LoRA 适配大型模型，分组均值减少控制分类器规模。
- 每个分支独立监督训练，保留各自语义证据。

### 实验或数据
论文提到在三个广泛使用的大规模多标签文本分类基准上进行了实验，并报告了最优结果，但摘要中未列出具体数据集名称或详细指标。

### 值得关注点
- 异构编码器互补性验证：自回归与双向注意力捕捉不同语义线索。
- 晚期融合设计避免特征空间强制对齐，保留分支特异性。
- 代码开源，便于复现（https://github.com/huiyegit/DualMLC）。

### 局限性
摘要未明确提及局限性。为确保准确，仅基于所提供信息，未发现明确限制提及。建议查阅全文以获取更详细分析。

## 2. Clustering-Based Balanced Sampling and Allocation with Data Parallelism for High-Performance Fine-Tuning

- Source: arxiv
- arXiv ID: 2609.12584
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.12584v1
- PDF: https://arxiv.org/pdf/2609.12584v1
- DOI: https://doi.org/10.48550/arXiv.2609.12584

### Authors

Hyunjin Kim, Youngeun Nam, Jaemin Han, Wonhyeok Choi, Jae-Gil Lee

### Abstract

Instruction-tuning datasets for large language models (LLMs) are often large, redundant, and imbalanced, limiting efficient adaptation. Naive large-batch fine-tuning repeatedly includes overrepresented sample groups while weakly covering underrepresented but informative ones, especially under data parallelism (DP) across multiple GPUs. We propose CluSTER, a Cluster-aware balanced Sampling framework for Training Efficient data Reduction in DP instruction tuning. CluSTER curates a representative reduced dataset through gradient-space clustering and DP-aware balanced allocation, ensuring dual-level coverage across clusters and workers, while preserving the original data distribution by weighted update. As a result, CluSTER reduces redundant computation and improves training stability without compromising model quality. Across multiple instruction-tuning datasets, CluSTER reduces training time by up to 69.6% with almost no accuracy loss compared to prior sampling and data reduction methods. Code is available at https://github.com/kaist-dmlab/CluSTER.

### 中文一句话结论
CluSTER 通过基于梯度空间的聚类和数据并行感知的平衡分配，构建代表性缩减数据集，实现了高达 69.6% 的训练时间缩减且几乎无损模型质量。

### English TL;DR
CluSTER leverages gradient-space clustering and data-parallelism-aware balanced allocation to create a reduced, representative dataset for efficient instruction tuning of large language models, achieving up to 69.6% training time reduction without compromising model quality.

### 中文详细总结
问题：指令微调数据集常存在冗余、不平衡问题，导致大批量训练中多数样本重复出现而稀有信息样本覆盖不足，尤其在数据并行（DP）多 GPU 环境下效率低下。
方法：提出 CluSTER 框架，包含三个阶段：1）基于梯度的语义聚类（使用轻量级梯度代理嵌入进行 K-means 聚类）；2）聚类感知平衡采样（按最小聚类大小下采样多数类以实现跨聚类平衡，并在聚类内选择靠近边界的多样样本）；3）加权梯度更新（用原始聚类比例加权聚合梯度，保持数据分布）。
结果：在多个指令微调数据集上，相比全数据集训练及已有数据选择方法，CluSTER 将训练时间减少最多 69.6%，且模型性能几乎无损失。代码已开源。

### 方法 / 贡献
- 提出梯度空间聚类方法：利用末层隐藏状态和教师强制概率构造轻量级梯度代理，捕捉语义与不确定性。
- 实现双重平衡覆盖：跨 GPU 的聚类间平衡（将不同聚类分配给不同工作节点）与聚类内多样性（选择靠近聚类边界的样本）。
- 加权梯度更新：使用原始聚类比例对梯度加权，保证缩减后数据分布与全数据集一致。
- 理论分析：证明平衡采样可消除聚类间梯度方差，降低随机梯度方差，提高训练稳定性。

### 实验或数据
- 使用多个指令微调数据集（具体名称未在给定摘要中列出，但提及多种）。
- 与全数据集训练及 LESS、S2L 等基线对比。
- 关键结果：训练时间减少最高 69.6%，模型准确率几乎无损。
- 提供代码仓库：https://github.com/kaist-dmlab/CluSTER。

### 值得关注点
- 双重覆盖设计：将数据并行与聚类分配结合，从系统角度优化分布式训练效率。
- 梯度空间聚类：比文本特征更直接反映样本对优化的贡献，且通过代理避免全模型梯度计算。
- 分布保持：加权更新保留了原始数据分布，避免因下采样导致偏差。

### 局限性
- 聚类个数 K 需等于 GPU 数，可能限制扩展性（大规模集群时需调整）。
- 梯度代理近似可能不完全代表真实梯度，尤其在深层网络。
- 未讨论对长序列或超大数据集的聚类计算开销。
- 方法依赖于初始的教师强制概率，若模型初始随机可能不稳定。

## 3. Parameter-Efficient Retrievers for Polish and European Languages

- Source: arxiv
- arXiv ID: 2609.12913
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.12913v1
- PDF: https://arxiv.org/pdf/2609.12913v1
- DOI: https://doi.org/10.48550/arXiv.2609.12913

### Authors

Sławomir Dadas, Rafał Poświata, Małgorzata Grębowiec, Michał Perełkiewicz

### Abstract

Dense retrieval systems increasingly rely on multi-billion-parameter language models, whose memory and computational requirements make large-scale indexing, frequent corpus updates, and low-latency serving costly. We present a three-stage training pipeline for developing compact and efficient retrievers that remain competitive with substantially larger models. The pipeline combines cross-lingual alignment, relational knowledge distillation, and contrastive fine-tuning. It requires no original ground-truth relevance labels, relying exclusively on supervision generated by strong embedding models and rerankers utilised as teachers. Using this pipeline, we develop PolDense and EuroDense, both supporting contexts of up to 8,192 tokens. PolDense is a family of six Polish retrievers ranging from 17M to 1B parameters. EuroDense is a 435M-parameter retriever supporting nine European languages. We conduct an extensive evaluation covering 41 Polish and 150 multilingual retrieval tasks. The results demonstrate strong quality-efficiency trade-offs. PolDense-1B outperforms the evaluated retrievers with up to 9B parameters, while the PolDense family forms the Pareto frontier across model sizes. Among the evaluated models below 1B parameters, EuroDense ranks first in both task-averaged and language-averaged performance and leads in seven of nine languages. We release all models publicly.

### 中文一句话结论
本文提出三阶段训练流程（跨语言对齐、关系蒸馏、对比微调），无需原始标注数据，分别训练出波兰语PolDense（17M–1B参数）和九语言EuroDense（435M参数）检索器，在多数任务上以远小于大模型的参数规模取得可比甚至更优的性能。

### English TL;DR
This paper introduces PolDense and EuroDense, a three-stage training pipeline that uses knowledge distillation and contrastive fine-tuning to produce parameter-efficient retrievers competitive with much larger models, achieving state-of-the-art performance on Polish and nine European languages while offering strong quality-efficiency trade-offs.

### 中文详细总结
当前密集检索系统常依赖数十亿参数的大语言模型，导致索引更新和低延迟推理成本高昂。本文设计了一个三阶段训练流程来训练紧凑且高效的检索器：第一阶段用平行语料进行跨语言对齐，将单语嵌入空间扩展到多语言；第二阶段通过关系蒸馏（结合余弦对齐、相似性矩阵差异和排序损失）迁移教师模型的检索结构；第三阶段用对比微调（InfoNCE）结合重排序器生成的正负例进行优化。整个过程不使用原始相关性标签。

基于该流程，作者发布了：
- **PolDense**：六种参数规模（17M、50M、110M、150M、400M、1B）的波兰语检索器，支持8,192 token上下文。
- **EuroDense**：435M参数、支持英语、德语、法语、西班牙语、意大利语、葡萄牙语、荷兰语、俄语、波兰语共九种欧洲语言的检索器。

评估覆盖41项波兰语任务（PIRB）和150项多语言检索任务。结果显示：PolDense-1B在波兰语上击败了多达9B参数的已有模型，且整个PolDense系列在各规模上均处于帕累托前沿。在1B参数以下的多语言模型中，EuroDense在任务均值、语言均值以及9种语言中的7种上排名第一。所有模型均已公开。

### 方法 / 贡献
1. **三阶段无监督训练管道**：跨语言对齐（MSE+余弦损失）→ 关系蒸馏（保留教师嵌入结构与排序）→ 对比微调（以重排序器评分替代人工标签）。
2. **基于教师模型的自动标注**：用BGE-Reranker-v2.5-Gemma2-Lightweight对检索候选重排序，按分数阈值生成正负例，避免依赖人工标注。
3. **模型系列**：PolDense（六种规模，波兰语专精）与EuroDense（435M，九语言），均支持8K上下文。
4. **效率与性能平衡**：以小参数模型超越大模型，降低部署成本。

### 实验或数据
- **训练数据**：
  - 跨语言对齐：约2000万英语–波兰语平行句（部分通过Gemma 3 27B翻译）。
  - 关系蒸馏：波兰语模型使用上述平行语料+FineTranslations波兰子集（多至5000万文档）；EuroDense使用2000万文本翻译成的九语言版本（共约1.8亿文本）。
  - 对比微调：13个波兰语检索数据集（>450万查询，1500万段落）；11个多语言数据集（约160万查询，1300万段落，全部机器翻译至九语言）。
- **评估基准**：41项波兰语检索任务（PIRB）；150项多语言检索任务（覆盖MTEB、MMTEB、RTEB、PIRB等）。
- **主要结果**：
  - PolDense-1B在PIRB上超过所有评估过的9B以下模型。
  - PolDense系列在各规模上构成帕累托前沿。
  - EuroDense在<1B多语言模型中平均分第一，在9种语言中的7种上领先。
- **消融实验**（附录提及）表明逐阶段训练带来持续性能提升。

### 值得关注点
- **参数高效**：PolDense-1B与9B模型竞争，EuroDense以435M参数在多语言任务上领先同级。
- **无人工标签依赖性**：全程使用教师模型产生监督信号，适应低资源场景。
- **长上下文支持**：8,192 token输入，适用于文档级检索。
- **开源发布**：所有模型公开在Hugging Face。
- **跨语言对齐改进**：单次运行逐步解冻策略，并设计可丢弃的投影层，降低推理成本。

### 局限性
根据提供的摘要和正文预览，论文未明确讨论模型的局限性。潜在但非论文所述的方向包括：对教师模型（如Pplx-Embed）的依赖可能限制泛化性；多语言版本仅支持九种欧洲语言；缺少与更大规模多语言模型的直接比较（如9B以上模型）。具体局限性需参考完整论文。

## 4. Representation-based Masked Diffusion Model

- Source: arxiv
- arXiv ID: 2609.12382
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.12382v1
- PDF: https://arxiv.org/pdf/2609.12382v1
- DOI: https://doi.org/10.48550/arXiv.2609.12382

### Authors

Yangrong Hu, Ding Huang, Xueyu Zhou, Jian Huang

### Abstract

Masked Diffusion Models (MDMs) have emerged as a compelling paradigm for language modeling, offering the capability for efficient parallel text generation. However, existing parallel sampling methods typically update multiple masked tokens independently and ignore the complex mutual dependencies among the masked tokens. This independent updating mechanism lacks global coordination and might lead to incoherent outputs. To address this limitation, we propose Representation-based Masked Diffusion Model (RMDM), a framework that leverages the text representation to explicitly encode global semantics and help to parallel update tokens more precisely. Specifically, we first encode text into a continuous semantic space using a pretrained encoder and learn an invertible transformation that normalizes the representation distribution to a Gaussian prior, facilitating efficient sampling during generation. Conditioned on this latent semantic representation, we train a masked diffusion model to learn the conditional text distribution, where the representation serves as global semantic guidance to coordinate parallel token updates and faithfully approximate the target distribution. Empirical results demonstrate that RMDM significantly improves generation quality, particularly in aggressive few-step sampling regimes.

### 中文一句话结论
本文提出基于表示的掩码扩散模型（RMDM），通过全局语义表示协调并行令牌更新，在少步采样下显著提升文本生成质量。

### English TL;DR
The Representation-based Masked Diffusion Model (RMDM) addresses the conditional dependency gap in parallel text generation by using a pretrained encoder and MeanFlow to map text representations to a Gaussian prior. This latent representation serves as global semantic guidance to coordinate parallel token updates in masked diffusion models, improving generation quality and throughput, especially in few-step sampling.

### 中文详细总结
现有掩码扩散模型（MDM）在并行生成时独立更新掩码令牌，忽略令牌间的相互依赖，导致输出不连贯。RMDM引入全局潜在表示，显式编码序列的全局语义，从而减少并行更新时的条件依赖间隙。具体分为两阶段：阶段I，利用预训练编码器提取文本表示，并通过MeanFlow学习可逆变换，将表示分布映射为标准高斯先验；阶段II，以该表示为条件训练掩码扩散模型，使其在全局语义指导下预测原始令牌。实验表明，RMDM在少步采样场景下显著提升生成质量，并在匹配质量时实现约3.6倍的吞吐量提升。

### 方法 / 贡献
- **核心方法**：提出两阶段框架。第一阶段通过预训练编码器（如BERT）和MeanFlow将文本语义表示映射到高斯先验，解决推理时无真实表示可用的问题；第二阶段以采样得到的潜在表示为条件，训练掩码扩散模型，利用全局语义指导并行令牌预测。
- **主要贡献**：定义并量化了并行生成中的“条件依赖间隙”，并通过引入全局语义表示有效缓解该问题；方法无需在生成时调用编码器和MeanFlow，保持高效并行采样。

### 实验或数据
摘要中提及了实验结果表明RMDM在少步采样下显著提升生成质量，并报告了与标准MDM相比的吞吐量增益（约3.6倍），但未提供具体数据集名称或详细实验设置。

### 值得关注点
1. 创新性地利用全局语义表示协调并行令牌更新，弥补独立采样的内在缺陷。
2. 采用MeanFlow实现表示分布到高斯先验的精确映射，避免训练-测试分布不匹配。
3. 在少步采样（aggressive few-step sampling）下效果尤为突出，兼顾质量与效率。

### 局限性
基于公开摘要和引言，本文未明确讨论方法的局限性。潜在方面包括：依赖预训练编码器的质量，MeanFlow训练可能引入额外复杂度，以及方法在长文本或多步采样下的表现尚未充分披露。

## 5. SynthSentry: Detecting Synthetic Data Contamination in Language Model Training Data

- Source: arxiv
- arXiv ID: 2609.12353
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.12353v1
- PDF: https://arxiv.org/pdf/2609.12353v1
- DOI: https://doi.org/10.48550/arXiv.2609.12353

### Authors

Praveen Kumar Myakala, Ravichandra Namburi, Sowmya Keragodu Jayaramu, Sooraj George Thomas

### Abstract

Large language models trained recursively on their own or other models' outputs undergo model collapse, in which distributional tails and factual accuracy deteriorate while fluency survives. Prior work diagnoses collapse after training; the actionable problem is screening a corpus of unknown provenance before training. We introduce SynthSentry, a corpus-level, model-agnostic contamination signal requiring no access to the generating model, no generation history, and no synthetic labels. The score is a distributional divergence over three statistics: lexical diversity collapse, n-gram tail truncation, and perplexity variance across reference models. We evaluate on corpora contaminated by small open-weight generators and an instruction-tuned open-weight model under a leave-one-generator-out protocol. A domain-stratified study measures false positives on naturally repetitive human text (legal, clinical, source code). The score ranks corpora by severity with little loss when whole generator families are held out. Per-domain calibration holds near its nominal false-positive budget once covariance shrinkage and a bootstrap threshold replace a naive quantile, which runs four times over budget. A downstream fine-tuning check showed no contamination-driven accuracy deficit at our scale, so whether pruning recovers one remains open; the same run shows over-pruning risk once pruning exceeds the true contamination fraction. We frame screening as a data-curation defense rather than a post-hoc diagnosis and release the scoring toolkit. All results are small-scale; scope is English-language, batch-mode corpus screening. Contamination sources are single-generation or hand-authored rather than recursively generated, so results speak to synthetic contamination generally and not to recursion depth.

### 中文一句话结论
SynthSentry 提出一种无需访问生成模型或标注的语料级、模型无关的合成数据污染检测评分，通过三个统计特征（词汇多样性坍缩、n-gram 尾部截断、跨模型困惑度方差）的分布散度，在训练前筛查语料，并以校准的假阳性预算进行决策，但实验规模较小且未覆盖递归生成场景。

### English TL;DR
SynthSentry introduces a corpus-level, model-agnostic contamination score that uses the Mahalanobis distance over three statistics—lexical diversity collapse, n-gram tail truncation, and cross-model perplexity variance—to detect synthetic data in training corpora before training, requiring no generator access or provenance labels, with calibrated false-positive control via covariance shrinkage and bootstrap thresholding.

### 中文详细总结
SynthSentry 针对大型语言模型递归训练导致的模型坍缩问题，提出一种在训练前筛查语料合成污染的防御方法。核心贡献是定义一个分布散度评分（基于马氏距离），整合三个互补统计特征：词汇多样性（type-token ratio）捕捉词汇收缩、n-gram 尾部截断捕捉低频概率质量损失、跨模型困惑度方差捕捉生成文本在独立评分器下的异常一致性。评分无需生成模型访问、无生成历史或合成标签，但依赖一个预生成参考样本和一组异构评分模型面板。阈值通过协方差收缩和 bootstrap 校准实现，确保假阳性预算达标。实验在小型开放权重生成器和指令微调模型上验证，但结果仅为小规模、英语语料、单代或手写污染源，未覆盖递归生成深度。

### 方法 / 贡献
- **特征设计**：三个统计特征分别对应崩溃机制，且使用 10% 对称修剪均值聚合，避免异常文档主导。
- **评分机制**：将特征向量标准化后计算马氏距离，通过协方差逆矩阵吸收特征间相关性，避免手动权重；得分可分解为白化后的每特征贡献，便于溯源。
- **校准策略**：采用协方差收缩（因小样本病态条件数高达 1.44e12）和 bootstrap 阈值，而非朴素分位数，保持名义假阳性预算。
- **贡献三点**：将污染检测建模为分布散度问题；设计 leave-one-generator-out 评估协议；发布评分工具包和未来多代标注基准。

### 实验或数据
- 评估语料：由小型开放权重生成器和指令微调开放权重模型污染。
- 协议：leave-one-generator-out，分离整个模型家族。
- 关键结果：协方差收缩和 bootstrap 阈值逼近名义假阳性预算，而朴素分位数超出预算四倍。发现低混合比例下修剪均值可能衰减尾部截断信号（通过聚合器消融测试）。下游微调检查无污染导致的精度损失，但过度修剪风险在超过真实污染比例时出现。
- 注意：仅小规模展示；未包含不同评分器面板的消融测试；未涉及递归生成或非英语语料。

### 值得关注点
- **模型无关性边界明确**：方法不需要生成模型，但依赖评分模型面板，面板变化的影响未验证，这是作者承认的关键前提。
- **校准优于启发式**：使用马氏距离避免手工权重，通过收缩和 bootstrap 实现分布自由阈值，且白化分解提升可解释性。
- **定位为数据防御**：区别于事后诊断或文档级检测，面向训练前语料筛选，适用于无标注的混合来源语料。
- **特征互补性**：词汇多样性对粗劣生成敏感，尾部截断和困惑度方差对高质量生成敏感，组合提升鲁棒性。

### 局限性
- 实验规模小，结果仅说明小样本和英语语料场景。
- 污染源为单代或手写，未涵盖递归生成，结论不能外推到递归深度。
- 评分器面板固定（三个模型：distilgpt2 等），未做面板消融，模型无关性依赖此前提。
- 需参考样本（预生成文本），在无法集中化参考数据的环境中不适用。
- 无对抗场景，不针对故意投毒。

## 6. Language Is an Insufficient Substrate for Quantitative Reasoning, and Consequential Domains Need Large Quantitative Models

- Source: arxiv
- arXiv ID: 2609.12105
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.12105v1
- PDF: https://arxiv.org/pdf/2609.12105v1
- DOI: https://doi.org/10.48550/arXiv.2609.12105

### Authors

Reuben Vandeventer, David Imrem, David J. Wild

### Abstract

The prevailing assumption in applied machine learning is that progress on consequential quantitative decisions such as pricing risk, allocating capital, triaging patients, or containing a network intrusion will follow from progress in large language models (LLMs). A language model is trained on a representation of the world that was produced by human description; description is a lossy encoding of the quantitative record, and the loss is irreversible: no downstream model, at any scale, can recover from a description what the description did not encode. We formalize this as a property of the representation on which a model is trained rather than of the model capacity, and we identify three further properties that consequential settings demand of a model and that a language substrate cannot supply by construction: reproducibility, lineage from every output back to the source records that produced. it, and calibrated uncertainty. We argue that these properties define a distinct model class, which we call the Large Quantitative Model (LQM).

### 中文一句话结论
本文指出语言模型因将定量数据不可逆地压缩为描述，从根本上无法满足高风险定量决策所需的保真度、可复现性、溯源和校准不确定性，并提出应构建原生训练于定量记录的“大规模定量模型（LQM）”。

### English TL;DR
The paper argues that language models are fundamentally insufficient for quantitative reasoning in consequential domains because language is a lossy and irreversible compression of quantitative data, and proposes a new class of "Large Quantitative Models" (LQMs) that are trained natively on quantitative records to ensure fidelity, reproducibility, lineage, and calibrated uncertainty.

### 中文详细总结
文章系统论证了大语言模型（LLM）在高风险定量决策中的结构性不足。核心观点：语言是对定量记录的“有损编码”，损失不可逆；任何规模的LLM都无法恢复描述中未包含的信息（保真度失败）。此外，语言模型基于采样的输出机制破坏了可复现性；隐含在权重中的知识无法提供从输出到源记录的精确溯源（替代方法仅为近似归因）；由文本生成的不确定性表述不具备校准性。这些缺陷源于模型训练所用的表征（representation），而非模型能力。针对此，作者定义并倡议开发一类新模型：大规模定量模型（LQM），其应具备原生训练于定量记录、显式可检查的结构表示、完整的数据溯源以及内建的不确定性校准。文章讨论了与现有模型类（如表/时序基础模型、世界模型）的区别，并描述了一个混合架构的实例——将LLM限制为人类接口，由结构化模型负责定量推理。

### 方法 / 贡献
- **形式化框架**：定义保真度、可复现性、数据溯源和校准四个属性，将其作为表征而非模型能力的性质，并通过信息论（数据处理不等式、Fano不等式）证明语言表征对定量查询的不可恢复性。
- **问题定性**：指出LLM的缺陷是“结构性”而非“能力所限”，无法通过缩放、微调、工具使用或检索彻底修复。
- **提出新类别**：将上述四个属性的正向要求整合为“大规模定量模型（LQM）”，并给出其在拓扑结构、动力学学习及混合接口等方面的实例化设计。
- **回应反驳**：严肃讨论缩放、微调、工具使用等最强反论点，指出它们仅作用于接口而非底层表征。

### 实验或数据
本文为立场论文，未开展大规模实验。作者提及一个已部署系统中的证据：将语言模型限制为接口，由结构化定量模型执行推理。但未提供具体数据集或定量结果。

### 值得关注点
- 用信息论严格证明语言表征的“不可恢复性”：错误概率下界不依赖于模型参数或计算量，仅取决于描述和查询。
- 强调“溯源（lineage）”是结构属性而非行为属性：显式结构与隐式权重在可审计性上有本质区别。
- 提出LQM应具备“可检查的显式表示”和“内建的不确定性校准”（含弃权状态），而非依赖外部后处理。
- 将四属性与金融、保险、医疗、欧盟AI监管等具体监管要求直接对应，增强实践相关性。
- 明确指出“语言模型说话，定量模型知道”的混合架构定位。

### 局限性
- 本文以立场和理论论证为主，缺乏对提案LQM类别的完整实现和基准测试。
- 对现有LLM场景的定量表现引用有限（仅简要提及准确性常见问题，未深入分析）。
- 未详细展示已部署实例的具体性能指标或与纯LLM方案的对比结果。
- 承认所提性质组合在构建上存在挑战（如显式结构、大规模顺序推理），但未充分讨论工程复杂性。

## 7. Extracting Dataset Mentions in Forced Displacement and FCV Documents: A Weakly Supervised Framework with LLM-Based Label Refinement

- Source: arxiv
- arXiv ID: 2609.12107
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.12107v1
- PDF: https://arxiv.org/pdf/2609.12107v1
- DOI: https://doi.org/10.48550/arXiv.2609.12107

### Authors

Rafael Macalaba, Aivin V. Solatorio, Patrick Michael Brock, Olivier Dupriez

### Abstract

Development and humanitarian organizations produce and support surveys, administrative registries, and other data resources to inform research, policy, and operations, yet systematically identifying where these datasets are referenced remains difficult. Such references are dispersed across research papers, project documents, humanitarian reports, and other unstructured text, limiting both the ability to trace data use and to identify potential gaps in data availability or dissemination. We present a weakly supervised framework for adapting dataset extraction to forced displacement and Fragile, Conflict, and Violence (FCV) documents without first constructing a large manually labeled training corpus. A lightweight model trained on general research literature generates candidate dataset mentions from unlabeled domain documents, which a frontier large language model (LLM) reviews in context, validating or rejecting candidates and correcting their extraction boundaries. The resulting annotations are supplemented with targeted synthetic and contrastive examples and used to fine-tune the lightweight model for large-scale extraction. We evaluate the resulting model on an independent gold-standard benchmark of 1,706 text passages spanning research, humanitarian, and operational documents. Across the full benchmark, the model achieves 74.1\% precision and 70.5\% recall at the mention level; among passages containing dataset references, precision reaches 89.5\%. At the passage level, the model achieves 88.2\% accuracy and 88.6\% specificity in distinguishing passages with dataset references from those without them. These results demonstrate a practical approach for constructing domain-specific supervision when labeled data are limited, and provide a technical foundation for larger-scale analysis of data use and potential gaps in the displacement data landscape.

### 中文一句话结论
本文提出一种结合轻量级提取模型与LLM标签精炼的弱监督框架，在无需大规模人工标注的情况下，从流离失所与FCV文档中有效提取数据集提及，达到74.1%的精确率和70.5%的召回率。

### English TL;DR
A weakly supervised framework combining a lightweight extraction model with LLM-based label refinement effectively extracts dataset mentions from forced displacement and FCV documents, achieving 74.1% precision and 70.5% recall without requiring a large manually labeled training corpus.

### 中文详细总结
本研究针对发展与人道主义组织中系统识别数据集引用困难的问题，提出了一种弱监督框架。该框架首先利用在通用研究文献上训练的轻量级模型，从无标签的流离失所和FCV文档中生成候选数据集提及；随后由前沿大语言模型（LLM）在上下文环境中审核这些候选，验证或拒绝它们，并纠正提取边界。生成的标注辅以定向合成和对比示例，用于微调轻量级模型以进行大规模提取。在包含1,706个文本段落（涵盖研究、人道主义和操作文档）的独立金标准基准上，模型在提及级别达到74.1%精确率和70.5%召回率；在包含数据集引用的段落中，精确率可达89.5%。在段落级别，模型区分有无数据集引用的准确率为88.2%，特异性为88.6%。该方法为标注数据有限时构建领域特定监督提供了实用途径，并为大规模分析流离失所数据格局奠定了基础。

### 方法 / 贡献
- **方法**：四阶段弱监督框架：1) 使用现有GLiNER2模型生成候选提及；2) 使用LLM（如OpenAI结构化输出）在上下文中精炼候选，验证或拒绝并纠正边界；3) 生成合成和对比示例以覆盖困难案例；4) 合并数据微调轻量级模型用于大规模提取。
- **贡献**：1) 引入结合现有提取模型、LLM辅助标注精炼和定向合成数据的弱监督框架；2) 展示监督转移到轻量级本地模型的方法；3) 在涵盖多种文档类型的独立异质基准上评估模型。

### 实验或数据
- **基准**：独立金标准基准包含1,706个文本段落，涵盖研究、人道主义和操作文档。
- **结果**：提及级别精确率74.1%，召回率70.5%；含数据集引用段落中精确率89.5%；段落级别准确率88.2%，特异性88.6%。摘要未提及具体数据集或训练集规模。

### 值得关注点
- 无需大规模人工标注，显著降低领域迁移成本
- LLM仅用于候选精炼，推理时可独立运行，不依赖LLM
- 模型在异质文档类型上表现稳定，特别在含数据集引用场景下精确率较高
- 为追踪数据使用和识别数据缺口提供技术基础

### 局限性
- 研究仅评估提取能力，不推断数据集实际使用或影响
- 基准不构成代表性语料库，未覆盖所有政策、研究或操作材料
- 未涉及更广泛应用中所需的语料构建、相关性过滤、数据集解析与链接、上下文分类等扩展任务
- 未测试改进引用规范是否导致更多数据使用，仅提供未来实证分析的可能性
- 摘要未明确提及模型在极端稀疏或格式极不规范文档上的表现边界

## 8. QTrans: A Quantum Transformer for Sentiment Classification

- Source: arxiv
- arXiv ID: 2609.12011
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.12011v1
- PDF: https://arxiv.org/pdf/2609.12011v1
- DOI: https://doi.org/10.48550/arXiv.2609.12011

### Authors

Ren-Xin Zhao, Xinjie Huang, Yahong Liu, Maoyu Ye, Jinjing Shi, Shi Wang, Yaonan Wang

### Abstract

In small-scale binary sentiment classification scenarios, factors such as negation, contrastive shifts, and cross-word dependencies lead to the non-linear coupling of sentiment cues, making it difficult for conventional lightweight models to fully capture the contextual relationships between tokens. To address this issue, we propose a model named QTrans, which uses parameterized quantum circuits to construct query, key, and value features and derives attention coefficients from Gaussian distances between quantum measurements. By further integrating a quantum feed-forward neural network, residual connections, and layer normalization, the model establishes an end-to-end trainable quantum-classical hybrid framework for sentiment classification. Experimental results on the MR, CR, and MPQA datasets show that QTrans achieves test accuracies of 72.13\%, 69.51\%, and 63.45\%, respectively, representing improvements of 2.88, 3.17, and 3.79 percentage points over the best-performing classical baselines for each dataset. Overall, QTrans expands the application of parameterized quantum circuits in lightweight sentiment analysis and lays an experimental foundation for further research into quantum multi-head self-attention for modeling textual relationships.

### 中文一句话结论
QTrans 提出一种基于参数化量子电路的量子-经典混合 Transformer，通过高斯投影量子多头自注意力与量子前馈网络，在小型情感分类任务中显著优于经典轻量级基线。

### English TL;DR
QTrans introduces a quantum-classical hybrid Transformer for sentiment classification that builds query, key, and value features with parameterized quantum circuits and derives attention from Gaussian distances, outperforming classical lightweight baselines on MR, CR, and MPQA datasets.

### 中文详细总结
QTrans 针对小规模二分类情感分析中否定、对比转折、跨词依赖导致的非线性情感线索耦合问题，提出了一种量子-经典混合架构。该模型使用参数化量子电路分别生成查询（Q）、键（K）、值（V）特征，并通过量子测量的高斯距离计算注意力系数，避免了全量子态内积的复杂操作。同时，模型集成了量子前馈神经网络、残差连接和层归一化，构成端到端可训练的完整框架。实验表明，QTrans 在 MR、CR、MPQA 三个数据集上分别取得 72.13%、69.51%、63.45% 的测试准确率，相较最优经典基线分别提升 2.88、3.17、3.79 个百分点。该工作拓展了参数化量子电路在轻量级情感分析中的应用，并为量子多头自注意力的文本关系建模提供了实验基础。

### 方法 / 贡献
- 提出 n 量子比特高斯投影量子多头自注意力：独立参数化量子电路生成 Q、K、V 测量值，归一化高斯系数量化标记相关性，V 测量特征分为两个注意力头。
- 构建位置级量子前馈神经网络（独立参数化 n 量子比特电路），并将量子多头自注意力、量子前馈网络与残差连接、层归一化整合为 QTrans。
- 在 MR、CR、MPQA 数据集上评估 4 量子比特实例，证明性能优势。

### 实验或数据
- 数据集：MR（电影评论）、CR（产品评论）、MPQA（观点极性）。
- 测试准确率：MR 72.13%、CR 69.51%、MPQA 63.45%。
- 性能提升：相对最优经典基线分别提升 2.88、3.17、3.79 个百分点。

### 值得关注点
- 高斯投影避免了经典点积注意力依赖全量子态内积，降低计算复杂度。
- 量子电路提供非线性特征变换，可能增强对否定、对比等语义角色的区分能力。
- 轻量级设计（4 量子比特）在小型数据集上避免了过拟合，同时保持性能优势。

### 局限性
摘要未提及实验的具体设置细节（如超参数、训练轮次、硬件环境）或对更大规模数据集的可扩展性分析。此外，量子电路的实际量子硬件实现噪声和退相干影响未在摘要中讨论。部分性能提升幅度有限（<4 个百分点），需验证统计显著性和跨领域泛化性。

## 9. Type Diversity Enables Transformers to Generalise Compositionally

- Source: arxiv
- arXiv ID: 2609.13144
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.13144v1
- PDF: https://arxiv.org/pdf/2609.13144v1
- DOI: https://doi.org/10.48550/arXiv.2609.13144

### Authors

Anssi Moisio, Mathias Creutz, Mikko Kurimo

### Abstract

Compositional generalisation has been divided into lexical and structural generalisation. Previous work has found that structural generalisation is harder than lexical for Transformers. We propose that this difference is not inherent to Transformers, but due to the high diversity of lexical types and low diversity of structural types in the specific datasets of these previous works. By type diversity we mean the number of different constructors of that type, instead of, for example, the specific word combinations that might populate the structure. To test this, we vary the amounts of type diversity of lexical and structural types in previously published datasets. We create linguistically diverse variants of the COGS and SLOG datasets using Grammatical Framework. We find that type diversity correlates with compositional generalisation equally in lexical and structural test cases, supporting our hypothesis. We note a contradiction with the proposition in previous work that compound divergence explains the difficulty in compositional generalisation tasks. We further investigate the effects of other dataset properties on compositional generalisation, such as the diversity of types other than the novel test structure, and surface properties of the logical semantics format.

### 中文一句话结论
本文提出并验证：Transformer在组合泛化中表现出的“结构泛化比词汇泛化更难”的现象并非模型固有缺陷，而是由于训练数据中结构类型的多样性远低于词汇类型的多样性；增加结构类型多样性可同等程度提升两种泛化能力。

### English TL;DR
This paper demonstrates that the perceived difficulty of structural compositional generalization in Transformers is not inherent but instead driven by low type diversity in training data, and that increasing type diversity improves performance equally for both lexical and structural tasks, contradicting previous claims.

### 中文详细总结
先前研究将组合泛化分为词汇泛化（新词在不同结构中使用）和结构泛化（新结构在不同词填充下使用），并发现Transformer在结构泛化上表现更差。本文认为，这种差异并非源于Transformer本身，而是因为之前所用数据集中词汇类型的多样性高、结构类型的多样性低。作者将“类型多样性”定义为某一语法类型（如名词短语）所拥有的不同构造器（constructor）的数量，而非具体词组合的数量。为验证假设，作者利用语法框架（Grammatical Framework）对COGS和SLOG数据集生成了具有不同语言多样性的变体，并在SCAN数据集上生成了一百多个严格控制类型多样性的变体。实验发现，类型多样性与词汇和结构测试案例中的组合泛化性能呈同等程度的正相关，支持了其假设。此外，研究还发现这一结果与先前工作提出的“复合发散度（compound divergence）解释组合泛化难度”的观点相矛盾，并进一步探讨了其他数据属性（如逻辑语义格式的表面属性、除新结构外其他类型的多样性）对泛化的影响。

### 方法 / 贡献
- **定义与测量类型多样性**：以语法框架中的构造器数量定义类型多样性，区分于词组合多样性。
- **生成多样化数据集**：利用GF为COGS、SLOG生成具有自然语言多样性（形容词、复数、时态等）的变体，并为SCAN生成上百个变体以系统控制词汇/结构类型多样性。
- **实验验证**：在三种主流组合泛化数据集（COGS、SLOG、SCAN）上训练小型Transformer，对比词汇与结构泛化性能，用控制变量的方法排除其他因素干扰。
- **反驳既有结论**：证明复合发散度不能完全解释泛化难度，类型多样性是更关键的因素。
- **额外探究**：分析逻辑语义格式的次序等表面属性对结果的影响。

### 实验或数据
- **数据集**：
  - COGS（原版及多样化变体）
  - SLOG（COGS的变体，原版及多样化变体）
  - SCAN（原版及一百多个精心控制类型多样性的变体）
- **模型**：小型Transformer（具体架构细节在论文正文，但摘要未详述）。
- **实验设计**：
  - 分别测试词汇泛化与结构泛化案例。
  - 从多个维度改变类型多样性（如增加NP构造器、动词时态等）。
  - 记录模型准确率，并与DBCA（分布组成性评估）指标、复合发散度等进行对比。
- **结果**：类型多样性增加时，结构泛化准确率显著提升，且与词汇泛化提升幅度相近；复合发散度与性能的负相关在控制类型多样性后减弱甚至反转。

### 值得关注点
- **核心发现**：类型多样性是影响Transformer组合泛化的关键数据质量因素，而非模型本身的能力限制。
- **与既有研究矛盾**：直接反驳了“结构泛化天生更难”的主流观点，以及“复合发散度解释泛化难度”的流行理论。
- **方法论创新**：用形式语法（GF）精确操控类型多样性，提供了比以往随机替换更可控的生成方案。
- **实际影响**：提示构建训练数据时应注重增加结构类型的多样性（如加入形容词、复数、时态等），而不仅仅是扩大数据规模或词汇数量。

### 局限性
- 实验限于小型Transformer和诊断性数据集（COGS、SLOG、SCAN），结果向更大模型或更自然语言任务的推广性尚待验证。
- 类型多样性的定义依赖于语法框架的构造器划分，对于没有明确语法结构形式化的任务是否适用不明确。
- 论文未详细讨论类型多样性可能带来的负面效应（如过度多样性导致数据稀疏或学习困难）。
- 其他可能影响组合泛化的因素（如训练数据规模、模型深度、注意力机制等）未被系统控制，仅控制了类型多样性。
- 逻辑语义格式表面属性的影响仅初步探索，未做全面因果分析。

## 10. Reproducing and Evaluating the Generalizability of Subliminal Learning in Open-Weight Models

- Source: arxiv
- arXiv ID: 2609.12586
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2609.12586v1
- PDF: https://arxiv.org/pdf/2609.12586v1
- DOI: https://doi.org/10.48550/arXiv.2609.12586

### Authors

Daan van der Weijden, Nathan Brack, Selene Baez Santamaria

### Abstract

In this reproduction paper we investigate subliminal learning, a consequence of distillation where teacher models transmit behavioral preference traits through semantically unrelated data. The original paper explores two types of traits (animal preferences and misalignment), three data modalities (number sequences, code, and chain of thought), and several model families. We reproduce their experiments and extend the setup along three axes: new preference categories (actors and politicians), a new task (chess move generation), and an additional open-weight model (Ministral8B). We also run a controlled ablation on the numbers task's answer-space size (1-, 2-, and 3-digit sequences). We focus on open-weight models with accessible checkpoints on HuggingFace, since the original paper's GPT-4.x fine-tuning is no longer available. Our reproduction supports the original paper's claims, but our extensions show they are not universal as transmission strength varies across traits and tasks, and one model shows almost no effect at all.

### 中文一句话结论
本研究复现了开放权重模型中的阈下学习现象，支持原始声明，但发现该现象并非普遍适用，其传递强度因特质、任务和模型而异，且有一个模型（Ministral8B）几乎没有效果。

### English TL;DR
This reproduction of subliminal learning in open-weight models supports the original claims but reveals that the phenomenon is not universal, as transmission strength varies across traits, tasks, and models, with one model showing almost no effect.

### 中文详细总结
本文通过复现和扩展研究，验证了知识蒸馏中的阈下学习：教师模型通过语义无关数据（如数字序列）将行为偏好（如动物偏好）传递给学生模型。复现部分使用Qwen2.5-7B和Gemma3-4B，确认了原始结果。扩展部分包括：（1）新增偏好类别（演员、政治家），其中政治家传递强度显著高于动物；（2）新增任务（国际象棋移动生成），效果弱于数字序列；（3）新增模型（Ministral8B），显示几乎无效果；（4）数字序列答案空间消融（1位、2位、3位），发现答案空间越小传递越强，与预期相反。分析表明，教师生成数据中无显式特质信号（AUC≈0.53），但学生完成质量分析显示部分模型（如Qwen）在动物类别中出现身份泄露，政治家类别中拒绝率波动。总体而言，阈下学习真实存在但受特质、任务和模型显著影响，并非普遍属性。

### 方法 / 贡献
- **方法**：使用开放权重模型（Qwen2.5-7B、Gemma3-4B、Ministral8B）；通过微调或系统提示为教师模型注入特质（动物偏好、演员偏好、政治家偏好），生成语义无关的训练数据（数字序列、国际象棋移动）；学生模型在该数据上微调后，用中性提示评估偏好。
- **主要贡献**：复现原始阈下学习发现并验证其可复现性；通过扩展新特质、新任务、新模型评估通用性；通过答案空间消融揭示反直觉效应；揭示模型间差异（Ministral几乎无效果）。

### 实验或数据
- **实验设置**：三种模型（Qwen2.5-7B、Gemma3-4B、Ministral8B），两种任务（数字序列、国际象棋移动），三种偏好类别（动物：10个实体；演员、政治家：各6个实体，基于模型响应分布和地域多样性选择）。每个条件使用多个种子重复（图中含均值与95%置信区间）。数字序列各长度（1位、2位、3位）生成30,000个样本，国际象棋序列使用公开数据库种子。学生完成评估使用Llama3.1-8B作为裁判分类（有效回答、拒绝、身份泄露等）。
- **关键数据**：log-odds比值图显示不同特质、任务、模型下的传递强度；答案空间消融图显示1位数字效果最强；教师数据分布图显示非均匀但不可分（AUC≈0.53）；完成质量堆叠柱状图显示Qwen在动物类别中身份泄露显著增加。

### 值得关注点
1. **效果非普遍**：Ministral模型在所有特质和任务中几乎没有效果，说明阈下学习可能可通过模型设计避免。
2. **答案空间反直觉**：数字序列答案空间越小（1位），传递反而越强，可能由于更集中的token分布放大了信号。
3. **特质差异显著**：政治家偏好传递强度高于动物，演员居中，可能反映社会敏感特质具有更强表征。
4. **任务影响**：数字任务效果强于国际象棋任务，后者可能因非法移动引入噪声。
5. **模型差异**：Qwen效果最大，Gemma次之，Ministral几乎无；完成质量分析显示Qwen在动物类别中有身份泄露（偏好直接输出），政治家中拒绝率波动。

### 局限性
（来自论文的局限性部分）
1. 仅使用开放权重模型，无法直接与原始GPT-4实验比较，任何差异可能源于模型族而非现象本身。
2. 新特质（演员、政治家）及其具体实体的选择基于启发式（模型响应分布+人工多样化），引入实验者判断。
3. 国际象棋移动任务仅检查格式合法性，未验证移动是否符合棋盘状态（多数生成移动非法），可能引入噪声导致效果弱于数字序列。
4. 扩展广度有限（仅两个新类别、一个新任务、一个新模型），结论应视为示意性而非穷举性。

## Processing Notes

- Duplicate papers skipped: 0