# -*- coding: utf-8 -*-
import src.config
import telebot
import time
import urllib.request
import xml.etree.ElementTree as ET



def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            # url = ('https://translate.yandex.net/api/v1.5/tr/translate?key='+src.config.yandexToken+'&text='+m.text+'&lang=en').encode('utf-8')

            userText = m.text.encode('utf-8')
            userText = m.text.encode('ansii')
            print(userText)
            url = 'https://translate.yandex.net/api/v1.5/tr/translate?key=' + src.config.yandexToken + '&text='+userText+'&lang=en'

            # url.encode('utf-8', 'ignore').decode('utf-8')
            # url.encode('ascii', 'ignore')
            # url.encode('ascii', 'replace')
            # url.encode('ascii', 'xmlcharrefreplace')


            print(url)
            f = urllib.request.urlopen(url)
            # root = ET.fromstring(f.read().decode('utf-8'))
            # for translation in root.iter('Translation'):
            #     bot.send_message(m.chat.id, translation.getText())

if __name__ == '__main__':
    bot = telebot.TeleBot(src.config.botToken)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
    while True:
        time.sleep(200)