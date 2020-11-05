import time
import math

class Countdown:
	def __init__(self):
		self.start_time = None
		self.limit = 0
		self.current_time = None
		self.started = False

	def start(self, time_limit):
		if(self.started):
			return
		self.start_time = time.perf_counter()
		self.limit = time_limit
		self.started = True

	def hasStarted(self):
		return(self.started)

	def timeLeft(self):
		return(math.floor(time.perf_counter() - self.start_time))

	def isFinished(self):
		if(time.perf_counter() - self.start_time > self.limit):
			self.started = False
			return(True)
		return(False)
