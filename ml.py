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

	def train(self, hadoop, numIterations, defect = False):
		i = 0
		j = 0
		while numIterations == -1 or i < numIterations:
			if defect and math.log10(random.randint(1, i+1)) > random.randint(2,4) and hadoop:
				Trainer().trainingFailed("hadoop crashed, that's too bad")
				exit(1)
			if hadoop:
				if random.randint(1,10) > 7:
					j += 1
				print "mappers: {0}, reducers: {1}".format(i, j),
			else:
				print i,
			i += 1
			sys.stdout.flush()
			time.sleep(float(i)/1000)
			print "\r",

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

	trainer = Trainer()

	def __init__(self, args):
		try:
			self._TRAINING_FILE = os.stat(args.trainingData)
		except:
			self.trainer.trainingFailed("how can i learn without any training? ..")
		self._HADOOP = args.hadoop.lower() in ("yes", "true", "t", "1")
		self._NUM_ITERATIONS = int(args.iterations)
		random.seed()

	def pretrainingChecks(self):
		if self._TRAINING_FILE.st_size < self._DEFAULT_MINIMUM_FILE_SIZE/random.randint(1,100):
			self.trainer.trainingFailed("i can't train on this data, please give me more..")

		if self._NUM_ITERATIONS > 0 and self._NUM_ITERATIONS < 1000:
			self.trainer.trainingFailed("do you really expect to achieve perfection with that little iterations? ..")

	def main(self):
		try:
			self.pretrainingChecks()
			print("truly thinking like an ml'er. starting up the training:")
			self.trainer.train(self._HADOOP, self._NUM_ITERATIONS, True)
		except KeyboardInterrupt:
			print("\none cannot simply stop machine learning..")
			self._DEFAULT_MINIMUM_FILE_SIZE = 0
			self.main()

if __name__ == '__main__':
    ml(ArgsParser().getArgs()).main()

