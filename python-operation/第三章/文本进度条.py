import time
scale =3 
for  i in range(scale + 1) :
    a = "."*i
    print("\rstarting{0}".format(a),end=" ")
    time.sleep(0.5)
print("Done!")