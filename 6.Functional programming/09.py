# 这时是十进制的
print(int("12345"))
# 求八进制的字符串12345,表示成10进制的数为多少
print(int("12345",base=8))
# 新建一个函数,此函数是默认的输入字符是16进制
# 把此字符串返回十进制的数字
def int16(x,base=16):
    print(int(x,base))

int16("12345")
import functools
int16 = functools.partial(int,base=16)
print(int16("12345"))