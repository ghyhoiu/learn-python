def isOdd(num):
    try:
        if type(num) == type(0.):
            raise TypeError
        if num%2 == 0:
            return False
        else:
            return True
    except TypeError:
            print('这不是一个有效的整数！')

print(isOdd(6))
print(isOdd(8))
print(isOdd(-5))
print(isOdd('hello world'))
print(isOdd(0.5))