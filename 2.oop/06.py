# 属性案例
# 创建student类,描述学生
# 但name格式并不统一
# 可以使用增加一个函数,然后自动调用的方式,但很麻烦
class student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # 如果不想修改代码,并想将name变成大写
        self.setName(name)

    def intro(self):
        print ("my name is {0}".format(self.name))
    def setName(self,name):
        self.name = name.upper()

S1 = student("xiaoming",18)
S2 = student("XiaoHong",24)

S1.intro()
S2.intro()

# 属性案例二(property)
# 定义一个类,有name和age两个属性
# 对于任意输入的年龄,我们希望可以大写保存
# 年龄,我们希望可以使用整数保存

class Person():
    def fget(self):
        return  self._name

    def fset(self,name):
        # 所有输入的姓名以大写形式来保存
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel,"doc")
P1 = Person()
P1.name = "guanguan"
#P1.age = 19.8
print(P1.name)
#print(P1.age)

class Number():
    def fget(self):
        return self._age
    def fset(self,age):
        self._age =int (age)

    def fdel(self):
        self._age = 0
    age = property(fget, fset, fdel, "doc")

N1 = Number()
N1.age = 19.8
print(N1.age)
