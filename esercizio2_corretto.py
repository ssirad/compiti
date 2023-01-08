import sys

minore1 = sys.maxsize
minore2 = sys.maxsize
numero = int(input("Numero: "))

while numero != 0:
    if numero != 0:
        if numero < minore1 and numero < minore2:
            minore1 = minore2
            minore2 = numero
        elif numero < minore1 and numero > minore2:
            minore1 = numero
    numero = int(input("Numero: "))

print(minore2, minore1)
