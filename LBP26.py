'''Program to convert fahrenheit to celsius.

Input Format

fahrenheit

Constraints

no

Output Format

celsius

Sample Input 0

32
Sample Output 0

0
Sample Input 1

12
Sample Output 1

-11'''

#solution
#formula for fahrenheit to celsius conversion C = (F - 32) × 5/9

def ftoc(f):
    return int((f-32)*(5/9))

print(ftoc(int(input())))