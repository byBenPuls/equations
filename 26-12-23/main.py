from math import sqrt, cos, acos
from sys import exit
from traceback import format_exc
from datetime import datetime
from prettytable import PrettyTable

log_file = 'log.log'


def closing():
    input('\nДля завершения работы программы нажмите enter...')


def error(file):
    request = input('Произошла ошибка во время работы программы!\nХотите сохранить запись об ошибке в логе? (y/n): ')
    if request.lower() == 'y':
        with open(file, 'a') as logger:
            logger.write('{}: Программа была внезапно завершена из-за непредвиденной ошибки!\n{}\n'.format(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'), format_exc()))
        logger.close()
    elif request.lower() == 'n':
        exit(0)


def quadr_equations(first, k1, k2, k3, discr, unk1, unk2, file):
    print('Данные о решении записаны в лог-файле в папке программы!')
    with open(file, 'a') as logger:
        logger.write('{}: Решено квадратное уравнение вида: {}\nCoefficients: {}, {}, {}; D: {}; X: {}, {}.\n'.format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'), first, k1, k2, k3, discr, unk1, unk2))
    logger.close()
    closing()


def cub_equations(first, k1, k2, k3, k4, e1, e2, e3, unk3, file):
    print('Данные о решении записаны в лог-файле в папке программы!')
    with open(file, 'a') as logger:
        logger.write(
            f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Решено кубическое уравнение вида: {first}'
            f'\nCoefficients: {k1}, {k2}, {k3}, {k4}; Q: {e1}; R: {e2}; Delta: {e3}; X: {unk3}.\n')
    logger.close()
    closing()


def discriminant(k1, k2, k3):
    disc = (k2 ** 2) - (4 * k1 * k3)
    return disc


def unknown1(k1, k2):
    res = -k2 / (2 * k1)
    return res


def unknown2(k1, k2, discr):
    res1 = (-k2 + sqrt(discr)) / (2 * k1)
    res2 = (-k2 - sqrt(discr)) / (2 * k1)
    return [res1, res2]


try:
    main_table = PrettyTable()
    main_table.field_names = ['Номер', 'Название']
    main_table.add_row([1, 'Квадратное уравнение'])
    main_table.add_row([2, 'Кубическое уравнение'])
    main_table.add_row([3, 'Линейное уравнение'])
    main_table.add_row([4, 'Показательное уравнение'])
    print(main_table)
    main = int(input('\nВыберите число: '))
    if main == 1:
        a, b, c = map(int, input('ax^2+bx+c=0\nВведите коэффициенты квадратного уравнения: ').split())
        if 0 in [a, b, c]:
            print('Ошибка! Коэффициент не может быть равен нулю. Вы ввели: {}, {}, {}.'.format(a, b, c))
            closing()
        else:
            equation = '{}x^2{}x{}=0'.format(a, '%+d' % b, '%+d' % c)
            d = discriminant(a, b, c)
            if d < 0:
                print(f'Квадратное уравнение {equation} не имеет действительных корней')
                closing()
            elif d == 0:
                x1 = unknown1(a, b)
                input(
                    'Квадратное уравнение {} имеет только один корень: {:.5f}. При этом дискриминант равен {}.'.format(
                        equation, x1, d))
                quadr_equations(equation, a, b, c, d, x1, '', log_file)
            else:
                x2 = unknown2(a, b, d)[0]
                x3 = unknown2(a, b, d)[1]
                print('Квадратное уравнение {} имеет два корня: {:.5f}, {:.5f}. При этом дискриминант равен {}.'.format(
                    equation, x2, x3, d))
                continuation = int(input('1 - увидеть полное решение\n2 - закрыть программу\nВыберите число: '))
                if continuation == 1:
                    print('Решаем дискриминант: D=b^2-4*a*c\nD= {}^2-4*{}*{}'.format(b, a, c))
                    print(
                        'Дискриминант получился {}. Извлекаем квадратный корень из дискриминанта и получаем {}'.format(
                            d,
                            sqrt(
                                d)))
                    print('Считаем неизвестные по формулам:\nx1=-b+sqrt(D)/2*a\nx2= -b-sqrt(D)/2*a')
                    print(
                        'Подставляем значения и получаем: \nx1={}+{}/2*{}={}\nx2= {}-{}/2*{}={}'.format('%+d' % -b,
                                                                                                        sqrt(
                                                                                                            d),
                                                                                                        a, x2,
                                                                                                        '%+d' % -b,
                                                                                                        sqrt(
                                                                                                            d), a,
                                                                                                        x3))
                    quadr_equations(equation, a, b, c, d, x2, x3, log_file)
                if continuation == 2:
                    print('')
    elif main == 2:
        a1, b1, c1, d1 = map(int, input('ax^3+bx^2+cx+d=0\nВведите коэффициенты кубического уравнения: ').split())
        if 0 in [a1, b1, c1, d1]:
            input('Ошибка! Коэффициент не может быть равен нулю. Вы ввели: {}, {}, {}, {}.'.format(a1, b1, c1, d1))
            closing()
        equation1 = '{}x^3{}x^2{}x{}=0'.format(a1, '%+d' % b1, '%+d' % c1, '%+d' % d1)
        q = (3 * a1 * c1 - b1 ** 2) / (9 * a1 ** 2)
        r = (9 * a1 * b1 * c1 - 27 * a1 ** 2 * d1 - 2 * b1 ** 3) / (54 * a1 ** 3)
        delta = q ** 3 + r ** 2
        rho = sqrt((-q ** 3))
        theta = acos(r / rho)
        s_real = rho ** (1. / 3.) * cos(theta / 3)
        t_real = rho ** (1. / 3.) * cos(-theta / 3)
        x4 = s_real + t_real - b1 / (3 * a1)
        if a1 + b1 + c1 + d1 == 0:
            x5 = 1
            input('Один из корней уравнения равен 1')
        else:
            print(
                '\nРешено кубическое уравнение: {}\nQ: {}, R: {}, Delta: {}, X: {}'.format(equation1, q, r, delta, x4))
            cub_equations(equation1, a1, b1, c1, d1, q, r, delta, x4, log_file)
    elif main == 3:
        input('Не готово')

    elif main == 4:
        input('Не готово')
except (TypeError, ValueError, SyntaxError, ZeroDivisionError):
    error(log_file)
# Created by Ben_Puls+-
