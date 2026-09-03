# Daily arXiv - 2026-09-03

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-03T00:25:49
- Paper count: 10

## 1. Some Emotions Run Deeper: Layer-wise Probing and Causal Intervention in Large Language Models

- Source: arxiv
- arXiv ID: 2609.01279
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.01279v1
- PDF: https://arxiv.org/pdf/2609.01279v1
- DOI: https://doi.org/10.48550/arXiv.2609.01279

### Authors

Tian Fang, Gaël Guibon, Davide Buscaldi

### Abstract

Emotion is expressed in text along a wide spectrum, from surface lexical cues to inferences entangled with content. Most layer-wise analyses of emotion in LLMs use a single corpus, leaving open whether the depth at which emotion becomes accessible is a property of the model or also of the text source. We investigate this across three datasets spanning different degrees of explicitness and contextualization in emotion expression (Twitter posts, Reddit comments, and autobiographical narratives) and eight 1B--9B open-weight LLMs from the Llama, Qwen, and Granite families. We combine layer-wise probing with offline feature scaling and online forward interventions, transfer analyses, and an early-exit classifier. We find that (i) the best probing layer shifts systematically across corpora, from input-adjacent layers to over half model depth, and this ordering persists after matching label-by-length-bin distributions; (ii) across the evaluated settings, forward-pass interventions on probe-selected bands reduce test accuracy by 5--6 points more than same-width random bands ($q < 0.01$); (iii) selected bands transfer across datasets and emotion categories, suggesting partially shared affective information rather than strictly per-emotion substrates; and (iv) probe-selected early-exit representations outperform full-depth exits by $6.9$ percentage points on average.

### 中文一句话结论  
大语言模型中情感信息的线性可解码深度因文本来源的显式程度而异：短社交帖子浅层解码，自传体叙事深层解码，且探针选中的层对情感读出具因果作用。

### English TL;DR  
The paper shows that the depth at which emotion information becomes linearly decodable in large language models varies systematically with the explicitness of the text source, and that probe-selected layers are causally involved in emotion readout and enable more accurate early-exit classification than full-depth representations.

### 中文详细总结  
本研究通过层探针和因果干预，系统分析了三种不同显式程度的情感语料（Twitter帖子的显式情感、Reddit评论的中等隐式、自传体叙事的深度隐式）在8个1B-9B开源LLM（Llama、Qwen、Granite家族）中的内部表征。主要发现：  
- 最佳探针层随语料源从输入邻近层（Emotion）到过半深度（ISEAR）系统性迁移，且长度匹配后顺序不变。  
- 对探针选中层的正向干预比随机层降低测试精度5-6个百分点（q<0.01），表明这些层因果参与情感读出。  
- 选中的层带可在数据集和情感类别间迁移，说明情感信息部分共享而非严格独立。  
- 探针选中的早期退出表征平均比全深度退出高6.9个百分点的准确率。  
组合了层探针、离线特征缩放、在线正向干预、迁移分析和早期退出分类器。

### 方法 / 贡献  
- 采用线性探针（逻辑回归）加固定非参数池化（拼接均值、最大值、最小值）的方法，逐层定位情感信息的线性可解码性。  
- 采用离线特征缩放和在线前向干预（扰动选中层带）验证探针选定层的因果相关性，而非仅诊断性。  
- 引入跨数据集和跨情感类别的迁移分析，检验情感表征的共享程度。  
- 使用探针选定的早期退出机制，验证在减少模型深度的情况下仍能取得优于全深度退出的性能。  
- 主要贡献：证明了情感信息深度强烈依赖文本源风格，而非仅模型固有性质；提供了因果干预证据；发现了情感表征的部分跨域共享性。

### 实验或数据  
- **数据集**: Emotion（Twitter，6类，限制为4类）、GoEmotions（Reddit，27类，限制为4类）、ISEAR（自传体叙事，7类，限制为4类）；只保留恐惧、喜悦、愤怒、悲伤共同标签，切分后训练/验证/测试规模见表1。  
- **模型**: 8个开源解码器仅LLM：Llama-3.2-1B/3B-Instruct、Llama-3.1-8B-Instruct；Qwen-3.5-2B/4B/9B；Granite-4.1-3B/8B。  
- **探针设置**: 固定StandardScaler+LogisticRegression (C=1.0)，每层训练分类器并评估验证集F1，报告归一化深度。  
- **干预实验**: 对探针选定的连续层带进行正向干预（扰动），与同宽度随机层带比较测试精度下降差异。  
- **早期退出**: 在探针选定层带处截断，使用线性探针分类与全深度退出对比。

### 值得关注点  
1. **深度依赖文本源**: 短推特显式情感极浅（均值归一化深度0.066），Reddit评论中等（0.219），自传叙事很深（0.590），排序在长度匹配后仍保持。  
2. **因果角色**: 探针选中的层带被扰动后比随机层带造成更大精度下降（平均5-6 points），证明其情感读出的因果参与。  
3. **迁移性**: 探针选定层带可在不同数据集和情感类别间迁移（干预设置下更强），表明存在部分共享的情感信息基础。  
4. **早期退出优势**: 仅使用探针选定的层带（而非全模型）即可获得更优的分类性能（+6.9%），兼具效率与精度。

### 局限性  
- 仅研究四个基本情感（恐惧、喜悦、愤怒、悲伤），未覆盖更细粒或复杂情感（如羞愧、嫉妒）。  
- 语料仅限于英语，结论可能不推广到其他语言或文化情感表达。  
- 模型仅覆盖8个1B-9B开源LLM（Llama、Qwen、Granite），未包含更大规模或封闭模型。  
- 探针和干预设置基于线性分类器，可能遗漏非线性可解码信息。  
- 未探讨情感信息的表示是否与模型其他能力（如推理、事实）共享底层机制。

## 2. Prompt-Robust Language Models: Which Training Strategies Work?

- Source: arxiv
- arXiv ID: 2609.01217
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.01217v1
- PDF: https://arxiv.org/pdf/2609.01217v1
- DOI: https://doi.org/10.48550/arXiv.2609.01217

### Authors

Frederic Sadrieh, Michal Štefánik

### Abstract

