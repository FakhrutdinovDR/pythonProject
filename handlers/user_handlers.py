from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

@dp.message(CommandStart())
async def proccessstart(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

@dp.message(Command(commands='help'))
async def proccesshelp(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

