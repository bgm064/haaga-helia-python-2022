# Kirjoita ratkaisu tähän
str = input("Anna sana: ")

if str[1] == str[-2]:
    print(f"Toinen ja toiseksi viimeinen kirjain on {str[1]}")
else:
    print("Toinen ja toiseksi viimeinen kirjain eroavat")