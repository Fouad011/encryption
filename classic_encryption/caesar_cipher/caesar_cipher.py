def code(x):
    if type(x) is str :
        return ord(x)-65
    elif type(x) is int:
        return chr(x+65)

def chiffre(M, k):
    Mn = normalise(M)
    C = ''
    for c in Mn:
        n = (code(c)+k)%26
        C += code(n)
    return C

def dechiffre(C, k):
    Cn = normalise(C)
    M = ''
    for c in Cn:
        n = (code(c)-k)%26
        M += code(n)
    return M

def normalise(m):
    m = m.upper()
    m = m.split(' ')
    M = ''
    for x in m:
        M += x
    return M

def Menu():
    print("0\t:\tencrypt")
    print("1\t:\tdecrypt")
    s = int(input("enter a number (0 or 1) : "))
    print("message for encrypt or decrypt")
    msg = str(input("message: "))
    print("type of key is integer")
    key = int(input("key: "))
    if s==0:
        print("cipher text message : ", chiffre(msg, key))
    elif s==1:
        print("plain text message : ", dechiffre(msg, key))

Menu()
