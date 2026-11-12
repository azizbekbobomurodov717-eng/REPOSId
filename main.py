import telebot

bot = telebot.TeleBot("8835666769:AAH1Gd9sowontTl0OfXL3uMm-zSKc3A2pI0")

@bot.message_handler(["start"])
def boshlash(message):bot.send_photo(message.chat.id, caption="salom botimizga xush kelibsiz!!!", photo="https://x-plays.ru/public/images/1705067083.webp")


print("Bot ishga tushdi...")
bot.infinity_polling()
