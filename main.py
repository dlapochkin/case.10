from random import *


def main():
    stats = {'ходы': 0, 'металл': 0, 'алюминий': 0, 'фотоэлемент': 0, 'зонд': 0, 'жизнеобеспечение': 0, 'двигатель': 0,
             'связь': 0, 'навигация': 0, 'ремонт': 0, 'броня': 1}
    print('все плохо')
    #тут предисловие
    #правила
    #совет: первым делом жизнеобеспечение
    statistics(stats)
    wait = input()
    print('')
    stats['ходы'] += 1
    move(stats)


def statistics(stats):
    print('{:-^81s}{:19s}{:-^21s}'.format('Склад', '', 'Жизнеобеспечение'))
    print('|{:19s}|{:19s}|{:19s}|{:19s}|{:19s}|{:19s}|'.format(' Металл: '+str(stats['металл']),
                                                               ' Алюминий: '+str(stats['алюминий']),
                                                               ' Фотоэлементы: '+str(stats['фотоэлемент']),
                                                               ' Зонды: '+str(stats['зонд']), '',
                                                               ' Ходов доступно: '+str(stats['ходы'])))
    print('{:-^81s}{:19s}{:-^21s}'.format('', '', ''))
    print('{:-^121}'.format('Системы корабля'))
    ship = list(stats.values())[5:]
    state = []
    for x in ship:
        if x == 1:
            state.append('стабильно')
        else:
            state.append('в критическом состоянии')
    print('|{:<119}|'.format(' Система жизнеобеспечения: '+state[0]))
    print('|{:<119}|'.format(' Двигательный отсек: ' + state[1]))
    print('|{:<119}|'.format(' Система связи: ' + state[2]))
    print('|{:<119}|'.format(' Система навигации: ' + state[3]))
    print('|{:<119}|'.format(' Ремонтный отсек: ' + state[4]))
    print('|{:<119}|'.format(' Корпус: ' + state[5]))
    print('{:-^121}'.format(''))



def move(stats):
    if stats['ходы'] == 0:
        print('game over')
    elif stats['жизнеобеспечение'] == stats['двигатель'] == stats['связь'] == stats['навигация'] == stats['ремонт'] == stats['броня'] == 1:
        print('you won')
    events = {}
    stats = events[randint(0, len(events) - 1)](stats)




main()