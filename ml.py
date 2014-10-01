import argparse
import math
import os
import random
import sys
import time

class Trainer(object):
	def trainingFailed(self, extraMsg):
		print("what is the point of ml if you don't even try...")
		print(extraMsg)
		exit(1)

	def trainForever(self, hadoop, numIterations, defect = False):
		i = 0
		while numIterations == -1 or i < numIterations:
			if defect and math.log10(random.randint(1, i+1)) > random.randint(2,4):
				Trainer().trainingFailed("hadoop crashed, that's too bad")
				exit(1)
			print i,
			i += 1
			sys.stdout.flush()
			time.sleep(float(i)/1000)
			print "\r",

class ArgsParser(object):
	def getArgs(self):
		parser = argparse.ArgumentParser(description='the power of ml in one little script')
		parser.add_argument('--training_data', dest='trainingData', help='data for training', required=True)
		parser.add_argument('--hadoop', dest="hadoop", help="use hadoop?", default=True)
		parser.add_argument('--iterations', dest="iterations", help='number of iterations', default=-1)
		return parser.parse_args()

class ml(object):

	_DEFAULT_MINIMUM_FILE_SIZE = 10000
	_TRAINING_FILE = None
	_HADOOP = True
	_NUM_ITERATIONS = -1

	trainer = Trainer()

	def __init__(self, args):
		self._TRAINING_FILE = os.stat(args.trainingData)
		self._HADOOP = bool(args.hadoop)
		self._NUM_ITERATIONS = int(args.iterations)
		random.seed()

	def checkFileSize(self):
		if self._TRAINING_FILE.st_size < self._DEFAULT_MINIMUM_FILE_SIZE/random.randint(1,100):
			self.trainer.trainingFailed("i can't train on this data, please give me more.")

	def main(self):
		self.checkFileSize()
		print("truly thinking like an ml'er. starting up the training.")
		self.trainer.trainForever(self._HADOOP, self._NUM_ITERATIONS, True)

if __name__ == '__main__':
    ml(ArgsParser().getArgs()).main()

