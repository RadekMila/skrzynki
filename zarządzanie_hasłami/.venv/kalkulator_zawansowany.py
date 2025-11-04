import math
import operator


def kalkulator_podstawowy():
    while True:
        # + - dodawanie | - = odejmowanie | * - mnożenie | / - dzielenie | ** - potęgowanie | zaokr - zkorąglenie do liczby (x) |
        dzialania = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "**": operator.pow
        }
        print("OPCJE:+ | - | * | / | ** | zaokr |","exit to quit")

        rodzaj = input(":")
        liczba1 = float(input("int1:"))

        if rodzaj == "exit":
            break

        elif rodzaj == "zaokr":
            y = int(input("Podaj liczbe po przecinku do ktorej chcesz zaokrąglić:"))
            wynik = f":{liczba1:.{y}f}"
            print(wynik)
            continue

        liczba2 = float(input(":"))

        if rodzaj in dzialania:
            wynik = dzialania[rodzaj](liczba1, liczba2)
            print(f"{wynik}")





def kalkulator_zaawansowany():
    while True:
        #// - dzielenie całkowite | % - dzielenie z resztą | abs - wartość bezwzględna(|x|) | sqrt - pierwiastek | ! - silnia |
        print("OPCJE:// | % | abs | sqrt | ! |","exit to quit")
        rodzaj2 = input(":")

        if rodzaj2 == "exit":
            break


        liczba1 = float(input(":"))

        if rodzaj2 == "!":
            silnia = 1
            for x in range(1, int(liczba1 + 1)):
                silnia *= x
            print(silnia)
            continue

        elif rodzaj2 == "abs":
            wynik = operator.abs(liczba1)
            print(wynik)
            continue

        elif rodzaj2 == "sqrt":
            wynik = math.sqrt(liczba1)
            print(wynik)
            continue

        liczba2 = float(input(":"))

        dzialania = {
            "//": operator.floordiv,
            "%": operator.mod,

        }

        if rodzaj2 in dzialania:
            wynik = dzialania[rodzaj2](liczba1, liczba2)
            print(f"{wynik}")


def kalkulaotr_profesjonalny():
    while True:
        print("|log|","exit to quit")
        rodzaj = input(":").lower()

        if rodzaj == "exit":
            break

        if rodzaj == "log":
            l = input('podaj log(x):')
            log = float(input(f"log{l}(X)"))
            if l == "e":
                l = math.e
            wynik = math.log(l,log)
            print(f":{wynik:.6f}")

def kalkulator_trygonometryczny():
    rodzaj_tryg = input(" RAD | SIN | COS | TG | CTG").upper()
    if rodzaj_tryg == "RAD":
        stopnie = float(input("Stopnie:"))
        rad = stopnie * math.pi / 180
        print(f"RADIANY:{rad}")

    elif rodzaj_tryg == "SIN":
        # Obliczanie radianów
        pi = 3.14159
        stopnie = float(input("Stopnie:"))
        xrad = stopnie * pi / 180
        print(f"{xrad:.6f}")

        # szereg taylora
        n = 3
        y = 0.000000005
        liczba = 3
        znak = 1

        wyniki = []
        while True:
            z = math.pow(xrad, n) / math.factorial(n)
            b = z * znak
            wyniki.append(round(b, 10))

            if liczba == 9:
                break

            n += 2
            liczba += 2
            znak *= -1

        suma_wynikow = sum(wyniki)
        final = xrad - suma_wynikow
        print(f"SINα:{stopnie}° = {final:.10f}")

    elif rodzaj_tryg == "COS":
        # Obliczanie radianów
        pi = 3.14159
        stopnie = float(input("Stopnie:"))
        xrad = stopnie * pi / 180
        print(f"{xrad:.6f}")

        # szereg taylora
        n = 2
        y = 0.000000005
        liczba = 3
        znak = 1

        wyniki = []
        while True:
            z = math.pow(xrad, n) / math.factorial(n)
            b = z * znak
            wyniki.append(round(b, 10))

            if liczba == 9:
                break

            n += 2
            liczba += 2
            znak *= -1

        suma_wynikow = sum(wyniki)
        final = 1 - suma_wynikow
        print(f"COSα:{stopnie}° = {final:.10f}")

    elif rodzaj_tryg == "TG":
        stopnie_TG = float(input("Stopnie:"))

        pi = 3.14159
        xrad = stopnie_TG * pi / 180

        # szereg taylora
        n = 3
        y = 0.000000005
        liczba = 3
        znak = 1

        wyniki = []
        while True:
            z = math.pow(xrad, n) / math.factorial(n)
            b = z * znak
            wyniki.append(round(b, 10))

            if liczba == 9:
                break

            n += 2
            liczba += 2
            znak *= -1

        suma_wynikow = sum(wyniki)
        SIN = xrad - suma_wynikow

        # Obliczanie radianów
        pi = 3.14159
        xrad = stopnie_TG * pi / 180


        # szereg taylora
        n = 2
        y = 0.000000005
        liczba = 3
        znak = 1

        wyniki = []
        while True:
            z = math.pow(xrad, n) / math.factorial(n)
            b = z * znak
            wyniki.append(round(b, 10))

            if liczba == 9:
                break

            n += 2
            liczba += 2
            znak *= -1

        suma_wynikow = sum(wyniki)
        COS = 1 - suma_wynikow

        TG = SIN/COS
        print(f"TGα:{stopnie_TG}° = {TG:.10f}")

    elif rodzaj_tryg == "CTG":
        stopnie_CTG = float(input("Stopnie:"))

        pi = 3.14159
        xrad = stopnie_CTG * pi / 180

        # szereg taylora
        n = 3
        y = 0.000000005
        liczba = 3
        znak = 1

        wyniki = []
        while True:
            z = math.pow(xrad, n) / math.factorial(n)
            b = z * znak
            wyniki.append(round(b, 10))

            if liczba == 9:
                break

            n += 2
            liczba += 2
            znak *= -1

        suma_wynikow = sum(wyniki)
        SIN = xrad - suma_wynikow

        # Obliczanie radianów
        pi = 3.14159
        xrad = stopnie_CTG * pi / 180

        # szereg taylora
        n = 2
        y = 0.000000005
        liczba = 3
        znak = 1

        wyniki = []
        while True:
            z = math.pow(xrad, n) / math.factorial(n)
            b = z * znak
            wyniki.append(round(b, 10))

            if liczba == 9:
                break

            n += 2
            liczba += 2
            znak *= -1

        suma_wynikow = sum(wyniki)
        COS = 1 - suma_wynikow

        CTG = COS / SIN
        print(f"TGα:{stopnie_CTG}° = {CTG:.10f}")
from sympy import symbols
from sympy.matrices import Matrix

def kalkulator_analityczny():
    #macierze







def menu():
    wybor = input("Wybierz kalkulator \"P\" / \"Z\" / \"PRO\" / \"TRYG\" | \"ANALIT\":").upper()
    if wybor == "P":
        kalkulator_podstawowy()
    elif wybor == "Z":
        kalkulator_zaawansowany()
    elif wybor == "PRO":
        kalkulaotr_profesjonalny()
    elif wybor == "TRYG":
        kalkulator_trygonometryczny()
    elif wybor == "ANALIT":
        kalkulator_analityczny()
    else:
        print("Nie ma podanego kalkulatora")


menu()
