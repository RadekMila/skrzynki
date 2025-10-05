import random


def symbole():
    global rzad1, rzad2, rzad3, wynik
    symbole1 = {"🍒": 10, "🍋": 20, "🔔": 50, "⭐": 100, "7️⃣": 200}
    wagi = {"🍒": 50, "🍋": 30, "🔔": 15, "⭐": 4, "7️⃣": 1}

    losuj = random.choices(list(symbole1.keys()), weights=[wagi[s] for s in symbole1.keys()], k=3)
    wynik = losuj
    rzad1 = losuj[0]
    rzad2 = losuj[1]
    rzad3 = losuj[2]
    return wynik


def slotsy_gracz():

    saldo = 100
    print("Aby zobaczyc saldo wpisz \"PLN\"")
    while True:
        gracz = input("Podaj stawke na jakiej chcesz grać.Aby zakonczyc gre wpisz \"q\".\n:")

        if gracz.upper() == "PLN":
            print(saldo)
            continue

        if gracz.lower() == "q":
            print("koniec gry")
            break

        else:
            try:
                gracz = int(gracz)

                if gracz <= 0:
                    print("Stawka musi wynośić więcej niz zero(0)")
                    continue

                if gracz > saldo:
                    print(f"Nie możesz postawić {gracz}, masz tylko {saldo} na koncie!")
                    continue


            except ValueError:
                print(f"Stawka:{gracz} jest większa od salda gracza")
                continue

        wynik = symbole()
        rzad1, rzad2, rzad3 = wynik

        if rzad1 == rzad2 == rzad3 and rzad1 == "🍒" and rzad2 == "🍒" and rzad3 == "🍒":
            print(wynik)
            print("Wygrałeś")
            saldo += gracz * 0.2 + gracz
            print(saldo)

        elif rzad1 == rzad2 == rzad3 and rzad1 == "🍋" and rzad2 == "🍋" and rzad3 == "🍋":
            print(wynik)
            print("Wygrałeś")
            saldo += gracz * 0.5 + gracz
            print(saldo)

        elif rzad1 == rzad2 == rzad3 and rzad1 == "🔔" and rzad2 == "🔔" and rzad3 == "🔔":
            print(wynik)
            print("Wygrałeś")
            saldo += gracz * 0.75 + gracz
            print(saldo)

        elif rzad1 == rzad2 == rzad3 and rzad1 == "⭐" and rzad2 == "⭐" and rzad3 == "⭐":
            print(wynik)
            print("Wygrałeś")
            saldo += gracz * 4 + gracz
            print(saldo)

        elif rzad1 == rzad2 == rzad3 and rzad1 == "7️⃣" and rzad2 == "7️⃣" and rzad3 == "7️⃣":
            print(wynik)
            print("Wygrałeś")
            saldo += gracz * 8 + gracz
            print(saldo)

        else:
            print(wynik)
            print("Przegrałeś")
            saldo -= gracz
            print(f"SALDO:{saldo}")

        if saldo <= 0:
            print("Skończyły ci sie pieniądze")
            break


slotsy_gracz()
