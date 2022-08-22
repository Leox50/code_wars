'''

Write a function that will check whether ANY permutation of
the characters of the input string is a palindrome.
Bonus points for a solution that is efficient and/or
that uses only built-in language functions. Deem yourself brilliant
if you can come up with a version that does not use any function whatsoever.

Example

madam -> True
adamm -> True
junk -> False

Hint

The brute force approach would be to generate all the permutations
of the string and check each one of them whether it is a palindrome.
However, an optimized approach will not require this at all.

'''

def permute_a_palindrome(input):

    #firstly, we need to create a dictionary
    #will an element as a key and the number of
    #elements in the givern array as the value to the key

    dic = dict()
    for i in input:
        dic[i] = input.count(i)

    #any palindrome has 0 or 1 odd numbers and many even numbers
    #so we need to create an array of o=hoq many there are odd numbers
    #and check if our rule is applicable to the case

    return len([i for i in dic.values() if i % 2 != 0]) <= 1