Despite their strong performance, large language models remain highly sensitive to prompt formulation. Prior work addresses this through refined data construction or through dedicated robustness objectives. We reproduce and compare these strategies under controlled conditions, and measure how effective they are in addressing models' prompt sensitivity. We find the current robustness fine-tuning methods improve over standard fine-tuning and in-context learning, but the best-to-worst prompt gap remains as high as 40-57% of performance. Moreover, the recent robustness-enhancing methods we test - CoIN for contrastive alignment and PPCL for consistency regularization - often fail to outperform the simplest data construction strategy: training on one template per batch. Our diagnostics explain these results. The auxiliary objectives move the quantity they penalize, but do not generalize beyond it. Additionally, data construction strategies differ due to the conflicting signs of per-template gradients on 57-64% of parameters. Thus, batches that mix formulations force the optimizer to reconcile competing updates instead of finding a shared, prompt-agnostic one.

### 中文一句话结论
本研究系统比较了提升大语言模型提示鲁棒性的训练策略，发现虽然鲁棒性微调优于标准方法，但最佳与最差提示之间的性能差距仍然高达40–57%，且复杂的鲁棒性方法（如CoIN和PPCL）往往不如简单的数据构造策略（如每批次仅用一个模板）。

### English TL;DR
This study systematically compares prompt robustness training strategies for large language models and finds that while robustness fine-tuning improves over standard methods, the best-to-worst prompt gap remains large (40-57%) and sophisticated approaches like CoIN and PPCL often fail to outperform simple data construction strategies such as training on one template per batch.

### 中文详细总结
论文针对大语言模型对提示表述高度敏感的问题，在受控条件下复现并比较了三种类别的训练时鲁棒性方法：（1）数据构造策略（如每批次单模板、全混合、全模板同批次等）；（2）一致性正则化方法PPCL；（3）对比对齐方法CoIN。实验使用四个基础模型（Llama3.2-1B、Llama3.1-8B、Qwen3-0.6B、Qwen3-8B），在48个训练数据集和11个测试数据集上进行评估。结果表明，所有多提示微调方法均优于标准单提示微调和上下文学习，但最佳与最差提示之间的性能差距仍然高达40–57%。更关键的发现是，PPCL和CoIN等复杂方法并未持续优于最简单的数据构造策略——每批次仅用一个模板（One-at-a-Time）。梯度分析揭示了原因：不同模板的梯度在57–64%的参数上存在符号冲突，导致全模板同批次训练时优化器被迫调和矛盾更新，而非找到共享的、与提示无关的更新方向。附加的鲁棒性目标虽然能惩罚特定指标，但无法泛化到其他扰动。

### 方法 / 贡献
- **方法分类**：论文系统比较了三类训练时鲁棒性策略——数据构造（四种批次构建方式）、一致性正则化（PPCL）、对比对齐（CoIN）。
- **主要贡献**：
  1. 在受控条件下首次系统比较三类方法，并追踪了梯度空间中的模板干扰现象（每模板梯度在57–64%参数上符号冲突）。
  2. 复现CoIN和PPCL，发现它们未能可靠优于简单数据构造策略，并诊断出其损失目标无法泛化的原因。
  3. 指出现有训练时鲁棒性方法的性能上限：最佳与最差提示差距仍达40–57%。

### 实验或数据
- **模型**：使用两个模型家族（Llama3.2-1B、Llama3.1-8B；Qwen3-0.6B、Qwen3-8B）的基础版本，8B模型采用LoRA以减少计算成本。
- **数据集**：复制自T0设置，训练集48个数据集，测试集11个未见任务数据集。使用PromptSource模板集合，涵盖释义和结构变化。每个数据集最多10,240个训练样本，仅保留至少一个模板的数据集。
- **评估指标**：以Rouge-L为主，报告平均、最佳和最差模板性能；使用统计显著性检验（bootstrap检验，α=0.05）确定最佳运行组。
- **关键结果**：多提示IFT方法普遍提升所有指标，但最差模板提升有限；One-at-a-Time策略在较小模型上表现一致最佳，而All-in-One-Batch因梯度冲突降低鲁棒性。

### 值得关注点
- **梯度冲突**：不同模板的更新向量方向不一致，平均余弦相似度仅0.54，57–64%的参数更新符号相反，这解释了全模板同批次训练效果不佳的原因。
- **简单策略胜出**：最简单的数据构造策略（每批次仅用一个模板）持续优于或等效于复杂方法（CoIN、PPCL），提示当前鲁棒性目标的额外复杂性未带来显著增益。
- **模型规模影响**：小模型（1B）对提示变化极为敏感；大模型（8B）鲁棒性差异更大，但Llama3.1-8B的方差较低，且部分多提示方法反而降低了最差模板性能。
- **鲁棒性上限**：即使采用最佳训练策略，模型对提示表述的敏感性仍不可忽视（40–57%的差距），表明现有方法尚未根本解决该问题。

### 局限性
- 研究仅测试了基础模型（非经过指令微调或RLHF的版本），结果可能不直接适用于已对齐模型。
- 鲁棒性方法（CoIN和PPCL）未能超越简单数据构造，但其失效原因可能部分源于超参数或实现细节（如学习率扫描范围有限）。
- 评估仅覆盖11个测试数据集，且模板类型限于释义和结构变化，未涉及更极端的提示扰动（如任务替换或噪声注入）。
- 性能差距（40–57%）仍然较大，说明当前训练时方法无法彻底消除提示敏感性，需要更根本的解决方案。
- 计算成本方面，多模板训练需要更多训练步数或更长训练时间，但论文未提供详细的效率对比。

## 3. From Confusion to Clarity: Confusion-Aware Retrieval and Knowledge Injection for Text Classification

- Source: arxiv
- arXiv ID: 2609.01564
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.01564v1
- PDF: https://arxiv.org/pdf/2609.01564v1
- DOI: https://doi.org/10.48550/arXiv.2609.01564

### Authors

Manish Gupta, Chaitanya Giri, Jayasimha Talur

### Abstract

Large language models (LLMs) struggle to classify text into taxonomies with many semantically similar labels, as the distinctions are domain-specific and not captured by pre-training. To handle large label spaces, a common approach retrieves top-$K$ candidate labels by embedding similarity and prompt the LLM to choose among them. However, top-$K$ retrieval reduces the number of candidates but does not help the model tell similar ones apart. When two similar labels both appear as candidates, the model lacks the signal to choose correctly between them. We propose a framework that (1) identifies which label pairs the model struggles to distinguish, (2) expands the candidate set to include confusable labels, and (3) generates targeted rules to differentiate between similar candidates. The framework requires no fine-tuning, and the generated rules transfer to smaller, cheaper models. On three benchmarks (WOS, Flipkart, LEDGAR), our approach improves Macro F1 by up to 10.0pp over retrieval baselines, with smaller models (2B--20B) gaining up to 11.5pp via cross-model transfer.

