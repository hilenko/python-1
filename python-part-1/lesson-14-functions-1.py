
def myfunction1(name):
    print('congratulations ' + name + ' wish you all the best!!!' )


def summa (x, y):
    return x + y


def factorial (x):
    '''Calculator for factorial of number! '''
    start = 1
    for i in range(1, x + 1):
        start = start * i
    return start


for i in range(1, 10 +1):
    print(str(i) + '!\t= ' + str(factorial(i)))



print(factorial(5))

i = summa(10,20)
print(i)
myfunction1("Ivan")
