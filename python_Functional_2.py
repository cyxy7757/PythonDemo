## 返回函数
import functools
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 实现一个可变参数的求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
# f = lazy_sum(1, 3, 5)
# print(f())
# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力

## 闭包
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs

# f1, f2, f3 = count()
# print('f1:',f1(),'f2:',f2(),'f3:',f3()) # f1: 9 f2: 9 f3: 9
#! 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs

# f1, f2, f3 = count()
# print('f1:',f1(),'f2:',f2(),'f3:',f3()) # f1: 1 f2: 4 f3: 9

# 一个函数可以返回一个计算结果，也可以返回一个函数。返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

## 匿名函数

# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
# list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# f = lambda x: x * x
# print(f(5))

# 同样，也可以把匿名函数作为返回值返回
# def build(x, y):
#     return lambda: x * x + y * y

## 装饰器

# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
# def now():
#     print('2018-09-11')
# f = now
# f()

# 函数对象有一个__name__属性，可以拿到函数的名字
# def now():
#      print('2018-09-11')
# print(now.__name__)

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数
# @log放到now()函数的定义处，相当于执行了语句： now = log(now)
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s()'% func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def now():
#      print('2018-09-11')

# #now()

# now = log(now)
# print(now.__name__) # wrapper

# Python内置的functools.wraps就是干这个事,转化func的name

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
     print('2018-09-11')

now = log(now)
print(now.__name__) # wrapper