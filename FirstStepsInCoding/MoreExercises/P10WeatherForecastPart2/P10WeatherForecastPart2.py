temperature = float(input())

if temperature < 5:
    print("unknown")
elif temperature < 12:
    print("Cold")
elif temperature < 15:
    print("Cool")
elif temperature <= 20:
    print("Mild")
elif temperature < 26:
    print("Warm")
elif temperature <= 35:
    print("Hot")
else:
    print("unknown")