import requests
class Telegram:
	def setup(self):
		print("setting up telegram module...")
	
	def output(*params):
		requests.get("https://api.telegram.org/bot521006452:AAF6NQA0gjOs-6HNnvXuYcwcwKT5BKt08WI/sendMessage?text=" + params[1] + "&chat_id=63620166")
