from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons: dict[str, KeyboardButton] = {'startyes': KeyboardButton(text='Давай'),
                                      'startno': KeyboardButton(text='Не хочу'),
                                      'stone': KeyboardButton(text='Камень'),
                                      'clips': KeyboardButton(text='Ножницы'),
                                      'paper': KeyboardButton(text='Бумага')}

# Кнопки предложения начала игры
keyboardonstart = ReplyKeyboardMarkup(keyboard=[[buttons['startyes'], buttons['startno']]],
                                      resize_keyboard=True, one_time_keyboard=True)

# Кнопки вариантов игры
keyboardgame = ReplyKeyboardMarkup(keyboard=[[buttons['stone'], buttons['clips'], buttons['paper']]],
                                   resize_keyboard=True)
