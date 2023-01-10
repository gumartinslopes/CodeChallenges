# Challenge link: https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
# Instructions:
# Given two integers a and b, which can be positive or negative, find the sum of all
# the integers between and including them and return it. If the two numbers are equal return a or b.
# Note: a and b are not ordered!

# Trivial solution -----------------------------------------
def get_sum(a,b):
    sum = 0
    if a < b:
        for i in range(a, b + 1):
            sum += i
    else:
        for i in range(b,a + 1):
            sum += i
    return sum
#-------------------------------------------------------------

# Hardcore solution-------------------------------------------
def get_sum_2(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
#-------------------------------------------------------------