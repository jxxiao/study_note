# 从Seq2Seq到Attention再到Transformer

本文将会梳理一遍我最近学习Transformer的总结，将会分为三个部分,第一部分RNN，第二部分Encoder-Decoder和最基础的attention（。第三部分Transformer，Transformer中有很多东西都可以更加细化，比如attention有哪些，normalization等等，这些将会单独再补。

## 1 Seq2Seq

Seq2Seq解决的主要是输入和输出不等长的问题，例如输入长度为n输出长度为m。

![](http://ww1.sinaimg.cn/large/006tNc79ly1g59lffdwa8j312o0s2ahj.jpg)

如上图所示，通过一个RNN得到红色部分令为c，之后将在Decoder每一个解码时输入c。
$$
y_{t}=f(h_{t-1},c)
$$

## 2 Attention

attention引入的原因就是当我们使用RNN去编码信息，我们只是将一串信息编码成c，在解码时对于每一个解码器来说c是一样的，这显然不符合逻辑，比如在上一节的途中，我们解码出“machine”时，重点应该是"机器"，所以我们就考虑对$c$进行处理。我们可以理解为有一个打分操作，在解码出"machine"的过程中，我们给"机"、"器"这两个编码打一个高分，"学"、"习"打一个低分，在解码出"laerning"的时候给"机"、"器"打一个低分，"学"、"习"打一个高分。

下图将展示我们如何打分：

![Scoer](http://ww3.sinaimg.cn/large/006tNc79ly1g59k7lrkdkj312s0t2tdp.jpg)

$z_0$可以看成网络的参数，理解为这句话的key就可以。我们把$z_0$和$h_1$通过一个match来给其打分，这个match可以直接点积两个向量，也可以是一个神经网络。把$z_0$和h依次打完分之后，我们可以得到$c_0$，$c_0$是decoder模块的输入，如下图所示。

![](http://ww4.sinaimg.cn/large/006tNc79ly1g59kq2v3ljj311s0r8q83.jpg)

之后再使用$z_1$和h进行打分，再得到$c_1$,如下图：

![](http://ww1.sinaimg.cn/large/006tNc79ly1g59kt4wwc5j310c0qsgr4.jpg) 

以此类推就能decoder完一句话。

总结一下，在Decoder我们将会用一下几个式子：
$$
\alpha_t=H^{T}Wz_t \\
\hat{\alpha}_t=sofmax(\alpha_t) \\
c^{t}=\sum\hat{\alpha}_t^ih^i \\
y_{out} = f(z^{t-1},c^{t-1})
$$
第一、二两个式子是打分，第三个式子是得到Decoder的输入，第四个式子是将Decoder的输入和上一层隐藏层值输入得到输出结果。

## 3 Transformer

### self-attention

$$
a^i = Wx^i
$$

$$
q^i=W^qa^i\\
k^i=W^ka^i\\
v^i=W^va^i
$$

Scaled Dot-Product Attention:
$$
\alpha_{1,i}=q^1 \cdot k^i/\sqrt{d}
$$

![Self-attention](http://ww1.sinaimg.cn/large/006tNc79ly1g4yo28i3npj313j0u0q9w.jpg)

之后对$(\alpha_{1,1},\alpha_{1,2},...,\alpha_{1,j})$做softmax得到$(\hat{\alpha}_{1,1},\hat{\alpha}_{1,2},...,\hat{\alpha}_{1,j})$。

$$
b^1=\sum_{i}\hat{\alpha}_{1,i}v^{i}
$$

![并行](http://ww3.sinaimg.cn/large/006tNc79ly1g4yovr539vj313y0u015m.jpg)

总结公式为:
$$
I = W x\\
Q=W^qI \\
K=W^kI \\
V=W^vI \\

A = K^TQ \\
\hat{A} = softmax(A) \\

O = V\hat{A}
$$
I为词向量，先分别得到$QKV$，再得到$\hat{A}=softmax(K^TQ)$，之后得到输出O。

### multi-head Self-attention

多头attention可以理解为我们用多个attention去关注不同层次的信息。比如一句话中出现it，多头attention就会关注多种it的可能性。在Transformer中为8头。

![multi-head Self-attention](http://ww3.sinaimg.cn/large/006tNc79ly1g4yoxz4h4rj31450u00yy.jpg)

### Positional Encoding

在上面的过程中，实际上我们并没有用位置信息，我打你和你打我的结果是一样的，所以，在这里加入位置信息。是通过直接把一个位置信息$e^i$，add到a上去（不是append）。

![Positional Encoding](http://ww1.sinaimg.cn/large/006tNc79ly1g4yozx2vwfj313z0u0q9n.jpg)

### Transformer

![Transformer](http://ww2.sinaimg.cn/large/006tNc79ly1g59lzzv5lhj312a0seagq.jpg)

上图左边为Encoder过程右边为Decoder过程，$N\times$代表这个过程才重复几次。

Eocoder过程：

1. 先输入Input Embedding，再把位置信息加入进去。
2. 经过一个Multi-Head Attention得到结果，再把未经过多头机制的数据和这个结果相加(add & Norm)，再做一个Layer Normalization(会单独开一篇出来讲Normalization)。
3. 通过一个前馈网络之后再add&Norm。

Decoder过程：

1. 输入Output Embedding，再加上位置信息。
2. Mask Multi-Head Attention： 只会attend到已经产生的句子。举个例子，再翻译（我爱你，I love you）的时候，当我们生成love的时候只会attention到I，因为you还没有产生。
3. Multi-Head Attention，attend到Encoder的输出，再Add&Norm。注意这里Attention的箭头，三个箭头两个来自Encoder，一个来自Masked Multi-Head Attention，这是说明K和V来自Encoder，Q来自Masked Multi-Head Attention。
4. 前馈神经网络之后再add&Norm。



仔细看上面的过程，实际上只有Encoder过程是并行的，Decoder还是一个一个弹出结果的。

假设现在有一个翻译任务，（我是个学生，I am a student）

$t_0$时刻：我是个学生 在Input Embedding后输入进去，Output Embedding输入<Bos>，运算结束输出machine。

$t_1$时刻：Output Embedding输入[<Bos> I]，得到结果am

$t_2$时刻：Output Embedding输入[<Bos> I am]，得到结果a

$t_3$时刻：Output Embedding输入[<Bos> I am a]，得到结果student

$t_4$时刻：Output Embedding输入[<Bos> I am a  student]，得到结果<EOS>。

本文基本参考台湾大学李宏毅老师的课程，推荐观看李宏毅老师讲解Seq2Seq和Transformer。

推荐阅读

[Transformer](https://jalammar.github.io/illustrated-transformer/),中文版本在这[中文版本](https://blog.csdn.net/qq_41664845/article/details/84969266)
