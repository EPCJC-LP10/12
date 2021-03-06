# -*- coding: utf-8 -*-

#
# Exemplo utilização de array de registos
# Os elementos da lista NÃO são mantidos ordenados
# (a inserção é feita depois da última posição anterior)
# © EPCJC
#

def menu():
    print
    print "1: Inserir novo contacto"
    print "2: Listar todos os contactos"
    print "3: Pesquisar contacto por código"
    print "4: Alterar dados de um contacto"
    print "5: Eliminar contacto"
    
    print "0: Terminar"
    print

def posicao_livro(codigo):
    ''' Encontra a posicao onde se encontra o contacto com o código recebido
    
        Pesquisa por um código de contacto nos contacos
        já inseridos. Se NÃO encontra o código, devolve o valor -1; 
        caso contrário, devolve a posicão do contacto dentro da lista
        
    '''
    
    for pos in range(len(contacto)):
        if contactos[pos].codigo == codigo:
            return pos
                    
    return -1   # não encontrou
    
    

def inserir():
    codigo = input("Introduza código: ")
    posicao = posicao_contacto(codigo)
    if posicao != -1:
        print("Código já existente.\n")
        return
    
    # ler os restantes dados do registo
    nome = raw_input("Introduza o nome: ")
    numero = raw_input("Numero:")
    
    
    
    # Criar o novo registo
    novo_registo = contacto(codigo, titulo, ano, autor)

    # Adicionar o registo à lista 
    
    contactos.append(novo_registo)
    
    
def apresentar_registo(registo):
        print "Código: ", registo.codigo
        print "Nome: ", registo.nome
        print "Numero: ", registo.numero
        print "-------------------------------"


def listar_todos():
    if len(contactos) == 0:
        print "Não existem contactos inseridos"
        return

    for registo in contactos:
        apresentar_registo(registo)
        

#Outra maneira de fazer a listagem
def listar_todos_alternativa():
    if len(contactos) == 0:
        print "Não existem contactos inseridos"
        return

    for i in range(len(contactos)):
        apresentar_registo(contactos[i])



def pesquisar():
    codigo = input("Introduza código do contacto: ")
    posicao = posicao_contacto(codigo)
    if posicao == -1:
        print "Esse código não existe."
        return

    apresentar_registo(contactos[posicao])
    
def alterar():
    codigo = input("Introduza código do contacto: ")
    posicao = posicao_contactos(codigo)
    if posicao == -1:
        print "Esse código não existe."
        return

    apresentar_registo(contactos[posicao])

    # A melhorar: perguntar qual o campo que se pretende alterar
    # Assim altera todos os campos com exceção do código

    #ler os novos dados
    novo_nome = raw_input("Introduza novo nome: ")
    novo_numero = raw_input("Novo numero: ")
   
    

    # Substituir o registo
    contactos[posicao] = contactos[posicao]._replace(nome=novo_nome, 
    	numero=novo_numero)

    
    
def eliminar():
    codigo = input("Introduza código do contacto: ")
    posicao = posicao_contacto(codigo)
    if posicao == -1:
        print "Esse código não existe."
        return

    apresentar_registo(Livros[posicao])
    opcao = raw_input("Tem a certeza que deseja eliminar este registo (S/N)? ")
    if opcao.lower() == "s":
        #eliminar registo na posição posicao
        Livros.pop(posicao)
        print "Registo eliminado"
    else:
        print "Registo não eliminado"


##################################

from collections import namedtuple

contacto = namedtuple("contacto", "codigo, nome, numero")

contactos = []
	
quero_sair = False
while not quero_sair:
    menu()
    op = raw_input("Introduza opção: ")
    if op == '1':
        inserir()
    elif op == '2':
        listar_todos()		
    elif op == '3':
        pesquisar()
    elif op == '4':
        alterar()
    elif op == '5':
        eliminar()
    elif op == '0': 
        quero_sair = True
    else:
		print "Opção inválida"
        
print 

