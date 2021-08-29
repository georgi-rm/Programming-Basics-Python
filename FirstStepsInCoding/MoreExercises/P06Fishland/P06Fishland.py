price_of_skumria = float(input())
price_of_caca = float(input())
quantity_of_palamud = float(input())
quantity_of_safrid = float(input())
quantity_of_shels = int(input())

price_of_palamud = 1.6 * price_of_skumria
price_of_safrid = 1.8 * price_of_caca

total = quantity_of_palamud * price_of_palamud + quantity_of_safrid * price_of_safrid + quantity_of_shels * 7.5

print(f"{total:.2f}")