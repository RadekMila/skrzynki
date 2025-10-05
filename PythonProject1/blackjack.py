import random
from operator import index


def talia_kart():
    global talia
    talia = ["2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠",
             "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥",
             "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦",
             "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣",
             "J♠", "J♥", "J♦", "J♣",
             "Q♠", "Q♥", "Q♦", "Q♣",
             "K♠", "K♥", "K♦", "K♣",
             "A♠", "A♥", "A♦", "A♣"]


def punkty_talia():
    global talia_punkty
    talia_punkty = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                    "J": 10, "Q": 10, "K": 10, "A": 11}
    return talia_punkty


def tasowanie_talii(powtorzenia=150):
    for _ in range(powtorzenia):
        random_index = random.randint(0, len(talia) - 1)
        karta = talia.pop(random_index)

        new_index = random.randint(0, len(talia))
        talia.insert(new_index, karta)


talia_kart()
tasowanie_talii(150)
punkty_talia()


def reka_ai():
    global reka_ai1,karta_ai1,karta_ai2,suma_ai,punkt_ai1,punkt_ai2,karta3
    reka_ai1 = []

    karta_ai1 = talia.pop()
    reka_ai1.append(karta_ai1)

    karta_ai2 = talia.pop()
    reka_ai1.append(karta_ai2)

    karta3 = talia.pop()
    reka_ai1.append(karta3)

    punkty = 0

    nominal_ai1 = karta_ai1[:-1]
    nominal_ai2 = karta_ai2[:-1]
    nominal_aidobrana = karta3[:-1]

    punkt_ai1 = int(talia_punkty[nominal_ai1])
    punkt_ai2 = int(talia_punkty[nominal_ai2])
    punkty_aidobrana = int(talia_punkty[nominal_aidobrana])

    suma_ai = 0

    suma_ai += punkt_ai1 + punkt_ai2

    if suma_ai < 16:
        suma_ai += punkty_aidobrana



    if suma_ai > 21 and punkt_ai1 and punkt_ai2 == "A":
        suma_ai -= 10

    print(f"AI:{karta_ai1}")
    print(f"punkty_AI:{punkt_ai1}")

reka_ai()


def reka_gracza():
    global reka_gracza1,suma
    reka_gracza1 = []

    karta1 = talia.pop()
    gracz_karta = reka_gracza1.append(karta1)

    karta2 = talia.pop()
    gracz_karta = reka_gracza1.append(karta2)

    punkty = 0



    nominal1 = karta1[:-1]
    nominal2 = karta2[:-1]


    punkt1 = int(talia_punkty[nominal1])
    punkt2 = int(talia_punkty[nominal2])

    suma = 0

    suma += punkt1 + punkt2

    if suma > 21 and nominal1 and nominal2 == "A":
        suma -= 10

    print(f"GRACZ:{karta1} {karta2}")
    print(f"Punkty_gracz:{suma}")


    dobiera = True
    while dobiera:
       gracz = input("D-Dobierz,S-Stand").upper()
       if gracz == "D":
            karta_dobrana = talia.pop()
            reka_gracza1.append(karta_dobrana)
            print("GRACZ:", " ".join(reka_gracza1))

            nominal_dobrana = karta_dobrana[:-1]
            punkt_dobrany = int(talia_punkty[nominal_dobrana])
            suma += punkt_dobrany
            print(f"punkty_gracz:{suma}")

       tura = 0
       if gracz =="S":
           tura += 1

       if suma == 21 and tura == 0:
           print("BlackJack,Wygrałeś")
           break

       elif suma_ai == 21 and tura == 0:
           print("BlackJack,Przegrałeś")
           print(f"{karta_ai1} {karta_ai2} {karta3}")
           break

       elif suma > 21:
           print(f"AI:{karta_ai1} {karta_ai2}")
           print(f"Punkty_ai:{suma_ai}")
           print("BUST,PRZEGRAŁEŚ")
           break

       elif suma_ai > 21:
           print(f"AI:{karta_ai1} {karta_ai2}")
           print(f"Punkty_ai:{suma_ai}")
           print("BUST AI,WYGRAŁEŚ")
           break

       elif suma > 21 and punkt_ai1 + punkt_ai2 < 16:
           print(f"AI:{karta_ai1} {karta_ai2} {karta3}")
           print(f"Punkty_ai:{suma_ai}")
           print("BUST,Przegrałeś")
           break

       elif suma_ai > 21 and punkt_ai1 + punkt_ai2 < 16:
           print(f"AI:{karta_ai1} {karta_ai2} {karta3}")
           print(f"Punkty_ai:{suma_ai}")
           print("BUST AI,WYGRAŁEŚ")
           break



       elif gracz == "S" and punkt_ai1 + punkt_ai2 < 16:
           print(f"AI:{karta_ai1} {karta_ai2} {karta3}")
           print(f"Punkty_ai:{suma_ai}")
           dobiera = False

       elif gracz == "S":
           print(f"AI:{karta_ai1} {karta_ai2}")
           print(f"Punkty_ai:{suma_ai}")
           dobiera = False

       if (gracz == "S" and suma != 22 and suma > suma_ai) \
               or (suma > 21 and suma_ai != 22) \
               or (suma_ai > 21):
           print("Wygrałeś")

       elif (gracz == "S" and suma != 22 and suma < suma_ai) \
               or (suma > 21 and suma_ai != 22) \
               or (suma_ai > 21):
           print("Przegrałeś")



reka_gracza()














