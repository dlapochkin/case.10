import random

stats = {'score': 1, 'treasury': 10, 'provisions': 10, 'land': 10, 'military': 2,
         'population': 5, 'distemper': 0, 'yield_coef': 0.1}


def move(stats):
    stats = incomes(stats)
    events = {}
    actions = random.randint(1, 5)
    events_copy = events.copy()
    move(stats)


def statistics(stats):
    '{:13s}{:22s}{:19s}'.format('Наименование', 'Температура плавления', 'Температура кипения')
    print('{:-^121s}'.format('Текущая статистика'))
    print('|{:^19s}|{:^19s}|{:^19s}|{:^19s}|{:^19s}|{:^19s}|'.format('Казна', 'Провизия',
                                                             'Пахотные земли', 'Народ', 'Военная сила', 'Смута'))
    print('{:-^121s}'.format(''))
    print('|{:^19d}|{:^19d}|{:^19d}|{:^19d}|{:^19d}|{:^19.0%}|'.format(stats['treasury'], stats['provisions'], stats['land'],
                                                             stats['population'], stats['military'], stats['distemper']))
    print('{:-^121s}'.format(''))


def incomes(stats):
    i = random.randint(0, 3)
    if i == 0:
        stats = up_harvest(stats)
    elif i == 1:
        stats = down_harvest(stats)
    else:
        stats = harvest(stats)
    stats['treasury'] += stats['population'] * 2
    statistics(stats)
    return stats


def harvest(stats):
    stats['provisions'] += int(stats['land'] * 10 * (1 + stats['yield_coef']))
    return stats


def up_harvest(stats):
    coef = random.randint(5, 20)
    print('Этот год выдался высокоурожайным. Получено на ', coef, '% больше продовольствия.', sep='')
    stats['provisions'] += int(stats['land'] * 10 * (1 + stats['yield_coef'] + coef / 100))
    return stats


def down_harvest(stats):
    coef = random.randint(5, 20)
    print('Этот год выдался низкоурожайным. Получено на ', coef, '% меньше продовольствия.', sep='')
    stats['provisions'] += int(stats['land'] * 10 * (1 + stats['yield_coef'] - coef / 100))
    return stats


move(stats)