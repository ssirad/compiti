numero = int(input("Numero: "))
minore1 = numero
minore2 = minore1
while numero != 0:
    numero = int(input("Numero: "))
    if numero != 0:
        if numero < minore1 and numero < minore2:
            minore1 = minore2
            minore2 = numero
        elif numero < minore1 and numero > minore2:
            minore1 = numero
        elif minore2 == minore1:
            minore2 = numero
else:
    print(minore1, minore2)
