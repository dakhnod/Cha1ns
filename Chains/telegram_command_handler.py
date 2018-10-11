import Input,Output
from Input import telegram_bot
from Output import front_camera


def callback(params):
	telegram = Input_telegram_bot
	text = params[0].message.text
	id = params[0].message.chat_id
	if not text.startswith("/"):
		telegram.respondMessage(id, "sorry, i understand only commands")
	elif text.startswith("/picture"):
		telegram.respondImage(id, Output_front_camera.capture())
	else:
		telegram.respondMessage(id, "sorry, unknown command") 
	return True

def setup():
	return [Input.telegram_bot,Output.front_camera]
