import telebot

bot = telebot.TeleBot("7078518271:AAH6uvQs0exvBe2EaA4IO2XPA7z0RDNcIts")

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
def wel(message):
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


bot.polling(none_stop=True)