foot = int(input("请输入腿的数量:"))
head = int(input("请输入头的数量:"))
while foot%2!=0:
    print("鸡鸡和兔兔的脚为偶数哦,请新输入")
    foot = int(input("请输入腿的数量"))
    head = int(input("请输入头的数量"))
rabbit = foot/2-head
while rabbit<0 :#rabbit>head:
    print ("脚和头的数量不匹配,请重新输入")
    foot=int(input ("请输入腿的数量"))
    head=int(input ("请输入头的数量"))
chicken = head - rabbit
print("兔兔有{0}只,鸡鸡有{1}只".format(rabbit,chicken))
