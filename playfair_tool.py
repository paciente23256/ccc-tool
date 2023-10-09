#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Cifra PlayFair

"""
A cifra Playfair é uma substituição polialfabética em bloco bigrâmico (ou digrâmico). 
Nesta substituição, as letras são tomadas duas a duas (bloco bigrâmico), de acordo com 
regras aplicadas a uma grade de 5 por 5 que contém o alfabeto de cifra.
"""

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
         'X', 'Y', 'Z']

"""
Função: key_key()
Recebe a chave como input do utilizador. Manipula caracteres válidos e casos especiais.
Parâmetro: Nenhum
Retorna: Retorna a chave digitada pelo utilizador

"""

xrange=range

def get_key():
    k = input().upper()
    key = []
    for char in k:
        if char in alpha and char not in key:  # adicione o caracter à matriz se for válido e ainda não estiver na matriz
            key.append(char)
        elif char == "J":  # lida com o caso quando a letra J aparece na chave
            key.append("I")
    for char in alpha:
        if char not in key:  # adicione o resto do alfabeto que não aparece na chave a matriz
            key.append(char)
    return key


"""
Função: gen_matrix(key)
Gera uma matriz Playfair com a chave fornecida.
Parâmetro: key - A chave a ser usada para gerar uma matriz Playfair.
Retorna: Retorna a matriz Playfair com a chave.
"""


def gen_matrix(key):
    matrix = []
    counter = 0
    if key == '':  # cria a matriz em branco
        for xcounter in xrange(5):
            x = []
            for ycounter in xrange(5):
                x.append(alpha[counter])
                counter += 1
            matrix.append(x)
    else:  # cria a matriz com a chave
        for xcounter in xrange(5):
            x = []
            for ycounter in xrange(5):
                x.append(key[counter])
                counter += 1
            matrix.append(x)
    return matrix


"""
Função: print_matrix(matrix)
Imprime a matriz Playfair fornecida.
Parâmetro: matrix - A matriz Playfair imprime.
Devoluções: Nenhuma.
"""


def print_matrix(matrix):
    for counter in xrange(5):
        print ("%c %c %c %c %c" % (
            matrix[counter][0], matrix[counter][1], matrix[counter][2], matrix[counter][3], matrix[counter][4]))
    print ("\n")


"""
Função: get_message()
Recebe a mensagem com input do utilizador. Manipula caracteres válidos e casos especiais.
Parâmetro: Nenhum
Return: Retorna a mensagem resultante.
"""


def get_message():
    m = input()
    m2 = []
    for char in m.upper():
        if char in alpha:  # lida com caracteres válidos na mensagem
            m2.append(char)
        elif char == "J":  # lida com o caso quando "J" qdo aparece na mensagem
            m2.append("I")
        elif char == ".":  # troca o ponto por x, por conveniência
            m2.append("X")
    return ''.join(m2)


"""
Função encrypt(message, key_matrix)
Executa a cifragem da mensagem fornecida com a matriz Playfair com a chave ex. [B][E][N][F][I][C][A].
Parâmetro: message - A mensagem que ira ser cifrada
Parâmetro: key_matrix - A matriz Playfair com chave a ser usada cifrada.
Retorna: não retorna nada, o texto cifrado resultante é impresso no final
        da função.
"""


def encrypt(message, key_matrix):
    coords = []
    ciphertext = []
    digraphs = parse_message(message)

    for d in digraphs:
        swap = []
        temp = []
        coords = get_coords(d, key_matrix)
        if coords[0][0] == coords[1][0]:  # o dígrafo esta no mesmo eixo x
            x, y = ((coords[0][0], (coords[0][1] + 1) % 5))
            swap.append((x, y))
            x, y = ((coords[1][0], (coords[1][1] + 1) % 5))
            swap.append((x, y))
        elif coords[0][1] == coords[1][1]:  # o dígrafo esta no mesmo eixo y
            x, y = (((coords[0][0] + 1) % 5), coords[0][1])
            swap.append((x, y))
            x, y = (((coords[1][0] + 1) % 5), coords[1][1])
            swap.append((x, y))
        else:  # o dígrafo está em diferentes eixos x e y
            swap.append((coords[0][0], coords[1][1]))
            swap.append((coords[1][0], coords[0][1]))

        for x, y in swap:
            ciphertext.append(key_matrix[x][y])

    print ("A mensagem cifrada é: %s " % ''.join(ciphertext))


