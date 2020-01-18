name = input('please input your name: ')
print('hello', name)

num1 = input('input your number_1 : ')
num2 = input('input your number_2 : ')

sum = int(num1) + int(num2)
print(sum)

messages = ''

while True:
    messages = input('Enter password: ')
    if messages == 'secret':
        break
    else:
        print(messages + ' password Not correct')

print('password was: ' + messages)


mylist = []
msg = ''

while msg != 'stop':
    msg = input('Enter yout item , and STOP to finish ')
    mylist.append(msg)

print(mylist)