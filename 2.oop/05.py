class person():
    name = "xiaoming"
    age = 18

    def eat(self):
        print("eating...")
    def drink(self):
        print("drinking...")
    def sleep(self):
        print("zzz...")
class teach(person):
    def wrok(self):
        print("working")

class student(person):
    def study(self):
        print("work homework...")

class tutol(teach,student):
    pass


t = tutol()
print(tutol.__mro__)# 打印MRO表
print(t.__dict__)
print(tutol.__dict__)


print("*"*20)
# 以下为Mixin的使用方法
class teacherMixin():
    def work(self):
        print ("work homework....")
class studentMixin():
    def teach(self):
        print("teaching...")

class tutorm(person,teacherMixin,studentMixin):
    pass
tt = tutorm
print(tutorm.__mro__)
print(tutorm.__dict__)
print(tt.__dict__)