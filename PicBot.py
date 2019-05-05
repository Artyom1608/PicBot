import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import sys,time
import datetime
from google_images_download import google_images_download
import random

now = datetime.datetime.now()

def searchPhoto(keyword):
    orig_stdout = sys.stdout
    f = open('URLS.txt', 'w')
    sys.stdout = f

    try:
        response = google_images_download.googleimagesdownload()

        arguments = {"keywords"     : keyword,
                     "limit"        : 5,
                     "print_urls"   : True,
                     "size"         : ">2MP",
                     }
        paths = response.download(arguments)
    except :
        print("Erore di aray")
        pass


    sys.stdout = orig_stdout
    f.close()

    with open('URLS.txt') as f:
        content = f.readlines()
    f.close()

    urls = []
    for j in range(len(content)):
        if content[j][:9] == 'Completed':
            urls.append(content[j-1][11:-1])
    print(urls)

    return urls[random.randint(0,len(urls)-1)]

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(chat_id)
    print(bot.getChat(chat_id)['first_name']+" ha digitato : "+msg['text']+" "+str(now.hour)+":"+str(now.minute))
    if content_type == 'text':
        if msg['text'] == "/start" :
            bot.sendMessage(chat_id,"Ciao %s sono il PicBot, cerca una parola e io ti manderò l'immagine corrispondente" %bot.getChat(chat_id)['first_name'])
        else :
            bot.sendMessage(chat_id,"Sto cercando un immagine...")
            url=searchPhoto(msg['text'])
            print("Url della foto: %s" %url)
            bot.sendMessage(chat_id,"Ecco cosa ho trovato:")
            bot.sendPhoto(chat_id,url)


TOKEN = '885700745:AAHeLVTEg_9eyxLzYA4W8par_jkugJZnMPE'

bot = telepot.Bot(TOKEN)
print(bot.getMe())
bot.message_loop(on_chat_message)
print ('Listening ...')
#Mette il bot sempre in ascolto evitando di far terminare il programma
while 1:

    try:
        time.sleep(60)
    except KeyboardInterrupt:
        print("Bot terminato")
        sys.exit(10)
