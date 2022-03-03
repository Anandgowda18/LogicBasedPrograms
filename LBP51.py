'''Given a valid IP address, return a defanged version of that IP address. A defanged IP address replaces every period '.' with "[.]".

Input Format

A string

Constraints

non-empty String

Output Format

replacement String

Sample Input 0

1.1.1.1
Sample Output 0

1[.]1[.]1[.]1
Sample Input 1

255.100.50.0
Sample Output 1

255[.]100[.]50[.]0
Sample Input 2

1.2.3.4
Sample Output 2

1[.]2[.]3[.]4'''

#solution

print(input().replace('.','[.]'))