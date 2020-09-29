'''
Task:

https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
'''

# Solution:

def snail(m):
    dim = len(m)
    track = []
    rev = m
    if m == [[]]:
        return []
    while True:
        m=rev
        for i in range(len(m[0])):
            track.append(m[0][i])
        rev = [[m[j][i] for j in range(1, len(m))] for i in range(len(m[0]) - 1, -1, -1)]
        if len(track) == dim*dim:
            return track