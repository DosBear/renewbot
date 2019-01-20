
# -*- coding: utf-8 -*-
import telebot
import logging
from timeout import timeout
from telebot import apihelper
from config import SECRETS, START_MESSAGE

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(SECRETS['telegram']['token'], threaded=True)

if SECRETS['telegram']['proxy_ip'] != "":
    apihelper.proxy = {
        'http': "http://{0}:{1}".format(SECRETS['telegram']['proxy_port'], SECRETS['telegram']['proxy_ip']), 
        'https': "https://{0}:{1}".format(SECRETS['telegram']['proxy_port'], SECRETS['telegram']['proxy_ip'])}

#@timeout(15)
def send_all(text):
    for user in SECRETS['telegram']['public_users']:
        try:
            bot.send_message(user, text)
        except Exception as e:
            logging.exception("sendall error {0}".format(e))
            return
    logging.warning(text)

#@timeout(15)
def send_private(text):
    for user in SECRETS['telegram']['private_users']:
        try:
            bot.send_message(user, text)
        except Exception as e:
            logging.exception("send_private error {0}".format(e))
            return
    logging.warning(text)

send_private(START_MESSAGE)
