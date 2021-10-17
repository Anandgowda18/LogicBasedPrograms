'''Implement the following function int BlackJack(int n1,int n2);
the function accepts two +ve integers n1 and n2 as its arguments. Implement the function on given two vlaues to return an int value as follows
return whichever value is nearest to 21 without going over. Return if they go both go over.

Input Format

two int values n1 and n2

Constraints

no

Output Format

0 or n1 or n2

Sample Input 0

19
21
Sample Output 0

21
Sample Input 1

21
19
Sample Output 1

21
Sample Input 2

19
22
Sample Output 2

19'''

#solution

def blackjack(n1,n2):
    if n1<=21 and n2<=21:
        if n1 > n2:
            return n1
        return n2
    else:
        if n1<=21:
            return n1
        elif n2<=21:
            return n2
        else:
            return 0

n1 = int(input())
n2 = int(input())
print(blackjack(n1,n2))