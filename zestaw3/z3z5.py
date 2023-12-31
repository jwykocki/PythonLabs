# W ramach zapoznania się z klasami, proszę napisać klasę o nazwie Bug taką, żeby zawierała licznik wskazujący
# aktualną liczbę powołanych do życia obiektów, identyfikator (lokalną zmienną obiektu, do której przypiszemy
# aktualny powiększony licznik). Licznik powinien rosnąć wraz z wywołaniem __init__ oraz maleć z wywołaniem __del__
# (uwaga: współdzielony licznik będziemy używać w zapisie Bug.licznik). Proszę też zdefiniować __str__ wypisującą
# licznik i bieżące id. Proszę też napisać jakiś opisowy komentarz w klasie (w formie docstring). Finalnie, niech dla kodu:
# bugs = []
# for i in range(100):
# bugs.append(Bug())
# print(bugs[-1])
# wypisują się licznik, identyfikator, a przy niszczeniu obiektu w __del__ niech będzie też print informacji
# typu 'Koniec', licznik, identyfikator.

class Bug:
    """
    Klasa reprezentująca obiekty Bug.

    Każdy obiekt Bug ma swój unikalny identyfikator (lokalna zmienna),
    a także korzysta ze współdzielonego licznika obiektów klasy Bug.
    Licznik jest inkrementowany w __init__ i dekrementowany w __del__.
    """

    licznik = 0

    def __init__(self):
        Bug.licznik += 1
        self.identyfikator = Bug.licznik

    def __del__(self):
        Bug.licznik -= 1
        print(f'Koniec, Licznik: {Bug.licznik}, Identyfikator: {self.identyfikator}')

    def __str__(self):
        return f'Licznik: {Bug.licznik}, Identyfikator: {self.identyfikator}'


bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])
del bugs[-1]
print("Koniec programu")
