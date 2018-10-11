from telegram.ext import Updater,MessageHandler, CommandHandler, Filters
import logging                                                                                                                                                                                                                                

class Telegram_bot:

	def handler(self, bot, update):
		self.callback(__name__, update)
	
	def setup(self):
		logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
		self.updater = Updater(token='593203892:AAEtktfQUr89Mt1q1J_WbwikRHTdWpDqQDo')
		dispatcher = self.updater.dispatcher
		
		echo_handler = MessageHandler(Filters.text, self.handler)
		commandHandler = CommandHandler(["picture", "test"], self.handler)	

		dispatcher.add_handler(echo_handler)
		dispatcher.add_handler(commandHandler)

		self.updater.start_polling()

	def cleanup(self):
		self.updater.stop()
	
	def respondMessage(self, chatid, text):
		self.updater.bot.sendMessage(chat_id=chatid, text=text)

	def respondImage(self, chatid, imagePath):
		self.updater.bot.sendPhoto(chat_id=chatid, photo=open(imagePath, 'rb'))
	
	def sendImage(self, imagePath):
		self.updater.bot.sendPhoto(chat_id=63620166, photo=open(imagePath, 'rb'))
	
	def sendMessage(self, text):
		self.updater.bot.sendMessage(chat_id=63620166, text=text)
