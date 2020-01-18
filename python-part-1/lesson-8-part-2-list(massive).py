cars = ["bmw", "merc", "audi","opel", "matiz", "lada", "volkswagen", "shoha"]

for i in cars:
    #print(i.upper())
    print(i.capitalize())


my_list = list(range(1, 10 + 1))
print(my_list)

for i in my_list:
    i = i * 10
    print(i)

my_list.reverse()
print(my_list)
print("===============================")
print("Min number from my list is: " + str(min(my_list)))
print("Max number from my list is: " + str(max(my_list)))
print("Sum number from my list is: " + str(sum(my_list)))

print("============V2===================")
mycars = cars[1:4 +1 ]
print(mycars)

print("============V3===================")
mycars = cars[:5]
print(mycars)

mycars = cars[-4 :-1]
print(mycars)

#copy list
mytestcars = cars[:]
print(mytestcars)