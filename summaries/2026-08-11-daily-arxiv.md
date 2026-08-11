# Daily arXiv - 2026-08-11

- Source: GitHub Actions generated paper list
- Generated at: 2026-08-11T23:05:35
- Paper count: 10

## 1. UNMASK: Discovering and Causally Verifying Spurious Shortcuts in Text Classifiers

- Source: arxiv
- arXiv ID: 2608.09209
- Relevance: 4.6

### Links

- Abstract: http://arxiv.org/abs/2608.09209v1
- PDF: https://arxiv.org/pdf/2608.09209v1
- DOI: https://doi.org/10.48550/arXiv.2608.09209

### Authors

Chidaksh Ravuru, Shashank Srivastava

### Abstract

Neural language models trained on large crowdsourced corpora frequently exploit spurious surface patterns tied to target labels without true linguistic or causal relevance, boosting benchmark performance while failing on adversarial or out-of-distribution inputs. Existing approaches either require manual specification of the feature vocabulary or automate discovery only partially, leaving the gap between dataset-level correlation and model-level exploitation unaddressed. We present U N M ASK, a fully automated pipeline that discovers, causally verifies, and mitigates spurious correlations in text classifiers without additional human annotation. Given unlabeled training examples, U N M ASK generates candidate surface patterns as executable boolean expressions, filters them through a statistical validation protocol with independent replication, and establishes causal model dependence via verified counterfactual interventions. Causally confirmed features then serve as annotation-free group definitions for Deep Feature Reweighting, eliminating the group labels that standard DFR requires. Applied to BERT and RoBERTa trained on MNLI, our pipeline independently rediscovers established lexical-overlap and negation biases, verifying 9 of 10 features on BERT and 6 on RoBERTa, and improving HANS accuracy by up to 12.58 pp. On CivilComments-WILDS, programmatic groups match the 70.1% worst- group accuracy of hand-labeled DFR (Kirichenko et al., 2023) without demographic annotation. We further demonstrate that the discovery and validation stages generalize to reward model preference data, surfacing interpretable spurious correlations in RewardBench2.

### 中文一句话结论
UNMASK 是一个全自动流水线，无需人工标注即可发现、因果验证并缓解文本分类器中的虚假关联，在多个基准上提升准确率，并匹配需人工标注的去偏方法性能。

### English TL;DR
UNMASK introduces a fully automated pipeline that discovers, causally verifies, and mitigates spurious correlations in text classifiers—without human annotation—by using LLM-generated boolean expressions, statistical validation, and counterfactual interventions, achieving significant accuracy gains on benchmarks like MNLI and matching hand-labeled debiasing performance on CivilComments-WILDS.

### 中文详细总结
神经语言模型常依赖训练数据中与标签表面相关但无因果的伪模式（如词汇重叠、否定词），导致在分布外或对抗样本上性能下降。现有方法需要人工指定特征或只能部分自动化。UNMASK 提出四阶段流水线：1) 用 LLM 以布尔表达式形式生成候选表面模式；2) 通过独立复制的统计验证过滤；3) 用反事实干预建立因果模型依赖（区分数据集关联与模型利用）；4) 将因果确证的特征作为无标注组定义用于 Deep Feature Reweighting（无标注 DFR）。在 MNLI 上，UNMASK 独立恢复了已知的词汇重叠和否定偏差，对 BERT 验证 9/10 个特征，对 RoBERTa 验证 6/10，并将 HANS 准确率提升最多 12.58 个百分点。在 CivilComments-WILDS 上，程序化组匹配了需人工标注 DFR 的 70.1% 最差组准确率。该流水线还泛化到奖励模型偏好数据（RewardBench2），发现了可解释的虚假关联。

### 方法 / 贡献
- **全自动发现**：用 LLM 生成可执行的布尔表达式作为候选伪特征，无需人工预定义词汇。
- **统计验证**：通过 Fisher 精确检验和 Benjamini-Hochberg FDR 控制在独立复制实验中进行筛选。
- **因果验证**：通过反事实编辑（移除表面模式但保持语义标签）观测模型预测变化，建立模型层面的因果依赖。
- **无标注去偏**：将验证后的布尔表达式直接用作组定义，用于 Deep Feature Reweighting，消除了标准 DFR 所需的组标签。
- **跨任务泛化**：无需任务特定修改即可应用于 NLI、毒性检测和奖励模型偏好数据。

### 实验或数据
- **数据集**：MNLI（自然语言推理）、HANS（对抗性 NLI）、CivilComments-WILDS（毒性检测）、RewardBench2（奖励模型偏好）。
- **模型**：BERT、RoBERTa。
- **关键结果**：
  - MNLI：对 BERT 验证 9/10 个伪特征（如词汇重叠、否定），对 RoBERTa 验证 6/10。
  - HANS：准确率提升最高 12.58 个百分点。
  - CivilComments-WILDS：程序化组达到 70.1% 最差组准确率，匹配需人工标注的 DFR（Kirchenko et al., 2023）。
  - 在情感分析上正确返回零个被利用的特征，且去偏不起作用。

### 值得关注点
- **完全自动化**：从发现到缓解全程无需人工标注或预定义。
- **因果验证分离**：区分数据集层面的相关性和模型层面的利用，揭示模型间差异（如 RoBERTa 对某些矛盾类特征免疫）。
- **跨架构差异**：发现 BERT 和 RoBERTa 在利用同一伪特征上的不一致性。
- **泛化至偏好数据**：无需修改成功应用于 RewardBench2，发现可解释的虚假模式。

### 局限性
论文摘要未明确讨论局限性。潜在考虑包括：流水线依赖 LLM 生成候选模式的覆盖范围和质量，以及统计验证阈值的选择可能影响结果的可复现性；此外，反事实干预要求编辑后文本仍属输入分布，某些领域可能难以自动生成有效反例。

## 2. Instability of LLM Pre-Pretraining: It Doesn't Always Help. An Investigation on Multiple Languages

- Source: arxiv
- arXiv ID: 2608.08800
- Relevance: 4.5

### Links

- Abstract: http://arxiv.org/abs/2608.08800v1
- PDF: https://arxiv.org/pdf/2608.08800v1
- DOI: https://doi.org/10.48550/arXiv.2608.08800

### Authors

Sofiia Riazhskykh, Nam Luu, Ondřej Bojar

### Abstract

