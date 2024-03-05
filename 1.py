import random

body = 0

def nasobeni(a, b):
    vysledek = a * b
    return vysledek

def kontrola(vysledek, vysledek_zak):
    global body  # Přidáno pro možnost aktualizace globální proměnné body
    if vysledek == vysledek_zak:
        body += 1  # Opraveno z body + 1 na body += 1
        print("Skvělá práce! máš to správně")
    else:
        print("Bohužel spletl jsi se, příště to bude lepší")

for a in range(9):
    x = random.randint(1,10)
    y = random.randint(1,10)

    vysledek_zak = int(input(f"{x} * {y} = "))

    vysledek = nasobeni(x, y)
    kontrola(vysledek, vysledek_zak)

print("Celkový počet bodů:", body)  # Body po cyklu
