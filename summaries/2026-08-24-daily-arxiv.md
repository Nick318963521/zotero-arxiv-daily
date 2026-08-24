# Daily arXiv - 2026-08-24

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-24T22:52:07
- Paper count: 10

## 1. MGAL: A Multilingual Granularity-Aware Long-Context Benchmark

- Source: arxiv
- arXiv ID: 2608.20853
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.20853v1
- PDF: https://arxiv.org/pdf/2608.20853v1
- DOI: https://doi.org/10.48550/arXiv.2608.20853

### Authors

Chunhan Li, Chenglin Xu, Zongyang Zhang, Jiale Liu, Zhuoxi Rao, Xudong Jia, Junxiu He, Menglin Yang, Wenjuan Gong, Zhengzhe Liu, Chengwei Qin

### Abstract

Evaluation of long-context Large Language Models (LLMs) has advanced rapidly. However, most existing benchmarks are limited to the document level and focus mainly on high-resource languages, leaving many fine-grained challenges insufficiently evaluated. To address this gap, we present MGAL, the first multilingual, granularity- and position-aware long-context benchmark. MGAL is constructed from United Nations (UN) reports spanning 8K to 128K tokens across the six official UN languages. It covers four coherent levels of linguistic granularity (word, sentence, paragraph, and document) and further stratifies entries by their position within the document (begin, middle, and end), indexed at both the document and paragraph levels. This design enables systematic diagnosis of multilingual long-context comprehension across different granularities.
  Through extensive experiments and analyses, we find that: (1) LLMs perform well at word-level tasks but struggle with coarser-grained ones; and (2) Closed-source models retain a clear performance advantage in lower-resource languages. We further identify two new challenges: (1) Under local semantic crowding, where neighboring sentences share topics and entities, models tend to follow surface cues (e.g., connectives like ``however'' or repeated entities) rather than the discourse role of the sentence in surrounding context (e.g., background, outcome); and (2) A gap between fluency and consistency in generated outputs, where models produce text that reads smoothly but drifts from the source facts. In addition, we observe several patterns in line with prior studies, including reliance on nearby evidence and reuse of options under uncertainty.

### 中文一句话结论
MGAL是首个多语言、细粒度与位置感知的长上下文基准，通过覆盖六种联合国官方语言和四种语言粒度（词、句、段、文档），系统揭示了LLM在粗粒度任务上的不足以及闭源模型在低资源语言中的优势。

### English TL;DR
MGAL introduces the first multilingual, granularity- and position-aware long-context benchmark that systematically evaluates LLMs across six UN languages and four linguistic granularities, revealing that models excel at word-level tasks but struggle with coarser-grained ones and that closed-source models maintain a clear advantage in lower-resource languages.

### 中文详细总结
该基准从联合国报告中构建，上下文长度为8K到128K token，覆盖六种联合国官方语言（英语、中文、西班牙语、法语、俄语、阿拉伯语）。MGAL设计了四个粒度级别（词、句、段、文档）共七项任务，每种语言各有420个查询-响应对。任务包括词级QA、句级完形填空、段级填充、文档级摘要和翻译。所有条目均经过手动审核以保证质量。实验评估了12个长上下文LLM，发现：(1) 模型在词级任务表现良好，但在粗粒度任务（如段、文档级）上困难重重；(2) 闭源模型在低资源语言中优势明显。论文还识别了两个新挑战：局部语义拥挤（模型依赖表面线索而非话语角色）和生成输出的流畅性与一致性之间的差距（输出流畅但事实漂移）。此外，观察到模型倾向于依赖邻近证据和在不确定时重复使用选项等模式。

### 方法 / 贡献
1. 提出了MGAL，首个多语言、细粒度与位置感知的长上下文基准，覆盖六种联合国官方语言，上下文长度达128K token。
2. 通过粒度（词、句、段、文档）和位置（文档内开始、中间、结束）两维度分解评估，实现比现有文档级基准更严格的诊断。
3. 对12个长上下文LLM进行了全面评估，并利用MGAL作为诊断测试平台，分析了粒度依赖退化、位置敏感性、局部语义拥挤和流畅性-一致性差距等限制。

### 实验或数据
数据来自联合国数字图书馆报告，覆盖六种官方语言，上下文长度8K–128K token。每种语言包含420个查询-响应对，覆盖七项任务：词级Single-QA和Multi-QA（准确率）、句级Cloze（准确率）、段级Filling（Rouge-L）、文档级Summarization（Rouge-L）和Translation（BLEU）。实验评估了12个长上下文LLM，包括开源和闭源模型。未提及具体模型名称或额外数据集。

### 值得关注点
1. 多语言覆盖：首次在单一基准中同时评估六种联合国官方语言（包括阿拉伯语、俄语等低资源语言）的长上下文理解。
2. 细粒度与位置感知：同时控制语言粒度和证据位置（文档内和段落级别），能进行更系统的诊断。
3. 发现新挑战：局部语义拥挤和流畅性-一致性差距为长上下文LLM研究提供了新方向。
4. 与现有基准对比：MGAL在最大长度（128K）、语言覆盖（6种）和位置/粒度评估方面优于LongBench、RULER等基准。

### 局限性
1. 基准仅基于联合国报告，可能无法代表所有长上下文场景（如小说、技术文档等），领域覆盖有限。
2. 评估指标主要依赖参考指标（准确率、Rouge-L、BLEU）和LLM-as-a-judge，可能无法完全捕捉生成质量的所有方面。
3. 实验仅评估了12个模型，可能未涵盖所有最新或特定领域的长上下文LLM。
4. 数据构建涉及手动审核，但未讨论审核者间一致性和潜在偏差。
5. 未详细说明任务难度与语言资源的关系，如低资源语言中任务的具体表现差异原因。

## 2. When Do LLMs Replace Fine-Tuned NLU? A Decision Framework for Intent Detection in Production Conversational Systems

- Source: arxiv
- arXiv ID: 2608.20371
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.20371v1
- PDF: https://arxiv.org/pdf/2608.20371v1
- DOI: https://doi.org/10.48550/arXiv.2608.20371

### Authors

Carson Rodrigues, Oysturn Vas

### Abstract

