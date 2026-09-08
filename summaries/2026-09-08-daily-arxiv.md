# Daily arXiv - 2026-09-08

- Source: GitHub Actions generated paper list
- Generated at: 2026-09-08T00:32:52
- Paper count: 10

## 1. A Repeated-Measurement Study for Cultural Analytics of English Song Lyrics Using Five Large Language Models

- Source: arxiv
- arXiv ID: 2609.04428
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2609.04428v1
- PDF: https://arxiv.org/pdf/2609.04428v1
- DOI: https://doi.org/10.48550/arXiv.2609.04428

### Authors

E. Cho Smith, Samuel Ho, Dawn Laux

### Abstract

Large language models (LLMs) are increasingly used to annotate cultural texts at scales that are impractical for human coders. However, before their outputs are treated as measurements of latent social constructs, it is necessary to establish whether those measurements are reliable. This study evaluates five LLMs as zero-shot annotators of four social constructs expressed in English song lyrics: self-esteem, self-control, seeking belonging, and seeking recognition. Using repeated annotations of a large lyric corpus, we examine three properties of LLM-based measurement: consistency across repeated runs, convergence across models, and transferability of consensus labels to supervised classification. The findings show that LLM-based measurement is not uniformly reliable across constructs. Self-esteem exhibits the strongest repeated-measurement reliability across models, while seeking recognition is generally less stable; self-control and seeking belonging show intermediate but model-dependent reliability. Downstream classification further indicates that consensus LLM labels contain learnable signal, although transferability does not itself establish construct validity. Repeated-measurement stability and cross-model convergence should therefore be reported before LLM annotations are treated as scalable measurements in cultural analytics.

### 中文一句话结论
该研究评估了五个大语言模型对英语歌词中四种社会构念的零样本注释，发现测量可靠性因构念而异，强调在将LLM注释视为可扩展测量之前需报告重复测量稳定性和跨模型收敛性。

### English TL;DR
This study evaluates five large language models for zero-shot annotation of four social constructs in English song lyrics and finds that measurement reliability varies by construct, highlighting the need to report repeated-measurement stability and cross-model convergence before treating LLM annotations as scalable cultural analytics measurements.

### 中文详细总结
研究使用五个大语言模型（GPT-4o-mini、o3-mini、Claude 3.7 Sonnet、DeepSeek-R1、Gemini 2.0 Flash）对英语歌词进行零样本注释，评估四个社会构念：自尊、自控、寻求归属、寻求认可。通过重复注释（每个模型三次），检验了三个属性：多次运行的一致性、跨模型收敛性、以及共识标签对监督分类的可转移性。结果发现：自尊的重复测量可靠性最强，寻求认可最不稳定，自控和寻求归属居中且依赖模型。下游分类实验表明，共识标签包含可学习信号，但可转移性本身不证明构念效度。研究强调，在将LLM输出作为文化分析的可扩展测量之前，应报告重复测量稳定性和跨模型收敛性。

### 方法 / 贡献
- **方法**：使用五个LLM进行零样本注释，每个模型重复三次；通过Fleiss' κ评估重复可靠性及跨模型一致性；使用共识标签训练BigBird分类器进行下游转移实验。
- **贡献**：系统评估了LLM作为文化分析测量工具的可靠性，揭示了构念依赖性和跨模型差异，提出了报告稳定性和收敛性的要求，为后续构念效度研究奠定基础。

### 实验或数据
- **实验**：对69,130首英语歌词进行重复注释（每个模型三次），使用Music4All数据集。下游分类实验使用内部平衡集（960首16类平衡样本，以及每个构念1,000首二进制样本）和外部验证集（1,572首含人类验证标签的歌词）。
- **数据**：大歌词语料库，来源于Music4All数据库，经语言过滤和长度筛选后保留69,130首。

### 值得关注点
- 自尊构念的注释可靠性最高，寻求认可最低，表明构念性质影响LLM测量稳定性。
- 跨模型共识标签可用于训练监督分类器，但构念效度需独立验证。
- 研究强调文化分析中LLM输出应经过可靠性检验，避免直接作为有效测量。

### 局限性
- 仅针对英语歌词，可能不适用于其他语言或文本类型。
- 零样本设置，模型版本随时间变化，结果可能不具长期稳定性。
- 构念效度未验证，仅关注测量可靠性，不能直接推广至真实心理构念。
- 数据版权限制，无法公开完整语料和注释，影响可复现性。

## 2. Reinforcement Learning for improving Large Language Models' Catalan text simplification capabilities

- Source: arxiv
- arXiv ID: 2609.04823
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.04823v1
- PDF: https://arxiv.org/pdf/2609.04823v1
- DOI: https://doi.org/10.48550/arXiv.2609.04823

### Authors

Arnau Ayguadé Domingo, Stefan Bott, Horacio Saggion

### Abstract

Although automatic text simplification (ATS) is critical for accessibility, its progress has not matched the rapid evolution of broader natural language processing techniques. This paper investigates the application of reinforcement learning (RL) to improve the quality of ATS for low-resource languages using Large Language Models (LLMs). The paper introduces a novel reward function, designed to guide LLMs toward a targeted simplification style with Group Relative Policy Optimization (GRPO), that combines the SARI metric with specific penalty components. The effectiveness of GRPO with this reward function is motivated and demonstrated by post-training IberianLLM-7B-Instruct on the ASSET dataset. After post-training on the English ASSET, the model's ATS performance improves on two curated Catalan benchmarks while also successfully suppressing previously observed negative behaviors. Cross-lingual transfer learning is explored by translating ASSET into Catalan and Spanish and post-training the model on each version, but these fail to show a significant improvement on the out-of-domain benchmark.

### 中文一句话结论  
本文通过GRPO强化学习结合SARI与长度/复制惩罚项的新型奖励函数，对IberianLLM进行后训练，显著提升了加泰罗尼亚语的自动文本简化质量，同时抑制了过度生成行为；但利用翻译语料进行跨语言迁移的效果有限。

