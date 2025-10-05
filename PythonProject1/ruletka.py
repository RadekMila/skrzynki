import random

def losowanie():
    liczba = random.randint(1,36)
    kolor = "Czarny" if liczba % 2 == 0 else "Czerwony"
    return kolor,liczba

def ruletka():
    balans = 100
    kolor, liczba = losowanie()

    gracz = input("Obstaw kolor i liczbe 1-36:").capitalize()
    los = gracz.split()

    if len(los) != 2:
        print("Błędny input")
        return

    kolor2 = los[0]
    numer = int(los[1])
    if numer not in range(1,37):
        print("liczba ma być w zakresie 1-36")
        return

    if kolor2 not in ["Czarny","Czerwony"]:
        print("Kolor może być Czarny lub Czerwony")

    stawka = input("Prosze podać stawke.wpisz balans aby sprawdzic ile masz pieniedzy")
    if stawka.lower() == "balans":
        print(f"Balans:{balans}")
        return

    try:
        stawka = int(stawka)
    except ValueError:
        print("❌ Stawka musi być liczbą!")
        return

    print(f"Wypadł kolor:{kolor} i liczba:{liczba}")

    if kolor2 == kolor and numer == liczba:
        print(f"odgadłeś kolor:{kolor} i liczbe:{liczba}")
        balans += stawka * 2
    elif kolor2 == kolor:
        print(f"odgadłeś kolor:{kolor}")
        balans += stawka
    elif numer == liczba:
        print(f"odgadłeś liczbe:{liczba}")
        balans += stawka
    else:
        print("nic nie odgadłeś")
        balans -= stawka

    print(f"twój balans:{balans}")

ruletka()