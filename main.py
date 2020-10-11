def tabla (x):
    mult=1
    while mult <= 10:
        res=x*mult
        print(str(x) + "x" + str(mult) + "=" + str(res))
        mult = mult + 1

tabla(3)

def bucle():
    for i in range(30,50,1):
        print (i)

bucle()

def ConvertFtoC(x):
    res=((9/5) * x + 32)
    return res

def TablaF():
    for i in range(0,130,10):
        print(str(i) + "C= " + str(ConvertFtoC(i)))

TablaF()

def esBisiesto(x):
    if x%4 == 0 and (x%400 == 0 or x%100 != 0):
        return True
    return False

print(esBisiesto(2020)) # Año Bisiesto. tiene que dar True
print(esBisiesto(2019)) # Año común. False
print(esBisiesto(1900)) # 1900 es divisible entre 4 pero no es divisible por 400, es un año común. False
print(esBisiesto(2000)) # 200 es divisible entre 4 y 400, es un año Bisiesto. True

def diaDelMes(x):
    dias = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if x >= 1 and x<=12:
        return dias.get(x)
    return -1

print(diaDelMes(5))
print(diaDelMes(2))
print(diaDelMes(13))

def fechaValida(d,m,aaaa):
    valido=False

    if diaDelMes(m) > 0:
        if d>=1 and d<= diaDelMes(m):
            valido=True
        else:
            valido=False;

        if m==2 and esBisiesto(aaaa):
            if d>=1 and d <=(diaDelMes(m)+1):
                valido= True

    return valido

print(fechaValida(29,2,2020))
print(fechaValida(32,3,2020))
print(fechaValida(24,9,2020))

def Mayusculas(cadena):
    res=""
    for i in cadena:
        if i.isupper():
            res="".join([res, i])
    return res


print(Mayusculas("Universal Serial Bus"))