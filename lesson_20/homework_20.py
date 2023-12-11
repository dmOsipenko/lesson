# 􏰁еализуйте итератор колоды карт (52 штуки) CardDeck.
# Каждая карта представлена в виде строки типа «2 􏰂ик».
# 􏰂ри вызове функции next() будет представлена следующая карта.
# 􏰂о окончании перебора всех элементов возникнет ошибка StopIteration.


#ВАРИАНТ 1
class CardDeck:

    def __init__(self):
        self.card_desk = []
        for card in list(range(2, 11)) + ['B', 'D', 'K', 'T']:
            for suits in ['♦️', '♠️', '♥️', '♣️']:
                self.card_desk.append(str(card) + suits)
        self.index = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.card_desk):
            raise StopIteration
        else:
            card = self.card_desk[self.index]
            self.index += 1
            return card

deck = CardDeck()
for card in deck:
    print(card)

#ВАРИАНТ 2
# card_desk = []
#
# for card in list(range(2, 11)) + ['B', 'D', 'K', 'T']:
#     for suits in ['♦️', '♠️', '♥️', '♣️']:
#         card_desk.append(str(card) + suits)
#
# card_deck = (i for i in card_desk)
# while True:
#     try:
#         print(next(card_deck))
#     except StopIteration:
#         print(f'Калода закончилась')
#         break
