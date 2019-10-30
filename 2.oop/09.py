class Person():
# 实例方法
    def eat(self):
        print(self)
        print("eating...")

# 类方法
# 类方法的第一个参数,一般命名为cls.用于区别self
    @classmethod
    def play(cls):
        print("playing...")

# 静态方法
    @staticmethod
    def say():
        print("talking...")
xiaoming = Person()
# 访问实例方法

xiaoming.eat()
# 类方法

xiaoming.play()
# 静态方法

xiaoming.say()