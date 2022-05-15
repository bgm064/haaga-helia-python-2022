# tee ratkaisu tänne
def lisaa_elokuva(register: list, name: str, director: str, year: int, length: int):
    film = {"nimi": name, "ohjaaja": director, "vuosi": year, "pituus": length}
    register.append(film)


if __name__ == "__main__":
    rekisteri = []
    lisaa_elokuva(rekisteri, "Pythonin viemää", "Pekka Python", 2017, 116)
    lisaa_elokuva(rekisteri, "Python lentokoneessa", "Renny Pytholin", 2001, 94)
    print(rekisteri)