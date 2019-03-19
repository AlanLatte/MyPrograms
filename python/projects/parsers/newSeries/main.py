import requests,re, os, webbrowser
from bs4 import BeautifulSoup as bs
from time import sleep

def parse_anidub(url, index):
    pattern = r'>(.*)<'
    tag = 'div'
    attr = {'title'}
    data = parser(url, index, pattern, tag, attr)
    data_write(data=f'{index}'+data)

def parse_anilibria(url, index):
    def get_series():
        pattern = r'(С|с)ерия \d-\d+'
        tag = 'td'
        attr = {'class':'torrentcol1'}
        return parser(url, index, pattern, tag, attr)
    def get_name():
        pattern = r'(>\s.*\s+<)'
        tag = 'h1'
        attr = {'class':'release-title'}
        data = parser(url, index, pattern, tag, attr)
        pattern = r'[^\t\n><]'
        matches = re.finditer(pattern, data)
        return ''.join(match.group() for matchNum, match in enumerate(matches))
    data_series = get_series().split(' ')[1].split('-')[1]
    data_name = get_name()
    data_write(data=f'{index}'+'> '+data_name+' ['+data_series+']<')

def parser( url,
            index,
            pattern,
            tag,
            attr):
    with requests.Session() as session:
        request = session.get(url)
        if request.status_code == 200:
            soup = bs(request.content,'html.parser')
            divs = soup.find_all(tag, attrs=attr)
            data = re.search(pattern, str(divs)).group()
        elif request.status_code == 404:
            text = 'line '+str(index)+'in urls.txt was broken'
            data_write(data=f'{index}>'+text)
            print(text)
        else:
            print('Server fall')
        return data

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
    items = list(range(0, 100))
    l = len(items)
    for i in url:
        for q, item in enumerate(items):
            printProgressBar(q + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 25)
            index = url.index(i)
        if re.search(r'anilibria', i):
            parse_anilibria(url=i, index=index+1)
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

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '#'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + ':' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    if iteration == total:
        print()
if __name__ == '__main__':
    print('Loading...')
    main()
    print('Done!')
    sleep(3)
