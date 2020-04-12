import solutions.primes


def check_prime_divisible(num, primes):

    for i in primes:
        if num % i != 0:
            return False

    return True

def check_divisible(num):
    for i in range(1,20):
        if num % i != 0:
            return False
    return True


def run():
    print("problem 5")

    num = 20
    primes = solutions.primes.generate(20)
    print(primes)

    done = False
    while (not done):
        num += 1
        if num % 10000000 == 0:
            print(num)

        if (check_prime_divisible(num, primes)):
            if (check_divisible(num)):
                done = True

    print(num)

    
