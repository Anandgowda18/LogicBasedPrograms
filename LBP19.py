'''A network protocol specifies how data is exchanged via transmission media. The protocol converts each message into a stream of 1's and 0's.
Given a decimal number, write an algorithm to convert the number into a binary form.

Input Format

a decimal number from the user

Constraints

n>=0

Output Format

its equalent binary form

Sample Input 0

4
Sample Output 0

100
Sample Input 1

8
Sample Output 1

1000'''

#solution

n = int(input())
print(bin(n)[2:])