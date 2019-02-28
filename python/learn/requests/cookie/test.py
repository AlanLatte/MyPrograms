<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
url = 'https://rasp.dmami.ru/site/group?group=181-362&session=0'
cookies = {
    'bpc' : '89a0ada592fc339f7847813f87c3199b'
    }
r = requests.get(url, cookies=cookies)
print(r)
print(r.text)
=======
import requests
from bs4 import BeautifulSoup
url = 'https://rasp.dmami.ru/site/group?group=181-362&session=0'
cookies = {
    'bpc' : '89a0ada592fc339f7847813f87c3199b'
    }
r = requests.get(url, cookies=cookies)
print(r)
print(r.text)
>>>>>>> Some error have exists
