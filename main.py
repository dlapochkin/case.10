"""
Case-study 10
Developers:
Кривошапова Д. Е.:40%
Кузнецов А. Д.: 40%
Лапочкин Д. А.: 50%
"""


from random import *
import string


def main():
    """
    Start of the game
    :return: None
    """
    stats = {'ходы': 20, 'металл': 2, 'алюминий': 1, 'фотоэлемент': 1, 'зонд': 3, 'жизнеобеспечение': 0, 'двигатель': 0,
             'связь': 0, 'навигация': 0, 'ремонт': 0, 'корпус': 0}
    stats_dop = {'жизнеобеспечение': 0, 'двигатель': 0, 'связь': 0, 'навигация': 0, 'ремонт': 0}
    print('Вы - один из членов космической экспедиции по исследованию системы NSU, некогда населенной людьми.\nПопав в '
          'аварию во время сверхскоростных передвижений, вы отклонились от курса и потеряли связь с командованием.'
          '\nТем не менее, вам удалось отправить сигнал о помощи, который, к сожалению, привлек внимание враждебно '
          'настроенных остатков цивилизации - космических пиратов.\nДрейфовать в открытом космосе, ожидая подмоги, вам '
          'не позволяет также ограниченность необходимых для жизни ресурсов, которых, по расчетам, хватит на',
          stats['ходы'], 'ходов.\nЕдинственный шанс на спасение - возможность починить все системы корабля и вновь '
                         'соединиться с экспедиционной командой.\n')
    print('Система жизнеобеспечения отвечает за поддержание вашей жизнедеятельности; при поломке '
          'количество доступных вам ходов сокращается в два раза быстрее.\nДвигательный отсек приводит корабль в '
          'движение, а также дает возможность приземляться на космические объекты.\nСистема связи не дает возможности '
          'связаться с командованием, в то же время ее нестабильная работа может привести к отрицательным '
          'последствиям.\nНавигационная система отвечает за ориентирование корабля в пространстве; поломка увеличивает '
          'шанс столкновения кораля с поверхностью при приземлении.\nРемонтный отсек позволяет вам ремонтировать '
          'остальные системы корабля (даже в критическом состоянии), а также собирать зонды.\nКорпус поглощает '
          'большинство полученного урона при столкновении, что уберегает остальные системы корабля от поломки.\n')
    stability_1 = choice(list(stats_dop.keys()))
    stats_dop.pop(stability_1)
    stability_2 = choice(list(stats_dop.keys()))
    stats[stability_1] = 1
    stats[stability_2] = 1
    statistics(stats)
    input('Для продолжения введите любой символ.')
    turn(stats)


def statistics(stats):
    """
    Prints the table with current state of the system
    :param stats: current state of the system elements
    :return: None
    """
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
    """
    Determines the end of the game
    :param stats: current state of the system elements
    :return: None
    """
    events = {0: planet,
              1: planet,
              2: meteorite_collision,
              3: space_debris,
              4: electromagnetic_radiation,
              5: water,
              6: cellular_system,
              7: people,
              8: pirate,
              9: exchange,
              10: engine}
    stats = events[randint(0, len(events) - 1)](stats)
    if stats['жизнеобеспечение']:
        stats['ходы'] -= 1
    else:
        stats['ходы'] -= 2
    if stats['ходы'] <= 0:
        print('\nК сожалению, необходимые для поддержания вашей жизни ресурсы иссякли. На этом моменте вы вынуждены '
              'закончить ваше путешествие.')
        exit()
    if stats['жизнеобеспечение'] and stats['двигатель'] and stats['связь'] and stats['навигация'] and \
            stats['ремонт'] and stats['корпус']:
        print('Починив корабль, вы успешно преодолеваете магнитный барьер, не позволявший связаться с командой. Теперь '
              'ваша эвакуация - лишь вопрос времени.')
        exit()
    statistics(stats)
    dial(stats)
    turn(stats)


