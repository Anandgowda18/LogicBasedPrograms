'''There is a great war between the even and odd numbers. Many numbers already lost thier life in this war and its your task to end this. You have to determine which group sums larger. the even, or the odd, the larger group wins. Create a function that takes an array of integers , sums the even and odd numbers seperately, then return the difference between sum of even and odd numbers. **Note: if result is -ve convert it into +ve. **

Input Format

number and array elements

Constraints

no

Output Format

difference between sum of even and odd numbers

Sample Input 0

4
2 8 7 5
Sample Output 0

2
Sample Input 1

3
12 90 75
Sample Output 1

27
Sample Input 2

12
5 9 45 6 2 7 34 8 6 90 5 243
Sample Output 2

168
Sample Input 3

5
75 89 12 147 88
Sample Output 3

211'''

#solution

n1 = int(input())
n2 = input().split(' ')
list_even = []
list_odd = []
for i in n2:
    if int(i)%2 == 0:
        list_even.append(int(i))
    else:
        list_odd.append(int(i))
x = (sum(list_even))-(sum(list_odd))
print(abs(x))