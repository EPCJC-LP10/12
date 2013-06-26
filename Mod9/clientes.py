# -*- coding: utf-8 -*-

from collections import namedtuple



clienteReg = namedtuple("clienteReg", "cod, nome, telefone")
listaClientes = []



def menu():
    print 
    print " ****** Menu Clientes ****** "
    print
    print "1. Inserir novo Clientes"
    print "2. Listar todos Clientes"
    print "3. Pesquisar Clientes"
    print "4. Alterar dados de um Clientes"
    print "5. Eliminar Clientes"
    print  
    print "0. Menu Anterior"
  
    op = raw_input("Opção: ")
    return op

def encontrar_posicao(cod):
    pos = -1
    for i in range (len(listaClientes)):
        if listaClientes[i].cod == cod:
            pos = i
            break
                            
    return pos


def inserir():
    cod = raw_input("Qual o cod? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "cod repetido"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    telefone = raw_input("Qual o telefone? ")
   
    
    registo = clienteReg(cod, nome, telefone,)
    listaClientes.append(registo)


def pesquisar():
    cod = raw_input("Qual a cod do cliente a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe cliente com essa cod"
        return

    print "cod: ", listaClintes[pos].id
    print "nome: ", listaClientes[pos].nome
    


def listar():
    for i in range (len(listaClientes)):
        print "cod: ", listaClientes[i].cod
        print "nome: ", listaClientes[i].nome
     
        
  

def eliminar():
    cod = raw_input ("cod do cliente a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe cliente com essa cod"
        return

    # TODO: Confirmar eliminação
    listaClientes.pop(pos)


    
def alterar():
    cod = input ("cod do cliente a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe cliente com esse cod"
        return

    # só altera o nome
    novonome = raw_input("Qual a marca? ")
    listaClientes[pos] = listaClientes[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu()

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