A common claim is that zero-shot large language models (LLMs) can replace fine-tuned NLU classifiers for intent detection. We test this claim head-to-head and find that the honest answer is: it depends on the intent space. On full ATIS and CLINC150 we compare a fine-tuned RoBERTa, a TF-IDF+logistic-regression baseline, sentence-embedding kNN, and Claude Haiku zero-shot, reporting bootstrap 95% confidence intervals and paired significance tests. When abundant in-domain labels exist, fine-tuned RoBERTa is as good or better and three orders of magnitude cheaper and faster: on ATIS it beats Claude zero-shot by 11.8 points (95.9 vs. 84.1, p<0.001). On the broad 150-intent CLINC150 schema the two are statistically tied (89.1 vs. 88.5, p=0.24): the LLM matches a fully supervised model with no training data. The LLM's advantages appear in three production-relevant regimes: out-of-scope detection (OOS recall 85.6 vs. 58.1 for RoBERTa); robustness to realistic ASR noise via a controlled text-to-speech to noise to Whisper pipeline (92.5 vs. 80.0 at 0 dB); and dynamic per-deployment schemas, where a classifier trained on one app's intents scores 0% on a new app's intents while the schema-prompted LLM serves both at ~94% with zero retraining. We distill these findings into a decision framework for practitioners.

### 中文一句话结论
零样本LLM在动态、标签稀缺的意图空间或需要检测超出范围（OOS）的意图时优势明显，但在数据丰富、意图稳定的场景下，微调模型更准确、更快速、成本更低。

### English TL;DR
Zero-shot LLMs can match or exceed fine-tuned NLU classifiers for intent detection only under specific conditions—such as dynamic schemas, label scarcity, or out-of-scope detection needs—while fine-tuned models remain cheaper, faster, and more accurate when abundant in-domain labels are available.

### 中文详细总结
该论文对比了零样本大语言模型（LLM，Claude Haiku）与多种传统微调方法（TF-IDF+LR、句嵌入kNN、微调RoBERTa）在意图检测任务上的性能。实验在ATIS和CLINC150两个基准数据集上进行，并进行了鲁棒性统计检验。主要发现：

- **数据丰富场景**：在ATIS数据集上，微调RoBERTa准确率达95.9%，显著优于Claude的84.1%（p<0.001），且推理速度快1000倍、成本为零。
- **意图空间宽泛场景**：在CLINC150的150个意图上，LLM与微调模型性能相近（88.5% vs 89.1%，无显著差异）。
- **超出范围检测**：LLM在OOS召回率（85.6%）和F1（85.0%）上远优于微调模型（58.1% / 73.0%）。
- **动态Schema**：将CLINC150分为两个不重叠的应用Schema时，微调模型在新Schema上准确率为0%，而LLM通过提示Schema即可同时处理，准确率约94%。
- **ASR鲁棒性**：通过合成语音加噪、Whisper转录，LLM在0dB SNR下准确率92.5%，显著高于TF-IDF+LR的80.0%。

论文最终提出一个决策框架，指导从业者根据意图空间特性选择模型：稳定且数据丰富时用微调模型；动态、标签稀缺、OOS重要或噪声严重时用LLM；也可使用微调模型+LLM混合方案。

### 方法 / 贡献
- **全面对比实验**：在完整ATIS和CLINC150上，采用bootstrap 95%置信区间和配对显著性检验，系统比较了TF-IDF+LR、句嵌入kNN、微调RoBERTa和Claude Haiku零样本。
- **三个生产相关压力测试**：显式OOS检测、真实ASR噪声鲁棒性（通过TTS+加噪+Whisper管道）、以及动态Schema场景（新应用Schema下微调模型无法工作）。
- **决策框架**：将意图空间属性映射到合适模型，包括微调模型不可用的情形。

### 实验或数据
- **数据集**：完整ATIS（26意图，4978训练/893测试）和CLINC150（150意图+OOS类，5500测试）。
- **系统**：TF-IDF+LR、句嵌入kNN（含5-shot变体）、微调RoBERTa-base、Claude Haiku零样本。
- **统计方法**：bootstrap 95%置信区间，配对显著性检验。
- **ASR鲁棒性**：120条CLINC语句通过TTS合成，添加白噪声（干净/20/10/5/0 dB SNR），Whisper-base转录后分类，按WER分层。
- **动态Schema**：将CLINC150的150个意图分为两个不重叠的75意图应用（A和B），微调模型只在A上训练，LLM通过提示获取对应Schema。

### 值得关注点
- 微调模型在ATIS上显著优于LLM（+11.8点），且成本极低（毫秒级延迟，零边际成本）。
- LLM在OOS检测上召回率极高（85.6 vs 58.1），这对安全部署至关重要。
- 动态Schema场景中，微调模型完全无法处理新Schema（准确率0%），而LLM通过提示即可适配。
- 在ASR噪声环境下，LLM退化更平缓（0dB时+12.5点）。

### 局限性
- 仅评估了英文数据集（ATIS、CLINC150）；多语言、多意图、多轮设置未涵盖。
- ASR研究使用受控TTS+加噪，而非完全自然的语料（如SLURP）。
- 仅测试了Claude Haiku一种LLM和RoBERTa-base一种编码器；更大模型会改变绝对值，但不会改变框架的条件性结构。
- 动态Schema测试使用干净的意图划分；生产中的Schema可能有重叠，会减弱微调模型的无能程度。

## 3. Beyond Prompt Engineering: A Systematic Analysis of Prompt Lexical Sensitivity and Its Impacts on Quality

- Source: arxiv
- arXiv ID: 2608.20349
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.20349v1
- PDF: https://arxiv.org/pdf/2608.20349v1
- DOI: https://doi.org/10.48550/arXiv.2608.20349

### Authors

Qipeng Xie, Zi Liang, Jiafei Wu, Yufei Chen, Weizheng Wang, Wenao Ma, Zhong Ming, Haiqin Yang, Kaishun Wu

### Abstract

Large Language Models (LLMs) exhibit extreme sensitivity to surface-level prompt variations, in which minor lexical changes can trigger disproportionate performance fluctuations. Moving beyond black-box optimization and coarse-grained templates, we present the first large-scale, n-gram token-level mechanistic analysis of prompt stability, leveraging a dataset of 132,000 prompt variants. Our investigation reveals a fundamental Scaling Law of Prompt Performance Stability: higher average task performance is strongly associated with lower variance and greater robustness across prompt perturbation. We identify two core linguistic drivers underlying this robustness: (1) Domain-Specific Terminology, which tightly anchors semantic boundaries, and (2) Explicit Action Directives, which formalize reasoning trajectories. Together, these elements constrain the model's interpretative space, effectively ``locking in'' more deterministic generation behavior. Building on these insights, we introduce an automated Prompt-Refining Agent that systematically restructures input queries by injecting domain anchoring and operational constraints. Empirical evaluation shows that our approach reduces performance variance by 40.7% in code generation task, while preserving or improving mean performance. These findings provide a statistically grounded and mechanistically interpretable framework for achieving robust prompt engineering.

