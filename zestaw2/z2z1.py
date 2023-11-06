# # Mamy zagnieżdżoną listę, która może zawierać różne heterogeniczne typy, na przykład inną listę,
# # ale również krotkę, słownik. Dodaj element o kolejnej wartości w najbardziej zagnieżdżonej liście.
# # Napisz program, który zrobi to uniwersalnie, dla dowolnego zagnieżdżenia, również jeśli pojawią się inne typy.
# # Dla [1 [2, 3] 4] chodzi o [1 [2, 3, 4] 4], dla [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7] powinno być
# # [3, 4, [2, [1, 2, [7, 8, 9], 3, 4], 3, 4], 5, 6, 7]. Jeżeli największe zagnieżdżenie na danym poziomie się powtórzy,
# # należy dodać w obu zagnieżdżeniach, czyli dla [1, [3], [2]] należy uzyskać [1, [3, 4], [2, 3]]. Przykład bardziej
# # złożony: list1 = [1, 2, [3, 4, [5, {'klucz': [5, 6], 'tekst': [1, 2]}], 5], 'hello', 3, [4, 5], (5, (6, (1, [7, 8])))].
# # Tutaj na takim samym, największym poziomie zagnieżdżenia, są listy będące wartościami w słowniku (listy [5, 6], [1, 2])
# # a także zagnieżdżona w krotkach (lista [7, 8]) i do to do nich powinien zostać dodany kolejny element. Zatem oczekiwane
# # jest: [1, 2, [3, 4, [5, {'klucz': [5, 6, 7], 'tekst': [1, 2, 3]}], 5], 'hello', 3, [4, 5, 6], (5, [6, [7, 8, 9]])].


def count_max_level(data):
    if isinstance(data, list):
        max_level = 0
        for element in data:
            level = count_max_level(element)
            if level > max_level:
                max_level = level
        return max_level + 1
    elif isinstance(data, dict):
        max = 0
        for key, value in data.items():
            new_max = count_max_level(value)
            if new_max > max:
                max = new_max
        return max
    elif isinstance(data, (tuple, map)):
        data = list(data)
        return count_max_level(data)
    else:
        return 0


def add_element_to_nested_list(data, level, max_level):
    if isinstance(data, list):
        # print("lvl: ", level, "data: ", data)
        for i in range(len(data)):
            if isinstance(data[i], dict):
                for key, value in data[i].items():
                    add_element_to_nested_list(value, level + 2, max_level)
            elif isinstance(data[i], list):
                add_element_to_nested_list(data[i], level + 1, max_level)
            elif isinstance(data[i], (tuple, map)):
                data[i] = list(data[i])
                add_element_to_nested_list(data[i], level + 1, max_level)
        if level == max_level:
            data.append(data[i] + 1)
    elif isinstance(data, dict):
        for key, value in data.items():
            add_element_to_nested_list(value, level + 2, max_level)
    elif isinstance(data, (tuple, map)):
        data = list(data)
        add_element_to_nested_list(data, level, max_level)
    return data


def count_max_level_and_add_element(data):
    max_level = count_max_level(data)
    return add_element_to_nested_list(data, 1, max_level)


# quick tests
list1 = [1, 2, [3, 4, [5, {'klucz': [5, 6], 'tekst': [1, 2]}], 5], 'hello', 3, [4, 5], (5, (6, (1, [7, 8])))]
expected_list1 = [1, 2, [3, 4, [5, {'klucz': [5, 6, 7], 'tekst': [1, 2, 3]}], 5], 'hello', 3, [4, 5], [5, [6, [1, [7, 8, 9]]]]]
if count_max_level_and_add_element(list1) != expected_list1:
    print("ERROR with list1")

list2 = [1, [2, 3], 4]
expected_list2 = [1, [2, 3, 4], 4]
if count_max_level_and_add_element(list2) != expected_list2:
    print("ERROR with list2")

list3 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
expected_list3 = [3, 4, [2, [1, 2, [7, 8, 9], 3, 4], 3, 4], 5, 6, 7]
if count_max_level_and_add_element(list3) != expected_list3:
    print("ERROR with list3")

list4 = [1, [3], [2]]
expected_list4 = [1, [3, 4], [2, 3]]
if count_max_level_and_add_element(list4) != expected_list4:
    print("ERROR with list4")


list5 = [1, 2, [3, 4, [5, {'klucz': 4, 'tekst': 1}], 5], 'hello', 3, [4, 5], (5, (6, (1, 8)))]
expected_list5 = [1, 2, [3, 4, [5, {'klucz': 4, 'tekst': 1}], 5], 'hello', 3, [4, 5], [5, [6, [1, 8, 9]]]]
if count_max_level_and_add_element(list5) != expected_list5:
    print("ERROR with list5")