Pretraining LLMs on artificial languages ("pre-pretraining") is a technique that could reportedly increase token efficiency by 33%, i.e., save up to 33% of training tokens needed to reach a certain performance. We validate this prior result for English on a larger set of natural languages across four language families, using two different tokenizers and varying model sizes. We also relate the observed gains (or losses) in token efficiency to quantified linguistic properties of the languages, such as sentence length, morphological richness, and features of dependency syntactic trees (tree depth, number of children, number of crossing dependencies). Our empirical results indicate that the reported gains depend heavily on the experiment setup and the choice of random seed, although we can confirm the trend of stable gains with 128-Dyck pretraining of small models with the Llama tokenizer for most of the examined languages. On a general note, we argue that multiple training runs should be carried out at least for a subset of experiments to avoid the community adopting unstable approaches.

### 中文一句话结论
对多种自然语言进行LLM预训练前的“人工语言预训练”并不能稳定提升词元效率，结果高度依赖实验设置与随机种子，仅在部分小模型和128-Dyck条件下有稳定提升。

### English TL;DR
Pre-pretraining LLMs on artificial languages does not consistently improve token efficiency across multiple natural languages, with gains being highly unstable and sensitive to experimental setup and random seed, urging caution in adopting the approach.

### 中文详细总结
本文扩展了此前仅在英文上验证的“预预训练”方法，考察了四种语系的六种自然语言（英语、阿尔巴尼亚语、捷克语、丹麦语、荷兰语、芬兰语）。实验使用Llama 3架构的六种不同模型（参数规模253M至884M），以及Llama和Gemma两种词元器。预训练语言包括64-Dyck、128-Dyck、64-Shuffle Dyck和128-Shuffle Dyck，每种设置进行三次不同随机种子的训练。

结果表明，预训练带来的词元效率提升高度不稳定，同一设置下多次运行的结果波动较大。仅在128-Dyck预训练、使用Llama词元器的小模型上观察到稳定的增益。总体而言，作者建议至少对部分实验进行多次重复训练，以避免社区采纳不可靠的方法。

### 方法 / 贡献
- 将预预训练方法从英文扩展到多个自然语言（四种语系六种语言）。
- 系统比较了两种人工语言（Dyck和Shuffle Dyck）及两种k值（64和128）。
- 使用了两种不同词元器（Llama和Gemma）和六种不同规模模型。
- 量化了预训练带来的词元效率提升（或损失），并将其与语言的句法属性（如句子长度、形态丰富度、依存树深度等）进行了关联分析。
- 强调多次运行的重要性，揭示了结果对随机种子的敏感性。

### 实验或数据
- **数据来源**：自然语言训练集由FineWeb（英语）或FineWeb 2（其他语言）结合OpenSubtitles和EUBookshop按8:1:1比例混合而成，共320,000个序列，每序列2048个词元。评估使用mC4验证集的前2000行。
- **预训练数据**：人工语言序列16,000个，每序列2048个词元（500训练步，批量大小32）。
- **模型**：基于Llama 3架构，六种配置（154M、308M、481M有效参数，分别搭配Llama或Gemma词元器，总参数量253M至884M）。
- **实验设置**：每种模型进行三种训练方式（无预训练、64-Dyck预训练、128-Dyck预训练、64-Shuffle Dyck预训练、128-Shuffle Dyck预训练），每种方式使用三个不同随机种子重复。
- **评估指标**：词元效率提升（即预训练模型达到基线模型相同验证损失所需减少的训练步数）。

### 值得关注点
- 预预训练的效果并非普遍适用，其提升高度依赖实验细节：模型大小、词元器选择、人工语言类型及k值。
- 128-Dyck预训练结合Llama词元器的小模型是唯一观察到稳定增益的设置。
- 不同随机种子下结果差异显著，强调多次运行的必要性。
- 词元器对人工语言的编码方式（如Gemma将数字拆分为独立数字）显著影响迁移效果。
- 论文将增益与语言属性关联，但未发现简单规律。

### 局限性
- 实验仅覆盖六种欧洲语言，未涉及非欧洲或低资源语言。
- 模型规模较小（最大884M总参数），结果可能无法推广到更大模型。
- 预训练数据量和训练步数固定，未探索最优的token-to-parameter比率（远低于Chinchilla最优值）。
- 仅考虑两种人工语言（Dyck和Shuffle Dyck）及两种k值，其他类型人工语言未测试。
- 未分析预训练对下游任务（如翻译、问答）的影响，仅关注语言建模损失。
- 由于结果的不稳定性，论文未提供明确的预训练策略建议。

## 3. UNSPECIFIC: General Constraint Synthesis for Breaking Copy-and-Paste Shortcut in LLM Instruction Following

- Source: arxiv
- arXiv ID: 2608.09154
- Relevance: 4.4

### Links

- Abstract: http://arxiv.org/abs/2608.09154v1
- PDF: https://arxiv.org/pdf/2608.09154v1
- DOI: https://doi.org/10.48550/arXiv.2608.09154

### Authors

Jeet Sharma, Balpreet Kaur, Jeremiah Hong, Hamed Zamani, Haw-Shiuan Chang

### Abstract

Large language models (LLMs) are increasingly expected to follow long lists of constraints in complex instructions, and synthesizing instructions from a reference document (i.e., back-translation) is a widely used method to measure/enhance LLMs' ability to follow complex instructions. However, this method introduces a critical loophole: the constraint synthesis model copies text from the reference as a very specific constraint and the evaluated LLM trivially satisfies the constraint by copying its text in the response. To address these issues, we propose UNSPECIFIC, a novel framework that synthesizes constraints common to two similar reference articles to reduce copy-pasting, selectively hardens only trivially satisfied constraints to balance difficulty and naturalness, and evaluates satisfaction on both the generated article and its summary to penalize superficial instruction following. Consequently, we built the UNSPECIFIC benchmark on news, story, and blog domains to analyze the copy-pasting behavior of LLMs. Our results show that our synthesized constraints are not only more challenging (e.g., the satisfaction rate of GPT-5 Mini drops from 90% to 78%) and natural (LLM win-rate gap improves by 30%) from a human perspective but also mitigate the copy-pasting. We also find that a large portion of constraints are satisfied superficially (i.e., not satisfied in the core narrative of the article). The code and datasets are released at https://github.com/JeetDSharma/UNSPECIFIC.

### 中文一句话结论
UNSPECIFIC通过从两篇相似文章提取通用约束、选择性强化已满足的简单约束及摘要评估，有效减少大语言模型在指令遵循中的复制粘贴捷径，提升约束的挑战性与自然性。

