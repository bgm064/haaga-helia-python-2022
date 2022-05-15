# tee ratkaisu tänne
from tokenize import String


def histogrammi(str):
    list = []
    
    for char in str:
        add = char + " " + (str.count(char) * "*")
        if add not in list:
            list.append(add)
    
    for row in list:
        print(row)
    

if __name__ == "__main__":
    histogrammi("abba")
    print()
    histogrammi("saippuakauppias")