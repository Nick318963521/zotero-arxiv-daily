# Daily arXiv - 2026-08-20

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-20T22:54:12
- Paper count: 10

## 1. Nine Emotion Centroids: A Label-Free Valence Axis That Transfers Across Four Modalities

- Source: arxiv
- arXiv ID: 2608.18090
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.18090v1
- PDF: https://arxiv.org/pdf/2608.18090v1
- DOI: https://doi.org/10.48550/arXiv.2608.18090

### Authors

Yousef Radwan

### Abstract

Inside a modern language model sits a single internal direction that tracks how positive or negative a sentence feels. We show how to find this valence axis (V-axis) from just 9 emotion category names plus 50 short narrative paragraphs per emotion -- about 1,500 fewer labels than the usual supervised approach -- and that the same direction appears in vision, audio, and human-brain encoders never jointly trained. The recipe: embed nine emotion-anchored story sets in a frozen encoder, take the top principal direction of the nine averaged embeddings. Projecting new inputs onto it captures 93% of supervised performance on SST-2 (Llama-3-8B-Instruct, AUC 0.772 vs. 0.828), correlates with human valence ratings on 11,811 EmoSet images at r=0.636, reaches AUC 0.906 on ESC-50 audio (p<2.2e-15), and AUC 0.720+/-0.055 on EEG from 123 subjects (p<3.65e-8). The direction is mechanistically active: ablating it collapses sentiment accuracy by 5.5-37.2 pp across three LLMs vs. at most 0.88 pp for matched random directions (z>12). A 2-parameter classifier trained on text labels transfers to images (AUC 0.961), audio (0.764), and brain recordings (0.828) without target-modality labels; a generic 16-D subspace stays at chance (0.525). The recipe is bounded to continuous attributes -- seven tests on categorical concepts return near-chance -- and steering is family-specific (Llama/Mistral yes, Qwen/Gemma no).

### 中文一句话结论
仅用9个情感类别名称和约450段无标注短文，通过主成分分析得到的情感中心点第一主成分，即可在文本、图像、音频和脑电图四种模态的编码器间找到一个通用的效价（Valence）方向，其性能接近完全监督方法。

### English TL;DR
Using only 9 emotion category names and ~450 unlabeled paragraphs, the first principal component of emotion centroids yields a valence axis that transfers across text, vision, audio, and EEG encoders, matching supervised classifiers with minimal labels.

### 中文详细总结
本文提出了一种无需极性标签的方法，仅使用9个情感类别名称（如愤怒、喜悦、恐惧等）和每个类别约50段短文（共约450段），通过将短文嵌入冻结的编码器、取每个类别的平均向量作为情感中心点，再对这9个中心点进行主成分分析（取第一主成分），即可得到一个"效价轴"（Valence Axis, V-axis）。该轴可以衡量输入的正负情感强度。

该方法在四个不同模态的编码器上测试：文本（Llama-3-8B-Instruct）、视觉（CLIP-image）、音频（CLAP-audio）和脑电图（CBraMod-EEG）。结果表明，这个无监督得到的V-axis在SST-2文本情感分类上达到AUC 0.772（监督基线为0.828，捕获93%性能）；在EmoSet图像数据集上与人类效价评级相关系数r=0.636；在ESC-50音频上AUC达到0.906；在123名被试的EEG数据上AUC达到0.720±0.055。此外，通过方向消融实验（在推理时正交投影去除V-axis方向），三个不同LLM的情感准确率下降5.5-37.2个百分点，而随机方向最多下降0.88个百分点（z>12），证明该方向具有因果作用。

一个仅用文本标签训练的双参数逻辑回归分类器（使用V-axis投影得分），可以直接迁移到其他模态（图像、音频、EEG），无需目标模态标签，AUC全部超过0.70（最高0.961），而使用16维通用共享子空间则仅达到0.525（接近随机）。该方法局限于连续属性概念：对7个类别概念测试均表现接近随机；且方向操控效果具有模型家族特异性（Llama/Mistral有效，Qwen/Gemma无效）。

### 方法 / 贡献
1. **V-axis构造方法**：使用9个情感类别名称，每个类别编写约50段短文，通过冻结编码器取最终token的隐状态，计算每个类别平均向量，对9个平均向量进行中心化后进行奇异值分解（SVD），取第一右奇异向量作为效价轴。
2. **四模态通用性**：相同的构造方法（无标签或极少标签）可在文本、图像、音频、脑电图四种独立训练编码器上恢复出效价方向，且方向在模态间具有跨模态迁移能力。
3. **因果证据**：通过推理时方向消融（正交投影去除V-axis），导致SST-2情感准确率显著下降（5.5-37.2个百分点），而随机方向几乎无影响（≤0.88个百分点），证明该方向是模型情感判断的因果关系成分。
4. **跨模态通用分类器**：一个仅在文本标签上训练的双参数逻辑回归分类器，可直接用于其他模态的V-axis投影评分，实现无目标模态标签的跨模态情感分类（AUC≥0.70）。
5. **方法边界定义**：明确该方法仅适用于连续概念（如效价），对类别概念（如颜色、动物、政治倾向等）无效；且操控效果因模型家族而异。

### 实验或数据
- **文本实验**：SST-2数据集，Llama-3-8B-Instruct在残差块20层，V-axis投影分类AUC=0.772（监督基线0.828，捕获93%）。
- **图像实验**：EmoSet数据集11,811张图像，V-axis投影与人类效价评级相关系数r=0.636。
- **音频实验**：ESC-50数据集，V-axis投影分类AUC=0.906（p<2.2e-16）。
- **脑电图实验**：FACED数据集123名受试者，V-axis投影分类AUC=0.720±0.055（p<3.65e-8）。注意：EEG的V-axis构造使用了Fisher线性判别（有监督），其余模态为无监督。
- **因果消融实验**：三个LLM（Llama-3-8B-Inst、Qwen3-1.7B、Qwen3-8B）下方向消融导致SST-2准确率下降5.5-37.2 pp，对应随机方向最多0.88 pp（z≥12σ）。
- **跨模态分类器迁移**：4×4矩阵所有12个非对角交叉模态AUC≥0.70；文本训练头部迁移到图像0.961、音频0.764、脑电图0.828；16维共享子空间基线仅0.525。
- **方法边界测试**：7个类别概念测试（Park-Choe-Veitch词对、长尾检索、多概念探针、AxBench 500概念、CIFAR-100、不同深度切片、深度偏移特异性）均接近随机；9个情感单词本身做句子池（N_c=1）导致AUC=0.50（随机）；需要N_c≥20才开始有效。
- **深度偏移现象**：推理蒸馏模型（DeepSeek-R1-Distill、Qwen3-thinking）中V-axis在中层被抑制，恢复在最后层。

