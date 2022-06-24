# a = float(input('Enter first value: '))
# b = float(input('Enter second value: '))
a = 9
b = 2

math = a/b
print('division =', math)
math = a%b
print('modulus =',math)
math = a//b
print('floor =', math)
math = a**b
print('exponential =', math)

print('-----------------')
#reverse number
i = int(input('Give value: '))
rev = 0
while i > 0:
    rev = (rev * 10) + i % 10
    i = i // 10
print('reverse:', rev)

#reverse string #slicing method
a = input('Enter a word: ')     #.....-3,-2,-1
print(a[-1::-1])                #start,stop,step


#using for loop # understood slightly
z = 'Bangladesh'
w = ''
for char in z:
    w = char + w
print(w)


#using reversed() function
str = input('enter text: ')

reversed_str = reversed(str)
print(''.join(reversed_str))



#for loop #don't understood
b = input('Enter string: ')
for i in range((len(b)-1),-1,-1):
    print(b[i], end='')


