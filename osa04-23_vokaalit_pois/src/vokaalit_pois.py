# tee ratkaisu tänne
def ilman_vokaaleja(string):
    vocals = 'aeiouyåäö'
    new_string = ''
    for letter in string:
        if letter not in vocals:
            new_string += letter
    return new_string

if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))