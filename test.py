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
