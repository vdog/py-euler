

def generate(max):
    if max < 2:
        return []

    sieve = [1] * max
    sieve[0] = 0
    sieve[1] = 0

    primes = []
    for i in range(2, max):
        if sieve[i] == 1:
            for j in range(i, max):
                if j % i == 0:
                    sieve[j] = 0
            primes.append(i)

    return primes



