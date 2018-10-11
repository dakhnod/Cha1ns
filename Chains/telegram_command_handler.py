import Output,Input
from Input import telegram_bot
from Output import telegram_bot


def callback(params):
	telegram = Input_telegram_bot
	text = params[0].message.text
	if not text.startswith("/"):
		telegram.sendMessage("sorry, i understand only commands")
		return
	
	if text.startswith("/picture "):
		pass
	else:
		telegram.sendMessage("sorry, unknown command") 
		

def setup():
	return [Input.telegram_bot]
