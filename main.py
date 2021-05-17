from random import *


def main():
    stats = {'ходы': 30, 'металл': 0, 'алюминий': 0, 'фотоэлемент': 0, 'зонд': 0, 'жизнеобеспечение': 1, 'двигатель': 1,
             'связь': 0, 'навигация': 0, 'ремонт': 0, 'корпус': 0}
    # тут предисловие
    # правила
    # совет: первым делом жизнеобеспечение
    statistics(stats)
    input()
    stats['ходы'] -= 1
    turn(stats)


def statistics(stats):
    print('+{:-^79s}+{:19s}+{:-^19s}+'.format('Склад', '', 'Жизнеобеспечение'))
    print('|{:19s}|{:19s}|{:19s}|{:19s}|{:19s}|{:19s}|'.format(' Металл: ' + str(stats['металл']),
                                                               ' Алюминий: ' + str(stats['алюминий']),
                                                               ' Фотоэлементы: ' + str(stats['фотоэлемент']),
                                                               ' Зонды: ' + str(stats['зонд']), '',
                                                               'Ходов доступно: ' + str(stats['ходы'])))
    print('+{:-^79s}+{:19s}+{:-^19s}+'.format('', '', ''))
    print('+{:-^119}+'.format('Системы корабля'))
    ship = list(stats.values())[5:]
    state = []
    for x in ship:
        if x == 1:
            state.append('стабильно')
        else:
            state.append('в критическом состоянии')
    print('|{:<119}|'.format(' Система жизнеобеспечения: ' + state[0]))
    print('|{:<119}|'.format(' Двигательный отсек: ' + state[1]))
    print('|{:<119}|'.format(' Система связи: ' + state[2]))
    print('|{:<119}|'.format(' Система навигации: ' + state[3]))
    print('|{:<119}|'.format(' Ремонтный отсек: ' + state[4]))
    print('|{:<119}|'.format(' Корпус: ' + state[5]))
    print('+{:-^119}+'.format(''))


def turn(stats):
    if stats['ходы'] <= 0:
        print('game over')
        exit()
    elif stats['жизнеобеспечение'] and stats['двигатель'] and stats['связь'] and stats['навигация'] and \
            stats['ремонт'] and stats['корпус']:
        print('you won')
        exit()
    events = {0: meteorite_collision}
    stats = events[randint(0, len(events) - 1)](stats)
    if stats['жизнеобеспечение']:
        stats['ходы'] -= 1
    else:
        stats['ходы'] -= 2
    stats = dial(stats)
    turn(stats)


def dial(stats):
    if not stats['жизнеобеспечение']:
        print('Внимание! Повреждена система жизнеобеспечения, количество доступных ходов сокращается в два раза быстрее.'
              ' Рекомендуется задействовать ремонтный отсек.')
    i = input('''1. Следующий ход\n2. Ремонтный отсек\n''')
    if i == '1':
        return stats
    elif i == '2':
        return stats
    else:
        print('Ошибка ввода. Попробуйте еще раз.')
        dial(stats)


def meteorite_collision(stats):
    enabled = []
    for key in list(stats.keys())[5:-1]:
        if stats[key]:
            enabled.append(key)
    if stats['корпус']:
        stats['корпус'] = 0
        print('\nКорабль столкнулся с метеоритом. Поврежден корпус, остальные системы остались нетронутыми.\n')
    elif enabled:
        systems = {'жизнеобеспечение': 'Повреждена система жизнеобеспечения.',
                   'двигатель': 'Поврежден двигательный отсек.',
                   'связь': 'Повреждена система связи', 'навигация': 'Повреждена система навигации.',
                   'ремонт': 'Поврежден ремонтный отсек.'}
        broken = choice(enabled)
        stats[broken] = 0
        print('\nКорабль столкнулся с метеоритом.', systems[broken], '\n')
    else:
        print('\nКорабль столкнулся с метеоритом. Все системы находятся в критическом состоянии.\n')
    statistics(stats)
    return stats




main()
