# 函数作为返回值返回,被返回的函数在函数体内定义
def myF():
    def myF2():
        print("in the myF2")
        return 2
    return myF2
f2=myF()
print(f2)
f2()
# 复杂一点的例子
# 标准的闭包结构
def myF3(*args):
    def myF4():
        rst=0
        for n in args:
            rst += n
        print(rst)
        return rst
    return myF4
f5=myF3(1,2,3,4,54,56,6)
f5()