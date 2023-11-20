tup = tuple(i for i in range(0,10))
print(sum(tup))

long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
set_word = set(long_word)
for i in set_word:
    print(f'{i} - {long_word.count(i)}')


week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))