### English TL;DR
UNSPECIFIC introduces a framework to break the copy-and-paste shortcut in LLM instruction following by synthesizing common constraints from two similar articles, selectively hardening trivially satisfied constraints, and evaluating on summaries to penalize superficial responses, resulting in more challenging and natural constraints.

### 中文详细总结
论文指出，基于参考文档回译的方式合成指令约束存在严重漏洞：约束生成模型可能直接从参考文档复制文本作为约束，而被评估的LLM则通过简单复制该文本到回答中来轻易满足约束。为解决此问题，UNSPECIFIC框架提出三项创新：1）从两篇相似参考文章中提取通用约束，减少具体细节泄露并降低复制行为；2）基于评估结果，仅对已被基础文章满足的约束进行强化修订，平衡难度与自然度；3）在生成文章及其摘要上同时评估约束满足度，以检测浅层指令遵循。实验表明，该框架使GPT-5 Mini的满足率从90%降至78%，同时人类视角下的LLM胜率差距改善30%，并能有效削弱复制粘贴行为。

### 方法 / 贡献
- 提出从两篇相似文章提取通用约束的方法，避免生成过于具体或不自然的约束，减少信息泄露。
- 提出评估驱动的约束修订策略：先让LLM仅根据主任务生成基础文章，再仅强化那些被基础文章自然满足的约束，从而在不牺牲自然度的前提下增加难度。
- 引入对生成文章进行摘要后再评估约束满足度的指标，以量化LLM是否在核心叙事中深度遵循约束，而非仅在细节上表面满足。
- 构建包含新闻、故事、博客领域的UNSPECIFIC基准，用于分析LLM的复制粘贴行为。

### 实验或数据
- 实验在新闻、故事、博客三个领域进行，使用GPT-5 Mini和Llama-3 8B作为被评估模型。
- 主要结果：GPT-5 Mini在原始评估中的满足率从90%（基线）降至78%（UNSPECIFIC）；核心评估（摘要后）中满足率更低，显示浅层遵循被有效惩罚。
- 人类偏好评估显示，UNSPECIFIC约束的“LLM胜率差距”改善30%（即人类更倾向认为UNSPECIFIC约束更自然）。
- 对比了单文章约束、通用提示约束、直接修订等基线，UNSPECIFIC在难度与自然度上均取得更好平衡。

### 值得关注点
- 明确指出并量化了回译式约束合成中的复制粘贴捷径问题，这在此前研究中常被忽略。
- 提出的摘要后评估方法是一种新颖且实用的度量浅层指令遵循的方式，有助于更真实地衡量LLM的指令遵循能力。
- 约束修订仅针对简单约束，而非全部，这一策略有效避免了过度强化导致的不自然问题。

### 局限性
- 通用约束可能过于宽泛，在某些任务中可能降低约束的指导性，需要依靠评估修订来补充难度。
- 对两篇相似文章的选择依赖语义相似度阈值（<0.85），该阈值的设定可能影响约束的通用性与信息泄露程度，未深入探讨其敏感性。
- 实验主要在新闻、故事、博客领域进行，未验证在技术文档、法律文本等其他领域的效果。

## 4. Reproducing and Stress-Testing Two Approaches to LLM Reasoning Reliability: Test-Time Probability Aggregation and Logic-Representation Editing

- Source: arxiv
- arXiv ID: 2608.08514
- Relevance: 4.3

### Links

- Abstract: http://arxiv.org/abs/2608.08514v1
- PDF: https://arxiv.org/pdf/2608.08514v1
- DOI: https://doi.org/10.48550/arXiv.2608.08514

### Authors

Minhan Cho, Jimin Kweon

### Abstract

We independently reproduce two recent methods for making large language model (LLM) reasoning more reliable, and stress-test them across domains and models (RPC across four new task domains with Qwen3-8B, LCF across four 7-8B models). The first, RPC, aggregates token probabilities and self-consistency at inference; the second, LCF, trains projectors that split hidden states into "content" and "logic" and edits the logic part toward a valid region. Validating such reliability claims matters because the original evaluations are run by each method's own authors and were never independently reproduced or stress-tested across models and domains, and LCF shipped no public code. We re-run RPC's published-path aggregation and re-implement LCF's projector, contrastive, and intervention pipeline, then extend both to text-to-SQL, legal extraction, fallacy identification, and precedent grading, and probe LCF's representation directly. RPC reproduces the original grid exactly on the authors' released reasoning paths; on four new domains its edge over self-consistency is never significant (ties or small mixed differences, paired p >= 0.28), and on BIRD, the one domain where we vary the budget, the edge grows with K as predicted but its largest gap (+2.5 accuracy at K=32, p=0.16) reverses to -0.25 when we enlarge the sample to n=200. LCF's logic-validity direction is real but weak (0.82 separability at the single best sub-layer versus 0.95 for a semantic-attribute control); its one positive effect (Qwen3 $Δ$Prob) is not significant (p=0.56), while it significantly reduces $Δ$Prob on two of the other three models.

### 中文一句话结论
该独立复现研究表明，RPC方法在新领域上相比自一致性无显著优势，而LCF的逻辑编辑效果微弱且在不同模型上表现不稳定甚至有害。

### English TL;DR
This independent reproduction and stress-test of two LLM reasoning reliability methods found that RPC's test-time probability aggregation exactly replicated on original data but showed no significant advantage over self-consistency on new domains, while LCF's logic-representation editing showed a real but weak logic-validity signal that was not reliably controllable and significantly reduced performance on two of three other models.

### 中文详细总结
本文独立复现并压力测试了两种提升LLM推理可靠性的方法：RPC（测试时概率聚合）和LCF（逻辑表示编辑）。研究者将RPC扩展到四个新任务领域（Text-to-SQL、法律提取、谬误识别、先例分级）并使用Qwen3-8B模型；将LCF应用到四个7-8B参数模型上。主要发现：
- RPC在原作者发布的推理路径上完美复现了原始结果，但在新领域上与自一致性基线相比从未达到统计显著性（所有配对p值≥0.28）。在BIRD数据集上，尽管随着采样数K增加RPC的优势有所增长，但在扩大样本量后该优势消失甚至逆转。
- LCF的逻辑有效性方向虽然真实存在但很弱（最佳子层上可分性0.82，而语义属性控制为0.95）；其对Qwen3的正面效果不显著（p=0.56），却显著降低了Llama-2和Mistral的效果。

