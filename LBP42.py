'''Jackson, a math student, is developing an application on prime numbers. for the given two integers on the display of the application, the user has to identify all the prime numbers within the given range (including the given values). afterwards the application will sum all those prime numbers. Jackson has to write an algorithm to find the sum of all the prime numbers of the given range. Write an algorithm to find the sum of all the prime numbers of the given range.

Input Format

two space sepearted integers RL and RR.

Constraints

no

Output Format

sum of the prime numbers between RL and RR.

Sample Input 0

2
10
Sample Output 0

17
Sample Input 1

45
89
Sample Output 1

682
Sample Input 2

3
12
Sample Output 2

26'''

#solution

n1 = int(input())
n2 = int(input())
count = 0
for n in range(n1,n2+1):
    for j in range(2,n):
        if n%j == 0:
            break
    else:
        count+=n
print(count)