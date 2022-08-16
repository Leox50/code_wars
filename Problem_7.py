"""

Every book has n pages with page numbers 1 to n. The summary is made by adding up the number of digits of all page numbers.

Task: Given the summary, find the number of pages n the book has.

Example

If the input is summary=25, then the output must be n=17: The numbers 1 to 17 have 25 digits in total: 1234567891011121314151617.

Be aware that you'll get enormous books having up to 100.000 pages.

All inputs will be valid.

"""

def amount_of_pages(summary):
    # we are going to add values to this variable in a loop to verify it in advance
    string = ''
    j = 1
    # here I need to set a verification of the length being less than the summary number
    while len(string) <= summary:
        string += str(j)
        if len(string) == summary:
            return j
        else:
            pass
        j += 1

amount_of_pages(5)