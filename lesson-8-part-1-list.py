

cities = ["Kiev","lvov zakarpatya","odessa", "nikolaev", "frankov","poltava"]
print(cities)      #print list
print(len(cities)) # count cities
print(cities[-1])  #last city
print(cities[1].upper())
cities[2] = "dnipro"
print(cities)

cities.append("dnipro-2")
print(cities)
cities.insert(2, "new york")
print(cities)

del cities [3]
print(cities)
cities.remove("Kiev")
print(cities)
deleted_city = cities.pop()
print("deleted city is: " + deleted_city )
print(cities)

# #sort
# cities.sort()
# print(cities)
#
# cities.sort(reverse=True)
# print(cities)

cities.reverse()
print(cities)