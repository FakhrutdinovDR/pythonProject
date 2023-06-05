from random import choice
from keyboards import keyboards
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

router: Router = Router()

# Выбор нужного варианта и валидация
def validate(message: Message, variant: str):
    if message.text == variant:
        return None
    elif (message.text == 'Камень' and variant == 'Ножницы') or (message.text == 'Ножницы' and variant == 'Бумага') or \
            (message.text == 'Бумага' and variant == 'Камень'):
        return True
    else:
        return False

@router.message(CommandStart())
async def proccessstart(message: Message):
    await message.answer(text=f"{LEXICON_RU['/start']}", reply_markup=keyboards.keyboardonstart)

@router.message(Command(commands='help'))
async def proccesshelp(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=keyboards.keyboardonstart)

@router.message(F.text == 'Давай')
async def initgame(message: Message):
    await message.answer(text=LEXICON_RU['rungame'], reply_markup=keyboards.keyboardgame)

@router.message(F.text == 'Не хочу')
async def stopgame(message: Message):
    await message.answer(text=LEXICON_RU['stopgame'])

@router.message(F.text.in_({'Камень', 'Ножницы', 'Бумага'}))
async def gamelogic(message: Message):
    variant = choice(['Камень', 'Ножницы', 'Бумага'])
    if validate(message, variant) is not None:
        result = ("Ты проиграл", "Ты победил")[validate(message, variant)]
    else:
        result = 'У нас ничья'
    await message.answer(text=f'Мой вариант: {variant}\n'
                              f'Ты выбрал: {message.text}\n'
                              f'{result}\n'
                              f'Сыграем еще?', reply_markup=keyboards.keyboardonstart)
