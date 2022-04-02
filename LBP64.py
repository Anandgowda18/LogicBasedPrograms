'''Create a function that takes a string, check if it has the same number of x's and o's and returns either true or false.
1. return boolean value true or false.
2. returns true if the amount x's and o's are the same.
3. returns false if they are not the same amount.
4. the string can contains any character.
5. when 'x' and 'o' are not in the string, return true.

Input Format

a string

Constraints

No

Output Format

true or false

Sample Input 0

ooxx
Sample Output 0

true
Sample Input 1

xooxx
Sample Output 1

false'''

#Solution

def xo(string):
    if string.lower().count('x') == 0 and string.lower().count('o') == 0:
        return 'true'
    elif string.lower().count('x') == string.lower().count('o'):
        return 'true'
    else:
        return 'false'

string = input()
print(xo(string))