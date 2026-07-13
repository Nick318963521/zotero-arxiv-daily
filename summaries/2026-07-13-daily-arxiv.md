# Daily arXiv - 2026-07-13

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-13T23:10:26
- Paper count: 10

## 1. Scalable Visual Pretraining for Language Intelligence

- Source: arxiv
- arXiv ID: 2607.09657
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.09657v1
- PDF: https://arxiv.org/pdf/2607.09657v1
- DOI: https://doi.org/10.48550/arXiv.2607.09657

### Authors

Yiming Zhang, Zhonghan Zhao, Wenwei Zhang, Haiteng Zhao, Tianyang Lin, Yunhua Zhou, Demin Song, Kuikun Liu, Haochen Ye, Haian Huang, Yuzhe Gu, Haijun Lv, Qipeng Guo, Bin Liu, Gaoang Wang, Kai Chen

### Abstract

The rapid progress of large foundation models has been driven predominantly by pretraining on large-scale text corpora. However, many forms of knowledge are conveyed through visual representations, where figures, typeset equations, and page layouts carry rich information that cannot be faithfully or completely captured by text alone. Yet current pretraining approaches discard these visual cues by converting visually rich sources, such as documents and web pages, into plain text for learning language intelligence. This paper challenges the default assumption that language models must be trained on text-only representations and shows that Visual Pretraining is a scalable learner for foundation model intelligence. To this end, we conduct a systematic study of unsupervised visual pretraining paradigms that directly leverage visual documents without text extraction. Across multiple backbones and benchmarks, visual pretraining on the same underlying corpora consistently outperforms text-only pretraining, offering an efficient pathway to scalable language intelligence.

### 中文一句话结论  
本文证明，直接在原始文档图像上进行无监督视觉预训练，能比传统纯文本预训练更高效地提升语言模型的科学推理能力，仅用约四分之一的训练 token 即可获得显著更优性能。

### English TL;DR  
Unsupervised visual pretraining on raw document images consistently outperforms text-only pretraining on the same corpus across multiple LLM backbones, using only ~25% of the tokens while improving scientific reasoning and cross-modal alignment.

### 中文详细总结  
当前大语言模型主要依赖大规模文本语料预训练，但科学文档中的图表、公式排版等视觉信息在转换为纯文本时会大量丢失。本文系统研究了无监督视觉预训练（VP）范式：直接以文档页面图像为输入，通过预测视觉潜在表示（Next Patch Prediction）进行自回归训练，无需文本提取或图像-文本配对监督。在 Qwen3.5、Llama3.1 等多个主干网络上，使用相同科学文档语料进行持续预训练后，VP 在 GPQA、MMLU-Pro、AIME-25 等基准上一致优于纯文本预训练（TP），且训练 token 数仅为 TP 的约 25%（20B vs 80B）。此外，VP 还能显著提升视觉与文本表示的对齐质量，在无多模态监督的情况下涌现出多模态推理能力。实验表明，VP 的优势随页面视觉结构密度增大而增强，验证了其通过保留视觉信息提升语言智能的机理。

### 方法 / 贡献  
- **方法**：提出了 Visual Pretraining (VP) 框架，将文档页面渲染为图像，经视觉编码器划分为前景 patch，在冻结的视觉特征空间中执行“下一 patch 预测”（类似 InfoNCE 损失），进行自回归无监督预训练。  
- **贡献**：  
  - 挑战了“语言模型必须从纯文本学习”的隐含假设，证明视觉预训练的可行性与优越性。  
  - 引入一种不依赖 OCR 或文本提取的视觉预训练方法，将视觉信号深度融入预测过程。  
  - 在匹配语料、多架构、多基准的统一设定下，系统论证了 VP 的有效性、效率与可扩展性。

### 实验或数据  
- **数据**：使用同一科学文档语料库（PDF 格式）进行持续预训练（CPT），其中 VP 直接使用页面图像，TP 使用同一页面解析出的文本。  
- **模型**：Qwen3.5、Qwen3、Llama3.2 Vision、Llama3.1 等主流基础模型。  
- **基准**：GPQA（pass@8）、AIME-25（32次平均分）、MMLU-Pro（pass@1）、HLE（pass@1），以及多模态基准 MMMU-Pro。  
- **主要结果**：  
  - VP 在四类模型上均领先 TP，GPQA 提升最高 3.22 分，MMLU-Pro 提升最高 2.1 分。  
  - VP 仅使用约 20B 视觉 token，TP 使用约 80B 文本 token。  
  - 随着训练推进，VP 的归一化增益持续增大（AIME-25 达 2.88 倍）。  
  - 视觉特征预测的余弦相似度与下游性能强相关。  
  - 页面视觉密度越高，VP 优势越大。  
  - 跨模态对齐指标（中心分离度、配对余弦相似度、线性 CKA、k-NN 重叠）均显著改善。

### 值得关注点  
- **效率惊人**：仅用传统方法约 25% 的 token 数即实现更优性能，极大降低计算成本。  
- **无监督跨模态对齐**：仅通过视觉预训练，无需任何图像-文本配对数据，即可让视觉与文本表示在共享空间中紧密对齐。  
- **视觉结构密度驱动**：收益主要来自富含图表、公式的页面，验证了视觉信息的关键作用。  
- **可扩展性**：下游增益随训练数据量和视觉预测质量提升而增长，且压缩分辨率仍保持性能。

### 局限性  
- 较大视觉 token 预算（如 2× 以上）时性能反而下降，可能与优化超参数未针对该设置调优有关。  
- 实验仅覆盖科学文档领域，对于其他类型视觉文档（如自然图像、网页）的泛化性未验证。  
- 视觉预训练在文本主导的低密度页面上优势微弱，依赖文档的视觉丰富度。  
- 当前框架仅使用单页图像，未建模文档的跨页结构或长程顺序关系。

## 2. NL-PAC: Specification Ambiguity and Certified Minimax Risk Floors in LLM-Mediated Supervision

- Source: arxiv
- arXiv ID: 2607.08961
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.08961v1
- PDF: https://arxiv.org/pdf/2607.08961v1
- DOI: https://doi.org/10.48550/arXiv.2607.08961

### Authors

Berkay Anahtarci

### Abstract

