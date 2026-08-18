# Daily arXiv - 2026-08-18

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-18T23:13:33
- Paper count: 10

## 1. LLMs Get Smarter from Targeted Synthetic Multilingual Data

- Source: arxiv
- arXiv ID: 2608.15964
- Relevance: 4.7

### Links

- Abstract: http://arxiv.org/abs/2608.15964v1
- PDF: https://arxiv.org/pdf/2608.15964v1
- DOI: https://doi.org/10.48550/arXiv.2608.15964

### Authors

Ishika Agarwal, Arkajyoti Charaborty, Tanner Sorensen, Neha Gupta, Andreas Stolcke

### Abstract

Language-specific competency (LSC) is the phenomenon of a language model performing better or worse depending on the language of the prompt. In other words, a language model outputs different (and potentially incorrect) responses to the same semantic query when prompted in different languages. Prior work attributes this to an internal misalignment of semantic representation across languages. Currently, there are two main approaches to address LSC in the literature: (1) routing all queries through English, improving performance, but limiting language expressivity to English; or (2) training on language-balanced data, equalizing model performance across languages, but reducing overall performance. In this work, we take a data centric perspective and introduce HOTFIXR: Hardness Optimized Training data For Improving X-Lingual Reasoning. It is a data generation framework that uses models to probe and learn a student model's multilingual weaknesses, and generates data to mitigate them. HOTFIXR can generate multilingual synthetic training data that can improve multilingual performance. We evaluate on three in-distribution tasks, three out-of-distribution tasks, and four out-of-distribution languages. On average, HOTFIXR (1) improves in-distribution performance by 6.2%, (2) reduces catastrophic forgetting (induced by fine-tuning) on OOD tasks by 3.7%, and (3) on OOD languages by 7.1%. Overall, as many real-world applications requires multilingual LLMs, our work contributes to the efforts of making LLMs multilingually proficient. We will release code upon acceptance.

### 中文一句话结论
HOTFIXR通过针对性生成多语言合成训练数据，有效提升了大语言模型的多语言性能，同时减少了灾难性遗忘。

### English TL;DR
HOTFIXR, a targeted synthetic multilingual data generation framework, enhances LLM multilingual performance by probing and mitigating student model weaknesses, improving in-distribution accuracy by 6.2% while reducing catastrophic forgetting on out-of-distribution tasks and languages.

### 中文详细总结
本文提出HOTFIXR（Hardness Optimized Training data For Improving X-Lingual Reasoning），一个针对大语言模型语言特定能力差异（LSC）的数据生成框架。LSC指同一模型在不同语言下对相同语义查询给出不同甚至错误回答的现象，现有解决方案（如统一经过英语处理或平衡语言训练数据）均有性能损失。HOTFIXR采用数据为中心视角，通过训练问题生成模型，利用学生模型的反馈信号（包括语言无关能力不足和语言特定能力不足）来生成能够改善多语言能力的合成训练数据。实验表明，该方法在分布内任务上平均提升6.2%，在分布外任务上减少了3.7%的灾难性遗忘，在分布外语言上减少了7.1%。该方法权衡了多语言一致性和整体性能，找到了平衡点。

### 方法 / 贡献
- **方法**：HOTFIXR包含三个阶段：（1）使用问题生成模型生成数据样本；（2）设计获取函数（acquisition function）评估学生模型的语言缺陷，包括语言无关能力不足（通过英语推理不确定性衡量）和语言特定能力不足（通过不同语言下推理表征的余弦距离衡量）；（3）利用GRPO优化算法，根据获取函数分数训练问题生成模型，使其产生更具挑战性的样本。
- **贡献**：提出一种新的合成数据生成框架，能够自动识别并针对性改善多语言模型的薄弱环节，在不显著牺牲整体性能的前提下提升多语言能力。

### 实验或数据
- **实验设置**：使用三个分布内任务、三个分布外任务和四种分布外语言进行评估。
- **主要结果**：HOTFIXR在分布内性能上达到56.2%，优于所有基线方法（Base为51.9%）；分布外性能为64.7%，仅次于Base的65.6%但远优于其他训练基线；语言一致性（跨语言性能标准差）最低（9.4），表明多语言性能更均衡。
- **数据**：实验基于多语言HotPotQA等数据集，但具体训练数据细节未在摘要中详细说明。

### 值得关注点
1. **创新性**：提出基于学生模型反馈信号生成针对性训练数据的方法，解决了多语言模型性能与一致性之间的权衡问题。
2. **实用性**：方法可应用于多种多语言场景，代码即将开源。
3. **鲁棒性**：在分布外任务和语言上仍能保持较好性能，减少了微调带来的灾难性遗忘。

### 局限性
- **模型依赖**：框架依赖问题生成模型和学生模型的质量，可能受限于基础模型的能力。
- **语言覆盖**：目前仅测试了法语、西班牙语、阿拉伯语、葡萄牙语和意大利语，对更多低资源语言的效果未知。
- **评估范围**：实验仅覆盖少量任务和语言，未在大规模多语言基准上全面验证。
- **假设限制**：假设英语为最强语言，可能不适用于英语能力较弱的多语言模型。

## 2. Discrete Diffusion Language Models Are Training-Free Multi-Label Classifiers

- Source: arxiv
- arXiv ID: 2608.14649
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.14649v1
- PDF: https://arxiv.org/pdf/2608.14649v1
- DOI: https://doi.org/10.48550/arXiv.2608.14649

### Authors

Pawan Kumar

### Abstract

We present dLLM-SetScore, a training-free method that uses discrete masked-diffusion language models for multi-label text classification. For each candidate label, it asks a short yes/no question and compares the probabilities of the two answer tokens at one masked position. The method uses no task-specific fine-tuning or training on textual-entailment datasets; a 200-example labelled validation slice selects thresholds, temperature, and prompt wording.
  We first show that placing all labels in one prompt creates a strong slot-position asymmetry: the first answer slot is predicted positive on $99.4\%$ of GoEmotions examples and $100\%$ of Reuters examples. Per-label scoring places every label in the same syntactic position, making predictions invariant to label order and avoiding this artifact. We evaluate LLaDA-8B and Dream-7B on six datasets against NLI models, an autoregressive LLM, SetFit, and supervised classifiers. On the five datasets shared by both diffusion families, Instruct checkpoints improve macro-F1 in 9 of 10 comparisons and micro-F1 in 8 of 10, although these comparisons do not identify the cause. Within our protocol, LLaDA-Instruct records the highest training-free values for both Reuters and ECtHR metrics. We prove permutation invariance, characterize thresholded decisions under weighted Hamming loss, and derive shortlist ceilings for recall and F1. An exploratory local Joint Set Refinement step lowers F1 from biased and unbiased initializations and is retained as a negative result.

