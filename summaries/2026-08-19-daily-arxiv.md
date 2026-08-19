# Daily arXiv - 2026-08-19

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-19T22:35:59
- Paper count: 10

## 1. BEAR-Bench: A Bilingual Enterprise and Academic Reasoning Benchmark for Multimodal Models

- Source: arxiv
- arXiv ID: 2608.17895
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.17895v1
- PDF: https://arxiv.org/pdf/2608.17895v1
- DOI: https://doi.org/10.48550/arXiv.2608.17895

### Authors

Liubov Chubarova, Alexandra Kuleshova, Daniil Volkov, Kirill Sultanov, Alexey Zaytsev

### Abstract

While Multimodal Large Language Models (MLLMs) have made significant strides in visual comprehension, their ability to reason about text-dense, professional documents remains incompletely evaluated. Existing benchmarks emphasize information extraction, require external domain knowledge, or cover professional documents only as one of many settings. They are also largely English- or Chinese-centric, leaving other languages and Russian, in particular, substantially underrepresented. To address these limitations, we introduce BEAR-Bench (Bilingual Enterprise and Academic Reasoning), a self-contained, complex English-and-Russian benchmark comprising 1000 human-annotated questions based on text-rich business and scientific documents. We evaluate 16 proprietary and open-weight MLLMs, including Gemini 3.1 Pro and Qwen3.5-397B, on BEAR-Bench and observe clear headroom even for the strongest systems. Finally, we use the resulting model outputs to compare existing hallucination detection methods, evaluating not only how often models fail on BEAR-Bench but also how reliably those failures can be identified.

### 中文一句话结论
BEAR-Bench 是一个专门评估多模态大模型在英俄双语、文本密集的商业与学术文档上进行多步推理能力的基准，包含1000个人工标注问题，实验表明即使最强模型仍有显著提升空间。

### English TL;DR
BEAR-Bench is a new bilingual (English–Russian) benchmark of 1,000 hand-annotated, multi-step reasoning questions over text-dense business and scientific documents, showing that even top proprietary and open-weight MLLMs leave substantial room for improvement and providing a systematic comparison of hallucination detection methods for such professional-document reasoning.

### 中文详细总结
现有基准主要关注信息提取或依赖外部领域知识，且偏向英文与中文，俄语显著不足。BEAR-Bench 填补了这一空白，包含商业（财务报告、投资者演示、流程图等）和科学（公式、图表、学术版面等）两大领域，共1000个问题，均为自包含、需多步逻辑推理的题目。评估了16个闭源与开源多模态大模型（如 Gemini 3.1 Pro、Qwen3.5-397B），发现即使最强模型也存在明显不足。此外，利用BEAR-Bench对比了多种幻觉检测方法（基于不确定性、表征、隐状态探针以及MLLM作为评判者），分析了不同部署场景下的可靠性。

### 方法 / 贡献
1. **BEAR-Bench基准**：首个针对英俄双语专业文档、需多步推理的基准，问题自包含，无需外部知识。
2. **系统评估**：评估16个多模态大模型，揭示显著性能差距。
3. **幻觉检测对比**：首次在专业文档推理场景下系统比较多种幻觉检测方法，覆盖可访问模型内部信号（开源）与仅可访问输出（闭源）两种部署模式。

### 实验或数据
- 基准包含1000个人工标注问题，其中618个为俄语。
- 使用66,000页图像通过视觉内容分类（含图表、公式等）与文本密度过滤构建候选池，最终由13名领域专家标注。
- 评估了16个模型，包括闭源（如Gemini 3.1 Pro、Claude Opus 4.6）与开源（如Qwen3.5、gemma-4）。
- 实验涵盖幻觉检测方法比较，但论文未提供具体数值结果细节。

### 值得关注点
- **双语覆盖**：同时包含英文与俄语，填补斯拉夫语系在多模态推理基准中的空白。
- **多步推理设计**：问题需跨文本与视觉元素（如图表、表格、公式）进行逻辑推理，而非简单提取。
- **实用导向**：不仅评估模型失败率，还系统研究如何可靠检测这些失败，对实际部署有直接参考价值。

### 局限性
- 基准规模相对较小（1000题），可能限制统计显著性。
- 仅包含商业与科学领域，未覆盖法律、医学等其他专业文档。
- 人工标注过程可能引入主观偏差，尽管使用领域专家。
- 幻觉检测对比未提供详尽数值结果，难以复现或比较具体性能。

## 2. SpeechSense: A Paralinguistic-Focused Dataset for Fine-Grained Speech Sentiment Analysis

- Source: arxiv
- arXiv ID: 2608.17931
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.17931v1
- PDF: https://arxiv.org/pdf/2608.17931v1
- DOI: https://doi.org/10.48550/arXiv.2608.17931

### Authors

Shicheng Ma, Wenqian Cui, Irwin King

### Abstract

Recent advances in AI have revolutionized speech processing, yet effective speech understanding requires discerning not just what is said, but how it is said. Speech Sentiment Analysis plays a critical role in decoding these paralinguistic cues for diverse real-world applications such as recruitment and customer service. However, existing Speech Sentiment Analysis research faces two primary limitations. First, dominant approaches rely on text-centric pipelines that cascade Automatic Speech Recognition with text analysis. This process inevitably discards essential acoustic features like prosody and tone, failing to capture attitudinal meanings in acoustically ambiguous utterances. Second, current benchmarks suffer from a mismatch in label granularity, prioritizing basic emotions (e.g., happy, sad) over the nuanced interpersonal stances (e.g., confident, impatient) necessary for social sensitivity. To address these limitations, we propose a novel dataset, SpeechSense, for fine-grained speech sentiment analysis. Specifically, we define a specialized 8-class taxonomy of interpersonal stances detectable primarily through prosodic cues beyond lexical content alone. We then construct a curated dataset based on this taxonomy, built from high-fidelity speech synthesis and rigorous human validation. Comprehensive experiments across multi-modal LLMs, text-only LLMs, and speech encoders demonstrate that models with acoustic access consistently outperform text-only baselines. These results empirically validate the primacy of acoustic cues in detecting subtle speaker attitudes, highlighting the necessity of SpeechSense. Dataset and supplementary materials are available at https://github.com/Sher13cked/SpeechSense.