### 中文一句话结论
本文提出一种无需微调的混淆感知框架，通过识别LLM易混淆的标签对、扩展候选集并生成针对性区分规则，在三个基准测试中将Macro F1最高提升10个百分点。

### English TL;DR
This paper proposes a confusion-aware, fine-tuning-free framework that identifies confusing label pairs based on model errors, augments these pairs in the candidate set, and injects automatically generated targeted disambiguation rules. On three benchmarks (WOS, Flipkart, LEDGAR), it achieves up to 10.0pp Macro F1 improvement over retrieval baselines, and rules generated by a large model transfer to smaller models (2B-20B) with up to 11.5pp gain.

### 中文详细总结
大型语言模型（LLM）在标签空间大且语义相似的文本分类任务中表现不佳，传统基于检索的候选标签方法虽能缩小范围，但无法帮助模型区分相似标签。本文提出**混淆感知知识增强分类框架**：第一步，通过分析分类器在训练集上的混淆矩阵，识别模型易混淆的标签对；第二步，在推理时自动将混淆伙伴标签加入候选集，确保正确的标签对同时出现；第三步，利用三阶段管线（单样本推理、合并、双向合并）生成目标性区分规则，将规则注入提示中帮助模型做出正确选择。无需微调，且大模型生成的规则可直接传递给更小的模型使用。在三个数据集（WOS, Flipkart, LEDGAR）上，该方法在Macro F1上比检索基线最高提升10.0个百分点，小模型（2B–20B）通过跨模型知识转移最高提升11.5个百分点。

### 方法 / 贡献
1. 提出混淆感知检索策略：基于训练集错误分析，识别系统混淆的标签对，并在推理时将互为混淆伙伴的标签强制同时加入候选集。
2. 设计三阶段知识生成管线：先对每个误分类实例提取区分信号，再合并为方向性规则，最后对称合并为双向规则，无需微调。
3. 轻量级推理：生成的规则可在单个LLM调用中注入，只需一次推理；规则可跨模型转移（例如从235B模型转移到2B–20B模型）。

### 实验或数据
- 数据集：WOS（134标签, 学术），Flipkart（351标签, 电商三级层级），LEDGAR（100标签, 法律）。
- 主要模型：Qwen3-32B作为分类器与知识生成器；跨模型转移使用Qwen3-235B生成规则，转移到Ministral 3B/8B、Qwen3.5-2B/4B/9B、GPT-OSS-20B。
- 基线：零样本、少样本、MIPROv2、GEPA、检索Top-K（K=10/20）。
- 结果：在全部数据集和层级上Macro F1最高；对最深的Flipkart L3层，相比检索K=20提升+4.4pp，相比零样本提升+11.2pp；显著优于所有基线（p<0.05）。
- 消融实验详见附录，文中未详细展开。

### 值得关注点
- 混淆伙伴的加入使候选集中正确标签从未包含率14%降至1.9%，显著缓解检索遗漏问题。
- 生成的区分规则使LLM在选择错误率（候选集中有正确标签但未选）从21.3%降至8.6%。
- 跨模型转移效果显著：例如Qwen3.5-2B在Flipkart L3从69.9%提升至81.4%。
- 规则无需重新训练，一次生成可复用至多个小型模型。

### 局限性
- 知识生成依赖已有训练集错误：需要有一定量错误样本才能有效生成规则，对极少数据或零错误场景可能受限。
- 混淆对数量选择需设定阈值（本文用τ=75%覆盖），该超参数对不同任务可能敏感。
- 规则生成采用LLM自身，可能存在生成规则偏差或不够精确的风险。
- 实验仅覆盖三个公开数据集（法律、学术、电商），领域推广性尚待验证。
- 未与完全微调的模型在同条件下进行深入比较（仅简要讨论）。

## 4. Does task decomposition improve automatic NLG evaluation?

- Source: arxiv
- arXiv ID: 2609.01139
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.01139v1
- PDF: https://arxiv.org/pdf/2609.01139v1
- DOI: https://doi.org/10.48550/arXiv.2609.01139

### Authors

Sebastian Steindl, Nikos Voskarides, Alberto Gasparin, Diego Marcheggiani

### Abstract

The LLM-as-a-judge (LLMaJ) framework has emerged as a promising solution for cheap, reproducible, reference-free Natural Language Generation (NLG) evaluation. Prior work seeks to improve LLMaJ by decomposing evaluation tasks into simpler sub-tasks. In this work, we systematically compare LLMaJ methods with and without decomposition on multiple NLG datasets. We find no evidence that LLMaJ with task decomposition leads to performance gains over a fair baseline that does not use decomposition. Instead, we find that previously reported performance gains in decomposition-based LLMaJ stem from using human labels as training data, and not task decomposition itself. Also, we find that, when human labels are available, LLMaJ without using task decomposition can perform comparably to human annotators.

### 中文一句话结论
任务分解并未提升以 LLM 为裁判的 NLG 评估表现，先前报告的改进源于使用人工标签作为训练数据，而非分解本身。

### English TL;DR
This paper finds no evidence that task decomposition improves NLG evaluation with LLM-as-a-judge, showing that previously reported gains stem from using human labels as training data rather than from decomposition itself, and that direct prediction without decomposition can achieve comparable performance to human annotators when human labels are available.

### 中文详细总结
本文系统比较了基于任务分解的 LLM-as-a-judge（LLMaJ）方法与直接预测方法在多个 NLG 数据集上的表现。研究发现，任务分解并未带来性能提升，先前分解方法的优势实际来自人工标签的使用。当人工标签可用时，直接预测方法可达到与人类标注者相当的性能，且优于分解方法。本文还尝试了更合理的分解逻辑（如 AOI）和上下文学习（ICL），但仍未显著改善分解方法的表现。

### 方法 / 贡献
- 系统比较了分解式 LLMaJ（如 HD-Eval、CheckEval）与直接预测基线。
- 揭示了分解方法性能提升的真正来源（人工标签而非分解）。
- 证明直接预测方法在有人工标签时可达人类水平。
- 提出了原子性、可观察性、独立性（AOI）分解和 ICL 扩展，但效果有限。

