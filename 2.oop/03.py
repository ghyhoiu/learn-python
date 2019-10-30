class Student():# 01
    name = "xiaoming"
    age = 18
    # 注意say的写法,参数有一个self
    def say(self):# self并不是关键字,可以换成其他
        self.name = "xiaohong"
        self.age = 200
        print("My name is{0}".format(self.name))
        print("My age is{0}".format(self.age))
    def SayAgain():
        print(__class__.name)# 03
        print(__class__.age)

        print("hello , nice to meet you")

S = Student()
Student.SayAgain()# 02
# 这时没有self,调用时需要绑定类函数使用名

xiaohong = Student()
xiaohong.say()



