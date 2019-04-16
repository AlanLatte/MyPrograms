# -*- coding: utf-8 -*-
import os,requests, re, webbrowser
from hashlib import sha1
from bs4 import BeautifulSoup

""" Change directory to current """
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))

def get_file_data(DB_filename: str, mode='r'):
    """
        types:
            data    —   tuple
            index   —   int
    """
    with open(DB_filename, mode) as raw_data:

        data = raw_data.read().split('\n')
        index = data.index('')

        if '' in data:  del data[index];\
                        return tuple(data)
        else:           return tuple(data)

def parser(urls: tuple, headers: dict):
    """
        types:
            url             —   str
            index           —   int
            headers         —   dict
            error_message   —   str
            result          —   str
            title           —   str
            series          —   str

        information:
            index for notify the user of any error
    """
    result = str()


    """Start logic of parser"""

    for index, url in enumerate(urls,1):
        request = requests.get(url, headers=headers)
        error_message = f'The {index} url was broken'
        if request.status_code == 200:

            soup = BeautifulSoup(request.content, 'html.parser')

            if re.search(r'www.anilibria.tv', url):

                title = soup.find(name='img', attrs={'id': 'adminPoster'}).get('alt')
                try:
                    series = re.search(r'(?<=((С|c)ерия 1-)).*(?= \[)', soup.text).group()
                except AttributeError:
                    series = re.search(r'(\d).*(?= \[)', soup.text).group()
                result+= f'{index} > {title} [{series}] <\n'

            elif re.search(r'anime.anidub.com', url):

                title = soup.find(name='h1', attrs={'class': 'titlfull'}).renderContents().decode('utf-8')
                result+= f'{index} > {title} <\n'

            else:

                data = error_message
                result+= f'{index} > {data} <\n'
        else:
            return error_message
    return result

class Record:
    def clear_data(file:str, mode='w', ):
        with open(file, mode) as result:
            result.write
    def append_result(file:str, data:str, mode='a'):
        with open(file, mode, encoding='utf-8') as result:
            result.write(f'{data}')

def check_data(data, DB_result, url):
    """
        types:
            old_data    —   tuple
            new_data    —   tuple
            result      —   list
            index       —   int
    """
    old_data = get_file_data(DB_filename = DB_result, mode='r')
    Record.clear_data(file=DB_result, mode='w')
    Record.append_result(file=DB_result, data=data, mode='a')
    new_data = get_file_data(DB_filename = DB_result, mode='r')
    if old_data != new_data:
        result=list(set(new_data) - set(old_data))
        for i in range(len(result)):
            index = result[i][0]
            print(f'New series of {result[i]} available.')
            webbrowser.open(str(url[int(index)-1]))
    else:
        print('New series didn`t come out :c')

if __name__ == '__main__':
    """
        types:
            DB_urls     —   str
            DB_result   —   str
            urls        —   tuple
            headers     —   dict
            data        —   str
            LISTDIR     —   tuple

        information:
            DB          —   Data Base
    """

    DB_urls     =   'urls.txt'
    DB_result   =   'result.txt'
    LISTDIR = tuple(os.listdir())
    headers =   {
                    'accept'     : '*/*',
                    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
                }
    """ Check for files """
    # REVIEW: Доделать систему switch-case
    if DB_result not in LISTDIR:
        Record.clear_data(file=DB_result, mode='w')
    if DB_urls not in LISTDIR:
        Record.clear_data(file=DB_urls, mode='w')

    urls = get_file_data(DB_filename = DB_urls, mode='r')

    if urls:
        data = parser(urls, headers)
        check_data(data, DB_result, url=urls)
    else:
        print(f'Paste in {DB_urls} any urls')