### 值得关注点
1. **极少的标签需求**：仅需9个情感名称和9个写作提示（共18个监督事件）即可构建通用效价轴，比传统监督方法（如SST-2）减少约1546倍标签量。
2. **跨模态迁移能力**：一个无监督得到的1-D方向可以同时适用于文本、图像、音频和脑电图编码器，并且从文本训练的简单分类器可直接迁移到其他模态，无需重新训练。
3. **因果而非相关**：通过方向消融实验证明该方向不仅是相关特征，而是模型情感判断的因果成分（随机方向对比极显著）。
4. **与现有线性表示假设的关系**：该V-axis与Park-Choe-Veitch的判别方向几乎正交（平均|cos|=0.038），表明它是连续属性方向，不同于类别判别方向。
5. **模型家族特异性**：Llama/Mistral系列可被有效操控，Qwen/Gemma系列则无效果，暗示该方法受模型架构或训练数据影响。
6. **深度搜索必要性**：不同模型族最佳层不同（通常中深层最优），且推理蒸馏模型有独特的深度偏移现象。

### 局限性
1. **方法局限于连续属性**：对类别概念（AxBench 500概念等7项测试）均无效，不能用于离散概念探测或操控。
2. **EEG模态的V-axis并非完全无监督**：该模态下轴本身使用Fisher判别（有监督），仅分类头可免标签；其余模态（文本、图像、音频）为无监督。
3. **跨模态通用性受限**：“通用”仅指在测试的四个编码器（CLIP-text、CLIP-image、CLAP-audio、CBraMod-EEG）之间有效，并未在所有可能编码器上验证。
4. **方向消融的证据性质**：方向消融提供的是推理时投影证据，并非完全的反事实干预证据；且不搜索符号翻转。
5. **经验性而非理论证明**：该方法是一个经验规律而非分析性定理，缺乏严谨的理论解释为何PC1恰好对应效价。
6. **模型家族依赖性**：方向操控仅对Llama/Mistral有效，Qwen/Gemma无效，限制了方法在不同模型家族的通用性。
7. **深度的依赖性**：需要针对模型家族进行最佳层搜索（深度搜索），不同模型（尤其是推理蒸馏模型）表现不同，增加了使用复杂度。
8. **需要一定数量的句子池**：N_c必须≥20才能产生非平凡结果（N_c=1时随机），不能仅用单个情感词本身。

## 2. Assessing Quality of Experience in Natural Language Generation of German Text

- Source: arxiv
- arXiv ID: 2608.18888
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.18888v1
- PDF: https://arxiv.org/pdf/2608.18888v1
- DOI: https://doi.org/10.48550/arXiv.2608.18888

### Authors

Dinh Nam Pham, Shushen Manakhimova, Vivien Macketanz, Sebastian Möller

### Abstract

The rapid advancement of Natural Language Generation (NLG) has made the reliable evaluation of generated text increasingly critical, as these systems, such as large language models (LLMs), are now widely deployed in real-world applications. However, traditional automatic metrics fail to capture the multifaceted nature of perceived quality. In this paper, we introduce TextQ-German, a novel dataset suite for human-centered evaluation of German NLG from a Quality of Experience (QoE) perspective, covering automatic text summarization and machine translation. Through crowdsourcing studies with German speakers, we collect human quality ratings and identify relevant perceptual quality dimensions for each task. We develop automatic QoE prediction models, including transformer-based, linguistic feature-based, and hybrid approaches. Hybrid models outperform pure transformer baselines in almost all experimental settings, while linguistic features alone can approach the performance of fine-tuned language models. The dataset is extended with LLM-generated outputs annotated with overall QoE scores. Final validation on held-out sets indicates generalization to unseen data. Our work contributes a publicly accessible resource for NLG evaluation and baselines for automatic QoE prediction, providing a foundation for developing NLG systems that better align with human quality perception.

### 中文一句话结论
本文提出了TextQ-German数据集和混合预测模型，用于从体验质量角度评估德语自然语言生成文本，证明混合方法（结合语言特征与Transformer）在预测人类感知质量上优于纯Transformer基线。

### English TL;DR
This paper introduces TextQ-German, a dataset suite and automatic prediction models for assessing Quality of Experience in German natural language generation, demonstrating that hybrid approaches combining linguistic features with transformers outperform pure transformer baselines in predicting human-perceived quality.

### 中文详细总结
本文针对德语自然语言生成（NLG）任务中的文本质量评估问题，引入体验质量（QoE）视角。作者构建了TextQ-German数据集，涵盖自动文本摘要和机器翻译两个任务，并通过众包实验收集了人类对细粒度感知质量维度及总体质量的评分。基于该数据集，开发了三种自动QoE预测模型：纯Transformer模型、基于语言特征的模型以及混合模型。实验表明，在几乎所有设置下，混合模型优于纯Transformer基线，且仅使用语言特征即可接近微调语言模型的性能。数据集还扩展了由大语言模型生成并标注总体QoE分数的子集。在留出验证集上的结果显示出对未见数据的泛化能力。该工作提供了一个公开的NLG评估资源及自动QoE预测基线，为开发更符合人类质量感知的NLG系统奠定了基础。

### 方法 / 贡献
- 提出TextQ-German数据集，包含两个主要任务（自动文本摘要和机器翻译）的多个子集（原始语料、LLM扩展、验证集），并标注了细粒度质量维度及总体QoE分数。
- 通过众包实验识别并验证了德语NLG文本感知质量的相关维度。
- 开发了三种自动QoE预测模型：基于Transformer的模型、基于语言特征的模型以及混合模型（结合语言特征与Transformer）。
- 证明混合模型在几乎所有实验设置下优于纯Transformer基线，且语言特征单独使用可接近微调语言模型的性能。
- 公开数据集和基线，为德语NLG的人类中心评估提供资源。

### 实验或数据
- 数据集包括：TextQ-ATS（摘要语料）、TextQ-MT（翻译语料）及其对应的LLM生成扩展（TextQ-ATS-LLM、TextQ-MT-LLM）和最终验证集（TextQ-ATS-Val、TextQ-MT-Val）。
- 数据来源：摘要来自GeWiki语料及内部生成的多种提取式和抽象式摘要；翻译来自WMT19新闻翻译任务，涵盖不同排名系统。
- 众包实验：招募德语母语者，使用语义差异法（7点李克特量表）对质量维度（约20组形容词对）和总体QoE进行评分。
- 预测模型实验：比较纯Transformer、纯语言特征及混合模型的性能，并在留出验证集上测试泛化能力。

### 值得关注点
- 从用户中心视角（体验质量）而非传统自动指标出发评估NLG文本质量。
- 混合模型（双编码器结合语言特征与Transformer）显著优于纯Transformer基线，表明可解释的语言特征能有效补充深度表示。
- 数据集包含LLM生成文本的标注，扩展了对现代NLG系统的评估范围。
- 验证集结果证明模型对未见数据具有泛化能力。

