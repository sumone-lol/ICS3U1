'''
4. Write programs to accomplish each task.
- Read three integers and determine if any of the three is a multiple of the
other two.
- Read three integers and determine if exactly two are greater than 10.
'''

int1 = int(input("Enter an integer\n"))
int2 = int(input("Enter another integer\n"))
int3 = int(input("Enter another integer\n"))

if int1 % int2 == 0 \
    or int1 % int3 == 0 \
    or int2 % int1 == 0 \
    or int2 % int3 == 0 \
    or int3 % int1 == 0 \
    or int3 % int2 == 0:
        print("One of the integers is a multiple of the other two.")
if (int1 > 10 and int2 > 10) \
    or (int1 > 10 and int3 > 10) \
    or (int2 > 10 and int3 > 10):
        print("Two of the integers are greater than 10.")