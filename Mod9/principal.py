# -*- coding: utf-8 -*-

import menu
import frota
import util


# nome dos ficheiros
fxfrota = "fxfrota.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
	frota.listaVeiculos = util.ler_ficheiro(fxfrota)


def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
	util.escrever_ficheiro(fxfrota, frota.listaVeiculos)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        frota.gerir()
    elif op == '2':
        pass    #por fazer
    elif op == '0':
        terminar = True


escrever_ficheiros()


