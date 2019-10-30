# lambda表达式
# 以lambda开头
# 紧跟参数(如果有的话)
# 参数后面用逗号和表达式分开
# 只是一个表达式,没有return

# 计算一个数的123倍(单个参数)
stm = lambda x:x * 123
print(stm(12))
# 计算三个数字的加法(多个参数)
stm2 = lambda a,b,c: a + b + c
print (stm2(12,3,5))