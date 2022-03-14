# Kirjoita ratkaisu tähän
password = input("Salasana: ")

while True:
    confirm = input("Toista salasana: ")
    
    if confirm == password:
        print("Käyttäjätunnus luotu!")
        break
    else:
        print("Ei ollut sama!")