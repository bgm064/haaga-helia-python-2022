# Kirjoita ratkaisu tähän
num = int(input("Anna luku: "))
i = 1

while i + 1 <= num:
    print(i + 1)    # Print first number + 1
    print(i)        # Print first number
    i += 2

if i <= num:
    print(i)