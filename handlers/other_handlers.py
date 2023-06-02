from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

router: Router = Router()
@router.message()
async def proccessingother(message: Message):
    try:
        await message.send_copy(message.chat.id)
    except:
        await message.answer(text=LEXICON_RU['no_ans'])
