'''Implement a program to calculate sum of prime digits present in the given number

Input Format

a number from the user

Constraints

n>0

Output Format

print sum of prime digits

Sample Input 0

123
Sample Output 0

5
Sample Input 1

101
Sample Output 1

0
Sample Input 2

142
Sample Output 2

2'''

#solution
n = input()
sum = 0
if int(n) > 0:
    for i in n:
        if int(i)>1:
            for j in range(2,int(i)):
                if int(i) % j == 0:
                    break
            else:
                sum = sum + int(i)
    print(sum)
else:
    print("Invaild")