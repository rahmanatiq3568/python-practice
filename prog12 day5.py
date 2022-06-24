#stack practice, next Queue #LIFO (last in first out)
def push(a,val):
    a.append(val)
def popitem(a):
    a.pop()
def peek(a):
    last=len(a) -1
    print('Peeked element: ', a[last])
def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])

a = []
while True:
    choice = int(input('enter 1 to push \nenter 2 to pop \nenter 3 to peek \nenter 4 to display \nenter 5 to exit \nEnter our choice: ' ))

    if choice == 1:
        val = int(input('Enter value to push: '))
        push(a,val)
        print('Value pushed.')
    elif choice == 2:
        if len(a) == 0:
            print('empty stack.')
        else:
            popitem(a)
    elif choice == 3:
        if len(a) == 0:
            print('empty stack.')
        else:
            peek(a)
    elif choice == 4:
        if len(a) == 0:
            print('empty stack.')
        else:
            display(a)
    else:
        break;
