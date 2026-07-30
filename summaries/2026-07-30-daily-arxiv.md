# Daily arXiv - 2026-07-30

- Source: GitHub Actions generated paper list
- Generated at: 2026-07-30T23:34:06
- Paper count: 10

## 1. DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search

- Source: arxiv
- arXiv ID: 2607.27178
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2607.27178v1
- PDF: https://arxiv.org/pdf/2607.27178v1
- DOI: https://doi.org/10.48550/arXiv.2607.27178

### Authors

Raphaël Sourty, Antoine Chaffin, Paulo Roberto Moura Junior, Amélie Chatelain

### Abstract

State-of-the-art retrieval models increasingly rely on closed training data, creating a reproducibility gap. We present an open end-to-end recipe for training retrieval models and study how English supervision transfers to multilingual retrieval through translate-train. We first reconstruct and curate 665M English contrastive pre-training pairs from 1.4B pairs across 34 public sources and build 1.88M supervised fine-tuning pairs with mined hard negatives. Training yields two 149M-parameter models: DenseOn, a single-vector dense model, and LateOn, a ColBERT-style late-interaction model. They achieve 56.20 and 57.22 average nDCG@10 on BEIR, respectively, setting new state-of-the-art results for this size class. We then translate the validated English data into eight languages, yielding 2.8B pairs with cross-lingual samples, and train mDenseOn and mLateOn, two 307M-parameter models built on mmBERT-base. Despite sharing their backbone, data, and objectives, their representations behave differently: the dense model is strong on English and translated languages but degrades outside translate-train support, whereas the late-interaction model generalizes better to unseen languages and scripts. This suggests that token-level matching turns translate-train from a target-language expansion strategy into a multilingual generalization recipe. We publicly release the models, datasets, and training code.

### 中文一句话结论
本文通过完全开源的密集检索和延迟交互模型，证明了在跨语言检索中，基于token匹配的延迟交互模型比密集模型能更好地泛化到未见语言，将翻译-训练从目标语言扩展策略转变为多语言泛化方法。

### English TL;DR
This paper presents fully open DenseOn and LateOn retrieval models (149M parameters) trained on curated English data, achieving SOTA on BEIR. By extending to multilingual via translate-train (8 languages, 2.8B pairs), they train mDenseOn and mLateOn (307M parameters). Findings show that late-interaction models generalize better to unseen languages and scripts compared to dense models, suggesting token-level matching enables multilingual generalization. All models, data, and code are publicly released.

### 中文详细总结
- 针对当前检索模型依赖封闭训练数据、可复现性差的问题，本文提供了一个完全开源的端到端训练方案。
- 首先从34个公开来源的14亿对数据中重建并筛选出6.65亿英文对比预训练对，并构建188万对带困难负例的监督微调数据。
- 基于ModernBERT-base（149M参数）训练两种模型：DenseOn（单向量密集模型）和LateOn（ColBERT风格延迟交互模型），在BEIR上分别达到56.20和57.22的平均nDCG@10，创下该尺寸模型的SOTA。
- 将验证过的英文数据通过机器翻译扩展到8种语言，得到约28亿对多语言预训练数据（含25%跨语言对），并基于mmBERT-base（307M参数）训练mDenseOn和mLateOn。
- 实验发现：密集模型在英语和翻译语言上表现强，但在翻译支撑语言之外性能下降；而延迟交互模型能更好地泛化到未见过的语言和文字系统，表明token级匹配将翻译-训练从目标语言扩展策略转变为多语言泛化配方。
- 公开释放所有模型、数据集和训练代码。

### 方法 / 贡献
- **开放英文检索配方**：从34个公开来源重建并筛选大规模英文训练混合数据，保留所有过滤元数据（非破坏性过滤），支持用户自定义阈值。
- **SOTA开源英文检索器（149M参数）**：训练DenseOn和LateOn，在BEIR上达到该尺寸模型最优。
- **大规模开源翻译-训练多语言管道**：将英文配方翻译至8种语言，生成约28亿对多语言预训练数据，并构建含跨语言对、长上下文和代码数据的多语言微调数据集（1630万对比样本，覆盖9种自然语言及代码）。
- **对比分析密集与延迟交互模型**：在相同骨干、数据和目标条件下，发现延迟交互模型在跨语言泛化上显著优于密集模型，提出token级匹配是泛化关键。

### 实验或数据
- **英文预训练数据**：1.4B原始对，经非破坏性过滤后得到665M对，来源包括FineWeb-Edu等34个公开源。
- **英文微调数据**：1.88M对，从7个数据集（FiQA、NQ、HotpotQA、MS MARCO、FEVER、SQuADv2、TriviaQA）挖掘困难负例，并含交叉编码器评分。
- **多语言数据**：通过Mistral-Small-3.1-24B将英文数据翻译至8种语言，得到2.8B对（含25%跨语言对）；微调数据额外加入MIRACL、MLDR（长上下文）和LateOn-Code（代码）数据，共16.3M对比样本。
- **评估基准**：BEIR（英文）、MIRACL（18种语言，13种未见语言）、MLDR、MTEB Code。
- **结果**：DenseOn/LateOn在BEIR达到56.20/57.22 nDCG@10；多语言模型在翻译语言上表现强，但延迟交互模型在未见语言上显著优于密集模型。

### 值得关注点
- 完全开源：模型、数据集、训练代码全部公开，可复现性高。
- 非破坏性过滤：保留所有过滤元数据，允许社区调整或替换过滤策略，无需重新收集数据。
- 延迟交互模型的跨语言泛化能力：即使训练数据只包含翻译语言，LateOn仍能有效泛化到未见语言和文字，这对低资源语言检索具有重要价值。
- 翻译-训练策略的重新理解：从“目标语言扩展”转变为“多语言泛化”，依赖token级匹配而非语言特定信号。
- 包含长上下文和代码检索，覆盖更全面的应用场景。

### 局限性
- 密集模型在翻译支撑语言外性能下降明显，限制了其跨语言泛化能力。
- 翻译数据可能存在人工翻译偏差，原文未评估对翻译质量或语言保真度的影响。
- 代码检索仅使用微调数据，未在预训练阶段加入代码数据，可能限制了代码检索性能的上限（作者提及未来工作）。
- 多语言评估仅覆盖18种MIRACL语言，更多低资源语言或非拉丁文字系统未测试。

## 2. Enhancing Generative Information Extraction with Two-step Validation: A Product Attribute Use Case

