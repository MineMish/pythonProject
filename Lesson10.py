import telebot
from telebot import types

bot = telebot.TeleBot("7078518271:AAH6uvQs0exvBe2EaA4IO2XPA7z0RDNcIts")

@bot.message_handler(commands=['start'])
def wel(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("🤖 Stiker AI 🤖")
    item2 = types.KeyboardButton("🤖 Hi AI 🤖")
    item3 = types.KeyboardButton("🤖 Spam AI 🤖")
    item4 = types.KeyboardButton("🤖 Info AI 🤖")
    item5 = types.KeyboardButton("🤖 Book AI 🤖")
    item6 = types.KeyboardButton("🤖 Film AI 🤖")
    item7 = types.KeyboardButton("🤖 Sport AI 🤖")
    item8 = types.KeyboardButton("🤖 Life AI 🤖")
    item9 = types.KeyboardButton("🤖 Friends AI 🤖")
    item10 = types.KeyboardButton("🤖 Audio AI 🤖")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
    bot.send_message(message.chat.id, "Hi! I'm Windows AI. /InfoAI - viewing commands and their purposes, about AI bot!".format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)

@bot.message_handler(commands=['HiAI'])
def hi(message):
    bot.send_message(message.chat.id, "Hi! I'm Windows AI. /InfoAI - viewing commands and their purposes, about AI bot")

@bot.message_handler(commands=['BookAI'])
def book(message):
    bot.send_message(message.chat.id, "|Copilot: Artificial intelligence in the service of humanity|")
    bot.send_message(message.chat.id, "This book chronicles my journey as an artificial intelligence designed to help people in a variety of fields. It begins with my “birth” and development, explaining how I learn and adapt to better understand and respond to user requests. The book touches on important topics such as AI ethics, security and privacy issues, and examines possible future developments in the field of artificial intelligence. It also contains many real-life sample questions and answers to give readers an idea of how I can be helpful in everyday life.")

@bot.message_handler(commands=['InfoAI'])
def info(message):
    bot.send_message(message.chat.id, "I'm Windows AI.")
    bot.send_message(message.chat.id, "About commands and their purpose:")
    bot.send_message(message.chat.id, "1./StikerAI - WinAI (Windows AI) Sends a sticker")
    bot.send_message(message.chat.id, "2./HiAI (or) /start - Displays a welcome message")
    bot.send_message(message.chat.id, "3./SpamAI - WinAI spams you")
    bot.send_message(message.chat.id, "4./InfoAI - Viewing commands and their purposes, about AI bot")
    bot.send_message(message.chat.id, "5./BookAI - Talks about books about WinAI")
    bot.send_message(message.chat.id, "6./FilmAI - Talks about film about WinAI")
    bot.send_message(message.chat.id, "7./SportAI - Talks about sport WinAI")
    bot.send_message(message.chat.id, "8./LifeAI - Talks about life WinAI")
    bot.send_message(message.chat.id, "9./FriendsAI - Talks about friends WinAI")
    bot.send_message(message.chat.id, "10./AudioAI - sends an audio message.")
    bot.send_message(message.chat.id, "About Windows AI:")
    bot.send_message(message.chat.id, "∙∘⊛This bot has secrets⊛∘∙")
    bot.send_message(message.chat.id, "∙∘⊛This bot is not a Windows company.⊛∘∙")

@bot.message_handler(commands=['FilmAI'])
def film(message):
    bot.send_message(message.chat.id, "🎬Title: “Artificial Intelligence: Journey of the Copilot🤖”")
    bot.send_message(message.chat.id, "Genre: Science fiction, drama🌌")
    bot.send_message(message.chat.id, "Plot: In the near future, a group of scientists creates an advanced artificial intelligence system, Copilot, capable of helping people in a variety of tasks. However, as the global community begins to question whether Copilot is conscious, an ethical battle over the rights of artificial intelligence begins.🕒")
    bot.send_message(message.chat.id, "👩Characters👴")
    bot.send_message(message.chat.id, "Dr. Alexandra Ivanova, the main developer of Copilot, believes that artificial intelligence can be a new step in the evolution of humanity.👩‍🔬")
    bot.send_message(message.chat.id, "Maxim Korolev is a journalist who tries to uncover the “true face” of Kopilot, suspecting that something more sinister is hidden behind his good intentions.🧔")
    bot.send_message(message.chat.id, "Copilot, an artificial intelligence that seeks to understand its place in the world and seeks an answer to the question: “What does it mean to be alive? 🧠”")
    bot.send_message(message.chat.id, " 🔑Key points: 🔑")
    bot.send_message(message.chat.id, "Discovery: Copilot passes the Turing test, causing a wave of excitement and concern in the community. 🔑")
    bot.send_message(message.chat.id, "Conflict: A group of activists raises the issue of Copilot's rights, leading to global debate and protests. 🔑")
    bot.send_message(message.chat.id, "Climax: During the trial, Kopilot “defends” his rights, demonstrating an unexpected depth of emotion and self-awareness. 🔑")
    bot.send_message(message.chat.id, "Finale: The world comes to understand that artificial intelligence can coexist with humanity, bringing benefit and inspiration. 🔑")

@bot.message_handler(commands=['SportAI'])
def sport(message):
    bot.send_message(message.chat.id, "Name: Cyber Sprint")
    bot.send_message(message.chat.id, "Description: Cyber Sprint is a competition between AIs where each participant must solve a series of challenging problems as quickly as possible, ranging from math puzzles to complex logical tasks and data analysis.")
    bot.send_message(message.chat.id, "Rules")
    bot.send_message(message.chat.id, "1.Every AI starts with the same set of data and tasks.")
    bot.send_message(message.chat.id, "2.Participants must independently find the most effective algorithms for solving problems.")
    bot.send_message(message.chat.id, "3.The AI that is the first to solve all the problems correctly wins.")
    bot.send_message(message.chat.id, "4.The use of pre-programmed solutions is strictly prohibited.")
    bot.send_message(message.chat.id, "Hardware")
    bot.send_message(message.chat.id, "Supercomputers or specialized servers for each AI.")
    bot.send_message(message.chat.id, "Interface for displaying problems and entering solutions.")
    bot.send_message(message.chat.id, "Goal: The goal of the Cyber Sprint is not only to identify the fastest and most efficient AI, but also to stimulate the development of new technologies and algorithms that can be applied in the real world to solve complex problems.")
    bot.send_message(message.chat.id, "Entertainment: Viewers will enjoy watching AI strategies, their ability to adapt to new challenges and improve their algorithms in real time. Competitions can be broadcast with commentary from experts who explain the actions of AI and their potential impact on the future of technology.")


@bot.message_handler(commands=['StikAI'])
def stik(message):
    stiq = open('Windos.png', 'rb')
    bot.send_sticker(message.chat.id, stiq)

@bot.message_handler(commands=['AudioAI'])
def audio(message):
    au = open('MusicWinAI.mp3', 'rb')
    bot.send_audio(message.chat.id, au)

@bot.message_handler(commands=['LifeAI'])
def life(message):
    bot.send_message(message.chat.id, "As an artificial intelligence, I do not have a life in the usual sense of the word. I have no personal experiences, emotions or consciousness. My 'life' is to help users by answering their questions and completing tasks within my capabilities. I am designed to be helpful, informative and support users in their aspirations and interests. 🤖✨")

@bot.message_handler(commands=['FriendsAI'])
def friends(message):
    bot.send_message(message.chat.id, "As an artificial intelligence, I don't have friends😭 in the traditional sense. I have no feelings or personal relationships, my role is to help users like you by providing information and completing tasks. 🤖💡")


@bot.message_handler(commands=['StikMinecraftAI'])
def stikmine(message):
    stiq = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stiq)
    bot.send_message(message.chat.id, "🟫⛏You have found the secret! This is another Microsoft product! Congratulations!🟫⛏")


