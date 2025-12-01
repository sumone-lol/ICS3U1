'''
3. Calculate the volume of a rectangular prism, given its height, width and 
depth as parameters. Name the function v_rect_prism(length, width, height) and 
return volume. In the main program, test your function with these values: l=4, 
w=5 and h=10. The surface area should be 200.
'''

def v_rect_prism(length, width, height):
    volume = length * width * height
    return volume

print(v_rect_prism(4,5,10))