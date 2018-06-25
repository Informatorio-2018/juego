from random import randint

tablero = []

for i in range(5):
	tablero.append('O')

def print_tablero(a):
	for i in tablero:
		print (' '.join(tablero))


def random_fila(a):
	return randint(0,len(tablero)-1)

def random_col(a):
	return randint(0,len(tablero)-1)

fila = random_fila(tablero)

col = random_col(tablero)

print (fila)
print (col)

print_tablero(tablero)

while True:
	try:
		adi_col = int(input('Adivina la columna: '))
		break
	except:
		print('Error, ingrese un numero entero')
		continue

while True:
	try:
		adi_fila = int(input('Adivina la fila: '))
		break
	except:
		print('Error, ingrese un numero entero')
		continue

if adi_fila == fila and adi_col == col:
	print('Felicitaciones! Hundiste mi nave!')

print(asd)