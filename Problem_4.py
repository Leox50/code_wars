"""

Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.

"""

def high(x):
    set_of_let = dict()
    max_value = max([sum([ord(i) - 96 for i in j]) for j in x.split(' ')])
    for j in x.split(' '):
        set_of_let[j] = sum([ord(i) - 96 for i in j])

    for key in set_of_let:
        if set_of_let[key] == max_value:
            return print(key)

high('man i need a taxi up to ubud')