### 中文一句话结论
我们提出了SpeechSense，一个聚焦副语言特征的细粒度语音情感分析数据集，通过定义8类人际态度标签并构建语音数据，实验证明利用声学线索的模型在检测细微态度上显著优于纯文本基线，验证了声学特征在此任务中的核心地位。

### English TL;DR
SpeechSense introduces a fine-grained, paralinguistic-focused dataset with an 8-class taxonomy of interpersonal stances, demonstrating through comprehensive experiments that models utilizing acoustic cues consistently outperform text-only baselines in speech sentiment analysis.

### 中文详细总结
现有语音情感分析研究存在两大局限：一是主流方法依赖级联自动语音识别和文本分析的两阶段流程，导致韵律、语调等关键声学特征丢失；二是现有基准数据集仅关注基本情感标签，无法支持对社交互动至关重要的细粒度人际态度（如自信、不耐烦）的识别。SpeechSense提出了一个专为细粒度语音情感分析设计的数据集，定义了一个8类人际态度标签体系，包括自信、紧张、温暖、冷漠、热情、不耐烦、讽刺和中性。数据集通过三步流程构建：（1）设计语义-韵律解耦的中性文本，避免模型从文本内容推断态度；（2）利用高保真文本转语音系统通过角色扮演策略生成带有指定态度的语音；（3）经过严格的人工验证筛选。实验在多种模型架构上证明，能获取声学信息的模型在全部态度类别上显著超越纯文本模型，验证了声学线索在检测细微情感中的必要性。

### 方法 / 贡献
- 定义了细粒度人际态度标签体系，区分8类主要依靠韵律而非字面内容识别的情感状态，并分为四个对比组（内在确定性、高能量效价、社交连接、韵律偏差）
- 构建了包含高保真合成语音与人工验证的数据集，通过语义-韵律解耦的文本设计确保模型关注声学而非语义线索
- 通过多模态LLM、纯文本LLM和语音编码器的系统实验验证声学信息对细粒度情感检测的必要性

### 实验或数据
- 数据集使用Lovo.ai TTS系统合成，经过双阶段人工验证和筛选
- 实验覆盖多模态LLM（Qwen2.5-Omni）、纯文本LLM（Qwen2.5）和语音编码器（Whisper、HuBERT、Wav2Vec2）
- 结果显示带有声学输入的模型在所有8个态度类别上一致优于纯文本基线
- 数据集和补充材料已开源（见论文链接）

### 值得关注点
- 提出了针对人际态度而非基本情感的新分类体系，填补了现有情感分析数据集标签粒度的空白
- 采用语义-韵律解耦策略，确保模型无法依赖文本内容作弊，真实反映声学特征辨识能力
- 对合成语音用于细粒度情感研究的可行性提供了系统验证，为低资源态度数据生成提供了参考方案

### 局限性
- 论文摘要未报告具体的实验评估指标和数据集规模等量化信息
- 依赖于文本转语音合成数据，可能未能完全复现真实录音中副语言表达的自然变化
- 未详细讨论不同态度类别的识别难度差异或模型泛化至真实场景语音的潜力

## 3. Abra: Scaling Diffusion Image Training

- Source: arxiv
- arXiv ID: 2608.17286
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.17286v1
- PDF: https://arxiv.org/pdf/2608.17286v1
- DOI: https://doi.org/10.48550/arXiv.2608.17286

### Authors

Kyle Chickering, Wei-An Lin, Swayam Bhanded, Dan Saunders, Akshat Tripathi, Jiaming Song, Shyamal Buch, Xinchen Yan

### Abstract

Compute-optimal scaling laws guide the training of frontier language models yet remain largely unexplored for visual generation. We present a systematic scaling law study for text-to-image diffusion models using Abra, a controlled family of flow-matching transformers trained across three orders of magnitude worth of compute ($10^{19}$ to $10^{22}$ FLOPs), reaching significantly larger compute budgets than previous works. We demonstrate that diffusion models scale just as predictably as language models but require far more data to train optimally: compute optimality occurs at approximately $200$ image tokens per parameter, ten times the Chinchilla compute-optimal prescription for LLMs. We show that unlike language models, diffusion models are robust to overtraining and that practitioners should err on the side of more data rather than a larger model. Finally, we show that this predictability extends beyond training loss to generative quality metrics, optimal CFG settings, representation quality, and even the shape of the training curves, which collapse onto a universal form.

### 中文一句话结论
文本到图像扩散模型遵循与语言模型相似的缩放定律，但达到计算最优所需的数据量约为语言模型的10倍（约200个图像token每参数），且对过训练具有鲁棒性。

### English TL;DR
The paper systematically demonstrates that text-to-image diffusion models scale predictably like language models but require about ten times more data (200 image tokens per parameter) to achieve compute-optimal performance, with robustness to overtraining and universal scaling behavior across multiple metrics.

### 中文详细总结
本研究通过Abra系列流匹配变换器（60M-2B参数），在10^19至10^22 FLOPs的计算范围内系统研究了文本到图像扩散模型的缩放定律。主要发现包括：
- 扩散模型与语言模型一样可预测，但计算最优时需约200个图像token每参数，是Chinchilla规则（20 token每参数）的10倍。
- 扩散模型对过训练鲁棒，建议实践中优先增加数据而非模型规模。
- 缩放可预测性不仅限于训练损失，还扩展到生成质量指标、最优CFG设置、表示质量以及训练曲线形状（呈通用形式）。
研究还发现表示质量与生成能力以不同速率缩放，并首次观察到扩散模型的缩放塌缩现象。

