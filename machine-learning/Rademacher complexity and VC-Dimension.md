[TOC]

# Rademacher complexity and VC-Dimension

## 1 拉德马赫复杂度 Rademacher Complexity

思想：通过去衡量一个假设对随机噪声的拟合程度好坏来评估这个函数族的复杂度。

### 1.1 Empirical Rademacher Complexity

定义**Empirical Rademacher Complexity** 令G为一个从Z到$[a,b]$的映射函数集合，$S=(z_1,z_2,...,z_m)$为大小为$m$的固定样本，其中$z_i\in Z$。那么相对于样本S，函数族G的Empirical Rademacher Complexity定义为：
$$
\widehat{\mathfrak{R}}_{S}(\mathrm{S})=\underset{\boldsymbol{\sigma}}{E}\left[\sup _{g \in \mathcal{G}} \frac{1}{m} \sum_{i=1}^{m} \sigma_{i} g\left(z_{i}\right)\right]\tag{1}
$$
其中
$\boldsymbol{\sigma}=\left(\sigma_{1}, \ldots, \sigma_{m}\right)^{\top}$，$\sigma_i$是取值$\{+1, -1\}$的独立随机变量，称为Rademacher变量。
注：

>1. $S=\left(z_{1}, z_{2}, \ldots, z_{m}\right)=\left(\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right), \ldots,\left(x_{m}, y_{m}\right)\right)$
>2. $g\left(z_{i}\right)$表示用于之对应的假设 h 来预测$y_i$所产生的错误。
>3. Rademacher变量是个取$\{-1,+1\}​$两个值的均匀随机变量，上述的期望就是基于这个均匀随机变量的分布来求的。
>4. 上述式子可改写成:
>
> $$
> \widehat{\mathfrak{R}}_{S}(G)=E\left[\sup _{\sigma} \frac{\sigma g_{s}}{m}\right]
> $$
>
>5. 越复杂的函数族G可以产生更多不同的$g_s$，因此平均的说能更好的拟合随机噪声

### 1.2 Rademacher Complexity

定义**Rademacher Complexity**  令D为产生样本的分布。对任意的整数$m>1$，G的Rademacher Complexity是Empirical Rademacher Complexity的期望，其中的期望是基于样本根据分布采样而来的:
$$
\mathfrak{R}_{m}(G)=\underset{S \sim D^{m}}{E}\left[\widehat{\mathfrak{R}}_{S}(G)\right]
$$

### 1.3 证明