### 中文一句话结论
本文提出 dLLM-SetScore，一种无需训练的多标签文本分类方法，利用离散掩码扩散语言模型对每个标签进行独立的是/否问答，有效避免了槽位位置不对称问题，在多个数据集上取得了具有竞争力的无训练分类性能。

### English TL;DR
dLLM-SetScore uses discrete masked-diffusion language models in a training-free manner for multi-label text classification by posing per-label yes/no questions, addressing a slot-position asymmetry issue and achieving competitive results without task-specific fine-tuning.

### 中文详细总结
本文提出 dLLM-SetScore，一种训练自由的框架，利用离散掩码扩散语言模型（如 LLaDA-8B 和 Dream-7B）进行多标签文本分类。方法对每个候选标签构造一个简短的是/否提示，并通过比较单一掩码位置上“是”和“否”两个答案 token 的对数概率来生成评分。该方法无需对扩散模型进行任务特定微调，也无需在文本蕴含数据集上训练；仅使用 200 个标注验证样本选择阈值、温度和提示模板。研究发现，将所有标签放在同一个多槽答案提示中会导致严重的槽位位置不对称（第一个答案槽在 GoEmotions 上 99.4% 为正，Reuters 上 100% 为正）。按标签评分将每个标签置于相同的句法位置，避免了这一伪影，使预测对标签顺序具有置换不变性。在六个数据集（GoEmotions、Reuters-21578、EURLEX57K、ECtHR Task A、Jigsaw Toxic、AAPD）上，与 NLI 模型（BART-MNLI、DeBERTa-NLI）、自回归 LLM（Qwen2.5-7B-Instruct）、SetFit 和有监督分类器（BERT、RoBERTa、T5）比较。在两个扩散系列共享的五个数据集上，Instruct 检查点在 macro-F1（9/10）和 micro-F1（8/10）上大多优于 Base 检查点，但该比较未识别出原因。在作者协议内，LLaDA-Instruct 在 Reuters 和 ECtHR 上取得了最高的无训练指标值。论文还提供了置换不变性、加权汉明损失下的阈值决策以及基于候选短列表的召回率和 F1 上界的理论分析。探索性的局部联合集细化步骤（JSR）从有偏和无偏初始化均降低了 F1，作为负面结果保留。

### 方法 / 贡献
1. **识别槽位位置不对称**：发现将所有标签放入一个多槽掩码提示会导致第一个答案槽几乎总是预测为正，严重破坏多标签分类。
2. **提出按标签评分**：为每个标签单独构建是/否提示，所有标签位于相同句法位置，实现置换不变性，完全避免槽位不对称。
3. **实证对比检查点差异**：在 LLaDA-8B 和 Dream-7B 上，Instruct 检查点大多优于 Base 检查点，但未归因于指令调优机制。
4. **理论分析**：证明了按标签评分器的置换不变性、在阈值匹配的加权汉明损失下的贝叶斯最优性，以及候选短列表对召回率和 F1 的上界。
5. **无训练框架**：不进行任务特定微调或 NLI 训练，仅使用 200 个验证样本选择超参数。

### 实验或数据
- **数据集**：GoEmotions、Reuters-21578、EURLEX57K、ECtHR Task A、Jigsaw Toxic、AAPD，共六个数据集。
- **扩散模型**：LLaDA-8B（Base 和 Instruct）、Dream-7B（Base 和 Instruct）。
- **比较基线**：BART-MNLI、DeBERTa-NLI、Qwen2.5-7B-Instruct、SetFit（少样本）、有监督 BERT、RoBERTa、T5。
- **主要结果**：在五个共享数据集上，Instruct 模型在 macro-F1（9/10 对比）和 micro-F1（8/10 对比）上优于 Base。LLaDA-Instruct 在 Reuters（micro/macro）和 ECtHR（micro/macro）上取得最高无训练指标。混合集成（BART-MNLI + SetFit + LLaDA-Instruct）在 Reuters 上达到 82.4/79.3（micro/macro F1），距有监督 RoBERTa 仅差 7 micro-F1。
- **负面结果**：局部联合集细化（JSR）在所有配置下均降低 F1。

### 值得关注点
- **槽位位置不对称的发现与解决**：揭示了多槽提示中因第一个掩码位置承载过多上下文导致的伪影，按标签评分简单有效。
- **训练自由的实用性**：无需微调即可获得竞争结果，尤其在法律（ECtHR）和新闻（Reuters）领域表现突出。
- **Instruct 检查点的一致优势**：虽未解释机制，但两个扩散系列均呈现稳定模式，值得后续研究。
- **理论贡献**：为按标签评分提供了置换不变性、贝叶斯最优性和短列表上限等理论保障。
- **负面结果报告**：JSR 的失败被明确记录，为社区提供经验教训。

### 局限性
1. **依赖验证集参数选择**：阈值、温度和提示模板仍需要 200 个标注样本的验证集。
2. **Instruct 优势原因未明**：论文明确指出比较未识别出 Instruct 与 Base 差异的机制。
3. **按标签评分效率**：每个标签需独立进行扩散模型前向传播，对于大规模标签集可能计算开销较大（论文未讨论效率但可推断）。
4. **提示模板偏差**：按标签评分虽消除了槽位不对称，但仍受提示措辞、标签描述和词汇偏差影响，论文对此有探索但未完全消除。
5. **JSR 探索失败**：局部联合集细化从有偏和无偏初始化均降低 F1，未找到可用变体。

## 3. Clause Encounters of the Third Kind: Can LLMs Replace Language Teachers?

- Source: arxiv
- arXiv ID: 2608.16286
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.16286v1
- PDF: https://arxiv.org/pdf/2608.16286v1
- DOI: https://doi.org/10.48550/arXiv.2608.16286

### Authors

Kristina Šekrst, Ana Kovačić

### Abstract

