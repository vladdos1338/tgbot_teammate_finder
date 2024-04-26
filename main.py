from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
from config import BOT_TOKEN


# Определяем функцию-обработчик сообщений.
async def start(update, context):
    print(f"Пользователь {update.message.from_user.first_name} запустил бота.")
    keyboard = [['/brawl_stars', '/valorant', '/gta5'],
                ['/dota2', '/cs_go', '/minecraft'],
                ['/wow', '/pubg', '/fortnite']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)
    await update.message.reply_text('Привет! Хочешь найти себе напарников для игры? Тогда выбери в какие игры ты играешь:', reply_markup=reply_markup)


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    start_message = CommandHandler('start', start)

    # Регистрируем обработчик в приложении.
    application.add_handler(start_message)

    # Запускаем приложение.
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()