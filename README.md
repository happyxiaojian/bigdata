# BIGDATA
**the proof of work of the bigdata learning **

#### 2019年3月27日 09:44:39

今天看的一句比较有感觉的话是：所谓的成熟，有一个标志是喜欢的依旧喜欢但可以不拥有，害怕的依然害怕但可以去面对。

大数据学习的进度报告：昨天跟张盼聊天聊得忘了时间，几乎没怎么推进。昨天开始看python相关的东西了。在学习的过程中发现又一个问题是，以前的预习的东西有的缺少实践的环节。现在的策略是直接看正式课的内容，理论先过一遍，不纠结，然后实践，最后反过来验证理论，理解。



#### 2019年3月26日 09:11:33

昨天通过 **PDF** 文档学习了**storm** 和 **zookeeper** , 学习的效果不尽人意，速度太慢，东西太多了看的多，马上就忘了。今天想到的是，可以多个文档一起比较起来看；另一个想到的学习的方式是，先把理论快速的过一遍，不对自己有过高的要求，不急于求成，然后马上进行理论的实践，通过实践再回过头去好好研究理论，这样应该可以避免空洞的看理论速度慢的问题。



#### 2019年3月25日 09:06:30

昨天学习发现一个问题，学习的进度太慢了，以前一直喜欢看视频学习，分析了下那些内容比较简单的
东西很好理解；但是现在学习的东西很多都是非常复杂的，不容易理解，需要常常去复习，这
个时候视频就显得很鸡肋，还是文档容易复习，而且现在要慢慢的适应文档的自学方式.现在给每天的任
务是早上早读的方式去读文档。



#### 2019年3月24日 22:00:33

看了9个小时的电视剧，19版的《倚天屠龙记》+ 《都挺好》
没有学习大数据，心情比较崩溃😫



#### 2019-03-22 14:16:32

the second time edit README.MD



#### 2019-03-24 10:41:01

今天从9：30过来，到现在已经差不多学习一个小时，**HDFS**

**hadoop2.0** 的主要思想是**JobTracker**两个主要的功能分分离成单独的组件，这两个功
能是资源管理和任务调度/监控

新的资源管理器全局管理所有应用程序计算资源的分配

**ApplicationMaster**负责相应的调度和协调

**ResourceManager**和每一台机器的阶段管理服务器能够管理用户在哪台机器上的进程
并能对计算进行组织。

**NodeManager**是每一台机器框架的代理，是执行应用程序的容器，监控应用程序的资
源使用情况（CPU 内存 磁盘 网络）并且向调度器汇报。

每一个应用的**ApplicationMaster**的职责有：向调度器索要适当的资源容器，运行任务，
跟踪应用程序的状态和监控他们的进程，处理任务的失败原因

客户端不变，其调用API及接口大部分保持兼容，这也是为了开发使用者透明化，
对原码不必做大的改变，但是原框架的**JobTracker**和**TaskTracker**不见了，取而代之的
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







