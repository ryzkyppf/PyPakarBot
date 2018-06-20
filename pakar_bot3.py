# -*- coding: utf-8 -*-
import time
import datetime
import pymysql
import pymysql.cursors
import telebot
from telebot import types
from collections import Counter

API_TOKEN = '413035429:AAHAsUnIE08sMQucXrsYYsX7AwNlGxsrtjw'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}

con = pymysql.connect(db="pakar", user="root", passwd="",host="localhost",port=3306,autocommit=True)

gejala = []

diagnosa = 0

cf = 0


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
        self.qhari= None

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    chat_id = message.chat.id
    msg = bot.reply_to(message, """\
Selamat datang, Ini merupakan bot Diagnosa Awal Penyakit Ginjal.\n 
""")
    bot.send_message(chat_id, 'Silahkan menjawab semua poin pertanyaan berikut 27 pertanyaan diagnosa dengan yakin. Jawablah dengan menekan jawaban yang disediakan.')
    bot.send_message(chat_id, 'Siapa Nama Anda?')
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Berapakah umur anda? ')
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
        msg = bot.reply_to(message, '1. Apakah anda demam tinggi dan menggigil?', reply_markup=markup)
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
        msg = bot.reply_to(message, '2. Apakah anda merasa nyeri pada pinggang sisi belakang atau samping satu atau kedua sisi?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q3_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q2 step')

def process_q3_step(message):
    try:
        chat_id = message.chat.id
        q2 = message.text
        user = user_dict[chat_id]
        user.q2 = q2
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '3. Apakah anda merasa Nyeri dan rasa terbakar ketika buang air kecil?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q4_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q3 step')

def process_q4_step(message):
    try:
        chat_id = message.chat.id
        q3 = message.text
        user = user_dict[chat_id]
        user.q3 = q3
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '4. Apakah urin berbau busuk, keruh, bernanah?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q5_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q4 step')


def process_q5_step(message):
    try:
        chat_id = message.chat.id
        q4 = message.text
        user = user_dict[chat_id]
        user.q4 = q4
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '5. Apakah terdapat darah dalam urin/urin berwarna kemerahan?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q6_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q5 step')

def process_q6_step(message):
    try:
        chat_id = message.chat.id
        q5 = message.text
        user = user_dict[chat_id]
        user.q5 = q5
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '6. Apakah anda merasa sering buang air kecil?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q7_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q6 step')


def process_q7_step(message):
    try:
        chat_id = message.chat.id
        q6 = message.text
        user = user_dict[chat_id]
        user.q6 = q6
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '7. Apakah anda merasa desakan untuk segera buang air kecil?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q8_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q7 step')


def process_q8_step(message):
    try:
        chat_id = message.chat.id
        q7 = message.text
        user = user_dict[chat_id]
        user.q7 = q7
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '8. Apakah anda sering mual dan muntah?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q9_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q8 step')


def process_q9_step(message):
    try:
        chat_id = message.chat.id
        q8 = message.text
        user = user_dict[chat_id]
        user.q8 = q8
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '9. Apakah anda sering merasa lesu?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q10_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q9 step')


def process_q10_step(message):
    try:
        chat_id = message.chat.id
        q9 = message.text
        user = user_dict[chat_id]
        user.q9 = q9
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '10. Apakah anda mudah kelelahan?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q11_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q10 step')


def process_q11_step(message):
    try:
        chat_id = message.chat.id
        q10 = message.text
        user = user_dict[chat_id]
        user.q10 = q10
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '11. Apakah anda sering mengalami gangguan daya pikir / merasa kebingungan?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q12_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q11 step')


def process_q12_step(message):
    try:
        chat_id = message.chat.id
        q11 = message.text
        user = user_dict[chat_id]
        user.q11 = q11
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '12. Apakah anda mengalami demam yang menetap?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q13_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q12 step')


def process_q13_step(message):
    try:
        chat_id = message.chat.id
        q12 = message.text
        user = user_dict[chat_id]
        user.q12 = q12
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '13. Apakah anda mengalami nyeri yang menjalar ke perut bawah dan selangkangan (hilang timbul)?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q14_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q13 step')


def process_q14_step(message):
    try:
        chat_id = message.chat.id
        q13 = message.text
        user = user_dict[chat_id]
        user.q13 = q13
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '14. Apakah mengalami jumlah urin yang menurun/sedikit?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q15_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q14 step')


def process_q15_step(message):
    try:
        chat_id = message.chat.id
        q14 = message.text
        user = user_dict[chat_id]
        user.q14 = q14
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '15. Apakah terdapat benjolan pada punggung bawah atau pinggang satu atau kedua sisi?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q16_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q15 step')


