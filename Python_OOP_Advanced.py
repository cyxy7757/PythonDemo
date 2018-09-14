# 面向对象高级编程

# 使用 __slots__
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性

# class Student(object):
#     pass

# 给实例绑定一个属性
# s = Student()
# s.name = 'Michael'

# 给实例绑定一个方法
# from types import MethodType
# def set_age(self, age): # 定义一个函数作为实例方法
#     self.age = age

# s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
# s.set_age(25)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：

# 为了给所有实例都绑定方法，可以给class绑定方法
# def set_score(self, score):
#     self.score = score
# Student.set_score = set_score

# 给class绑定方法后，所有实例均可调用：
# s.set_score(100)
# s2 = Student()
# s2.set_score(50)

# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

# class Student(object):
#     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

## 使用@property

# 为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：

# class Student(object):
#     def get_score(self):
#         return self._score
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100')
#         self._score = value

# s = Student()
# s.set_score(60)
# score = s.get_score()
# print(score)
# # 属性不能随便设置了
# s.set_score(-100)

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

# class Student2(object):
#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100')
#         self._score = value

# stu = Student2()
# stu.score = 1000
# print(stu.score)

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：


## 多重继承

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

## 定制类

# __str__ 方便调试，打印类的详细信息
#  class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name=%s)' % self.name
#     __repr__ = __str__

# __iter__ 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b

#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值


# __getattr__
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：

# __call__


## 使用枚举类
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# @unique装饰器可以帮助我们检查保证没有重复值。

day1 = Weekday.Fri
print('day1:',day1)