'''A company wishes to devise an order confirmation procedure. They plan to require an extra confirmation instead of simply auto-confirming the order at the time it is placed. for this purpose, the system will generate one time password to be shared with the customer. The customer who is placing the order has to enter the OTP to confirm the order. The OTP generated for the requested order ID, as the product of the digits in orderID. ** **Write an algorithm to find the OTP for the OrderID.

Input Format

an intger representing order id

Constraints

no

Output Format

an integer representing OTP

Sample Input 0

2342
Sample Output 0

48
Sample Input 1

123
Sample Output 1

6
Sample Input 2

456
Sample Output 2

120'''

#solution

product = 1
for i in input():
    product = product * int(i)
print(product)