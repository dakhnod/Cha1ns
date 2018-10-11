from picamera import PiCamera
import time
from os.path import abspath,dirname

class Front_camera:
	def setup(self):
		camera = self.camera = PiCamera()
		camera.rotation = 180
		camera.start_preview()
	
	def cleanup(self):
		self.camera.stop_preview()

	def capture(self):
		file = dirname(__file__) + "/images/" + str(time.time()) + ".jpg"
		self.camera.capture(file)
		return file
