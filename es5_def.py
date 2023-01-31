a = float(input("Lunghezza: "))
b = float(input("Profondità: "))
c = float(input("Altezza: "))
n = int(input("Numero piani: "))


def volume(a, b, c, n):
    volum = 0
    for i in range(n):
        area_base = a*b
        v = area_base*c
        volum += v
    print(volum)

volume(a, b, c, n)
