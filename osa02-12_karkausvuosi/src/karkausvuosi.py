# Kirjoita ratkaisu tähän
year = int(input("Anna vuosi:"))
leap = False

if year % 4 == 0:
    leap = True
    if year % 100 == 0 and year % 400 != 0:
        leap = False

if leap:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")