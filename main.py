from random import *
import string


def main():
    stats = {'ходы': 20, 'металл': 2, 'алюминий': 2, 'фотоэлемент': 2, 'зонд': 5, 'жизнеобеспечение': 0, 'двигатель': 0,
             'связь': 0, 'навигация': 0, 'ремонт': 0, 'корпус': 0}
    stats_dop = {'жизнеобеспечение': 0, 'двигатель': 0, 'связь': 0, 'навигация': 0, 'ремонт': 0, 'корпус': 0}
    # тут предисловие
    stability_1 = choice(list(stats_dop.keys()))
    stats_dop.pop(stability_1)
    stability_2 = choice(list(stats_dop.keys()))
    stats[stability_1] = 1
    stats[stability_2] = 1
    statistics(stats)
    input()
    turn(stats)


def statistics(stats):
    if stats['ходы'] < 0:
        stats['ходы'] = 0
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
    events = {0: planet,
              1: planet,
              2: meteorite_collision,
              3: space_debris,
              4: electromagnetic_radiation,
              5: water,
              6: cellular_system,
              7: help,
              9: pirate,
              10: exchange,
              11: engine}
    stats = events[randint(0, len(events) - 1)](stats)
    if stats['жизнеобеспечение']:
        stats['ходы'] -= 1
    else:
        stats['ходы'] -= 2
    statistics(stats)
    if stats['ходы'] <= 0:
        print('game over')
        exit()
    dial(stats)
    if stats['жизнеобеспечение'] and stats['двигатель'] and stats['связь'] and stats['навигация'] and \
            stats['ремонт'] and stats['корпус']:
        print('you won')
        exit()
    turn(stats)


def dial(stats):
    if not stats['жизнеобеспечение']:
        print('Повреждена система жизнеобеспечения, количество доступных ходов сокращается в два раза быстрее.')
    if stats['ходы'] < 5:
        print('Ресурсы системы жизнеобеспечения на исходе.')
    i = input('''1. Следующий ход\n2. Ремонтный отсек\n''')
    if i == '1':
        return stats
    elif i == '2':
        stats = repair(stats)
        return dial(stats)
    else:
        print('Ошибка ввода. Попробуйте еще раз.')
        return dial(stats)


def repair(stats):
    a = input('\nВыберите одно из действий:\n1. Починить систему корабля \n2. Собрать зонд\n3. Выход\n')
    if a == '1':
        ship = ['жизнеобеспечение', 'двигатель', 'связь', 'навигация', 'ремонт', 'корпус']
        price = {'жизнеобеспечение': [1, 1, 1],
                 'двигатель': [3, 3, 0],
                 'связь': [0, 2, 0],
                 'навигация': [2, 2, 1],
                 'ремонт': [4, 3, 0],
                 'корпус': [4, 0, 0]}
        statistics(stats)
        print('+{:-^59s}+'.format('Стоимость ремонта систем'), '\n',
              '|{:^20s}|{:^12s}|{:^12s}|{:^12s}|'.format('Система', 'Металл', 'Алюминий', 'Фотоэлементы'), '\n', '+',
              '-' * 59, '+', sep='')
        i = 1
        for item in ship:
            print('|{:20s}|{:^12d}|{:^12d}|{:^12d}|'.format(str(i) + '. ' + item.capitalize(), price[item][0],
                                                            price[item][1],
                                                            price[item][2]))
            i += 1
        print('-' * 61)
        n = input('Введите цифру системы, которую вы хотите отремонтировать, '
                  'либо введите пустую строку для выхода из ремонтного отсека.\n')
        if n == '':
            return repair(stats)
        n = int(n)
        if stats.get(ship[n - 1]) == 0:
            if price.get(ship[n - 1])[0] <= stats['металл'] and price.get(ship[n - 1])[1] <= stats['алюминий'] and \
                    price.get(ship[n - 1])[2] <= stats['фотоэлемент']:
                stats['металл'] -= price.get(ship[n - 1])[0]
                stats['алюминий'] -= price.get(ship[n - 1])[1]
                stats['фотоэлемент'] -= price.get(ship[n - 1])[2]
                stats[ship[n - 1]] = 1
                systems = {'жизнеобеспечение': 'систему жизнеобеспечения.', 'двигатель': 'двигательный отсек.',
                           'связь': 'систему связи', 'навигация': 'систему навигации.', 'ремонт': 'ремонтный отсек.',
                           'корпус': 'корпус.'}
                print('Вы починили', systems[ship[n - 1]])
                statistics(stats)
            else:
                print('Недостаточно средств. Попробуйте еще раз.')
                q = input('Введите любой символ для продолжения:\n')
        else:
            print('Эта часть корабля уже отремонтирована.')
            q = input('Введите любой символ для продолжения:\n')
            repair(stats)
        return stats
    elif a == '3':
        return stats
    elif a == '2':
        return assembling(stats)


