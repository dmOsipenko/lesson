
# Есть массив состоящий из слов и чисел, нужно записать в файл сначала слова в порядке их длины,
# а после слов цифры в порядке возрастания

lst = ['Dmitry',31,1992,'Osipenko','Rainisa',5,46]

lst_str = []
lst_int = []

for item in lst:
    if isinstance(item,str):
        lst_str.append(item)
        lst_str.sort(key=lambda x: len(x.strip()))
    else:
        lst_int.append(str(item))
        lst_int.sort(key= int)

with open('array','w') as file:
    file.write(f"{' '.join(lst_str).strip()}\n")
    file.write(' '.join(lst_int).strip())
