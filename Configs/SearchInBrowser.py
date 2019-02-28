import webbrowser
try:    webbrowser.open("https://google.com/search?q={}".format(''.join(a.replace(" ","+") for a in input('Google:\t'))))
except: print('some error is exists.')
