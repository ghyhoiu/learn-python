
'''
定义一个学生类,用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空壳;pass代表直接略过
    pass

# 定义一个对象
xiaoming = Student()

# 定义一个类, 用来描述听课的学生
class ListenStudent():
    name = None
    age = 18
    crouse = "python"

    def DoHomework(self):
        print ("正在学习")

    # 推荐在函数末尾使用return
        return None

# 实例化一个叫xiaohong 的学生
xiaohong = ListenStudent()
print (xiaohong.age)
print (xiaohong.crouse)
# 注意成员函数的调用没有传入参数
xiaohong.DoHomework()


