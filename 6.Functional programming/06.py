# 排序案例
l1 = [1,2,3,5,2,2435,24,5234,52,435]
l2 = sorted(l1)
l3 = sorted(l1,reverse=True)
print (l2)
print (l3)
# 排序案例2
# 按照绝对值进行排序
a1 = [9,-8,-23,9,893,-8989,-99,98]
a2 = sorted(a1,key=abs)
a3 = sorted(a1,key=abs,reverse=True)
print (a2)
print (a3)