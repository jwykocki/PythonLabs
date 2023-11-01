# Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z
# kilku cyfr(ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string,
# a potem go wypisać.
import sys

n = sys.argv[1]
n = int(n)

if n < 0 or n > 99:
    print("Give the number between 0 and 99")
    exit(1)

s = "|"
for i in range(0, n):
    s += "....|"
s += "\n"
s += "0"
i = 1
while i <= n:
    s += " " * 3
    if i < 10:
        s += " "
    s += str(i)
    i += 1

print(s)
