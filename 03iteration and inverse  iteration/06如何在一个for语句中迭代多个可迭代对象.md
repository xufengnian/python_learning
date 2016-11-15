#如何在一个for语句中迭代多个可迭代对象呢？

看图说话
![](http://i.imgur.com/KdSUXLd.png)

所谓的并行，就是你需要多个数据集中的每一项进行联合操作

所谓的串行，就是你需要对多个数据集中的每一项进行单一操作

##并行解决方案

根据问题，我们先使用随机数生成3个成绩列表吧

	>>> from random import randint
	>>> chinese = [randint(60,100) for x in range(40)]
	>>> math = [randint(60,100) for x in range(40)]
	>>> english = [randint(60,100) for x in range(40)]

如何解决？

此处不再介绍传统方法，我们采用zip()函数，将不同数据集文件打包成一个元组的列表

	>>> zip([1,2,3,4],('a','b','c','d'))
	[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

对于问题一，我们首先建立一个空列表用来存放3科总分
	total = []

然后就是利用zip()函数，通过for循环迭代了
	for c,m,e in zip(chinese,math,english):
		total.append(c + m + e)

输出total如下

	[231, 240, 237, 208, 233, 229, 222, 220, 229, 258, 238, 224, 212, 249, 252, 240, 253, 207, 224, 229, 283, 230, 252, 258, 243, 241, 249, 246, 216, 235, 235, 206, 245, 249, 186, 221, 199, 219, 226, 221]

##串行解决方案

使用标准库中的itertools.chain,它能将多个可迭代对象连接

比如
	
	from itertools import chain
	for x in chain([1,2,3,4],['a','b','c']):
		print x

输出

	1
	2
	3
	4
	a
	b
	c

两个数据集之间像链条一样连接起来

好了，为了解决问题二，我们还是随机生成4个班级的成绩，班级人数不同

	>>> c1 = [randint(60,100) for x in range(40)]
	>>> c2 = [randint(60,100) for x in range(42)]
	>>> c3 = [randint(60,100) for x in range(45)]
	>>> c4 = [randint(60,100) for x in range(48)]

使用chain()之后的效果呢

	from itertools import chain
	>>> counter = 0
	>>> for x in chain(c1,c2,c3,c4):
	...     if x >90:
	...             counter +=1
	...

输出下counter

	40

搞定！