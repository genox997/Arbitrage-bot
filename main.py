#!/usr/bin/env python
# -*- coding: utf-8 -*-

import schedule
import telepot
import time
from arbitrage import catch
from telepot.loop import MessageLoop


TOKEN = 'blablablabla'
my_id = 1234

def search():
    odds=catch()
    for odd in odds:
        if hasattr(odd, 'w_amount'):
            src_msg = "Match: " + odd.p1  + " vs " + odd.p2 + "\n" \
                      + "1: " + odd.win + " X: " + odd.draw + " 2: " + odd.lost + "\n" \
                      + "Bet: " +  str(odd.w_amount) + "(1) " +  str(odd.d_amount) + "(X) " +  str(odd.l_amount) + "(2) \n" \
                      + "Profit = " + str(odd.profit) + "%"


        else:
            src_msg= "Match: " + odd.p1  + " vs " + odd.p2 + "\n" \
                      + "1: " + odd.q1 + " 2: " + odd.q2 + "\n" \
                      + "Bet: " + str(odd.p1_amount) + " (1)  " + str(odd.p2_amount) + " (2)  \n" \
                      + "Profit = " + str(odd.profit) + "%"
        print(src_msg)
        bot.sendMessage(my_id,src_msg)


def handle(msg):
    print("Message: " + msg['text'])

    if msg['from']['id'] == my_id and msg['text'] == "/search":
        bot.sendMessage(my_id,"Searching...")
        search()


bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()
schedule.every().day.at('17:08').do(search)

while 1:
    schedule.run_pending()
    time.sleep(10)