### English TL;DR  
This paper demonstrates that reinforcement learning with a novel reward function combining SARI and length/copy penalties significantly improves large language models' Catalan text simplification capabilities, achieving notable gains on curated benchmarks while suppressing undesirable generation behaviors.

### 中文详细总结  
自动文本简化（ATS）对信息无障碍至关重要，但在低资源语言中进展缓慢。本文探索使用强化学习（RL）来提升大语言模型（LLM）的加泰罗尼亚语简化能力。作者提出一种新的奖励函数，结合SARI指标与复制惩罚和长度惩罚，并采用组相对策略优化（GRPO）对IberianLLM-7B-Instruct进行后训练。训练数据使用ASSET数据集（英文原始版及自动翻译的加泰罗尼亚语和西班牙语版）。实验表明：基于英文ASSET后训练的模型在加泰罗尼亚语iDEM基准和ASSET测试集上均有显著提升，并完全消除了过度生成问题。而基于翻译语料后训练的模型仅在域内ASSET测试集上有提升，在跨域iDEM基准上未表现出显著改进。跨语言迁移效果依赖于训练数据质量，未来应发展无参考简化指标作为奖励函数。

### 方法 / 贡献  
- 提出一种针对句子简化的新型奖励函数：基于SARI（归一化到[0,1]），并加入复制惩罚（若输出与源句相同则扣0.5）和长度惩罚（输出长度超过参考长度5词以上时施加指数衰减惩罚）。  
- 采用GRPO进行后训练，无需额外的价值函数估计器。  
- 验证了强化学习在低资源语言ATS中的有效性，并探索了通过自动翻译语料进行跨语言迁移的局限性。  

### 实验或数据  
- **数据集**：  
  - **ASSET**（英文句子级简化语料，2000句，每句10个人工参考）；自动翻译为加泰罗尼亚语和西班牙语，并基于BLEURT分数（0.7–0.9）过滤。  
  - **iDEM**（加泰罗尼亚语专家精简化语料，380句，经BLEURT >0.5过滤后保留304句），用作跨域基准。  
- **模型**：IberianLLM-7B-Instruct。  
- **训练**：分别用英文、加泰罗尼亚语、西班牙语ASSET进行GRPO后训练，每个版本约12k–15k样本。  
- **评估**：在加泰罗尼亚语ASSET测试集（10%）和iDEM上计算SARI分数。  
- **结果**：  
  - 英文版后训练：ASSET测试集SARI从47.75提升至50.41，iDEM从43.31提升至44.50（显著）。  
  - 翻译版后训练：ASSET测试集也有提升（约50分），但iDEM上无显著改善（42.82/42.47）。  

### 值得关注点  
- 首次将GRPO用于ATS，并设计了针对简化的奖惩机制。  
- 抑制过度生成行为：长度惩罚有效消除了模型不生成结束符的问题。  
- 跨语言迁移的有趣发现：英文训练数据带来的简化能力可跨域迁移到加泰语，而翻译语料则不能。  

### 局限性  
- **ASSET数据集质量**：每条源句对应10个参考，可能导致训练不能充分压缩输出多样性；测试集按源-参考对拆分会造成数据泄漏，iDEM用于更可靠的评估。  
- **SARI指标依赖参考**：奖励函数仍需参考简化，限制了RL无监督优势的发挥；SARI本身存在已知缺陷（如对过度生成不敏感），惩罚项虽部分缓解但非完美。  
- **翻译语料质量**：自动翻译可能改变简化特性，跨语言迁移效果受限于此。  
- **实验范围**：仅在一个模型（IberianLLM）和一个基准备（iDEM）上进行跨域评估，结论需更多验证。

## 3. PLUME: Parameter-Efficient Personalization of Large Language Models via Low-Rank User Modulation in Shared Subspaces

- Source: arxiv
- arXiv ID: 2609.04715
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2609.04715v1
- PDF: https://arxiv.org/pdf/2609.04715v1
- DOI: https://doi.org/10.48550/arXiv.2609.04715

### Authors

Xinyu Li, Hao Zhou, Jianfeng Zhu, Julina Maharjan, Ruixin Guo, Feodor Dragan, Ruoming Jin

### Abstract

Personalizing large language models (LLMs) is essential for delivering AI assistance that aligns with individual users' styles, intents, and preferences. While per-user fine-tuning can substantially enhance personalization quality, it introduces significant parameter and storage overhead, limiting scalability to large user populations. We propose PLUME (Personalized Low-Rank Adaptation through User Modulation and Shared Subspace), a lightweight framework that achieves efficient and expressive per-user adaptation by leveraging a shared task-specific subspace. Specifically, PLUME first learns a global task subspace from aggregated user data. Personalization is then achieved by training only a lightweight small square matrix within this subspace, enabling each user to obtain a tailored model while keeping shared components fixed. Cross-layer shared parameters and rank-1 residual terms are further introduced to significantly reduce redundancy while maintaining expressiveness. Experiments on multiple personalized text generation benchmarks demonstrate that PLUME achieves comparable or superior performance to strong baselines, while reducing per-user parameters by over 95%. These results establish shared-subspace modulation with minimal residuals as a scalable and semantically grounded approach to LLM personalization.

### 中文一句话结论
PLUME 通过在共享任务子空间中训练极小的用户专属矩阵和秩 1 残差，实现了大语言模型的高效个性化，参数量减少超 95% 且性能不输强基线。

### English TL;DR
PLUME achieves scalable LLM personalization by learning a shared task subspace and training only a tiny per-user square matrix plus rank-1 residuals, matching or surpassing strong baselines while reducing per-user parameters by over 95%.

### 中文详细总结
大语言模型的个性化对实现贴合用户风格与偏好的 AI 助手至关重要。但为每个用户微调模型会带来巨大的参数和存储开销，限制其在大规模用户群上的扩展性。PLUME 提出了一种轻量级框架，首先从聚合的多用户数据中学习一个全局的任务子空间，随后每个用户的个性化仅需在该子空间内训练一个小型方阵，并引入跨层共享参数和秩 1 残差项来减少冗余、保持表达能力。实验表明，在多个个性化文本生成基准上，PLUME 达到或超越了强基线效果，同时每个用户的参数量减少了 95% 以上，验证了共享子空间结合极小残差的策略是一种可扩展且语义上可靠的个性化方案。

