"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
solution(n) = 99.
"""
def solution(n):
    result = ''
    for i in range(n):
       result += '9'
    return int(result)
