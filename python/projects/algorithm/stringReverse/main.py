some = 'Привет как дела?'
massive = list(some)
print(''.join(massive[-i] for i in range(1, len(massive)+1)))