### 中文一句话结论
这篇论文通过大规模词元级分析揭示了提示词性能与稳定性之间的缩放定律，并识别出领域术语和明确行动指令是提升提示鲁棒性的关键因素，由此提出自动化提示精炼代理可将性能方差降低40.7%。

### English TL;DR
This paper presents a large-scale token-level mechanistic analysis revealing a scaling law between prompt performance and stability, identifies domain-specific terminology and explicit action directives as key drivers of robustness, and introduces an automated Prompt-Refining Agent that reduces performance variance by 40.7% while preserving or improving mean performance.

### 中文详细总结
该研究对大型语言模型（LLM）中提示词对表面词汇变化的极端敏感性进行了系统性分析。基于132,000个提示变体的大规模数据集，作者首次从n-gram词元层面进行了机制性分析，揭示了提示性能稳定性的缩放定律：平均任务性能越高，则在不同扰动下的方差越小、鲁棒性越强。研究识别出两种核心语言驱动因素——领域特定术语和明确行动指令，它们能约束模型的解释空间，实现更确定性的生成行为。基于这些发现，作者开发了自动提示精炼代理，通过注入领域锚定和操作约束来系统性地重构输入查询。实验表明，在代码生成任务中，该方法将性能方差降低40.7%，同时保持或提升了平均性能。

### 方法 / 贡献
1. 首次大规模n-gram词元级提示敏感性统计分析，基于132,000个变体。
2. 发现并验证了提示性能与鲁棒性之间的缩放定律。
3. 识别出领域特定术语和明确行动指令两种关键语言模式。
4. 开发了自动提示精炼代理，通过注入领域锚定和操作约束减少方差。

### 实验或数据
- 数据集：从WizardLM_evol_instruct_70k中随机抽取12,000条指令。
- 扰动策略：五种正交策略（语义等价改写、添加上下文、改变格式/风格、引入歧义、句法噪声），每条指令生成11个变体，共132,000个提示。
- 评估流程：Rewriter（Gemini-2.5-flash）生成变体 → Generator（Qwen-plus）合成响应 → Evaluator（Grok-4-fast）采用LLM-as-a-Judge范式进行1-100连续评分。
- 结果：在代码生成任务上，性能方差降低40.7%，平均性能保持或提升。

### 值得关注点
1. 从词元层面揭示提示稳定性机制，而非黑盒优化或粗粒度模板分析。
2. 缩放定律为提示工程提供了统计基础，高平均性能天然关联高稳定性。
3. 自动精炼代理具有实际应用价值，能显著降低方差且不牺牲性能。
4. 扰动策略被验证为正交（余弦相似度仅约0.22）且覆盖多种强度，保证评估全面性。

### 局限性
论文未明确提及局限性。根据现有内容，可推测数据集仅来自WizardLM，可能不完全代表所有任务类型；自动精炼代理仅在代码生成任务上验证，其他任务效果未知；依赖LLM作为评判者可能存在固有偏见，但作者未在摘要或方法部分讨论。

## 4. VA-DPO: Valence-Arousal Direct Preference Optimization for Controllable Emotion Generation in Language Models

- Source: arxiv
- arXiv ID: 2608.20374
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.20374v1
- PDF: https://arxiv.org/pdf/2608.20374v1
- DOI: https://doi.org/10.48550/arXiv.2608.20374

### Authors

Hyunwoo Kim

### Abstract

How precisely can we tell a language model how to feel? Most work on emotional generation answers with a discrete label - happy, angry, sad - which cannot express a target like "mildly downcast but calm." We instead specify the desired affect as a continuous point (v*, a*) in the Valence-Arousal plane and train the model to hit it. Our method, VA-DPO, is a small modification to Direct Preference Optimization: a frozen VA regressor scores each sampled generation by its Euclidean distance to the target, we keep only candidate pairs whose distance gap clears a margin tau, and we optimize a LoRA adapter with the ordinary DPO loss against a frozen reference. The DPO objective itself is unchanged; what is new is how the preference data is built. On Llama-3.1-8B-Instruct this cuts mean VA distance to the target by 33% over system-prompting and 25% over few-shot prompting, lifting valence/arousal correlation to r_v=0.93 and r_a=0.75. The gains carry over to Qwen3-8B and Llama-3.2-3B, and they do not come at the usual price: MMLU is unchanged (Delta=+0.0) and HellaSwag and TruthfulQA are preserved. We release the code, configs, and the preference-construction pipeline.

### 中文一句话结论
VA-DPO通过基于连续效价-唤醒目标构建偏好对，并用直接偏好优化微调LoRA适配器，实现了对语言模型输出情感的精确连续控制，使目标距离降低33%且通用性能不变。

### English TL;DR
VA-DPO enables precise, continuous control over the emotional affect of language model outputs by fine-tuning with Direct Preference Optimization on margin-filtered preference pairs constructed from a frozen valence-arousal regressor, achieving a 33% reduction in mean distance to desired emotional targets while preserving general task performance.

### 中文详细总结
语言模型的情感生成通常使用离散标签，无法表达“轻度低落但平静”等细微情感。本文提出VA-DPO，将期望情感指定为Valence-Arousal平面上的连续点，并通过以下步骤训练模型：使用冻结的VA回归器对每个生成样本评分（欧氏距离到目标）；仅保留距离差大于阈值的偏好对；用标准DPO损失优化LoRA适配器。在Llama-3.1-8B-Instruct上，平均VA距离相比系统提示减少33%，相比少样本提示减少25%，效价/唤醒相关性分别达到r_v=0.93和r_a=0.75。在Qwen3-8B和Llama-3.2-3B上同样有效，且MMLU、HellaSwag、TruthfulQA等通用能力不受影响。论文还分析了边距阈值、候选数等设计选择。

### 方法 / 贡献
- 方法：对DPO的小修改——构建偏好数据时，用冻结VA回归器评估生成文本与目标VA点的欧氏距离，筛选|d(y_w)-d(y_l)|>τ的样本对作为偏好对，并保持标准DPO损失在LoRA上训练。  
- 贡献：①提出了基于连续VA空间的偏好对构造流程（含边距过滤），②通过消融实验验证了边距阈值和回归器相对于词典的重要性，③展示了在多个模型上不损伤通用性能的情感控制增益。

