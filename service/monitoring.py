import requests
import telebot
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup
import os
import re


def main():
    name = os.environ.get('SERVICE_NAME', 'noname')
    url = os.environ.get('SERVICE_URL', '')
    chat_id = os.environ.get('TELEGRAM_CHAT', '')
    api_token = os.environ.get('TELEGRAM_BOT_TOKEN', '')
    bot = telebot.TeleBot(api_token, parse_mode=None)
    
    while True:
        r = requests.get(url)
        if r.status_code != 200:
            dt = str(datetime.now())
            try:
                r.encoding = 'utf-8'
                soup = BeautifulSoup(r.text, 'lxml')
                for tag in soup.find_all("title"):
                    print(tag)
                p = re.compile(r'<.*?>')
                message = p.sub('', str(tag))
            except Exception as e:
                message = str(r.status_code)+': '+str(e)
            bot.send_message(
                chat_id, 
                name+'\n'+message+'\n'+url+'\n'+dt
                )
            sleep(59)
        sleep(1)


if __name__ == '__main__':
    main()