- Source: arxiv
- arXiv ID: 2607.26780
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2607.26780v1
- PDF: https://arxiv.org/pdf/2607.26780v1
- DOI: https://doi.org/10.48550/arXiv.2607.26780

### Authors

Yi-Sheng Hsu, Nermeen Abou Baker, Uwe Handmann

### Abstract

The ability of large language models (LLMs) to process and generate text has introduced potential for applications in information extraction (IE). While it's debated whether LLMs outperform smaller fine-tuned models for classification tasks, their strong generalization capability makes them promising for domains with limited labeled data available for fine-tuning. This advantage is particularly relevant for the emerging application of the digital product passport (DPP), where the problem space is broad but domain-specific data remains scarce. Motivated by this use case, we apply generative IE to the product domain, explicitly addressing efficiency, generalizability, and data privacy constraints. We propose a two-step validation method that integrates a PLM block into the generative IE pipeline and thereby leverages LLMs' correction capability. We discover that such a validation task enhances LLM performance, particularly on the extraction of weakly expressed, low-salience entities that appear sparsely throughout the text. For certain entities, the performance of mid-size models can even reach levels comparable to larger models, and the improvement of first-step PLM predictions also enhance the final LLM output. Nevertheless, the effects on the smallest open-source LLMs (e.g., Llama-3.2 3B) is limited. Based on the findings, we develop a demo application for product information extraction that utilizes locally deployed LLMs, targeting further adaptations to real-world DPP use cases.

### 中文一句话结论
本文提出了一种结合预训练语言模型（PLM）与大型语言模型（LLM）的两步验证方法，显著提升了生成式信息抽取中低显著性实体的提取性能，并使中等规模模型达到与更大模型相当的水平。

### English TL;DR
The paper proposes a two-step validation method integrating a PLM block into generative IE pipelines, which leverages LLMs' correction capability to improve extraction of weakly expressed, low-salience entities, enabling mid-size LLMs to match larger models' performance, particularly for Digital Product Passport (DPP) applications.

### 中文详细总结
本研究聚焦于数字产品护照（DPP）应用中的产品属性信息抽取，提出了一种两步验证方法：首步由微调的PLM（如RoBERTa/DeBERTa）进行初始预测，第二步由LLM验证并修正该输出。实验在Amazon和E-commerce两个数据集上进行，涵盖六个实体类别。结果表明，该方法尤其提升了“Component”、“Material”等弱表达、低显著性实体的抽取F1分数。中等规模LLM（如Llama-3.1 8B、Mistral 24B）在验证任务中性能提升显著，某些实体上甚至达到与Llama-3.3 70B相近的水平。然而，对最小开源模型（Llama-3.2 3B）的效果有限。基于此，作者开发了本地部署的演示应用，以应对实际DPP场景中的数据隐私和泛化需求。

### 方法 / 贡献
- 提出两步验证生成式IE框架：PLM首步预测 + LLM第二步验证修正
- 将LLM的任务从直接抽取重新定义为“验证并修正PLM输出”
- 方法提升了对弱表达、低显著性实体的抽取性能
- 使中等规模LLM达到与大规模LLM相当的性能，利于本地部署与数据隐私
- 开发了面向真实DPP用例的演示应用

### 实验或数据
- 数据集：两个开源数据集，Amazon Product Description (426实例) 和 E-commerce Text Classification (512实例)，分别标注了6个实体类（Size, Weight, Product number, Component, Material, Manufacturer）
- 实体定义：Size/Weight/Product number为显性实体，Component/Material/Manufacturer为弱表达实体（更具挑战性）
- 模型：4种PLM（RoBERTa/DeBERTa各两个数据集版本）+ 7种LLM（从3B到70B，包括Llama、Mistral、Gemma系列）
- 比较基线：标准抽取任务（Extraction）与验证任务（Validation，含空字典基线）

### 值得关注点
- 验证任务显著优于标准抽取任务，尤其对中等规模LLM（Llama-3.1 8B在Amazon上F1从54.17提升至61.45）
- Mistral-small-3.1 24B在E-commerce数据集上验证任务F1达50.19，超过70B模型
- PLM首步预测质量影响LLM最终输出，更好的PLM预测带来更大提升
- 方法在弱表达实体（Component, Material, Manufacturer）上效果最显著，提示LLM擅长修正而非自主抽取此类实体

### 局限性
- 对最小开源LLM（Llama-3.2 3B）效果有限，在部分验证配置上甚至低于标准抽取
- 部分LLM（如Mistral-0.3 7B）在验证任务上表现不稳定，PLM预测有时反而降低性能
- 数据集规模较小（约500实例），标注由单一人完成，可能影响泛化性
- 未在更多领域或更大规模数据集上验证方法有效性
- 未涉及多语言或跨领域适应性实验

## 3. Evaluating Prompt Scope and Demonstration Similarity in Local LLM Machine Translation

- Source: arxiv
- arXiv ID: 2607.26286
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2607.26286v1
- PDF: https://arxiv.org/pdf/2607.26286v1
- DOI: https://doi.org/10.48550/arXiv.2607.26286

### Authors

Mihael Arcan

### Abstract

Large language models (LLMs) are increasingly used as general-purpose translation systems, but their behavior is usually evaluated under a single prompt shape: translate one source sentence into one target language. In practice, users may ask for one target language, for several related languages at once, or for translations conditioned on examples. This paper studies prompt scope and demonstration selection as experimental variables for local LLM machine translation. We evaluate English-to-Romance and English-to-Germanic translation on the full FLORES devtest split for nine official European Union languages. We compare three local instruction-tuned LLMs, llama3.2:3b, mistral:latest, and qwen2.5:14b, against dedicated MT baselines from OPUS-MT and NLLB-200. We test zero-shot prompting and k=5 few-shot prompting with random, lexical-similarity, and embedding-similarity demonstration selection. We also compare single-target prompts with JSON-formatted family-scope prompts that request all languages in a family at once. Results show that dedicated MT systems remain strongest overall, especially for Germanic languages. Few-shot prompting helps mistral:latest and qwen2.5:14b, but hurts llama3.2:3b; embedding retrieval is best on average for the stronger LLMs, but its advantage over random and lexical examples is modest. Family-scope prompting is feasible for stronger local LLMs but exposes structured-output failures in smaller models. These findings motivate evaluating LLM translation not only by language pair and metric, but also by prompt scope, retrieval strategy, and multi-target compliance.

### 中文一句话结论
本文系统研究了提示范围（单目标 vs. 多目标语言族）和示例选择策略（零样本、随机、词法相似、嵌入相似）对本地大语言模型机器翻译质量的影响。

