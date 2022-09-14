from aiogram import types
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('post', 'action')

def git_line():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = ['delete', 'edit']
    keyboard.add(types.InlineKeyboardButton(text='delete', callback_data=cb.new('delete')),
                 types.InlineKeyboardButton(text='edit', callback_data=cb.new('edit'))
                 )