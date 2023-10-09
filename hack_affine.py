
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Cifra Affine Tool - Forca Bruta

import sys, time
import os

# calcula o modulo inverso de um número
def mod_inv (num, mod):
    for x in range(0,mod + 1):
        if ((num*x)%mod == 1):
            return x
        
    sys.exit('ERRO!!: O modulo %d inverso de %d não existe!' % (mod, num))

# verifica arguments
if len(sys.argv) > 1 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
    sys.exit('Excutar brute force a msg inserida' % sys.argv[0])


print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("|               *Criptoanalise*               |")
print("|         *Cifra de Affine - Tool*            |")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+ Ataque - Força Bruta")
# criptograma
msg = input('\n+ Inserir Mensagem/criptograma: ')
# escreve ficheiro
exploit = open('exploit.txt','w')
exploit.write('*** Chaves Testadas ***\n');
# tempo inicial
timer = time.time ()
# Brute force algorito
for i in range(0,26):
    if (i%2 != 0) and (i != 13):
        for j in range(0,26):
            exploit.write('\n# Chave usada <%d,%d>\n# Mensagem : ' % (i,j))
            inv = mod_inv(i,26)
            for c in msg:
                v = ord(c)
                if (v >= 65) and (v <= 90):
                    # maiusc.
                    cip = ((v - 65 - j)*inv + 26)%26 + 65
                elif (v >= 97) and (v <= 122):
                    # minusc.
                    cip = ((v - 97 - j)*inv + 26)%26 + 97
                else:
                    # outros caract
                    cip = v
                # decifra escreve no ficheiro o resultado               
                
                exploit.write('%c' % cip)
                # tempo final
                t = round (time.time () - timer, 2)
               
with open('exploit.txt', 'r') as log:
     print(''.join(log.readlines()))
     print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
     print ('Tempo de processamento : %s ' % t)
     print ('\n') 
     print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

