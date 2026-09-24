# Daily arXiv - 2026-09-24

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-24T00:33:57
- Paper count: 10

## 1. The Probabilistic Structure of Large Language Models

- Source: arxiv
- arXiv ID: 2609.25134
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.25134v1
- PDF: https://arxiv.org/pdf/2609.25134v1
- DOI: https://doi.org/10.48550/arXiv.2609.25134

### Authors

Adnan Aboulalaâ

### Abstract

This paper presents a probabilistic perspective on large language models (LLMs), developed with the aim of bringing together, in a single self-contained account, tools that are usually treated separately across the literature. LLMs are described through probability measures on the set of sequences of tokens, specified via their autoregressive conditional distributions. Training is formulated as a maximum-likelihood estimation problem, addressed by stochastic gradient methods, while text generation is viewed as the sequential simulation of the resulting stochastic process. The role of the asymmetry of the Kullback--Leibler divergence in text generation is examined in relation with characteristic phenomena such as hallucination and the distinction between statistical plausibility and truth. As a complementary illustration of the same viewpoint, we also discuss diffusion models, built around the score function, which cast generation not as sequential token prediction but as the simulation of a reverse-time stochastic process transforming noise into data both in discrete and continuous time.

### 中文一句话结论
本文从概率论角度统一阐述了大型语言模型作为词元序列上的概率测度，并探讨了其训练、生成与扩散模型之间的联系。

### English TL;DR
This paper provides a unified probabilistic perspective on large language models by framing them as probability measures on token sequences, training via maximum likelihood, and generation as sequential stochastic simulation, while also connecting to diffusion models through score-based generative processes.

### 中文详细总结
本文以概率论为核心，系统构建了大型语言模型的统一理论框架。首先，将语言模型定义为有限词汇表上词元序列的概率测度，通过自回归条件分布进行参数化。训练过程被形式化为最大似然估计问题，通过随机梯度方法求解；文本生成则被视为对所得随机过程的顺序模拟。文章特别分析了KL散度的不对称性在文本生成中的作用，解释了幻觉现象以及统计合理性与真实性之间的区别。作为补充，文章还讨论了基于分数函数的扩散模型，该模型通过逆时随机过程将噪声转化为数据，而非顺序词元预测。

### 方法 / 贡献
- 提出统一概率框架，将语言模型明确定义为词元序列上的概率测度
- 系统梳理训练、生成过程中的概率基础，明确区分真实分布P*、经验分布P_emp和参数化族P_θ
- 揭示KL散度不对称性在生成中的关键作用，联系幻觉现象
- 将扩散模型纳入同一视角，展示逆时随机过程的生成范式

### 实验或数据
论文未提供实验或数据集。它是一篇理论综述性文章，聚焦于概率框架的形式化推导和概念澄清。

### 值得关注点
- 清晰区分了概率测度的三个层次：未知真实分布、经验分布和参数化模型族
- 详细解释了为何最优概率词并非实际生成词，以及为何不应如此选择
- 指出了统计正确性与真理性的根本区别——模型只学习统计规律，无法判断陈述的真实性

### 局限性
- 未涉及实际的模型训练细节或实验结果
- 对Transformers架构的描述较为简略，主要将其作为计算黑箱
- 未讨论计算效率、内存限制等工程实践问题

## 2. One Domain, Many Tongues: Composing Domain and Language LoRAs for Cross-Lingual Remote-Sensing MLLMs without Paired Data

- Source: arxiv
- arXiv ID: 2609.26097
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.26097v1
- PDF: https://arxiv.org/pdf/2609.26097v1
- DOI: https://doi.org/10.48550/arXiv.2609.26097

### Authors

Xuechen Li

### Abstract

Remote-sensing (RS) multimodal large language models (MLLMs) are trained and evaluated only in English, while text-only instruction data covers over 100 languages. We propose MODL (Mutually Orthogonal Domain-Language composition), a recipe that adds new languages to an English RS MLLM without a single multilingual RS example: a domain LoRA trained on English RS imagery and a language LoRA trained on text alone are learned jointly, under one loss term that keeps the two updates mutually orthogonal at every layer throughout training. This constraint is the recipe's active ingredient. Without it, the same training answers RS questions correctly but in English, erases much of the base model's multilingual text ability, and diverges on one seed in three; sixteen alternatives, from training-free merging to prior orthogonality variants, fail the same way. MODL repairs every failure on every seed: answers are correct and in the target language 56-71% of the time, where the best alternative reaches 27% and most stay below 8%, text ability stays at the level of the untrained base, and on Spanish it surpasses Qwen2.5-VL-7B, with zero multilingual-multimodal data. A single five-language adapter retains English, Spanish, and Vietnamese at full strength across three seeds; non-Latin scripts remain an open boundary.

### 中文一句话结论
提出一种互正交领域与语言LoRA联合训练方法（MODL），仅需英语遥感数据和无图像文本指令即可为遥感多模态大模型添加新语言，无需任何多语言多模态数据，且显著优于所有基线。

### English TL;DR
MODL (Mutually Orthogonal Domain-Language composition) jointly trains a domain LoRA on English remote-sensing imagery and a language LoRA on text-only instructions under a mutual orthogonality constraint, enabling an English-centric RS MLLM to answer correctly in a new target language without any multilingual multimodal training data, achieving 56–71% correct-and-in-language accuracy vs. <27% for all alternatives.

### 中文详细总结
摘要指出，现有遥感多模态大模型（RS MLLMs）仅限于英语训练和评估，而文本指令数据覆盖100多种语言。本文提出MODL方法，通过一个互正交损失项，在训练过程中保持领域LoRA（基于英语遥感图像和指令训练）与语言LoRA（仅基于目标语言文本指令训练）的更新每层相互正交。该约束是关键因素：没有它，联合训练会正确回答但输出英语、抹除基座模型的多语言文本能力，且三分之一的种子发散；16种替代方法（包括无训练合并、先验正交变体等）均出现相同失败。MODL在所有种子上修复所有失败：在目标语言中正确回答问题率达到56–71%，最佳替代方法仅达27%，多数低于8%；文本能力保持未训练水平；在西班牙语场景分类上甚至超越Qwen2.5-VL-7B（零多语言多模态数据）。单次五语言适配器（英语、西班牙语、越南语）在三个种子上保持完整性能，但非拉丁字母仍是开放边界。

