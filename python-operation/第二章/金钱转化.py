TempStr = input ("请输入带单位的金额: ")
if TempStr [-1] in [ 'u','U']:
    c=0
    c=eval(TempStr[0:-1])/7.14
    print("转化后的金额是{0}元".format(c))
elif TempStr [-1] in [ 'c','C']:
    f=7.14*eval(TempStr[0:-1])
    print("转化后的金额是{0}刀".format(f))
else:
    print("要带单位哦！！！！！！！！！")