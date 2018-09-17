# 错误、调试和测试

## 错误处理
# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常常见
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:',r)  
# except ZeroDivisionError as e:
#     print('except:', e)
# else:
#     pass
# finally:
#     print('finally...')

# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')

# 记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
# Python内置的logging模块可以非常容易地记录错误信息：

# 抛出错误
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：

# class FooError(ValueError):
#     pass

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value:%s'%s)
#     return 10 / n

# foo('0')

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

## 调试

# 1,print

# 2,assert 
# def foo(s):
#     assert s !=0, 's is zero!'
#     return 10 / s

# foo(0)

# 3,logging

# 4,pdb  运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行
import pdb

s = '0'
n = int(s)  
pdb.set_trace()
print(n)

# 5,IDE