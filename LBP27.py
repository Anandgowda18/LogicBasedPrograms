'''Given three integers i,j & k, a sequence sum to be the value of i+(i+1)+(i+2)..+j+(j-1)+(j-2)+..+k (increment from i until it equals to j, then decrement from j until equals k). Given values i,j,k. caluclate the sequence sum as described.
int getSequenceSum(int,int,int);

Input Format

Three int values

Constraints

no

Output Format

sum based on given constraints

Sample Input 0

5
9
6
Sample Output 0

56
Sample Input 1

0
5
-1
Sample Output 1

24
Sample Input 2

6
10
5
Sample Output 2

75'''

#solution

def summation(i,j,k):
    summ = 0
    for x in range(i,j+1):
        summ+=x
    for y in range(k,j):
        summ+=y
    return summ
i = int(input())
j = int(input())
k = int(input())
print(summation(i,j,k))