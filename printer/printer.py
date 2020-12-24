import telegram

class Printer:
        def __init__(self,token,chat_id=None):
                self.token = token
                self.chat_id = chat_id

        def print(self,text):
                telegram.Bot(token=self.token).send_message(chat_id=self.chat_id,text=text)

