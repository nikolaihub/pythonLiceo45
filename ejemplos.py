#! /usr/bin/env python
#-*- coding:utf-8 -*-

#Ejemplo 1

if  A>2:
	A=A-1
	print A
else:
	print “Fin del Juego”

#Ejemplo 2

if  A>2:
	A=A-1
	print A
else:
	print “Fin del Juego”

#Ejemplo 3

jugando=True

while jugando:
	if A>2:
		A=A-1
		print A
	else:
		print “Fin del Juego”
		jugando=false

#Ejemplo 4

for i in range(1,3):
	A=input(“Decíme un animal: ”)
	print A

#Ejemplo 5

rutas=(“Manzana”,”Banana”,”Pera”,”Durazno”)

A=input(Decíme una fruta:)

if A in frutas:
	print “La fruta está en la canasta”
else:
	print “La fruta no está en la canasta”

