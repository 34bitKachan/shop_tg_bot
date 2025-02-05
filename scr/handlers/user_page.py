from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram import Router, F
from scr.filters.chat_type import ChatTypeFilter
from scr.database.controller import DataBase
router_user_page = Router()
router_user_page.message.filter(ChatTypeFilter(chat_type="private"))

aa = 543

@router_user_page.message(Command("page"))
async def show_page(mes: Message):
    name = mes.chat.first_name
    await DataBase.add_user(name)
    await mes.answer(f"Вы " + mes.chat.first_name)
