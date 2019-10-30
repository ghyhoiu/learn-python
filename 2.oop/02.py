class A():
    name = "xiaoming"
    age = 18
    # 注意say的写法,参数有一个self
    def say(self):
        self.name = "xiaohong"
        self.age = 200

print(A.name)
print(A.age)

print("*"*20)
# id 可以判别是否为同一个变量
print(id(A.name))
print(id(A.age))

print('*'*20)

a = A()

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
# 结论表示a和A中变量相同
# 此案例表明,类实例的属性和其实例的属性在不对实例赋值的情况下,指向的是同一个变量

b = A()
b.age = 16
b.name = "xiaohong"

print('*'*20)
print (b.name)
print(b.age)
print(id(b.name))
print(id(b.age))
# 当赋值时,会改变变量
print(A.__dict__)
print(a.__dict__)
print(b.__dict__)