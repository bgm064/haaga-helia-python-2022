# Kirjoita ratkaisu tähän
story = ""
previous = ""

while True:
    word = input("Anna sana: ")
    
    if word == "loppu" or word == previous:
        break
    else:
        story += word + " "
        previous = word

print(story)