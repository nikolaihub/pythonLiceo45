#! /usr/bin/env python
#-*- coding:utf-8 -*-

print "Hola mundo"

nombre = raw_input('Cual es tu nombre?\n')
print 'Hola, ', nombre

5*63.458

from math import sqrt
sqrt(81) + (2+5)*13 - 45/(12-7)

print 'Hola'*20

lista = ['Peñarol', 'Santos']
cuadro = raw_input('De que cuadro sos?\n')
if cuadro in lista:
	print 'Suerte en la final!'
else:
	print 'No estan en la final de la Libertadores! Intenten el año que viene ;)'

import turtle
for x in range(1,19):
	turtle.forward(100)
	if x % 2 == 0:
		turtle.left(175)
	else:
		turtle.left(225)
		
import turtle
while True:
	turtle.forward(150)
	turtle.left(125)
		
from turtle import *
pensize(3)
color('blue')
lados = int(raw_input('Cuantos lados queres? '))
for n in range(lados):
    fd(20)
    rt(360 / lados)
raw_input('Continuar')

