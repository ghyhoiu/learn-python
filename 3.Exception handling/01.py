# 简单异常案例
try:
    num = int(input("请输入你要输入的数字(整数):"))
    rst = 100/num
    print("计算结果是{0}".format(rst))
except:
    print("你为什么要输入{0},你还能干点啥".format(num))
    #  exit是退出程序
    exit()