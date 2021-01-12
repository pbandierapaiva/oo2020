#!/bin/python
#
# pilha0.py
# Implementação de Classe Pilha usando atributo lista
#

class Pilha:
	
	def __init__(self):
		self.lista = []
		
	def push(self, objeto):
		print("no push")
		self.lista.append(objeto)
		
	def pop(self):
		print("no pop")
		obj= self.peek()
		if obj:
			del self.lista[-1]
		return obj
		
	def peek(self):
		print("no peek")
		try:	
			return self.lista[-1]
		except:
			print("Lista vazia")
			return None
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		


