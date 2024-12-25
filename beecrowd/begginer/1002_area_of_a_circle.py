# The formula to calculate the area of a circumference is defined as A = π . R2. 
# Considering to this problem that π = 3.14159:
# Calculate the area using the formula given in the problem description.

# -*- coding: utf-8 -*-

n = 3.14159

radio = float(input())

area = n * pow(radio, 2)

print("A=%0.4f" %area)