### 方法 / 贡献
- **共享子空间学习**：从聚合的用户数据中预训练一个全局的低秩任务子空间，捕获所有用户共有的任务知识。
- **轻量用户调制**：每个用户仅需学习一个小型方阵（在共享子空间内）以及若干秩 1 残差项，即可实现个性化；共享参数在其他用户间保持固定。
- **跨层参数共享与残差项**：进一步减少冗余，同时保持模型的表达能力，使极少的参数即可描述用户特有的偏好。
- **高效扩展**：每个用户的额外参数相比全模型微调或独立 LoRA 大幅降低，支持大规模用户群。

### 实验或数据
在**多个个性化文本生成基准**上进行了对比实验，具体数据集未在摘要中详述。PLUME 与多个强基线（如全微调、独立 LoRA 等）比较，取得了相当或更优的性能，同时每个用户的参数量减少了 95% 以上。

### 值得关注点
- **90%+ 的参数压缩**：每个用户只需极少量参数（一个小方阵 + 秩 1 残差），存储和通信效率极高。
- **不牺牲性能**：大幅压缩参数的同时，生成质量依然匹配甚至超越昂贵的基线方法。
- **共享子空间的语义基础**：任务子空间从多用户数据中共同学习，使个性化调制具有语义合理性与泛化能力。
- **自然适用于大用户群**：框架的轻量特性使其能够扩展到海量用户的个性化场景。

### 局限性
未在摘要中直接提及，可能包括：对特定任务或子空间泛化能力的潜在限制；与完全独立微调相比，共享子空间是否能覆盖所有用户极端偏好的不确定性。

## 4. LentEx: Generalizable Latent Entity Extraction via Synthetic Data and Instruction-Tuned LLMs

- Source: arxiv
- arXiv ID: 2609.04511
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.04511v1
- PDF: https://arxiv.org/pdf/2609.04511v1
- DOI: https://doi.org/10.48550/arXiv.2609.04511

### Authors

Umesh Bodhwani, Yuan Ling, Cibi Chakravarthy Senthilkumar, Shujing Dong, Yarong Feng, Hongfei Li, Ayush Goyal

### Abstract

Latent entity extraction (LEE) tackles the challenge of identifying implicit, contextually inferred entities within free text-an area where traditional entity extraction methods fall short. In this paper, we introduce LentEx, a novel framework for latent entity extraction that leverages synthetic data generation and instruction fine-tuning to optimize smaller, efficient large language models (LLMs). Latent entities, which are often abstract and thematic, are crucial for applications such as retrieval-augmented generation (RAG), customer persona analysis, and knowledge graph enrichment. LentEx addresses the scarcity of labeled datasets by employing a template-based approach to generate diverse, contextually rich synthetic data, ensuring high variability and alignment with real-world distributions. To our knowledge, LentEx is the first to systematically approach LEE through the lens of LLMs. LentEx demonstrates significant performance improvements across multiple tasks, notably surpassing state-of-the-art models on the MTEB Clustering Benchmark. Furthermore, our methodology enables robust generalization to unseen domains, making LentEx highly applicable in real-world NLP tasks, including RAG and clustering, thereby establishing a new paradigm for latent entity understanding and extraction in natural language processing.

### 中文一句话结论
LentEx 提出一种利用模板化合成数据生成与指令微调小型 LLM 的隐式实体抽取框架，在 MTEB 聚类基准上超越现有模型，并能泛化到未见领域。

### English TL;DR
LentEx introduces a framework for latent entity extraction using template-based synthetic data generation and instruction fine-tuning of smaller LLMs, achieving state-of-the-art performance on clustering benchmarks and robust generalization to unseen domains without labeled data.

### 中文详细总结
LentEx 针对“隐式实体抽取”（Latent Entity Extraction, LEE）任务提出了一种新框架。与传统的命名实体识别不同，LEE 关注文本中未明确出现、但可通过上下文推断出的抽象或主题性实体，例如从评论中推断“用户画像”或从查询中推断“技术领域”。

该方法的核心思路是：先使用 Claude 3 Sonnet 通过模板和少样本提示生成 100 个领域组合，再为每个领域生成合成输入-输出样本，共约 10000 条训练数据，并用 Rouge-L 相似度过滤掉文本中可能“显式泄露”实体的样本。随后，使用 LoRA 对 Mistral-7B-Instruct-v0.2 进行指令微调，得到高效且可泛化的 LEE 模型。

实验显示，LentEx 在语义相似度评估上显著优于基线和 Claude-3-Haiku，并在 MTEB Clustering Benchmark 上超过现有最先进模型。该方法还可应用于检索增强生成（RAG）、客户画像分析、知识图谱扩充和文本聚类等任务。

### 方法 / 贡献
- 形式化定义了领域无关的隐式实体抽取问题。
- 提出一种无需人工标注种子数据的模板化合成数据生成流程。
- 使用合成数据对小型 LLM（Mistral-7B-Instruct-v0.2 + LoRA）进行指令微调。
- 在多个下游任务上超越基于嵌入和基于生成的最先进方法。
- 据作者所述，这是首个系统性地用 LLM 解决 LEE 问题的框架。

### 实验或数据
- 合成数据：100 个领域组合，约 10000 条样本，使用 Rouge-L 相似度过滤。
- 模型训练：Mistral-7B-Instruct-v0.2，LoRA rank=16，lr=0.0001，4×NVIDIA A10G，1 epoch。
- 语义相似度评估平均得分：Mistral-7B-Instruct-v0.2 为 61.17，Claude-3-Haiku 为 66.48，LentEx 为 77.79。
- 聚类任务：在 MTEB Clustering Benchmark 上超过现有最先进模型，并在 arxiv、biorxiv、medrxiv、reddit、stackexchange、twenty-newsgroups 等数据上报告了 v-measure 结果。