### 方法 / 贡献
- 方法：提出MODL，联合训练领域LoRA（基于英语遥感指令）和语言LoRA（基于目标语言文本指令），并在每一层施加对称互正交损失（公式），使两更新子空间在训练过程中始终近似正交。
- 贡献：1）首个跨语言遥感MLLM配方，无需任何多语言多模态配对数据；2）将问题重新诊断为干扰和输出语言保真度，而非能力迁移；3）提供机制证据：只有持续互正交的约束有效，函数空间变体(FIC)及初始化/顺序正交方法（OSRM, O-LoRA）均失败；4）提出预注册评估协议，量化了两个评估陷阱（缺失EOS监督造成7倍指标污染，不一致翻译造成的参考偏差）。

### 实验或数据
- 数据集：使用GeoChat-Bench分类测试集（每语言2195项）、Belebele文本多语言能力测试（每语言900项），目标语言包括西班牙语、越南语（主要实验）及额外三种语言（五语言变体）。
- 基线：对比16种替代方法，包括无训练合并、联合训练、函数空间一致性（FIC）、先验正交方法（OSRM、O-LoRA）等。所有设置匹配训练预算、三种子。
- 结果：MODL在正确且目标语言准确率（A∩L）上达到56–71%（最佳基线27%，多数<8%）；在西班牙语场景分类上超越Qwen2.5-VL-7B；文本能力保留；五语言适配器保持英语、西语、越语完整性能。

### 值得关注点
- 关键创新：单一互正交损失项，从几何上解耦领域与语言子空间，同时避免干扰并保留基座模型的多语言技能。
- 实验严谨性：预注册协议、三种子、量化评估陷阱、对比多种几何/功能类替代方法。
- 实用性：无需昂贵多语言多模态翻译数据，仅需英语遥感指令+目标语言文本指令。

### 局限性
- 非拉丁字母语言（如中文、阿拉伯语）仍为开放边界，当前五语言适配器仅对英语、西班牙语、越南语保持完整性能。
- 方法尚未在更大型MLLM或更多语言上验证。

## 3. TransBERT: A Framework for Synthetic Translation in Domain-Specific Language Modeling

- Source: arxiv
- arXiv ID: 2609.26347
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.26347v1
- PDF: https://arxiv.org/pdf/2609.26347v1
- DOI: https://doi.org/10.48550/arXiv.2609.26347

### Authors

Julien Knafou, Luc Mottin, Anaïs Mottaz, Alexandre Flament, Patrick Ruch

### Abstract

The scarcity of non-English language data in specialized domains significantly limits the development of effective Natural Language Processing (NLP) tools. We present TransBERT, a novel framework for pre-training language models using exclusively synthetically translated text, and introduce TransCorpus, a scalable translation toolkit. Focusing on the life sciences domain in French, our approach demonstrates that state-of-the-art performance on various downstream tasks can be achieved solely by leveraging synthetically translated data. We release the TransCorpus toolkit, the TransCorpus-bio-fr corpus (36.4GB of French life sciences text), TransBERT-bio-fr, its associated pre-trained language model and reproducible code for both pre-training and fine-tuning. Our results highlight the viability of synthetic translation in a high-resource translation direction for building high-quality NLP resources in low-resource language/domain pairs.

### 中文一句话结论
TransBERT框架证明：在法文生命科学领域，仅使用合成翻译的语料预训练语言模型即可达到与真实语料相当的性能。

### English TL;DR
TransBERT demonstrates that pre-training language models solely on synthetically translated English-to-French texts can achieve state-of-the-art performance on French life sciences NLP tasks, releasing the TransCorpus toolkit, a 36.4GB corpus, and a pretrained model.

### 中文详细总结
生命科学等专业领域非英语数据稀缺，限制了NLP工具的开发。本文提出TransBERT框架，仅使用合成翻译的文本预训练语言模型；同时发布TransCorpus可扩展翻译工具包。以法文生命科学领域为例，使用M2M-100 1.2B模型进行句子级翻译，构建了36.4GB的TransCorpus-bio-fr语料库，并预训练得到TransBERT-bio-fr模型。在DrBenchmark多个下游任务上，该模型达到与现有最优模型相当的性能，验证了合成翻译在高质量资源方向（英→法）上的可行性。

### 方法 / 贡献
- **方法**：基于fairseq和M2M-100多语言翻译模型，采用句子级翻译、长度分桶（bucketing）减少填充，支持多GPU分布式处理，实现大规模语料高效合成翻译。
- **贡献**：
  1. 开源TransCorpus工具包（支持100种语言翻译）。
  2. 发布36.4GB法文生命科学合成语料TransCorpus-bio-fr及配套分词器。
  3. 发布基于该语料预训练的TransBERT-bio-fr模型。
  4. 提供可复现的预训练和微调代码。

### 实验或数据
- **数据**：英文生命科学语料（约2200万篇摘要）经翻译得到36.4GB法文语料。
- **实验**：在法文生命科学基准DrBenchmark（包含命名实体识别、关系抽取、文本分类等任务）上微调并评估，与CamemBERT-Bio、DrBERT等现有模型对比。结果显示仅用合成数据预训练的TransBERT-bio-fr在多数任务上达到或超越真实语料模型性能。

### 值得关注点
- 首次系统验证：在英→法高资源翻译方向上，纯合成翻译数据足以训练出高质量领域语言模型。
- 提供完整开源工具链：从翻译、语料库到预训练模型全流程可复现。
- 句子级翻译策略比文档级更快且避免重复问题，实用性高。

### 局限性
- 仅针对法语生命科学领域验证，其他语言或领域的泛化能力未知。
- 依赖英文源语料质量，低资源翻译方向（如非英语源语言）效果未考证。
- 合成翻译可能引入噪声或领域术语偏差，论文未深入分析对下游任务的潜在负面影响。

## 4. FineWeb-CLaR: Culture, Language, and Region Annotations for Benchmark-Aligned Corpus Auditing

- Source: arxiv
- arXiv ID: 2609.25298
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.25298v1
- PDF: https://arxiv.org/pdf/2609.25298v1
- DOI: https://doi.org/10.48550/arXiv.2609.25298

