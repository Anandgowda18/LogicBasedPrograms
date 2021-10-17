'''Create a function/method to convert celsius to fahrenheit

Input Format

celsius

Constraints

no

Output Format

Fahrenheit

Sample Input 0

0
Sample Output 0

32
Sample Input 1

4
Sample Output 1

39
Sample Input 2

90
Sample Output 2

194'''

#solution
#formula for celsius to fahrenheit conversion F = C×(9/5)+32

def ctof(c):
    return int(c * (9/5) + 32)

print(ctof(int(input())))