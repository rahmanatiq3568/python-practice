data = [10,20,30,20,30,40,50,50,60,70,80,90,90,100]
def remove_duplicates(duplist):
	noduplist = []
	
	for element in duplist:
		if element not in noduplist:
			noduplist.append(element)	
	return noduplist
			
print(remove_duplicates(data))

print('------')


data2 = [10,20,30,20,30,40,50,50,60,70,80,90,90,100]


def remove_duplicates(duplist):
    list4 = []
    for element in duplist:
        if element not in list4:
            list4.append(element)
    return list4
print(remove_duplicates(data2))

print('------')

data3 = [10,20,30,20,30,40,50,50,60,70,80,90,90,100]

def remove_duplicates(duplist):
	noduplist = []
	for element in duplist:
		if element not in noduplist:
			noduplist.append(element)	
	return noduplist
print(remove_duplicates(data3))


