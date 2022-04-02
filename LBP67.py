'''Create a function/method that takes, a word and returns true if the word has two consecutive identical letters.

Input Format

A string from the user

Constraints

No

Output Format

true or false

Sample Input 0

loop
Sample Output 0

true
Sample Input 1

yummy
Sample Output 1

true
Sample Input 2

orange
Sample Output 2

false'''

#solution

def identical(string):
    for i in range(1,len(string)):
        if (string[i-1] == string[i]) and ((i-(i-1)) == 1):
            return 'true'
    return 'false'
print(identical(input()))