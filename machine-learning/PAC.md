[TOC]

# PAC学习框架

## 1.PAC学习模型

介绍定义以及一些符号

$\mathcal{X}:$所有可能的例子，也叫输入空间

$\mathcal{Y}:$所有可能的标签或目标值。本节所有的$\mathcal{Y}$都认为是$\mathcal{Y}=\{0, 1\}$，也就是二分类

$concept \ c:\mathcal{X}\to\mathcal{Y}$  $\mathcal{X}$到$\mathcal{Y}$的映射，我们可以假设$c$是$\mathcal{X}$的子集，其$\mathcal{Y}=1$。

$\mathcal{C}(concept \ class)：​$我们希望学习的概念集合

假设有一些样本固定但不知道分布，且是独立同分布的$\mathcal{D}​$，我们的学习问题就如下：

学习者考虑一组固定的可能的概念$\mathcal{H}$，称为一个**假设集(hypothesis set)**，$\mathcal{H}$通常和$C$是不一致的。这里有一些样本$\mathcal{S}=\{x_1,x_2,…x_m\}$根据$\mathcal{D}$以及标签$(c(x_1),…,c(x_m))$绘制独立同分布。

通过$\mathcal{S}$来选择一个假设$h_S\in\mathcal{H}$，其相对于$concept \ c$有一个小的泛化误差($generalization error$)。

假设$h\in \mathcal{H}$的泛化误差，也被称为真实误差($true \ error$)或就叫$h$的$error$，标记为$R(h)$，定义如下：

**定义1.1 泛化误差$Generalization\ error$**

给定假设$h \in \mathcal{H}$，一个目标概念$target \ concept \ c \in \mathcal{C}$和一个基础分布$\mathcal{D}$，泛化误差被定义为:

$$
R(h)=\mathop{Pr}_{x\sim\mathcal{D}}[h(x)\neq c(x)]=\mathop{E}_{x\sim\mathcal{D}}[1_{h(x)\neq c(x)}]\tag{1.1}
$$

由于分布$\mathcal{D}$和目标概念($concept \ c$)是未知的，因此学习者无法直接获得假设的泛化误差，但是学习者可以一个假设在标签样本$\mathcal(S)$上的经验误差($emprical \ error$)。

**定义1.2经验误差$Empirical \ error$**

给定假设$h \in \mathcal{H}$，一个目标概念$target \ concept \ c\in \mathcal{C}$和一个样本$\mathcal{S}=(x_1,…,x_m)$，经验误差被定义为：

$$
\hat{R}(h)=\frac{1}{m}\sum_{i=1}^{m}1_{h(x_i)\neq c(x_i)} \tag{1.2}
$$

因此，$h\in\mathcal{H}​$的经验误差是样本$\mathcal{S}​$的平均误差，而泛化误差是基于分布$\mathcal{D}​$的期望误差。

$$
E[\hat{R}(h)]=R(h) \tag{1.3}
$$

$$
\mathop{E}_{S\sim D^m}[\hat{R}(H)]=\frac{1}{m}\sum_{i=1}^{m}\mathop{E}_{S\sim D^m}[1_{h(x_i)\neq c(x_i)}]=\frac{1}{m}\sum_{i=1}^{m}\mathop{E}_{S\sim D^m}[1_{h(x)\neq c(x)}]
$$

**定义1.3 PAC学习**

如果存在算法$\mathcal{A}$和多项式函数$poly(.,.,.,.)$，对于$\forall \epsilon > 0$和$\forall \delta>0$对于所有$\mathcal{X}$上的概率分布$\mathcal{D}$和任意目标概念$c\in \mathcal{C}$，当样本量$m\ge poly(\frac{1}{\epsilon},\frac{1}{\delta},n,size(c))$满足下列条件我们称为可PAC学习的。
$$
\mathop{Pr}_{S\sim D^m}[R(h_S)\leq\epsilon]>1-\delta \tag{1.4}
$$
如果$\mathcal{A}$运行时间复杂度小于$poly(\frac{1}{\epsilon},\frac{1}{\delta},n,size(c))$，$\mathcal{C}$被称为有效的可学习。



## 2 对有限假设集的保证——假设一致性



















## 3 对有限假设集的保证——假设不一致性

本节为有限集的假设不一致性提供了学习的保证