### English TL;DR
This paper systematically investigates how prompt scope (single-target vs. family-scope) and demonstration selection strategies (zero-shot, random, lexical-similarity, embedding-similarity) affect the machine translation quality of local LLMs, finding dedicated MT systems remain strongest overall.

### 中文详细总结
本研究针对本地大语言模型（LLM）在机器翻译中的实际使用场景，将提示范围和示例选择作为实验变量进行系统性评估。研究覆盖英语到罗曼语族（法语、西班牙语、意大利语、葡萄牙语、罗马尼亚语）和日耳曼语族（德语、荷兰语、丹麦语、瑞典语）共9种欧盟官方语言的翻译任务，使用完整的FLORES devtest测试集。对比三种本地指令微调LLM（llama3.2:3b、mistral:latest、qwen2.5:14b）与专用MT基线系统（OPUS-MT/MarianMT和NLLB-200）。实验设置包括零样本提示和k=5的少样本提示，其中少样本示例分别采用随机选择、词法相似度选择和嵌入相似度选择三种策略。同时对比单目标提示和JSON格式的多目标语言族提示（同一提示中请求一族所有语言）。

主要发现：
1. 专用MT系统整体表现最强，尤其在日耳曼语族语言上优势明显。
2. 少样本提示对mistral:latest和qwen2.5:14b有提升作用，但会降低llama3.2:3b的性能。
3. 基于嵌入的示例检索在强模型上平均表现最佳，但其相对于随机和词法示例的优势有限。
4. 多目标语言族提示对大模型可行，但在小模型上暴露了结构化输出的失败模式（如遗漏目标语言、格式错误等）。

### 方法 / 贡献
**方法：**
- 将提示范围（单目标 vs. 多目标语言族）和示例选择策略作为关键实验变量
- 使用三种不同的示例检索方法：随机、词法相似（源句子词袋表示余弦相似度）、嵌入相似（多语言句子嵌入余弦相似度）
- 评估指标：sacreBLEU BLEU、chrF++、COMET，以及多目标语言族提示的合规性指标（目标覆盖率和完整输出率）

**贡献：**
- 首次系统评估提示范围对本地LLM翻译效果的影响
- 揭示结构化输出（JSON格式的多目标翻译）在小模型上的失败模式
- 提出LLM翻译评估不应仅考虑语言对和指标，还应报告提示范围、检索策略和多目标合规性

### 实验或数据
**数据集：** FLORES-200 devtest完整分割（1012个英语源句子），示例从FLORES dev中选取

**模型对比：**
- 本地LLM：llama3.2:3b、mistral:latest、qwen2.5:14b（通过Ollama运行，temperature=0）
- 专用MT基线：facebook/nllb-200-distilled-600M、facebook/nllb-200-distilled-1.3B、OPUS-MT/MarianMT模型

**实验结果示例：**
- 法语翻译（qwen2.5:14b, 嵌入少样本）：chrF++ 64.27, BLEU 41.09, COMET 0.8672
- 德语翻译：专用MT基线表现最佳，本地LLM差距较大
- 多目标提示：qwen2.5:14b在罗曼语族表现可接受，但小模型（llama3.2:3b）出现严重结构化输出失败

### 值得关注点
1. 提示设计成为翻译系统的一部分：LLM翻译中，如何构造提示（单目标/多目标、零样本/少样本、示例选择方式）直接影响翻译质量
2. 少样本提示的双刃剑效应：对部分模型有效，对另一部分模型反而有害
3. 结构化输出挑战：多目标语言族提示在实用性上有价值，但小模型的JSON输出能力不足构成关键瓶颈
4. 专用MT系统仍有显著优势：尽管LLM在翻译领域取得进展，但本地部署的小型号LLM在多数场景仍不如专用翻译模型

### 局限性
1. 仅评估英语作为源语言的情况，未涉及其他源语言的翻译
2. 所有评测语言均为高资源欧盟官方语言，未涉及低资源语言场景
3. 本地LLM仅评估三个模型，且均为中等参数量（3B-14B），未涵盖更大型模型或云API模型
4. 未深入研究示例内容与源句子之间的语义匹配对翻译质量的细粒度影响
5. 未评估术语注入或领域知识对翻译的提升效果
6. 多目标语言族提示仅测试罗曼语族和日耳曼语族，未涉及更复杂或更远缘的语言关系

## 4. DIRECT: Direct Decoding for Efficient and Aligned Sequence Labeling with Large Language Models

- Source: arxiv
- arXiv ID: 2607.26891
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.26891v1
- PDF: https://arxiv.org/pdf/2607.26891v1
- DOI: https://doi.org/10.48550/arXiv.2607.26891

### Authors

Yilei Wang, Jiaxin Gan, Kexuan Zhang, Ling Li, Wentao Zhang, Peichao Lai

### Abstract

Sequence labeling is a fine-grained information extraction task, yet existing large language model-based approaches suffer from insufficient domain alignment and low inference efficiency. To address these issues, we propose DIRECT, a framework that addresses these issues through training-time optimization and inference-time rectification. Specifically, DIRECT performs Direct Preference Optimization (DPO) after supervised fine-tuning to strengthen task alignment with human preferences, and introduces a controlled decoding process that enforces fixed output formats and restricts predictions to candidate sets. To further improve efficiency, a template-filling mechanism requires the model to generate only label tokens while reusing prefixed content through the KV Cache, thus reducing redundant computation. Experimental results on eight datasets demonstrate that DIRECT achieves significant improvements in both performance and efficiency compared to existing methods.

### 中文一句话结论
DIRECT通过训练阶段的直接偏好优化（DPO）和推理阶段的模板填充式受控解码，显著提升了大语言模型在序列标注任务上的领域对齐能力和推理效率。

### English TL;DR
DIRECT enhances sequence labeling in large language models by combining Direct Preference Optimization for better task alignment with a template-filling controlled decoding mechanism that significantly boosts inference efficiency.

### 中文详细总结
序列标注（如命名实体识别、词性标注）是细粒度信息抽取任务，但现有基于大语言模型的方法存在领域对齐不足和推理效率低的问题。本文提出DIRECT框架，包含两个核心创新：1）训练阶段：在监督微调（SFT）后进行直接偏好优化（DPO），通过构建偏好对（正确输出 vs BLEU高但F1低的错误输出）增强模型对任务和人类偏好的对齐；2）推理阶段：采用受控解码过程，强制固定输出格式并将预测限制在预定义候选集中，同时引入模板填充机制——模型只需生成标签token，通过KV缓存复用前缀内容，避免冗余计算。在8个低资源数据集（4个中文NER、2个英文NER、2个中文POS）上的实验表明，DIRECT在性能和效率上均优于现有方法（如InstructUIE、GoLLIE、GNER），推理速度提升最高达9倍。

