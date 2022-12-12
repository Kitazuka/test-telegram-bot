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
def commands(message):
    if message.text == "Generate random graphic":
        pm = bot.send_message(
            message.chat.id, "Pick the trading pair (for example: BTCUSDT)"
        )
        bot.register_next_step_handler(pm, send_image)
    else:
        bot.send_message(message.chat.id, "Incorrect command")


def send_image(message):
    pair = message.text
    try:
        photo_url = get_image_url(pair)
        bot.send_photo(message.chat.id, photo_url)
    except AttributeError:
        pm = bot.send_message(
            message.chat.id,
            (
                "Incorrect pair, "
                "pick another trading pair "
                "(for example: BTCUSDT)"
            ),
        )
        bot.register_next_step_handler(pm, send_image)


bot.polling(none_stop=True)
