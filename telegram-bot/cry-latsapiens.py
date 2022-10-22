from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "5719668913:AAGEyT9pj_tm45GVU51llA7xnKUS3B2Ftt0"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def sen_welcome(message):
    answer = "Assalomu alaykum, Xush kelibsez!"
    answer +=  "\nMatn kiriting:"
    bot.reply_to(message=message, text=answer)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    print(msg.isascii())
    if msg.isascii():
        answer = to_cyrillic(msg)
    else:
        answer = to_latin(msg)
    bot.reply_to(message, answer)

bot.polling()








#matn = input("Matn kiritng!")
#if matn.isascii():
#    print(to_cyrillic(matn))
#else:
#    print(to_latin(matn))
