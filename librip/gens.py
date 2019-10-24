import random


def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for dict in items:
            if args[0] in dict.keys() and not dict[args[0]] is None:
                yield dict[args[0]]
    else:
        for dict in items:
            elem = {}
            for arg in args:
                if arg in dict.keys() and not dict[arg] is None:
                    elem[arg] = dict[arg]
            if len(elem) != 0:
                yield elem


def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield random.randint(begin, end)
