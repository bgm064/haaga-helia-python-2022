# Tee ratkaisu tänne
def anagrammi(a: str, b: str):
    if sorted(a) == sorted(b):
        return True
    else:
        return False


if __name__ == "__main__":
    print(anagrammi("talo", "tola")) # True
    print(anagrammi("talo", "lato")) # True
    print(anagrammi("talo", "olat")) # True
    print(anagrammi("tammi", "mitta")) # False
    print(anagrammi("python", "java")) # False