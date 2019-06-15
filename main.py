"""
Universidade Federal de Pernanbuco - UFPE (www.ufpe.com.br)
Centro de Informática - CIn (www2.cin.ufpe.br)
Bacharelado em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-06-14

Copyright © 2019 todos os direitos reservados
"""

import os
import jogos

def main():
    """
    Funcao principal que chama as funcoes do arquivo jogos.py
    """
    condicao_jogar = True #condicao que garante o loop de jogo
    while condicao_jogar:
        #Escolhendo o modo de jogo
        modo_de_jogo = -1
        while modo_de_jogo < 1 or modo_de_jogo > 2:
            try:
                os.system('cls||clear')
                modo_de_jogo = int(input("Escolha um modo de jogo: \n1-Notakto \n2-Misere \nSua escolha: "))
            except (KeyError, ValueError):
                os.system('cls||clear')

        #caso escolha o Notakto
        if  modo_de_jogo == 1:
            jogos.notakto(False)
        #caso escolha o Misere
        elif modo_de_jogo == 2:   
            jogos.misere(True)
        
        print('')
        continua_jogar = str() #param para o usuario escolher se quer continuar a jogar ou nao
        while continua_jogar != 'S' and continua_jogar != 'N':
            try:
                continua_jogar = input("Quer continuar jogando? [s/n]: ").upper()
            except (KeyError, ValueError):
                print("Opcao invalida.")
        
        if continua_jogar == 'S':
            os.system('cls||clear')
        else:
            condicao_jogar = False
        
if __name__ == '__main__':
    os.system('cls||clear')
    main()