**Hoeffding‘s Inequality**：假设$X_1,X_2,…X_m​$是独立同分布的随机变量，令$\bar{X}=\frac{1}{m}\sum_{i=1}^mX_i​$，假设$E(\bar{X})=\mu​$，且有$P[a\leq X_i\leq b]=1​$对所有$i​$成立。那么对$\forall \epsilon>0​$，有下列不等式存在：
$$
P(|\frac{1}{m}\sum_{i=1}^{m}X_i-\mu|\ge\epsilon)\leq2e^{\frac{-2m\epsilon^2}{(b-a)^2}}\tag{3.1}
$$


证明过程：先证明$Hoeffding's \ lemma​$，再根据$Markov​$不等式。



**Hoeffding's lemma**：

假设$X$是一个随机变量，取值于$[a,b]$，且$E(X)=0$，那么对于任意的$\lambda>0​$有
$$
E(e^{\lambda X})\leq e^{\frac{\lambda^2(b-a)^2}{8}}\tag{3.2}
$$
证明**Hoeffding's lemma**:

$f(e^{\lambda x})​$是一个凸函数，所以对任意的$\alpha=\frac{b-x}{b-a}​$有$f(x)\leq \alpha f(a)​$，证明如下：

$y-f(a)=\frac{f(b)-f(a)}{b-a}(x-a)​$，所以有如下不等式：
$$
f(x)\leq f(a)+\frac{f(b)-f(a)}{b-a}(x-a)\tag{3.2.1}
$$
将$\alpha=\frac{b-x}{b-a}，f(x)=e^{\lambda x}​$带入：
$$
e^{\lambda x}\leq f(a)+\frac{f(b)-f(a)}{b-a}(x-a),\forall x\in[a,b]
$$
再把$x$看成随机变量$X​$，同时取期望：
$$
E(e^{\lambda X})\leq\frac{b-E(X)}{b-a}e^{\lambda a}-\frac{E(X)-a}{b-a}e^{\lambda b}
$$
因为$E(X)=0$，所以：
$$
E(e^{\lambda x})\leq\frac{b}{b-a}e^{\lambda a}-\frac{a}{b-a}e^{\lambda b} \tag{3.2.2}
$$
做变量代换，令$h=\lambda (b-a), p=\frac{-a}{b-a}​$，构造函数$L(h)=-hp+ln(1-p+pe^h)​$

$$
\begin{aligned}
e^{L(h)}&=e^{-hp+ln(1-p+pe^h)}\\
&=(1-p+pe^h)e^{-hp} \\
&=\frac{b}{b-a}e^{\lambda a}-\frac{a}{b-a}e^{\lambda b}
\end{aligned} \tag{3.2.3}
$$

根据 公式3.2.2 公式3.2.3所以$E(e^{\lambda x})\leq e^{L(h)}$，若证明$E(e^{\lambda x})\leq e^{L(h)}\leq e^{\frac{\lambda^2(b-a)^2}{8}}$即可。

证明$L(h)\leq e^{\frac{\lambda^2(b-a)^2}{8}}=\frac{h^2}{8}​$，令
$$
g(h)=L(h)-\frac{h^2}{8}=-hp+ln(1-p+pe^h)-\frac{h^2}{8},(h>0)
$$
$g(0)=0​$,$g'(h)=-p+\frac{pe^h}{1-p+pe^h}-\frac{h}{4}​$

$g'(0)=0, g''(h)=\frac{(1-p)pe^h}{(1-p+pe^h)}-\frac{1}{4}​$

设$m=1-p,n=pe^h$，则
$$
g''(h)=\frac{mn}{(m+n)^2}-\frac{1}{4}=\frac{1}{\frac{n}{m}+\frac{m}{n}+2}-\frac{1}{4}\leq 0
$$

$$
g''(h)\leq0\to(g'(h)\downarrow,g'(0)=0)\to(g(h)\downarrow,g(0)=0)
$$

所以$g(h)\leq 0​$，所以有$L(h)\leq\frac{h^2}{8}=\frac{\lambda^2(b-a)^2}{8}​$

故Hoeffding's lemma成立。



马尔科夫不等式：

$$
Pr(X>a)<\frac{E(X)}{a}
$$

证明:

$$
\begin{aligned}
E(X)&=\int_0^{\infty}xp(x)dx\\
&\ge\int_a^{\infty}xp(x)dx\\
&\ge a\int_a^{\infty} p(x)dx\\
&=a*Pr(x>a)\\
故：\\&Pr(x>a)<\frac{E(x)}{a}
\end{aligned}
$$

**证明Hoeffding‘s Inequality：**