### 值得关注点
- 首次系统性地将 LLM 用于隐式实体抽取。
- 无需人工标注数据，通过模板化合成数据解决标注稀缺问题。
- 能泛化到未见领域，适合 RAG、聚类、用户画像分析等真实场景。
- 使用较小的 LLM 即可达到较强效果，具有计算效率优势。

### 局限性
摘要和可见内容中未明确列出局限性。根据方法本身可推测，其性能可能依赖合成数据的多样性与模板质量，且实验主要围绕 Mistral-7B 和特定下游任务展开，但这一点并未在原文摘要中明确说明。

## 5. Can Activation Steering Capture Multidimensional Authorship Style?

- Source: arxiv
- arXiv ID: 2609.04792
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2609.04792v1
- PDF: https://arxiv.org/pdf/2609.04792v1
- DOI: https://doi.org/10.48550/arXiv.2609.04792

### Authors

Hieu Tran, Calvin Bao, Marine Carpuat

### Abstract

Activation steering has shown promise for controlling LLM generation along well-defined attributes, but it remains unclear whether it can handle the multidimensional and hard-to-define nature of authorship style. We ask whether structured contrastive prompting along rhetorically-motivated dimensions can construct rich style representations directly in activation space, bypassing the need for natural language style descriptors or dedicated training. We find that the resulting directions share a common authorship backbone while conflicting on aspect-specific residuals that carry genuine stylistic signal, explaining why naive aggregation fails. We operationalize this in Aspect-Aware Activation Steering (A3S), a training-free framework that merges per-aspect contrastive directions with interference-aware aggregation and tunes steering strength per instance. A3S improves authorship style transfer where it is genuinely multi-aspect, outperforms a trained baseline in preference evaluations on out-of-domain benchmarks, and keeps target-exemplar overlap consistently low.

### 中文一句话结论
本文提出A3S，通过修辞维度对比提示提取多方面作者风格的激活方向，以干扰感知融合与自适应强度搜索实现无需训练的高质量多维作者风格迁移，优于自然语言描述和训练基线。

### English TL;DR
A3S is a training-free framework that extracts per-aspect contrastive directions in LLM activation space via structured rhetorical prompting, merges them with interference-aware aggregation, and adaptively tunes steering strength, achieving superior multidimensional authorship style transfer over natural language descriptors and trained baselines.

### 中文详细总结
作者风格是多维的（词汇、句法、修辞等），现有提示方法用自然语言描述风格丢失细粒度信息，训练方法需数据且泛化有限，而传统激活干预将风格视为单一属性。本文提出A3S，将目标范例分解为修辞维度（如语气、视角、结构），通过对比提示生成每个维度的正反样例，提取对比激活方向。研究发现这些方向共享一个共同的作者风格主干，但在方面特定残差上冲突，解释了简单平均为何失败。A3S采用参数竞争平衡（PCB）融合方向，并用混合自适应搜索为每个输入动态调整干预强度。在MUD、LaMP、LongLaMP基准上，A3S显著提升多维作者风格迁移，偏好评估中优于训练基线TinyStyler（尤其域外场景），且保持低目标-范例重叠。

### 方法 / 贡献
1. **几何发现**：基于范例的方面方向可分解为共享的作者风格主干与携带真实风格信号的方面特定残差，为多维激活干预提供理论依据。
2. **A3S框架**：无训练推理时框架，通过PCB融合方面方向，并利用混合自适应搜索按实例调整干预强度。
3. **实证结果**：在多个基准上，激活空间风格表示比自然语言描述更有效捕捉细粒度作者风格，且域外泛化优于学习式基线。

### 实验或数据
实验在三个多维作者风格迁移基准（MUD、LaMP、LongLaMP）上进行，与提示基线（STYLL、RG）和训练基线（TinyStyler）比较，评估使用人类偏好和LLM偏好，并报告目标-范例重叠指标。A3S在偏好评估中优于TinyStyler（尤其域外基准），重叠率始终较低。

### 值得关注点
1. 利用修辞理论指导对比提示，避免自然语言描述的信息瓶颈。
2. 发现方面方向间共享主干+冲突残差的几何结构，并针对性设计PCB融合。
3. 无需训练，仅需少量范例即可提取风格方向。
4. 自适应强度搜索避免全局固定系数导致的欠/过干预。

### 局限性
根据提供的论文内容，未明确讨论局限性。从方法看，需为每个方面生成多个对比对（K=4），可能增加推理开销；且提示模板及修辞维度选择可能影响效果，但文中未详细阐述这些潜在问题。

## 6. Vectorizing Classical Tamil: Representation Learning for Verse-Commentary Pairs

- Source: arxiv
- arXiv ID: 2609.04755
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.04755v1
- PDF: https://arxiv.org/pdf/2609.04755v1
- DOI: https://doi.org/10.48550/arXiv.2609.04755

### Authors

Amrit Gopinath, Sangeetha Sivanesan

### Abstract

We construct a corpus of 1,262 verse-commentary (urai) pairs from five Classical Tamil source sections, ranging from technical grammatical prose to modern paraphrase, and ask what information representation learning can recover. We train recurrent and Transformer encoders, a Siamese-style pair-matching network, an mBART-style encoder-decoder, and a decoder-only language model. Each analysis is interpreted against an appropriate control on the same data. TF-IDF provides a strong no-training lexical retrieval baseline, alongside representation analyses and generation controls for the learned models. A fixed string containing the 25 most frequent commentary words scores higher on generation overlap than the decoder-only model. Canonical correlation reaches 1.000 on Gaussian noise at these sample sizes, token-F1 spans only about 0.02-0.20 on this corpus, and the encoder-decoder continues to lower training loss for sixteen epochs after validation loss has begun to rise. One narrow result remains: the decoder-only model prefers authentic word order in 107 of 112 minimal-pair comparisons (95.5%), but does not reproduce held-out commentary content. We release the extraction and evaluation protocol; redistribution of the source commentaries remains subject to permission.

### 中文一句话结论
从1,262对古典泰米尔语诗-注对中进行的表征学习实验表明，模型主要捕捉到词汇重叠，未能学到深层对齐，仅在词序偏好上有一个窄的结果（95.5%正确），但无法生成正确注释。

