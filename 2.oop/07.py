# __call__举例
class A():
    def __init__(self, name=0):
        print("已经被调用")

    def __call__(self):
        print("再一次被调用")
    def __str__(self):
        return"小明是个好学生"
    # 这时将对象变为字符串使用
a = A()
a()
print(a)

class B():
    name = "Noname"
    age = 18
    def __getattr__(self,item):
        print("没有找到哦")

b = B()
print(b.name)
print(b.attr)
# 这时不会报错,只会用魔法函数