### 方法 / 贡献
- 提出Abra系列，一组受控的稠密流匹配变换器，涵盖60M至2B参数。
- 通过系统缩放实验推导出计算最优缩放定律，给出200 TPP的实用规则。
- 证明扩散模型训练对过训练鲁棒，并精确刻画该现象。
- 将分析扩展到常见生成指标，发现表示与生成能力异速缩放。
- 首次展示扩散模型存在缩放塌缩。

### 实验或数据
摘要未提供具体实验细节或使用的数据集名称。研究训练了Abra模型族（60M-2B参数），计算量覆盖三个数量级（10^19-10^22 FLOPs），并基于μP进行超参数转移以拟合缩放定律。未提及特定图像数据集或评估基准。

### 值得关注点
- 计算最优数据量需求是语言模型的10倍，对实际训练预算分配有直接指导意义。
- 扩散模型对过训练鲁棒这一特性与语言模型不同，为小模型+大数据策略提供了支持。
- 缩放可预测性跨越损失、生成质量、表示质量等多个维度，增强了扩散模型的可工程化程度。

### 局限性
摘要未明确讨论局限性。基于内容推测：（1）缩放定律可能依赖特定模型架构（稠密流匹配变换器）和计算范围（10^22 FLOPs以下），更大预算或不同架构下的行为需进一步验证；（2）研究聚焦文本到图像生成，未涉及视频、多模态或其它视觉生成任务；（3）未探讨训练数据的组成、质量或多样性对缩放定律的影响。

## 4. Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What Accuracy Cannot See

- Source: arxiv
- arXiv ID: 2608.17744
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.17744v1
- PDF: https://arxiv.org/pdf/2608.17744v1
- DOI: https://doi.org/10.48550/arXiv.2608.17744

### Authors

Ayoub Kirouane, Christos Petrocheilos

### Abstract

Take three frontier mixture-of-experts models (Alibaba, OpenAI, NVIDIA; 3.6-4.0B active parameters each) and fine-tune them to reason in a low-resource language. On accuracy benchmarks almost nothing happens, and the benchmark itself is noise at this scale: changing only the random seed moves the score by 7.7 points, more than every data and recipe effect we measured. That null is our first result. The real changes live where accuracy cannot see. Base models never think in Greek: 0 of 1,000 reasoning traces, even when the question is Greek, so the model answers correctly while reasoning in a form its user cannot read, audit, or correct. After supervised fine-tuning (SFT), every released checkpoint reasons in the language of the question on ~98% of items, one family at 3x fewer tokens, with judged grammaticality improving on all four models and general ability within a few points of each base: nothing was forgotten, and fluency was gained. We propose six behavioural dimensions that make such changes measurable, each gated to reject any metric that correlates with output length, and we report how our own instruments lied: six failures, each caught by a control. What SFT cannot do is fix its own defects: a quarter of answers skip the requested format, answers leak into the reasoning channel, and an explicit "think in English" is obeyed under half the time. Reinforcement learning with verifiable rewards, pre-registered before training, fixes the first two outright (fallback 24% to 2.5%, leak 3.5% to 0.0%, both against a flat random-reward control) and moves the third (+9.1pp), while the Greek reasoning habit survives an accuracy-only gradient untouched. We release five checkpoints. The instruments, the controls and the pre-registration travel to any low-resource language; Greek is the case that let us measure them.

### 中文一句话结论
本研究发现，在低资源语言推理微调中，传统的准确率基准几乎完全无法反映真实行为变化，监督微调（SFT）能够高效教会模型用目标语言进行推理并提升流畅性，但会引入格式缺陷，而基于可验证奖励的强化学习（RLVR）可以有效修复这些缺陷而不损害语言习惯。

### English TL;DR
Standard accuracy benchmarks are nearly uninformative for low-resource language reasoning fine-tuning, as they are dominated by noise (7.7-point seed variation exceeds all data and recipe effects). The real changes occur in behavioral dimensions: SFT teaches models to reason in the target language (~98% of traces) with 3x fewer tokens and improved fluency, but introduces answer-format errors (24% fallback, 3.5% leakage). RLVR fixes these defects (to 2.5% and 0.0% respectively) while preserving the language reasoning habit.

### 中文详细总结
本研究使用三个前沿MoE模型系列（阿里巴巴Qwen3.6-35B-A3B、OpenAI Gpt-OSS-20B、NVIDIA NemotronH-30B-A3B，活跃参数3.6-4.0B），通过LoRA微调使其用希腊语进行推理。主要发现：

1. **准确率基准几乎无用**：仅改变随机种子就导致7.7分的波动，大于所有数据和训练配置的效果。在15个实验配置中，最佳得分76.5仅比基础模型77.2略低。

2. **SFT的关键改变**：
   - 基础模型从不在希腊语中思考（0/1000条推理轨迹）
   - SFT后，~98%的项目使用问题语言推理，一个系列token使用量减少3倍
   - 语法性评价在所有四个模型上均有提升，通用能力几乎没有下降

3. **SFT的缺陷**：
   - 24%的答案跳过请求的格式
   - 3.5%的答案泄漏到推理通道中
   - 明确的"用英语思考"指令仅在不到一半的情况下被遵守

4. **RLVR修复**：
   - 格式回退从24%降至2.5%
   - 答案泄漏从3.5%降至0.0%
   - "用英语思考"遵从率提升+9.1个百分点
   - 希腊语推理习惯在仅准确率梯度下保持不变（98.2%）

5. **六种行为维度**：提出推理语言、token消耗、难易区分、遗忘内容等维度，并设立门控拒绝任何与输出长度相关的指标。

