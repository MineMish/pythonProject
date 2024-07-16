import telebot
import openai

bot = telebot.TeleBot("7023251839:AAEkux-W3fdZS0Izx0JDnaylkLJedfEl9oo")
openai.api_key = "OPENAI_API_KEY"

@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)

bot.polling()