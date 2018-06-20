import time

import pdb
import pymysql
import pymysql.cursors
import telebot
from telebot import types

API_TOKEN = '413035429:AAHAsUnIE08sMQucXrsYYsX7AwNlGxsrtjw'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}
con = pymysql.connect(db="python", user="root", passwd="",host="localhost",port=3306,autocommit=True)

class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None
        self.q1= None
        self.q2= None
        self.q3= None
        self.q4= None
        self.q5= None
        self.q6= None
        self.q7= None
        self.q8= None
        self.q9= None
        self.q10= None
        self.q11= None
        self.q12= None
        self.q13= None
        self.q14= None
        self.q15= None
        self.q16= None
        self.q17= None
        self.q18= None
        self.q19= None
        self.q20= None
        self.q21= None
        self.q22= None
        self.q22= None
        self.q23= None
        self.q24= None
        self.q25= None
        self.q26= None
        self.q27= None
        self.qlanjut= None


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Selamat datang, Saya adalah bot Diagnosa Awal Penyakit Ginjal.
Silahkan menjayab semua poin pertanyaan berikut dengan yakin. Jawablah denga menekan jawaban yang disediakan.

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
        bot.register_next_step_handler(msg, process_q1_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan age step')

def process_q1_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        user.sex = sex
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, 'Apakah anda demam tinggi dan menggigil?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q2_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q1 step')


def process_q2_step(message):
    try:
        chat_id = message.chat.id
        q1 = message.text
        user = user_dict[chat_id]
        user.q1 = q1
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, 'Apakah anda merasa nyeri pada pinggang sisi belakang atau samping satu atau kedua sisi?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q27_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q2 step')

def process_q27_step(message):
    try:
        chat_id = message.chat.id
        q26 = message.text
        user = user_dict[chat_id]
        user.q26 = q26
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, 'Apakah anda sering mengalami penurunan kesadaran hingga tidak sadarkan diri?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_diagnosa)
    except Exception as e:
        bot.reply_to(message, 'oooops q27 step')


def process_diagnosa(message):
    try:
        chat_id = message.chat.id
        q27 = message.text
        user = user_dict[chat_id]
        user.q27 = q27
        bot.send_message(chat_id, 'Halo ' + user.name + '\n Umur:' + str(user.age) + '\n Jenis kelamin:' + user.sex )
        bot.send_message(chat_id, '\n Diagnosa penyakit : ' + user.q1 )
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, 'Ingin melakukan diagnosa lebih lanjut dengan dokter?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_lanjut)
    except Exception as e:
        bot.reply_to(message, 'oooops sex step')


def process_lanjut(message):
    try:
        chat_id = message.chat.id
        qlanjut = message.text
        user = user_dict[chat_id]
        user.qlanjut=qlanjut

        with con.cursor() as cursor:
            sql = "INSERT INTO diagnosa(sex) VALUES('" + user.sex + "')"
            cursor.execute(sql)

            sql2 = "INSERT INTO gejala(namaPenyakit) VALUES('" + user.sex + "')"
            cursor.execute(sql2)

        con.commit()
        con.close()

        msg = bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex + '\n jawaban:' + user.q27 )
        bot.register_next_step_handler(msg, send_end)
        
    except Exception as e:
        bot.reply_to(message,'oops lanjut')

def send_end(message):
    msg = bot.reply_to(message, """Byeee Lanjut""")



bot.polling()