class Storage:

	def __init__(self): 
		self.__jogo = [' '] * 10
		self.__vez = 0 		# var de instãncia   __ sign privado
		self.__resultado = 0

	def zera(self):
		self.__jogo = [' '] * 10
		self.__estado = 0
		self.__resultado = 0; 

	def getJogo(self):
		return self.__jogo
		
	def setJogo(self, casa, sig):
		self.__jogo[casa] = sig

	def getVez(self):
		return self.__vez
		
	def setVez(self):
		self.__vez = not self.__vez

	def getResultado(self):
		return self.__resultado
		
	def setResultado(self, resultado):
		self.__resultado = resultado