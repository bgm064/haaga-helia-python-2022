# Kirjoita ratkaisu tähän
string = input("Sana: ")
start = (28 - len(string)) // 2
end = start

if len(string) % 2 != 0:
    end += 1

print("*" * 30)
print("*" + start * " " + string + end * " " + "*")
print("*" * 30)