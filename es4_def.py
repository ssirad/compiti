t = int(input("Tempo(s): "))
a = int(input("Accelerazione(m/s²): "))

def velocita(t, a):
    v = a*t
    print(v)
    
velocita(t, a)
