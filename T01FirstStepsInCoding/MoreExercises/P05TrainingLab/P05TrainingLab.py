length = float(input()) * 100
width = float(input()) * 100
width = width - 100
chairs_by_length = length // 120
chairs_by_width = width // 70
total_chairs = int( chairs_by_length * chairs_by_width - 3 )
print(total_chairs)
