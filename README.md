# BIGDATA
the proof of work of the bigdata learning 

the first time edit at localtion 

#### #2019-03-22 14:16:32

the second time edit README.MD

#### 2019-03-24 10:41:01

今天从9：30过来，到现在已经差不多学习一个小时，HDFS

hadoop2.0 的主要思想是JobTracker两个主要的功能分分离成单独的组件，这两个功
能是资源管理和任务调度/监控

新的资源管理器全局管理所有应用程序计算资源的分配

ApplicationMaster负责相应的调度和协调

ResourceManager和每一台机器的阶段管理服务器能够管理用户在哪台机器上的进程
并能对计算进行组织。

NodeManager是每一台机器框架的代理，是执行应用程序的容器，监控应用程序的资
源使用情况（CPU 内存 磁盘 网络）并且向调度器汇报。

每一个应用的ApplicationMaster的职责有：向调度器索要适当的资源容器，运行任务，
跟踪应用程序的状态和监控他们的进程，处理任务的失败原因

客户端不变，其调用API及接口大部分保持兼容，这也是为了开发使用者透明化，
对原码不必做大的改变，但是原框架的JobTracker和TaskTracker不见了，取而代之的
是ResourceManager AppliactionMaster NodeManager三个部分。

ResourceManager是一个中心的服务，它做的事情是调度、启动每一个Job所属的
ApplicationMaster、另外监控ApplicationMaster的存在情况。Job里面所在的task的监
控，重启等内容不见了，这就是ApplicationMaster存在的原因。ResourceManager负
责作业与资源的调度，接收JobSubmitter提交的作业，按照作业的上下文(context)信
息，以及从NodeManager收集来的状态信息，启动调度过程，分配一个Container作
为Application Master

 *NodeManager 功能比较专一，就是负责Container状态的维护，并向RM保持心跳。

ApplicationMaster负责一个Job生命周期内的所有工作，类似老的框架中JobTracker,
但注意每一个Job(不是每一种)都有一个ApplicationMaster,他可以运行在ResourceManager
以外的机器上.

#### 2019年3月24日 22:00:33
看了9个小时的电视剧，19版的《倚天屠龙记》+ 《都挺好》
没有学习大数据，心情比较崩溃😫

#### 2019年3月25日 09:06:30
昨天学习发现一个问题，学习的进度太慢了，以前一直喜欢看视频学习，分析了下那些内容比较简单的
东西很好理解；但是现在学习的东西很多都是非常复杂的，不容易理解，需要常常去复习，这
个时候视频就显得很鸡肋，还是文档容易复习，而且现在要慢慢的适应文档的自学方式.现在给每天的任
务是早上早读的方式去读文档。