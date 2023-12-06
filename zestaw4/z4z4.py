# Dynamiczny charakter języka Python nie pozwala na bezpośrednie przeładowywanie funkcji o tych
# samych nazwach, ale różnych argumentach. Z pomocą dekoratorów pojawiają się w język techniki emulujące takie
# zachowania. W ramach zadania proszę przestudiować materiał na temat singledispatch oraz singledispatchmethod z
# modułu functools oraz napisać dowolny kod ilustrujący te przypadki (inny niż w podanej dokumentacji)
#  https://docs.python.org/3/library/functools.html#functools.singledispatch
from functools import singledispatchmethod

class DataProcessor:
    @singledispatchmethod
    def process(self, data):
        print(f"Processing generic data: {data}")

    @process.register(int)
    def process_int_data(self, data):
        print(f"Processing integer data: {data}")

    @process.register(str)
    def process_str_data(self, data):
        print(f"Processing string data: {data}")

    @process.register(list)
    def process_list_data(self, data):
        print(f"Processing list data: {data}")


processor = DataProcessor()
processor.process(42)
processor.process("Hello")
processor.process([1, 2, 3])
processor.process(3.14)         #nieokreslona dla float, dlatego funkcja domyslna
