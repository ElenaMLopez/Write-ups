
p = 11
q = 13
d = 103
texto = "Bv>!cb;[-1;b	'>b[;Pb,-!P>&'vd-bd>P,vw1;1-b>bdv1>b	'>b;b,;O>b>PbY1y-;,Dv!&"

def descifrar(texto):
    t2=""
    for caracter in texto:
        t2 += chr(ord(caracter)**d % (p*q))
    return t2

print(descifrar(texto))
