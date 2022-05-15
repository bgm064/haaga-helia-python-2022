# tee ratkaisu tänne
def lookup(persons):
    name = input("nimi: ")

    if name in persons:
        print(persons[name])
    else:
        print("ei numeroa")

def add(persons):
    name = input("nimi: ")
    num = input("numero: ")
    persons[name] = num

    print("ok!")

def main():
    persons = {}

    while True:
        cmd = input("komento (1 hae, 2 lisää, 3 lopeta): ")
        if cmd == "1":
            lookup(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break

    print("lopetetaan...")

main()