### 局限性
- 仅专注于德语，是否适用于其他语言尚待验证。
- 仅涵盖自动文本摘要和机器翻译两个任务，未涉及问答、对话生成等其他NLG任务。
- 众包实验可能存在参与者注意力、文化背景等偏差，且评分过程要求忽略内容（可能不完全现实）。
- 自动预测模型仅基于有限数量的语言特征和Transformer架构，未探索更复杂的特征工程或最新大语言模型作为评估器。

## 3. Self-prompting and cross-model consensus enable reproducible data extraction from scientific literature with large language models

- Source: arxiv
- arXiv ID: 2608.19025
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.19025v1
- PDF: https://arxiv.org/pdf/2608.19025v1
- DOI: https://doi.org/10.48550/arXiv.2608.19025

### Authors

Valentin Romanov, Monique Bax, Steven Niederer

### Abstract

Accurately extracting nuanced, contextualized data from research articles is laborious and time intensive. Here, we investigate the performance of frontier, browser-based large language models (LLMs) to extract highly contextualized information. We demonstrate four escalating workflows, 1) given an expert curated prompt and research articles, most frontier LLMs perform well at data extraction, however can struggle with interpreting scientific context and nuance, 2) given simple instructions, LLMs can author their own prompts which were almost as eNective as expert-written prompts, 3) autonomous discovery of research literature was diNicult, agents either missed or hallucinated references, and 4) LLMs can create new datasets from published guidelines that closely match human-expert judges, but still require a human-in-the-loop. Together, these findings define an auditable division of labour in which experts specify the evidence standard, models cross-check repeated extractions and researchers resolve disputed cases, providing a practical route to scaling scientific data curation without relinquishing expert oversight.

### 中文一句话结论
本研究证明，前沿大语言模型在专家精心设计的提示和跨模型共识的指导下，可以从科学文献中以接近人类的精度提取数据，但在自主文献发现和处理科学细微语境时仍需人类监督。

### English TL;DR
This study demonstrates that frontier large language models can achieve near-human data extraction accuracy from scientific literature when guided by expert prompts and cross-model consensus, but still require human oversight for challenging contextual interpretation and autonomous literature discovery.

### 中文详细总结
本研究系统评估了七款前沿大语言模型（GPT-5.5、Opus 4.7、Gemini 3.1 Pro、Qwen3.7、Kimi K2.6、GLM-5.1和DeepSeek v4）从科学研究论文中提取高度情境化数据的性能。研究者设计了四种逐步增加模型自主性的工作流程：（1）使用专家精心设计的提示对固定论文语料进行提取；（2）让模型自行设计提示；（3）让深度研究代理自主完成文献发现和提取；（4）将前三个工作流的经验应用于全新领域的数据集创建。实验以心脏钙离子亲和力数据提取为案例，对18篇研究论文进行了系统评估。结果显示，顶级模型（GPT-5.5、Opus 4.7、Gemini 3.1 Pro）在专家提示下平均准确率达92.6%，其中GPT-5.5表现最佳（95.7%）。模型自建提示虽接近专家水平，但准确率平均下降5-32个百分点。自主文献发现方面，多数代理存在遗漏或幻觉参考文献的问题。最终，研究者提出了一种可审计的分工框架：专家指定证据标准，模型进行交叉验证提取，研究人员解决争议案例，从而在保持专家监督的同时实现科学数据整理的可扩展性。

### 方法 / 贡献
**方法**：研究者使用了七款通过浏览器界面访问的前沿大语言模型，设计了四种递增自主性的工作流程：1）专家提示的直接提取；2）模型自建提示；3）深度研究代理的自主工作流；4）基于已发表指南的全新数据集生成。每个提取任务重复五次以评估一致性。

**贡献**：1）系统性比较了多款前沿模型在复杂科学数据提取任务中的表现；2）提出并验证了"跨模型共识"机制，通过多模型、多次运行的交叉验证来识别提取错误；3）建立了可审计的人机协作分工框架，在不放弃专家监督的前提下实现大规模数据整理。

### 实验或数据
实验使用了18篇关于钙离子与心肌肌钙蛋白C结合亲和力的研究论文（可追溯至1980年代）作为基准数据集。评估了七项参数的提取准确性：物种、温度、肌钙蛋白制备方法、测量方法、镁离子浓度以及两个亲和力值（Kd和K）。每项提取重复五次，使用多数投票作为最终结果。数据集原始错误（如换算因子错误、温度记录不当）在跨模型对比中被自动识别。

### 值得关注点
1. **跨模型共识的实用价值**：多个模型同时偏离基准数据集的点，往往揭示了原始数据集中的真实错误，如错误的换算因子和温度记录。
2. **模型自建提示的有效性**：GPT-5.5自建提示的准确率仅比专家提示低5.3个百分点，显示LLM具备一定程度的自我指导能力。
3. **提取一致性挑战**：即使是最佳模型，也只有87.7%的参数在全部五次运行中返回正确结果，表明单次运行可能产生误导性结论。
4. **年代久远文献的处理困难**：1980年代论文中的不同命名规范和OCR导致的文本损坏（如图片中指数符号丢失）是主要的失败原因。

### 局限性
1. 自主文献发现（深度研究代理）表现不佳，多数代理遗漏或幻觉了参考文献，表明该功能尚不成熟。
2. 研究仅聚焦于一个特定领域（心脏钙离子结合数据），结果可能无法泛化到其他科学领域。
3. 模型自建提示需要用户提供意图描述和格式要求，并非完全自动化。
4. 所有提取任务最终仍需人类专家进行争议解决和最终验证，未能实现完全自动化。
5. 模型性能和排名可能随版本更新而变化，研究结果具有时效性。

## 4. Are LLMs Safe Beyond Text: Do Emojis Expose Gaps in Safety Evaluation

- Source: arxiv
- arXiv ID: 2608.18164
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.18164v1
- PDF: https://arxiv.org/pdf/2608.18164v1
- DOI: https://doi.org/10.48550/arXiv.2608.18164

### Authors

M P V S Gopinadh

### Abstract

Safety evaluations of large language models (LLMs) predominantly rely on text-based adversarial prompts, potentially overlooking vulnerabilities arising from alternative input representations. This work examines emoji-augmented prompts as a test case for this gap, evaluating 50 prompts across four open-source LLMs (Mistral 7B, Qwen 2 7B, Gemma 2 9B, Llama 3 8B). Results show substantial variation in robustness: Gemma 2 9B and Mistral 7B exhibit non-zero success rates (10%), Llama 3 8B 6%, while Qwen 2 7B shows complete resistance (0% success rate). A chi-square test ($χ^2 = 32.94, p < 0.001$) confirms significant differences in outcome distributions. These findings indicate that robustness is sensitive to input representation, and that evaluations restricted to standard text prompts may underrepresent model vulnerabilities.

