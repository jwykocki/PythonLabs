# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right
# włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną
# [Zad. 4.5  https://ufkapano.github.io/algorytmy/lekcja04/zadania.html].

def iterative_inversion(L, left, right):
    if left < 0 or right >= len(L) or left > right:
        return
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def recursive_inversion(L, left, right):
    if left < 0 or right >= len(L) or left > right:
        return

    if left < right:
        L[left], L[right] = L[right], L[left]
        recursive_inversion(L, left + 1, right - 1)


lista = [1, 2, 3, 4, 5, 6, 7]
lista2 = lista.copy()
iterative_inversion(lista, 2, 5)
recursive_inversion(lista2, 2, 5)
print(lista)
print(lista2)
