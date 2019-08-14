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
@summary: Lista de exercicios 01 - jogo adivinha numero aleatorio
@imports: unidecode
@python_Ver: 3.7.3
"""
import funcoes 
from unidecode import unidecode
import random

def validando_chute(tentativas, numero_aleatorio):
    roda = True

    while roda is True:
        chute = input("informe um número de 1 a 100 ")
        # verifica se o chute pode virar numero 
        try:
            chute = int(chute)
            # verifica se chute esta entre 0 e 100
            if chute >= 0 and chute <=100:
                tentativas -= 1
                roda = verifica_chute(tentativas, chute, numero_aleatorio)
            else:
                print("número invalido")

        except:
            print('carácter informado nao e número')

def verifica_chute(tentativas, chute, numero_aleatorio):
    
    acertou = chute == numero_aleatorio
    valor_maior = chute > numero_aleatorio
    valor_menor = chute < numero_aleatorio
    fim = tentativas == 0

    if acertou:
        print("voce acertou")
        return False
    else:

        if fim:
            print(f"voce perdeu, o número era {numero_aleatorio}")
            return False
        else:
            escrita = funcoes.ortografia(tentativas)

            if valor_maior:
                print(f"chute maior que o número secreto, voce ainda tem {tentativas} {escrita}")
            elif valor_menor:
                print(f"chute menor que o número secreto, voce ainda tem {tentativas} {escrita}")

            return True


def jogo_adivinha():
    jogar = True
    
    while jogar is True:
        tentativas = funcoes.escolha_nivel()
        numero_aleatorio = random.randrange(0, 100)
        validando_chute(tentativas, numero_aleatorio)
        jogar = funcoes.jogar_novamente()

jogo_adivinha()