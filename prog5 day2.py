#function
def simplefunction():
    print("Hello World")
    a,b = 5,6 
    sum = a + b
    print(sum)
simplefunction() 
print('--------')   

#with parameter
def math(num1, num2, num3):
    sum= num1+num2+num3
    print(sum)
math(3,5, 5)
math(4,5,5)
print('--------')      

#default parameter
def math2(num1, num2 = 5):
    print(num1,' ',num2)
math2(5)

def wishcard(name, wish = 'Happy Birthday to:'):
    print(wish, name)

wishcard('Kamal')

def wishcard(name, wish = 'Happy Birthday to:'):
    print(wish, name)

wishcard('Happy friendship day','Kamal')
print('--------')   

var = 10 
def math3():
    loc = var
    loc = loc + 1
    print(loc)
math3()
print('--------')   

#xargs
def add(*details):
    print(details)
add(102,'kamal','general')
print('--------')   

def math4(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
        print(sum)
math4(30+40)
math4(30+40+50)
math4(30+40+40+100)

print('--------')

#xxargs
def student(**details):
    print(details)
student(id=102, name='Anis')

