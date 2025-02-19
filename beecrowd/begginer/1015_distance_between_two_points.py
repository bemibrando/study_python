""" 
Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four decimal places, according to the formula:

distance = sqrt( pow((x2 - x1), 2) + pow((y2 - y1), 2) )
 """
import math

def distanceBetween(x1, y1, x2, y2):
    distance = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    return distance
    
value = input().split(" ")
value1 = input().split(" ")

x1 = float(value[0])
y1 = float(value[1])

x2 = float(value1[0])
y2 = float(value1[1])

distance = distanceBetween(x1, y1, x2, y2)

print("%0.4f" %distance)