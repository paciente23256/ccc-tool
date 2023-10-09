#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Exercicio # 13 a) - Cifra de Vigenere - Analise de frequencias

"""
Tabela de frequencias  portuguesa - no qui-quadrado
com duas variaveis (x,y)
i=(xi,yi)
N medidas de uma variável aleatória X. Em cada medida,
a variável X assume os valores x1, x2, ...,xN.

K=(ksize,c)

"""


def get_qui_quadrado(s):
        s=s.lower()
        e_frq= [
        0.1463, 0.0104, 0.0388, 0.0499, 0.1257, 0.0102, 0.0130,
        0.0078, 0.0619, 0.0040, 0.0002, 0.0278, 0.0474, 0.0445,
        0.0974, 0.0252, 0.0120, 0.0653, 0.0681, 0.0434, 0.0364,
        0.0158, 0.0004, 0.0025, 0.0001, 0.0047]
        expct_count={}
        for each in set(s):
            q=ord(each)-97
            expct_count[each]=e_frq[q]*len(s)
        chi_sqr=sum(((s.count(a)-expct_count[a])**2)/expct_count[a] for a in set(s))
        return chi_sqr

def get_key(c,key_size):
    c=c.lower()
    k_string=""
    for l in range(key_size):
        s=""
        for i in range(l,len(c),key_size):
            s+=c[i]
        pos_sets=[]
        for i in range(26):
            pos_sets.append("".join([chr(((ord(each)-97-i)%26)+97) for each in s]).upper())
        chi_sqr_vals=[]
        for i in range(len(pos_sets)):
            chi_sqr_vals.append(get_qui_quadrado(pos_sets[i]))
        k=chr(chi_sqr_vals.index(min(chi_sqr_vals))+97)
        k_string+=k
    return k_string

def decrypt(k,c):
    k_code=[(ord(a)-97) for a in k]
    dcr_msg_code=[]
    for i in range(len(c)):
        dcr_msg_code.append(((ord(c[i])-97)-k_code[i%len(k)])%26)
    dcr_msg=[chr(a+97) for a in dcr_msg_code]
    return "".join(dcr_msg)

#def main():
while True:
    print("")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("|               *Criptoanalise*               |")
    print("|    Analise de frequencias Vigenere          |")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

    c=input("+ Inserir msg cifrada: ")
    key_size=int(input("\n+ Inserir tamanho da chave [int]: "))
    print("+ Chave inserida:",key_size)
    k=get_key(c,key_size)
    print("++ A Chave usada na Cifra: ",k.upper())

    d_opt=input("\n+ Quer desencriptar o criptograma? (S/n)")
    while (d_opt!='s' and d_opt!='n'):
        print("Opção invalida!")

    if d_opt=='s':
        msg=decrypt(k,c)
        print("\n+ Mensagem decifrada:\033[37;40m ",msg)
        print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    else:
        exit()

#if __name__ == '__main__':
#    main()
