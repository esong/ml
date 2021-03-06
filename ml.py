import argparse
import math
import os
import random
import signal
import sys
import subprocess
import time

class ArgsParser(object):
	def getArgs(self):
		parser = argparse.ArgumentParser(description='the power of ml in one little script')
		parser.add_argument('--training_data', dest='trainingData', help='data for training')
		parser.add_argument('--hadoop', dest="hadoop", help="use hadoop?", default='true')
		parser.add_argument('--iterations', dest="iterations", help='number of iterations', default=-1)
		return parser.parse_args()

class ml(object):

	_DEFAULT_MINIMUM_FILE_SIZE = 10000
	_TRAINING_FILE = None
	_HADOOP = True
	_NUM_ITERATIONS = -1
	_PROCESS_NAME = ""

	def __init__(self, args):
		try:
			self._TRAINING_FILE = os.stat(args.trainingData)
		except:
			self.trainingFailed("how can i learn without any training? ..")
		self._HADOOP = args.hadoop.lower() in ("yes", "true", "t", "1")
		self._NUM_ITERATIONS = int(args.iterations)
		self._PROCESS_NAME = sys.argv[0]

		signal.signal(signal.SIGTERM, self.signalHandler)
		signal.signal(signal.SIGINT, self.signalHandler)

		random.seed()

	def signalHandler(self, inputSignal, frame):
		if inputSignal == signal.SIGTERM: 
			print("\nnice try, but you cannot just stop machine learning...")
		else:
			#Debug line
			#exit(1)
			print("\none cannot simply stop machine learning..")

	def pretrainingChecks(self):
		oneInstanceCheck = subprocess.Popen("ps -ef | grep {0} | grep -v grep".format(self._PROCESS_NAME), shell=True, stdout=subprocess.PIPE)
		oneInstanceCheckResult = oneInstanceCheck.stdout.read()
		if oneInstanceCheckResult.count("\n") > 1:
			self.trainingFailed("don't try to cheat, ml isn't that easy..")

		if self._TRAINING_FILE.st_size < self._DEFAULT_MINIMUM_FILE_SIZE/random.randint(1,100):
			self.trainingFailed("i can't train on this data, please give me more..")

		if self._NUM_ITERATIONS > 0 and self._NUM_ITERATIONS < 1000:
			self.trainingFailed("do you really expect to achieve perfection with almost no iterations? ..")

		print("truly thinking like an ml'er. starting up the training:")

	def trainingFailed(self, extraMsg):
		print("what is the point of ml if you don't even try...")
		print(extraMsg)
		while(True):
			answer = raw_input('retry? [y/n] ')
			if answer == 'y':
				print("may the god of ml bless you..")
				self.main()
			elif answer == 'n':
				print("ml will always wait..")
				exit(1)
			else:
				print("even ml cannot understand that answer..")

	def train(self, hadoop, numIterations, defect = False):
		i = 0
		j = 0
		while numIterations == -1 or i < numIterations:
			if defect and math.log10(random.randint(1, i+1)) > random.randint(2,4) and hadoop:
				self.trainingFailed("hadoop crashed, that's too bad")
				exit(1)
			if hadoop:
				if random.randint(1,10) > 7:
					j += 1
				print "finished mappers: {0}, finished reducers: {1}".format(i, j),
			else:
				print i,
			i += 1
			sys.stdout.flush()
			time.sleep(float(i)/1000)
			print "\r",

	def main(self):
		self.pretrainingChecks()
		self.train(self._HADOOP, self._NUM_ITERATIONS, True)

if __name__ == '__main__':
    ml(ArgsParser().getArgs()).main()