### Authors

Yusser Al Ghussin, Eva Gavaller, Cristina España-Bonet, Josef van Genabith, Simon Ostermann

### Abstract

Cultural evaluation coverage and robustness in language models are difficult to diagnose because pretraining corpora and cultural benchmarks are rarely indexed with comparable metadata. Benchmarks increasingly target culturally situated phenomena at the level of languages, regions, and locale-specific practices, while web-scale corpora are usually organized only by language. A shared culture-language-region layer makes these resources comparable, enabling audits of whether a target cultural phenomenon is represented in pretraining data, evaluated by benchmarks or both. To this end, we introduce FineWeb-CLaR, a large-scale annotated dataset derived from FineWeb and FineWeb-2 that places web documents on a shared culture-language-region axis for corpus auditing and benchmark alignment.
  FineWeb-CLaR annotates the full 30.9B-document collection from FineWeb and FineWeb-2 with URL-derived region labels and cultural-topic provenance. Our region resolver assigns a non-empty region to 25.61% of documents (7.92B). For cultural-topic analysis, we induce locale-specific topics and project them onto the 14 leaves of the Cultural Taxonomy of Liu et al. (2025), producing Locale Topic Distributions (LTDs) for corpus-side comparison. We also annotate 277 cultural NLP benchmarks with the same taxonomy, language coverage, and region coverage. Together, these resources enable direct comparison between corpus-side pretraining evidence and benchmark-side evaluation coverage.

### 中文一句话结论
FineWeb-CLaR为FineWeb和FineWeb-2的309亿文档添加了基于URL的区域标签和文化分类主题元数据，使预训练语料库与文化基准之间的直接审计和对齐成为可能。

### English TL;DR
FineWeb-CLaR annotates the 30.9B-document FineWeb and FineWeb-2 corpora with URL-derived region labels and cultural-taxonomy-aligned topic metadata, enabling direct, large-scale auditing of pretraining data against culturally situated benchmarks.

### 中文详细总结
该研究指出，语言模型的跨文化评估覆盖率和稳健性难以诊断，原因在于预训练语料库和文化基准很少共享可比较的元数据。为了解决这一问题，论文提出了FineWeb-CLaR，一个基于FineWeb和FineWeb-2的大规模注释数据集。该数据集通过URL派生的区域标签和文化分类主题元数据，将网络文档置于共享的文化-语言-区域坐标轴上。具体而言，区域解析器为25.61%的文档（约79.2亿）分配了非空区域标签；同时，通过主题建模在每个语言-区域局部环境中诱导主题，并将这些主题映射到Liu等人提出的文化分类的14个叶节点，生成局部主题分布。此外，研究还注释了277个文化NLP基准，使其具备相同的分类标签、语言覆盖和区域覆盖信息，从而实现了预训练语料证据与基准评估覆盖之间的直接比较。

### 方法 / 贡献
主要贡献包括：
1. **FineWeb-CLaR数据集**：为FineWeb和FineWeb-2添加了区域元数据和文化分类对齐的主题元数据。
2. **可扩展的URL区域归属方法**：基于URL解析（如ccTLD、域名、路径、查询参数）进行区域分配，并附带置信度和解析来源元数据。
3. **文化分类对齐的局部主题分布**：使用BGE-M3嵌入和FASTopic进行主题建模，通过嵌入排名和LLM裁决将主题质心映射到14个文化分类叶节点。
4. **扩展文化基准调查**：在已有工作基础上额外注释了212个文化NLP基准，提供了局部元数据。

### 实验或数据
- 数据规模：FineWeb和FineWeb-2共30,914,158,759个文档。
- 区域解析覆盖：查找表覆盖14.97%（约46.3亿文档），广泛设置（任意非XX区域）覆盖25.61%（约79.2亿文档）。
- 置信度分布：高置信度7.71%，中置信度3.59%，低置信度3.71%。
- 查找表规模：1,335,000条URL签名行。
- 基准注释：277个文化NLP基准被注释。
- 评估：通过与独立自动参考信号（IP地理位置和Open Graph locale）的一致性来验证区域解析器表现，未使用人工标注。

### 值得关注点
- **桥梁作用**：首次在web规模上连接了预训练语料库和文化基准，使研究人员能够诊断特定文化现象是否在预训练数据中存在、是否被基准评估覆盖，或两者皆有。
- **共享轴设计**：通过文化-语言-区域三层元数据，使得不同来源的资源可直接比较，克服了传统仅基于语言索引的局限性。
- **透明度与可靠性**：区域标签附带置信度和解析来源元数据，避免了将噪声信号误认为精确标签，为后续使用提供了可控性。
- **可复制性**：方法设计为可扩展和模块化，可应用于其他web语料库。

### 局限性
- **区域标签的弱监督性**：URL派生的区域标签是弱信号，不代表作者位置、受众位置或文化身份，ccTLD等信号可能具有误导性（如.com域名广泛使用）。
- **缺少黄金标准评估**：由于没有一个“正确”的区域标签定义，无法进行完全人工验证，仅依赖于与自动参考信号的一致性。
- **区域覆盖不完整**：仅25.61%的文档获得区域标签，74.39%的文档无法解析（标记为none）。
- **文化分类的简化**：将复杂文化现象映射到14个叶节点可能过于简化，无法完全捕捉细微的文化差异。
- **语言-区域局部定义**：主题建模在每个语言-区域局部进行，但某些文化现象可能超越单一语言-区域边界。

## 5. Calibration as a First-Class Criterion in LLM Evaluation

- Source: arxiv
- arXiv ID: 2609.26489
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.26489v1
- PDF: https://arxiv.org/pdf/2609.26489v1
- DOI: https://doi.org/10.48550/arXiv.2609.26489

### Authors

Mario Sanz-Guerrero, Katharina von der Wense

### Abstract