### English TL;DR
Despite careful controls and multiple model architectures, representation learning on 1,262 Classical Tamil verse-commentary pairs largely fails to recover meaningful alignment beyond lexical overlap, with only a decoder-only model showing a narrow preference for authentic word order (95.5% accuracy) but failing to reproduce held-out commentary content.

### 中文详细总结
本文构建了一个包含1,262对古典泰米尔语诗句与注释（urai）的语料库，来源包括Naaladiyar、Thirukadukam和Tholkappiyam的三个部分，对应的注释风格包括现代释义、学术评论和词汇注释。作者训练了多种模型：LSTM、BiLSTM、小型Transformer编码器、Siamese对匹配网络、mBART式编解码器以及仅解码器语言模型。所有分析均基于匹配的控制基线进行解释。TF-IDF词汇检索提供了强大的无训练基线。主要发现：典型相关分析（CCA）在样本量不足时不可解释（高斯噪声下达到1.000）；令牌F1仅在0.02–0.20之间，低于一个包含25个最常用注释词的固定字符串；编解码器在4轮后过拟合；分离编码器未能恢复诗-注对齐；Siamese模型虽能拟合训练对，但可能利用来源标识而非真正理解诗-注关系。唯一窄结果是：仅解码器模型在112次最小对比较中107次偏好真实词序（95.5%），但无法生成保留的注释内容。作者公开了数据提取和评估协议，但注释源数据的重新分发需获许可。

### 方法 / 贡献
- 构建了1,262对古典泰米尔语诗-注语料库，涵盖五种来源和三种注释风格。
- 系统比较了多种表征学习模型（递归、Transformer、Siamese、编解码、仅解码器），并设置严格的控制基线（TF-IDF、高斯噪声、固定字符串等）。
- 提出一种“最小对词序偏好探针”，用于测试仅解码器模型是否偏好真实词序。
- 公开了提取和评估协议，强调小数据下古典语言NLP的谨慎评估原则。

### 实验或数据
- 语料库：1,262对诗句-注释对，来自Naaladiyar (393对，现代释义)、Tholkappiyam Eluttatikaram (379对，学术评论)、Tholkappiyam Sollatikaram (287对)、Tholkappiyam Porulatikaram (103对)、Thirukadukam (100对，词汇注释)。
- 模型训练：所有模型从头训练，种子3407，使用90/10分割（1,136训练/126验证）。仅解码器模型有词序偏好测试（112对，13对基于语法规则，99对随机重排）。
- 关键结果：CCA在高斯噪声下达到1.000；令牌F1最大值0.060（仅解码器），低于TF-IDF的0.084和固定字符串的0.108；仅解码器词序偏好95.5%准确率；编解码器在4轮后验证损失上升；分离编码器对余弦相似度极低，分类器在池内仅略高于随机。

### 值得关注点
- 该研究展示了在极小语料（1,262对）下进行古典语言NLP时控制基线的重要性：如果没有高斯噪声对照，CCA结果可能被误读。
- 固定字符串（高频25词）在重叠指标上超过所有训练模型，提示模型可能只学会了高频搭配。
- 词序偏好探针（95.5%）是一个窄但可复现的结果，表明模型学到了一些局部顺序特征，但远未达到理解语法或生成内容。
- 论文公开了评估方法，可作为后续研究在类似小数据古典语言任务中的基准。

### 局限性
- 语料库规模小（1,262对），且来源风格差异大，可能限制了模型学习深层表征的能力。
- 分词采用简单的空白分词，未考虑泰米尔语的黏着性，可能导致欠佳的表征。
- 词序偏好探针仅基于112个最小对，且大多数为随机重排，无法全面评估语法能力。
- 分离编码器和Siamese模型的评估发现，分类器在跨源池中可能利用源标识而非诗-注关系，说明实验结果可能受到数据集偏差影响。
- 编解码器未能生成有意义的注释内容，提示生成模型在此任务上无效。
- 作者指出重新分发注释源需要许可，可能限制可复现性。

## 7. EuroAlpaca: Task-Preserving Localisation of Instruction Data for European Languages

- Source: arxiv
- arXiv ID: 2609.05043
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2609.05043v1
- PDF: https://arxiv.org/pdf/2609.05043v1
- DOI: https://doi.org/10.48550/arXiv.2609.05043

### Authors

Aleix Sant, Jordi Luque, Carlos Escolano

### Abstract

Machine translation (MT) offers a scalable way to extend English instruction-tuning data to multiple languages, but it can distort task-critical constraints and required outputs, creating corrupted training examples and degrading models trained on such data. We introduce EuroAlpaca, a task-preserving localisation pipeline and near-parallel resource covering 50 European languages and regional varieties, together with European-IFEval, a multilingual benchmark for verifiable instruction following. Depending on the example, our pipeline applies field-wise MT while preserving task-critical content or reconstructs a task-equivalent target-language instance, followed by validation of cross-field coherence and target-language consistency. Across LoRA experiments with four LLMs, training on directly translated data improves ROUGE-L and F-BERT on the Aya Evaluation Suite, but reduces accuracy on European-IFEval by 29.8% relative to the unadapted baseline. In contrast, adaptation with EuroAlpaca improves accuracy by 12.9% over the same baseline, reversing the degradation caused by direct MT, while also achieving the highest ROUGE-L and F-BERT scores on Aya. These results show that preserving task semantics is essential for multilingual instruction tuning.

### 中文一句话结论
EuroAlpaca 通过任务保持的本地化流水线，在 50 种欧洲语言上显著提升了指令跟随准确率，证明保持任务语义对多语言指令微调至关重要。

### English TL;DR
EuroAlpaca is a task-preserving localisation pipeline and multilingual benchmark for 50 European languages. It shows that direct translation degrades verifiable instruction-following accuracy by 29.8% while their approach improves it by 12.9%, demonstrating that preserving task semantics is essential for multilingual instruction tuning.