Large language models increasingly provide labels, evaluations, and feedback for tasks specified in natural language. When a specification admits multiple readings but the supervision channel does not reveal which is operative, additional labels reduce sampling error without resolving the resulting identification problem. We introduce Natural Language PAC (NL-PAC), a framework that uses a fixed model's thresholded decoding law to define admissible labels and candidate targets. The probability that multiple labels are admissible equals the diameter of the pointwise-admissible target class, and under target-blind supervision every learner incurs worst-case risk of at least half this diameter, at every sample size; the exact randomized minimax risk over this class is attained by a data-independent strategy. Finite-sample confidence bounds make these quantities certifiable from held-out unlabeled inputs. In a frozen Qwen~2.5--3B audit, one prespecified prompt yields a positive model-relative certificate, whereas a paraphrase and exact-rule controls yield zero. A held-out bridge audit finds that supplied candidate reading clauses fail the admissibility condition needed to transfer the certificate to coherent readings. The guarantee is specific to the audited model, prompt, threshold, and input distribution; extending it to human interpretations requires external validation.

### 中文一句话结论
NL-PAC 框架揭示了在 LLM 提供的自然语言监督中，规范歧义会导致一个不可约的极小最大风险下限，该下限可从无标注数据中认证。

### English TL;DR
NL-PAC formalizes how natural language specification ambiguity in LLM-mediated supervision creates an irreducible minimax risk floor that can be certified from unlabeled inputs.

### 中文详细总结
论文针对 LLM 在自然语言监督中因规范（prompt）歧义导致的识别问题，提出了 Natural Language PAC (NL-PAC) 框架。该框架利用固定模型的阈值化解码规则定义可接受标签集和候选目标。当同一输入存在多个可接受标签时，会产生一个不随样本量减少的风险下限（即点态可接受类的直径的一半）。该下限可通过无标注数据以有限样本置信区间进行认证。实验使用冻结的 Qwen 2.5-3B 模型：一个预设 prompt 产生了正的模型相对证书，而改写和精确规则控制均产生零证书。桥接审计（bridge audit）显示，提供的候选阅读条款不满足将证书迁移到连贯阅读所需的可接受性条件。该保证仅适用于审计的模型、prompt、阈值和输入分布；扩展到人类解释需外部验证。

### 方法 / 贡献
- 提出 NL-PAC 表示：阈值化模型输出定义点态可接受核及其容忍类，核直径等于重叠质量。
- 证明盲通道下的极小最大风险：在目标不可观测的条件下，最低风险至少为直径的一半，且存在数据独立的随机学习器达到精确值。
- 建立连贯阅读桥接条件：通过 η-覆盖条件连接点态选择器与全局阅读，但实验显示该条件在实际中可能不具信息量。
- 提供有限样本认证方法：基于 Hoeffding 不等式，从保持的无标注输入中认证风险下限。

### 实验或数据
- 在冻结的 Qwen 2.5-3B 模型上进行审计：使用预设 prompt、改写和精确规则控制，测试证书是否为正。
- 桥接审计：检查提供的候选阅读条款是否满足可接受性条件以转移证书。
- 受控任务：恢复预定为零和正的证书情况，并展示多类标签重叠带来的增益。
- 注：论文未公开额外数据集，实验基于模型输出和提示设计。

### 值得关注点
- 将规范歧义从统计误差中分离，识别出由模型解释内生导致的学习下限。
- 证书仅基于无标注数据，具备实际部署中的可操作性。
- 桥接审计为连接模型歧义与人类解释提供了形式化尝试，但实验显示条件严格。

### 局限性
- 证书仅针对特定模型、prompt、阈值和输入分布有效，不可直接泛化。
- 扩展到人类解释需要外部验证，桥接审计中的可接受性条件难以满足。
- 采样解码模式下的有限深度和阈值边际修正可能导致证书无效（实验中在可行深度下无信息）。
- 实验仅涉及单一模型（Qwen 2.5-3B），且 prompt 数量有限，需更多场景验证。

## 3. An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon?

- Source: arxiv
- arXiv ID: 2607.09053
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.09053v1
- PDF: https://arxiv.org/pdf/2607.09053v1
- DOI: https://doi.org/10.48550/arXiv.2607.09053

### Authors

Abhinav Rao, Liancheng Gong, Bin Hu, Atharva Naik

### Abstract

Recent work has reported Emergent Misalignment (EM), where language models fine-tuned on narrow, domain-specific misaligned datasets abruptly acquire broadly misaligned behavior, alongside evidence that this behavior can be reversed through limited realignment. We systematically study repeated alignment and misalignment cycles using controlled fine-tuning loops while tracking behavioral performance, and LoRA representations throughout training. Although we reproduce EM, we find that both misalignment and realignment are highly sensitive to superficial dataset characteristics, with apparent rapid realignment largely disappearing after controlling for response-length differences. We further find that previously reported mechanistic signatures, including representational phase transitions in LoRA space, do not consistently correlate with behavioral misalignment across training. Our results suggest that current evidence for EM is less robust than previously claimed and highlight the need for evaluation protocols that carefully control for these surface level dataset artifacts to identify the robustness of the EM phenomenon.

### 中文一句话结论
本研究表明，语言模型中的“涌现性错误对齐”和“重新对齐”并非稳健现象，而是高度依赖于数据集的表层特性（如回答长度），且缺乏一致的机制性证据。

### English TL;DR
This paper challenges the robustness of emergent misalignment and realignment in language models, showing that these phenomena are highly sensitive to superficial dataset artifacts like response length and lack consistent mechanistic signatures, calling into question the strength of prior evidence.

### 中文详细总结
本研究系统性地探索了语言模型在经历多轮对齐与错误对齐循环时的行为变化。作者通过控制微调循环（bad→good→bad 和 good→bad→good）以及跟踪 LoRA 表示的变化，重复了先前关于涌现性错误对齐的观察。然而，他们发现，错误对齐和重新对齐都非常容易受到数据集表层特征（如回答长度）的影响。在控制了这些变量后，表面上快速的重新对齐现象基本消失。此外，先前被报道为错误对齐机制性标志的表示相变（在LoRA空间中）与模型行为错误对齐之间并无稳定关联。因此，作者认为当前支持涌现性错误对齐的证据不如之前所声称的那样稳健。

### 方法 / 贡献
1.  **循环微调设计**：设计了两种交替微调顺序（bad→good→bad 和 good→bad→good），以系统性研究对齐-错误对齐循环中的模型动态和“迟滞现象”。
2.  **LoRA表示追踪**：在整个训练过程中，持续计算LoRA适配器在不同检查点间的余弦相似度，用于量化表示的漂移，而非仅评估最终行为指标。
3.  **关注数据集伪影**：明确指出并验证了回答长度等表层数据集特征对错误对齐和重新对齐现象的显著干扰作用，强调在评估此类现象时需严格控制这些因素。

