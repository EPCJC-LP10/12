# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


veiculoReg = namedtuple("veiculoReg", "matricula, marca, volume, custo100, requisitado")
listaVeiculos = []



def encontrar_posicao(matricula):
    pos = -1
    for i in range (len(listaVeiculos)):
        if listaVeiculos[i].matricula == matricula:
            pos = i
            break
                            
    return pos


def inserir():
    matricula = raw_input("Qual a Matricula? ")

    pos = encontrar_posicao(matricula)

    if pos >= 0:
        print "Matricula repetida"
        return

    #ler dados
    marca = raw_input("Qual a Marca? ")
    volume = raw_input("Qual o volume de carga? ")
    custo100 = raw_input("Qual o custo por 100Kms? ")
    requisitado  = "N"
    
    registo = veiculoReg(matricula, marca, volume, custo100, requisitado)
    listaVeiculos.append(registo)


def pesquisar():
    matricula = raw_input("Qual a matricula do veiculo a pesquisar? ")

    pos = encontrar_posicao(matricula)

    if pos == -1:
        print "Não existe veiculo com essa matricula"
        return

    print "matricula: ", listaVeiculos[pos].id
    print "marca: ", listaVeiculos[pos].marca
    


def listar():
    for i in range (len(listaVeiculos)):
        print "Matricula: ", listaVeiculos[i].matricula
        print "Marca: ", listaVeiculos[i].marca
        print "Requisitado: ", listaVeiculos[i].requisitado
        
  

def eliminar():
    matricula = raw_input ("matricula do veiculo a eliminar --> ")
    pos = encontrar_posicao(matricula)

    if pos == -1:
        print "Não existe veiculo com essa matricula"
        return

    # TODO: Confirmar eliminação
    listaVeiculos.pop(pos)


    
def alterar():
    matricula = input ("matriclula do veiculo a alterar --> ")
    pos = encontrar_posicao(matricula)

    if pos == -1:
        print "Não existe veiculo com esse matricula"
        return

    # só altera o nome
    novonome = raw_input("Qual a marca? ")
    listaVeiculos[pos] = listaVeiculos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.frota()

        if op == '1':
            inserir()
        elif op =='2':
            listar()
        elif op == '3':
            pesquisar()
        elif op == '4':
            alterar()
        elif op == '5':
            eliminar()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










