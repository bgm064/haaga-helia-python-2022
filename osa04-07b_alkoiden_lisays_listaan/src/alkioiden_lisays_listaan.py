# Kirjoita ratkaisu tähän
size = int(input("Kuinka monta lukua: "))
list = []
i = 1

while i <= size:
    num = int(input(f"Anna luku {i}: "))
    list.append(num)
    i += 1

print(list)