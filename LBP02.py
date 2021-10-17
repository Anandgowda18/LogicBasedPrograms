'''Given an integer n, perform the following conditional actions,

if n is odd, print Weird,
if n is even and in the inclusive range of 2 to 5, print Not Weird.
if n is even and in the inclusive range of 6 to 20, print Weird.
if n is even and greater than 20, print Not Weird.

Input Format

a number from the user

Constraints

1<=n<=100

Output Format

Weird or Not Weird

Sample Input 0

3
Sample Output 0

Weird
Sample Input 1

24
Sample Output 1

Not Weird'''
#solution
n = int(input())
if n > 0:
    if n%2 == 1:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")