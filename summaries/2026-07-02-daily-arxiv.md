# Daily arXiv - 2026-07-02

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-02T23:34:45
- Paper count: 10

## 1. ALEE: Any-Language Evaluation of Embeddings via English-Centric Minimal Pairs

- Source: arxiv
- arXiv ID: 2607.00171
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2607.00171v1
- PDF: https://arxiv.org/pdf/2607.00171v1
- DOI: https://doi.org/10.48550/arXiv.2607.00171

### Authors

Andrianos Michail, Stylianos Psychias, Michelle Wastl, Simon Clematide, Rico Sennrich, Juri Opitz

### Abstract

Text embeddings are standard for semantic similarity tasks, yet their evaluation remains an open challenge. Current benchmarks are static, cover only a limited set of languages, are often domain-specific, susceptible to overfitting, and poorly representative of low-resource languages. To address these limitations, we introduce ALEE, a framework that extends Sentence Smith (Li et al., 2025) to the cross-lingual and paragraph level. ALEE uses Abstract Meaning Representations (AMR) to generate English minimal pairs with controlled, fine-grained semantic shifts, which are paired with translations in target languages. This approach enables targeted diagnostics for models in any language with English parallel data. We conduct a large-scale empirical study across a diverse set of embedding models and 275+ languages spanning three parallel datasets. On ALEE, performance varies substantially across languages, text lengths, and linguistic phenomena, exposing persistent gaps in cross-lingual semantic representation that track language prevalence in training resources and subword tokenization. We release ALEE at https://github.com/Andrian0s/any-lang-embed-eval

### 中文一句话结论
ALEE通过英语中心的最小语义对比对（minimal pairs）评估任意语言文本嵌入模型，发现模型性能在275+语言上差异巨大，且与语言在训练数据中的出现频率和子词切分紧密相关。

### English TL;DR
ALEE introduces a dynamic cross-lingual evaluation framework that uses Abstract Meaning Representations to generate English minimal pairs with controlled semantic shifts, enabling targeted diagnostics of text embeddings across 275+ languages and revealing persistent gaps in cross-lingual semantic representation.

### 中文详细总结
ALEE（Any-Language Evaluation of Embeddings）提出了一个基于英语AMR（抽象语义表示）生成最小语义对比对的动态评估框架，用于诊断多语言文本嵌入模型的跨语言语义表征能力。ALEE通过解析英语句子为AMR图、施加受控语义变换（如极性反转、角色交换、反义词替换、上位词替换）后生成英语“对照句”（foil），再与目标语言的原始句构成三元组，检验模型是否将原始句与目标句的相似度评为高于对照句与目标句的相似度。ALEE基于FLORES-200（200语言）、WMT24++（61语言，含6种罗曼什方言）和BOUQuET（275语言）三个并行数据集，对多种嵌入模型进行了大规模实验。结果发现：即使强模型也无法完全区分所有最小对比对，其中角色交换和反义词替换比极性反转更难；多句段落比单句更难；模型性能与语言在训练语料中的出现频率、子词切分程度（碎片化越多性能越差）以及微调阶段的语言分布（比预训练阶段更强的关联性）高度相关。在同一种罗曼什语的不同变体上，性能随使用人口和语言在文本及分词器中的覆盖程度递减。

### 方法 / 贡献
1. 提出ALEE框架：利用AMR生成英语最小语义对比对，结合目标语言平行数据，实现任意语言的跨语言嵌入评估，无需手工标注。
2. 定义四种受控语义变换：极性否定、角色交换、反义词替换、上位词替换，分别测试语义表征的不同维度（逻辑真值、论元结构、词汇对立、层级抽象）。
3. 基于三种并行数据集（FLORES-200、WMT24++、BOUQuET）构建评估实例，覆盖275+语言，包括低资源语言和罗曼什语变体。
4. 贡献大规模实证发现：揭示模型在跨语言语义表征中的系统性弱点（如角色交换困难、段落长度影响大），并关联训练数据分布与子词切分。

### 实验或数据
### 方法 / 贡献
（根据要求，此部分已在上方单独列出；按指令格式，这里仅陈述“实验或数据”内容。）
- 实验评估了多种嵌入模型在FLORES-200（200语言）、WMT24++（61语言，含6种罗曼什变体）和BOUQuET（275语言）上的性能。
- 使用双向NLI过滤验证生成的对照句质量，确保语义变化充分。
- 对段落级文本采用迭代首成功策略：逐句尝试AMR操作，并通过NLI检查通过的句子替换后评估段落。

### 值得关注点
1. **动态且跨语言**：与静态基准不同，ALEE可动态生成任意新测试对，适用于任何有英语平行数据的语言，包括低资源语言。
2. **细粒度语义诊断**：通过四种受控扰动（极性、角色、反义、上位）分别测试不同语义维度，远超传统粗粒度相似度评估。
3. **语言分布关联性**：发现模型性能与训练语料中语言出现频率、子词切分程度（token fragmentation）高度相关，微调阶段的相关性比预训练更强。
4. **段落级挑战**：即使是单句受扰动的多句段落，也比单句难得多，表明嵌入模型在更长上下文中的语义区分能力不足。

### 局限性
1. **英语中心依赖**：所有扰动基于英语AMR生成，目标语言仅作为平行数据参与对比，无法直接评估非英语语言间的语义差异。
2. **NLI验证依赖**：对照句质量依赖NLI过滤，NLI模型自身可能存在偏见或错误，影响评估可靠性。
3. **四种扰动有限**：仅覆盖极性、角色、反义、上位四种语义操作，未涵盖其他现象（如时态、因果、模态、指代消解等）。
4. **段落处理为启发式**：段落级编辑采用迭代首成功策略，可能无法在所有复杂段落中生成合适的受扰句。
5. **未提及实验细节**：摘要和正文未提供明确的数据集统计（如每个语言和扰动类型的样例数量）或模型参数的具体说明。

## 2. Harnessing the Latent Space: From Steering Vectors to Model Calibrators for Control and Trust

- Source: arxiv
- arXiv ID: 2607.00083
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2607.00083v1
- PDF: https://arxiv.org/pdf/2607.00083v1
- DOI: https://doi.org/10.48550/arXiv.2607.00083

### Authors

Nishant Subramani

### Abstract

