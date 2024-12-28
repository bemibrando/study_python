# Read three values (variables A, B and C), which are the three student's grades. 
# Then, calculate the average, considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5. 
# Consider that each grade can go from 0 to 10.0, always with one decimal place.

# -*- coding: utf-8 -*-

a = float(input())
b = float(input())
c = float(input())

avg = (a * 2 + b * 3 + c * 5)/10

print("MEDIA = %.1f" %avg)