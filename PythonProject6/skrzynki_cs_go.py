import sys
import time
import random

print("Skrzynia Brakout | Skrzynia Phoneix | Skrzynia Gamma1")


# lista skinów z których bedzie loswanie po wylosowaniu rzadkosci
def skiny_Breakout():
    global skiny_niebieskie, skiny_rozowe, skiny_fioletowe, skiny_czerwone, noz, wszystkie_skiny1

    skiny_niebieskie = ["MP7 | Miejskie ryzyko", "Negev | Pustynny szturm", "P2000 | Kość słoniowa", "SSG 08 | Otchłań",
                        "UMP-45 | Labirynt"]

    skiny_rozowe = ["PP-Bizon | Ozyrys", "CZ75-Auto | Tygrys", "Nova | Koi", "P250 | Supernowa"]

    skiny_fioletowe = ["Desert Eagle | Konspiracja", "Five-SeveN | Ptasia zagrywka", "Glock-18 | Żywiołak wody"]

    skiny_czerwone = ["P90 | Asiimov", "M4A1-S | Cyrex"]

    noz = ["Butterfly Knife | Black Laminate",
           "Butterfly Knife | Autotronic",
           "Butterfly Knife | Gamma Doppler",
           "Butterfly Knife | Freehand",
           "Butterfly Knife | Lore",
           "Butterfly Knife | Bright Water"]

    wszystkie_skiny1 = skiny_niebieskie + skiny_rozowe + skiny_fioletowe + skiny_czerwone + noz


skiny_Breakout()


def skiny_Phoenix():
    global skiny_niebieskie2, skiny_rozowe2, skiny_fioletowe2, skiny_czerwone2, noz2, wszystkie_skiny2
    skiny_niebieskie2 = [
        "UMP-45 | Kapral",
        "Negev | Teren",
        "Tec-9 | Burza piaskowa",
        "MAG-7 | Strażnik niebios"
    ]

    skiny_rozowe2 = [
        "MAC-10 | Skwar",
        "SG 553 | Puls",
        "FAMAS | Sierżant",
        "USP-S | Obrońca"
    ]

    skiny_fioletowe2 = [
        "AK-47 | Czerwona linia",
        "P90 | Trygon",
        "Nova | Antyk"
    ]

    skiny_czerwone2 = [
        "AWP | Asiimov",
        "AUG | Kameleon"
    ]

    noz2 = [
        "Butterfly Knife | Fade",
        "Karambit | Case Hardened",
        "Flip Knife | Doppler",
        "M9 Bayonet | Marble Fade",
        "Butterfly Knife | Gamma Doppler",
        "Butterfly Knife | Bright Water"
    ]

    wszystkie_skiny2 = skiny_niebieskie2 + skiny_rozowe2 + skiny_fioletowe2 + skiny_czerwone2 + noz2


skiny_Phoenix()


def skiny_Gamma1():
    global skiny_niebieskie3, skiny_rozowe3, skiny_fioletowe3, skiny_czerwone3, noz3, wszystkie_skiny3
    skiny_niebieskie3 = [
        "Five-SeveN | Brutalny daimyō",
        "MAC-10 | Mięsożerca",
        "Nova | Exo",
        "P250 | Żelazne okucie",
        "PP-Bizon | Żniwiarz",
        "SG 553 | Awiator",
        "Tec-9 | Czapa lodowa",
    ]

    skiny_rozowe3 = [
        "AUG | Arystokrata",
        "AWP | Fobos",
        "P90 | Chopper",
        "Rewolwer R8 | Restart",
        "Obrzyn | Limetka"
    ]

    skiny_fioletowe3 = [
        "M4A4 | Kosmiczna pustka",
        "P2000 | Smok cesarski",
        "SCAR-20 | Krwawy sport"
    ]

    skiny_czerwone3 = [
        "Glock-18 | Pustynny buntownik",
        "M4A1-S | Mecha Industries"
    ]

    noz3 = [
        "Karambit | Gamma Doppler",
        "Flip Knife | Gamma Doppler",
        "Butterfly Knife | Gamma Doppler",
        "M9 Bayonet | Gamma Doppler",
        "Karambit | Autotronic",
        "Flip Knife | Marble Fade"
    ]

    wszystkie_skiny3 = skiny_niebieskie3 + skiny_rozowe3 + skiny_fioletowe3 + skiny_czerwone3 + noz3


skiny_Gamma1()