While various organizations now actively encourage LLM use in classrooms, we still lack rigorous, systematic evaluations of how well these models actually perform the fundamental tasks of language pedagogy. This paper examines whether state-of-the-art LLMs can deliver the kind of corrective feedback and methodological explanations that language learners need. The study tests multiple large language models on their ability to identify, correct, and explain common learner mistakes in English, by systematically varying model parameters to investigate how these technical adjustments affect output quality, pedagogical clarity, and consistency, along with using retrieval-augmented generation to query methodological data. The evaluation employs automated metrics (GLEU, BERTScore) but also human expert judgments to capture dimensions that purely computational measures miss: linguistic nuance, cultural sensitivity, and instructional appropriateness. While models demonstrate impressive surface-level correction abilities, their explanations often lack the terminological and domain knowledge that effective language teaching requires, suggesting that current enthusiasm for AI-assisted language learning may be outpacing our understanding of these systems' actual pedagogical competence.

### 中文一句话结论
当前最先进的LLM能有效纠正英语表层错误，但缺乏语言教学所需的深层术语知识、领域知识及教学适当性，无法替代人类语言教师。

### English TL;DR
State-of-the-art LLMs can correct surface-level learner errors but lack the deep pedagogical, terminological, and domain knowledge required for effective language teaching, and thus cannot replace human language teachers.

### 中文详细总结
本研究系统评估了GPT、Claude、Gemini等三个最先进的大语言模型在英语教学中执行纠错反馈和方法解释等核心任务的能力。研究者构建了一个包含20个句子的测试集，这些句子来自ESP（专门用途英语）课堂中学生的常见错误，涵盖主谓一致、冠词、混合语法错误及ESP术语与语体四个类别。模型被要求识别错误、提供修正并给出解释。研究通过系统改变生成参数（温度、top-k、top-p）及使用检索增强生成（RAG）来观察输出质量、教学清晰度和一致性的变化。评估同时采用自动化指标（GLEU、BERTScore）和人类专家判断。结果表明，虽然模型在语法表层错误纠正上表现优异（如GPT-4o达到97%的语法纠错率），但在ESP术语和语体判断上表现不佳（如GPT-4o仅11%），且其解释时常缺乏术语准确性和领域知识。此外，GPT-5生成的测试题与教师设计的测试题对比显示，学生完成LLM生成测试用时更短，但深层学习效果可能不足。研究指出，对AI辅助语言学习的热情可能已超过对其实际教学能力的理解。

### 方法 / 贡献
- 构建了包含20个常见英语学习者错误的测试集（15句语法错误+5句ESP术语/语体错误），覆盖四个类别。
- 对GPT-4o、GPT-5、Claude Opus 4.6、Gemini 2.5 Pro等多个模型进行系统测试，变化生成参数（温度、top-k、top-p）并加入RAG。
- 采用双轨评估：自动化指标（GLEU、BERTScore）与人类专家（应用语言学、ESP领域专家）判断相结合，捕捉教学适当性、文化敏感性等计算指标无法衡量的维度。
- 贡献了针对LLM教学能力的实证评估框架，揭示了技术能力与教学能力之间的差距。

### 实验或数据
- 实验一：20个句子测试集，来自生物技术本科ESP课程常见错误，由两名独立评分者（应用语言学背景）和一名ESP领域专家评估。
- 实验二：GPT-5生成与教师设计的同一课内测试题对比，收集了55次（GPT-5生成）和43次（教师设计）学生答题记录，包括完成时间、尝试次数和分数。
- 主要结果：语法纠错率最高达100% (GPT-5)，ESP术语纠错率最高仅47% (GPT-5)；RAG显著提升术语识别从21%到89%。

### 值得关注点
- 模型在语法纠错上表现接近人类，但ESP术语和语体判断能力明显不足，显示LLM缺乏领域知识。
- RAG（检索增强生成）能显著提升术语识别，但整体教学定性仍不足。
- 学生使用LLM生成测试题时完成时间更短，可能反映浅层认知加工，而非深层学习。
- 人类专家评估揭示了自动化指标无法捕捉的语言细微差别、文化敏感性和教学适当性维度。

### 局限性
- 测试集规模较小（仅20句，且集中于英语ESP领域），限制了结论的泛化性。
- 仅评估了英语语言教学，未涉及其他语言或更广泛的教学场景。
- 模型测试时未提供学习者特定背景信息（与人类教师接手新班级时类似），但实际教学情境中教师通常具有更多上下文。
- 研究未测量LLM反馈对学习者长期学习结果的影响。

## 4. LLM Safety Alignment in Low-Resource Languages: A Systematic Literature Review

- Source: arxiv
- arXiv ID: 2608.14626
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.14626v1
- PDF: https://arxiv.org/pdf/2608.14626v1
- DOI: https://doi.org/10.48550/arXiv.2608.14626

### Authors

Valdini Douglace Lemofouet, Blessing Ngozi Uzor, Paula Chikaodinaka Anyanwu, Danielle Blanche Kapsa, Sukairaj Hafiz Imam, P Sam Sahil, Abigail Oppong, Tassallah Abdullahi, Clemencia Siro, Idris Abdulmumin, Seid Muhie Yimam, Shamsuddeen Hassan Muhammad

### Abstract

Large Language Models (LLMs) have achieved substantial progress in safety alignment, yet their safety guarantees remain significantly weaker in low-resource and multilingual settings than in high-resource languages. In this paper, we conduct a Systematic Literature Review (SLR) of LLM safety alignment in low-resource languages by adopting the PRISMA 2020 methodology. Out of roughly 1,500 papers identified from Semantic Scholar, arXiv, and OpenAlex, 50 relevant studies have been selected and analyzed. Our review is organized around four themes: safety alignment methods, multilingual safety risks, evaluation benchmarks, and cross-lingual transferability. We further propose a taxonomy of safety alignment approaches based on three adaptation mechanisms: data adaptation, objective optimization, and mechanistic alignment. Across literature, translated English benchmarks fail to sufficiently represent culturally rooted harms, and multilingual models are more vulnerable to cross-lingual jailbreaks, code-switching attacks, and safety degradation in underrepresented languages. These failures are driven by several key factors, including uneven multilingual pre-training coverage, insufficient native-language preference data, poor transfer of safety representations, and a lack of culturally aware evaluation frameworks. The review also notes that many low-resource languages, especially African languages, have fewer safety benchmarks available than other multilingual regions. Overall, the results reveal a persistent multilingual safety gap, and suggest that future progress will require culturally grounded benchmarks, participatory data collection, balanced multilingual pre-training, and scalable multilingual alignment methods.

