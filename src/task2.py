def runner(func_deco):
    count_run = 0

    def wrapper():
        print("SpaceShip")
        nonlocal count_run
        count_run += 1
        func_deco()
        print("moon")
        return count_run

    return wrapper


def print_str():
    print("some func")


runn_all = runner(print_str)
print(runn_all())
print(runn_all())
print(runn_all())
print(runn_all())