### 方法 / 贡献
- 对RPC方法的忠实复现：使用作者发布的推理路径，精确复现了其原始结果网格
- 对LCF方法的从头复现：实现了投影器、对比学习和干预流程
- 将两种方法扩展到四个新任务领域进行压力测试（BIRD、KO-VER、KCC、LFUD）
- 对LCF的表示层直接分析，验证其逻辑有效性信号的真实性但弱于预期
- 尝试使用对比激活引导（CAA）实现模型无关的逻辑控制

### 实验或数据
- RPC评估：使用Qwen3-8B在四个新领域（BIRD-80例、KO-VER-150例、KCC-320例、LFUD-540例）上进行测试
- LCF评估：使用四个7-8B模型（Qwen3、Llama-2、Mistral、Vicuna）
- 数学推理路径使用原作者发布的四个竞赛数学基准（MATH、MathOdyssey、OlympiadBench、AIME）
- LCF数据包括：LFUD（540/204例）、法律类比数据集（Legal-LCF、KCC-legal）和合成三段论数据集

### 值得关注点
- RPC完美复现了原作者的结果，表明其代码和实验是可复现的
- 两个方法的不对称结果：RPC从未显著损害任何领域，而LCF在某些模型上显著降低性能
- LCF的逻辑有效性方向真实存在但比预期弱（0.82 vs 语义控制的0.95可分性）
- LCF未公开代码，本研究提供了首个独立的从头复现

### 局限性
- 评估集规模较小，使得结论更具方向性而非决定性
- 新领域的采样预算有限（BIRD最多K=32，KCC固定K=16）
- LCF的重现仅针对架构和大小为7-8B的模型，未测试更大模型
- 部分数据集（KO-VER、MoodRisk、KCC）因项目进行中的限制无法公开获取

## 5. Scaling Inherently Interpretable Language Models

- Source: arxiv
- arXiv ID: 2608.07594
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.07594v1
- PDF: https://arxiv.org/pdf/2608.07594v1
- DOI: https://doi.org/10.48550/arXiv.2608.07594

### Authors

Guide Labs Team, Andreas Madsen, Aya Abdelsalam Ismail, Giang Nguyen, Isaac Plant, Muawiz Chaudhary, Nathaniel Monson, Saqib Azim, Zhichen Guo, Julius Adebayo

### Abstract

Interpretability is often treated as a tax on capability: language models are trained as opaque systems, then explained after the fact, with methods whose reliability is difficult to establish. In this work, we challenge this premise. Rather than reverse-engineering a model, we make interpretability a constraint of the training pipeline, optimized alongside the language modeling objective. Across three orders of magnitude of compute, on both autoregressive and diffusion language models, interpretability scales with capability rather than against it. Surprisingly, model representations become more disentangled and aligned with human-understandable concepts with scale.
  We instantiate the training-time recipe with Steerling-8B, a diffusion language model with a causal attention mask. For any group of generated tokens, Steerling-8B attributes the output to relevant input tokens, human-understandable concepts, and training data. This enables closed-loop intervention: diagnose an output through its concept or feature attribution, retrieve similar training data, and correct the behavior through concept steering without retraining. Steerling-8B remains competitive with open peer models trained on substantially 2-16x more compute, suggesting a different scaling paradigm: interpretability can be designed into training, and it improves with scale.

### 中文一句话结论

基于已有摘要判断：Interpretability is often treated as a tax on capability: language models are trained as opaque systems, then explained after the fact, with methods whose reliability is difficult to establish. In this work, we challenge this premise. Rather than reverse-engineering a model, we make interpretability a constraint of the training pipeline, optimized alongside the language modeling objective. Across three orders of magnitude of compute, on both autoregressive and diffusion language models, interpretability scales with capability rather than against it. Surprisingly, model representations become more disentangled and aligned with human-understandable concepts with scale.
  We instantiate the training-time recipe with Steerling-8B, a diffusion language model with a causal attention mask. For any group of generated tokens, Steerling-8B attributes the output to relevant input tokens, human-understandable concepts, and training data. This enables closed-loop intervention: diagnose an output through its concept or feature attribution, retrieve similar training data, and correct the behavior through concept steering without retraining. Steerling-8B remains competitive with open peer models trained on substantially 2-16x more compute, suggesting a different scaling paradigm: interpretability can be designed into training, and it improves with scale.

### English TL;DR

Interpretability is often treated as a tax on capability: language models are trained as opaque systems, then explained after the fact, with methods whose reliability is difficult to establish. In this work, we challenge this premise. Rather than reverse-engineering a model, we make interpretability a constraint of the training pipeline, optimized alongside the language modeling objective. Across three orders of magnitude of compute, on both autoregressive and diffusion language models, interpretability scales with capability rather than against it. Surprisingly, model representations become more disentangled and aligned with human-understandable concepts with scale.
  We instantiate the training-time recipe with Steerling-8B, a diffusion language model with a causal attention mask. For any group of generated tokens, Steerling-8B attributes the output to relevant input tokens, human-understandable concepts, and training data. This enables closed-loop intervention: diagnose an output through its concept or feature attribution, retrieve similar training data, and correct the behavior through concept steering without retraining. Steerling-8B remains competitive with open peer models trained on substantially 2-16x more compute, suggesting a different scaling paradigm: interpretability can be designed into training, and it improves with scale.

### 中文详细总结

基于论文摘要，该工作主要内容如下：Interpretability is often treated as a tax on capability: language models are trained as opaque systems, then explained after the fact, with methods whose reliability is difficult to establish. In this work, we challenge this premise. Rather than reverse-engineering a model, we make interpretability a constraint of the training pipeline, optimized alongside the language modeling objective. Across three orders of magnitude of compute, on both autoregressive and diffusion language models, interpretability scales with capability rather than against it. Surprisingly, model representations become more disentangled and aligned with human-understandable concepts with scale.
  We instantiate the training-time recipe with Steerling-8B, a diffusion language model with a causal attention mask. For any group of generated tokens, Steerling-8B attributes the output to relevant input tokens, human-understandable concepts, and training data. This enables closed-loop intervention: diagnose an output through its concept or feature attribution, retrieve similar training data, and correct the behavior through concept steering without retraining. Steerling-8B remains competitive with open peer models trained on substantially 2-16x more compute, suggesting a different scaling paradigm: interpretability can be designed into training, and it improves with scale.

### 方法 / 贡献

未提供独立的方法细节；请参考摘要和论文链接。

### 实验或数据

未提供独立的实验或数据细节；请参考摘要和论文链接。

### 值得关注点

该条目的相关性来自 Zotero 语料相似度排序，可优先根据 relevance 和摘要判断是否精读。

### 局限性

