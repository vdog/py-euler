# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
sum = 0
for i in range(1000):
    if ( i % 5 == 0):
        sum += i
    elif (i % 3 == 0):
        sum += i

print(sum)
