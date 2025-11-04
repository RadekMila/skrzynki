import math

# Obliczanie radianów
pi = 3.14159
stopnie = float(input("Stopnie:"))
xrad = stopnie * pi / 180
print(xrad)

# szereg taylora
n = 3
y = 0.000000005
liczba = 3
znak = 1
print("3")
while True:
        z = math.pow(xrad, n) / math.factorial(n)
        b = z * znak

        print(f"{b:.{liczba}f}")
        if liczba == 9:
            break

        n += 2
        liczba += 2
        znak *= -1
        print(n)

