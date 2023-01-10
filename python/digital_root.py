# Challenge link: https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue 
# reducing in this way until a single-digit number is produced. The input will be a 
# non-negative integer.

# Trivial solution -----------------------------------------
def sum_str(s):
    sum = 0
    for i in s:
        sum += int(i)
    return sum

def digital_root(n):
    str_n = str(n)
    if len(str_n) > 1:
        return digital_root(sum_str(str_n))
    else:
        return n
#-------------------------------------------------------------