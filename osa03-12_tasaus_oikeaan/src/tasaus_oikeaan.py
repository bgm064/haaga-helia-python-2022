# Kirjoita ratkaisu tähän
string = input("Sana: ")
index = 0
stars = ""

while index + len(string) < 20:
    stars += "*"
    index += 1

print(stars + string)