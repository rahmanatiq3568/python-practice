def enqueue(a):
    val = int(input('Enter value: '))
    a.append(val)
def dequeue(a):
    if len(a) == 0:
        print('Empty queue.')
    else :
        x = a.pop(0)
        print('Dequeued item: ', x)
def peek(a):
    if len(a) == 0:
        print('Epmty queue.')
    else: 
        x = a[0]
        print('Peeked Item: ', x)
def display(a):
    if len(a) == 0:
        print('Empty queue.')
    else: 
        for i in range(len(a)):
            print(a[i])

a = []

while True:
    ch = int(input('1 -> Enqueue \n2 -> Dequeue \n3 -> Peek \n4 -> Display \n5 -> Exit \nEnter your choices: '))
    if ch == 1:
        enqueue(a)
    elif ch == 2:
        dequeue(a)
    elif ch == 3:
        peek(a)
    elif ch == 4:
        display(a)
    else:
        break
    

