all_cars = ["bmw", "merc", "audi", "opel", "matiz", "lada", "seab", "shoha"]
german_cars = ["bmw", "merc", "audi","opel"]

for i  in all_cars:
    if i  in german_cars:
        print(i + " is german car")
    else:
        print(i + " isn't gernam car")