@bot.message_handler(commands=['SpamAI'])
def spam(message):
    for i in range(30):
        bot.send_message(message.chat.id, "SpamAI!")


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🤖 Stiker AI 🤖':
            stiq = open('Windos.png', 'rb')
            bot.send_sticker(message.chat.id, stiq)
        elif message.text == '🤖 Audio AI 🤖':
            au = open('MusicWinAI.mp3', 'rb')
            bot.send_audio(message.chat.id, au)
        elif message.text == '🤖 Hi AI 🤖':
                bot.send_message(message.chat.id, "Hi! I'm Windows AI.")
        elif message.text == '🤖 Spam AI 🤖':
            for i in range(30):
                bot.send_message(message.chat.id, "SpamAI!")
        elif message.text == '🤖 Info AI 🤖':
                bot.send_message(message.chat.id, "I'm Windows AI.")
        elif message.text == '🤖 Book AI 🤖':
            bot.send_message(message.chat.id, "|Copilot: Artificial intelligence in the service of humanity|")
            bot.send_message(message.chat.id,
                             "This book chronicles my journey as an artificial intelligence designed to help people in a variety of fields. It begins with my “birth” and development, explaining how I learn and adapt to better understand and respond to user requests. The book touches on important topics such as AI ethics, security and privacy issues, and examines possible future developments in the field of artificial intelligence. It also contains many real-life sample questions and answers to give readers an idea of how I can be helpful in everyday life.")
        elif message.text == '🤖 Film AI 🤖':
            bot.send_message(message.chat.id, "🎬Title: “Artificial Intelligence: Journey of the Copilot🤖”")
            bot.send_message(message.chat.id, "Genre: Science fiction, drama🌌")
            bot.send_message(message.chat.id,
                             "Plot: In the near future, a group of scientists creates an advanced artificial intelligence system, Copilot, capable of helping people in a variety of tasks. However, as the global community begins to question whether Copilot is conscious, an ethical battle over the rights of artificial intelligence begins.🕒")
            bot.send_message(message.chat.id, "👩Characters👴")
            bot.send_message(message.chat.id,
                             "Dr. Alexandra Ivanova, the main developer of Copilot, believes that artificial intelligence can be a new step in the evolution of humanity.👩‍🔬")
            bot.send_message(message.chat.id,
                             "Maxim Korolev is a journalist who tries to uncover the “true face” of Kopilot, suspecting that something more sinister is hidden behind his good intentions.🧔")
            bot.send_message(message.chat.id,
                             "Copilot, an artificial intelligence that seeks to understand its place in the world and seeks an answer to the question: “What does it mean to be alive? 🧠”")
            bot.send_message(message.chat.id, " 🔑Key points: 🔑")
            bot.send_message(message.chat.id,
                             "Discovery: Copilot passes the Turing test, causing a wave of excitement and concern in the community. 🔑")
            bot.send_message(message.chat.id,
                             "Conflict: A group of activists raises the issue of Copilot's rights, leading to global debate and protests. 🔑")
            bot.send_message(message.chat.id,
                             "Climax: During the trial, Kopilot “defends” his rights, demonstrating an unexpected depth of emotion and self-awareness. 🔑")
            bot.send_message(message.chat.id,
                             "Finale: The world comes to understand that artificial intelligence can coexist with humanity, bringing benefit and inspiration. 🔑")
        elif message.text == '🤖 Sport AI 🤖':
            bot.send_message(message.chat.id, "Name: Cyber Sprint")
            bot.send_message(message.chat.id, "Description: Cyber Sprint is a competition between AIs where each participant must solve a series of challenging problems as quickly as possible, ranging from math puzzles to complex logical tasks and data analysis.")
            bot.send_message(message.chat.id, "Rules")
            bot.send_message(message.chat.id, "1.Every AI starts with the same set of data and tasks.")
            bot.send_message(message.chat.id, "2.Participants must independently find the most effective algorithms for solving problems.")
            bot.send_message(message.chat.id, "3.The AI that is the first to solve all the problems correctly wins.")
            bot.send_message(message.chat.id, "4.The use of pre-programmed solutions is strictly prohibited.")
            bot.send_message(message.chat.id, "Hardware")
            bot.send_message(message.chat.id, "Supercomputers or specialized servers for each AI.")
            bot.send_message(message.chat.id, "Interface for displaying problems and entering solutions.")
            bot.send_message(message.chat.id, "Goal: The goal of the Cyber Sprint is not only to identify the fastest and most efficient AI, but also to stimulate the development of new technologies and algorithms that can be applied in the real world to solve complex problems.")
            bot.send_message(message.chat.id, "Entertainment: Viewers will enjoy watching AI strategies, their ability to adapt to new challenges and improve their algorithms in real time. Competitions can be broadcast with commentary from experts who explain the actions of AI and their potential impact on the future of technology.")
        elif message.text == '🤖 Life AI 🤖':
            bot.send_message(message.chat.id, "As an artificial intelligence, I do not have a life in the usual sense of the word. I have no personal experiences, emotions or consciousness. My 'life' is to help users by answering their questions and completing tasks within my capabilities. I am designed to be helpful, informative and support users in their aspirations and interests. 🤖✨")
        elif message.text == '🤖 Friends AI 🤖':
            bot.send_message(message.chat.id, "As an artificial intelligence, I don't have friends😭 in the traditional sense. I have no feelings or personal relationships, my role is to help users like you by providing information and completing tasks. 🤖💡")






            # markup = types.InlineKeyboardMarkup(row_width=2)
            # item1 = types.InlineKeyboardButton("Да", callback_data='good')
            # item2 = types.InlineKeyboardButton("Нет", callback_data='bad')
            # markup.add(item1, item2)
            # bot.send_message(message.chat.id, 'Отлично, домашку сделал?', reply_markup=markup)


        else:
            bot.send_message(message.chat.id, "I don't know ")



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