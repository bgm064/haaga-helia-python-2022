# tee ratkaisu tänne
def eniten_kirjainta(string):
    most_common = string[0]
    for letter in string:
        if string.count(most_common) < string.count(letter):
            most_common = letter

    return most_common

if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))
    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))