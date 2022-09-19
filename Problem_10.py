'''

Dot Calculator

You have to write a calculator that receives strings for input. The dots will represent the number in the equation. There will be dots on one side, an operator, and dots again after the operator. The dots and the operator will be separated by one space.

Here are the following valid operators :

+ Addition
- Subtraction
* Multiplication
// Integer Division
Your Work (Task)

You'll have to return a string that contains dots, as many the equation returns. If the result is 0, return the empty string. When it comes to subtraction, the first number will always be greater than or equal to the second number.

Examples (Input => Output)

* "..... + ..............." => "...................."
* "..... - ..."             => ".."
* "..... - ."               => "...."
* "..... * ..."             => "..............."
* "..... * .."              => ".........."
* "..... // .."             => ".."
* "..... // ."              => "....."
* ". // .."                 => ""
* ".. - .."                 => ""

'''

def calculator(txt):
    #if we have an addition sign, then we can return only the sum of the dots
    if '+' in txt:
        return print(''.join(['.' for _ in range(txt.count('.'))]))
    #if we have a subtraction sign, then we need to split the string line
    #.split() method returns a list, so we are referring to it by indexes
    #the same thing to all operators below
    elif '-' in txt:
        return print(''.join(['.' for _ in range(txt.split('-')[0].count('.') - txt.split('-')[1].count('.'))]))
    elif '*' in txt:
        return print(''.join(['.' for _ in range(txt.split('*')[0].count('.') * txt.split('*')[1].count('.'))]))
    else:
        return print(''.join(['.' for _ in range(txt.split('//')[0].count('.') // txt.split('//')[1].count('.'))]))

calculator('..... + ...............')