from telebot import TeleBot
from model import classify

TOKEN = '6533250733:AAHMRsdFY-jRawjGPn5A-pPb5qYT6oa_LvU'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(content_types=['photo'])
def classify_food(message):
    try:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        ext = file_info.file_path.split('.')[-1]
        downloaded_file = bot.download_file(file_info.file_path)
        img_path_save = f"classify_image.{ext}"
        
        with open(img_path_save, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        res = classify(img_path_save)
        bot.send_message(message.chat.id, res)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")

if __name__ == '__main__':
    bot.polling(none_stop=True)
