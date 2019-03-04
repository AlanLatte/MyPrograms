# massive =  	[
#                 ['ПеРрова', 'И.С', ['555','44','76']],
#                 ['Перова', 'С.С', ['555','44','77']],
#                 ['Петрова', 'И.С', ['555','44','77']],
#                 ['Петрова', 'И.С', ['555','44','77']],
#                 ['ПетDова', 'И.С', ['555','44','74']]
#             ]


masssive = ['a','b','a','a','c','c']

for i in range(len(masssive)):
    for q in range(len(masssive)):
        if masssive[i] == masssive[q]:
            print(masssive[q])
    del masssive[q]