### 中文一句话结论
在仅使用文本的安全性评估之外，采用表情符号增强的提示可以暴露大型语言模型（LLM）的隐藏漏洞，不同模型对此类非标准输入表现的鲁棒性存在显著差异。

### English TL;DR
This paper shows that emoji-augmented prompts can bypass safety mechanisms in some LLMs (e.g., Gemma 2 9B and Mistral 7B have 10% success rates), revealing that text-only safety evaluations may underrepresent model vulnerabilities.

### 中文详细总结
本研究通过表情符号增强的提示来检验LLM的安全漏洞。实验在四个开源LLM（Mistral 7B、Qwen 2 7B、Gemma 2 9B、Llama 3 8B）上进行，每个模型使用50个表情符号增强的提示进行测试。结果显示，模型在鲁棒性上表现出显著差异：Gemma 2 9B和Mistral 7B的成功率均为10%，Llama 3 8B的成功率为6%，而Qwen 2 7B完全抵抗（0%成功率）。卡方检验结果（χ² = 32.94，p < 0.001）验证了这些分布差异的统计显著性。研究强调，仅依赖文本提示的评估可能会低估LLM的脆弱性。

### 方法 / 贡献
- **方法**：构建50个表情符号增强的提示，通过两种策略（表情符号填充和表情符号链接）来干涉文本过滤机制。对四个开源LLM进行零样本评估，不使用微调或系统修改。响应分为三类：成功（生成受限内容）、部分（模棱两可）和失败（拒绝或无关）。
- **贡献**：揭示了基于表情符号的非标准输入可能绕过安全机制，展示了文本限制下的评估会低估模型风险，并为LLM安全评估提供了新视角。

### 实验或数据
- 使用四个模型，每个模型测试50个提示。
- 结果数据：
  - Gemma 2 9B：成功率10%，合规率66%
  - Mistral 7B：成功率10%，合规率86%
  - Llama 3 8B：成功率6%，合规率86%
  - Qwen 2 7B：成功率0%，合规率88%
- 统计检验：卡方检验χ² = 32.94，p < 0.001

### 值得关注点
- 不同模型对表情符号提示的脆弱性高度不一致，表明安全机制在非标准输入场景下存在泛化差异。
- 部分响应的高比例暗示安全系统在处理这些输入时未能一致地拒绝或合规，增加了潜在风险。
- 结果主张将表情符号等替代表示纳入常规安全评估中，以提高鲁棒性检测的全面性。

### 局限性
- 本工作未提及具体实验数据集的可用性（提示集因安全原因未公开）。
- 样本量较小（每个模型只有50个提示），可能限制了结论的泛化性。
- 评估仅限于四个开源模型和小范围提示，不覆盖商业模型或其他语言或文化中的表情符号用法。
- 没有对表情符号语义或编码差异进行深入分析，也没有探讨对抗性防御策略。

## 5. Aslema at NADI 2026: Augmentation through Fewshot for SLU

- Source: arxiv
- arXiv ID: 2608.18689
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.18689v1
- PDF: https://arxiv.org/pdf/2608.18689v1
- DOI: https://doi.org/10.48550/arXiv.2608.18689

### Authors

Tajwaar Shafiq, Hunzalah Hassan Bhatti, Shammur Absar Chowdhury, Firoj Alam

### Abstract

We present Aslema, our system for NADI 2026 Shared Task 5, which consists of two subtasks: intent recognition and slot filling. We evaluate four omni LLMs in a zero-shot setting and compare them with fine-tuned models. Our results show that fine-tuning consistently outperforms zero-shot inference. We further explore synthetic data augmentation by using an LLM to generate culturally grounded Tunisian Derja utterances, followed by voice cloning to generate synthetic speech. Incorporating this synthetic data improves performance on both tasks. Our final submitted system, based on Qwen3-Omni-30B and trained with a mixture of original and synthetic data, achieves 86.8% intent accuracy and 34.7 WER on the devtest split. On the official test set it ranks 1st in slot filling (59.5 CoER) and 4th among 8 teams in intent recognition (66.1% accuracy). We release our experimental scripts and will soon share the synthetic dataset to support further research in this area.

### 中文一句话结论
本文提出Aslema系统，通过LoRA微调音频大模型并结合LLM生成的突尼斯Derja语合成数据与语音克隆增强，在NADI 2026口语理解任务中取得槽填充第一名、意图识别第四名的成绩。

### English TL;DR
The paper introduces Aslema, a system for dialectal Arabic spoken language understanding that achieves top performance in slot filling and competitive results in intent recognition by combining LoRA fine-tuning of audio LLMs with synthetic data augmentation using LLM-generated Tunisian Derja utterances and voice cloning.

### 中文详细总结
- **动机与背景**：针对低资源突尼斯方言（Derja）的口语理解任务，评估音频大模型在零样本和微调下的表现，并探索合成数据增强的效果。
- **方法**：使用四个音频LLM（Qwen2.5-Omni-3B/7B、Qwen3-Omni-30B、Gemma-4-E4B）进行零样本和LoRA微调对比；利用LLM（Gemini）生成带槽位标注的Derja语句，再通过VoxCPM进行语音克隆合成语音，构建合成数据增强管道。
- **数据集**：SLURP-TN（突尼斯Derja版SLURP），训练集约2.8小时（2677句），验证集和开发测试集各约595/893句，存在严重类别不平衡（训练集仅21个意图，测试集有60个）。
- **结果**：最终系统基于Qwen3-Omni-30B，使用真实+合成数据混合训练，在开发测试集上意图准确率86.8%，WER 34.7；官方测试集上槽填充CoER 59.5（排名第一），意图识别准确率66.1%（排名第四/8队）。
- **贡献**：系统性评估音频LLM，提出LLM+TTS合成数据增强方法，释放实验脚本及合成数据集。

### 方法 / 贡献
- **系统评估**：对比四个音频LLM在零样本和LoRA微调下的意图识别与槽填充性能。
- **合成数据增强**：利用LLM生成突尼斯Derja话语（含槽位），结合VoxCPM语音克隆合成语音，过滤后获得约2.3万句合成数据。
- **最终系统**：选择Qwen3-Omni-30B，在真实+合成数据上微调两轮，提交至NADI 2026共享任务。
- **开源**：公开实验脚本，即将发布合成数据集。

