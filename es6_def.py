n = int(input("Numero: "))
def count_even_divisors(n):
    count = 0
    for i in range(2, n + 1):
        if n % i == 0 and i % 2 == 0:
            count += 1
    print(count)

count_even_divisors(n)
