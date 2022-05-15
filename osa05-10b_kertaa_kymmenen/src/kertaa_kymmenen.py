# tee ratkaisu tänne
def kertaa_kymmenen(start: int, end: int):
    dictionary = {}
    while start <= end:
        dictionary[start] = start * 10
        start += 1
    
    return dictionary

if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)