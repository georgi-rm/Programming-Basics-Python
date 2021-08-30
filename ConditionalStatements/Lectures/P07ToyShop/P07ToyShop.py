price_of_excursion = float(input())
quantity_of_puzzles = int(input())
quantity_of_speaking_dolls = int(input())
quantity_of_teddy_bears = int(input())
quantity_of_minions = int(input())
quantity_of_trucks = int(input())

earned_money = quantity_of_puzzles * 2.60 + quantity_of_speaking_dolls * 3 + quantity_of_teddy_bears * 4.10 + quantity_of_minions * 8.20 + quantity_of_trucks * 2
number_of_sold_toys = quantity_of_puzzles + quantity_of_speaking_dolls + quantity_of_teddy_bears + quantity_of_minions + quantity_of_trucks

if number_of_sold_toys >= 50:
    earned_money = 0.75 * earned_money

total = earned_money * 0.9

money_difference = abs(total - price_of_excursion)

if total >= price_of_excursion:
    print(f"Yes! {money_difference:.2f} lv left.")
else:
    print(f"Not enough money! {money_difference:.2f} lv needed.")