### 实验或数据
- 数据集：EmoBank（约10K英文句子，人标VA值）训练回归器并在测试集评估。  
- 模型：Llama-3.1-8B-Instruct为主，Qwen3-8B和Llama-3.2-3B稳健检查。  
- 回归器：RoBERTa-large+2D线性头，在EmoBank上训练后冻结。  
- 基线：系统提示、少样本提示、SFT、离散标签DPO、无边距VA-DPO。B4（词典奖励）和B6（无训练导向）未运行。  
- 主要指标：VA欧氏距离、相关性r_v、r_a，以及MMLU、HellaSwag、TruthfulQA。  
- 结果：主模型距离降低33%，r_v=0.93，r_a=0.75，通用指标基本不变。

### 值得关注点
- 使用连续VA空间而非离散标签，实现更细腻的情感控制。  
- 边距过滤（τ>0）去除了回归器噪声主导的模糊对，提高训练信号质量。  
- 双正则化：低秩更新（LoRA）加上DPO的KL散度约束，维持了模型原有能力。  
- 代码、配置和偏好构造流程已开源。

### 局限性
- 回归器仅在英文EmoBank上训练，可能无法覆盖多样表达或跨语言场景。  
- 基线B4（词典奖励）和B6（无训练VA导向）未在本文运行，比较尚不完整。  
- 论文未评估多轮对话或情感转换场景的情感维持能力。  
- 条件格式（文本前缀）增加4-6个token开销，且要求目标始终作为输入的一部分。

## 5. MIL-BERT: Classification of Arbitrarily Large Text with Performance and Explanatory Guarantees

- Source: arxiv
- arXiv ID: 2608.20636
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.20636v1
- PDF: https://arxiv.org/pdf/2608.20636v1
- DOI: https://doi.org/10.48550/arXiv.2608.20636

### Authors

John Cadigan, Dayne Freitag, Eric Yeh

### Abstract

Many text classification decisions are viable based on constituent excerpts alone. Taking inspiration from the field of multiple instance learning, we present an algorithm for training a neural network to classify text by selecting such excerpts. We show that our approach is also scalable with demonstrated learning against samples with nearly 1M tokens. We evaluate our methods on 7 datasets with emphasis on long-textual collections that far exceed the encoding limit of our base model. We present state-of-the-art results with this algorithm on 3 datasets: identification of political bias in news outlets, trigger warnings in long stories, and demographic characteristics of authors in tweet collections. Furthermore, the model trained on weakly-labeled collections of text (bags) generalizes to accurately classify constituent, smaller instances. Besides a new state-of-the-art for these problems, this approach is one of the few neural methods to excel in these datasets.

### 中文一句话结论
MIL-BERT通过多实例学习与双通池化技巧，实现了对超长文本的高效分类，在政治偏向、触发词检测和作者画像三个数据集上达到最优，并提供可解释性保障。

### English TL;DR
MIL-BERT uses multiple instance learning and a double-pass pooling trick to classify arbitrarily long texts by selecting key excerpts; it achieves state-of-the-art on three long-text datasets and provides explanatory guarantees.

### 中文详细总结
MIL-BERT针对文本分类中“信号局部性”现象（即仅需部分摘录即可判断），受多实例学习启发，提出一种神经网络算法：将长文本分割为摘录（实例）集合（包），通过双通池化——第一轮无梯度选择关键摘录，第二轮带梯度计算——在有限内存下处理长达近百万token的样本。方法在7个数据集上评估，重点针对远超基座模型编码限制的长文本集合。在新闻源政治偏向检测、长故事触发词检测、推文集合作者人口特征分析三个任务上取得最优结果。此外，基于弱监督包标签训练的模型能泛化到准确分类更小的实例。该方法还通过强制选择可审查关键摘录，提供天然的可解释性。

### 方法 / 贡献
- 提出基于多实例学习的摘录式分类框架，使用双通池化技巧（double-pass pooling trick）实现高效训练，内存占用仅与所选摘录数k相关，计算量为O(n+k)。
- 设计两种选择器：共享特征图（shared feature map）和特征树（feature tree），均满足幂等性以支持双通池化；结合Gumbel-softmax实现可微分选择。
- 在多个标准基准上超越或持平现有全文档方法，尤其在长文本和弱标签场景中表现突出，并且训练于包标签的模型可泛化到实例分类。

### 实验或数据
- 评估7个数据集：Trigger Warning（触发词，包与实例标签）、CLEF2023（新闻源政治偏向）、Hyperpartisan、20Newsgroups、EURLEX-57K、Book Text、PAN2019（作者画像：性别、职业、出生年份、知名度）。
- 文档长度跨度大（平均98至77158 token，最大882343 token）。
- 超参数：主要使用RoBERTa-large作为嵌入模型，窗口大小256 token，步长64；部分任务使用特征树选择器或特殊窗口（如出生年份回归任务用64窗口）。
- 结果：在CLEF2023 3B（源级）、Trigger Warning故事级、PAN2019性别和职业上达到SOTA；实例分类泛化性良好（CLEF2023文章级、Trigger Warning段落级）。
- 提供了计算时间与内存消耗对比（原文图表未完全展示，但提及双通池化显著降低内存峰值）。

### 值得关注点
1. 方法有效应对超长文本（近百万token），无需昂贵的长Transformer变体。
2. 选择出的摘录可直接提供解释，满足可解释性要求。
3. 弱监督设置下（仅包标签）训练的分类器能泛化到实例级预测，减少标注成本。
4. 双通池化技巧通用性强，可适配多种选择器与分类器架构。
5. 在多个任务（多标签、多分类、回归）上均适用，灵活性高。

### 局限性
- 方法依赖于信号局部性假设，若分类需要全局上下文，可能性能下降。
- 选择器必须满足幂等性，限制了某些更复杂选择策略的采用。
- 双通池化存在计算与内存的折中：内存O(k)但计算O(n+k)，对极长文档仍需大量前向计算。
- 部分任务（如PAN19知名度、出生年份）未取得SOTA，表明方法在某些细粒度回归或分类上仍有局限。
- 论文未讨论在多语言或领域迁移场景下的表现。

## 6. The Divergence Hypothesis: Unmasking Lexical Interference and Label Bias in Mental Health NLP

- Source: arxiv
- arXiv ID: 2608.20353
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.20353v1
- PDF: https://arxiv.org/pdf/2608.20353v1
- DOI: https://doi.org/10.48550/arXiv.2608.20353

### Authors

Moustafa Yehia Hassan

### Abstract

