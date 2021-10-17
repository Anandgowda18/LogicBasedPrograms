'''An e-commerce website wishes to find the lucky customer who will be eligible for full value cash back. For this purpose,a number N is fed to the system. It will return another number that is calculated by an algorithm. In the algorithm, a sequence is generated, in which each number n the sum of the preceding numbers. initially the sequence will have two 1's in it.
The System will return the Nth number from the generated sequence which is treated as the order ID. The lucky customer will be one who has placed that order.
Write an alorithm to help the website find the lucky customer.

Input Format

an integer value from the user

Constraints

no constraints

Output Format

print order ID as an integer

Sample Input 0

8
Sample Output 0

21
Sample Input 1

5
Sample Output 1

5'''

#solution

def lucky(num):
    n1 = 1
    n2 = 1
    summ = 0
    for i in range(2,num):
        summ = n1+n2
        n1 = n2
        n2 = summ
    return summ
print(lucky(int(input())))