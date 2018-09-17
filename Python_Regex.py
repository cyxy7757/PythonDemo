# 正则表达式
import re

s ='ABC\\-001' # python 的字符串
s1 = r'ABC\-001' # 建议使用Python的r前缀，就不用考虑转义的问题了

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
test = '用户输入的字符串'
if re.match(r'正则表达式',test):
    print('match')
else:
    print('failure')

# 切分字符串
# 用正则表达式切分字符串比用固定的字符更灵活

# str1 = 'a b  c'
# list1 = str1.split(' ')
# print('list1:',list1)

# list2 = re.split(r'\s+', str1)
# print('list2:',list2)

# str2 = 'a,b, c  d'
# list3 = re.split(r'[\s\,]+',str2)
# print('list3:',list3)

# str3 = 'a,b;; c  d'
# list4 = re.split(r'[\s\,\;]+',str3)
# print('list4:',list4)

# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group)
# ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
phone_regex = r'^(\d{3})-(\d{3,8})$'
phoneStr = '010-12345'

m = re.match(phone_regex,phoneStr)
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))