# tee ratkaisu tänne
def lookup(persons):
    name = input("nimi: ")

    if name in persons:
        for num in persons[name]:
            print(num)
    else:
        print("ei numeroa")

def add(persons):
    name = input("nimi: ")
    num = input("numero: ")

    if name not in persons:
        persons[name] = []
    persons[name].append(num)
    print("ok!")
    

def main():
    persons = {}

    while True:
        cmd = input("komento (1 hae, 2 lisää, 3 lopeta): ")
        if (cmd == "1"):
            lookup(persons)
        if (cmd == "2"):
            add(persons)
        if (cmd == "3"):
            break

    print("lopetetaan...")

main()