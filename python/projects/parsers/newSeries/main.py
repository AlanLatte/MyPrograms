import requests,re, os
from bs4 import BeautifulSoup as bs
def parse_anidub(url, index):
    with requests.Session() as session:
        try:
            request = session.get(url)
            if request.status_code == 200:
                soup = bs(request.content,'html.parser')
                divs = soup.find_all('div', attrs={'title'})
                data = re.search(r'>(.*)<', str(divs)).group()
                text_write(data=data)
            else:
                print('Server fall')
        except None:
            text = 'line '+str(index+1)+' in urls.txt was broken'
            text_write(data=text)
            print(text)
# nextserial
# def parse_anilibria(url,index):
#     with requests.Session() as session:
#
#         try:
#             request = session.get(url)
#             if request.status_code == 200:
#                 soup = bs(request.content,'html.parser')
#                 regular = lambda string: re.search(r'>(.*)<', str(string), re.DOTALL).group()
#                 divs = soup.find_all('div', attrs={'detail_torrent_side'})
#                 name = soup.find_all('img', class_='detail_torrent_pic', id='adminPoster')
#                 text_write(regular(string=divs)+'--'+regular(string=name))
#             else:
#                 print('Server fall')
#         except:
#             text = 'line '+str(index+1)+' in urls.txt was broken'
#             text_write(data=text)
#             print(text)

def text_write(data):
    with open('result.txt', mode='a', encoding='utf=8') as result:
        result.write(data+'\n')

def site_detect(url):
    clean_data(url)
    for i in url:
        index = url.index(i)
        if re.search(r'www.anilibria', i):
            # parse_anilibria(url=i, index=index)
            print('Please paste only Anidub url')
        else:
            parse_anidub(url=i, index=index)

def change_dir():
    os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))

def text_data():
    with open('result.txt', mode='w') as clean:
        clean.write
    with open('urls.txt', mode='r') as data:
        return data.read().split('\n')

def clean_data(url):
    index = url.index('')
    if index:
        del url[index]
    return url
def main():
    change_dir()
    site_detect(url=text_data())


if __name__ == '__main__':
    main()