### 实验或数据
- 使用了 SummEval、TopicalChat 和 Seahorse 三个 NLG 评估数据集。
- 主要采用 Spearman's ρ、Advantage Probability（AP）和 Win-Rate（WR）作为评估指标。
- 使用 Claude-4（Sonnet）为主模型，并在 Qwen3-32B 和 GPT-OSS-120B 上验证趋势一致性。
- 对 HD-Eval 和 CheckEval 进行了复现，并与原始报告结果对比。

### 值得关注点
- 直接预测（无分解）在多个指标上优于或持平于分解方法。
- 人工标签是关键因素：直接预测+人工标签在 SummEval 上 AP 达 0.846，TopicalChat 上达 0.888。
- 分解方法的扩展（AOI、ICL）仅带来微小改进，未能超越直接预测。
- 在 TopicalChat 上，直接预测无人工标签的 ρ 达 0.701，优于所有分解方法。

### 局限性
- 仅使用了有限数量的 NLG 评估数据集（三个），可能不覆盖所有场景。
- 分解方法中的子标准无真值标注，无法直接评估分解质量。
- 实验中未探索其他 LLM 模型（如 GPT-4、Llama 系列）的广泛影响。
- 未涉及更复杂的分解结构（如多层、动态分解）或混合方法。

## 5. The Curse of Multilinguality in Lexical Normalization

- Source: arxiv
- arXiv ID: 2609.00329
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.00329v1
- PDF: https://arxiv.org/pdf/2609.00329v1
- DOI: https://doi.org/10.48550/arXiv.2609.00329

### Authors

Saman Rahbar

### Abstract

Lexical normalization rewrites the noisy, non-standard words that fill user-generated text (tmrw, u, gr8) into their standard forms. Because labelled data is scarce for most languages, a popular shortcut is to train a single model on many languages at once. We ask a simple question: how many languages should such a model be trained on? Using one fixed-capacity character-level model and twelve languages from a standard benchmark, we vary the number of jointly trained languages from one to twelve and measure per-language accuracy. We find a clear curse of multilinguality: accuracy is highest when a language is trained with only a few others, often just one to four, and then falls steadily and substantially, dropping by about forty percent as the rest are piled on. A control that holds the total amount of training data constant makes the decline arrive sooner and fall further, which points to competition among the languages for one fixed-size model rather than to how much data is available. We also test whether a language's typological distance from the others predicts its ideal number of co-training languages, and find no dependable rule: any apparent relationship rests on a couple of languages and does not hold up. For compact normalization models, less can be more: a few languages beat pooling everything into a single model.

### 中文一句话结论
固定容量字符级模型在词汇归一化中，联合训练的语言数量从1增加到12时，每种语言的准确率先升后降，在1-4种语言时达到峰值，之后下降约40%，呈现出“多语言诅咒”，且该现象源于模型容量竞争而非数据量，而语言类型距离无法可靠预测最佳搭配语言数。

### English TL;DR
Using a fixed-capacity character-level model for lexical normalization across 1–12 languages from the MultiLexNorm benchmark, per-language accuracy peaks when training with only 1–4 other languages and then drops steadily by about 40% as more languages are added. A control experiment shows this decline is due to competition for model capacity, not data volume. Typological distance does not reliably predict the optimal number of co-training languages. Two languages (Spanish, Italian) perform below zero ERR but improve with more languages, highlighting a floor effect. For compact models, less can be more.

### 中文详细总结
该论文研究词汇归一化任务中的“多语言诅咒”。作者固定一个字符级Transformer模型（1.49M参数），从零开始训练，在MultiLexNorm基准的12种语言上，每次随机选择1到12种语言联合训练，并测量每种语言的错误减少率（ERR）。结果显示：对于大多数语言，ERR在联合训练1-4种语言时达到峰值，之后随语言数量增加而持续下降，到12种语言时平均下降约40%。控制实验（固定总训练数据量）表明，下降主要由模型容量竞争引起，而非数据总量。此外，语言类型距离（基于URIEL）不能可靠预测每种语言的最佳语言数。西班牙语和意大利语在所有条件下的ERR均为负值（即模型破坏多于修复），但更多语言反而改善性能，表明它们是数据稀疏导致的特殊情况。总体而言，固定容量模型下，少量语言联合训练效果优于全部语言混训。

### 方法 / 贡献
- 方法：使用固定容量（1.49M参数）的字符级编码器-解码器Transformer，从零开始训练，避免预训练模型引入未知容量。在MultiLexNorm的12种语言上，采用随机子集采样（覆盖约束）和3个随机种子，共390次训练，评估ERR随联合语言数（k=1到12）的变化。
- 贡献：
  1. 首次刻画词汇归一化中准确率-语言数量前沿，证明存在“多语言诅咒”。
  2. 通过控制总训练数据量的对照实验，将性能下降归因于模型容量竞争而非数据量。
  3. 测试并否定语言类型距离能预测最佳语言数的假设，发现该关系脆弱且依赖少数语言。

### 实验或数据
- 数据：MultiLexNorm基准的12种语言（丹麦语、德语、英语、西班牙语、克罗地亚语、印尼-英语混合、意大利语、荷兰语、斯洛文尼亚语、塞尔维亚语、土耳其语、土耳其-德语混合），训练集大小6k-57k tokens，变化率6.6%-37.0%。使用官方训练/测试集划分，5种语言无开发集时从训练集留出10%作开发集。
- 实验：对每个k从1到12，随机抽取k种语言子集（覆盖约束确保每种语言出现次数相当），联合训练模型，早期停止，记录每种语言测试ERR。重复3个种子。控制实验：固定总训练数据量（如k=1时的数据量），重复上述流程。
- 结果：10种语言（排除西班牙语和意大利语）平均ERR在k=2时最高（0.316），k=12时降至0.191（下降40%）。方言最优k*平均为2.5，英语、德语、荷兰语、土耳其-德语在k=1时最优。西班牙语和意大利语ERR始终为负，但随k增加而改善（k=8-10时最佳）。

### 值得关注点
- 多语言诅咒在小型字符级模型上成立，与大规模模型中的现象一致，但机制更直接：模型容量固定，语言间竞争导致负干扰。
- 英语等数据充足的语言单独训练最好，而数据稀疏但变化率高的语言（如土耳其语）可受益于更多合作语言（k=6）。
- 西班牙语和意大利语的反常行为（负ERR但随语言数增加改善）反证了容量竞争解释：它们因训练数据中改变例过少而失败，加入更多语言提供更多共享模式，但总体仍不如不训练。
- 即使将西班牙语和意大利语纳入平均，多语言诅咒仍存在（45%下降），说明结论稳健。