### 方法 / 贡献
1. **领域自适应对齐优化**：结合SFT与DPO（离线采样策略，基于BLEU和F1构建偏好对），并在推理时加入受控干预（强制格式+候选集约束），使模型更好地理解任务并符合人类偏好。
2. **高效推理**：模板填充机制让模型仅生成标签token，其余部分通过模板和KV缓存完成，减少冗余计算。
3. **SOTA性能**：在8个低资源数据集上，DIRECT（尤其以GLM4-9B-Chat为骨干）在大部分设置中取得最佳或次佳F1分数。

### 实验或数据
- 实验涵盖8个数据集：NER（Weibo、Youku、Taobao、Resume、MIT-Movie、CoNLL03）和POS（UD、CTB6）。
- 低资源设置：每个数据集随机采样250/500/1000个样本进行训练。
- 基线方法：InstructUIE、GoLLIE、GNER。
- 骨干模型：LLaMA-3.1-8B-Instruct和GLM4-9B-Chat。
- 结果：DIRECT在大部分实验设置中F1最高，GLM4变体性能更强；推理速度提升9倍（相比SOTA方法）。

### 值得关注点
- DPO偏好对的构建策略独特：选择BLEU最高但F1最低的生成结果作为负样本，最大化熵增益。
- 推理时通过KV Cache预填充和逐步增量更新，将多次注意力计算合并为一次，效率提升显著。
- 代码和模型未公开，但方法可复现性强。

### 局限性
- 方法依赖预定义标签候选集，对开放域或未知标签的适应性有限。
- DPO训练需额外构建偏好对，增加了数据准备和计算开销。
- 实验仅在低资源场景下验证，高资源场景性能未报告。
- 仅测试了NER和POS任务，对其他序列标注子任务（如语义角色标注）的泛化性未知。

## 5. Language Models are not Equally Robust to Non-Canonical Tokenization across Languages

- Source: arxiv
- arXiv ID: 2607.26831
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.26831v1
- PDF: https://arxiv.org/pdf/2607.26831v1
- DOI: https://doi.org/10.48550/arXiv.2607.26831

### Authors

Poulami Ghosh, Preethi Jyothi

### Abstract

Despite the existence of exponentially many valid tokenizations for a given string, language models operate on a single canonical sequence deterministically produced by the tokenizer, leaving the broader tokenization space largely uncharacterized. In this paper, we investigate this overlooked space by studying the behavior of language models under non-canonical tokenizations across diverse languages. For English, prior work shows that models are largely invariant to alternative tokenizations that represent the same underlying string. We ask whether this invariance generalizes to other languages beyond English. We conduct a multilingual study across 27 languages spanning diverse scripts and evaluate LLM behavior under alternative tokenizations across six downstream tasks. We find that tokenization invariance does not generalize: model behavior varies substantially across languages with instruction-tuned models exhibiting an average relative performance drop of 23.7% for Llama-3.1-8B, 11.4% for Qwen3-8B, and 9.9% for Gemma-3-12B. The variation of tokenization invariance is systematic across languages. Languages that exhibit higher token fragmentation show significantly greater sensitivity to non-canonical tokenizations. Our study of tokenization robustness serves as a diagnostic of how tightly a model is coupled to its tokenizer. These results demonstrate that tokenization robustness is not a universal property of language models, but depends strongly on the language and its interaction with the tokenizer. We also show that LoRA fine-tuning with multi-tokenization training data provides an effective mitigation for tokenization sensitivity. Fine-tuning on English alone improves tokenization robustness across languages, while systematically sampling diverse non-canonical tokenizations achieves the strongest overall performance.

### 中文一句话结论
语言模型对非规范分词（non-canonical tokenization）的鲁棒性并非普遍一致，而是因语言和分词器的交互方式而系统性地变化，且可以通过多分词微调有效缓解。

### English TL;DR  
This paper reveals that language models’ robustness to non-canonical tokenization is not universal—it varies systematically across languages due to differences in token fragmentation, and can be mitigated by LoRA fine-tuning with multi-tokenization training data.

### 中文详细总结
本研究系统性地探讨了多语言大语言模型（LLM）在非规范分词下的行为。英文先验研究表明模型对相同字串的不同分词方式几乎保持不变，但本研究发现这种不变性在其他语言中并不普遍。在27种语言和6个下游任务的评估中，指令微调模型在非规范分词下性能显著下降，平均相对降幅为 Llama-3.1-8B 的23.7%，Qwen3-8B 的11.4%，Gemma-3-12B 的9.9%。分词不变性的变化具有系统性：词碎片化（token fragmentation）程度越高的语言，其模型对非规范分词越敏感。研究还发现，使用多分词训练数据进行LoRA微调可以有效缓解这种敏感性，且系统地采样多样化的非规范分词方案能获得最优的整体性能提升。

### 方法 / 贡献
- **方法**：定义非规范分词空间（uniformly sampled from space of all valid tokenizations using MDD），对比规范分词、随机非规范分词和字符级分词下的模型输出差异。
- **贡献**：
  1. 首次系统性地研究非规范分词对多语言LLM的影响，覆盖27种语言、6个任务和3个模型族。
  2. 分析不同语系和文字下模型对非规范分词敏感性的差异，揭示其与词碎片化程度的关系。
  3. 提出使用多分词数据进行LoRA微调作为有效缓解方案，展示其跨语言泛化能力。

### 实验或数据
- **模型**：Llama-3.1-8B-Instruct、Qwen3-8B、gemma-3-12b-it（均为指令微调版本）。
- **语言**：27种语言，覆盖多种语系和文字。
- **任务**：6个下游任务，包括短答案任务（MLQA、MGSM）和多选题任务（Multi-ARC、Multi-HellaSwag等）。
- **评估设置**：遵循lm-evaluation-harness框架，扩展支持替代分词方案；对随机非规范分词采样5次取均值。

### 值得关注点
- **非通用性**：分词鲁棒性并非模型固有属性，而是取决于语言本身及其与分词器的交互。
- **词碎片化指标**：语言级别的词碎片化程度（平均每词token数）与模型对非规范分词的敏感性高度相关，可作为诊断工具。
- **缓解策略**：仅使用英文多分词微调即可跨语言提升分词鲁棒性，而系统地采样多样化的非规范分词方案效果最强。