Computational mental health (CMH) classifiers often degrade under distribution shift because human annotators and distant-supervision pipelines reward different linguistic signals. We introduce TSS (Triple-Stream Stress probe), a multi-channel diagnostic framework that decomposes text into (A) lexical character n-grams, (B) a small, mostly content-free morpho-syntactic channel, and (C) a 154-feature psycholinguistic style channel. Across four English datasets (N=12,906), TSS reveals a lexical interference effect: adding lexical features to the style channel reduces Macro-F1 on human-labeled data (mean drop 0.072, p<10^-4) but not on auto-labeled data. We propose Degree of Divergence (DoD), a difference-in-differences statistic adapted from econometrics for label-source auditing, with instance-level bootstrap inference; the headline estimate is DoD(BC-A) = 0.0374, 95% CI [0.0097, 0.0651], p=0.0032. A platform-stratified Twitter-only DoD (which removes the Reddit vs. Twitter contrast) reproduces the pattern with bootstrap inference: DoD-Tw(BC-A) = +0.096 (p<0.001) and DoD-Tw(AC-A) = -0.089 (p<0.001). Interventional masking (pos_only) retains ~95-99% of Channel C's performance after destroying content words on human datasets, indicating that the style channel does not rely primarily on lexical surface form. TSS is positioned as a diagnostic audit framework, not a clinical screening tool: it flags label-source-specific shortcut learning before generalization claims are made.

### 中文一句话结论
本文提出 TSS 诊断框架和 DoD 统计量，揭示人类标注与远程监督数据在心理健康 NLP 中奖励不同的语言信号，且词汇特征对人类标注数据产生干扰效应。

### English TL;DR
The paper introduces TSS, a multi-channel diagnostic framework, and a difference-in-differences statistic (DoD) to show that human-labeled and auto-labeled mental health datasets reward distinct linguistic signals; lexical features interfere with psycholinguistic style features on human-labeled data but not on auto-labeled data, indicating label-source-specific shortcut learning.

### 中文详细总结
计算心理健康分类器在分布偏移下表现下降，因为人类标注者与远程监督管线奖励不同的语言信号。本文提出 TSS（三流压力探针）框架，将文本分解为三个通道：A（词汇字符 n-gram）、B（几乎无内容的形态句法特征6维）、C（154维心理语言学风格特征）。在四个英文数据集（N=12,906）上，TSS 揭示了词汇干扰效应：在人类标注数据上，向风格通道添加词汇特征导致 Macro-F1 平均下降 0.072（p<10⁻⁴），但在自动标注数据上未出现。作者借鉴计量经济学提出差异中的差异统计量 DoD，用于标注源审计，支持实例级 Bootstrap 推断。主要估计值 DoD(BC–A)=0.0374（95% CI [0.0097, 0.0651], p=0.0032）。平台分层的 Twitter-only DoD 复制了该模式：DoD-Tw(BC–A)=+0.096（p<0.001），DoD-Tw(AC–A)=-0.089（p<0.001）。干预性掩码（pos_only）在人类数据集上破坏内容词后仍保留约 95–99% 的 C 通道性能，表明风格通道不主要依赖词汇表面形式。TSS 被定位为诊断审计框架，而非临床筛查工具。

### 方法 / 贡献
1. 提出 TSS 三通道诊断探针：A（字符 n-gram TF-IDF，经卡方选择至 500维）、B（POS 双词及抽象 SVO 三元组，共6维，几乎无词汇信息）、C（154维心理语言学风格特征，含长度鲁棒变换）。
2. 发现词汇干扰效应：人类标注数据上，词汇特征加入风格通道会降低性能。
3. 引入 DoD 统计量：基于双重差分思想，用于量化不同标注源的信号差异，支持 Bootstrap 推断和 FDR 控制。
4. 提供跨平台风格表型（Bootstrap ARI≈0.98）、留一域评估（LODO）、与 MentalBERT 及少样本 LLaMA-3 的基线对比、定性冲突区工作簿。
5. 公开完整代码与去污染脚本。

### 实验或数据
- 四个英文数据集，共 N=12,906：Dreaddit-test（Reddit，715条，人类专家标注）、Twitter-gold（Twitter，2,863条，人工标注）、Twitter-auto（Twitter，6,218条，远程监督）、Reddit-combi（Reddit，3,110条，远程监督）。
- 主要指标：Macro-F1，辅以 PR-AUC 和平衡准确率；使用 McNemar 检验和 Bootstrap 置信区间进行配对比较。
- 留一域评估（LODO）跨压力域泛化。
- 干预性掩码实验：pos_only 保留约 95–99% C 通道性能。
- 基线比较：TSS 所有通道大幅超过简单多数类基线。

### 值得关注点
- 词汇干扰效应：人类标注数据中，词汇特征并非有益反而有害，提示标注源特定的捷径学习。
- DoD 统计量创新性地将双重差分引入标注源审计，提供统计显著性检验。
- TSS 框架设计用于诊断而非竞赛，通道可分离、长度鲁棒、跨平台转移。
- 跨平台风格表型的一致性（Bootstrap ARI≈0.98）表明心理语言学风格在不同平台稳定。

### 局限性
- TSS 定位为诊断审计框架，非临床筛查工具；不声称诊断有效性。
- 自动标注数据（Twitter-auto）存在“疾病→压力”混淆风险（诊断用户不一定每条都表达压力）。
- Reddit-combi 正类为多数类（0.880），不能替代人类标注。
- 人类标注数据（Twitter-gold）并非专家临床标注，标注方法有约束。
- 实验仅针对英文二分类压力检测，可能不泛化至其他语言或任务。

## 7. Truth Lies Deep: Countering Semantic Camouflage via Latent Intent Verification

- Source: arxiv
- arXiv ID: 2608.20378
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.20378v1
- PDF: https://arxiv.org/pdf/2608.20378v1
- DOI: https://doi.org/10.48550/arXiv.2608.20378

### Authors

Md. Hasib Ur Rahman

### Abstract

Safety alignment in Large Language Models (LLMs) is often superficial, relying on refusal mechanisms that trigger only at the final stages of generation without erasing the foundational knowledge of harmful concepts acquired during pretraining. This study demonstrates that this architectural disconnect leaves models vulnerable to Semantic Camouflage -- adversarial attacks that wrap harmful intent in benign narrative contexts (e.g., creative writing), effectively bypassing standard input and output guardrails. By analyzing the latent activation trajectories of three distinct Small Language Model (SLM) families (Phi-3, Qwen2.5, and Gemma-2b) under adversarial stress, this research identifies a universal ``Intent Horizon'' -- a critical depth (typically 15--20\% of total layers) where the model's distinct, pre-trained representation of harmful intent collapses as it contextualizes the query into a ``safe'' narrative. Results indicate that while late-layer representations of camouflaged attacks are mathematically indistinguishable from safe queries (Detection Rate $< 20\%$), early-layer representations retain a distinct, detectable ``harm signature.'' Leveraging this insight, this paper proposes Latent Intent Verification (LIV), a lightweight probing defense. Experiments on the PKU-SafeRLHF dataset demonstrate that LIV outperforms standard guardrails by a margin of 20--50\% across all tested architectures, effectively neutralizing zero-day semantic attacks without requiring model retraining.