### 局限性
- 模型固定为1.49M参数，更大模型可能改变结果（如西班牙语和意大利语可能随模型容量增加而成功）。
- 仅使用MultiLexNorm的12种语言（部分为代码混合），结论可能不推广到更多语言或不同领域。
- 未分析模型错误类型，对西班牙语和意大利语的失败原因仅为推测，未验证。
- 测试ERR仅基于2000 tokens样本（除最终验证外），可能引入采样噪声。
- 未探究不同训练策略（如语言加权、课程学习）能否缓解诅咒。

## 6. Value Over Language Model: Detecting Original Contribution in Writing

- Source: arxiv
- arXiv ID: 2609.00700
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.00700v1
- PDF: https://arxiv.org/pdf/2609.00700v1
- DOI: https://doi.org/10.48550/arXiv.2609.00700

### Authors

Vibhhu Sharma, Thorsten Joachims, Sarah Dean

### Abstract

LLMs have been rapidly adopted across writing tasks, prompting the development of tools for detecting LLM-generated text. Yet, these tools largely measure how much of a document's surface text was written by an LLM and aren't fundamentally designed to measure how much of the information content or ideas originated from the LLM itself rather than being supplied by the user in the prompt. In this work, we design a framework that measures how much value a person adds on top of what a language model could have easily produced by itself. The method requires no training or labeled data and never scores the document's surface text, insulating it from stylistic confounders. Instead, it extracts the document's content at increasing levels of granularity, uses an LLM to reconstruct the document from each partial representation, and compares these reconstructions with those produced from the task description alone. We call this framework Value Over Language Model (VOLM), which measures a document's contribution relative to a replacement-level document that an LLM could produce from the task description alone. We evaluate VOLM with a specific instantiation of this framework across three domains: news articles, ICLR peer reviews, and argumentative essays. VOLM separates human-authored documents from matched LLM-generated documents produced from generic task descriptions, while remaining substantially invariant to content-preserving transformations, including LLM-based reconstruction and round-trip translation. We further find that increasingly constrained content extractors reduce residual differences between LLM-generated and humanized text, demonstrating the importance of disentangling informational content from stylistic variation. We hope these results encourage further work on specialized instantiations of the framework and on assessing human contributions in LLM-assisted writing more generally.

### 中文一句话结论
提出VOLM框架，通过衡量文档信息内容超出语言模型自身生成水平的部分，来量化人类的原创贡献，无需训练或标注数据。

### English TL;DR
VOLM is a training-free framework that quantifies a human author's original contribution in a document by measuring how much of its informational content exceeds what a language model could generate from the task description alone, using content extraction and reconstruction to avoid reliance on surface text or stylistic confounders.

### 中文详细总结
该论文提出Value Over Language Model (VOLM)框架，旨在区分文档中人类作者的原创贡献与语言模型自动生成的内容。与现有检测方法关注文本表面是否由LLM生成不同，VOLM通过提取文档内容的不同粒度信息，利用LLM进行重构，并与仅基于任务描述生成的重构文档进行比较，从而量化人类在信息层面的增值。该方法无需训练或标注数据，且不直接评估文档表面文本，因此对风格变换（如改写、翻译）具有鲁棒性。实验在新闻文章、ICLR同行评审和议论文三个领域进行，表明VOLM能有效区分人类撰写与LLM生成的文档，并对内容保留变换保持稳定。

### 方法 / 贡献
1. 重新定义问题：从检测LLM生成的文本比例转向衡量人类原创信息贡献。
2. 提出VOLM通用框架，通过提取-重构-评分流程量化贡献。
3. 实现无需训练或标注数据的具体算法，仅使用现成LLM的对数概率。
4. 证明VOLM对内容保留变换（如LLM改写、往返翻译）具有鲁棒性，同时保持对原创内容差异的敏感性。

### 实验或数据
在三个领域评估：新闻文章、ICLR同行评审、议论文。使用匹配的人类撰写和LLM生成的文档。VOLM能够分离两类文档，并对内容保留变换（包括LLM重构和往返翻译）保持实质不变性。进一步发现，更受约束的内容提取器能减少LLM生成与人类改良文本之间的残余差异，表明区分信息内容与风格变异的重要性。

### 值得关注点
1. 提出从信息内容而非表面文本出发的原创性检测新视角。
2. 无需训练数据，直接使用现成LLM，易于应用。
3. 对风格变换鲁棒，可避免因表达方式不同导致的误判。
4. 框架通用，可适应不同领域和任务描述。

### 局限性
论文未明确讨论局限性，但框架依赖特定的LLM用于重构，且提取器与重构器的设计可能影响结果。此外，需要任务描述作为输入，对于无明确任务描述的场景可能不适用。通用性需要更多领域验证。

## 7. The Interlingua Hypothesis: LLMs Translate via a Latent Task-agnostic Feature Space

- Source: arxiv
- arXiv ID: 2609.00515
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.00515v1
- PDF: https://arxiv.org/pdf/2609.00515v1
- DOI: https://doi.org/10.48550/arXiv.2609.00515

### Authors

Jacob Brinton, Jannik Brinkmann, Mark Crovella, Aaron Mueller

### Abstract

Large language models (LLMs) have recently demonstrated improved machine translation performance over strong supervised baselines. This raises questions as to what mechanisms underlie how LLMs perform machine translation between languages. Motivated by recent interpretability findings--namely, that LLMs use massively multilingual latent feature representations to perform language modeling--we propose the interlingua hypothesis. The hypothesis holds that language models translate by reading a source sentence into a latent feature space, and generate a target sentence by reading from the latent feature space. We show three lines of evidence in support of this hypothesis: (1) variance in BLEU across language pairs is largely predictable from language-specific competences with no language pair-specific interaction terms; (2) many model components are causally influential in both monolingual tasks and translation tasks; and (3) fine-tuning on monolingual data recovers a large proportion of translation improvements relative to fine-tuning on aligned documents. Together, these provide convergent evidence in support of the interlingua hypothesis, and suggest new ways of understanding and improving how LLMs can be leveraged to perform translation tasks.

### 中文一句话结论
本文提出“中间语假说”：大语言模型（LLM）执行机器翻译时，并不是依赖语言对专属机制，而是先把源语言句子编码到一个与任务无关的潜在特征空间，再从这个空间解码生成目标语言句子。

### English TL;DR
The interlingua hypothesis proposes that large language models translate by encoding source sentences into a latent task-agnostic feature space and decoding from it, supported by evidence that translation performance is predictable from monolingual abilities, shared causal components, and recovery of translation improvements via monolingual fine-tuning.

