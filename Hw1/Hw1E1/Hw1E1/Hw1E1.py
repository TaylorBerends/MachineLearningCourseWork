import numpy as np

lockers = np.zeros(100) #create array of 100 closed lockers (0 = closed, 1 = open)

for sn in range(1,101): #sn = sstrudent number, loop through 1 to 100 for student numbers
    i = sn - 1 #begining index is student number minus one as arrays are zero indexed
    while(i < 100): #while index is less than 100
        if(lockers[i] == 0):
            lockers[i] = 1; #open locker
        elif(lockers[i] == 1):
            lockers[i] = 0; #close locker
        i = i+(sn) #increase index by student number then repeat loop
    

print(lockers)

openLockers = list()
for i in range(100):
    if(lockers[i] == 1):
        openLockers.append(i+1)

print("\nOpen Lockers:")
print(openLockers)