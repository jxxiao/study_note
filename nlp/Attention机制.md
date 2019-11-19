# Attention机制

本文主要从RNN，Seq2Seq再到Attention机制

## 1. 经典RNN结构(N->N)

经典的RNN输入长度为N，输出也为N，如下图：

![经典RNN](http://ww1.sinaimg.cn/large/006tNc79ly1g45sui9nrzj30go0d574u.jpg)


$$
h_1 = Wx_1+b \\
y_1 = softmax(Vx_1+c)
$$


## 2.N->1

输入长度为N，输出长度为1:

![N_1](http://ww3.sinaimg.cn/large/006tNc79ly1g45szlo4drj30go0csgm5.jpg)

## 3. 1->N

输入长度为1，输出长度为N:

![1->N](http://ww3.sinaimg.cn/large/006tNc79ly1g45t2gqcehj30go0d2dg7.jpg)

另一种：

![](http://ww4.sinaimg.cn/large/006tNc79ly1g45t3jwuyyj30go0efwf0.jpg)

## 4.Encoder-Decoder(N->M)

因为Seq2Seq不一定是等长的，所以提出了Encoder-Decoder模型。

先Encoder:

![Encoder](http://ww1.sinaimg.cn/large/006tNc79ly1g468q8qf9xj30go0avmxl.jpg)

再Decoder(下图有两种Decoder):

![](http://ww3.sinaimg.cn/large/006tNc79ly1g468rb4xx1j30go06pq35.jpg)



![](http://ww4.sinaimg.cn/large/006tNc79ly1g468rd7d7tj30go09874k.jpg)

## 5. Attention机制

先看一张图：

![](http://ww3.sinaimg.cn/large/006tNc79ly1g469dnfpihj30go0hi74w.jpg)

简单来说就是$c$中含有的信息不够多，$h_1,h_2,h_3$解码的都是同一个c，所以决定用$h_1,h_2,h_3$解码不同的$c$。听上去会有点拗口，用通俗的话来说，原来我们是先把文本编码成为一个拥有上下文信息的c，再去解码这个c。但是c如果太短就存不了很多信息，所以我们决定去生成多个c，解码的时候用哪个c呢？attention给了个参数叫$a$,看下图:

![](http://ww3.sinaimg.cn/large/006tNc79ly1g469020yjcj30go06iaaf.jpg)

再解码出"I"的时候，$h_1$比较重要，所以$a_{11}$就要大点，其它的就要小一点。剩下的问题就是**怎么求这$a$?**