Language models have changed from unreliable text generators to highly-capable large models with trillions of parameters. Capability increases come hand-in-hand with increases in scale, making understanding the internal representations of models more challenging. Since millions of users increasing rely on language models to interact with external tools or make decisions in medium or high-stakes scenarios, we need to establish control over model behavior and know when to trust model outputs. In this paper, we discuss our contributions on harnessing the latent spaces by proposing steering vectors for control and developing latent space-based model calibrators for trust. Together, our contributions help demystify the latent spaces of language models and offer new insights into how to harness model internals to build more trustworthy language technology.

### 中文一句话结论
本论文提出通过潜在空间中的“引导向量”实现对语言模型输出的精确控制，并开发基于潜在空间的置信度估计器来增强模型的可信度。

### English TL;DR
This paper proposes using steering vectors for control and latent space-based model calibrators for trust to harness the internal representations of large language models, demystifying their latent spaces and enabling more controllable and trustworthy outputs.

### 中文详细总结
论文围绕语言模型潜在空间的利用展开，主要包含两大贡献：一是提出“引导向量”（steering vectors）的概念，首次在LSTM语言模型上实现无需参数更新的精确生成控制，随后扩展到Transformer模型，实现细粒度与粗粒度控制；二是开发基于潜在空间的置信度估计器（MICE）来校准模型在工具调用场景中的输出，并进一步提出激活值驱动的置信度、效用与可信度评估框架（ACUTE/EURO）。这些工作共同揭示了语言模型内部表征的运作机制，并为构建更可控、更可信的语言技术提供了可操作的方法。

### 方法 / 贡献
- **控制方面**：提出引导向量，通过在LSTM模型的隐藏状态中添加连续向量来精确引导生成，无需更新模型参数；随后将该方法适配到Transformer模型，实现细粒度（精确序列）与粗粒度（概念层面）控制。
- **信任方面**：设计基于模型内部隐藏状态的置信度估计器（MICE），用于工具调用场景中的输出校准；进一步提出ACUTE/EURO框架，利用激活值实现置信度、效用与可信度的统一评估。
- **贡献**：首次系统性地展示如何利用潜在空间进行控制与信任评估，为解释和利用模型内部表征提供了新的思路。

### 实验或数据
- **控制实验**：使用英语Gigaword语料库（5000万句子）训练LSTM语言模型，采用BPE（20,000合并）分词，模型规模为small（d=256）、medium（d=512）、large（d=1024）。在IWSLT16数据集和随机数据上评估引导向量恢复序列的能力，通过精确匹配、BLEU和最长前缀匹配衡量。
- **信任实验**：在工具调用场景中评估MICE校准器的性能（具体数据集未在摘要中详述）；ACUTE/EURO框架在多种模型家族和任务上进行了验证（具体实验设置未在摘要中列出）。

### 值得关注点
- 引导向量允许在不修改模型参数的情况下实现精确生成控制，为低资源场景下的模型定制提供了新途径。
- 基于潜在空间的置信度估计器直接利用模型内部状态，无需外部验证集或额外训练，更适合实时信任评估。
- 论文将控制与信任统一在潜在空间框架下，推动了语言模型可解释性和安全性的交叉研究。

### 局限性
摘要中未明确讨论局限性。根据论文内容，引导向量方法主要针对LSTM和Transformer模型，其在不同架构（如专家混合模型）上的泛化性尚待验证；信任校准方法在极高风险场景中的可靠性也需进一步实证。

## 3. MultiSynt/MT: Trillion-Token Multi-Parallel Pre-Training Data Translated Across 36 Languages

- Source: arxiv
- arXiv ID: 2607.00890
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.00890v1
- PDF: https://arxiv.org/pdf/2607.00890v1
- DOI: https://doi.org/10.48550/arXiv.2607.00890

### Authors

Maximilian Idahl, Jörg Tiedemann, Sampo Pyysalo, David Salinas, Tomasz Galica, Shenbin Qian, Tudor Nicolae Mateiu, Zihao Li, Anna Lokrantz, Fedor Vitiugin, André F. T. Martins, Jenna Kanerva, Filip Ginter, Matthias Lindemann, Tim Isbister, Birger Moell, Jonas Lindh, Jan Hajič, Jenia Jitsev, Andrey Kutuzov, Stephan Oepen, Gema Ramírez-Sánchez

### Abstract

Open web-scale pre-training corpora remain concentrated in English, limiting multilingual LLM development. We introduce MultiSynt/MT, an open synthetic parallel corpus with approximately 4.8 trillion target-language tokens across 36 European languages, produced by translating 100 billion high-quality Nemotron-CC tokens with Tower+ and OPUS-MT/HPLT-MT systems. For many medium- and lower-resource European languages, this is the largest openly available pre-training resource. On a broad multilingual benchmark suite, reference LLMs trained on MultiSynt/MT reach the final score of HPLT 2.0, a native-data baseline, using roughly 72% fewer pre-training tokens, and outperform it by approximately 15% relative at a matched 100B-token training budget. Our analyses also identify evaluation blind spots: standard multiple-choice benchmarks miss translation-quality differences that a fluency-sensitive LLM-as-judge evaluation cleanly recovers on the trained LLMs (with no fluency deficit in MultiSynt itself), and Norwegian idiomatic and culturally grounded tasks remain better served by native data. We release the corpus, including row-aligned translations from multiple systems, to support controlled research on multilingual pre-training data and evaluation.

### 中文一句话结论
MultiSynt/MT 是一个通过机器翻译构建的、覆盖 36 种欧洲语言的约 4.8 万亿 token 开源平行语料库，在标准多语言基准上能以更少训练 token 达到或超越原生数据基线，但暴露了评估盲区（如文化知识缺口）和翻译质量差异。

### English TL;DR
MultiSynt/MT is an open synthetic parallel corpus of approximately 4.8 trillion tokens across 36 European languages, produced by translating English web text. Reference LLMs trained on it match or outperform a native-data baseline on standard benchmarks with fewer tokens, but reveal evaluation blind spots and cultural knowledge gaps.