### 方法 / 贡献
- **方法**：LoRA微调（r=32, α=64），单周期，有效batch=32，学习率2×10⁻⁴，专家步长3。训练使用单个NVIDIA DGX B200节点（8×B200 GPU，180GB HBM3e）。
- **语料**：118,092行希腊语数据，分为推理半部分（59,107行，数学、科学、世界知识等8个领域）和直接半部分（58,985行，来自Sophea-Titan-1指令语料，91%希腊语+9%英语）。
- **贡献**：(1) 证明准确率基准在低资源语言推理中的无效性；(2) 提出六种可测量的行为维度；(3) 识别并量化SFT的格式缺陷；(4) 展示RLVR对格式缺陷的修复效果；(5) 发布五个检查点；(6) 提供可迁移至任何低资源语言的工具、控制方法和预注册方案。

### 实验或数据
- **模型**：四个检查点（三个系列），活跃参数3.6-4.0B，总参数20.9-36.0B
- **语料**：118,092行希腊语数据，推理轨迹由LLM生成并通过黄金答案验证（STaR规则），典型产出率60-95%
- **基准**：1,000项三项希腊语探针在思考模式下测量；仅种子变化导致7.7分波动
- **验证**：15个独立训练配置验证，6项仪器失败被控制方法捕获
- 数据来源：公共英语数据集的翻译版，包括OpenR1-Math-220k、ECQA、科学、医学、逻辑等

### 值得关注点
1. **准确率噪声大于效应**：随机种子变化（7.7分）大于所有数据选择和训练配置的效果，这一发现对低资源语言模型评估方法学有根本性影响
2. **SFT实现98%语言匹配**：基础模型零希腊语推理，SFT后几乎全部使用希腊语，且token效率提升3倍
3. **RLVR精准修复格式缺陷**：格式回退从24%降至2.5%，答案泄漏从3.5%降至0.0%，且不破坏语言习惯
4. **六种行为维度**：为低资源语言推理评估提供了超越准确率的可量化工具
5. **可控复现**：发布五个检查点，工具和控制方法可迁移至任何低资源语言

### 局限性
1. 研究仅限于MoE架构模型，结论不推广至密集模型
2. 希腊语作为案例，虽设计了可迁移工具，但其他低资源语言可能需要调整
3. 研究规模限制：所有训练和评估在单个节点上运行，更大规模或其他训练方案可能产生不同结果
4. 语料主要集中在数学（38.2%）和科学（18.7%），常识等维度评估不足
5. LoRA参数和训练配置的具体选择可能影响结果泛化性
6. 推理轨迹由LLM生成而非人工标注，存在质量和一致性限制
7. RLVR实验中"用英语思考"遵从率提升但未达到预注册标准

## 5. What Tokens are Learned when Tokenization is Optimized Jointly with Language Modeling?

- Source: arxiv
- arXiv ID: 2608.17325
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.17325v1
- PDF: https://arxiv.org/pdf/2608.17325v1
- DOI: https://doi.org/10.48550/arXiv.2608.17325

### Authors

Saketh Reddy Vemula, Parameswari Krishnamurthy

### Abstract

Tokenization is a fundamental component of language modeling pipelines. Despite its importance, it is often fixed, even though it significantly impacts model performance across languages. In this work, we analyze what tokens are learned when tokenization is jointly optimized with language modeling. We compare tokenizer-free approaches such as SSLMs and H-Nets with fixed tokenizers across 18 typologically and script-diverse languages. Our results show that joint optimization fundamentally alters token structure. SSLMs recover morphologically aligned and contextually efficient tokens, whereas H-Nets prioritize byte-level efficiency, producing longer tokens with very low overlap with standard subword vocabularies. We further show that tokenization behavior varies across language typologies. Agglutinative languages exhibit more dynamic segmentation patterns while learning. Through downstream evaluation, with pretrained-then-finetuned BERT models, we find that SSLM-based pretokenization consistently reduces language modeling perplexity and achieves competitive downstream performance despite distinct vocabularies. Overall, tokenizer-free approaches optimize for contextual and computational efficiency rather than strict morphological structure, resulting in fundamentally different yet effective vocabularies for downstream NLP.

### 中文一句话结论
联合优化分词与语言建模会从根本上改变所学语素的结构：无分词器方法（如SSLM）倾向于学到形态对齐且上下文高效的语素，而H-Net则优先考虑字节效率，产出较长但词汇重叠度极低的语素。

### English TL;DR
Joint optimization of tokenization with language modeling fundamentally alters token structure, with tokenizer-free approaches like SSLMs learning morphologically aligned tokens and H-Nets learning byte-efficient tokens, producing effective vocabularies that prioritize contextual and computational efficiency over strict morphology.

### 中文详细总结
本文探究了当分词与语言建模联合优化时，模型到底学到了什么样的语素。作者在18种类型和文字多样的语言上，比较了无分词器方法（SSLM、H-Net）与固定分词方法（BPE、ULM等）。结果表明，联合优化从根本上改变了语素结构：SSLM能恢复出形态对齐且上下文高效的语素；H-Net则优先考虑字节层级的压缩效率，产出的语素较长且与标准子词词表重叠度很低。此外，分词行为因语言类型而异——黏着语在学习过程中表现出更动态的分割模式。通过先预训练再微调BERT模型的下游评估，基于SSLM的预分词持续降低了语言建模困惑度，并在下游任务上取得有竞争力的性能，尽管语系词表截然不同。总体而言，无分词器方法优化的是上下文和计算效率而非严格的形态结构，因此产生了根本不同但有效的词表。

### 方法 / 贡献
- **对比方法**：系统比较了两种无分词器架构（SSLM、H-Net）与多种固定分词算法（BPE、ULM、WordPiece、SaGe、Morfessor等）在18种语言上的表现。
- **内在评测**：设计了语素对齐、上下文指数、有效词表大小等指标，分析所学语素的带理属性。
- **下游评测**：在英语、印地语、泰卢固语上预训练并微调BERT（12M参数），评估情感分析、POS、NER、依存句法四项任务。
- **贡献点**：揭示了联合优化下语素结构的变化规律、语言类型学的影响，并验证了无分词器方法在困惑度和下游性能上的有效性。

