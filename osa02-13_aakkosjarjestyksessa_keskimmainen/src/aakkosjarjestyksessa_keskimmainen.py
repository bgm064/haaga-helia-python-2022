# Kirjoita ratkaisu tähän
let1 = input("Anna 1. kirjain:")
let2 = input("Anna 2. kirjain:")
let3 = input("Anna 3. kirjain:")

if let2 > let1 > let3 or let2 < let1 < let3:
    mid = let1
elif let1 > let2 > let3 or let1 < let2 < let3:
    mid = let2
elif let1 > let3 > let2 or let1 < let3 < let2:
    mid = let3

print(f"Keskimmäinen kirjain on {mid}")
