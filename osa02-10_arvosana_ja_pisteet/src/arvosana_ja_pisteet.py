# Kirjoita ratkaisu tähän
score = int(input("Anna pisteet [0-100]:"))
grade = ""

if score < 0 or score > 100:
    grade = "mahdotonta!"
elif score >= 0 and score <= 49:
    grade = "hylätty"
elif score >= 50 and score <= 59:
    grade = "1"
elif score >= 60 and score <= 69:
    grade = "2"
elif score >= 70 and score <= 79:
    grade = "3"
elif score >= 80 and score <= 89:
    grade = "4"
elif score >= 90 and score <= 100:
    grade = "5"

print(f"Arvosana: {grade}")