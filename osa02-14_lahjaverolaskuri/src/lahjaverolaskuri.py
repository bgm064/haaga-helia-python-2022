# Kirjoita ratkaisu tähän
gift = int(input("Lahjan suuruus? "))

if gift < 5000:
    print("Ei veroa!")
else:
    if gift > 5000 and gift < 25000:
        gift = (gift - 5000) * 0.08 + 100
    elif gift > 25000 and gift < 55000:
        gift = (gift - 25000) * 0.1 + 1700
    elif gift > 55000 and gift < 200000:
        gift = (gift - 55000) * 0.12 + 4700
    elif gift > 200000 and gift < 1000000:
        gift = (gift - 200000) * 0.15 + 22100
    elif gift > 1000000:
        gift = (gift - 1000000) * 0.17 + 142100
    print(f"Vero: {float(gift)} ")
