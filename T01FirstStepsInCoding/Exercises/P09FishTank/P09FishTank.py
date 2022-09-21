length_in_cm = int(input())
weight_in_cm = int(input())
height_in_cm = int(input())
fill_percentage = float(input())

volume_in_cubic_cm = length_in_cm * weight_in_cm * height_in_cm
volume_in_liters = volume_in_cubic_cm / 1000
volume_to_fill_with_watter = volume_in_liters * (100 - fill_percentage) / 100
print(volume_to_fill_with_watter)