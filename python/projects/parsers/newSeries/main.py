import requests,re, os, webbrowser
from bs4 import BeautifulSoup as bs
def parse_anidub(url, index):
    with requests.Session() as session:
        request = session.get(url)
        if request.status_code == 200:
            soup = bs(request.content,'html.parser')
            divs = soup.find_all('div', attrs={'title'})
            data = re.search(r'>(.*)<', str(divs)).group()
            data_write(data=f'{index}'+data)
        elif request.status_code == 404:
            text = 'line '+str(index)+' in urls.txt was broken'
            data_write(data=f'{index}>'+text)
            print(text)
        else:
            print('Server fall')

def data_check(BEFORE, AFTER, url):
    if BEFORE != AFTER:
        result=list(set(AFTER) - set(BEFORE))
        for i in range(len(result)):
            index = re.search('^\d+', result[i], flags=0).group()
            webbrowser.open(str(url[int(index)-1]))
    else:
        print('New series did not come out')

def data_write(data):
    with open('result.txt', mode='a', encoding='utf=8') as result:
        result.write(data+'\n')

def site_detect(url):
    for i in url:
        index = url.index(i)
        if re.search(r'anilibria', i):
            print('Please paste only Anidub url')
        elif re.search(r'anime.anidub', i):
            parse_anidub(url=i, index=index+1)

def change_dir():
    os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))

def result_clear():
    with open('result.txt', mode='w') as clean:
        clean.write

def get_result():
    with open('result.txt', mode='r') as data:
        return data.read().split('\n')

def get_urls():
    with open('urls.txt', mode='r') as data:
        return data.read().split('\n')

def clean_data(url):
    index = url.index('')
    if index:
        del url[index]
    return url

def main():
    change_dir()
    BEFORE = clean_data(get_result())
    result_clear()
    urls = clean_data(get_urls())
    site_detect(url=urls)
    AFTER = clean_data(get_result())
    data_check(BEFORE, AFTER, url=urls)

if __name__ == '__main__':
    main()
