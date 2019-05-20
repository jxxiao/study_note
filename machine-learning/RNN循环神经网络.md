---
typora-root-url: ../../study_note
---

# RNN循环神经网络

## 基本循环神经网络

![RNN_1](/image/RNN_1.jpg)

x是一个向量，表示**输入层**的值

s是一个向量，表示**隐藏层**的值

U是输入层到隐藏层的**权重矩阵**

o是一个向量，表示**输出层**的值

V是隐藏层到输出层的权重矩阵。

W是**隐藏层**上一次的值作为这一次的输入的权重

![RNN_2](/image/RNN_2.jpg)


$$
o_t = g(Vs_t)\tag{1}
$$

$$
s_t = f(Ux_t + Ws_{t-1})\tag{2}
$$



## 双向循环神经网络

略

## 深度循环神经网络

略

## 循环神经网络的训练

### 循环神经网络的训练算法：BPTT

1. 前向计算每个神经元的输出值；
2. 反向计算每个神经元的**误差项**$\delta_j$，它是误差函数E对神经元j的加权输入$net_j$的偏导数；
3. 计算每个权重的梯度。

#### 前向计算

> 公式(2)
> $$
> s_t = f(Ux_t + Ws_{t-1})
> $$

假设输入的向量$x$的维度是m，输出向量$s$的维度是n，则矩阵U的维度为$n\times m$，矩阵W的维度是$n\times n$。展开成矩阵如下式子。

>$$
>\left[
>\begin{matrix}
>s_{1}^{t}\\
>s_{2}^{t}\\
>·\\
>·\\
>s_{n}^{t}\\
>\end{matrix}
>\right]
>=f(
>\left[
>\begin{matrix}
>u_{11}u_{12}···u_{1m}\\
>u_{21}u_{22}···u_{2m}\\
>·\\
>·\\
>u_{n1}u_{n2}···u_{nm}\\
>\end{matrix}
>\right]
>\left[
>\begin{matrix}
>x_1\\
>x_{2}\\
>·\\
>·\\
>x_{m}\\
>\end{matrix}
>\right]
>+
>\left[
>\begin{matrix}
>w_{11}w_{12}···w_{1n}\\
>w_{21}w_{22}···w_{2n}\\
>·\\
>·\\
>w_{n1}w_{n2}···w_{nn}\\
>\end{matrix}
>\right]
>\left[
>\begin{matrix}
>s_{1}^{t-1}\\
>s_{2}^{t-1}\\
>·\\
>·\\
>s_{n}^{t-1}\\
>\end{matrix}
>\right]
>)
>$$
>
>
>
>

#### 误差项计算

BTPP算法将第l层t时刻的**误差项$\delta_t^l$**值沿两个方向传播，一个是传到上层网络得到$\delta_t^{l-1}$，一个沿时间传到初始时刻$t_1$，得到$\delta_1^l$，这一部分只和W有关。
$$
net_t = Ux_t + Ws_{t-1} \\
s_{t-1} = f(net_{t-1})\\
$$

$$
\frac{\partial net_t}{\partial net_{t-1}} = \frac{\partial net_t}{\partial s_{t-1}}\frac{\partial s_{t-1}}{\partial net_{t-1}}
$$

对上式第一项求导，其结果为Jacobian矩阵(一眼就能看出来是W):

>$$
>\begin{align}
>\frac{\partial net_{t}}{\partial s_{t-1}}&=\left[
> \begin{matrix}
>   \frac{\partial net_1^t}{\partial s_1^{t-1}}&\frac{\partial net_1^{t}}{\partial s_2^{t-1}}&···&\frac{\partial net_1^{t}}{\partial s_n^{t-1}}\\
>   \frac{\partial net_2^t}{\partial s_1^{t-1}}&\frac{\partial net_2^{t}}{\partial s_2^{t-1}}&···&\frac{\partial net_2^{t}}{\partial s_n^{t-1}}\\
>   &·&&\\
>   &·&&\\
>   \frac{\partial net_n^t}{\partial s_1^{t-1}}&\frac{\partial net_n^{t}}{\partial s_2^{t-1}}&···&\frac{\partial net_n^{t}}{\partial s_n^{t-1}}\\
>  \end{matrix}
>  \right]\\
>  &=\left[
>  	\begin{matrix}
>  		w_{11}&w_{12}&···&w_{1n}\\
>  		w_{21}&w_{22}&···&w_{2n}\\
>  		&·&&\\
>  		&·&&\\
>  		w_{n1}&w_{n2}&···&w_{nn}
>  	\end{matrix}
>  	\right]\\
>  &=W
>\end{align}
>$$