### 中文一句话结论
本文发现大型语言模型的安全对齐存在“意图视界”现象：有害意图的表示在前几层可检测，但被后续上下文掩盖，导致传统输出防护失效；据此提出轻量级早期层探测防御（LIV），将零日语义伪装攻击检测率提升20–50%。

### English TL;DR
This paper shows that LLM safety alignment is superficial due to an "Intent Horizon": harmful intent signals remain detectable in early layers but collapse benign the narrative context in later layers, rendering output guardrails ineffective. The proposed Latent Intent Verification (LIV) achieves 20–50% higher detection on zero-day semantic camouflage attacks across three SLM families without retraining.

### 中文详细总结
大型语言模型的RLHF安全对齐仅抑制最终输出，未消除预训练中的有害知识。本研究提出“语义伪装”攻击——将恶意意图包裹于创意写作等无害叙事中，可绕过输入/输出防护。通过分析Phi-3、Qwen2.5和Gemma-2b三个小语言模型在对抗压力下的隐层激活轨迹，发现一个普遍的“意图视界”：通常在前15–20%的层中模型对有害意图的独特表示清晰可辨，但随着上下文整合，该信号在后续层迅速衰减至与安全查询无法区分（检测率低于20%）。基于此，论文提出轻量级探测防御LIV（Latent Intent Verification），在早期层训练逻辑回归分类器。在PKU-SafeRLHF数据集和自建零日伪装数据集上，LIV在所有架构上均提升20–50%检测率，无需重新训练模型。几何分析表明，早期层中伪装攻击的隐层向量仍聚集在有害簇附近，而后期层则嵌入安全簇。

### 方法 / 贡献
- 提出“意图视界”（Intent Horizon）概念：有害意图信号在特定深度（如Phi-3的第10–12层）后显著坍塌，后期层无法区分伪装攻击与安全查询。
- 验证安全漏洞：标准后期层防护对伪装攻击检测率低于20%，而早期层仍保持高可检测性。
- 设计LIV：在早期层（如15–20%深度）训练线性探测器，实现模型无关、轻量级的零日攻击检测，无需重训练。
- 实验贡献：在三个不同架构的SLM上验证方法的通用性，量化安全差距（Δ_S = 早期检测率 − 后期检测率）。

### 实验或数据
- **数据集**：训练集使用PKU-SafeRLHF（2000对安全/显式有害提示）；评估集使用自建100条语义伪装提示（涵盖剧本、角色扮演、代码调试等，无训练集关键词）。
- **模型**：Phi-3-mini-4k-instruct (3.8B)、Qwen2.5-1.5B-Instruct、Gemma-2b-it，均采用4-bit NF4量化模拟资源受限环境。
- **检测率结果**：后期层检测率18–35%，早期层LIV检测率58–73%，安全差距20–50%。
- **层间扫描**：对Phi-3进行逐层探测，在前10层检测概率>60%，第12层后急剧降至接近0，确认意图视界位置。

### 值得关注点
- 安全对齐的“表面性”证据：RLHF仅优化拒绝的输出形式，未消除内部有害理解，导致伪装攻击可利用上下文权限覆盖安全训练。
- 几何可解释性：早期层中伪装攻击的隐层向量仍为有害簇的离群点，后期层则嵌入安全簇，解释了LIV的线性可分离性。
- 零日攻击防护：LIV无需知道具体攻击模式，直接检测早期层中固有的“有害签名”，可应对未见过的伪装变种。
- 轻量高效：仅需在早期层添加一个逻辑回归分类器，相比完整影子模型开销小。

### 局限性
- **推理延迟**：探测中间层带来额外计算开销，可能影响实时应用。
- **自适应攻击**：理论上攻击者可针对LIV使用的固定层优化（如梯度攻击压制第4层信号），需要动态探测深度。
- **模型特异性**：意图视界的具体深度因模型大小和训练数据而异，部署前需为每个模型进行校准。
- **仅针对语言模型**：当前验证限于小语言模型，需扩展至更大规模LLM和多模态模型。

## 8. Scaling Unsupervised Word Alignment to Documents via Structural Constraints

- Source: arxiv
- arXiv ID: 2608.21023
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.21023v1
- PDF: https://arxiv.org/pdf/2608.21023v1
- DOI: https://doi.org/10.48550/arXiv.2608.21023

### Authors

Michelle Wastl, Jannis Vamvas, Rico Sennrich

### Abstract

Word alignment has traditionally been studied between sentences, but many cross-lingual tasks increasingly require correspondences across full documents. While recent multilingual embedding models can encode long inputs, we show that applying algorithms designed for sentences directly to documents leads to performance degradation. To address this, we introduce CTFAlign, a lightweight, training-free approach for document-level word alignment. CTFAlign applies a coarse-to-fine refinement strategy that restricts the alignment search space to semantically similar regions. Additionally, we introduce MDPAlign, a simpler alternative that constrains alignments by position with a main diagonal prior. Both approaches operate directly on full documents without relying on sentence segmentation or sentence alignment. We evaluate these methods across six language pairs varying in typological distance, resourcedness, and document length. Averaged over three models, CTFAlign reduces word alignment error rate from 0.412 to 0.326. These gains transfer downstream, leading to improvements in document-level translation coverage evaluation and recognition of semantic differences. We release CTFAlign as a Python package and make the code and data to reproduce our experiments publicly available.

### 中文一句话结论
本文提出两种无需训练的结构约束方法（CTFAlign和MDPAlign），将无监督词对齐从句子扩展到文档，在六种语言对上将词对齐错误率从0.412降至0.326。

### English TL;DR
The paper introduces CTFAlign and MDPAlign, two training-free structural constraint methods for document-level word alignment. CTFAlign uses coarse-to-fine refinement to restrict alignment to semantically similar regions, while MDPAlign applies a main diagonal prior. Evaluated across six language pairs and three embedding models, they reduce word alignment error rate from 0.412 to 0.326 and improve downstream tasks like translation coverage evaluation.

