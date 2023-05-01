def code(x):
    if type(x) is str :
        return ord(x)-65
    elif type(x) is int:
        return chr(x+65)

def chiffre(M, k):
    Mn = normalise(M)
    C = ''
    i = 0
    for c in Mn:
        n = (code(c)+k[i])%26
        C += code(n)
        i += 1
        if len(k)==i:
            i = 0
    return C

def dechiffre(C, k):
    Cn = normalise(C)
    M = ''
    i = 0
    for c in Cn:
        n = (code(c)-k[i])%26
        M += code(n)
        i += 1
        if len(k)==i:
            i = 0
    return M

def normalise(m):
    m = m.upper()
    m = m.split(' ')
    M = ''
    for x in m:
        M += x
    return M

def clef(k):
    cles = []
    for c in k:
        cles.append(code(normalise(c)))
    return cles

def Menu():
    print("0\t:\tencrypt")
    print("1\t:\tdecrypt")
    s = int(input("enter a number (0 or 1) : "))
    print("message for encrypt or decrypt")
    msg = str(input("msg: "))
    print("type of key is string")
    cle = str(input("text key: "))
    key = clef(cle)
    if s==0:
        print("encrypt message : ", chiffre(msg, key))
    elif s==1:
        print("decrypt message : ", dechiffre(msg, key))

Menu()
