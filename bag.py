#!/bin/python
#
# bag.py
# Implementação de Classe Bag derivada de lista
#
# 
#
import random

class Bag():
	
	def __init__(self):
		self.saco = []
		self.i = 0
	def __iter__(self):
		self.i = 0
		random.shuffle(self.saco)
		return self
	def __next__(self):
		if self.i >= self.size():
			raise StopIteration
		self.i +=1
		return self.saco[self.i-1]
		
	def isEmpty(self):
		if len(self.saco):
			return True
		else:
			return False
	def size(self):
		return 	len(self.saco)
	def __len__(self):
		return self.size()	
	def add(self, item):
		self.saco.append(item)
		
s = Bag()
s.add(87)
s.add(8)
s.add(7)
s.add(2)
s.add(5)

for i in s: print(i, end=' ')
print()

for i in s: print(i, end=' ')
print()
for i in s: print(i, end=' ')
print()