Calibration of language models -- the alignment between expressed or implicit confidence and empirical correctness -- is a well-studied subfield within NLP. Methods to measure it already exist. The problem is adoption: outside this subfield, NLP research regularly introduces new models, datasets, and benchmarks without checking whether the model's confidence scores are meaningful. We argue that this adoption gap is a major obstacle to trustworthy LLM evaluation. Miscalibration causes problems in two distinct areas: at deployment, where overconfident mistakes cause real harm, and inside the research pipeline, where methods like LLM-as-a-judge, synthetic data generation, and active learning rely on calibrated confidence without verifying it. Standard calibration metrics only require two inputs per example: a confidence score and a correctness judgment. Most benchmarks in use today already provide both, meaning calibration can be reported immediately. For open-ended generation, however, defining these two inputs is still an open challenge. We argue that each NLP subfield should pair its main performance metric with a calibration score and call for treating calibration as an essential property of every model rather than a niche topic.

### 中文一句话结论
本文主张将校准（模型置信度与真实正确率之间的一致性）提升为LLM评估的一等标准，并呼吁每个NLP子领域在其主要性能指标旁补充校准分数，而不是将其视为小众研究话题。

### English TL;DR
The paper argues that calibration (the alignment between model confidence and correctness) should be treated as a first-class evaluation criterion for LLMs, rather than a niche topic, and that every subfield should pair its main performance metric with a calibration score.

### 中文详细总结
本文指出，校准方法已成熟，但未被广泛采纳是LLM可信评估的主要障碍。校准失败在两个层面造成问题：(1) 部署层面，过度自信的错误会造成实际危害（如法律、医疗场景中的幻觉引用和错误剂量）；(2) 研究流程内部，LLM-as-a-judge、合成数据生成和主动学习等方法都无条件假设模型置信度是可靠的。标准校准指标（ECE、Brier分数、AUROC）仅需每个样本两个输入——置信度分数和正确性判断，而当前多数基准已同时提供两者，因此可以立即报告校准结果。作者审查了GPT-5.5、Claude Sonnet 4.6、Gemini 3.5 Flash、DeepSeek V3.2、Llama 3、Qwen3、Gemma 3、GPT-OSS和OLMo 3等主要模型的技术报告，发现无一报告校准指标（GPT-4是例外）。此外，指令微调和RLHF会损害校准（即使准确率提升），且当前评分机制奖励盲目猜测而非弃权。对于开放式生成任务，如何定义置信度和正确性仍是开放问题，作者建议语义分组作为起点。

### 方法 / 贡献
- **定义层面**：厘清三种置信度信号（token/序列概率、口头化置信度、行为信号）的区别与各自的评估适用场景，以及认知不确定性与偶然不确定性的区分
- **问题诊断**：指出校准采纳鸿沟是阻碍可信LLM评估的主要障碍，并系统分析校准失败在部署和研究管线两大场景中的具体危害
- **指标分析**：评述ECE、Brier分数、AUROC的适用边界，强调它们仅需置信度和正确性两个输入，绝大部分现有基准已可立即报告校准
- **具体建议**：每个子领域应在其主指标旁增加校准分数列；主要排行榜应添加校准列；审稿人应将缺失校准报告视为方法学缺陷；将"自信地犯错"的惩罚高于"不知道"的评分机制改革
- **研究议程**：开放式生成的校准研究（语义分组）应与简单任务上的报告规范并行推进

### 实验或数据
本文无新增实验。作者实例化地审查了九个主要模型家族（GPT-5.5、Claude Sonnet 4.6、Gemini 3.5 Flash、DeepSeek V3.2、Llama 3、Qwen3、Gemma 3、GPT-OSS、OLMo 3）的技术报告和模型卡，发现均报告了数十个能力和安全基准分数但无一报告校准。GPT-4技术报告被引为记录RLHF对校准影响的早期例外。此外引用了现有研究证据：法律领域幻觉引证（Dahl et al. 2024）、医学问答错误（Kim et al. 2025）、以及指令微调后模型置信度膨胀（Sanz-Guerrero et al. 2026）。

### 值得关注点
- 校准是人口层面属性，与准确率相互独立：两个同样90%正确的模型，一个可能知道何时错误，另一个可能完全盲目
- 序列概率是唯一天然存在的置信度信号；口头化置信度对提示措辞敏感；行为信号（如犹豫、拒绝回答）是用户在部署中实际依赖的
- RLHF和指令微调即使提升准确率也会损害校准；对话格式本身使模型对"自己生成的答案"过度自信
- 当前基准对"我不知道"和错误答案同样给零分，导致盲目猜测严格优于弃权，直接促进幻觉
- AUROC衡量的是排序能力而非校准数值本身，模型将所有置信度整体膨胀后AUROC不变

### 局限性
- 对九个模型报告的审查被作者明确声明为"例证而非完整调查"，可能遗漏个别报告校准的案例
- 开放式生成中如何定义置信度和正确性仍是开放问题，语义分组方法标准化和跨任务分析尚未完成
- 对校准缺失的后果论证主要基于文献引用而非作者自己的系统实证验证
- 未讨论校准分数与现有排行榜总分如何加权或折中，也未提供具体实施指南
- 校准评估需要每个样本的置信度和正确性标签，但在人工参与的真实部署中，正确性往往无法即时获得

## 6. Differentiable Fuzzy Inference Layer: A Monotone, Compositional Ordinal Reasoning Head for Large Language Models

- Source: arxiv
- arXiv ID: 2609.26113
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.26113v1
- PDF: https://arxiv.org/pdf/2609.26113v1
- DOI: https://doi.org/10.48550/arXiv.2609.26113

### Authors

Zhen Zhang, Amr Alanwar

### Abstract

A state-of-the-art language model asked to interpret "most of most students passed" typically answers "most," though composing two instances of "most" yields a proportion closer to "some." We trace this failure to an architectural choice rather than a data deficit: standard classifier heads treat ordinal categories as independent labels, with no mechanism to respect their natural ordering or compose them algebraically. We introduce the Differentiable Fuzzy Inference Layer (DFIL), a dual-path prediction head pairing a standard classifier with a scalar-bottlenecked branch grounded in a bank of ordered membership functions. DFIL supplies two structural primitives that a label-only head cannot inherit: monotonicity in the underlying quantity, and compositional reasoning via t-norm operations without any compositional training data. The scalar branch additionally provides an interpretable interface for analyzing residual errors. We instantiate DFIL on ordinal natural-language tasks across diverse LLM families.

### 中文一句话结论
该论文提出可微模糊推理层（DFIL），通过在大型语言模型的预测头部引入标量瓶颈分支与有序隶属函数和 t-范数运算，从架构上保证了序数推理的单调性和组合性，使模型能够正确地将“most of most”组合推理为“some”而非“most”。

