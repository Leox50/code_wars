# Replace With Alphabet Position

def alphabet_position(text):
    alph = dict()
    lst_let = 'abcdefghijklmnopqrstuvwxyz'

    i = 1

    for letter in lst_let:
        alph[letter] = i
        i += 1

    string = ''

    for j in text:
        if j.lower() in lst_let:
            string = string + ' ' + str(alph[j.lower()])

    return string.lstrip(' ')