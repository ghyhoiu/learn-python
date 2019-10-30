# raise案例
try:
    print("i love my little baby")
    print("这个世界,你好吗")
    # 手动引发一个错误
    raise ValueError
    print("结束了吗?")
except ValueError:
    print("这可是我自己引发的错误哦!")
    exit()
except exception:
    print("我应该在每次异常检查中都加入这一句")
finally :
    print("你猜我会出现吗?")
    print("啊!我暴露了")