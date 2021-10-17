'''Program to find number of occurences of the given digit in the number n

Input Format

two numbers n and d

Constraints

no constraints

Output Format

number of occurrences

Sample Input 0

199
9
Sample Output 0

2
Sample Input 1

111
1
Sample Output 1

3'''

#solution

n = int(input())
d = int(input())
def find(n,d):
    return n.count(d)
    
print(find(str(n),str(d)))