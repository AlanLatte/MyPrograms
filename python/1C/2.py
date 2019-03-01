string = 'Петрова И.С 555-44-77'
massive =   [
                ['ПеРрова', 'И.С', ['555','44','76']],
                ['Перова', 'С.С', ['555','44','77']],
                ['Петрова', 'И.С', ['555','44','77']]
            ]

correct = []
for i in range(len(massive)):
    correct.append(massive[i][-1][-1])
print(correct)
d = []
for i in correct:
    d.append(correct.index(i))
    if d > 1:
        for q in range(2):
            print(massive[lol])
