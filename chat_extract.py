from telegram.ext import *
import telegram
import threading
from telegram.error import *
import ctypes


class ChatIDExtractor(threading.Thread):
        def __init__(self,token):
                self.token = token
                self.chat_id = None
                threading.Thread.__init__(self)
                self.updater = Updater(token=token,use_context=True)
                self.dispatcher = self.updater.dispatcher

        def get_id(self):
                if hasattr(self, '_thread_id'): 
                    return self._thread_id 
                for id, thread in threading._active.items(): 
                    if thread is self: 
                        return id
   
        def raise_exception(self): 
                thread_id = self.get_id()
                res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit)) 
                if res > 1: 
                    ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
                    print('pensi')
                    return "lol"

        def start(self):
                self.dispatcher.add_handler(MessageHandler(Filters.text,self.echo))
                self.dispatcher.add_handler(CommandHandler('start', self.bot_start))
                self.dispatcher.add_error_handler(self.error_callback)
                print("Started polling for messages. Send a message to the bot you have created so that the program can extract the chat id, which you can use for the notification mechanism.")
                self.updater.start_polling()

        def chat_id_extraction(self,update,context):
                print("Received msg '{}'".format(update.message.text.encode()))
                self.chat_id = update._effective_chat.id
                msg = "Chat ID "+str(self.chat_id)+" extracted. Please use this chat for notification. Example : \n\nPrinter("+str(self.chat_id)+").print(msg)\n\nOR\n\np=Printer(API_TOKEN,"+str(self.chat_id)+")\np.print(msg)\n\nIn case this chat thread is lost, please use ChatIDExtractor(API_TOKEN).start() to extract the new chat id."
                print(msg)
                context.bot.send_message(chat_id=self.chat_id,text=msg)
                msg = "\n\n\nPlease exit the program and use the chat id statically"
                print(msg)
                context.bot.send_message(chat_id=self.chat_id,text=msg)

        def bot_start(self,update,context):
                self.chat_id_extraction(update,context)

        def echo(self,update,context):
                self.chat_id_extraction(update,context)

        def error_callback(self, update, context):
                try:
                    raise context.error
                except Exception as e:
                    print(str(e))