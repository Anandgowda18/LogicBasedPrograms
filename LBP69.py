'''Create a function/method that takes a string as a argument and returns a new string by removing all vowels from it

Input Format

a string from the user

Constraints

No

Output Format

A string

Sample Input 0

welcome
Sample Output 0

wlcm
Sample Input 1

demo
Sample Output 1

dm'''

#solution

def remove_vowels(string):
    return ''.join(i for i in string if i.lower() not in 'aeiou')

print(remove_vowels(input()))