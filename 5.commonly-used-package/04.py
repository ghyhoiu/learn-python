# os模块的案例
# getcwd():获取当前的工作目录
import os
mydir = os.getcwd
print (mydir)
# listdir(): 获取一个目录中所有的子目录和文件名的列表
print(os.listdir())
# makedirs():递归创建文件夹
# print(os.makedirs("test")) 可以使用，但之后还会测试，所以将其变为标注，对之后的测试有帮助
# system()运行系统的shell命令
# print(os.system()) # 不知道为什么在windows下不能使用
# getenv(): 获取当前的环境变量值 
print(os.getenv("PATH")) 
print(os.pardir)
print(os.curdir)
print(os.linesep)
print(os.sep)
print(os.name)

 