### 实验或数据
- **语言覆盖**：18种语言，按类型分为黏着语（芬兰语、匈牙利语、蒙古语等9种）、分析/内部曲折语（英语、瑞典语、希伯来语3种）、融合语（梵语、印地语、俄语等6种）。
- **数据来源**：主要使用WMT News Crawl领域新闻语料，并依据字节溢价控制各语言数据量（以英文250K句子为基准）。
- **训练配置**：SSLM约2M参数，H-Net约3M参数；固定分词器使用相同文本训练。
- **下游任务**：在英语、印地语、泰卢固语上，先预训练BERT（12M参数），再微调三个任务（包括情感分析、词性标注、命名实体识别、依存句法分析）。
- **主要结果**：SSLM预分词持续降低语言建模困惑度，并在下游任务上取得与固定分词器竞争的性能。

### 值得关注点
- SSLM学会的语素与形态单元高度对齐，且上下文效率高；H-Net则产出更长的字节级语素，与标准子词词表几乎不重叠。
- 黏着语（如芬兰语、匈牙利语）在学习过程中语素分割模式更动态，而融合语（如印地语、俄语）变化较小。
- 尽管语素结构截然不同，无分词器方法在下游任务上表现不输甚至优于固定分词器，说明上下文和计算效率是更有效的优化目标。

### 局限性
本摘要中未明确讨论局限性。实际论文可能涉及计算开销（如SSLM训练较慢）、模型规模仅限12M参数、下游评测语言较少（仅3种）以及对更大模型或更复杂任务的泛化性待验证。

## 6. Interpretable Humans, Alien LLMs: Expert Analysis of Latent Structures in Assessment Responses

- Source: arxiv
- arXiv ID: 2608.17810
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.17810v1
- PDF: https://arxiv.org/pdf/2608.17810v1
- DOI: https://doi.org/10.48550/arXiv.2608.17810

### Authors

Alona Strugatski, Licol Zeinfeld, Jason Cooper, Shelley Rap, Gil Schwarts, Giora Alexandron

### Abstract

The evaluation of large language models (LLMs) relies heavily on human-designed assessments, implicitly assuming that AI and humans employ similar underlying cognitive constructs. Challenging this assumption, we investigate whether the latent factors governing LLM performance carry the same substantive, human-interpretable meaning as the cognitive constructs governing human learners. Using responses from humans and six LLMs across quantitative reasoning and chemistry assessments, we conducted Exploratory Factor Analysis (EFA) separately for both groups. Subject-Matter Experts (SMEs) then blindly evaluated the resulting factor graphs to ascribe pedagogical meaning to the emerged constructs. SMEs successfully interpreted most of the human-derived factors. Conversely, they could not ascribe meaning to any LLM-derived factors in quantitative reasoning and interpreted only half of the LLM factors in chemistry. By combining data-driven EFA with blind expert interpretation, this framework shows that LLMs frequently operate on statistically opaque mechanisms distinct from human reasoning.

### 中文一句话结论
本研究表明，LLM在教育评估中的潜在因子结构对人类专家而言基本不可解释，与人类学习者的因子结构存在本质差异。

### English TL;DR
This paper shows that latent factors underlying LLM performance on educational assessments are largely uninterpretable to human experts, unlike those for humans, suggesting that LLMs rely on statistically opaque mechanisms distinct from human reasoning.

### 中文详细总结
该研究挑战了“人类和AI使用相似认知结构”的假设，通过探索性因子分析（EFA）和学科专家（SME）盲评，比较了人类与六种LLM在定量推理和化学评估中的潜在因子结构。SME能成功解释大部分人类因子，但无法解释LLM在定量推理中的任何因子，在化学中也只能解释一半因子。这一框架表明，LLM常依赖人类无法理解的统计机制运行。

### 方法 / 贡献
- 对931名学生和979名大学入学考生（分别来自化学和定量推理评估）以及六种多模态LLM（Claude 3.5/4.5、GPT-4o/5.2、Gemini 1.5/3 Pro）的响应数据进行评分与预处理。
- 分别对人和LLM响应组独立进行EFA，基于Kaiser准则确定因子数量（化学:4因子；定量推理:5因子）。
- 将因子加载图盲化、打乱后，由5-6名学科专家进行盲目解释，判断因子是否具有教育意义。
- 主要贡献：提供基于测量视角的LLM评估方法，超越准确率比较，揭示潜结构缺乏可解释性。

### 实验或数据
- 化学评估：22题（最终保留15题），931名学生（平均71.49/100分）；LLM平均76.14/100分。
- 定量推理评估：20题（全部保留），979名考生（平均12.45/20分）；LLM平均11.94/20分。
- LLM响应收集：每模型20次独立响应，共120次/评估，通过零样本提示、PDF形式输入。
- EFA使用最小残差估计和斜交旋转（oblimin）。

### 值得关注点
- 人类因子在两项评估中均完全可解释（SME成功解释全部因子）。
- LLM因子在定量推理中完全不可解释（0/5因子），化学中仅50%可解释（2/4因子）。
- 该方法揭示了LLM评估中“构念等同性”假设的潜在失效，为AI评估提供了新视角。

### 局限性
- 局限于两个特定评估（化学、定量推理），可能不推广至其他领域。
- LLM响应池化跨六种模型，可能掩盖模型间差异。
- 因子保留仅使用Kaiser准则（特征值>1），未采用其他方法验证。
- 人类和LLM数据样本量差异较大（人类>900，LLM为120次响应池化）。
- 未明确分析数据公开性与具体实验材料（如评估题目内容未列出）。

## 7. There is No Theoretical Curse of Multilinguality For Embedding Space Structure

