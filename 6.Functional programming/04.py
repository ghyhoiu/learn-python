from functools import reduce
 
# 定义一个操作函数
# 必须要有两个参数
def myAdd(x,y):
    return x + y

res = reduce(myAdd , [1,2,3,4,5]) 
print(res)