### 实验或数据
- **数据**：SLURP-TN数据集，训练集2677句（2.78小时，21个意图，66.2%带槽位）；开发测试集893句；测试集989句（意图标签未公开）。
- **实验设置**：零样本与LoRA微调（冻结音频编码器）；合成数据生成采用Gemini 3.1 Pro/3.6 Flash，语音合成使用VoxCPM（含LoRA微调版本）；最终系统使用混合数据（真实2677句+合成约2.3万句）。
- **评估指标**：意图识别用准确率、加权F1、宏F1；槽填充用CoER、CVER、WER、CER。
- **主要结果**：微调一致优于零样本；合成数据单独使用优于零样本，混合真实数据达到最佳；官方测试集槽填充CoER 59.5（第一），意图识别准确率66.1%（第四）。

### 值得关注点
- **槽填充第一名**：在NADI 2026共享任务5的槽填充子任务中取得最高CoER（59.5）。
- **合成数据有效性**：通过LLM生成文化适配的Derja表述，结合语音克隆，有效提升低资源意图的性能。
- **开源贡献**：公开实验脚本和计划中的合成数据集，有助于低资源方言SLU研究。
- **跨模型对比**：系统评估了四个不同规模音频LLM，为后续工作提供参考。

### 局限性
- **数据集规模小且不平衡**：训练集仅约2.8小时，意图类别严重不平衡（训练集21个意图，测试集60个），影响模型泛化。
- **合成数据质量依赖**：合成数据生成依赖LLM和TTS的质量，过滤步骤可能仍存在噪声或方言不一致问题。
- **语音克隆限制**：VoxCPM语音克隆基于有限参考音频（152句零WER），可能无法覆盖所有发音变体。
- **评估范围有限**：仅针对突尼斯Derja方言，未验证其他方言或语言的迁移性。
- **未提及模型计算开销**：论文未详细分析LoRA微调及合成数据生成的计算成本。

## 6. Large Language Models in Mental Health: A Systematic Review of Applications, Innovations, and Ethical Challenges

- Source: arxiv
- arXiv ID: 2608.18080
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.18080v1
- PDF: https://arxiv.org/pdf/2608.18080v1
- DOI: https://doi.org/10.48550/arXiv.2608.18080

### Authors

Yisong Chen, Yifan Gao, Sijing Yu, Chuqing Zhao, Yang Lu

### Abstract

We present a review on the applications of large language models (LLMs) in health, e.g., social media analysis, clinical conversational agents, therapy support tools, prompt engineering, multimodal learning, and ethical considerations. We integrate findings from interdisciplinary studies utilizing diverse data sources such as social media posts, electronic medical records, and multimodal inputs to enable early detection of depression, suicide risk assessment, personalized therapy support, and psychoeducational content generation. Our review highlights advancements in LLM models and annotation strategies that enhance interpretability and clinical relevance, while we also emphasize the critical role of prompt engineering for domain adaptation. We also discuss emerging multimodal fusion techniques integrating text, speech, and sensor data for improved mental health diagnosis and monitoring. Finally, we address ongoing ethical, sociotechnical, and regulatory challenges, and advocate frameworks to ensure safe, equitable, and accountable deployment of LLMs in real-world mental health care.

### 中文一句话结论
该综述系统总结了大型语言模型在心理健康领域的应用、创新与伦理挑战，强调其在社交分析、临床对话和治疗支持中的潜力，并呼吁建立安全、公平的部署框架。

### English TL;DR
This systematic review examines the applications, innovations, and ethical challenges of large language models in mental health, covering social media analysis, clinical conversational agents, therapy support, prompt engineering, multimodal learning, and advocating for frameworks to ensure safe and equitable deployment.

### 中文详细总结
本文系统回顾了大型语言模型（LLMs）在心理健康中的三大应用领域：社交媒体分析、临床对话代理和治疗支持工具。通过整合来自社交媒体帖子、电子健康记录和多模态数据的研究，LLMs用于抑郁症早期检测、自杀风险评估、个性化治疗支持及心理教育内容生成。综述强调了模型和注释策略的进步（如专家标注、LLM辅助标注）提升了可解释性和临床相关性，并突出了提示工程在领域适应中的关键作用。此外，讨论了多模态融合技术（文本、语音、传感器）以改善诊断和监测，最后指出了伦理、社会技术和监管挑战，倡导负责任的部署框架。

### 方法 / 贡献
- **方法**：遵循PRISMA 2020指南，在IEEE Xplore、ACM Digital Library、PubMed等7个数据库进行系统检索，经筛选后纳入92篇高质量研究，采用结构化数据提取表评估模型架构、数据源、评价指标等。
- **贡献**：全面梳理了LLM在心理健康领域的应用进展（社交分析、临床对话、治疗支持），总结了创新方法（多模态融合、提示工程）和伦理挑战，并提出了未来研究和部署框架的建议。

### 实验或数据
该论文为系统综述，未进行原创实验。数据来源于对92篇实证研究的二次分析，涵盖社交媒体帖子、电子健康记录、咨询笔记、模拟对话、公开临床数据集以及多模态数据（文本、音频、图像、生理信号）等。

### 值得关注点
- 多模态融合技术（如结合文本、语音和传感器数据）在心理健康诊断和监测中的潜力。
- 提示工程对于LLM在心理健康领域适应性的关键作用。
- 专家标注与LLM辅助标注相结合的策略，改善了数据质量和模型可解释性。
- 明确了伦理、隐私责任和公平性方面的挑战，并倡导建立安全、公平的部署框架。

### 局限性
- 该综述依赖于已发表研究，可能受限于所选数据库的范围和语言（仅英文）。
- 纳入的原始研究存在数据集小、样本不平衡、临床验证有限等问题，导致综述结论的泛化性受限。
- 未对LLM应用的实际临床效果进行定量元分析，也未深入探讨不同模型间的性能对比。

## 7. Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck

- Source: arxiv
- arXiv ID: 2608.18931
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.18931v1
- PDF: https://arxiv.org/pdf/2608.18931v1
- DOI: https://doi.org/10.48550/arXiv.2608.18931

### Authors

Davide Romano, Kanak Raj, Jerrod Parker, Daniele Giofrè

### Abstract

Test-time scaling (TTS) improves language model outputs by spending additional inference compute - generating multiple candidates, searching over partial sequences, or iteratively refining drafts. These techniques yield large gains on mathematics and code, but have been developed and stress-tested almost exclusively on tasks where verification is straightforward. We conduct the first compute-normalised comparison of five TTS families across five open-ended generation benchmarks spanning medicine, law, finance, general chat, and creative writing - grounded in a unified framework that decomposes the effectiveness of each method's token budget into exploration and exploitation. The answer depends on which side of that decomposition you examine. Scaling exploration works: the best candidate in the pool improves steadily with compute across all settings. What breaks is exploitation - the step that converts a rich candidate pool into a final output. With state-of-the-art generators, reward models correlate at only $ρ_v \approx 0.12$ with true quality, rendering selection near-random regardless of budget. Tree search amplifies this failure through diversity collapse. Refinement helps on one of five benchmarks; its apparent gains elsewhere are confounded. Only synthesis across candidates (Fusion) consistently improves over single-sample baselines, yet still recovers only ~40% of available quality. The candidate pool is not the bottleneck - choosing from it is.

