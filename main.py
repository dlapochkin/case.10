import random

'''
def main(stats):
    score = 1
    param = {'Казна': 100, 'Зерно': 1000, 'Земля': 10, 'Военные силы': 2,
             'Население': 50, 'Смута': 0, 'Коэффициент урожайности': 0.1}
    events = {}
    param['Земля'] = 20
def menu():
    menu = {'Обмен валюты':'exchange()','Купить военную силу':'def ','Объявить войну':'start_war()'}
#функция меняет деньги на зерно и обратно
def exchange(stats):
    print('Хотите обменять валюту?','1 - да, 2 - нет')
    a = int(input())
    if a == 1:
        #цена десятка зерна в денежных единицах (покупка зерна)
        value_seed = random.randint(10,15)
        #цена одной денежной единицы в зернах (продажа зерна)
        value_sale = random.randint(5,10)
        print('-' * 178)
        print(stats)
        print('Купить десяток зерна - ', value_seed,'ден ед.','Нажмите 1')
        print('Продать десяток зерна - ', value_sale,'ден ед.','Нажмите 2')
        b = int(input())
        if b == 1:
            cb = int(input('Выберите количество '))
            if cb * value_seed < stats['Казна']:
                #сколько уйдет ден ед
                db = cb * value_seed
                stats['Казна'] -= db
                #сколько прибавиться зерна
                stats['Зерно'] += cb * 10
                return stats
            else:
                print('Недостаточно средств. Введите заново')
                exchange(stats)
        if b == 2:
            cs = int(input('Выберите количество зерна (в десятках)'))
            if cs * 10 < stats['Зерно']:
                #сколько придет ден ед
                ds = cs * value_sale
                stats['Казна'] -= ds
                # сколько убавиться зерна
                stats['Зерно'] += cs * 10
                return stats
            else:
                print('Недостаточно зерна. Введите заново')
                exchange(stats)
        else:
            print('Неверно введено значение. Введите заново')
            exchange()
    elif a == 2:
        return
    else:
        print('Неверно введено значение. Введите заново')
        exchange(stats)


stats = {'Казна': 100, 'Зерно': 1000, 'Земля': 10, 'Военные силы': 2,
             'Население': 50, 'Смута': 0, 'Коэффициент урожайности': 0.1}
print(stats)

'''




#Черновик
'''
param = {'Казна': 100, 'Зерно': 1000, 'Земля': 10, 'Военные силы': 2,
             'Население': 50, 'Смута': 0, 'Коэффициент урожайности': 0.1}
#цена десятка зерна в денежных единицах (покупка зерна)
value_seed = random.randint(10,15)
#цена одной денежной единицы в зернах (продажа зерна)
value_sale = random.randint(5,10)
print('-' * 300)
print('Купить десяток зерна - ', value_seed, ' ден ед')
print('Продать десяток зерна - ', value_sale,' ден ед')
c = input('Выберите количество ')
#сколько уйдет ден ед
d = int(c) * value_sale
param['Казна'] -= d
print(param)'''


