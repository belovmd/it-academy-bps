def runner(func_deco):
    def wa_original_function(*args):
        print("SpaceShip")
        func_deco(*args)
        print("moon")
    return wa_original_function


def print_str(str):
    print(str)


runn_all = runner(print_str)
runn_all("Demons")