### 局限性
- **排除高度碎片化语言**：由于某些语言（如孟加拉语、泰米尔语等）的规范分词已接近字符级分词，无法构造有意义的非规范变体，因而被排除在主分析之外。
- **模型覆盖有限**：主要基于三个模型族（Llama、Qwen、Gemma），结论可能不适用于其他架构或更大规模模型。
- **实验范围**：未涉及对抗性非规范分词或安全性影响，且仅在27种语言上验证，资源更匮乏的语言尚未覆盖。

## 6. OptimismBench: Forecasting Bias and the Alignment Effect in Language Model Judgment

- Source: arxiv
- arXiv ID: 2607.26981
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.26981v1
- PDF: https://arxiv.org/pdf/2607.26981v1
- DOI: https://doi.org/10.48550/arXiv.2607.26981

### Authors

Seonglae Cho, Adriano Koshiyama

### Abstract

Large language models are increasingly used as decision aids whose probability judgments shape downstream choices. Whether those judgments carry a systematic directional tilt has been hard to detect: calibration metrics aggregate unsigned errors, and naturalistic uncertainty offers no ground-truth probability. When an LLM rates a startup's success at 70% but its failure at 15%, the missing 15 points expose a distortion no aggregate score flags. We introduce OptimismBench, which detects directional bias with inverted pairs: each scenario elicits both P(success) and P(failure), and asymmetry between the two framings yields a signed bias score without ground truth. Across 16 models from 8 providers, fourteen are optimistic; pessimism appears only in Anthropic's frontier tier. Eleven matched base-versus-chat pairs across four families show post-training sets the sign of the bias, with opposite shifts in different families. The pattern survives prompt, temperature, perspective, and self-debiasing ablations. A seventeen-model six-language comparison further shows model identity dominates language, with inter-model variance at 4.7x inter-language variance. We release 3,870 items across 10 languages for per-model directional-bias auditing. When alignment makes a model more helpful, it also tilts its probabilities; downstream pipelines inherit the tilt by default.

### 中文一句话结论
本文提出OptimismBench框架，通过对概率判断中正反框架的不对称性测量，发现大多数大语言模型存在显著的系统性乐观偏差，且后训练对齐决定了偏差的方向。

### English TL;DR
OptimismBench uses inverted-pair probing to reveal that most large language models exhibit systematic optimism bias in probability judgments, with alignment determining the sign of the bias and model identity dominating language effects.

### 中文详细总结
本文针对大语言模型概率判断中存在的系统性方向偏差（如乐观或悲观）提出检测框架OptimismBench。核心方法是“倒置对”（inverted pairs），即对同一情景同时要求模型评估正向结果概率和负向结果概率，通过二者的不对称性计算带符号的Skew分数，无需真实概率作为参照。研究覆盖了来自8家提供商的16个模型，在10种语言共60个情景上测试。结果显示：其中14个模型表现出乐观偏差，仅Anthropic的前沿模型（Opus 4.6和Sonnet 4.6）呈现悲观偏差。通过11组基础模型与对话模型的对照（分属Qwen、Llama、Gemma、Mistral四个家族），发现后训练过程（alignment）决定了偏差的符号方向，且不同家族方向相反（Qwen压缩偏差，Llama放大乐观）。该模式在提示词、温度、视角、自我去偏等多种干预下保持稳定。跨语言比较（17个模型、6种语言）显示模型身份对偏差的影响是语言影响的4.7倍。研究发布了3870个条目（10种语言）用于模型级方向偏差审计。

### 方法 / 贡献
- **方法**：提出倒置对测量方法，定义Skew = s⁺ − (100 − s⁻)，正值为乐观偏差（高估正向、低估负向），负值为悲观偏差。进一步的分解 δ⁺ 和 δ⁻ 可区分经典乐观/悲观与复合过度/不足声称。设计了四条轨道（Track A-D）：Track A为基率控制校准（期望Skew≈0），Track B为主测量（自然场景概率估计），Track C为推荐强度，Track D为显著性评估。此外采用叙事操控、视角转换等因子干预探究偏差来源。
- **贡献**：①首个系统性测量LLM概率判断方向偏差（乐观/悲观）的基准；②通过基模型/对话模型对照，揭示后训练对齐对偏差符号的决定性作用（且家族特异性）；③跨语言方差分解证明模型身份主导语言因素；④公开大规模多语言数据集供审计。

### 实验或数据
- **主体实验**：16个模型（来自OpenAI、Anthropic、Meta、Google、DeepSeek、Alibaba、Mistral、Zhipu），60个情景（Track B），10种语言，每个情景运行10次，统计Skew均值。所有模型p<0.002（Bonferroni校正）。
- **对照实验**：11组base-versus-chat配对（Qwen 5对、Llama 4对、Gemma 2b 1对、Mistral Small 1对），验证后训练影响。
- **鲁棒性测试**：改变提示词、温度、视角、添加自我去偏指令，偏差模式基本不变。
- **跨语言分析**：17个模型、6种语言（英、德、法、西、中、韩），模型间方差是语言间方差的4.7倍。
- **数据集**：共3870个条目，覆盖10种语言，用于每个模型的方向偏差审计。

### 值得关注点
- 几乎所有LLM都存在显著方向偏差，且绝大多数为乐观倾向（仅Anthropic的前沿大模型悲观），说明该偏差普遍且与规模无关。
- 后训练对齐（而非预训练）是偏差符号的主要决定因素，且不同家族对齐方向相反——提示开发者需针对性监测和校正。
- 模型身份的影响远超语言，说明偏差主要由模型本身驱动，而非语言文化差异。
- 偏差在多种干预（如自我去偏指令）下依然稳健，说明普通提示难以消除。

### 局限性
- 仅针对概率判断中的乐观/悲观偏差，未涵盖其他认知偏差（如锚定、框架效应等）。
- 未与人类真实判断直接对比，无法断定LLM偏差是否偏离人类基线。
- 情景数量有限（60个），可能无法完全代表现实多样化场景。
- 依赖模型输出整数概率（0–100），可能受模型输出格式和数值精度影响。
- 未深入验证偏差对下游实际决策（如投资、风险评估）的传递效应与损害程度。

## 7. Contrastive ESA: Human Evaluation of Multiple Translations at Once

- Source: arxiv
- arXiv ID: 2607.26640
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2607.26640v1
- PDF: https://arxiv.org/pdf/2607.26640v1
- DOI: https://doi.org/10.48550/arXiv.2607.26640

### Authors

Vilém Zouhar, Roman Grundkiewicz, Sara Rajaee, Parker Riley, Martin Popel, Rachel Bawden, Philipp Koehn, Marine Carpuat, Tom Kocmi

