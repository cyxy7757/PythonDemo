# 常用第三方模块
import requests
r = requests.get('https://www.douban.com/') # 豆瓣首页
# print(r.status_code)
# print(r.headers)

import psutil
print(psutil.cpu_count())

