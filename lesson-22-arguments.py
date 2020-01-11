import sys
import os

# print('hello')
#
# print(sys.argv[1:])
# print(sys.argv[1])

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == '-h':
        print('''
        -h - help 
        -a - show all arg 
        -o - output
        '''
              )
    #print('Arguments is: ' + str(sys.argv[1:]))
else:
    print('Arguments NOT PROVIDE')

print('\n\tnext block will os module')

sys.exit()

#os.mkdir('create_dir_from_python')
#os.system('ls -la create_dir_from_python')