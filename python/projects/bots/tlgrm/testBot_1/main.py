from flask import Flask
from flask import request
from flask import jsonify
import api_token, requests, json, re
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)
def main_URL(command='getMe'):
    URL = 'https://api.telegram.org/bot' + api_data.token + command
    return URL


def send_message(chat_id, text='bla-bla'):
    url = main_URL(command='sendMessage')
    answer =    {
                'chat_id':chat_id,
                'text':text
                }
    return requests.post(url, data=None, json=answer).json()

@app.route('/747145208:AAEDNuN3O83inPPLgjdpRT3VIw4lBAUQL8I', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        req_json = request.get_json()
        chat_id = req_json['message']['chat']['id']
        message_text = req_json['message']['text']
        if re.search(r'/\w+',message_text):
            price = get_price(parce_text(message_text))
            send_message(chat_id, text=price)
        else:
            send_message(chat_id, text='Вот что я умею:\
                                        \
                                        \
                                        Курс относительно $ криптовалюты. (нр:/crypto)\
                                        Расписание для 181-362 группы (в процессе)')
        return jsonify(req_json)
    return '<h1>Hello</h1>'

def get_price(crypto):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format(crypto)
    r = requests.get(url).json()
    price = r[-1]["price_usd"]
    return price

def parce_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto[1:]

def write_json(data, filename = 'data.json'):
    with open(filename, mode='w') as json_data:
        json.dump(data,json_data,indent=2, ensure_ascii=False)

def main():
    get_update = requests.get(main_URL(command='getUpdates')).json()
    chat_id = get_update['result'][-1]['message']['chat']['id']
    send_message(chat_id, text='bla-bla')


if __name__ == '__main__':
    # main()
    app.run()
