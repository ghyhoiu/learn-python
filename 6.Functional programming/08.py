
# 这时的f和hello两个函数是一样的id
# 现在有新的需求,每次打印hello的时候打印系统当前的系统时间
# 不改变现有代码
# 使用装饰器
import time
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())
        # 无论执行什么,都先执行这一个语句
        return f(*args,**kwargs)
    return wrapper
# 上面定义了装饰器
@printTime
def hello():
    print("hello world")
f=hello 
f()
