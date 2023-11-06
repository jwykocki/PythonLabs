# Dla dowolnego podanego łańcucha znakowego wypisać: ile jest w nim słów (poprzez słowo rozumiemy
# ciąg co najmniej jednego znaku innego niż znak przestankowy, dla uproszczenia przyjmijmy, że liczymy
# a-z, A-Z i 0-9 jako coś, co składa się na słowa), ile liter, ile cyfr, oraz wypisać statystykę częstości
# występowania poszczególnych liter oraz cyfr.


def text_analyse(text):
    words_amount = 0
    letters_amount = 0
    digits_amount = 0
    letters_frequency = {}
    digits_frequency = {}
    was_previous_punctuation = True
    for character in text:
        if character.isalpha():
            if was_previous_punctuation:
                words_amount += 1
            was_previous_punctuation = False
            if character in letters_frequency:
                letters_frequency[character] += 1
            else:
                letters_frequency[character] = 1
            letters_amount += 1
        elif character.isnumeric():
            if was_previous_punctuation:
                words_amount += 1
            was_previous_punctuation = False
            digits_amount += 1
            if character in digits_frequency:
                digits_frequency[character] += 1
            else:
                digits_frequency[character] = 1
        else:
            was_previous_punctuation = True
    print("Ilość słów:", words_amount)
    print("Ilość liter:", letters_amount)
    print("Ilość cyfr:", digits_amount)
    print("Częstość występowania liter:")
    for letter, amount in letters_frequency.items():
        print(f"{letter}: {amount}")
    print("Częstość występowania cyfr:")
    for digit, amount in digits_frequency.items():
        print(f"{digit}: {amount}")


# quick tests


text_analyse("AlA ma, k0t4 i 3 p5s4! su.per")  # w:8 l:15 d:5
