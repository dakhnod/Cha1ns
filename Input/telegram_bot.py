from telegram.ext import Updater,MessageHandler, CommandHandler, Filters
import logging                                                                                                                                                                                                                                

class Telegram_bot:
	def start(self):
		self.updater.start_polling()

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
