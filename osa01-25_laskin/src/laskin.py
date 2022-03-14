# Kirjoita ratkaisu tähän
num1 = int(input("Luku 1: "))
num2 = int(input("Luku 2: "))
comm = input("Komento: ")

if comm == "summa":
    print(f"{num1} + {num2} = {num1 + num2}")

if comm == "tulo":
    print(f"{num1} * {num2} = {num1 * num2}")

if comm == "erotus":
    print(f"{num1} - {num2} = {num1 - num2}")

