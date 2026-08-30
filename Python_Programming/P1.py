# write a program to calculate area of triangle or rectangle
import math
def calculate_area(dimension1, dimension2, shape = "triangle"):
    if shape=="triangle":
        area = 1/2*(dimension1*dimension2)
    elif(shape=="rectangle"):
        area = dimension1*dimension2
    else:
        print('invalid shape for which area should be calculate')
    return area

base = 10 
height = 20
triangle_area = calculate_area(base, height, "triangle") 
print("area of triangle : ", triangle_area)  

base = 45
height = 25
rectangle_area = calculate_area(base, height, "rectangle")
print("area of triangle is :", rectangle_area)


def print_pattern(n=5):
    for i in range(n+1):
        print('*' * i)
    for i in range(n+1, 0, -1):
        print('*' * i)
        # s = " "
        # for j in range(i+1):
        # #     s = s + "*"
        # print(s)
    
print_pattern(4)

# for i in range(5):
#     print("*")
#     for j in range(i):
#         print(j*'*')
