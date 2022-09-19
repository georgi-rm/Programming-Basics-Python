year_training_price = int(input())

sneakers_price = year_training_price * 0.6
outfit_price = sneakers_price * 0.8
ball_price = outfit_price / 4
accessories_price = ball_price / 5

total = year_training_price + sneakers_price + outfit_price + ball_price + accessories_price

print(total)
