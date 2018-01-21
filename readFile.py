def lineDetails(filename):
    fin = open(filename, encoding="utf-8")
    for line in fin:
        print (line)
lineDetails('receiptText.txt')