### 中文一句话结论
本文通过系统性文献综述发现，大语言模型在低资源语言中的安全对齐显著弱于高资源语言，存在持续的多语言安全差距。

### English TL;DR
This systematic literature review finds that LLM safety alignment is significantly weaker in low-resource languages due to a persistent multilingual safety gap, driven by factors such as uneven pre-training coverage, insufficient native-language data, and a lack of culturally aware benchmarks, and calls for culturally grounded evaluation, participatory data collection, and scalable multilingual alignment methods.

### 中文详细总结
本研究采用PRISMA 2020方法论，对LLM在低资源语言中的安全对齐进行了系统性文献综述。从Semantic Scholar、arXiv和OpenAlex检索的约1500篇论文中，筛选出50篇相关研究进行分析。综述围绕四个主题展开：安全对齐方法、多语言安全风险、评估基准和跨语言可迁移性。研究发现，翻译自英语的基准无法充分代表文化根源性危害，多语言模型在跨语言越狱、代码切换攻击和低代表性语言中的安全退化方面更为脆弱。这些失败由多个关键因素驱动，包括不均衡的多语言预训练覆盖、不足的本地语言偏好数据、安全表征的差迁移以及缺乏文化感知的评估框架。综述指出，许多低资源语言（尤其是非洲语言）的安全基准比其他多语言区域更少，结果揭示了持续存在的多语言安全差距。

### 方法 / 贡献
- **方法论**：采用PRISMA 2020系统性文献综述框架，从约1500篇论文中筛选出50篇进行综合分析
- **分类体系**：提出基于三种适应机制的安全对齐方法分类：数据适应、目标优化和机制对齐
- **研究主题**：围绕四个维度综述：安全对齐方法、多语言安全风险、评估基准和跨语言可迁移性
- **贡献**：首次专门针对非洲及低资源语言进行LLM安全对齐的系统性文献综述

### 实验或数据
- 检索来源：Semantic Scholar、arXiv和OpenAlex
- 初始检索：约1500篇论文
- 去重后：1300篇
- 筛选过程：Python自动过滤 → 242篇候选 → LLM评估（Claude Sonnet）筛选 → 两轮人工审核
- 最终纳入：50篇相关研究

### 值得关注点
1. **安全差距持续性**：低资源语言的安全保障显著弱于高资源语言
2. **文化危害缺失**：翻译自英语的基准无法捕捉文化特定危害
3. **跨语言越狱**：仅将有害英文提示翻译成低资源语言即可实现79%的越狱成功率
4. **非洲语言资源匮乏**：非洲语言的安全基准比其他多语言区域更少
5. **三种对齐机制**：数据适应、目标优化和机制对齐是主要适应策略
6. **未来方向**：需要文化根基基准、参与式数据收集、均衡多语言预训练和可扩展的多语言对齐方法

### 局限性
1. **文献覆盖范围**：仅从三个数据库检索，可能遗漏其他来源的相关研究
2. **筛选主观性**：虽然采用PRISMA方法，但LLM辅助筛选和人工审核仍可能引入选择偏差
3. **语言代表性**：现有文献主要关注少数低资源语言，对更多低资源语言的研究不足
4. **缺乏实验验证**：作为综述论文，未进行原创实验验证所提方法的有效性
5. **时效性**：由于发布时间限制，可能未涵盖最新研究进展

## 5. Augmenting Text to Increase Translation Difficulty

- Source: arxiv
- arXiv ID: 2608.15932
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.15932v1
- PDF: https://arxiv.org/pdf/2608.15932v1
- DOI: https://doi.org/10.48550/arXiv.2608.15932

### Authors

William Kalikman, Šimon Sukup, Michal Tešnar, Vilém Zouhar

### Abstract

As state-of-the-art machine translation models saturate standard benchmarks, the field needs more challenging evaluations to distinguish between models of varying quality. We propose augmenting existing benchmarks to increase translation difficulty by combining adversarial optimization with a differentiable translation difficulty estimator. Our Adversarial Translation Optimization (ATO) uses gradients from a combined difficulty and fluency objective to iteratively replace tokens. Because each step branches over candidate substitutions at every position, optimization becomes a tree search problem, which we address with Beam Search. ATO offers a gradient-based alternative to LLM-based dataset creation without LLM prompting, expensive human curation, or task-specific model training. Our ATO-modified benchmark lowers average translation quality (xCOMET) from 0.93 to 0.82, compared to 0.88 for paraphrasing and 0.86 for a zero-shot baseline. Human evaluation shows the modified texts are somewhat less natural than the baselines but remain reasonably grammatical and plausible while being substantially harder to translate. We release two datasets of 350 English texts each, generated by our methods, as well as the code.

### 中文一句话结论
本文提出对抗翻译优化（ATO），一种基于梯度的 beam search 方法，在不依赖 LLM 提示或人工标注的情况下，通过联合优化翻译难度和流畅度，自动增强现有基准以生成更难翻译的评测文本。

### English TL;DR
This paper introduces Adversarial Translation Optimization (ATO), a gradient-based method using beam search and a combined difficulty-fluency objective to iteratively replace tokens in source texts, creating more challenging benchmarks for machine translation evaluation.

### 中文详细总结
当前机器翻译模型在标准基准上趋于饱和，需要更具挑战性的评测来区分模型质量差异。本文提出对抗翻译优化（ATO），核心思想是利用可微的翻译难度估计器（Sentinel）结合流畅度约束，通过 beam search 和贪婪坐标梯度策略，迭代替换源文本中的 token，生成更难翻译但仍保持语法合理性的文本。ATO 提供两种变体：ATO-Direct 限制替换为整词，ATO-TwoPhase 先优化难度再优化流畅度。实验显示，ATO 修改后的基准将平均翻译质量（xCOMET）从 0.93 降至 0.82，优于基线和零样本基线。人类评估确认修改文本虽然自然度略低，但语法合理且可读，翻译难度显著增加。

