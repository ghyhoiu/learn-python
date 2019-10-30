a = "＋"
b = " "
c = "－"
d = "丨"
 
def f_sa(n):
    for i in range(10*n+1):
        if i%10 == 0:
            print(a,end="")
        elif i%2 == 1:
            print(b,end="")
        else:
            print(c,end="")
    print("\n")
def f_sb(n):
    for i in range(14*n+1):
        if i%14 == 0:
            print(d,end="")
        else:
            print(b,end="")
    print("\n")
def f_sn(n):
    for i in range(5*n+1):
        if i%5 == 0:
            f_sa(n)
        else:
            f_sb(n)    
def main():
    while True:
        n = input("请输入每边包含的正方形个数：")
        if n == 'q':
            break
        else:
            f_sn(eval(n))
 
main()