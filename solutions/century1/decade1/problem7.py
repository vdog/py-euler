
import solutions.primes

def run():
    print("problem7")

    primes = solutions.primes.generate(125000)
    print(len(primes))
    print(primes[9999])
    print(primes[10000])
    print(primes[10001])
