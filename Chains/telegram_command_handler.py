import Input
from Input import telegram_bot


def callback(params):
	telegram = Input_telegram_bot
	text = params[0].message.text
	id = params[0].message.chat_id
	if not text.startswith("/"):
		telegram.respondMessage(id, "sorry, i understand only commands")
		return
	
	if text.startswith("/picture "):
		telegram.respondMessage(id, "stub!")
	else:
		telegram.respondMessage(id, "sorry, unknown command") 
		

def setup():
	return [Input.telegram_bot]
