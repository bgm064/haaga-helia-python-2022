# tee ratkaisu tänne
def pisin_naapurijono(list):
    values = []
    temp = 0
    count = 0
    for i in list:
        last = temp
        temp = i

        if temp - 1 == last or temp + 1 == last:
            count += 1
            values.append(count)

        else:
             count = 1

    return max(values)

if __name__ == "__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))