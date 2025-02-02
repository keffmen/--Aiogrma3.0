from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data_base import base


def builder_menu() -> InlineKeyboardBuilder.as_markup:
    """
    Функция, которая создает клавиатуру для выбора категорий
    :return:
    """

    # Создаем Макет клавиатуры
    markup = InlineKeyboardBuilder()

    # buttons = []
    #
    # for key in menu.keys():
    #     buttons.append(InlineKeyboardButton(text=menu[key]['title'], callback_data=f"menu:{key}"))
    #
    # if menu_id:
    #     # Если не пришли категории в данном меню, то просто делаем кнопку назад
    #     markup.row(InlineKeyboardButton(text='Назад', callback_data=f'back:{menu_id}'))

    return markup.as_markup()