price_of_strawberries = float(input())
quantity_of_bananas = float(input())
quantity_of_oranges = float(input())
quantity_of_raspberries = float(input())
quantity_of_strawberries = float(input())

price_of_raspberries = price_of_strawberries / 2
price_of_oranges = price_of_raspberries * 0.60
price_of_bananas = price_of_raspberries * 0.20

total_money_for_strawberries = price_of_strawberries * quantity_of_strawberries
total_money_for_raspberries = price_of_raspberries * quantity_of_raspberries
total_money_for_oranges = price_of_oranges * quantity_of_oranges
total_money_for_bananas = price_of_bananas * quantity_of_bananas

total = total_money_for_strawberries + total_money_for_raspberries + total_money_for_oranges + total_money_for_bananas
print(total)
