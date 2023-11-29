# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class Result:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        glas_letter = str()
        sogl_letter = str()
        numbers = 0
        const = 'aeiouy'
        if type(self.value) == str:
            for item in str(self.value).lower().strip().replace(' ',''):
                if item in const:
                    glas_letter += item
                else:
                    sogl_letter += item
            res = len(glas_letter) * len(sogl_letter)

            if res <= self.len_value(self.value):
                print(f'Гласные: {glas_letter}')
            else:
                print(f'Согласные: {sogl_letter}')
        elif type(self.value) == int:
            str_int = str(self.value)
            for item in str_int:
                if int(item) % 2 == 0:
                    numbers += int(item)
            print(numbers * self.len_value(str(self.value)))


    def len_value(self, v):
        len_v = len(v)
        return len_v


result = Result('Hello  oooo')
result.get_value()

result_2 = Result(432)
result_2.get_value()