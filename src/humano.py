from jogador import Jogador

class Humano(Jogador):

	def __init__(self, tipo):
		super().__init__(tipo)  # private varibale or property in Python

	def joga(self):
	
		posics = '0123456789'
		p = input('digite o nr: ')
		if p != '':
		
			if posics.index(p) > -1:
							
					return int(p);
					
		return 0