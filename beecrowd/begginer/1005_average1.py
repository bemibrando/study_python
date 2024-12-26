# Read two floating points' values of double precision A and B, corresponding to two student's grades. 
# After this, calculate the student's average, considering that grade A has weight 3.5 and B has weight 7.5. 
# Each grade can be from zero to ten, always with one digit after the decimal point. 
# Don’t forget to print the end of line after the result, otherwise you will receive “Presentation Error”. 
# Don’t forget the space before and after the equal sign.

# -*- coding: utf-8 -*-

a = float(input())
b = float(input())

avg = (a * 3.5 + b * 7.5)/11

print("MEDIA = %.5f" %avg)