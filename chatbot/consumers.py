import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# 🔹 إنشاء بوت الدردشة وتدريبه على اللغات
chatbot = ChatBot("JobBoardBot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")  # يمكنك إضافة "chatterbot.corpus.arabic" للعربية

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_message = data['message'].strip()

        # 🔹 استدعاء الرد من ChatterBot
        bot_response = str(chatbot.get_response(user_message))

        await self.send(text_data=json.dumps({'message': bot_response}))