### 方法 / 贡献
1. 提出 ATO 方法：无需 LLM 提示或人工标注，通过梯度信号和 beam search 自动生成更难翻译的文本。
2. 设计联合优化目标：结合翻译难度估计器（Sentinel）和流畅度正则项（如 CoLA 或困惑度），避免生成无意义文本。
3. 两种变体：ATO-Direct（仅整词替换，后按困惑度筛选）和 ATO-TwoPhase（两阶段优化，先难后顺）。
4. 开源自研数据集（各 350 条英文文本）和代码。

### 实验或数据
- 使用 200 条种子文本，翻译至 5 种目标语言，由 3 个不同能力的翻译模型评估。
- 基线对比：原始文本、释义（paraphrasing）、零样本改写。
- 指标：xCOMET（无参考翻译质量估计）。
- 结果：原始 0.93 → ATO-TwoPhase 0.82，释义 0.88，零样本 0.86。
- 人类评估：13 名多语参与者确认 ATO 文本更难译，自然度略低但合理。

### 值得关注点
1. 将对抗优化从 LLM 安全领域迁移至机器翻译评测，思路新颖。
2. 联合优化难度与流畅度，避免单纯追求难度导致无意义文本。
3. 提供开源数据和代码，可复现。
4. 人类评估验证了实际翻译难度提升。

### 局限性
1. 仅使用 Sentinel 作为难度估计器，依赖其准确性。
2. 人类评估显示自然度略低于基线，可能影响实际使用。
3. 评估仅限于 5 种语言和 3 个翻译模型，泛化性未充分验证。
4. 未与基于 LLM 的方法直接比较（论文称需大量提示工程，但未提供定量对比）。
5. 数据集规模较小（各 350 条），可能受统计噪声影响。

## 6. Why Summaries Turn Neutral: Policy Attribution for Sentiment Drift in Reinforcement Learning from Human Feedback

- Source: arxiv
- arXiv ID: 2608.15530
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.15530v1
- PDF: https://arxiv.org/pdf/2608.15530v1
- DOI: https://doi.org/10.48550/arXiv.2608.15530

### Authors

Mikhail Krasitskii, Alexander Gelbukh, Olga Kolesnikova, Grigori Sidorov

### Abstract

Reinforcement learning with human feedback (RLHF) aligns LLMs with human preferences, improving summarization fluency and safety, but causes sentiment drift: overly neutral summaries stripped of emotional nuance. We diagnose why RL acts as a sentiment neutralizer and present Policy Attribution, a framework using gradient and logit decomposition to trace drift to reward model (RM) signals and KL (Kullback-Leibler) penalty. Sentiment drift reflects a strategic bias toward "low-risk" tokens maximizing expected rewards under preference uncertainty (Stiennon et al., 2020; Gao, Schulman, and Hilton, 2023). On Reddit TL;DR and CNN/DailyMail, RLHF summaries get higher rewards but show 30-40% lower sentiment variance. Cross-lingual analysis across eight languages shows language-independent drift, with morphologically richer languages more suppressed (Krasitskii et al., 2026). We propose and validate a sentiment-aware regularization technique reducing drift by 18-22% without harming summary quality. The code and toolkit will be public.

### 中文一句话结论
本文通过“Policy Attribution”框架诊断出RLHF导致摘要情感漂移（过度中性化）的主要原因是KL惩罚（约82%），并提出情感感知正则化技术可减少漂移18-22%而不损害质量。

### English TL;DR
RLHF causes summarization sentiment drift (over-neutralization), and this paper introduces Policy Attribution using gradient/logit decomposition to trace the cause primarily to KL regularization (~82% of suppression) rather than reward model signals. The proposed sentiment-aware regularization reduces drift by 18–22% without harming summary quality, validated on Reddit TL;DR and CNN/DailyMail across eight languages.

### 中文详细总结
RLHF虽然提升了摘要的流畅性和安全性，但导致“情感漂移”——摘要变得过度中性，失去情感细节。本文提出**Policy Attribution**框架，通过梯度和logit分解追踪漂移来源，发现KL惩罚（β项）是主要驱动因素（约82%），而奖励模型信号贡献较小。情感漂移反映了模型在偏好不确定性下选择“低风险”词元的策略性偏见。实验在Reddit TL;DR和CNN/DailyMail上进行，RLHF摘要获得更高奖励但情感方差降低30-40%。跨语言分析（8种语言）显示漂移是语言无关的，但形态更丰富的语言受抑制更严重。本文还验证了Direct Preference Optimization (DPO)同样存在情感抑制。提出的**情感感知KL正则化**技术通过放松情感标记的KL惩罚，在不降低摘要质量（ROUGE-L）前提下将漂移减少18-22%。

### 方法 / 贡献
1. **Policy Attribution框架**：将策略梯度分解为奖励、KL惩罚和PPO裁剪三个组成部分，使用Integrated Gradients逐token计算各成分的归因分数。
2. **情感漂移的量化定义**：通过情感方差（SV）和Jensen-Shannon散度（JSD）衡量情感分布的偏移。
3. **跨语言诊断**：对8种类型学差异显著的语言（英语、阿拉伯语、芬兰语等）进行系统性分析。
4. **情感感知KL正则化**：对情感标记放宽KL惩罚，减少中性化趋势。
5. 公开Policy Attribution工具包。

### 实验或数据
- **数据集**：Reddit TL;DR（非正式文本）和CNN/DailyMail（新闻文本），多语言分析使用平行翻译子集。
- **模型**：Llama-3-8B和Mistral-7B-v0.1，使用PPO和DPO两种对齐方法。
- **主要结果**：
  - RLHF摘要情感方差降低30-40%，JSD显示分布显著偏移。
  - KL惩罚贡献约82%的情感抑制，奖励模型仅贡献少量。
  - 提出的正则化技术在两个数据集上减少情感漂移18-22%，ROUGE-L无明显下降。
  - DPO同样产生情感抑制，随β增大而加剧。
- **超参数**：学习率1e-5、批大小64、PPO轮数4、β ∈ {0.05, 0.1, 0.2}。

### 值得关注点
- 提供了从归因角度系统诊断RLHF副作用的可解释方法，而非仅定性描述。
- 发现KL惩罚而非奖励模型是情感中性化的主因，修正了以往直觉。
- 跨语言分析揭示形态丰富语言（如芬兰语）受抑制更重，提示语言类型学因素的影响。
- 情感感知正则化是轻量级、有效的缓解方案，且不牺牲摘要质量。