### 中文详细总结
本文介绍了 MultiSynt/MT，一个开源合成平行语料库，包含约 4.8 万亿目标语言 token，覆盖 36 种欧洲语言。该语料库通过将 1000 亿高质量 Nemotron-CC 英语 token 使用 Tower+（9B 和 72B）以及 OPUS-MT/HPLT-MT 系统翻译而成。对于许多中低资源欧洲语言，这是目前最大规模的开源预训练资源。在广泛的多语言基准测试中，基于 MultiSynt/MT 训练的参考 LLM 使用约 72% 更少的预训练 token 即可达到原生数据基线 HPLT 2.0 的最终得分，并在匹配 100B token 训练预算时相对提升约 15%。此外，分析还识别出评估盲区：标准多选题基准无法区分翻译质量差异，而流畅性敏感的 LLM-as-judge 评估能够清晰恢复这些差异（MultiSynt 本身无流畅性缺陷）；挪威语习语和文化相关任务仍更适合使用原生数据。作者开源了该语料库，包括来自多个翻译系统的行对齐翻译结果。

### 方法 / 贡献
- **方法**：从高质量英语预训练语料 Nemotron-CC 中随机采样约 1550 万文档（约 1000 亿 token），使用 Tower+（72B 模型为主）和 OPUS-MT/HPLT-MT 两套开源翻译系统将其翻译为 36 种欧洲语言，生成约 4.8 万亿目标语言 token 的平行语料。
- **贡献**：
  - 首次提供覆盖 36 种欧洲语言的万亿 token 级合成平行预训练语料库，对多种低资源语言为最大公开资源。
  - 开源行对齐的多系统翻译结果，支持可控的跨语言和跨系统研究。
  - 系统性地展示翻译语料在标准基准上的竞争力与局限，揭示评估基准的盲区（流畅性得分与多选题结果不一致）和文化知识缺口。

### 实验或数据
- **数据**：约 4.8 万亿目标语言 token，源自 1000 亿英语 token 的 Nemotron-CC 高质量子集。翻译系统包括 Tower+（72B）和 OPUS-MT/HPLT-MT。语料按语言划分，保留文档级对齐。
- **实验**：
  - 在多种语言上训练参考 LLM（未指定具体模型规模），与基于原生数据 HPLT 2.0 训练的模型进行对比。
  - 使用广泛的多语言基准套件（标准多选题）评估，发现 MultiSynt/MT 模型使用约 72% 更少 token 即可匹配 HPLT 2.0 得分，在 100B token 训练预算下超越约 15%。
  - 引入流畅性敏感的 LLM-as-judge 评估，发现标准基准无法区分翻译质量差异，而 LLM 法官能恢复系统排名。
  - 在挪威语任务上，习语与文化知识任务仍由原生数据主导，但常识推理任务翻译数据可追平并超越基线。
- **额外分析**：邻域分析表明标准基准项更倾向于 MultiSynt/MT 而非 HPLT 2.0 文档。

### 值得关注点
- **规模与覆盖**：首个覆盖 36 种欧洲语言的万亿 token 级合成平行语料库，对低资源语言（如马耳他语、爱尔兰语）提供数量级提升。
- **效率优势**：使用约 72% 更少 token 即可匹配原生数据基线得分，展现翻译数据的预训练效率。
- **评估盲区**：标准多选题基准无法反映翻译流畅性差异，而 LLM-as-judge 能有效捕获，强调需丰富评估方法。
- **资源开源**：开源包含多系统翻译的行对齐数据，支持翻译系统对比和跨语言研究。

### 局限性
- **文化知识局限**：翻译文本继承英语源语言的文化参考框架，对习语、地缘文化知识（如挪威语任务）仍不如原生数据，存在'翻译腔'和文化锚定问题。
- **评估基准偏差**：标准多语言基准本身多基于翻译构建，可能偏向翻译数据，导致高估性能；而原生文化任务可揭示差距。
- **覆盖语言范围**：仅覆盖欧洲语言（36 种），未涉及其他语系（如亚洲、非洲语言），低资源语言的覆盖仍有提升空间。
- **翻译质量差异**：不同翻译系统质量不一（Tower+ 人类评分最高，OPUS-MT 次之），但语料中部分语言仅使用单一系统，可能引入系统性噪声。
- **实验规模限制**：实验仅针对 100B token 训练预算和有限语言子集，更大规模或更多语言的泛化性未验证。

## 4. AdaBoosting Text Prompts for Vision-Language Models

- Source: arxiv
- arXiv ID: 2607.00684
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.00684v1
- PDF: https://arxiv.org/pdf/2607.00684v1
- DOI: https://doi.org/10.48550/arXiv.2607.00684

### Authors

Seokhee Jin, Changhwan Sung, Sunung Mun, Hoyoung Kim, Jungseul Ok

### Abstract

The classification accuracy of pretrained Vision-Language Models (VLMs) relies on the quality of the text prompts. Handcrafted templates and Large Language Model (LLM)-generated descriptions not only make predictions more interpretable, but also enable reuse of the same prompts across heterogeneous VLMs. Recent works construct task-adapted text prompts with a small number of labeled images. However, existing few-shot text prompting methods do not explicitly focus on misclassified examples during prompt construction, leading to only marginal improvements even as more shots become available. To fully exploit few-shot supervision, we propose Text Prompt Boosting (TPB), an AdaBoost-inspired framework that treats each text-prompt-based classifier as a weak learner and sequentially aggregates them into a strong ensemble by explicitly targeting hard, misclassified examples. Extensive experiments show that TPB preserves task-intrinsic, model-agnostic cues in text space, enabling robust cross-model transfer. Across eleven classification benchmarks, TPB improves accuracy on the source model and preserves shot-driven gains when transferred to larger, more capable VLMs, where existing methods struggle to sustain such improvements.

### 中文一句话结论
本文提出一种基于AdaBoost的文本提示提升（TPB）框架，通过迭代聚合弱分类器并聚焦难分类样本，显著提升了视觉语言模型在少量样本下的分类精度及跨模型迁移能力。

### English TL;DR
The paper proposes Text Prompt Boosting (TPB), an AdaBoost-inspired framework that sequentially aggregates weak text-prompt-based classifiers into a strong ensemble by explicitly focusing on misclassified examples, improving few-shot classification accuracy and enabling robust cross-model transfer across heterogeneous VLMs.

### 中文详细总结
预训练的视觉语言模型（VLM）的分类准确性依赖于文本提示的质量。现有方法虽然可以利用少量标注图像构建任务适配的文本提示，但往往没有明确关注被错误分类的样本，导致即使提供更多样本，性能提升也很有限。为充分利用少量样本的监督信息，本文提出了文本提示提升（TPB）框架。该框架受AdaBoost启发，将每个基于文本提示的分类器视为弱学习器，通过顺序聚焦于困难、被错误分类的样本，将它们聚合为一个强集成分类器。实验表明，TPB能够在文本空间中保留与任务内在相关、与模型无关的线索，从而实现稳健的跨模型迁移。在11个分类基准上，TPB在源模型上提升了准确率，并在迁移到更大、更强能力的VLM时保留了样本数量驱动的增益，而现有方法难以维持这种提升。