设$X_i=Z_i-E(Z_i),\bar{X}=\frac{1}{m}\sum_{i=1}^{m}X_i$，根据指数函数和Morkov不等式，对于$\forall \lambda>0,\epsilon>0$
$$
\begin{aligned}
&P(|\frac{1}{m}\sum_{i=1}^{m}Z_i-E(Z)|\ge\epsilon)\leq2e^{\frac{-2m\epsilon^2}{(b-a)^2}}\\
&P(\bar{X}\ge\epsilon)=P(e^{\lambda\bar{X}}\ge e^{\lambda\epsilon})\leq\frac{E(e^{\lambda\bar{X}})}{e^{\lambda\epsilon}}
\end{aligned}\tag{1}
$$

$$
E(e^{\lambda\bar{X}})=E(e^{\frac{\lambda}{m}\sum_{i=1}^{m}X_i})=\prod_{i=1}^{m}E(e^{\frac{\lambda}{m}X_i})\tag{2}
$$

根据Hoeffding's lemma，
$$
E(e^{\lambda X})\leq e^{\frac{\lambda^2(b-a)^2}{8}} \\
E(e^{\frac{\lambda}{m}X_i})\leq e^{\frac{\lambda^2(b-a)^2}{8m}}\tag{3}
$$
所以根据公式(1)(2)(3)：
$$
P(\bar{X}\ge\epsilon)\leq\frac{\prod_{i=1}^{m}E(e^{\frac{\lambda}{m}X_i})}{e^{\lambda\epsilon}}\leq e^{-\lambda \epsilon + \frac{\lambda^2(b-a)^2}{8m}}
$$
令$\lambda=\frac{4m\epsilon}{(b-a)^2}$，可得
$$
P(\bar{X}\ge\epsilon)\leq e^{\frac{-2m\epsilon^2}{(b-a)^2}}
$$


同理：
$$
P(\bar{X}\leq-\epsilon)\leq e^{\frac{-2m\epsilon^2}{(b-a)^2}}
$$
所以:
$$
P(|\frac{1}{m}\sum_{i=1}^{m}Z_i-\mu|\ge\epsilon)\leq 2 e^{\frac{-2m\epsilon^2}{(b-a)^2}}
$$


因为书上的是二项分布，所以
$$
\mathop{Pr}_{S\sim D^m}[|\hat{R}(h)-R(h)|\ge \epsilon]\leq 2e^{-2m\epsilon^2}
$$
令$\delta=2e^{-2m\epsilon^2}​$,下列式子至少有$1-\delta​$的概率成立：
$$
R(h)\leq \hat{R}(h)+\sqrt{\frac{log\frac{2}{\delta}}{2m}}
$$

**证明：**因为$\delta=2e^{-2m\epsilon^2}$，所以$\epsilon =\sqrt{\frac{log\frac{2}{\delta}}{2m}}$

故：
$$
\begin{aligned}
\mathop{Pr}_{S\sim D^m}[R(h)-\hat{R}(h)\leq\sqrt\frac{log\frac{2}{\delta}}{2m}]&\ge\mathop{Pr}_{S\sim D^m}[\hat{R}(h)-R(h)\leq\sqrt\frac{log\frac{2}{\delta}}{2m}]\\
&\ge 1-\delta
\end{aligned}
$$


#### Learning bound 有限H，不一致情况

$$
\forall h\in \mathcal{H},R(h)\leq\hat{R}(h)+\sqrt{\frac{log|H|+log\frac{2}{\delta}}{2m}}
$$



证明：
$$
\begin{aligned}
&P[\exists h\in \mathop{H}|\hat{R}(h)-R(h)>\epsilon]\\
=&Pr[(|\hat{R}(h_1)-R(h_1)|>\epsilon)\lor(|\hat{R}(h_2)-R(h_2)|>\epsilon)\lor ... \lor(|\hat{R}(h_1)-R(h_1)|>\epsilon)]\\
\leq&\sum_{h\in\mathop{H}}Pr[(|\hat{R}(h)-R(h)|>\epsilon)]\\
\leq&2|\mathop{H}|e^{-2m\epsilon^2}
\end{aligned}
$$
令$\delta = 2|\mathop{H}|e^{-2m\epsilon^2}$，也就是$\epsilon=\sqrt{\frac{log|H|+log\frac{2}{\delta}}{2m}}$，带入即可得：
$$
\forall h\in \mathcal{H},R(h)\leq\hat{R}(h)+\sqrt{\frac{log|H|+log\frac{2}{\delta}}{2m}}
$$

## 4 概括

本节，将考虑几个与学习场景相关的重要问题。
