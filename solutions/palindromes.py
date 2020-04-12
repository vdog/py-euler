
def is_palindrome(num):
    digits = int_to_digit_list(num)
    retval = True
    front = 0
    back = len(digits) - 1
    while front < back:
        if digits[front] != digits[back]:
            retval = False
        front += 1
        back -= 1
    return retval

def int_to_digit_list(num):
    retval = []
    working = num
    while working > 0:
        digit = working % 10
        retval.insert(0, digit)
        working = working - digit
        working = int(working / 10)
    return retval