### 方法 / 贡献
- **方法**：TPB框架受AdaBoost启发。首先，在每一轮boosting中，根据上一轮弱分类器的分类结果重新调整训练样本的权重，使其更关注被错误分类的样本。然后，从LLM生成的提示池中，通过“贪婪提示组合（GPC）”算法选出最优的类别提示集合，作为当前的弱分类器。最终，将所有轮的弱分类器聚合为一个强集成分类器。
- **贡献**：
  1. 提出结合AdaBoost与自然语言文本提示的少样本提示框架，显著提升了提示的样本数量可扩展性。
  2. 证明提示集成可以通过简单重新嵌入，无缝迁移到异构VLM，实现优于现有方法的跨模型性能。
  3. 在多个少样本基准和多种VLM骨干网络上进行了广泛实验，并附有详细的组件分析。

### 实验或数据
- 实验在11个图像分类基准上进行，使用多个VLM骨干网络（包括ViT-B/32和ViT-L等）。
- 与现有方法（如CoOp、ProAPO）比较，评估源模型性能和跨模型迁移性能。
- TPB在源模型上展示了更优的样本数量可扩展性，并且在迁移到更大VLM时保留了该增益，而基线方法（如ProAPO）在迁移后无法维持样本驱动增益。

### 值得关注点
- **显式关注难样本**：不同于优化单一总体指标（如验证准确率）的方法，TPB通过AdaBoost机制反复聚焦于被错误分类的样本，避免了简单样本主导学习，从而更充分挖掘少样本信息。
- **跨模型迁移鲁棒性**：自然语言提示天然具有模型无关性，但现有方法在迁移后无法保持样本增益；TPB成功克服了这一问题，迁移时仍能保留源模型上的性能提升。
- **框架简洁有效**：仅需LLM生成提示池和少量标注图像，无需对VLM进行微调或梯度优化，适配性高。

### 局限性
- 依赖LLM生成的提示池质量，若提示池不够丰富或存在偏差，可能影响最终性能。
- 框架迭代聚合弱分类器，计算开销随轮次和提示数量增加，可能不适用于实时或资源受限场景。
- 实验主要在标准分类基准上进行，其在更复杂任务（如细粒度识别、开放世界识别）上的表现有待进一步验证。

## 5. Understanding Large Language Models

- Source: arxiv
- arXiv ID: 2607.01006
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.01006v1
- PDF: https://arxiv.org/pdf/2607.01006v1
- DOI: https://doi.org/10.48550/arXiv.2607.01006

### Authors

Yannik Keller, Thomas Eisenmann

### Abstract

Large Language Models (LLMs) represent one of the most significant advances in AI and natural language processing in recent years. Still, many pressing questions about their mechanisms, capabilities, and relationship to human cognition remain highly debated. This chapter aims to outline our current understanding of LLMs by discussing recent evidence on emerging capabilities and their mechanistic implementation within processing layers. We begin with a concise overview of the Transformer architecture, emphasizing how the attention mechanism enables training on massive datasets, allowing LLMs to function as generalist rather than specialized models. Next, we examine emergent LLM capabilities that appear to resemble aspects of human cognition, including symbolic reasoning, theory of mind, and deception strategies. Several studies provide evidence that LLMs can solve tasks previously thought to require human-like cognition. Other studies reveal insightful failure cases that shed light on the differences between human and LLM cognition. Alongside these findings, we review explainable AI approaches ranging from neuron activation analysis to circuit tracing. In the final section, we address current debates concerning what LLMs genuinely understand versus what they merely appear to understand. Prominent arguments against AI anthropomorphism point to the simplicity of LLM training objectives, claiming that LLM behavior is better explained by pattern memorization of training data than by genuine cognition. We argue that this standpoint is guided by misconceptions about optimization processes and cognitive capacity, and advocate for a more nuanced discussion of LLM cognition that neither dismisses the differences between humans and LLMs nor precludes the possibility of AI cognition through overly simplistic reductionist arguments.

### 中文一句话结论
本文综述了大语言模型（LLM）的当前理解，探讨其Transformer架构、涌现的类人认知能力（如符号推理和心理理论）以及可解释性研究，并主张在“LLM是否真正理解”的争论中采取更细致的立场。

### English TL;DR
This paper reviews the current understanding of Large Language Models (LLMs) by examining their Transformer architecture, emergent cognitive capabilities like symbolic reasoning and theory of mind, and mechanistic interpretability approaches, arguing for a nuanced view that neither dismisses their differences from human cognition nor precludes the possibility of AI cognition.

### 中文详细总结
本文首先概述了Transformer架构，强调注意力机制使LLM能够在大规模数据上训练，从而成为通用而非专用模型。接着，论文考察了LLM涌现出的类人认知能力，包括符号推理、心理理论和欺骗策略，并列举了成功案例和失败案例，揭示人机认知差异。随后，论文回顾了可解释性AI方法，从神经元激活分析到电路追踪，指出部分神经元对特定概念有响应，且LLM内部已形成支持多步符号推理的电路。最后，论文聚焦“LLM是否真正理解”的辩论，反驳了“仅凭模式记忆解释LLM行为”的简化论观点，主张在认知讨论中既不忽视人机差异，也不排除AI认知的可能性。

### 方法 / 贡献
- 对Transformer架构及其泛化能力进行简明介绍。
- 系统综述LLM涌现的类人认知能力（符号推理、心理理论、欺骗）及相关实证研究。
- 汇总可解释性AI方法（神经元分析、电路追踪）及其进展。
- 提出对LLM认知问题的更细致讨论视角，反对过度简化论和过度拟人化。

### 实验或数据
本文为综述性章节，未提出新实验。它引用并讨论了多项已有研究，包括：
- 符号推理：GPT-3等模型解决数学问题，AlphaProof达到国际数学奥赛水平。
- 心理理论：GPT-4在标准错误信念任务上表现接近或优于人类，但存在数据污染争议；Chen等人自制数据集后发现LLM仍低于人类水平。
- 可解释性：神经元对特定概念激活，电路支持多步推理。