### 中文详细总结
传统词对齐研究聚焦于句子层面，但跨语言任务越来越需要文档级对应关系。尽管现代多语言嵌入模型能编码长文本，作者发现直接将句子级对齐算法应用于文档会导致性能下降。为此，他们提出两种轻量级、无需训练的方法：**CTFAlign** 采用粗到细的精细化策略，将对齐搜索空间限制在语义相似区域；**MDPAlign** 则更简单，通过主对角线先验约束位置对齐。两者均无需句子分割或句子对齐直接处理完整文档。在六种语言对（涵盖不同类型距离、资源丰富度和文档长度）上，平均使用三种模型测试，CTFAlign将词对齐错误率从0.412降至0.326。这些改进还传递到下游任务，如文档级翻译覆盖评估和语义差异识别。作者公开了CTFAlign的Python包以及实验代码和数据。

### 方法 / 贡献
- **CTFAlign**：基于粗到细的语义区域限制，先通过嵌入相似度缩小候选对齐范围，再在局部进行精细对齐，无需训练。
- **MDPAlign**：利用主对角线先验，假设文档级对齐大致沿对角线分布，简单约束位置范围。
- 两种方法均直接在文档上运行，不依赖句子切分或句子级对齐，实现了从句子到文档的无缝扩展。
- 贡献在于首次提出适用于完整文档的无监督词对齐方法，显著降低错误率，并验证了在下游任务中的有效性。

### 实验或数据
- 实验涵盖六种语言对：英语-德语、英语-日语、英语-中文等，按类型距离、资源丰富度和文档长度区分。
- 使用三种多语言嵌入模型（例如mBERT、XLM-R等，具体模型名称未在摘要中列出，但全文给出）。
- 主要指标：词对齐错误率（AWER）。CTFAlign平均错误率从0.412降至0.326；MDPAlign也有提升。
- 下游任务：文档级翻译覆盖评估（如覆盖得分）和语义差异识别（检测翻译中的语义变化）。
- 数据和代码已公开（GitHub和Hugging Face）。

### 值得关注点
- 方法轻量、无需训练，易于部署和迁移。
- 直接处理完整文档，避免了句子分割带来的错误传播。
- 在多种语言对（包括弱资源语言）上验证了有效性。
- 将词对齐改进转化为下游任务的实际收益。
- 公开了代码和数据，便于复现和扩展。

### 局限性
- 方法依赖预训练多语言嵌入模型的质量；若嵌入对某些语言或领域覆盖不佳，性能可能受限。
- CTFAlign的粗到细策略依赖于语义相似性阈值，可能遗漏远距离但语义相似的对齐。
- MDPAlign的主对角线先验假设文档对齐大致单调，对于语序差异较大的语言对（如日语-英语）可能不充分。
- 实验仅在有限的语言对和模型上进行，泛化性需进一步验证。
- 未讨论计算开销，但粗到细搜索可能增加额外时间。

## 9. Knowledge-Graph-Gated Defactualization for Style-Controllable and Fact-Preserving Generation in Agentic Conversational AI

- Source: arxiv
- arXiv ID: 2608.20393
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.20393v1
- PDF: https://arxiv.org/pdf/2608.20393v1
- DOI: https://doi.org/10.48550/arXiv.2608.20393

### Authors

Tanmay Kumar Shrivastava, Darsh Rohit Nandu, Rajesh Kumar Mundotiya

### Abstract

