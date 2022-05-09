# tee ratkaisu tänne
def summa(a: list, b: list):
    sum = []

    for i in range(len(a)):
       sum.append(a[i] + b[i])

    return sum


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b)) # [8, 10, 12]