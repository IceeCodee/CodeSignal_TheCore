"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
solution(n) = 11.
"""
def solution(n):
   return int(n/10) + (n%10)
