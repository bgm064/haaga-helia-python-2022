# tee ratkaisu tänne
def palindromi(word):
    reverse = ""
    lenght = len(word) - 1
    
    while lenght >= 0:
        reverse += word[lenght]
        lenght -= 1

    return word == reverse

# myös:
# def palindromi(word):
   # for i in range(len(word)//2):

       # if word[i] != word[len(word)-i-1]:
           # return False
    # return True


while True:
    word = input("Anna palindromi: ")

    if palindromi(word):
        print(f"{word} on palindromi!")
        break

    print("ei ollut palindromi")