count_pens = int(input())
count_markers = int(input())
liters_board_detergent = int(input())
discount_percentage = int(input())

total = count_pens * 5.8 + count_markers * 7.2 + liters_board_detergent * 1.2
total = total - total * discount_percentage / 100

print(total)
