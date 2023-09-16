from enum import IntEnum

import telegram
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove

from prostir.domain import massages

send_contact_button = telegram.KeyboardButton(text=massages.REQUEST_CONTACT, request_contact=True)
keyboard = [[send_contact_button]]


class State(IntEnum):
    START = 1
    REQUEST_CONTACT = 2
    END = ConversationHandler.END


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> State:
    await update.message.reply_text(
        massages.WELLCOME,
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return State.REQUEST_CONTACT


async def save_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> State:
    if update.message.contact.user_id != update.message.from_user.id:
        await update.message.reply_text(
            massages.ON_INCORRECT_CONTACT,
        )
        return State.REQUEST_CONTACT

    print(update.message.contact.phone_number)
    await update.message.reply_text(
        massages.CONTACT_WAS_SAVED,
        reply_markup=ReplyKeyboardRemove(),
    )

    return State.END


async def fallback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> State:
    await update.message.reply_text(
        massages.ON_UNKNOWN_MESSAGE
    )
    return State.REQUEST_CONTACT

bot = ApplicationBuilder().token("6053672183:AAHsWiGgslTfeR5dgRjcSeliufE_a6Lt5JM").build()
bot.add_handler(
    ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            State.REQUEST_CONTACT: [MessageHandler(filters.CONTACT, save_contact)],
        },
        fallbacks=[MessageHandler(filters.ALL, fallback_handler)],
    ),
)
