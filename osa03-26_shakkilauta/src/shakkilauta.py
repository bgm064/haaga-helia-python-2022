# tee ratkaisu tänne
def shakkilauta(x):
    i = 0

    while i < x:
        if i % 2 == 0:
            y = "10" * x    # even rows
        else:
            y = "01" * x    # odd rows
            
        print(y[0:x])       # delete surplus
        i += 1

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(3)
