a = float(input("Lunghezza: "))
b = float(input("Profondità: "))
c = float(input("Altezza: "))

def volume(a, b, c):
    area_base = a*b
    volume = area_base*c
    print(volume)
    
volume(a, b, c)
