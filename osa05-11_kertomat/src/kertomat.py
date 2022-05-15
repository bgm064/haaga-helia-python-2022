# tee ratkaisu tänne
def kertomat(n: int):
    dictionary = {}
    start = 1
    factorial = 1
    
    while start <= n:
        factorial *= start
        dictionary[start] = factorial
        start += 1
        
    return dictionary


if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])