g = {
    'А': 'БЖ',
    'Б': 'ВЗ',
    'В': 'Г',
    'Ж': 'З',
    'З': 'АВ',
    'К': 'Е',
    'И': 'А',
    'Е': 'ИА',
    'Д': 'КЕАЖ',
    'Г': 'ЗЖД',
}


def f(s, p):
    if len(p) > 1 and p[0] == p[-1]:
        return 1
    if len(p) != len(set(p)):
        return 0
    return sum([f(x, p + x) for x in g[s]])


print(f('З', 'З'))