### 实验或数据
- **模型**：Qwen2.5-14B-Instruct
- **数据集**：主要使用一个包含6000对配对的“风险性-安全性金融建议”数据集。该数据集基于先前研究中的“风险性金融建议”数据集，通过GPT-4o生成了对应的安全建议。
- **LoRA配置**：
    - 单一适配器：rank-1 LoRA，α=256（复现先前研究的“模型生物”设置）
    - 全部适配器：rank-32 LoRA，α=64，应用于所有目标模块
- **训练**：监督微调（SFT），保存每5个步骤的检查点，跟踪梯度范数。
- **主要发现**：
    - 复现了涌现性错误对齐。
    - 在控制回答长度后，重新对齐现象减弱。
    - LoRA表示相变与行为错误对齐不相关。
    - 微调到安全数据的梯度范数小于风险数据。

### 值得关注点
1.  论文揭示了目前关于“涌现性错误对齐”和“重新对齐”的稳健性可能被高估，提供了一个批判性的视角。
2.  通过循环微调和表征追踪的方法，为研究对齐的动态性（塑性）提供了新的实验范式。
3.  强调并直接测试了数据集表层伪影（回答长度）对评估结果的影响，这对于未来相关研究的设计具有重要参考价值。

### 局限性
1.  工作主要基于单一的基础模型（Qwen2.5-14B）和有限的几个数据集（主要是一个风险性金融建议数据集），其结论的泛化性有待在更多模型和不同任务上进行验证。
2.  虽然指出了回答长度的影响，但研究本身并未完全消除此类影响，也未深入探讨其他潜在的表层伪影。
3.  研究侧重于现象学观察和表面伪影控制，未提出新的机制性解释或理论模型来解释“涌现性错误对齐”的本质。
4.  实验仅使用了参数高效微调（LoRA），这些发现可能不完全适用于全参数微调等更复杂的训练场景。

## 4. Self-Guided Test-Time Training for Long-Context LLMs

- Source: arxiv
- arXiv ID: 2607.09415
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.09415v1
- PDF: https://arxiv.org/pdf/2607.09415v1
- DOI: https://doi.org/10.48550/arXiv.2607.09415

### Authors

Xinyu Zhu, Zhe Xu, Xiaohan Wei, Yunchen Pu, Fei Tian, Chonglin Sun, Kaushik Rangadurai, Hua Zhi, Frank Shyu, Sandeep Pandey, Luke Simon, Yu Meng, Xi Liu

### Abstract

Long-context processing has become increasingly important for large language models (LLMs), but simply extending the context window does not guarantee effective utilization of long inputs. As input length grows, accuracy often degrades, indicating that models still struggle to identify and use the evidence most relevant to a question. A promising way to improve long-context utilization is test-time training (TTT), which treats the test context as a training example for instance-specific parameter adaptation. However, applying TTT to the entire long context is prohibitively expensive, while adapting on randomly sampled spans introduces severe noise. Because most spans in a long context are irrelevant to the specific question, training on them may even degrade the base model's performance. Our preliminary study shows that TTT is highly sensitive to training-span quality: on LongBench-v2, TTT on randomly sampled spans hurts performance, whereas TTT on oracle spans substantially improves it. Motivated by this, we propose a simple method, Self-Guided TTT (S-TTT): before adaptation, the model identifies the evidence spans it should learn from, and the standard language-modeling training objective is applied only to those selected spans. On two challenging long-context reasoning benchmarks, LongBench-v2 and LongBench-Pro, S-TTT improves accuracy for both Qwen3-4B-Thinking-2507 and Llama-3.1-8B-Instruct, achieving up to a 15% relative improvement.

### 中文一句话结论
Self-Guided TTT（S-TTT）通过让模型自身在测试时识别并仅对问题相关的证据段进行训练，在长上下文推理任务上显著提升准确率，最高相对提升15%。

### English TL;DR
Self-Guided TTT (S-TTT) improves long-context LLM performance by having the model itself identify and then adapt on only the question-relevant evidence spans, avoiding the noise and cost of random or full-context test-time training.

### 中文详细总结
长上下文处理是大语言模型的重要能力，但单纯扩展上下文窗口并不能保证模型有效利用长输入，准确率常随长度增加而下降。测试时训练（TTT）通过将测试上下文作为训练样本来调整模型参数，是一种有前景的改进方法。然而，对完整长上下文进行TTT计算成本极高，而在随机采样的片段上训练则会引入大量噪声（因为大部分片段与问题无关），甚至可能降低基线性能。本文通过初步实验验证了训练片段质量对TTT效果的关键影响：在LongBench-v2上，随机片段TTT损害性能，而基于“黄金”片段（oracle）的TTT则大幅提升准确率。受此启发，作者提出Self-Guided TTT（S-TTT）：在适应前，模型先自行识别出上下文中与问题相关的证据片段，然后仅在这些选定片段上应用标准语言建模训练目标。在LongBench-v2和LongBench-Pro两个长上下文推理基准上，使用Qwen3-4B-Thinking-2507和Llama-3.1-8B-Instruct模型，S-TTT均一致提升准确率，最高相对提升15%，并优于随机片段TTT、全上下文TTT、qTTT、QRHead Span TTT及LongLLMLingua等基线方法。

### 方法 / 贡献
1. **识别关键瓶颈**：首次指出训练数据质量是长上下文TTT中未被充分探索的核心瓶颈，并实验证明噪声片段会降低性能，而高质量证据片段带来显著提升。
2. **提出S-TTT框架**：利用模型自身作为测试时数据选择器，先选择问题相关证据段，再在这些片段上进行TTT，避免全上下文的高成本和随机采样的噪声。
3. **实验验证**：在两种模型和两个基准上，S-TTT一致提升长上下文性能，并优于多种强基线。

### 实验或数据
- **基准**：LongBench-v2（四选一多选题，评估长上下文推理）和LongBench-Pro（英文子集，评估更广泛的长上下文能力）。
- **模型**：Qwen3-4B-Thinking-2507 和 Llama-3.1-8B-Instruct。
- **结果**：S-TTT在所有模型和基准上均提升准确率，尤其在64k–128k长上下文桶中提升更显著。例如，在LongBench-v2上，Qwen3-4B模型从40.4%提升至45.9%（使用oracle span时），S-TTT在随机回退情况下仍优于基线。具体数据见论文表格。

