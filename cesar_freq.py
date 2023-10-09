'''
Cifra de cesar ataque de frequencias

'''

import string, sys, re, subprocess

"""
decifra
"""

def decrypt(key, ciphertext):
    '''
      parametros: char key - deslocamento de A
      string texto cifrado - mensagem codificada a ser lida
      desc: decifra a mensagem invertendo o deslocamento de cada letra por chave
    '''
    shift = ord(key.upper()) - 65
    plaintext = ""
    for c in ciphertext.upper():
        if ord(c) != ord(" "):
            nchar = chr(ord(c) - shift)
            if ord(nchar) < 65:
                nchar = chr(ord(nchar) + 26)
            elif ord(nchar) > 90:
                nchar = chr(ord(nchar) - 26)
            plaintext += nchar
        else:
            plaintext += " "
    return plaintext

if __name__ == '__main__':

    subprocess.call('clear',shell=True)

try:
    # modo auto: obtem texto cifrado de opt
    raw_ciphertext = sys.argv[1]
except:
    # Menu - input do utilizador
        
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("|              * Criptoanalise*               |")
      print("|       Cifra de Caesar -  Frequencias        |") 
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
raw_ciphertext = input("+ Inserir A Chave Cifrada: ")
raw_bruteforce = input("\n+ forca bruta?: n ")
  
ciphertext = raw_ciphertext.upper()
if (raw_bruteforce.upper()).find("Y") != -1:
    bruteforce = True
else:
    bruteforce = False

# verifique a frequência de ocorrência de cada letra (A a Z)
for l in list(map(chr, range(ord('A'), ord('[')))):
    freq = ciphertext.count(l) / float(len(ciphertext.replace(" ", "")))
    # se a letra aparecer 10% ou mais, pode ser 'E'
    if freq >= .1 or bruteforce:
        # rodapara que a chave de descriptografia seja A 
        key = chr(ord(l) - 4)
        if ord(key) < 65:
            key = chr(ord(key) + 26)
        elif ord(key) > 90:
            key = chr(ord(key) - 26)

        print("\n=> Chave Possivel: A=" + key + ". A decifrar..")
        print(decrypt(key, ciphertext) + "\n")


print("+ Numero de frequencias encontras no criptograma")
print("Letra E")
print(len(re.findall("e", raw_ciphertext)))
print("Letra O")
print(len(re.findall("o", raw_ciphertext)))
print("letra S")
print(len(re.findall("s", raw_ciphertext)))
print("letra R")
print(len(re.findall("r", raw_ciphertext)))
