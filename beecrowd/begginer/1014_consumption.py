""" 
Calculate a car's average consumption being provided the total distance traveled (in Km) and the spent fuel total (in liters).
 """

def averageConsumption(totalDistance, totalFuel):
    avgConsumption = totalDistance/totalFuel
    return avgConsumption

x = int(input())
y = float(input())
    
kml = averageConsumption(x,y)
    
print("%0.3f km/l" %kml)