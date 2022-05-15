# tee ratkaisu tänne
def vanhin(persons: list):
    oldest = []

    for i in persons:
        oldest.append(i[1])

    keyword = min(oldest)

    for i in persons:
        if keyword == i[1]:
            return i[0]


if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4 ]

    print(vanhin(hlista))