### 局限性
- 归因分析基于特定模型（Llama-3-8B、Mistral-7B）和梯度近似，可能不完全推广到其他架构。
- 情感检测依赖预训练分类器，其偏误可能影响度量。
- 只测试了PPO和DPO，未涵盖KTO等其他对齐方法。
- 单语言数据集（英文）经过翻译进行多语言评估，原文情感标记在翻译中可能损失。
- 情感感知正则化的参数选择（哪些token视为情感标记）可能引入新的敏感度。

## 7. Language models suffer from a curse of ambiguity

- Source: arxiv
- arXiv ID: 2608.15448
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.15448v1
- PDF: https://arxiv.org/pdf/2608.15448v1
- DOI: https://doi.org/10.48550/arXiv.2608.15448

### Authors

Nicolas Zucchet, Hyun Dong Lee, Scott Linderman

### Abstract

Large language models increasingly rely on sampling as a driver of their own improvement, making the fidelity of their learned distributions more critical than ever. Yet, not all distributions are equally easy to learn. In this work, we identify a curse of ambiguity: in large language models, and more broadly in all neural networks that produce discrete probability distributions, the more ambiguous a next-token distribution is, the harder it is to learn accurately. Through an extensive theoretical analysis, we trace this curse to architectural and learning roots. More ambiguous distributions require more capacity to be stored, larger embeddings to be represented, more steps to be fitted, and amplify token-sampling noise. We validate these findings on synthetic tasks with controlled ground truth and observe the same signatures in language models trained on real data. Our results provide a new perspective on the statistical capabilities of large language models and a practical framework for when to trust their output distribution.

### 中文一句话结论
本文发现大型语言模型中存在“歧义诅咒”：下一词分布越歧义（均匀分布在越多候选词上），模型就越难准确学习该分布。

### English TL;DR
The paper identifies a "curse of ambiguity" in language models, showing that more ambiguous next-token probability distributions are inherently harder to learn due to increased capacity, embedding, and optimization demands, as well as amplified noise.

### 中文详细总结
本文提出并形式化了“歧义诅咒”：在大型语言模型（以及所有输出离散概率分布的神经网络）中，下一词分布的歧义程度越高，准确学习的难度就越大。歧义通过支持集大小（或熵指数）度量。作者从架构和学习两个根源分析该诅咒：架构上，更歧义的分布需要更多模型容量（参数数量）来存储，且需要更大的嵌入维度来表征；学习上，它们需要更多的优化步数来拟合，同时会放大从分布中采样时的噪声。理论分析基于线性头部（softmax分类层）和均匀支持集的简化模型，并在可控的合成任务以及真实数据训练的语言模型上验证了理论预测。结果表明，更歧义的分布会使容量需求随歧义度线性增加（容量 ∝ hd/k），所需嵌入维度至少线性增长，且学习速度更慢、采样噪声更大。这些发现为理解语言模型的统计能力提供了新视角，也为何时信任模型的输出分布提供了实用框架。

### 方法 / 贡献
- 识别并形式化了大型语言模型中的“歧义诅咒”。  
- 从架构根源（容量、嵌入维度）和学习根源（收敛步数、采样噪声）分析该诅咒，提供了理论推导（基于线性头部和Hebbian模型）。  
- 通过合成任务（带可控真实分布）和真实数据训练的语言模型进行实验验证，并论证结论可推广至更大模型。

### 实验或数据
- 合成任务：控制真实下一词分布的支持集大小（歧义度），验证容量、嵌入维度、收敛步数、噪声放大的理论预测。  
- 真实数据：在语言模型（如小型Transformer）上观察到了与合成任务一致的特征（如歧义度升高时损失更大、收敛更慢）。  
- 未见大规模实验，但论文论证了结果应随模型规模扩展。

### 值得关注点
- 揭示了语言模型校准中的一个基础局限：歧义度直接影响学习难度，这与模型规模无关。  
- 对依赖模型采样（如自改进、推理时扩展、强化学习后训练）的应用具有重要警示：在歧义高的上下文中，模型输出的分布可能不可靠。  
- 提供了一个实用框架：根据歧义度判断是否信任模型的输出分布，例如在歧义高时谨慎使用温度缩放或采样。

### 局限性
- 理论分析主要基于线性头部和均匀支持集的简化假设，真实分布的歧义形式可能更复杂（如非均匀、长尾）。  
- 实证验证限于中小规模语言模型，对更大模型（如数百亿参数）的直接验证尚缺。  
- 论文未深入探讨如何在实际系统中缓解歧义诅咒（如通过架构改进或训练策略）。  
- 分析聚焦于下一词分布的预测，未考虑长程依赖或更深层表示的交互效应。

## 8. TAHB: A Comprehensive Benchmark for Text-Attributed Hypergraph Learning

- Source: arxiv
- arXiv ID: 2608.15055
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.15055v1
- PDF: https://arxiv.org/pdf/2608.15055v1
- DOI: https://doi.org/10.48550/arXiv.2608.15055

### Authors

David Yoon Suk Kang, JungHyun Kim, Juhyun Jeon, Sang-Wook Kim

### Abstract

Hypergraphs effectively model higher-order groupwise relationships beyond pairwise interactions, while pretrained language models (PLMs) and large language models (LLMs) provide rich semantic understanding from textual attributes. However, research on combining language models with hypergraph learning remains limited due to the lack of public text-attributed hypergraph benchmarks. To address this limitation, we present TAHB (Text-Attributed Hypergraph Benchmark), the first public benchmark integrating hypergraph structures and raw textual attributes. TAHB contains 10 real-world datasets from four domains - e-commerce, academia, movies, and politics networks - enabling systematic evaluation of text-aware hypergraph representation learning. Experimental results show that TAHB preserves key structural properties of real-world hypergraphs and consistently reproduces performance tendencies observed in existing benchmarks. Furthermore, experiments under both LLM-as-Enhancer and LLM-as-Predictor settings demonstrate that LLM-enhanced textual semantics improve hypergraph learning performance, while structural and textual information jointly provide the best setting for LLM-based prediction. Our benchmark provides a foundation for future research at the intersection of hypergraph learning and language models.

### 中文一句话结论
TAHB 是首个公开的文本属性超图基准，包含来自四个领域的10个真实世界数据集，验证了结合大语言模型语义与超图结构可一致提升学习性能。

