from time import sleep
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '::'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    if iteration == total:
        print()
items = list(range(0, 10))
l = len(items)

for i, item in enumerate(items):
    sleep(0.1)
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
