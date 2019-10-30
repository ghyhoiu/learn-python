class Person():
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        print("设置属性:{0}".format(key))
        # 以下案例会导致死循环
        #self.key  = value
        # 为了避免进入死循环,规定统一调用父类魔法函数
        super().__setattr__(key,value)
p = Person()
p.age = 18