同理，第二项也是Jacobian矩阵:

>$$
>\begin{align}
>\frac{\partial s_{t-1}}{\partial net_{t-1}}&=
>    \left[
>    	\begin{matrix}
>    		\frac{\partial s_1^{t-1}}{\partial net_{1}^{t-1}}&
>    		\frac{\partial s_1^{t-1}}{\partial net_{2}^{t-1}}&
>    		···&
>    		\frac{\partial s_1^{t-1}}{\partial net_{n}^{t-1}}\\
>    		\frac{\partial s_2^{t-1}}{\partial net_{1}^{t-1}}&
>    		\frac{\partial s_2^{t-1}}{\partial net_{2}^{t-1}}&
>    		···&
>    		\frac{\partial s_2^{t-1}}{\partial net_{n}^{t-1}}\\
>    		&·&&\\
>    		&·&&\\
>    		\frac{\partial s_n^{t-1}}{\partial net_{1}^{t-1}}&
>    		\frac{\partial s_n^{t-1}}{\partial net_{2}^{t-1}}&
>    		···&
>    		\frac{\partial s_n^{t-1}}{\partial net_{n}^{t-1}}\\
>    	\end{matrix}
>    \right]\\
>    &=
>    \left[
>    \begin{matrix}
>    f^{'}(net_{1}^{t-1})&0&···&0\\
>    0&f^{'}(net_{2}^{t-1})&···&0\\
>    &·&&\\
>    &·&&\\
>    0&0&···&f^{'}(net_{n}^{t-1})
>    \end{matrix}
>    \right]\\
>    &=diag[f^{'}(net_{n}^{t-1})]\\
>\end{align}
>$$
>
>其中，diag[a]表示根据向量a创建一个对角矩阵，即
>$$
>diag(a)=
>\left[
>\begin{matrix}
>a_1&0&···&0\\
>0&a_2&...&0\\
>&·&&\\
>&·&&\\
>0&0&···&a_n
>\end{matrix}
>\right]
>$$

将两项合在一起
$$
\begin{align}
\frac{\partial net_t}{\partial net_{t-1}} &= \frac{\partial net_t}{\partial s_{t-1}}\frac{\partial s_{t-1}}{\partial net_{t-1}}\\
&=Wdiag[f^{'}(net_{t-1})]\\
&=
\left[
\begin{matrix}
w_{11}f^{'}(net_1^{t-1})&w_{12}f^{'}(net_2^{t-1})&···&w_{1n}f^{'}(net_n^{t-1})\\
w_{21}f^{'}(net_1^{t-1})&w_{22}f^{'}(net_2^{t-1})&···&w_{2n}f^{'}(net_n^{t-1})\\
&·&&\\
&·&&\\
w_{n1}f^{'}(net_1^{t-1})&w_{n2}f^{'}(net_2^{t-1})&···&w_{nn}f^{'}(net_n^{t-1})\\
\end{matrix}
\right]
\end{align}
$$
上式描述了将$\delta$沿时间往前传递一个时刻的规律，有了这个规律我么就可以求任意时刻$k$的误差项$\delta_k$（$\delta_k^T=\frac{\partial E}{\partial net_k}$）：
$$
\begin{align}
\delta_k^T&=\frac{\partial E}{\partial net_k}\\
&=\frac{\partial E}{\partial net_t}\frac{\partial net_t}{\partial net_k}\\
&=\frac{\partial E}{\partial net_t}\frac{\partial net_t}{\partial net_{t-1}}\frac{\partial net_{t-1}}{\partial net_{t-2}}···\frac{\partial net_{k+1}}{\partial net_k}\\
&=Wdiag[f^{'}(net_{t-1})]Wdiag[f^{'}(net_{t-2})]···Wdiag[f^{'}(net_{k})]\delta_t^{l}\\
&=\delta_t^T\prod_{i=k}^{t-1}Wdiag[f^{'}(net_i)]
\end{align}
$$
所以**循环层**的**加权输入**$net^l$和上一层的**加权输入**$net^{l-1}$关系如下：
$$
net_t^l=Ua_t^{l-1}+Ws_{t-1}\\
a_t^{l-1}=f^{l-1}(net_t^{l-1})
$$

$$
\begin{align}
\frac{\partial net_t^l}{\partial net_t^{l-1}}&=
\end{align}
$$