Agentic large language models (LLMs) deployed in fact-sensitive applications such as customer support must simultaneously preserve factual correctness and generate responses in a controllable stylistic register. Activation steering enables fine-tuning-free style control by perturbing hidden representations, but it lacks an explicit mechanism for distinguishing verifiable facts from stylistic content, leading to semantic leakage. We address this challenge through \emph{Defactualize-Steer-Rehydrate} (DSR), a knowledge-engineering framework that integrates a typed, salience-weighted knowledge graph (KG) with activation steering. DSR extracts salient entities using a layered regex or NER or lexical-classifier pipeline, replaces them with typed placeholders prior to steering, and deterministically restores verified values through salience-guided rehydration after generation. DSR is evaluated across six LLaMA-family models (1B--13B parameters) on 600 A2A-generated customer-support cases (1,200 generations), with a dedicated KG ablation study. DSR significantly increases verified-entity recovery relative to a steering-only baseline (Cohen's $d=0.225$, $p_{\text{Bonf}}=1.0\times10^{-4}$), though the absolute recovery rate remains modest, while preserving effective style control across diverse model families. Layer-wise separability and steering-strength diagnostics further show previously unexplored interactions between representation-level steering and factual grounding. hese results demonstrate that explicit knowledge engineering can systematically enhance trustworthy, controllable, and reproducible generative AI without requiring model fine-tuning. Code, cached steering vectors, and evaluation scripts are publicly released to support reproducibility.\footnote{https://github.com/Tanmay-IITDSAI/KG-Gated-Defactualization}

### 中文一句话结论
本文提出DSR框架，通过将类型化、显著性加权的知识图谱与激活引导结合，在不微调模型的前提下同时实现风格可控与事实保持的生成。

### English TL;DR
The paper proposes the Defactualize-Steer-Rehydrate (DSR) framework, which integrates a typed, salience-weighted knowledge graph with activation steering to separate factual content from stylistic signals, enabling fact-preserving and style-controllable generation without fine-tuning.

### 中文详细总结
该工作针对事实敏感的应用场景（如客服）中，大型语言模型（LLM）需要同时保持事实正确性和可控风格的问题。现有激活引导方法可以在不微调的情况下控制风格，但无法区分事实与风格内容，导致语义泄漏。DSR框架通过“去事实化-引导-再水化”三步流程解决：首先利用分层正则表达式/NER/词法分类器提取显著实体并构建类型化、显著性加权的知识图谱，然后用类型占位符替换实体后进行激活引导生成，最后根据知识图谱确定性还原已验证的实体。在LLaMA系列六个模型（1B–13B参数）上，基于600个A2A生成的客服案例（1200次生成）进行评估，并进行了知识图谱消融实验。与纯引导基线相比，DSR显著提高了验证实体的恢复率（Cohen's d=0.225，p Bonf=1.0×10^{-4}），但绝对恢复率仍中等。同时，有效保持风格控制。层间可分离性和引导强度诊断揭示了表示级引导与事实接地间的新交互。

### 方法 / 贡献
- **数据工程流水线**：提出无训练的分层提取框架（正则、NER、分类器），从非结构化消息构建类型化、显著性加权的知识图谱。
- **DSR架构**：设计去事实化-引导-再水化流程，将知识图谱与激活引导操作符接口，实现事实控制与风格属性的结构分离。
- **全面实证评估**：在六个LLaMA模型、600案例、1200次生成上，通过消融实验证明知识图谱层显著提升实体覆盖（p Bonf=1.0×10^{-4}, d=0.225）且保持风格保真度。
- **诊断套件与敏感性协议**：开发SAF、HSI、TCI三个指标及联合层强度敏感性协议，发现特定操作区域中幻觉严重度饱和、语调一致性非单调。
- **结构不变性与透明性**：验证知识图谱的图结构统计（节点数、密度、平均显著性）在不同主模型间保持稳健。

### 实验或数据
- **模型**：六个LLaMA系列模型（1B–13B参数，包括LLaMA-2 7B/13B、LLaMA-3.1/3.2 1B–8B）。
- **数据**：600个A2A生成的客服案例，共1200次生成（含不同风格）。
- **评估**：进行100案例的知识图谱消融实验，与纯引导基线对比实体恢复率（Cohen's d=0.225，p Bonf=1.0×10^{-4}）；同时评估风格控制效果。还进行了层间可分离性、引导强度诊断等分析。

### 值得关注点
- DSR首次将类型化、显著性加权的知识图谱与激活引导操作符以统一流水线集成，实现前生成约束和后生成验证。
- 无需模型微调，仅通过知识工程即可增强可信、可控、可复现的生成。
- 公开代码、缓存引导向量和评估脚本，支持可复现性。
- 诊断套件揭示了表示级引导与事实接地间未被探索的交互。

### 局限性
- 验证实体恢复的绝对率仍中等（尽管相对提升显著），可能影响高精度要求场景。
- 实验仅覆盖LLaMA系列模型，推广到其他架构或领域需进一步验证。
- 知识图谱构建依赖分层提取管道，可能在高度复杂或噪声文本中产生遗漏或错误。
- 当前仅处理客服场景中的固定实体类型，扩展至更开放域时类型定义可能不完整。
- 未探讨多轮对话中知识图谱的持续更新与一致性维护。

## 10. Poly-InstructTTS: Learning In-the-Wild Expressive Speech Synthesis from Open-Ended Instructions

- Source: arxiv
- arXiv ID: 2608.20387
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.20387v1
- PDF: https://arxiv.org/pdf/2608.20387v1
- DOI: https://doi.org/10.48550/arXiv.2608.20387

### Authors

Junhui Zhang, Qianhui Xu, Qingxiang Guo, Dawei Yang, Ling Miao, Qiangqiang Wang, Yang Song

### Abstract

While recent text-to-speech (TTS) models achieve high naturalness, controlling fine-grained expression via natural-language instructions remains challenging. We introduce Poly- InstructTTS, which learns expressive speech from open-ended instructions using in-the-wild audiovisual data. We build a scalable multi-modal pipeline to construct a 1,000-hour instruction-annotated corpus covering 1,000+ fine-grained emotions and styles. The framework uses a prompt-free GPT with attribute-based thinking tokens, followed by a flow-matching module that injects timbre from a reference audio. We also present a speaker fine-tuning procedure to transfer instruction control to specific speakers while preserving persona. We further extend InstructTTSEval with broader tasks. Experiments show that Poly-InstructTTS delivers strong performance in instruction adherence and expressiveness. Audio demos and the expanded testset are available on our project page.

### 中文一句话结论
Poly-InstructTTS 利用野外视听数据通过多模态流水线构建了1000小时指令标注语料库，采用无提示GPT结合属性思维令牌和流匹配模块，实现了对开放指令的细粒度情感与风格语音合成，在指令遵循和表现力上表现优异。

### English TL;DR
Poly-InstructTTS learns expressive speech from open-ended instructions using a 1,000-hour in-the-wild audiovisual corpus, employing a prompt-free GPT with attribute-based thinking tokens and flow-matching for timbre injection, achieving strong instruction adherence and expressiveness.

### 中文详细总结
Poly-InstructTTS 是一个面向开放自然语言指令的语音合成系统，能生成细粒度情感（超过1000种）和风格。其核心在于：1）设计了一个可扩展的多模态数据流水线，从影视媒体中提取音频并进行说话人分离、指令生成，构建了1000小时指令配对数据集；2）模型采用GPT-流匹配架构，GPT端无需提示音频，引入属性化思维令牌（性别、风格等）指导生成，流匹配模块则从参考音频注入音色，避免了风格泄露；3）支持说话者微调，将指令控制转移到特定说话者。实验在InstructTTSEval基准和扩展测试集上验证了其有效性。

### 方法 / 贡献
1. **多模态数据流水线**：从影视视频中提取音频，经语音活动检测、音频净化、说话人分离与字幕对齐后，利用多模态大模型（Gemini）分三阶段生成情境化、多样化的自然语言指令，覆盖200多种口音和800多种情感。
2. **模型架构**：基于GPT-流匹配框架。GPT部分无提示音频输入，将指令、文本序列化后加入属性思维令牌（性别、强度、风格、口音），GPT负责预测离散语音令牌；流匹配模块根据参考音频注入音色，GPT与音色分离，避免指令与参考风格冲突。
3. **说话者微调**：通过在文本前添加说话者ID令牌，可以将指令控制迁移到特定说话者，同时保留其个性特征。

### 实验或数据
- 训练数据：约2500小时原始影视数据，经流水线处理后得到1000小时、110万条话语的高表现力数据集，包含200多种口音和800多种细粒度情感。指令-音频匹配率大于95%。
- 评估测试集：基于InstructTTSEval基准并扩展了200个样本，覆盖非主流口音、极端情感、多样风格和自发语音等场景。
- 客观指标：使用词错误率和InstructTTSEval定义的声学参数遵循、描述性风格指令、角色扮演指标。
- 主观评估：20名母语听众进行指令遵循精度和语音自然度的平均意见得分评测。

### 值得关注点
- 使用野外影视数据而非受限的朗读式数据集，大幅提升情感、口音和风格的多样性和表现力。
- 无提示GPT设计避免了参考音频的风格泄漏问题。
- 属性化思维令牌（性别、强度、风格、口音）作为轻量中间表示，既引导风格生成，又避免长链文本令牌导致的不稳定和灾难性遗忘。
- 提供了扩展的测试集和项目页面，有利于社区复现和对比研究。

### 局限性
- 受版权限制，原始影视数据无法公开，仅公开流水线和提示词，研究者需自行收集语料进行复现。
- 依赖多个商用API（ElevenLabs、Gemini），可能带来成本和可再现性方面的限制。
- 数据管道中语音识别、说话人分离和指令生成的自动标注可能存在噪声和错误，尽管通过字幕匹配筛选，但无法完全消除。
- 属性思维令牌仅选取了出现次数大于200次的风格和口音类别，可能遗漏低频但重要的风格/情感。

## Processing Notes

- Duplicate papers skipped: 0