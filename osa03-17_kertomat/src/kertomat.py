# Kirjoita ratkaisu tähän
while True:
    num = int(input("Anna luku: "))

    if num <= 0:
        break
    
    i = 1
    j = 1
    
    while j <= num:
        i *= j
        j += 1

    print(f"Luvun {num} kertoma on {i}")

print("Kiitos ja moi!") 