stats = stats = {'ходы': 0, 'металл': 3, 'алюминий': 4, 'фотоэлемент': 0, 'зонд': 0, 'жизнеобеспечение': 0, 'двигатель': 0, 'связь': 0, 'навигация': 0, 'ремонт': 0, 'броня': 0}
def repair(stats):
    print('Стоимость ремонта систем корабля:')
    print('1. Жизнеобеспечение: 2 алюминия\n2. Двигатель: 2 металла\n3. Связь: 2 алюминия\n4. Навигация: 3 металла\n5. Ремонт: 1 металл\n6. Броня: 2 металла')
    print('Стоимость сборки одного зонда:\n1 алюминий')
    print('-'*176)
    print('Выберите одно из действий:\n1. Починить систему корабля \n2. Собрать зонд\n3. Выход')
    print('-' * 176)
    a = int(input('Введите цифру:\n'))
    if a == 3:
        #выход из функции
        return stats
    elif a == 2:
        #покупка зонда
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
        price = ['алюминий','металл','алюминий','металл','металл']
        print('Стоимость ремонта систем корабля:')
        print('1. Жизнеобеспечение: 2 алюминия\n2. Двигатель: 2 металла\n3. Связь: 2 алюминия\n4. Навигация: 3 металла\n5. Ремонт: 1 металл\n6. Броня: 2 металла')
        n = int(input('Выберите номер элемента:\n'))
        # Цена - константа
        if stats.get(ship[n-1]) == 0:
            if stats.get(price[n-1]) > 1:
                stats[price[n-1]] -= 2
                stats[ship[n-1]] = 1
            else:
                print('Недостаточно средств. Попробуйте еще раз.')
                q = input('Введите любой символ для продолжения:\n')
                return repair(stats)
        else:
            print('Эта часть корабля уже отремонтирована.')
            q = input('Введите любой символ для продолжения:\n')
            repair(stats)
        '''
        if n == 1:
            #Цена - константа
            if stats.get('жизнеобеспечение') == 0:
                if stats.get('алюминий') > 1:
                    stats['алюминий'] -= 2
                    stats['жизнеобеспечение'] = 1
                else:
                    print('Недостаточно средств. Попробуйте еще раз.')
                    q = input('Введите любой символ для продолжения:\n')
                    return repair(stats)
            else:
                print('Эта часть корабля уже отремонтирована.')
                q = input('Введите любой символ для продолжения:\n')
                repair(stats)

        elif n == 2:
            #Цена - константа
            if stats.get('двигатель') == 0:
                if stats.get('металл') > 1:
                    stats['металл'] -= 2
                    stats['двигатель'] = 1
                else:
                    print('Недостаточно средств. Попробуйте еще раз.')
                    q = input('Введите любой символ для продолжения:\n')
                    return repair(stats)
            else:
                print('Эта часть корабля уже отремонтирована.')
                q = input('Введите любой символ для продолжения:\n')
                repair(stats)

        elif n == 3:
            #Цена - константа
            if stats.get('связь') == 0:
                if stats.get('алюминий') > 1:
                    stats['алюминий'] -= 2
                    stats['связь'] = 1
                else:
                    print('Недостаточно средств. Попробуйте еще раз.')
                    q = input('Введите любой символ для продолжения:\n')
                    return repair(stats)
            else:
                print('Эта часть корабля уже отремонтирована.')
                q = input('Введите любой символ для продолжения:\n')
                repair(stats)

        elif n == 4:
            #Цена - константа
            if stats.get('навигация') == 0:
                if stats.get('металл') > 2:
                    stats['металл'] -= 3
                    stats['навигация'] = 1
                else:
                    print('Недостаточно средств. Попробуйте еще раз.')
                    q = input('Введите любой символ для продолжения:\n')
                    return repair(stats)
            else:
                print('Эта часть корабля уже отремонтирована.')
                q = input('Введите любой символ для продолжения:\n')
                repair(stats)

        elif n == 5:
            #Цена - константа
            if stats.get('ремонт') == 0:
                if stats.get('металл') > 0:
                    stats['металл'] -= 1
                    stats['ремонт'] = 1
                else:
                    print('Недостаточно средств. Попробуйте еще раз.')
                    q = input('Введите любой символ для продолжения:\n')
                    return repair(stats)
            else:
                print('Эта часть корабля уже отремонтирована.')
                q = input('Введите любой символ для продолжения:\n')
                repair(stats)

        elif n == 6:
            #Цена - константа
            if stats.get('броня') == 0:
                if stats.get('металл') > 1:
                    stats['металл'] -= 2
                    stats['броня'] = 1
                else:
                    print('Недостаточно средств. Попробуйте еще раз.')
                    q = input('Введите любой символ для продолжения:\n')
                    return repair(stats)
            else:
                print('Эта часть корабля уже отремонтирована.')
                q = input('Введите любой символ для продолжения:\n')
                repair(stats)'''

    return stats
repair(stats)






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












