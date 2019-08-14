# -*- coding: utf-8 -*-
"""
Created on Sun Aug
@author: Victor Hugo Fleury Barreto
@ra: 1912120006
@email: vh15fleury@hotmail.com

@class: programacao Avancada de Computadores
@professor: Prof. MSc. Tiago Henrique Franca Baroni
@course: Ciencia de Dados e Inteligencia Artificial
@subject: Revisao de conceitos basicos do Pyhton
@summary: Lista de exercicios 01 - script com funcoes utilizadas nos dois jogos 
@imports: unidecode
@python_Ver: 3.7.3
"""

from unidecode import unidecode
import random

def escolha_nivel():

    # tipos de dificuldade
    niveis = [{'dificuldade':'Fácil', 'tentativa':15},
     {'dificuldade':'Médio', 'tentativa':10},
     {'dificuldade':'Difícil', 'tentativa':5}]
    nivel_valido = False

    # enquanto o nivel nao for encontrado, o programa continuara perguntando pro usuario
    while nivel_valido == False:
        jogar_nivel = input('qual nivel voce quer jogar? Fácil, Médio ou Difícil? ')
        jogar_nivel = unidecode(jogar_nivel.lower().lstrip())

        # laço para verificar se nivel digitado e valido
        for posicao in range(len(niveis)):
            nivel = unidecode(niveis[posicao]['dificuldade'].lower())

            # se o nivel for encontrado, retorna a quantidade de tentativas
            if jogar_nivel == nivel:
                tentativa = niveis[posicao]['tentativa']
                nivel_valido = True
                break

        # se nao for encontrado impreme uma mensagem de erro
        if nivel_valido != True:
            print('nivel invalido')


    return tentativa

# funcao que deixa a palavra 'tentativa' no plural ou singular
def ortografia (tentativas):

    if tentativas >1:
        return 'tentativas'
    else:
        return 'tentativa'

def jogar_novamente():
    jogar = False

    # o programa perguntara pro usuario até ele inserir um carácter valido
    while jogar is False:
        pergunta = input("deseja jogar novamente? (s/n)")
        
        # verifica se a pergunta do usuario e valido, caso contrario imprima um erro
        if pergunta.lower().lstrip() == 's':
            return True
        elif pergunta.lower().lstrip()  == 'n':
            return False
        else:
            print("valor inválido")
