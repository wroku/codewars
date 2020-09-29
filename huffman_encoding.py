'''
Task:

https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d

Motivation

Natural language texts often have a very high frequency of certain letters, in German for example, almost every 5th letter is an E, but only every 500th is a Q. It would then be clever to choose a very small representation for E. This is exactly what the Huffman compression is about, choosing the length of the representation based on the frequencies of the symbol in the text.

Algorithm

Let's assume we want to encode the word "aaaabcc", then we calculate the frequencies of the letters in the text:
Symbol 	Frequency
a 	    4
b 	    1
c 	    2

Now we choose a smaller representation the more often it occurs, to minimize the overall space needed. The algorithm uses a tree for encoding and decoding:

  .
 / \
a   .
   / \
   b  c

Usually we choose 0 for the left branch and 1 for the right branch (but it might also be swapped). By traversing from the root to the symbol leaf, we want to encode, we get the matching representation. To decode a sequence of binary digits into a symbol, we start from the root and just follow the path in the same way, until we reach a symbol.

Considering the above tree, we would encode a with 0, b with 10 and c with 11. Therefore encoding "aaaabcc" will result in 0000101111.

(Note: As you can see the encoding is not optimal, since the code for b and c have same length, but that is topic of another data compression Kata.)
Tree construction

To build the tree, we turn each symbol into a leaf and sort them by their frequency. In every step, we remove 2 trees with the smallest frequency and put them under a node. This node gets reinserted and has the sum of the frequencies of both trees as new frequency. We are finished, when there is only 1 tree left.

(Hint: Maybe you can do it without sorting in every step?)

Goal

Write functions frequencies, encode and decode.

Note: Frequency lists with just one or less elements should get rejected. (Because then there is no information we could encode, but the length.)

'''


# Solution:

from collections import Counter


def frequencies(s):
    return [(k, v) for k, v in Counter(s).items()]


def grow_tree(freqs):
    tree = sorted(freqs, key=lambda x: x[1], reverse=True)
    while len(tree) > 2:
        tree = tree[:-2:] + [([tree[-2][0], tree[-1][0]], tree[-2][1] + tree[-1][1])]
        tree.sort(key=lambda x: x[1], reverse=True)
    print(tree)
    return [tree[0][0]] + [tree[1][0]]


def encode(freqs, s):
    res = ''
    if len(freqs) <= 1:
        return None

    def traverse(tree, c):
        r = ''
        if type(tree) == str:
            return None
        elif tree[0] == c:
            r += '0'
            return r
        elif tree[1] == c:
            r += '1'
            return r
        elif type(tree[0]) is str and type(tree[1]) is str:
            return None
        elif traverse(tree[0], c):
            r += '0' + traverse(tree[0], c)
            return r
        elif traverse(tree[1], c):
            r += '1' + traverse(tree[1], c)
            return r

    for char in s:
        res += traverse(grow_tree(freqs), char)

    return res


def decode(freqs, bits):
    if len(freqs) <= 1:
        return None
    res = ''
    old_tree = grow_tree(freqs)
    tree = old_tree

    for b in bits:
        if type(tree[int(b)]) == str:
            res += tree[int(b)]
            tree = old_tree
        else:
            tree = tree[int(b)]

    return res