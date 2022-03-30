# tee ratkaisu tänne
def nelio(str, x):
    i = 0
    row = ""

    while i < x * x:
        if i > 0 and i % x == 0:
            print(row)
            row = ""
        row += str[i % len(str)]
        i += 1
    print(row)

if __name__ == "__main__":
    nelio("ab", 3)
    print()
    nelio("aybabtu", 5)