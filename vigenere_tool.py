#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Cifra VIGENERE - tool

#Alfabeto - maiusculas

from string import ascii_uppercase
# Este módulo fornece acesso ao Unicode Character Database (UCD) que define as propriedades dos caracteres para todos os caracteres Unicode
import unicodedata
#Expressores regurales
import re, runpy


def go_vegenere_freq():
        runpy.run_path('vegenere_freq.py')
def go_kasiski():
        runpy.run_path('kasiski.py')
  

"""
VIGENERE
"""

class vigenere (object):

  #Remove acentos e passa para maiuscula
  def parse_msg(self, original):
    msg = unicodedata.normalize("NFD", original)
    msg = msg.encode("ascii", "ignore")
    msg = msg.decode("utf-8")
    msg = self.maiusculo(msg)
    return msg

  #Passar msg para maiusculas
  def maiusculo(self, msg):
    msg = msg.upper()

    return msg

  #Transcreve a msg com a palavra-chave
  def transcrever(self, msg, chave):
    tam_msg = len(msg)
    tam_chave = len(chave)

    transcrito = ""
    ponteiro = 0

    for i in range(tam_msg):
      if((ord(msg[i]) >= 65) and (ord(msg[i]) <= 90)):
        transcrito = "".join((transcrito,chave[ponteiro]))

        if(ponteiro == tam_chave-1):
          ponteiro = 0
        else:
          ponteiro += 1
      else:
        transcrito = "".join((transcrito,msg[i]))
    return transcrito

  def alfabeto(self):
    alfabeto = ascii_uppercase
    alfabeto = list(alfabeto)
    return alfabeto

  #Monta a tabela da cifra
  def montar_tabela(self):
    tabula = []
    alfabeto = self.alfabeto()

    for i in range(len(alfabeto)):
      tabula.append(alfabeto)
      alfabeto = alfabeto[1:] + alfabeto[:1]

    return tabula

  #cifra a mensagem: frase original + frase transcrita = frase cifrada
  def cifrar_msg(self, msg, chave):
    msg = self.parse_msg(msg)
    chave = self.parse_msg(chave)
    transcrito = self.transcrever(msg, chave)

    cifrado = ""
    alfabeto = self.alfabeto()
    tabula = self.montar_tabela()

    for i in range(len(msg)):
      if((ord(msg[i]) >= 65) and (ord(msg[i]) <= 90)):
        ind_msg = alfabeto.index(msg[i])
        ind_trans = alfabeto.index(transcrito[i])
        cifrado = cifrado + tabula[ind_msg][ind_trans]
      else:
        cifrado = cifrado + msg[i]

    return cifrado

  # Decifra a mensagem: frase cifrada + palavra chave = frase original
  def decifrar_msg(self, cifrado, chave):
    cifrado = self.parse_msg(cifrado)
    chave = self.parse_msg(chave)
    transcrito = self.transcrever(cifrado, chave)
    decifrado = ""
    alfabeto = self.alfabeto()
    tabula = self.montar_tabela()

    for i in range(len(cifrado)):
      if((ord(cifrado[i]) >= 65) and (ord(cifrado[i]) <= 90)):
        ind_p_chave = alfabeto.index(transcrito[i])
        ind_cifrado = tabula[ind_p_chave].index(cifrado[i])
        decifrado = decifrado + alfabeto[ind_cifrado]
      else:
        decifrado = decifrado + cifrado[i]

    return decifrado


"""
Ataque Vigenere
"""