### 中文详细总结
EuroAlpaca 提出了一种任务保持的本地化流水线，将英语指令数据集（Alpaca Cleaned，共 51,760 条样本）适配到 50 种欧洲语言及地区变体，并配套创建了 European-IFEval 多语言可验证指令跟随基准。该流水线根据样本任务类型动态路由：对于适合翻译的样本进行字段级机器翻译（保留任务关键字段），否则执行任务级重写以重构语义等价的目标语言实例，随后通过跨字段一致性和目标语言一致性验证。在四个 LLM 上的 LoRA 微调实验显示：直接翻译的数据虽能提升 Aya 评估套件上的 ROUGE-L 和 F-BERT 分数，但导致 European-IFEval 准确率下降 29.8%；使用 EuroAlpaca 适配后，准确率提升 12.9%，逆转了直接翻译的退化，并在 Aya 上取得最高分数。这表明多语言指令微调必须优先保持任务语义而非仅追求表面流畅度。

### 方法 / 贡献
1. **任务保持的本地化流水线**：LLM 引导的层次化路由，先判断样本是否适合字段级翻译（MT）或需任务级重写（LOC），再为 MT 样本指定每个字段的翻译/保留策略。  
2. **EuroAlpaca 资源**：源对齐的近平行数据集，覆盖英语及 50 种欧洲语言。  
3. **European-IFEval 基准**：标准化多语言可验证指令跟随评测集。  
4. **对照实验**：在四个当前小型 SOTA 模型上进行语言特定微调。  
5. **与现有多语言数据集比较**：包括 Bactrian-X、Okapi 和 MITS。

### 实验或数据
- **源数据**：Alpaca Cleaned（51,760 条），其中直接翻译 27,946 条（54.0%）、字段保留翻译 12,726 条（24.6%）、任务级本地化 11,088 条（21.4%）。  
- **模型与微调**：四个 LLM 进行 LoRA 实验。  
- **评估**：  
  - Aya Evaluation Suite（基于 ROUGE-L 和 F-BERT 的参考相似性）。  
  - European-IFEval（可验证指令跟随准确率）。  
- **结果**：  
  - 直接 MT：ROUGE-L 和 F-BERT 提升，但准确率下降 29.8%（相对未适配基线）。  
  - EuroAlpaca：准确率提升 12.9%（相对未适配基线），同时 ROUGE-L 和 F-BERT 最高。

### 值得关注点
- **评估脱节**：直接翻译提升参考相似性但严重损害指令跟随能力，表明常用参考指标无法衡量任务保真度。  
- **EuroAlpaca 逆转退化**：在提升指令跟随准确率（+12.9%）的同时保持甚至提高参考相似性，证明任务保持是必要且有效的。  
- **结构化决策**：流水线显式区分字段级翻译与任务级重写，避免机器翻译破坏语言依赖约束（如语法错误、押韵、代码字段）。

### 局限性
- 仅基于单源数据集（Alpaca Cleaned），未验证在其他复杂指令数据集（如 ShareGPT、OpenAssistant）上的泛化能力。  
- 语言覆盖限于 50 种欧洲语言及地区变体，未包含亚洲、非洲等低资源语言。  
- 任务保持依赖 LLM 判断模块，其决策可能引入系统偏差。  
- 实验仅使用小型模型（通过 LoRA 微调），在更大或不同架构模型上的效果未知。  
- 未评估本地化数据的 zero-shot 跨语言迁移能力。

## 8. Technical Manual for a Toolkit for Measuring Contextual Individuation in Transformer Language Models

- Source: arxiv
- arXiv ID: 2609.05333
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.05333v1
- PDF: https://arxiv.org/pdf/2609.05333v1
- DOI: https://doi.org/10.48550/arXiv.2609.05333

### Authors

José Luciano Verçosa Marques, Frederico Jorge Heitmann, Daniel Omar Perez, Marcelo Vinicius de Paula, Tárcio André dos Santos Barros

### Abstract

A transformer language model assigns a single, context-independent vector to a word type at its embedding layer, yet is widely believed to individuate that word's occurrences by context in its later layers. Testing this belief cleanly requires a construct that holds the word form fixed while its context and intended sense vary in a controlled, labeled way. This manual documents an open toolkit built around such a construct, which we call a bridge form: a single written word that recurs, unchanged, across two or more subject domains with a different sense in each. We describe, and justify, every stage of the pipeline: the declarative specification of bridge forms and their source domains, corpus acquisition from Wikipedia, occurrence localization, layer-wise representation extraction, a domain-pairwise silhouette measurement of separation in the model's representation space, and a paired visualization protocol. Each design choice is presented together with the methodological failure mode it is meant to avoid (sense contamination from overly broad category labels, the multi-group bias of the silhouette coefficient, subword-tokenization misalignment, and axis-comparability artifacts in dimensionality-reduced plots, among others). This manuscript is a methodological and implementation reference: it does not report or interpret empirical outcomes of running the toolkit on any particular model or bridge-form set. The toolkit, its full source, and the corpora used to exercise it are archived separately (Section 9) under a persistent identifier, and are intended to be cited as an instrument by studies that use it to produce and interpret empirical results.

### 中文一句话结论
本文介绍并论证了一个开源工具包，利用跨领域重复出现的“桥接词”来测量Transformer语言模型在不同层中如何通过上下文区分词义，但不报告任何实证结果。

### English TL;DR
This paper documents and justifies an open-source toolkit that uses recurrent words across distinct domains (bridge forms) to measure how transformer language models contextualize and separate word senses in their internal representations, serving as a methodological reference without reporting empirical findings.

### 中文详细总结
该工具包围绕“桥接词”概念构建：一个单词形式固定，但在不同主题领域（如物理、经济、地理）中具有不同含义。由于词嵌入层对同一词形输出相同向量，后期层中出现的任何分离都只能归因于上下文。工具包流程包括：桥接词及其来源领域的声明、从维基百科获取语料、定位词出现位置、按层提取表示、使用成对轮廓系数测量领域分离度，以及配对可视化。每个设计选择都明确说明了要避免的方法论失败模式（如类别标签过宽导致的语义污染、轮廓系数的多组偏差、子词分词对齐问题、降维图中的轴可比性伪影）。本文档是方法和实现参考，不报告或解释任何特定模型或桥接词集上的实证结果。

