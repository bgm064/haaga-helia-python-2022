# Kirjoita ratkaisu tähän
pay = float(input("Tuntipalkka:"))
hours = int(input("Työtunnit:"))
day = input("Viikonpäivä:")
wage = hours * pay

if day == "sunnuntai":
    wage = (hours * pay) * 2

print(f"Palkka {wage} euroa")