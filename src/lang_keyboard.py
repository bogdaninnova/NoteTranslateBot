            # if m.text == '/lang':
            #     markup = types.ReplyKeyboardMarkup()
            #     markup.row('sq', 'en', 'ar', 'hy', 'az', 'eu', 'be', 'bg', 'bs', 'cy', 'vi', 'hu', 'ht', 'gl', 'nl')
            #     markup.row('el', 'ka', 'da', 'he', 'id', 'ga', 'it', 'is', 'es', 'ca', 'ky', 'zh', 'ko', 'la', 'lv')
            #     markup.row('lt', 'mg', 'ms', 'mt', 'mk', 'mn', 'de', 'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk')
            #     markup.row('sl', 'sw', 'tg', 'th', 'tl', 'tt', 'tr', 'uz', 'uk', 'fi', 'fr', 'hr', 'cs', 'sv', 'ja')
            #     markup.row()
            #     bot.send_message(m.chat.id, "Choose destination language:", reply_markup=markup)
            #     break
            # if m.text in ['sq', 'en', 'ar', 'hy', 'az', 'eu', 'be', 'bg', 'bs', 'cy', 'vi', 'hu', 'ht', 'gl', 'nl',
            #               'el', 'ka', 'da', 'he', 'id', 'ga', 'it', 'is', 'es', 'ca', 'ky', 'zh', 'ko', 'la', 'lv',
            #               'lt', 'mg', 'ms', 'mt', 'mk', 'mn', 'de', 'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk',
            #               'sl', 'sw', 'tg', 'th', 'tl', 'tt', 'tr', 'uz', 'uk', 'fi', 'fr', 'hr', 'cs', 'sv', 'ja']:
            #     bot.send_message(m.chat.id, "You chose " + m.text, reply_markup=types.ReplyKeyboardHide())
            #
            #     conn.cursor().execute('INSERT INTO usersLanguage(UserId, lang) values(%s, %s)'
            #                           ' ON CONFLICT (UserId) DO UPDATE SET Lang = EXCLUDED.Lang',
            #                           (str(m.chat.id), m.text))
            #     conn.commit()
            #     break

            # cur = conn.cursor()
            # cur.execute('SELECT lang FROM usersLanguage where UserId = %s', [m.chat.id])
            # row = cur.fetchone()
            # if row is None:
            #     lang = 'en'
            # else:
            #     lang = row[0]