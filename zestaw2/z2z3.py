import re
import json


def convert_roman_to_arabic(roman_numerals):
    roman_to_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'M': 1000}
    if not (bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman_numerals))):
        return

    arabic = 0
    for i in range(len(roman_numerals)):
        if i > 0 and roman_to_arabic[roman_numerals[i]] > roman_to_arabic[roman_numerals[i - 1]]:
            arabic += roman_to_arabic[roman_numerals[i]] - 2 * roman_to_arabic[roman_numerals[i - 1]]
        else:
            arabic += roman_to_arabic[roman_numerals[i]]
    return arabic


# quick tests


def convert_to_dictionary_string(text):
    text2 = '{\"' + text.replace(' (', "\":").replace(',', ", \"").replace(')', '') + '}'
    return text2


# from: https://catonmat.net/tools/generate-random-roman-numerals
roman_examples = "MLXXXIII (1083),MMMXXXVII (3037),MMLXXXVII (2087),CCLXVIII (268),MMMDXXI (3521),DCCIX (709)," \
                 "MDCLXVI (1666),MDCCXXXIV (1734),MMCMXXX (2930),MMCCXXIII (2223),MMMCCCI (3301),MMMDCLXIV (3664)," \
                 "MMMDCXIII (3613),DCCXXXVII (737),CMXCI (991),MMCDLXXI (2471),VI (6),MMMCCCXXI (3321),DCV (605)," \
                 "MMCMLVI (2956)"
result = json.loads(convert_to_dictionary_string(roman_examples))

for key in result:
    if result[key] != convert_roman_to_arabic(key):
        print("Error : ", key)
        break

roman_bad_examples = {"MLM", "IIII", "M1", "IIV", "MMM."}

for example in roman_bad_examples:
    if convert_roman_to_arabic(example) is not None:
        print("Error : ", example)
        break
