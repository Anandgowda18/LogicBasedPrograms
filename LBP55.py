'''Create a function/method that takes two Strings and returns true of the first string ends with second string, otherwise return false

Input Format

two strings

Constraints

No

Output Format

true or false

Sample Input 0

abc
bc
Sample Output 0

true
Sample Input 1

abc
d
Sample Output 1

false'''

#solution

input1 = input()
input2 = input()
if input1.endswith(input2):
    print('true')
else:
    print('false')