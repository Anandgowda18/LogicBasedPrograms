'''Implement a program to return First capital letter in a String

Input Format

A string from the user

Constraints

non-empty string

Output Format

First Capital letter

Sample Input 0

Test
Sample Output 0

T
Sample Input 1

Hello
Sample Output 1

H
Sample Input 2

wElCoMe
Sample Output 2

E'''

#solution

def firstprime(string):
    for i in string:
        if i.isupper():
            return i

print(firstprime(input()))