'''You are given Strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have you want to know how many of the stones you have are also jewels.

Letter are case sensitive. so "a" is considered as a different type of stone from "A".

Input Format

A string

Constraints

no

Output Format

how many of the stones

Sample Input 0

aA
aAAbbbb
Sample Output 0

3
Sample Input 1

z
ZZ
Sample Output 1

0
Sample Input 2

aAc
aDbcAC
Sample Output 2

3'''

#solution

n1 = input()
n2 = input()
total = 0
for i in n1:
    total+= n2.count(i)
print(total)