import math

figure_type = input()
if figure_type == "square":
    side = float(input())
    area = side * side
elif figure_type == "rectangle":
    side_one = float(input())
    side_two = float(input())
    area = side_one * side_two
elif figure_type == "circle":
    radius = float(input())
    area = math.pi * radius * radius
else:
    hypotenuse = float(input())
    height = float(input())
    area = hypotenuse * height / 2
print(f"{area:.3f}")