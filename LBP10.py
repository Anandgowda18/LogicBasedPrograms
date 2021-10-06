'''Implement a program to calculate sum of odd digits present in the given number

Input Format

a number from the user

Constraints

n>0

Output Format

print sum of odd digits

Sample Input 0

123
Sample Output 0

4
Sample Input 1

101
Sample Output 1

2'''
#solution
n = input()
sum = 0
for i in n:
    if int(i)%2 == 1:
        sum = sum + int(i)
print(sum)