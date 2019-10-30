# else 案例

try:
    num = int(input("请输入你要输入的数字(整数):"))
    rst = 100/num
    print("计算结果是{0}".format(rst))
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
except Exception as e:
    print("我也不知道哪里错了")
    print(e)
    exit()
else:
    print("你成功了,小伙子.你是最吼滴!!")