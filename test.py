a =   		[
                ['ПеРрова', 'И.С', ['555','44','76']],
                ['Перова', 'С.С', ['555','44','77']],
                ['Петрова', 'И.С', ['555','44','77']],
                ['ПетDова', 'И.С', ['555','44','74']]
            ]
while len(a)>0:
	i = 1
	q = 0
	while i-1<len(a[-1][-1])-1:
		if a[-1][0]==[-1][-1][i]:
			q=2
			print(a[i])
			del a[i]
			i-=1
		i+=1	
	if q == 2:
		print(a[0])
	del a[0]

print(a[-1][-1][-1])