def dial(stats):
    """
    Warns of an imminent end of the game
    :param stats: current state of system elements
    :return: new state of system elements
    """
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
    """
    Fixes the element of the system
    :param stats: current state of the system elements
    :return: new state of the system elements
    """
    a = input('Выберите одно из действий, либо введите любой другой символ для выхода:\n1. Починить систему корабля'
              '\n2. Собрать зонд\n')
    if a == '1':
        ship = ['жизнеобеспечение', 'двигатель', 'связь', 'навигация', 'ремонт', 'корпус']
        price = {'жизнеобеспечение': [1, 1, 1],
                 'двигатель': [2, 3, 0],
                 'связь': [1, 2, 1],
                 'навигация': [2, 2, 3],
                 'ремонт': [3, 3, 1],
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
                           'связь': 'систему связи.', 'навигация': 'систему навигации.', 'ремонт': 'ремонтный отсек.',
                           'корпус': 'корпус.'}
                print('Вы починили', systems[ship[n - 1]])
                statistics(stats)
            else:
                print('Недостаточно ресурсов для ремонта системы.')
                return repair(stats)
        else:
            print('Эта система корабля уже отремонтирована.')
            return repair(stats)
        return stats
    elif a == '2':
        return assembling(stats)
    return stats


def assembling(stats):
    """
    Creates a prode
    :param stats: current state of system elements
    :return: new state of system elements
    """
    allow = min(stats.get('алюминий'), stats.get('металл'), stats.get('фотоэлемент'))
    statistics(stats)
    if stats['ремонт'] == 0:
        print('К сожалению, ремонтный отсек не может собирать дроны, находясь в критическом состоянии.')
        return repair(stats)
    print('Стоимость сборки одного зонда составляет: 1 металл, 1 алюминий, 1 фотоэлемент. ')
    if allow == 0:
        print('Недостаточно ресурсов для сборки хотя бы одного дрона.\n')
        return repair(stats)
    print('Введите количество собираемых зондов (доступно: ', allow, '). Для выхода введите пустую строку.', sep='')
    n = int(input())
    if n > allow:
        print('Недостаточно ресурсов для сборки ', n, ' зондов.')
        return assembling(stats)
    elif allow >= n > 0:
        stats['алюминий'] -= n
        stats['металл'] -= n
        stats['фотоэлемент'] -= n
        stats['зонд'] += n
        if n == 1:
            print('Собран зонд.')
        if n >= 5:
            print('Собрано', n, 'зондов.')
        else:
            print('Собрано', n, 'зонда.')
        return repair(stats)
    print('Ошибка ввода. Попробуйте еще раз.')
    return assembling(stats)


def meteorite_collision(stats):
    """
    Reflects the impact of a random event
    :param stats: current state of the system
    :return: new state of the system
    """

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
    return stats


def space_debris(stats):
    """
        Reflects the impact of a random event
        :param stats: current state of the system
        :return: new state of the system
        """
    resources = {'m1': 'Получен 1 металл', 'm2': 'Получено 2 металла', 'al0': '', 'al1': ', 1 алюминий', 'cell0': '',
                 'cell1': ', 1 фотоэлемент'}
    m, al, cell = randint(1, 2), randint(0, 1), randint(0, 1)
    print('\nНайдено скопление космического мусора. ', resources['m' + str(m)], resources['al' + str(al)],
          resources['cell' + str(cell)], '.\n', sep='')
    stats['металл'] += m
    stats['алюминий'] += al
    stats['фотоэлемент'] += cell
    return stats


def electromagnetic_radiation(stats):
    """
        Reflects the impact of a random event
        :param stats: current state of the system
        :return: new state of the system
        """
    print('\nКорабль попал в зону действия аномально сильного электромагнитного излучения, контроль над кораблем был '
          'потерян. На перезапуск систем потрачено на один ход больше.\n')
    stats['ходы'] -= 1
    return stats


def water(stats):
    """
        Reflects the impact of a random event
        :param stats: current state of the system
        :return: new state of the system
        """
    script = {0: 'На одной из планет системы найдена жидкая вода. Отфильтрованная, она может быть применена в пищу или '
                 'для получения кислорода. ',
              1: 'В атмосфере одной из планет системы найдены скопления водяного пара. '
                 'Собранный конденсат пригоден в пищу или для получения кислорода. ',
              2: 'Одна из планет системы на ' + str(randint(20, 70)) + '% состоит изо льда. Растопив ледяные глыбы, вы '
                                                                       'вполне можете употребить воду в пищу или '
                                                                       'использовать ее для получения кислорода. '}
    print('\n', script[randint(0, 2)], 'Количество ходов увеличено на два.\n', sep='')
    stats['ходы'] += 2
    return stats


