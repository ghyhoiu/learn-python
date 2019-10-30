# 简单异常案例
# 给出提示
try:
    num = int(input("请输入你要输入的数字(整数):"))
    rst = 100/num
    print("计算结果是{0}".format(rst))
# 捕获一个异常,把异常实例化,出错信息会在实例里
# 注意以下写法:
# 以下语句是捕获 ZeroDivisionError异常并并实例化
# 如果出现了多种错误,要把越具体的情况,越往前放
except ZeroDivisionError as e:
    print("你为什么要输入{0},你还能干点啥???????".format(num))
    print(e)
    exit()
except ValueError as e:
    print("省点心吧,看不见要输入整数吗?")
    print(e)
except NameError as e:
    print("连名字都能打错,自己考虑吧")
    print(e)
    exit()
except AttributeError as e:
    print("对象没有这个属性,要不再试试")
    print(e)
    exit()
# 如果写上下面这句话,所有的错误都会被拦截
# 下面这句话一定是最后一个exception
except Exception as e:
    print("我也不知道哪里错了")
    print(e)
    exit()