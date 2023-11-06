# Mamy trzy liczby całkowite, x, y, z reprezentujące wymiary prostopadłościanu, oraz pewną liczbę naturalną n.
# Wypisz listę wszystkich możliwych współrzędnych (i, j, k) na trójwymiarowej siatce, gdzie i+j+k nie jest równe n.
# Warunki: 0 ≤ i ≤ x, 0 ≤ j ≤ y, 0 ≤ k ≤ z. Rozwiązanie zapisz w postaci list składanych (list comprehesion), ale można
# zacząć od zagnieżdżonych pętli. Przykład. Niech x = 1, y = 1, z = 2, n = 3. Lista wszystkich permutacji trójek [i, j, k]
# w tym przykładzie: [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], [1,0,0], [1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2]].
# Elementy, które nie sumują się do 3 to: [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2]].
# Parametry x, y, z, n wczytać na początku za pomocą funkcji input().


a, b, c, d = map(int, input("Podaj x, y, z i n oddzielone spacją: ").split())


def f(x, y, z, n):
    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    return result


print(f(a, b, c, d))

# quick tests

test_result = f(1, 1, 2, 3)
expected = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
if test_result != expected:
    print("ERROR")