### 中文详细总结
论文提出并检验了 LLM 机器翻译的“中间语假说”。该假说认为，模型翻译时复用其多语言、任务无关的潜在特征表示：先“读入”源语言句子的抽象特征，再基于这些特征“读出”目标语言句子，因此不需要专门的翻译模块或语言对特定机制。作者通过三条证据支持该假说：(1) 语言对之间的 BLEU 差异主要可由源语言和目标语言各自的单语能力预测，加入语言对交互项并不能显著提高预测力；(2) 许多模型组件在单语任务和翻译任务中都有因果影响，说明存在共享的任务无关表示；(3) 仅用单语数据微调就能恢复与平行语料微调相当大比例的翻译提升。结论表明 LLM 的翻译能力在很大程度上源于其单语语言建模能力，而非专门的翻译机制。

### 方法 / 贡献
- 提出“中间语假说”并用三种互补证据进行验证。
- 使用线性模型（仅源/目标语言单语能力项）与双线性模型（额外加语言对交互项）预测翻译 BLEU，检验是否需要语言对特定机制。
- 单语能力代理指标包括：FLORES 困惑度、MultiBLiMP 语法可接受性准确率/margin、GlobalMMLU 多语言常识问答准确率。
- 翻译性能用 FLORES 上的 2-shot prompting + sacreBLEU 评估。
- 通过因果中介分析检验模型组件在单语和翻译任务中的共享因果影响。
- 对比单语数据微调与平行语料微调对翻译性能的恢复程度。

### 实验或数据
- 模型：Llama-3.1-8B 和 Aya-23-8B。
- 数据：FLORES 翻译基准、MultiBLiMP、GlobalMMLU；共 18 种共同语言用于回归分析。
- GlobalMMLU 准确率预测 BLEU 的线性模型 \(R^2\) 为 Llama 0.739、Aya 0.510；MultiBLiMP 准确率对应 \(R^2\) 为 0.294 和 0.235。
- 双线性模型与线性模型预测力几乎相同，说明语言对交互项没有显著增益。
- 目标语言能力比源语言能力更重要：目标语言间平均 BLEU 方差是源语言的 9.3 倍（Llama）和 3.9 倍（Aya）。
- 摘要提及单语微调可恢复大部分翻译提升；预览中未给出具体恢复比例数值。

### 值得关注点
- 翻译表现主要受目标语言单语能力驱动，源语言能力影响较小。
- GlobalMMLU（世界知识）比语法可接受性更能预测翻译质量。
- 单语微调可能成为无需大规模平行语料提升翻译的途径。
- 研究为“LLM 翻译能力来自通用多语言抽象表示”提供了机制层面的证据。

### 局限性
- 作者指出没有任何单一实验能最终确证中间语假说，只是三类证据的汇聚。
- 结论针对“完全训练好的 LLM”所用机制，不讨论预训练数据中平行语料的作用。
- MultiBLiMP 在部分语言上存在饱和问题，因此需要额外代理指标。
- 回归分析仅限于 18 种共同语言，可能不能推广到所有语言。
- 关于单语微调恢复翻译提升的具体幅度，在提供的材料中未给出详细量化结果。

## 8. KItCAT: Knowledge Injection via Input Corruption for Auto-regressive Training

- Source: arxiv
- arXiv ID: 2609.00082
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.00082v1
- PDF: https://arxiv.org/pdf/2609.00082v1
- DOI: https://doi.org/10.48550/arXiv.2609.00082

### Authors

Meghanadh Pulivarthi, Kushagra Bhushan, Vineet Kumar, Gaurav Pandey, Jaydeep Sen, Dinesh Raghu, Sachindra Joshi, Yatin Nandwani

### Abstract

LLMs acquire vast amounts of knowledge during pre-training, but often lack the specialized knowledge needed to answer questions from niche sources such as manuals or technical documents unseen during pre-training. Continued pre-training (CPT) is widely used to inject such knowledge into model parameters. However, niche documents seldom repeat facts, making it difficult for CPT to robustly acquire such knowledge. Recent works address this by generating multiple paraphrases of the new knowledge, but paraphrasing is computationally expensive and typically requires powerful LLMs. In this work, we introduce KItCAT: Knowledge Injection via Corrupted Auto-regressive Training, a lightweight training strategy that reduces the need for paraphrasing in decoder-only LLMs. KItCAT augments standard next-token prediction by stochastically corrupting the input sequence. During training, a random subset of input tokens is replaced with other vocabulary tokens while the original next-token labels are kept unchanged. This simple intervention generates diverse training inputs from each sample, enabling large-scale data augmentation at negligible cost. We show that KItCAT consistently improves over CPT across multiple datasets and model families. Code is available at https://github.com/meghanadhpulivarthi/KItCAT.

### 中文一句话结论
KItCAT通过在自回归训练中随机替换部分输入词元，在不依赖代价高昂的释义生成的情况下，显著提升了大语言模型从专业文档中注入知识的效果。

### English TL;DR
KItCAT is a lightweight training strategy that stochastically corrupts input tokens during auto-regressive training to inject specialized knowledge into decoder-only LLMs, reducing the need for expensive paraphrasing while consistently outperforming standard continued pre-training.

### 中文详细总结
KItCAT是一种轻量级的训练方法，旨在解决大语言模型在持续预训练（CPT）中因专业文档缺乏重复而难以稳健吸收知识的问题。传统方法通过生成多个释义来增加数据多样性，但计算成本高且依赖强大LLM。KItCAT在标准自回归训练目标中，对输入序列进行随机词元替换（如随机词掩码、随机词替换、上下文相近词替换或关键词掩码），同时保持原标签不变。这使每个样本在每轮训练中产生不同扰动，防止模型过度拟合表面词汇模式，从而鼓励学习语义更稳固的表征。实验表明，KItCAT在多个数据集和多种模型家族上一致优于标准CPT，且可与现有释义方法互补。

### 方法 / 贡献
- **方法**：提出四种输入扰动方案（随机替换、掩码、上下文替换、关键词掩码），在解码器-only LLM的持续预训练中随机替换部分输入词元，而预测标签保持不变。
- **贡献**：
  1. 首次将输入扰动引入知识注入场景，减少对昂贵释义生成的依赖。
  2. 在多个数据集和模型家族上验证了该方法持续优于标准CPT。
  3. 证明该方法可与基于释义的数据增强互补，降低对合成数据的依赖。