### English TL;DR
The paper introduces the Differentiable Fuzzy Inference Layer (DFIL), a dual-path prediction head for LLMs that combines a standard classifier with a scalar-bottlenecked branch using ordered membership functions and t-norm operations. DFIL provides two structural primitives standard heads lack: monotonicity in the underlying quantity and compositional reasoning without any compositional training data, fixing failures like interpreting "most of most students passed" as "most" instead of "some."

### 中文详细总结
论文指出，SOTA 语言模型在解释“most of most students passed”时通常回答“most”，但两次“most”的组合比例更接近“some”（0.78×0.78≈0.61）。作者将这一失败归因于架构选择而非数据不足：标准分类头将序数类别视为独立标签，没有机制尊重其自然排序或以代数方式组合它们。作者提出 DFIL——一个双路径预测头，将标准分类器与一个基于有序隶属函数库的标量瓶颈分支配对。DFIL 提供两个标签仅分类头无法继承的结构原语：底层数量的单调性，以及通过 t-范数运算实现的组合推理——且无需任何组合训练数据。标量分支还提供了一个可解释的接口用于分析残差误差。作者在多个 LLM 家族上对序数自然语言任务进行了 DFIL 实例化，并证明了两个结构保证定理（单调最近中心推理和比例平移下的组合封闭性）。

### 方法 / 贡献
- **DFIL 架构**：双路径预测头，主路径为标准分类器，DFIL 路径通过小型数值头提取标量 $\hat{p}\in[0,1]$，并将其投影到一组学习到的有序高斯隶属函数上，与主干网络端到端联合训练。
- **单调性**：采用最近中心决策规则（$\arg\min_q |p-c_q|$），由有序中心 $c_0<c_1<\cdots<c_{Q-1}$ 保证预测随 $p$ 单调不减（定理 1）。
- **组合性**：利用乘积 t-范数在比例层面进行组合，定义比例平移组合算子 $Q^{(n)}$，证明深层组合不会预测高于基础类别的结果（定理 2）——“most of most” ≤ “most”。
- **理论贡献**：证明有序高斯隶属函数能精确实现 $[0,1]$ 上的任意 $Q$ 步单调目标；证明任何 $d\geq 2$ 维隐藏状态上的线性头无法保证单调性。
- **可解释性**：标量分支提供可解释的接口，用于分析残差误差。
- **参数开销**：基于 LoRA，额外增加约 0.9–2.1M 参数（取决于主干大小）。

### 实验或数据
根据提供的摘要和正文预览：论文在六个 LLM 主干上实例化 DFIL，报告称 DFIL 在单步准确率上与微调持平，同时在组合推理、低预算样本效率和自然语言单调一致性方面有可测量的提升。论文参考了 FRoG 基准（记录了量化推理上的逆缩放现象），并提到与 PRESQUE 的对比中 DFIL 在 FRoG-Hard 上高出 25 个百分点以上。此外，一个初始化鲁棒性实验将模糊训练信号隔离为组合优势的因果机制。但摘要和预览中未提供具体的数据集规模、完整实验设置或详细数值结果表。

### 值得关注点
- 论文将 LLM 量化推理失败归因于**预测头的架构限制**而非数据不足，这一诊断本身具有价值。
- DFIL 无需组合训练数据即可实现组合推理，是显著的实用优势。
- 提供了严格的数学保证（单调性和组合封闭性定理），而非仅凭经验观察。
- 与多种基线（LoRA 微调、CORAL、LaSQuE、PRESQUE、ANFIS）的系统对比，展示 DFIL 是唯一同时满足全部六项头部能力的方法。

### 局限性
所提供的摘要和正文预览中未明确列出局限性部分。根据文中信息可合理推断的局限包括：DFIL 增加了约 0.9–2.1M 的额外参数开销；组合推理采用比例平移形式（$p \mapsto c_{q_1}p$），可能不涵盖所有类型的组合语义；论文未提供完整实验数据表，无法评估各主干上的详细性能差异；组合封闭性定理仅针对比例平移推理规则，其他 t-范数变体仅在附录中讨论。

## 7. ufakzeka-1: Building and Evaluating a 151M-Parameter Turkish Language Model from Scratch

- Source: arxiv
- arXiv ID: 2609.25081
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.25081v1
- PDF: https://arxiv.org/pdf/2609.25081v1
- DOI: https://doi.org/10.48550/arXiv.2609.25081

### Authors

Sait Furkan Teke

### Abstract

We describe ufakzeka-1, a 151M-parameter (182M with embeddings) decoder-only Turkish language model pretrained from scratch on 13.5B tokens of openly licensed text and instruction-tuned for chat, at a total cost of about \$286 in cloud GPU, API and notebook time. The contribution is not the model's capability, which is what a model this size can be expected to have, but the record of building and measuring it: a Turkish byte-level tokenizer at 1.77 tokens per word, a three-stage pretraining schedule, a post-training mixture of openly licensed and generated data, and an evaluation battery of release gates, a rule-checked sweep of 5,508 conversations, judged conversations and hand tests, all with prompts held out from the training data, enforced by decontamination inside the data build and by a checked-in invariant script we run before each build. We report three findings that we believe transfer to other small-model efforts: a safety gate that had been "fixed" with training data written from its own questions read 64/64 while the honest figure was 34/64; training-seed variance was as large as the spread across every recipe we tried, so single-seed comparisons at this scale are uninformative; and data rounds repaired only what was absent from the data, while identity tracking over long context and multi-turn arithmetic did not move across any data change we tried, which we read as limits of the model size rather than gaps in the data, a reading the next, larger model will test. Weights, the data recipe, the evaluation code and the spend ledger are released under Apache-2.0.

### 中文一句话结论
本文记录了用约286美元从头构建一个151M参数的土耳其语小语言模型的全过程，并揭示了三个对开发小模型具有普遍借鉴意义的发现：修复安全门的方式会隐藏真实失败率、训练种子随机性导致单种子实验无意义，以及部分能力（如长上下文身份跟踪和多轮算术）受限于模型规模而非数据量。