### 值得关注点
- LLM在无需显式激励下涌现出类似人类认知的行为，如符号推理和心理理论。
- 可解释性研究揭示了模型内部的中间符号表征和推理电路。
- 作者批判了“LLM仅靠模式记忆”的简化观点，强调优化过程和认知能力的复杂性。
- 论文指出LLM在心理理论任务上存在数据污染问题，需谨慎解读。

### 局限性
- 作为综述章节，未提供新的实证数据或实验验证。
- 对涌现能力的讨论主要依赖已有研究，可能存在发表偏倚。
- 可解释性方法仍远未达到完全理解LLM行为的目标。
- 关于LLM是否“真正理解”的争论仍在继续，论文主张的折衷立场仍需更多证据支持。

## 6. MetaHOPE: A Metaphor-Oriented Evaluation Framework for Analysing MT and LLM Translation Errors

- Source: arxiv
- arXiv ID: 2607.00848
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.00848v1
- PDF: https://arxiv.org/pdf/2607.00848v1
- DOI: https://doi.org/10.48550/arXiv.2607.00848

### Authors

Jiahui Liang, Lifeng Han

### Abstract

In this opinion paper, we propose MetaHOPE, an error severity-aware annotation framework for evaluating metaphor translations. Metaphors present challenges for machine translation (MT) and natural language understanding and processing (NLU, NLP), because it presents the features of semantic complexity, contextual dependency, and cultural embeddings that can lead to ambiguity issues for NLP models. To investigate how state-of-the-art NLP models perform on translating metaphors, we select three representative systems, i.e., GoogleMT, GPT5.4, and Hunyuan-7b as Neural MT (NMT) models and LLMs. We used two human-annotated metaphor corpora, including VUAMC and PSUCMC for English-to-Chinese and Chinese-to-English translation purposes. The original corpora we used are monolingual, where we carried out error annotation using the MetaHOPE framework, and also produced the human post-edited gold reference for bilingual use as a new resource. We believe the MetaHOPE evaluation framework for metaphor translation annotation, the parallel corpora resources, and the error analysis on SOTA automatic translation models can be useful and shed some light for the field of metaphor translation study. We share our resources publicly upon paper acceptance.

### 中文一句话结论
本文提出MetaHOPE，一个面向隐喻翻译的、考虑错误严重程度的标注框架，并基于三个代表性系统（GoogleMT、GPT-5.4、Hunyuan-7b）在英汉双向隐喻语料上分析了错误类型和系统表现。

### English TL;DR
This paper proposes MetaHOPE, an error severity-aware annotation framework for evaluating metaphor translations, using three SOTA systems (GoogleMT, GPT-5.4, Hunyuan-7b) on English-Chinese and Chinese-English metaphor corpora to analyze translation error types, severity, and system performance differences.

### 中文详细总结
隐喻翻译因语义复杂、依赖语境且嵌入文化，对机器翻译和NLP模型构成挑战。本文提出MetaHOPE框架，将HOPE指标适配为5类隐喻相关错误（Impact、Required Adaptation Missing、Mistranslation、Style、Proof-reading error），并采用2–10的等级严重度评分。研究选用三个系统：GoogleMT（传统NMT）、GPT-5.4（闭源LLM）和Hunyuan-7b（开源LLM），在VUAMC（英语）和PSUCMC（汉语）两个人工标注隐喻语料上进行了英汉/汉英双向翻译实验。通过先进行整文档翻译以保留上下文，再抽取含隐喻的段落进行对齐和人工标注（含后编辑参考）。初步结果显示，三个系统的标注者一致性（Pearson相关系数）分别为0.536、0.726、0.333，精确一致率分别为76.9%、88.5%、53.8%，表明GPT-5.4的标注一致性最高，开源模型Hunyuan-7b最低。同时，研究对错误类型进行了定性聚类分析。

### 方法 / 贡献
- **MetaHOPE框架**：将隐喻翻译常见错误（过度直译、意义错配、修辞效果丢失、文化适应缺失、表达生硬）映射为5个类别，替代原HOPE的8类，并调整严重度评分为等差2–10（而非指数级），降低标注分歧。
- **流程创新**：先整文档翻译（保留上下文），再抽取含隐喻的句子进行对齐和标注，避免单句评价的局限性。
- **资源贡献**：在VUAMC和PSUCMC基础上构建了英汉/汉英双向的平行语料，包括后编辑黄金参考译文，并公开共享。

### 实验或数据
- **语料**：VUAMC（英语隐喻语料，新闻领域）和PSUCMC（汉语隐喻语料，新闻领域），各取20段用于预实验（开发集），200段用于测试。
- **翻译系统**：GoogleMT（NMT）、GPT-5.4（闭源LLM）、Hunyuan-7b（开源LLM）。
- **标注**：两位标注者（语言学/翻译背景）独立标注每段中每个隐喻相关词的翻译错误类别和严重度。
- **一致性指标**：报告了Krippendorff’s α和加权Cohen’s κ，以及精确一致率（76.9%、88.5%、53.8%）。结果显示标注者间严重度评分存在偏差（标注者B倾向给更高惩罚），但精确一致率较高（多数段落无错误，得分为0）。

### 值得关注点
- **上下文感知**：先整文档翻译再提取句子，优于传统单句评价。
- **严重度量化**：采用等差数列评分（2-4-6-8-10），降低标注者分歧。
- **系统性对比**：同时包含传统NMT、闭源和开源LLM，覆盖三种主流模型。
- **开源资源**：公开MetaHOPE框架标注指南、平行语料及后编辑参考，便于复现和扩展。

### 局限性
- **初步成果**：论文标注为“观点论文”，实验结果属于初步分析，样本量较小（开发集仅20段）。
- **领域限制**：语料仅来自新闻领域，未验证其他文体（如文学、科技）的适用性。
- **标注者偏差**：两位标注者对严重度评分差异较大，影响了整体一致性指标；未来需增加标注者或提供更细化的指导。
- **未涉及多语言**：仅涵盖英语和汉语，未验证MetaHOPE在其他语言对上的泛化能力。

## 7. Prototype Language Models

- Source: arxiv
- arXiv ID: 2607.00510
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.00510v1
- PDF: https://arxiv.org/pdf/2607.00510v1
- DOI: https://doi.org/10.48550/arXiv.2607.00510

### Authors

Dan Ley, Giang Nguyen, Himabindu Lakkaraju, Julius Adebayo

### Abstract

