# Kirjoita ratkaisu tähän
per1 = str(input("Henkilö 1:\nNimi:"))
age1 = int(input("Ikä:"))
per2 = str(input("Henkilö 2:\nNimi:"))
age2 = int(input("Ikä:"))

if age1 > age2:
    print(f"Vanhempi on {per1}")
elif age1 < age2:
    print(f"Vanhempi on {per2}")
else:
    print(f"{per1} ja {per2} ovat yhtä vanhoja")