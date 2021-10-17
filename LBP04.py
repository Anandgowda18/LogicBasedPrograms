'''The e-commerce company Bookshelf wishes to analyse its monthly sales data between minimum range 30 to max range 100. The company has categorized these book sales into four groups depending on the number of sales with the help of these groups the company will know which stock they should increase or decrease in their inventory for the next month. the groups are as follows
sales range groups
30-50 ------------------> D
51-60 ------------------> C
61-80 ------------------> B
81-100 -----------------> A

write an alg to find the group for the given book sale count.

Input Format

an integer salesCount represent total sales of a book

Constraints

30<=saleCount<=100

Output Format

a character representing the group of given sale count or invalid

Sample Input 0

57
Sample Output 0

C
Sample Input 1

99
Sample Output 1

A'''
#solution
salecount = int(input())
if salecount>=30 and salecount <=100:
    if salecount >=30 and salecount <= 50:
        print("D")
    elif salecount >=51 and salecount <= 60:
        print("C")
    elif salecount >=61 and salecount <= 80:
        print("B")
    else:
        print("A")
else:
    print("invalid")