def process_q16_step(message):
    try:
        chat_id = message.chat.id
        q15 = message.text
        user = user_dict[chat_id]
        user.q15 = q15
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '16. Apakah anda mengalami penurunan nafsu makan?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q17_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q16 step')


def process_q17_step(message):
    try:
        chat_id = message.chat.id
        q16 = message.text
        user = user_dict[chat_id]
        user.q16 = q16
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '17. Apakah anda mengalami penurunan berat badan tanpa sebab yang jelas?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q18_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q17 step')


def process_q18_step(message):
    try:
        chat_id = message.chat.id
        q17 = message.text
        user = user_dict[chat_id]
        user.q17 = q17
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '18. Apakah anda mengalami tidak keluar urin sama sekali?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q19_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q18 step')


def process_q19_step(message):
    try:
        chat_id = message.chat.id
        q18 = message.text
        user = user_dict[chat_id]
        user.q18 = q18
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '19. Apakah anda mengalami bengkak pada salah satu atau lebih (wajah, badan, kaki, tangan)?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q20_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q19 step')


def process_q20_step(message):
    try:
        chat_id = message.chat.id
        q19 = message.text
        user = user_dict[chat_id]
        user.q19 = q19
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '20. Apakah anda mengalami sesak napas?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q21_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q20 step')


def process_q21_step(message):
    try:
        chat_id = message.chat.id
        q20 = message.text
        user = user_dict[chat_id]
        user.q20 = q20
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '21. Apakah anda sering mengalami gatal-gatal pada kulit?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q22_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q21 step')


def process_q22_step(message):
    try:
        chat_id = message.chat.id
        q21 = message.text
        user = user_dict[chat_id]
        user.q21 = q21
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '22. Apakah anda sering mengalami sakit kepala?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q23_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q22 step')


def process_q23_step(message):
    try:
        chat_id = message.chat.id
        q22 = message.text
        user = user_dict[chat_id]
        user.q22 = q22
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '23. Apakah anda mengalami peningkatan jumlah urin?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q24_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q23 step')


def process_q24_step(message):
    try:
        chat_id = message.chat.id
        q23 = message.text
        user = user_dict[chat_id]
        user.q23 = q23
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '24. Apakah anda mengalami warna kulit bertambah gelap tanpa sebab yang jelas?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q25_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q24 step')


def process_q25_step(message):
    try:
        chat_id = message.chat.id
        q24 = message.text
        user = user_dict[chat_id]
        user.q24 = q24
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '25. Apakah anda mengalami urin yang berbuih?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q26_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q25 step')


def process_q26_step(message):
    try:
        chat_id = message.chat.id
        q25 = message.text
        user = user_dict[chat_id]
        user.q25 = q25
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '26. Apakah anda mengalami peningkatan berat badan?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q27_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q26 step')


def process_q27_step(message):
    try:
        chat_id = message.chat.id
        q26 = message.text
        user = user_dict[chat_id]
        user.q26 = q26
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '27. Apakah anda sering mengalami penurunan kesadaran hingga tidak sadarkan diri?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_diagnosa)
    except Exception as e:
        bot.reply_to(message, 'oooops q27 step')


