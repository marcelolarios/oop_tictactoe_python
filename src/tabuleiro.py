from storage import Storage
from humano import Humano
from computador import Computador

class Tabuleiro:
	def __init__(self):
		self.quem = ''
		self.jh = Humano('x')
		self.jc = Computador('o')
		self.sto = Storage()
	
	def rodada(self):
		while True:
			if not self.partida():
				print(self.aviso(3)) #interrup
				return
			print(self.aviso(4)) #Nova partida
			
	def partida(self): #1 completa
		self.sto.zera()
		while True: 
			j = self.jc if self.sto.getVez() else self.jh
			self.quem = j.getTipo()
			if j == self.jh: self.mostra() #aviso proximo a jogar
			if not self.lance(j): return False
			if self.compara(): break
			self.sto.setVez()
		self.mostra()
		return True

	def lance(self,j):
		while True:
			casa = j.joga()
			if casa == 0: return False
			v = self.sto.getJogo();
			pos = v[casa]
			if pos == ' ':
				self.sto.setJogo(casa, j.getTipo())
				break
		return True
	
	def compara(self):	# Método comum
		
		v = self.sto.getJogo();
		possibs = [[1,2,3],[4,5,6],[7,8,9],[7,4,1],[8,5,2],[9,6,3],[1,5,9],[7,5,3]]

		for i in range(0, 8):
			pb = possibs[i]
			if v[pb[0]] == v[pb[1]] and v[pb[1]] == v[pb[2]] and v[pb[2]] != ' ':
				self.sto.setResultado(1)  #há vencedor
				return True
		for i in range(1, 10):  #começa do 1 senão é loop infinito
			if v[i] == ' ':	return False 
		self.sto.setResultado(2)
		return True #empatou
		
	def mostra(self):
		v = self.sto.getJogo();
		#j = self.sto.jogo
		print('7|8|9','\t\t','|',v[7],'|',v[8],'|',v[9],'|   ', self.aviso(self.sto.getResultado()), sep='')
		print('4|5|6','\t\t','|',v[4],'|',v[5],'|',v[6],'|'   , sep='')
		print('1|2|3','\t\t','|',v[1],'|',v[2],'|',v[3],'|\n' , sep='')

	def aviso(self,i):
		if   i==1: return "jogador \"" + self.quem + "\" venceu!"
		elif i==2: return "Empatou!"
		elif i==3: return "\n*** Jogo Interrompido ***\n"
		elif i==4: return "\n\n*** Nova partida ***\n"
		else:  return "jogador \"" + self.quem + "\", sua vez"

