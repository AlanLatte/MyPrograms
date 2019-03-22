import requests, re, datetime
def get_data(cookies, headers, url):
    data = requests.post(url, cookies=cookies, headers=headers)
    try:
        mass = ['ДцАТБ 3-1', 'ДцИС', 'ДтМОБ']
        for i in mass:
            if re.search(f'{i.lower()}', data.text):
                print(i)

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
