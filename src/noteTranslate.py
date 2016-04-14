# -*- coding: utf-8 -*-
import src.config
import telebot
import time
import urllib.request
from urllib.parse import quote
import xml.etree.ElementTree as ET

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            if m.text[0] == '/':
                userText = m.text[1:]
            else:
                userText = m.text
            url = 'https://translate.yandex.net/api/v1.5/tr/translate?key='\
                  + src.config.yandexToken + '&text='+quote(userText)+'&lang=en'
            f = urllib.request.urlopen(url)
            root = ET.fromstring(f.read().decode('utf-8'))
            for tr in root.iter():
                if tr.tag == 'text':
                    bot.send_message(m.chat.id, tr.text)

if __name__ == '__main__':
    bot = telebot.TeleBot(src.config.botToken)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
    while True:
        time.sleep(200)