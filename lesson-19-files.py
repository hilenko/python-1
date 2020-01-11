

inputfile = 'passwords.txt'
outputfile = 'my_output.txt'

lookfor = 'petya'

myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='w', encoding='latin_1')



#print(myfile.read())

for num, line in enumerate(myfile1, 1):
    if lookfor in line:
        print(str(num) + '. ' + line.strip())
        myfile2.write('Found : ' + line)

myfile1.close()
myfile2.close()


