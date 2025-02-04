from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram import Router, F

router_user_page = Router()
router_user_page.message.filter(F.chat.type == "private")


@router_user_page.message(Command("page"))
async def show_page(mes: Message):
    await mes.answer(f"Вы " + mes.chat.first_name)
