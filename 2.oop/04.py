# 继承的语法
# 在Python中,任何的类都叫做object
class Preson():
    name="Noname"
    age=0
    __petname="sec"  # 此时petname是受保护的,子类可以用,但不能公用

    def sleeep(self):
        print("sleep...")

    def work(self):
        print("make money")
# 父类写在括号中'
class Teacher(Preson):
    teacher_id="123412"

    def make_test(self):  # 子类可以定义独有的成员属性和方法
        print("attention")

    def work(self):
        self.make_test()
        Preson.work(self)

t=Teacher()
print(t.name)
# print(t.__petname)   # 子类不能访问父类中的受保护的成员
print(t.teacher_id)
t.make_test()
t.work()





class Animal():
      pass
class Crawl_Ani(Animal):
      def __init__(self):
          print("I am a init cat")
class dog(Crawl_Ani):
    # __init__就叫定义函数
    # 每次实例化时,第一个被调用
    # 因为主要功能是进行初始化,所以得名
    # 定义函数的格式是固定的,一定要有一个变量
    def __init__(self):
        print("I am init in dog")
# 实例化的时候,括号内的参数余姚和构造函数的参数相匹配
# 实例化是,自动调用了dog中的构造函数
huhu = dog()

class cat(Crawl_Ani):
    pass
# 这时子类没有构造函数,于是自动调用了父类的调用函数
xiaodou = cat()


# 这是一个多继承的例子
# 子类可以直接拥有父类的属性,私有的除外
class fish():
    def __init__(self,name):
       self.name = name
        # 以上为构造函数的初始化
    def swim(self):
        print("I am swimming")
class bird():
    def fly(self):
        print("I am fling ")
class people():
    def __init__(self, name):
        self.name = name
    def work(self):
        print("I am working")


class SuperMan(people,bird,fish):

       pass

# 在这里我出现了一个问题,没有pass,导致系统认为我在定义函数.提醒我需要缩进
S=SuperMan('dachao')
S.fly()
S.work()


