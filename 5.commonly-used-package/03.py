# datetime常见属性
# datetime.time:一个理想的日期,提供year ,month ,day 属性
import datetime
import time
import timeit
print(datetime.date(2018,9,2))
# datetime.time:一个理想的时间,提供hour ,minute, second 属性
# datetime.datetime:提供日期和时间的一个组合
from datetime import datetime
# 常用类方法
# today
print(datetime.today())
# now 
print(datetime.now())
# utcnow
print(datetime.utcnow())
# fromtimestamp: 表示从当前时间戳返回本地时间
print(datetime.fromtimestamp(time.time()))
# datetime.timedelta:提供一个时间长度
# 将当前时间向后移动一个小时
from datetime import timedelta
t1 = datetime.now()
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
td = timedelta(hours=1)
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))
# timeit: 时间测量工具
def p():
    time.sleep(3.6)
tl = time.time()
p()
print(time.time() - tl)
# 利用timeit来比较两种生成列表的时间快慢
c = '''
sum = []
for i in range(1000):
    sum.append(i) 
'''
t1 = timeit.timeit(stmt="[i for i in range(1000)]",number = 100000)
t2 = timeit.timeit(stmt=c,number = 100000)
print(t1)
print(t2)
# setup的使用方法
s = '''
def doit(num):
    for i in range(num):
        print("this is {} time".format(i))
'''
t = timeit.timeit(stmt=s,setup= s+"num=3",number=10)
print(t）