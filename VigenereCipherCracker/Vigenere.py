# Helpful sources:
# http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher/
# https://www.youtube.com/watch?v=LaWp_Kq0cKs
# http://homework.nwsnet.de/releases/8c5e/

from collections import Counter
import sys

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}


def createShiftedCipher(cipher, space):
    emptySpaces = ""
    for i in range(space):
        emptySpaces = " " + emptySpaces
    shiftedCipher =  emptySpaces + cipher
    shiftedCipher = shiftedCipher[0: len(cipher)]
    return shiftedCipher


def calcCoincidences(original, newStr):
    counter = 0
    for i in range(len(original)):
        if original[i] is newStr[i]:
            counter+=1
    return counter


def findKeySize(cipher):
    shift = 0
    max = 0

    for i in range (1, len(cipher)):
        shiftedCipher = createShiftedCipher(cipher, i)
        result = calcCoincidences(cipher, shiftedCipher)

        if (max <  result):
            max = result
            shift = i

    print "shift is max at " + str(shift) + " with " + str(max) + " coincidences"
    return shift


def breakIntoBlocks(cipher, shift):
    blockShiftList = []

    for i in range(shift):
        list = cipher[i:][::shift]
        blockShiftList.append(list)
    return blockShiftList

def calcLetterFreqInBlock(block):
    freqDict = Counter(block)
    for i in range(len(alphabet)):
        freqDict[alphabet[i]] = freqDict[alphabet[i]]/float(len(block))
    return freqDict

def findMostProbableLetter(blockFreqDict):
    # This is the most tricky part.
    # You must be careful with what you're shifting.
    # Are you shifting the frequency of the english letter distribution or
    # the the block text's distribution when the other stays fixed?
    # Whatever you do, make sure you correlate the right shifting number
    # or else you could get the wrong shift and wrong letter.
    # Here, the English Freq stays the same, but block freq moves -1
    #
    # For example, shift 0 first iteration:  accum += English Freq ["A"] * Block Freq ["A"]
    # Then shift 1 first iteration: accum += English Freq ["A"] * Block freq ["B"]
    # NOT THIS ONE: English Freq ["B"] * block freq ["A"]
    # See how both shifted alignment by 1 in different ways? It affects the answer.
    # Later it affects how you shift when you decrypt.

    max = 0
    shift = 0
    for x in range(len(alphabet)):
        accum = 0
        for i in range(len(alphabet)):
            shiftedLetterPos = (i + x) % len(alphabet)
            currLetter = alphabet[i]
            shiftedLetter = alphabet[shiftedLetterPos]
            accum += blockFreqDict[shiftedLetter] * (englishLetterFreq[currLetter])
        if max < accum:
            max = accum
            shift = x

    return alphabet[shift]

def findKey(blockList):
    key = ""
    for i in range(len(blockList)):
        blockFreqDict = calcLetterFreqInBlock(blockList[i])
        key += findMostProbableLetter(blockFreqDict)
    return key


def caesarShift(string, shift):
    result = ""
    for i in range(len(string)):
        letter = string[i]
        letterPos = alphabet.index(letter)
        letterPos = (letterPos + shift) % len(alphabet)
        result += (alphabet[letterPos])
    return result


def decrypt(cipher, key):
    plainText = ""
    for i in range(len(cipher)):
        currLetter = cipher[i]
        shiftLetter = key[i%len(key)]
        letterPos = alphabet.index(currLetter)
        shiftLetterPos = alphabet.index(shiftLetter)
        plainLetterPos = (letterPos - shiftLetterPos) % len(alphabet)
        plainText += alphabet[plainLetterPos]
    print plainText


cipherText = 'KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'


keySize = findKeySize(cipherText)
blockList = breakIntoBlocks(cipherText, keySize)
print "block list"
print blockList
print ""
key = findKey(blockList)
print "Key: " + key + "\n"
decrypt(cipherText, key)
