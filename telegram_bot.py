import os

import telebot

from telebot import types

from image import get_image_url

bot = telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=["start"])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Generate random graphic")
    markup.add(item)

    # greeting message
    bot.send_message(
        message.chat.id,
        "Welcome, {0.first_name}!\n"
        "Here you can generate random graph of trading.".format(
            message.from_user, bot.get_me()
        ),
        parse_mode="html",
        reply_markup=markup,
    )


@bot.message_handler(content_types=["text"])
def send_image(message):
    if message.chat.type == "private":
        if message.text == "Generate random graphic":
            bot.send_photo(message.chat.id, get_image_url())
        else:
            bot.send_message(message.chat.id, "Incorrect command")


bot.polling(none_stop=True)