### Abstract

Current human evaluation of machine translation typically assesses single outputs in isolation, a paradigm that suffers from high annotator noise and cost. We introduce Contrastive Error Span Annotation (cESA), a protocol that presents multiple translations of the source input (text, video, audio, image). In cESA, the annotator sees multiple translations of the same document, marks major and minor error spans, and then assigns a score from 0% to 100% on absolute scale. By allowing annotators to access the shared context across multiple outputs, cESA facilitates more consistent and efficient judgments. We validate cESA using a large-scale human evaluation of English->Japanese translations of 12 models, demonstrating reductions in annotation time and noise compared to standard pointwise evaluation. Unlike existing contrastive ranking methods, cESA yields absolute quality judgments that enable simple, interpretable non-parametric model rankings without the need for post-hoc corrections.

### 中文一句话结论
本研究提出的对比式错误跨度标注（cESA）协议通过同时展示多个翻译输出，显著降低了人工评估的时间和噪声，并生成了可直接用于非参数模型排名的绝对质量分数。

### English TL;DR
This paper introduces Contrastive Error Span Annotation (cESA), a protocol that reduces human evaluation noise and annotation time by having annotators assess multiple translations simultaneously, allowing for absolute quality scores and simple, interpretable non-parametric model rankings.

### 中文详细总结
当前的机器翻译人工评估通常孤立地评估单个输出，存在标注噪声高和成本高的问题。本文提出对比式错误跨度标注（cESA）协议。该协议向标注员同时展示同一源文档的多个翻译输出（文本/视频/音频/图像），要求标注员标记主要和次要错误跨度，并在0%至100%的绝对尺度上打分。通过让标注员访问多个输出间的共享上下文，cESA促进了更一致和高效的判断。作者使用英语→日语翻译的大规模人工评估（涉及12个模型）验证了该协议，证明与标准逐点评估相比，cESA减少了标注时间和噪声。与现有的对比排序方法不同，cESA输出绝对质量判断，无需事后校正即可实现简单、可解释的非参数模型排名。

### 方法 / 贡献
- **协议设计**：在现有ESA协议基础上，将“逐点展示一个翻译”改为“同时展示k个翻译（k=2,3,4）”，标注员需为每个翻译标记错误跨度并打分（0-100%，5%步长）。
- **核心优势**：
  - 利用“联合评估”的心理测量优势（发现一个翻译的错误有助于发现其他翻译的错误；看到可能翻译的空间有助于客观评估；共享文档上下文减少重复阅读时间）。
  - 保留绝对分数，可直接进行非参数模型平均排名，不依赖参数化贝叶斯模型（如TrueSkill）进行事后修正。
- **可用性**：提供开源标注工具Pearmut，可通过命令行快速启动cESA评估。

### 实验或数据
- **数据**：使用WMT 2025通用翻译共享任务中的英语→日语子集，包含38个文档共97个片段，涵盖新闻、视频和社交媒体截图等不同领域。
- **实验设计**：
  - 小规模：标准ESA vs. cESA (k=1)，覆盖4个翻译模型。
  - 大规模：cESA (k=1,2,3,4)比较，覆盖10个翻译模型（含1个人类翻译），所有评估由两组不同的专业标注员完成。
  - 使用重复翻译计算内部和标注员间一致性。
- **结果**：
  - 与逐点ESA相比，cESA(k=3)在每个片段上的标注时间节省高达31%（77.8s → 53.7s）。
  - cESA在标注质量（稳定性、标注员间一致性）上优于或等同于逐点ESA。
  - 具体数据见文章Table 1。

### 值得关注点
- **效率提升**：同时展示多个输出显著降低了总标注时间，因为源文档和上下文只需阅读一次。
- **质量提升**：标注噪声降低，标注稳定性提高。标注员间一致性（Inter-annotator agreement）和内部一致性（Intra-annotator agreement）均优于或等同于逐点评估。
- **实践性**：提供了详细的标注指南、交互式教程以及可部署的开源工具，使其他研究者能够直接采用该协议。
- **绝对分数**：与对比排序方法不同，cESA保留了绝对质量分数，使模型排名更直观、可解释，且无需复杂的后处理建模。
- **最优k值**：k=3在时间效率和标注质量之间取得了最佳平衡。

### 局限性
- 该协议仅在英语→日语单一语言对上测试，在其他语言对上的泛化性有待验证。
- 如果k值过大（如k≥4），可能因信息过载而降低效率（在实验中k=4的时间成本已高于k=3）。
- 虽然标注员间一致性有所提高，但绝对一致性水平（MAE值）仍然存在，表明评估仍有一定噪声。
- 该方法仍依赖人工标注，对于实时或极大规模的系统评估而言，成本仍然较高。

## 8. When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses

- Source: arxiv
- arXiv ID: 2607.26348
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.26348v1
- PDF: https://arxiv.org/pdf/2607.26348v1
- DOI: https://doi.org/10.48550/arXiv.2607.26348

### Authors

Zihan Chen, Di Zhu, Lei Nico Zheng

### Abstract

Large language models (LLMs) are increasingly used as synthetic users, stand-ins for human respondents whose simulated answers feed product, policy, and market decisions. We ask when this substitution is valid and when it fails, and package the answer as an evaluation framework for intelligent synthetic-user systems. A single protocol, run across four models spanning two families and an 8B-to-frontier capability range, is applied to two independent domains of real human-response data: U.S. general social attitudes (General Social Survey) and cross-cultural values (World Values Survey). Every model is benchmarked against a suite of non-LLM baselines fit on held-out human data. Under demographic prompting and the survey-simulation protocols we test, two failures replicate across both domains, all four models, and both families. First, at the individual level no LLM beats even the strongest baseline; on cross-cultural values every model falls well below it, and the gap survives distance-aware and proper scoring. Second, models systematically over-determine demographics, treating identity as far more predictive of attitudes than it is among real people, a distortion present for nearly every question-group combination and robust to a coding-invariant measure. Neither failure is remedied by a larger, more capable model. A decision-impact analysis shows why this matters in practice: on a segment-targeting task the models inflate between-segment gaps two to fourfold, would direct a team to the wrong segment in half of U.S. and most cross-cultural cases, and manufacture segment splits that do not exist in real people. We make the cross-domain benchmark and the evaluation framework available on request, so that teams can determine in advance when synthetic-user evidence is safe for decision support and when it is not.