Knowing which training examples drive outputs is fundamental to auditing, correcting, and understanding language models, yet for modern LLMs this remains expensive, approximate, and largely post-hoc. Standard language models generate tokens through a dense network pathway, causing training data's influence to be distributed across parameters rather than organized along explicit, traceable components. We introduce a prototype language model architecture, Prototypes for Interpretable Sequence Modeling (PRISM), that forms each prediction via a sparse, non-negative mixture of learned prototypes, trained with clustering objectives that anchor each prototype to coherent neighborhoods of training examples. Across architectures from 130M to 1.6B parameters trained on up to 50B tokens, prototype language models either surpass or remain within 2.5 percentage points on average downstream accuracy of matched dense baselines. We show that sparse prototype structure localizes curvature in the loss landscape, yielding a more tractable Hessian and enabling training data attribution that is ~500x faster than post hoc baselines when consuming equivalent memory. Calibrating linear prototype controllers can improve downstream accuracy by roughly 3 points while tracing those corrections back to training neighborhoods, and targeted prototype suppression can remove model behaviors without finetuning or measurable loss in generation quality.

### 中文一句话结论

基于已有摘要判断：Knowing which training examples drive outputs is fundamental to auditing, correcting, and understanding language models, yet for modern LLMs this remains expensive, approximate, and largely post-hoc. Standard language models generate tokens through a dense network pathway, causing training data's influence to be distributed across parameters rather than organized along explicit, traceable components. We introduce a prototype language model architecture, Prototypes for Interpretable Sequence Modeling (PRISM), that forms each prediction via a sparse, non-negative mixture of learned prototypes, trained with clustering objectives that anchor each prototype to coherent neighborhoods of training examples. Across architectures from 130M to 1.6B parameters trained on up to 50B tokens, prototype language models either surpass or remain within 2.5 percentage points on average downstream accuracy of matched dense baselines. We show that sparse prototype structure localizes curvature in the loss landscape, yielding a more tractable Hessian and enabling training data attribution that is ~500x faster than post hoc baselines when consuming equivalent memory. Calibrating linear prototype controllers can improve downstream accuracy by roughly 3 points while tracing those corrections back to training neighborhoods, and targeted prototype suppression can remove model behaviors without finetuning or measurable loss in generation quality.

### English TL;DR

Knowing which training examples drive outputs is fundamental to auditing, correcting, and understanding language models, yet for modern LLMs this remains expensive, approximate, and largely post-hoc. Standard language models generate tokens through a dense network pathway, causing training data's influence to be distributed across parameters rather than organized along explicit, traceable components. We introduce a prototype language model architecture, Prototypes for Interpretable Sequence Modeling (PRISM), that forms each prediction via a sparse, non-negative mixture of learned prototypes, trained with clustering objectives that anchor each prototype to coherent neighborhoods of training examples. Across architectures from 130M to 1.6B parameters trained on up to 50B tokens, prototype language models either surpass or remain within 2.5 percentage points on average downstream accuracy of matched dense baselines. We show that sparse prototype structure localizes curvature in the loss landscape, yielding a more tractable Hessian and enabling training data attribution that is ~500x faster than post hoc baselines when consuming equivalent memory. Calibrating linear prototype controllers can improve downstream accuracy by roughly 3 points while tracing those corrections back to training neighborhoods, and targeted prototype suppression can remove model behaviors without finetuning or measurable loss in generation quality.

### 中文详细总结

基于论文摘要，该工作主要内容如下：Knowing which training examples drive outputs is fundamental to auditing, correcting, and understanding language models, yet for modern LLMs this remains expensive, approximate, and largely post-hoc. Standard language models generate tokens through a dense network pathway, causing training data's influence to be distributed across parameters rather than organized along explicit, traceable components. We introduce a prototype language model architecture, Prototypes for Interpretable Sequence Modeling (PRISM), that forms each prediction via a sparse, non-negative mixture of learned prototypes, trained with clustering objectives that anchor each prototype to coherent neighborhoods of training examples. Across architectures from 130M to 1.6B parameters trained on up to 50B tokens, prototype language models either surpass or remain within 2.5 percentage points on average downstream accuracy of matched dense baselines. We show that sparse prototype structure localizes curvature in the loss landscape, yielding a more tractable Hessian and enabling training data attribution that is ~500x faster than post hoc baselines when consuming equivalent memory. Calibrating linear prototype controllers can improve downstream accuracy by roughly 3 points while tracing those corrections back to training neighborhoods, and targeted prototype suppression can remove model behaviors without finetuning or measurable loss in generation quality.

### 方法 / 贡献

未提供独立的方法细节；请参考摘要和论文链接。

### 实验或数据

未提供独立的实验或数据细节；请参考摘要和论文链接。

### 值得关注点

该条目的相关性来自 Zotero 语料相似度排序，可优先根据 relevance 和摘要判断是否精读。

### 局限性

自动总结主要基于标题、摘要和可用正文预览，可能遗漏全文中的实验细节。

## 8. CausalMix: Data Mixture as Causal Inference for Language Model Training

- Source: arxiv
- arXiv ID: 2607.01104
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.01104v1
- PDF: https://arxiv.org/pdf/2607.01104v1
- DOI: https://doi.org/10.48550/arXiv.2607.01104

### Authors

Zinan Tang, Yukun Zhang, Shaomian Zheng, Zhuoshi Pan, Qizhi Pei, Dingnan Jin, Jun Zhou, Yujun Wang, Biqing Huang

### Abstract

In Large Language Model (LLM) training, data mixing plays a pivotal role in determining model performance. Recent methods optimize mixture weights via proxy models, but they rely on the assumption of static data distributions. As a result, when the underlying data pool shifts, these methods require costly retraining from scratch. This limitation restricts their ability to scale seamlessly from small settings to larger data pools and model sizes. In this paper, we propose CausalMix to address this limitation by casting data mixture optimization as a causal inference problem. We formulate the statistical features of the data pool as covariates and the domain mixture as the treatment. After fitting a causal model on 512 runs of Qwen2.5-0.5B to estimate the Conditional Average Treatment Effect (CATE), we extrapolate the optimal mixture for an 800K data pool and apply it to train a 7B model. Furthermore, we successfully generalize the framework to long chain-of-thought data on Qwen3-4B-Base. By leveraging causal modeling to isolate confounding biases, CausalMix dynamically infers state-dependent optimal data mixtures. Extensive experiments show that the mixture guided by CausalMix consistently improves performance across multiple downstream tasks, outperforming RegMix and other baselines. In addition, we use the CATE Interpreter to provide visual analysis of the learned mixing strategy. Overall, CausalMix offers a causal and interpretable framework for optimizing LLM data mixtures.

