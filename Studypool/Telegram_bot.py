from Studypool import const
import telebot
from telebot.types import Update


telegram_bot = telebot.TeleBot(const.API)

def run_bot():
    const.last_upd_id = None
    telegram_bot = telebot.TeleBot(const.API)
    updates = telegram_bot.get_updates()
    for up in updates:
        ch_id = up.message.chat.id
        const.waiting_pass_users.add(ch_id)
        const.last_upd_id = up.update_id + 1

def upd():
    updates = telegram_bot.get_updates(offset= const.last_upd_id)
    for up in updates:
        txt = up.message.text
        if txt == "/start":
            welcome(message = up.message)
        elif txt == "/help":
            help(up.message)
        else:
            handler(message = up.message)
        const.last_upd_id = up.update_id + 1



@telegram_bot.message_handler(commands = ['help'])
def help(message):
    telegram_bot.reply_to(
        message, 
        "Hello there, I am a Studypool helper develepod by Kerillos. \n I get data about newly posted jobs on Studypool and let you know immediately. type or click /start to begin. :)"
    )



@telegram_bot.message_handler(commands = ['start'])
def welcome(message):
    telegram_bot.reply_to(message, "Hello, I am a Studypool helper developed by Kerillos.")
    if message.chat.id in const.active_users:
        telegram_bot.send_message(message.chat.id, "You are already authenticated")
    else:
        const.waiting_pass_users.add(message.chat.id)
        telegram_bot.send_message(message.chat.id, "Please send password to get authenticated")



@telegram_bot.message_handler()
def handler(message):
    if message.chat.id in const.active_users:
        telegram_bot.send_message(message.chat.id , "I am sorry, I am not programmed to reply to messages.")
    elif message.chat.id in const.waiting_pass_users:
        txt = message.text
        ch_id = message.chat.id
        if txt == const.bot_password:
            telegram_bot.send_message(ch_id, "Correct Password. Welcome on board, I am currently active. :)")
            const.active_users.add(ch_id)
            const.waiting_pass_users.remove(ch_id)
        else:
            telegram_bot.send_message(ch_id, "Incorrect Password, please try again")
    else:
        ch_id = message.chat.id
        telegram_bot.send_message(ch_id, "I am sorry I don't recognise you, please type /start to start the bot running. :)")

def send (mes = ""):
    upd()
    for user in const.active_users:
        telegram_bot.send_message(user, mes)