def assembling(stats):
    allow = min(stats.get('алюминий'), stats.get('металл'), stats.get('фотоэлемент'))
    statistics(stats)
    print('Стоимость сборки одного зонда составляет: 1 металл, 1 алюминий, 1 фотоэлемент. ')
    if allow == 0:
        im = input('Недостаточно ресурсов для сборки хотя бы одного дрона. Для выхода введите любой символ.\n')
        return repair(stats)
    print('Введите количество собираемых зондов (доступно: ', allow, '). Для выхода введите пустую строку.', sep='')
    n = int(input())
    if n > allow:
        print('Недостаточно ресурсов для сборки ', n, ' зондов.')
        return assembling(stats)
    elif n <= allow:
        stats['алюминий'] -= n
        stats['металл'] -= n
        stats['фотоэлемент'] -= n
        stats['зонд'] += n
        return repair(stats)
    print('Ошибка ввода. Попробуйте еще раз.')
    return assembling(stats)


def meteorite_collision(stats):
    enabled = []
    for key in list(stats.keys())[5:-1]:
        if stats[key]:
            enabled.append(key)
    if stats['корпус']:
        stats['корпус'] = 0
        print('Корабль столкнулся с метеоритом. Поврежден корпус, остальные системы остались нетронутыми.\n')
    elif enabled:
        systems = {'жизнеобеспечение': 'Повреждена система жизнеобеспечения.',
                   'двигатель': 'Поврежден двигательный отсек.',
                   'связь': 'Повреждена система связи', 'навигация': 'Повреждена система навигации.',
                   'ремонт': 'Поврежден ремонтный отсек.'}
        broken = choice(enabled)
        stats[broken] = 0
        print('Корабль столкнулся с метеоритом.', systems[broken], '\n')
    else:
        print('Корабль столкнулся с метеоритом. Все системы находятся в критическом состоянии.\n')
    return stats


def space_debris(stats):
    resources = {'m1': 'Получен 1 металл', 'm2': 'Получено 2 металла', 'al0': '', 'al1': ', 1 алюминий', 'cell0': '',
                 'cell1': ', 1 фотоэлемент'}
    m, al, cell = randint(1, 2), randint(0, 1), randint(0, 1)
    print('Найдено скопление космического мусора. ', resources['m' + str(m)], resources['al' + str(al)],
          resources['cell' + str(cell)], '.\n', sep='')
    stats['металл'] += m
    stats['алюминий'] += al
    stats['фотоэлемент'] += cell
    return stats


def electromagnetic_radiation(stats):
    print('Корабль попал в зону действия аномально сильного электромагнитного излучения, контроль над кораблем был '
          'потерян. На перезапуск систем потрачено на один ход больше.\n')
    stats['ходы'] -= 1
    return stats


def water(stats):
    script = {0: 'На одной из планет системы найдена жидкая вода. Отфильтрованная, она может быть применена в пищу или '
                 'для получения кислорода.',
              1: 'В атмосфере одной из планет системы найдены скопления водяного пара.'
                 'Собранный конденсат пригоден в пищу или для получения кислорода.',
              2: 'Одна из планет системы на ' + str(randint(20, 70)) + '% состоит изо льда. Растопив его, вы '
                                                                       'вполне можете применить его в пищу или '
                                                                       'для получения кислорода.'}
    print(script[randint(0, 2)], 'Количество ходов увеличено на два.')
    stats['ходы'] += 2
    return stats


