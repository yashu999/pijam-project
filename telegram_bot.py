import configparser
import io
import os.path
import time
from io import BytesIO

import VideoCapture
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def on_chat_message(msg):
    try:
        username = msg.get('from').get('username')
    except:
        username = 'Yesh999Bot'
    content_type, chat_type, chat_id, = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Take photo', callback_data='take_photo')],
    ])

    bot.sendMessage(chat_id, 'Hi, ' + username, reply_markup=keyboard)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Take another photo', callback_data='take_photo')],
    ])

    if query_data == 'take_photo':
        camera = VideoCapture.Device()
        camera.setResolution(1920, 1080)
        image = camera.getImage()
        image = image.rotate(90, expand=True)
        temp_file = BytesIO()
        image.save(temp_file, "jpeg")
        temp_file.seek(0)
        bot.sendPhoto(from_id, temp_file, reply_markup=keyboard)
        temp_file.close()
        camera = None


camera = VideoCapture.Device()

if not os.path.isfile('./config.ini'):
    # Create the configuration file as it doesn't exist yet
    cfgfile = open('./config.ini', 'w', encoding="utf-8")

    # Add content to the file
    Config = configparser.ConfigParser()
    Config.add_section(u'TG API')
    Config.set(u'TG API',u'token', u'971914614:AAHc4Oo9Rblvc71nfZaNAfH-9nMtbge1a0s')
    Config.write(cfgfile)
    cfgfile.close()

# Load the configuration file
with open("config.ini", encoding='utf-8') as f:
    sample_config = f.read()
config = configparser.RawConfigParser(allow_no_value=False)
config.read_file(io.StringIO(sample_config))

TOKEN = config.get('TG API', 'token')

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while True:
    time.sleep(1)
