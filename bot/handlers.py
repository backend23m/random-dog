from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from .dog_image import get_dog_image


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        text=f'Asslomu alaykum {user.full_name}! press dog button for getting dog random image.',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='🐶')]],
            resize_keyboard=True
        )
    )

def dog(update: Update, context: CallbackContext):
    image = get_dog_image()
    update.message.reply_photo(
        photo=image,
        caption='<b><i>a random dog image.</i></b>',
        parse_mode='HTML'
    )