def cellular_system(stats):
    if stats['связь'] == 0:
        print('Помехи, создаваемые сломанной системой связи, привлекли лишнее внимание.')
        return pirate(stats)
    resources = {'m1': '1 металл', 'm2': '2 металла', 'al0': '', 'al1': ', 1 алюминий', 'cell0': '',
                 'cell1': ', 1 фотоэлемент'}
    m = randint(1, 2)
    al = randint(0, 1)
    cell = randint(0, 1)
    print('Система связи корабля получила сигнал от вышедшего из строя искусственного спутника. Разобрав его, вы '
          'получили ', resources['m' + str(m)], resources['al' + str(al)], resources['cell' + str(cell)], '.', sep='')
    stats['металл'] += m
    stats['алюминий'] += al
    stats['фотоэлемент'] += cell
    return stats


def help(stats):
    resources = {'cell1': 'Получен 1 фотоэлемент', 'cell2': 'Получено 2 фотоэлемента', 'al0': '',
                 'al1': ', 1 алюминий', 'm0': '', 'm1': ', 1 металл', 'm2': ', 2 металла'}
    cell, al, m = randint(1, 2), randint(0, 1), randint(0, 2)
    print('На планете ', str(name()), ' вы встретили расположенное к контакту поселение. ',
          resources['cell' + str(cell)], resources['al' + str(al)], resources['m' + str(m)], '.\n',
          'Полученная провизия увеличивает ваши запасы и дает 2 дополнительных хода.', sep='')
    stats['металл'] += m
    stats['алюминий'] += al
    stats['фотоэлемент'] += cell
    stats['ходы'] += 2
    return stats


def prode(stats):
    if stats['зонд'] > 0:
        stats['зонд'] -= 1
        t = randint(0, 2)
        if t == 0:
            t = input('''Произошла неудача, зонд потерян. Введите "1" для отправки еще одного зонда, либо любой 
            другой символ для выхода.''')
            if t == '1':
                return prode(stats)
            else:
                return planet_dial(stats)
        else:
            res = {'m1': '1 металл', 'm2': '2 металла', 'm3': '3 металла', 'al0': '', 'al1': ', 1 алюминий',
                         'al2': ', 2 алюминия', 'al3': ', 3 алюминия', 'cell0': '', 'cell1': ', 1 фотоэлемент',
                         'cell2': ', 2 фотоэлемента', 'cell3': ', 3 фотоэлемента'}
            m = randint(1, 3)
            al = randint(0, 3)
            cell = randint(0, 3)
            print('Вернувшийся из экспедиции зонд принес вам ', res['m'+str(m)], res['al'+str(al)],
                  res['cell'+str(cell)], '.', sep='')
            stats['алюминий'] += al
            stats['фотоэлемент'] += cell
            stats['металл'] += m
    else:
        print('У вас недостаточно зондов для запуска. Рекомендуется посетить ремонтный отсек.')
    return stats


def name():
    letters = string.ascii_uppercase
    rand_string = ''.join(sample(letters, 3))
    return 'NSU' + rand_string


def landing(stats):
    if stats['двигатель'] == 0:
        print('Отсек двигатель неисправен')
    else:
        t = randint(0, 2)
        if stats['навигация'] == 0:
            if stats['корпус'] == 0:
                stats['двигатель'] = 0
            else:
                stats['корпус'] = 0

        if t == 0:
            print('На планете пусто')
        else:
            stats['алюминий'] += randint(0, 3)
            stats['фотоэлемент'] += randint(0, 3)
            stats['металл'] += randint(1, 3)
    return stats


def planet(stats):
    object = {0: 'обнаружена планета ', 1: 'обнаружена карликовая планета ',
              2: 'обнаружен спутник '+str(name())+' планеты '}
    sc = randint(0, 2)
    planet_name = name()
    im_stats = stats.copy()
    im_stats['ходы'] -= 1
    statistics(im_stats)
    print('В этой системе ', object[sc], planet_name, ', ', sep='', end='')
    if sc == 2:
        print('на котором могут быть найдены ценные ресурсы.\n')
    else:
        print('на которой могут быть найдены ценные ресурсы.\n')
    return planet_dial(stats)