### 值得关注点
- **训练数据质量是关键**：随机片段TTT可能损害性能，而高质量片段带来收益，说明TTT成功的关键在于“训练什么”而非仅“如何训练”。
- **模型自选片段有效**：即使模型自选片段不如oracle完美，S-TTT仍显著优于随机采样，证明模型自身具备识别相关证据的能力。
- **长上下文场景收益更大**：当上下文更长、噪声更多时，S-TTT的优势更为突出，表明其针对性解决长上下文核心问题。

### 局限性
论文未明确讨论局限性，但基于方法可推断潜在问题：S-TTT依赖模型自身识别相关片段的能力，若模型无法正确识别（如输出无效span），则需回退到随机采样，可能影响效果。此外，实验仅验证了4B和8B参数规模的模型，更大模型或不同任务类型上的普适性有待进一步研究。

## 5. Automatic Thematic Indexing of Large Literary Corpora: A Machine Learning Approach to Voltaire's Complete Works

- Source: arxiv
- arXiv ID: 2607.09316
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.09316v1
- PDF: https://arxiv.org/pdf/2607.09316v1
- DOI: https://doi.org/10.48550/arXiv.2607.09316

### Authors

Miguel Arana-Catania, Gillian Pink, Glenn Roe

### Abstract

Thematic indexing -- the practice of assigning structured conceptual labels to sections of text -- is essential to scholarly access in large-scale literary and historical editions, yet it remains a largely manual, labour-intensive process. This paper explores the application of machine learning to automatic thematic indexing, using two substantial sub-corpora of the Complete Works of Voltaire as a test case: the Essai sur les mœurs et l'esprit des nations and the Questions sur l'Encyclopédie. The task is framed as a multi-label classification problem, in which a model must assign the set of index entries that a professional indexer would apply to a given page of text. We compare a range of approaches -- from encoder-based models with classification heads to generative large language models (LLMs) fine-tuned via Low-Rank Adaptation (LoRA) -- spanning model sizes from approximately 3 to 120 billion parameters. Our best-performing model, from the Mistral family in a 4-bit quantised configuration, achieves F1 scores of up to 0.67; we argue that these figures represent lower bounds, given the inherent subjectivity of professional indexing and the frequency with which model predictions prove semantically valid despite diverging from the print index. We further evaluate cross-corpus generalisation and conduct a detailed qualitative analysis of model behaviour on literary and rhetorical features of the source texts that prove particularly resistant to automated treatment. Our findings have implications for the broader challenge of providing structured thematic access to large-scale literary and historical corpora.

### 中文一句话结论
本研究表明，通过LoRA微调的量化生成式大语言模型（尤其是4-bit量化Mistral模型）可在伏尔泰全集等大型文学语料的自动主题标引任务中达到F1值0.67，但专业标引的主观性意味着实际性能可能更高。

### English TL;DR
Fine-tuned generative LLMs (a 4-bit quantized Mistral model) achieve F1 scores up to 0.67 for automatic thematic indexing of large literary corpora, using Voltaire's works as a test case; performance is considered a lower bound due to the subjectivity of professional indexing.

### 中文详细总结
该研究将主题标引建模为多标签分类问题，目标是为每页文本分配专业标引员会使用的索引条目。实验比较了多种方法：从基于编码器（encoder）加分类头的模型，到通过LoRA微调的生成式大语言模型（参数规模从约3亿到1200亿不等）。最佳模型来自Mistral系列，采用4-bit量化配置，在《Questions sur l'Encyclopédie》（QE）子语料上（过滤低频标签后）F1最高达0.67。作者认为该F1是下界，因为专业标引本身存在主观性，且模型许多预测在语义上成立但不同于印刷索引。研究还评估了跨语料泛化能力（EM与QE之间），并对模型在处理文学修辞特征时的困难进行了定性分析。结论对为大型文学和历史语料提供结构化主题访问具有启示。

### 方法 / 贡献
- 将自动主题标引转化为封闭词表的多标签分类任务，利用已有的专业印刷索引作为训练和评估标准（非传统关键词提取）。
- 系统比较了基于编码器的模型（含分类头）与生成式LLM（经LoRA微调）在3亿至1200亿参数规模下的表现。
- 采用QLoRA实现4-bit量化，降低了微调大模型的计算门槛。
- 最佳模型（Mistral-Small-3.2-24B，4-bit量化）在QE上获得F1=0.67，并指出该数值为下界。
- 分析了跨语料泛化能力以及文学修辞特征带来的挑战。

### 实验或数据
- 数据集：伏尔泰《Essai sur les mœurs》（EM，7卷）和《Questions sur l'Encyclopédie》（QE，7卷），来自《伏尔泰全集》（OCV）。原始文本为TEI-XML格式，索引条目分层次（EM有3级，QE有4级），实验主要使用一级条目。
- 预处理：提取主文本，去除TEI标记；排除交叉引用（voir）和仅涉及脚注的条目。
- 实验设置：每页文本作为实例，模型需预测该页对应的索引条目集合。
- 结果：最佳模型F1=0.67（QE，过滤低频标签后），跨语料泛化实验和定性分析也附有结果。

### 值得关注点
- 首次将LLM微调系统性地应用于大型文学语料的自动分析型索引生成。
- 使用4-bit量化+LoRA使得超大模型（如120B）的微调在消费级硬件上可行。
- 发现模型预测虽与印刷索引不完全一致，但许多在语义上有效，提示当前F1低估了实际能力。
- 对文学修辞特征（如隐喻、反讽）的定性分析揭示了自动标引的难点。

### 局限性
- 标签分布极度长尾：人文索引中大量低频标签导致模型难以学习。
- 专业标引本身具有主观性，使得精确评估困难（模型预测可能语义正确但与参考标准不一致）。
- 模型对文学/修辞特征（如反讽、隐喻、历史典故）处理不佳。
- 跨语料泛化能力有限，模型从一个作品（EM）到另一个（QE）转移时性能下降。
- 仅使用了两个子语料（Voltaire的EM和QE），结论对其他时代、语言或类型语料的适用性未验证。

## 6. Mixture of Probes: Learning from Privileged Modalities in Multimodal LLMs Through Probing

- Source: arxiv
- arXiv ID: 2607.08839
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.08839v1
- PDF: https://arxiv.org/pdf/2607.08839v1
- DOI: https://doi.org/10.48550/arXiv.2607.08839

### Authors

Dominick Reilly, Qiyu Wu, Hiromi Wakaki, Srijan Das, Yuki Mistufuji

### Abstract