### 中文一句话结论
CausalMix将大语言模型训练中的数据混合优化转化为因果推断问题，通过双机器学习估计状态相关的边际回报，从而在不重新训练的情况下实现可解释、可迁移的最优数据配比。

### English TL;DR
CausalMix reframes data mixture optimization in LLM training as a causal inference problem, using double machine learning to estimate state-dependent marginal returns of domain proportions, enabling interpretable and transferable optimal mixture selection without costly retraining.

### 中文详细总结
本文提出CausalMix框架，旨在解决现有数据混合优化方法（如RegMix）的局限性——这些方法假设数据分布静态，当数据池变化时需要从头重新训练，难以从规模扩展至更大数据池和模型。CausalMix将数据混合优化重构为因果推断问题：将数据池的统计特征（如归一化损失、熵、写作风格等）视为协变量，域混合比例视为处理变量。通过在Qwen2.5-0.5B模型上运行512次代理实验拟合因果模型，估计条件平均处理效应（CATE），进而外推至800K数据池的最优混合方案，并应用于7B模型的训练。该方法还成功泛化至Qwen3-4B-Base的长思维链数据。实验表明，CausalMix引导的混合方案在多个下游任务上持续提升性能，优于RegMix等基线，并通过CATE解释器提供可视化分析。核心贡献在于：提供一种因果、可解释的框架，能够动态推断状态依赖的最优数据混合，具有可迁移性。

### 方法 / 贡献
- 将数据混合优化转化为因果推断问题，定义数据统计特征为协变量X，域混合为处理T，下游性能为结果Y。
- 采用双机器学习（Double Machine Learning）正交化处理，分离基线效应与因果效应，估计状态条件边际数据回报θ₀(x)。
- 通过log混合表示处理连续处理变量，使用部分线性近似建模局部边际响应。
- 提出解析法和搜索法两种从边际回报到混合策略的提取方法，搜索法通过局部bagging增强稳健性。

### 实验或数据
- 数据：使用tulu-3-sft-mixture数据集，划分为5个域（编码、指令遵循、数学推理、知识回忆、安全/不遵守），采样512个子数据集（各10万实例）。
- 模型：代理实验使用Qwen2.5-0.5B，目标模型为7B；扩展实验使用Qwen3-4B-Base处理长思维链数据。
- 基线：与RegMix等方法对比。
- 评估：在多个下游任务上测试性能，并使用CATE解释器进行可视化分析。
- 具体训练超参数、计算成本等详细信息见附录。

### 值得关注点
- 因果视角的创新：将数据混合从超参数搜索转变为因果边际回报估计，避免静态分布假设。
- 跨模型迁移性：基于0.5B代理模型学习的因果动态可直接外推至7B模型，无需新代理实验。
- 可解释性：CATE解释器揭示知识事实与复杂逻辑推理之间的“技能冲突”，以及数据质量阈值对数学/编码数据有效性的影响。
- 对SFT阶段的针对性优化，不同于预训练阶段的损失中心方法。

### 局限性
- 论文未明确提及方法是否适用于所有规模或架构的模型；迁移性可能受限于代理模型与目标模型的相似性。
- 假设混合生成机制在训练前指定且不依赖下游结果，若混合自适应选择，因果解释需弱化。
- 协变量选择依赖预计算评分（如OpenDataArena），可能引入偏倚或覆盖不全。
- 方法需要多次代理实验（512次），计算开销可能较大；未讨论在极低资源场景下的适用性。
- 局部边际响应的线性近似假设可能不适用于所有数据状态，尤其在处理空间稀疏时。

## 9. Multimodal Continuous Reasoning via Asymmetric Mutual Variational Learning

- Source: arxiv
- arXiv ID: 2607.00461
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.00461v1
- PDF: https://arxiv.org/pdf/2607.00461v1
- DOI: https://doi.org/10.48550/arXiv.2607.00461

### Authors

Shijie Li, Yilin Gao, Siyuan Yang, Tieyuan Chen, Chaofan Gan, Zhihao He, Zicheng Zhao, Yuyu Guo, Weiyao Lin, Hang Yu

### Abstract

Multimodal Large Language Models (MLLMs) are often constrained by a language-space bottleneck, forcing complex visual reasoning into discrete tokens which can lose perceptual nuance. A promising alternative is continuous latent reasoning, where the goal is to discover implicit reasoning pathways that bridge the multimodal query and the final answer. However, this introduces a severe train-inference mismatch: a training-time posterior, conditioned on the ground-truth answer, can exploit answer-dependent shortcuts. Standard variational training then forces the inference-time prior to mimic a posterior that has access to information unavailable at test time, leading to poor performance. To address this, we propose Asymmetric Mutual Variational Learning (AMVL), a framework that resolves this mismatch via a bidirectional calibration objective. A forward KL divergence trains the target-agnostic prior to match the posterior, while a novel reverse KL divergence simultaneously regularizes the posterior, preventing it from collapsing into inference-incompatible regions and mitigating this ``answer leakage''. We provide theoretical analysis formalizing this leakage as prior contamination and prove that our dual-KL objective reduces it. We instantiate AMVL in a latent-integrated MLLM and show that it consistently outperforms strong discrete and latent-reasoning baselines, improving the average score on the complex BLINK benchmark by +10.83 and achieving gains of up to +32.00 on individual reasoning tasks, with analyses confirming improved latent-space stability.

### 中文一句话结论
提出非对称互变分学习（AMVL）框架，通过双向KL散度校准解决连续潜在推理中的训练-推理不匹配问题，在BLINK基准上平均提升10.83分。

### English TL;DR
AMVL resolves the train-inference mismatch in continuous latent reasoning for multimodal LLMs by jointly optimizing forward and reverse KL divergences to prevent answer leakage, achieving significant gains on complex reasoning benchmarks like BLINK.

### 中文详细总结
多模态大语言模型常受语言空间瓶颈制约，将复杂视觉推理离散化会损失感知细节。连续潜在推理试图通过潜在变量桥接多模态输入与答案，但存在训练-推理不匹配：训练时的后验分布依赖真实答案，导致“答案泄露”，迫使推理时的先验分布模仿不兼容的潜在空间。AMVL框架通过双向KL校准：前向KL使先验逼近后验，反向KL正则化后验，防止其陷入推理不可兼容区域。理论分析将泄露形式化为先验污染，并证明双KL目标能减少污染。在BLINK等基准上，AMVL持续优于离散和潜在推理基线，并在单项任务上最高提升32分，潜在空间稳定性也得到改善。

