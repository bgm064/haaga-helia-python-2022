# tee ratkaisu tänne
def joulukuusi(height):
    stars = "*"
    i = 1
    
    print("joulukuusi!")

    while i < height:
        print(" " * (height - i) + stars)
        stars += "**"
        i += 1

    print(" " * (height - 1) + "*")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(5)