from random import *
import string


def main():
    stats = {'ходы': 20, 'металл': 1, 'алюминий': 1, 'фотоэлемент': 0, 'зонд': 5, 'жизнеобеспечение': 0, 'двигатель': 0,
             'связь': 0, 'навигация': 0, 'ремонт': 0, 'корпус': 0}
    stats_dop = {'жизнеобеспечение': 0, 'двигатель': 0, 'связь': 0, 'навигация': 0, 'ремонт': 0, 'корпус': 0}
    # правила
    # тут предисловие
    # совет: первым делом жизнеобеспечение
    stability_1 = choice(list(stats_dop.keys()))
    stats_dop.pop(stability_1)
    stability_2 = choice(list(stats_dop.keys()))
    stats[stability_1] = 1
    stats[stability_2] = 1
    print(stability_1,stability_2)
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
'''stats = {'ходы': 20, 'металл': 1, 'алюминий': 1, 'фотоэлемент': 0, 'зонд': 5, 'жизнеобеспечение': 0, 'двигатель': 0,
             'связь': 0, 'навигация': 0, 'ремонт': 0, 'корпус': 0}
statistics(stats)'''
def turn(stats):
    events = {0: planet,
              1: planet,
              2: meteorite_collision,
              3: space_debris,
              4: electromagnetic_radiation,
              5: water,
              6: cellular_system,
              7: help,
              8: cellular_system,
              9: pirate,
              10: exchange,
              11: cold_freeze}
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
    print('-'*176)
    print('Выберите одно из действий:\n1. Починить систему корабля \n2. Собрать зонд\n3. Выход')
    print('-' * 176)
    a = int(input('Введите цифру:\n'))
    if a == 3:
        #выход из функции
        return stats
    elif a == 2:
        #покупка зонда
        print('Стоимость сборки одного зонда:\nЗонд - 1 алюминий')
        allow = stats.get('алюминий')
        #цена 1 алюминий
        print('Выберите количество зондов (Доступно:',allow,')')
        n = int(input())
        if n > allow:
            print('Недостаточно средств. Попробуйте еще раз.')
            q = input('Введите любой символ для продолжения:\n')
            return repair(stats)
        elif n <= allow:
            stats['алюминий'] -= n
            stats['зонд'] += n
            #def statistics
            print(stats)
            q = input('Введите любой символ для продолжения:\n')
        else:
            print('Неверно введено значение. Попробуйте еще раз.')
        return repair(stats)
    #ремонт корабля
    elif a == 1:
        #функция работает,не работает
        ship = ['жизнеобеспечение','двигатель','связь','навигация','ремонт','корпус']
        #price = ['алюминий','металл','алюминий','металл','металл']
        #словарь (система корабля : алюминий, металл, фотоэлемент)
        price = {'жизнеобеспечение':[1,1,0], 'двигатель':[3,3,0], 'связь':[2,0,0], 'навигация':[2,2,1], 'ремонт':[3,4,0], 'корпус':[0,5,0] }
        print('У вас есть : алюминий -',stats['алюминий'],'шт. металл -',stats['металл'],'шт. фотоэлемент -',stats['фотоэлемент'],'шт.')
        print('Стоимость ремонта систем корабля:')
        print('1. Жизнеобеспечение: 1 алюминий, 1 металл\n2. Двигатель: 3 алюминия, 3 металла\n3. Связь: 2 алюминия\n4. Навигация: 2 алюминия, 2 металла, 1 фотоэлемент\n5. Ремонт: 3 алюминия, 4 металла\n6. Корпус: 5 металла\n7. Выход')
        n = int(input('Выберите номер элемента:\n'))
        # Цена - константа
        if n == 7:
            return repair(stats)
        if stats.get(ship[n-1]) == 0:
            #алюминий
            if price.get(ship[n-1])[0] <= stats['алюминий'] and price.get(ship[n-1])[1] <= stats['металл'] and price.get(ship[n-1])[2] <= stats['фотоэлемент']:
                stats['алюминий'] -= price.get(ship[n-1])[0]
                stats['металл'] -= price.get(ship[n-1])[1]
                stats['фотоэлемент'] -= price.get(ship[n-1])[2]
                stats[ship[n-1]] = 1
                print('Вы починили -',ship[n-1])
                return repair(stats)
            else:
                print('Недостаточно средств. Попробуйте еще раз.')
                q = input('Введите любой символ для продолжения:\n')
                return repair(stats)
        else:
            print('Эта часть корабля уже отремонтирована.')
            q = input('Введите любой символ для продолжения:\n')
            repair(stats)
    return stats


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
              2: 'Одна из планет системы на '+str(randint(20, 70))+'% состоит изо льда. Растопив его, вы '
                                                                               'вполне можете применить его в пищу или '
                                                                               'для получения кислорода.'}
    print(script[randint(0, 2)], 'Количество ходов увеличено на два.')
    stats['ходы'] += 2
    return stats


