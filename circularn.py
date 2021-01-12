#!/bin/python
#
# circularn.py
# Implementação de Classe Circular utilizando nós
#
#
#

class CircularN:

	def __init__(self, d=None):
		if not d:
			self.prox = None
			self.ant = None
			self.dado = None
		else:
			self.dado = d
			self.prox = self
			self.ant = self
		
	def corrente(self):
		return self.dado

	def insere(self, objeto):

		if not self.prox or not self.ant:
			self.dado = objeto
			self.prox = self
			self.ant = self
		else:
			no = CircularN( objeto )
			no.prox = self.prox
			self.prox = no
			no.ant = self
			no.prox.ant = no

		
	def proximo(self):
		return self.prox

	def anterior(self):
		return self.ant
		
		
		
		
		
