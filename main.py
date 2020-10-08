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