"""
Task:

https://www.codewars.com/kata/58c5577d61aefcf3ff000081

Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C
    A       I       V       D       E       N

The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN

Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that include punctuation. Don't filter out punctuation as they are a part of the string.
"""

# Solution:

def encode_rail_fence_cipher(string, n):
    s = 2 + (n - 2) * 2
    res = string[::s]
    for i in range(1, n-1):
        h1 = string[i::s]
        h2 = string[i + (n - i - 1) * 2::s]
        for ii in range(len(h2)):
            res += h1[ii] + h2[ii]
        if len(h1) > len(h2):
            res += h1[-1]
    return res + string[n-1::s]


def decode_rail_fence_cipher(string, n):
    if not string:
        return ''
    s = 2 + (n - 2) * 2
    rails = {}
    count = (len(string)-1) // (n-1)
    bonus = (len(string)-1) % s
    cycle = list(range(n)) + list(range(n - 2, 0, -1))
    cycle = cycle * (int(count/2)) + cycle[:bonus+1]
    if count % 2:
        bonus -= (n-1)
    rails[0] = int(count/2) + 1
    for i in range(1, n-1):
        rails[i] = count
    rails[n - 1] = int(count / 2)
    if count % 2:
        rails[n-1] += 1
        for i in range(n-2, 0, -1):
            if bonus:
                rails[i] += 1
                bonus -= 1
    else:
        for i in range(1, n-1):
            if bonus:
                rails[i] += 1
                bonus -= 1
    start = 0
    for i in range(n):
        new_start = start + rails[i]
        rails[i] = string[start:start + rails[i]]
        start = new_start
    rails = {k:iter(v) for k, v in rails.items()}
    res = ''
    for k in cycle:
        res += next(rails[k])
    return res