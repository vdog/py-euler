import solutions.fibonacci
def run():
    #prev2 = 1
    #prev1 = 2
    #fib = prev1 + prev2
    #sum = 2
    #while fib < 4000000:
    #    if (fib % 2 == 0):
    #        sum += fib
    #    prev2 = prev1
    #    prev1 = fib
    #    fib = prev1 + prev2
    #print(sum)
    fibs = solutions.fibonacci.generate(4000000)
    sum = 0
    for f in fibs:
        if f % 2 == 0:
            sum += f
    print(sum)