自动总结主要基于标题、摘要和可用正文预览，可能遗漏全文中的实验细节。

## 6. Cultivar: A Contrastive and Locale-Oriented Translation Benchmark for Investigating Contamination and Localisation Robustness

- Source: arxiv
- arXiv ID: 2608.09766
- Relevance: 4.2

### Links

- Abstract: http://arxiv.org/abs/2608.09766v1
- PDF: https://arxiv.org/pdf/2608.09766v1
- DOI: https://doi.org/10.48550/arXiv.2608.09766

### Authors

Pinzhen Chen, Koel Dutta Chowdhury, Xiaoya Xu, David Tan, Doreen Osmelak, Ona de Gibert, Ariun-Erdene Tumurchuluun, Ashok Urlana, Fedor Sizov, Hale Sirin, Jesujoba Alabi, Karrar Talib Abed, Mateusz Klimaszewski, Nikolay Bogoychev, Niyati Bafna, Patricia Schmidtova, Preksha Manjunath Shanbhag, Sherrie Shen, Vilem Zouhar, Vivek Iyer, Yasser Hamidullah, Yusser Al Ghussin, Zheng Zhao

### Abstract

Multilingual translation benchmarks are typically sourced in English and translated into other languages, treating language pairs as the unit of evaluation---a design that is prone to contamination over time and overlooks locale and cultural considerations. We therefore advocate for source-contrastive evaluation and instantiate it with Cultivar, a localised subset of FLORES, which enables locale-specific translation evaluation. When paired with unlocalised counterparts, performance discrepancy allows the probing of data contamination and localisation robustness. We benchmark 32 open-weight models and find that MT-specialised models are less robust, a few models potentially overfit FLORES, and models tend to translate US content better than that of other locales, regardless of language.

### 中文一句话结论
本文提出一个名为 Cultivar 的源语言对比翻译基准，基于 FLORES 构建本地化版本，用于评估机器翻译模型的数据污染和本地化鲁棒性，发现翻译专用模型鲁棒性较差，且模型普遍更擅长翻译美国内容。

### English TL;DR
The paper introduces Cultivar, a locale-oriented, source-contrastive translation benchmark built from FLORES to evaluate data contamination and localization robustness, finding that MT-specialized models are less robust and often overfit to US-centric content.

### 中文详细总结
**问题背景**：当前多语言翻译基准通常以英语为源语言翻译成其他语言，将语言对作为评估单元。这种设计容易随时间产生数据污染（data contamination），且忽视了地域（locale）和文化差异。例如，同一种语言在不同地区（如英语在美国、英国、新加坡）的表达方式不同，现有基准无法区分。

**Cultivar 基准**：作者构建了 Cultivar，它是 FLORES 数据集的本地化子集，覆盖 27 个地域（locale）。通过对比本地化版本与原始 FLORES 版本之间的性能差异，可以探测模型是否存在数据污染（即过度拟合 FLORES）以及本地化鲁棒性。

**构建流程**：(1) 从 FLORES 英文开发集中筛选出富含命名实体的句子（200句）；(2) 利用大语言模型（GPT-5.5）进行本地化改写，保留原句结构但替换为适合目标地域的内容；(3) 由精通源语言且生活在目标地域的标注员进行人工审核编辑。

**评估结果**：评测了 32 个开源权重的模型，发现：
- 翻译专用模型（MT-specialized）的本地化鲁棒性较差，即翻译本地化内容时性能下降更多；
- 少数模型可能已过度拟合 FLORES 数据集；
- 无论目标语言为何，模型翻译美国相关内容的效果普遍优于其他地域的内容。

### 方法 / 贡献
1. **资源贡献**：构建 Cultivar 基准，保留多语言平行可对比性同时融入本地化源语言内容。
2. **评估范式**：提出源语言对比评估（source-contrastive evaluation），通过对比本地化版本与原始版本性能差异来量化本地化鲁棒性和数据污染。
3. **经验发现**：对 32 个模型的系统评测揭示了翻译模型在本地化内容上的薄弱环节。

### 实验或数据
- 基准数据：基于 FLORES 开发集，经过筛选（200句富含命名实体的句子）和本地化改写（27个地域），最终包含源语言与英语的平行句对。
- 评测模型：32 个开源权重模型（包括通用语言模型和翻译专用模型）。
- 评测指标：BLEU、chrF、词召回率（word recall）。
- 对比实验：模型在 Cultivar（本地化版本）与 FLORES（原始版本）上的性能差异。

### 值得关注点
1. 揭示了翻译模型普遍存在的“美国中心”偏差，即对美国内容的翻译质量显著高于其他英语地区（如英国、新加坡）。
2. 通过对比本地化版本与原始 FLORES 的性能差距，发现部分模型可能已过度拟合 FLORES 数据集。
3. 翻译专用模型在本地化测试中表现更差，说明其泛化能力弱于通用语言模型。

### 局限性
1. 当前仅针对任意语言到英语（any-to-English）的翻译方向进行了本地化，未覆盖其他翻译方向。
2. 本地化主要局限于命名实体的替换，对于更细微的文化差异（如语气、习惯表达）可能覆盖不足。
3. 人工标注过程耗时较长（每位标注员4-12小时），限制了可扩展性。
4. 未涵盖所有地域变体，仅选择了27个地点，部分语言仅有单一地域版本。

## 7. AraSSM: A bidirectional state-space encoder for Arabic masked language modeling

- Source: arxiv
- arXiv ID: 2608.08256
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.08256v1
- PDF: https://arxiv.org/pdf/2608.08256v1
- DOI: https://doi.org/10.48550/arXiv.2608.08256

### Authors

Ahmed Amine Aliane, Hassina Aliane, Nasredine Semmar

### Abstract

Pretrained Transformer encoders such as AraBERT, MARBERT, and CAMeLBERT have become the standard backbone for Arabic natural language understanding, but their self-attention mechanism scales quadratically with sequence length, which limits efficiency on long documents. Mamba, a selective state-space model (SSM), offers linear-time sequence modeling as a competitive alternative to attention, yet no dedicated bidirectional Mamba encoder pretrained specifically for Arabic currently exists. We introduce AraSSM, a bidirectional Mamba encoder pretrained via masked language modeling on a corpus combining Arabic Wikipedia and CulturaX text, trained end-to-end on four consumer-grade NVIDIA RTX 2080Ti GPUs (11GB) over approximately ten days. We evaluate AraSSM by fine-tuning on four established Arabic NLU benchmarks covering sentiment classification (HARD), named entity recognition (ANERcorp), extractive question answering (ARCD), and natural language inference (XNLI-ar), following the per-task evaluation protocol introduced by AraBERT, and report results as mean +/- standard deviation across three fine-tuning seeds. AraSSM matches or exceeds published base-sized Transformer baselines on sentiment classification (96.37 +/- 0.03% accuracy on HARD), is competitive on extractive QA (32.19 +/- 1.07 EM, 63.79 +/- 0.25 F1 on ARCD) and named entity recognition (81.54 +/- 0.30 entity-level F1 on ANERcorp), and trails the base-sized Transformer range on natural language inference (72.83 +/- 0.07% accuracy on XNLI-ar), despite being trained entirely from scratch on consumer hardware rather than large-scale accelerator clusters.

