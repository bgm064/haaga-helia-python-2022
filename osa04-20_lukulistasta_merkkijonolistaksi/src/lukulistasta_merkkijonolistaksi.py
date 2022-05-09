# tee ratkaisu tänne
def muotoile(lista):
    edited_list = []
    for i in lista:
        edited_list.append(f"{i:.2f}")
    
    return edited_list

if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)