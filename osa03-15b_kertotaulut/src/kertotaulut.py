# Kirjoita ratkaisu tähän
num = int(input("Anna luku: "))
i = 1
j = 1

while i + j < num + num:
    print(i, " x ", j, " = ", i * j)
    j += 1
        
    if j > num:
        j = 1
        i += 1
    
print(i, " x ", j, " = ", i * j)