# 抽象类的实现
import abc

# 声明一个类并且指定当前类的元素
class human(metaclass=abc.ABCMeta):

    # 定义一个抽象类的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass

    # 定义静态的抽象方法
    @abc.abstractstaticmethod
    def sleep():
        pass
