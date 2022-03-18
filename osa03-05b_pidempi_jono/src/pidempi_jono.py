# Kirjoita ratkaisu tähän
first = input("Anna jono 1: ")
second = input("Anna jono 2: ")

if len(first) > len(second):
    print(f"{first} on pidempi")
elif len(second) > len(first):
    print(f"{second} on pidempi")
else:
    print("Jonot ovat yhtä pitkät")