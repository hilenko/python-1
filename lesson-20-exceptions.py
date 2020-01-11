import sys
filename = 'name .txt'

#myfile = open(filename, mode='r')
# print(myfile.read())

try:
    print('Insity try')
    myfile = open(filename, mode='r')
except Exception:
    print('Inside except')
    print('Found Error')
    print(sys.exc_info()[1])
else:
    print('Insie else')
    print(myfile.read())
    sys.exit()
# finally:
#     print('Inside finally')

print('\n The End')