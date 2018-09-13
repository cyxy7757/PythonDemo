# 高级特性
from collections import Iterable
from collections import Iterator

## 切片
# 取 一个list 的前三个元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']


# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])

# 这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片
print(L[0:3])

# 如果第一个索引是0，还可以省略：
#print(L[:3])

# Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
# L[-2:] L[-2:-1]

# 切片操作十分有用。我们先创建一个0-99的数列,可以通过切片轻松取出某一段数列。比如前10个数,或后10个数

#L[0:10] L[-10:0]

# 前10个数，每两个取一个：
L[:10:2]

# 所有数，每5个取一个：
L[::5]

# 甚至什么都不写，只写[:]就可以原样复制一个list
L[:]

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
# sliTuple = (0,1,2,3,4,5)[:3]
# print(sliTuple)

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串

# print('asdfghj'[:3])

# 在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。

## 迭代
# Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上

# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
d = {'a':1, 'b':2, 'c':3}
# for key in d:
#     print(key)

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

# 由于字符串也是可迭代对象，因此，也可以作用于for循环
# for ch in 'AVC':
#     print(ch)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
# print(isinstance('abc',Iterable)) # true
# print(isinstance([1,2,3],Iterable)) # true
# print(isinstance(123,Iterable)) # false

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)

# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)
# 1 1
# 2 4
# 3 9


## 列表生成式

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：

# theList = []
# for x in range(1, 11):
#     theList.append(x * x)
# print(theList)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
# theList = [x * x for x in range(1, 11)]
# print(theList)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方

# theList = [x * x for x in range(1, 11) if x % 2 == 0]
# print(theList)

# 还可以使用两层循环，可以生成全排列

# twoLayerList = [m + n for m in 'ABC' for n in 'XYZ']
# print(twoLayerList)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k,v in d.items():
#     print(k, '=', v)

# 因此，列表生成式也可以使用两个变量来生成list

# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# theList = [k + '=' + v for k,v in d.items()]

# 把一个list中所有的字符串变成小写
# theList = ['Hello', 'World', 'Apple']
# print([s.lower() for s in theList])

# 使用内建的isinstance函数可以判断一个变量是不是字符串
# x = 'abc'
# y = 124
# print(isinstance(x,str)) # true
# print(isinstance(y,str)) # false

## 生成器
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
theList = [x * x for x in range(10)]
theg = (x * x for x in range(10))
print(theList)
print(theg)

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
# 上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
# for n in theg:
#     print(n)

## 迭代器

# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：

#一类是集合数据类型，如list、tuple、dict、set、str等；

#一类是generator，包括生成器和带yield的generator function。

#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

#可以使用isinstance()判断一个对象是否是Iterable对象


isinstance([], Iterable) # true
isinstance({}, Iterable) # true
isinstance('abc', Iterable) # true
isinstance((x for x in range(10)), Iterable) # true

# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

#可以使用isinstance()判断一个对象是否是Iterator对象

isinstance((x for x in range(10)), Iterator) # true
isinstance([], Iterator) # false
isinstance({}, Iterator) # false
isinstance('abc', Iterator) # false

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

isinstance(iter([]), Iterator) # true
isinstance(iter('abc'), Iterator) # true

# Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
