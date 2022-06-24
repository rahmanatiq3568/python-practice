#tuple practise
#tuple is like list, but unchangeble
#Tuple take less memory than List

cars = ("Ford", "Mercedes", "Audi")
print(cars)
print(len(cars))

mycars = list(cars)         #tuple changed to list
print(mycars)
mycars[0] = 'Toyota'

myNewcars = tuple(mycars)   #list changed to tuple
print(myNewcars)
print(len(myNewcars[0]))

import sys
carsT = ("Ford", "Mercedes", "Audi")
carsL = ["Ford", "Mercedes", "Audi"]
carsD = {"Ford", "Mercedes", "Audi"}
print("Size of Tuple: ",sys.getsizeof(carsT))  
print("Size of List: ",sys.getsizeof(carsL))
print("Size of Dictionary: ",sys.getsizeof(carsD))  

del mycars                  #to delete list/tuple