def cellular_system(stats):
    """
        Reflects the impact of a random event
        :param stats: current state of the system
        :return: new state of the system
        """
    if stats['связь'] == 0:
        print('\nПомехи, создаваемые сломанной системой связи, привлекли лишнее внимание.', end='')
        return pirate(stats)
    resources = {'m1': '1 металл', 'm2': '2 металла', 'al0': '', 'al1': ', 1 алюминий', 'cell0': '',
                 'cell1': ', 1 фотоэлемент'}
    m = randint(1, 2)
    al = randint(0, 1)
    cell = randint(0, 1)
    print('\nСистема связи корабля получила сигнал от вышедшего из строя искусственного спутника. Разобрав его, вы '
          'получили ', resources['m' + str(m)], resources['al' + str(al)], resources['cell' + str(cell)], '.\n', sep='')
    stats['металл'] += m
    stats['алюминий'] += al
    stats['фотоэлемент'] += cell
    return stats


def people(stats):
    """
    Reflects the impact of a random event
    :param stats: current state of the system
    :return: new state of the system
    """
    resources = {'cell1': 'Получен 1 фотоэлемент', 'cell2': 'Получено 2 фотоэлемента', 'al0': '',
                 'al1': ', 1 алюминий', 'm0': '', 'm1': ', 1 металл', 'm2': ', 2 металла'}
    cell, al, m = randint(1, 2), randint(0, 1), randint(0, 2)
    print('\nНа планете ', str(name()), ' вы встретили расположенное к контакту поселение. ',
          resources['cell' + str(cell)], resources['al' + str(al)], resources['m' + str(m)], '.\n',
          'Полученная провизия увеличивает ваши запасы и дает 2 дополнительных хода.\n', sep='')
    stats['металл'] += m
    stats['алюминий'] += al
    stats['фотоэлемент'] += cell
    stats['ходы'] += 2
    return stats


def prode(stats):
    """
        Reflects the impact of a prode launch
        :param stats: current state of the system
        :return: new state of the system
        """
    if stats['зонд'] > 0:
        stats['зонд'] -= 1
        t = randint(0, 2)
        if t == 0:
            t = input('Произошла неудача, зонд потерян. Введите "1" для отправки еще одного зонда, либо любой другой '
                      'символ для выхода.\n')
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
            print('\nВернувшийся из экспедиции зонд принес вам ', res['m'+str(m)], res['al'+str(al)],
                  res['cell'+str(cell)], '.\n', sep='')
            stats['алюминий'] += al
            stats['фотоэлемент'] += cell
            stats['металл'] += m
    else:
        print('У вас недостаточно зондов для запуска. Рекомендуется посетить ремонтный отсек.')
        return planet_dial(stats)
    return stats


def name():
    """
    Generates a random name
    :return: random name
    """
    letters = string.ascii_uppercase
    rand_string = ''.join(sample(letters, 3))
    return 'NSU-I' + rand_string


def landing(stats):
    """
        Reflects the impact of the landing on the planet
        :param stats: current state of the system
        :return: new state of the system
        """
    if stats['двигатель'] == 0:
        print('Двигательный отсек неисправен. Невозможно совершить посадку.')
        return planet_dial(stats)
    enabled = []
    for key in list(stats.keys())[5:]:
        if stats[key]:
            enabled.append(key)
    t = randint(0, 2)
    if stats['навигация'] == 0:
        if t == 0:
            i = 1
        else:
            i = 0
    else:
        if t != 0:
            i = 1
        else:
            i = 0
    if i == 0:
        systems = {'жизнеобеспечение': 'Повреждена система жизнеобеспечения.',
                   'двигатель': 'Поврежден двигательный отсек.', 'связь': 'Повреждена система связи.',
                   'навигация': 'Повреждена система навигации.', 'ремонт': 'Поврежден ремонтный отсек.',
                   'корпус': 'Поврежден корпус.'}
        if 'корпус' in enabled:
            broken = 'корпус'
        else:
            broken = choice(enabled)
        stats[broken] = 0
        print('Посадка оказалась неудачной.', systems[broken])
    else:
        res = {'m1': '1 металл', 'm2': '2 металла', 'm3': '3 металла', 'al0': '', 'al1': ', 1 алюминий',
               'al2': ', 2 алюминия', 'al3': ', 3 алюминия', 'cell0': '', 'cell1': ', 1 фотоэлемент',
               'cell2': ', 2 фотоэлемента', 'cell3': ', 3 фотоэлемента'}
        m = randint(1, 3)
        al = randint(0, 3)
        cell = randint(0, 3)
        print('\nСовершив удачную посадку, на планете вы сумели найти ', res['m' + str(m)], res['al' + str(al)],
              res['cell' + str(cell)], '.\n', sep='')
        stats['алюминий'] += al
        stats['фотоэлемент'] += cell
        stats['металл'] += m
    return stats