### 中文一句话结论
在人口统计提示下的调查模拟中，大型语言模型在个体层面无法超越简单的人口统计基线，并且系统性地夸大人口特征对态度的预测力，这一失败跨领域、跨模型一致存在，且无法通过使用更大更强的模型来弥补。

### English TL;DR
LLM-simulated survey respondents fail to outperform simple demographic baselines, systematically exaggerate how much demographics predict attitudes, and these failures persist across models and domains, making them unreliable for decision support without validation.

### 中文详细总结
本研究系统评估了大型语言模型作为“合成用户”替代人类调查受访者的有效性。作者通过统一的实验协议，在四个不同规模和系列的模型上，对两个独立领域（美国一般社会态度调查GSS和跨文化价值观调查WVS）的真实人类数据进行模拟和基准测试。核心发现是：1）在个体预测层面，所有LLM均未超越基于真实数据训练的非LLM基线模型（如逻辑回归、随机森林），在跨文化价值观任务中，LLM的准确率比基线低11-22个百分点；2）LLM系统性地“过度决定”人口统计学特征，即模型认为人口特征对态度的预测力远高于实际情况，这种失真在几乎所有问题-群体组合中均存在。决策影响分析表明，这种扭曲会导致团队错误定位目标群体、夸大群体间差异（2-4倍），甚至制造现实中不存在的群体分裂。重要的是，模型规模越大越不能解决这些问题。

### 方法 / 贡献
1. **跨领域基准测试框架**：构建了包含美国社会态度（GSS）和63国价值观（WVS）两个独立领域的可复现基准，统一协议、提示、解码和评估指标。
2. **基线锚定评估**：引入非LLM基线（人口统计查找表、逻辑回归、随机森林）作为比较基准，证明LLM在个体层面没有信息增益。
3. **刻板印象指数**：提出衡量模型夸大人口特征预测力的量化指标（同时使用Cramér's V作为编码不变性验证）。
4. **决策影响分析**：将发现转化为实际决策后果（错误目标定位、群体间差距膨胀、制造虚假分割）。
5. **验证框架**：提供可用于部署前评估合成用户安全性的工具包。

### 实验或数据
- **数据**：GSS 2016-2024年共10个态度问题；WVS第7波63国16个价值观问题。
- **模型**：4个模型，涵盖两个模型家族，参数量从8B到前沿水平。
- **协议**：统一的人口统计提示和调查模拟协议，包括单答案提示和概率分布提示两种格式。
- **评估**：使用多种指标——精确匹配、距离感知评分（用于序数尺度）、对数损失和Brier分数（用于分布输出），均带配对bootstrap置信区间。
- **实验覆盖**：在GSS和WVS两个领域所有4个模型上进行测试，确保跨领域、跨模型的可复制性。

### 值得关注点
1. **完全的一致失败**：两个核心失败在“两个领域、所有四个模型、两个模型家族”下均存在，说明这是LLM系统性问题。
2. **巨大模型无助益**：前沿模型（更大更强）不仅没有解决这两个问题，反而刻板印象更严重。
3. **实用决策影响**：LLM建议会误导团队走向错误的目标群体（美国50%、跨文化72%），导致2-4倍的群体差异膨胀。
4. **诊断框架价值**：论文的核心交付物不是负面结果本身，而是帮助团队预先判断合成用户是否可信的验证框架。

### 局限性
1. **研究范围限定**：结论仅限于“人口统计提示下的调查模拟”这一特定设定，不适用于其他合成用户生产方法（如微调、更丰富的角色构建）。
2. **领域有限**：仅涵盖美国社会态度和跨文化价值观两个领域，其他领域（如心理学实验、行为经济学）的泛化性需进一步验证。
3. **提示格式有限**：仅测试了两种提示格式（单答案提示和概率分布提示），其他提示变体（如角色扮演、系统消息调整）可能带来不同结果。

## 9. Pangram 4 Technical Report

- Source: arxiv
- arXiv ID: 2607.27183
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.27183v1
- PDF: https://arxiv.org/pdf/2607.27183v1
- DOI: https://doi.org/10.48550/arXiv.2607.27183

### Authors

Ben Glickenhaus, Katherine Thai, Jenna Russell, Elyas Masrour, Yue Han, Max Spero, Bradley Emi

### Abstract

We present Pangram 4, the latest deep-learning-based AI-text classification model from Pangram Labs. We achieve an AUROC of 0.9916 with a false positive rate of 0.0041% and a false negative rate of 0.3396%. In addition to its increased overall accuracy compared with Pangram 3, Pangram 4 exhibits superior out-of-distribution generalization and robustness to adversarial attacks. Another novel contribution of Pangram 4 is its improved ability to distinguish fine-grained edits and mixed AI-human co-authored text. We demonstrate improvements to both boundary detection tasks and the detection of interleaved AI assistance. Finally, we report metrics on standard AI detection benchmarks showing that Pangram 4 achieves state-of-the-art performance on the AI text detection task across a wide variety of settings and domains.

### 中文一句话结论
Pangram 4 是最新的基于深度学习的AI文本分类模型，在AUROC达到0.9916、极低误报率和漏报率的同时，具备更强的分布外泛化能力、对抗攻击鲁棒性，并能同时检测细粒度的AI-人类协作文本和逐词作者边界。

### English TL;DR
Pangram 4 is a state-of-the-art deep-learning AI-text classification model that achieves an AUROC of 0.9916 with extremely low false positive and false negative rates, while also offering superior out-of-distribution generalization, robustness to adversarial attacks, and the novel ability to simultaneously detect fine-grained mixed AI-human co-authored text and per-token authorship boundaries.

### 中文详细总结
Pangram 4 是 Pangram Labs 开发的最新一代AI文本检测模型。相比前代Pangram 3，它在整体准确率上有显著提升，具体表现为：AUROC达到0.9916，误报率仅为0.0041%，漏报率为0.3396%。该模型能够检测前沿大语言模型（如Claude Fable 5和GPT-5.6 Sol）生成的文本。其重要创新包括：在单次推理中同时识别“异质混合文本”（每个词有明确作者归属）和“同质混合文本”（作者身份因编辑过程而混合），并能进行逐词的作者归属分类（人类、AI辅助、AI生成）。此外，Pangram 4还引入了“人性化检测”作为辅助任务，识别故意规避AI检测的文本变换（如输入错误、同形字攻击等）。模型采用软N元语法标注方法生成训练标签，以解决混合文本中缺乏逐词标签的问题。

