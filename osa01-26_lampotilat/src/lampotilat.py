# Kirjoita ratkaisu tähän
fahr = int(input("Anna lämpötila (F):"))
cels = (fahr - 32) / 1.8

print(f"{fahr} fahrenheit-astetta on {cels} celsius-astetta")

if cels < 0:
    print("Paleltaa!")