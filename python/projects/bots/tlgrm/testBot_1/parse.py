import requests
from main import write_json
import re
def get_price(crypto):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format(crypto)
    r = requests.get(url).json()
    price = r[-1]["price_usd"]
    # write_json(r.json(), filename = 'data.json')
    return price

def parce_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto[1:]
def main():
    print(get_price(parce_text('/bitcoin')))

if __name__ == '__main__':
    main()
