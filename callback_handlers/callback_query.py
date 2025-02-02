from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold
import states
from aiogram.fsm.context import FSMContext
from keyboard import key_builder as mm

router = Router()


@router.callback_query(F.data.split(':')[0] == 'menu')
async def callback_menu_answer(query: CallbackQuery):
    ...

