

def sum(max):
    retval = max * max + max
    retval /= 2
    return int(retval)

def sum_of_squares(max):
    retval = 0
    for i in range(1, max+1):
        retval = i * i + retval
    return int(retval)

def run():
    print("problem6")

    print(sum(10))
    print(sum_of_squares(10))

    sum100 = sum(100)
    square_sum_100 = sum100 * sum100
    print(square_sum_100)

    sum_square_100 = sum_of_squares(100)
    print(sum_square_100)
    print(square_sum_100 - sum_square_100)


