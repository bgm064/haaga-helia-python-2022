# Kirjoita ratkaisu tähän

print("Kerro huominen sääennuste:")
temp = int(input("Lämpötila: "))
rain = input("Sataako (kyllä/ei):")

print("Pue housut ja t-paita")

if temp <= 20:
    print("Ota myös pitkähihainen paita")

if temp <= 10:
    print("Pue päälle takki")

if temp <= 5:
    print("Pue päälle takki")
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")

if rain == "kyllä":
    print("Muista sateenvarjo!")