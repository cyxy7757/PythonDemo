# 面向对象编程

# 类和实例
# 在Python中，定义类是通过class关键字

# class Student(object):
#     pass

# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的
# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
# bar = Student()
# bar.name = 'lili'
# print(bar.name)

# 可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# bart = Student('lili',99)
# print(bart.name,bart.score)

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

## 数据封装

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def print_score(self):
#         print('%s: %s'%(self.name, self.score))
    
#     def get_score(self):
#         if self.score >=90:
#             return 'A'
#         elif self.score >=60:
#             return 'B'
#         else:
#             return 'C'

# lili = Student('lili',88)
# lili.print_score()

# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

## 访问限制

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
# 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_self(self):
        print('%s: %s'%(self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name = name

# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：

## 继承和多态

# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

# 获取对象信息
# 我们来判断对象类型，使用type()函数
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 能用type()判断的基本类型也可以用isinstance()判断：


# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
#print(dir('abc'))


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

# 可以传入一个default参数，如果属性不存在，就返回默认值：
# getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

## 实例属性和类属性

# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

def Student(object):
    name = 'i am student'