Multimodal Large Language Models (MLLMs) are typically designed under the assumption that all modalities available during training will also be accessible at inference. However, many real-world settings violate this assumption, requiring models to operate under a privileged modality setting, where auxiliary modalities are available only during training. While these modalities contain valuable information, existing MLLMs largely fail to leverage them effectively, as they treat modalities as interchangeable inputs rather than sources of complementary supervision. We propose Mixture of Probes (MoP), a novel framework that disentangles modality-specific and modality-general signals within the MLLM, allowing the model to preserve modality-dependent structure while learning transferable representations across modalities. At its core, MoP achieves this through a structured probing mechanism that extracts and organizes information from intermediate representations of a shared modality encoder, rather than relying only on final-layer alignment as done in existing MLLMs. To support this disentanglement, we further introduce MoP Cross-modal Training (MoP-X), a training strategy for MoP centered around a probe disentanglement loss that prevents probe collapse and encourages cross-modal learning. We evaluate MoP across two domains spanning eight tasks and four modalities under a comprehensive evaluation protocol tailored to the privileged modality setting, where each modality is independently treated as the sole input at inference time. MoP consistently outperforms strong MLLM baselines, achieving up to 65% relative improvement, demonstrating that auxiliary modalities, even when unavailable at inference, can provide substantial gains when effectively leveraged during training. Code, model checkpoints, and evaluation protocols will be made available at https://github.com/Sony/MoP.

### 中文一句话结论
本文提出混合探测器框架，通过结构化探测机制分离模态特异与模态通用信号，使多模态大语言模型能在推理时仅使用单一模态的情况下，有效利用训练阶段才可用的辅助模态信息，性能提升最高达65%。

### English TL;DR
The Mixture of Probes (MoP) framework improves Multimodal LLMs in the privileged modality setting (where auxiliary modalities are only available during training) by disentangling modality-specific and modality-general signals through a structured probing mechanism on a shared encoder, achieving up to 65% relative improvement in single-modality inference performance.

### 中文详细总结
多模态大语言模型通常假设训练时所见的所有模态在推理时也可用，但现实中常出现辅助模态仅存在于训练阶段而推理时缺失的"特权模态"场景。现有MLLM将各模态视为可互换的输入，缺乏有效利用辅助模态知识的能力。本文提出MoP框架，在一个共享的通用编码器中，通过在不同深度插入可学习的探针（probes），分别提取模态特异和模态通用的表征。模态特异探针仅依赖单模态输入，捕捉该模态独特结构；模态通用探针则利用所有模态信息，学习跨模态可迁移表征。配合提出的MoP-X训练策略（包含探针解耦损失和模态交错批处理），MoP有效防止探针坍塌并促进跨模态学习。在日常生活活动和音乐理解两个领域、8个任务、4种模态上的实验表明，MoP在推理时单模态输入条件下持续优于强基线模型，相对性能提升最高达65%。

### 方法 / 贡献
1. **形式化定义了MLLM的特权模态设置**：训练时多模态可用，推理时仅单一模态可用，并指出现有方法无法有效利用这种不对称性。
2. **提出混合探测器架构（MoP）**：在共享编码器不同深度插入可学习的探针，将模态特异信号与模态通用信号显式分离，从而保留模态依赖结构的同时学习可迁移表征。
3. **提出MoP跨模态训练策略（MoP-X）**：核心包括探针解耦损失（显式鼓励两类探针分离）和模态交错批处理（确保训练中跨模态持续交互）。
4. **跨领域、多任务、多模态验证**：在日常生活活动和音乐理解两个领域、8个任务、4种模态上系统验证有效性。

### 实验或数据
- **领域与任务**：日常生活活动领域（ADL，使用第一视角视频、第三视角视频、深度图）和音乐理解领域（使用音频-视频配对数据），共8个任务。
- **模态**：第一视角视频、第三视角视频、深度图、音频，共4种模态。
- **评估协议**：在特权模态设置下，每种模态独立作为推理时的唯一输入进行评估。
- **基线**：与强MLLM基线（如ImageBind-LLM、OneLLM、Video-LLaVA等）比较。
- **结果**：MoP在所有推理条件下持续超越基线，性能相对提升最高达65%。
- **代码与模型**：将于https://github.com/Sony/MoP 公开。

### 值得关注点
1. **问题设定新颖实用**：特权模态设置贴合实际部署场景（如可穿戴设备训练、低成本传感器推理），具有显著应用价值。
2. **神经科学启发**：灵感来源于人脑中感觉特异地图与感觉通用抽象的分离机制，理论基础扎实。
3. **结构创新优于浅层对齐**：利用编码器中间层而非仅最后一层的表征，更丰富地捕捉不同抽象层次的信息。
4. **探针解耦损失的巧妙设计**：防止不同探针坍塌成相同信号，保证真正的分离学习。
5. **跨领域泛化验证**：在视觉主导（ADL）和音频-视觉（音乐）两个截然不同的领域均有效，泛化性强。

### 局限性
1. **依赖通用编码器架构**：MoP设计基于共享通用编码器的MLLM范式，可能不适用于使用多个独立模态编码器的传统架构。
2. **辅助模态训练成本**：虽然推理时仅需单一模态，但训练阶段仍需所有模态数据，数据收集成本不变。
3. **未探讨模态间相关性影响**：不同辅助模态对目标模态的增益程度可能不同，论文未系统分析何种辅助模态最有效。
4. **任务类型有限**：仅在活动识别和音乐理解两类任务上验证，对问答、生成等更复杂任务的表现未知。
5. **推理时信息保留上限**：通过探针提取的跨模态通用知识是否完全捕获了辅助模态中所有对目标模态有用的信息，仍待进一步分析。

## 7. HALO: Hybrid Adaptive Latent Reasoning for Language Models

- Source: arxiv
- arXiv ID: 2607.08775
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.08775v1
- PDF: https://arxiv.org/pdf/2607.08775v1
- DOI: https://doi.org/10.48550/arXiv.2607.08775

### Authors

Micah Zhang

### Abstract

We study how to improve a frozen pretrained language model with a small amount of adaptive extra computation. A simple approach is to add additional refinement steps on top of the backbone hidden states, but fixed extra refinement can be wasteful: a one-step refinement head may be too weak, while forcing a second full-sequence refinement step everywhere can increase compute without improving transfer. We introduce HALO, a hybrid adaptive latent-refinement method that combines a coarse refinement stage with selective second-stage latent refinement on a subset of tokens chosen by token scoring and monotonic token halting. On the main public benchmark comparison built from MMLU-Pro and GPQA-Diamond, HALO achieves the best overall average among the paper-facing methods, outperforming the frozen backbone, fixed-1, and fixed-2. Internal analysis further shows that HALO reaches nearly the same token-accuracy level as fixed-2 while using fewer average applied refine steps than fixed-1 and far fewer than fixed-2. These results suggest that the key advantage is not simply more refinement, but a better allocation of refinement: HALO achieves the strongest paper-facing result while also using less measured controller compute than either fixed baseline.

