# ELMO GPT和Bert

[TOC]

## ELMO

ELMO的全称是Embedding from Language Models，论文为[Deep contextualized word representation](https://arxiv.org/abs/1802.05365)。

在之前Word2vec的方法Embedding中，无法表示出一词多义，使用一个Embedding去表示一个词是不恰当的，所以提出了ELMO，ELMO的思想是：先学会一个词的Word Embedding，这个时候虽然无法区分多义词，但是在实际使用Word Embedding时，因为词的上下文已经出现了，所以可以通过上下文动态调整Word Embedding。

ELMO分为两个阶段，第一阶段通过语言模型进行预训练；第二阶段是在进行下游任务时，从预训练网络中提取对应单词在各层的Word Embedding作为新的特征补充到下游任务。

ELMO的结构如下图，ELOM采用了双层双向LSTM。

![Elmo](http://ww1.sinaimg.cn/large/006tNc79gy1g5cks8516zj30n40aignf.jpg)

ELMO的第一阶段预训练，ELMO的第一阶段预训练的任务是根据词的上下文去推测词，左边的LSTM负责通过上文推测词，右边的LSTM负责通过下文推测词。这样的LSTM会得到三组向量，第一组是Word Embedding的向量$x$，第二组是LSTM第一层的向量$h_1$，第三组是LSTM第二层的向量$h_2$，$h_1$和$h_2$是由正向LSTM和反向LSTM的向量append起来，如下图所示。

![ELMO-1](http://ww3.sinaimg.cn/large/006tNc79gy1g5cjbn0hp2j31260stn69.jpg)

第二阶段下游任务，在我们进行下游任务的时候，第一阶段预训练的神经网络参数已经确定了，我们把句子输入到神经网络中，我们会得到之前的三组向量，将每一个向量设定一个权重值，之后相加得到$ELMO^{task}=w_0x+w_1h_1+w_2h_2$，如下图所示（下图缺了token的Embedding x），这个权重值是需要学习的来的。这样就能得到特定任务中的Word Embedding$[x;ELMO^{task}]$，右边的图告诉我们的是在进行不同任务时这个三个向量的权重比是不一样的，很明显在进行Coref（指代消解）和SQuAD（阅读理解）时很依赖LSTM第一层的向量。文章中还表示LSTM第一层更多的捕捉到的是语法信息，而LSTM第二层更多的捕捉到的是语义信息。最后，这一类的预训练方法被称为"Feature-based Pre-Training"。

![Elmo-2](http://ww2.sinaimg.cn/large/006tNc79gy1g5cla5b4dpj311s0s4wm7.jpg)

ELMO的具体过程可以见下图:

![ELMO](http://ww4.sinaimg.cn/large/006tNc79gy1g5d5ls55p8j30z80juacy.jpg)

### ELMO总结

使词在不同上下文中拥有不同的词向量

## GPT

全称Generative Pre-Training。 GPT的特点：

1. Pre-Traning
2. 单向Transformer(Deocder模块)
3. Fine-Tuning

![GPT-Transformer](http://ww3.sinaimg.cn/large/006tNc79ly1g5fglbqu2oj306q0ck74t.jpg)

如上图所示，GPT使用的是Transformer的Decoder模块，所以GPT只能利用上文信息，而无法利用下文信息。

### 预训练

GPT的结构如下图：

![GPT](http://ww1.sinaimg.cn/large/006tNc79ly1g5fh3idnjbj30bs0aq3zd.jpg)

每一个蓝色的Trm就是最上面的Transformer的结构，可以看出这是一个单向的Transformer结构。$E_1$输入的是<BOS>，$T_1$预测的是第一个词，$E_N$输入的是最后一个词。

我们的优化的最大似然函数为：
$$
L_1(\mathcal{U})= \sum_ilogP(u_i|u_{i-k},...,u_{i-1};\Theta)
$$
$\mathcal{U}=\{u_1,u_2,…,u_n\}$表示语料库，$k$是窗口大小，$\Theta$是神经网络参数。

Trm中的计算过程如下：
$$
\begin{aligned} h_{0} &=U W_{e}+W_{p} \\ h_{l} &=\text { transformer_block }\left(h_{l-1}\right) \forall i \in[1, n] \\ P(u) &=\operatorname{softmax}\left(h_{n} W_{e}^{T}\right) \end{aligned}
$$

### Fine-Tuning

这是训练的第二步，运用少量带label的数据对模型参数进行微调。也是我们进行下游任务的时候。

这里就是一个监督学习过程，根据不同下游任务需要调整输入数据结构。

![GPT-task](http://ww3.sinaimg.cn/large/006tNc79gy1g5jbvt1if0j30y40iw7a2.jpg)

## Bert

 Bert的全称是Bidirectional Encoder Representations from Transformers。从名字中可以看出是使用了Transformer中的Encoder模块，并且是双向Encoder。同时Bert是不需要label的，只需要收集一堆句子就可以训练，Bert提供了两种训练方式Masked LM和Next Sentence Prediction。

![Bert](http://ww4.sinaimg.cn/large/006tNc79gy1g5cg7i2b8cj311x0jz7b3.jpg)

上图就是Bert的结构，其中黄色Bert部分就是右侧Transformer的Encoder模块。

1. 不需要label
2. 每一个句子都会生产出一个embedding。

Bert预训练有两种方式，Masked LM和Next Sentence Prediction。

###Masked LM

会以15%的概率去掉一句话中的词成为MASK，然后通过Bert来预测该词（就是完形填空，可以理解成CBOW）。

![Maksed Lm](http://ww4.sinaimg.cn/large/006tNc79gy1g5cgeuqbwtj312c0sgq74.jpg)

如上图，根据上下文Bert会推出MASK的Embedding，之后将Embedding的内容丢进Linear Multi-class Classifier，去猜测MASK掉的词是哪一个。 



### Next Sentence Prediction

![](http://ww3.sinaimg.cn/large/006tNc79gy1g5njz1l2f5j31280satem.jpg)

先通过负采样，采样句子的样本，输入句子的第二个片段会以50%的概率从全部文本中选取，会以50%概率从第一个片段剩下的句子中提取。和word2vec中的负采样的原理一样，通过采样正例和负例来加速训练过程。就可以在sentence-level水平上做分类，判断下一个句子是不是上一个句子的下一句。分类是通过CLS位置输出的向量进行判断的。

### Task

在做具体任务的时候，BERT要结合到我们的具体任务中。GPT Bert和ELMo的不同在于，下游任务和Embedding是否分离，在ELMo中可以通过ELMo得到Embedding，再去用新的网络进行下游任务。而Bert和GPT只需要对输入稍微修改，就可以直接进行下游任务。

ERNIE是百度为中文设计的BERT模型，不同的地方只是在MASK的时候会MASK掉一个词，而不是一个字。

## GPT-2

GPT-2相对于GPT-1而言，有三个点：

1. 更大的模型，叠加了48和Block。
2. 更多的数据，使用了比GPT-1更大的数据。
3. fine-tuning阶段，不再做有监督的学习任务。

## 缺点

**ELMO**

使用双向LSTM，抽取特征能力不如Transformer。

双向LSTM直接拼接(append)特征向量，有点不合理。

**GPT**

单向语言模型，在处理类似阅读理解等一些任务时会有缺陷。

 