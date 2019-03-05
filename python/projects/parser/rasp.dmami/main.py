import requests, re, datetime
def get_data(cookies, headers, url):
    data = requests.post(url, cookies=cookies, headers=headers)
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    time =  {
            '1' : '9:00-10:30' ,
            '2' : '10:40-12:10',
            '3' : '12:20-13:50',
            '4' : '14:30-10:00',
            '5' : '16:10-17:40',
            '6' : '17:50-19:20',
            '7' : '19:20-20:50'
            }
    today = datetime.datetime.today().weekday()+1
    try:
        grid = data.json()['grid']
        print(days[today-1])
        print('============\n')
        for pair in range(1, 7):
            pairs = grid[str(today)][str(pair)]
            if len(pairs) > 0:
                print(time[str(pair)])
                print(pairs[0]['subject'])
                print(pairs[0]['teacher'])
                auditories = pairs[0]['auditories']
                print(','.join(auditories[i]['title'] for i in range(len(auditories))))
                print()
    except ValueError:
        cookies_correct = re.search(r'bpc=\w+', data.text).group().split('=')[-1]
        main(bpc=cookies_correct)

def main(bpc='89a0ada592fc339f7847813f87c3199b', group = '181-362'):
    get_data(   cookies = {'bpc': bpc, 'group': group},\
                headers = {'referer': 'https://rasp.dmami.ru/' },\
                url = f'https://rasp.dmami.ru/site/group?group={group}&session=0'\
            )

if __name__ == '__main__':
    main()
