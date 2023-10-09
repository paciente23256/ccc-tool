#!/usr/bin/python3
# -*- coding: utf-8 -*-


import runpy

"""atalhos"""
def go_cesar():
        runpy.run_path('cesar_tool.py')
def go_playfair():
        runpy.run_path('playfair_tool.py')
def go_railfence():
        runpy.run_path('railfence_tool.py')
def go_vigenere():
        runpy.run_path('vigenere_tool.py')
def go_affine():
        runpy.run_path('affine_tool.py')

if __name__ == "__main__":

    while True:
        print("")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("|               *Criptoanalise*               |")
        print("|                                             |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(*["\033[37;40m1. Cifra de Cesar Tool", "2. Cifra PlayFair Tool", "3. Cifra RailFence Tool" , "4. Cifra Vigenere Tool", "5. Cifra Affine Tool" , "0. Sair"], sep="\n")
        # input do utilizador
        choice = input("Escolha uma opção: ").strip() or "0"

        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

        # executa as funcoes com base no input do utilizador
        if choice not in ("1", "2", "3", "4", "5", "0"):
            print(" ! ERRO. Escolha uma opção válida.")
        elif choice == "1":
            go_cesar()
        elif choice == "2":
            go_playfair()
        elif choice == "3":
            go_railfence()
        elif choice == "4":
            go_vigenere()
        elif choice == "5":
            go_affine()
        elif choice == "0":
            print("Adeus.")
            break
