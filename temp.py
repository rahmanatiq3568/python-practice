def push(a,val):
    a.append(val)
def popitem(a):
    item=a.pop()
    print('Popped item: ' ,item)
def peek(a):
    last=len(a)-1
    print('Peek element= ',a[last])
def display(a):
    for i in range(len(a)-1,0,-1):
        print(a[i])  
    
a = []

while True:
    choice = int(input(' 1 -> push \n 2-> pop \n 3 -> peek \n 4 -> display \n 5 -> exit \nEnter your choices: '))
    if choice == 1:
        val = int(input('Enter value to push:'))
        push(a,val)
        print('element pushed.')
    elif choice == 2:
        if len(a) == 0:
            print('Empty list.')
        else:
            popitem(a)
    elif choice == 3:
        if len(a) == 0:
            print('empty list.')
        else:
            peek(a)
    elif choice == 4:
        if len(a) == 0:
            print('Empty stack')
        else:
            display(a)
    else:
        break;
        