import src.config
import src.translation
import telebot
import time
import random


def listener(messages):
    for m in messages:
        if m.content_type == 'text':

            if m.text == '/help' or m.text == '/start':
                bot.send_message(m.chat.id, 'Commands:\n'
                                            '/show -- Show word list\n'
                                            '/add "word" -- Add "word" to the list\n'
                                            '/remove "word" -- Remove "word" from your list\n'
                                            '/test -- show one word with translation')
                break

            if m.text == '/add':
                bot.send_message(m.chat.id, 'Type "/add word" for adding word to the list')
                break

            if m.text == '/remove':
                bot.send_message(m.chat.id, 'Type "/remove word" for removing word to the list')
                break

            if m.text == '/show':
                cur = src.translation.conn.cursor()
                cur.execute('SELECT word FROM words where user_id = %s', [str(m.chat.id)])
                count = 0
                while True:
                    row = cur.fetchone()
                    if row is None:
                        break
                    count += 1
                    bot.send_message(m.chat.id, row[0])
                if count == 0:
                    bot.send_message(m.chat.id, 'Your list is empty')
                break

            if m.text == '/test':
                cur = src.translation.conn.cursor()
                cur.execute('SELECT count(1) FROM words where user_id = %s', [str(m.chat.id)])
                row = cur.fetchone()
                count = 0
                if row is not None:
                    count = row[0]
                    if row[0] == 0:
                        bot.send_message(m.chat.id, 'Your list is empty')
                        break
                num = random.randrange(0, count + 1, 1)

                cur = src.translation.conn.cursor()
                cur.execute('SELECT word FROM words where user_id = %s', [str(m.chat.id)])
                while True:
                    row = cur.fetchone()
                    if row is None:
                        break
                    if num == 0:
                        bot.send_message(m.chat.id, row[0])
                        time.sleep(3)
                        bot.send_message(m.chat.id, src.translation.get_translation(row[0]))
                        break
                    num -= 1
                break

            word = m.text

            if m.text[:8] == '/remove ':
                word = m.text[8:]
                cursor = src.translation.conn.cursor()
                cursor.execute('delete from words where user_id = %s and lower(word) = lower(%s)',
                               (str(m.chat.id), word))
                src.translation.conn.commit()
                if cursor.rowcount != 0:
                    bot.send_message(m.chat.id, 'Word "' + word + '" was removed from your list')
                else:
                    bot.send_message(m.chat.id, 'Word "' + word + '" is not in your list')
                break

            is_add = False
            if m.text[:5] == '/add ':
                is_add = True
                word = m.text[5:]

            bot.send_message(m.chat.id, src.translation.get_translation(word, id, is_add))

if __name__ == '__main__':
    bot = telebot.TeleBot(src.config.botToken)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
    while True:
        time.sleep(200)
