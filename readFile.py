def lineDetails(filename):
    itemCount = 0
    randomList = []
    itemTempList = []
    itemList = []
    fin = open(filename, encoding="utf-8")
    for line in fin:
        lineLength = len(line)
        lastIndexOfString = lineLength - 1
        randomList.append(line.rstrip())

    for item in randomList:
        length = len(item)
        lastIndex = length - 1

        if item == '':
            pass

        if item.endswith('A') or item.endswith('E') or item.endswith('H') and item[-5] == '.':
            itemTempList.append(item)
            itemCount += 1

    for i in itemTempList:
        spaceCount = 0

        if i[0] == 'E': # Case 1, 2 spaces
            while spaceCount < 2:

                if i[0] != ' ':
                    i = i[1:]
                else:
                    spaceCount += 1

                    i = i[1:]

            itemList.append(i)

        elif i[0].isdigit(): # Case 2, 1 space
            while spaceCount < 1:
                if i[0] != ' ':
                    i = i[1:]
                else:
                    spaceCount += 1
                    i = i[1:]

            itemList.append(i)
        else:
            pass

    print (itemList)

# char -> boolean
def notLetters(x):
    if ord(x) < 65 or ord(x) > 122:
        return True
    else:
        return False

lineDetails('receiptText.txt')