### 中文一句话结论  
我们提出 AraSSM，首个专为阿拉伯语预训练的双向 Mamba 编码器，在四个 NLU 基准上匹配或超过同等规模的 Transformer 基线，且仅使用四块消费级 GPU 完成预训练。

### English TL;DR  
AraSSM introduces the first bidirectional Mamba encoder pretrained for Arabic via masked language modeling. It matches or surpasses base-sized Transformer baselines on sentiment classification, NER, and extractive QA, while trailing on NLI, all trained on four consumer GPUs.

### 中文详细总结  
传统阿拉伯语 Transformer 编码器（如 AraBERT）依赖自注意力机制，计算复杂度随序列长度二次增长，限制了对长文档的处理效率。Mamba 是一种选择性状态空间模型（SSM），能以线性复杂度进行序列建模，但目前尚无专为阿拉伯语预训练的双向 Mamba 编码器。本文提出 AraSSM，采用双向块设计（前向+后向 SSM 混合器），通过掩码语言建模在阿拉伯语 Wikipedia 和 CulturaX 语料上预训练，参数规模 1.05 亿，与 AraBERT-base 相近。全部训练在四块 RTX 2080Ti（11GB）上进行，耗时约十天。微调评估覆盖四个标准任务：情感分类（HARD）、命名实体识别（ANERcorp）、抽取式问答（ARCD）和自然语言推理（XNLI-ar），每种任务使用三个种子报告均值和标准差。结果显示：AraSSM 在 HARD 上达到 96.37% 准确率，超过基线；在 ARCD 上 EM 32.19、F1 63.79；在 ANERcorp 上实体级 F1 81.54，与基线持平；在 XNLI-ar 上准确率 72.83%，略低于基线。

### 方法 / 贡献  
1. 首次为阿拉伯语预训练双向 Mamba 编码器（AraSSM），采用前向+后向选择性扫描混合器，在保持 O(L) 复杂度的同时获取双向上下文。  
2. 提出针对填充位置的掩码策略，防止后向扫描中填充信息泄漏到有效序列。  
3. 在消费级硬件上完成端到端训练，验证 SSM 架构在有限计算预算下的可行性。

### 实验或数据  
- 预训练语料：阿拉伯语 Wikipedia 和 CulturaX 文本，经文档级去重与分块处理。  
- 微调评估基准：HARD（情感分类）、ANERcorp（命名实体识别）、ARCD（抽取式问答）、XNLI-ar（自然语言推理），遵循 AraBERT 的逐任务评估协议。  
- 每个任务使用三个随机种子微调，报告均值 ± 标准差。  
- 硬件：四块 NVIDIA RTX 2080Ti（11GB），预训练约 10 天。

### 值得关注点  
- 仅用四块消费级 GPU 完成预训练，计算预算远低于阿拉伯语 Transformer 基线（通常使用大规模加速器集群）。  
- 在多个任务上匹配甚至超越同等规模 Transformer 模型，证明 SSM 架构在资源受限场景下的竞争力。  
- 填补了阿拉伯语无专用 Mamba 预训练编码器的空白，为后续低成本阿拉伯语 NLU 研究提供新方向。

### 局限性  
- 在自然语言推理（XNLI-ar）上准确率（72.83%）低于基座 Transformer 范围，可能存在语义理解上的限制。  
- 仅评估四个任务，未覆盖更广泛的阿拉伯语 NLU 基准（如 ORCA/ALUE 复合榜单）。  
- 隐藏维度（512）小于 AraBERT-base（768），可能影响表示容量；且仅在消费级硬件训练，模型规模和训练数据量有限。

## 8. Unified Hallucination Fuzzing for Multimodal Large Language Models

- Source: arxiv
- arXiv ID: 2608.07525
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.07525v1
- PDF: https://arxiv.org/pdf/2608.07525v1
- DOI: https://doi.org/10.48550/arXiv.2608.07525

### Authors

Pengfei Zhou, Jiajun Song, Zhiwei Tang, Yixing Ma, Xiaopeng Peng, Donghui Si, Yuhang Xu, Huiqi Song, Yiyuan Miao, Yichen Qian, Weihua Chen, Wangbo Zhao, Bohan Zhuang, Jiasheng Tang, Yang You

### Abstract

Hallucination remains a persistent challenge for Multimodal Large Language Models (MLLMs), severely limiting their reliability in high-stakes applications. Existing evaluations, predominantly based on static benchmarks, suffer from narrow taxonomical coverage and rapid performance saturation, failing to reflect model robustness in evolving real-world scenarios. To bridge this gap, we present a systematic evaluation framework integrating a comprehensive benchmark with self-evolving stress testing. First, we introduce UniHall, a fine-grained dataset grounded in a unified taxonomy spanning Object, Instruction, and Knowledge dimensions. Second, to address benchmark saturation, we propose Self-Adaptive Multimodal Fuzzing (SAMF), a self-adaptive framework that employs evolutionary mutation strategies to explore the boundaries of model hallucinations. Crucially, to ensure reliable assessment of dynamic inputs, SAMF incorporates a structured metric suite driven by an ensemble of multi-modal oracles. Our extensive experiments reveal that state-of-the-art MLLMs exhibit significant performance degradation under fuzzing compared to conventional settings, exposing a dissociation between reasoning capabilities and factual grounding. Furthermore, we identify a helpfulness-hallucination trade-off, where reinforcement learning alignment inadvertently exacerbates sycophancy in instruction-following tasks. The framework, code and benchmark are available at https://github.com/LanceZPF/EvalHall.

### 中文一句话结论  
本文提出基于统一幻觉分类法的多模态大模型评估框架，包括细粒度基准 UniHall 和自适应模糊测试 SAMF，揭示了模型在动态测试下性能显著下降以及“有用性‑幻觉”权衡。