def losowanie():
    # losowanie skina po losowaniu rzadkosci
    # skrzynia breakout
    niebieski = random.choice(skiny_niebieskie)
    rozowy = random.choice(skiny_rozowe)
    fioletowy = random.choice(skiny_fioletowe)
    czerwony = random.choice(skiny_czerwone)
    zlote = random.choice(noz)

    # skrzynia Phoneix
    niebieski2 = random.choice(skiny_niebieskie2)
    rozowy2 = random.choice(skiny_rozowe2)
    fioletowy2 = random.choice(skiny_fioletowe2)
    czerwony2 = random.choice(skiny_czerwone2)
    zlote2 = random.choice(noz2)

    # skrzynia gamma1
    niebieski3 = random.choice(skiny_niebieskie3)
    rozowy3 = random.choice(skiny_rozowe3)
    fioletowy3 = random.choice(skiny_fioletowe3)
    czerwony3 = random.choice(skiny_czerwone3)
    zlote3 = random.choice(noz3)

    # dobieranie wag(procentów(%)) do rzadkosci skinów
    kolor = ["niebieski", "różowy", "fioletowy", "czerwony", "złoty"]
    wagi = [60, 25, 10, 4, 1]

    # lista bedzie sie wypełniała w zależnosci od wylosowanej rzadkosci
    skrzynia = []

    # losowanie rzadkosci w wybranej przez użytkownika skrzynki
    if wybór == "1":
        skrzynia.append(wszystkie_skiny1)
        los_rzadkosc = random.choices(kolor, weights=wagi, k=1)[0]

        # losowanie skina (NIEBIESKI)
        if los_rzadkosc == "niebieski":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny1)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{niebieski}<<<")

        # losowanie skina (RÓŻOWY)
        elif los_rzadkosc == "różowy":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny1)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{rozowy}<<<")

        # losowanie skina (FIOLETOWY)
        elif los_rzadkosc == "fioletowy":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny1)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{fioletowy}<<<")

        # losowanie skina (CZERWONY)
        elif los_rzadkosc == "czerwony":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny1)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{czerwony}<<<")

        # losowanie skina (ZŁOTY)
        elif los_rzadkosc == "złoty":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny1)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{zlote}<<<")

    if wybór == "2":
        skrzynia.append(wszystkie_skiny2)
        los_rzadkosc = random.choices(kolor, weights=wagi, k=1)[0]

        # losowanie skina (NIEBIESKI)
        if los_rzadkosc == "niebieski":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny2)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{niebieski2}<<<")

        # losowanie skina (RÓŻOWY)
        elif los_rzadkosc == "różowy":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny2)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{rozowy2}<<<")

        # losowanie skina (FIOLETOWY)
        elif los_rzadkosc == "fioletowy":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny2)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{fioletowy2}<<<")

        # losowanie skina (CZERWONY)
        elif los_rzadkosc == "czerwony":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny2)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{czerwony2}<<<")

        # losowanie skina (ZŁOTY)
        elif los_rzadkosc == "złoty":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny2)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{zlote2}<<<")

    if wybór == "3":
        skrzynia.append(wszystkie_skiny3)
        los_rzadkosc = random.choices(kolor, weights=wagi, k=1)[0]

        # losowanie skina (NIEBIESKI)
        if los_rzadkosc == "niebieski":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny3)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{niebieski3}<<<")

        # losowanie skina (RÓŻOWY)
        elif los_rzadkosc == "różowy":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny3)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{rozowy3}<<<")

        # losowanie skina (FIOLETOWY)
        elif los_rzadkosc == "fioletowy":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny3)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{fioletowy3}<<<")

        # losowanie skina (CZERWONY)
        elif los_rzadkosc == "czerwony":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny3)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{czerwony3}<<<")

        # losowanie skina (ZŁOTY)
        elif los_rzadkosc == "złoty":
            print("Losowanie...")
            delay = 0.05
            for i in range(20):
                x = random.choice(wszystkie_skiny3)
                print(f"\r{x}", end="", flush=True)
                time.sleep(delay)
                delay += 0.02
            print(f"\r>>>{zlote3}<<<")


# wybieranie skrzynki i rozpoczynanie funkcji w razie blednego inputu cofa uzytkownika do ponownego wpisanaia liczby
while True:
    wybór = input("\nWybierz skrzynie 1|2|3")
    if wybór in ["1", "2", "3"]:
        losowanie()
    elif wybór != "1" or wybór != "2" or wybór != "3":
        print("Błędny input")
        continue
