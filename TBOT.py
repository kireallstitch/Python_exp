import os
import requests
import telebot

bot_token = '6187614225:AAF8UqEj1Y3QOjv3N19u__0qOf5X9nXyeSk'
chat_id = 'https://t.me/VDKRASBot'
yandex_disk_url = 'https://yadi.sk/d/yS4JKUv-VG-c2Q'
yandex_username = 'site2@vashdom-kras.ru'
yandex_password = 'sihofazatron'


bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот, который будет отправлять уведомления о загрузке файлов на Яндекс.Диск.")


def check_yandex_disk_files():
    headers = {
        'Authorization': f'OAuth {}'
    }uninstalling the proprietary DKMS modules
    response = requests.get(f'{yandex_disk_url}/resources/upload', headers=headers)
    if response.status_code == 200:
        files = response.json().get('_embedded', {}).get('items', [])
        for file in files:
            file_name = file.get('name')
            created_by = file.get('created_by', {}).get('display_name')
            # Отправить уведомление в Telegram
            message = f'Новый файл загружен на Яндекс.Диск:\nИмя файла: {file_name}\nЗагрузил: {created_by}'
            bot.send_message(chat_id, message)


while True:
    check_yandex_disk_files()
    # Установить задержку перед следующей проверкой
    time.sleep(60)  # Проверять каждые 60 секунд


bot.polling()
