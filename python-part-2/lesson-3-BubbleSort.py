# Lessons by Python
#
#
#
#
# by Sergey Gilenko
# ======================

sortlist = [10, 100, 33, 16, -18, 40, 64 , 11, 90]

def bubblesort(mylist):
    last_item = len(sortlist) - 1
    for i in range(0, last_item):
        for x in range(0, last_item - i):
            #print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]

    return mylist

print("old list: ", sortlist)
newlist = bubblesort(sortlist).copy()
print("Sorted list: ", newlist)





