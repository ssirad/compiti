'''
Esercizio 1: Si vuole calcolare la superficie di un razzo approssimabile come corpo a un cilindro (raggio di base r e altezza h1),
come testa a un cono (raggio di base sempre r e altezza h2) e con 4 alettoni approssimabili a dei triangoli rettangoli uguali
(di cateti c1 e c2 e spessore irrilevante).
'''
from math import pi, sqrt

def area_alettoni(cat_1, cat_2):
    #   area triangolo = (b * h)/2
    area = (cat_1 * cat_2)/2
    return area

def area_cilindro(raggio, altezza):
    #   cilindro = (2πr * h) + πr**2
    area_laterale = raggio * altezza * pi
    area_tot = area_laterale + pi * raggio**2
    return area_tot

def area_cono(raggio, altezza):
    #   cono = πr * a
    apotema = sqrt(raggio**2 + altezza**2)
    area_laterale = apotema * pi * raggio
    return area_laterale

def main():
    r = float(input("raggio base: "))
    h1 = float(input("altezza cilindro: "))
    h2 = float(input("altezza cono: "))
    c1 = float(input("cateto 1 alettoni:"))
    c2 = float(input("cateto 2 alettoni:"))

    alettoni = area_alettoni(c1, c2)
    cilindro = area_cilindro(r, h1)
    cono = area_cono(r, h2)
    area_razzo = alettoni * 4, cilindro, cono
    print(area_razzo)
main()

