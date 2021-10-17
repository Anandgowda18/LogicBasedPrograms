'''Create a function that sums the total number of digits between two numbers inclusive. for example, if the numbers are 19 and 22, then (1+9)+(2+0)+(2+1)+(2+2)=19.

Input Format

two numbers from the user

Constraints

no

Output Format

sum of digits between n1 and n2

Sample Input 0

19
22
Sample Output 0

19
Sample Input 1

7
8
Sample Output 1

15
Sample Input 2

17
20
Sample Output 2

29'''

#solution

n1 = int(input())
n2 = int(input())
string = ''.join(str(i) for i in range(n1,n2+1))
sum = 0
for i in string:
    sum+=int(i)
print(sum)