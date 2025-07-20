from collections import Counter

text = '''EPAHR ELNFO CPOIO ASROS MWIWA SOTAV TIOES INDED DXTAT YTNTU OMEPC ASFCR
LTORN MOGRA SAORO SLLAH AMGAB OGTEW DOSME ILOOO DRFTA TVABT RHDER DEXPH
NOYIP WIITO CEDON WIRTU LMRNX LWAIN OVTUH LIONN XARLU SOTSS RNNMI EGERH
AATCE FRMOS NS'''.replace("\n","")

keyword = "CAVALRY"
def getArray(keySize,text):
    i = 0
    o = []
    while i < len(text):
        o.append(text[i:min(i+keySize,len(text))])
        i += keySize
    return o

def valid(plaintext, array):
    for y in range(0,len(array)):
        if plaintext <= Counter(array[y]):
            return True
        for i in range(1,len(keyword)):
            c1 = Counter(keyword[0:i])
            c2 = Counter(keyword[i:len(keyword)])
            if c1 <= Counter(array[y-1]) and c2 <= Counter(array[y]):
                return True

    return False

def run():
    for keySize in range(2,50):
        plaintext = Counter(keyword)
        arr = getArray(keySize, text)
        if valid(plaintext=plaintext, array=arr):
            print(keySize)

run()
print("----\nend")