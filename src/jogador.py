class Jogador:

	def __init__(self, tipo): # construtor
		self.__tipo = tipo  # private varibale or property in Python
	
	def joga(self):
		pass
		
	def getTipo(self):
		return self.__tipo