def planet(stats):
    """
        Reflects the impact of a random event
        :param stats: current state of the system
        :return: new state of the system
        """
    object = {0: 'обнаружена планета ', 1: 'обнаружена карликовая планета ',
              2: 'обнаружен спутник '+str(name())+' планеты '}
    sc = randint(0, 2)
    planet_name = name()
    print('\nВ этой системе ', object[sc], planet_name, ', ', sep='', end='')
    if sc == 2:
        print('на котором могут быть найдены ценные ресурсы.\n')
    else:
        print('на которой могут быть найдены ценные ресурсы.\n')
    im_stats = stats.copy()
    im_stats['ходы'] -= 1
    statistics(im_stats)
    return planet_dial(stats)


def planet_dial(stats):
    """
    Gives the player the choice of action
    :param stats: current state of system elements
    :return: new state of system elements
    """
    r = input('''Выберите действие, либо введите любой другой символ для выхода:
1. Отправить зонд
2. Высадиться на планету (не безопасно)
''')
    if r == '1':
        return prode(stats)
    elif r == '2':
        return landing(stats)
    return stats


def pirate(stats):
    """
        Reflects the impact of a random event
        :param stats: current state of the system
        :return: new state of the system
        """
    print('\nНа вас напали космические пираты. ', end='')
    al = randint(0, 2)
    met = randint(2, 3)
    pht = randint(0, 1)
    grab = {'al0': '', 'al1': '1 алюминий', 'al2': '2 алюминия', 'met2': '2 металла', 'met3': '3 металла', 'pht0': '',
            'pht1': '1 фотоэлемент'}
    if (stats['алюминий'] - al >= 0 and al > 0) or (stats['металл'] - met >= 0 and met > 0) or \
            (stats['фотоэлемент'] - pht >= 0 and pht > 0):
        print('После нападения у вас украли:')
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
        print('У вас нечего грабить. Пираты сжалились над вами и отдали вам',met,'металл и ', al,'алюминий.')
        stats['металл'] += met
        stats['алюминий'] += al
    print('')
    return stats


def exchange(stats):
    """
    Reflects the impact of a changing operation
    :param stats: current state of the system
    :return: new state of the system
    """
    print('На планете', name(), 'вы встретили торговца. Для начала обмена введите "1", либо любой другой символ для '
                                'выхода.')
    r = randint(1, 2)
    choice = {1: 'Обмен: 1 алюминий за 2 металла', 2: 'Обмен: 1 металл за 1 алюминий'}
    invent = {1: 'алюминия', 2: 'металла'}
    a = input()
    if a == '1':
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
                    return stats
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
                    return stats
                else:
                    print('Недостаточно средств. Попробуйте еще раз.')
                    return exchange(stats)
        elif b == 2:
            return stats
        else:
            print('Неверно введено значение. Попробуйте заново.')
            return exchange(stats)
    else:
        return stats


def engine(stats):
    """
    Brakes the engine
    :param stats: current state of the system
    :return: new state of the system
    """
    if stats['двигатель'] == 1:
        scripts = {1: 'Сломалась система охлаждения двигателя.', 2: 'Превышение нормы давления в двигателе.',
                   3: 'Корабль попал в магнитную бурю.', 4: 'Высокие нагрузки вывели двигатель из строя.'}
        print(scripts[randint(1, 4)], 'Двигательный отсек в критическом состоянии.')
        stats['двигатель'] = 0
        return stats
    print('Критическое состояние двигателя привело к его полному отказу. На перезапуск потрачен дополнительный ход.')
    stats['ходы'] -= 1
    return stats


main()
