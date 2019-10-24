#!/usr/bin/env python3
from liprip.gens import field
from librip.gens import gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Кресло', 'price': 5000, 'color': 'grey'},
    {'title': 'Книжная полка', 'price': 1200, 'color': 'brown'}
]

# Реализация задания 1
# str(...)[1:-1] - срез нач. с индекса 1 по -1 не включая его (убираем [])
print(str(list(field(goods, 'title', 'price')))[1:-1])
print(str(list(gen_random(1, 4, 10)))[1:-1])
