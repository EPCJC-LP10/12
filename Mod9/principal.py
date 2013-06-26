# -*- coding: utf-8 -*-

import menu
import frota
import util
import clientes


# nome dos ficheiros
fxfrota = "fxfrota.dat"
fxClientes = "clientes.dat"

def ler_ficheiros():
    # adicionar todos ficheiros a ler
    frota.listaVeiculos = util.ler_ficheiro(fxfrota)
    clientes.listaClientes = util.ler_ficheiro(fxClientes)


def escrever_ficheiros():
    # adicionar todos ficheiros a guardar
    util.escrever_ficheiro(fxfrota, clientes.listaClientes)
    util.escrever_ficheiro(fxClientes, clientes.listaClientes)


# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        frota.gerir()
    if op == '2':
        clientes.gerir()
    
    elif op == '0':
        terminar = True


escrever_ficheiros()


