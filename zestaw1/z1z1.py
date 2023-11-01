# Napisać program, który czyta podane jako zewnętrzne argumenty liczby naturalne, a następnie każdą rozkłada na czynniki pierwsze (co polega na zapisaniu dowolnej liczby naturalnej za pomocą iloczynu liczb pierwszych). Wymagany jest format wyjściowy w postaci a1^k1*a2^k2*…*a3, jeśli ki==1 to opuszczamy wykładnik potęgi. Przykładowo, jeśli wywołamy:
# zadanie1.py 4407 13041599400
# to powinno się wypisać (proszę tak to sformatować):
# 4407 = 3*13*113 13041599400 = 2^3*3^4*5^2*805037
# Do wczytania zewnętrznych argumentów proponuję na początek coś bardzo podobnego do tego, co jest w języku C++, czyli użycie listy argumentów (bez używania getopt czy argparse):
# import sys # importujemy modul
# argv = sys.argv[1:] # argv to lista, a 1: robi selekcje bez pierwszego argumentu – nazwy programu
# for i in range(1,len(argv)): # za pomoca generatora
# print(int(sys.argv[i])) # wpisujemy, rzutowanie z typu str na int przyda sie potem

import sys
from math import sqrt

argv = sys.argv[:]
for i in range(1, len(argv)):
    n = int(sys.argv[i])
    print(n, "=", end=" ")
    sq = int(sqrt(n))
    k = 2
    counter = 1
    prev = 0
    while n > 1 and k <= sq:
        while n % k == 0:
            if prev != k:
                if counter > 1:
                    print('^', counter, end="*", sep="")
                else:
                    if prev != 0:
                        print("*", end="")
                counter = 1
                print(k, end='')
                prev = k
            else:
                counter += 1
            n /= k
        k = k+1
    if counter > 1:
        print("^", counter, end="*", sep="")
    else:
        if prev != 0:
            print("*", end="")

    if n > 1:
        print(int(n), end="")
    print()
