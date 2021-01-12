#!/bin/python
#
# circular.py
# Implementação de Classe Circular derivada de lista
#
#
#

class Circular(list):

	def __init__(self):
		list.__init__(self)
		self.pos = None
		pass
		
	def corrente(self):
		return self[self.pos]
		
	def proximo(self):
		if self.pos is None:
			return None
		if self.pos>=len(self)-1:
			self.pos=0
		else:
			self.pos+=1
		return self[self.pos]

	def anterior(self):
		if self.pos is None:
			return None
		if self.pos==0:
			self.pos= len(self)-1
		else:
			self.pos-=1
		return self[self.pos]
		
	def insere(self, objeto):
		self.append(objeto)
		self.pos = len(self)-1
		
		
		
		
		
