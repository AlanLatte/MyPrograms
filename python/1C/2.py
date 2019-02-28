<<<<<<< HEAD
massive = [['Иванов', 'П.С.', '555-66-77'], ['Иванов', 'П.С.', '555-66-76'], ['Иванов', 'П.F.','555-66-77'],['Иванов', 'П.F.','555-66-76'], ['Иванов', 'П.F.','555-66-36']]
number = []
for i in range(len(massive)):
    number.append(massive[i][2].split('-')[-1])

find = []

for i in range(len(number)):
    ind = number.index(number[i])
    find.append(ind)
print(find)
#
# for i in range(len(find)):
=======
massive = [['Иванов', 'П.С.', '555-66-77'], ['Иванов', 'П.С.', '555-66-76'], ['Иванов', 'П.F.','555-66-77'],['Иванов', 'П.F.','555-66-76'], ['Иванов', 'П.F.','555-66-36']]
number = []
for i in range(len(massive)):
    number.append(massive[i][2].split('-')[-1])

find = []

for i in range(len(number)):
    ind = number.index(number[i])
    find.append(ind)
print(find)
#
# for i in range(len(find)):
>>>>>>> Some error have exists
