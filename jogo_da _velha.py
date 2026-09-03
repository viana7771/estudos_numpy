import numpy as np
from random import choice

def criando_matriz():
    matriz = ([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    array = np.array(matriz)
    print(array)

def criando_players():
    player1 = str(input('Insira o nome player 1: '))
    player2 = str(input('Insira o nome player 1: '))

    print('Players criados com sucesso!')

    return player1, player2

def escolha_ordem_inicio(player1, player2):
    escolha = choice([player1, player2])
    return escolha

def main():
    criando_matriz()

    player1, player2 = criando_players()

    jogador_inicial = escolha_ordem_inicio()

    print(f'Quem começa é: {jogador_inicial}')

if __name__ == '__main__':
    main()