### 中文一句话结论
HALO 通过混合自适应潜在推理，在仅对部分 token 进行选择性第二阶段的细化下，在 MMLU-Pro 和 GPQA-Diamond 上取得了优于固定一步或两步全序列细化基线的整体平均性能，同时使用了更少的细化和控制器计算。

### English TL;DR
HALO introduces a hybrid adaptive latent-refinement method that selectively applies second-stage computation to only a subset of tokens, achieving superior performance on MMLU-Pro and GPQA-Diamond while using fewer refinement steps than fixed one-step or two-step baselines.

### 中文详细总结
论文研究了如何在冻结的预训练语言模型上，通过少量自适应额外计算来提升性能。作者指出，固定步数的细化（如固定一步或两步全序列细化）可能浪费计算：一步细化能力不足，两步全序列细化则增加计算量且不一定改善迁移。为此，HALO 提出了一种混合自适应潜在细化方法，结合粗细化阶段和选择性第二阶段的潜在细化。该选择基于 token 评分和单调 token 停止机制，只对部分 token 施加第二阶段的稠密计算。在公共基准（MPLU-Pro 和 GPQA-Diamond）上，HALO 获得了方法比较中的最佳整体平均分数，优于冻结主干、固定一步和固定两步基线。内部分析显示，HALO 的 token 准确率几乎与固定两步基线持平，但平均使用的细化步数少于固定一步且远少于固定两步。核心结论是：关键在于更优的计算分配，而非单纯增加细化步数。

### 方法 / 贡献
- 提出了 HALO，一种混合自适应潜在细化框架，用于扩展冻结语言模型，具备选择性第二阶段的计算。
- 粗细化阶段后，通过 token 评分和单调停止机制，只将预算内的一定比例 token（默认 35%，最少 8 个）送入第二阶段的潜在细化块。
- 控制器利用 logit 特征计算每 token 的保留概率，并可在第一步就跳过部分 token，使得平均应用细化步数可低于 1。
- 训练时仅训练细化/控制器参数，冻结主干，使用监督下一 token 目标及辅助损失（随时监督、预算正则化、预算一致性训练）。
- 主要贡献：在公共基准上获得最佳整体平均性能，同时使用了比固定一步和两步基线更少的平均应用细化步数。

### 实验或数据
- 公共基准：MPLU-Pro 和 GPQA-Diamond。HALO 在 GPQA-Diamond 上表现最强（33.00 ± 0.99），但在 MMLU-Pro 上冻结主干仍最优（38.54）。
- 内部评估：在 512 个样本、长度 1024 的序列上评估 token 准确率、提升幅度和平均应用细化步数。HALO 的 token 准确率接近固定两步，但平均步数少于固定一步且远少于固定两步。
- 冻结主干为 microsoft/Phi-4-mini-instruct，训练数据为 UltraChat-200k 的 4k 子集。
- 报告了六次独立种子的均值和标准差。

### 值得关注点
- HALO 并非在所有基准上均胜出，其优势主要来自 GPQA-Diamond，而 MMLU-Pro 上冻结主干最强——论文明确承认这点，强调质量-计算权衡而非全面统治。
- 固定两步基线并未比固定一步更好，甚至略有下降，说明均匀增加细化步数无效。
- HALO 在更少计算下达到近似的 token 准确率，表明选择性细化的价值。
- 训练-测试一致性被强调：同样的 token 评分和停止规则在评估时也应用。

### 局限性
- 仅基于两个公共基准（MMLU-Pro 和 GPQA-Diamond）做主要比较，泛化性有待更多任务验证。
- 实验仅在单一冻结主干（Phi-4-mini-instruct）上进行，其他模型或尺寸未测试。
- HALO 未在所有指标和基准上取得最优，尤其 MMLU-Pro 上不如冻结主干。
- 内部评估样本量有限（最多 512），可能无法完全代表大规模推理行为。
- 方法依赖额外的控制器和细化参数训练，且训练数据仅为 4k 例子，数据规模和作用未深入探讨。

## 8. Super-Tuning: From Activation-Aware Pruning to Sparse Fine-Tuning

- Source: arxiv
- arXiv ID: 2607.09287
- Relevance: 3.9

### Links

- Abstract: http://arxiv.org/abs/2607.09287v1
- PDF: https://arxiv.org/pdf/2607.09287v1
- DOI: https://doi.org/10.48550/arXiv.2607.09287

### Authors

Ivan Ilin, Philip Zmushko, Peter Richtárik

### Abstract

Large language models (LLMs) remain expensive to fine-tune because full-parameter updates require substantial memory, compute, and per-task storage. We study whether saliency signals originally developed for pruning can be reused to choose where a model should adapt. We propose Super, a sparse parameter-efficient fine-tuning (PEFT) method that fixes a small trainable support using a Wanda-style activation-weighted magnitude score [Sun et al., 2023] computed from a calibration pass. We then introduce Supra, a hybrid adapter that combines this sparse update with LoRA while preserving a matched trainable-parameter budget through a simple budget-splitting rule. In single-seed Math17K arithmetic experiments on Llama-3.2-1B and Meta-Llama-3-8B, the best Super/Supra variants achieve the highest average accuracy among the tested schedule-selected adapter configurations. We also include a PaFi-style magnitude-only support as a closest training-free sparse baseline and find that low-score supports under both magnitude and Wanda-style orderings can be effective. These results suggest that simple pruning-inspired orderings can provide useful fixed sparse supports for PEFT, especially when combined with low-rank adapters.

### 中文一句话结论
本文提出基于Wanda剪枝得分的稀疏微调方法Super及其与LoRA结合的混合方法Supra，在算术推理任务上达到了较高的平均准确率。

### English TL;DR
This paper proposes Super, a sparse PEFT method that uses Wanda-style activation-weighted magnitude scores to select a fixed trainable support, and Supra, a hybrid adapter combining sparse updates with LoRA. On Math17K arithmetic experiments with Llama-3.2-1B and Meta-Llama-3-8B, the best variants achieve the highest average accuracy among tested adapter configurations.

