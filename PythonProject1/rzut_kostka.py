
import random


def kostka():
    numery = [1, 2, 3, 4, 5, 6]
    rzut_kostka = random.choice(numery)
    return rzut_kostka

def ai_wybor():
    ai_liczby = [1, 2, 3, 4, 5, 6]
    ai_kostka = random.choice(ai_liczby)
    return ai_kostka

def koniec():
    breakpoint()


def gracz():
    punkty_ai = 0
    punkty_gracz = 0

    print("Jeśli chcesz zakończyć gre wpisz \"p\"")
    while True:
        try:
            wynik = kostka()
            AI = ai_wybor()

            gracz_wybor = int(input("Wybierz liczbe 1-6."))
            ai_wybor()

            if gracz_wybor > 6 or gracz_wybor < 1:
                print(f"Liczba {gracz_wybor} jest poza zakresem,prosze wybrac liczbe 1-6!.")
                continue

            if gracz_wybor == wynik:
                punkty_gracz +=1
                print(f"Zgadłeś liczbe {gracz_wybor} poprawnie!\nPunkty gracz:{punkty_gracz}")

            elif gracz_wybor != wynik:
                print(f"Zgadłeś liczbe {gracz_wybor} niepoprawnie!\nPunkty gracz:{punkty_gracz}")

            if AI == wynik:
                punkty_ai += 1
                print(f"AI Zgadło liczbe {AI} poprawnie!\nPunkty AI:{punkty_ai}")

            elif AI != wynik:
                print(f"AI zgadło liczbe {AI} Niepoprawnie!\nPunkty AI:{punkty_ai}")


        except ValueError:
            print("Podana liczba jest nie poprawna")
            koniec()


gracz()
