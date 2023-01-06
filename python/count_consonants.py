# Challenge link: https://www.codewars.com/kata/564e7fc20f0b53eb02000106
# Description:
#   Write a function consonantCount, consonant_count or ConsonantCount that takes a string of English-language 
#   text and returns the number of consonants in the string.
#   Consonants are all letters used to write English excluding the vowels a, e, i, o, u.

def consonant_count(s):
    consonants = ['a','e','i','o','u']
    count = 0
    for w in s:
        if w.lower() not in consonants and w.isalpha():
            count += 1
    return count
