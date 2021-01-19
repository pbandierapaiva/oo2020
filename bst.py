#!/bin/python
#
# bsty
# Implementação de Classe BST árvore binária de busca
#
# 
#


class Node():

	def __init__(self, item):
		self.val = item
		self.noE = None
		self.noD = None
		
	def add(self, item):
		if item > self.val:
			if self.noD:
				self.noD.add(item)
			else:
				self.noD = Node( item )	
		else:
			if self.noE:
				self.noE.add(item)
			else:
				self.noE = Node( item )	


	def inorder(self):
		if self.noE:
			self.noE.inorder()
		print( self.val, end=' ')
		if self.noD:
			self.noD.inorder()
	def revinorder(self):
		if self.noD:
			self.noD.revinorder()
		print( self.val, end=' ')
		if self.noE:
			self.noE.revinorder()

	def depth(self):
		hd, he = 0,0
		
		if  not self.noD and  not self.noE:
			return 0
	
		if self.noD:
			hd = self.noD.depth()
		if self.noE:
			he = self.noE.depth()
		if hd>he:
			return 1 + hd
		else:
			return 1 + he

	def level(self, lev):
		lista= []
		if lev==0:
			return [ self.val ]
		if self.noE:
			lista+= self.noE.level(lev-1)
		if self.noD:
			lista+= self.noD.level(lev-1)
		return lista
	def bylevel(self):
		lista = []
		for i in range( self.depth()+1 ):
			lista += self.level( i ) 
		print( lista )
	def pai(self, no):
		acha = None
		if no ==self:
			print("Raiz")
			return None
		if self.noE:
			if self.noE == no:
				return self
			acha = self.noE.pai(no)
		if self.noD and not acha:
			if self.noD == no:
				return self
			acha = self.noD.pai(no)
		return acha
			
			
			
		
		
    
    		
bst = Node(12) 		#                     12           
bst.add(14)		#                         14
bst.add(13)		#                      13    34
bst.add(34)		#                    13    15   54
bst.add(15)		#                            17    64
bst.add(54)
bst.add(13)
bst.add(64)
bst.add(17)
#bst.inorder()
#print()
#bst.revinorder()























