x = ' '.join([a for a in ''.join(a for a in input('Введите текст:\t') if a in ''.join(chr(i) for i in range(1040,1104)) or a==" ").split() if len(a)>1]).split()
print("Уникальных русских слов: " + str(len([i for i in [x[:i].count(x[i]) for i in range(len(x))] if i==0])))
