import random


stats = {'ходы': 0, 'металл': 3, 'алюминий': 4, 'фотоэлемент': 0, 'зонд': 0, 'жизнеобеспечение': 0, 'двигатель': 0, 'связь': 0, 'навигация': 0, 'ремонт': 0, 'броня': 0}
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
        ship = ['жизнеобеспечение','двигатель','связь','навигация','ремонт','броня']
        #price = ['алюминий','металл','алюминий','металл','металл']
        #словарь (система корабля : алюминий, металл, фотоэлемент)
        price = {'жизнеобеспечение':[1,1,0], 'двигатель':[3,3,0], 'связь':[2,0,0], 'навигация':[2,2,1], 'ремонт':[3,4,0], 'броня':[0,5,0] }
        print('У вас есть : алюминий -',stats['алюминий'],'шт. металл -',stats['металл'],'шт. фотоэлемент -',stats['фотоэлемент'],'шт.')
        print('Стоимость ремонта систем корабля:')
        print('1. Жизнеобеспечение: 1 алюминий, 1 металл\n2. Двигатель: 3 алюминия, 3 металла\n3. Связь: 2 алюминия\n4. Навигация: 2 алюминия, 2 металла, 1 фотоэлемент\n5. Ремонт: 3 алюминия, 4 металла\n6. Броня: 5 металла\n7. Выход')
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

def pirate(stats):
    al = random.randint(0,2)
    met = random.randint(2,3)
    pht = random.randint(0,1)

    grab = {'al0':'','al1':' 1 алюминий','al2':'2 алюминия','met2': '2 металла','met3': '3 металла', 'pht0': '', 'pht1': '1 фотоэлемент'}
    print('На вас напали космические пираты.\nПосле нападения у вас украли:',grab['al'+ str(al)],grab['met'+ str(met)],grab['pht'+ str(pht)])
    stats['алюминий'] -= al
    stats['металл'] -= met
    stats['фотоэлемент'] -= pht
    return stats

def exchange(stats):
    print('Вы встретили торговца.Хотите с ним обменяться ресурсами?\n1. Да.\n2. Нет и выйти.')
    r = random.randint(1,2)
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



'''
n = int(input())
dict = {}
for i in range(0,n):
    a = list(input().split())
    key = a[0]
    v = a[1:]
    dict[key] = v
s = input()
print(dict)
if s in dict.values():
    print(1)
    for k, v in dict.items():
        if v == s:
            print(k)'''



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
'''
#1
#{"dog":1,"cat":2}
'''
r = json.loads(input())
wrd = input()
print(r[wrd])
'''

#2
'''
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
'''
#3

r = {"response":{"count":10,"items":[{"id":12,"user name":"Ivan","bdate":"12.3.1984"},
                                     {"id":64,"user name":"Petrov","bdate":"25.9.1980"},
                                     {"id":39,"user name":"Yakovleva","bdate":"14.6.1984"},
                                     {"id":88,"user name":"Svetlova","bdate":"19.1.1980"},
                                     {"id":103,"user name":"Mironov","bdate":"15.12.1980"},
                                     {"id":503,"user name":"Voronova"},
                                     {"id":9,"user name":"Sidorov","bdate":"3.5"},
                                     {"id":395,"user name":"Danilova","bdate":"6.2.1978"},
                                     {"id":1002,"user name":"Kuznetsov","bdate":"8.10.1978"},
                                     {"id":932,"user name":"Denisova","bdate":"28.11"},]}}
dict = {}
a = r["response"]['items']


#кортеж
for i in range(0,len(a)):
    for key, value in a[i].items():
        if key == 'bdate':
            if value.count('.') == 2:
                key1 = 2018 - int(value[-4:])
                if key1 in dict:
                    dict[key1] += 1
                else:
                    dict[key1] = 1
s = []
for k in dict:
    a = (k,dict[k])
    s.append(a)
s = sorted((s))
print(s)
print(s[0][1])

#for m in range(0,len(s)):




#кортеж



print(dict)
#print(tuple(sorted()))
#print(r["response"]['items'])