**定理 1.1** 令G为从Z到$[0,1]$的映射函数族。那么对任意的$\delta>0$，至少以概率$1-\delta$，以下的不等式对所有的$g\in G$都成立：
$$
\begin{array}{l}{E[g(z)] \leq \frac{1}{m} \sum_{i=1}^{m} g\left(z_{i}\right)+2 \Re_{m}(G)+\sqrt{\frac{\log \frac{1}{\delta}}{2 m}}}\\
{E[g(z)] \leq \frac{1}{m} \sum_{i=1}^{m} g\left(z_{i}\right)+2 \widehat{\mathfrak{R}}_{S}(G)+3 \sqrt{\frac{\log \frac{2}{\delta}}{2 m}}}\end{array}
$$
先要证明这个：
>**McDiarmid不等式**：令$(x_1,x_2,…,x_m)\in \mathcal{X}^m$为独立随机变量的集合，假设存在$c_1,…,c_m>0$，使得$f:\mathcal{X}\to R$满足以下条件：
$$
\left|f\left(x_{1}, \ldots, x_{i}, \ldots, x_{m}\right)-f\left(x_{1}, \ldots, x_{i}^{\prime}, \ldots, x_{m}\right)\right| \leq c_{i}
$$
对所有$i\in [1,m]$以及任意的点$x_1,…,x_m,x_{i}^{'}\in \mathcal{X}$都成立。令$f(x_1,…,x_m)$，那么对所有的$\epsilon>0$，下列不等式成立：
$$
\begin{array}{c}{\operatorname{Pr}[f(S)-E[f(S)] \geq \epsilon] \leq \exp \left(\frac{-2 \epsilon^{2}}{\sum_{i=1}^{m} c_{i}^{2}}\right)} \\ {\operatorname{Pr}[f(S)-E[f(S)] \leq-\epsilon] \leq \exp \left(\frac{-2 \epsilon^{2}}{\sum_{i=1}^{m} c_{i}^{2}}\right)}\end{array}
$$

Proof:

>1. 对任意样本$S=\left(z_{1}, \dots, z_{m}\right)$和任意$g\in G$，用$\widehat{E}_{S}[g]$表示g在任意样本S下的empirical average：
>
>   $$
>   \widehat{E}_{S}[g]=\frac{1}{m} \sum_{i=1}^{m} g\left(z_{i}\right)​
>   $$
>
>2. 我们在样本集合上定义一个函数$\Phi:\mathcal{X}\to\mathbb{R}$，记为：
>
>   $$
>   \Phi(S)=\sup _{g \in G}\left(E[g]-\widehat{E}_{S}[g]\right)
>   $$
>
>3. 令$S,S^{'}$为两个大小为m的样本，这两个样本中只有一个点不同，例如$S=\left(z_{1}, \dots, z_{m-1}, z_{m}\right), S^{\prime}=\left(z_{1}, z_{2}, \dots, z_{m-1}, z_{m}^{\prime}\right)​$
>
>4. 根据最大值的差一定不超过差的最大值，可得:
>   $$
>   \begin{aligned} \Phi\left(S^{\prime}\right)-\Phi(S) &=\sup _{g \in G}\left(E[g]-\widehat{E}_{S^{\prime}}[g]\right)-\sup _{g \in G}\left(E[g]-\widehat{E}_{S}[g]\right) \\ & \leq \sup _{g \in G}\left(E[g]-\widehat{E}_{S^{\prime}}[g]-E[g]+\widehat{E}_{S}[g]\right) \\ &=\sup _{g \in G}\left(\widehat{E}_{S}[g]-\widehat{E}_{S^{\prime}}[g]\right) \\ &=\sup _{g \in G} \frac{g\left(z_{m}\right)-g\left(z_{m}^{\prime}\right)}{m} \\ & \leq \frac{1}{m} \end{aligned}
>   $$
>
>
>   同理，我们也可以得到Φ(S)−Φ(S′)≤1mΦ(S)−Φ(S′)≤1m, 因此
>   $$
>   \left|\Phi(S)-\Phi\left(S^{\prime}\right)\right| \leq \frac{1}{m}
>   $$
>
>
>5. 应用McDiarmid第一个不等式，有:
>   $$
>   \operatorname{Pr}[\Phi(S)-E[\Phi(S)] \geq \epsilon] \leq \exp \left(\frac{-2 \epsilon^{2}}{1 / m}\right)
>   $$
>   令$\delta=\exp \left(-2 m \epsilon^{2}\right) \Rightarrow \epsilon=\sqrt{\frac{\log \frac{1}{\delta}}{2 m}}$，即以下不等式至少以$1- \delta$概率成立：
>   $$
>   \Phi(S) \geq E[\Phi(S)]+\sqrt{\frac{\log \frac{1}{\delta}}{2 m}}
>   $$
>
>6. 求$E[\Phi(S)]​$的上界。
>   $$
>   \begin{aligned} 
>   E[\Phi(S)] &=E\left[\sup _{g \in G}\left(E[g]-\widehat{E}_{S}(g)\right)\right] \\ &=E\left[\sup _{g \in G}\left[\widehat{E}_{S^{\prime}}(g)-\widehat{E}_{S}(g)\right]\right] \\
>   &\leq E_{S, S^{\prime}}\left[\sup \widehat{E}_{S^{\prime}}[g]-\widehat{E}_{S}(g)\right] \\ 
>   &=E_{S, S^{\prime}}\left[\sup _{g \in G} \frac{1}{m} \sum_{i=1}^{m}\left(g\left(z_{i}^{\prime}\right)-g\left(z_{i}\right)\right)\right]\\
>   &=\underset{\sigma, S, S^{\prime}}{E}\left[\sup _{g \in G} \frac{1}{m} \sum_{i=1}^{m} \sigma_{i}\left(g\left(z_{i}^{\prime}\right)-g\left(z_{i}\right)\right)\right]\\
>   &=\leq \underset{\sigma, S^{\prime}}{E}\left[\sup _{g \in G} \frac{1}{m} \sum_{i=1}^{m} \sigma_{i} g\left(z_{i}^{\prime}\right)\right]+\underset{\sigma, S}{E}\left[\sup _{g \in G} \frac{1}{m} \sum_{i=1}^{m}-\sigma_{i} g\left(z_{i}\right)\right]\\
>   &=2 \underset{\sigma, S}{E} \left[\underset{g \in G}{\sup } \frac{1}{m} \sum_{i=1}^{m} \sigma_{i} g\left(z_{i}\right)\right]\\
>   &=2\Re_{m}(G)
>   \end{aligned}
>   $$
>
>7. 所以：
> $$
> E[g]-\widehat{E}_{S}[g] \leq \Phi(S) \leq E[\Phi(S)]+\sqrt{\frac{\log \frac{1}{\delta}}{2 m}} \leq 2 \mathfrak{R}_{m}(G)+\sqrt{\frac{\log \frac{1}{\delta}}{2 m}}
> $$
> $$
> E[g] \leq \widehat{E}_{S}[g]+2 \mathfrak{R}_{m}(G)+\sqrt{\frac{\log \frac{1}{\delta}}{2 m}} =\frac{1}{m} \sum_{i=1}^{m} g\left(z_{i}\right)+2 \mathfrak{R}_{m}(G)+\sqrt{\frac{\log \frac{1}{\delta}}{2 m}}
> $$
>8. 证明第二个不等式:
根据定义2.1，将样本S 改变一点，则$\hat{\mathfrak{R}}_{S}(G)$将至多改变$\frac{1}{m}$, 且$E[\hat{\mathfrak{R}}_{S}(G)]=\mathfrak{R}_{m}(G)$。将$\hat{\mathfrak{R}}_{S}(G)$看作McDiarmid不等式中的$f(s)$，应用McDiarmid不等式中的第二个不等式有:
$$
\operatorname{Pr}\left[\widehat{\mathfrak{R}}_{S}(G)-\mathfrak{R}_{m}(G) \leq-\epsilon\right] \leq \exp \left(-2 \epsilon^{2} m\right)
$$
令：$\frac{\delta}{2}=\exp \left(-2 \epsilon^{2} m\right) \Rightarrow \epsilon=\sqrt{\frac{\log \frac{1}{\delta}}{2 m}}$。所以至多以$\frac{\delta}{2}$的概率$\mathfrak{R}_{m}(G)>\widehat{\mathfrak{R}}_{S}(G)+\sqrt{\frac{\log \frac{1}{\delta}}{2 m}}$成立。另外，把第五步的$\delta$换成$\frac{\delta}{2}$,得到：
$$
\begin{aligned}
\Phi(S) & \leq E[\Phi(S)]+\sqrt{\frac{\log \frac{2}{\delta}}{2 m}} \\
& \leq 2 \mathfrak{R}_{m}(G)+\sqrt{\frac{\log \frac{2}{\delta}}{2 m}} \\
& \leq 2 \widehat{\mathfrak{R}}_{S}(G)+3 \sqrt{\frac{\log \frac{2}{\delta}}{2 m}}
\end{aligned}
$$
$
\Longrightarrow
$
$$
E[g(z)] \leq \frac{1}{m} \sum_{i=1}^{m} g\left(z_{i}\right)+2 \widehat{\Re}_{S}(G)+3 \sqrt{\frac{\log \frac{2}{\delta}}{2 m}}
$$

把上面的结果用到0-1损失函数，得到以下引理。
**引理 1.1**
&nbsp;&nbsp;&nbsp;&nbsp; 令H为取值为{−1,+1}的函数族，令G为与H相对应的且损失函数为0-1损失的函数族:$G=\{(x, y) \rightarrow \mathbb{l}(h(x) \neq y) : h \in H\}$，对于任意样本$S=\left(\left(x_{1}, y_{1}\right), \ldots,\left(x_{m}, y_{m}\right)\right)$，以下等式成立
$$
\widehat{\mathfrak{R}}_{S}(G)=\frac{1}{2} \widehat{\mathfrak{R}}_{S_{\mathcal{X}}}(H)
$$
proof:
> $$
\begin{aligned}
\widehat{\mathfrak{R}}_{S}(G) &=E\left[\sup _{h \in H} \frac{1}{m} \sum_{i=1}^{m} \sigma_{i} \|\left(h\left(x_{i}\right) \neq y_{i}\right)\right]\\
&=E\left[\sup _{h \in H} \frac{1}{m} \sum_{i=1}^{m} \sigma_{i} \frac{1-y_{i} h\left(x_{i}\right)}{2}\right] \\
&=\frac{1}{2} E\left[\sup _{h \in H} \frac{1}{m} \sum_{i=1}^{m}\left(\sigma_{i}-\sigma_{i} y_{i} h\left(x_{i}\right)\right)\right]\\
&=\frac{1}{2} E\left[\frac{1}{m} \sum_{i=1}^{m} \sigma_{i}+\sup _{h \in H}-\sigma_{i} y_{i} h\left(x_{i}\right)\right] \\
&=\frac{1}{2} E\left[\frac{1}{m} \sup _{h \in H}-\sigma_{i} y_{i} h\left(x_{i}\right)\right]\\
&=\frac{1}{2} E\left[\sup _{h \in H} \frac{1}{m} \sum_{i=1}^{m} \sigma_{i} h\left(x_{i}\right)\right]\\
&=\frac{1}{2} \widehat{\mathfrak{R}}_{S_{\mathcal{X}}}(H)\\
\end{aligned}
$$
所以：
$$
\begin{array}{c}{\widehat{\mathcal{R}}(h)=\frac{1}{m} \sum_{i=1}^{m} 1_{\left(h\left(x_{i}\right) \neq y_{j}\right)}=\frac{1}{m} \sum_{i=1}^{m} g\left(x_{i}\right)=\widehat{E}_{S}[g]} \\ {\mathcal{R}(h)=E[\widehat{\mathcal{R}}(h)]=E\left[\widehat{E}_{S}[g]\right]=E[g(z)]}\end{array}
$$

$$
\begin{array}{l}{\mathcal{R}(h) \leq \widehat{\mathcal{R}}(h)+\mathfrak{R}_{m}(H)+\sqrt{\frac{\log \frac{1}{\delta}}{2 m}}} \\ {\mathcal{R}(h) \leq \widehat{\mathcal{R}}(h)+\widehat{\Re}_{S}(H)+3 \sqrt{\frac{\log \frac{2}{\delta}}{2 m}}}\end{array}
$$

$$
\widehat{\mathfrak{R}}_{S}(H)=\underset{\sigma}{E}\left[\sup _{h \in H} \frac{1}{m} \sum_{i=1}^{m}-\delta_{i} h\left(x_{i}\right)\right]=-\underset{\delta}{E}\left[\inf _{h\in H} \frac{1}{m} \sum_{i=1}^{m} \delta_{i} h\left(x_{i}\right)\right]
$$
## 2 增长函数 Growth Function

先讲**对分(dichotomy)**的概念：

>对于假设空间$\mathcal{H}={h:\mathcal{X}\to\{+1,-1\}}$，我们称
>$$
>h(X_1,X_2,...,X_N)=(h(X_1),h(X_2),...,h(X_N))\in\{+1,-1\}^N
>$$
>$\mathcal{H}(X_1,X_2,…,X_N)$表示假设空间$\mathcal{H}$在训练集$\mathcal{D}$上的所有对分。

显然，$\mathcal{H}(X_1,X_2,…,X_N)$的元素个数(即$|\mathcal{H}(X_1,X_2,…X_N)|$)是取决于数据集$\mathcal{D}$的，例如当N=3时候，且三个点不在一条直线上时，对分数为8，而在一条直线上对分数是6。为了去掉对于具体的数据集$\mathcal{D}$的依赖性，引入了**增长函数**:

>假设空间$\mathcal{H}$的增长函数$m_\mathcal{H}(N)$为
>$$
>m_{\mathcal{H}}(N)=\max _{X_{1}, X_{2}, \ldots, X_{N} \in \mathcal{X}}\left|\mathcal{H}\left(X_{1}, X_{2}, \ldots, X_{N}\right)\right|
>$$
>增长函数$m_{\mathcal{H}}(N)$表示假设空间$\mathcal{H}$对任意N个样本所能赋予标记的最大可能结果数，其上界为$2^N$。

## 3 VC Bound

### 3.1 打散(shatter)

先介绍打散，

> 当假设空间$\mathcal{H}$作用于大小为$N$的样本集$\mathcal{D}$时，产生对分数量等于$2^N$即$m_{\mathcal{H}}(N)=2^{N}$时，就称$\mathcal{D}$被$\mathcal{H}$打散了。



### 3.2 break point

> 对于假设空间$\mathcal{H}$的增长函数$m_{\mathcal{H}}(N)$，从$N=1$出发逐渐增大，当增大到$k$时，出现 $m_{\mathcal{H}}(N)<2N$的情形，则我们说$k$是该假设空间的break point。换句话说，对于任何大小为$N(N≥k)$的数据集，$\mathcal{H}$都没有办法打碎它。

>设break point存在且为 k 的假设空间的增长函数上界为 B(N,k)，则 B(N,k) 满足
>$$
>\mathbb{m}_{H}(N) \leq B(N, k) \leq \sum_{i=0}^{k-1} \left( \begin{array}{c}{N} \\ {i}\end{array}\right) \leq N^{k-1}
>$$
>

## 4 VC 维度

