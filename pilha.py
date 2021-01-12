#!/bin/python
#
# pilha.py
# Implementação de Classe Pilha derivada de lista
#
# LIFO - Last in first out
#

class Pilha(list):
	
	def __init__(self):
		list.__init__(self)
		
	def push(self, objeto):
		print("no push")
		self.append(objeto)
		
	def pop(self):
		print("no pop")
		obj= self.peek()
		if obj:
			del self[-1]
		return obj
		
	def peek(self):
		print("no peek")
		try:	
			return self[-1]
		except:
			print("Lista vazia")
			return None
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		