def cellular_system(stats):
    print('Помехи, создаваемые сломанной системой связи, привлекли лишнее внимание.', end='')
    return pirate(stats)


def help(stats):
    resources = {'cell1': 'Получен 1 фотоэлемент', 'cell2': 'Получено 2 фотоэлемента', 'al0': '',
                 'al1': ', 1 алюминий', 'm0': '', 'm1': ', 1 металл', 'm2': ', 2 металла'}
    cell, al, m = randint(1, 2), randint(0, 1), randint(0, 2)
    print('На одной из планет системы вы встретили дружелюбное население, расположенное к контакту и готовое оказазать '
          'вам помощь. ', resources['cell' + str(cell)], resources['al'+str(al)], resources['m'+str(m)], '.\n',
          'Полученная провизия увеличивает ваши запасы и дает 2 дополнительных хода.', sep='')
    stats['металл'] += m
    stats['алюминий'] += al
    stats['фотоэлемент'] += cell
    stats['ходы'] += 2
    return stats


def prode(stats):
    '''
    функция- запуск зонда
    :param stats:
    :return:
    '''
    if stats['зонд'] > 0:
        stats['зонд'] -= 1
        t=randint(0,1)
        print('fsfgfdhhsdfshfd')
        if t==1:
            stats['алюминий'] += randint(0, 3)
            stats['фотоэлемент'] += randint(0, 3)
            stats['металл'] += randint(1, 3)
        else:
            t=int(input('''Произошла неудача, зонд потерян. Вы можете:
            1.Отправить ещё один.
            2.Перейти к следующему ходу'''))
            if t==1:
                prode(stats)
    else:
        print('У вас недостаточно зондов')
    return stats


def name():
    '''
     генерирует рандомное имя
    :return:
    '''
    letters = string.ascii_lowercase
    rand_string = ''.join(sample(letters, 3))
    return 'NSU'+rand_string


def landing(stats):
    '''
    приземление
    :param stats:
    :return:
    '''
    if stats['двигатель']==0:
        print('Отсек двигатель неисправен')
    else:
        t=randint(0,2)
        if stats['навигация']==0:
            if stats['корпус']==0:
                stats['двигатель']=0
            else:
                stats['корпус']=0

        if t==0:
            print('На планете пусто')
        else:
            stats['алюминий'] += randint(0, 3)
            stats['фотоэлемент'] += randint(0, 3)
            stats['металл'] += randint(1, 3)
    return stats


def planet(stats):
    '''
    выбор что сделать с планетой
    :param stats:
    :return:
    '''
    planet_name=name()
    print('В этой системе найден объект',planet_name)
    r=int(input('''Вы можете:
     1.Отправить зонт
     2.Высадиться на планету самостоятельно 
     3.Перейти к следующему ходу'''))
    if r==1:
        prode(stats)
    elif r==2:
        landing(stats)
    else:
        dial(stats)
    return stats


def pirate(stats):
    al = randint(0,2)
    met = randint(2,3)
    pht = randint(0,1)
    grab = {'al0':'','al1':' 1 алюминий','al2':'2 алюминия','met2': '2 металла','met3': '3 металла', 'pht0': '', 'pht1': '1 фотоэлемент'}
    if (stats['алюминий'] - al >= 0 and al > 0) or (stats['металл'] - met >= 0 and met > 0) or (stats['фотоэлемент'] - pht >= 0 and pht > 0):
        print('На вас напали космические пираты. После нападения у вас украли:')
        if stats['алюминий'] - al >= 0 and al > 0:
            stats['алюминий'] -= al
            print('-',grab['al' + str(al)],end='')
        elif stats['металл'] - met >= 0 and met > 0:
            stats['металл'] -= met
            print('-',grab['met' + str(met)],end='')
        elif stats['фотоэлемент'] - pht >= 0 and pht > 0:
            stats['фотоэлемент'] -= pht
            print('-',grab['pht' + str(pht)],end = '\n')
    else:
        print('У вас нет ресурсов и пираты подарили вам 1 металл и 1 алюминия')
        stats['металл'] += met
        stats['алюминий'] += al
    return stats