def planet_dial(stats):
    r = int(input('''Выберите действие, либо введите любой другой символ для выхода.
        1. Отправить зонд
        2. Высадиться на планету (не безопасно)'''))
    if r == 1:
        prode(stats)
    elif r == 2:
        landing(stats)
    return stats


def pirate(stats):
    al = randint(0, 2)
    met = randint(2, 3)
    pht = randint(0, 1)
    grab = {'al0': '', 'al1': ' 1 алюминий', 'al2': '2 алюминия', 'met2': '2 металла', 'met3': '3 металла', 'pht0': '',
            'pht1': '1 фотоэлемент'}
    if (stats['алюминий'] - al >= 0 and al > 0) or (stats['металл'] - met >= 0 and met > 0) or \
            (stats['фотоэлемент'] - pht >= 0 and pht > 0):
        print('На вас напали космические пираты. После нападения у вас украли:')
        if stats['алюминий'] - al >= 0 and al > 0:
            stats['алюминий'] -= al
            print(grab['al' + str(al)])
        elif stats['металл'] - met >= 0 and met > 0:
            stats['металл'] -= met
            print(grab['met' + str(met)])
        elif stats['фотоэлемент'] - pht >= 0 and pht > 0:
            stats['фотоэлемент'] -= pht
            print(grab['pht' + str(pht)])
    else:
        print('У вас нечего грабить. Пираты сжалились над вами и отдали вам 1 металл и 1 алюминий')
        stats['металл'] += met
        stats['алюминий'] += al
    return stats


def exchange(stats):
    print('Вы встретили торговца.Хотите с ним обменяться ресурсами?\n1. Да.\n2. Нет и выйти.')
    r = randint(1, 2)
    # 0 - алюминий за металл, 1 - металл за алюминий
    choice = {1: 'Обмен: 1 алюминий за 2 металла', 2: 'Обмен: 1 металл за 1 алюминий'}
    invent = {1: 'алюминия', 2: 'металла'}
    a = int(input('Введите значение:\n'))
    if a == 1:
        print(choice[r], 'Хотите обменяться?', '1. Обменяться.\n2. Нет и выйти.', sep='\n')
        b = int(input('Введите значение:\n'))
        if b == 1:
            if r == 1:
                allow = stats['металл'] // 2
                print('Введите количество алюминия. Доступно:', allow)
                n = int(input())
                if n <= allow:
                    stats['металл'] -= 2 * n
                    stats['алюминий'] += n
                    print('Инвентарь: алюминий', stats['алюминий'], 'металл', stats['металл'])
                else:
                    print('Недостаточно средств. Попробуйте еще раз.')
                    return exchange(stats)
            else:
                print('Введите количество металла. Доступно:', stats['алюминий'])
                n = int(input())
                if n <= stats['алюминий']:
                    stats['металл'] += n
                    stats['алюминий'] -= n
                    print('Инвентарь: алюминий', stats['алюминий'], 'металл', stats['металл'])
                else:
                    print('Недостаточно средств. Попробуйте еще раз.')
                    return exchange(stats)
        elif b == 2:
            return stats
        else:
            print('Неверно введено значение. Попробуйте заново.')
            return exchange(stats)
    elif a == 2:
        return stats
    else:
        print('Неверно введено значение. Попробуйте заново.')
        return exchange(stats)


def engine(stats):
    if stats['двигатель'] == 1:
        scripts = {1: 'Сломалась система охлаждения двигателя.', 2: 'Превышение нормы давления в двигателе.',
                   3: 'Корабль попал в магнитную бурю.', 4: 'Высокие нагрузки вывели двигатель из строя.'}
        print(scripts[randint(1, 4)], 'Двигательный отсек в критическом состоянии.')
        stats['двигатель'] = 0
        return stats
    print('Критическое состояние двигателя привело к его полному отказу. На перезапуск потрачен дополнительный ход.')
    stats['ход'] -= 1
    return stats


main()
