def dicti():
    string = "abasadb"
    dict = {}
    for i in string:
        dict.setdefault(i, 0)
        if i in dict:
            dict.update({i : dict[i] + 1})
    
    dict.values()
    return dict

def mass():
	string = "abasadb"
	data, massive = [], []
	for i in string:
	    if i in massive:
	        data[massive.index(i)]+=1
	    else:
	        data.append(1)
	        massive.append(i)
	return ''.join(massive[a]+str(data[a]) for a in range(len(massive)))


<<<<<<< HEAD
print(mass())
=======
print(mass())
print(dicti())
>>>>>>> e2bde8d8e22564b0bfc80ba4e7e3f3529a882550
