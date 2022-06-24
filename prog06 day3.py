#celcius to fahrenhiet
celcius = float(input('Enter tempereture in celcius:'))
fahrenhiet = celcius*9/5+32
print('Temperature in fahrenhiet', fahrenhiet)

print('-----------')

def get_sum(nums):
   sum = 0
   for num in nums:
       sum = sum + num
   return sum

nums = [13,89,65,42,12,11,56]
 
total = get_sum(nums)
print("The total of each elements:",total)

print('-----------')

#check prime number
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            print(num,'is not a prime number')
            break
    else:
        print(num, 'is a prime number')
is_prime(19)

#binary to decimal
def num(decimal):
    if decimal==0:
        return
    else:
        num(int(decimal/2))
        print(decimal%2, end='')
num(10)
print('-----------')

#random number
from ast import NotIn
import random
random_num = random.randint(0,10)
print(random_num)

#remove duplicate
list1 = [1,2,2,3,4,5,6,5,7,7,8,9]
list2 = []
for x in list1:
    if x not in list2:
        list2.append(x)

print(list2)

print('----------')

data = [10,20,30,20,30,40,50,50,60,70,80,90,90,100]


def remove_duplicates(duplist):
    list4 = []
    for element in duplist:
        if element not in list4:
            list4.append(element)
    return list4
print(remove_duplicates(data))

print('----------')

data2 = [1,2,3,3,4,5,5,6,3,6,7,8,9,9]

def remove_duplicates2(duplist2):
    noduplist2 = []

    for z in duplist2:
        if z not in noduplist2:
            noduplist2.append(z)
    return noduplist2

print(remove_duplicates2(data2))
