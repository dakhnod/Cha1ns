import Output,Input
from Input import telegram_bot
from Output import telegram_bot


def callback(*params):
	print(params)

def setup(chain, moduleObjects):
	chain(Input.telegram_bot, Output.telegram_bot, callback=callback)
