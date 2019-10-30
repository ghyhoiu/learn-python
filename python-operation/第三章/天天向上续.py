# 无论是平年还是闰年，对七取余之后都是小于四，所以不考虑
i=0
a=1
while i<365:
    i=i+1
    if i%7<4:
        a=a
    elif i%7>=4:
        a=a+a*0.01
print("最后你的能力值是{0}".format(a))