class ataque (object):
  def encontrar_espacamento(self, cifrado):
    cifrado_norm = self.remover_espaco_esp(cifrado)
    sequencia_espacamento = []

    #verifica o espaçamento de sequencias repetidas. Tamanho = 3
    for i in range(len(cifrado_norm)):
      #Agarra 3 letras em sequencia
      if (i+2 < len(cifrado_norm)):
        sequencia = cifrado_norm[i] + cifrado_norm[i+1] + cifrado_norm[i+2]

        #escolhidas as 3 letras, verifica no resto do texto quantas vezes encontra a sequencia
        for j in range(len(cifrado_norm)):
          if(j+2 < len(cifrado_norm)):
            sequencia_2 = cifrado_norm[j] + cifrado_norm[j+1] + cifrado_norm[j+2]
            #Se a sequencia do primeiro for tiver sido encontrada no texto, insere essa sequencia no array com seu espaçamento
            if((sequencia == sequencia_2)):
              if(j>i):
                espacamento = j-i
              else:
                espacamento = i-j

              elemento = [sequencia, espacamento]

              if ((elemento not in sequencia_espacamento) and elemento[1] != 0):
                sequencia_espacamento.append([sequencia, espacamento])
          else:
            break
      else:
        break

    return sequencia_espacamento

  #Remove espaços e caracteres especiais
  def remover_espaco_esp(self, cifrado):
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', cifrado)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço. incluir numeros: re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)
    texto = re.sub('[^a-zA-Z \\\]', '', palavraSemAcento)
    texto = texto.replace(" ", "")

    #retorna o texto cifrado apenas com as letras
    return texto

  def obter_fatores(self, sequencia_espacamento):
    fatores = []
    fator_comum = []

    for i in range(len(sequencia_espacamento)):
      if sequencia_espacamento[i][1] not in fatores:
        fatores.append(sequencia_espacamento[i][1])

    #encontra os fatores
    for fator in fatores:
      for divisor in range(2, fator+1):
        if (fator % divisor == 0):
          fator_comum.append(divisor)

    #conta quantas vezes cada fator aparece
    contador = 0
    qtd_fator = []
    for fator in fator_comum:
      for i in fator_comum:
        if fator == i:
          contador += 1
      if [fator, contador] not in qtd_fator:
        qtd_fator.append([fator, contador])
      contador = 0

    return qtd_fator

  def possiveis_tam_chave(self, qtd_fator):
    total = 0
    for fator in qtd_fator:
      total = total + fator[1]

    print("Os possíveis tamanhos da chave são: ")
    for fator in qtd_fator:
      percentual = (fator[1]*100)/total
      print(fator[0], "-", percentual, "%")
    print("\n")

"""
MAIN MENU

"""
cifra = vigenere()
ataque = ataque()

while True:
    print("")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("|               *Criptoanalise*               |")
    print("|         *Cifra de Vigenere - Tool*          |")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print(*["1. Cifrar", "2. Decifrar", "3. Frequencias", "4. Posssiveis Chaves" ,"5. Kasiski" , "0. Sair"], sep="\n")
    # input do utilizador
    choice = input("Escolha uma opção: ").strip() or "0"

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

    # executa as funcoes com base no input do utilizador
    if choice not in ("1", "2", "3", "4", "5", "0"):

        print(" ! ERRO. Escolha uma opção válida.")

    elif choice == "1":
        msg = input("+ Inserir msg a ser cifrada: ")
        chave = input("+ Inserir a palavra-chave: ")
        cifrado = cifra.cifrar_msg(msg, chave)
        print("\n+ Mensagem Cifrada:")
        print(cifrado)

    elif choice =="2":
        cifrado = input("+ Inserir msg a cifrada: ")
        chave = input("+ Inserir a palavra-chave: ")
        decifrado = cifra.decifrar_msg(cifrado, chave)
        print("\n+ Texto Decifrado:")
        print(decifrado)
    elif choice =="3":
      go_vegenere_freq()
      
    elif choice =="4":
        cifrado_atk = input("+ Iniciar Ataque -> msg cifrada: ")
        sequencia_espacamento = ataque.encontrar_espacamento(cifrado_atk)
        qtd_fator = ataque.obter_fatores(sequencia_espacamento)
        tam_chave = ataque.possiveis_tam_chave(qtd_fator)
    elif choice =="5":
      go_kasiski()
    

    elif choice == "0":
        print("Adeus.")
        break