"""
Função decrypt(message, key_matrix)
Executa a decifragem da mensagem fornecida com a matriz Playfair com chave fornecida.
Parâmetro: menssage - Mensagem a decifrar
Parâmetro: key_matrix - A matriz Playfair com chave a ser usada para decifragem.
Return: não retorna nada, o texto simples resultante é impresso no final da função.
"""


def decrypt(message, key_matrix):
    coords = []
    plaintext = []
    digraphs = parse_message(message)

    for d in digraphs:
        swap = []
        temp = []
        coords = get_coords(d, key_matrix)
        if coords[0][0] == coords[1][0]:  # digraph lies on same x axis
            x, y = ((coords[0][0], (coords[0][1] - 1) % 5))
            swap.append((x, y))
            x, y = ((coords[1][0], (coords[1][1] - 1) % 5))
            swap.append((x, y))
        elif coords[0][1] == coords[1][1]:  # digraph lies on same y axis
            x, y = (((coords[0][0] - 1) % 5), coords[0][1])
            swap.append((x, y))
            x, y = (((coords[1][0] - 1) % 5), coords[1][1])
            swap.append((x, y))
        else:  # digraph lies on different x & y axis
            swap.append((coords[0][0], coords[1][1]))
            swap.append((coords[1][0], coords[0][1]))

        for x, y in swap:
            plaintext.append(key_matrix[x][y])

    print ("Your decrypted message is: %s " % ''.join(plaintext))


"""
Function: parse_message(message)
Analisa a mensagem inserida pelo utilizador.
Prepara o texto manipulando casos em que letras duplas aparecem uma ao lado da outra.
Ignora caracteres não alfabéticos, números e pontuação.
Parâmetro: message - Menssagem inserida pelo utilizador.
Retorna: Retorna um array de dígrafos resultantes da mensagem fornecida.
"""


def parse_message(message):
    digraphs = []
    while len(message) > 0:
        digraph = message[:2]
        if len(digraph) == 1:  # caractere único à direita no final da mensagem
            digraph = digraph = "%c%c" % (digraph[0], "X")
            digraphs.append(digraph)
            message = message[1:]
        elif digraph[0] == digraph[1]:  # lida com letras duplas que aparecem no mesmo dígrafo
            digraph = "%c%c" % (digraph[0], "X")
            digraphs.append(digraph)
            message = message[1:]
        else:  # adiciona o dígrafo à lista
            digraphs.append(digraph)
            message = message[2:]

    return digraphs


"""
Funcao: get_coords(digraph, key_matrix)
Retorna as coordenadas das letras no dígrafo fornecido da matriz com a chave fornecida.
Parâmetro: digraph - O dígrafo de duas letras a ser pesquisado na matriz chave.
Parâmetro: key_matrix - A matriz Playfair c/ a chave para realizar a pesquisa.
Retorna: Retorna um array com as coordenadas do dígrafo fornecido.
"""


def get_coords(digraph, key_matrix):
    coords = []
    for char in digraph:
        for x in xrange(5):
            for y in xrange(5):
                if key_matrix[x][y] == char:
                    coords.append((x, y))
    return coords


def main():

    print ("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print ("|               *Criptoanalise*               |")
    print ("|          *Cifra Playfair Tool*              |")
    print ("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

    m = gen_matrix('')
    print ("\nA Matriz PLAYFAIR:\n")
    print_matrix(m)

    print ("Inserir a Chave:")
    k = get_key()

    print ("\nA Matriz PlayFair c/ a Chave:\n")
    m = gen_matrix(k)
    print_matrix(m)

    opcao = ""
    while opcao != "1" and opcao != "2" and opcao != "3":
        print ("+ Escolha uma opção!")
        print ("1 - Cifrar uma mensagem")
        print ("2 - Decifrar uma mensagem")
        print ("3 - Sair")
        print ("=> Opcao:")
        opcao = input()

        if opcao == "1":
            print ("\nMessagem Cifrada:")
            print ("Inserir a mensagem a cifrar. \nSão apenas válidos carateres/letras de A-Z. \nOs pontos serão trocados por um X.")
            message = get_message()
            print ("Mensagem Inserida: %s" % message)
            ciphertext = encrypt(message, m)

        elif opcao == "2":
            print ("\nMensagem Decifrada:")
            print ("Inserir a mensagem a decifrar. \nSão apenas válidos carateres/letras de A-Z.")
            message = get_message()
            print ("Mensagem Inserida: %s" % message)
            plaintext = decrypt(message, m)

        elif opcao == "3":
            print ("Adeus")
            break

main()
