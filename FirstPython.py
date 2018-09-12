# msg = 'Hello world python'
# print(msg)

s = set([1,2,3,4,4,5])
print(s)

# 定义一个求绝对值的函数，当入参错误时，给出提示。
# def my_abs(x):
#     if not isinstance(x,(int, float)):
#         raise TypeError("类型错啦，只能整数或者浮点数"")
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_abs(-5))
# print(my_abs('a'))

# 默认参数
def enroll(name, gender, age = 8, city = 'Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

# print(enroll('lili','girl'))
# print(enroll('dick','boy',9,'henbei'))
print(enroll('jack','boy', city='henbei'))

# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# def add_end(l=None):
#     if l is None:
#         l = []
#     l.append('End')
#     return l

# 可变参数
# def calc(*numbers):
#     sum = 0
#     for number in numbers:
#         sum = sum + number*number
#     return sum

# # print(calc())
# # print(calc(1,2,3,4))

# # *nums表示把nums这个list的所有元素作为可变参数传进去
# nums = [4,5,6,7]
# print(calc(*nums))

# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:',name,'age:',age,'others:',kw)

#print(person('Michael',20))

# print(person('Bob',22,city = 'Beijing'))
# person('Adam', 45, gender='M', job='Engineer')

#extra = {'city':'Beijing', 'job':"English"}
#print(person("Jack",24,city = extra["city"], Job = extra["job"]))
# 简化写法
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
#print(person("Jack",24,**extra))

# 命名关键字参数

# 检查是否有city和job参数
# def person(name, age, **kw):
#     if "city" in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
# def person(name, age, *, city, job):
#     print(name, age, city, job)

# print(person('Jack', 24,city = 'shenzhen',job = 'coder'))

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
