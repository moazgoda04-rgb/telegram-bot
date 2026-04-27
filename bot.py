import telebot
from telebot import types

BOT_TOKEN = "8693778483:AAH4rFcWLDCob4uY7N0IJdsVO9kd5PJvWm4"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
    btn1 = types.KeyboardButton("خدماتنا 📋")
    btn2 = types.KeyboardButton("تواصل معنا 📞")
    markup.add(btn1, btn2)
    bot.reply_to(message, f"أهلاً {message.from_user.first_name}! 👋 اختار من القائمة:", reply_markup=markup)
@bot.message_handler(func=lambda msg: msg.text == "خدماتنا 📋")
def services(message):
    bot.reply_to(message, "خدماتنا:\n1. بوت ترحيبي\n2. بوت للمتاجر\n3. بوت مخصص")
@bot.message_handler(func=lambda msg: msg.text == "تواصل معنا 📞")
def contact(message):
    bot.reply_to(message, "تواصل معنا على:\n@your_username")
bot.infinity_polling()           