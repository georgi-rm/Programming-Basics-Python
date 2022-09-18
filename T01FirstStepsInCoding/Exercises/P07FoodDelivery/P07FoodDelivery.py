price_of_chicken_menu = 10.35
price_of_fish_menu = 12.40
price_of_vegan_menu = 8.15

price_of_delivery = 2.50

quantity_of_chicken_menu = int(input())
quantity_of_fish_menu = int(input())
quantity_of_vegan_menu = int(input())

price_for_menus = quantity_of_chicken_menu * price_of_chicken_menu + quantity_of_fish_menu * price_of_fish_menu + quantity_of_vegan_menu * price_of_vegan_menu
price_for_desert = price_for_menus * 0.2

total = price_for_menus + price_for_desert + price_of_delivery

print(total)
