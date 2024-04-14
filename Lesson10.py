import telebot
from telebot import types

bot = telebot.TeleBot("7078518271:AAH6uvQs0exvBe2EaA4IO2XPA7z0RDNcIts")

@bot.message_handler(commands=['start'])
def wel(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Stiker AI")
    item2 = types.KeyboardButton("Hi AI")
    item3 = types.KeyboardButton("Spam AI")
    item4 = types.KeyboardButton("Info AI")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Hi! I'm Windows AI.".format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)

@bot.message_handler(commands=['HiAI'])
def wel(message):
    bot.send_message(message.chat.id, "Hi! I'm Windows AI.")

@bot.message_handler(commands=['InfoAI'])
def wel(message):
    bot.send_message(message.chat.id, "I'm Windows AI.")


@bot.message_handler(commands=['StikAI'])
def stik(message):
    stiq = open('Windos.png', 'rb')
    bot.send_sticker(message.chat.id, stiq)

@bot.message_handler(commands=['StikMinecraftAI'])
def stik(message):
    stiq = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stiq)
    bot.send_message(message.chat.id, "You have found the secret! This is another Microsoft product! Congratulations!")


@bot.message_handler(commands=['SpamAI'])
def spam(message):
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")
    bot.send_message(message.chat.id, "SpamAI!")


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Stiker AI':
            stiq = open('Windos.png', 'rb')
            bot.send_sticker(message.chat.id, stiq)
        elif message.text == 'Hi AI':
                bot.send_message(message.chat.id, "Hi! I'm Windows AI.")
        elif message.text == 'Spam AI':
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
                bot.send_message(message.chat.id, "SpamAI!")
        elif message.text == 'Info AI':
                bot.send_message(message.chat.id, "I'm Windows AI.")



            # markup = types.InlineKeyboardMarkup(row_width=2)
            # item1 = types.InlineKeyboardButton("Да", callback_data='good')
            # item2 = types.InlineKeyboardButton("Нет", callback_data='bad')
            # markup.add(item1, item2)
            # bot.send_message(message.chat.id, 'Отлично, домашку сделал?', reply_markup=markup)


        else:
            bot.send_message(message.chat.id, 'I don\'t know ')



# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'good':
#                 bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
#                 bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
#                     text="ЭТО ШЕДЕВР!")
#             elif call.data == 'bad':
#                 bot.send_message(call.message.chat.id, 'Маме расскажу, ругать будет 😢')
#                 bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
#                     text="ТІКАЙ З СЕЛА!!!!")
#             # remove inline buttons
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
#                 reply_markup=None)
#             # show alert
#     except Exception as e:
#         print(repr(e))


bot.polling(none_stop=True)