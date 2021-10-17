'''For each of the 6 coffee cups I buy, I get a 7th cup free. In total, I get 7 cups. Implement a program that takes n cups bought and print as an integer the total number of cups I would get.

Input Format

n number of cups from user

Constraints

n>0

Output Format

number of cups present have

Sample Input 0

13
Sample Output 0

15
Sample Input 1

6
Sample Output 1

7'''
#solution
n = int(input())
total_cups = 0
if n > 0:
    total_cups = n + (n//6)
    print(total_cups)