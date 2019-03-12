import requests,re, os, webbrowser
from bs4 import BeautifulSoup as bs
def parse_anidub(url, index):
    with requests.Session() as session:
        try:
            request = session.get(url)
            if request.status_code == 200:
                soup = bs(request.content,'html.parser')
                divs = soup.find_all('div', attrs={'title'})
                data = re.search(r'>(.*)<', str(divs)).group()
                data_write(data=f'{index}'+data)
            else:
                print('Server fall')
        except:
            text = 'line '+str(index)+' in urls.txt was broken'
            data_write(data=f'{index}'+text)
            print(text)


def open_url(url, index):
    try:
        webbrowser.open(str(url))
    except:
        print('An error occurred while opening the link url')

def data_check():
    BEFORE = clean_data(get_result())
    result_clear()
    site_detect(url=clean_data(get_urls()))
    AFTER = clean_data(get_result())
    if BEFORE != AFTER:
        result=list(set(AFTER) - set(BEFORE))
        print(result)
    else:
        print('New series did not come out')

def data_write(data):
    with open('result.txt', mode='a', encoding='utf=8') as result:
        result.write(data+'\n')

def site_detect(url):
    for i in url:
        index = url.index(i)
        if re.search(r'www.anilibria', i):
            print('Please paste only Anidub url')
        else:
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
    data_check()

if __name__ == '__main__':
    main()
