'''
Esercizio 2: Realizzare un programma per il calcolo del volume di un castello costituito da un corpo cubico e da 4 torri a forma di cilindro
sormontate da una guglia a forma di cono.
'''

from math import pi

def volume_cubo(lato):
    volume = lato**3
    return volume

def volume_cilindro(raggio, altezza):
    volume = raggio**2 * pi * altezza
    return volume

def volume_cono(raggio, altezza):
    volume = (raggio**2 * pi * altezza)/3
    return volume

def main():
    r = float(input("raggio cilindri: "))
    h = float(input("altezza cilindri: "))
    h2 = float(input("altezza coni: "))
    l = float(input("lato castello: "))

    cubo = volume_cubo(l)
    cilindro = volume_cilindro(r, h)
    cono = volume_cono(r, h2)
    print("volume castello: ", cubo + cilindro * 4 + cono * 4)

main()
