import logging,os
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
from random import choice, sample

f = open("dishes.txt", "r")
food = f.read().strip().split()
f.close()

updater = Updater(token = os.environ["TOKEN"], use_context = True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
	string = "要么用 /say 让我说三个吃的，要么就复读你！\n 菜名来自 https://home.meishichina.com/recipe-menu.html"
	context.bot.send_message(chat_id = update.effective_chat.id, text = string)
start_handler = CommandHandler('start', start)

def say(update, context):
	preword = ["试试","吃","要么吃","还是吃","果然吃","超推荐","去吃","一起吃"]
	postword = ["吧","哈","噢","哦","呀","咯","喵"]
	string = "{}{}{}～".format(choice(preword),"，".join(sample(food, 3)),choice(postword))
	context.bot.send_message(chat_id = update.effective_chat.id, text = string)
say_handler = CommandHandler('say', say)

#复读
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def echo_sticker(update, context):
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=update.message.sticker)


echo_handler = MessageHandler(Filters.text, echo)
echo_sticker_handler = MessageHandler(Filters.sticker, echo_sticker)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(say_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(echo_sticker_handler)

updater.start_polling()