def process_diagnosa(message):
    try:
        chat_id = message.chat.id
        q27 = message.text
        user = user_dict[chat_id]
        user.q27 = q27

        #Start of engine
        A = ['Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak']
        B = ['Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak']
        C = ['Tidak', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak'] 
        D = ['Tidak', 'Ya', 'Tidak', 'Tidak', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak']
        E = ['Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya']
        F = ['Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak']
        G = ['Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Tidak', 'Tidak', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Tidak']
        H = ['Tidak', 'Ya', 'Tidak', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak']

        gejala.extend((user.q1, user.q2, user.q3, user.q4, user.q5, user.q6, user.q7, user.q8, user.q9, user.q10, user.q11, user.q12, user.q13, user.q14, user.q15, user.q16, user.q17, user.q18, user.q19, user.q20, user.q21, user.q22, user.q23, user.q24, user.q25, user.q26, user.q27))

        input_multiset = Counter(gejala)

        if gejala == A:
            diagnosa = 'Infeksi Saluran Kemih Bagian Atas'
            user.diagnosa = diagnosa
            cf= '60%'
            user.cf = cf
        elif gejala == B:
            diagnosa = 'Infeksi Saluran Kemih Bagian Bawah'
            user.diagnosa = diagnosa
            cf = '80%'
            user.cf = cf
        elif gejala == C:
            diagnosa = 'Batu Ginjal'
            user.diagnosa = diagnosa
            cf = '73%'
            user.cf = cf
        elif gejala == D:
            diagnosa = 'Kanker Ginjal'
            user.diagnosa = diagnosa
            cf = '99%'
        elif gejala == E:
            diagnosa = 'Gagal Ginjal Akut'
            user.diagnosa = diagnosa
            cf = '76%'
            user.cf = cf
        elif gejala == F:
            diagnosa = 'Gagal Ginjal Kronis'
            user.diagnosa = diagnosa
            cf = '73%'
            user.cf = cf
        elif gejala == G:
            diagnosa = 'Sindrom Nefrotik'
            user.diagnosa = diagnosa
            cf = '93%'
            user.cf = cf
        elif gejala == H:
            diagnosa = 'Penyakit Ginjal Polikistik'
            user.diagnosa = diagnosa
            cf = '91%'
            user.cf = cf
        else:
            diagnosa = 'Bukan Penyakit Ginjal'
            user.diagnosa = diagnosa
            cf = '-'
            user.cf = cf
        #End of engine    
        
        bot.send_message(chat_id, 'Halo ' + user.name + ',\nBerikut ini hasil diagnosa awal anda: ' )
        bot.send_message(chat_id, '\n Kemungkinan Anda beresiko mengalami ' + diagnosa + '\nDengan persentase kemungkinan sebesar = ' + cf )
        bot.send_message(chat_id, 'Mohon melakukan diagnosa lebih lanjut untuk kepastian penyakit anda.' )
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, 'Ingin melakukan diagnosa lebih lanjut dengan dokter?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_lanjut)
    except Exception as e:
        bot.reply_to(message, 'oooops diagnosa')


def process_lanjut(message):
    try:
        chat_id = message.chat.id
        qlanjut = message.text
        user = user_dict[chat_id]
        user.qlanjut=qlanjut

        if (qlanjut == 'Ya'):
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Rabu', 'Kamis', 'Jumat')
            msg = bot.reply_to(message, 'Kapan anda ingin melakukan diagnosa?', reply_markup=markup)
            bot.register_next_step_handler(msg, process_diagnosa2)
        else:
            msg = bot.reply_to(message, """Byeee""")
    except Exception as e:
        bot.reply_to(message, 'oooops Proses lanjut step')


def process_diagnosa2(message):
    try:
        chat_id = message.chat.id
        qhari = message.text
        user = user_dict[chat_id]
        user.qhari = qhari

        if (qhari == 'Rabu'):
            d = datetime.datetime.now().date()
            next_monday = next_weekday(d, 2) # 0 = Monday, 1=Tuesday, 2=Wednesday...
            user.next_monday = next_monday
            print(user.next_monday)

        elif (qhari == 'Kamis'):
            d = datetime.datetime.now().date()
            next_monday = next_weekday(d, 3) # 0 = Monday, 1=Tuesday, 2=Wednesday...
            user.next_monday = next_monday
            print(user.next_monday)            

        elif (qhari == 'Jumat'):
            d = datetime.datetime.now().date()
            next_monday = next_weekday(d, 4) # 0 = Monday, 1=Tuesday, 2=Wednesday...
            user.next_monday = next_monday
            print(user.next_monday)


        #penulisan query
        with con.cursor() as cursor:
            sql = "INSERT INTO diagnosa(nama, sex, age, diagnosa, jadwal, tanggald, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27 ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) " 
            data = (user.name, user.sex, user.age, user.diagnosa, user.qhari, user.next_monday, user.q1, user.q2, user.q3, user.q4, user.q5, user.q6, user.q7, user.q8, user.q9, user.q10, user.q11, user.q12, user.q13, user.q14, user.q15, user.q16, user.q17, user.q18, user.q19, user.q20, user.q21, user.q22, user.q23, user.q24, user.q25, user.q26, user.q27)
            cursor.execute(sql, data)
            '''
            sql2 = "INSERT INTO diagnosa(nama, sex, age, diagnosa, jadwal ) VALUES('"+user.name+"','" + user.sex + "', '"+user.age+"', '"+user.diagnosa+"', '"+user.qhari+"')"
            cursor.execute(sql2)
            '''
        con.commit()
        con.close()
        #Akhir Query

        msg = bot.reply_to(message, 'Silahkan melakukan diagnosa awal pada '+user.qhari+' di Klinik Bersama')
        bot.send_message(chat_id, """Terima kasih telah memanfaatkan fasilitas Sistem Pakar Diagnosa Awal Penyakit Ginjal \nSemoga hari anda menyenangkan \n""")
        bot.send_message(chat_id, 'Untuk memulai kembali ketikkan atau klik /start ')
    except Exception as e:
        bot.reply_to(message, 'oooops diagnosa2')
    



bot.polling()

#SBAdmin