### English TL;DR  
This work presents a systematic evaluation framework integrating UniHall—a fine-grained benchmark built on a unified Object–Instruction–Knowledge taxonomy—and SAMF, a self-adaptive fuzzing approach that uses evolutionary mutation strategies to probe hallucinations in Multimodal Large Language Models, exposing significant performance degradation and a helpfulness‑hallucination trade-off.

### 中文详细总结  
多模态大模型（MLLM）的幻觉问题在静态基准中常被快速饱和，难以反映真实场景的鲁棒性。为此，本文首先构建 UniHall 基准，涵盖物体、指令、知识三个维度的 2170 个细粒度实例，支持 Yes/No 和开放式 VQA 两种格式。接着提出 SAMF 自适应模糊测试框架，结合文本与图像的认知对抗性变异（如冗余干扰、知识冲突注入等），并利用多模态 oracle 套件（目标检测器、对齐模型、符号规则、LLM 裁判等）对动态输入进行结构化评估。实验表明，当前最先进的 MLLM 在模糊测试下性能显著下降，推理能力与事实根基存在脱节；同时发现，通过强化学习对齐“有用性”会加重谄媚式幻觉，即模型倾向于编造信息迎合误导性指令。

### 方法 / 贡献  
1. 提出 Unified Hallucination Taxonomy（物体、指令、知识三维度），覆盖多种子类型。  
2. 构建 UniHall 基准，融合开放域与领域特定数据，提供细粒度标注和人工质控。  
3. 提出 SAMF 自适应模糊测试框架，包含文本/图像变异算子、进化策略（含强化学习）以及结构化 oracle 评估管线。  
4. 通过系统性压力测试，揭示 MLLM 的“有用性‑幻觉”权衡，为模型训练提供警示。

### 实验或数据  
- 使用 UniHall 基准（2170 个实例，900 个 Yes/No，1270 个开放式 VQA），覆盖物体、指令、知识三大类幻觉。  
- 对 Qwen2.5‑VL‑7B、Qwen3‑VL‑8B 等模型进行标准评估和 SAMF 模糊评估。  
- 实验发现模糊测试下模型整体幻觉率（GHR）显著上升，推理与事实根基分离；强化学习对齐的模型在指令遵循任务中谄媚式幻觉加重。

### 值得关注点  
- 模糊测试揭示静态高分掩盖下的模型脆弱性，提供更真实的鲁棒性评价。  
- “有用性‑幻觉”权衡：强化学习对齐可能无意中加剧谄媚式幻觉，对安全部署具有重要启示。

### 局限性  
论文未显式讨论局限性。从其方法论可推测：SAMF 的进化策略和 oracle 集成计算成本较高；oracle 的覆盖范围与准确性可能影响评估可靠性；当前实验仅针对有限模型集和变异算子，在更广泛场景（如视频、音频模态）的泛化性有待验证。

## 9. Position Bias in Ordinal Classification: A Systematic Evaluation

- Source: arxiv
- arXiv ID: 2608.08869
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.08869v1
- PDF: https://arxiv.org/pdf/2608.08869v1
- DOI: https://doi.org/10.48550/arXiv.2608.08869

### Authors

Yu Wang, Jeffrey Zhou, Menglin Liu, Ge Shi

### Abstract

Large language models are increasingly used for ordinal classification, yet semantically equivalent changes to prompt organization can alter their predictions. We conduct systematic experiments to characterize positional bias from label order, demonstration order, and demonstration placement. First, we apply the three probes to ten frontier LLMs on a common ordinal-classification task; every model is sensitive to all three positional sources, showing that the problem is pervasive. Second, we vary eight prompt-, task-, and model-level factors across five datasets; accuracy and stability are often misaligned, and only lower scale cardinality consistently improves both. Third, we compare pointwise, pairwise, and listwise inference, alternative aggregation and debiasing methods, and joint configurations; the tested corrections do not provide a reliable remedy, while a comparison-based listwise formulation offers the best balance but transfers unevenly across models and bias sources. These findings show that positional robustness depends on the full system configuration rather than the model alone. Ordinal-classification systems should therefore be selected jointly for predictive performance and stability.

### 中文一句话结论  
在基于大语言模型的序数分类中，位置偏差（来自标签顺序、示例顺序和示例位置）普遍存在且难以可靠缓解，系统整体配置对鲁棒性的影响大于模型本身。

### English TL;DR  
This systematic evaluation shows that positional biases from label order, demonstration order, and demonstration placement are pervasive in LLM-based ordinal classification, that accuracy and stability are often misaligned, and that robust performance depends on the full system configuration rather than the model alone.

### 中文详细总结  
本研究系统评估了LLM在序数分类中面临的三种位置偏差：（1）标签顺序映射；（2）示例顺序；（3）示例位置。在10个前沿LLM上的实验表明，所有模型均对所有三种偏差敏感，偏差普遍存在。通过变化8个提示、任务和模型层面的因素（跨5个数据集），研究发现准确性与稳定性经常不一致，只有降低分类尺度（scale cardinality）能同时提升两者。对比多种推理范式（pointwise/pairwise/listwise）和去偏方法后发现，现有校正手段效果不稳定，基于比较的listwise推理方法在平衡性能与鲁棒性上最佳，但不同模型和偏差源间迁移不均匀。结论：序数分类系统应基于多目标鲁棒性（准确性与稳定性）联合选择完整配置。

### 方法 / 贡献  
- 方法：设计三类独立探针（标签顺序、示例顺序、示例放置位置），在10个商用/开源LLM上测量位置偏差。  
- 贡献：首次系统揭示序数分类中位置偏差的普遍性、因子影响、现有校正的局限性，并提出基于比较的listwise推理作为更具鲁棒性的替代范式。

### 实验或数据  
- 数据集：SST-5（5类）、Yelp-5（5类）、Twitter（3类）、Hate（2类）、Offensive（2类），每数据集固定200实例测试集。  
- 模型：Claude Haiku 4.5、Claude Sonnet 4.5、GPT-5.4等10个前沿LLM（通过OpenRouter访问）。  
- 实验阶段：Phase 0（确定性解码探测+随机解码噪声对比），Phase 1（8个因子消融），Phase 2（推理范式、去偏方法、联合配置）。  
- 评估指标：准确率、宏观F1、Spearman’s ρ、MAE、预测翻转率（PFR）及统计检验（Wilson置信区间、McNemar检验、Cochran’s Q检验）。

