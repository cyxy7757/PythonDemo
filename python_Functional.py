# 函数式编程
from functools import reduce
from operator import itemgetter, attrgetter
## 高阶函数

# 函数本身也可以赋值给变量，即：变量可以指向函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
# 编写高阶函数，就是让函数的参数能够接收别的函数

# def add(x, y, f):
#     return f(x) + f(y)

# print(add(-5, 6, abs))

# map/reduce

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
# def f(x):
#     return x*x
# r = map(f,[1, 2, 3, 4])
# print(list(r))

# 把这个list所有数字转为字符串
#print(list(map(str, [1, 2, 3, 4])))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

# 对一个序列求和，就可以用reduce实现
# def add(x, y):
#     return x + y

# print(reduce(add,[1, 2, 3]))

# 当然求和运算可以直接用Python内建函数sum()，没必要动用reduce
# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场

# def fn(x, y):
#     return x * 10 + y

# print(reduce(fn,[1, 3, 5, 7]))

# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数

# def fn(x, y):
#     return x * 10 + y

# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return  digits[s]
# print(reduce(fn,map(char2num,'13579')))

# 整理成一个str2int的函数就是
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn,map(char2num,s))

# print(str2int('13579'))

# 还可以用lambda函数进一步简化成：

# def char2num(s):
#     return DIGITS[s]

# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y,map(char2num,s))

# 也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！

## filter
# Python内建的filter()函数用于过滤序列 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

# 在一个list中，删掉偶数，只保留奇数
# def is_odd(n):
#     return  n % 2 == 1

# y = list(filter(is_odd,[1, 2, 4, 5, 7, 8]))
# print(y)

# 把一个序列中的空字符串删掉
# def not_empty(s):
#     return s and s.strip()

# y = list(filter(not_empty,['a', '', 'b']))
# print(y)

## sorted

# Python内置的sorted()函数就可以对list进行排序
#print(sorted([23,4,5,-90,-3]))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序

#print(sorted([23,4,5,-90,-3], key = abs))

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
# 我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较

#sortedList = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower())

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
#sortedList = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower(), reverse = True)

L = [('Bob', 75), ('Tony', 18),('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 按姓名排序
# L2 = sorted(L,key = itemgetter(0))
# print(L2)

# 按分数从高到底牌
L3 = sorted(L,key = itemgetter(1),reverse = True)
print(L3)