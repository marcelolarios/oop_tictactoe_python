from jogador import Jogador
import random

class Computador(Jogador):

	def __init__(self, tipo):
		super().__init__(tipo)  # private varibale or property in Python

	def joga(self):
	
		p = random.randint(1, 9)
		return int(p)
