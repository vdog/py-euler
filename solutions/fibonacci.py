

def generate(max):
    if max < 1:
        return []
    if max == 1:
        return [1]
    if max == 2:
        return [1, 2]

    prev2 = 1
    prev1 = 2
    fibs = [1, 2]
    fib = prev1 + prev2
    while fib <= max:
        fibs.append(fib)
        prev2 = prev1
        prev1 = fib
        fib = prev1 + prev2

    return fibs


