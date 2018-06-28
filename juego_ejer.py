# Juego de piedra, papel y tijera

# 1=piedra
# 2=pàpel
# 3=tijera
from os import system

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
			print("\nEmpate!\n")

		elif(self.mano==1 and self.manocpu==2):
			print("\nPerdiste!\n")

		elif(self.mano==1 and self.manocpu==3):
			print("\nGanaste!\n")
		
		elif(self.mano==2 and self.manocpu==3):
			print("\nPerdiste!\n")

		elif(self.mano==2 and self.manocpu==1):
			print("\nGanaste!\n")

		elif(self.mano==3 and self.manocpu==1):
			print("\nPerdiste!\n")

		elif(self.mano==3 and self.manocpu==2):
      			print("\nGanaste!\n")


###MENU####
def menu():
	while True:
		system('cls')
		print("Jugando! Piedra, papel o tijera")
		print("1-Piedra\n2-Papel\n3-Tijera\n4-Salir")

		while True:
			try:
				opc = int(input("\nElige!: "))
				break
			except:
				print('Error, opción incorrecta!\n')
				continue

		if(opc==1 or opc== 2 or opc== 3):
			partida = Juego(opc)
			partida.Mano_Comp()
			partida.validar_ganador()
			input()
		elif(opc==4):
			break

menu()
