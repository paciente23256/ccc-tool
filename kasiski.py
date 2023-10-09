
from math import gcd
from collections import Counter
import subprocess

def c2i(c, alphabet):
    return alphabet.index (c)


def i2c(i, alphabet):
    return alphabet[i]


def prepare_string(s, alphabet):
    temp = s
    alphaList = list (alphabet)
    sList = list (temp)
    for index in range (len (sList)):
        for index2 in range (len (alphaList)):
            if temp[index] == alphaList[index2]:
                break
            if index2 + 1 == len (alphaList):
                sList.remove (temp[index])

    final = ''.join (sList)
    return final


def vigenere_encode(plaintext, key, alphabet):
    plaintext = prepare_string (plaintext, alphabet)
    plainList = list (plaintext)
    keyList = list (key)
    alphaList = list (alphabet)
    encodeText = ""

    for index in range (len (plainList)):
        plainIndex = c2i (plainList[index], alphabet)
        keyIndex = c2i (((keyList[index % len (key)])), alphabet)
        encodeTextIndex = (plainIndex + keyIndex) % (26)
        encodeText += i2c (encodeTextIndex, alphabet)

    return encodeText


def vigenere_decode(ciphertext, key, alphabet):
    ciphertext = prepare_string (ciphertext, alphabet)
    cipherList = list (ciphertext)
    keyList = list (key)
    alphaList = list (alphabet)
    decodeText = ""

    for index in range (len (ciphertext)):
        cipherIndex = c2i (cipherList[index], alphabet)
        keyIndex = c2i (((keyList[index % len (key)])), alphabet)
        decodeTextIndex = (cipherIndex - keyIndex) % (26)
        decodeText += i2c (decodeTextIndex, alphabet)

    return decodeText


def index_of_coincidence(ciphertext, alpha):
    n = float (len (ciphertext))
    alphaList = list (alpha)
    # print("Length of ciphertext: " + str(n))
    c = Counter (ciphertext)
    ioc = 0

    for index in range (len (alphaList)):
        ioc += (ciphertext.count (alpha[index]) * (ciphertext.count (alpha[index]) - 1))

    ioc = ioc * (1 / (n * (n - 1)))

    # print("Index of Coincidence: " + str(ioc))

    return ioc


def kasiski_test(ciphertext):  # Code partially provided
    trigraphList = []
    distanceList = []

    for index in range (len (ciphertext) - 1):
        currentTrigraph = ciphertext[index:index + 3]
        if currentTrigraph not in trigraphList:
            trigraphList.append (currentTrigraph)
        else:
            previousIndex = ciphertext.find (currentTrigraph)
            distance = index - previousIndex
            distanceList.append (distance)

    # Code is provided to find the gcd of any common distances appearing at least twice, just add your array:
    dCount = Counter (distanceList)  # put your array of distances here)
    topCount = dCount.most_common (6)
    my_gcd = topCount[0][0]
    for index in range (1, len (topCount)):
        if topCount[index][1] > 1:
            my_gcd = gcd (my_gcd, topCount[index][0])

    return my_gcd


def run_key_test(ciphertext, alphabet):  # Code provided
    """Runs Kasiski test and formats the output nicely"""
    kasiski = kasiski_test (ciphertext)
    out = "Kasiski determined the key: " + str (kasiski);
    return out



def rotate_list(old_list):  # Code provided
    """Takes the given list, removes the first element, and appends it to the end of the list, then returns the
    new list"""
    new_list = old_list[:]
    new_list.append (old_list[0])
    del new_list[0]
    return new_list


def find_total_difference(list1, list2):
    """Takes two lists of equal length containing numbers, finds the difference between each pair of matching
    numbers, sums those differences, and returns that sum"""
    sum = 0
    for index in range (len (list1)):
        sum += abs (list1[index] - list2[index])

    return sum


def find_likely_letters(coset, alpha, pt_freq):
    alphaList = list (alpha)
    cosetFreqList = []
    for index in range (len (alphaList)):
        cosetFreqList.append ((coset.count (alpha[index])))

    differenceList = []
    for index in range (len (alphaList)):
        differenceList.append (find_total_difference (cosetFreqList, pt_freq))
        cosetFreqList = rotate_list (cosetFreqList)

    letter1 = differenceList.index (min (differenceList))
    letter1 = i2c (letter1, alpha)

    secondSmallestIndex = sorted (differenceList)[1]
    letter2 = i2c (differenceList.index (secondSmallestIndex), alpha)
    # return statement provided.  feel free to replace "letter1" and "letter2" with other variable names.
   # return "the most likely letter is: " + letter1 + " followed by: " + letter2


def crack(ciphertext, alpha, pt_freq):  # Code provided
    """User-friendly walkthrough of decoding methods"""
    print ("Your cipher text is: " + ciphertext)
    out = run_key_test (ciphertext, alpha)
    print (out)


alpha = "abcdefghijklmnopqrstuvwyxz"

pt_freq = [0.1463, 0.0104, 0.0388, 0.0499, 0.1257, 0.0102, 0.0130,
        0.0078, 0.0619, 0.0040, 0.0002, 0.0278, 0.0474, 0.0445,
        0.0974, 0.0252, 0.0120, 0.0653, 0.0681, 0.0434, 0.0364,
        0.0158, 0.0004, 0.0025, 0.0001, 0.0047]



if __name__ == "__main__":
    
    subprocess.call('clear',shell=True)


while True:
    print("")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("|               *Criptoanalise*               |")
    print("|               METODO kASISKI                |")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

    YOURTEXTHERE = input("Introduza a mensagem cifrada: ")
    crack (YOURTEXTHERE, alpha, pt_freq)
