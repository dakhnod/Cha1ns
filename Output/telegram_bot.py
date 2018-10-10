import telegram

class Telegram_bot:
	def setup(self):
		global bot
		bot = telegram.Bot('593203892:AAEtktfQUr89Mt1q1J_WbwikRHTdWpDqQDo')
	
	
	def sendMessage(self, text):
		bot.sendMessage(chat_id=63620166, text=text)
