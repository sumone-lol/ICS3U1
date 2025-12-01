'''
1. Calculate the area of a circle, given its radius as a parameter. Name the 
function area_circle(r) and return area. In the main program, test your 
function with these values: r=1 and r=5. The area should be 3.14 and 78.54 
respectively
'''

def area_circle(r):
    area = 3.14 * r ** 2
    return area

area1 = area_circle(1)
area2 = area_circle(5)
print(area1, area2)