from threading import Thread
import threading
import time

class MyThread(threading.Thread):
	def __init__(self, target = None, args= (), name= None):
		threading.Thread.__init__(self)
		self._name = name
		self._target = target
		self._args = args
	def run(self):
		print(f"Run thread {self.name}")
		if self._target:
			self._target(*self._args)
	def stop(self):
		self._stop()
def cal_square(numbers):
	print("calculate square number")
	for n in numbers:
		time.sleep(0.2)
		print ('square:', n*n)


def cal_cube(numbers):
	print("calculate cube number \n")
	for n in numbers:
		time.sleep(0.2)
		print ('cube:', n*n*n)

arr = [2,3,7,9]
try:
	t = time.time()
	t1 = MyThread(target=cal_square, args=(arr,))
	t2 = MyThread(target=cal_cube, args=(arr,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print ("done in ", time.time()- t)
except Exception as err:
	print (err)

