from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

router: Router = Router()

@router.message(CommandStart())
async def proccessstart(message: Message):
    await message.answer(text=f"{LEXICON_RU['/start']}: {message.from_user.first_name}")

@router.message(Command(commands='help'))
async def proccesshelp(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

