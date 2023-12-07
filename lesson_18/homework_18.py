import string


class Alphabet:

    def __init__(self, lang, letters):
        self.letters = list(letters)
        self.lang = lang

    def print(self):
        print(self.letters)

    def letters_num(self):
         len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = 0
    def __init__(self):
        super().__init__('En', string.ascii_letters)

    def is_en_letter(self, char):
        if type(char) == str:
            if str(char).upper() in self.letters:
                return True
            else:
                return False

    def letters_num(self):
        return self.__letters_num
    @staticmethod
    def example():
        print(f'Some text in English ...')

eng = EngAlphabet()
eng.print()
print(eng.letters_num())
eng.example()


class Tomato:
    states = {
        0: 'зеленый',
        1: 'Почти созрел',
        2: 'Можно кушать'
    }

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        if self._state != self.states[2]:
            current_index = list(self.states.values()).index(self._state)
            self._state = self.states[current_index + 1]
            return self._state

    def is_ripe(self):
        return self._state == self.states[2]


class TomatoBush:
    def __init__(self, count_tomato):
        self.tomatoes = [Tomato(i) for i in range(count_tomato)]

    def grow_all(self):
        for item in self.tomatoes:
            return item.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            return tomato.is_ripe()

    def give_away_all(self):
        self.tomatoes.clear()
        print(f'Список пуст {self.tomatoes}')

class Gardener:
    def __init__(self, name, plant: Tomato):
        self.name = name
        self._plant = plant

    def work(self):
        return self._plant.grow()

    def harvest(self):
       if self._plant.is_ripe():

           return print(f'Помидоры созрели. Можно собирать!')
       else:
           return print(f'Помидоры еше не созрели!!!!')
    @staticmethod
    def knowledge_base():
        print(f'Справка по садоводству')

Gardener.knowledge_base()
gardener = Gardener('Dima', Tomato(1))
bush = TomatoBush(1)

print(gardener.work())
gardener.harvest()
print(gardener.work())
gardener.harvest()
