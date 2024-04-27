import sqlite3
from telegram.ext import ConversationHandler

con = sqlite3.connect("data/db/teams_db.sqlite")
cur = con.cursor()


games_id = {
    1: 'brawl_stars',
    2: 'valorant',
    3: 'gta5',
    4: 'dota2',
    5: 'cs_go',
    6: 'minecraft',
    7: 'wow',
    8: 'pubg',
    9: 'fortnite'
}


def add_user_to_db(update):
    user_id = update.message.from_user.username
    chat_id = update.message.chat_id
    print(user_id)
    info = cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
    if not info:
        cur.execute("INSERT INTO users(user_id, chat_id) VALUES(?, ?)", (user_id, chat_id,))
    con.commit()


async def contact(update, context):
    user_id = update.message.from_user.username
    message = update.message.text
    cur.execute("UPDATE users SET contact = (?) WHERE user_id = (?)", (message, user_id,))
    con.commit()
    await update.message.reply_text("Ваша информация успешно добавлена! Чтобы найти напарника пишите /find")
    return ConversationHandler.END


async def find(update, context):
    user_id = update.message.from_user.username
    user = cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchall()[0]
    user_games = []
    teammate_games = []
    for i, val in enumerate(user[1:]):
        if val == 1:
            user_games.append(games_id[i])
    while not set(user_games) & set(teammate_games):
        teammate_games = []
        teammate = cur.execute("SELECT * FROM users "
                               "WHERE user_id not in (?) "
                               "ORDER BY RANDOM() LIMIT 1", (user_id,)).fetchall()[0]
        for i, val in enumerate(teammate[1:]):
            if val == 1:
                teammate_games.append(games_id[i])
    intersection_games = ', '.join(list(set(user_games) & set(teammate_games)))
    await update.message.reply_text(f"Напарник найден! Общие игры - "
                                    f"{intersection_games}. ")
    await update.message.reply_text(f"Информация: {teammate[1]}")
    await update.message.reply_text(f"Его телеграм: @{teammate[0]}")
    # Отправляем сообщение, тому, кого нашли
    await context.bot.send_message(text=f'Тебя нашел пользователь @{user[0]}', chat_id=teammate[11])
    await context.bot.send_message(text=f'Его информация: {user[1]}', chat_id=teammate[11])
    await context.bot.send_message(text=f'Ваши общие игры - {intersection_games}', chat_id=teammate[11])


async def brawl_stars(update, context):
    user_id = update.message.from_user.username
    info = cur.execute("SELECT (brawl_stars) FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
    if info:
        cur.execute("UPDATE users SET brawl_stars = (0) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Brawl Stars была успешно удалена из ваших игр')
    else:
        cur.execute("UPDATE users SET brawl_stars = (1) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Brawl Stars была успешно добавлена в ваши игры. '
                                        'Если это всё пишите /contact')
    con.commit()


async def valorant(update, context):
    user_id = update.message.from_user.username
    info = cur.execute("SELECT (valorant) FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
    if info:
        cur.execute("UPDATE users SET valorant = (0) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Valorant была успешно удалена из ваших игр')
    else:
        cur.execute("UPDATE users SET valorant = (1) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Valorant была успешно добавлена в ваши игры. '
                                        'Если это всё пишите /contact')
    con.commit()


async def gta5(update, context):
    user_id = update.message.from_user.username
    info = cur.execute("SELECT (gta5) FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
    if info:
        cur.execute("UPDATE users SET gta5 = (0) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('GTA V была успешно удалена из ваших игр')
    else:
        cur.execute("UPDATE users SET gta5 = (1) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('GTA V была успешно добавлена в ваши игры. '
                                        'Если это всё пишите /contact')
    con.commit()


async def dota2(update, context):
    user_id = update.message.from_user.username
    info = cur.execute("SELECT (dota2) FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
    if info:
        cur.execute("UPDATE users SET dota2 = (0) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Dota 2 была успешно удалена из ваших игр')
    else:
        cur.execute("UPDATE users SET dota2 = (1) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Dota 2 была успешно добавлена в ваши игры. '
                                        'Если это всё пишите /contact')
    con.commit()


async def cs_go(update, context):
    user_id = update.message.from_user.username
    info = cur.execute("SELECT (cs_go) FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
    if info:
        cur.execute("UPDATE users SET cs_go = (0) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Counter Strike 2 была успешно удалена из ваших игр')
    else:
        cur.execute("UPDATE users SET cs_go = (1) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Counter Strike 2 была успешно добавлена в ваши игры. '
                                        'Если это всё пишите /contact')
    con.commit()


async def wow(update, context):
    user_id = update.message.from_user.username
    info = cur.execute("SELECT (wow) FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
    if info:
        cur.execute("UPDATE users SET wow = (0) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('World of tanks была успешно удалена из ваших игр')
    else:
        cur.execute("UPDATE users SET wow = (1) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('World of tanks была успешно добавлена в ваши игры. '
                                        'Если это всё пишите /contact')
    con.commit()


async def pubg(update, context):
    user_id = update.message.from_user.username
    info = cur.execute("SELECT (pubg) FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
    if info:
        cur.execute("UPDATE users SET pubg = (0) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('PUBG была успешно удалена из ваших игр')
    else:
        cur.execute("UPDATE users SET pubg = (1) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('PUBG была успешно добавлена в ваши игры. '
                                        'Если это всё пишите /contact')
    con.commit()


async def fortnite(update, context):
    user_id = update.message.from_user.username
    info = cur.execute("SELECT (fortnite) FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
    if info:
        cur.execute("UPDATE users SET fortnite = (0) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Fortnite была успешно удалена из ваших игр')
    else:
        cur.execute("UPDATE users SET fortnite = (1) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Fortnite была успешно добавлена в ваши игры. '
                                        'Если это всё пишите /contact')
    con.commit()


async def minecraft(update, context):
    user_id = update.message.from_user.username
    info = cur.execute("SELECT (minecraft) FROM users WHERE user_id=?", (user_id,)).fetchone()[0]
    if info:
        cur.execute("UPDATE users SET minecraft = (0) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Minecraft была успешно удалена из ваших игр')
    else:
        cur.execute("UPDATE users SET minecraft = (1) WHERE user_id = (?)", (user_id,))
        await update.message.reply_text('Minecraft была успешно добавлена в ваши игры. '
                                        'Если это всё пишите /contact')
    con.commit()
