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
@summary: Lista de exercicios 01 - jogo forca
@imports: unidecode
@python_Ver: 3.7.3
"""
from unidecode import unidecode
import funcoes 
import random

def escolhendo_palavra():
    palavra = {1:'Abacate', 2: 'Abacaxi', 3:'Coco', 4:'Amora', 5:'Banana', 6:'Araticum', 7:'Cacau', 8:'Laranja', 9:'Framboesa'}
    posicao_aleatoria = random.randrange(1, 9)

    return palavra[posicao_aleatoria]

def verifica_chute(palavras_chutadas, chute):
    chute = chute.lstrip().lower()
    try:
        chute = int(chute)
        print("informe uma letra, nao um numero")
        return False

    except:

        if chute in palavras_chutadas:
            print('palavra ja escolhida')
            return False

        if len(chute) >1:
            print("informe uma letra, nao uma palavra")

            return False
        else:
            palavras_chutadas.add(chute)
            return chute.lower()

def verifica_letra(tentativas, palavra):
    letras_adivinhadas = [" _ "]*len(palavra)
    palavras_chutadas = {''}


    while tentativas >0:
        acertou = False

        print(letras_adivinhadas)
        chute = input('digite uma letra ')
        chute = verifica_chute(palavras_chutadas, chute)
        
        if chute != False:
            # procura em cada letra da palavra se e igual ao chute
            for posicao in range(len(palavra)):

                if unidecode(palavra[posicao].lower()) == unidecode(chute):
                    letras_adivinhadas[posicao] = palavra[posicao]
                    acertou = True  
                    
            # se letra for acertada, verifica se esta faltando mais alguma letra
            if acertou == True:

                if " _ " in letras_adivinhadas:
                    pass
                else:
                    print('voce acertou a palavra')
                    print(letras_adivinhadas)
                    break
            # se chute estiver errado verifica se tem mais tentativas
            else:
                tentativas -=1
                escrita = funcoes.ortografia(tentativas)

                if tentativas == 0:
                    print(f'voce perdeu, a palavra era {palavra}')
                else:
                    print(f"errou, {tentativas} {escrita}")

def jogo_forca():
    jogar = True
    
    while jogar is True:
        tentativas = funcoes.escolha_nivel()
        palavra_escolhida = escolhendo_palavra()
        verifica_letra(tentativas, palavra_escolhida)
        jogar = funcoes.jogar_novamente()



jogo_forca()