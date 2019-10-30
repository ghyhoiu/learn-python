# 对于一个列表,偶数组成新的列表
# 定义过滤函数
# 过滤函数要求有输入,有布尔值
def isEven(a):
    return a % 2 == 0

l = [1,23,2,45,3,4,5]
l1=filter(isEven,l)
for i in l1:
    print(i)