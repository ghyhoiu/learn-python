# map举例
# 有一个列表,想对列表中的每一个元素乘以10,并得到新的列表
def mulTen(n):
    return n *10
l1 =[i for i in range(10)]
l2 =map(mulTen,l1)
for i in l2:
    print(i)