### English TL;DR
This paper documents the construction and rigorous evaluation of ufakzeka-1, a 151M-parameter Turkish language model built from scratch for ~$286, yielding three transferable findings for small-model development: safety gate fixes can mask true failure rates (64/64 vs. honest 34/64), training-seed variance rivals recipe differences (making single-seed comparisons uninformative), and certain capabilities (long-context identity tracking, multi-turn arithmetic) are limited by model size rather than data gaps.

### 中文详细总结
本文介绍了ufakzeka-1，一个151M参数（含嵌入层182M）的纯解码器土耳其语语言模型，从头训练于135亿token的开放许可文本，并进行了指令微调以支持对话功能。项目总成本约286美元（含云GPU、API和笔记本时间）。作者的核心贡献不在于模型性能（此规模模型性能符合预期），而在于完整的构建与评估记录：土耳其语字节级分词器（1.77 token/词）、三阶段预训练方案、混合开放许可与生成数据的后训练，以及包含发布门控测试、5,508轮对话规则检查、LLM评判对话和人工测试的评估体系。所有评估提示均与训练数据隔离，通过数据构建中的去污染措施和构建前运行的固定检查脚本确保。论文报告三个可推广到其他小模型项目的发现：用自身问题修复的安全门会隐藏真实失败率（测试显示64/64完美通过，实则真实通过率仅34/64）；训练种子随机性导致的性能波动与不同配方的差异相当，因此此规模下单种子比较无意义；数据轮次只能修复数据中缺失的问题行为，而长上下文身份跟踪和多轮算术问题在多次数据调整后均未改善，表明是模型规模限制而非数据缺陷，需更大模型验证。

### 方法 / 贡献
- **模型架构**：24层，隐藏层768维，12个注意力头含4个KV头（分组查询注意力），SwiGLU前馈网络，RoPE位置编码，QK归一化，RMSNorm，输入输出嵌入共享。布局与Qwen3一致，可直接加载为标准`Qwen3ForCausalLM`。
- **分词器**：字节级BPE，词表40,960，训练于25GB土耳其语文本。预分词器为Qwen2正则表达式变体（移除英语缩写规则以正确处理土耳其语撇号后缀），平均1.77 token/词。
- **预训练三阶段**：
  1. 6.5B token：Muon优化器+AdamW（嵌入层）+预热-稳定-衰减调度
  2. 5.5B token：Hyperball归一化Muon变体+QA数据层
  3. 1.5B token：移除logit软上限+上下文扩展至4,096+混合近期数据
- **后训练**：154,506个对话监督微调，39,105个序列，3轮训练。混合比例：生成故事/多轮对话22%、公开土耳其语指令集27%、Wikipedia句子知识13%、长拼接会话8%、短故事8%、模板化家族（算术/安全/身份等）约12%。
- **评估体系**：发布门控9项测试、22类5,508轮规则检查对话、LLM评判对话、人工测试。

### 实验或数据
- **预训练数据**：所有来源均为商业许可（FineWeb2-HQ土耳其语、mogan土耳其语爬虫、FinePDFs-edu、FineWiki、BILGEM合成数据、COSMOS合成语料、FineMath英语数学4%）。经过去重、URL去重、13-gram去污染、脱敏。
- **后训练数据**：公开指令集（Turkish-SFT-Dataset-v1.0, diyalog-dataset, Turkce-Atlas-Instruct, Aya土耳其语拆分等）+ 生成数据（故事、多轮对话）+ Wikipedia引导句知识+模板化数据族。
- **基准测试**：HellaSwag、ARC（土耳其语版）、XCOPA、Belebele、TurBLiMP、TurkishMMLU，零-shot对数似然评估。结果：ufakzeka-1在ARC-easy和XCOPA落后于5倍规模模型不到3分；指令微调使HellaSwag/TurBLiMP损失约2分，TurkishMMLU提升4分。
- **评估结果**：5,508轮对话中5,190通过；算术最弱（1,000中807通过）；LLM评判有用性79.2（4.2%回避率），日常能力84.5；人工测试50轮中27好/9弱/14差。

### 值得关注点
1. **低预算可行性**：总成本仅约286美元（含H100 GPU约66美元、API等），证明小规模模型可从零训练且全流程文档化
2. **安全门测试陷阱**：用问题本身训练修复后测试表现完美（64/64），但改用未见变体时真实通过率仅34/64，提示需严格分离评测与训练模板
3. **种子随机性影响**：同一配方三种子在有用性上产生6分差异，身份门故障数从3到18不等，建议小规模实验至少用三种子
4. **模型规模瓶颈**：长上下文身份跟踪、多轮算术等能力在所有数据调整后均无改善，明确指向模型规模限制而非数据问题
5. **完整开源**：权重、数据配方、评估代码、支出账目均以Apache-2.0许可发布

### 局限性
1. **模型规模限制**：151M参数导致多项能力（长上下文身份跟踪、多轮算术、拒答坚持问题）无法通过数据改善，需更大模型验证
2. **人工测试样本有限**：仅50轮人工测试，且由开发用AI助手而非独立人类评估，结果仅具指示性
3. **部分基准接近随机水平**：ARC-challenge、Belebele、TurkishMMLU上所有模型（包括更大模型）均接近随机水平，表明这些任务在当前规模下难以有效区分模型能力
4. **DPO尝试失败**：偏好优化（DPO）在此规模下降低对话质量，最终仅使用SFT检查点
5. **评判分数不可复现**：LLM评判所用评判模型标识符未公开，仅提供转录和分数而非复现方法
6. **特定语言局限性**：分词器针对土耳其语优化，llama.cpp需要专用补丁（15行修改），非标准配置可能带来兼容性问题

## 8. Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training

- Source: arxiv
- arXiv ID: 2609.25510
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.25510v1
- PDF: https://arxiv.org/pdf/2609.25510v1
- DOI: https://doi.org/10.48550/arXiv.2609.25510

### Authors

Jacob Beck, Philip V. Ogren, Ari Kobren

### Abstract

