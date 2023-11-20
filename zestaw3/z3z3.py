# Python jest językiem, w którym przy użyciu kodu o niewielkiej długości, ale z umiejętnym użyciem bibliotek,
# da się osiągnąć interesujące wyniki. Wymaga to jednak zapoznania się z możliwościami różnych bibliotek,
# celem tego zadania jest właśnie podstawowe użycie biblioteki do rysowania (matplotlib) oraz biblioteki numpy.
# Zadanie: napisać prosty i zwięzły program, który pozwoli na wczytanie wielomianu funkcji f(x) jako danej wejściowej
# (łańcuch znakowy) oraz przedział x (od – x_min, do – x_max). Cel: narysować ten wielomian za pomocą plt.plot(x_val, y_val)
# (gdzie x_val i y_val to będą, odpowiednio, tablica wygenerowana za pomocą x_val = np.linspace(x_min, x_max, 200),
# a tablica y_val wyliczona z użyciem funkcji eval dla wartości z tablicy x_val.

import numpy as np
import matplotlib.pyplot as plt

def plot_polynomial(equation, x_min, x_max):
    x_val = np.linspace(x_min, x_max, 200)
    y_val = [eval(equation) for x in x_val]

    plt.plot(x_val, y_val, label=equation)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Wykres wielomianu: ' + equation)
    plt.grid(True)
    plt.legend()
    plt.show()


equation = input("Podaj wielomian f(x): ")
x_min = float(input("Podaj x_min: "))
x_max = float(input("Podaj x_max: "))

plot_polynomial(equation, x_min, x_max)
