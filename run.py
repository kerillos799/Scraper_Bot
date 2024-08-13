from Studypool.bot import parse 
import time
from sched import scheduler
from Studypool import const
import telebot
from telebot.types import Update
from Studypool import Telegram_bot as tele


with parse() as bot:
    tele.run_bot()
    print("bot ran.....")
    tele.send(mes="Openning Studypool....")
    print("message sent")
    bot.frst_page()
    time.sleep(3)
    bot.open_popup()
    time.sleep(3)
    tele.send(mes= "Loging in...")
    bot.login()
    time.sleep(3)
    bot.details(mail = const.gmail , password = const.pas)
    time.sleep(10)
    try:
        bot.ten_rep_popup()
    except:
        print()
    time.sleep(3)
    tele.send(mes= "Openning questions list...")
    bot.open_ques_list()
    time.sleep(20)
    bot.apply_filter()
    tele.send(mes= "I am up and running. :)")
    while (1):
        bot.access_ques()
        time.sleep(10)


    