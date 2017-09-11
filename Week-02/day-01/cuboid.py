# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000
a = 200
b = 300
c = 150

surface = ((a+b+c) * 2)
volume = a * b * c
print("Surface Area:" +str(surface))
print("Volume:" +str(volume))