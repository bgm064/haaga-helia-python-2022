# Kirjoita ratkaisu tähän
word = input("Sana: ")
char = input("Merkki: ")
index = word.find(char)

if index + 3 < len(word):
    print(word[index:index+3])