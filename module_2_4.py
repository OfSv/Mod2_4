numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []


for i in range(1, len(numbers)):
    is_prime = True
    for j in range(len(primes)):
        if numbers[i] % primes[j] == 0:
            is_prime = False
            break
        else:
            continue
    if is_prime == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
        continue

print("Простые числа: ", primes)
print("Составные числа: ", not_primes)
