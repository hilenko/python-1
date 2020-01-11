# generate data - http://www.generatedata.com/
# help reg - https://regex101.com/

import re

input_file = 'dump_data.txt'
output_file = 'result.txt'

inputfile = open(input_file, mode='r', encoding='latin-1')
resultfile = open(output_file, mode='w', encoding='latin-1')
mytext = inputfile.read()

lookfor = r'[\w.-]+@(?!intel\.com)[A-Za-z]+\.[\w.]+'

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + '\n')

print('Total: ' + str(len(results)))
