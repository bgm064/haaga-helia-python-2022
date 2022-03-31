# tee ratkaisu tänne
def lista_tahtina(stars: list):
    for i in range(len(stars)):
        print(stars[i] * "*")

if __name__ == "__main__":
    print(lista_tahtina([3, 7, 1, 1, 2]))

# myös:
# def lista_tahtina(lista: list):
   # for luku in lista:
        # print("*" * luku)