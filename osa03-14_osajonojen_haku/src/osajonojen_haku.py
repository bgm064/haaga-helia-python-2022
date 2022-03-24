# Kirjoita ratkaisu tähän
word = input("Sana: ")
char = input("Merkki: ")
index = 0

while index + 3 <= len(word):
    if word[index] == char:
        print(word[index:index+3])
    index += 1