"""
Task:

https://www.codewars.com/kata/54eb33e5bc1a25440d000891

My little sister came back home from school with the following task: given a squared sheet of paper she has to cut it in pieces which, when assembled, give squares the sides of which form an increasing sequence of numbers. At the beginning it was lot of fun but little by little we were tired of seeing the pile of torn paper. So we decided to write a program that could help us and protects trees.
Task

Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².

If there are multiple solutions (and there will be), return as far as possible the result with the largest possible values:
Examples

decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.
Note

Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists, return nil, null, Nothing, None (depending on the language) or "[]" (C) ,{} (C++), [] (Swift, Go).

The function "decompose" will take a positive integer n and return the decomposition of N = n² as:

*    [x1 ... xk] or
*    "x1 ... xk" or
*    Just [x1 ... xk] or
*    Some [x1 ... xk] or
*    {x1 ... xk} or
*    "[x1,x2, ... ,xk]"

depending on the language (see "Sample tests")

"""


# Solution:


def checkBranch(n):
    if ( n* *0.5) % 1 == 0:
        return [int( n* *0.5)]
    elif n in [2, 3, 6, 7, 8]:
        return None
    b = int( n* *0.5)
    tc = 0
    for i in range(b - tc, 0, -1):
        if checkBranch(n - i** 2):
            if i not in checkBranch(n - i ** 2):
                return [i] + checkBranch(n - i ** 2)
            else:
                tc += 1
        else:
            tc += 1

def decompose(n):


    for i in range(n - 1, 0, -1):
        print(str(i))
        #Checking if we still stand a chance
        if i*(i+1)*(2*i+1)/6 < n**2:
            return None
        elif checkBranch(n**2 - i**2):
            return checkBranch(n**2 - i**2)[::-1] + [i]

    5 months ago