- Source: arxiv
- arXiv ID: 2608.17088
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.17088v1
- PDF: https://arxiv.org/pdf/2608.17088v1
- DOI: https://doi.org/10.48550/arXiv.2608.17088

### Authors

Niyati Bafna, Neha Verma, Vilém Zouhar, Philipp Koehn, David Yarowsky

### Abstract

A central goal of multilingual NLP is to achieve high monolingual performance per language and cross-lingual alignment for large-scale language coverage with a multilingual model. The curse of multilinguality describes the phenomenon of degradation in multilingual model performance as we increase language coverage, posing a threat to the above goal. This paper asks whether multilingual embedding spaces are inherently incapable of achieving perfect multilinguality without a prohibitive increase in required capacity. We first formalize the goal of "perfect multilinguality", embodied in two multilinguality conditions. We then prove that the minimum dimensionality required for perfect multilinguality grows only logarithmically in the number of languages. That is, we show that there is no theoretical curse of multilinguality for embedding space structure. This suggests that the empirical curse of multilinguality is a result of real world data and training conditions. We back this understanding with a small-scale empirical study. Our paper provides the first theoretical and intrinsic perspective on the curse of multilinguality, with implications for the scientific understanding of this phenomenon.

### 中文一句话结论
该论文证明实现完美多语言嵌入所需的最小维度仅随语言数量对数增长，因此从理论上讲，并不存在必然的“多语言性诅咒”。

### English TL;DR
This paper proves that the minimum dimensionality required for perfect multilingual embedding grows only logarithmically with the number of languages, showing that the empirical curse of multilinguality is not a theoretical necessity.

### 中文详细总结
论文旨在回答多语言嵌入空间是否天生无法在不增加容量的情况下实现完美多语言性。作者首先形式化定义了“完美多语言性”的两个条件，然后通过数学证明指出，实现完美多语言性所需的最小维度仅随语言数量对数增长，即从理论结构上不存在对多语言性的诅咒。该结果表明，在实践中观察到的多语言性诅咒（模型性能随语言覆盖增加而下降）应归因于真实世界数据和训练条件的限制，而非嵌入空间的理论缺陷。论文还通过小规模实证研究支持了这一理论理解。

### 方法 / 贡献
- **形式化定义**：提出了实现“完美多语言性”的两个数学条件。  
- **理论证明**：证明满足完美多语言性所需的最小维度与语言数量成对数关系，而非线性或指数关系。  
- **首次理论视角**：从嵌入空间的结构出发，为多语言性诅咒提供了首个理论分析，区分了理论可能性与现实限制。

### 实验或数据
论文进行了一项小规模实证研究，但摘要中未提供具体数据集、模型或实验设置的详细信息。

### 值得关注点
- 理论结果明确否定了“多语言性诅咒是嵌入空间固有属性”的观点，为设计更高效的多语言模型提供了理论基础。  
- 研究将实证观察中的性能退化归因于数据和训练条件，提示未来工作可聚焦于改善数据质量和训练方法。

### 局限性
- 理论证明基于假设的完美多语言性条件，可能与实际应用中的近似多语言性存在差距。  
- 实证研究规模较小，缺乏详细的实验设置和数据集描述，无法完全验证理论的实际影响。

## 8. Uncertainty-Aware Decision Making in Multimodal Large Language Models

- Source: arxiv
- arXiv ID: 2608.17084
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.17084v1
- PDF: https://arxiv.org/pdf/2608.17084v1
- DOI: https://doi.org/10.48550/arXiv.2608.17084

### Authors

Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed

### Abstract

Multimodal large language models (MLLMs) increasingly answer questions whose correctness depends on visual, textual, temporal, acoustic, document, chart, or embodied evidence. Their failures are therefore not only linguistic. A fluent answer may conceal poor input quality, a perceptual error, weak grounding, conflict between modalities, unstable reasoning, distribution shift, or a question that is not answerable from the supplied evidence. This survey organizes the literature on uncertainty-aware MLLMs around a decision-centered framework: uncertainty sources give rise to observable signals, signals must be calibrated or controlled for risk, and calibrated uncertainty should determine the system action. We review work on token and logit uncertainty, semantic disagreement, perturbation instability, grounding and attribution scores, verbalized confidence, verifier and judge scores, conformal prediction, selective answering, abstention, clarification, retrieval, self-checking, and escalation. The central argument is that uncertainty should not be evaluated only as a confidence number; it should be evaluated by whether it improves behavior under insufficient, conflicting, shifted, or high-risk multimodal evidence. We position this survey against text-only uncertainty and abstention surveys, broad MLLM surveys, MLLM hallucination surveys, and safety-oriented reviews. We conclude with open problems in source-aware decomposition, action-aware benchmarks, calibration under shift, black-box uncertainty estimation, broader modality coverage, reproducible reporting, and human-centered uncertainty communication.

### 中文一句话结论
本综述主张：多模态大语言模型的不确定性应通过决策中心框架评估，即根据不确定性来指导系统行为（如弃权、澄清、检索、升级），而不仅仅是依赖置信度数值。

### English TL;DR
This survey proposes that uncertainty in multimodal large language models should be evaluated and managed through a decision-centered framework that moves beyond simple confidence scores to actionable policies like abstention, clarification, and escalation based on multimodal evidence quality.

### 中文详细总结
本文是一篇关于多模态大语言模型（MLLM）不确定性感知决策的综述。核心论点：MLLM的失败不仅源于语言层面，更与输入质量、感知错误、模态冲突、推理不稳、分布偏移等问题相关。为此，作者提出了一个“来源-信号-校准-行动”（source-signal-calibration-action）的决策中心框架：不确定性来源（如感官模糊、接地失败）产生可观测信号（如熵、语义分歧、接地分数）；信号需经校准或风险控制；校准后的不确定性应决定系统动作（如直接回答、弃权、要求澄清、检索证据、升级到人类专家）。文章综述了包括令牌/对数不确定性、语义不一致、扰动稳定性、接地与归因分数、口头化置信度、验证器/评判器分数、共形预测、选择性回答、弃权、澄清、检索、自我检查、升级等多类方法。强调不确定性应通过是否改善在不足、冲突、偏移或高风险多模态证据下的行为来评估，而非仅作为置信度数字。文章最后列出了开放问题，包括来源感知分解、行动感知基准、偏移下校准、黑箱不确定性估计、更广泛模态覆盖、可复现报告、以人为中心的不确定性沟通。

