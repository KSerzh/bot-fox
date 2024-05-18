import os
import telebot

# Получите токен бота от BotFather и установите его в переменную окружения
BOT_TOKEN = os.environ.get('6247927588:AAGkpTTpRqUzL6rbt4iaf74TqONTZ_xj_34')
bot = telebot.TeleBot(BOT_TOKEN)

class IrregularVerbsBot:
    def __init__(self):
        self.verbs = {
            "be": ["was, were", "been", "быть, являться"],
            "beat": ["beat", "beaten", "бить, колотить"],
            # Добавьте остальные глаголы сюда
        }

    def get_verb_forms(self, verb):
        if verb in self.verbs:
            return self.verbs[verb]
        else:
            return None

    def main(self):
        @bot.message_handler(func=lambda message: True)
        def handle_message(message):
            verb = message.text.strip().lower()
            forms = self.get_verb_forms(verb)
            if forms:
                response = f"Past Simple: {forms[0]}\nPast Participle: {forms[1]}\nПеревод: {forms[2]}"
            else:
                response = "Глагол не найден. Попробуйте еще раз."
            bot.reply_to(message, response)

        bot.polling(none_stop=True)

if __name__ == "__main__":
    bot = IrregularVerbsBot()
    bot.main()