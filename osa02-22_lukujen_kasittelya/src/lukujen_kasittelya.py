# Kirjoita ratkaisu tähän
counter = 0
num_sum = 0
pos_counter = 0
neg_counter = 0

print("Syötä kokonaislukuja, 0 lopettaa:")

while True:
    num = int(input("Luku: "))
    counter += 1
    num_sum += num

    if num > 0:
        pos_counter += 1
    elif num < 0:
        neg_counter += 1
    else:
        break

print(f"Lukuja yhteensä {counter - 1}")
print(f"Lukujen summa {num_sum}")
print(f"Lukujen keskiarvo {num_sum / (counter - 1)}")

if pos_counter > 0:
    pos_counter - 1
if neg_counter > 0:
    neg_counter - 1

print(f"Positiivisia {pos_counter}")
print(f"Negatiivisia {neg_counter}")