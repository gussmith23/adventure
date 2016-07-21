import telebot
import configparser

# get config
config = configparser.ConfigParser()
config.read("character_creator_bot.cfg")

# get bot
bot = telebot.TeleBot(config['telegram_bot_api']['telegram_token'])
lastUpdate = 0;