### 实验或数据
论文在多个数据集和三种模型家族上进行了实验，代码已公开（https://github.com/meghanadhpulivarthi/KItCAT）。摘要和内容未提供具体数据集名称、指标或实验设置细节。

### 值得关注点
- 核心洞察：防止模型在每轮训练中见到完全相同的输入，从而抑制对虚假词汇模式的重度依赖。
- 方法极简单：仅需随机替换输入词元，无需外部生成模型或大量计算。
- 与现有释义方法互补，可叠加使用进一步提升性能。

### 局限性
论文未明确讨论方法的局限性。潜在挑战包括：扰动概率和策略的选择对效果敏感；对于高度专业且噪声敏感的知识注入场景，随机替换可能引入误导信号；在极低数据量下，扰动可能造成信息丢失。

## 9. PersianAnonymizer: Evaluating LLM-Labeled Training for Efficient NER-based Anonymization in Persian

- Source: arxiv
- arXiv ID: 2609.00958
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.00958v1
- PDF: https://arxiv.org/pdf/2609.00958v1
- DOI: https://doi.org/10.48550/arXiv.2609.00958

### Authors

Mohammad Hossein Shalchian, Mostafa Amiri, Amir Mahdi Sadeghzadeh

### Abstract

We target practical anonymization of Persian customer chats by training a compact NER model from LLM-labeled supervision and selecting the best labeler for deployment. We compare three instruction-tuned LLMs: DeepSeek-V3-0324, GPT-OSS-120B, and Qwen3-235B-A22B-Instruct-2507, to produce span annotations under a shared JSON protocol, yielding four corpora (OSS_ZeroShot, Qwen_ZeroShot, Qwen_FewShot, DeepSeek_FewShot). A MatinaRoberta-based token-classifier is trained per corpus and evaluated with token-level Precision/Recall/F1 (overall and per-class). We also report Label Coverage Recall (LCR), the proportion of gold non-O tokens predicted as non-O, and quantify cross-labeler behavior via a token-level Venn on test annotations. Finally, we contrast test-set annotation latency of the LLMs on H200 nodes with the trained NER's test-time labeling on a single RTX 3090. Results show that supervision from OSS_ZeroShot yields the strongest macro-F1 and LCR, while the resulting NER labels an entire 40K-message test set in approximately 2 minutes on one consumer GPU. This establishes a practical path to high-quality, low-cost anonymization for Persian industrial data.

### 中文一句话结论
本文通过比较三种大语言模型（DeepSeek-V3、GPT-OSS-120B、Qwen3-235B）作为标注器，训练紧凑型NER模型用于波斯语聊天匿名化，发现OSS_ZeroShot标注产生的监督信号在宏F1和标签覆盖召回率上最优，且训练后的NER可在单张消费级GPU上快速处理大规模数据。

### English TL;DR
This paper trains a compact NER model for Persian chat anonymization using LLM-labeled supervision, comparing three instruction-tuned LLMs. OSS_ZeroShot labels yield the best downstream performance (macro-F1 and LCR), while the resulting NER can label 40K messages in ~2 minutes on a single RTX 3090, enabling practical, low-cost anonymization for industrial Persian data.

### 中文详细总结
本研究针对波斯语客户聊天数据的实际匿名化需求，通过训练紧凑型命名实体识别模型，并利用大语言模型生成的标注来替代人工标注。作者比较了三种指令微调的大语言模型（DeepSeek-V3-0324、GPT-OSS-120B、Qwen3-235B-A22B-Instruct-2507）作为标注器，在统一的JSON协议下生成跨度标注，共得到四个语料库（OSS_ZeroShot、Qwen_ZeroShot、Qwen_FewShot、DeepSeek_FewShot）。每个语料库训练一个基于MatinaRoberta的标记分类器，并以标记级别的精确率、召回率、F1值（总体和每类）以及标签覆盖召回率进行评测。结果显示，来自OSS_ZeroShot的监督信号取得了最强的宏F1和LCR值，而训练后的NER模型在单张RTX 3090上仅需约2分钟即可标注整个4万条消息的测试集，为波斯语工业数据的高质量、低成本匿名化提供了一条实用路径。

### 方法 / 贡献
- 方法：采用“LLM标注+紧凑NER推理”的范式，首先使用三种指令微调LLM（DeepSeek-V3、GPT-OSS-120B、Qwen3-235B）对波斯语聊天数据进行跨度级标注，通过统一的JSON协议和解析后处理生成BIO格式的标注语料。然后基于MatinaRoberta为每个语料库训练一个紧凑型NER模型（标记分类器），并评估其泛化能力。
- 贡献：首次系统比较了多种LLM作为波斯语匿名化NER标注器的效果，并选择最佳标注器用于下游训练；证明了紧凑NER模型在单张消费级GPU上即可实现快速、低成本的工业级匿名化，填补了波斯语领域此方向的研究空白。

### 实验或数据
- 数据集：构建了包含265,000行消息的大规模波斯语匿名化语料库，每行消息为组织聊天流中的单条用户消息，内容简短、非正式，包含PII（如姓名、电话、邮箱、URL等）。标注集采用BIO标签方案，包括14种实体类型（COST、CREDIT_CARD、DATETIME、EMAIL、IBAN、IP_ADDRESS、LOCATION、NUMBER、ORGANIZATION、PASSWORD、PERSON、PHONENUMBER、URL、USERNAME）。
- 实验设置：三个LLM在8×H200（140GB）节点上并行标注，分别得到四个语料库（OSS_ZeroShot、Qwen_ZeroShot、Qwen_FewShot、DeepSeek_FewShot）。每个语料库训练一个MatinaRoberta模型，在40K测试集上评估标记级精确率、召回率、F1（总体和每类）、标签覆盖召回率，并跨标注器比较测试集标注的一致性。同时对比了LLM标注（H200）与NER推理（单RTX 3090）的延迟。
- 结果：OSS_ZeroShot监督的NER在宏F1和LCR上最优；NER推理速度远快于LLM标注（40K条约2分钟 vs LLM最短4分钟）。

### 值得关注点
- 首次针对波斯语工业聊天数据，系统地比较了三种LLM作为NER标注器的效果，并选择最佳标注器进行下游训练。
- 证明了紧凑NER模型在单张消费级GPU上即可实现大规模匿名化（40K条/2分钟），显著降低了成本和延迟。
- 使用了标签覆盖召回率（LCR）和跨标注器一致性分析，提供了更全面的标注质量评估。
- 统一了标注协议和提示模板，确保了不同LLM之间的可比性。

