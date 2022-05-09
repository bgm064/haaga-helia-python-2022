# tee ratkaisu tänne
def pisin(list):
    longest = list[0]
    for string in list:
        if len(longest) < len(string):
            longest = string
    
    return longest

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))