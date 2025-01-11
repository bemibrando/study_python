""" 
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.
 """

from sys import stdin

for line in stdin:
    if line == '':
        break;
    
    line = line.split(" ")
    
    A = float(line[0])
    B = float(line[1])
    C = float(line[2])
    
    pi = 3.14159
    
    triangle = (A * C) / 2
    circle = pi * C * C
    trapezium = (A + B) / 2 * C
    square = B * B
    rectangle = A * B
    
    print("TRIANGULO: {:.3f}".format(triangle))
    print("CIRCULO: {:.3f}".format(circle))
    print("TRAPEZIO: {:.3f}".format(trapezium))
    print("QUADRADO: {:.3f}".format(square))
    print("RETANGULO: {:.3f}".format(rectangle))