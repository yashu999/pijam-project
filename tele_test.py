import telepot
from cam_test import capture

bot = telepot.Bot('971914614:AAHc4Oo9Rblvc71nfZaNAfH-9nMtbge1a0s')

a=bot.getUpdates()[-1]

#print (a)
x=(a['message']['text'])
print('Recieved msg:',x)

moist = 1234
if x=='Plant':
    q = capture()
    photo = open('camworks.jpg', 'rb')
    bot.sendPhoto(597318456,photo, caption='Plant Pic',)
    bot.sendMessage(597318456,moist)
    print('sent photo')
    