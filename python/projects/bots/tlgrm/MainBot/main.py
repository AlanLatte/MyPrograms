import telebot, requests, api_token, datetime, re
from flask import Flask, request
from telebot import types
token = token.token
url = 'https://470e108e.ngrok.io'

app = Flask(__name__)
bot = telebot.TeleBot(token, threaded=True, skip_pending=False, num_threads=2)
bot.remove_webhook()
bot.set_webhook(url)

@app.route('/', methods=['POST'])
def webhook():
    updates = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([updates])
    return 'ok', 200

@bot.message_handler(commands=['start'])
def start(message):
    message_text=   "Hello,\nIt`s my test bot!\nCreated By: @Alanlatte\n"+\
                    "For more content /list"
    bot.send_message(message.chat.id, text=message_text)
    list(message)
@bot.message_handler(commands=['list'])
def list(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_rasp = types.KeyboardButton(text="/rasp")
    button_group = types.KeyboardButton(text="/group")
    button_where_i_am = types.KeyboardButton(text="/whereIAm")
    button_weather = types.KeyboardButton(text="/weather")
    keyboard.add(button_rasp, button_group, button_where_i_am, button_weather)
    bot.send_message(message.chat.id, text='List Commands',reply_markup=keyboard)

@bot.message_handler(commands=['group'])
def group(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button0 = types.InlineKeyboardButton(text="181-362", url="https://vk.com/polytech181362")
    url_button1 = types.InlineKeyboardButton(text="Поликек", url="https://vk.com/lowpolykek")
    url_button2 = types.InlineKeyboardButton(text="Подслушанно", url="https://vk.com/mpu_overhear")
    keyboard.add(url_button0, url_button1, url_button2)
    bot.send_message(message.chat.id, "Группы", reply_markup=keyboard)

@bot.message_handler(commands=['rasp'])
def rasp(message):
    def get_data(cookies, headers, url):
        data = requests.post(url, cookies=cookies, headers=headers)
        days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
        time =  {
                '1' : '9:00-10:30' ,
                '2' : '10:40-12:10',
                '3' : '12:20-13:50',
                '4' : '14:30-10:00',
                '5' : '16:10-17:40',
                '6' : '17:50-19:20',
                '7' : '19:20-20:50'
                }
        today = datetime.datetime.today().weekday()+1
        try:
            grid = data.json()['grid']
            print(days[today-1])
            print('============\n')
            for pair in range(1, 7):
                pairs = grid[str(today)][str(pair)]
                if len(pairs) > 0:
                    print(time[str(pair)])
                    print(pairs[0]['subject'])
                    print(pairs[0]['teacher'])
                    auditories = pairs[0]['auditories']
                    print(','.join(auditories[i]['title'] for i in range(len(auditories))))
                    print()
        except ValueError:
            cookies_correct = re.search(r'bpc=\w+', data.text).group().split('=')[-1]
            main(bpc=cookies_correct)

    def main(bpc='89a0ada592fc339f7847813f87c3199b', group='181-362'):
        get_data(   cookies = {'bpc': bpc, 'group': group},\
                    headers = {'referer': 'https://rasp.dmami.ru/' },\
                    url = 'https://rasp.dmami.ru/site/group?group=181-362&session=0'\
                )
    bot.send_message(message.chat.id, main())

@bot.message_handler(commands=["whereIAm"])
def geophone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Поделись местоположением", reply_markup=keyboard)

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):
    bot.send_message(message.chat.id, text='Я понимаю только текст.')

@bot.message_handler(commands=['weather'])
def weather(message):
	url = 'http://api.openweathermap.org/data/2.5/weather?appid='+'549ca41931ed23380bcccacbf85794fd'+'&q={}'.format('Moscow')
	clss = requests.get(url).json()['weather'][0]['main']
	data = lambda clas, name: requests.get(url).json()[clas][name]
	temp = data('main', 'temp'); humidity = data('main', 'humidity')
	result_data = "Temp:\t{0:.2f}".format(temp- 273,15)+u"\u00B0"+'C\n'+'humidity:\t'+str(humidity)+"%"
	bot.send_message(message.chat.id, text = clss+"\n"+result_data)

@bot.edited_message_handler(content_types=['text'])
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, text='check command in /list')


if __name__ == '__main__':
    app.run()
