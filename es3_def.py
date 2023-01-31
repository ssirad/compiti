nome = input("nome: ")
n = int(input("Quante volte? "))

def messaggio(m, n):
    if n%2 == 0:
        for i in range(n):
            print(m)
    else:
        for i in range(n):
            print("Gino")

messaggio(nome, n)
