from telegram import ReplyKeyboardMarkup
from telegram.ext import *
from requests_to_db import brawl_stars, fortnite, gta5, cs_go, valorant, dota2, pubg, wow, minecraft, add_user_to_db
from requests_to_db import contact
from config import BOT_TOKEN


# Определяем функцию-обработчик сообщений.
async def start(update, context):
    user_id = update.message.from_user.username
    print(f"Пользователь {user_id} запустил бота.")
    # Если у пользователя нет никнейма, то бот просит его создать
    if user_id == None:
        await update.message.reply_text("Чтобы найти союзника создайте себе username в настройках телеграмма!")
    else:
        add_user_to_db(update)
        keyboard = [['/brawl_stars', '/valorant', '/gta5'],
                    ['/dota2', '/cs_go', '/minecraft'],
                    ['/wow', '/pubg', '/fortnite']]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)
        await update.message.reply_text('Привет! Хочешь найти себе напарников для игры? Тогда выбери в какие игры ты играешь:', reply_markup=reply_markup)


async def contact_response(update, context):
    await update.message.reply_text('Напишите какую-либо информацию о себе, которую увидит ваш будущий напарник:')
    return 1


def stop():
    pass


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    start_message = CommandHandler('start', start)
    contact_info = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('contact', contact_response)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(filters.TEXT, contact)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    # Регистрируем обработчики в приложении.
    application.add_handler(start_message)
    application.add_handler(contact_info)
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