# Kirjoita ratkaisu tähän
list = []

while True:
    word = input("sana: ")
    
    if word in list:
        break
    
    list.append(word)

print(f"Annoit {len(list)} eri sanaa")