Large language models (LLMs) can improve solutions to verifiable scientific and algorithmic problems by spending additional computation at test time. Recent systems achieve strong results with increasingly elaborate evolutionary search harnesses or by updating model parameters during test-time training. We ask how much of this machinery is necessary. We introduce Hill Sampling, a simple procedure that repeatedly samples candidate program edits from a frozen LLM, retains the best program found so far, and conditions all subsequent samples on that program. We evaluate the method on circle packing, sums/differences of sets, and Erdos' minimum-overlap problem using three open-weight models. Hill Sampling sets a new state of the art on circle packing among published methods, improves over the AlphaEvolve reference on Erdos' minimum-overlap problem, and achieves strong results on sums and differences of finite sets. The circle-packing and Erdos results require only hours of wall-clock time on eight NVIDIA H100 GPUs. To our knowledge, we also conduct, the largest study, by parameter count, of evolution strategies (ES) applied directly to LLM weights at test time. Surprisingly, learning the weights is worse than setting the ES learning rate to zero: at zero learning rate, the method is still searching in weight space through fixed random perturbations. Those perturbations can help exploration, but randomness from token sampling is stronger still, and repeated sampling remains substantially weaker than Hill Sampling. These results suggest a simple test-time compute allocation strategy: repeatedly sample edits to the best verified solution found so far, before introducing additional complexity such as adding archives, diversity mechanisms, evolutionary scaffolds, or test-time parameter learning.

### 中文一句话结论
Hill Sampling——一种从冻结的LLM中反复采样程序编辑并始终以当前最优解为条件的简单方法——在多个科学/算法问题上超越了更复杂的进化搜索与测试时训练方法，并取得了新的最优结果。

### English TL;DR
Hill Sampling, a simple procedure that repeatedly samples program edits from a frozen LLM while conditioning on the best solution found so far, achieves state-of-the-art results on several scientific and algorithmic problems, outperforming more complex evolutionary and test-time training methods.

### 中文详细总结
本文提出Hill Sampling，一种极简的测试时计算分配策略：从冻结的LLM中反复采样候选程序编辑，保留迄今为止找到的最优程序，并让所有后续采样都以此最优程序为条件。作者在三个可验证问题（圆填充、集合的和/差、Erdos最小重叠问题）上使用三种开放权重模型进行评估。结果显示，Hill Sampling在圆填充问题上达到了已发表方法的新SOTA，在Erdos最小重叠问题上优于AlphaEvolve基线，在有限集合的和与差上也取得了强结果。此外，作者进行了截至目前按参数规模最大的进化策略（ES）直接应用于LLM权重的测试时研究，发现学习权重（非零学习率）反而不如将ES学习率设为零（仅固定随机扰动搜索权重空间）。但随机扰动带来的探索效果弱于token采样的随机性，而重复采样（不加条件）也明显弱于Hill Sampling。这表明，在引入档案、多样性机制、进化支架或测试时参数学习等额外复杂度之前，先对当前最优解反复采样编辑是一个简单且更优的选择。

### 方法 / 贡献
- 方法：Hill Sampling —— 从冻结LLM中反复采样程序编辑，每次以当前最优程序为条件（贪婪保持最优）。
- 贡献1：证明了极简方法可超越复杂的进化搜索和测试时训练，挑战增加复杂度是否必要的假设。
- 贡献2：进行了最大参数规模的ES直接应用于LLM权重的测试时研究，发现权重学习不如零学习率的随机扰动。
- 贡献3：提出简单的测试时计算分配策略：优先对最优解反复采样编辑，不必引入额外复杂性。

### 实验或数据
摘要提及的实验任务：圆填充（circle packing）、集合的和/差（sums/differences of sets）、Erdos最小重叠问题。使用三种开放权重模型。计算资源：圆填充和Erdos任务仅需8块NVIDIA H100 GPU数小时。摘要未提供具体数据集名称或详细数值结果。

### 值得关注点
- Hill Sampling在圆填充上超越所有已发表方法，达到新SOTA。
- 在Erdos问题中优于AlphaEvolve参考。
- ES学习率设为零（仅随机扰动）反而优于学习权重，但不如token采样随机性。
- 重复采样（无条件）显著弱于Hill Sampling，强调条件采样的价值。
- 方法极简，易于复现，且计算开销低。

### 局限性
摘要未明确讨论局限性。根据方法特性，Hill Sampling依赖可验证的奖励函数（适用于科学和算法问题），可能无法直接应用于开放式或主观评价任务。此外，实验仅限三个问题，未测试更广泛任务或更大规模模型。

## 9. A retrospective analysis on the use of LLMs to study infant syntax learning

- Source: arxiv
- arXiv ID: 2609.26539
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.26539v1
- PDF: https://arxiv.org/pdf/2609.26539v1
- DOI: https://doi.org/10.48550/arXiv.2609.26539

### Authors

Hélie Bazin, Anouk Barberousse, François Yvon

### Abstract

Large language models (LLMs) have increasingly been used to investigate how children acquire syntax at an early stage of development. This is notably the central scientific goal of the BabyLM challenge, a community-wide effort to develop models that achieve human-level syntactic performance while being trained on developmentally realistic corpora. In this paper, we reflect on the use of LLMs in the study of infant syntax learning by providing an epistemological assessment of several studies from this research program. We discuss how datasets are built, which models are implemented, how they are trained and syntactically evaluated. We observe significant assumptions in the methodology of BabyLM and related studies, thus mitigating their theoretical scope. We additionally observe that using developmentally-realistic corpora have limited effects on models performance on commonly-used benchmarks, which suggest important computational differences between LLMs and the infant syntax learner.

### 中文一句话结论
本文通过认识论评估指出，使用LLM研究婴儿句法习得时存在显著的方法论假设，且发展现实语料库对模型性能影响有限，表明LLM与婴儿句法学习者在计算上存在重要差异。

### English TL;DR
This paper provides an epistemological assessment of using LLMs to study infant syntax learning, concluding that significant methodological assumptions limit theoretical scope and that developmentally-realistic corpora have restricted effects on syntactic benchmarks, highlighting key computational differences between LLMs and infants.

### 中文详细总结
本文对BabyLM挑战及相关研究进行了认识论反思，系统分析了如何构建面向儿童的语料库、选择何种模型架构、训练方式及句法评估方法。研究发现，这些研究在方法论上存在重要假设（如语料库中儿童导向语音的比例、训练轮数等），限制了其理论解释力。此外，使用发展现实语料库对模型在常见句法基准（如BLiMP）上的表现提升有限，说明LLM与婴儿句法学习者之间存在显著计算差异。

