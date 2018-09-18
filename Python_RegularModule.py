# 常用的内建模块
# datetime
 #from datetime import datetime, timedelta, timezone


# now = datetime.now()
# #print(now)

# # timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）
# dt = now.timestamp()  # 时间转时间戳
# #print('dt:',dt)

# t = 1429417200.0
# dt2 = datetime.fromtimestamp(t) # 时间戳转时间,转为本机时间
# #print('dt2:',dt2)

# # timestamp也可以直接被转换到UTC标准时区的时间：
# dt3 = datetime.utcfromtimestamp(t)
#print('dt3:',dt3)

## str 转换为datetime

# cday = datetime.strptime('2015-6-1 10:19:59', '%Y-%m-%d %H:%M:%S')
# print('cday:',cday)

# datetime 转化为 str
# str_time = now.strftime('%a,%b %d %H:%M')
# print('str_time:',str_time)

# datetime 加减

# date1 = now + timedelta(hours=10) # 10 小时后
# print('date1:',date1)

# date2 = now - timedelta(days=1) # 一天前
# print('date2:',date2)

# date3 = now + timedelta(days=2, hours=10) #两天 10小时后
# print('date3:',date3)


## collections是Python内建的一个集合模块，提供了许多有用的集合类。



# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
# 定义一个点
# from collections import namedtuple
# Point = namedtuple('Point',['x', 'y'])
# p = Point(1, 3)
# print('p.x:',p.x,'p.y:',p.y)

# deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的
# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2']) # key2不存在，返回默认值

# counter 
# Counter是一个简单的计数器，例如，统计字符出现的个数

# from collections import Counter
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1

#print('c:',c)
# Counter实际上也是dict的一个子类


# base64
# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
import base64

print(base64.b64encode(b'dfdfdf'))

# hashlib 摘要算法 md5 和 SHA1

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib'.encode('utf-8'))
# print(md5.hexdigest())

# Python自带的hmac模块实现了标准的Hmac算法。我们来看看如何使用hmac实现带key的哈希。


# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x : x <= 10,natuals)
# print(list(ns))

# urllib提供了一系列用于操作URL的功能
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s'%(k, v))
    print('Data:',data.decode('utf-8'))


