alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

filename = "1000popEngWords.txt"

def caeserShift(cipher):
    """
    Takes a cipher line and saves all the caesar shift
    combinations which gets returned
    """

    shiftList = []
    for i in range(len(alphabet)):
        plainText = ""
        for x in range(len(cipher)):
            currLetterPos = alphabet.index(cipher[x].upper())
            plainLetterPos = (currLetterPos+i) % len(alphabet)
            plainText += alphabet[plainLetterPos]
        print "+" + str(i) + ") " + plainText
        shiftList.append(plainText)
    return shiftList

def findMostProbable(shiftList):
    """
    Takes the shift list from caesarShift()
    and checks every line against every line in
    the popular 1000 word list. It keeps a counter
    for every shift and the highest one gets
    the shifted word returned.
    """
    max = 0
    winnerShift= ""

    popList = []
    with open(filename) as f:
        popList = f.read().splitlines()

    for i in range (len(shiftList)):
        points = 0
        for j in range(len(popList)):
            if popList[j].upper() in shiftList[i]:
                points+= 1
        if points > max:
            max = points
            winnerShift = shiftList[i]

    return winnerShift

def main():
    cipherText = "QEBNRFZHYOLTKCLUGRJMPLSBOQEBIXWVALD"
    shiftList = caeserShift(cipherText)
    winner = findMostProbable(shiftList)
    print "\n" + "Most probable: " + winner

if __name__ == "__main__":
    main()