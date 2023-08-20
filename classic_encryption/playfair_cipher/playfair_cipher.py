def code(x):
    if type(x) is str :
        return ord(x)-65
    elif type(x) is int:
        return chr(x+65)

def getTab(K):
    dic = dict()
    k = K.upper()
    tab = []
    for x in k:
        if x not in tab:
            tab.append(x)
    for x in map(code, range(26)):
        if x not in tab:
            tab.append(x)
    t = [[0]*5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            t[i][j] = tab[(5*i)+j]
    return t

def doubleChar(m):
    M = normalise(m)
    D = list()
    for i in range(0, len(M)-1, 2):
        D.append(M[i]+M[i+1])
    return D

def position(M, tab):
    d = dict()
    for i in range(5):
        for j in range(5):
            for k in range(len(M)):
                if tab[i][j] == M: return (i, j)

def newCharChef(c1, c2, tab):
    pc1 = position(c1, tab)
    pc2 = position(c2, tab)
    i1, j1 = pc1
    i2, j2 = pc2
    if i1==i2: return(tab[i1][(j1+1)%5]+tab[i1][(j2+1)%5])
    elif j1==j2: return(tab[(i1+1)%5][j1]+tab[(i2+1)%5][j1])
    else: return(tab[i1][j2]+tab[i2][j1])

def newCharDechef(c1, c2, tab):
    pc1 = position(c1, tab)
    pc2 = position(c2, tab)
    i1, j1 = pc1
    i2, j2 = pc2
    if i1==i2: return(tab[i1][(j1+4)%5]+tab[i1][(j2+4)%5])
    elif j1==j2: return(tab[(i1+4)%5][j1]+tab[(i2+4)%5][j1])
    else: return(tab[i1][j2]+tab[i2][j1])

def chiffre(m, k):
    M = normalise(m)
    tab = getTab(k)
    C = ''
    for x in doubleChar(M):
        C += newCharChef(x[0], x[1], tab)
    return C

def dechiffre(c, k):
    C = normalise(c)
    tab = getTab(k)
    M = ''
    for x in doubleChar(C):
        M += newCharDechef(x[0], x[1], tab)
    return M

def normalise(m):
    m = m.upper()
    m = m.split(' ')
    M = ''
    for x in m:
        M += x
    return M

def clef(k):
    K = normalise(k)
    cles = []
    for c in K:
        cles.append(code(c))
    return cles

def Menu():
    print("0\t:\tencrypt")
    print("1\t:\tdecrypt")
    s = int(input("enter a number (0 or 1) : "))
    print("\tmessage for encrypt or decrypt")
    msg = str(input("msg: "))
    print("\ttype of key is string")
    key = str(input("text key: "))
    if s==0:
        print("encrypt message : ", chiffre(msg, key))
    elif s==1:
        print("decrypt message : ", dechiffre(msg, key))

Menu()
