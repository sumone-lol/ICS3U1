'''
2. Calculate the surface area of a cylinder, given its height and radius as a 
parameter. Name the function sa_cylinder(height, radius) and return 
surface_area. In the main program, test your function with these values: h=4, 
r=10 and h=1, r=1. The surface area should be 879.6 and 12.56 respectively.
'''

def sa_cylinder(height, radius):
    surface_area = (3.14 * radius ** 2) * 2 + (2 * 3.14 * radius * height)
    return surface_area

print(sa_cylinder(4,10), sa_cylinder(1,1))