### 方法 / 贡献
- **方法**：对BabyLM挑战及若干相关研究进行系统性方法论审查，比较不同模型在句法基准上的表现。
- **贡献**：揭示了该研究范式的方法论假设（如数据集构成、训练策略）如何削弱其理论范围；明确指出发展现实语料库在提升模型句法能力上的局限性，为后续认知建模提供批判性视角。

### 实验或数据
本文未进行新的实验或构建新数据集，而是回顾并比较了多项已有研究（如BabyLM各届竞赛、使用CHILDES语料库的模型等）的语料库构成、模型规模和句法基准表现。

### 值得关注点
- **方法论假设**：语料库中儿童导向语音比例的定义模糊，不同研究差异大（0%–100%），影响结论可比性。
- **有限效果**：即使使用发展现实语料库，模型在常见句法基准上提升有限，暗示当前LLM架构与婴儿学习机制的本质差异。
- **计算差异**：训练轮数（多epoch）等实践与婴儿一次性暴露的现实不符，进一步削弱模拟合理性。

### 局限性
论文未明确讨论自身局限性，但作为回顾性分析，其观察依赖于所审查研究的质量和假设。此外，分析范围局限于BabyLM挑战及少量相关研究，未涵盖跨模态、交互等更丰富的婴幼儿语言学习场景。

## 10. ClusterFewshot: Improving Few-shot Optimization for LLMs workflow

- Source: arxiv
- arXiv ID: 2609.25939
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.25939v1
- PDF: https://arxiv.org/pdf/2609.25939v1
- DOI: https://doi.org/10.48550/arXiv.2609.25939

### Authors

Omri Bar Haim, Shahar Katz, Lior Wolf

### Abstract

The performance of large language model (LLM) workflows often depends on selecting a small set of in-context demonstrations to guide model behavior on new tasks. Recent methods improve this process by augmenting prompts with successful reasoning paths. However, their demonstration selection relies on random sampling or metric-based rankings, overlooking the semantic structure of the task. We propose ClusterFewshot, a strategy that combines semantic structuring with utility-aware scoring to construct representative and effective few-shot demonstration sets. Evaluated within DSPy-based pipelines, ClusterFewshot substantially reduces optimization cost across multiple benchmarks, while consistently improving accuracy relative to prior bootstrap-based methods in both standalone prompt tuning and hybrid prompt-weight optimization.

### 中文一句话结论  
ClusterFewshot 通过语义聚类与效用评分结合，在降低优化成本的同时提升少样本演示选取质量，在多种基准上优于现有基于随机或指标排序的方法。  

### English TL;DR  
ClusterFewshot combines semantic clustering with utility-aware scoring to improve few-shot demonstration selection for LLM workflows, reducing optimization cost and boosting accuracy on multiple benchmarks compared to prior bootstrap-based approaches.  

### 中文详细总结  
本文提出 **ClusterFewshot**，一种面向大语言模型（LLM）工作流的少样本演示选取策略，旨在解决现有方法（如随机搜索或基于指标的排序）忽视任务语义结构的问题。该方法首先对训练示例进行语义嵌入和K-means聚类（通过网格搜索选择最佳嵌入模型与聚类数），然后从每个类中选取代表性样本，并利用在验证集上的一轮评估（one-shot scoring）计算每个候选示例的效用。最终从全局Top-k和每个类最佳结果中选优。在基于DSPy的管道中，ClusterFewshot在三个基准（GSM8K、HotPotQA、Iris）上显著降低了优化成本（如所需评估次数），并在纯提示优化和混合提示-权重优化中均保持或提升了准确率。此外，该方法在ReAct智能体场景下也表现出灵活性，并对不同模型大小、模型家族及聚类采样方式具有鲁棒性。  

### 方法 / 贡献  
1. 识别出现有演示选取流程中缺乏语义信息的关键局限。  
2. 提出ClusterFewshot，将语义聚类（嵌入后K-means）与效用驱动评分（基于验证子集的一轮评估）结合，指导少样本演示构建。  
3. 在独立的提示优化与混合提示-权重优化（如BetterTogether）管道中，验证了ClusterFewshot在降低优化成本的同时提升或保持准确率。  
4. 拓展到ReAct智能体场景，并评估了不同模型尺寸、模型家族和聚类采样策略下的鲁棒性。  

### 实验或数据  
- 实验在**DSPy**框架内实现，并与**BootstrapFewShotRS（BFRS）** 和**MIPROv2**等基线对比。  
- 使用三个基准：**GSM8K**（数学推理）、**HotPotQA**（多跳问答）、**Iris**（分类）。  
- 评估场景包括纯提示优化与混合提示-权重优化（即与LoRA微调交替）。  
- 额外进行了ReAct智能体设置下的测试，以及不同模型大小（如不同规模LLM）和不同嵌入模型（all-mpnet-base-v2，gtr-t5-base，bge-large-en-v1.5，Qwen3-Embedding-0.6B）的消融实验。  
- 优化成本（即所需引导轮次/评估数）显著降低，准确率在多数设置中更高或持平。  

### 值得关注点  
- 将**语义结构**引入自动演示选取流程，弥补了现有优化器忽视示例分布的缺陷。  
- 通过一次引导+聚类+单次打分，避免了对随机搜索的大量重复评估，大幅降低计算开销。  
- 在混合优化（提示+微调）中仍保持优势，说明语义选取与参数微调可协同工作。  
- 方法对嵌入模型和聚类数选取具有自动校准机制（基于轮廓系数），适应性较强。  

### 局限性  
- 仅评估了基于引导（bootstrap）的优化管道，与其他黑盒提示优化方法（如直接偏好优化、强化学习）的比较未涉及。  
- 依赖嵌入模型的质量，虽然通过网格搜索选择最优模型，但在罕见任务或跨语言场景下的泛化性尚未验证。  
- 未明确讨论大规模任务（如数千示例）时的计算开销，虽然一次引导降低重复成本，但聚类和评分步骤仍可能带来额外时间。  
- 实验仅在三个基准上开展，缺乏更多样化任务（如开放域生成、长文本推理）的验证。  
- 论文未提及对非英文任务或低资源设置下的表现。

## Processing Notes

- Duplicate papers skipped: 0