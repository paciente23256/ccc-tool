#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Cifra Affine Tool

import subprocess, runpy
#import brutefoce from hack_affine

def go_affine_bforce():
    runpy.run_path('hack_affine.py')
        
def chk_fact(number):
    divisor = number
    dividend = 26
    remainder = dividend % divisor
    while remainder > 0:
        dividend =  divisor
        divisor = remainder
        remainder = dividend % divisor
    if divisor != 1:
        print ('O valor de alfa não pode ser obtido')
        quit()
    else:
        pass

def strcheck():
    cont = ''
    while cont != "I":
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        str = input('Enter the string to be encrypted: ')
        if str == "":
            print ('A msg não pode estar em branco')
            cont = ''
            while cont != 'X':
                cont = input('Carregue  S or N para continuar: ')
                if cont.upper() == 'S':
                    cont = 'X'
                elif cont.upper() == 'N':
                    cont = input('Operação cancelada')
                    quit()
                else:
                    print('opcao invalida')
                    continue
        else:
            cont == "I"
            return(str)

def moduloinverse(a_var):
    remainder = 0
    multiple = 0
    while remainder != 1:
        divisor = 26
        dividend = a_var*multiple
        remainder = dividend % divisor
        multiple += 1
    return(multiple-1)

"""

C = [(P * a) + b] mod n        # C = Texto cifrado , P = Texto em Claro, n = 26 (comprimento dos carateres)
P = [(C – b) * a^(-1) ] mod n  # (a,b) as 2 chaves usadas para a cifra Affine.

"""

def encrypt(input_str):
    for var in input_str:
                if var in alphabet_list:
                    x = alphabet_list.index(var)
                    newvalue = a_var*x + b_var
                    newvalue = newvalue%26
                    encrypt_temp = alphabet_list[newvalue]
                    encrypt_temp = encrypt_temp.upper()
                    encrypt_list.append(encrypt_temp)
    encryptmsg=''.join(encrypt_list)
    print('A mensagem cifrada é: ', encryptmsg)


def decrypt(input_str):
    a_var_inverse = moduloinverse(a_var)
    for var in input_str:
                if var in alphabet_list:
                    x = alphabet_list.index(var)
                    newvalue = a_var_inverse*(x - b_var)
                    if newvalue >= 0:
                        newvalue = newvalue%26
                    else:
                        multiple = 1
                        difference = -1
                        while difference <= 0:
                            factor = multiple*26
                            difference = factor + newvalue
                            multiple += 1
                        newvalue = difference % 26
                    decrypt_temp = alphabet_list[newvalue]
                    decrypt_list.append(decrypt_temp)
    decryptmsg=''.join(decrypt_list)
    print('A Mensagem Decifrada é:  ', decryptmsg)



if __name__ == "__main__":

    subprocess.call('clear',shell=True)

while True:

    print("")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("|              * Criptoanalise*               |")
    print("|         *Cifra de Affine - Tool*            |")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print(*["1. cifrar", "2. decifrar", "3. Força-Bruta", "0. Sair"], sep="\n")
    # input do utilizador
    choice = input("Escolha uma opção: ").strip() or "0"

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

    # executa as funcoes com base no input do utilizador
    if choice not in ("1", "2", "3", "0"):
        print(" ! ERRO. Escolha uma opção válida.")
    elif choice == "1":
        alphabet_list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        encrypt_list = list()
        input_str_list = list()
        cont = ''
        a_var = int(input ('Inserir Valor de Alpha: '))
        b_var = int(input ('Inserir Valor de Beta:  '))
        if a_var in range(1,26):
            if a_var != 26:
                chk_fact(a_var)
                input_str = strcheck()
                input_str = input_str.lower()
                encrypt(input_str)
    elif choice == "2":
        alphabet_list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        decrypt_list = list()
        input_str_list = list()
        cont = ''
        a_var = int(input ('Inserir Valor de Alpha: '))
        b_var = int(input ('Inserir Valor de Beta:  '))
        if a_var in range(1,26):
            if a_var != 26:
                chk_fact(a_var)
                input_str = strcheck()
                input_str = input_str.lower()
                decrypt(input_str)
            else:
                print (' O valor do alpha deve ser entre 1-26')
    elif choice == "3":
        go_affine_bforce()
        
    elif choice == "0":
        print("Adeus.")
        break

