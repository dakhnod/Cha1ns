from _thread import start_new_thread
import time

class Dummy:
	def delayed(self):
		time.sleep(1)
		self.callback(__name__)

	def setup(self, callback_):
		self.callback = callback_
		start_new_thread(self.delayed, ())
	
	def cleanup():
		pass
