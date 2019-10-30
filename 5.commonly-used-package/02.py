# 需要导入时间模块
import time
# 时间模块的属性
# timezone:当前时区和UTC时间相差的秒数,在没有夏令时的情况下的间隔
print(time.timezone)
# altzone:获取当前时区与UTC时间相差的秒数,在夏令时的情况下的间隔
print(time.altzone)
# daylight:测当前时间是否是夏令时时间状态,0 表示是,若发生错误,则表示不是夏令时时间
# 得到时间戳
print(time.time())
# time.localtime:得到的为当前时间
t= time.localtime()
print(t)
print(t.tm_mday)
# asctime() 返回元祖的正常字符串化之后的时间格式
# 格式: time.asctime(时间元祖)
# 返回值: 字符串
print(time.asctime(t))
# ctime(): 直接获取字符串化的当前时间
print(time.ctime())
# mktime(): 使用时间元祖获得对应的时间戳
print(time.mktime(t))
# clock : 获取cpu时间,3.0~3.3 版本可以使用 3.6的调用有问题
# sleep : 使程序进入睡眠,n秒之后继续
for i in range(4):
    time.sleep(1)
    print(i)
