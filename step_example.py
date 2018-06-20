import pymysql
import time

import telebot
from telebot import types

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}

con = pymysql.connect(db="python", user="root", passwd="",host="localhost",port=3306,autocommit=True)
cur = con.cursor()


class User:
  def __init__(self, name):
    self.name = name
    self.age = None
    self.sex = None
    self.q27 = None

@bot.message_handler(commands=['help', 'start'])

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Siapa Nama Anda?
""")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
  try:
    chat_id = message.chat.id
    name = message.text
    user = User(name)
    user_dict[chat_id] = user
    msg = bot.reply_to(message, 'Berapakah umur anda?')
    bot.register_next_step_handler(msg, process_age_step)
  except Exception as e:
    bot.reply_to(message, 'Kesalahan name step')

def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Umur haruslah sebuah angka. Berapakah usia anda?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Pria', 'Wanita')
        msg = bot.reply_to(message, 'Apakah jenis kelamin anda?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q27_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan age step')

def process_data(message):
  try:
       chat_id = message.chat.id
       q27 = message.text
       user = user_dict[chat_id]
       user.q27 = q27

       con.execute("INSERT INTO diagnosa (sex) VALUES (user.sex)")
              
       #msg = bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex + '\n jawaban:' + user.q27 )
       #bot.register_next_step_handler(msg, send_end)
  except Exception as e:
        bot.reply_to(message, 'oooops')

def send_end(message):
        msg = bot.reply_to(message,"""Byeee""")

bot.polling()