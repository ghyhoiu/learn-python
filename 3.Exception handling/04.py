# raise案例2
# 定义一个自己的错误
# 注意: 自己定义的异常必须是系统异常的子类

class QingError(ValueError):
   pass
try:
    print("i love my little baby")
    print("这个世界,你好吗")
    # 手动引发一个错误
    raise QingError
    print("结束了吗?")
except QingError:
    print("这可是我自己引发的错误哦!")
    print("这个错误的名字可是真的好听")
    exit()
except exception:
    print("我应该在每次异常检查中都加入这一句")
finally :
    print("你猜我会出现吗?")
    print("啊!我暴露了")