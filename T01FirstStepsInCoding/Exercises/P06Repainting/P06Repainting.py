price_nylon = 1.50
price_paint = 14.50
price_paint_thinner = 5.00
price_bag = 0.40

quantity_nylon = int(input()) + 2
quantity_paint = 1.1 * int(input())
quantity_paint_thinner = int(input())
hours_of_work = int(input())

price_of_materials = quantity_nylon * price_nylon + quantity_paint * price_paint + quantity_paint_thinner * price_paint_thinner + price_bag

payment_of_workers = price_of_materials * 0.3 * hours_of_work

total = price_of_materials + payment_of_workers

print(total)
