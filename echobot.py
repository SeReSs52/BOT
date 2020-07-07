import telebot
import random
token = '1369221356:AAEyH13RKLsDdD4RS5u2XU_U9GRERMj_iZM'

bot = telebot.TeleBot(token)
bad_words = ['Кто тебе разрешил сюда писать??', "Ты не достоин писать сюда, выйди из этого чата!"]

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    chislo = random.randint(0, 1)
    if(message.text == "Как дела?"):
        message.text = "Плохо, меня Денис програмировал";
    if(message.text == "game"):
        bot.send_dice(message.chat.id)
    elif(chislo):
        message.text = random.choice(bad_words)
        bot.send_message(message.chat.id, message.text)

bot.infinity_polling()