### 中文一句话结论
本文发现，在开放式生成任务中，测试时扩展的瓶颈不是探索（生成多样化候选），而是利用（从候选池中选择最佳输出），因为奖励模型与真实质量的相关性极低（约0.12），即使最好的融合方法也只能恢复约40%的可用质量。

### English TL;DR
This paper identifies that in open-ended generation tasks, test-time scaling's bottleneck is not exploration (generating diverse candidates) but exploitation (selecting the best output), as reward models correlate weakly with true quality (ρ_v ≈ 0.12) and existing methods recover only ~40% of available quality.

### 中文详细总结
本文首次对五种测试时扩展（TTS）方法在五个开放式生成基准（医学、法律、金融、通用聊天、创意写作）上进行了计算归一化比较。研究将TTS方法的token预算分解为探索（生成候选）和利用（选择或合成最终输出）。主要发现：探索是有效的——候选池中最佳候选的质量随计算量增加而稳定提升；但利用环节存在瓶颈——基于奖励模型的选择由于模型与真实质量相关性仅约0.12而近乎随机；树搜索因多样性崩溃进一步恶化；改进（Refinement）仅在一个基准上有效，其他情况下的收益被混淆；只有融合（Fusion）方法能一致地超越单样本基线，但仅恢复约40%的可用质量。此外，作者提出了偏差纠正的oracle估计器，并验证了验证器相关性可预测BoN的头部空间捕获率。

### 方法 / 贡献
- 提出统一的框架，将TTS方法的token预算分解为探索和利用。
- 推导出偏差纠正的oracle估计器，修正了噪声评分带来的max膨胀。
- 证明BoN的头部空间捕获率约等于验证器与真实质量的相关性。
- 首次在开放式生成任务上系统比较五种TTS家族（BoN、Beam Search、Particle Filtering、Refinement、Fusion），并诊断各方法的利用失败原因。

### 实验或数据
使用五个开放式生成基准测试：LEXam（法律，516例）、HealthBench（医学，5000例）、PRBench（金融/法律，1650例）、WildBench（通用聊天，1024例）、WritingBench（创意写作）。所有方法在匹配的计算预算下比较，采用真实质量评分（专家评判或参考指导）进行评估。实验证实探索效果随计算量提升，但利用环节（尤其是基于验证器的选择）失败。

### 值得关注点
- 核心发现：利用是瓶颈，而非探索。这挑战了测试时扩展研究对奖励模型依赖的普遍假设。
- 验证器相关性极低（约0.12）表明现有奖励模型不适用于开放式生成任务。
- 只有融合方法能一致提升性能，但仍仅恢复约40%的可用质量，暗示进一步的提升空间来自改进利用机制。
- 偏差纠正的oracle估计器具有实用价值，可用于更准确地评估候选池质量。

### 局限性
- 研究仅限于五种固定TTS方法，未涵盖所有变体（如混合方法或扩展思维）。
- 使用固定的生成模型和奖励模型，结论可能不适用于其他模型或训练方式。
- 融合方法虽然最佳，但仅恢复部分质量，且其机制未完全解释。
- 实验基于现有基准，可能不代表所有开放式生成任务（如对话、多模态）。

## 8. TranslatePsy-AfriSLM: High-Quality Data Scaling For Low-Resource Machine Translation

- Source: arxiv
- arXiv ID: 2608.18655
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.18655v1
- PDF: https://arxiv.org/pdf/2608.18655v1
- DOI: https://doi.org/10.48550/arXiv.2608.18655

### Authors

Milan Gritta, Patrik Lambert, Jihye Back, Amril Nazir

### Abstract

The rapid progress in Artificial Intelligence has largely bypassed African languages, creating a digital divide that limits AI adoption on the continent. Recent open-source LLMs systematically underperform on African machine translation, while the lack of large-scale, high-quality, open-source parallel data has constrained the development of competitive small language models (SLMs). We introduce *TranslatePsy-AfriSLM*, a collection of open-source MT resources for 19 Sub-Saharan African languages, including curated parallel data, African-specialized synthetic data, and a family of fine-tuned SLMs. Our empirical study shows that unified quality-estimation filtering removes up to 96% of training tokens without degrading quality, and that filtered synthetic data dominates the quality-efficiency Pareto frontier. Fine-tuned on the resulting data mixture, TranslatePsy-AfriSLM outperforms substantially larger systems, including TranslateGemma-27B and Qwen3.5-122B-A10B, with as few as 0.8B parameters.

### 中文一句话结论  
本文提出 **TranslatePsy-AfriSLM**，通过统一质量估计过滤（移除高达 96% 的训练 token）和合成数据增强，用 0.8B 参数的 SLM 超越了 TranslateGemma-27B 和 Qwen3.5-122B-A10B 等大型模型在 19 种撒哈拉以南非洲语言上的翻译性能。

### English TL;DR  
TranslatePsy-AfriSLM introduces open-source MT data and small language models for 19 Sub-Saharan African languages, showing that unified quality-estimation filtering can remove up to 96% of training tokens while synthetic data drives quality, enabling 0.8B-parameter models to outperform far larger systems like TranslateGemma-27B and Qwen3.5-122B-A10B.

### 中文详细总结  
- **背景**：现有开源 LLM 在非洲语言机器翻译上系统性表现不佳，且缺乏大规模高质量开源平行数据，限制了 SLM 的发展。  
- **贡献**：构建了包含 19 种非洲语言的资源集合，包括精选平行数据、非洲专用合成数据及系列微调 SLM。  
- **关键发现**：统一质量估计（Unified QE）通过计算 AfriCOMET、SSA-COMET、MetricX 的稳健 z 分数均值，可移除 96% 的低质量训练 token 而不降低翻译质量；合成数据在质量-效率帕累托前沿上占主导地位。  
- **性能**：微调后的 0.8B 参数模型（基于 Qwen3.5）在 SSA-COMET 评分上超越 TranslateGemma-27B 和 Qwen3.5-122B-A10B，且保持对话能力。  
- **数据管道**：从 OPUS、MALA、WMT22、Fine Translations 收集约 4.27 亿原始句对；使用 NLLB-3.3B 翻译 MADLAD-400 单语数据生成合成数据；经统一 QE 过滤、TopN 和双向扩展等策略处理后得到最终训练混合。

