import telegram
import random


def send_test_message():
    try:
        random_number = random.randint(0, 1000)
        telegram_notify = telegram.Bot("5486552094:AAHerV2KBIDv1zH7rdvYkIyFH6PMrAZWGv8")
        message = "`Số random là {}`".format(random_number)

        telegram_notify.send_message(chat_id="-723967576", text=message,
                                     parse_mode='Markdown')
    except Exception as ex:
        print(ex)

send_test_message()