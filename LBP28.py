'''You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Input Format

a number from the user

Constraints

no

Output Format

number of ways

Sample Input 0

1
Sample Output 0

1
Sample Input 1

2
Sample Output 1

2'''

#solution
#this problem is a Fibonacci
def fibo(num):
    n1=1
    n2=1
    summ=0
    for i in range(2,num+1):
        summ = n1+n2
        n1,n2 = n2,summ
    return summ
print(fibo(int(input())))