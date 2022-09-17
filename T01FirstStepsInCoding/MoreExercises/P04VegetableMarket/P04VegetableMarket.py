price_of_vegetables = float(input())
price_of_fruits = float(input())
quantity_of_vegetables = int(input())
quantity_of_fruits = int(input())
total_in_lv = price_of_vegetables * quantity_of_vegetables + price_of_fruits * quantity_of_fruits
total_in_eur = total_in_lv / 1.94
print(f"{total_in_eur:.2f}")