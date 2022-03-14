# Kirjoita ratkaisu tähän
word1 = str(input("Anna 1. sana:"))
word2 = str(input("Anna 2. sana:"))

if word1 > word2:
    print(f"{word1} on aakkosjärjestyksessä viimeinen.")
elif word1 < word2:
    print(f"{word2} on aakkosjärjestyksessä viimeinen.")
else:
    print("Annoit saman sanan kahdesti.")