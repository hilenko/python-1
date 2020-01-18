"""
Recursion functions
1) privet n time
2) sum        0+1+2+3+4+5
3) factorial  5! = 1 * 2 * 3 * 4 * 5
4) fidonacci  0,1,1,2,3,5,8,13,21,34,55,89

"""

def privet(x):
    if x == 0:
        return
    else:
        print('Helo world!')
        privet(x -1)

privet(1)

def sum(x):
    if x == 0:
        return 0
    # elif x == 1:
    #     return 1
    else:
        return x + sum(x - 1)

z = sum(5)
print(z)


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))


def fido(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fido(x -1) + fido(x -2)

print(fido(7))