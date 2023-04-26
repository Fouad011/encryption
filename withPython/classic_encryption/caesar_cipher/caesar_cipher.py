def codage(c):
    tab = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(0, 26)))
    return tab[c]
def decodage(n):
    tab = dict(zip(range(0, 26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    return tab[n]
def chiffre(M, k):
    Mn = normalise(M)
    C = ''
    for c in Mn:
        n = (codage(c)+k)%26
        C += decodage(n)
    return C
def dechiffre(C, k):
    Cn = normalise(C)
    M = ''
    for c in Cn:
        n = (codage(c)-k)%26
        M += decodage(n)
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
    msg = str(input("msg: "))
    print("type of key is integer")
    key = int(input("key: "))
    if s==0:
        print("encrypt message : ", chiffre(msg, key))
    elif s==1:
        print("decrypt message : ", dechiffre(msg, key))
Menu()
