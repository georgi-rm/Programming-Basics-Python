number_of_days = int(input())
number_of_cake_makers = int(input())
number_of_cakes = int(input())
number_of_waffles = int(input())
number_of_pancakes = int(input())

price_of_cakes = number_of_cakes * 45
price_of_waffles = number_of_waffles * 5.80
price_of_pancakes = number_of_pancakes * 3.20

total_price_for_products = price_of_cakes + price_of_waffles + price_of_pancakes
total_price_from_campaign = total_price_for_products * number_of_cake_makers * number_of_days
total_income = total_price_from_campaign * 7 / 8
print(total_income)