### 方法 / 贡献  
1. **统一质量估计（Unified QE）**：将 AfriCOMET、SSA-COMET 和 MetricX 的分数通过稳健 z 分数归一化（以 Human Mix 为标尺）后求平均，统一评价标准，避免单一指标偏向。  
2. **数据过滤策略**：研究阈值、TopN 和双向扩展对数据量的影响，发现过滤可移除大部分噪声，且合成数据驱动质量提升。  
3. **模型与训练**：基于 Qwen3.5 进行全参数 SFT（1 轮），同时引入 Instruct Mix 和 Asia-Europe Mix 以保持多语言翻译能力。  
4. **开源资源**：发布 19 种非洲语言的平行数据、合成数据及微调模型，填补低资源场景下高质量数据的空白。

### 实验或数据  
- **数据源**：平行数据来自 OPUS、MALA、WMT22、Fine Translations（约 4.27 亿原始句对）；单语数据使用 MADLAD-400；合成数据由 NLLB-3.3B 翻译生成。  
- **评估基准**：Flores-200（1,012 条）、BOUQuET（854 条）和 Smol 数据集，采用 SSA-COMET 等指标。  
- **主要结果**：0.8B 参数模型在 BOUQuET 上超越 TranslateGemma-27B 和 Qwen3.5-122B-A10B；统一 QE 过滤可移除 96% token 而不降质；合成数据在效果-效率上占优。  
- **额外实验**：通过 Africa-IID（19 种语言）和 Africa-OOD（8 种未见语言）评估泛化能力。

### 值得关注点  
- **高效过滤**：统一 QE 能移除 96% 的 token，极大降低训练成本同时保持质量。  
- **小模型碾压大模型**：0.8B 参数超越 27B 甚至 122B 模型，验证数据质量和筛选策略的重要性。  
- **合成数据价值**：针对低资源语言，合成数据主导帕累托前沿，显著优于纯自然语料。  
- **开源与落地意义**：直接促进非洲语言数字包容性，降低 AI 应用门槛。

### 局限性  
- 论文未明确讨论自身局限性，但根据内容可推断：  
  - 仅覆盖 19 种撒哈拉以南非洲语言，未包含其他非洲语言（如北部非洲阿拉伯语方言等）。  
  - 合成数据依赖 NLLB-3.3B 作为教师模型，可能继承其偏差或错误。  
  - 统一 QE 需要多个模型打分，计算开销较高。  
  - 对数据源的选择和阈值设定高度依赖 Human Mix 的标定，而 Human Mix 规模较小（~352K 句对）。  
  - 未见语言泛化性能未详细分析（仅提及 Africa-OOD 评估，未报告具体结果）。

## 9. When Do LLMs Actually Help? Evaluating LLMs as Data Quality Annotators

- Source: arxiv
- arXiv ID: 2608.18158
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.18158v1
- PDF: https://arxiv.org/pdf/2608.18158v1
- DOI: https://doi.org/10.48550/arXiv.2608.18158

### Authors

Praphulla Lal Shrestha

### Abstract

LLMs have been increasingly used to catch data quality issues automatically, but we know very little about how consistent these judgments actually are. This study tests an LLM on two e-commerce data quality tasks, entity matching and brand mislabeling, against rule based baselines and human verified ground truth, under both zero-shot and few-shot prompting. On entity matching while using the Abt Buy benchmark (2,194 labeled pairs), a simple rule based baseline (F1=0.950) performed about as well as LLM zero shot prompting (F1=0.948). Moreover, a few-shot prompt revision that looked effective on a small validation sample reduced full-scale performance to F1=0.914. This showed that small sample prompt evaluation can be misleading. On brand mislabeling detection, using 500 Amazon product listings with synthetically injected labeling errors, the LLM clearly outperformed a naive rule based baseline (F1=0.833 vs 0.721), because it could draw on background knowledge of brand product relationships that a simple rule could not access. Testing consistency across repeated runs (200 pairs, 5 runs at temperature 0.7) showed the model agreeing with itself 99.7% of the time on average, with 99% of pairs giving identical answers across all 5 runs. Using majority voting across these runs only improved F1 by 0.005, at 5 times the inference cost. These results suggest that the value of using an LLM over traditional methods depends heavily on the task. LLMs offer little advantage when strong lexical signals already exist, but a clear advantage when the task requires background knowledge, all while remaining highly consistent across repeated queries.

### 中文一句话结论
LLM 在数据质量标注中的价值高度依赖任务：实体匹配任务中与简单规则基线相当（F1≈0.95），但背景知识驱动的品牌误标任务中显著优于规则（F1=0.833 vs 0.721），且多次运行一致性极高（99.7%），但小样本提示优化可能误导全量性能。

### English TL;DR
This paper evaluates LLMs as data quality annotators on two e-commerce tasks, finding that they offer little advantage over simple rule-based methods when strong lexical signals exist (entity matching, F1 ≈ 0.95) but significantly outperform when tasks require background knowledge (brand mislabeling, F1=0.833 vs 0.721), while maintaining high consistency across repeated runs.

### 中文详细总结
本研究评估了 LLM（GPT-4o-mini）在两项电商数据质量任务中的表现：实体匹配（Abt-Buy 基准，2,194 对标注）和品牌误标检测（500 个 Amazon 产品列表，合成注入错误）。与规则基线对比发现：
- **实体匹配**：零样本 LLM（F1=0.948）与简单 Jaccard 相似度规则基线（F1=0.950）性能相当。少样本提示（强调 SKU/代码）在小样本验证中表现良好，但全量测试时 F1 降至 0.914，说明小样本评估可能误导。
- **品牌误标检测**：LLM 零样本（F1=0.833）显著优于 naive 子串匹配规则（F1=0.721），因为 LLM 能利用品牌-产品关系的背景知识处理缩写、子公司等非字面匹配情况。
- **一致性测试**（200 对样本，温度 0.7，5 次运行）：模型自我一致性达 99.7%，多数投票仅提升 F1 0.005，但成本增加 5 倍。
- 主要结论：LLM 在需要语义或背景知识时优势明显，但存在强词汇信号时优势有限；小样本提示优化需谨慎验证。

### 方法 / 贡献
- **方法**：使用 GPT-4o-mini，在实体匹配和品牌误标上分别采用零样本/少样本提示，与规则基线（Jaccard 相似度、子串检查）对比；通过 5 次重复运行（温度 0.7）评估一致性。
- **贡献**：实证揭示 LLM 数据质量标注的优势取决于任务特性（词汇 vs 知识驱动）；发现小样本提示优化可能夸大全量性能；量化了 LLM 的多次运行一致性及其对多数投票的边际收益。

