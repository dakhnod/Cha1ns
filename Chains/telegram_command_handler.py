import Output,Input
from Input import telegram_bot
from Output import telegram_bot


def callback(params):
	text = params[0].message.text
	if not text.startswith("/"):
		telegram.sendMessage("sorry, i understand only commands")
		return
	
	if text.startswith("/picture "):
		pass
	else:
		telegram.sendMessage("sorry, unknown command") 
		

def setup(chain, moduleObjects):
	chain(Input.telegram_bot, Output.telegram_bot, callback=callback)
	global telegram
	telegram = moduleObjects[Output.telegram_bot]