### English TL;DR
TAHB is the first public benchmark integrating hypergraph structures and raw textual attributes across 10 real-world datasets from four domains, demonstrating that combining LLM-enhanced semantics with hypergraph topology consistently improves learning performance.

### 中文详细总结
TAHB（Text-Attributed Hypergraph Benchmark）是首个公开的文本属性超图基准，将超图结构与原始文本属性相结合。它包含来自电子商务、学术、电影和政治四个领域的10个真实世界数据集。每个节点（如论文、产品、电影、法案）都附有丰富的原始文本（如摘要、描述、评论、内容），超边捕捉自然发生的群体关系（如合著、共享评审、共同演员、共同发起）。实验验证了TAHB保持了真实超图的关键结构属性，并复现了现有非文本超图基准中的性能趋势。此外，在LLM-as-Enhancer（LLM作为增强器）和LLM-as-Predictor（LLM作为预测器）两种设置下，LLM增强的文本语义均显著提升了超图学习性能，且结构与文本信息联合为LLM预测提供了最佳设置。该基准为超图学习与语言模型的交叉研究提供了基础。

### 方法 / 贡献
- 提出首个公开的文本属性超图基准TAHB，包含10个来自四个领域的真实数据集，每个数据集均提供原始文本和超图结构。
- 系统验证了基准的结构特性、文本分布和性能趋势与已有基准一致，确保可靠性。
- 从两个角度（LLM-as-Enhancer 和 LLM-as-Predictor）研究了LLM与超图学习的整合，证明了语义与结构的强互补性。

### 实验或数据
- 数据：10个真实世界超图数据集，来源于e-commerce、academia、movies、politics四个领域。节点附带原始文本（如论文摘要、产品描述、电影元数据、法案内容），超边基于自然群体关系（如合著、共同评审、共同演员、共同发起）构建。
- 实验：验证了结构特性保持、文本分布与现有TAG数据集相似、文本-节点语义一致性高。下游任务（节点分类和超边预测）实验表明，在两种LLM设置下，结合文本和结构均优于单独使用任一信息。所有代码、数据和实验管线已公开。

### 值得关注点
- 首次将原始文本属性与超图结构结合在公开基准中，填补了现有基准的空白。
- LLM增强的语义（作为增强器）能显著提升传统超图神经网络性能。
- 在LLM作为预测器时，联合使用超图拓扑和文本语义在所有数据集上达到最优，证明两者强互补。

### 局限性
- 目前仅包含四个领域（电商、学术、电影、政治）和10个数据集，可能无法覆盖所有应用场景。
- 主要评估节点分类和超边预测任务，未涉及其他潜在任务（如聚类、推荐等）。
- 未详细分析超图大小、文本长度或LLM版本对性能的具体影响。

## 9. Beyond Tokens: A Survey on Decoding Methods for Large Language and Vision-Language Models

- Source: arxiv
- arXiv ID: 2608.14797
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.14797v1
- PDF: https://arxiv.org/pdf/2608.14797v1
- DOI: https://doi.org/10.48550/arXiv.2608.14797

### Authors

Haoran Wang, Xiongxiao Xu, Philip S. Yu, Kai Shu

### Abstract

Large language models (LLMs) and large vision-language models (LVLMs) have demonstrated impressive generative capabilities, yet ensuring their outputs align with user intent is still challenging. While most existing approaches address this issue at the training stage, inference-time approaches like decoding methods offer a more efficient and scalable solution. Decoding methods control model generation by guiding token-level selection, performing sequence-level generation, or generating tokens in parallel to accelerate the process. In this survey, we identify three emerging paradigms from recent works on decoding methods for LLMs and LVLMs, provide a systematic review of these methods, highlight ongoing challenges, and discuss potential future research directions. Our goal is to underscore the efficiency and effectiveness of decoding methods and offer a practical view of their applications. Paper lists and more resources on decoding methods for LLMs and LVLMs can be found at https://github.com/wang2226/Awesome-LLM-Decoding.

### 中文一句话结论
本综述系统回顾了大型语言模型与多模态视觉语言模型中的解码方法，归纳出三种新兴范式（词元级、序列级、并行解码），并指出其无需重新训练即可高效提升生成对齐性。

### English TL;DR
This survey categorizes and reviews inference-time decoding methods for large language models and vision-language models, highlighting three emerging paradigms—token-level, sequence-level, and parallel decoding—as efficient, model-agnostic approaches to improve generation alignment without retraining.

### 中文详细总结
该综述聚焦于大语言模型（LLM）和大型视觉语言模型（LVLM）的推理时解码方法。文章指出，尽管训练阶段对齐方法（如微调、强化学习）有效，但解码方法提供更高效、可扩展的解决方案。作者识别出三种新兴范式：词元级解码（如对比搜索、对比解码）、序列级解码（如基于数据集搜索的方法）和并行解码（如推测解码）。文章系统梳理了这些方法在减轻幻觉、提升安全性、增强视觉接地、改进推理、提高鲁棒性及加速生成等方面的应用，并讨论了当前挑战（如泛化性、评估标准）和未来方向。虽然同时涵盖文本与视觉语言模型，但当前解码方法研究仍以纯文本为主。

### 方法 / 贡献
本文贡献在于对LLM和LVLM推理时解码方法进行全面分类与系统综述：归纳出三种新兴范式，总结其经典与当代变体（如贪心搜索、束搜索、top‑k/top‑p采样、对比解码、推测解码等），并展示了这些方法在多种下游任务（幻觉缓解、安全对齐、推理增强等）中的有效性。文章还提供了方法分类图与在线资源列表。

### 实验或数据
本文为一篇综述论文，未开展新的实验或使用特定数据集。文中引用的实验结果均来自参考文献，不包含原始实验数据或评估基准。

### 值得关注点
1. **高效性与可迁移性**：解码方法无需重新训练或修改模型参数，可即插即用于不同规模、不同架构的模型。  
2. **对齐能力**：通过调整生成过程中的概率分布或搜索策略，可显著改善生成结果与用户意图的一致性（如减少幻觉、增强安全性）。  
3. **可视化/多模态扩展**：虽以文本为主，但已初步延伸至视觉语言模型，例如用于改善视觉定位和图像描述生成。  
4. **解释性**：部分解码方法（如对比解码）能揭示模型内部推理过程，提升可解释性。

