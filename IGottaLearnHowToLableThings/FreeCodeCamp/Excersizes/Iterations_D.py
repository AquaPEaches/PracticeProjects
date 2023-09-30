Count = int() #How many things did we need to count
WhatNumber = False #To check if a specific number was in the List
Total = int() #To Check the total amount of all the numbers summed in the list

Rocket = [0, 41, 52, 13, 24, 12, 16, 26, 3]
#Data we will be counting



print("Before: ", Count)

for thing in Rocket:
    Count += 1
    Total += thing
    print(Count, thing)
    if thing == 3:
        WhatNumber = True
    

print('After:', Count, Total, WhatNumber)