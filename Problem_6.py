'''

Take 2 strings s1 and s2 including only letters from a to z.
Return a new sorted string, the longest possible,
containing distinct letters -
each taken only once - coming from s1 or s2.

Example:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

'''

def longest(a1, a2):
    # I am using the set function as it returns only unique numbers
    # however, set func also has an unpredictable behavior, so we need to
    # get back to list and sort it.
    return print(''.join([str(i) for i in sorted(list(set(a1+a2)))]))

longest("aretheyhere", "yestheyarehere")