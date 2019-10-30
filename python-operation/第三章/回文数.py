a = input("请输入你心中的那个数字: ")
b=len(a)
for i in range (0,b):               
    if(a[i]==a[b-i-1]):
        c=1
    else:
        c=0
if(c==1):
    print("yes，这是回文数")
else:
    print("no，这不是回文数")

