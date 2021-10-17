'''Implement a program to calculate sum of digits that are divisible by 3 in the given number

Input Format

a number from the user

Constraints

n>0

Output Format

print sum of digits that are divisible by 3

Sample Input 0

123
Sample Output 0

3
Sample Input 1

163
Sample Output 1

9'''

#solution

n = input()
sum = 0
for i in n:
    if int(i)%3 == 0:
        sum = sum + int(i)
print(sum)