### 方法 / 贡献
- 提出了“桥接词”概念，作为固定词形、变化语境和意义的受控构造，用于直接测试模型是否通过上下文区分词义。
- 开源工具包提供了端到端流程：声明桥接词和领域、从Wikipedia获取语料、定位词出现、按层提取隐藏状态、使用成对轮廓系数（而非多组）测量表示空间中的分离度，以及配对可视化。
- 每个设计选择均明确说明其理由及要避免的失败模式，提高可重复性和可审计性。
- 工具包作为仪器使用，可插入不同模型（编码器/解码器，大小不同，预训练目标不同），无需训练分类器。

### 实验或数据
本文未报告任何实验或数据集结果。工具包适用的语料从Wikipedia按领域获取，但文中未展示具体运行结果。工具包、源代码和示例语料库已单独存档。

### 值得关注点
- 桥接词构造提供了结构性保证：嵌入层输出相同，因此后期层分离只能来自上下文，无需依赖下游任务或人工标注。
- 成对轮廓系数避免了多组轮廓系数的偏差，可在全表示维度上直接测量模型自身的几何分离度，无需训练分类器。
- 可视化采用配对且轴可比的方法，避免降维伪影。
- 明确文档化了每个设计选择及其避免的方法论陷阱，提升了工具包的可靠性和可复现性。

### 局限性
- 本文是方法论参考，不报告任何实证结果，因此工具包在具体模型或桥接词上的有效性未被展示。
- 桥接词方法依赖于领域作为词义的代理，偶尔可能在同一领域内出现非典型词义，牺牲了词义级别的精确性。
- 工具包尚未包含统计验证或多模型、多桥接词的大规模分析，这些超出了单个工具包运行的范围。
- 已知的潜在失败模式（如类别标签过宽、子词分词对齐、降维伪影）虽已设计避免，但需要实际使用中进一步验证。

## 9. A Systematic Evaluation of Cross-Lingual Consistency Enhancement Methods in Multilingual Language Models

- Source: arxiv
- arXiv ID: 2609.04409
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.04409v1
- PDF: https://arxiv.org/pdf/2609.04409v1
- DOI: https://doi.org/10.48550/arXiv.2609.04409

### Authors

Jirui Qi, Mingyang Wang, Hinrich Schütze, Raquel Fernández, Arianna Bisazza

### Abstract

Multilingual language models often produce inconsistent answers to semantically equivalent questions across languages, motivating methods to improve cross-lingual consistency (CLC). However, existing methods are typically evaluated using different models, tasks, and protocols, leaving their relative strengths unclear. In this work, we present a unified evaluation of representative CLC-enhancement methods for question answering, spanning inference-time interventions and post-training approaches across three model families and three closed-form benchmarks. The results show that post-training methods are generally more reliable, with direct distribution alignment consistently improving CLC across all model-dataset combinations, while other methods are more sensitive to answer format and the breadth of language coverage. Notably, cross-domain transfer is limited unless source and target tasks share similar output formats. We further investigate whether CLC enhancement hurts models' ability to respond differently *when needed*, that is, when asked culture-dependent questions. Across two benchmarks of culturally diverse question answering, we find no systematic degradation in controlled closed-form evaluation, whereas open-ended generation reveals occasional accuracy reductions, particularly for non-English responses. Our work highlights the need to evaluate CLC enhancement for both cross-domain robustness and culturally appropriate variation, informing future work in post-training and benchmark development.

### 中文一句话结论  
后训练方法（特别是直接分布对齐）能稳定提高多语言模型的跨语言一致性，但跨领域迁移有限，且不会系统性损害文化多样性知识，仅在开放生成中对非英语回答有轻微准确率下降。

### English TL;DR  
Post-training methods, particularly direct distribution alignment, consistently improve cross-lingual consistency in multilingual language models, but their cross-domain transfer is limited, and while they do not systematically degrade culturally diverse knowledge in closed-form evaluations, they may cause slight accuracy reductions for non-English open-ended responses.

### 中文详细总结  
本文对多语言问答中提升跨语言一致性（CLC）的多种方法进行了统一评估，涵盖推理时干预和后训练两类方法，在三个模型族和五个基准上比较。结果表明，后训练方法普遍更可靠，其中直接分布对齐在所有模型-数据集组合上稳定提升CLC；其他方法则对答案格式和语言覆盖范围更敏感。跨领域迁移较弱，仅当源任务与目标任务共享相似输出格式时才有改进。此外，CLC增强不会在封闭式问答中系统性损害文化多样性知识，但在开放生成中观察到非英语回答的轻微准确率下降，提示存在过度对齐风险。

### 方法 / 贡献  
- 统一评估了四类代表性CLC增强方法：推理时表示干预（INCLINE）、英语枢轴偏好对齐（如MAPO）、多语言自对齐（CALM）和直接一致性优化（DCO）。  
- 首次系统评估CLC增强的跨领域迁移能力，发现增益仅在任务输出格式相似时转移。  
- 首次研究CLC增强对文化多样性知识的影响，发现封闭式QA中无系统性退化，且文化无关与文化多样性提示在表示空间可区分。  

### 实验或数据  
- 使用三个模型族（Qwen2.5-7B-Instruct、Gemma3-4B-IT及其他）和五个基准：文化无关数据集（BMLAMA、MMMLU、XCSQA）用于域内和跨域评估；文化多样性数据集（GEOMLAMA、BLEND）用于测试文化适应性。  
- 训练设置包括双语英语枢轴后训练和联合多语言后训练。  
- 评估指标覆盖封闭式问答（准确率、排名一致性）和开放式生成（自动化及人工评估）。  

### 值得关注点  
- 后训练方法（尤其是直接一致性优化）在稳定性上显著优于推理时干预，后者对语言覆盖和格式敏感。  
- 跨领域迁移普遍较弱，暗示当前方法主要对齐后训练分布附近的行为，而非实现广泛的多语言知识迁移。  
- 文化多样性知识在封闭式问答中得以保留，但在开放式生成中非英语回答准确率略有下降，需警惕过度对齐风险。  

