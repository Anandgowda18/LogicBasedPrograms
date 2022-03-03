'''Given s string, implement a program to find max occurring character in the given string.

Input Format

A string

Constraints

No

Output Format

max occuuring character

Sample Input 0

welcome
Sample Output 0

e
Sample Input 1

java
Sample Output 1

a
Sample Input 2

aabbbccccddddd
Sample Output 2

d'''

#solution

n = input()
dict1 = {i:n.count(i) for i in n}
tup = zip(dict1.values(),dict1.keys())
print(max(tup)[1])