### 局限性
1. **领域覆盖不平衡**：当前研究主要集中于纯文本解码，视觉、视频与代码等模态的解码方法尚属新兴扩展，综述深度有限。  
2. **评估标准不一**：缺乏统一的评价指标来衡量不同解码方法在多样性、质量、对齐性等方面的综合表现。  
3. **方法泛化性**：部分先进解码方法（如基于监督信号的序列级解码）需要额外训练或外部知识库，可能限制实际部署。  
4. **动态挑战**：随着模型规模增长，解码方法的计算开销（如并行解码中的验证器）仍需进一步优化。

## 10. Multi-Granularity Sentiment Integration for LLM-Based Multimodal Sentiment Analysis

- Source: arxiv
- arXiv ID: 2608.16201
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.16201v1
- PDF: https://arxiv.org/pdf/2608.16201v1
- DOI: https://doi.org/10.48550/arXiv.2608.16201

### Authors

Shanshan Lin, Yuesheng Wu, Chao Chen, Yizhe Yang, Zhihao Chen, Zexian Yang, Xiangwen Liao

### Abstract

Multimodal sentiment analysis (MSA) aims to predict sentiment polarity and intensity from heterogeneous inputs such as text, audio, and vision. While large language models (LLMs) offer strong semantic priors for MSA, effectively incorporating audio and visual signals effectively remains challenging. A key challenge is that audio and visual sentiment cues evolve over different temporal scales, yet many LLM-based methods compress these signals through shallow projection or coarse pooling before fusing them with text, which can weaken cross-modal alignment and erase fine-grained affective information. We propose MGSI, a multi-granularity sentiment integration framework for LLM-based MSA. MGSI first encodes audio and visual streams at short-, medium-, and long-range temporal scales, preserving both local variations and global affective trends. It then refines non-text features through text-guided alignment, and applies polarity- and intensity-aware enhancement to better handle ambiguous and near-neutral samples. The resulting multimodal representation is finally compressed into a small set of pseudo-tokens for efficient conditioning of a frozen LLM. Experiments on four public benchmarks show that MGSI substantially outperforms frozen-LLM baselines and remains competitive with strong multimodal methods. Further ablation and sensitivity analyses support the effectiveness of multi-granularity temporal modeling, text-guided refinement, and adaptive sentiment calibration.

### 中文一句话结论
MGSI通过多粒度时间编码和文本引导对齐，在保持低参数量下显著提升了基于冻结大语言模型的多模态情感分析性能，在四个公开基准上超越同类方法。

### English TL;DR
MGSI (Multi-Granularity Sentiment Integration) proposes a lightweight framework for LLM-based multimodal sentiment analysis that preserves sentiment-relevant temporal structures from audio and visual streams at multiple scales before compressing them into pseudo-tokens for a frozen LLM, achieving state-of-the-art results on four benchmarks.

### 中文详细总结
多模态情感分析旨在从文本、音频和视觉输入中预测情感极性与强度。现有基于大语言模型（LLM）的方法在融合非文本模态时，常通过浅层投影或粗粒度池化压缩音频和视觉信号，导致跨模态对齐弱化、情感细节丢失。本文提出MGSI框架，核心思路是在将多模态表示压缩为伪令牌注入冻结LLM之前，先显式保留音频和视觉流中的情感相关时间结构。具体地，MGSI对每个非文本模态使用短、中、长三个时间尺度的编码器分别建模局部波动、中等模式与长期演变；随后通过文本引导的门控机制对齐非文本特征，并引入非中性分类器和自适应情感校准器分别强化极性判别与处理模糊样本；最终将融合表示压缩为少量伪令牌，高效地调节冻结LLM。实验在CMU-MOSI、CMU-MOSEI、CH-SIMS和CH-SIMSV2四个公共基准上进行，MGSI显著优于各类基于冻结LLM的基线方法，并与全微调方法竞争。

### 方法 / 贡献
- **多粒度时间编码**：为音频和视觉流分别设置短程（1D卷积）、中程（膨胀卷积）、长程（Transformer）三个并行分支，捕获不同时间尺度的情感信息，再通过多头自注意力融合。
- **文本引导对齐**：利用全局文本表示生成模态门控，调节非文本特征，使音频和视觉表示向语义锚点靠拢。
- **非中性分类器**：针对情感强度大于阈值τ的样本，附加二分类损失（正/负），增强极性判别能力。
- **自适应情感校准器**：通过样本依赖的残差校正模块，对融合特征进行微调，提升对近中性模糊样本的处理。
- **多尺度融合适配器**：将校准后的表示通过K个并行MLP分支和1D卷积压缩为4个伪令牌，注入冻结LLM，实现轻量化适配。

### 实验或数据
- 数据集：四个公开多模态情感分析基准：CMU-MOSI（英语）、CMU-MOSEI（英语）、CH-SIMS（中文）、CH-SIMSV2（中文）。
- 对比基线：包括基于LLM的提示方法（如DEVA）、适配器方法（如MSE-Adapter）以及全微调多模态模型。
- 主要结果：MGSI在情感强度回归（MAE/Corr）和分类（Acc-2/F1）指标上一致优于所有冻结LLM基线，且与全微调方法性能相当或更优。
- 消融实验验证了多粒度编码、文本引导对齐、非中性分类器和自适应校准器各模块的有效性。
- 敏感度分析表明模型对短程、中程、长程编码的分支数量及伪令牌数量（M=4）鲁棒。

### 值得关注点
- 明确将“时间-语义压缩”定位为LLM多模态情感分析的关键瓶颈，而非仅关注特征-LLM映射。
- 多粒度设计无需大幅增加参数量，仅通过并行轻量编码器即可保留多尺度情感信息。
- 非中性分类器和自适应校准器的组合为处理极性与模糊样本提供了互补的增强机制。
- 伪令牌压缩策略在保持表示能力的同时，将LLM推理的注意力开销控制在低位。

### 局限性
摘要中未明确讨论方法的局限性。但根据方法设计可推断：模型依赖预提取的音频/视觉特征（而非端到端学习）；多粒度编码需要为每个模态设置超参数（如卷积核大小、膨胀率、Transformer层数）；在极低资源或模态缺失场景下的鲁棒性未被验证。此外，当前仅使用冻结LLM，未探索与全微调LLM的结合潜力。

## Processing Notes

- Duplicate papers skipped: 0