
text = input(f'Введите текст: ')
count = len(text)
print(text[2])
print(text[-2])
if count >= 5:
    print(text[:5])
print(text[:-2])
print(text[1::2])
print(text[2::2])
print(text[::-1])
print(text[-1::-2])
print(count)