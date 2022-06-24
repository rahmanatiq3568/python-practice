#function of list

#1
subject = ['Bullet echo','Carrom', 'Golf', 'Battle royale']
print(len(subject))
#2
subject.append("PUBG")
print(subject)
#3
subject.insert(4,"freefire")
print(subject)
#4
subject.remove("Carrom")
print(subject)
#5
subject.sort()
print(subject)
#6
subject.reverse()
print(subject)
#7
subject.pop()
subject.pop()
print(subject)
#8
subject2 = subject.copy()
print(subject2)
#9
pos = subject.index("Golf")
print(pos)
#10
subject = ['Bullet echo','Carrom', 'Golf', 'Golf', 'Golf', 'Battle royale']
pos = subject.count("Golf")
print(pos)
#11
subject.clear()
print(subject)

#range function
num = list(range(15))
print(num)

num = list(range(6,20))
print(num)

num = list(range(0,100,2))    #to show even num
print(num)

num = list(range(1,100,2))    #to show odd num
print(num)

