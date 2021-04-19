"""Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции"""


def euqal_koef(a, b, *args):
    koef = 0
    for i in range(len(args)):
        koef += args[i]
    print(a * b + koef)


def print_str(str_arg):
    print(str_arg)


def running():
    print_str("START")
    euqal_koef(2, 4, 1, 3)
    euqal_koef(3, 5)
    print("END")


def running_onefunc(func):
    print("One Func")
    func()
    print("notEND")


def running_many(*funcs):
    count_atr = 0
    for func in funcs:
        print("running func {}".format(count_atr))
        func()
        count_atr += 1


running_onefunc(running)
running_many(running, running)
