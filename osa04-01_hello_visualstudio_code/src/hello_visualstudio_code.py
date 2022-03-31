# Kirjoita ratkaisu tähän
while True:
    ide = input("Editori: ").lower()

    if ide == "visual studio code":
        break
    elif ide == "word" or ide == "notepad":
        print("surkea")
    else:
        print("ei ole hyvä")

print("loistava valinta!")