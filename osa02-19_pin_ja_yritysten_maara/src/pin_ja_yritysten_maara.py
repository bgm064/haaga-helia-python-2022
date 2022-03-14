# Kirjoita ratkaisu tähän
attempt = 0

while True:
    pin = int(input("PIN-koodi: "))
    attempt += 1

    if pin == 4321:
        break
    else:
        print("Väärin")

if attempt == 1:
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {attempt} yritystä")