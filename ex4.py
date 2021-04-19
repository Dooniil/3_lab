class StringFormatter:
    def __init__(self, string, split_let=' '):
        self.__string = string
        self.__split_let = split_let
        self.__splitted = string.split(split_let)

    @property
    def string(self):
        return self.__string

    def del_less(self, n):
        for i, word in enumerate(self.__splitted):
            if len(word) < n:
                self.__splitted.pop(i)
        self.__string = ' '.join(self.__splitted)

    def change_num(self):
        for i, sym in enumerate(self.__string):
            if sym.isdigit():
                self.__string = self.__string.replace(self.__string[i], '*')
        
    def set_spaces(self):
        string = ''.join(self.__splitted)
        self.__string = ' '.join(string)

    def sort_by_len(self):
        self.__splitted.sort(key=lambda x: len(x))
        self.__string = ' '.join(self.__splitted)

    def sort_by_alph(self):
        self.__splitted.sort(key=lambda x: x[0])
        self.__string = ' '.join(self.__splitted)

string = StringFormatter('my name is Daniil')
string.del_less(3)
print(string.string)
string2 = StringFormatter('my name is3242 234domen')
string2.change_num()
print(string2.string)
string3 = StringFormatter('my name is Daniil')
string3.set_spaces()
print(string3.string)
string4 = StringFormatter('my name is Daniil')
string4.sort_by_len()
print(string4.string)
string4.sort_by_alph()
print(string4.string)

