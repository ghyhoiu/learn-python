# 高阶函数举例
# funA是普通函数,返回一个传入数字的123倍

def funA(n):
    return n*123

print(funA(12))
# 调用一个函数
def funB(n):
    return funA(n) * 3

print(funB(4))

# 写一个高阶函数
def funC(n, f):
    #假定函数是把n扩大123倍
    return f(n) * 3

print(funC(4,funA))

def funD(n):
    return n*89
print(funC(3,funD))
# 高阶函数比较灵活