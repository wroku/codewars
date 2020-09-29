'''
Task:

Consider the following array:

[1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 12345678910, 1234567891011...]

If we join these blocks of numbers, we come up with an infinite sequence which starts with 112123123412345123456.... The list is infinite.

You will be given an number (n) and your task will be to return the element at that index in the sequence, where 1 ≤ n ≤ 10^18. Assume the indexes start with 1, not 0. For example:

solve(1) = 1, because the first character in the sequence is 1. There is no index 0.
solve(2) = 1, because the second character is also 1.
solve(3) = 2, because the third character is 2.

More examples in the test cases. Good luck!

'''

# Solution:

from decimal import Decimal as D


def sum(a1, n, r):
    return ( (D('2') * a1 + ( D(str(n)) - D('1') ) * D(str(r)) ) / D('2')) * D(str(n))


def first(r):
    s = 0
    for i in range(1, r):
        s += 9 * 10**(i-1) * i
    return D(str(s + r))


def solve(n):
    print(n)
    r, s, Sn = 1, 0, D(str(n))
    while Sn > s + sum(first(r), 9 * (10 ** (r - 1)), r):
        Sn -= sum(first(r), 9 * (10 ** (r - 1)), r)
        r += 1

    a = first(r)
    nn4 = ((4 * a ** 2 - 4 * a * r + r ** 2 + 8 * r * Sn)**D('0.5') - 2 * a + r) / (2 * r)

    if nn4 % 1 == 0:
        pos = Sn - sum(first(r), int(nn4 - 1), r)
    else:
        pos = Sn - sum(first(r), int(nn4), r)

    i = 1
    while pos - 9 * 10**(i-1) * i > 0:
        pos -= 9 * 10**(i-1) * i
        i += 1

    pos = int(pos)
    if pos >= i:
        number = pos//i
        if i > 1:
            number += 10**(i-1)
    else:
        number = 10**(i-1)
    if pos % i == 0 and i > 1:
        digit = str(number-1)[-1]
    else:
        digit = str(number)[pos % i - 1]
    return int(digit)