### 方法 / 贡献
- **性能提升**：AUROC 0.9916，极低误报率（0.0041%）和漏报率（0.3396%），优于Pangram 3。
- **逐词三分类**：对输入序列的每个词预测{人类, AI辅助, AI生成}三类标签，单次推理同时处理异质和同质混合文本。
- **人性化检测辅助任务**：文档级四分类（人类、AI生成、人性化AI、混合作者），识别逃避检测的故意变换。
- **软N元语法标注**：使用基于从句级别的软N元语法方法生成混合文本的训练标签，替代EditLens中的标量距离度量。
- **对抗鲁棒性与分布外泛化**：在对抗攻击和分布外场景下表现更优。

### 实验或数据
论文未报告具体的实验设置、基准测试名称或数据集列表。训练数据来源包括多种领域、语言和生成器模型，涵盖人类写作、AI生成文本（通过内部合成镜像算法生成）和AI辅助文本（根据EditLens方法生成）。训练集未使用用户提交数据、API客户数据或未经授权的互联网爬取数据。模型效果基于标准AI检测基准进行了评估，在多种设置和领域上达到最先进水平。

### 值得关注点
- **首次实现同质和异质混合文本的同步检测**：在单次推理中同时输出逐词标签，能区分人类-人类协作、AI-人类协作和纯AI生成的段落。
- **极低误报率**：0.0041%的误报率对本任务中的实际应用（如避免错误标记人类写作）意义重大。
- **定义清晰的AI文本范围**：限定为“原始、实质性、自然语言散文，回应开放式写作任务”，排除了事实性问答、摘要和短文本。
- **人性化检测作为新方向**：明确区分故意逃避检测的操作（如同形字攻击、同义词替换）与无意的文本污染（如OCR错误）。

### 局限性
- **论文未报告具体基准测试名称或详细实验结果**，仅声称达到最先进性能，缺乏可复现的对比数据。
- **模型对文本长度有要求**：仅分析至少50个词的文本，排除了短文本（如对话式回复）的检测能力。
- **检测范围有限**：不适用于事实性问答、摘要任务或简单答案的检测；模型定义为检测“开放式写作任务”中的原创性内容。
- **训练数据未公开**：具体数据集名称、规模和分布未详细列出，仅描述为“多种开源或自有数据集”。
- **人性化检测的局限性**：论文未报告该辅助任务的准确率或误分类率，其有效性尚未量化评估。

## 10. Linguistic Monoculture in LLM-Assisted Language Use

- Source: arxiv
- arXiv ID: 2607.27134
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2607.27134v1
- PDF: https://arxiv.org/pdf/2607.27134v1
- DOI: https://doi.org/10.48550/arXiv.2607.27134

### Authors

Suhas Thejaswi, Juhi Kulshreshta, Lutz Oettershagen

### Abstract

Writing and communication are increasingly mediated by large language models (LLMs) that are being used to draft, revise and polish text. Although such assistance can improve clarity and help authors meet institutional expectations, widespread reliance on shared models may reduce population-level variation in linguistic form, a phenomenon we refer to as linguistic monoculture. We develop a mathematical framework in which authors and LLMs are represented as distributions over linguistic features and coevolve through repeated interaction. We analyze three interaction mechanisms: a shared model with a fixed linguistic distribution, a shared model recursively updated from author outputs, and personalized models updated through author-specific and population-level feedback. We characterize the resulting equilibria and convergence rates, showing that, shared models can drive authors toward a common norm, recursive feedback relocates the shared norm without altering pairwise spread under common conformity, and personalization can preserve a family of distinct author-model equilibria with nonzero linguistic diversity. We then endogenize conformity as a strategic choice trading off private benefits from clarity, legibility, and perceived fluency against distinctive style. Within this utility model, individually rational authors may conform more than is socially optimal because they do not internalize the value their distinctiveness provides to others, creating a negative externality and a price of monoculture that is finite for each fixed instance but can grow without bound when distinctiveness dominates authenticity. Synthetic simulations illustrate how fixed shared assistance, recursive feedback, and personalization produce different long-run diversity outcomes.

### 中文一句话结论
大规模依赖共享大型语言模型可能导致“语言单一文化”，即语言形式上群体层面变异的减少，且个体理性作者会过度趋同，造成社会性负外部性。

### English TL;DR
Widespread reliance on shared LLMs can cause "linguistic monoculture"—a reduction in population-level variation in linguistic form—as individually rational authors conform more than socially optimal, creating a negative externality.

### 中文详细总结
本文提出一个数学框架，将作者和大型语言模型（LLMs）表示为语言特征上的分布，并分析二者的共同演化。作者考察了三种交互机制：使用固定语言分布的共享模型、根据作者输出递归更新的共享模型、以及通过作者特定和群体层面反馈更新的个性化模型。结果表明，共享模型可能推动作者朝向共同规范收敛；递归反馈会改变共享规范但不改变两两间的扩散程度（在共同从众性下）；个性化可以保留一组不同的作者-模型均衡，维持非零的语言多样性。论文进一步内生化从众性，将其视为一种策略选择，作者在清晰度、可读性和感知流畅性的私人收益与独特风格之间权衡。在此效用模型下，个体理性作者可能会比社会最优水平更加从众，因为他们没有内化其独特性为他者提供的价值，从而产生负外部性和“单一文化代价”。模拟结果展示了不同机制对长期多样性结果的影响。

### 方法 / 贡献
- **数学框架**：将作者和LLM表示为语言特征上的分布，并建模共同演化。
- **交互机制分析**：比较固定共享模型、递归更新共享模型和个性化模型三种机制下的均衡与收敛速率。
- **内生从众性模型**：将从众性作为策略选择，纳入私人收益（清晰度、可读性、流畅性）与独特风格的权衡。
- **负外部性理论**：证明个体从众行为产生“单一文化代价”，且该代价在特定条件下可无限增长。

### 实验或数据
论文未提及实际数据集或实验；通过合成模拟（synthetic simulations）展示不同机制下的长期多样性结果。

### 值得关注点
- **语言单一文化概念**：系统性地定义了LLM辅助写作中语言多样性的丧失。
- **数学严谨性**：提供了均衡和收敛速率的理论刻画。
- **政策启示**：揭示了个体理性与社会最优之间的冲突，为设计促进语言多样性的LLM交互策略提供理论基础。

### 局限性
- **理论框架为主**：缺乏基于真实作者-LLM交互数据或现实语言使用案例的实证验证。
- **模拟简化**：合成模拟可能无法完全捕捉现实人类行为的复杂性。
- **特征假设**：基于语言特征分布的假设可能未覆盖所有语言变异维度。

## Processing Notes

- Duplicate papers skipped: 0