""" 
Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:

Maior AB = (a + b + abs(a - b)) / 2
 """

from sys import stdin

def MaiorAB(A, B):
    greatest = (A + B + abs(A - B)) / 2
    return greatest

for line in stdin:
    if line == '':
        break
    
    line = line.split(" ")
    
    A, B, C = line
    
    greatest = MaiorAB(int(A), int(B))
    greatest = MaiorAB(greatest, int(C))
    
    print("%d eh o maior" %greatest)