import telebot as t
from telebot import types

bot = t.TeleBot('924946285:AAEtfhMLLDkBJ-nat40GGmF6nQnDpc8IFsE')

#Чтобы запустить данный проект , должен быть установлен VPN на компьютер 

@bot.message_handler(commands=['start', 'help'], content_types=['text'])
def help_message(message):
    bot.reply_to(message, """\
    Привет , я бот портфолио
исполнителя - C O R S O
    """)
    mane = types.ReplyKeyboardMarkup()
    profile = types.KeyboardButton('Написать создателю')
    about = types.KeyboardButton('О проекте')
    music = types.KeyboardButton('Послушать творчество')
    restart = types.KeyboardButton('Перезапустить бота')
    mane.row(profile, about)
    mane.row(music)
    mane.row(restart)
    bot.send_sticker(message.chat.id, 'CAADAgADDAUAAj-VzAr92XWPaBV8HRYE', reply_markup=mane)
    'bot.send_audio(message, "CQADAgADDAUAAt7JcEhEgzzkiAwWyBYE")'


@bot.message_handler(content_types=['text'])
def navigation(message):
    if message.text == 'Написать создателю':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Написать  TG", url='t.me/dkeew')
        vk_button = types.InlineKeyboardButton(text="Написать VK", url='vk.com/kuznecoovv')
        keyboard.add(url_button)
        keyboard.add(vk_button)
        bot.send_message(message.chat.id, 'Связь с автором данного проэкта', reply_markup=keyboard)

    elif message.text == 'О проекте':
        keyboard_about = types.InlineKeyboardMarkup()
        git_button = types.InlineKeyboardButton(text='Просмотр библиотеки TeleBot',
                                                url='https://github.com/eternnoir/pyTelegramBotAPI')
        keyboard_about.add(git_button)
        bot.send_message(message.chat.id,
                         ("Данный бот был написан проекта по информатике\n"
                          "на языке Python 3.7.4 \n"
                          "\n"
                          "При создании этого бота использовалась\n"
                          "библиотека telebot \n"
                          "\n"
                          "Спасибо, что воспользовались ботом!"), reply_markup=keyboard_about)

    elif message.text == 'Послушать творчество':
        k_music = types.InlineKeyboardMarkup()
        music_button = types.InlineKeyboardButton('Перейти в группу ВК', url='https://vk.com/corsomusic')
        k_music.add(music_button)
        k_test = types.ReplyKeyboardMarkup()
        t_button = types.KeyboardButton("Find Yourself.mp3 - C O R S O")
        main_menu_b = types.KeyboardButton('---Главное меню---')
        k_test.row(t_button)
        k_test.row(main_menu_b)
        bot.send_message(message.chat.id, ('''
        Все творчество ты можешь услышать
         
либо в группе ВК или прям здесь
        
выбери  более удобный  формат для прослушивания'''), reply_markup=k_music)
        bot.send_message(message.chat.id, text="[downside menu updated]", reply_markup=k_test)
    elif message.text == 'Перезапустить бота':
        bot.send_message(message.chat.id, 'Что бы перезапустить бота нажмите на эту кнопку (/start)')
    elif message.text == "Find Yourself.mp3 - C O R S O":
        bot.send_audio(message.chat.id, audio=('CQADAgADWwQAAuKqkEufvu_EP2wJPhYE'), performer='c o r s o')
    elif message.text == '---Главное меню---':
        bot.send_message(message.chat.id, 'Что бы выйти в главное меню бота нажмите на эту кнопку (/start)')


@bot.message_handler(content_types=['audio', 'text'])
def music_sender(message):
    if message.text == "Find Yourself":
        bot.send_audio(message.chat.id, audio=('CQADAgADWwQAAuKqkEufvu_EP2wJPhYE'), performer='c o r s o')


@bot.message_handler(content_types=['sticker', 'photo', 'audio'])
def sticker_id(message):
    print(message)




bot.polling()

