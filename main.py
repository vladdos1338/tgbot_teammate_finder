from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
from requests_to_db import brawl_stars, fortnite, gta5, cs_go, valorant, dota2, pubg, wow, minecraft, add_user_to_db
from config import BOT_TOKEN


# Определяем функцию-обработчик сообщений.
async def start(update, context):
    print(f"Пользователь {update.message.from_user.first_name} запустил бота.")
    add_user_to_db(update)
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
    application.add_handler(CommandHandler('brawl_stars', brawl_stars))
    application.add_handler(CommandHandler('valorant', valorant))
    application.add_handler(CommandHandler('gta5', gta5))
    application.add_handler(CommandHandler('dota2', dota2))
    application.add_handler(CommandHandler('cs_go', cs_go))
    application.add_handler(CommandHandler('minecraft', minecraft))
    application.add_handler(CommandHandler('wow', wow))
    application.add_handler(CommandHandler('pubg', pubg))
    application.add_handler(CommandHandler('fortnite', fortnite))

    # Запускаем приложение.
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()