### 局限性  
- 跨领域迁移能力有限，表明当前CLC增强方法无法将一致性泛化到分布外的任务或知识域。  
- 开放式生成中非英语回答的准确率下降暗示潜在的过度对齐问题，但仅基于两个文化多样性基准，泛化性需进一步验证。  
- 仅涵盖三个模型族和五个基准，可能无法代表所有多语言模型或任务类型。此外，实验未涉及低资源语言的扩展评估。

## 10. Molecular Déjà Vu: Digit-Level Retrieval of Published Values in Frontier Language Models

- Source: arxiv
- arXiv ID: 2609.05381
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2609.05381v1
- PDF: https://arxiv.org/pdf/2609.05381v1
- DOI: https://doi.org/10.48550/arXiv.2609.05381

### Authors

Matthias Busch, Marius Tacke, Sviatlana V. Lamaka, Mikhail L. Zheludkevich, Christian J. Cyron, Roland C. Aydin, Christian Feiler

### Abstract

Large language models (LLMs) are increasingly evaluated on molecular property benchmarks, but accuracy cannot distinguish a model that predicts a property from one that retrieves a published number. We audit 22 frontier models on 12 regression benchmarks for verbatim retrieval and find that it is widespread but relatively benchmark-specific: on five datasets more than $50\%$ of the LLMs show verbatim retrieval, while on the remaining datasets it appears only in isolated cells. We run our experiments at two reasoning levels and find that reasoning changes retrieval. The same experiments, on the same molecules and with the same prompt, are flagged $89\%$ more often at the higher reasoning level than at the lowest one. Finally, we test a way to interrupt retrieval in our most contaminated cases, and find that the strongest models in some cases still recognise a combination of transformed SMILES strings and original labels. Furthermore, suppressing retrieval moves the prediction errors of the different models closer together in relative terms, while their differing use of verbatim retrieval spreads them apart. This indicates that the general predictive capability of an LLM is not determined solely by the amount of memorised values. This work provides an overview of the amount and depth of verbatim retrieval in molecular regression benchmarks using LLMs.

### 中文一句话结论  
前沿语言模型在分子性质回归基准中频繁直接记忆并输出已发表数值，其发生程度因基准而异，且随推理强度增加而加剧。

### English TL;DR  
Frontier language models frequently retrieve memorized published values rather than genuinely predicting molecular properties, with this verbatim retrieval being widespread but benchmark-specific, increasing with reasoning level, and when suppressed, revealing that predictive capability does not depend solely on the amount of memorized values.

### 中文详细总结  
本文系统审查了22个前沿大语言模型在12个分子性质回归基准上的逐字检索现象。研究发现，检索普遍存在但高度依赖基准：在5个数据集中，超过50%的模型表现出逐字检索；在其他基准中则仅零星出现。提高模型的推理水平会显著增加检索率——相同分子和提示下，高推理水平标记的检索次数比低水平高89%。通过盲化实验（变换SMILES字符串并隐藏属性名称）试图抑制检索，发现最强模型在某些情况下仍能识别变换后的字符串与原始标签的组合。抑制检索后，不同模型的预测误差在相对值上趋于接近，而检索的差异则拉开其误差，表明模型的预测能力不仅取决于记忆数值的数量。

### 方法 / 贡献  
- 设计仅依赖于数字位数（精确到1、2、3位有效数字）的检测统计量，适用于数值回归基准。  
- 构建了22个模型×12个基准的“污染地图”，在受控推理水平下使用相同分子和提示。  
- 测量了推理水平对检索的影响（从最低到最高推理设置进行比较）。  
- 提出并测试了一种在上下文学习中抑制检索的盲化方法。  
- 主要贡献：①首次系统评估分子回归基准中的逐字检索；②揭示推理水平与检索的正相关；③证明抑制检索后模型预测误差的趋同现象。

### 实验或数据  
- 实验涵盖22个前沿模型（包括Gemini、GPT、Claude等）和12个分子性质回归基准（包括实验测量值、量子化学计算值、正对照45个教科书沸点以及2024–2025年抗病毒活性盲测结果）。  
- 每个模型在500个分子上零样本查询（正对照全量45个分子），要求输出三位有效数字。  
- 主实验使用约1,024 token推理水平，重复进行最低推理水平实验以比较。  
- 推理阶梯实验：5个模型在最多5个推理设置下运行每个基准的最多60个分子，每个设置重复3次。  
- 盲化实验：在4个模型及其最受污染的3个基准上测试，使用100个上下文示例和两种条件（原始SMILES vs 变换SMILES并隐藏属性名称）。  
- 数据来源包括FreeSolv、ChemBench等，所有基准的标签分布用于计算零假设基线。

### 值得关注点  
- 检索在不同基准间差异巨大，某些基准（如FreeSolv）几乎所有模型都高度污染。  
- 推理水平越高，检索越频繁，且并非所有模型对相同推理设置使用相同数量的推理token。  
- 盲化实验显示，最强模型即使面对变换的SMILES仍能恢复原始标签，且抑制检索后模型间预测误差差距缩小。  
- 同一模型在同一分子上，仅改变推理设置即可改变检索行为。  
- 三位有效数字的准确预测在实验噪声水平下几乎不可能实现，因此超低误差（如0.025 kcal/mol远低于0.6 kcal/mol不确定性）直接暴露了记忆。

### 局限性  
- 研究限于22个模型和12个基准，可能不覆盖所有前沿模型和化学性质任务。  
- 检测方法仅基于数字逐字匹配，可能无法捕捉近似记忆或非完全一致的检索（如舍入或单位转换）。  
- 盲化实验仅测试4个模型，且仅针对最污染的三个基准，泛化性有限。  
- 无法区分检索来自基准文件本身还是基础文献；两种来源对评估有效性的影响相同，但补救策略不同。  
- 零假设基于标签独立性假设，若基准中多位数字存在内在结构（如物理约束），则可能高估检索显著性。  
- 论文未明确讨论其他类型数据污染（如分子结构记忆）或对分类任务的适用性。

## Processing Notes

- Duplicate papers skipped: 0