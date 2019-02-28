<<<<<<< HEAD
def dicti():
    string = "abasadb"
    dict = {}
    for i in string:
        dict.setdefault(i, 0)
        if i in dict:
            dict.update({i : dict[i] + 1})
    return dict
print(dicti())
def mass():
	string = "aaffafasdas"
	data, massive = [], []
	for i in string:
	    if i in massive:
	        data[massive.index(i)]+=1
	    else:
	        data.append(1)
	        massive.append(i)
	print(massive)
	print(data)
=======
def dicti():
    string = "abasadb"
    dict = {}
    for i in string:
        dict.setdefault(i, 0)
        if i in dict:
            dict.update({i : dict[i] + 1})
    return dict
print(dicti())
def mass():
	string = "aaffafasdas"
	data, massive = [], []
	for i in string:
	    if i in massive:
	        data[massive.index(i)]+=1
	    else:
	        data.append(1)
	        massive.append(i)
	print(massive)
	print(data)
>>>>>>> Some error have exists
print(mass)