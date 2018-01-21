def lineDetails(filename):
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

        if item.endswith('A') or item.endswith('E') or item.endswith('H') or item.endswith('R') and item[-5] == '.':
            itemTempList.append(item)

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

    finalList = []

    for item in itemList:
        spaceCount2 = 0
        tempChar = ''
        dpIndex = item.find('.')
        realIndex = dpIndex
        while spaceCount2 < 2:
            tempChar = item[realIndex]
            if tempChar != ' ':
                realIndex -= 1
            else:
                spaceCount2 += 1

        itemName = item[0: realIndex]
        priceIndex = len(item) - realIndex
        price = item[realIndex + 1: len(item) - 2]
        itemQuantityPair = (itemName, float(price))
        finalList.append(itemQuantityPair)

    print (finalList)
    total = 0
    z = 0
    while z < len(finalList):
        price = finalList[z][1]
        total += price
        z += 1
    print (total)
#lineDetails('receiptText.txt')
lineDetails('receiptTextv2.txt')
