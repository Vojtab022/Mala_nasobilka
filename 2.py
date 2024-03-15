import random

operatory = ['+', '-', '/', '*']

body = 0

def nasobeni(x, y):
    vysledek = eval (str(x) + random.choice(operatory) + str(y))
    return vysledek

def kontrola(vysledek, vysledek_zak):
    global body
    if int(vysledek) == int(vysledek_zak):
        body += 1
        print("Skvělá práce! máš to správně")
    else:
        print("Bohužel spletl jsi se, příště to bude lepší")

for a in range(10):
    x = random.randint(1,10)
    y = random.randint(1,10)

    vysledek_zak = input(str(x) +random.choice(operatory)+ str(y)+'=' )

    vysledek = nasobeni(x, y)
    kontrola(vysledek, vysledek_zak)

print("Celkový počet bodů:", body)