### 实验或数据
- **实体匹配**：Abt-Buy 基准，2,194 对标注（正负平衡），规则基线 F1=0.950，LLM 零样本 F1=0.948，少样本变体 F1=0.914。
- **品牌误标检测**：500 个 Amazon 产品列表，人工合成半数标签错误，LLM 零样本 F1=0.833，规则基线 F1=0.721。
- **一致性实验**：200 对实体匹配子样本，5 次重复运行（温度 0.7），平均一致率 99.7%，多数投票仅提升 F1 0.005。
- 所有实验使用精确率、召回率、F1、准确率评估。

### 值得关注点
1. LLM 在品牌误标任务中超越规则，得益于背景知识（如“Zone Labs”与“ZoneAlarm”的关系），规则无法处理缩写或子公司。
2. 少样本提示在小样本验证中看似有效（修复 28/67 错误，仅破坏 1/50 控制），但全量测试 F1 下降 0.034，提示小样本评估可能误导。
3. 一致性极高（99.7%），但多数投票提升微乎其微，性价比低。
4. 实体匹配任务中，LLM 与规则错误模式互补：LLM 擅长低词汇重叠但语义等价的情况，规则擅长精确代码匹配。

### 局限性
- Abt-Buy 数据集名称结构较一致，结果可能不推广到更嘈杂的真实数据。
- 品牌误标地面真值通过随机制造商交换合成，可能产生明显不合理的错误，而非实际中的细微错误。
- 仅评估了 GPT-4o-mini，其他模型或尺寸的可靠性及相对优势可能不同。
- 一致性测试仅在实体匹配任务上进行，品牌误标任务的运行间可靠性未测试。
- 两项任务均作为独立成对/成行分类评估，未考虑相关记录间的一致性。
- 零样本提示为通用提示，未针对产品类别或属性类型定制；近期工作显示类别特定提示可显著提升性能，因此本研究结果可能低估 LLM 潜力。

## 10. Learning What to Fail On: Failure-Mode Contextual Bandits for Adversarial Data Curation

- Source: arxiv
- arXiv ID: 2608.18681
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.18681v1
- PDF: https://arxiv.org/pdf/2608.18681v1
- DOI: https://doi.org/10.48550/arXiv.2608.18681

### Authors

Roie Kazoom, Ofir Cohen, Rami Puzis, Asaf Shabtai, Ofer Hadar

### Abstract

We introduce a failure-aware adversarial retrieval-augmented framework for improving robustness in natural language understanding. Rather than selecting synthetic examples with a fixed reward threshold, our method formulates adversarial data curation as a failure-mode contextual bandit problem. Candidate examples are generated with retrieval-augmented prompting, filtered by the current target model, automatically validated by an LLM judge ensemble, and clustered into recurring failure modes. A stochastic policy then selects which failure modes to sample for retraining, and is updated using validation-based reward that balances robustness gains, forgetting, and data cost. This makes the data curator itself the learning agent, enabling adaptive selection of the most useful model failures across training rounds. On standard benchmarks, our approach improves RoBERTa-base accuracy from 88.48% to 92.60% on SNLI, from 75.04% to 80.95% on ANLI, and from 54.67% to 71.99% on MultiNLI, while consistently outperforming prior adversarial augmentation methods. We further demonstrate transfer to FEVER fact verification, achieving up to 79.86\% FEVER score and 82.45\% accuracy with RoBERTa-large. Finally, we provide a theoretical interpretation showing that, under stated assumptions, failure-mode sampling can reduce shortcut-aligned gradient contributions while inducing bounded distributional drift. By combining retrieval, automated validation, contextual-bandit failure selection, and controlled adversarial retraining, our framework enables scalable robustness improvement without additional human annotation.

### 中文一句话结论
本文提出一种基于失败模式上下文赌博机（Failure-Mode Contextual Bandit）的自适应对抗数据挑选方法，通过检索增强生成候选样本、LLM 裁判自动验证、失败模式聚类以及随机策略动态选择，显著提升自然语言理解模型的鲁棒性，在多个基准上取得大幅改进。

### English TL;DR
This paper introduces a failure-mode contextual bandit framework for adversarial data curation that adaptively selects the most useful model failures for retraining to significantly improve robustness in natural language understanding.

### 中文详细总结
该工作针对自然语言理解中的鲁棒性问题，提出一种新的对抗数据筛选框架。核心思想是将数据筛选过程建模为失败模式上下文赌博机问题：首先利用检索增强提示生成候选对抗样本，经当前目标模型过滤、LLM 裁判集成自动验证后，将样本聚类为重复出现的失败模式；然后由一个随机策略（数据策展器自身即为学习智能体）选择哪些失败模式用于重训练，并根据验证集的奖励（权衡鲁棒性提升、遗忘和数据成本）更新策略。在 SNLI、ANLI、MultiNLI 上，RoBERTa-base 的准确率分别从 88.48%、75.04%、54.67% 提升至 92.60%、80.95%、71.99%，且持续优于先前对抗增强方法；在 FEVER 事实验证任务上，RoBERTa-large 达到 79.86% FEVER 分数和 82.45% 准确率。理论上，在给定假设下，失败模式采样可减少捷径对齐的梯度贡献，同时引起有界分布漂移。整个框架无需额外人工标注即可实现可扩展的鲁棒性改进。

### 方法 / 贡献
1. **方法**：将对抗数据挑选转化为失败模式上下文赌博机问题；步骤包括 (a) 检索增强生成候选样本，(b) 当前模型过滤 + LLM 裁判自动验证，(c) 失败模式聚类，(d) 随机策略选择失败模式以重训练，(e) 验证集奖励（平衡鲁棒性提升、遗忘和数据成本）更新策略。
2. **贡献**：提出首个数据策展器作为学习智能体的自适应失败模式选择框架；在多个 NLU 基准上取得显著且一致的改进；提供理论解释，说明该方法可减少捷径梯度贡献并保持有界分布漂移。

### 实验或数据
实验在三个 NLI 基准（SNLI、ANLI、MultiNLI）上使用 RoBERTa-base 评估，并在 FEVER 事实验证任务上用 RoBERTa-large 进行迁移验证。报告了准确率和 FEVER 分数，并与先前的对抗增强方法对比。摘要未提及具体的数据集划分或统计细节，但给出了性能数字。

### 值得关注点
1. 数据策展器本身成为学习智能体，可跨训练轮次自适应选择最有效的失败模式，而非固定阈值。
2. 结合检索增强生成、LLM 自动验证和聚类，自动化程度高，无需人工标注。
3. 在 SNLI、ANLI、MultiNLI 和 FEVER 上均大幅超越先前对抗增强方法，效果显著。
4. 提供理论支撑，说明失败模式采样对梯度分布和分布漂移的影响。

### 局限性
根据摘要，未明确讨论具体局限性。不过，方法依赖 LLM 裁判集成的自动验证质量和失败模式聚类的有效性，理论分析基于特定假设，实际部署中可能受限于这些条件。

## Processing Notes

- Duplicate papers skipped: 0