def multi(*args):
    sum = 1;
    count = 1;
    for i in args:
        if type(i) is type(1) or type(i) is type(1.):
            sum *= i
        else:
            print('第{}项不是一个有效的整数！'.format(count))
            return;
        count += 1
    return sum


print(multi(3 , 4))