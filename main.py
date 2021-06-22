import telebot
import random

from telebot import types

bot = telebot.TeleBot("1898808473:AAEs8kO-pm_mhC4d0aEr2j_T9p_MIfGr5uQ")

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Подбросить монетку")
item2 = types.KeyboardButton("🎲 Бросить кость")
item3 = types.KeyboardButton("👍 Да / Нет 👎")
markup2.row(item1)
markup2.row(item2)
markup2.row(item3)

markupi = types.InlineKeyboardMarkup(row_width=2)
button1 = types.InlineKeyboardButton("1 кость", callback_data='1')
button2 = types.InlineKeyboardButton("2 кости", callback_data='2')
markupi.add(button1, button2)


def dice(message):
    k = random.randint(1, 6)

    if k == 1:
        photo = open('kub1.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif k == 2:
        photo = open('kub2.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif k == 3:
        photo = open('kub3.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif k == 4:
        photo = open('kub4.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif k == 5:
        photo = open('kub5.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif k == 6:
        photo = open('kub6.png', 'rb')
        bot.send_photo(message.chat.id, photo)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '1':
                dice(call.message)
            elif call.data == '2':
                dice(call.message)
                dice(call.message)
    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    sticker = open('pushistik.jpg', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n"
                     "Я - <b>{1.first_name}</b>, "
                     "бот созданный чтобы разрешить "
                     "ваши жизненно важные споры.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id, 'Переключитесь на клавиатуру'
                                      ' с кнопками)\n\n'
                     'или просто напишите мне:\n\n'
                     '" М " - если хотите подбросить монетку \n'
                     '" К "- если хотите бросить кость 🎲 \n'
                     '" Д " или " Н "- если хотите просто узнать:'
                     ' да 👍 или нет 👎',
                     reply_markup=markup2)


# content_types=['text']

@bot.message_handler(content_types=None)
def lalala(message):
    if message.text == 'Подбросить монетку' or message.text == 'М' or \
            message.text == 'м' or message.text == 'M':
        m = random.randint(0, 2)
        if m == 0:
            bot.send_message(message.chat.id, 'Решка')
            photo = open('reshka.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, 'Орёл')
            photo = open('orel.png', 'rb')
            bot.send_photo(message.chat.id, photo)

    elif message.text == '🎲 Бросить кость' or message.text == 'K' or \
            message.text == 'к' or message.text == 'К':
        bot.send_message(message.chat.id, 'Бросаем:', reply_markup=markupi)

    elif message.text == '👍 Да / Нет 👎' or \
            message.text == 'Н' or message.text == 'н' or \
            message.text == 'H' or message.text == 'Д' or message.text == 'д':
        m = random.randint(0, 2)
        if m == 0:
            bot.send_message(message.chat.id, 'ДА')
            sticker = open('stich_yes.jpg', 'rb')
            bot.send_sticker(message.chat.id, sticker)
        else:
            bot.send_message(message.chat.id, 'НЕТ')
            sticker = open('stich_no.jpg', 'rb')
            bot.send_sticker(message.chat.id, sticker)

    else:
        bot.send_message(message.chat.id, 'Что-то пошло не по плану🧐')
        bot.send_message(message.chat.id, 'Переключитесь на клавиатуру '
                                          'с кнопками, пожалуйста)\n\n'
                         'или просто напишите мне:\n\n'
                         '" М "-если хотите подбросить монетку  \n'
                         '" К "- если хотите бросить кость 🎲 \n'
                         '" Д " или " Н "- если хотите просто узнать: '
                         'да 👍 или нет 👎', reply_markup=markup2)

bot.polling()
