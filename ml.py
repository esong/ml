import argparse
import math
import os
import random
import sys
import time

class Parser(object):
	def getArgs(self):
		parser = argparse.ArgumentParser(description='the power of ml in one little script')
		parser.add_argument('--training_data', dest='trainingData', help='data for training', required=True)
		return parser.parse_args()

class Display(object):
	def printForever(self):
		i = 0
		while True:
		    print i,
		    i += 1
		    sys.stdout.flush()
		    time.sleep(float(i)/1000)
		    print "\r",

class ml(object):

	_DEFAULT_MINIMUM_FILE_SIZE = 10000
	_TRAINING_FILE = None

	display = Display()

	def __init__(self, args):
		self._TRAINING_FILE = os.stat(args.trainingData)
		random.seed()

	def trainingFailed(self, extraMsg):
		print("what is the point of ml if you don't even try...")
		print(extraMsg)
		exit(1)

	def checkFileSize(self):
		if self._TRAINING_FILE.st_size < self._DEFAULT_MINIMUM_FILE_SIZE/random.randint(1,100):
			self.trainingFailed("i can't train on this data, please give me more.")

	def train(self):
		self.checkFileSize()
		print("truly thinking like an ml'er. starting up the training.")
		self.display.printForever()

if __name__ == '__main__':
    ml(Parser().getArgs()).train()

