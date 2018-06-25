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
###MENU####
while True:
	print("Jugando! Piedra, papel o tijera")
	print("1-Piedra\n2-Papel\n3-Tijera\n4-Salir")
	opc = int(input("Elige!: "))

	if(opc==1 or opc== 2 or opc== 3):
		partida = Juego(opc)
		partida.Mano_Comp()
		partida.validar_ganador()
		input()
	elif(opc==4):
		break
	else:
		print("Opción incorrecta")
		input()