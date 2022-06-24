#queue practice #FIFO (first in first out)
def enqueue(a):
    val = int(input('Enter number to enqueue: '))
    a.append(val)
def dequeue(a):
    if len(a) == 0:
        print('Empty queue.')
    else:
        x = a.pop(0)
        print('Dequeued Item: ', x)
def peek(a):
    if len(a) == 0:
        print('Empty queue.')
    else: 
        x = a[0]
        print('Peek item: ', x)
def display(a):
    if len(a) == 0:
        print('Empty queue.')
    else:
        for i in range(len(a)):
            print(a[i])

a = []

while True:
    ch = int(input("1 -> Enqueue \n2 -> Dequeue \n3 -> Peek \n4 -> Display \n5 -> Exit \nEnter your choice: "))
    if ch == 1:
        enqueue(a)
    if ch == 2:
        dequeue(a)
    if ch == 3:
        peek(a)
    if ch == 4:
        display(a)
    if ch == 5:
        break
    