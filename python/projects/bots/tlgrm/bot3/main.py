<<<<<<< HEAD
import telebot
from flask import Flask, request
from flask_sslify import SSLify

token = '619356941:AAEAO9Bj_yveS5LKs8L2lBcMFL6d28eBbxs'
url = 'https://testuser123123.pythonanywhere.com'
bot = telebot.TeleBot(token)
bot.remove_webhook()
bot.set_webhook(url=url)

app = Flask(__name__)
sslify = SSLify(app=app)
@app.route('/', methods=['POST'])
def webhook():
    updates = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([updates])
    return 'ok', 200

@bot.message_handler(command=['start'])
def start(message):
    bot.send_message(message.chat.id, text='hello!')
=======
import telebot
from flask import Flask, request
from flask_sslify import SSLify

token = '619356941:AAEAO9Bj_yveS5LKs8L2lBcMFL6d28eBbxs'
url = 'https://testuser123123.pythonanywhere.com'
bot = telebot.TeleBot(token)
bot.remove_webhook()
bot.set_webhook(url=url)

app = Flask(__name__)
sslify = SSLify(app=app)
@app.route('/', methods=['POST'])
def webhook():
    updates = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([updates])
    return 'ok', 200

@bot.message_handler(command=['start'])
def start(message):
    bot.send_message(message.chat.id, text='hello!')
>>>>>>> Some error have exists