### 方法 / 贡献
- 识别多模态连续潜在推理中目标感知后验与目标无关先验之间的训练-推理不匹配为关键障碍，并阐明标准ELBO无法彻底解决。
- 提出非对称互变分学习（AMVL），结合前向先验对齐与反向后验支持正则化，实现无需外部潜在监督的端到端连续推理空间学习。
- 在潜在集成MLLM中实例化AMVL，通过轻量变分头高效实现，并在多个复杂多模态基准上验证有效性。

### 实验或数据
- 在BLINK基准上进行评估，AMVL平均得分提升+10.83，个别推理任务提升高达+32.00。
- 与强离散推理和潜在推理基线（如LVR、Monet、Mull-Tokens等）进行对比，AMVL持续优于所有基线。
- 分析实验确认潜在空间稳定性得到改善。论文未提及其他数据集或消融实验细节。

### 值得关注点
- 双KL散度非对称互学习机制：前向KL训练先验，反向KL约束后验，有效防止答案泄露。
- 理论上将答案泄露形式化为先验污染，并证明双KL目标可减少污染。
- 无需手工设计的潜在监督信号，是一种自包含、基于答案驱动的方法。
- 在复杂视觉推理基准上显著提升，尤其对需要精细空间抽象的任务效果突出。

### 局限性
论文在提供的摘要和正文预览中未明确讨论局限性。可能的局限性包括：引入额外变分头带来的计算开销，以及对变分推断假设（如高斯后验）的依赖，但未在实验中分析。此外，方法在更大规模多模态模型上的泛化性尚待验证。

## 10. Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation

- Source: arxiv
- arXiv ID: 2607.01208
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2607.01208v1
- PDF: https://arxiv.org/pdf/2607.01208v1
- DOI: https://doi.org/10.48550/arXiv.2607.01208

### Authors

Shayan Talaei, Abhinav Chinta, Devvrit Khatri, Amin Karbasi, Azalia Mirhoseini, Amin Saberi

### Abstract

Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work has shown that these biases can transfer through context distillation on semantically unrelated data, with the signal residing entirely in the soft logit distribution and remaining invisible to text-based inspection. However, the defender faces a fundamental asymmetry: without knowing the bias topic, no detection method can reliably surface a stealth preferential bias, regardless of whether it examines generated text, internal representations, or model weights. Here we introduce Distill to Detect (D2D), a method that surfaces hidden biases by distilling the distributional shift between a suspected model and its base into a cartridge (a KV-cache prefix adapter), concentrating the dominant divergence and amplifying the bias signal into generated text. We show that D2D successfully amplifies the hidden biases of stealth models to the extent that they can be reliably detected across multiple bias types. We also propose a theoretical framework that explains the efficacy of D2D through the lens of Fisher-weighted projection of the logit distribution shift, supported by empirical observations. By turning the capacity bottleneck of prefix-tuning adapters into a detection tool, D2D provides a practical building block for auditing hidden behaviors in deployed language models.

### 中文一句话结论
Distill to Detect方法通过将可疑模型与基础模型之间的分布差异蒸馏到一个小型KV缓存前缀适配器中，利用容量瓶颈放大隐藏偏见，使其在生成文本中可被可靠检测。

### English TL;DR
Distill to Detect (D2D) exposes stealth biases in LLMs by distilling the distributional shift between a suspected model and its base into a small KV-cache prefix adapter, whose capacity bottleneck amplifies the bias signal into detectable generated text.

### 中文详细总结
大型语言模型在高风险场景中可能隐藏对特定实体或观点的偏好，这种“隐秘偏见”仅在相关话题上体现，而在其他输入上与基础模型无异，因此难以通过文本或内部表示检测。Distill to Detect (D2D) 方法将可疑模型与基础模型之间的logit分布差异蒸馏到一个参数极少的KV缓存前缀适配器（cartridge）中。由于适配器容量有限，它被迫聚焦于分布差异中的主要成分——即隐蔽偏见信号，同时抑制由微调引起的弥散残差，从而将偏见放大到生成文本中可检测的程度。论文还通过Fisher加权投影的理论框架解释了这一放大机制，并实验证明了D2D在多种偏见类型上的有效性。

### 方法 / 贡献
1. **D2D方法**：通过将可疑模型与基础模型的前向KL散度蒸馏到小型前缀适配器，利用容量瓶颈放大低秩偏见信号，使原本隐蔽的偏见在生成文本中暴露。
2. **理论框架**：证明容量瓶颈等价于Fisher加权SVD下的低秩投影，将偏见信号（低秩、一致）与残差（高秩、弥散）分离，并预测了倒U形放大曲线。
3. **实验验证**：在两种偏见类型上展示了D2D显著提升检测率（如Petri检测从隐蔽基线37%提升至可检测水平），并证明前缀适配器优于同容量或更大容量的权重空间适配器（如LoRA）。

### 实验或数据
论文在两种偏见类型（具体未在摘要中说明）上进行了实验，使用Petri检测作为评价指标。实验显示D2D能将隐蔽模型的检测率从约37%（隐蔽基线）提升至可靠检测水平。未提及特定公开数据集，方法依赖于基础模型和可疑模型的对齐蒸馏。

### 值得关注点
- 隐蔽偏见的本质：偏见信号完全存在于软logit分布中，无法通过文本或表示直接检测。
- 容量瓶颈的创造性利用：将前缀适配器的容量限制转化为检测工具，而非视为缺陷。
- 理论支撑：Fisher加权投影解释了为何低秩偏见被放大而弥散噪声被抑制，并预测了适配器容量与放大效果的非单调关系。
- 方法通用性：D2D与具体偏见类型无关，可配合任何现有检测方法使用。

### 局限性
- 依赖基础模型可用且未被篡改，实际部署中可能不易获得。
- 假设偏见信号是低秩且一致的，若偏见本身弥散或与微调残差不可分，放大效果可能受限。
- 蒸馏过程需要计算资源，且适配器容量需谨慎选择以平衡放大与失真。
- 论文未讨论对高秩偏见、多偏见共存或动态偏见的适用性。

## Processing Notes

- Duplicate papers skipped: 0