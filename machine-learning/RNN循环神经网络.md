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
2. 反向计算每个神经元的**误差项**$\delta_j$

#### 前向计算

$$
s_t = f(Ux_t + Ws_{t-1})
$$

#### 误差项计算

$$
net_t = Ux_t + Ws_{t-1} \\
s_{t-1} = f(net_{t-1})
$$

$$
\frac{\partial net_t}{\partial net_{t-1}} = \frac{\partial net_t}{\partial s_{t-1}}\frac{\partial s_{t-1}}{\partial net_{t-1}}
$$

