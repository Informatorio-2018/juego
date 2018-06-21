# Juego de piedra, papel y tijera

# 1=piedra
# 2=pàpel
# 3=tijera

class Juego():
	manocpu=0

	def __init__(self,mano):
		self.mano=mano

	def Mano_Comp(self):
		from random import randint
		self.manocpu=randint(1, 3)
		return self.manocpu
	

	def validar_ganador(self):

		if (self.mano==self.manocpu):
			print("Empate!")

		elif(self.mano==1 and self.manocpu==2):
			print("Perdiste!")

		elif(self.mano==1 and self.manocpu==3):
			print("Ganaste!")
		
		elif(self.mano==2 and self.manocpu==3):
			print("Perdiste!")

		elif(self.mano==2 and self.manocpu==1):
			print("Ganaste!")

		elif(self.mano==3 and self.manocpu==1):
			print("Perdiste!")

		elif(self.mano==3 and self.manocpu==2):
			print("Ganaste!")