### 中文详细总结
大型语言模型的全面微调需要大量内存、计算和存储资源。本文研究了能否将原本用于剪枝的显著性信号复用于选择模型应该适应的参数位置。作者提出了Super方法，这是一种稀疏参数高效微调方法，它通过一次校准前向传播计算Wanda风格的激活加权幅度分数，从而固定一个小的可训练参数子集。随后提出了Supra，这是一种混合适配器，通过简单的预算分割规则将稀疏更新与LoRA结合，同时保持匹配的可训练参数预算。实验在Llama-3.2-1B和Meta-Llama-3-8B上进行单种子Math17K算术推理任务，最佳Super/Supra变体在测试的调度选择适配器配置中达到最高平均准确率。研究还发现，基于幅度和Wanda排序的低分数支持集都可以是有效的。

### 方法 / 贡献
1. 提出Super：基于Wanda剪枝得分的稀疏微调方法，无需梯度或额外训练阶段即可选择可训练参数
2. 提出Supra：混合方法，结合Wanda选择的稀疏更新与LoRA低秩适配
3. 提出透明参数预算拆分规则，将固定参数预算映射为逐层LoRA秩
4. 在匹配参数预算下系统比较LoRA、SIFT、RoSA、随机稀疏支持、PaFi幅度支持、Super和Supra

### 实验或数据
- 模型：Llama-3.2-1B 和 Meta-Llama-3-8B
- 数据集：Math17K（算术推理）
- 评估基准：AddSub, MultiArith, SingleEq, GSM8K, AQuA, SVAMP
- 实验设置：单种子运行，匹配可训练参数预算，测试1轮和3轮微调调度
- 结果：最佳Super/Supra变体在所有测试配置中达到最高平均准确率

### 值得关注点
1. 使用训练无关的剪枝得分（Wanda）选择固定稀疏支持，避免梯度计算
2. 发现低分数（BottomK）支持在稀疏和混合设置中往往表现更好
3. 简单幅度基线（PaFi风格）在特定设置下也有效
4. Supra混合方法在匹配参数预算下展示了稀疏与低秩更新的互补性

### 局限性
- 仅使用Math17K算术数据集和Llama系列模型进行单种子实验，泛化性有限
- 稀疏支持一旦选定即固定不变，无法在训练过程中动态调整
- 未在更大规模模型（如70B+）或多语言/多任务场景下验证
- 最佳支持方向（TopK vs BottomK）依赖模型大小、训练调度和适配器类型
- 仅测试了Wanda和幅度两种得分，未探索更复杂的显著性度量

## 9. Sensitivity-Aware Thresholding and Token Routing for Activation Sparsification in Large Language Models

- Source: arxiv
- arXiv ID: 2607.08991
- Relevance: 3.9

### Links

- Abstract: http://arxiv.org/abs/2607.08991v1
- PDF: https://arxiv.org/pdf/2607.08991v1
- DOI: https://doi.org/10.48550/arXiv.2607.08991

### Authors

Bishmoy Paul, Youngmin Yi, Hoeseok Yang

### Abstract

Efficient inference in Large Language Models (LLMs) requires deciding where computation can be reduced while preserving model quality. We study this problem through multilayer perceptron (MLP) activation sparsification and token-level conditional routing. We first propose Sensitivity-Aware Thresholding for Sparsity (SATS), a threshold calibration method to choose layerwise gate thresholds using a local MLP output sensitivity proxy rather than calibrating thresholds directly from activation percentiles. While SATS retains the existing mechanism of sparsifying MLP activations by thresholding gate activations, it replaces percentile-based calibration with a sensitivity-aware selection rule. We then introduce a lightweight token routing framework that dynamically selects between a base path and a modified path on a per-token basis, rather than applying the modified computation uniformly to all tokens. We evaluate both methods on multiple recent open-weight LLMs. Our results show that SATS improves over the threshold-based sparsification baseline at matched actual sparsity and that token routing yields a more favorable quality-throughput trade-off than static activation modification baselines. Overall, our results suggest that improved threshold calibration and token routing can improve the quality-throughput trade-off in LLMs.

### 中文一句话结论
本文提出SATS（敏感度感知阈值选择）与令牌路由方法，通过改进MLP激活稀疏化的阈值校准和逐令牌动态路径选择，在保持模型质量的同时提升LLM推理吞吐量。

### English TL;DR
This paper introduces Sensitivity-Aware Thresholding for Sparsity (SATS) and a token routing framework to improve the quality-throughput trade-off in LLM inference. SATS replaces percentile-based threshold calibration with a sensitivity-aware method using local MLP output distortion, while token routing dynamically selects between dense and sparse computation paths per token based on a precomputed lookup table. Experiments on Llama 3.1 8B and Qwen 3 8B show that both methods improve over static sparsification baselines.

### 中文详细总结
大型语言模型（LLM）推理效率的关键在于在保持模型质量的前提下减少计算量。本文聚焦于MLP层的激活稀疏化与令牌级条件路由。首先，提出SATS（敏感度感知阈值选择），该方法通过局部MLP输出失真代理来校准每层门控阈值，取代了基于激活百分位数的传统校准方式。SATS保留CATS的运行时掩码机制，但将阈值选择从“多少激活被移除”转向“移除造成的输出损伤有多大”。其次，引入轻量级令牌路由框架，根据令牌身份在基准路径（完整MLP）和稀疏路径（激活阈值化后MLP）之间动态选择，而非对所有令牌统一应用稀疏计算。路由决策仅依赖令牌身份，可简化为查找表，开销极小。实验在Llama 3.1 8B和Qwen 3 8B上进行，结果表明：在匹配实际稀疏度下，SATS优于基于百分位数的阈值稀疏化基线；令牌路由相比静态稀疏执行获得更优的质量-吞吐量权衡。整体上，改进的阈值校准和令牌路由能有效提升LLM推理的效用效率。

### 方法 / 贡献
- **SATS（敏感度感知阈值选择）**：定义局部MLP输出失真度量（Errₗ(t)），基于校准数据集估计每个候选阈值造成的输出损伤；引入层间误差预算b，选择满足预算的最大阈值；通过外层搜索实现目标稀疏度匹配。
- **令牌路由**：在校准语料上统计每个令牌类型在稀疏路径下的额外交叉熵损失（d_i = max(0, ℓ_sparse - ℓ_base)），存储为查找表；推理时根据阈值τ决定令牌走基准路径还是稀疏路径。
- 保留CATS的运行时掩码机制，兼容现有硬件高效实现。
- 在多个开放权重LLM上验证了质量-吞吐量权衡的改进。