### 方法 / 贡献
1. 提出了一个来源-信号-校准-行动分类法，系统组织MLLM不确定性文献。  
2. 综合了多模态系统特有的不确定性来源，包括感官模糊、感知错误、接地失败、跨模态冲突、语言先验主导、推理不稳定、可回答性不确定性及分布偏移。  
3. 将不确定性估计与具体响应动作（如弃权、澄清、检索、自我检查、升级）联系起来。  
4. 将评估重新组织为不确定性下的行为导向，而非仅关注置信度质量。

### 实验或数据
该论文为一篇综述论文，未进行新的实验或使用特定数据集。文中提及的各类方法来自其他已发表工作，但本综述本身不涉及实验或数据。

### 值得关注点
- 决策中心视角：将不确定性从数值度量转向指导系统实际行为。  
- 多模态特有不确定性源的系统分类（如感官模糊、接地失败、模态冲突）。  
- 连接不确定性估计与响应动作的完整链条，涵盖弃权、澄清、检索、升级等。  
- 明确了开放问题清单，为未来研究提供方向。

### 局限性
- 未解决不确定性源的源感知分解（即区分不同来源贡献）。  
- 缺乏专门针对动作类型（而非仅正确率）的基准测试。  
- 分布偏移下的校准方法尚不完善。  
- 黑箱模型的不确定性估计仍具挑战。  
- 对更广泛模态（如触觉、嗅觉、多模态时间序列）的覆盖不足。  
- 可复现报告标准需要统一。  
- 以人为中心的不确定性沟通（如如何向用户表达不确定性）需进一步研究。

## 9. SIGMA: SHAP-Guided Implicit-Trajectory Generation for Metadata-Free LLM-Based AutoFE

- Source: arxiv
- arXiv ID: 2608.17948
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.17948v1
- PDF: https://arxiv.org/pdf/2608.17948v1
- DOI: https://doi.org/10.48550/arXiv.2608.17948

### Authors

Xuan Zheng, Kento Uchida, Shinichi Shirakawa

### Abstract

Recent research has leveraged Large Language Models (LLMs) to enhance Automated Feature Engineering (AutoFE) through semantic descriptions and trajectory-based prompting. However, there exist two challenges that limit their applicability and scalability in long-horizon optimization: (1) semantic metadata is unavailable in many practical settings, and (2) trajectory accumulation increases the risk of exceeding the context window, while without it, the generation process can become unstable, leading to becoming stuck in the local optima and a high duplicate rate of generated features. To this end, we propose a SHAP-enhanced Implicit-trajectory Generation for Metadata-free AutoFE (SIGMA), a scalable constant-context optimization framework. SIGMA leverages SHAP values to provide task-aware signals for guiding group feature generation instead of semantic information. In addition, we adopt an EXposed-feature Implicit Trajectory (EXIT) approach, where the exposed features in the prompt implicitly represent the trajectory. Empirical results demonstrate that SIGMA achieves performance comparable to the state-of-the-art (SOTA) LLM baselines with a nearly constant prompt length. Notably, EXIT significantly reduces the duplicate ratio of generated features from 37.2% to 6.8%. At the same time, SIGMA matches traditional SOTA performance with only 5.4 features on average, demonstrating substantial efficiency gains in feature utilization.

### 中文一句话结论
SIGMA 提出了一种无需语义元数据的、基于 SHAP 引导和隐式轨迹的 LLM 自动特征工程框架，在保持近似恒定提示长度的同时达到与 SOTA 相当的性能，并将特征重复率从 37.2% 降至 6.8%。

### English TL;DR
SIGMA is a metadata-free LLM-based AutoFE framework that uses SHAP values for task-aware group-wise feature generation and an exposed-feature implicit trajectory (EXIT) to avoid explicit trajectory accumulation. It achieves SOTA-comparable performance with nearly constant prompt length, cutting duplicate feature generation from 37.2% to 6.8% and using only 5.4 features on average to match traditional SOTA.

### 中文详细总结
现有基于 LLM 的自动特征工程（AutoFE）通常依赖语义描述和显式轨迹提示，但面临两个问题：实际场景中常缺乏语义元数据；轨迹累积易超出上下文窗口，而移除轨迹又会导致生成不稳定、陷入局部最优和高重复率。SIGMA 提出用 SHAP 值替代语义信息，为分组特征生成提供任务感知信号；同时提出 EXIT（Exposed-feature Implicit Trajectory），让提示中暴露的特征隐式代表优化历史，而非显式列举轨迹。实验表明，SIGMA 在近恒定提示长度下达到与 SOTA LLM 基线相当的性能，特征重复率从 37.2% 降至 6.8%，并且平均仅用 5.4 个特征即可匹配传统 SOTA 性能。

### 方法 / 贡献
- 提出 SIGMA，一个无需语义元数据的 LLM-based AutoFE 框架，用 SHAP 值作为任务感知信号。
- 将特征按 SHAP 值与噪声阈值分为 top、useful、weak 三组，进行组内（intra-group）和跨组（cross-group）特征生成。
- 提出 EXIT 策略：通过动态屏蔽已选特征来隐式传递轨迹信息，避免显式轨迹带来的上下文膨胀。
- 跟踪失败生成中频繁出现的操作，并在提示中临时禁止，但不会禁止持续有效的操作。
- 每轮生成一个组内特征和一个跨组特征，由下游模型评估后仅接受带来正向提升的特征。

