from telegram.ext import Updater,MessageHandler, CommandHandler, Filters
import _thread
import logging                                                                                                                                                                                                                                

class Telegram_bot:
	def start(self, updater):
		updater.start_polling()

	def echo(self, bot, update):
		#bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text[::-1])
		self.callback(__name__, bot, update.message)
	
	def setup(self, callback_):
		self.callback = callback_
                                                                                                                                                                                                                                              
		logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
		updater = Updater(token='593203892:AAEtktfQUr89Mt1q1J_WbwikRHTdWpDqQDo')
		dispatcher = updater.dispatcher
		echo_handler = MessageHandler(Filters.text, self.echo)
		dispatcher.add_handler(echo_handler)
		_thread.start_new_thread(self.start, (updater,))

	def cleanup():
		pass
