# tee ratkaisu tänne
def kaikki_vaarinpain(lista):
    reverse_list = []
    
    for i in lista:
        reverse_list.append(i[::-1])
    
    return reverse_list[::-1]

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)