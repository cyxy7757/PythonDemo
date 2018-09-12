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