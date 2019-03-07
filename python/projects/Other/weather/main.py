import requests, datetime
def weather(URL,time,api_key,city):
    url = URL+time+api_key+city; time = requests.get(url).json()['dt']
    print(datetime.datetime.now().strftime('%H:%M:%S\n----------'))
    print(requests.get(url).json()['weather'][0]['main'])
    data = lambda clas, name: requests.get(url).json()[clas][name]
    temp = data('main', 'temp'); humidity = data('main', 'humidity')
    print("Temp: {0:.2f}".format(temp- 273,15)+u"\u00B0"+'C\n'+'humidity: '+str(humidity)+"%")

weather(URL     = 'http://api.openweathermap.org/data/2.5/'                     ,\
        time    = 'weather'                                                     ,\
        api_key = '?appid='        +    '549ca41931ed23380bcccacbf85794fd'      ,\
        city    = '&q='            +                   'Moscow'                 )
