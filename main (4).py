import telebot

bot = telebot.TeleBot("8835666769:AAH1Gd9sowontTl0OfXL3uMm-zSKc3A2pI0")

@bot.message_handler(commands = ["start"])
def start(massage):
    bot.reply_to(massage , text="Assalomu Alaykum bu mening  1 chi telegramdagi kodim!!!")

@bot.message_handler(commands = ["help"])
def help(message):
    bot.reply_to(message , text="""🛠 Yordam bo'limi
Botdan foydalanishda qiyinchilikka duch kelgan bolsangiz, quyidagi komandalardan foydalanishingiz mumkin:

/info — Bot haqida umumiy malumot

/about — Botning vazifasi va imkoniyatlari

/username — Botning foydalanuvchi nomi

/nickname — Botning nomi

/description — Botning tavsifi

Qoshimcha savollar bolsa, adminga murojaat qiling: @azizbek_bobomurodov""")

@bot.message_handler(commands = ["info"])
def info(massage):
    bot.reply_to(massage , text="""ℹ️ Ma'lumot

Ushbu bot Sensorika tizimi uchun maxsus ishlab chiqilgan bo'lib, foydalanuvchilarga qulay va tezkor xizmat ko'rsatishga yordam beradi.""")


@bot.message_handler(commands = ["about"])
def about(massage):
    bot.reply_to(massage , text="""🤖 Bot haqida

Sensorika's bot — bu sizning ishingizni yengillashtirish va kerakli ma'lumotlarni tezkor yetkazib berish uchun yaratilgan avtomatlashtirilgan yordamchi.""")


@bot.message_handler(commands = ["username"])
def username(massage):
    bot.reply_to(massage , text="""🔗 Bot manzili (username):
https://t.me/sensorika_48_bot""")
    

@bot.message_handler(commands = ["nickname"])
def nickname(massage):
    bot.reply_to(massage , text="""🏷 Bot nomi:
Sensorika's bot""")
    

@bot.message_handler(commands = ["description"])
def description(massage):
    bot.reply_to(massage , text="""📝 Tavsif

Ushbu bot Sensorika platformasining rasmiy boti bo'lib, foydalanuvchilar bilan muloqot qilish, so'rovlarni qabul qilish va zaruriy ma'lumotlarni taqdim etish uchun xizmat qiladi.""")

import telebot
from telebot import types



@bot.message_handler(commands=['uyin'])
def send_welcome(message):
    bot.reply_to(message, "Salom! O'yinni boshlash uchun /game buyrug'ini yuboring.")

@bot.message_handler(commands=['game'])
def send_game(message):
    markup = types.InlineKeyboardMarkup()
    
    web_app = types.WebAppInfo(url="https://yandex.uz/games/home")
    
    button = types.InlineKeyboardButton(text="🎮 O'yinni o'ynash", web_app=web_app)
    markup.add(button)
    
    bot.send_message(
        message.chat.id, 
        "Marhamat, tugmani bosing va o'yinni boshlang!", 
        reply_markup=markup
    )

print("Bot ishga tushdi...")
bot.infinity_polling()






print("working....")
bot.infinity_polling()