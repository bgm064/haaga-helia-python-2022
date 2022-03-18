# Kirjoita ratkaisu tähän
until = int(input("Mihin asti: "))
counter = 1
sum = 1
str = ""

while until > sum:
    counter += 1
    sum += counter
    str += f" + {counter}"

print(f"Laskettiin 1{str} = {sum}")