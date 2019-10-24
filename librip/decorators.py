# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно


def print_result(func):
    def wrap(*args):
        print(func.__name__)
        return_value = func(*args)
        if isinstance(return_value, list):
            print('\n'.join(str(value) for value in return_value))
        elif isinstance(return_value, dict):
            print('\n'.join((str(key) + ' = ' + str(return_value[key])) for key in return_value.keys()))
        else:
            print(return_value)
        return return_value
    return wrap
