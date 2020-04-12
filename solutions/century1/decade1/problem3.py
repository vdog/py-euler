import solutions.primes
def run():
    print("problem3")
    primes = solutions.primes.generate(10000)
    print(primes)
    start = 600851475143

    maxp = 0
    for p in primes:
        if start % p == 0:
            maxp = p

    print(maxp)
