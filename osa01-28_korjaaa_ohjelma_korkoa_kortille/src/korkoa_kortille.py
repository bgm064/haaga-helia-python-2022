# Korjaa ohjelma
pisteet = int(input("Kuinka paljon pisteitä?"))

if pisteet < 100:
    kerroin = 1.1
    print("Sait 10 % bonusta")

if pisteet >= 100:
    kerroin = 1.15
    print("Sait 15 % bonusta")

pisteet *= kerroin
print("Pisteitä on nyt", pisteet)