import numpy as np

def criar_matiz():
    matriz = ([
        [1, 2, 3],
        [4, 5, 6,],
        [7, 8, 9,]
    ])
    array = np.array(matriz)

    return array

def mostrando_primeiro_elemento(array):
    return array[2, 1]

def main():
    matriz = criar_matiz()

    primeiro_elemento = mostrando_primeiro_elemento(matriz)

    print(matriz)
    print(f'\nPrimeiro elemento: {primeiro_elemento}')


if __name__ == '__main__':
    main()