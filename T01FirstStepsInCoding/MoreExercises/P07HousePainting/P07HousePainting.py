height_of_walls = float(input())
width_of_walls = float(input())
height_of_roof = float(input())

area_of_front_walls = 2 * height_of_walls * height_of_walls - 1.2 * 2
area_of_side_walls = 2* height_of_walls * width_of_walls - 2 * 1.5 * 1.5
area_of_roof = 2 * height_of_walls * height_of_roof / 2 + 2 * height_of_walls * width_of_walls
area_of_walls = area_of_front_walls + area_of_side_walls

liters_of_green_paint = area_of_walls / 3.4
liters_of_red_paint = area_of_roof / 4.3

print(f"{liters_of_green_paint:.2f}")
print(f"{liters_of_red_paint:.2f}")