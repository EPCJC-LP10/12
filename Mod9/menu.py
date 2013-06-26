# -*- coding: utf-8 -*-

def principal():
    print 
    print "    ****** MENU ******* "
    print
    print "   1. Gestão de Frota"
    print "   2. Gestão de Clientes"
    print
    print "   3. Registar Mudança"
    print 
    print "   0. Sair"
   

    op = raw_input("Opção: ")
    return op


def frota():
    print
    print " ***** Menu Frota ****** "
    print
    print "1. Inserir novo veiculos"
    print "2. Listar todos veiculos"
    print "3. Pesquisar veiculos"
    print "4. Alterar dados de um veiculos "
    print "5. Eliminar veiculos"
    print 
    print "0. Menu Anterior"
    op = raw_input("Opção: ")
    return op
    




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"

