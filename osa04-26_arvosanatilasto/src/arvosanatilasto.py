# Kirjoita ratkaisu tähän
score = []
while True:
    string = input("Koepisteet ja harjoitusten määrä: ")
    if string == "":
        break
    numbers = string.split(" ")
    score.append(int(numbers[0]))       
    score.append(int(numbers[1]) // 10)

i = 0
stars = ["","","","","",""]
while True:
    if i >= len(score):
        break
    if score[i] >= 10:
        if  score[i] + score[i+1] >= 28:
            stars[0] +="*"
        elif score[i] + score[i+1] >= 24:
            stars[1] += "*"
        elif score[i] + score[i+1] >= 21:
            stars[2] += "*"
        elif score[i] + score[i+1] >= 18:
            stars[3] += "*"
        elif score[i] + score[i+1] >= 15:
            stars[4] += "*"
        else:
            stars[5] += "*"
    else:
        stars[5] += "*"
    i +=2

average = f"{2*sum(score)/len(score):.1f}"
if sum(score) > 0:
    approval = f"{100 * (1 - len(stars[5])/(len(stars[0]+stars[1]+stars[2]+stars[3]+stars[4]+stars[5] ))):.1f}"

print("Tilasto:")
print(f"Pisteiden keskiarvo: {average}")
print(f"Hyväksymisprosentti: {approval}")
print("Arvosanajakauma:")
print(f"  5: {stars[0]}")
print(f"  4: {stars[1]}")
print(f"  3: {stars[2]}")
print(f"  2: {stars[3]}")
print(f"  1: {stars[4]}")
print(f"  0: {stars[5]}")