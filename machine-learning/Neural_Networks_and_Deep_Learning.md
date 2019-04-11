# Neural Networks and Deep Learning 习题解答

## 感知机

* sigmoid神经元模拟感知机（第一部分）  

> 对一个由感知机组成的神经网络，假设将其中所有的权值和偏移都乘上一个正常数$c\gt0$,证明网络的行为并不会发生改变。  

$$
output
\begin{cases}
0, &if\ w·x+b \le 0 \\  
1, &if\ w·x+b \gt 0
\end{cases}
$$

两边同时乘c  

$$
output
\begin{cases}
0, &if\ cw\cdot x+cb \le 0 \\  
1, &if\ cw\cdot x+cb \gt 0
\end{cases}
$$

* sigmoid神经元模拟感知机（第二部分)  

>假设与上述问题相同的初始条件——由感知机构成的神经网络。假设感知机的所有输入都已经被选定。我们并不需要实际的值，只需要保证输入固定。假定对网络中任意感知机的输入$x$都满足$w\cdot x  +b \ne 0$。现在将网络中所有的感知机都替换为sigmoid神经元，然后将所有的权值和偏移都乘上一个正常数$c\gt0$。证明在极限情况即下$c\to \infty$，这个由sigmoid神经元构成的网络与感知机构成的网络行为相同。同时想想当$w\cdot x +b = 0$时为何不是如此？

对于$sigmod()$函数来说$w\cdot x + b$乘上c不影响$w\cdot x + b\le 0$和$w\cdot x + b\gt 0$的结果。因此对于$\sigma (w\cdot x + b)\le 0$和$\sigma (w\cdot x + b)\gt 0$的结果没有影响。  
当$w\cdot x +b = 0$时，$\sigma(w\cdot x +b)=0.5$无法判断结果，所以无法分类。


