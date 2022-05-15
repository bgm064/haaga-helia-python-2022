# tee ratkaisu tänne
def kaanna(d: dict):
    copy = {}

    for key in d:         
        copy[key] = d[key]
    for key in copy:
        del d[key]
    for key in copy:
        d[copy[key]] = key


if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas", 5: "viides"}
    kaanna(s)
    print(s)