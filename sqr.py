from math import sqrt, cos, acos
from sys import exit
from traceback import format_exc
from datetime import datetime

def error(text, file):
    request = input('{}\nХотите сохранить запись об ошибке в логе? (y/n): '.format(text))
    if request.lower() == 'y':
        with open(file, 'a') as log:
            log.write('\n[{}] Программа была внезапно завершена из-за непредвиденной ошибки!\n{}'.format(
                datetime.now(), format_exc()))
        log.close()
    elif request.lower() == 'n':
        exit(0)

try:
    main = int(input('1 - квадратное\n2 - кубическое\n3 - линейное\nВыберите число: '))
    if main == 1:
        a, b, c = map(int, input('ax^2+bx+c=0\nВведите коэффициенты квадратного уравнения: ').split())
        if 0 in [a, b, c]:
            input(
                'Ошибка! Коэффициент не может быть равен нулю. Вы ввели: {}, {}, {}.'
                '\nДля завершения работы программы нажмите enter...'.format(
                    a, b, c))
        else:
            equation = '{}x^2{}x{}=0'.format(a, '%+d' % b, '%+d' % c)
            d = (b ** 2) - (4 * a * c)
            if d < 0:
                input('Квадратное уравнение {} не имеет действительных корней..'.format(equation))
            elif d == 0:
                x1 = -b / (2 * a)
                input(
                    'Квадратное уравнение {} имеет только один корень: {:.5f}. При этом дискриминант равен {}.'.format(
                        equation, x1, d))
            else:
                x2 = (-b + sqrt(d)) / (2 * a)
                x3 = (-b - sqrt(d)) / (2 * a)
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
                                                                                                        sqrt(d),
                                                                                                        a, x2,
                                                                                                        '%+d' % -b,
                                                                                                        sqrt(d), a, x3))
                    print('Данные о решении записаны в лог-файле в папке программы!')
                with open('log.txt', 'a') as log:
                    log.write(f'\nРешено квадратное уравнение: {equation}\nD: {d}, X: {x2}, {x3}')
                log.close()
                input('Для завершения работы программы нажмите клавишу enter...')
            if continuation == 2:
                print('')
    elif main == 2:
        a1, b1, c1, d1 = map(int, input('ax^3+bx^2+cx+d=0\nВведите коэффициенты кубического уравнения: ').split())
        if 0 in [a1, b1, c1, d1]:
            input(
                'Ошибка! Коэффициент не может быть равен нулю. Вы ввели: {}, {}, {}, {}.'
                '\nДля завершения работы программы нажмите enter...'.format(
                    a1, b1, c1, d1))
        equation1 = '{}x^3+{}x^2+{}x+{}=0'.format(a1, '%+d' % b1, '%+d' % c1, d1)
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
            print('Данные о решении записаны в лог-файле в папке программы!')
            input('Для завершения работы программы нажмите клавишу enter...')
            with open('log.txt', 'a') as log:
                log.write(
                    '\nРешено кубическое уравнение: {}\nQ: {}, R: {}, Delta: {}, X: {}'.format(equation1, q, r, delta,
                                                                                               x4))
            log.close()
    elif main == 3:
        input('Не готово')
except TypeError:
    request = input('Во время работы программы произошла ошибка!\nХотите сохранить запись об ошибке в логе? (y/n): ')
    if request.lower() == 'y':
        with open('log.txt', 'a') as log:
            log.write('\n[{}] Программа была внезапно завершена из-за непредвиденной ошибки!\n{}'.format(
                datetime.now(), format_exc()))
        log.close()
    elif request.lower() == 'n':
        exit(0)
except SyntaxError:

except ZeroDivisionError:
    error('Кажется, ', 'log.txt')
except ValueError:
    request = input('Во время работы программы произошла ошибка!\nХотите сохранить запись об ошибке в логе? (y/n): ')
    if request.lower() == 'y':
        with open('log.txt', 'a') as log:
            log.write(
                '\n[{}] Программа была внезапно завершена из-за непредвиденной ошибки!\n{}'.format(
                    datetime.now(), format_exc()))
        log.close()
    elif request.lower() == 'n':
        exit(0)
# Created by Ben_Puls