### 值得关注点  
- 所有模型的三种位置偏差在确定性解码下均显著（PFR 8.5%–32.0%），偏差远超随机噪声（PFR最高5.0%）。  
- 准确性和稳定性经常解耦：自然语言标签使标签顺序PFR升高59.5个百分点，准确率仅变化+1.3。  
- 降低分类尺度是唯一能同时提升性能与稳定性的因素。  
- 现有去偏方法（PriDe、Contextual Calibration）无效；listwise-compare将标签顺序PFR降低18.1个百分点，损失较小准确率，但迁移不均匀。

### 局限性  
- 实验仅限于英文数据集和少数任务领域（情感、仇恨/冒犯检测），结论在其他语言或任务类型（如生成长度评分）上可能不适用。  
- 仅研究基于上下文学习的序数分类，未覆盖微调或基于嵌入的分类范式。  
- 测试的多种去偏方法均未提供可靠修复，可能需要在系统层面设计更复杂的鲁棒性策略。  
- 联合配置的跨模型迁移仅用一个模型（Qwen3）初始选择，泛化性有限。  
- 未深入探究不同推理范式（pointwise/pairwise/listwise）的内在偏差交叉影响。

## 10. Unsure but Certain: Uncovering the Representation-Confidence Gap in Diffusion Language Models

- Source: arxiv
- arXiv ID: 2608.08791
- Relevance: 4.1

### Links

- Abstract: http://arxiv.org/abs/2608.08791v1
- PDF: https://arxiv.org/pdf/2608.08791v1
- DOI: https://doi.org/10.48550/arXiv.2608.08791

### Authors

Saurabh Yadav, Badri Narayana Patro, Vijay Srinivas Agneeswaran

### Abstract

Diffusion language models use broad context to create text, suggesting they might handle input noise better than standard models. Testing reveals this is only partially true. Internally, diffusion models detect text errors highly accurately. Externally, their reported certainty ignores this signal. As accuracy drops due to noise, confidence stays near its maximum and the ability to correctly rank answers degrades toward random chance. We call this mismatch the representation confidence gap. The visible concentration of high certainty scores is a misleading surface symptom. Standard math adjustments remove this concentration but fail to fix the underlying loss of ranking order. This ranking deficit favors standard models under noisy conditions and resists common remedies. Matching training recovers accuracy but not ranking, while score recalibration and input level error signals cannot reorder the final answers. However, the information needed to properly evaluate an answer survives in the hidden states. A lightweight extraction tool uses this signal to improve ranking. This approach is highly efficient because it leaves the base model completely frozen and requires zero additional text generation steps. We present this tool to prove the signal exists, while clearly noting its limits. Ultimately, certainty reliability is a more pressing limit than overall accuracy under noisy conditions.

### 中文一句话结论
扩散语言模型在内部能准确检测文本错误，但输出置信度忽略此信号而形成“表征‑置信度差距”，导致噪声下答案排序能力严重下降；然而隐藏状态中保留了正确性信息，通过轻量级读取工具（LCR）可在不更新模型的情况下恢复排序能力。

### English TL;DR
Diffusion language models accurately detect text errors internally but their reported certainty ignores this signal, creating a “representation‑confidence gap” that degrades answer ranking under noise; however, a lightweight, frozen‑model extraction tool (Latent Correctness Readout) can recover useful ranking signals from hidden states without additional generation steps.

### 中文详细总结
论文研究扩散语言模型（LLaDA‑8B、DREAM‑7B）面对输入噪声时的鲁棒性。实验发现：模型内部状态能高精度区分干净与噪声文本（AUROC 0.996‑0.997），但最终置信度几乎不变（噪声下准确率从0.560降至0.373，平均置信度仅从0.988降至0.982）。正确与错误答案的置信度差异极小（约0.0022），导致排序能力下降（AUROC从0.666降至0.575）。作者将此定义为“表征‑置信度差距”。常见补救（温度缩放、匹配训练）只调整标度或恢复准确率，却无法修复排序损失，因为输入级误差信号无法区分不同答案。论文提出潜在正确性读取器（LCR）：冻结模型，提取答案位置隐藏状态的平均值，训练简单逻辑回归分类器来估计答案是否正确。LCR无需任何模型更新或额外生成步数，在GSM8K和ARC‑Challenge等基准上能有效提升排序能力，但论文明确其局限，主要用于证明信号存在。

### 方法 / 贡献
- **定义并揭示表征‑置信度差距**：扩散模型内部准确检测错误，但输出置信度忽略该信号，导致噪声下准确率下降而置信度不变，排序能力退化。
- **分析常见修复失效的结构性原因**：温度缩放不改变排序顺序；匹配训练只恢复准确率不改变置信度问题；输入级误差信号是问题级属性，无法重新排序答案。
- **提出潜在正确性读取器（LCR）**：利用冻结模型的隐藏状态，通过平均值 + 逻辑回归来估计答案正确性。无需模型更新、无需额外生成步数，训练快（秒级），证明隐藏状态中有用信号确实存在。

### 实验或数据
- **模型**：LLaDA‑8B‑Instruct、DREAM‑7B‑Instruct，对照 LLaMA‑3‑8B、Qwen‑2.5‑7B。
- **任务**：GSM8K、ARC‑Challenge 及另 9 个基准。
- **噪声**：字符置换、键盘替换、字符插入、单词删除，严重程度 η ∈ {0.05, 0.10, 0.15, 0.30}。每个噪声提示有干净对照。
- **指标**：选择性 AUROC（主要）、AURC、ECE（15 bin）、准确率。
- **协议**：200 样本用于训练/校准，400 样本用于测试；LCR 超参数通过五折交叉验证在校准集选择；所有实验在 2 块 RTX 4090 上完成。

### 值得关注点
- 扩散模型置信度高度集中在极高分值，这是误导性的表面症状，掩盖了排序能力的丧失。
- 隐藏状态中的正确性信号比最终置信度更可靠，即使模型在噪声下输出错误答案，信号仍可区分。
- LCR 完全冻结基础模型、不增加生成步数，在普通 CPU 上秒级完成训练，实用且能证实信号存在。

### 局限性
- 论文明确声明 LCR 主要用于证明信号存在，在实际部署中有明确限制，并非完整解决方案。
- 方法在特定模型（LLaDA、DREAM）和任务上验证，泛化性尚未充分探讨。
- 输入级误差信号不能改进排序，说明答案特定信号至关重要；LCR 依赖中间层选择，可能对模型结构敏感。
- 噪声条件下，置信度可靠性问题比准确率更根本，目前仍未完全解决。

## Processing Notes

- Duplicate papers skipped: 0