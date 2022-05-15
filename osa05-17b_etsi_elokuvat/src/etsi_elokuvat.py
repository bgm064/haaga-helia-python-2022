# tee ratkaisu tänne
def etsi_elokuvat(register: list, keyword: str):
    found = []
    
    for film in register:
        if keyword.lower() in film['nimi'].lower():
            found.append(film)

    return found


if __name__ == "__main__":
    rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
    {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
    {"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

    lista = etsi_elokuvat(rekisteri, "python")
    print(lista)