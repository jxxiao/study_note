# 1 决策树

## 1.1 决策树模型和学习

### 1.1.1 决策树模型

对实例进行分类的树形结构。

由结点（node）和有向边（directed edge）组成

结点两种类型：

​	内部节点（internal node）：表示一个特征或属性

​	叶结点（leaf node）：表示一个类



## 1.2 特征选择

熵：表示随机变量不确定性的度量

X是一个取有限个值的离散随机变量，其概率分布为
$$
P(X=x_i)=p_i, i = 1,2,...n{}
$$
则随机变量X的熵定义为：
$$
H(X)=-\sum_{i=1}^{n}p_ilogp_i
$$

### 信息增益

特征A对训练数据集D的信息增益g(D,A)，定义为集合D的**经验熵H(D)**与特征A给定条件下D的经验**条件熵H(D|A)**之差，即
$$
g(D,A) = H(D)-H(D|A)
$$
id253696155129uks