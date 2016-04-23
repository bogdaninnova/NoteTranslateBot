# -*- coding: utf-8 -*-
import src.config
import telebot
from telebot import types
import time
import urllib.request
import psycopg2
from urllib.parse import quote
import xml.etree.ElementTree as ET

conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='191993'")

def listener(messages):
    for m in messages:
        if m.content_type == 'text':

            if m.text == '/help':
                bot.send_message(m.chat.id, 'Press /language for language choosing')
                break

            if m.text == '/test':
                bot.send_message(m.chat.id, 'Press /language for language choosing')
                break

            if m.text == '/language':
                markup = types.ReplyKeyboardMarkup()
                markup.row('sq', 'en', 'ar', 'hy', 'az', 'eu', 'be', 'bg', 'bs', 'cy', 'vi', 'hu', 'ht', 'gl', 'nl')
                markup.row('el', 'ka', 'da', 'he', 'id', 'ga', 'it', 'is', 'es', 'ca', 'ky', 'zh', 'ko', 'la', 'lv')
                markup.row('lt', 'mg', 'ms', 'mt', 'mk', 'mn', 'de', 'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk')
                markup.row('sl', 'sw', 'tg', 'th', 'tl', 'tt', 'tr', 'uz', 'uk', 'fi', 'fr', 'hr', 'cs', 'sv', 'ja')
                markup.row()
                bot.send_message(m.chat.id, "Choose destination language:", reply_markup=markup)
                break
            if m.text in ['sq', 'en', 'ar', 'hy', 'az', 'eu', 'be', 'bg', 'bs', 'cy', 'vi', 'hu', 'ht', 'gl', 'nl',
                          'el', 'ka', 'da', 'he', 'id', 'ga', 'it', 'is', 'es', 'ca', 'ky', 'zh', 'ko', 'la', 'lv',
                          'lt', 'mg', 'ms', 'mt', 'mk', 'mn', 'de', 'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk',
                          'sl', 'sw', 'tg', 'th', 'tl', 'tt', 'tr', 'uz', 'uk', 'fi', 'fr', 'hr', 'cs', 'sv', 'ja']:
                bot.send_message(m.chat.id, "You chose " + m.text, reply_markup=types.ReplyKeyboardHide())

                conn.cursor().execute('INSERT INTO usersLanguage(UserId, lang) values(%s, %s)'
                                      ' ON CONFLICT (UserId) DO UPDATE SET Lang = EXCLUDED.Lang',
                                      (str(m.chat.id), m.text))
                conn.commit()
                break

            cur = conn.cursor()
            cur.execute('SELECT lang FROM usersLanguage where UserId = 119970632', m.chat.id)
            row = cur.fetchone()
            if row is None:
                lang = 'en'
            else:
                lang = row[0]

            url = 'https://translate.yandex.net/api/v1.5/tr/translate?key='\
                  + src.config.yandexToken + '&text='+quote(m.text)+'&lang='+lang

            f = urllib.request.urlopen(url)
            root = ET.fromstring(f.read().decode('utf-8'))
            for tr in root.iter():
                if tr.tag == 'text':
                    bot.send_message(m.chat.id, tr.text)
                    if tr.text != m.text:
                        conn.cursor().execute("INSERT INTO words(user_id, word, rating)"
                                              " values(%s, %s, %s) ON CONFLICT (user_id, word) DO NOTHING",
                                              (str(m.chat.id), m.text, 100))
                    conn.commit()

if __name__ == '__main__':
    bot = telebot.TeleBot(src.config.botToken)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
    while True:
        time.sleep(200)