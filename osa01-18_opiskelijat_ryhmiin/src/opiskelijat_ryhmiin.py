# Kirjoita ratkaisu tähän
student = int(input("Montako opiskelijaa?"))
size = int(input("Mikä on ryhmän koko? "))
groups = (student + size - 1) // size

print(f"Ryhmien määrä: {groups}")