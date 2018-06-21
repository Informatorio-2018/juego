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
	