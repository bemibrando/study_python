# In this problem, the task is to read a code of a product 1, the number of units of product 1, 
# the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. 
# After this, calculate and show the amount to be paid.

# -*- coding: utf-8 -*-

total = 0

for i in range (0, 2):
    line = input().split(" ")
    
    code, quantity, value = line

    total += float(quantity) * float(value)


print("VALOR A PAGAR: R$ %.2f" %total)