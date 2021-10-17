'''Implement a program to find sum of even number between x and y both are inclusive.

Input Format

two int values

Constraints

no

Output Format

sum of even numbers between x and y

Sample Input 0

10
15
Sample Output 0

36
Sample Input 1

0
10
Sample Output 1

30'''

#solution

def evensum(num1,num2):
    summ = 0
    for i in range(num1,num2+1,2):
            summ+=i
    return summ
num1 = int(input())
num2 = int(input())
if num1%2 == 0:
    print(evensum(num1,num2))
else:
    num1+=1
    print(evensum(num1,num2))