#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Cifra de cesar Tool (2 files)

import runpy, sys

def go_cesar():
        runpy.run_path('cesar_tool.py')

def go_playfair():
        runpy.run_path('playfair_tool.py')

def go_railfence():
        runpy.run_path('railfence_tool.py')

def go_vigenere():
        runpy.run_path('vigenere_tool.py')

def menu():
    
    while True:

        print("")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("|       MESI2022 *CCA - Criptoanalise*        |")
        print("|            Oscar | Pedro | Rui              |")
        print("|         *Cifra de Caesar - Tool*            |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(*["\033[37;40m1. Cifrar", "2. Decifrar", "3. Brute-Force" , "4. Analise de Frequencias" , "0. Sair"], sep="\n")
        # input do utilizador
        choice = input("Escolha uma opção: ").strip() or "0"

        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

        # executa as funcoes com base no input do utilizador
        if choice not in ("1", "2", "3", "4", "0"):
            print(" ! ERRO. Escolha uma opção válida.")
        elif choice == "1":
            go_cesar
        elif choice == "2":
            go_playfair
        elif choice == "3":
            go_railfence
        elif choice == "4":
            go_vigenere
        elif choice == "0":
            print("Adeus.")
            break
        
