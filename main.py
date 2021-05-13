def main():
    score = 1
    stats = {'treasury': 10, 'provisions': 10, 'land': 10, 'military': 2,
             'population': 5, 'distemper': 0, 'yield_coef': 0.1}
    events = {}


def statistics(stats):
    '{:13s}{:22s}{:19s}'.format('Наименование', 'Температура плавления', 'Температура кипения')
    print('{:-^121s}'.format('Текущая статистика'))
    print('|{:^19s}|{:^19s}|{:^19s}|{:^19s}|{:^19s}|{:^19s}|'.format('Казна', 'Провизия',
                                                             'Пахотные земли', 'Народ', 'Военная сила', 'Смута'))
    print('{:-^121s}'.format(''))
    print('|{:^19d}|{:^19d}|{:^19d}|{:^19d}|{:^19d}|{:^19.0%}|'.format(stats['treasury'], stats['provisions'], stats['land'],
                                                             stats['population'], stats['military'], stats['distemper']))
    print('{:-^121s}'.format(''))