def exchange(stats):
    print('Вы встретили торговца.Хотите с ним обменяться ресурсами?\n1. Да.\n2. Нет и выйти.')
    r = randint(1,2)
    #0 - алюминий за металл, 1 - металл за алюминий
    choice = {1: 'Обмен: 1 алюминий за 2 металла', 2:'Обмен: 1 металл за 1 алюминий'}
    invent = {1:'алюминия',2:'металла'}
    a = int(input('Введите значение:\n'))
    if a == 1:
        print(choice[r],'Хотите обменяться?','1. Обменяться.\n2. Нет и выйти.',sep='\n')
        b = int(input('Введите значение:\n'))
        if b == 1:
            if r == 1:
                allow = stats['металл'] // 2
                print('Введите количество алюминия. Доступно:',allow)
                n = int(input())
                if n <= allow:
                    stats['металл'] -= 2 * n
                    stats['алюминий'] += n
                    print('Инвентарь: алюминий',stats['алюминий'],'металл',stats['металл'])
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


def cold_freeze(stats):
    #в итоге всегда ломается двигатель
    if stats['двигатель'] == 1:
        dict = {1:'Сломалась система охлождения двигателя',2:'Превышение нормы давления в двигателе',3:'Корабль попал в магнитную бурю',4:'Высокие нагрузки на двигатель'}
        r = randint(1,4)
        print(dict[r], '- работа двигателя в критичском состоянии.')
        stats['двигатель'] = 0
        return stats
    else:
        return stats

main()

#кр 180521

import json
#example
'''
r = {'is_claimed': 3, 'rating': 3.5}
r = json.dumps(r)
loaded_r = json.loads(r)
loaded_r['rating'] #Output 3.5
type(r) #Output str
type(loaded_r) #Output dict

#1
#{"dog":1,"cat":2}

r = json.loads(input())
wrd = input()
print(r[wrd])

#2

r = json.loads(input())
#r = ([{"key1":[0,4,1],"key2":[3,-8,14,5]},{"key1":[1,7],"key2":[9,-13]},{"key2":[1,-1,1],"key3":[3]}])
dict = {}

for i in range(0,len(r)):
    for key, value in r[i].items():
        if key in dict:
            dict[key] += int(sum(value))
        else:
            dict[key] = int(sum(value))
print(json.dumps(dict))



# конвертируем в JSON:
# в результате получаем строк JSON:

#3
r = {"response":{"count":10,"items":[{"id":12,"user name":"Ivan","bdate":"12.3.1984"},{"id":64,"user name":"Petrov","bdate":"25.9.1980"},{"id":39,"user name":"Yakovleva","bdate":"14.6.1984"},{"id":88,"user name":"Svetlova","bdate":"19.1.1980"},{"id":103,"user name":"Mironov","bdate":"15.12.1980"},{"id":503,"user name":"Voronova"},{"id":9,"user name":"Sidorov","bdate":"3.5"},{"id":395,"user name":"Danilova","bdate":"6.2.1978"},{"id":1002,"user name":"Kuznetsov","bdate":"8.10.1978"},{"id":932,"user name":"Denisova","bdate":"28.11"}]}}
dict = {}
r = json.loads(input())
a = r["response"]['items']
#кортеж
for i in range(0,len(a)):
    for key, value in a[i].items():

        #day,month,year = value.split('.')
        #print(day)
        if key == 'bdate':
            day = value[:value.find('.')]
            month = value[value.find('.')+1:value.rfind('.')]
            year = value[value.rfind('.')+1:]
            #if value.count('.') == 2:
            if day != '' and month != '' and len(year) == 4:
                key1 = 2018 - int(value[-4:])
                if key1 in dict:
                    dict[key1] += 1
                else:
                    dict[key1] = 1

s = []
for k in dict:
    a = (k,dict[k])
    s.append(a)
print(sorted(s, key=lambda point: (-point[1],point[0])))
print(new_s)
coord = [(3, 11, 14), (3, 9, 18), (3, 10, 10), (3, 11, 12), (3, 11, 10), (3, 10, 12), (3, 9, 14)]
print(sorted(coord, key=lambda point: (point[1], -point[2])))
'''

