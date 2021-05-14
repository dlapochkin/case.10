import string, random
from random import randint


def prode(stats):
    '''
    функция- запуск зонда
    :param stats:
    :return:
    '''
    if stats['зонд'] > 0:
        stats['зонд'] -= 1
        t=randint(0,1)
        print(t)
        if t==1:
            d['алюминий'] += randint(0, 3)
            d['фотоэлемент'] += randint(0, 3)
            d['металл'] += randint(1, 3)
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
    rand_string = ''.join(random.sample(letters, 3))
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
            if stats['броня']==0:

            else:
                stats['броня']==0

        if t==0:
            print('На планете пусто')
        else:

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

stats = {'ходы': 0, 'металл': 0, 'алюминий': 0, 'фотоэлемент': 0, 'зонд':5, 'жизнеобеспечение': 0, 'двигатель': 0, 'связь': 0, 'навигация': 0, 'ремонтный отсек': 0, 'броня': 0}

print(prode(stats))

