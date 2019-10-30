i=0
a=1
while i<365:
    i=i+1
    if i%10<=6:
        a=a
    elif i%10>6:
        a=a+a*0.01
print("最后你的能力值是{0}".format(a))
