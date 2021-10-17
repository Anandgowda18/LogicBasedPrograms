'''To check whether the given number is leap year or not.

Input Format

year from the user

Constraints

no constraint

Output Format

True or False

Sample Input 0

2020
Sample Output 0

True
Sample Input 1

2021
Sample Output 1

False'''
#solution
year = int(input())
if year % 4 == 0 and year%100 != 0 or year%400 == 0:
    print("True")
else:
    print("False")