#! /usr/bin/env python
#-*- coding:utf-8 -*-
import random

veces = 0
nombre = raw_input('¡Hola! ¿Cómo te llamás?')
numero = random.randint(1, 20)
print 'Bueno, ' + nombre + ', estoy pensando en un número del 1 al 20.'

while veces < 6:
    print 'Adiviná en qué número estoy pensando.'
    guess = input()
    veces = veces + 1
    if guess < numero:
        print 'Te quedaste corto.'
    elif guess > numero:
        print 'Te pasaste.'
	else guess == numero:
        break

if guess == numero:
    veces = str(veces)
    print '¡Muy bien, ' + nombre + '! ¡Adivinaste en ' + veces + ' intentos!'

if guess != numero:
    print '¡Uh, estuviste cerca! El número en el que estaba pensando era ' + str(numero)

