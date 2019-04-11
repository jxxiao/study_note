[TOC]

# pympi

在Python环境下使用**MPI**接口在集群上进行多进程并行计算。

**What is MPI？**

- MPI不是语言，是一个库，我们可以使用C、C++结合MPI提供的接口来将串行的程序进行并行化处理。
- 它是一种标准而不是特定的实现，具体的可以有很多不同的实现，例如MPICH、OpenMPI等。
- 它是一种消息传递编程模型，顾名思义，它就是专门服务于进程间通信的。

MPI的工作方式：同时启动一组进程，在同一个通信域中不同的进程都有不同的编号，利用MPI提供的接口来给不同编号的进程分配不同的任务和帮助进程相互交流最终完成同一个任务。这些进程都在这个通信域下。

## 1 Python中的并行

由于CPython中的GIL的存在，我们无法在CPython中使用多线程利用多核资源进行并行计算了，因此我们在Python中可以利用多进程的方式充分利用多核资源。多线程多进程最主要的差距在，多线程可以共享内存，而多进程是互相独立的，因此需要进程之间的通信。

Python中我们可以使用很多方式进行多进程编程，例如`os.fork()`来创建进程或者通过`multiprocessing`模块来更方便的创建进程和进程池等。

### 1.1 MPI与mpi4py

mpi4py是一个构建在MPI之上的Python库，主要使用Cython编写。mpi4py使得Python的数据结构可以方便的在多进程中传递。

mpi4py是一个很强大的库，它实现了很多MPI标准中的接口，包括点对点通信，组内集合通信、非阻塞通信、重复非阻塞通信、组间通信等，基本上我能想到用到的MPI接口mpi4py中都有相应的实现。不仅是Python对象，mpi4py对numpy也有很好的支持并且传递效率很高。同时它还提供了SWIG和F2PY的接口能够让我们将自己的Fortran或者C/C++程序在封装成Python后仍然能够使用mpi4py的对象和接口来进行并行处理。可见mpi4py的作者的功力的确是非常了得。

### 1.2 mpi4py

### MPI环境管理

mpi4py提供了相应的接口`Init()`和`Finalize()`来初始化和结束mpi环境。但是mpi4py通过在`__init__.py`中写入了初始化的操作，因此在我们`from mpi4py import MPI`的时候就已经自动初始化mpi环境。

`MPI_Finalize()`被注册到了Python的C接口`Py_AtExit()`，这样在Python进程结束时候就会自动调用`MPI_Finalize()`， 因此不再需要我们显式的去掉用`Finalize()`。

### 通信域(Communicator)

mpi4py直接提供了相应的通信域的Python类，其中`Comm`是通信域的基类，`Intracomm`和`Intercomm`是其派生类，这根MPI的C++实现中是相同的。

同时它也提供了两个预定义的通信域对象:

1. 包含所有进程的`COMM_WORLD`
2. 只包含调用进程本身的`COMM_SELF`

```
In [1]: from mpi4py import MPI
In [2]: MPI.COMM_SELF
Out[2]: <mpi4py.MPI.Intracomm at 0x7f2fa2fd59d0>
In [3]: MPI.COMM_WORLD
Out[3]: <mpi4py.MPI.Intracomm at 0x7f2fa2fd59f0>
```

通信域对象则提供了与通信域相关的接口，例如获取当前进程号`Get_rank()`、获取通信域内的进程数`Get_size()`、获取进程组`Get_group()`、对进程组进行集合运算、分割`Split()`合并等等。

```shell
In [4]: comm = MPI.COMM_WORLD                   
In [5]: comm.Get_rank()                         
Out[5]: 0                                       
In [6]: comm.Get_size()                         
Out[6]: 1                                       
In [7]: comm.Get_group()                        
Out[7]: <mpi4py.MPI.Group at 0x7f2fa40fec30>    
In [9]: comm.Split(0, 0)                        
Out[9]: <mpi4py.MPI.Intracomm at 0x7f2fa2fd5bd0>
```

## 2 点对点通信

mpi4py提供了点对点通信的接口使得多个进程间能够互相传递Python的内置对象（基于pickle序列化），同时也提供了直接的数组传递（numpy数组，接近C语言的效率）。

如果我们需要传递通用的Python对象，则需要使用通信域对象的方法中小写的接口，例如`send()`,`recv()`,`isend()`等。

MPI中的点到点通信有很多中，其中包括标准通信，缓存通信，同步通信和就绪通信，同时上面这些通信又有非阻塞的异步版本等等。这些在mpi4py中都有相应的Python版本的接口来让我们更灵活的处理进程间通信。这里我只用标准通信的阻塞和非阻塞版本来做个举例：

### 2.1 阻塞标准通信

这里我尝试使用mpi4py的接口在两个进程中传递Python list对象。

```python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = range(10)
    comm.send(data, dest=1, tag=11)
    print("process {} send {}...".format(rank, data))
else:
    data = comm.recv(source=0, tag=11)
    print("process {} recv {}...".format(rank, data))

```

执行效果：

```shell
mpiexec -np 2 python mpi_Blocking.py

process 0 send range(0, 10)...
process 1 recv range(0, 10)...
```

### 2.2 非阻塞标准通信

```python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = range(10)
    comm.isend(data, dest=1, tag=11)
    print("process {} immediate send {}...".format(rank, data))
else:
    data = comm.recv(source=0, tag=11)
    print("process {} recv {}...".format(rank, data))
    
```

执行结果：

```shell
mpiexec -np 2 python mpi_Non-blocking.py

process 0 immediate send [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]...
process 1 recv [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]...
```

### 支持Numpy数组

可以通过接口直接传递数据对象，

例子：

```python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = np.arange(10, dtype='i')
    comm.Send([data, MPI.INT], dest=1, tag=11)
    print("process {} Send buffer-like array {}...".format(rank, data))
else:
    data = np.empty(10, dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=11)
    print("process {} recv buffer-like array {}...".format(rank, data))
```



```
process 0 Send buffer-like array [0 1 2 3 4 5 6 7 8 9]...
process 1 recv buffer-like array [0 1 2 3 4 5 6 7 8 9]...
```

## 3 组通信