### 实验或数据
摘要和预览内容显示，实验使用了 16 个公开表格分类数据集，来自 OpenML 和 Kaggle；每个数据集限制最多 50,000 个样本，按 8:2 划分训练集和测试集，并使用三种不同随机种子重复划分。摘要报告了与 SOTA LLM 基线的性能对比、提示长度近恒定、重复率从 37.2% 降至 6.8%，以及平均 5.4 个特征匹配传统 SOTA 的结果。

### 值得关注点
- 无需语义元数据，适用于隐私敏感或传感器日志等场景。
- 提示长度几乎恒定，支持长周期优化。
- EXIT 显著降低特征重复率。
- 特征利用率高，平均仅需少量特征即可达到较强性能。

### 局限性
所提供的摘要和预览内容未明确讨论局限性。可能存在的潜在问题（如 SHAP 计算开销、LLM 生成质量依赖等）在原文摘要中未提及，因此不作额外推断。

## 10. An Investigation of Translationese in the Generations of Multilingual Large Language Models

- Source: arxiv
- arXiv ID: 2608.17399
- Relevance: 4.0

### Links

- Abstract: http://arxiv.org/abs/2608.17399v1
- PDF: https://arxiv.org/pdf/2608.17399v1
- DOI: https://doi.org/10.48550/arXiv.2608.17399

### Authors

Maria Valentini, Téa Wright, Julisa Granados, Eliana Colunga, Katharina von der Wense

### Abstract

Text which has been translated from another language tends to carry with it evidence of translation$\unicode{x2014}$hence, it is often referred to as $\textit{translationese}$. Multilingual large language models (MLLMs) generate text in a variety of languages. However, it is still unclear if MLLMs' generations resemble internal translation (from English or, potentially, other languages) and, thus, result in translationese. Here, we ask the following research questions: (1) Does text generated by MLLMs resemble translationese? (2) How does translationese produced by MLLMs differ from translationese produced through direct translation? We leverage established indicators of translated text to evaluate text generated by state-of-the-art MLLMs in five languages, comparing to both non-translated and human-written baselines in order to isolate translationese from other kinds of interference. Through the use of high-accuracy classification models, analyses of variance on individual linguistic features, and the collection of human annotations in a subset of two languages (German and Spanish), we assess the translationese content of MLLM generations and examine the key features that distinguish MLLM-generated text from typical translation-related interference.

### 中文一句话结论
多语言大模型生成的非英语文本确实表现出翻译腔特征，但这种翻译腔与人类直接翻译产生的翻译腔存在关键差异。

### English TL;DR
Multilingual LLM outputs, especially in non-English languages, exhibit translationese—linguistic traces of translation—but differ significantly from human-translated text in key linguistic features.

### 中文详细总结
本研究探讨了多语言大语言模型（MLLMs）生成的文本是否具有“翻译腔”（translationese）特征。通过分析五个语言（英语、德语、西班牙语、希腊语和普什图语）中MLLM生成的文本，并与人类母语文本、人类翻译文本及机器翻译文本进行对比，研究者发现：MLLM生成的文本在所有语言中都表现出一定程度的翻译腔，在非英语语言中尤为显著。然而，MLLM产生的翻译腔与直接翻译（包括人类翻译和机器翻译）产生的翻译腔存在结构性差异，表明其不仅源于类似翻译的过程，还包含模型特有的风格偏差。

### 方法 / 贡献
1. 方法：使用基于SVM的二元分类器，采用已建立的翻译腔语言学指标（如类符-形符比、功能词频率、句长、代词频率、标点频率、词性n-gram分布、上下文功能词等）作为特征
2. 训练数据仅使用人类产生的数据（母语文本和人类翻译文本），避免模型学习到特定MT系统的偏差
3. 贡献：首次系统性地从翻译腔角度评估MLLM生成文本的自然性，区分了翻译腔与LLM特有风格偏差，并为未来评估MLLM输出质量提供了方法论框架

### 实验或数据
- 数据来源：Europarl多语言平行语料库（德语、西班牙语、希腊语）；英语Wikipedia+Open Language Data Initiative（普什图语）
- 实验语言：英语、德语、西班牙语、希腊语（高/中资源语言）和普什图语（低资源语言）
- 对比条件：MLLM直接生成 vs. MLLM生成英文+机器翻译 vs. 人类母语文本 vs. 人类英文+人类翻译 vs. 人类英文+机器翻译 vs. 人类英文+其他模型翻译
- 模型：Gemini-2.0-Flash-001和Llama-3.3-70B-Instruct
- 分类器精度：德语99.79%、西班牙语99.81%、希腊语99.95%、普什图语87.50%、英语99.36%
- 额外验证：使用Europarl-UdS数据集进行交叉验证

### 值得关注点
- MLLM生成的翻译腔与直接翻译（人类/机器）产生的翻译腔存在本质差异，表明模型具有独特的语言风格偏差
- 低资源语言（普什图语）中翻译腔效应更为显著，可能与训练数据不足导致的英语中心表征有关
- 研究使用了多种语言学指标（包括功能词频率、词性n-gram分布等）进行细粒度分析，而非仅依赖端到端分类
- 即使在英语中MLLM生成的文本也表现出一定程度的翻译腔特征

### 局限性
- 数据来源有限：主要依赖Europarl（议会文本）和Wikipedia，可能无法代表所有文本类型
- 仅测试了两种MLLM（Gemini和Llama），结论可能不适用于其他架构的模型
- 分类器训练数据中的人类翻译文本可能本身包含翻译腔特征，影响基准定义
- 实验中未明确区分模型大小、训练数据量和具体训练配置对翻译腔的影响
- 普什图语样本量较小（仅1000条），结果可能不够稳健
- 未探索翻译腔特征在不同生成任务（如对话、摘要）中的表现差异

## Processing Notes

- Duplicate papers skipped: 0