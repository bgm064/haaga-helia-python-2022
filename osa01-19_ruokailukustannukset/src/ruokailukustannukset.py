# Kirjoita ratkaisu tähän
times = int(input("Montako kertaa viikossa syöt Unicafessa? "))
price = float(input("Unicafe-lounaan hinta? "))
spend = float(input("Paljonko käytät viikossa ruokaostoksiin? "))
sum = float(times * price + spend)

print("\nKustannukset keskimäärin:")
print(f"Päivässä {sum / 7} euroa")
print(f"Viikossa {sum} euroa")