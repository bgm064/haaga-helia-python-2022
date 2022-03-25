# Kirjoita ratkaisu tähän
sentence = " " + input("Anna lause: ")
i = 1

while i < len(sentence):
    if sentence[i - 1] == " " and sentence[i] != " ":
        print(sentence[i])
    
    i += 1