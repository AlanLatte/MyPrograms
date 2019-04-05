import requests, re, datetime, json, os
import hashlib
# from time import sleep
from urllib.parse import quote

def get_bpc(cookies, headers, url):
    data = requests.post(url, cookies=cookies, headers=headers)
    bpc = re.search(r'(?<=bpc=).*(?=\;P)', data.text).group()
    return bpc

def main(bpc='1', group=quote('181-362')):
    cookies = {'bpc': bpc, 'group': group}
    headers = {'referer': 'https://rasp.dmami.ru/' }
    url = f'https://rasp.dmami.ru/site/group?group={group}&session=0'
    cookies['bpc']=get_bpc(cookies, headers, url)
    get_data(cookies, headers, url)

def get_data(cookies, headers, url):
    data = requests.post(url, cookies=cookies, headers=headers)
    check_data(data)
    # file_respone(mode='w', text=data.json())

def check_data(data):
    # hash_of_data = hashlib.sha1(file_respone(name='out.json', mode='r', text=None)).hexdigest()
    # hash_of_file = hashlib.sha1(data.text.encode()).hexdigest()
    # print(hash_of_data+'\n'+hash_of_file)
    file_respone(name='out.json', mode='r', text=None)

def file_respone(name='out.json', mode='r', text=None):
    with open(file=name, mode=mode, encoding='utf-8') as file:
        if mode=='r':
            return file.read().encode()
        elif mode=='w':
            json.dump(text, file, ensure_ascii=False, indent=2)

def change_dir():
    os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))

if __name__ == '__main__':
    change_dir()
    main()
    # sleep(3)