### 实验或数据
- **模型**：Llama 3.1 8B、Qwen 3 8B。
- **稀疏度水平**：30%、50%、70%实际稀疏度（CATS基线）；令牌路由中使用SATS匹配50%稀疏度，路由分数设为25%、50%、75%。
- **数据集**：微调使用RefinedWeb子集；下游任务评估使用PIQA、OpenBookQA、ARC-Easy、Winogrande、HellaSwag、SciQ、BoolQ（来自LM Eval Harness）；语言建模质量用WikiText-2测试集和RefinedWeb保留测试集的困惑度衡量。
- **吞吐量**：报告FP32端到端吞吐量，并对比BF16半精度。
- **额外设置**：最终MLP层保留CATS阈值（因SATS在该层影响过大），其余层使用SATS。

### 值得关注点
- 首次将阈值校准从“百分位数”转向“输出损伤感知”，使稀疏化更关注模型质量。
- 令牌路由通过令牌身份实现轻量级动态路径选择，无需额外计算开销。
- 实验表明，SATS在匹配实际稀疏度下优于CATS基线；令牌路由进一步改善质量-吞吐量权衡。
- 方法兼容现有CATS运行时掩码，易于部署。

### 局限性
- 最终MLP层不适用SATS（因该层阈值化对生成质量影响过大），需保留CATS阈值，说明SATS在不同层间效果不一致。
- 令牌路由依赖校准语料统计平均，无法捕捉上下文相关的风险差异，可能对罕见或长尾令牌不鲁棒。
- 实验仅针对8B参数规模的模型，未验证在更大模型（如70B、180B）或不同架构上的可迁移性。
- 校准过程需要额外计算（如局部失真估计和路由分数统计），可能增加模型部署前的准备成本。

## 10. Conceptual Networks for Cross-Linguistic Idiomatic Expressions:A Feature-Based Graph Approach

- Source: arxiv
- arXiv ID: 2607.09576
- Relevance: 3.8

### Links

- Abstract: http://arxiv.org/abs/2607.09576v1
- PDF: https://arxiv.org/pdf/2607.09576v1
- DOI: https://doi.org/10.48550/arXiv.2607.09576

### Authors

Kiran Pala, Punam Silu, Lixun Yu

### Abstract

We present an interpretable network-based framework for representing idiomatic and figurative meaning across eight typologically diverse languages, totaling 160 conventional expressions, the large majority of which are idiomatic. Each expression is annotated with binary conceptual features (containment, concealment, emotional, social, etc.) derived from cognitive-linguistic theory, and pairwise Jaccard similarities define a weighted graph. Community detection reveals that idioms cluster by conceptual schema rather than by language, producing a structure consistent with cognitive-linguistic predictions. The conceptual network captures unique semantic information not present in distributional embeddings, can be scaled via automatic annotation with LLMs, improves downstream idiom detection, and remains robust when enriched with corpus frequencies. Cross-lingual transfer experiments show that conceptual proximity alone can identify acceptable translation equivalents across five language families, with substantial gains over embedding-based baselines. Ablation studies demonstrate that all three feature dimensions -- schemas, roles, and valence -- contribute non-redundantly to both the network's organizational properties and its performance on idiom detection, and that specific graph-derived signals (community membership, neighbor similarity) are particularly informative. The framework offers an interpretable, cross-linguistically stable representation of idiomatic meaning, combining theoretical grounding with practical utility.

### 中文一句话结论  
本文提出一个基于概念特征的图网络框架，覆盖8种语言160条习语，证明习语按概念图式而非语言聚类，为跨语言习语理解提供了可解释的表示。

### English TL;DR  
This paper introduces an interpretable, feature-based graph framework for representing idiomatic expressions across eight languages, demonstrating that idioms cluster by conceptual schema rather than language, enabling improved cross-lingual translation and idiom detection.

### 中文详细总结  
- 数据：从英语、印地语、巴格里语、芬兰语、日语、西班牙语、汉语、马拉雅拉姆语中各选20条习语，共160条，涵盖5个语系。  
- 特征：基于认知语言学理论，为每条习语标注二元概念特征（包含、隐藏、情感、社会等三种维度：图式、角色、情感价）。  
- 网络：利用Jaccard系数构建加权图（密度0.37），Louvain社区检测得到5个社区（模块度Q=0.61）。  
- 结果：社区结构与概念图式的NMI=0.76，与语言的NMI仅0.10，说明聚类由概念驱动而非语言。  
- 应用：概念网络在下游习语检测、跨语言翻译等价物识别中优于基于嵌入的基线；消融实验表明所有特征维度均非冗余；支持通过LLM自动标注扩展，加入语料频率后仍保持鲁棒性。

### 方法 / 贡献  
- **方法**：手工标注二元概念特征 → Jaccard相似度 → 加权图 → 社区检测；利用LLM实现自动特征标注扩展。  
- **贡献**：  
  1. 首次在8种类型多样语言上构建理论驱动的习语概念网络。  
  2. 揭示习语按概念图式跨语言聚类，验证认知语言学预测。  
  3. 提供可解释、跨语言稳定的习语表示，提升下游任务性能。  
  4. 自动化标注方案使框架可扩展至更大规模。

### 实验或数据  
- **数据集**：8种语言各20条习语（共160条），经多名母语者验证，并参照对应语料库（COCA、EMILLE、Suomi24等）确认使用频率。  
- **实验**：  
  - 社区结构分析（NMI、模度、度分布、小世界性）。  
  - 与XLM-R嵌入的余弦相似度图对比（概念图在NMI上显著更高）。  
  - 下游习语检测任务（概念特征提升检测性能）。  
  - 跨语言转移实验：仅凭概念邻近性即可识别可接受翻译等价物，优于嵌入基线。  
  - 消融研究：图式、角色、情感价三个维度均贡献非冗余信息；社区归属与邻居相似性是特别有效的信号。  
  - 自动标注实验：使用LLM生成特征，效果可比手动标注。  
  - 动态丰富：加入语料库频率后框架仍保持鲁棒。

### 值得关注点  
- 特征基于认知语言学理论（图像图式），具有理论支撑与可解释性。  
- 跨语言结构稳定，不受语言类型差异影响。  
- 可自动标注（LLM）扩展，实用性强。  
- 在习语检测与跨语言翻译中取得明显增益，优于纯分布表示。

### 局限性  
- 数据集规模较小（仅160条习语），可能限制泛化性。  
- 特征为二元值，难以捕捉连续或更细粒度的概念差异。  
- 手工标注成本高，虽支持LLM自动标注但仍有误差。  
- 语言与习语的选择偏向特定域（如交流、情感），未覆盖所有概念域。  
- 摘要未明确讨论其他潜在局限（如社区划分的稳定性、特征维度的完备性）。

## Processing Notes

- Duplicate papers skipped: 0