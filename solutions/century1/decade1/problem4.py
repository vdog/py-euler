import solutions.palindromes


def run():
    print("problem 4")

    a = 999
    b = 999

    potential_palindrome = a*b

    max_palindrome = 0
    while (a > 99):
        b -= 1
        if b < 99:
            b = a - 1
            a -= 1
        potential_palindrome = a * b
        if solutions.palindromes.is_palindrome(potential_palindrome):
            if potential_palindrome > max_palindrome:
                max_palindrome = potential_palindrome
                print("{} {} {}".format(potential_palindrome, a, b))

    print(max_palindrome)