### 局限性
- 依赖LLM生成的标注，可能存在噪声和偏差，影响NER模型的最终性能。
- 研究仅针对波斯语客户聊天数据，其他语言或域可能需要重新适配。
- 未探讨不同规模或更小模型作为标注器的效果，也未考虑主动学习等进一步降低标注成本的方法。
- 论文提及在后续章节讨论局限性，包括对LLM标注重量的依赖和域适应需求等。

## 10. Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation

- Source: arxiv
- arXiv ID: 2609.01604
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.01604v1
- PDF: https://arxiv.org/pdf/2609.01604v1
- DOI: https://doi.org/10.48550/arXiv.2609.01604

### Authors

Himil Vasava, Ming Jiang

### Abstract

LLM-based evaluators of natural language generation (NLG) quality are widely deployed as scoring tools and as automated training signals, yet the internal procedure by which they assign a rating remains poorly understood. We investigate this procedure mechanistically through an eight-attack perturbation taxonomy across the Readability and Adequacy dimensions of NLG quality, a generation pipeline that produces paired clean and corrupt summaries with controlled error intensity and explicit token-level modification maps, and a four-experiment battery of causal tracing, logit-lens vocabulary projection, and attention-head knockout applied to Themis (Llama-3-8B) and Prometheus (Mistral-7B). Both evaluators implement a structured, coherent evaluation pipeline operating in two stages: below layer 15, attention performs local error comparison and routes the result to the final input position; above it, the MLP cascade integrates the signal and writes the rating, with the decision crystallizing in the residual stream at a sharp late layer (L = 26 on Themis, L = 25 on Prometheus). Furthermore, a base-model control at the same scale (Llama-3-8B) reproduces the routing architecture and crystallization but not the stage separation, isolating the two mechanisms that fine-tuning specifically installs, suppression of below-L15 MLP contribution at the last position and a two-layer advance of the crystallization depth, indicating that fine-tuning sculpts an existing substrate rather than building the pipeline from scratch. We release the source code and data at https://github.com/himil-v/judge-mech

### 中文一句话结论  
本文通过机制可解释性方法，揭示了LLM作为摘要评估器时存在一个两阶段内部流程：第15层以下的注意力模块负责局部错误比较与信号路由，第15层以上的MLP模块集成信号并写出评分；微调是对已有基座架构的雕琢，而非从头构建评估管道。

### English TL;DR  
This paper uses mechanistic interpretability to uncover the internal evaluation pipeline of LLM-as-a-judge models for summarization: a structured two-stage process where attention below layer 15 performs local error comparison and routing, while MLP above integrates signals and writes the rating; fine-tuning sculpts an existing substrate rather than building from scratch.

### 中文详细总结  
论文通过设计包含8种攻击类型的扰动分类体系（覆盖可读性与充分性维度），并利用生成管道产出成对且具有显式词级修改映射的干净/损坏摘要，结合因果追踪、logit-lens词汇投影、注意力头消融等四种机制分析方法，对Themis（Llama-3-8B）和Prometheus（Mistral-7B）两个评估器进行内部机制研究。主要发现包括：（1）评估器实现了一个结构化的两阶段管道：前15层注意力做局部错误比较并将结果路由至最终输入位置，后15层MLP级联集成信号并输出评分，决策在残差流中于清晰的晚层结晶（Themis在第26层，Prometheus在第25层）。（2）错误识别过程在注意力层因错误类型而异：可读性错误分散在相邻句法上下文，充分性错误则集中在扰动词上。（3）两个评估器写入评分的方式不同：Themis在顶层单步完成，Prometheus则跨中晚层分散写入并在最后一层进行反向修正。（4）基座模型（Llama-3-8B）对比发现，微调并未从头构建评估管道：基座已具备路由架构和晚层结晶特性，微调仅安装了两种具体修改——抑制最后位置上前15层MLP贡献（产生阶段分离）以及将结晶深度提前两层。

### 方法 / 贡献  
- **方法**：提出了一套包含8种错误类型的扰动分类体系，覆盖可读性与充分性两个质量维度；自动生成管道产生成对干净/损坏摘要，具有可控错误强度和显式词级修改图谱；应用因果追踪（窗口模式与最后token模式）、logit-lens词汇投影、注意力头消融四种机制方法。  
- **贡献**：首次系统揭示LLM作为NLG评估器的内部机制，证明其存在结构化两阶段评估流程；发现错误识别对不同质量维度采用不同的注意力策略；揭示了不同评估器在评分写入方式上的差异；通过基座模型对比，证明微调只是修改已有结构而非重建管道。

### 实验或数据  
- **实验**：使用CNN/DailyMail数据集生成评估样本，并利用XSum数据集验证跨领域泛化性。控制每个样本的扰动词数量（参数k）并通过显式token数组记录修改位置。对Themis（Llama-3-8B）和Prometheus（Mistral-7B）进行四项机制实验：窗口模式与最后token因果追踪、logit-lens、注意力头消融。  
- **数据**：经过手动验证（每个攻击类型约20对样本，检查扰动是否实际注入、token映射是否准确、类型是否匹配），合格率约95-100%。排除因果追踪条件不佳（评分变化低于阈值）的样本。

### 值得关注点  
- 发现可读性错误与充分性错误在注意力层中的处理模式截然不同：前者扩散至相邻语法上下文，后者集中在本义单词上。  
- 基座模型已具备与微调评估器相似的晚层结晶与路由结构，但缺乏底层MLP抑制作用——说明微调不是新功能添加，而是对已有基座的精细化调节。  
- 结晶深度从基座的L=28提前至评估器的L=26（Themis）或L=25（Prometheus），暗示微调提升了决策时效。  
- Themis与Prometheus在评分写入步数上存在差异：一个单步完成，另一个多步修正。

### 局限性  
- 研究仅聚焦于摘要评估任务，尚未覆盖对话、翻译等其他NLG生成任务。  
- 仅分析了两个基于不同基座（Llama-3-8B与Mistral-7B）的特定评估器，结论的通用性需更多模型验证。  
- 扰动分类体系虽覆盖8种多类型错误，但可能无法代表所有自然语言错误模式。  
- 因果追踪方法依赖显式词级修改图谱，对于复杂结构扰动（如句子级重写）难以直接应用。  
- 研究为观察性分析，未提出新的训练方法以提高评估器稳健性。

## Processing Notes

- Duplicate papers skipped: 0